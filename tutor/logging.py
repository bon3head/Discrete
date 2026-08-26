import json
import os
from datetime import datetime
from pathlib import Path
from .types import SessionPlan

def log_session(plan: SessionPlan, log_dir: str = "runtime/session_logs"):
    if not plan.logging or not plan.logging.get("log_required"):
        return
        
    os.makedirs(log_dir, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = Path(log_dir) / f"{today}.md"
    
    now = datetime.now().strftime("%H:%M")
    
    entry = f"## {now} — Orchestration\n"
    entry += f"- mode: {plan.mode}\n"
    entry += f"- task_type: {plan.task_type}\n"
    
    if plan.policy:
        entry += f"- hint_level_authorized: {plan.policy.get('max_hint_level')}\n"
        entry += f"- reference_solution_accessed: {plan.policy.get('reference_solution_allowed')}\n"
        
    if plan.verification_result:
        entry += f"- verification_verdict: {plan.verification_result.get('verdict')}\n"
        entry += f"- reason_code: {plan.verification_result.get('reason_code')}\n"
    else:
        entry += f"- reason_code: {plan.reason_code}\n"
        
    entry += "- struggle_flags: []\n\n"
    
    with open(log_file, "a") as f:
        f.write(entry)

def log_execution(req_id: str, chapter: int, section: str, plan, resp_obj, guard_res, log_dir: str = "runtime/session_logs"):
    if os.environ.get("TEST_RUN"):
        return
        
    os.makedirs(log_dir, exist_ok=True)
    log_file = Path(log_dir) / f"{datetime.now().strftime('%Y-%m-%d')}.md"
    
    entry = f"## {datetime.now().strftime('%H:%M')} — Executor\n"
    entry += f"- request_id: {req_id}\n"
    entry += f"- mode: {plan.mode}\n"
    entry += f"- task_type: {plan.task_type}\n"
    entry += f"- chapter: {chapter}\n"
    entry += f"- section: {section}\n"
    entry += f"- plan_status: {plan.status}\n"
    entry += f"- hint_level_authorized: {plan.policy.get('max_hint_level')}\n"
    entry += f"- hint_level_used: {resp_obj.hint_level_used}\n"
    entry += f"- guard_status: {guard_res.status}\n"
    entry += f"- guard_reason_code: {guard_res.reason_code}\n"
    if plan.verification_result:
        entry += f"- verification_verdict: {plan.verification_result.get('verdict')}\n"
    entry += f"- reference_solution_allowed: {plan.policy.get('reference_solution_allowed_by_policy', False)}\n"
    entry += f"- reference_solution_available_locally: {plan.policy.get('reference_solution_available_locally', False)}\n"
    entry += "- struggle_flags: []\n\n"
    
    with open(log_file, "a") as f:
        f.write(entry)
