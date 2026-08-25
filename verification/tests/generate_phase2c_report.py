import json
import sys
import subprocess
import os
import hashlib
from pathlib import Path
from verification import verify

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def generate():
    fixtures_dir = Path("verification/tests/fixtures")
    expected = json.loads((fixtures_dir / "recurrence_induction_expected.json").read_text())
    
    # Recurrence Results
    rec_claims = json.loads((fixtures_dir / "recurrence_claims.json").read_text())
    rec_results = []
    rec_passed = 0
    rec_unv_general = []
    
    for c in rec_claims:
        res = verify(c)
        ev = expected[c["claim_id"]]
        passed = (res["verdict"] == ev["expected_verdict"] and res["reason_code"] == ev["expected_reason_code"])
        if passed: rec_passed += 1
        rec_results.append({
            "claim_id": c.get("claim_id"),
            "expected_verdict": ev["expected_verdict"],
            "actual_verdict": res["verdict"],
            "passed": passed
        })
        if res["reason_code"] == "RECURRENCE_FINITE_EVIDENCE_ONLY":
            rec_unv_general.append(c["claim_id"])
            
    # Induction Results
    ind_claims = json.loads((fixtures_dir / "induction_claims.json").read_text())
    ind_results = []
    ind_passed = 0
    ind_unv_general = []
    
    for c in ind_claims:
        res = verify(c)
        ev = expected[c["claim_id"]]
        passed = (res["verdict"] == ev["expected_verdict"] and res["reason_code"] == ev["expected_reason_code"])
        if passed: ind_passed += 1
        ind_results.append({
            "claim_id": c.get("claim_id"),
            "expected_verdict": ev["expected_verdict"],
            "actual_verdict": res["verdict"],
            "passed": passed
        })
        if res["reason_code"] == "INDUCTION_FINITE_EVIDENCE_ONLY":
            ind_unv_general.append(c["claim_id"])
            
    # Mutation tests
    rec_parser_path = "verification/recurrences.py"
    orig_sha = sha256_file(rec_parser_path)
    
    # "Change recurrence verification so it compares candidate value to itself rather than recurrence RHS."
    orig_line = "if actual_val != rhs_val:"
    mutated_line = "if actual_val != actual_val:"
    
    with open(rec_parser_path, "r") as f:
        content = f.read()
        
    try:
        with open(rec_parser_path, "w") as f:
            f.write(content.replace(orig_line, mutated_line))
            
        proc = subprocess.run([sys.executable, "-m", "unittest", "verification/tests/test_recurrences.py"], capture_output=True, text=True, env={**os.environ, "PYTHONPATH": "."})
        ret_code = proc.returncode
        detected = (ret_code != 0)
        summary = "Tests failed" if detected else "Tests passed"
        
        # We need to capture the exact mutated result of the false candidate
        import verification.recurrences
        import importlib
        importlib.reload(verification.recurrences)
        # Using rec-fail-candidate which normally fails, but now passes? No, actually wait: if actual == actual, it doesn't fail, so it returns UNVERIFIABLE for general.
        false_cand_claim = [c for c in rec_claims if c["claim_id"] == "rec-fail-candidate"][0]
        actual_behavior = verification.recurrences.verify_recurrence(false_cand_claim)
        behavior_str = f"Verdict: {actual_behavior['verdict']}, Reason: {actual_behavior['reason_code']}"
        
    finally:
        with open(rec_parser_path, "w") as f:
            f.write(content)
        restored_sha = sha256_file(rec_parser_path)
        assert restored_sha == orig_sha, "SHA mismatch"
        
    mutation_results = [{
        "mutation_id": "recurrence_self_compare",
        "temporary_only": True,
        "restoration_method": "try/finally write with SHA-256 verification",
        "before_sha": orig_sha,
        "after_sha": restored_sha,
        "actual_mutated_behavior": behavior_str,
        "test_command": "python3 -m unittest verification/tests/test_recurrences.py",
        "test_return_code": ret_code,
        "detected": detected,
        "detector_output_summary": summary
    }]
    
    report = {
        "recurrence_results": rec_results,
        "induction_results": ind_results,
        "mathematical_honesty_check": rec_unv_general + ind_unv_general,
        "mutation_results": mutation_results,
        "summary": {
            "recurrence_total": len(rec_claims),
            "recurrence_passed": rec_passed,
            "induction_total": len(ind_claims),
            "induction_passed": ind_passed
        },
        "deferred_capabilities": [
            "recurrence solving",
            "generating functions",
            "formal induction proofs",
            "proof judgment",
            "natural-language/LaTeX parsing",
            "Sage",
            "graphs",
            "tutor integration"
        ]
    }
    
    os.makedirs("verification/reports", exist_ok=True)
    with open("verification/reports/phase2c_test_report.json", "w") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    generate()
