---
source_relative_path: "DM TXT/3-Logic/ads The Laws of Logic.html"
source_sha256: "f7e9e5bb2599062355436f44dd54101a2eaa562c0e2645e15f3ce5f5711d13bf"
scope_class: active_candidate
displayed_section_or_chapter: "Section 3.4 The Laws of Logic"
---

# Section 3.4 The Laws of Logic

# Subsection 3.4.1

In this section, we will list the most basic equivalences and implications of logic. Most of the equivalences listed in Table [Table 3.4.3 [UNRESOLVED_INTERNAL_LINK]](s-logic-laws.html#table-equivalences) should be obvious to the reader. Remember, 0 stands for contradiction, 1 for tautology.  Many logical laws are similar to algebraic laws.  For example, there is a logical law corresponding to the associative law of addition, \(a + (b + c) = (a + b) + c\text{.}\)  In fact, associativity of both conjunction and disjunction are among the laws of logic. Notice that with one exception, the laws are paired in such a way that exchanging the symbols \(\land\text{,}\) \(\lor\text{,}\) 1 and 0 for \(\lor\text{,}\) \(\land\text{,}\) 0, and 1, respectively, in any law gives you a second law. For example,  \(p \lor  0\Leftrightarrow p\) results in \(p \land  1 \Leftrightarrow p\text{.}\) This is called a *duality principle*. For now, think of it as a way of remembering two laws for the price of one. We will leave it to the reader to verify a few of these laws with truth tables. However, the reader should be careful in applying duality to the conditional operator and implication since the dual involves taking the converse. For example, the dual of \(p \land  q\Rightarrow p\) is \(p \lor  q \Leftarrow  p\text{,}\) which is usually written \(p\Rightarrow p \lor  q\text{.}\)

> **Example 3.4.1 — Verification of an Identity Law.**

> The Identity Law can be verified with this truth table.  The fact that \((p \land  1)\leftrightarrow p\) is a tautology serves as a valid proof.

> ![Table 3.4.2 . Truth table to demonstrate the identity law for conjunction. \(p\) \(1\) \(p\land 1 \) \((p\land 1)\leftrightarrow p\) 0 1 0 1 1 1 1 1]()

Some of the logical laws in Table [Table 3.4.4 [UNRESOLVED_INTERNAL_LINK]](s-logic-laws.html#table-implications) might be less obvious to you. For any that you are not comfortable with, substitute actual propositions for the logical variables. For example, if \(p\) is “John owns a pet store” and \(q\) is “John likes pets,” the detachment law should make sense.

![Table 3.4.3 . Basic Logical Laws - Equivalences Commutative Laws \(p \lor q\Leftrightarrow q\lor p\) \(p \land q\Leftrightarrow q \land p\) Associative Laws \((p \lor q) \lor r \Leftrightarrow p \lor (q \lor r)\) ( \(p \land q) \land r\Leftrightarrow p \land (q \land r)\) Distributive Laws \(p \land (q \lor r) \Leftrightarrow (p \land q ) \lor (p \land r)\) \(p \lor (q \land r) \Leftrightarrow (p \lor q) \land (p \lor r)\) Identity Laws \(p \lor 0\Leftrightarrow p\) \(p \land 1 \Leftrightarrow p\) Negation Laws \(p\land \neg p\Leftrightarrow 0\) \(p\lor \neg p\Leftrightarrow 1\) Idempotent Laws \(p \lor p \Leftrightarrow p\) \(p\land p \Leftrightarrow p\) Null Laws \(p \land 0 \Leftrightarrow 0\) \(p \lor 1 \Leftrightarrow 1\) Absorption Laws \(p \land (p\lor q)\Leftrightarrow p\) \(p \lor (p \land q) \Leftrightarrow p\) DeMorgan’s Laws \(\neg (p \lor q) \Leftrightarrow (\neg p) \land (\neg q)\) \(\neg (p \land q) \Leftrightarrow (\neg p) \lor (\neg q)\) Involution Law \(\neg (\neg p)\Leftrightarrow p\)]()

![Table 3.4.4 . Basic Logical Laws - Common Implications and Equivalences Detachment (AKA Modus Ponens) \((p \rightarrow q) \land p\Rightarrow q\) Indirect Reasoning (AKA Modus Tollens) \((p \to q) \land \neg q \Rightarrow \neg p\) Disjunctive Addition \(p\Rightarrow (p\lor q)\) Conjunctive Simplification \((p \land q) \Rightarrow p\) and \((p \land q) \Rightarrow q\) Disjunctive Simplification \((p \lor q) \land \neg p \Rightarrow q\) and \((p \lor q) \land \neg q\Rightarrow p\) Chain Rule \((p \to q) \land ( q \rightarrow r) \Rightarrow (p\to r)\) Conditional Equivalence \(p \rightarrow q \Leftrightarrow \neg p \lor q\) Biconditional Equivalences \((p \leftrightarrow q) \Leftrightarrow (p\rightarrow q) \land (q \rightarrow p)\Leftrightarrow (p \land q) \lor (\neg p \land \neg q)\) Contrapositive \((p\to q) \Leftrightarrow (\neg q \to \neg p)\)]()

> **Exercise 1 . —**

> Write the following in symbolic notation and determine whether it is a tautology: “If I study then I will learn. I will not learn. Therefore, I do not study.”

> **Exercise 2 . —**

> Show that the common fallacy \((p\to  q) \land  \neg p \Rightarrow  \neg q\) is not a law of logic.

> **Exercise 3 . —**

> Describe, in general, how duality can be applied to implications if we introduce the relation \(\Leftarrow\text{,}\) read “is implied by.”  We define this relation by
> 
> \begin{equation*}
> (p \Leftarrow q) \Leftrightarrow (q \Rightarrow p)\text{.}
> \end{equation*}

> **Exercise 4 . —**

> Write the dual of the following statements:

> \(\displaystyle (p \land q)\Rightarrow p\)
> \(\displaystyle (p\lor q)\land \neg q\Rightarrow p\)
