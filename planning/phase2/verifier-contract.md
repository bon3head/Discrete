# Phase 2A verifier contract

The harness accepts explicit JSON-like dictionaries only. It never parses
natural-language claims, LaTeX, Markdown, or student work.

Supported `kind` values are `logic_equivalence`, `truth_table`,
`finite_set_expression`, `counting_identity`, and `matrix_expression`.
Every response has `verdict`, `kind`, `reason_code`, `evidence`,
`limitations`, and `source`. Verdict is exactly `PASS`, `FAIL`, or
`UNVERIFIABLE`.

`PASS` requires exhaustive finite evaluation or exact integer/rational
arithmetic. `FAIL` includes a concrete counterexample, mismatched vector,
wrong result, or incompatible dimensions. `UNVERIFIABLE` covers malformed
schemas, undeclared variables, missing finite universes, unsupported operators,
non-finite claims, and unsupported claim kinds; it never guesses.

Logic expressions are ASTs using declared variable strings and `not`, `and`,
`or`, `xor`, `implies`, and `iff`. Valuations enumerate declared variables in
the supplied order. Truth-table claims evaluate one expression against an
explicit expected vector or property (`tautology`, `contradiction`, or
`equivalence`).

Finite sets use explicit finite `universe`, named finite sets, and AST
operators `union`, `intersection`, `difference`, `symmetric_difference`, and
`complement`. Equality is checked by exact enumeration.

Counting supports exact nonnegative integer `factorial`, `permutation`,
`combination`, and `binomial` operations. Matrices support exact integer or
`{"numerator": n, "denominator": d}` entries and `add`, `subtract`,
`multiply`, and `equal`; dimension errors are `UNVERIFIABLE` because the
requested operation is not defined.

Finite enumeration is evidence for the bounded claim only, never a proof of
an infinite/general mathematical statement.
