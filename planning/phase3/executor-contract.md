# Phase 3B Executor Contract

## Purpose
The Executor receives a `SessionPlan` from Phase 3A Orchestration, fetches the authorized corpus content from disk, and bundles it into an `AgentBrief`. 
It also provides a `validate_response(agent_brief, response)` function which enforces strict, deterministic limitations on the generated Antigravity response.

## Constraints
1. Executor must NOT mutate or reinterpret the SessionPlan. 
2. Executor must NOT retrieve outside the specified paths.
3. Executor must NOT rely on generative AI to validate rules.
