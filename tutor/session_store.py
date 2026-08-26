import json
import os
import uuid
from pathlib import Path
from datetime import datetime

SESSIONS_DIR = Path("runtime/sessions")

def get_session_dir(session_id: str) -> Path:
    # Validate UUID format to prevent path traversal
    import re
    if not re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', session_id, re.I):
        raise ValueError(f"Invalid session ID format: {session_id}")
    return SESSIONS_DIR / session_id

def load_session(session_id: str) -> dict:
    s_file = get_session_dir(session_id) / "session.json"
    if not s_file.exists():
        raise FileNotFoundError(f"Session {session_id} not found")
    with open(s_file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_session(session_id: str, data: dict):
    s_dir = get_session_dir(session_id)
    s_dir.mkdir(parents=True, exist_ok=True)

    tmp_path = str(s_dir / "session.json") + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.rename(tmp_path, s_dir / "session.json")

def create_session(args: dict) -> dict:
    session_id = str(uuid.uuid4())
    state = {
        "id": session_id,
        "created_at": datetime.now().isoformat(),
        "state": "CREATED",
        "exam_phase": "in_progress" if args.get("mode") == "mock_exam" else None,
        "student_attempt": {"provided": False},
        "turns": []
    }
    save_session(session_id, state)
    return state

def load_response(session_id: str) -> dict:
    r_file = get_session_dir(session_id) / "response.json"
    if not r_file.exists():
        return None
    with open(r_file, "r", encoding="utf-8") as f:
        return json.load(f)
        
def save_brief(session_id: str, brief_data: dict):

    tmp_path = str(get_session_dir(session_id) / "brief.json") + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(brief_data, f, indent=2)
    os.rename(tmp_path, get_session_dir(session_id) / "brief.json")

def save_verdict(session_id: str, verdict_data: dict):

    tmp_path = str(get_session_dir(session_id) / "verdict.json") + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(verdict_data, f, indent=2)
    os.rename(tmp_path, get_session_dir(session_id) / "verdict.json")

def load_verdict(session_id: str) -> dict:
    v_file = get_session_dir(session_id) / "verdict.json"
    if not v_file.exists():
        return None
    with open(v_file, "r", encoding="utf-8") as f:
        return json.load(f)
