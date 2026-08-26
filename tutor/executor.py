import json
from datetime import datetime
from pathlib import Path
import os
from .types import SessionRequest
from .agent_brief import prepare_agent_brief
from .response_contract import TutorResponse, GuardResult, ResponseCitation, VerificationFooter
from .response_guard import validate_response

def execute_session(req: SessionRequest, candidate_response: dict) -> GuardResult:
    # 1. Generate Brief
    brief_or_plan = prepare_agent_brief(req)
    if hasattr(brief_or_plan, "status") and brief_or_plan.status != "READY":
        # It's a SessionPlan or GuardResult indicating a failure to load
        if hasattr(brief_or_plan, "reason_code"):
            return GuardResult(brief_or_plan.status, brief_or_plan.reason_code)
        return GuardResult("UNVERIFIABLE", "PLAN_NOT_READY")
        
    brief = brief_or_plan
    
    # 2. Validate Response
    cits = [ResponseCitation(**c) for c in candidate_response.get("citations", [])]
    ft_dict = candidate_response.get("verification_footer")
    footer = VerificationFooter(**ft_dict) if ft_dict else None
    
    resp_obj = TutorResponse(
        hint_level_used=candidate_response.get("hint_level_used", "L3"),
        response_type=candidate_response.get("response_type", "hint"),
        body=candidate_response.get("body", ""),
        citations=cits,
        verification_footer=footer,
        next_step=candidate_response.get("next_step", ""),
        final_answer_reveal=candidate_response.get("final_answer_reveal", False)
    )
    
    guard_res = validate_response(brief, resp_obj)
    


    # 3. Log
    from .logging import log_execution
    plan = brief.session_plan
    chapter = req.context.get('chapter') if req.context else None
    section = req.context.get('section') if req.context else None
    log_execution(req.request_id, chapter, section, plan, resp_obj, guard_res)
    
    return guard_res
