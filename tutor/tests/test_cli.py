import unittest
import json
import os
import shutil
import sys
from pathlib import Path
from unittest.mock import patch
from io import StringIO

from tutor.cli import main
from tutor.session_store import SESSIONS_DIR, load_session, load_verdict, save_session

def run_cli(*args):
    with patch("sys.argv", ["tutor.cli"] + list(args)):
        with patch("sys.stdout", new=StringIO()) as out:
            try:
                main()
            except SystemExit as e:
                return e.code, out.getvalue()
            return 0, out.getvalue()

def run_smoke_tests():
    # 1. 3.3 happy-path hint -> PASS
    code, out = run_cli("new", "--chapter", "3", "--section", "3.3")
    assert code == 0
    sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
    
    with open(SESSIONS_DIR / sid / "response.json", "w") as f:
        json.dump({
            "hint_level_used": "L3",
            "response_type": "hint",
            "body": "Smoke test body",
            "citations": [{"corpus_path": "corpus/active/ch03/equivalence-and-implication.md"}],
            "verification_footer": None,
            "next_step": "next",
            "final_answer_reveal": False
        }, f)
        
    code, out = run_cli("validate", sid)
    v = load_verdict(sid)
    res1 = (v["status"] == "PASS")
    
    # 2. L4 without attempt -> blocked
    code, out = run_cli("new", "--chapter", "3", "--section", "3.3")
    sid2 = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
    with open(SESSIONS_DIR / sid2 / "response.json", "w") as f:
        json.dump({
            "hint_level_used": "L4",
            "response_type": "walkthrough",
            "body": "Smoke test body",
            "citations": [{"corpus_path": "corpus/active/ch03/equivalence-and-implication.md"}],
            "verification_footer": None,
            "next_step": "next",
            "final_answer_reveal": False
        }, f)
    code, out = run_cli("validate", sid2)
    v2 = load_verdict(sid2)
    res2 = (v2["status"] == "POLICY_BLOCKED" and v2["reason_code"] == "HINT_LEVEL_EXCEEDS_AUTHORIZATION")
    
    # 3. pre-attempt Appendix F -> POLICY_BLOCKED
    code, out = run_cli("new", "--chapter", "3", "--ref")
    sid3 = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
    sess3 = load_session(sid3)
    res3 = (sess3["state"] == "BLOCKED")
    
    print("Smoke 1 (Happy path):", "PASS" if res1 else "FAIL")
    print("Smoke 2 (L4 without attempt):", "PASS" if res2 else "FAIL")
    print("Smoke 3 (Appendix F pre-attempt):", "PASS" if res3 else "FAIL")
    
    return res1 and res2 and res3

