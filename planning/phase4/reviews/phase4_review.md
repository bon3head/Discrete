METHOD: subagent independent review

Finding 1
Severity: P0
Affected file: `tutor/session_store.py`
Evidence: `def get_session_dir(session_id: str) -> Path: return SESSIONS_DIR / session_id`
Why it violates a specific Phase 4 rule: Security / leaks. An attacker or malformed command could pass `--id ../../../etc` to traverse the file system, leading to arbitrary file read/overwrite or sensitive data disclosure outside the `runtime/sessions/` boundary.
Minimal recommended fix: Validate `session_id` to ensure it is a valid UUID, or sanitize the path in `get_session_dir` to confirm it resolves strictly within `SESSIONS_DIR`.

Finding 2
Severity: P1
Affected file: `tutor/cli.py` (`validate_command`)
Evidence: `session["state"] = verdict.status` (where `verdict.status` is `"PASS"` or similar on success).
Why it violates a specific Phase 4 rule: State machine consistency. `planning/phase4/session-protocol.md` specifies the explicit sequence: `RESPONSE_PRESENT` → `VALIDATED`. Assigning the guard's output status (`"PASS"`) instead of `"VALIDATED"` breaks the documented state machine.
Minimal recommended fix: Change to `session["state"] = "VALIDATED" if verdict.status == "PASS" else verdict.status`.

Finding 3
Severity: P1
Affected file: `tutor/cli.py` (`new_command`, `submit_attempt_command`)
Evidence: `new_command` and `submit_attempt_command` transition from `CREATED` directly to `BRIEFED` without recording a `PLANNED` state.
Why it violates a specific Phase 4 rule: State machine consistency. `session-protocol.md` mandates `CREATED` → `PLANNED` → `BRIEFED`, and explicitly requires: "Every state transition is a file operation + explicit status field in `session.json`. No hidden state."
Minimal recommended fix: Save the session with `session["state"] = "PLANNED"` immediately after `build_session_plan()` is successful, before continuing to `prepare_agent_brief()`.

Finding 4
Severity: P1
Affected file: `tutor/cli.py` (`new_command`)
Evidence: `request_id=f"{session_id}-turn0"` is hardcoded when a new turn is appended to an existing session (via `--id`).
Why it violates a specific Phase 4 rule: Schema adherence. `session-protocol.md` states: "Hint escalation creates a new turn in the SAME session: re-run build_session_plan, append turn record". With a hardcoded `-turn0`, all hint escalation turns incorrectly share the exact same `request_id`, breaking uniqueness and data schema.
Minimal recommended fix: Compute the index dynamically: `turn_index = len(session.get("turns", []))` and use `request_id=f"{session_id}-turn{turn_index}"`.

Finding 5
Severity: P1
Affected file: `tutor/cli.py` (`new_command`, `show_command`, `submit_attempt_command`)
Evidence: `load_session(session_id)` is called without a `try/except FileNotFoundError` block in `new_command` and `submit_attempt_command`. In `show_command`, `resp_dict.get("body", "")` is called without checking if `resp_dict` is `None` (which occurs if `response.json` is missing).
Why it violates a specific Phase 4 rule: Error handling. The application crashes with unhandled Python exceptions instead of gracefully exiting or providing clear error messages like it correctly does in `validate_command`.
Minimal recommended fix: Add `try/except FileNotFoundError` around `load_session` calls. Add an `if not resp_dict:` guard check in `show_command`.
