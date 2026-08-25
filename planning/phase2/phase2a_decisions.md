# Phase 2A decisions

- Python 3.14.4 is available. SymPy is not installed; no dependency is added.
- The implementation uses only the standard library (`dataclasses`,
  `fractions`, `itertools`, `math`, `json`). This keeps verification offline,
  deterministic, and CPU-only.
- Structured AST input is required. Natural-language parsing, LaTeX parsing,
  proof judgment, recurrence solving, graph algorithms, and infinite-set
  claims remain explicitly unsupported.
- Matrix shape mismatch returns `UNVERIFIABLE`, because the operation is
  undefined rather than a false equality.
- Exact rational matrix entries use an explicit numerator/denominator object;
  floating point values are rejected.


- Added strict serialization of `Fraction` objects to either integer or `{"numerator": n, "denominator": d}` dictionaries to prevent JSON serialization crashes during mismatch evidence generation.
- Strengthened permanent regression test for missing explicit universe in set verification to ensure it explicitly returns `UNVERIFIABLE`.
