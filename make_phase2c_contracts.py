import json, os
from pathlib import Path

Path("planning/phase2").mkdir(parents=True, exist_ok=True)
Path("verification/tests/fixtures").mkdir(parents=True, exist_ok=True)

contract = """# Recurrence and Induction Contract

## Shared AST
- `Literal integer`: `7`
- `Explicit rational`: `{"rational": {"numerator": 3, "denominator": 5}}`
- `Variable`: `{"var": "n"}`
- `Sequence ref`: `{"seq": "a", "at": <expr>}`
- `Operators`: `add`, `sub`, `mul`, `neg`, `pow` (exponent non-negative integer literal).

## Verdict Semantics
- Finite claims that exhaustively pass checking over the domain yield `PASS`.
- General claims that pass over a sampled finite domain yield `UNVERIFIABLE` with `RECURRENCE_FINITE_EVIDENCE_ONLY` or `INDUCTION_FINITE_EVIDENCE_ONLY`.
- If any base case or transition or substitution fails, return `FAIL` with concrete counterexample.
- Out of bounds sequence lookups or unsupported features return `UNVERIFIABLE`.
- Transitions where P(k)=false add a limitation noting trivial implication but provide no evidence.
"""
with open("planning/phase2/recurrence-induction-contract.md", "w") as f: f.write(contract)

schema = {
    "recurrence_substitution": {
        "required": ["claim_scope", "sequence", "index_variable", "initial_values", "recurrence", "candidate", "check_domain"]
    },
    "induction_evidence": {
        "required": ["claim_scope", "index_variable", "property", "base_indices", "transition", "check_domain"]
    }
}
with open("planning/phase2/recurrence-induction-schema.json", "w") as f: json.dump(schema, f, indent=2)

decisions = """# Phase 2C Decisions
- Only exact arithmetic (integers and exact Fractions) is supported.
- `claim_scope: "finite"` strictly ensures all sequence accesses fall within `check_domain`.
- Trivial induction transitions (P(k) is false) append a limitation rather than aborting, so genuine counterexamples later in the domain can still be caught.
- All non-conforming AST nodes safely return `UNVERIFIABLE`.
"""
with open("planning/phase2/phase2c_decisions.md", "w") as f: f.write(decisions)

matrix = """# Phase 2C Test Matrix
- Recurrence finite PASS
- Recurrence general UNVERIFIABLE (finite evidence)
- Recurrence FAIL wrong candidate
- Recurrence FAIL wrong initial value
- Recurrence UNVERIFIABLE unsupported syntax
- Induction finite PASS
- Induction general UNVERIFIABLE
- Induction FAIL base case
- Induction FAIL transition
- Induction UNVERIFIABLE out of bounds / unsupported
"""
with open("planning/phase2/recurrence-induction-test-matrix.md", "w") as f: f.write(matrix)

# Fixtures
rec_claims = [
    {
        "claim_id": "rec-pass-finite",
        "kind": "recurrence_substitution",
        "claim_scope": "finite",
        "sequence": "a",
        "index_variable": "n",
        "initial_values": {"0": 1},
        "recurrence": {"valid_from": 1, "rhs": {"op": "add", "args": [{"seq": "a", "at": {"op": "sub", "args": [{"var": "n"}, 1]}}, 2]}},
        "candidate": {"op": "add", "args": [{"op": "mul", "args": [2, {"var": "n"}]}, 1]},
        "check_domain": {"start": 0, "end": 12}
    },
    {
        "claim_id": "rec-unv-general",
        "kind": "recurrence_substitution",
        "claim_scope": "general",
        "sequence": "a",
        "index_variable": "n",
        "initial_values": {"0": 1},
        "recurrence": {"valid_from": 1, "rhs": {"op": "add", "args": [{"seq": "a", "at": {"op": "sub", "args": [{"var": "n"}, 1]}}, 2]}},
        "candidate": {"op": "add", "args": [{"op": "mul", "args": [2, {"var": "n"}]}, 1]},
        "check_domain": {"start": 0, "end": 12}
    },
    {
        "claim_id": "rec-fail-candidate",
        "kind": "recurrence_substitution",
        "claim_scope": "general",
        "sequence": "a",
        "index_variable": "n",
        "initial_values": {"0": 1},
        "recurrence": {"valid_from": 1, "rhs": {"op": "add", "args": [{"seq": "a", "at": {"op": "sub", "args": [{"var": "n"}, 1]}}, 2]}},
        "candidate": {"op": "add", "args": [{"var": "n"}, 1]},
        "check_domain": {"start": 0, "end": 12}
    },
    {
        "claim_id": "rec-fail-init",
        "kind": "recurrence_substitution",
        "claim_scope": "general",
        "sequence": "a",
        "index_variable": "n",
        "initial_values": {"0": 2},
        "recurrence": {"valid_from": 1, "rhs": {"op": "add", "args": [{"seq": "a", "at": {"op": "sub", "args": [{"var": "n"}, 1]}}, 2]}},
        "candidate": {"op": "add", "args": [{"op": "mul", "args": [2, {"var": "n"}]}, 1]},
        "check_domain": {"start": 0, "end": 12}
    },
    {
        "claim_id": "rec-unv-syntax",
        "kind": "recurrence_substitution",
        "claim_scope": "finite",
        "sequence": "a",
        "index_variable": "n",
        "initial_values": {"0": 1},
        "recurrence": {"valid_from": 1, "rhs": {"op": "add", "args": [{"seq": "a", "at": {"op": "sub", "args": [{"var": "n"}, 1]}}, 2]}},
        "candidate": {"op": "sin", "args": [{"var": "n"}]},
        "check_domain": {"start": 0, "end": 12}
    },
    {
        "claim_id": "rec-unv-domain",
        "kind": "recurrence_substitution",
        "claim_scope": "finite",
        "sequence": "a",
        "index_variable": "n",
        "initial_values": {"0": 1},
        "recurrence": {"valid_from": 1, "rhs": {"op": "add", "args": [{"seq": "a", "at": {"op": "sub", "args": [{"var": "n"}, 1]}}, 2]}},
        "candidate": {"op": "add", "args": [{"op": "mul", "args": [2, {"var": "n"}]}, 1]},
        "check_domain": {"start": 10, "end": 12} # missing base cases
    }
]
with open("verification/tests/fixtures/recurrence_claims.json", "w") as f: json.dump(rec_claims, f, indent=2)

