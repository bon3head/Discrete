#!/usr/bin/env python3
"""Deterministic PreTeXt HTML -> Markdown converter (Phase 1 active scope)."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parents[2]
PHASE0 = ROOT / "planning/phase0"
ACTIVE = ROOT / "corpus/active"

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def load_data():
    classified=json.loads((PHASE0/'source_inventory_classified.json').read_text())['records']
    scopes={x['relative_path']:x['scope_class'] for x in json.loads((PHASE0/'scope_classification.json').read_text())['records']}
    gaps=defaultdict(list)
    for x in json.loads((PHASE0/'content_gap_report.json').read_text())['content_gaps']:
        for ref in x['references']: gaps[ref['relative_path']].append(x['asset_path'])
    return classified,scopes,gaps

from collections import defaultdict
CLASSIFIED, SCOPES, GAPS = load_data()
PATH_TO_OUTPUT={}

def slug(s): return re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',s.lower())).strip('-')
def chapter_dir(rec):
    m=re.search(r'(?:Chapter|Section)\s+(\d+)',rec.get('displayed_section_or_chapter') or '')
    if not m: m=re.search(r'/(\d+)-',rec['relative_path'])
    return f'ch{int(m.group(1)):02d}' if m else 'misc'
def output_rel(rec):
    scope=rec['scope_class']; root={'active_candidate':'active','deferred_candidate':'deferred','reference':'reference','reference_solution':'reference_solution'}[scope]
    p=Path(rec['relative_path']); stem=slug(p.stem.replace('ads ','',1))
    if rec['classification']=='chapter_landing': return f'{root}/{chapter_dir(rec)}/index.md'
    if rec['classification']=='frontmatter': return f'{root}/frontmatter/index.md'
    if rec['classification']=='index': return f'{root}/index.md'
    if rec['classification']=='backmatter': return f'{root}/backmatter.md'
    return f'{root}/{chapter_dir(rec)}/{stem}.md'
for rec in CLASSIFIED:
    PATH_TO_OUTPUT[rec['relative_path']]=output_rel({**rec,'scope_class':SCOPES.get(rec['relative_path'],rec.get('scope_class','unknown_scope'))})

def clean_soup(soup):
    root=soup.select_one('main.ptx-main > #ptx-content')
    if not root: raise ValueError('missing main.ptx-main > #ptx-content')
    for x in root.select('script,style,link,nav,header,footer,.sidebar,.toc,.search,.searchbox,.ptx-page-footer,.ptx-sidebar'):
        x.decompose()
    return root

class Renderer:
    def __init__(self, source_rel, gaps): self.source_rel=source_rel; self.gaps=set(gaps); self.unhandled=[]; self.seen_gap=set()
    def text(self,node):
        return ' '.join(node.get_text(' ',strip=True).split())
    def math_text(self,node): return node.get_text('',strip=False)
    def inline(self,node):
        if isinstance(node,NavigableString): return str(node)
        if not isinstance(node,Tag): return ''
        if 'process-math' in node.get('class',[]): return node.get_text('',strip=False)
        if node.name=='script' and (node.get('type') or '').startswith('math/tex'): return node.get_text('',strip=False)
        if node.name in {'em','i'}: return '*'+self.children(node)+'*'
        if node.name in {'strong','b'}: return '**'+self.children(node)+'**'
        if node.name=='code': return '`'+node.get_text('',strip=False)+'`'
        if node.name=='br': return '\n'
        if node.name=='a':
            label=self.children(node).strip(); href=node.get('href','')
            if href.lower().split('#')[0].endswith('.html'):
                target=href.split('#')[0]
                matches=[k for k in PATH_TO_OUTPUT if Path(k).name==Path(target).name]
                if matches: href=Path('../'+PATH_TO_OUTPUT[matches[0]]).as_posix()
                else: label += ' [UNRESOLVED_INTERNAL_LINK]'
            return f'[{label}]({href})'
        return self.children(node)
    def children(self,node): return ''.join(self.inline(c) for c in node.children)
    def figure(self,node):
        img=node.find('img'); src=(img.get('src') if img else '')
        src=src.split('?',1)[0].split('#',1)[0]
        alt=(img.get('alt') if img else '') or self.text(node)
        if src in self.gaps:
            self.seen_gap.add(src); return f'![MISSING FIGURE: {alt}](GAP:{src})'
        return f'![{alt}]({src})'
    def block(self,node,quote=False):
        if isinstance(node,NavigableString): return str(node).strip()
        if not isinstance(node,Tag): return ''
        if node.name in {'p','div'}: return self.children(node).strip()
        if node.name=='figure': return self.figure(node)
        if node.name=='pre' and 'sagecell-sage' in node.get('class',[]):
            script=node.find('script',attrs={'type':lambda x:x and x.startswith('text/x-sage')})
            return '```sage\n'+(script.get_text() if script else node.get_text()) .strip('\n')+'\n```'
        if node.name in {'ul','ol'}:
            lines=[]
            for i,li in enumerate(node.find_all('li',recursive=False),1): lines.append(f'{i}. {self.children(li).strip()}')
            return '\n'.join(lines)
        if node.name=='table':
            rows=[]
            for tr in node.find_all('tr',recursive=True): rows.append([self.text(c) for c in tr.find_all(['th','td'],recursive=False)])
            if rows and all(len(r)==len(rows[0]) for r in rows):
                out=['| '+' | '.join(rows[0])+' |','| '+' | '.join('---' for _ in rows[0])+' |']
                out += ['| '+' | '.join(r)+' |' for r in rows[1:]]; return '\n'.join(out)
            self.unhandled.append('table'); return '```UNHANDLED_SOURCE\n'+str(node)+'\n```'
        if node.name in {'h1','h2','h3','h4','h5','h6'}:
            level=min(6,int(node.name[1:])); return '#'*level+' '+self.text(node)
        if node.name=='img':
            src=node.get('src',''); return self.figure(node.parent) if node.parent else f'![{node.get("alt","")}]({src})'
        if node.name in {'script','style','link'}: return ''
        if node.name not in {'section','article','span','div','li','p','a','em','i','strong','b','code'}:
            self.unhandled.append(node.name); return '```UNHANDLED_SOURCE\n'+str(node)+'\n```'
        return self.children(node).strip()
    def article(self,node):
        h=node.find(['h1','h2','h3','h4','h5','h6'],recursive=False)
        typ=node.get('class',[])[0] if node.get('class') else 'source'
        typ={'definition':'Definition','example':'Example','exercise':'Exercise','theorem':'Theorem','proposition':'Proposition','lemma':'Lemma','corollary':'Corollary'}.get(typ,typ.title())
        cn=h.find(class_='codenumber').get_text(' ',strip=True).strip() if h and h.find(class_='codenumber') else ''
        title=h.find(class_='title').get_text(' ',strip=True).rstrip('.') if h and h.find(class_='title') else ''
        label=f'> **{typ} {cn}' + (f' — {title}.' if title else ' —') + '**'
        body=[]
        for child in node.find_all(['div','ul','ol','figure','pre'],recursive=False):
            if child.name=='div' and ('para' in child.get('class',[]) or child.get('class')==['logical']): body.append(self.block(child))
            elif child.name in {'ul','ol','figure','pre'}: body.append(self.block(child))
        if not body:
            body=[self.children(node).strip()]
        # Figures nested inside exercise/definition prose are not direct
        # children; retain their known gap placeholders instead of dropping
        # them during article rendering.
        for img in node.find_all('img'):
            src=(img.get('src') or '').split('?',1)[0].split('#',1)[0]
            if src in self.gaps and src not in self.seen_gap:
                self.seen_gap.add(src)
                body.append(f'![MISSING FIGURE: {(img.get("alt") or "source figure")}] (GAP:{src})'.replace('] (', ']('))
        return label+'\n\n'+'\n\n'.join('> '+x.replace('\n','\n> ') for x in body if x)
    def render(self,root):
        out=[]
        def visit(node):
            if node.name=='article' and any(x in node.get('class',[]) for x in ('definition','example','exercise','theorem','proposition','lemma','corollary')):
                out.append(self.article(node)); return
            if node.name=='section':
                h=node.find(['h1','h2','h3','h4','h5','h6'],recursive=False)
                if h and not ('hide-type' in h.get('class',[]) and 'exercises' in node.get('class',[])): out.append('# '+self.text(h))
                for child in node.find_all(recursive=False):
                    if child is not h: visit(child)
                return
            if node.name in {'h1','h2','h3','h4','h5','h6','p','div','figure','pre','ul','ol'}:
                z=self.block(node)
                if z: out.append(z)
        for child in root.find_all(recursive=False): visit(child)
        return '\n\n'.join(x for x in out if x.strip())+'\n'

def convert(source, output=None):
    source=Path(source); rel=source.relative_to(ROOT).as_posix()
    rec=next(x for x in CLASSIFIED if x['relative_path']==rel)
    scope=SCOPES.get(rel,rec.get('scope_class','unknown_scope')); gaps=GAPS.get(rel,[])
    soup=BeautifulSoup(source.read_text(encoding='utf-8',errors='replace'),'html.parser'); root=clean_soup(soup)
    renderer=Renderer(rel,gaps); body=renderer.render(root)
    title=rec.get('displayed_section_or_chapter') or soup.title.get_text(' ',strip=True)
    fm=['---',f'source_relative_path: "{rel}"',f'source_sha256: "{sha256(source)}"',f'scope_class: {scope}',f'displayed_section_or_chapter: "{title}"']
    if gaps:
        fm.append('content_gap: true'); fm.append('missing_assets:'); fm += [f'  - "{g}"' for g in sorted(set(gaps))]
    text='\n'.join(fm)+'\n---\n\n'+body
    if output: output=Path(output); output.parent.mkdir(parents=True,exist_ok=True); output.write_text(text,encoding='utf-8')
    return {'relative_path':rel,'output':str(output) if output else None,'unhandled':sorted(set(renderer.unhandled)),'gaps_found':sorted(renderer.seen_gap),'text':text}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('source',nargs='?'); ap.add_argument('--output-root'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--active',action='store_true'); args=ap.parse_args()
    if args.active:
        results=[]
        for rec in CLASSIFIED:
            if SCOPES.get(rec['relative_path'])!='active_candidate': continue
            r=convert(ROOT/rec['relative_path'],None if args.dry_run else Path(args.output_root or ACTIVE)/output_rel({**rec,'scope_class':'active_candidate'})); results.append({k:r[k] for k in ('relative_path','output','unhandled','gaps_found')})
        print(json.dumps({'count':len(results),'results':results},indent=2)); return
    if not args.source: ap.error('source required unless --active')
    r=convert(ROOT/args.source, None if args.dry_run else Path(args.output_root or ACTIVE)/output_rel(next(x for x in CLASSIFIED if x['relative_path']==args.source)))
    print(json.dumps({k:r[k] for k in ('relative_path','output','unhandled','gaps_found')},indent=2))
if __name__=='__main__': main()
