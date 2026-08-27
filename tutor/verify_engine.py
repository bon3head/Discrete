import os
import sys
import sympy

def _sympy_worker(expr1_str, expr2_str, queue):
    # CRITICAL: explicit redirect to prevent JSON-RPC stream corruption
    sys.stdout = open(os.devnull, 'w')
    
    # Safe dictionary to allow basic sympy operations while preventing ACE
    safe_dict = {
        "__builtins__": {},
        "Add": sympy.Add,
        "Mul": sympy.Mul,
        "Symbol": sympy.Symbol,
        "Integer": sympy.Integer,
        "Pow": sympy.Pow,
        "Rational": sympy.Rational,
        "Float": sympy.Float,
    }
    
    try:
        # CRITICAL: explicit global_dict and local_dict to prevent Arbitrary Code Execution (ACE)
        expr1 = sympy.parse_expr(expr1_str, evaluate=False, global_dict=safe_dict, local_dict={})
        expr2 = sympy.parse_expr(expr2_str, evaluate=False, global_dict=safe_dict, local_dict={})
        
        diff = sympy.simplify(expr1 - expr2)
        queue.put(bool(diff == 0))
    except Exception:
        queue.put(False)
