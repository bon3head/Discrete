# Orchestration Contract

## Mission
Create a deterministic session plan based on the student's request that bounds the autonomous tutor's behavior according to `AGENTS.md`.

## Retrieval
- Catalog maps chapter and optional section to exact paths in `corpus/active/`.
- Deferred topics return `CLARIFICATION_REQUIRED` or `POLICY_BLOCKED` unless explicitly overridden (not implemented in 3A default).
- Unknown chapter/section returns `CLARIFICATION_REQUIRED`.

## Verification Dispatch
- If `claim` is provided, the orchestrator delegates it directly to the Phase 2 verification core based on `claim["kind"]`.
- The exact verification dictionary result is nested in `verification_result`.
- Unrecognized `claim["kind"]` or missing fields yield an orchestrator-level `UNVERIFIABLE`.

## Logging
- Uses a local, git-ignored runtime log: `runtime/session_logs/`
- Logs only metadata: `timestamp`, `mode`, `chapter`, `section`, `task_type`, `hint_level_authorized`, `verification_verdict`, `reason_code`, `reference_solution_accessed`, `struggle_flags`.
- Raw text and answers are specifically forbidden from these logs.
