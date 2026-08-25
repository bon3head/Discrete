import json, unittest
from pathlib import Path
from verification import verify
class MatrixTests(unittest.TestCase):
    def test_fixtures(self):
        claims=json.loads((Path(__file__).parent/'fixtures/matrix_claims.json').read_text())
        self.assertEqual([verify(c)['verdict'] for c in claims],['PASS','FAIL','UNVERIFIABLE'])
