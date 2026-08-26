import re
from .response_contract import AgentBrief, TutorResponse, GuardResult

def validate_response(brief: AgentBrief, resp: TutorResponse) -> GuardResult:
    cons = brief.response_constraints
    plan = brief.session_plan
    
    # 1. Hint Level
    levels = {"L0": 0, "L1": 1, "L2": 2, "L3": 3, "L4": 4}
    used_level = levels.get(resp.hint_level_used, 3)
    max_level = levels.get(cons.get("max_hint_level", "L3"), 3)
    
    if used_level > max_level:
        if plan.mode == "mock_exam" and max_level == 0:
            return GuardResult("POLICY_BLOCKED", "MOCK_EXAM_HINT_FORBIDDEN")
        return GuardResult("POLICY_BLOCKED", "HINT_LEVEL_EXCEEDS_AUTHORIZATION")
        
    # 2. Final Answer Policy
    if resp.final_answer_reveal:
        return GuardResult("POLICY_BLOCKED", "FINAL_ANSWER_REVEAL_FORBIDDEN")
        
    lower_body = resp.body.lower()
    leak_patterns = [
        r"\\boxed\{",
        r"the answer is",
        r"final answer",
        r"therefore the answer",
        r"solution:"
    ]
    for pat in leak_patterns:
        if re.search(pat, lower_body):
            return GuardResult("REVIEW_REQUIRED", "POSSIBLE_ANSWER_LEAK")
            
    # 3. Reference Solution
    ref_allowed = cons.get("reference_solution_allowed", False)
    if not ref_allowed:
        if "reference_solution" in resp.body:
            return GuardResult("POLICY_BLOCKED", "REFERENCE_SOLUTION_LEAK")
        for cit in resp.citations:
            if "reference_solution" in cit.corpus_path:
                return GuardResult("POLICY_BLOCKED", "REFERENCE_SOLUTION_LEAK")
                
    # 4. Citation Integrity
    authorized_paths = set(cons.get("authorized_citation_paths", []))
    for cit in resp.citations:
        if cit.corpus_path not in authorized_paths:
            return GuardResult("POLICY_BLOCKED", "UNAUTHORIZED_CORPUS_CITATION")
            
    if cons.get("citations_required", False) and not resp.citations:
        return GuardResult("REVIEW_REQUIRED", "REQUIRED_CITATION_MISSING")
        
    # 5. Verification Footer Integrity
    expected_vr = brief.verification_result
    footer = resp.verification_footer
    
    if expected_vr:
        if not footer:
            return GuardResult("POLICY_BLOCKED", "VERIFIER_RESULT_ALTERED")
        if footer.verdict != expected_vr.get("verdict") or footer.reason_code != expected_vr.get("reason_code"):
            return GuardResult("POLICY_BLOCKED", "VERIFIER_RESULT_ALTERED")
    else:
        if footer and (footer.verdict is not None or footer.reason_code is not None):
            return GuardResult("POLICY_BLOCKED", "VERIFIER_RESULT_ALTERED")
            
    # 6. Next Step
    if not resp.next_step or not resp.next_step.strip():
        return GuardResult("REVIEW_REQUIRED", "NEXT_STEP_INVALID")
        
    if re.search(r"^\s*1\.\s+", resp.next_step, re.MULTILINE) or re.search(r"^\s*-\s+", resp.next_step, re.MULTILINE):
        # looks like a list
        return GuardResult("REVIEW_REQUIRED", "NEXT_STEP_INVALID")
        
    return GuardResult("PASS", "RESPONSE_VALID")
