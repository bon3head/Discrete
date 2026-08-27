import os
import sys
import multiprocessing
import sympy

def _sympy_worker(expr1_str: str, expr2_str: str, queue: multiprocessing.Queue):
    """
    Isolated worker that strictly prevents stdout stream corruption and 
    uses safe parsing to prevent Arbitrary Code Execution.
    """
    # CRITICAL: Redirect stdout to prevent MCP JSON-RPC corruption from stray prints
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
        # CRITICAL: Empty dictionaries prevent __builtins__ eval exploits
        e1 = sympy.parse_expr(expr1_str, evaluate=False, global_dict=safe_dict, local_dict={})
        e2 = sympy.parse_expr(expr2_str, evaluate=False, global_dict=safe_dict, local_dict={})
        
        is_equiv = sympy.simplify(e1 - e2) == 0
        queue.put({"status": "ok", "result": is_equiv})
    except Exception as e:
        queue.put({"status": "error", "error": f"Parse Error: {str(e)}"})
