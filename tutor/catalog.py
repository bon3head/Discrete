import os
import re
import json
from pathlib import Path

_CATALOG = None
_SCOPE_MAP = None

def _load_scope_map():
    global _SCOPE_MAP
    _SCOPE_MAP = {}
    try:
        with open("planning/phase0/scope_classification.json", "r") as f:
            data = json.load(f)
            for item in data:
                _SCOPE_MAP[item["relative_path"]] = item["classification"]
    except Exception:
        pass

def _build_catalog():
    global _CATALOG
    if _SCOPE_MAP is None:
        _load_scope_map()
        
    _CATALOG = []
    base_dir = Path("corpus/active")
    if not base_dir.exists():
        return
        
    for ch_dir in base_dir.iterdir():
        if ch_dir.is_dir() and ch_dir.name.startswith("ch"):
            try:
                chapter_num = int(ch_dir.name[2:])
            except ValueError:
                continue
                
            for md_file in ch_dir.iterdir():
                if md_file.is_file() and md_file.suffix == ".md":
                    displayed = ""
                    source_rel = ""
                    with open(md_file, "r") as f:
                        lines = f.readlines()
                        if lines and lines[0].strip() == "---":
                            for line in lines[1:]:
                                if line.strip() == "---":
                                    break
                                if line.startswith("displayed_section_or_chapter:"):
                                    displayed = line.split(":", 1)[1].strip().strip('"').strip("'")
                                if line.startswith("source_relative_path:"):
                                    source_rel = line.split(":", 1)[1].strip().strip('"').strip("'")
                                    
                    section_num = None
                    m = re.match(r'^Section\s+([0-9]+\.[0-9]+)', displayed)
                    if m:
                        section_num = m.group(1)
                        
                    record_type = _SCOPE_MAP.get(source_rel, "unknown")
                    # Fallbacks based on prefix if scope_classification missed it
                    if record_type == "unknown":
                        if displayed.startswith("Chapter"): record_type = "chapter_landing"
                        elif displayed.startswith("Section"): record_type = "section_content"
                        elif displayed.startswith("Appendix"): record_type = "appendix_content"
                        
                    _CATALOG.append({
                        "chapter": chapter_num,
                        "section": section_num,
                        "corpus_path": str(md_file),
                        "displayed_section_or_chapter": displayed,
                        "record_type": record_type
                    })

def get_corpus_paths(chapter: int, section: str = None):
    if _CATALOG is None:
        _build_catalog()
        
    if section is not None:
        if not re.match(r'^[0-9]+\.[0-9]+$', section):
            return "INVALID_SECTION_IDENTIFIER", [], []
            
        matched_section = []
        for c in _CATALOG:
            if c["chapter"] == chapter and c["section"] == section:
                matched_section.append(c["corpus_path"])
                
        if not matched_section:
            return "UNKNOWN_SECTION", [], []
        return "active_candidate", [], sorted(matched_section)
        
    # Chapter only
    matched_chapter = []
    matched_section = []
    for c in _CATALOG:
        if c["chapter"] == chapter:
            if c["record_type"] == "chapter_landing":
                matched_chapter.append(c["corpus_path"])
            elif c["record_type"] == "section_content" and c["section"] is not None:
                matched_section.append(c["corpus_path"])
            
    if not matched_chapter and not matched_section:
        return "UNKNOWN_CHAPTER", [], []
        
    return "active_candidate", sorted(matched_chapter), sorted(matched_section)

def resolve_reference(reference_allowed: bool):
    if not reference_allowed:
        return None, [], []
        
    ref_path = Path("corpus/reference_solution/AppendixF-Hints_and_Solutions_to_Selected_Exercises.md")
    if ref_path.exists():
        return "reference_solution", [str(ref_path)], []
    return "reference_solution", [], []

def get_catalog_record(path: str):
    if _CATALOG is None:
        _build_catalog()
    for c in _CATALOG:
        if c["corpus_path"] == path:
            return c
    return None

def get_full_catalog():
    if _CATALOG is None:
        _build_catalog()
    return _CATALOG