ind_claims = [
    {
        "claim_id": "ind-unv-general",
        "kind": "induction_evidence",
        "claim_scope": "general",
        "index_variable": "n",
        "property": {"op": "ge", "lhs": {"op": "pow", "base": 2, "exponent": {"var": "n"}}, "rhs": {"op": "add", "args": [{"var": "n"}, 1]}},
        "base_indices": [0],
        "transition": {"from": "k", "to": {"op": "add", "args": [{"var": "k"}, 1]}},
        "check_domain": {"start": 0, "end": 20}
    },
    {
        "claim_id": "ind-pass-finite",
        "kind": "induction_evidence",
        "claim_scope": "finite",
        "index_variable": "n",
        "property": {"op": "ge", "lhs": {"op": "pow", "base": 2, "exponent": {"var": "n"}}, "rhs": {"op": "add", "args": [{"var": "n"}, 1]}},
        "base_indices": [0],
        "transition": {"from": "k", "to": {"op": "add", "args": [{"var": "k"}, 1]}},
        "check_domain": {"start": 0, "end": 20}
    },
    {
        "claim_id": "ind-fail-base",
        "kind": "induction_evidence",
        "claim_scope": "general",
        "index_variable": "n",
        "property": {"op": "lt", "lhs": {"op": "pow", "base": 2, "exponent": {"var": "n"}}, "rhs": {"var": "n"}},
        "base_indices": [0],
        "transition": {"from": "k", "to": {"op": "add", "args": [{"var": "k"}, 1]}},
        "check_domain": {"start": 0, "end": 20}
    },
    {
        "claim_id": "ind-fail-transition",
        "kind": "induction_evidence",
        "claim_scope": "general",
        "index_variable": "n",
        "property": {"op": "lt", "lhs": {"op": "pow", "base": 2, "exponent": {"var": "n"}}, "rhs": 100},
        "base_indices": [0],
        "transition": {"from": "k", "to": {"op": "add", "args": [{"var": "k"}, 1]}},
        "check_domain": {"start": 0, "end": 20}
    },
    {
        "claim_id": "ind-unv-syntax",
        "kind": "induction_evidence",
        "claim_scope": "general",
        "index_variable": "n",
        "property": {"op": "unknown", "lhs": 1, "rhs": 1},
        "base_indices": [0],
        "transition": {"from": "k", "to": {"op": "add", "args": [{"var": "k"}, 1]}},
        "check_domain": {"start": 0, "end": 20}
    }
]
with open("verification/tests/fixtures/induction_claims.json", "w") as f: json.dump(ind_claims, f, indent=2)

expected = {
    "rec-pass-finite": {"expected_verdict": "PASS", "expected_reason_code": "RECURRENCE_EXHAUSTIVE_FINITE"},
    "rec-unv-general": {"expected_verdict": "UNVERIFIABLE", "expected_reason_code": "RECURRENCE_FINITE_EVIDENCE_ONLY"},
    "rec-fail-candidate": {"expected_verdict": "FAIL", "expected_reason_code": "RECURRENCE_SUBSTITUTION_MISMATCH"},
    "rec-fail-init": {"expected_verdict": "FAIL", "expected_reason_code": "RECURRENCE_INITIAL_VALUE_MISMATCH"},
    "rec-unv-syntax": {"expected_verdict": "UNVERIFIABLE", "expected_reason_code": "EXACT_EXPR_UNSUPPORTED"},
    "rec-unv-domain": {"expected_verdict": "UNVERIFIABLE", "expected_reason_code": "RECURRENCE_DOMAIN_ERROR"},
    
    "ind-unv-general": {"expected_verdict": "UNVERIFIABLE", "expected_reason_code": "INDUCTION_FINITE_EVIDENCE_ONLY"},
    "ind-pass-finite": {"expected_verdict": "PASS", "expected_reason_code": "INDUCTION_EXHAUSTIVE_FINITE"},
    "ind-fail-base": {"expected_verdict": "FAIL", "expected_reason_code": "INDUCTION_BASE_CASE_FAIL"},
    "ind-fail-transition": {"expected_verdict": "FAIL", "expected_reason_code": "INDUCTION_TRANSITION_FAIL"},
    "ind-unv-syntax": {"expected_verdict": "UNVERIFIABLE", "expected_reason_code": "EXACT_EXPR_UNSUPPORTED"}
}
with open("verification/tests/fixtures/recurrence_induction_expected.json", "w") as f: json.dump(expected, f, indent=2)
