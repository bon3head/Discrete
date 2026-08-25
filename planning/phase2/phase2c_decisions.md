# Phase 2C Decisions
- Only exact arithmetic (integers and exact Fractions) is supported.
- `claim_scope: "finite"` strictly ensures all sequence accesses fall within `check_domain`.
- Any sampled index k where P(k) is false is treated immediately as a concrete property counterexample returning FAIL.
- All non-conforming AST nodes safely return `UNVERIFIABLE`.
