# Policy Reconciliation Report

This report extracts and correlates findings from the engineering reviews (`engineer_1_review.md`, `engineer_2_review.md`, and `engineer_3_review.md`) against the strict policy constraints defined in `AGENTS.md` (the ADS-Tutor Constitution). Stylistic, performance, and file-system-level bugs have been explicitly filtered out.

## 1. Unauthorized Hint Level (Violation of §8.1 Hint Ladder)
* **Provenance:** Engineer 1 Review → `tutor/response_guard.py` (Constants Defined in the Loop).
* **Finding:** The reviewer noted the presence of `levels = {"L0": 0, ...}` defined in the `validate_response` function.
* **Policy Issue:** Section 8.1 strictly defines the Hint Ladder with only four allowed escalation levels: L1 (Point), L2 (Identify), L3 (Scaffold), and L4 (Walkthrough). The introduction or recognition of an "L0" level is an unauthorized deviation from the mandatory escalation protocol.

## 2. Invalid Verdict Semantics (Violation of Rule 6 & §5.3)
* **Provenance:** Engineer 2 Review → `verification/dispatcher.py` (Magic Strings).
* **Finding:** The reviewer identified the use of the magic string `'CLAIM_NOT_OBJECT'` alongside valid strings like `'UNVERIFIABLE'`.
* **Policy Issue:** Section 5.3 strictly limits the verification verdicts to exactly three states: `PASS`, `FAIL`, or `UNVERIFIABLE`. Rule 6 explicitly states that if the harness cannot check a claim, it must be labeled `UNVERIFIABLE`. Emitting or handling a custom `'CLAIM_NOT_OBJECT'` verdict violates the Verification Protocol contract.

## 3. Subversion of the Attempt Gate (Violation of Rule 2 & §8.2)
* **Provenance:** Engineer 3 Review → `tutor/cli.py` (Local File Inclusion via `args.path`).
* **Finding:** In the `submit_attempt_command`, the application blindly accepts any string provided via `args.path` and saves it to the session state without verifying if the file actually exists or contains valid content.
* **Policy Issue:** Rule 2 and Section 8.2 (Attempt Gate) dictate that "L4 and any final answer require a student submission first." By failing to validate the existence and integrity of the submitted attempt file, the system allows a student to bypass the Attempt Gate entirely (e.g., by submitting a fake path like `/dev/null`). This subverts the Prime Directive to ensure the student actually attempts the problem before receiving a walkthrough.

## 4. Skipping Session Logging via Hard Exits (Violation of Rule 10)
* **Provenance:** Engineer 1 Review → `tutor/cli.py` (Random `sys.exit(1)` Bombs) AND Engineer 3 Review → `tutor/cli.py` (Unhandled Validation Exceptions).
* **Finding:** The CLI relies heavily on scattering `sys.exit(1)` calls for error states, and allows unhandled exceptions (e.g., throwing a `ValueError` during UUID validation) to abruptly terminate the process.
* **Policy Issue:** Rule 10 mandates: "SESSION LOGGING. Every session appends a structured log entry... Never skip logging." Hard-crashing the process or calling `sys.exit(1)` prematurely guarantees that the session loop cannot finalize and append its required audit log. This bypasses the generation of the spaced-repetition source and destroys the academic-integrity audit trail.
