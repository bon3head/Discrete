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
    
    # We only log metadata.
    # Ex: ## HH:MM — {chapter/section}
    # - task_type: ...
    
    now = datetime.now().strftime("%H:%M")
    
    # Extract metadata safely
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
