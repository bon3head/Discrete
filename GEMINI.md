# Zero-Trust Engineering Protocol

Verification before assertion. These are blocking gates, not style preferences.
Scope: all code changes in this workspace. Docs-only commits are exempt from
Rules 1–3 but never from Rules 6–9. AGENTS.md governs tutoring behavior; this
protocol governs engineering process.

1. **No untested commits.** The relevant test battery runs after the final
   edit and before the commit. Any edit after the last test run voids it —
   re-run. The battery output appears in the phase report.

2. **Every P0/P1 fix ships a permanent regression test**, named after the
   failure it guards (test_concurrent_turn_appends, not test_fix2).
   Scratch/experiment scripts are deleted, never committed.

3. **No placebo tests.** Tests guarding critical fixes (concurrency, state,
   corruption) must be proven as detectors: temporarily neutralize the fix in
   a scratch copy (SHA-256 before/after + try/finally restore), confirm the
   test fails, restore, verify hash, report the detector result.

4. **Evidence over prose.** Challenged claims are answered with verbatim
   artifacts — code, logs, command output — never re-explanation. Every
   number in a report must reconcile with every other number before emission;
   totals must equal their sums across sections.

5. **Name the boundary under test.** "Malformed input" tests must declare
   whether they test parse validity or schema validity — different
   boundaries, different fixtures, both required.

6. **Existence before citation.** Never reference a file, path, section, or
   artifact without verifying it exists at that moment (ls / read / hash).
   Phantom references are P0 defects.

7. **Scope discipline.** Implement exactly what was requested. Additions are
   proposals in the report, never unrequested code in the commit. Review
   `git status` and the staged diff before every commit; scratch files never
   enter the tree.

8. **Honest substitution.** If a required process step cannot run (network,
   tool failure), the report states the substitution and its cause
   explicitly. Never relabel a skipped step as performed.

9. **Closure requires terminal evidence.** Any "CLOSED" or "PASS" claim
   includes: final battery output, clean `git status`, commit log.
