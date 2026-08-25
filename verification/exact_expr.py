from fractions import Fraction

def eval_expr(expr, context, seq_evaluator=None):
    if isinstance(expr, int):
        return Fraction(expr)
    if isinstance(expr, dict):
        if "rational" in expr:
            rat = expr["rational"]
            num = rat.get("numerator")
            den = rat.get("denominator")
            if not isinstance(num, int) or not isinstance(den, int) or den == 0:
                raise ValueError("Invalid rational definition")
            return Fraction(num, den)
        if "var" in expr:
            v = expr["var"]
            if v not in context:
                raise ValueError(f"Unknown variable {v}")
            return Fraction(context[v])
        if "seq" in expr:
            if not seq_evaluator:
                raise ValueError("Sequence references are not supported in this context")
            seq_name = expr["seq"]
            if "at" not in expr:
                raise ValueError("Sequence reference missing 'at' index")
            at_val = eval_expr(expr["at"], context, seq_evaluator)
            if at_val.denominator != 1:
                raise ValueError("Sequence index must be an integer")
            return seq_evaluator(seq_name, int(at_val.numerator))
        if "op" in expr:
            op = expr["op"]
            if op == "add":
                res = Fraction(0)
                for a in expr.get("args", []):
                    res += eval_expr(a, context, seq_evaluator)
                return res
            if op == "sub":
                args = expr.get("args", [])
                if len(args) != 2:
                    raise ValueError("sub operator requires exactly 2 args")
                return eval_expr(args[0], context, seq_evaluator) - eval_expr(args[1], context, seq_evaluator)
            if op == "mul":
                res = Fraction(1)
                for a in expr.get("args", []):
                    res *= eval_expr(a, context, seq_evaluator)
                return res
            if op == "neg":
                return -eval_expr(expr.get("arg"), context, seq_evaluator)
            if op == "pow":
                base = eval_expr(expr.get("base"), context, seq_evaluator)
                exp_expr = expr.get("exponent")
                # Exponent must be a non-negative integer literal
                if not isinstance(exp_expr, int) and (not isinstance(exp_expr, dict) or "var" not in exp_expr):
                     # Allow var exponent for induction claims like 2^n
                     pass
                exp = eval_expr(exp_expr, context, seq_evaluator)
                if exp.denominator != 1 or exp < 0:
                     raise ValueError("pow exponent must evaluate to a non-negative integer")
                return base ** int(exp.numerator)
    raise ValueError(f"Unsupported AST node or type: {expr}")

def eval_prop_full(prop, context, seq_evaluator=None):
    op = prop.get("op")
    if op not in {"eq", "ne", "lt", "le", "gt", "ge"}:
        raise ValueError(f"Unsupported comparison operator: {op}")
    lhs = eval_expr(prop.get("lhs"), context, seq_evaluator)
    rhs = eval_expr(prop.get("rhs"), context, seq_evaluator)
    
    if op == "eq": result = (lhs == rhs)
    elif op == "ne": result = (lhs != rhs)
    elif op == "lt": result = (lhs < rhs)
    elif op == "le": result = (lhs <= rhs)
    elif op == "gt": result = (lhs > rhs)
    elif op == "ge": result = (lhs >= rhs)
    
    return {"result": result, "lhs": lhs, "rhs": rhs}
