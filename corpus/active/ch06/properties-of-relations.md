---
source_relative_path: "DM TXT/6-Relations/ads Properties of Relations.html"
source_sha256: "0a34c1668e9da8fda5dc18ab865bbbd05558ddaaee96c0fc51d2da4805a31a12"
scope_class: active_candidate
displayed_section_or_chapter: "Section 6.3 Properties of Relations"
content_gap: true
missing_assets:
  - "external/images/exercises-6-digraphs.png"
  - "external/images/fig-sol-6-3-11.png"
  - "external/images/fig-sol-6-3-5.png"
  - "external/images/pentagonal-digraph.png"
  - "external/images/pentagonal-hasse.png"
  - "external/images/subsets_2_hasse.png"
  - "generated/sageplot/graph-6-3-5.svg"
---

# Section 6.3 Properties of Relations

# Subsection 6.3.1 Individual Properties

Consider the set \(B = \{1, 2, 3, 4, 6, 12, 36, 48\}\) and the relations “divides” and \(\leq \) on \(B\text{.}\) We notice that these two relations on \(B\) have three properties in common:

Every element in \(B\) divides itself and is less than or equal to itself. This is called the reflexive property.
If we search for two elements from \(B\) where the first divides the second and the second divides the first, then we are forced to choose the two numbers to be the same. In other words, no two *different* numbers are related in both directions. The reader can verify that a similar fact is true for the relation \(\leq \) on \(B\text{.}\) This is called the antisymmetric property.
Next if we choose three values (not necessarily distinct) from \(B\) such that the first divides the second and the second divides the third, then we always find that the first number divides the third.  Again, the same is true if we replace “divides” with “is less than or equal to.” This is called the transitive property.

Relations that satisfy these properties are of special interest to us. Formal definitions of the properties follow.

> **Definition 6.3.1 — Reflexive Relation.**

> Let \(A\) be a set and let \(r\) be a relation on \(A\text{.}\) Then \(r\) is reflexive if and only if \(a r a\) for all \(a \in A\text{.}\)

> **Definition 6.3.2 — Antisymmetric Relation.**

> Let \(A\) be a set and let \(r\) be a relation on \(A\text{.}\)  Then \(r\) is antisymmetric if and only if whenever \(a r b\) and \(a \neq  b\) then \(b r a\) is false.

An equivalent condition for antisymmetry is that if \(a r b\) and  \(b r a\) then \(a = b\text{.}\) You are encouraged to convince yourself that this is true.  This condition is often more convenient to prove than the definition, even though the definition is probably easier to understand.

A word of warning about antisymmetry: Students frequently find it difficult to understand this definition. Keep in mind that this term is defined through an “If...then...” statement. The question that you must ask is: Is it true that whenever there are elements \(a\) and \(b\) from \(A\) where \(a r b\) and \(a \neq  b\text{,}\) it follows that \(b\) is not related to \(a\text{?}\) If so, then the relation  is antisymmetric.

Another way to determine whether a relation is antisymmetric is to examine (or imagine) its digraph. The relation is not antisymmetric if there exists a pair of vertices that are connected by edges in both directions.

> **Definition 6.3.3 — Transitive Relation.**

> Let \(A\) be a set and let \(r\) be a relation on \(A\text{.}\) \(r\) is transitive if and only if whenever \(a r b\) and \(b r c\) then \(a r c\text{.}\)

# Subsection 6.3.2 Partial Orderings

Not all relations have all three of the properties discussed above, but those that do are a special type of relation.

> **Definition 6.3.4 — Partial Ordering.**

> A relation on a set \(A\) that is reflexive, antisymmetric, and transitive is called a partial ordering on \(A\text{.}\) A set on which there is a partial ordering relation defined is called a partially ordered set or poset.

> **Example 6.3.5 — Set Containment as a Partial Ordering.**

> Let \(A\) be a set. Then \(\mathcal{P}(A)\) together with the relation \(\subseteq\) (set containment) is a poset. To prove this we observe that the three properties hold, as discussed in Chapter 4.

