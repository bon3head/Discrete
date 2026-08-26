import os
from .types import SessionRequest
from .session_plan import build_session_plan
from .response_contract import AgentBrief, GuardResult

def prepare_agent_brief(req: SessionRequest):
    plan = build_session_plan(req)
    if plan.status != "READY":
        # Cannot proceed to load context
        return plan
        
    retrieval = plan.retrieval
    if not retrieval:
        return plan
        
    authorized_paths = retrieval.get("chapter_context_paths", []) + retrieval.get("section_paths", [])
    authorized_context = []
    
    for path in authorized_paths:
        if not os.path.isfile(path):
            return GuardResult(
                status="UNVERIFIABLE",
                reason_code="AUTHORIZED_CORPUS_PATH_NOT_AVAILABLE"
            )
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        authorized_context.append({
            "corpus_path": path,
            "content": content,
            "source_provenance": {"origin": "local_disk"}
        })
        
    constraints = {
        "max_hint_level": plan.policy.get("max_hint_level"),
        "final_answer_reveal": plan.policy.get("final_answer_reveal", False),
        "reference_solution_allowed": plan.policy.get("reference_solution_allowed_by_policy", False),
        "citations_required": retrieval.get("citations_required", True),
        "authorized_citation_paths": authorized_paths.copy()
    }
    
    return AgentBrief(
        session_plan=plan,
        authorized_context=authorized_context,
        verification_result=plan.verification_result,
        response_constraints=constraints,
        agent_instructions=plan.agent_instructions
    )
