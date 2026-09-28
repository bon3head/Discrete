# Fusion Corpus: Deterministic Pedagogy for Discrete Mathematics

This document synthesizes ADHD-aware instructional frameworks with deterministic state-machine architectures. The goal is to construct an AI tutor for discrete mathematics that inherently prevents cognitive overload, task paralysis, and premature answer revelation through rigorous, external state verification (via the Model Context Protocol, MCP).

## 1. The Pedagogical State Machine: Enforcing the Hint Escalation Ladder

ADHD learners require a highly structured, predictable environment to bypass executive dysfunction. The Hint Escalation Protocol (L1 to L4) must not be a mere suggestion to a generative LLM; it must be enforced as a mathematically rigid **Mealy Machine**.

### State Definitions and Transitions
- **State $S_{L1}$ (Metacognitive/Orienting):** Focuses on initiating the task by lowering the threat level. 
  - *Discrete Math Example:* "What is the first step we usually take when proving set equality?"
- **State $S_{L2}$ (Strategy):** Nudges towards specific techniques.
  - *Discrete Math Example:* "What happens if we apply De Morgan's Laws to $(A \cup B)^c$?"
- **State $S_{L3}$ (Procedural/Structural):** Provides partial setup.
  - *Discrete Math Example:* "Start by assuming $x \in (A \cup B)^c$. What does the definition of complement tell us?"
- **State $S_{eval}$ (Attempt Evaluation):** The student submits a mathematical chunk.
- **State $S_{L4}$ (Walkthrough/Modeling):** The ultimate scaffold. 

### External Deterministic Enforcement
The LLM cannot autonomously transition from $S_{L3}$ to $S_{L4}$. A rigid supervisor process controls the state, injecting the current state $S_{current}$ into the LLM's context as read-only truth. 
- **Transition $\delta(S_{L1..3}, I_{attempt}) \to S_{eval}$**: Any student input that resembles mathematical notation or a logical claim triggers the attempt state.
- **Attempt Gate for $S_{L4}$**: To unlock $S_{L4}$, the system must cryptographically log a verifiable student attempt via the MCP server. Without this token, the Leak Check Middleware will forcefully block any LLM output containing terminal phrases (e.g., "Therefore", "The answer is", or a completed induction base case) and trigger a rewrite.

## 2. Micro-Chunking and Immediate Feedback via MCP Verification

ADHD learners thrive on immediate, specific feedback to maintain dopamine levels and engagement. Waiting until the end of a long proof (like a structural induction) to grade it leads to task paralysis.

### The MCP Verification Pipeline
We map the pedagogical need for "chunking" directly onto the MCP verification pipeline:
1. **Visual Checklists as State Variables:** For an induction proof, the supervisor maintains a strict checklist: `[ ] Base Case`, `[ ] Inductive Hypothesis`, `[ ] Inductive Step`.
2. **Micro-Evaluation:** When a student submits the Base Case chunk, the host agent passes it to a FastMCP server tool. For example:
   ```python
   @mcp.tool()
   def verify_base_case(claim: str, n_val: int) -> dict:
       # Deterministic sympy evaluation...
   ```
3. **Immediate Dopamine Hit:** The FastMCP server evaluates the step deterministically (Layer 2 Computational defense). If it passes, the checklist updates `[X] Base Case`. The LLM is strictly constrained to praise the effort ("Great job applying the base case substitution") without hallucinating subsequent steps, fulfilling the ADHD need for immediate positive reinforcement.

## 3. Cognitive Load Management through Architectural Constraints

Working memory limitations in ADHD learners mean that multi-step instructions or dense text cause system failures in the brain. The architecture must actively prune extraneous load.

### Dual-Coding and Externalizing Information
- **Read-Only Context Injection:** The supervisor maintains a "Brain Dump" state—a persistent on-screen ledger of knowns, unknowns, and relevant definitions (e.g., Definition of Subset). This externalizes the working memory load. 
- **Deterministic UI Rendering:** The LLM does not generate the UI. The state machine triggers dual-coding UI elements (e.g., rendering a Venn diagram alongside the text) based on the current step's verified MCP output.

### Preventing "Grading its Own Homework" (Trust and Predictability)
A tutor that hallucinates correctness and later backtracks shatters the predictable routine necessary for ADHD learners. The 3-Layer Defense ensures absolute predictability:
1. **Layer 1 (Structural):** RegEx/AST parsing ensures the chunk matches expected formats (e.g., checking if the student actually wrote "Assume $P(k)$ is true").
2. **Layer 2 (Computational):** MCP + SymPy evaluates logical equivalence.
3. **Layer 3 (Adversarial):** A separate LLM acts as a verifier to check natural language reasoning between steps.
Because the generative LLM acts purely as a presentation layer interpreting the `PASS`/`FAIL` signals from these deterministic systems, it cannot inadvertently confirm a flawed mathematical premise just to be "agreeable".

## 4. Conclusion

By fusing an ADHD-aware hint protocol with a strict MCP-driven state machine, the system prevents the generative AI from falling into its natural failure modes (sycophancy, over-explaining, and hallucination). The determinism of the Mealy Machine acts as the "executive function" the student might lack, strictly enforcing micro-chunking, managing working memory through externalized state, and guaranteeing that the cognitive heavy lifting remains entirely with the student until the attempt gate is verifiably breached.
