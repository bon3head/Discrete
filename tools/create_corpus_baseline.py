import json
import hashlib
from pathlib import Path

def generate_baseline():
    active_dir = Path("corpus/active")
    if not active_dir.exists():
        print("Error: corpus/active/ not found.")
        return
        
    records = []
    for md_file in active_dir.rglob("*.md"):
        with open(md_file, "rb") as f:
            sha = hashlib.sha256(f.read()).hexdigest()
        records.append({
            "path": str(md_file.relative_to(active_dir.parent)),
            "sha256": sha
        })
        
    records.sort(key=lambda x: x["path"])
    
    baseline = {
        "file_count": len(records),
        "files": records
    }
    
    out_path = Path("planning/phase1/corpus_active_baseline.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(baseline, f, indent=2)
        
    print(f"Created baseline with {len(records)} files at {out_path}")

if __name__ == "__main__":
    generate_baseline()
