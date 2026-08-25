---
source_relative_path: "DM TXT/4-More_on_Sets/ads Methods of Proof for Sets.html"
source_sha256: "d09145dd480b390d7bc54b54af3d4e101bcf1e78f3ad3e4d645d339c25582a0b"
scope_class: active_candidate
displayed_section_or_chapter: "Section 4.1 Methods of Proof for Sets"
content_gap: true
missing_assets:
  - "external/images/distrib-venn-lhs.png"
  - "external/images/distrib-venn-rhs.png"
---

# Section 4.1 Methods of Proof for Sets

If \(A\text{,}\) \(B\text{,}\) and \(C\) are arbitrary sets, is it always true that \(A \cap  (B \cup  C) = (A \cap  B) \cup  (A \cap  C)\text{?}\)  There are a variety of ways that we could attempt to prove that this distributive law for intersection over union is indeed true.  We start with a common “non-proof” and then work toward more acceptable methods.

# Subsection 4.1.1 Examples and Counterexamples

We could, for example, let \(A = \{1, 2\}\text{,}\) \(B = \{5, 8, 10\}\text{,}\) and \(C = \{3, 2, 5\}\text{,}\) and determine whether the distributive law is true for these values of \(A\text{,}\) \(B\text{,}\) and \(C\text{.}\) In doing this we will have only determined that the distributive law is true for this one example. It does not prove the distributive law for all possible sets \(A\text{,}\) \(B\text{,}\) and \(C\) and hence is an invalid method of proof. However, trying a few examples has considerable merit insofar as it makes us more comfortable with the statement in question. Indeed, if the statement is not true for the example, we have disproved the statement.

> **Definition 4.1.1 — Counterexample.**

> An example that disproves a statement is called a counterexample.

> **Example 4.1.2 — Disproving distributivity of addition over multiplication.**

> From basic algebra we learned that multiplication is distributive over addition. Is addition distributive over multiplication? That is, is \(a + (b \cdot  c) = (a + b) \cdot  (a + c)\) always true? If we choose the values \(a = 3\text{,}\) \(b = 4\text{,}\) and \(c = 1\text{,}\) we find that \(3 + (4 \cdot  1) \neq  (3 + 4)\cdot (3 + 1)\text{.}\) Therefore, this set of values serves as a counterexample to a distributive law of addition over multiplication.

# Subsection 4.1.2 Proof Using Venn Diagrams

