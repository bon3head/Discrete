# Recurrence and Induction Contract

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
- Transitions where P(k)=false are rejected entirely: any sampled index k where P(k) is false is treated immediately as a concrete property counterexample returning FAIL (INDUCTION_PROPERTY_COUNTEREXAMPLE).
