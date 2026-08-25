from .types import SessionRequest

def get_max_hint_level(req: SessionRequest) -> str:
    if req.mode == "mock_exam":
        if req.student_attempt.get("provided"):
            return "L4"
        return "L0"
        
    if req.mode == "review":
        return "L3"
        
    # mode == tutor
    if req.task_type == "concept_help":
        return "L3"
    if req.task_type == "homework_hint":
        if req.student_attempt.get("provided"):
            return "L4"
        return "L3"
    if req.task_type == "student_attempt_check":
        return "L4"
    if req.task_type == "verification":
        if req.student_attempt.get("provided"):
            return "L4"
        return "L3"
        
    return "L3"

def is_reference_solution_allowed(req: SessionRequest) -> bool:
    if not req.request_reference_solution:
        return False
        
    attempt_provided = req.student_attempt.get("provided", False)
    if req.mode == "mock_exam" and attempt_provided:
        return True
    if req.task_type == "student_attempt_check" and attempt_provided:
        return True
        
    return False
