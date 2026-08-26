import argparse
import sys
import json
import os
import sys
import glob
from pathlib import Path
from datetime import datetime

def set_latest_session(session_id):
    with open("runtime/latest", "w") as f:
        f.write(session_id)

def get_latest_session():
    try:
        with open("runtime/latest", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

import os
from .session_store import create_session, load_session, save_session, save_brief, load_response, save_verdict, load_verdict, SESSIONS_DIR
from .response_io import load_and_validate_response
from .types import SessionRequest
from .executor import execute_session
from .agent_brief import prepare_agent_brief
from .response_contract import GuardResult
from .session_plan import build_session_plan

def new_command(args):
    if getattr(args, "target", None):
        parts = args.target.split(".")
        try:
            args.chapter = int(parts[0])
            if len(parts) > 1:
                args.section = args.target
        except ValueError:
            print("Error: Malformed positional target. Must be CHAPTER[.SECTION].")
            sys.exit(1)
            
    if getattr(args, "hint_pos", None):
        args.hint = args.hint_pos

    if hasattr(args, "id") and args.id:
        session_id = args.id
        try:
            session = load_session(session_id)
        except FileNotFoundError:
            print(f"Error: Session {session_id} not found.")
            sys.exit(1)
    else:
        session = create_session({
            "mode": args.mode
        })
        session_id = session["id"]
    
    context = {"chapter": args.chapter}
    if args.section:
        context["section"] = args.section
        
    turn_index = len(session.get("turns", []))
    req = SessionRequest(
        request_id=f"{session_id}-turn{turn_index}",
        mode=args.mode,
        task_type=args.task,
        context=context,
        student_attempt=session["student_attempt"],
        request_reference_solution=args.ref
    )
    
    plan = build_session_plan(req)
    session["turns"].append({
        "request": req.__dict__,
        "requested_hint_level": args.hint
    })
    
    if plan.status != "READY":
        session["state"] = "BLOCKED"
        save_session(session_id, session)
        set_latest_session(session_id)
        print(f"Session {session_id} created in BLOCKED state: {plan.status} / {plan.reason_code}")
        return
        
    session["state"] = "PLANNED"
    save_session(session_id, session)

    brief = prepare_agent_brief(req)
    if hasattr(brief, "status") and brief.status != "READY":
        session["state"] = "BLOCKED"
        save_session(session_id, session)
        set_latest_session(session_id)
        print(f"Session {session_id} blocked during brief prep: {brief.status} / {brief.reason_code}")
        return
        
    brief_dict = {
        "session_plan": brief.session_plan.__dict__,
        "authorized_context": brief.authorized_context,
        "verification_result": brief.verification_result,
        "response_constraints": brief.response_constraints,
        "agent_instructions": brief.agent_instructions,
        "response_instructions": {
            "schema_path": "planning/phase3/response-schema.json",
            "authorized_hint_level": args.hint or brief.response_constraints.get("max_hint_level"),
            "citation_format": "[ADS §X.Y — corpus_path]",
            "final_answer_reveal": False,
            "next_step": "exactly one",
            "verifier_footer_rule": "copy verdict/reason_code verbatim when present, null when absent"
        }
    }
    
    save_brief(session_id, brief_dict)
    session["state"] = "BRIEFED"
    save_session(session_id, session)
    set_latest_session(session_id)
    print(f"Session {session_id} created. Brief written.")

def validate_command(args):
    session_id = getattr(args, "id", None) or get_latest_session()
    if not session_id:
        print("Error: No session ID provided and no latest session found.")
        sys.exit(1)

    try:
        session = load_session(session_id)
    except FileNotFoundError:
        print(f"Error: Session {session_id} not found.")
        sys.exit(1)
        
    try:
        resp_dict = load_response(session_id)
    except json.JSONDecodeError as e:
        print(f"Error: response.json is malformed JSON. {e}")
        sys.exit(1)

    if not resp_dict:
        print(f"Error: No response.json found in session {session_id}")
        sys.exit(1)
        
    session["state"] = "RESPONSE_PRESENT"
    save_session(session_id, session)
    
    schema_res = load_and_validate_response(resp_dict)
    if schema_res.status != "PASS":
        verdict = schema_res
        session["state"] = "REVIEW_REQUIRED"
    else:
        # Proceed to Guard
        req_dict = session["turns"][-1]["request"]
        req = SessionRequest(**req_dict)
        verdict = execute_session(req, resp_dict)
        session["state"] = "VALIDATED" if verdict.status == "PASS" else verdict.status
        
    save_verdict(session_id, verdict.__dict__)
    save_session(session_id, session)
    
    set_latest_session(session_id)
    print(f"Validation complete: {verdict.status} / {verdict.reason_code}")
    if verdict.evidence:
        print(f"Evidence: {verdict.evidence}")

def show_command(args):
    session_id = getattr(args, "id", None) or get_latest_session()
    if not session_id:
        print("Error: No session ID provided and no latest session found.")
        sys.exit(1)
        
    set_latest_session(session_id)
        
    verdict = load_verdict(session_id)
    if not verdict:
        # Auto-validate if verdict is missing
        print(f"Auto-validating session {session_id}...")
        
        # We need to temporarily set args.id to session_id in case it was None
        args.id = session_id
        validate_command(args)
        verdict = load_verdict(session_id)

        
    if verdict["status"] != "PASS":
        print(f"Cannot show response. Verdict is {verdict['status']}: {verdict['reason_code']}")
        sys.exit(1)
        
    try:
        resp_dict = load_response(session_id)
    except json.JSONDecodeError as e:
        print(f"Error: response.json is malformed JSON. {e}")
        sys.exit(1)

    if not resp_dict:
        print(f"Error: No response.json found in session {session_id}")
        sys.exit(1)
    session = load_session(session_id)
    session["state"] = "SHOWN"
    save_session(session_id, session)
    
    print(resp_dict.get("body", ""))

def submit_attempt_command(args):
    session_id = getattr(args, "id", None) or get_latest_session()
    if not session_id:
        print("Error: No session ID provided and no latest session found.")
        sys.exit(1)

    try:
        session = load_session(session_id)
    except FileNotFoundError:
        print(f"Error: Session {session_id} not found.")
        sys.exit(1)
        
    session["student_attempt"]["provided"] = True
    if args.path:
        session["student_attempt"]["path"] = args.path
        
    if session.get("exam_phase") == "in_progress":
        session["exam_phase"] = "submitted"
        
    req_dict = session["turns"][-1]["request"]
    req_dict["student_attempt"] = session["student_attempt"]
    
    req = SessionRequest(**req_dict)
    
    # re-plan
    plan = build_session_plan(req)
    
    if plan.status != "READY":
        session["state"] = "BLOCKED"
        save_session(session_id, session)
        print(f"Session {session_id} blocked during re-plan: {plan.status}")
        return
        
    session["state"] = "PLANNED"
    save_session(session_id, session)

    brief = prepare_agent_brief(req)
    brief_dict = {
        "session_plan": brief.session_plan.__dict__,
        "authorized_context": brief.authorized_context,
        "verification_result": brief.verification_result,
        "response_constraints": brief.response_constraints,
        "agent_instructions": brief.agent_instructions,
        "response_instructions": {
            "schema_path": "planning/phase3/response-schema.json",
            "authorized_hint_level": brief.response_constraints.get("max_hint_level"),
            "citation_format": "[ADS §X.Y — corpus_path]",
            "final_answer_reveal": False,
            "next_step": "exactly one",
            "verifier_footer_rule": "copy verdict/reason_code verbatim when present, null when absent"
        }
    }
    
    save_brief(session_id, brief_dict)
    session["state"] = "BRIEFED"
    session["turns"][-1]["request"] = req_dict
    save_session(session_id, session)
    set_latest_session(session_id)
    print(f"Attempt submitted for session {session_id}. Re-planned.")

def list_command(args):
    sessions_path = Path("runtime/sessions")
    if not sessions_path.exists():
        print("No sessions yet.")
        return
        
    session_dirs = [d for d in sessions_path.iterdir() if d.is_dir()]
    if not session_dirs:
        print("No sessions yet.")
        return
        
    session_dirs.sort(key=lambda d: d.stat().st_mtime, reverse=True)
    session_dirs = session_dirs[:10]
    
    for d in session_dirs:
        sid = d.name
        try:
            s = load_session(sid)
            turns = len(s.get("turns", []))
            max_hint = s.get("turns", [{}])[-1].get("requested_hint_level") if turns > 0 else "None"
            ctx = s.get("turns", [{}])[0].get("request", {}).get("context", {}) if turns > 0 else {}
            chap = ctx.get("chapter", "?")
            sec = ctx.get("section", "")
            if sec:
                chap_sec = sec
            else:
                chap_sec = str(chap)
            state = s.get("state", "UNKNOWN")
            print(f"{sid[:8]} | {chap_sec:<5} | {state:<15} | Turns: {turns} | Max Hint: {max_hint}")
        except Exception:
            print(f"{sid[:8]} | Error loading session data")

def doctor_command(args):
    import subprocess
    smoke_proc = subprocess.run([sys.executable, "-m", "tutor.cli", "smoke"])
    hashes_proc = subprocess.run([sys.executable, "planning/phase0/verify_source_hashes.py"])
    corpus_proc = subprocess.run([sys.executable, "tools/verify_corpus_baseline.py"])
    
    if smoke_proc.returncode == 0 and hashes_proc.returncode == 0 and corpus_proc.returncode == 0:
        sys.exit(0)
    else:
        sys.exit(1)

def smoke_command(args):
    # Tests the 3 permanent smoke scenarios
    print("Running smoke tests...")
    
    from tutor.tests.test_cli import run_smoke_tests
    success = run_smoke_tests()
    if not success:
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(prog="tutor.cli")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    new_p = subparsers.add_parser("new")
    new_p.add_argument("target", nargs="?", type=str)
    new_p.add_argument("hint_pos", nargs="?", type=str)
    new_p.add_argument("--id", type=str)
    new_p.add_argument("--chapter", type=int)
    new_p.add_argument("--section", type=str)
    new_p.add_argument("--task", type=str, default="homework_hint")
    new_p.add_argument("--hint", type=str, default="L1")
    new_p.add_argument("--mode", type=str, default="tutor")
    new_p.add_argument("--ref", action="store_true")
    new_p.set_defaults(func=new_command)
    
    exam_p = subparsers.add_parser("exam")
    exam_p.add_argument("chapter", type=int)
    exam_p.set_defaults(func=lambda args: new_command(argparse.Namespace(
        command="exam", target=None, hint_pos=None, id=None,
        chapter=args.chapter, section=None, task="homework_hint",
        hint=None, mode="mock_exam", ref=False)))
    
    val_p = subparsers.add_parser("validate")
    val_p.add_argument("id", nargs="?")
    val_p.set_defaults(func=validate_command)
    
    show_p = subparsers.add_parser("show")
    show_p.add_argument("id", nargs="?")
    show_p.set_defaults(func=show_command)
    
    sub_p = subparsers.add_parser("submit-attempt")
    sub_p.add_argument("id", nargs="?")
    sub_p.add_argument("--path", type=str)
    sub_p.set_defaults(func=submit_attempt_command)
    
    att_p = subparsers.add_parser("attempt")
    att_p.add_argument("path", type=str)
    att_p.add_argument("--id", type=str, nargs="?")
    att_p.set_defaults(func=lambda args: submit_attempt_command(argparse.Namespace(
        id=getattr(args, "id", None), path=args.path, command="attempt")))
        
    list_p = subparsers.add_parser("list")
    list_p.set_defaults(func=list_command)
    
    doc_p = subparsers.add_parser("doctor")
    doc_p.set_defaults(func=doctor_command)
    
    smoke_p = subparsers.add_parser("smoke")
    smoke_p.set_defaults(func=smoke_command)
    
    args = parser.parse_args()
    
    # We need to compute session_id BEFORE we check it for locking
    session_id = getattr(args, "id", None)
    if not session_id and args.command in ["validate", "show", "submit-attempt", "attempt"]:
        session_id = get_latest_session()
        args.id = session_id

    if session_id:
        import os
        import sys
        from pathlib import Path
        
        # Platform support: require POSIX fcntl for session locking
        try:
            import fcntl
        except ImportError:
            print("Error: ADS-Tutor session locking requires a POSIX environment (Linux/WSL2). Windows is not natively supported.")
            sys.exit(1)
            
        s_dir = Path("runtime/sessions") / session_id
        
        # Directory pollution fix: only create dir if new_command, else require existence
        if args.func.__name__ != "new_command" and not s_dir.exists():
            print(f"Error: Session {session_id} not found.")
            sys.exit(1)
            
        s_dir.mkdir(parents=True, exist_ok=True)
        lock_file = s_dir / ".lock"
        with open(lock_file, "w") as lf:
            fcntl.flock(lf, fcntl.LOCK_EX)
            try:
                args.func(args)
            except json.JSONDecodeError as e:
                print(f"Error: A session file is corrupted (invalid JSON): {e}")
                sys.exit(1)
    else:
        try:
            args.func(args)
        except json.JSONDecodeError as e:
            print(f"Error: A session file is corrupted (invalid JSON): {e}")
            sys.exit(1)



if __name__ == "__main__":
    main()
