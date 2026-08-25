import math
from .types import result
def verify_count(claim):
    try:
        op=claim["operation"]; args=claim["args"]; claimed=claim["claimed"]
        if not isinstance(args,list) or any(not isinstance(x,int) for x in args): raise ValueError("integer args required")
        if op=="factorial" and len(args)==1 and args[0]>=0: actual=math.factorial(args[0])
        elif op in {"permutation","combination","binomial"} and len(args)==2:
            n,k=args
            if n<0 or k<0 or k>n: raise ValueError("invalid n,k domain")
            actual=math.factorial(n)//math.factorial(n-k) if op=="permutation" else math.comb(n,k)
        else: raise ValueError("unsupported operation or arity")
        if actual!=claimed: return result(claim,"FAIL","COUNTING_RESULT_MISMATCH",{"expected":claimed,"actual":actual,"operation":op,"args":args})
        return result(claim,"PASS","COUNTING_EXACT_INTEGER",{"value":actual,"operation":op,"args":args})
    except (KeyError,ValueError,TypeError) as e: return result(claim,"UNVERIFIABLE","COUNTING_INVALID_DOMAIN_OR_SCHEMA",{},[str(e)])
