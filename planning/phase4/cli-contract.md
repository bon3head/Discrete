# CLI Contract

## Commands
- `new --chapter N [--section S] [--task T] [--hint H] [--mode M] [--ref]`
- `validate <id>`
- `show <id>`
- `submit-attempt <id> [--path P]`
- `smoke`

## Exit Codes
- 0: Success (including successful block/review states).
- 1: CLI fatal error (missing session, invalid args, JSON schema violations).
- `smoke` returns non-zero on test failures.
