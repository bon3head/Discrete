from fractions import Fraction
from .types import result
from .exact_expr import eval_expr
from .matrices import dump_val

def verify_recurrence(claim):
    try:
        scope = claim["claim_scope"]
        if scope not in {"general", "finite"}:
            raise ValueError("claim_scope must be general or finite")
            
        seq_name = claim["sequence"]
        index_var = claim["index_variable"]
        init_vals = claim["initial_values"]
        check_domain = claim["check_domain"]
        start, end = check_domain["start"], check_domain["end"]
        if not isinstance(start, int) or not isinstance(end, int) or start > end:
            raise ValueError("Invalid check domain")
            
        candidate = claim["candidate"]
        recurrence = claim["recurrence"]
        valid_from = recurrence["valid_from"]
        rhs = recurrence["rhs"]
        
        # Build evaluator for sequences
        def seq_evaluator(s, idx):
            if s != seq_name:
                raise ValueError(f"Unknown sequence {s}")
            if scope == "finite":
                if not (start <= idx <= end):
                    raise ValueError(f"Sequence index {idx} out of finite domain [{start}, {end}]")
            return eval_expr(candidate, {index_var: idx})
        
        limitations = []
        
        for n in range(start, end + 1):
            n_str = str(n)
            # 1. Check initial values if n in init_vals
            if n_str in init_vals:
                expected_val = Fraction(init_vals[n_str])
                actual_val = eval_expr(candidate, {index_var: n})
                if expected_val != actual_val:
                    return result(claim, "FAIL", "RECURRENCE_INITIAL_VALUE_MISMATCH", {
                        "index": n,
                        "expected": dump_val(expected_val),
                        "actual": dump_val(actual_val)
                    }, limitations)
            
            # 2. Check recurrence if n >= valid_from
            if n >= valid_from:
                actual_val = eval_expr(candidate, {index_var: n})
                rhs_val = eval_expr(rhs, {index_var: n}, seq_evaluator)
                if actual_val != rhs_val:
                    return result(claim, "FAIL", "RECURRENCE_SUBSTITUTION_MISMATCH", {
                        "index": n,
                        "candidate_value": dump_val(actual_val),
                        "recurrence_value": dump_val(rhs_val)
                    }, limitations)
                    
        # Success
        if scope == "finite":
            return result(claim, "PASS", "RECURRENCE_EXHAUSTIVE_FINITE", {}, limitations)
        else:
            limitations.append("Finite checks over a domain are evidence, not a formal proof.")
            return result(claim, "UNVERIFIABLE", "RECURRENCE_FINITE_EVIDENCE_ONLY", {
                "checked_domain": {"start": start, "end": end}
            }, limitations)
            
    except ValueError as e:
        if "out of finite domain" in str(e) or "Invalid check domain" in str(e):
            return result(claim, "UNVERIFIABLE", "RECURRENCE_DOMAIN_ERROR", {}, [str(e)])
        return result(claim, "UNVERIFIABLE", "EXACT_EXPR_UNSUPPORTED", {}, [str(e)])
    except Exception as e:
        return result(claim, "UNVERIFIABLE", "EXACT_EXPR_UNSUPPORTED", {}, [str(e)])
