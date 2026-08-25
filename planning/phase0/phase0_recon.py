#!/usr/bin/env python3
"""Read-only Phase 0 inventory; writes reports only beside this script."""
from __future__ import annotations

import hashlib, json, os, re, subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
EXCLUDED_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "planning", "dist", "build", ".cache"}
SEMANTIC = ("definition", "theorem", "proposition", "lemma", "corollary", "example", "exercise")

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def files_under(root: Path):
    for here, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_DIRS)
        for name in sorted(names):
            p = Path(here) / name
            if p.is_file():
                yield p

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack=[]; self.title_parts=[]; self.in_title=False; self.headings=[]
        self.ptx_main=False; self.content=False; self.primary=None; self.ids=[]
        self.count=Counter(); self.assets=[]; self.links=[]; self.external=[]
        self.all_ids=[]; self.depth_content=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); classes=set(a.get("class", "").split()); ident=a.get("id")
        self.stack.append((tag,a))
        if "ptx-main" in classes: self.ptx_main=True
        if ident == "ptx-content":
            self.content=True; self.depth_content=len(self.stack)
            self.primary={"tag":tag,"id":ident,"classes":sorted(classes)}
        if ident: self.all_ids.append(ident)
        if self.content and ident and tag in {"section","article","div"}:
            self.ids.append(ident)
        if "process-math" in classes: self.count["process_math"] += 1
        typ=(a.get("type") or "").lower()
        if tag == "script" and typ.startswith("math/tex"): self.count["math_tex_script"] += 1
        for kind in SEMANTIC:
            if kind in classes or f"{kind}-like" in classes:
                self.count[kind] += 1
        if tag == "pre" and ("sagecell-sage" in classes or "sagecell" in a.get("class", "")):
            self.count["sage_cells"] += 1
        if tag == "table": self.count["tables"] += 1
        if tag == "figure": self.count["figures"] += 1
        if tag == "img":
            self.count["images"] += 1
            if a.get("src"): self.assets.append(a["src"])
        if tag in {"img","source","video","audio","object","link","script"} and a.get("src"):
            self.assets.append(a["src"])
        if tag == "a" and a.get("href"):
            href=a["href"]; parsed=urlparse(href)
            if parsed.scheme or parsed.netloc or href.startswith("//") or href.startswith("mailto:"):
                self.external.append(href)
            elif href.lower().split("#")[0].endswith(".html"):
                self.links.append(href)
        if tag in {"h1","h2","h3","h4"}: self.headings.append([tag, []])
        if tag == "title": self.in_title=True
    def handle_endtag(self, tag):
        if tag == "title": self.in_title=False
        if self.stack: self.stack.pop()
    def handle_data(self, data):
        if self.in_title: self.title_parts.append(data)
        if self.headings and self.stack and self.stack[-1][0] == self.headings[-1][0]: self.headings[-1][1].append(data)

def classify(path: Path, parsed: Inspect, title: str, primary_classes=()) -> str:
    posix=path.as_posix().lower(); hay=f"{posix} {title.lower()}"
    if "index.html" in posix: return "index"
    if "back_matter.html" in posix: return "backmatter"
    if "frontmatter" in primary_classes or "front" in hay: return "frontmatter"
    if "appendix" in hay or ("back_matter" in posix and "glossary" in hay): return "appendix_content"
    if not parsed.content: return "navigation_or_support" if any(x in hay for x in ("toc","nav","search")) else "unknown"
    if "chapter" in primary_classes: return "chapter_landing"
    if re.search(r"/(?:ads )?(?:set theory|combinatorics|logic|more on sets|intro|relations|functions|recursion|graph theory|more matrix algebra)\.html$", posix): return "chapter_landing"
    return "section_content"

def scope(path: str, title: str, category: str) -> str:
    h=(path+" "+title).lower()
    if "appendixf" in h or "hints_and_solutions" in h or "hints and solutions" in h: return "reference_solution"
    if category == "frontmatter": return "reference"
    if category == "navigation_or_support": return "support"
    # Chapter-directory identity takes priority over words such as “notation”
    # occurring in an ordinary numbered chapter section title.
    if re.search(r"/(?:9-graph_theory|12-more_matrix_algebra)/", h): return "deferred_candidate"
    if re.search(r"/(?:[1-8]-)", h): return "active_candidate"
    if any(x in h for x in ("appendixd", "notation", "glossary", "index", "back_matter", "appendixa", "appendixb", "appendixc")): return "reference"
    return "unknown_scope"

def pdf_pages(path: Path):
    try:
        result=subprocess.run(["pdfinfo", str(path)], text=True, capture_output=True, timeout=10)
        m=re.search(r"^Pages:\s+(\d+)", result.stdout, re.M)
        return int(m.group(1)) if m else None
    except Exception: return None

