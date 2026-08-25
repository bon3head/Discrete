import json, unittest
from pathlib import Path
from verification.dispatcher import verify

class PropositionalTextTests(unittest.TestCase):
    def test_fixtures(self):
        claims = json.loads((Path(__file__).parent / "fixtures/propositional_text_claims.json").read_text())
        expected = json.loads((Path(__file__).parent / "fixtures/propositional_text_expected.json").read_text())
        
        for c in claims:
            res = verify(c)
            ev = expected[c["claim_id"]]
            self.assertEqual(res["verdict"], ev["expected_verdict"], f"Failed on {c['claim_id']} verdict")
            self.assertEqual(res["reason_code"], ev["expected_reason_code"], f"Failed on {c['claim_id']} reason")
            if "required_evidence" in ev:
                self.assertIn("evidence", res)
                for req in ev["required_evidence"]:
                    self.assertIn(req, res["evidence"])

    def test_source_provenance_equivalence(self):
        claim = {
            "kind": "propositional_text",
            "mode": "equivalence",
            "lhs_text": "p -> q",
            "rhs_text": "~p | q",
            "source": {"corpus_path": "test/path.md"}
        }
        res = verify(claim)
        self.assertEqual(res["source"], {"corpus_path": "test/path.md"})

    def test_source_provenance_property(self):
        claim = {
            "kind": "propositional_text",
            "mode": "property",
            "property": "tautology",
            "expression_text": "p | ~p",
            "source": {"corpus_path": "test/prop.md"}
        }
        res = verify(claim)
        self.assertEqual(res["source"], {"corpus_path": "test/prop.md"})
