import unittest
import json
import os
import sys
from unittest.mock import patch
from pathlib import Path

from tutor.types import SessionRequest
from tutor.executor import execute_session
from tutor.session_plan import build_session_plan

class ExecutorTests(unittest.TestCase):
    def setUp(self):
        with open("tutor/tests/fixtures/end_to_end_sessions.json", "r") as f:
            content = f.read().replace("None", "null")
            self.fixtures = json.loads(content)
            
        os.environ["TEST_RUN"] = "1"

    def test_all_end_to_end_fixtures(self):
        for f in self.fixtures:
            req_id = f["request"]["request_id"]
            with self.subTest(request_id=req_id):
                req = SessionRequest(**f["request"])
                
                # Check expected plan status first
                plan = build_session_plan(req)
                self.assertEqual(plan.status, f["expected_plan_status"], "Plan status mismatch")
                
                # For req-13, simulate a missing authorized path
                if req_id == "req-e2e-13":
                    original_isfile = os.path.isfile
                    def mock_isfile(path):
                        if "equivalence-and-implication.md" in str(path):
                            return False
                        return original_isfile(path)
                    
                    with patch("os.path.isfile", side_effect=mock_isfile):
                        guard_res = execute_session(req, f["candidate_response"])
                else:
                    guard_res = execute_session(req, f["candidate_response"])
                
                self.assertEqual(guard_res.status, f["expected_guard_status"], "Guard status mismatch")
                self.assertEqual(guard_res.reason_code, f["expected_reason_code"], "Guard reason mismatch")