> Let \(B \in  \mathcal{P}(A)\text{.}\) The fact that \(B \subseteq  B\) follows from the definition of subset. Hence, set containment is reflexive.
> Let \(B_1, B_2 \in \mathcal{P}(A)\) and assume that \(B_1\subseteq  B_2\) and \(B_1\neq  B_2\) . Could it be that \(B_2\subseteq  B_1\text{?}\) No. There must be some element \(a\in A\) such that \(a \notin B_1\text{,}\) but \(a\in B_2\text{.}\) This is exactly what we need to conclude that \(B_2\) is not contained in \(B_1\text{.}\)  Hence, set containment is antisymmetric.
> Let \(B_1, B_2,B_3 \in \mathcal{P}(A)\) and assume that \(B_1 \subseteq  B_2\) and \(B_2 \subseteq  B_3\) . Does it follow that \(B_1 \subseteq B_3\) ? Yes, if \(a\in B_1\text{,}\) then \(a\in B_2\) because \(B_1 \subseteq  B_2\text{.}\) Now that we have \(a\in B_2\) and we have assumed \(B_2 \subseteq B_3\text{,}\) we conclude that \(a\in B_3\text{.}\)  Therefore, \(B_1\subseteq B_3\) and so set containment is transitive.

> [Figure 6.2.6 [UNRESOLVED_INTERNAL_LINK]](s-graphs-of-relations-on-a-set.html#fig-graph-6-2-subsets-2) is the graph for the “set containment” relation on the power set of \(\{1,2\}\text{.}\)

[Figure 6.2.6 [UNRESOLVED_INTERNAL_LINK]](s-graphs-of-relations-on-a-set.html#fig-graph-6-2-subsets-2) is helpful insofar as it reminds us that each set is a subset of itself and shows us at a glance the relationship between the various subsets in \(\mathcal{P} (\{1,2\})\text{.}\) However, when a relation is a partial ordering, we can streamline a graph like this one.  The streamlined form of a graph is called a Hasse diagram or ordering diagram.  A Hasse diagram takes into account the following facts.

By the reflexive property, each vertex must be related to itself, so the arrows from a vertex to itself (called “self-loops”) are not drawn in a Hasse diagram. They are simply assumed.
By the antisymmetry property, connections between two distinct elements in a directed graph can only go one way, if at all.  When there is a connection, we agree to always place the second element above the first (as we do above with the connection from \(\{1\}\) to \(\{1,2\}\)). For this reason, we can just draw a connection without an arrow, just a line.
By the transitive property, if there are edges connecting one element up to a second element and the second element up to a third element, then there will be a direct connection from the first to the third. We see this in [Figure 6.2.6 [UNRESOLVED_INTERNAL_LINK]](s-graphs-of-relations-on-a-set.html#fig-graph-6-2-subsets-2) with \(\emptyset\) connected to \(\{1\}\)\(\)and then \(\{1\}\) connected to \(\{1,2\}\text{.}\) Notice the edge connecting \(\emptyset\) to \(\{1,2\}\text{.}\)  Whenever we identify this situation, remove the connection from the first to the third in a Hasse diagram and simply observe that an upward path of any length implies that the lower element is related to the upper one.

Using these observations as a guide, we can draw a Hasse diagram for \(\subseteq\) on \(\{1,2\}\) as in [Figure 6.3.6 [UNRESOLVED_INTERNAL_LINK]](s-properties-of-relations.html#subsets_2_hasse).

![MISSING FIGURE: described in detail following the image](GAP:external/images/subsets_2_hasse.png)

> **Example 6.3.7 — Definition of a relation using a Hasse diagram.**

> Consider the partial ordering relation \(s\) whose Hasse diagram is [Figure 6.3.8 [UNRESOLVED_INTERNAL_LINK]](s-properties-of-relations.html#fig-pentagonal-hasse).

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/pentagonal-hasse.png)

> How do we read this diagram? What is \(A\text{?}\) What is \(s\text{?}\) What does the digraph of \(s\) look like? Certainly \(A = \{1,2,3,4,5\}\) and \(1 s 2\text{,}\) \(3 s 4\text{,}\) \(1 s 4\text{,}\) \(1 s 5\text{,}\) etc., Notice that \(1 s 5\) is implied by the fact that there is a path of length three upward from 1 to 5. This follows from the edges that are shown and the transitive property that is presumed in a poset.  Since \(1 s 3\) and \(3 s
> 4\text{,}\) we know that \(1 s 4\text{.}\) We then combine \(1 s 4\) with \(4 s 5\) to infer \(1 s 5\text{.}\)  Without going into details why, here is a complete list of pairs defined by \(s\text{.}\)
> 
> 
> \begin{equation*}
> s = \{(1,1),(2,2),(3,3),(4,4),(5,5),(1,3),(1,4),(1,5),(1,2),(3,4),(3,5),(4,5),(2,5)\}
> \end{equation*}

> A digraph for \(s\) is [Figure 6.3.9 [UNRESOLVED_INTERNAL_LINK]](s-properties-of-relations.html#fig-pentagonal-digraph). It is certainly more complicated to read and difficult to draw than the Hasse diagram.

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/pentagonal-digraph.png)

A classic example of a partial ordering relation is \(\leq \) on the real numbers, \(\mathbb{R}\text{.}\) Indeed, when graphing partial ordering relations, it is natural to “plot” the elements from the given poset starting with the “least” element to the “greatest” and to use terms like “least,” “greatest,” etc. Because of this the reader should be forewarned that some texts use the symbol \(\leq\) for arbitrary partial orderings. This can be quite confusing for the novice, so we continue to use generic letters \(r\text{,}\) \(s\text{,}\) etc.

# Subsection 6.3.3 Equivalence Relations

Another common property of relations is symmetry.

> **Definition 6.3.10 — Symmetric Relation.**

> Let \(r\) be a relation on a set \(A\text{.}\) \(r\) is symmetric if and only if whenever \(a r b\text{,}\) it follows that \(b r a\text{.}\)

Consider the relation of equality defined on any set \(A\text{.}\) Certainly \(a = b\) implies that \(b = a\) so equality is a symmetric relation on \(A\text{.}\)

Surprisingly, equality is also an antisymmetric relation on \(A\text{.}\) This is due to the fact that the condition that defines the antisymmetry property, \(a = b\) and \(a \neq  b\text{,}\) is a contradiction. Remember, a conditional proposition is always true when the condition is false. So a relation can be both symmetric and antisymmetric on a set! Again recall that these terms are *not* negatives of one other. That said, there are very few important relations other than equality that are both symmetric and antisymmetric.

> **Definition 6.3.11 — Equivalence Relation.**

> A relation \(r\) on a set \(A\) is called an equivalence relation if and only if it is reflexive, symmetric, and transitive.

The classic example of an equivalence relation is equality on a set \(A\text{.}\) In fact, the term equivalence relation is used because those relations which satisfy the definition behave quite like the equality relation. Here is another important equivalence relation.

> **Example 6.3.12 — Equivalent Fractions.**

> Let \(\mathbb{Z}^*\) be the set of nonzero integers. One of the most basic equivalence relations in mathematics is the relation \(q\) on \(\mathbb{Z}\times \mathbb{Z}^*\) defined by \((a, b) q(c, d)\) if and only if \(a d = b c\text{.}\) We will leave it to the reader to, verify that \(q\) is indeed an equivalence relation. Be aware that since the elements of \(\mathbb{Z}\times \mathbb{Z}^*\) are ordered pairs, proving symmetry involves four numbers and transitivity involves six numbers. Two ordered pairs, \((a, b)\) and \((c, d)\text{,}\) are related if the fractions \(\frac{a}{b}\) and \(\frac{c}{d}\) are numerically equal.

> Reflecting on these comments on fractions, we see that any fraction is a member of a set of equivalent fractions that can be exchanged for one another when doing arithmetic.  This is an instance of an important property of all equivalence relations that motivates the following definition.

> **Definition 6.3.13 — Equivalence Classes.**

> Let \(r\) be an equivalence relation on \(A\text{,}\) and \(a \in A\text{.}\)  The equivalence class of \(a\) is the set, \([a]\text{,}\)  of all elements to which \(a\) is related.
> 
> \begin{equation*}
> [a]=\{b\in A : a r b\}
> \end{equation*}
> 
> The set of all equivalence classes with respect to \(r\) is denoted \(A/r\text{,}\) read “\(A\) mod \(r\text{.}\)”

When we want to make it clear that an equivalence class defined by an element \(a\) is based on a specific equivalence relation \(r\) we would refer to it as “the equivalence class of \(a\) under \(r\text{.}\)”  Whenever we encounter an equivalence relation on a set, we should immediately think about how the set is partitioned because of the following theorem.

> **Theorem 6.3.14 —**

> Let \(r\) be an equivalence relation on \(A\text{.}\)  Then the set of all distinct equivalence classes determined by \(r\) form a partition of \(A\) denoted \(A/r\) and read “\(A\) mod \(r\text{.}\)”

Our next example involves the following fundamental relations on the set of integers.

> **Definition 6.3.15 — Congruence Modulo \(n\) .**

> Let \(n\) be a positive integer, \(n\geq 2\text{.}\)  We define congruence modulo n to be the relation \(\equiv_n\) defined on the integers by
> 
> \begin{equation*}
> a \equiv_n b \Leftrightarrow n \mid (a-b)
> \end{equation*}

We observe the following about congruence modulo \(n\text{:}\)

This relation is reflexive, for if \(a \in  \mathbb{Z} \text{,}\) \(n \mid (a-a) \Rightarrow  a\equiv_n a \text{.}\)


This relation is symmetric. We can prove this through the following chain of implications.

\begin{equation*}
\begin{split}
a \equiv_n b &\Rightarrow   n \mid (a-b)\\
& \Rightarrow \textrm{For  some } k \in \mathbb{Z}, a-b = n k \\
& \Rightarrow b-a = n (-k)\\
& \Rightarrow n \mid (b-a)\\
& \Rightarrow b \equiv_n a 
\end{split}\text{.}
\end{equation*}


Finally, this relation is transitive.  We leave it to the reader to prove that if \(a \equiv_n b \) and \(b\equiv_n c\text{,}\) then \(a \equiv_n c\text{.}\)

Frequently, you will see the equivalent notation \(a \equiv b (\textrm{mod } n)\) for congruence modulo \(n\text{.}\)

> **Example 6.3.17 — Random Relations usually have no properties.**

> Consider the relation s described by the digraph in [Figure 6.3.18 [UNRESOLVED_INTERNAL_LINK]](s-properties-of-relations.html#fig-graph-6-3-5). This was created by randomly selecting whether or not two elements from \(\{a,b,c\}\) were related or not. Convince yourself that the following are true:

> This relation is not reflexive.
> It is not antisymmetric.
> Also, it is not symmetric.
> It is not transitive.
> Is \(s\) an equivalence relation or a partial ordering?

> ![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/graph-6-3-5.svg)

> Not every random choice of a relation will be so totally negative, but as the underlying set increases, the likelihood any of the properties are true begins to vanish.

> **Exercise 1 . —**

> Prove that [Definition 6.1.5 [UNRESOLVED_INTERNAL_LINK]](s-basic-definitions.html#Divides) on the set of positive integers is a partial ordering.  Note that this will imply that the relation is a partial ordering on any subset of the positive integers as well.

> **Exercise 2 . —**

> Let \(B = \{a, b\}\) and \(U = \mathcal{P}(B)\text{.}\) Draw a Hasse diagram for \(\subseteq \) on \(U\text{.}\)
> 
> Let \(A = \{1,2, 3, 6\}\text{.}\) Draw a Hasse diagram for divides on \(A\text{.}\)
> 
> Compare the graphs of parts a and b. What can you observe?
> Repeat the previous steps with \(B = \{a, b, c\}\) and \(A = \{1, 2, 3, 5, 6, 10, 15, 30\}\text{.}\)

> **Exercise 3 . —**

> Consider the relations defined by the digraphs in [Figure 6.3.19 [UNRESOLVED_INTERNAL_LINK]](s-properties-of-relations.html#fig-exercises-6-digraphs).
> 
> Determine whether the given relations are reflexive, symmetric, antisymmetric, or transitive. Try to develop procedures for determining the validity of these properties from the graphs,
> Which of the graphs are of equivalence relations or of partial orderings?

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/exercises-6-digraphs.png)

> **Exercise 4 . —**

> Determine which of the following are equivalence relations and/or partial ordering relations for the given sets:

> \(A = \{\textrm{ lines in the plane}\}\text{,}\) and \(r\) defined by  \(x r y\) if and only if \(x\) is parallel to \(y\text{.}\)  Assume every line is parallel to itself.
> 
> \(A = \mathbb{R}\) and \(r\) defined by  \(x r y\) if and only if \(\lvert x -y \rvert \leq  7\text{.}\)

> **Exercise 5 . —**

> Consider the  relation on \(\{1, 2, 3, 4, 5, 6\}\) defined by  \(r = \{(i,j):\enspace \lvert i - j\rvert  = 2\}\text{.}\)

> Is \(r\) reflexive?
> Is \(r\) symmetric?
> Is \(r\) transitive?
> Draw a graph of \(r\text{.}\)

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/fig-sol-6-3-5.png)

> **Exercise 6 . —**

> Let \(A = \{0, 1, 2, 3\}\) and let
> 
> \begin{equation*}
> r = \{(0, 0), (1, 1), (2, 2), (3, 3), (1, 2),(2, 1), (3, 2), (2, 3), (3, 1), (1, 3)\}
> \end{equation*}
> 
> 
> Verify that \(r\) is an equivalence relation on \(A\text{.}\)
> 
> Find \([a]\) for each element \(a \in A\text{,}\) and observe that \(\{[a] \mid  a \in A\}\) forms a partition of \(A\text{.}\)

> **Exercise 7 . —**

> Let \(r\) be an equivalence relation on an arbitrary nonempty set \(A\text{.}\) Prove that the set of all equivalence classes under \(r\) constitutes a partition of \(A\text{.}\)

> **Exercise 8 . —**

> Define \(r\) on the power set of some set \(U\) by \(A r B \Leftrightarrow  \lvert A \rvert = \lvert B \rvert \text{.}\) Prove that \(r\) is an equivalence relation. What are the equivalence classes under \(r\) if \(U =\{1, 2, 3\}\text{?}\)

> **Exercise 9 . —**

> Consider the following relations on \(\mathbb{Z}_8= \{0, 1, . . . , 7\}\text{.}\) Which are equivalence relations? For the equivalence relations, list the equivalence classes.

> \(a r b\) iff the English spellings of \(a\) and \(b\) begin with the same letter.
> 
> \(a s b\) iff \(a - b\) is a positive integer.
> 
> \(a t b\) iff \(a-b\) is an even integer.

> **Exercise 10 . —**

> Let \(n\) be a positive integer greater than or equal to two.

> Prove that congruence modulo \(n\) is transitive.
> What are the equivalence classes under congruence modulo 2?  How many distinct equivalence classes are there?
> What are the equivalence classes under congruence modulo 10? How many distinct equivalence classes are there?

> **Exercise 11 . —**

> In this exercise, we prove that implication is a partial ordering. Let \(A\) be any set of propositions, no two of which is equivalent to one another.

> Verify that \(q \to  q\) is a tautology, thereby showing that \(\Rightarrow\) is a reflexive relation on \(A\text{.}\)
> 
> Prove that \(\Rightarrow\) is antisymmetric on \(A\text{.}\) Note: we do not use \(=\) when speaking of propositions, but rather equivalence, \(\Leftrightarrow\text{.}\)
> 
> Prove that \(\Rightarrow\) is transitive on \(A\text{.}\)
> 
> Given that \(q_i\) is the proposition \(n < i\) on \(\mathbb{N}\text{,}\) draw the Hasse diagram for the relation \(\Rightarrow\) on \(\{q_1, q_2, q_3,\ldots \}\text{.}\)

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/fig-sol-6-3-11.png)
