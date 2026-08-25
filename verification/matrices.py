from fractions import Fraction
from .types import result
def val(x):
    if isinstance(x,int): return Fraction(x)
    if isinstance(x,dict) and set(x)=={'numerator','denominator'} and isinstance(x['numerator'],int) and isinstance(x['denominator'],int) and x['denominator']!=0: return Fraction(x['numerator'],x['denominator'])
    raise ValueError('matrix entries must be integers or rational objects')

def dump_val(x):
    if isinstance(x, Fraction):
        if x.denominator == 1:
            return x.numerator
        return {'numerator': x.numerator, 'denominator': x.denominator}
    return x

def dump_mat(x):
    if not isinstance(x, list): return x
    return [[dump_val(v) for v in r] for r in x]

def mat(x):
    if not isinstance(x,list) or not x or not all(isinstance(r,list) and r for r in x): raise ValueError('invalid matrix')
    if len({len(r) for r in x})!=1: raise ValueError('ragged matrix')
    return [[val(v) for v in r] for r in x]
def add(a,b,sign=1): return [[a[i][j]+sign*b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def verify_matrix(claim):
    try:
        op=claim['operation']; a=mat(claim['lhs']); b=mat(claim['rhs'])
        if op in {'add','subtract'}:
            if len(a)!=len(b) or len(a[0])!=len(b[0]): return result(claim,'UNVERIFIABLE','MATRIX_INCOMPATIBLE_DIMENSIONS',{'lhs_shape':[len(a),len(a[0])],'rhs_shape':[len(b),len(b[0])] },['the requested addition/subtraction is undefined for these shapes'])
            actual=add(a,b,1 if op=='add' else -1)
        elif op=='multiply':
            if len(a[0])!=len(b): return result(claim,'UNVERIFIABLE','MATRIX_INCOMPATIBLE_DIMENSIONS',{'lhs_shape':[len(a),len(a[0])],'rhs_shape':[len(b),len(b[0])] },['the requested multiplication is undefined because inner dimensions differ'])
            actual=[[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
        elif op=='equal': actual=(a==b)
        else: raise ValueError('unsupported matrix operation')
        if 'claimed' not in claim: raise ValueError('claimed result required')
        claimed=claim['claimed']
        if op=='equal': claimed=bool(claimed)
        else: claimed=[[val(v) for v in row] for row in claimed]
        if actual!=claimed:
            mismatches=[]
            if op=='equal': mismatches=[{'actual':dump_mat(actual),'claimed':dump_mat(claimed)}]
            else:
                for i in range(max(len(actual),len(claimed))):
                    for j in range(max(len(actual[i]) if i<len(actual) else 0,len(claimed[i]) if i<len(claimed) else 0)):
                        av=actual[i][j] if i<len(actual) and j<len(actual[i]) else None; cv=claimed[i][j] if i<len(claimed) and j<len(claimed[i]) else None
                        if av!=cv: mismatches.append({'row':i,'column':j,'actual':dump_val(av),'claimed':dump_val(cv)})
            return result(claim,'FAIL','MATRIX_RESULT_MISMATCH',{'actual':dump_mat(actual),'claimed':dump_mat(claimed),'mismatches':mismatches,'operation':op})
        return result(claim,'PASS','MATRIX_EXACT_ARITHMETIC',{'value':dump_mat(actual),'operation':op})
    except (KeyError,ValueError,TypeError,IndexError) as e: return result(claim,'UNVERIFIABLE','MATRIX_INVALID_OR_INCOMPATIBLE',{},[str(e)])
