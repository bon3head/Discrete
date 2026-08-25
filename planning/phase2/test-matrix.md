# Phase 2A test matrix

| Family | PASS | FAIL | UNVERIFIABLE |
|---|---|---|---|
| logic_equivalence | implication identity | explicit valuation mismatch | undeclared variable / malformed AST |
| truth_table | tautology and contradiction properties | claimed vector mismatch | malformed vector or unsupported property |
| finite_set_expression | intersection/union and complement | symmetric-difference counterexample | missing universe |
| counting_identity | factorial/permutation and binomial | wrong claimed result | negative/noninteger domain |
| matrix_expression | exact multiplication | wrong product | incompatible dimensions |

Adversarial coverage also includes malformed JSON-like input, unsupported
claim kind, and unsupported infinite-set statements. Every fixture records its
expected structured verdict and evidence requirement.
