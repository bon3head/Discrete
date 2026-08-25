# Phase 2A local verification harness

`verify(claim)` accepts explicit structured dictionaries and returns a JSON
object whose verdict is exactly `PASS`, `FAIL`, or `UNVERIFIABLE`.

The initial CPU-only families are logic equivalence, truth tables, finite set
expressions, counting identities, and exact matrix expressions. No natural-
language parsing, proof judgment, recurrence solving, graph algorithms,
network access, or reference-solution retrieval is included.

## Phase 2B Propositional Text Adapter

The `verify_propositional_text(claim)` adapter accepts plain text propositional logic grammar and routes it to the underlying logic equivalence and truth table verifiers.

### Supported Grammar
- **Variables:** `[A-Za-z][A-Za-z0-9_]*`
- **Operators:** `~`, `!`, `¬` (NOT); `&`, `∧` (AND); `|`, `∨` (OR); `->`, `→` (IMPLIES); `<->`, `↔` (IFF).
- **Groupings:** `(`, `)`

*Freeform English (e.g. "implies", "not", "and") and LaTeX (e.g. `\neg p`, `$p \to q$`) are explicitly unsupported and will return `UNVERIFIABLE` with `LOGIC_PARSE_ERROR`.*

### Public Adapter Call Shape

**Equivalence Mode:**
```json
{
  "kind": "propositional_text",
  "mode": "equivalence",
  "lhs_text": "p -> q",
  "rhs_text": "~p | q"
}
```

**Property Mode:**
```json
{
  "kind": "propositional_text",
  "mode": "property",
  "property": "tautology",
  "expression_text": "(p | ~p)"
}
```

### Examples of Verdicts
- **PASS:** `p -> q` and `~p | q` yields `PASS` with `LOGIC_EXHAUSTIVE_EQUIVALENCE`.
- **FAIL:** `p & q` and `p | q` yields `FAIL` with `LOGIC_COUNTEREXAMPLE` and an explicit counterexample valuation.
- **LOGIC_PARSE_ERROR:** `p <-> q <-> r` (chained biconditionals without parentheses) yields `UNVERIFIABLE` with `LOGIC_PARSE_ERROR`.
