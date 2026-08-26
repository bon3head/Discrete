# Phase 3B Review

Finding 1
Severity: P1
Affected file/path: `tutor/response_guard.py`
Evidence: `if footer and footer.verdict:` allows a footer with a `None` verdict but a non-null `reason_code` to bypass the check when `expected_vr` is empty.
Why it violates a specific Phase 3A/3B rule: "If no verification result exists, footer must be null." This allows an unauthorized mutation of the reason code.
Minimal recommended fix: Change to `if footer and (footer.verdict is not None or footer.reason_code is not None):`

Finding 2
Severity: P1
Affected file/path: `tutor/executor.py`
Evidence: The `execute_session` function directly writes to `runtime/session_logs/YYYY-MM-DD.md` using string formatting and `open()`.
Why it violates a specific Phase 3A/3B rule: It duplicates logging logic and bypasses `tutor/logging.py` which was designed for this. The instructions state to use `logging.py` ("extend only if required").
Minimal recommended fix: Move the logging logic to `tutor/logging.py` as an extended function (e.g. `log_execution`) and call it from `executor.py`.

Finding 3
Severity: P3
Affected file/path: `tutor/response_guard.py`
Evidence: Regex patterns like `r"solution:"` or `r"the answer is"` are overly broad and will cause false positives (e.g., "resolution:" or "the answer is incorrect").
Why it violates a specific Phase 3A/3B rule: It is an inherent limitation of deterministic text matching as requested.
Minimal recommended fix: Document this false-positive/false-negative limitation in the report limitations array. No code fix required.

Finding 4
Severity: P3
Affected file/path: `tutor/response_guard.py`
Evidence: Implicit citations (referencing a theorem by name without adding a citation object) cannot be detected.
Why it violates a specific Phase 3A/3B rule: Structural constraint only; cannot detect semantic bypasses.
Minimal recommended fix: Document this limitation. No code fix required.
