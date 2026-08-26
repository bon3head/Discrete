# ADS-Tutor: Daily Use

## Workflow

1. **Start a new session:**
   ```bash
   python3 -m tutor.cli new --chapter <N> [--section <S>] [--task <task>] [--hint <hint_level>] [--mode <mode>] [--ref]
   ```
   This generates a `session_id` and prepares `brief.json` in `runtime/sessions/<id>/`.

2. **Agent drafts a response:**
   The AI agent reads `brief.json`, follows the constraints, and writes `response.json` (adhering strictly to `planning/phase3/response-schema.json`).

3. **Validate the response:**
   ```bash
   python3 -m tutor.cli validate <id>
   ```
   This ensures structural validity and policy compliance. Writes `verdict.json`.
   If `status` is `PASS`, proceed. If `REVIEW_REQUIRED` or `POLICY_BLOCKED`, fix the response and re-validate.

4. **Show the response:**
   ```bash
   python3 -m tutor.cli show <id>
   ```
   Renders the markdown body only if the last validate verdict was `PASS`.

## Mock Exam Mode
- Start with `--mode mock_exam`. The system enforces L0 max hint level.
- Submit your attempt: `python3 -m tutor.cli submit-attempt <id>`. Max hint level escalates to L4.

## Escalate Hints
To get more help on the same problem, start a new turn in the same session:
```bash
python3 -m tutor.cli new --id <existing_id> --chapter <N> --hint <higher_hint_level>
```

## Maintenance
Run smoke tests to ensure system integrity:
```bash
python3 -m tutor.cli smoke
```
