# Phase 3A Decisions

- **Catalog Mapping**: We use a static mapping derived from the known `corpus/active/` layout, combined with `planning/phase0/scope_classification.json` to safely match chapter numbers and deferred bounds.
- **Reference Gate**: Enforced strictly at the plan generation step. Any violation overrides the entire plan to `POLICY_BLOCKED`.
- **Privacy Logging**: `runtime/session_logs/` is explicitly ignored.
