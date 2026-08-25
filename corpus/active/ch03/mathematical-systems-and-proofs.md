---
source_relative_path: "DM TXT/3-Logic/ads Mathematical Systems and Proofs.html"
source_sha256: "0c2f49dff58a83cecf0bb53b245f602eb78b830749b2096034e3bdbc70802047"
scope_class: active_candidate
displayed_section_or_chapter: "Section 3.5 Mathematical Systems and Proofs"
content_gap: true
missing_assets:
  - "generated/sageplot/pyramid.svg"
---

# Section 3.5 Mathematical Systems and Proofs

# Subsection 3.5.1 Mathematical Systems

In this section, we present an overview of what a mathematical system is and how logic plays an important role in one. The axiomatic method that we will use here will not be duplicated with as much formality anywhere else in the book, but we hope an emphasis on how mathematical facts are developed and organized will help to unify the concepts we will present. The system of propositions and logical operators we have developed will serve as a model for our discussion. Roughly, a mathematical system can be defined as follows.

> **Definition 3.5.1 — Mathematical System.**

> A mathematical system consists of:

> A set or universe, \(U\text{.}\)
> 
> Definitions: sentences that explain the meaning of concepts that relate to the universe. Any term used in describing the universe itself is said to be undefined. All definitions are given in terms of these undefined concepts of objects.
> Axioms: assertions about the properties of the universe and rules for creating and justifying more assertions. These rules always include the system of logic that we have developed to this point.
> Theorems: the additional assertions mentioned above.

> **Example 3.5.2 — Euclidean Geometry.**

> In Euclidean geometry the universe consists of points and lines (two undefined terms). Among the definitions is a definition of parallel lines and among the axioms is the axiom that two distinct parallel lines never meet.

> **Example 3.5.3 — Propositional Calculus.**

> Propositional calculus is a formal name for the logical system that we’ve been discussing. The universe consists of propositions. The axioms are the truth tables for the logical operators and the key definitions are those of equivalence and implication. We use propositions to describe any other mathematical system; therefore, this is the minimum amount of structure that a mathematical system can have.

> **Definition 3.5.4 — Theorem.**

> A true proposition derived from the axioms of a mathematical system is called a theorem.

Theorems are normally expressed in terms of a finite number of propositions, \(p_1, p_2, . . . ,p_n\) , called the *premises*, and a proposition,\(C\text{,}\) called the *conclusion*. These theorems take the form

\begin{equation*}
p_1\land  p_2\land  \cdots  \land p_n\Rightarrow C
\end{equation*}

or more informally,

\begin{equation*}
p_1, p_2, . . . , \textrm{ and } p_n \textrm{ imply } C
\end{equation*}

For a theorem of this type, we say that the premises imply the conclusion. When a theorem is stated, it is assumed that the axioms of the system are true. In addition, any previously proven theorem can be considered an extension of the axioms and can be used in demonstrating that the new theorem is true. When the proof is complete, the new theorem can be used to prove subsequent theorems. A mathematical system can be visualized as an inverted pyramid with the axioms at the base and the theorems expanding out in various directions.

![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/pyramid.svg)

> **Definition 3.5.6 — Proof.**

> A proof of a theorem is a finite sequence of logically valid steps that demonstrate that the premises of a theorem imply its conclusion.