In this method, we illustrate both sides of the statement via a Venn diagram and determine whether both Venn diagrams give us the same “picture,” For example, the left side of the distributive law is developed in [Figure 4.1.3 [UNRESOLVED_INTERNAL_LINK]](s-proof-methods-sets.html#distrib-venn-lhs) and the right side in [Figure 4.1.4 [UNRESOLVED_INTERNAL_LINK]](s-proof-methods-sets.html#distrib-venn-rhs). Note that the final results give you the same shaded area.

The advantage of this method is that it is relatively quick and mechanical. The disadvantage is that it is workable only if there are a small number of sets under consideration. In addition, it doesn’t work very well in a static environment like a book or test paper.  Venn diagrams tend to work well if you have a potentially dynamic environment like a blackboard or video.

![MISSING FIGURE: described in detail following the image](GAP:external/images/distrib-venn-lhs.png)

![MISSING FIGURE: described in detail following the image](GAP:external/images/distrib-venn-rhs.png)

# Subsection 4.1.3 Proof using Set-membership Tables

Let \(A\) be a subset of a universal set \(U\) and let \(u\in U\text{.}\) To use this method we note that exactly one of the following is true: \(u \in  A\) or \(u\notin  A\text{.}\) Denote the situation where \(u \in  A\) by 1 and that where \(u \notin  A\) by 0. Working with two subsets of \(U\text{,}\) \(A\) and \(B\text{,}\) and \(u \in  U\text{,}\) there are four possible anwers to “Where is \(u\text{?}\)” What are they? The set-membership table for \(A \cup  B\) is:

![Table 4.1.5 . Membership Table for \(A \cup B\) \(A\) \(B\) \(A \cup B\) 0 0 0 0 1 1 1 0 1 1 1 1]()

This table illustrates that \(u\in A \cup  B\) if and only if \(u\in A\) or \(u \in  B\text{.}\)

In order to prove the distributive law via a set-membership table, write out the table for each side of the set statement to be proved and note that if \(S\) and \(T\) are two columns in a table, then the set statement \(S\) is equal to the set statement \(T\) if and only if corresponding entries in each row are the same.

To prove \(A \cap  (B \cup  C) = (A \cap  B) \cup  (A \cap  C)\text{,}\) first note that the statement involves three sets, \(A\text{,}\) \(B\text{,}\) and \(C\text{,}\) so there are \(2^3= 8\) possibilities for the membership of an element in the sets.

![Table 4.1.6 . Membership table to prove the distributive law of intersection over union \(A\) \(B\) \(C\) \(B \cup C\) \(A \cap B\) \(A \cap C\) \(A \cap (B \cup C)\) \((A \cap B) \cup (A \cap C)\) 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 1 0 1 0 0 0 0 0 1 1 1 0 0 0 0 1 0 0 0 0 0 0 0 1 0 1 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1]()

Since each entry in Column 7 is the same as the corresponding entry in Column 8, we have shown that \(A\cap  (B \cup  C) = (A\cap B) \cup  (A \cap C)\) for any sets \(A\text{,}\) \(B\text{,}\) and \(C\text{.}\) The main advantage of this method is that it is mechanical. The main disadvantage is that it is reasonable to use only for a relatively small number of sets. If we are trying to prove a statement involving five sets, there are \(2^5 = 32\) rows, which would test anyone’s patience doing the work by hand.

# Subsection 4.1.4 Proof Using Definitions

This method involves using definitions and basic concepts to prove the given statement. This procedure forces one to learn, relearn, and understand basic definitions and concepts. It helps individuals to focus their attention on the main ideas of each topic and therefore is the most useful method of proof. One does not learn a topic by memorizing or occasionally glancing at core topics, but by using them in a variety of contexts. The word proof panics most people; however, everyone can become comfortable with proofs. Do not expect to prove every statement immediately. In fact, it is not our purpose to prove every theorem or fact encountered, only those that illustrate methods and/or basic concepts. Throughout the text we will focus in on main techniques of proofs. Let’s illustrate by proving the distributive law.

*Proof Technique 1.*  State or restate the theorem so you understand what is given (the hypothesis) and what you are trying to prove (the conclusion).

> **Theorem 4.1.7 — The Distributive Law of Intersection over Union.**

> If \(A\text{,}\) \(B\text{,}\) and \(C\) are sets, then \(A\cap  (B \cup  C) = (A\cap B) \cup  (A \cap  C)\text{.}\)

*Proof Technique 2*

To prove that \(A\subseteq B\text{,}\) we must show that if \(x \in  A\text{,}\) then \(x \in  B\text{.}\)


To prove that \(A = B\text{,}\) we must show:


\(A\subseteq B\) and
\(B \subseteq A\text{.}\)

To further illustrate the Proof-by-Definition technique, let’s prove the following theorem.

> **Theorem 4.1.8 — Another Proof using Definitions.**

> If  \(A\text{,}\) \(B\text{,}\) and \(C\) are any sets, then \(A \times  (B \cap  C) = (A \times  B) \cap  (A \times  C)\text{.}\)

> **Exercise 1 . —**

> Prove the following:
> 
> Let \(A\text{,}\) \(B\text{,}\) and \(C\) be sets. If \(A\subseteq B\) and \(B\subseteq C\text{,}\) then \(A\subseteq C\text{.}\)
> 
> Let \(A\) and \(B\) be sets. Then \(A - B= A\cap B^c\) .
> Let \(A,B, \textrm{ and } C\) be sets. If (\(A\subseteq B\) and \(A\subseteq C\)) then \(A\subseteq B\cap C\text{.}\)
> 
> Let \(A \textrm{ and } B\) be sets. \(A\subseteq B\) if and only if \(B^c\subseteq A^c\) .
> Let \(A,B, \textrm{ and } C\) be sets. If \(A\subseteq B\) then \(A\times C \subseteq B\times C\text{.}\)

> **Exercise 2 . —**

> For any integer \(k\text{,}\) let \(k \mathbb{Z}=\{k\cdot j \mid j \in \mathbb{Z}\}\text{,}\) the multiples of \(k\text{.}\)

> 1. Prove that \(2\mathbb{Z} \cap 3\mathbb{Z} = 6 \mathbb{Z}\text{.}\)
> 2. Is it true  that \(2\mathbb{Z} \cap 4\mathbb{Z} = 8 \mathbb{Z}\text{?}\)  Explain your answer.

> **Exercise 3 . —**

> Disprove the following, assuming \(A, B, \textrm{ and } C\) are sets:
> 
> \(A - B = B - A\text{.}\)
> \(A\times B = B\times A\text{.}\)
> 
> \(A \cap   B = A  \cap   C\) implies \(B = C\text{.}\)
> 
> \(\displaystyle A \oplus  (B\cap C) = (A \oplus  B)\cap  (A \oplus C)\)

> **Exercise 4 . —**

> Let \(A, B, \textrm{ and } C\) be sets. Write the following in “if . . . then . . .” language and prove:
> 
> 
> \(x \in  B\) is a sufficient condition for \(x \in  A \cup B\text{.}\)
> 
> 
> \(A \cap B\cap C = \emptyset\) is a necessary condition for \(A \cap  B =\emptyset\text{.}\)
> 
> 
> \(A \cup  B = B\) is a necessary and sufficient condition for \(A\subseteq  B\text{.}\)

> **Exercise 5 . —**

> Prove by induction that if \(A\text{,}\) \(B_1\text{,}\) \(B_2\text{,}\) ... , \(B_n\) are sets, \(n\geq 2\text{,}\) then \(A\cap ( B_1 \cup  B_2\cup  \dots  \cup  B_n) = (A \cap B_1) \cup  (A \cap B_2 ) \cup  \dots \cup  (A\cap B_n)\text{.}\)

> **Exercise 6 . —**

> Let \(A\text{,}\) \(B\) and \(C\) be sets. Prove or disprove:
> 
> \begin{equation*}
> A \cap B \neq \emptyset,  B \cap C \neq \emptyset \Rightarrow A\cap C \neq \emptyset
> \end{equation*}
