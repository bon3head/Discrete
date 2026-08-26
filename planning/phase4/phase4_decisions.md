# Phase 4 Decisions
- CLI logic uses Python's `argparse`.
- `session.json` handles state management. Turn logic maintains a `turns` array.
- Responses will strictly adhere to `response-schema.json`.
- Validations are purely syntactic and policy-driven; no LLM usage in CLI.
- POSIX/Linux is strictly required due to fcntl session locking. Windows is not supported natively.
- Verification hash JSON is treated as ephemeral and gitignored to prevent dirtying the tree on every run.
