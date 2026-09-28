# UX Pedagogy & Student Experience Proposal: ADS-Tutor Frontend

## 1. Inputting Math Attempts (Frictionless Entry)
**Pedagogical Goal:** Reduce cognitive load associated with formatting so the student's working memory is strictly preserved for discrete math logic.
*   **Syntax-First Gate (Parse vs. Verify):** Before routing to the SymPy/NetworkX verification backend, the UI must run a fast, local parse check. If the syntax is malformed (e.g., unclosed parentheses, unrecognized macros), return a UI-level syntax error instantly. Do not conflate syntax errors with logical `FAIL` verdicts. This prevents the student from wondering, "Is my math wrong, or is my typing wrong?"
*   **Hybrid Text Input:** Support standard keyboard fallbacks (`A U B` for union, `~p v q` for logic, `x \in Z`) seamlessly alongside formal LaTeX.
*   **Micro-Chunked Submissions:** The UI should encourage entering exactly *one* logical step at a time rather than a full monolithic proof block, enforcing the "TDD Gate" (§5) incrementally.

## 2. Reducing Friction When Stuck (The Struggle Pathway)
**Pedagogical Goal:** Normalize the state of being stuck and gracefully guide the student up the Hint Ladder (L1 -> L4) without them feeling defeated or passively waiting for the answer.
*   **Explicit State Management:** The frontend should visually indicate the current position on the Hint Ladder (e.g., a subtle "Hint Level 1" indicator). 
*   **Frictionless Escalation:** Provide a primary `/hint` or `/stuck` command (or explicit UI button) that predictably advances the ladder.
*   **The "Almost-There" Safety Net:** If the student's step fails verification (§5.3) but they are on the right track, use specific error highlighting (if SymPy can isolate the failing sub-expression) rather than a blanket rejection. 
*   **Graceful Surrender Handling:** If a student inputs "I give up", do not immediately dump an L4 Walkthrough. Instead, shift the UI to present an L3 Scaffold—such as a fill-in-the-blank layout—forcing them to complete a micro-step to maintain active learning.

## 3. Visually Structuring Feedback (Hierarchy & Cognitive Load)
**Pedagogical Goal:** Prevent "wall of text" fatigue. The UI must strictly enforce the 4-part Output Contract (§9 of the Constitution).
*   **Sticky Context (Context7 Integration):** Keep the current problem statement and any actively invoked definitions (e.g., *[ADS §4.1]* citations) persistently visible—either in a side panel or sticky header. The student should never have to scroll back up to remember what they are proving.
*   **Distinct Visual Verdict Badges:** The Verification Footer must be unmistakable to build trust in the automated grader:
    *   🟢 **[PASS]**: Green badge. Accompanied by positive reinforcement.
    *   🔴 **[FAIL]**: Red badge. Accompanied by a clear, localized diagnosis and an L1/L2 hint.
    *   🟡 **[UNVERIFIABLE]**: Orange/Warning badge. Explicitly notes that the human must review (e.g., "outside harness coverage").
*   **The "One Action" Rule:** The final Next Step prompt must be visually isolated from the rest of the text (e.g., bolded, placed in an accented box, or immediately above the text input cursor). It must contain exactly *one* question or required action.

## 4. The Interaction Loop
Every interaction must feel like a tight, responsive REPL for math logic:
`Student Input -> Syntax Check -> Verify() -> Visual Verdict Badge -> Scaffolded Next Prompt`
