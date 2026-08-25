from .propositional_parser import parse, ParseError
from .logic import verify_logic, verify_truth_table
from .types import result

def verify_propositional_text(claim):
    try:
        mode = claim.get("mode")
        if mode == "equivalence":
            if "lhs_text" not in claim or "rhs_text" not in claim:
                raise ValueError("Missing lhs_text or rhs_text")
            lhs_ast, vars_l = parse(claim["lhs_text"])
            rhs_ast, vars_r = parse(claim["rhs_text"])
            variables = sorted(list(vars_l | vars_r))
            
            inner_claim = {
                "kind": "logic_equivalence",
                "variables": variables,
                "lhs": lhs_ast,
                "rhs": rhs_ast,
                "source": claim.get("source", {})
            }
            res = verify_logic(inner_claim)
            res["kind"] = "propositional_text"
            
            if "evidence" not in res:
                res["evidence"] = {}
            res["evidence"]["lhs_text"] = claim["lhs_text"]
            res["evidence"]["rhs_text"] = claim["rhs_text"]
            return res
            
        elif mode == "property":
            if "expression_text" not in claim or "property" not in claim:
                raise ValueError("Missing expression_text or property")
            prop = claim["property"]
            if prop not in ["tautology", "contradiction"]:
                raise ValueError("Unsupported property")
                
            ast, vars_e = parse(claim["expression_text"])
            variables = sorted(list(vars_e))
            
            inner_claim = {
                "kind": "truth_table",
                "property": prop,
                "variables": variables,
                "expression": ast,
                "source": claim.get("source", {})
            }
            res = verify_truth_table(inner_claim)
            res["kind"] = "propositional_text"
            
            if "evidence" not in res:
                res["evidence"] = {}
            res["evidence"]["expression_text"] = claim["expression_text"]
            return res
            
        else:
            raise ValueError("Unsupported mode")
            
    except ParseError as e:
        return result(claim, "UNVERIFIABLE", "LOGIC_PARSE_ERROR", 
                      {"input": e.text, "offset": e.offset, "token": e.token, "message": e.message},
                      ["Input is outside the supported propositional-logic grammar."])
    except Exception as e:
        return result(claim, "UNVERIFIABLE", "LOGIC_PARSE_ERROR", 
                      {"message": str(e)}, 
                      ["Input is outside the supported propositional-logic grammar."])