def write(name, data):
    (OUT/name).write_text(json.dumps(data, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

def main():
    inventory=[]; baseline={}; html=[]; extensions=Counter()
    for p in files_under(ROOT):
        rel=p.relative_to(ROOT).as_posix(); ext=p.suffix.lower(); sha=digest(p); extensions[ext or "[no extension]"] += 1
        record={"source_root":str(ROOT),"relative_path":rel,"kind":"file","extension":ext or "[no extension]","size_bytes":p.stat().st_size,"sha256":sha,"excluded_from_conversion":ext not in {".html",".htm"},"exclusion_reason":None if ext in {".html",".htm"} else "non-HTML source or project metadata; not eligible for Phase 1 HTML conversion"}
        if ext == ".pdf":
            record["pdf_validation_anchor"]={"detected_page_count":pdf_pages(p),"page_count_method":"pdfinfo"}
        inventory.append(record)
        if rel != "AGENTS.md": baseline[rel]=sha
        # The glossary lacks an extension but carries the same generated-PreTeXt
        # signature as the HTML corpus pages.  Select by parsed source form.
        is_pretext_page = ext in {".html", ".htm"} or b"Generated from PreTeXt source" in p.read_bytes()[:2048]
        if not is_pretext_page: continue
        try:
            raw=p.read_text(encoding="utf-8", errors="replace"); parser=Inspect(); parser.feed(raw); parser.close()
            soup=BeautifulSoup(raw, "html.parser")
            content=soup.select_one("main.ptx-main > #ptx-content")
            primary=content.find(recursive=False) if content else None
            primary_data=({"tag":primary.name,"id":primary.get("id"),"classes":sorted(primary.get("class",[]))} if primary else None)
            principal_ids=([x.get("id") for x in content.find_all("section") if x.get("id")] if content else [])
            display=(primary.find(["h1","h2","h3","h4","h5","h6"]).get_text(" ",strip=True) if primary and primary.find(["h1","h2","h3","h4","h5","h6"]) else None)
            title=" ".join("".join(parser.title_parts).split())
            cat=classify(p,parser,title, primary.get("class",[]) if primary else ())
            duplicate=sorted(k for k,v in Counter(parser.all_ids).items() if v>1)
            resolved=[]; unresolved=[]
            for asset in sorted(set(parser.assets)):
                clean=asset.split("#",1)[0].split("?",1)[0]
                if not clean or urlparse(clean).scheme or clean.startswith("//"): continue
                exists=(p.parent / clean).resolve().is_file()
                (resolved if exists else unresolved).append(asset)
            warnings=[]
            if not content: warnings.append("missing main.ptx-main > #ptx-content")
            if duplicate: warnings.append("duplicate IDs: "+", ".join(duplicate))
            if unresolved: warnings.append("unresolved local assets: "+", ".join(unresolved))
            html.append({"relative_path":rel,"sha256":sha,"classification":cat,"title":title or None,"has_main_ptx_main":bool(soup.select_one("main.ptx-main")),"has_main_ptx_main_gt_ptx_content":bool(content),"primary_semantic_root":primary_data,"displayed_section_or_chapter":display,"principal_section_ids":list(dict.fromkeys(principal_ids)),"counts":{"process_math":parser.count["process_math"],"math_tex_script":parser.count["math_tex_script"],"definitions":parser.count["definition"],"theorem_proposition_lemma_corollary":sum(parser.count[x] for x in ("theorem","proposition","lemma","corollary")),"examples":parser.count["example"],"exercises":parser.count["exercise"],"sage_cells":parser.count["sage_cells"],"tables":parser.count["tables"],"figures":parser.count["figures"],"images":parser.count["images"],"local_html_links":len(parser.links),"external_links":len(parser.external)},"linked_assets":{"paths":sorted(set(parser.assets)),"resolved_local":resolved,"unresolved_local":unresolved},"warnings":warnings,"scope_class":scope(rel,title,cat)})
        except Exception as e:
            html.append({"relative_path":rel,"sha256":sha,"classification":"malformed_or_unreadable","reason":f"{type(e).__name__}: {e}","scope_class":"unknown_scope"})
    inventory_doc={"generated_at_utc":datetime.now(timezone.utc).isoformat(),"canonical_project_root":str(ROOT),"source_roots":[str(ROOT),str(ROOT/"DM TXT")],"exclusions":{"directory_names":sorted(EXCLUDED_DIRS),"note":"Excluded directories were not traversed; no files inside them are source corpus inputs."},"records":inventory}
    write("source_inventory_tree.json",inventory_doc)
    write("source_inventory_classified.json",{"generated_at_utc":datetime.now(timezone.utc).isoformat(),"html_file_count":len(html),"records":html})
    scopes=Counter(x.get("scope_class","unknown_scope") for x in html); cats=Counter(x.get("classification") for x in html)
    write("scope_classification.json",{"generated_at_utc":datetime.now(timezone.utc).isoformat(),"counts":dict(sorted(scopes.items())),"records":[{"relative_path":x["relative_path"],"classification":x.get("classification"),"scope_class":x.get("scope_class"),"title":x.get("title")} for x in html]})
    def slug(s): return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")
    used=defaultdict(list)
    for x in html:
        if x.get("classification") in {"section_content","chapter_landing","appendix_content","index","backmatter"}:
            key=f"{x['scope_class']}/{slug(Path(x['relative_path']).stem)}.md"; used[key].append(x["relative_path"])
    collisions={k:v for k,v in used.items() if len(v)>1}
    naming={"proposal_only":True,"source_provenance":"Each Markdown file must retain source_relative_path and source_sha256 in front matter.","rules":["One section_content source page maps to one Markdown file by default.","Use lowercase ASCII kebab-case derived from displayed number/title; preserve source numbering as a prefix when detected.","Place active_candidate under corpus/active/, deferred_candidate under corpus/deferred/, reference under corpus/reference/, and reference_solution under corpus/reference_solution/.","Put chapter landings in their chapter directory as index.md; map the frontmatter landing to corpus/reference/frontmatter/index.md; map index and backmatter explicitly under corpus/reference/.","Retain assets by provenance; do not rename source assets during initial conversion."],"detected_slug_collisions":collisions,"exceptions":[x["relative_path"] for x in html if x.get("classification") in {"unknown","malformed_or_unreadable","navigation_or_support"} or not x.get("displayed_section_or_chapter")]}
    write("naming_convention.json",naming)
    fixtures=[x["relative_path"] for x in html if x.get("classification")=="section_content"][:6]
    plan={"phase":"Phase 1 formulation only; no converter code","eligible_source_classes":["frontmatter","section_content","chapter_landing","appendix_content","index","backmatter"],"excluded_source_classes":["navigation_or_support","malformed_or_unreadable","unknown"],"math_requirements":["Preserve .process-math nodes.","Preserve script[type^=math/tex] nodes verbatim."],"semantic_taxonomy_found":{k:sum(x.get("counts",{}).get(k,0) for x in html) for k in ["definitions","theorem_proposition_lemma_corollary","examples","exercises","sage_cells","tables","figures","images"]},"fixture_candidates":fixtures,"frontmatter_required":["title","displayed_section_or_chapter","scope_class","source_relative_path","source_sha256","source_pretext_ids"],"test_gates":["Fidelity: math-node and semantic-block counts meet expected preserved counts.","Provenance: output front matter matches inventory path and SHA-256.","Asset resolution: every retained local asset link resolves or is explicitly flagged.","Idempotence: a second conversion run produces byte-identical outputs.","No default retrieval of reference_solution outputs."],"unresolved_ambiguities":["Confirm desired canonical output root before Phase 1.","Review unresolved local assets before converting them.","Known extraction quirk: the index page stores displayed_section_or_chapter as 'Index Index'; Phase 1 frontmatter extraction must de-duplicate this label."]}
    write("phase1_plan.json",plan)
    survey=f"# Phase 0 workspace survey\n\n- Canonical project root: `{ROOT}`\n- Confirmed corpus input root: `{ROOT}`; HTML subtree: `{ROOT/'DM TXT'}`.\n- Existing generated/output directory: `planning/phase0/` (created for this authorization).\n- `AGENTS.md` present. `.git/` exists but `git status` reported no usable worktree.\n- Detailed inventory excludes: {', '.join(sorted(EXCLUDED_DIRS))}.\n- Extension counts: `{dict(sorted(extensions.items()))}`.\n"
    (OUT/"00_workspace_survey.md").write_text(survey,encoding="utf-8")
    tax=f"# HTML taxonomy\n\n- HTML files: {len(html)}\n- Classification counts: `{dict(sorted(cats.items()))}`\n- Scope counts: `{dict(sorted(scopes.items()))}`\n- Files with warnings: {sum(bool(x.get('warnings')) for x in html)}. See `source_inventory_classified.json` for per-file warnings and assets.\n"
    (OUT/"01_html_taxonomy.md").write_text(tax,encoding="utf-8")
    layout="# Proposed canonical layout (proposal only)\n\n```text\ncorpus/\n  active/chNN/\n  deferred/chNN/\n  reference/\n  reference_solution/\n```\n\nOne content page maps to one Markdown page. Use numbered lowercase kebab-case paths where a displayed number is detected; retain source path and SHA-256 in front matter. See `naming_convention.json` for exceptions and collisions.\n"
    (OUT/"02_proposed_layout.md").write_text(layout,encoding="utf-8")
    form="# Phase 1 formulation\n\nPhase 1 may convert only the eligible classes identified in `phase1_plan.json`, using the listed fixtures and test gates. It must support both PreTeXt math representations and preserve provenance. No conversion was performed in Phase 0.\n"
    (OUT/"03_phase1_formulation.md").write_text(form,encoding="utf-8")
    # Return the exact baseline for a post-run comparison without writing inside source.
    agents=ROOT/"AGENTS.md"
    write("source_hash_baseline.json", {"source_root":str(ROOT),"hashes":baseline,"excluded_tracking_paths":{"AGENTS.md":"tracked separately because it has an approved amendment path"}})
    write("agents_md_baseline.json", {"relative_path":"AGENTS.md","sha256":digest(agents),"size_bytes":agents.stat().st_size,"tracking_policy":"Informational only: a mismatch requires user confirmation of an approved amendment; it is not automatically a corpus-integrity failure."})

if __name__ == "__main__": main()
