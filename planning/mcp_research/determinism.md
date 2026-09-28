# Architectural Findings: Deterministic State Machines & MCP Verification

## 1. Core Principle: Verification Before Assertion
In an AI tutoring system, the prime directive is to maximize skill transfer without revealing the answer prematurely or allowing the AI to hallucinate correctness. To mathematically guarantee the AI cannot bypass state transitions (e.g., unlocking answers before a valid student attempt), the state machine must be enforced externally, independent of the LLM's generative capacity.

## 2. State Machine Constraints
A tutor state machine transitions through specific pedagogical phases:
1. **Pre-attempt (Hint Ladder L1-L3)**: The tutor may provide structural guidance, identify laws, and scaffold, but must never reveal full steps.
2. **Attempt Evaluation**: The student provides an answer. The verification system (not the AI) must evaluate the answer's correctness.
3. **Post-attempt (Walkthrough L4)**: Only unlocked if the verification system registers a valid attempt.

### Mathematical Guarantee
To mathematically guarantee that the AI cannot jump states, we implement a **Mealy Machine** where the state transition is a function of the current state and a cryptographic or hardware-verified input (e.g., a hash of the verified student attempt).

- Let $S$ be the set of states: $\{S_{hint}, S_{verify}, S_{solution}\}$
- Let $\Sigma$ be the inputs: $\{I_{query}, I_{attempt}, I_{valid}\}$
- Transition function $\delta: S \times \Sigma \to S$

The LLM does not transition states; a rigid supervisor process transitions states. The LLM acts purely as a stateless function $f(s, c) \to r$, where $s \in S$ is injected into the context window as read-only, undeniable truth, and $c$ is the conversation history.

## 3. Python MCP Integration (FastMCP)
The Model Context Protocol (MCP) standardizes how AI models interact with data sources and tools. Using a framework like `FastMCP`, we can build a stateless verification server.

### Pipeline Architecture
1. **Host Agent (Antigravity)** receives user input.
2. **Host Agent** invokes an MCP tool, e.g., `verify_proof_step(step_data)`.
3. **MCP Server (FastMCP)** runs independent, deterministic checks (e.g., `sympy` simplification, finite state enumeration for logic).
4. **MCP Server** returns a strictly typed verdict: `PASS`, `FAIL`, or `UNVERIFIABLE`.
5. The **Tutor State Machine Supervisor** intercepts the output. If the state is $S_{hint}$ and the LLM attempts to emit a final solution, a pre-output middleware regex or structure scan (Leak Check) blocks the output and forces a rewrite.

### Example FastMCP Verifier Pattern
```python
from fastmcp import FastMCP, Context
import sympy

mcp = FastMCP("ADS-Tutor-Verification")

@mcp.tool()
def verify_set_equality(expr1: str, expr2: str) -> dict:
    """Verifies if two set expressions are mathematically equivalent."""
    try:
        e1 = sympy.sympify(expr1)
        e2 = sympy.sympify(expr2)
        is_equal = sympy.simplify(e1 - e2) == 0
        return {"verdict": "PASS" if is_equal else "FAIL"}
    except Exception as e:
        return {"verdict": "UNVERIFIABLE", "reason": str(e)}
```

## 4. Avoiding "Grading its Own Homework"
The LLM-as-judge pattern is inherently vulnerable to sycophancy and hallucination. To prevent the AI from grading its own homework:
1. **Layer 1 (Structural)**: RegEx and AST parsing to ensure the proof structure is valid.
2. **Layer 2 (Computational)**: Hand-off to deterministic systems (sympy, networkx) via MCP.
3. **Layer 3 (Adversarial)**: Only triggered if Layer 2 passes; involves another isolated LLM context checking the reasoning, but NEVER acts as the sole source of truth.

The LLM is restricted to translating the deterministic verifier's output (`PASS`/`FAIL`) into pedagogical feedback. It cannot override the verifier.

## 5. Summary
By combining a rigid, external supervisor state machine with a stateless, deterministic MCP verification server, we strip the generative model of its autonomy over the tutoring lifecycle. The model becomes a presentation layer over a deterministic mathematical engine, completely incapable of bypassing pedagogical gates.