Exactly what constitutes a proof is not always clear. For example, a research mathematician might require only a few steps to prove a theorem to a collegue, but might take an hour to give an effective proof to a class of students. Therefore, what constitutes a proof often depends on the audience. But the audience is not the only factor. One of the most famous theorems in graph theory, [The Four-Color Theorem [UNRESOLVED_INTERNAL_LINK]](s-planarity-and-colorings.html#theorem-four-color-theorem), was proven in 1976, after over a century of effort by many mathematicians.  Part of the proof consisted of having a computer check many different graphs for a certain property. Without the aid of the computer, this checking would have taken years. In the eyes of some mathematicians, this proof was considered questionable. Shorter proofs have been developed since 1976 and there is no controversy associated with The Four Color Theorem at this time.

# Subsection 3.5.2 Direct Proof

Theoretically, you can prove anything in propositional calculus with truth tables. In fact, the laws of logic stated in Section 3.4 are all theorems.  Propositional calculus is one of the few mathematical systems for which any valid sentence can be determined true or false by mechanical means. A program to write truth tables is not too difficult to write; however, what can be done theoretically is not always practical. For example,

\begin{equation*}
a, a\to  b, b\to  c, . . . ,y\to z\Rightarrow z
\end{equation*}

is a theorem in propositional calculus. However, suppose that you wrote such a program and you had it write the truth table for

\begin{equation*}
(a\land  (a\to  b)\land ( b\to  c)\land \cdots \land (y\to z))\to z
\end{equation*}

The truth table will have \(2^{26}\) cases. At one million cases per second, it would take approximately one hour to verify the theorem.  Now if you decided to check a similar theorem,

\begin{equation*}
p_1,p_1\to p_2,\ldots  ,p_{99}\to p_{100}\Rightarrow p_{100}
\end{equation*}

you would really have time trouble. There would be \(2^{100} \approx 1.26765\times 10^{30}\) cases to check in the truth table.  At one million cases per second it would take approximately \(1.46719\times 10^{19}\) days to check all cases.  For most of the remainder of this section, we will discuss an alternate method for proving theorems in propositional calculus. It is the same method that we will use in a less formal way for proofs in other systems. Formal axiomatic methods would be too unwieldy to actually use in later sections. However, none of the theorems in later chapters would be stated if they couldn’t be proven by the axiomatic method.

We will introduce two types of proof here, direct and indirect.

> **Example 3.5.7 — A typical direct proof.**

> This is a theorem: \(p \rightarrow  r, q\rightarrow s,p\lor q\Rightarrow s\lor r\text{.}\)   A direct proof of this theorem is:

> ![Table 3.5.8 . Direct proof of \(p \rightarrow r, q\rightarrow s,p\lor q\Rightarrow s\lor r\) Step Proposition Justification 1. \(p \lor q\) Premise 2. \(\neg p \rightarrow q\) (1), conditional rule 3. \(q \rightarrow s\) Premise 4. \(\neg p \rightarrow s\) (2), (3), chain rule 5. \(\neg s \rightarrow p\) (4), contrapositive 6. \(p \rightarrow r\) Premise 7. \(\neg s \rightarrow r\) (5), (6), chain rule 8. \(s \lor r\) (7), conditional rule \(\square\)]()

Note that \(\square\) marks the end of a proof.

[Example 3.5.7 [UNRESOLVED_INTERNAL_LINK]](s-math-systems.html#proof-3-5-1) illustrates the usual method of formal proof in a formal mathematical system. The rules governing these proofs are:

A proof must end in a finite number of steps.
Each step must be either a premise or a proposition that is implied from previous steps using any valid equivalence or implication.
For a direct proof, the last step must be the conclusion of the theorem. For an indirect proof (see below), the last step must be a contradiction.
Justification Column. The column labeled “justification” is analogous to the comments that appear in most good computer programs. They simply make the proof more readable.

> **Example 3.5.9 — Two proofs of the same theorem.**

> Here are two direct proofs of \(\neg p \lor  q, s\lor  p, \neg q \Rightarrow  s\text{:}\)

> ![Table 3.5.10 . Direct proof of \(\neg p \lor q, s\lor p, \neg q \Rightarrow s\) 1. \(\neg p \lor q\) Premise 2. \(\neg q\) Premise 3. \(\neg p\) Disjunctive simplification, (1), (2) 4. \(s\lor p\) Premise 5. \(s\) Disjunctive simplification, (3), (4). \(\square\)]()

> You are invited to justify the steps in this second proof:

> ![Table 3.5.11 . Alternate proof of \(\neg p \lor q, s\lor p, \neg q \Rightarrow s\) 1. \(\neg p \lor q\) 2. \(\neg q \rightarrow \neg p\) 3. \(s\lor p\) 4. \(p \lor s\) 5. \(\neg p \to s\) 6. \(\neg q \rightarrow s\) 7. \(\neg q\) 8. \(s\) \(\square\)]()

The conclusion of a theorem is often a conditional proposition. The condition of the conclusion can be included as a premise in the proof of the theorem. The object of the proof is then to prove the consequence of the conclusion. This rule is justified by the logical law

\begin{equation*}
p \rightarrow  (h \rightarrow  c) \Leftrightarrow  (p \land  h) \rightarrow  c
\end{equation*}

> **Example 3.5.12 — Example of a proof with a conditional conclusion.**

> The following proof of \(p \to  (q \rightarrow  s), \neg r  \lor p, q \Rightarrow r \rightarrow s\) includes \(r\) as a fourth premise. Inference of truth of \(s\) completes the proof.

> ![Table 3.5.13 . Proof of a theorem with a conditional conclusion. 1. \(\neg r \lor p\) Premise 2. \(r\) Added premise 3. \(p\) (1), (2), disjunction simplification 4. \(p \rightarrow (q \to s)\) Premise 5. \(q\rightarrow s\) (3), (4), detachment 6. \(q\) Premise 7. \(s\) (5), (6), detachment. \(\square\)]()

# Subsection 3.5.3 Indirect Proof

Consider a theorem \(P\Rightarrow C\text{,}\) where \(P\) represents \(p_1, p_2, . . . , \textrm{ and } p_n\text{,}\) the premises. The method of indirect proof is based on the equivalence \(P\rightarrow C\Leftrightarrow \neg (P\land  \neg C)\text{.}\) In words, this logical law states that if \(P \Rightarrow  C\text{,}\) then \(P \land  \neg  C\) is always false; that is, \(P \land  \neg C\) is a contradiction. This means that a valid method of proof is to negate the conclusion of a theorem and add this negation to the premises. If a contradiction can be implied from this set of propositions, the proof is complete. For the proofs in this section, a contradiction will often take the form \(t \land \neg t\text{.}\)

For proofs involving numbers, a contradiction might be \(1 = 0\) or \(0 < 0\text{.}\) Indirect proofs involving sets might conclude with \(x \in  \emptyset\) or (\(x \in  A\) and \(x \in  A^c\)). Indirect proofs are often more convenient than direct proofs in certain situations.  Indirect proofs are often called *proofs by contradiction*.

> **Example 3.5.14 — An Indirect Proof.**

> Here is an example of an indirect proof of the theorem in [Example 3.5.7 [UNRESOLVED_INTERNAL_LINK]](s-math-systems.html#proof-3-5-1).

> ![Table 3.5.15 . An Indirect proof of \(p \rightarrow r, q\rightarrow s,p\lor q\Rightarrow s\lor r\) 1. \(\neg (s \lor r)\) Negated conclusion 2. \(\neg s \land \neg r\) DeMorgan’s Law, (1) 3. \(\neg s\) Conjunctive simplification, (2) 4. \(q\to s\) Premise 5. \(\neg q\) Indirect reasoning, (3), (4) 6. \(\neg r\) Conjunctive simplification, (2) 7. \(p \rightarrow r\) Premise 8. \(\neg p\) Indirect reasoning, (6), (7) 9. \((\neg p) \land (\neg q)\) Conjunctive, (5), (8) 10. \(\neg (p \lor q)\) DeMorgan’s Law, (9) 11. \(p \lor q\) Premise 12. \(0\) (10), (11) \(\square\)]()

> **Example 3.5.17 — Yet Another Indirect Proof.**

> Here is an indirect proof of \(a \rightarrow  b, \neg (b \lor  c ) \Rightarrow  \neg  a\text{.}\)

> ![Table 3.5.18 . Indirect proof of \(a \rightarrow b, \neg (b \lor c ) \Rightarrow \neg a\) 1. \(a\) Negation of the conclusion 2. \(a\to b\) Premise 3. \(b\) (1), (2), detachment 4. \(b \lor c\) (3), disjunctive addition 5. \(\neg (b \lor c)\) Premise 6. \(0\) (4), (5) \(\square\)]()

As we mentioned at the outset of this section, we are only presenting an overview of what a mathematical system is. For greater detail on axiomatic theories, see Stoll (1961). An excellent description of how propositional calculus plays a part in artificial intelligence is contained in Hofstadter (1980). If you enjoy the challenge of constructing proofs in propositional calculus, you should enjoy the game WFF’N PROOF (1962), by L.E. Allen.

> **Exercise 1 . —**

> Prove with truth tables:

> \(\displaystyle p\lor  q, \neg q\Rightarrow  p\)
> \(\displaystyle p \rightarrow  q, \neg q \Rightarrow  \neg p\)

> **Exercise 2 . —**

> Prove with truth tables:

> \(\displaystyle q, \neg q\Rightarrow  p\)
> \(\displaystyle p \rightarrow  q \Leftrightarrow  \neg p \lor  q\)

> **Exercise 3 . —**

> Give direct and indirect proofs of:

> \(a \rightarrow  b, c \rightarrow  b, d\rightarrow  (a \lor  c), d\Rightarrow  b\text{.}\)
> \((p\to q) \land (r\to s), (q\rightarrow t) \land  (s \to  u), \neg (t \land u), p \rightarrow  r \Rightarrow  \neg p\text{.}\)
> \(p\to (q\to r),\neg s \lor p,q\Rightarrow s\to r\text{.}\)
> \(p\rightarrow  q, q\rightarrow  r, \neg (p \land  r), p \lor  r \Rightarrow  r\text{.}\)
> \(\displaystyle \neg q, p\to q, p\lor t \Rightarrow t\)

> **Exercise 4 . —**

> Give direct and indirect proofs of:

> \(p\rightarrow  q, \neg r\rightarrow  \neg q, \neg r \Rightarrow  \neg p\text{.}\)
> \(p\rightarrow  \neg q, \neg r\rightarrow  q, p \Rightarrow  r\text{.}\)
> \(a \lor  b, c \land  d, a \rightarrow  \neg c \Rightarrow  b\text{.}\)

> **Exercise 5 . —**

> Are the following arguments valid? If they are valid, construct formal proofs; if they aren’t valid, explain why not.

> If wages increase, then there will be inflation. The cost of living will not increase if there is no inflation. Wages will increase. Therefore, the cost of living will increase.
> If the races are fixed or the casinos are crooked, then the tourist trade will decline. If the tourist trade decreases, then the police will be happy. The police force is never happy. Therefore, the races are not fixed.

> **Exercise 6 . —**

> My salad contains beets and okra.  If my salad contains cottage cheese then it doesn’t contain beets. My salad contains cottage cheese or hummus.  Therefore, my salad contains hummus.

> **Exercise 7 . —**

> Describe how \(p_1,p_1\to p_2,\ldots  ,p_{99}\to p_{100}\Rightarrow p_{100}\) could be proved in 199 steps.
