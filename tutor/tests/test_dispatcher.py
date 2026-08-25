import unittest
import json
import os
import sys
from pathlib import Path

from tutor.types import SessionRequest
from tutor.session_plan import build_session_plan
from tutor.catalog import get_catalog_record
from verification.dispatcher import verify

class TutorOrchestrationTests(unittest.TestCase):
    def setUp(self):
        with open("tutor/tests/fixtures/session_requests.json", "r") as f:
            content = f.read().replace("None", "null")
            self.fixtures = json.loads(content)

    def test_all_fixtures(self):
        for f in self.fixtures:
            req_id = f["request"]["request_id"]
            with self.subTest(request_id=req_id):
                req_dict = f["request"]
                req = SessionRequest(**req_dict)
                
                if req_id == "req-13":
                    os.makedirs("corpus/reference_solution", exist_ok=True)
                    Path("corpus/reference_solution/AppendixF-Hints_and_Solutions_to_Selected_Exercises.md").touch()
                    
                plan = build_session_plan(req)
                
                if req_id == "req-13":
                    os.remove("corpus/reference_solution/AppendixF-Hints_and_Solutions_to_Selected_Exercises.md")
                
                self.assertEqual(plan.status, f["expected_status"], f"Status mismatch")
                
                if "expected_max_hint" in f and plan.policy:
                    self.assertEqual(plan.policy["max_hint_level"], f["expected_max_hint"], f"Hint mismatch")
                    
                if "expected_reason" in f:
                    self.assertEqual(plan.reason_code, f["expected_reason"], f"Reason mismatch")
                    
                if "expected_verification_verdict" in f:
                    self.assertEqual(plan.verification_result["verdict"], f["expected_verification_verdict"])
                    
                if "expected_reference_solution_available_locally" in f and plan.policy:
                    self.assertEqual(plan.policy.get("reference_solution_available_locally", False), f["expected_reference_solution_available_locally"])
                    
                # Exact Section Test 1 (3.1)
                if req_id == "req-11":
                    sec_paths = plan.retrieval["section_paths"]
                    ctx_paths = plan.retrieval["chapter_context_paths"]
                    self.assertEqual(len(sec_paths), 1, "Exactly one section path expected")
                    self.assertEqual(len(ctx_paths), 0, "Zero chapter context paths expected")
                    record = get_catalog_record(sec_paths[0])
                    self.assertEqual(record["section"], "3.1")
                    
                # Chapter-only test (req-1)
                if req_id == "req-1":
                    sec_paths = plan.retrieval["section_paths"]
                    ctx_paths = plan.retrieval["chapter_context_paths"]
                    self.assertEqual(len(ctx_paths), 1, "Expected exactly 1 chapter context path")
                    self.assertEqual(len(sec_paths), 9, "Expected exactly 9 section paths")
                    
                    # No duplicate path across chapter_context_paths and section_paths
                    intersect = set(ctx_paths).intersection(set(sec_paths))
                    self.assertEqual(len(intersect), 0, "Duplicate path found between context and sections")
                    
                    for p in sec_paths:
                        rec = get_catalog_record(p)
                        self.assertEqual(rec["chapter"], 3, "All records must be chapter 3")
                        self.assertIsNotNone(rec["section"], "Section number must not be null")
                        
                    for p in ctx_paths:
                        rec = get_catalog_record(p)
                        self.assertEqual(rec["record_type"], "chapter_landing", "Context must be chapter_landing")
                    
    def test_verifier_preservation(self):
        req_id = "req-7"
        f = next(fix for fix in self.fixtures if fix["request"]["request_id"] == req_id)
        
        req = SessionRequest(**f["request"])
        plan = build_session_plan(req)
        
        expected_verif = verify(req.claim)
        self.assertEqual(plan.verification_result, expected_verif, "Verification result altered")
