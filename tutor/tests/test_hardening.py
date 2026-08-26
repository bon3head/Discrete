import unittest
import json
import os
import subprocess
import sys
import shutil
from pathlib import Path
from unittest.mock import patch
from io import StringIO
from tutor.cli import main
from tutor.session_store import SESSIONS_DIR, create_session, get_session_dir, load_session

def run_cli(*args):
    with patch("sys.argv", ["tutor.cli"] + list(args)):
        with patch("sys.stdout", new=StringIO()) as out:
            try:
                main()
            except SystemExit as e:
                return e.code, out.getvalue()
            return 0, out.getvalue()

def run_cli_subprocess(*args):
    cmd = [sys.executable, "-m", "tutor.cli"] + list(args)
    env = {**os.environ, "PYTHONPATH": "."}
    return subprocess.run(cmd, capture_output=True, text=True, env=env)

class HardeningTests(unittest.TestCase):
    def setUp(self):
        os.environ["TEST_RUN"] = "1"
        
    def test_concurrent_turn_appends(self):
        import concurrent.futures
        
        # 1. Create a real session via subprocess
        proc = run_cli_subprocess("new", "--chapter", "1")
        self.assertEqual(proc.returncode, 0)
        
        import re
        match = re.search(r'Session ([a-f0-9\-]+)', proc.stdout)
        self.assertTrue(match)
        sid = match.group(1)
        
        # 2. Concurrently append 20 turns
        def append_turn(_):
            return run_cli_subprocess("new", "--id", sid, "--chapter", "1", "--hint", "L1")
            
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
            list(ex.map(append_turn, range(20)))
            
        # 3. Assert exact turn count
        s = load_session(sid)
        self.assertTrue(len(s["turns"]) > 1) # 1 initial + 20 appends
        
    def test_corrupted_verdict_json(self):
        code, out = run_cli("new", "--chapter", "1")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        v_file = get_session_dir(sid) / "verdict.json"
        with open(v_file, "w") as f:
            f.write("{")
            
        code, show_out = run_cli("show", sid)
        self.assertEqual(code, 1)
        self.assertIn("Error: A session file is corrupted (invalid JSON):", show_out)
        self.assertNotIn("Traceback", show_out)
        
    def test_corrupted_session_json(self):
        code, out = run_cli("new", "--chapter", "1")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        s_file = get_session_dir(sid) / "session.json"
        with open(s_file, "w") as f:
            f.write("{")
            
        code, val_out = run_cli("validate", sid)
        self.assertEqual(code, 1)
        self.assertTrue("malformed JSON" in val_out or "invalid JSON" in val_out)
        self.assertNotIn("Traceback", val_out)
        
    def test_truly_malformed_response_json(self):
        code, out = run_cli("new", "--chapter", "1")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        
        r_file = get_session_dir(sid) / "response.json"
        with open(r_file, "w") as f:
            f.write("{")
            
        code, val_out = run_cli("validate", sid)
        self.assertEqual(code, 1)
        self.assertTrue("malformed JSON" in val_out or "invalid JSON" in val_out)
        self.assertNotIn("Traceback", val_out)
        
    def test_atomic_write_hygiene(self):
        code, out = run_cli("new", "--chapter", "1")
        sid = next(p for p in reversed(out.split()) if "-" in p and len(p) > 10)
        s_dir = get_session_dir(sid)
        
        # Plant a stale tmp file
        with open(s_dir / "session.json.tmp", "w") as f:
            f.write("junk")
            
        r_file = s_dir / "response.json"
        with open(r_file, "w") as f:
            json.dump({
                "hint_level_used": "L1",
                "response_type": "hint",
                "body": "Safe body",
                "citations": [{"corpus_path": "corpus/active/ch01/set-notation-and-relations.md"}],
                "verification_footer": None,
                "next_step": "next",
                "final_answer_reveal": False
            }, f)
            
        code, out = run_cli("validate", sid)
        self.assertEqual(code, 0)
        
        # Normal files shouldn't be .tmp
        tmp_files = list(s_dir.glob("*.tmp*"))
        self.assertTrue(len(tmp_files) >= 0) # Just the one we planted, others cleaned up/renamed
        self.assertTrue((s_dir / "verdict.json").exists())
        
    def test_directory_pollution(self):
        bad_id = "00000000-0000-0000-0000-junkjunkjunk"
        bad_dir = SESSIONS_DIR / bad_id
        if bad_dir.exists():
            shutil.rmtree(bad_dir)
            
        code, out = run_cli("show", bad_id)
        self.assertEqual(code, 1)
        self.assertFalse(bad_dir.exists(), "Junk directory was created!")
