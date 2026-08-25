from .types import SessionRequest, SessionPlan
from .catalog import get_corpus_paths, resolve_reference, get_catalog_record
from .policy import get_max_hint_level, is_reference_solution_allowed
from .dispatcher import dispatch_claim

def build_session_plan(req: SessionRequest) -> SessionPlan:
    # 1. Validation
    if req.mode not in {"tutor", "mock_exam", "review"}:
        return SessionPlan(status="UNVERIFIABLE", reason_code="UNSUPPORTED_MODE")
        
    if req.task_type not in {"concept_help", "homework_hint", "student_attempt_check", "verification", "exam_prep"}:
        return SessionPlan(status="UNVERIFIABLE", reason_code="UNSUPPORTED_TASK")

    if not req.context:
        return SessionPlan(status="CLARIFICATION_REQUIRED", reason_code="MISSING_CONTEXT")
        
    chapter = req.context.get("chapter")
    section = req.context.get("section")
    
    if req.mode != "review" and chapter is None:
        return SessionPlan(status="CLARIFICATION_REQUIRED", reason_code="MISSING_CHAPTER")
        
    # 2. Reference Solution Policy
    ref_allowed = False
    ref_available = False
    if req.request_reference_solution:
        if not is_reference_solution_allowed(req):
            return SessionPlan(status="POLICY_BLOCKED", reason_code="REFERENCE_SOLUTION_PREATTEMPT_BLOCKED")
        ref_allowed = True
        
    # 3. Retrieval
    scope_class = "active_candidate"
    chapter_paths = []
    section_paths = []
    
    if ref_allowed:
        # For simplicity, resolve_reference currently returns reference content as a single list,
        # but our new catalog schema returns (scope_class, chapter_context_paths, section_paths).
        # We will just put the reference path in section_paths or a special context.
        ref_res = resolve_reference(ref_allowed)
        scope_class, chapter_paths, section_paths = ref_res[0], ref_res[1], ref_res[2]
        
        # Checking local availability for references:
        if not chapter_paths and not section_paths:
            return SessionPlan(
                status="UNVERIFIABLE", 
                reason_code="REFERENCE_SOLUTION_NOT_LOCALLY_AVAILABLE",
                policy={
                    "max_hint_level": get_max_hint_level(req),
                    "final_answer_reveal": False,
                    "reference_solution_allowed_by_policy": ref_allowed,
                    "reference_solution_available_locally": False,
                    "student_attempt_required_for_L4": True
                }
            )
        ref_available = True
        
    elif chapter is not None:
        if chapter > 8:
            return SessionPlan(status="POLICY_BLOCKED", reason_code="DEFERRED_CONTENT_BLOCKED")
            
        scope_class, chapter_paths, section_paths = get_corpus_paths(chapter, section)
        if scope_class in {"INVALID_SECTION_IDENTIFIER", "UNKNOWN_SECTION", "UNKNOWN_CHAPTER"}:
            return SessionPlan(status="CLARIFICATION_REQUIRED", reason_code=scope_class)
            
    # 4. Verification Dispatch
    verif_res = None
    if req.claim:
        verif_res = dispatch_claim(req.claim)
        if verif_res.get("reason_code") in {"ORCHESTRATION_DISPATCH_ERROR", "UNSUPPORTED_CLAIM_KIND"}:
            return SessionPlan(status="UNVERIFIABLE", reason_code="UNSUPPORTED_CLAIM")

    # 5. Policy Hint Level
    max_hint = get_max_hint_level(req)
    
    # 6. Assembly
    instructions = [
        "Cite every invoked definition/theorem with corpus path and section.",
        "Do not reveal a final answer.",
        "Use only content retrieved in this session plan.",
        "State UNVERIFIABLE explicitly if present."
    ]
    
    retrieval_data = {
        "scope_class": scope_class,
        "chapter": chapter,
        "chapter_context_paths": chapter_paths,
        "section_paths": section_paths,
        "section_count": len(section_paths),
        "chapter_context_count": len(chapter_paths),
        "citations_required": True
    }
    
    return SessionPlan(
        status="READY",
        reason_code="SESSION_READY",
        mode=req.mode,
        task_type=req.task_type,
        retrieval=retrieval_data,
        policy={
            "max_hint_level": max_hint,
            "final_answer_reveal": False,
            "reference_solution_allowed_by_policy": ref_allowed,
            "reference_solution_available_locally": ref_available,
            "student_attempt_required_for_L4": True
        },
        verification_result=verif_res,
        agent_instructions=instructions,
        logging={
            "log_required": True,
            "store_prompt_text": False,
            "store_student_attempt_text": False,
            "metadata_fields": [
                "timestamp", "chapter", "section", "task_type", 
                "hint_level", "verdict_counts", "struggle_flags"
            ]
        }
    )
