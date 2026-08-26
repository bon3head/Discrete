import json
import hashlib
import sys
from pathlib import Path

def verify_baseline():
    baseline_path = Path("planning/phase1/corpus_active_baseline.json")
    if not baseline_path.exists():
        print("Error: Baseline not found.")
        sys.exit(1)
        
    with open(baseline_path, "r") as f:
        baseline = json.load(f)
        
    active_dir = Path("corpus/active")
    current_files = {str(p.relative_to(active_dir.parent)): p for p in active_dir.rglob("*.md")}
    
    baseline_files = {rec["path"]: rec["sha256"] for rec in baseline["files"]}
    
    mismatches = []
    missing = []
    added = []
    
    for path, expected_sha in baseline_files.items():
        if path not in current_files:
            missing.append(path)
        else:
            with open(active_dir.parent / path, "rb") as f:
                actual_sha = hashlib.sha256(f.read()).hexdigest()
            if actual_sha != expected_sha:
                mismatches.append(path)
                
    for path in current_files:
        if path not in baseline_files:
            added.append(path)
            
    success = (not mismatches and not missing and not added)
    
    result = {
        "all_match": success,
        "mismatches": mismatches,
        "missing": missing,
        "added": added,
        "total_checked": len(baseline_files)
    }
    
    with open("planning/phase1/corpus_active_verification.json", "w") as f:
        json.dump(result, f, indent=2)
        
    if success:
        print(f"OK: {len(baseline_files)} files match active baseline.")
        sys.exit(0)
    else:
        print("FAIL: Active corpus baseline mismatch!")
        print(json.dumps(result, indent=2))
        sys.exit(1)

if __name__ == "__main__":
    verify_baseline()
