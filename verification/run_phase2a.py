import json, unittest
from pathlib import Path
from . import verify

ROOT=Path(__file__).parent
FIX=ROOT/'tests'/'fixtures'
def claims():
    out=[]
    for p in sorted(FIX.glob('*.json')):
        out.extend(json.loads(p.read_text()))
    return out
def main():
    fixtures=claims(); rows=[]
    expected={'logic-pass-001':'PASS','logic-fail-001':'FAIL','logic-unverifiable-001':'UNVERIFIABLE','truth-pass-tautology':'PASS','truth-pass-contradiction':'PASS','truth-pass-equivalence':'PASS','truth-fail-vector':'FAIL','set-pass-001':'PASS','set-pass-002':'PASS','set-fail-001':'FAIL','set-unverifiable-001':'UNVERIFIABLE','count-pass-001':'PASS','count-pass-002':'PASS','count-fail-001':'FAIL','count-unverifiable-001':'UNVERIFIABLE','matrix-pass-001':'PASS','matrix-fail-001':'FAIL','matrix-unverifiable-001':'UNVERIFIABLE'}
    for claim in fixtures:
        r=verify(claim); rows.append({'fixture_id':claim['claim_id'],'expected_verdict':expected[claim['claim_id']],'actual_verdict':r['verdict'],'assertion_passed':r['verdict']==expected[claim['claim_id']],'result':r})
    adversarial=[('malformed',None,'UNVERIFIABLE'),('unsupported_kind',{'claim_id':'adv-kind','kind':'proof','text':'x'},'UNVERIFIABLE'),('undeclared_variable',{'claim_id':'adv-var','kind':'logic_equivalence','variables':['p'],'lhs':'q','rhs':'p'},'UNVERIFIABLE'),('missing_universe',{'claim_id':'adv-universe','kind':'finite_set_expression','sets':{'A':[1]},'lhs':'A','rhs':'A'},'UNVERIFIABLE'),('matrix_shape',{'claim_id':'adv-shape','kind':'matrix_expression','operation':'multiply','lhs':[[1,2]],'rhs':[[1,2]],'claimed':[[1]]},'UNVERIFIABLE'),('infinite_set',{'claim_id':'adv-infinite','kind':'finite_set_expression','universe':'integers','sets':{},'lhs':'A','rhs':'A'},'UNVERIFIABLE')]
    adv=[]
    for name,claim,exp in adversarial:
        r=verify(claim); adv.append({'case':name,'expected_verdict':exp,'actual_verdict':r['verdict'],'assertion_passed':r['verdict']==exp,'result':r})
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests')); run=unittest.TextTestRunner(stream=open('/tmp/phase2a-unittest.log','w'),verbosity=0).run(suite)
    report={'fixture_results':rows,'adversarial_results':adv,'test_summary':{'fixture_total':len(rows),'fixture_assertions_passed':sum(x['assertion_passed'] for x in rows),'adversarial_total':len(adv),'adversarial_assertions_passed':sum(x['assertion_passed'] for x in adv),'total_assertions':len(rows)+len(adv),'total_assertions_passed':sum(x['assertion_passed'] for x in rows+adv),'unittest_run':run.testsRun,'unittest_failures':len(run.failures),'unittest_errors':len(run.errors),'all_assertions_passed':all(x['assertion_passed'] for x in rows+adv) and not run.failures and not run.errors}}
    (ROOT/'reports/phase2a_test_report.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
    print(json.dumps(report['test_summary'],indent=2))
if __name__=='__main__': main()
