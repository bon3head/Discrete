import json, unittest
from pathlib import Path
from verification.dispatcher import verify

class RecurrenceTests(unittest.TestCase):
    def test_fixtures(self):
        claims = json.loads((Path(__file__).parent / "fixtures/recurrence_claims.json").read_text())
        expected = json.loads((Path(__file__).parent / "fixtures/recurrence_induction_expected.json").read_text())
        for c in claims:
            res = verify(c)
            ev = expected[c["claim_id"]]
            self.assertEqual(res["verdict"], ev["expected_verdict"], f"Failed on {c['claim_id']} verdict")
            self.assertEqual(res["reason_code"], ev["expected_reason_code"], f"Failed on {c['claim_id']} reason")
