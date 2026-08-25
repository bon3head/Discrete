import json
import sys
import subprocess
import os
import hashlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tutor.types import SessionRequest
from tutor.session_plan import build_session_plan
from tutor.catalog import get_full_catalog

def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def generate():
    fixtures_file = Path("tutor/tests/fixtures/session_requests.json")
    with open(fixtures_file, "r") as f:
        fixtures = json.loads(f.read().replace("None", "null"))
        
    results = []
    passed = 0
    
    for fx in fixtures:
        if fx["request"]["request_id"] == "req-13":
            os.makedirs("corpus/reference_solution", exist_ok=True)
            Path("corpus/reference_solution/AppendixF-Hints_and_Solutions_to_Selected_Exercises.md").touch()
            
        req = SessionRequest(**fx["request"])
        plan = build_session_plan(req)
        
        if fx["request"]["request_id"] == "req-13":
            os.remove("corpus/reference_solution/AppendixF-Hints_and_Solutions_to_Selected_Exercises.md")
            
        fx_passed = True
        if plan.status != fx["expected_status"]: fx_passed = False
        if "expected_reason" in fx and plan.reason_code != fx["expected_reason"]: fx_passed = False
        
        max_hint = plan.policy.get("max_hint_level") if plan.policy else None
        if "expected_max_hint" in fx and max_hint != fx["expected_max_hint"]: fx_passed = False
        
        ref_avail = plan.policy.get("reference_solution_available_locally", False) if plan.policy else False
        exp_ref_avail = fx.get("expected_reference_solution_available_locally", False)
        if ref_avail != exp_ref_avail: fx_passed = False
        
        ret = plan.retrieval
        if ret:
            ctx_cnt = ret.get("chapter_context_count", 0)
            sec_cnt = ret.get("section_count", 0)
            tot_paths = len(set(ret.get("chapter_context_paths", []) + ret.get("section_paths", [])))
        else:
            ctx_cnt = sec_cnt = tot_paths = 0
            
        if fx_passed: passed += 1
            
        results.append({
            "request_id": fx["request"]["request_id"],
            "expected_status": fx["expected_status"],
            "actual_status": plan.status,
            "expected_reason_code": fx.get("expected_reason"),
            "actual_reason_code": plan.reason_code,
            "passed": fx_passed,
            "expected_max_hint_level": fx.get("expected_max_hint"),
            "actual_max_hint_level": max_hint,
            "expected_reference_solution_available_locally": exp_ref_avail,
            "actual_reference_solution_available_locally": ref_avail,
            "chapter_context_count": ctx_cnt,
            "section_count": sec_cnt,
            "total_unique_paths": tot_paths
        })
        
    policy_path = "tutor/policy.py"
    orig_sha = sha256_file(policy_path)
    
    with open(policy_path, "r") as f:
        content = f.read()
        
    lines = content.split("\n")
    for i in range(len(lines)-1, -1, -1):
        if "return False" in lines[i]:
            lines[i] = lines[i].replace("return False", "return True")
            break
    mutated_content = "\n".join(lines)
    
    try:
        with open(policy_path, "w") as f:
            f.write(mutated_content)
            
        proc = subprocess.run([sys.executable, "-m", "unittest", "tutor/tests/test_dispatcher.py"], capture_output=True, text=True, env={**os.environ, "PYTHONPATH": "."})
        detected = (proc.returncode != 0)
    finally:
        with open(policy_path, "w") as f:
            f.write(content)
        restored_sha = sha256_file(policy_path)
        assert restored_sha == orig_sha, "SHA mismatch on restore"
        
    mutation_result = {
        "mutation": "bypass Appendix F pre-attempt gate",
        "detected": detected,
        "detector_exit_code": proc.returncode,
        "before_sha": orig_sha,
        "after_sha": restored_sha,
        "restored_safely": (orig_sha == restored_sha)
    }
    
    # Generate Chapter 3 Catalog Table
    full_catalog = get_full_catalog()
    ch3_catalog = [c for c in full_catalog if c["chapter"] == 3]
    
    report = {
        "statement": "No fuzzy, topic, semantic, or RAG retrieval mechanisms were attempted. Retrieval strictly bounds to numerical catalog frontmatter parsing.",
        "chapter_3_catalog_table": ch3_catalog,
        "fixture_results": results,
        "mutation_result": mutation_result,
        "summary": {
            "total": len(fixtures),
            "passed": passed
        }
    }
    
    with open("tutor/reports/phase3a_test_report.json", "w") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    generate()
