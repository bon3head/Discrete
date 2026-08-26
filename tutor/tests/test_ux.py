import unittest
import subprocess
import os
import shutil
import json
from pathlib import Path

def run_tutor(*args):
    cmd = [os.path.abspath("bin/tutor")] + list(args)
    env = {**os.environ, "PYTHONPATH": "."}
    return subprocess.run(cmd, capture_output=True, text=True, env=env)

class UXTests(unittest.TestCase):
    def setUp(self):
        os.environ["TEST_RUN"] = "1"
        if Path("runtime/latest").exists():
            os.remove("runtime/latest")
            
    def get_latest_id(self):
        with open("runtime/latest", "r") as f:
            return f.read().strip()
            
    def test_positional_parsing_and_defaults(self):
        proc = run_tutor("new", "2.1")
        self.assertEqual(proc.returncode, 0)
        sid = self.get_latest_id()
        
        with open(f"runtime/sessions/{sid}/session.json") as f:
            data = json.load(f)
            
        req = data["turns"][0]["request"]
        self.assertEqual(req["context"]["chapter"], 2)
        self.assertEqual(req["context"]["section"], "2.1")
        self.assertEqual(data["turns"][0]["requested_hint_level"], "L1") # default
        
        # Test hint pos
        proc2 = run_tutor("new", "2.1", "L3")
        self.assertEqual(proc2.returncode, 0)
        sid2 = self.get_latest_id()
        with open(f"runtime/sessions/{sid2}/session.json") as f:
            data2 = json.load(f)
        self.assertEqual(data2["turns"][0]["requested_hint_level"], "L3")
        
    def test_exam_alias(self):
        proc = run_tutor("exam", "3")
        self.assertEqual(proc.returncode, 0)
        sid = self.get_latest_id()
        with open(f"runtime/sessions/{sid}/session.json") as f:
            data = json.load(f)
        self.assertEqual(data["exam_phase"], "in_progress")
        self.assertEqual(data["turns"][0]["request"]["mode"], "mock_exam")
        
    def test_latest_pointer_resolution(self):
        run_tutor("new", "1.1")
        sid = self.get_latest_id()
        
        # provide no id to validate
        proc = run_tutor("validate")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("No response.json found", proc.stdout)
        
    def test_stale_pointer_clean_failure(self):
        run_tutor("new", "1.1")
        sid = self.get_latest_id()
        shutil.rmtree(f"runtime/sessions/{sid}") # delete the dir
        
        proc = run_tutor("show")
        self.assertEqual(proc.returncode, 1)
        self.assertIn(f"Error: Session {sid} not found.", proc.stdout)
        self.assertNotIn("Traceback", proc.stdout)
        
    def test_show_auto_validate(self):
        run_tutor("new", "1.1")
        sid = self.get_latest_id()
        
        # valid response
        with open(f"runtime/sessions/{sid}/response.json", "w") as f:
            json.dump({
                "hint_level_used": "L1", "response_type": "hint", "body": "test body",
                "citations": [{"corpus_path": "corpus/active/ch01/set-notation-and-relations.md"}], "verification_footer": None, "next_step": "test", "final_answer_reveal": False
            }, f)
            
        proc = run_tutor("show")
        self.assertEqual(proc.returncode, 0)
        self.assertIn("Auto-validating session", proc.stdout)
        self.assertIn("test body", proc.stdout)
        
        # invalid response (REVIEW_REQUIRED refusal)
        run_tutor("new", "1.1")
        sid2 = self.get_latest_id()
        with open(f"runtime/sessions/{sid2}/response.json", "w") as f:
            json.dump({"bad": "data"}, f)
            
        proc2 = run_tutor("show")
        self.assertEqual(proc2.returncode, 1)
        self.assertIn("Auto-validating", proc2.stdout)
        self.assertIn("Cannot show response. Verdict is REVIEW_REQUIRED", proc2.stdout)
        
    def test_list_output_shape(self):
        run_tutor("new", "1.1")
        proc = run_tutor("list")
        self.assertEqual(proc.returncode, 0)
        # Check standard pipe layout
        self.assertRegex(proc.stdout, r'[a-f0-9]{8}\s+\|\s+1\.1\s+\|\s+BRIEFED\s+\|\s+Turns:\s+1\s+\|\s+Max Hint:\s+L1')
        
    def test_doctor_exit_codes(self):
        proc = run_tutor("doctor")
        self.assertEqual(proc.returncode, 0)
        self.assertIn("Smoke 1", proc.stdout)
        self.assertIn("OK: 49 files match", proc.stdout)
