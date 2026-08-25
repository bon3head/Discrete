#!/usr/bin/env python3
"""Compare the immutable Phase 0 source baseline with current on-disk bytes."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
baseline = json.loads((OUT / "source_hash_baseline.json").read_text(encoding="utf-8"))

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

records = []
for relative_path, baseline_sha256 in sorted(baseline["hashes"].items()):
    path = ROOT / relative_path
    current_sha256 = sha256(path) if path.is_file() else None
    records.append({
        "relative_path": relative_path,
        "baseline_sha256": baseline_sha256,
        "current_sha256": current_sha256,
        "match": current_sha256 == baseline_sha256,
        "current_mtime_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat() if path.exists() else None,
    })
(OUT / "source_hash_verification.json").write_text(json.dumps({
    "source_root": baseline["source_root"],
    "verified_at_utc": datetime.now(timezone.utc).isoformat(),
    "all_match": all(record["match"] for record in records),
    "records": records,
}, indent=2) + "\n", encoding="utf-8")
