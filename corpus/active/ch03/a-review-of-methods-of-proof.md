---
source_relative_path: "DM TXT/3-Logic/ads A Review of Methods of Proof.html"
source_sha256: "a63951b99f8b4a69a341f521e0c7c2caa5ecaa184e39a062ee3ffc777bd7696c"
scope_class: active_candidate
displayed_section_or_chapter: "Section 3.9 A Review of Methods of Proof"
---

# Section 3.9 A Review of Methods of Proof

One of the major goals of this chapter is to acquaint the reader with the key concepts in the nature of proof in logic, which of course carries over into all areas of mathematics and its applications. In this section we will stop, reflect, and “smell the roses,” so that these key ideas are not lost in the many concepts covered in logic. In Chapter 4 we will use set theory as a vehicle for further practice and insights into methods of proof.

# Subsection 3.9.1 Key Concepts in Proof

All theorems in mathematics can be expressed in the form “If \(P\) then \(C\)” (\(P \Rightarrow  C\)), or in the form “\(C_1\) if and only if \(C_2\)” (\(C_1 \Leftrightarrow C_2\)). The latter is equivalent to “If \(C_1\) then \(C_2\text{,}\)” and “If \(C_2\) then \(C_1\text{.}\)”

In “If \(P\) then \(C\text{,}\)” \(P\) is the premise (or hypothesis) and \(C\) is the conclusion. It is important to realize that a theorem makes a statement that is dependent on the premise being true.

There are two basic methods for proving \(P \Rightarrow  C\text{:}\)

*Directly:* Assume \(P\) is true and prove \(C\) is true.

*Indirectly (or by contradiction):*  Assume \(P\) is true and \(C\) is false and prove that this leads to a contradiction of some premise, theorem, or basic truth.

The method of proof for “If and only if” theorems is found in the law \((P\leftrightarrow  C) \Leftrightarrow
((P \rightarrow  C) \land  (C \rightarrow  P))\text{.}\) Hence to prove an “If and only if” statement one must prove an “if . . . then ...” statement and its converse.

The initial response of most people when confronted with the task of being told they must be able to read and do proofs is often “Why?” or “I can’t do proofs.” To answer the first question, doing proofs or problem solving, even on the most trivial level, involves being able to read statements. First we must understand the problem and know the hypothesis; second, we must realize when we are done and we must understand the conclusion. To apply theorems or algorithms we must be able to read theorems and their proofs intelligently.

To be able to do the actual proofs of theorems we are forced to learn:

the actual meaning of the theorems, and
the basic definitions and concepts of the topic discussed.

For example, when we discuss rational numbers and refer to a number \(x\) as being rational, this means we can substitute a fraction \(\frac{p}{q}\) in place of \(x\text{,}\) with the understanding that \(p\) and \(q\) are integers and \(q\neq 0\text{.}\) Therefore, to prove a theorem about rational numbers it is absolutely necessary that you know what a rational number “looks like.”

It’s easy to comment on the response, “I cannot do proofs.”  Have you tried? As elementary school students we may have been in awe of anyone who could handle algebraic expressions, especially complicated ones. We learned by trying and applying ourselves. Maybe we cannot solve all problems in algebra or calculus, but we are comfortable enough with these subjects to know that we can solve many and can express ourselves intelligently in these areas. The same remarks hold true for proofs.

# Subsection 3.9.2 The Art of Proving \(P \Rightarrow C\)

First one must completely realize what is given, the hypothesis. The importance of this is usually overlooked by beginners. It makes sense, whenever you begin any task, to spend considerable time thinking about the tools at your disposal. Write down the premise in precise language. Similarly, you have to know when the task is finished. Write down the conclusion in precise language. Then you usually start with \(P\) and attempt to show that \(C\) follows logically. How do you begin? Basically you attack the proof the same way you solve a complicated equation in elementary algebra. You may not know exactly what each and every step is but you must try something. If we are lucky, \(C\) follows naturally; if it doesn’t, try something else. Often what is helpful is to work backward from \(C\text{.}\) Finally, we have all learned, possibly the hard way, that mathematics is a participating sport, not a spectator sport. One learns proofs by doing them, not by watching others do them. We give several illustrations of how to set up the proofs of several examples. Our aim here is not to prove the statements given, but to concentrate on the logical procedure.

