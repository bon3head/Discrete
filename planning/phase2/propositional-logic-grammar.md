# Propositional Logic Text Grammar

This defines the strict bounded grammar accepted by the Phase 2B propositional-text adapter.

## Supported Tokens
- **Variables:** `[A-Za-z][A-Za-z0-9_]*`
- **Negation:** `¬`, `!`, `~`
- **Conjunction:** `∧`, `&`
- **Disjunction:** `∨`, `|`
- **Implication:** `→`, `->`
- **Biconditional:** `↔`, `<->`
- **Grouping:** `(`, `)`

## Precedence and Associativity
Highest to lowest:
1. **Negation** (right-associative: `~~p` is valid)
2. **Conjunction** (left-associative)
3. **Disjunction** (left-associative)
4. **Implication** (right-associative: `p -> q -> r` parses as `p -> (q -> r)`)
5. **Biconditional** (non-associative: `p <-> q <-> r` is a parse error)

## Exclusions
- Arbitrary English (e.g. "implies", "not", "and").
- LaTeX syntax (e.g. `
eg p`, `$p 	o q$`).
- Unmatched parentheses, empty input, trailing operators, adjacent propositions.
- Any other unsupported characters.