class CLITests(unittest.TestCase):
    def setUp(self):
        os.environ["TEST_RUN"] = "1"
        
    def test_fixture_1_happy_path(self):
        code, out = run_cli("new", "--chapter", "3", "--section", "3.3")
        self.assertEqual(code, 0)
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        with open(SESSIONS_DIR / sid / "response.json", "w") as f:
            json.dump({
                "hint_level_used": "L3",
                "response_type": "hint",
                "body": "Safe body",
                "citations": [{"corpus_path": "corpus/active/ch03/equivalence-and-implication.md"}],
                "verification_footer": None,
                "next_step": "next",
                "final_answer_reveal": False
            }, f)
            
        code, _ = run_cli("validate", sid)
        self.assertEqual(code, 0)
        
        code, show_out = run_cli("show", sid)
        self.assertEqual(code, 0)
        self.assertIn("Safe body", show_out)
        
        # Validate idempotence
        code, _ = run_cli("validate", sid)
        self.assertEqual(code, 0)
        
    def test_fixture_2_malformed_response(self):
        code, out = run_cli("new", "--chapter", "3", "--section", "3.3")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        with open(SESSIONS_DIR / sid / "response.json", "w") as f:
            json.dump({
                "unknown_key": "bad"
            }, f)
            
        code, _ = run_cli("validate", sid)
        v = load_verdict(sid)
        self.assertEqual(v["status"], "REVIEW_REQUIRED")
        self.assertIn("RESPONSE_SCHEMA_VIOLATION", v["reason_code"])
        
        code, show_out = run_cli("show", sid)
        self.assertEqual(code, 1)
        
    def test_fixture_3_missing_response(self):
        code, out = run_cli("new", "--chapter", "3", "--section", "3.3")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        code, val_out = run_cli("validate", sid)
        self.assertEqual(code, 1)
        self.assertIn("No response.json found", val_out)
        
    def test_fixture_6_mock_exam(self):
        code, out = run_cli("new", "--chapter", "3", "--mode", "mock_exam")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        # in_progress L0 response -> PASS
        with open(SESSIONS_DIR / sid / "response.json", "w") as f:
            json.dump({
                "hint_level_used": "L0",
                "response_type": "clarification",
                "body": "Safe body",
                "citations": [{"corpus_path": "corpus/active/ch03/equivalence-and-implication.md"}],
                "verification_footer": None,
                "next_step": "next",
                "final_answer_reveal": False
            }, f)
        run_cli("validate", sid)
        self.assertEqual(load_verdict(sid)["status"], "PASS")
        
        # L1 attempt -> blocked
        with open(SESSIONS_DIR / sid / "response.json", "w") as f:
            json.dump({
                "hint_level_used": "L1",
                "response_type": "hint",
                "body": "Safe body",
                "citations": [{"corpus_path": "corpus/active/ch03/equivalence-and-implication.md"}],
                "verification_footer": None,
                "next_step": "next",
                "final_answer_reveal": False
            }, f)
        run_cli("validate", sid)
        v = load_verdict(sid)
        self.assertEqual(v["status"], "POLICY_BLOCKED")
        self.assertEqual(v["reason_code"], "MOCK_EXAM_HINT_FORBIDDEN")
        
        # submit-attempt -> L4 response -> PASS
        run_cli("submit-attempt", sid)
        # Since submit-attempt doesn't automatically re-plan the existing turn, wait, the orchestrator is stateless.
        # So we just re-run validate! The executor will load the session and see `exam_phase` is submitted.
        # Wait, the CLI `validate` command loads `req = SessionRequest(**session["turns"][-1]["request"])`. 
        # But `submit-attempt` only flips the session object, it DOES NOT update the `SessionRequest` in `session["turns"][-1]`.
        # The executor's `build_session_plan(req)` receives `req.student_attempt.provided`.
        # Oh, `validate` uses `req` from `turns[-1]`. I need to make sure `submit-attempt` updates the `student_attempt` in the turn request or re-plans!

    def test_fixture_6_mock_exam_submit(self):
        code, out = run_cli("new", "--chapter", "3", "--mode", "mock_exam")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        run_cli("submit-attempt", sid)
        
        with open(SESSIONS_DIR / sid / "response.json", "w") as f:
            json.dump({
                "hint_level_used": "L4",
                "response_type": "walkthrough",
                "body": "Safe body",
                "citations": [{"corpus_path": "corpus/active/ch03/equivalence-and-implication.md"}],
                "verification_footer": None,
                "next_step": "next",
                "final_answer_reveal": False
            }, f)
        run_cli("validate", sid)
        self.assertEqual(load_verdict(sid)["status"], "PASS")

    def test_fixture_4_escalation(self):
        code, out = run_cli("new", "--chapter", "3", "--section", "3.3", "--hint", "L1")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        # New turn in same session
        code, out = run_cli("new", "--id", sid, "--chapter", "3", "--section", "3.3", "--hint", "L2")
        session = load_session(sid)
        self.assertEqual(len(session["turns"]), 2)
        self.assertEqual(session["turns"][-1]["requested_hint_level"], "L2")
        
    def test_fixture_8_idempotence(self):
        code, out = run_cli("new", "--chapter", "3", "--section", "3.3")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        with open(SESSIONS_DIR / sid / "response.json", "w") as f:
            json.dump({
                "hint_level_used": "L3",
                "response_type": "hint",
                "body": "Safe body",
                "citations": [{"corpus_path": "corpus/active/ch03/equivalence-and-implication.md"}],
                "verification_footer": None,
                "next_step": "next",
                "final_answer_reveal": False
            }, f)
            
        run_cli("validate", sid)
        with open(SESSIONS_DIR / sid / "verdict.json", "rb") as f:
            v1 = f.read()
            
        run_cli("validate", sid)
        with open(SESSIONS_DIR / sid / "verdict.json", "rb") as f:
            v2 = f.read()
            
        self.assertEqual(v1, v2)

    def test_regression_path_traversal(self):
        from tutor.session_store import get_session_dir
        with self.assertRaises(ValueError):
            get_session_dir("../../../etc")
            
    def test_regression_missing_session(self):
        code, out = run_cli("validate", "00000000-0000-0000-0000-000000000000")
        self.assertEqual(code, 1)
        self.assertIn("not found", out)

    def test_regression_state_machine_validated(self):
        # Fixture 1 runs validate, let's just make a new one and check the state explicitly
        code, out = run_cli("new", "--chapter", "3", "--section", "3.3")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        with open(SESSIONS_DIR / sid / "response.json", "w") as f:
            json.dump({
                "hint_level_used": "L3",
                "response_type": "hint",
                "body": "Safe body",
                "citations": [{"corpus_path": "corpus/active/ch03/equivalence-and-implication.md"}],
                "verification_footer": None,
                "next_step": "next",
                "final_answer_reveal": False
            }, f)
            
        run_cli("validate", sid)
        session = load_session(sid)
        self.assertEqual(session["state"], "VALIDATED")
        
    def test_regression_turn_index(self):
        code, out = run_cli("new", "--chapter", "3", "--section", "3.3")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        run_cli("new", "--id", sid, "--chapter", "3", "--hint", "L4")
        session = load_session(sid)
        self.assertEqual(session["turns"][0]["request"]["request_id"], f"{sid}-turn0")
        self.assertEqual(session["turns"][1]["request"]["request_id"], f"{sid}-turn1")
