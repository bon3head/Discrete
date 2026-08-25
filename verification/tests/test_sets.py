import json, unittest
from pathlib import Path
from verification import verify
class SetTests(unittest.TestCase):
    def test_fixtures(self):
        claims=json.loads((Path(__file__).parent/'fixtures/set_claims.json').read_text())
        self.assertEqual([verify(c)['verdict'] for c in claims],['PASS','PASS','FAIL','UNVERIFIABLE'])

    def test_missing_universe(self):
        # A claim that would pass if universe wasn't required
        claim = {
            'kind': 'finite_set_expression',
            'sets': {'A': []},
            'lhs': {'op': 'complement', 'arg': 'A'},
            'rhs': []
        }
        res = verify(claim)
        self.assertEqual(res['verdict'], 'UNVERIFIABLE')
        self.assertEqual(res['reason_code'], 'SET_MALFORMED_OR_MISSING_UNIVERSE')
