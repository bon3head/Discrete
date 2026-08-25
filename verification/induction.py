from fractions import Fraction
from .types import result
from .exact_expr import eval_expr, eval_prop_full
from .matrices import dump_val

def verify_induction(claim):
    try:
        scope = claim["claim_scope"]
        if scope not in {"general", "finite"}:
            raise ValueError("claim_scope must be general or finite")
            
        index_var = claim["index_variable"]
        prop = claim["property"]
        base_indices = claim["base_indices"]
        transition = claim["transition"]
        check_domain = claim["check_domain"]
        start, end = check_domain["start"], check_domain["end"]
        if not isinstance(start, int) or not isinstance(end, int) or start > end:
            raise ValueError("Invalid check domain")
            
        trans_from = transition["from"]
        trans_to = transition["to"]
        
        limitations = []
        
        # Base cases
        for b in base_indices:
            res = eval_prop_full(prop, {index_var: b})
            if not res["result"]:
                return result(claim, "FAIL", "INDUCTION_BASE_CASE_FAIL", {
                    "base_index": b,
                    "lhs": dump_val(res["lhs"]),
                    "rhs": dump_val(res["rhs"])
                }, limitations)
                
        # Transitions and sampled properties
        for k in range(start, end + 1):
            p_k = eval_prop_full(prop, {index_var: k})
            
            if not p_k["result"]:
                return result(claim, "FAIL", "INDUCTION_PROPERTY_COUNTEREXAMPLE", {
                    "failing_index": k,
                    "evaluated_property": False,
                    "lhs": dump_val(p_k["lhs"]),
                    "rhs": dump_val(p_k["rhs"]),
                    "check_domain": check_domain,
                    "index_type": "base" if k in base_indices else "sampled"
                }, limitations)
                
            target_k_expr = eval_expr(trans_to, {trans_from: k})
            if target_k_expr.denominator != 1:
                raise ValueError("Transition target must be an integer")
            target_k = int(target_k_expr.numerator)
            
            if start <= target_k <= end:
                p_next = eval_prop_full(prop, {index_var: target_k})
                if not p_next["result"]:
                    return result(claim, "FAIL", "INDUCTION_TRANSITION_FAIL", {
                        "k": k,
                        "target_k": target_k,
                        "p_k": True,
                        "p_next": False,
                        "p_k_lhs": dump_val(p_k["lhs"]),
                        "p_k_rhs": dump_val(p_k["rhs"]),
                        "p_next_lhs": dump_val(p_next["lhs"]),
                        "p_next_rhs": dump_val(p_next["rhs"])
                    }, limitations)
                    
        # Success
        if scope == "finite":
            return result(claim, "PASS", "INDUCTION_EXHAUSTIVE_FINITE", {}, limitations)
        else:
            limitations.append("All sampled base/property/transition checks passed, but finite computation is evidence and not a proof of the universal induction claim.")
            return result(claim, "UNVERIFIABLE", "INDUCTION_FINITE_EVIDENCE_ONLY", {
                "checked_domain": {"start": start, "end": end}
            }, limitations)

    except ValueError as e:
        return result(claim, "UNVERIFIABLE", "EXACT_EXPR_UNSUPPORTED", {}, [str(e)])
    except Exception as e:
        return result(claim, "UNVERIFIABLE", "EXACT_EXPR_UNSUPPORTED", {}, [str(e)])
