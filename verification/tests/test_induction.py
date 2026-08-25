import json, unittest
from pathlib import Path
from verification.dispatcher import verify

class InductionTests(unittest.TestCase):
    def test_fixtures(self):
        claims = json.loads((Path(__file__).parent / "fixtures/induction_claims.json").read_text())
        expected = json.loads((Path(__file__).parent / "fixtures/recurrence_induction_expected.json").read_text())
        for c in claims:
            res = verify(c)
            ev = expected[c["claim_id"]]
            self.assertEqual(res["verdict"], ev["expected_verdict"], f"Failed on {c['claim_id']} verdict. Result: {res}")
            self.assertEqual(res["reason_code"], ev["expected_reason_code"], f"Failed on {c['claim_id']} reason")

    def test_source_provenance(self):
        claims = json.loads((Path(__file__).parent / "fixtures/induction_claims.json").read_text())
        claim = next(c for c in claims if c["claim_id"] == "ind-prov-source")
        res = verify(claim)
        self.assertEqual(res["source"], {"corpus_path": "foo.md"})
