---
source_relative_path: "DM TXT/4-More_on_Sets/ads Laws of Set Theory.html"
source_sha256: "4c26e1a935e068d3e128102846971ea5c29ca6ed1237a2976628bf45e87c4291"
scope_class: active_candidate
displayed_section_or_chapter: "Section 4.2 Laws of Set Theory"
---

# Section 4.2 Laws of Set Theory

# Subsection 4.2.1 Tables of Laws

The following basic set laws can be derived using either the Basic Definition or the Set-Membership approach and can be illustrated by Venn diagrams.

![Table 4.2.1 . Basic Laws of Set Theory Commutative Laws (1) \(A \cup B = B \cup A\) ( \(1^{\prime}\) ) \(A \cap B = B\cap A\) Associative Laws (2) \(A \cup (B \cup C)= (A\cup B)\cup C\) ( \(2^{\prime}\) ) \(A \cap (B \cap C) = (A \cap B) \cap C \) Distributive Laws (3) \(A\cap (B \cup C)=(A\cap B )\cup (A\cap C)\) ( \(3^{\prime}\) ) \(A \cup (B \cap C) = (A \cup B ) \cap (A\cup C)\) Identity Laws (4) \(A \cup \emptyset = \emptyset \cup A = A\) ( \(4^{\prime}\) ) \(A \cap U = U \cap A = A\) Complement Laws (5) \(A\cup A^c= U\) ( \(5^{\prime}\) ) \(A\cap A^c= \emptyset\) Idempotent Laws (6) \(A \cup A = A\) ( \(6^{\prime}\) ) \(A\cap A = A\) Null Laws (7) \(A \cup U = U\) ( \(7^{\prime}\) ) \(A \cap \emptyset =\emptyset\) Absorption Laws (8) \(A \cup (A\cap B) = A\) ( \(8^{\prime}\) ) \(A\cap (A \cup B) = A\) DeMorgan’s Laws (9) \((A \cup B)^c= A^c\cap B^c\) ( \(9^{\prime}\) ) \((A\cap B)^c = A^c \cup B^c\) Involution Law (10) \((A^c)^c= A\)]()

It is quite clear that most of these laws resemble or, in fact, are analogues of laws in basic algebra and the algebra of propositions.

# Subsection 4.2.2 Proof Using Previously Proven Theorems

Once a few basic laws or theorems have been established, we frequently use them to prove additional theorems. This method of proof is usually more efficient than that of proof by Definition. To illustrate, let us prove the following Corollary to the Distributive Law.   The term "corollary" is used for theorems that can be proven with relative ease from previously proven theorems.

> **Corollary 4.2.2 — A Corollary to the Distributive Law of Sets.**

> Let A and B be sets. Then \((A\cap  B) \cup  (A\cap  B^c) = A\text{.}\)

# Subsection 4.2.3 Proof Using the Indirect Method/Contradiction

The procedure one most frequently uses to prove a theorem in mathematics is the Direct Method, as illustrated in [Theorem 4.1.7 [UNRESOLVED_INTERNAL_LINK]](s-proof-methods-sets.html#th-distr-law-i-over-u) and [Theorem 4.1.8 [UNRESOLVED_INTERNAL_LINK]](s-proof-methods-sets.html#th-set-proof-example2). Occasionally there are situations where this method is not applicable. Consider the following:

> **Theorem 4.2.3 — An Indirect Proof in Set Theory.**

> Let \(A, B, C\) be sets. If \(A\subseteq B\) and \(B\cap C = \emptyset\text{,}\) then \(A\cap C = \emptyset\text{.}\)

In the exercises that follow it is most important that you outline the logical procedures or methods you use.

> **Exercise 1 . —**

> Prove the associative law for intersection (Law \(2^{\prime}\)) with a Venn diagram.
> Prove DeMorgan’s Law (Law 9) with a membership table.
> Prove the Idempotent Law (Law 6) using basic definitions.

> **Exercise 2 . —**

> Prove the Absorption Law (Law \(8^{\prime}\))  with a membership table.
> Prove the Involution Law (Law 10) using basic definitions.

> **Exercise 3 . —**

> Prove the following using the set theory laws, as well as any other theorems proved so far.

> \(\displaystyle A \cup  (B - A) = A \cup  B\)
> \(\displaystyle A - B = B^c - A ^c\)
> \(\displaystyle A\subseteq B, A\cap C \neq \emptyset  \Rightarrow  B\cap C \neq \emptyset\)
> \(\displaystyle A\cap (B - C) = (A\cap B) - (A\cap C)\)
> \(\displaystyle A - (B \cup  C) = (A - B)\cap (A - C)\)

> **Exercise 4 . —**

> Use previously proven theorems to prove the following.

> \(\displaystyle A \cap (B\cap C)^c= (A\cap B^c)\cup (A\cap C^{c })\)
> \(\displaystyle A \cap (B\cap (A\cap B)^c)= \emptyset\)
> \(\displaystyle (A\cap B) \cup  B^c = A \cup  B^c\)
> \(A \cup  (B - C) = (A \cup  B) - (C - A)\text{.}\)

> **Exercise 5 . — Hierarchy of Set Operations.**

> The rules that determine the order of evaluation in a set expression that involves more than one operation are similar to the rules for logic. In the absence of parentheses, complementations are done first, intersections second, and unions third. Parentheses are used to override this order. If the same operation appears two or more consecutive times, evaluate from left to right. In what order are the following expressions performed?

> \(A \cup  B^c\cap C\text{.}\)
> \(A\cap B \cup  C\cap B\text{.}\)
> \(\displaystyle A \cup  B \cup  C^c\)

> **Exercise 6 . —**

> There are several ways that we can use to format the proofs in this chapter. One that should be familiar to you from Chapter 3 is illustrated with the following alternate proof of part (a) in [Theorem 4.1.7 [UNRESOLVED_INTERNAL_LINK]](s-proof-methods-sets.html#th-distr-law-i-over-u):

> ![Table 4.2.4 . An alternate format for the proof of Theorem 4.1.7 (1) \(x \in A \cap (B \cup C)\) Premise (2) \((x \in A) \land (x \in B \cup C)\) (1), definition of intersection (3) ( \(x \in A) \land ((x \in B) \lor (x \in C))\) (2), definition of union (4) \((x \in A)\land (x\in B)\lor (x \in A)\land (x\in C)\) (3), distribute \(\land\) over \(\lor\) (5) \((x \in A\cap B) \lor (x \in A \cap C)\) (4), definition of intersection (6) \(x \in (A \cap B) \cup (A \cap C)\) (5), definition of union \(\square\)]()

> Prove part (b) of [Theorem 4.1.8 [UNRESOLVED_INTERNAL_LINK]](s-proof-methods-sets.html#th-set-proof-example2) and [Theorem 4.2.3 [UNRESOLVED_INTERNAL_LINK]](s-laws-of-set-theory.html#theorem-example-sets-contradiction) using this format.
