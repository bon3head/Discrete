# ADS-Tutor: Daily Use

## Workflow (The Short Loop)

1. **Start a hint session:**
   ```bash
   tutor new 1.1
   ```
   *This initializes a session for Chapter 1, Section 1.1 (defaults to Hint Level 1).*

2. **Agent drafts a response:**
   The AI reads the problem context and writes `response.json` automatically in the background.

3. **Read the hint:**
   ```bash
   tutor show
   ```
   *This automatically validates the agent's response against the Prime Directive (no answer leaks, verified citations) and displays it.*

## Escalate Hints
To get more help on the latest problem:
```bash
tutor new 1.1 L2
```
Then run `tutor show` again.

## Submit an Attempt (Unlocks L4 Walkthrough)
You must submit your work before the tutor is allowed to give you a full walkthrough:
```bash
tutor attempt work.txt
tutor show
```

## Mock Exam Mode
Test yourself with zero hints (L0 lockout):
```bash
tutor exam 1
```

## Session Management & Health
List your recent sessions:
```bash
tutor list
```

Check system health (smoke tests and integrity hashes):
```bash
tutor doctor
```

---

## Setup
Add this alias to your `~/.bashrc` to make `tutor` location-independent:
```bash
alias tutor="$HOME/ma35100-tutor/tutor"
```
*(The actual script is located in `bin/tutor` due to naming conflicts, so adjust the path to `$HOME/ma35100-tutor/bin/tutor` if you follow standard installation).*

## Full Command Reference

The old flag-based CLI commands remain completely functional:
- `python3 -m tutor.cli new --chapter <N> [--section <S>] [--task <task>] [--hint <hint_level>] [--mode <mode>] [--ref]`
- `python3 -m tutor.cli validate <id>`
- `python3 -m tutor.cli show <id>`
- `python3 -m tutor.cli submit-attempt <id> --path <path>`
- `python3 -m tutor.cli smoke`