> **Example 3.9.1 — The Sum of Odd Integers.**

> We will outline a proof that the sum of any two odd integers is even. Our first step will be to write the theorem in the familiar conditional form: If \(x\) and \(y\) are odd integers, then \(x+y\) is even. The premise and conclusion of this theorem should be clear now. Notice that if \(x\) and \(y\) are not both odd, then the conclusion may or may not be true. Our only objective is to show that the truth of the premise forces the conclusion to be true. Therefore, we can express the integers \(x\) and \(y\) in the form that all odd integers take; that is:
> 
> \begin{equation*}
> n \in  \mathbb{Z} \textrm{ is odd implies that } (\exists m\in \mathbb{Z}) (n = 2m + 1)
> \end{equation*}
> 
> This observation allows us to examine the sum  \(x+y\) and to verify that it must be even.

> One final important point: This example involves two odd integers that may or may not be equal.  If we use the fact that \(x\) is odd and infer that \(x=2m+1\) for some integer \(m\text{,}\) we can do a similar thing with \(y\text{.}\) However, in this context we cannot write \(y=2m+1\) since we have already linked \(m\) to \(x\text{.}\)  We need to use a different variable, maybe \(q\) or \(m'\) - any other symbol that is not already used in our discussion.

> **Example 3.9.2 — The Square of an Even Integer.**

> Let \(n \in  \mathbb{Z}\text{.}\) We will outline a proof that \(n^2\) is even if and only if \(n\) is even.

> Outline of a proof: Since this is an “If and only if” theorem we must prove two things:

> (\(\Rightarrow \)) If \(n^2\) is even, then \(n\) is even. To do this directly, assume that \(n^{2 }\) is even and prove that \(n\) is even.   To do this indirectly, assume \(n^2\) is even and that \(n\) is odd, and reach a contradiction.   It turns out that the latter of the two approaches is easiest here.
> (\(\Leftarrow \)) If \(n\) is even, then \(n^2\) is even. To do this directly, assume that \(n\) is even and prove that \(n^2\) is even.

> Now that we have broken the theorem down into two parts and know what to prove, we proceed to prove the two implications. The final ingredient that we need is a convenient way of describing even integers. When we refer to an integer \(n\) (or \(m\text{,}\) or \(k\text{,.}\) . . ) as even, we can always replace it with a product of the form \(2q\text{,}\) where \(q\) is an integer (more precisely, \(\left.(\exists q) _{\mathbb{Z}} (n = 2q)\right)\text{.}\) In other words, for an integer to be even it must have a factor of two in its prime decomposition.

> **Example 3.9.3 — \(\sqrt{2}\) is irrational.**

> Our final example will be an outline of the proof that the square root of 2 is irrational (not an element of \(\mathbb{Q}\)). This is an example of the theorem that does not appear to be in the standard \(P \Rightarrow  C\) form. One way to rephrase the theorem is: If \(x\) is a  rational number, then \(x^2\neq 2\text{.}\) A direct proof of this theorem would require that we verify that the square of every rational number is not equal to 2. There is no convenient way of doing this, so we must turn to the indirect method of proof. In such a proof, we assume that \(x\) is a  rational number and that \(x^2=2\text{.}\) This will lead to a contradiction. In order to reach this contradiction, we need to use the following facts:

> A rational number is a quotient of two integers.
> Every fraction can be reduced to lowest terms, so that the numerator and denominator have no common factor greater than 1.
> If \(n\) is an integer, \(n^2\) is even if and only if \(n\) is even.

> **Exercise 1 . —**

> Prove that the sum of two odd positive integers is an even positive integer. You might want to read [Example 3.9.1 [UNRESOLVED_INTERNAL_LINK]](s-proof-review.html#ex-sumsofodds) before attempting this.

> **Exercise 2 . —**

> Write out a complete proof that if \(n\) is an integer, \(n^2\) is even if and only if \(n\) is even.

> **Exercise 3 . —**

> Write out a complete proof that \(\sqrt{2}\) is irrational.

> **Exercise 4 . —**

> Prove that the cube root of 2 is an irrational number.

> **Exercise 5 . —**

> Prove that if \(x\) and \(y\) are real numbers such that \(x + y \leq  1\text{,}\) then  \(x\leq \frac{1}{2}\) or \(y\leq  \frac{1}{2}\text{.}\)
