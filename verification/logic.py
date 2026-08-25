from itertools import product
from .types import result

OPS={"not","and","or","xor","implies","iff"}
def eval_expr(expr, val, declared):
    if isinstance(expr,str):
        if expr not in declared: raise KeyError(expr)
        return bool(val[expr])
    if not isinstance(expr,dict) or expr.get("op") not in OPS: raise ValueError("unsupported logic AST")
    op=expr["op"]
    args=expr.get("args")
    if op=="not":
        if "arg" not in expr: raise ValueError("not requires arg")
        return not eval_expr(expr["arg"],val,declared)
    if not isinstance(args,list) or len(args)!=2: raise ValueError("binary op requires two args")
    a,b=eval_expr(args[0],val,declared),eval_expr(args[1],val,declared)
    return {"and":a and b,"or":a or b,"xor":a != b,"implies":(not a) or b,"iff":a==b}[op]

def verify_logic(claim):
    try:
        vars=claim["variables"]
        if not isinstance(vars,list) or len(set(vars))!=len(vars) or any(not isinstance(x,str) for x in vars): raise ValueError("invalid variables")
        rows=[]
        for bits in product([False,True], repeat=len(vars)):
            v=dict(zip(vars,bits)); l=eval_expr(claim["lhs"],v,set(vars)); r=eval_expr(claim["rhs"],v,set(vars)); rows.append({"valuation":v,"lhs":l,"rhs":r})
        bad=[x for x in rows if x["lhs"]!=x["rhs"]]
        if bad: return result(claim,"FAIL","LOGIC_COUNTEREXAMPLE",{"counterexample":bad[0],"rows":rows})
        return result(claim,"PASS","LOGIC_EXHAUSTIVE_EQUIVALENCE",{"rows":rows,"valuation_count":len(rows)})
    except (KeyError,ValueError,TypeError,KeyError) as e: return result(claim,"UNVERIFIABLE","LOGIC_MALFORMED_OR_UNDECLARED",{},[str(e)])

def verify_truth_table(claim):
    try:
        vars=claim["variables"]
        if not isinstance(vars,list) or len(set(vars))!=len(vars) or any(not isinstance(x,str) for x in vars): raise ValueError("invalid variables")
        rows=[]; vector=[]
        for bits in product([False,True],repeat=len(vars)):
            v=dict(zip(vars,bits))
            if claim.get("property")=="equivalence":
                left=eval_expr(claim["lhs"],v,set(vars)); right=eval_expr(claim["rhs"],v,set(vars)); value=left==right; rows.append({"valuation":v,"lhs":left,"rhs":right,"value":value})
            else:
                value=eval_expr(claim["expression"],v,set(vars)); rows.append({"valuation":v,"value":value})
            vector.append(value)
        if "expected_vector" in claim:
            exp=claim["expected_vector"]
            if not isinstance(exp,list) or len(exp)!=len(vector) or any(not isinstance(x,bool) for x in exp): raise ValueError("expected_vector must be a Boolean vector of matching length")
            mismatches=[{"row":i,"valuation":rows[i]["valuation"],"expected":exp[i],"actual":vector[i]} for i in range(len(vector)) if exp[i]!=vector[i]]
            if mismatches: return result(claim,"FAIL","TRUTH_VECTOR_MISMATCH",{"expected":exp,"actual":vector,"mismatches":mismatches,"rows":rows})
        elif claim.get("property") not in {"tautology","contradiction","equivalence"}: raise ValueError("missing/unsupported property")
        if claim.get("property")=="tautology" and not all(vector): return result(claim,"FAIL","NOT_TAUTOLOGY",{"rows":rows})
        if claim.get("property")=="contradiction" and any(vector): return result(claim,"FAIL","NOT_CONTRADICTION",{"rows":rows})
        return result(claim,"PASS","TRUTH_TABLE_EXHAUSTIVE",{"vector":vector,"rows":rows})
    except (KeyError,ValueError,TypeError) as e: return result(claim,"UNVERIFIABLE","TRUTH_TABLE_MALFORMED",{},[str(e)])
