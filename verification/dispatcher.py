from .types import result
from .logic import verify_logic, verify_truth_table
from .sets import verify_set
from .counting import verify_count
from .matrices import verify_matrix
from .propositional_text import verify_propositional_text
from .recurrences import verify_recurrence
from .induction import verify_induction

def verify(claim):
    if not isinstance(claim,dict): return result({},'UNVERIFIABLE','CLAIM_NOT_OBJECT')
    try:
        kind=claim.get('kind')
        return {'logic_equivalence':verify_logic,'truth_table':verify_truth_table,'finite_set_expression':verify_set,'counting_identity':verify_count,'matrix_expression':verify_matrix,'propositional_text':verify_propositional_text, 'recurrence_substitution': verify_recurrence, 'induction_evidence': verify_induction}[kind](claim)
    except KeyError:
        return result(claim,'UNVERIFIABLE','UNSUPPORTED_CLAIM_KIND')
    except Exception as exc:
        return result(claim,'UNVERIFIABLE','DISPATCH_EXCEPTION',{},[f'{type(exc).__name__}: {exc}'])
