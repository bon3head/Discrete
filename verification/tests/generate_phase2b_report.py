import json
import sys
import subprocess
import os
import hashlib
from pathlib import Path
from verification import verify
from verification.propositional_parser import parse

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def generate():
    fixtures_dir = Path("verification/tests/fixtures")
    fixture_files = ["propositional_text_claims.json"]
    expected = json.loads((fixtures_dir / "propositional_text_expected.json").read_text())
    
    fixture_results = []
    fixture_passed = 0
    
    for f_name in fixture_files:
        f = fixtures_dir / f_name
        claims = json.loads(f.read_text())
        for c in claims:
            res = verify(c)
            ev = expected[c["claim_id"]]
            
            # verify required fields
            fields_ok = all(k in res for k in ["verdict", "kind", "reason_code", "evidence", "limitations", "source"])
            
            # Independent pass calculation based on oracle
            passed = (res["verdict"] == ev["expected_verdict"] and res["reason_code"] == ev["expected_reason_code"] and fields_ok)
            if passed and "required_evidence" in ev:
                for req in ev["required_evidence"]:
                    if req not in res.get("evidence", {}):
                        passed = False
            
            if passed:
                fixture_passed += 1

            fixture_results.append({
                "claim_id": c.get("claim_id", "unknown"),
                "kind": c.get("kind", "unknown"),
                "expected_verdict": ev["expected_verdict"],
                "actual_verdict": res["verdict"],
                "expected_reason_code": ev["expected_reason_code"],
                "actual_reason_code": res["reason_code"],
                "passed": passed, 
                "evidence_present": bool(res.get("evidence", {}))
            })

    adversarial_claims = [
        {"case_id": "chained_biconditional", "claim": {"kind": "propositional_text", "mode": "equivalence", "lhs_text": "p <-> q <-> r", "rhs_text": "p"}},
        {"case_id": "trailing_implication", "claim": {"kind": "propositional_text", "mode": "equivalence", "lhs_text": "p ->", "rhs_text": "p"}},
        {"case_id": "unmatched_parenthesis", "claim": {"kind": "propositional_text", "mode": "equivalence", "lhs_text": "(p | q", "rhs_text": "p"}},
        {"case_id": "adjacent_propositions", "claim": {"kind": "propositional_text", "mode": "equivalence", "lhs_text": "p q", "rhs_text": "p"}},
        {"case_id": "unsupported_word_operator", "claim": {"kind": "propositional_text", "mode": "equivalence", "lhs_text": "p and q", "rhs_text": "p"}}
    ]
    
    adversarial_results = []
    adv_passed = 0
    
    for adv in adversarial_claims:
        res = verify(adv["claim"])
        fields_ok = all(k in res for k in ["verdict", "kind", "reason_code", "evidence", "limitations", "source"])
        passed = (res["verdict"] == "UNVERIFIABLE" and fields_ok)
        if passed:
            adv_passed += 1
        adversarial_results.append({
            "case_id": adv["case_id"],
            "actual_verdict": res["verdict"],
            "passed": passed,
            "reason_code": res["reason_code"]
        })
        
    parser_path = "verification/propositional_parser.py"
    orig_sha = sha256_file(parser_path)
    
    mutations = [
        {
            "id": "implication_associativity",
            "file": parser_path,
            "orig": "right = self.parse_implies() # Right associative",
            "mutated": "right = self.parse_or()",
            "test_cmd": [sys.executable, "-m", "unittest", "verification/tests/test_propositional_text.py"]
        }
    ]
    
    mutation_results = []
    mut_detected = 0
    
    for m in mutations:
        with open(m["file"], "r") as f:
            content = f.read()
            
        if m["orig"] not in content:
            print(f"Warning: {m['id']} orig not found!")
            ret_code = 0
            summary = "Failed to apply mutation"
            detected = False
        else:
            try:
                # Apply mutation
                with open(m["file"], "w") as f:
                    f.write(content.replace(m["orig"], m["mutated"]))
                
                # Directly parse p -> q -> r to record exact behavior
                try:
                    import importlib
                    import verification.propositional_parser
                    importlib.reload(verification.propositional_parser)
                    ast, _ = verification.propositional_parser.parse("p -> q -> r")
                    actual_behavior = f"Parsed as AST: {ast}"
                except Exception as e:
                    actual_behavior = f"Parse Error: {e}"
                
                proc = subprocess.run(m["test_cmd"], capture_output=True, text=True, env={**os.environ, "PYTHONPATH": "."})
                ret_code = proc.returncode
                detected = (ret_code != 0)
                if detected:
                    mut_detected += 1
                summary = "Tests failed" if detected else "Tests passed"
            finally:
                # Always restore
                with open(m["file"], "w") as f:
                    f.write(content)
                
                # Check SHA
                restored_sha = sha256_file(m["file"])
                assert restored_sha == orig_sha, f"SHA mismatch! original: {orig_sha}, restored: {restored_sha}"
                
        mutation_results.append({
            "mutation_id": m["id"],
            "temporary_only": True,
            "restoration_method": "try/finally write with SHA-256 verification",
            "before_sha": orig_sha,
            "after_sha": restored_sha,
            "actual_mutated_behavior": actual_behavior,
            "test_command": " ".join(m["test_cmd"]),
            "test_return_code": ret_code,
            "detected": detected,
            "detector_output_summary": summary
        })

    report = {
        "environment": {
            "python_version": sys.version,
            "sympy_available": False,
            "dependency_policy": "standard-library-only"
        },
        "grammar_version": "1.0",
        "fixture_results": fixture_results,
        "adversarial_results": adversarial_results,
        "mutation_results": mutation_results,
        "summary": {
            "fixture_total": len(fixture_results),
            "fixture_passed": fixture_passed,
            "adversarial_total": len(adversarial_results),
            "adversarial_passed": adv_passed,
            "mutation_total": len(mutations),
            "mutation_detected": mut_detected
        },
        "deferred_capabilities": [
            "arbitrary English math interpretation",
            "LaTeX logic parsing",
            "quantifiers",
            "predicates",
            "proofs",
            "tutor integration"
        ]
    }
    
    os.makedirs("verification/reports", exist_ok=True)
    with open("verification/reports/phase2b_test_report.json", "w") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    generate()
