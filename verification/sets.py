from .types import result

OPS={"union","intersection","difference","symmetric_difference","complement"}
def ev(expr,sets,universe):
    if isinstance(expr,list): return set(expr)
    if isinstance(expr,str):
        if expr not in sets: raise KeyError(expr)
        return set(sets[expr])
    if not isinstance(expr,dict) or expr.get("op") not in OPS: raise ValueError("unsupported set AST")
    op=expr["op"]
    if op=="complement": return set(universe)-ev(expr.get("arg"),sets,universe)
    args=expr.get("args")
    if not isinstance(args,list) or len(args)!=2: raise ValueError("binary set op requires two args")
    a,b=ev(args[0],sets,universe),ev(args[1],sets,universe)
    return {"union":a|b,"intersection":a&b,"difference":a-b,"symmetric_difference":a^b}[op]
def verify_set(claim):
    try:
        u=claim["universe"]
        if not isinstance(u,list) or len(set(map(repr,u)))!=len(u): raise ValueError("invalid finite universe")
        sets=claim["sets"]
        if not isinstance(sets,dict) or any(not set(v)<=set(u) for v in sets.values()): raise ValueError("set outside universe")
        l,r=ev(claim["lhs"],sets,u),ev(claim["rhs"],sets,u)
        if l!=r: return result(claim,"FAIL","SET_COUNTEREXAMPLE",{"lhs":sorted(l,key=repr),"rhs":sorted(r,key=repr),"symmetric_difference":sorted(l^r,key=repr),"universe":u})
        return result(claim,"PASS","FINITE_SET_EXHAUSTIVE",{"value":sorted(l,key=repr),"universe":u})
    except (KeyError,ValueError,TypeError) as e: return result(claim,"UNVERIFIABLE","SET_MALFORMED_OR_MISSING_UNIVERSE",{},[str(e)])
