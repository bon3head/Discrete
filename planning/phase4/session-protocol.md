# Session Protocol

## States
`CREATED` → `PLANNED` → `BRIEFED` → `RESPONSE_PRESENT` → `VALIDATED` → `SHOWN`
↘ `BLOCKED` (terminal)   ↘ `REVIEW_REQUIRED` (user may edit+revalidate)

## Rules
- Every state transition is a file operation + explicit status field in `session.json`. No hidden state.
- `new` on a blocked plan creates the session in `BLOCKED` state, loads nothing, logs metadata.
- `validate` is idempotent.
- `show` refuses to render unless latest verdict == `PASS`. No override flag.
- Hint escalation creates a new turn in the SAME session: re-run `build_session_plan`, append turn record to `session.json`.
- `attempt_provided` transitions to true ONLY via `python3 -m tutor.cli submit-attempt <id>`.

## Mock Exam Flow
- `new --mode mock_exam` -> `exam_phase: in_progress`. Plan L0.
- `submit-attempt` -> `exam_phase: submitted`. Re-plans at L4.
- Appendix F rules still apply.
