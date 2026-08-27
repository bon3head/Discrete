import re
from pathlib import Path

def parse_corpus_block(block_type: str, block_id: str, corpus_root: str = 'corpus/active') -> str | None:
    """
    Scans corpus/active/**/*.md for a blockquote matching:
        > **{block_type} {block_id} —
    Extracts the full contiguous blockquote and returns it as a string.
    Returns None if not found.
    """
    target_pattern = re.compile(rf"^>\s*\*\*{re.escape(block_type)}\s+{re.escape(block_id)}\b")
    header_pattern = re.compile(r"^>\s*\*\*[A-Z][a-z]+\s+\d")
    
    # Sort for determinism
    for path in sorted(Path(corpus_root).rglob('*.md')):
        with open(path, 'r', encoding='utf-8') as f:
            in_block = False
            extracted = []
            pending_empty_lines = []
            for line in f:
                line = line.rstrip('\n')
                if not in_block:
                    if target_pattern.match(line):
                        in_block = True
                        extracted.append(line)
                else:
                    if not line.strip():
                        pending_empty_lines.append(line)
                    elif header_pattern.match(line):
                        break
                    elif line.startswith('>'):
                        extracted.extend(pending_empty_lines)
                        pending_empty_lines = []
                        extracted.append(line)
                    else:
                        break
            if in_block:
                return '\n'.join(extracted)
    return None

def get_section_text(chapter: str, corpus_root: str = 'corpus/active') -> str | None:
    """Returns the full raw markdown of a chapter directory's files concatenated."""
    chapter_dir = Path(corpus_root) / chapter
    if not chapter_dir.is_dir():
        return None
        
    texts = []
    for path in sorted(chapter_dir.glob('*.md')):
        with open(path, 'r', encoding='utf-8') as f:
            texts.append(f.read())
            
    if not texts:
        return None
        
    return '\n\n'.join(texts)
