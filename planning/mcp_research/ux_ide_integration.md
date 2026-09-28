# UX Architecture & IDE Integration Proposal: ADS-Tutor

This document outlines the UX architecture for the ADS-Tutor, leveraging the Antigravity IDE capabilities (Artifacts, Mermaid, Carousels, Markdown) and the existing deterministic MCP backend (`jflap-server`, local verifiers). 

## 1. Core Pedagogical Philosophy in UX
The goal is to maximize student transfer of skill to in-class exams. The UX must support:
- Verification-first tutoring: Students see visual proof of the state of their work.
- Scaffolded hint ladders (L1 to L4).
- High cognitive focus: Reduce extraneous UI clutter while keeping relevant data accessible.

## 2. Leveraging IDE Capabilities

### 2.1 Artifacts for Persistent Context
**The "Brain Dump" / Workpad as an Artifact:**
- The student's current hypothesis, given variables, and known theorems should be maintained in a persistent Markdown Artifact called `Session_Workpad.md`. 
- As the student explores, the agent updates the artifact to track:
  - **Given Information:** What is established.
  - **Goal:** The ultimate proof or answer sought.
  - **Attempted Steps:** A running log of what they have tried, decorated with validation tags (PASS/FAIL/UNVERIFIABLE).

**Why?** This prevents the student from losing track of their proof state across chat turns. When they ask "where am I?", they just glance at the artifact.

### 2.2 Mermaid Diagrams for Abstract Structures
Discrete math relies heavily on relationships. We use Mermaid to dynamically render structures via MCP responses.
- **Set Theory & Logic:** Use Mermaid state diagrams or flowcharts to represent subset relations (Hasse diagrams).
- **Induction Steps:** Visualize the domino effect. A flowchart showing `P(1) --> P(k) --> P(k+1)`, highlighting which step the student is currently proving.
- **Automata (via `jflap-server`):** When interacting with DFAs/NFAs, use the MCP tools (`jflap_parse_jff`, `jflap_simulate_automaton`) to extract state transitions and dynamically render them as Mermaid state diagrams. 

### 2.3 Carousels for Step-by-Step Walkthroughs (L4 Hints)
When a student reaches an L4 Hint (Walkthrough), dropping a wall of text is pedagogically harmful. Instead, we use **Carousels**.
- **Slide 1:** The setup and definition invocation.
- **Slide 2:** The algebraic manipulation or logical equivalence step.
- **Slide 3:** The final conclusion.
*UX Benefit:* The student clicks through at their own pace, reducing cognitive overload and mirroring the experience of an instructor writing on a whiteboard.

### 2.4 Markdown Alerts for Verification States
Utilize GitHub-flavored alerts to give instant, visceral feedback on the outputs of the deterministic backend.
- `> [!TIP]` for L1/L2 hints pointing to a theorem.
- `> [!NOTE]` for definitions pulled from the ADS corpus.
- `> [!WARNING]` for `FAIL` verdicts from the TDD verification gate.
- `> [!CAUTION]` for unverified claims or attempts to skip steps.

## 3. Integration with the MCP Backend

Our deterministic MCP backend (with symbolic/truth-table logic and JFLAP automata support) generates data that must be mapped to UI.

### 3.1 Automata & Grammars (JFLAP Server)
- **State Highlighting:** When running `jflap_simulate_automaton`, output the trace as a Markdown table or a Carousel showing the active state at each step of the string parsing.
- **L-Systems (`jflap_expand_lsystem`):** Generate successive iterations and display them sequentially in a Carousel to visually demonstrate the recursive expansion.
- **NFA to DFA Conversion:** Show the subset construction mapping in a Markdown table alongside a Mermaid state diagram of the resulting DFA.

### 3.2 Logic & Proof Verification
- **Truth Tables:** Render as clean Markdown tables. Use bolding to highlight rows where truth values diverge from the student's hypothesis.
- **Dependency Graphs:** For multi-step proofs, construct a Mermaid flowchart showing how axioms and previous steps feed into the current step. If a step is orphaned, color its node red (`style Node fill:#ffcccc`).

## 4. Proposed Layout and Interaction Loop

1. **Primary Chat Panel:** Kept clean. Used exclusively for conversational scaffolding, hints, and direct Q&A.
2. **Artifact Panel:** Houses the `Session_Workpad.md` (Brain Dump) and any generated diagrams. This persists and updates in real-time.
3. **Feedback Loop:**
   - Student inputs a step.
   - Agent routes to backend `verify()`.
   - Agent replies in chat with a `> [!WARNING]` or `> [!NOTE]` summarizing the result.
   - Agent updates the Artifact to reflect the new valid step or append the failed attempt to a "Scratchpad" section.

## 5. Example UI Scenarios

**Scenario 1: Proof by Induction (Stuck on Inductive Step)**
- **Artifact:** Shows `P(1)` as `[VERIFIED]`. Shows `P(k)` assumption. Goal: `P(k+1)`.
- **Chat:** Student asks "What now?"
- **Agent:** Responds with an L2 hint (Alert block) suggesting algebraic manipulation.
- **Carousel:** If escalated to L4, shows the algebraic expansion step-by-step.

**Scenario 2: Automata Construction**
- **Student:** "Does this NFA accept '010'?"
- **Backend:** `jflap_simulate_automaton` returns the trace.
- **Agent:** Renders a Carousel. Slide 1: Start state. Slide 2: Consuming '0' (showing multiple paths). Slide 3: Consuming '1'. Slide 4: Reject/Accept result.

## Conclusion
By treating the IDE not just as a text renderer, but as a dynamic, persistent workspace (Artifacts) and a pacing mechanism (Carousels), we transform the strict, rule-bound MCP backend into an empathetic, highly effective tutoring environment that naturally encourages the student to focus on understanding rather than rote completion.
