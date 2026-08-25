---
source_relative_path: "DM TXT/6-Relations/ads Basic Definitions.html"
source_sha256: "fe66bc311282157f923151c124d148564575f7c74f31f36c4d2117f0e0fdb852"
scope_class: active_candidate
displayed_section_or_chapter: "Section 6.1 Basic Definitions"
content_gap: true
missing_assets:
  - "external/images/graph-6-1-relation-composition.png"
  - "external/images/graph-6-1-relation-graph.png"
---

# Section 6.1 Basic Definitions

In Chapter 1 we introduced the concept of the Cartesian product of sets. Let’s assume that a person owns three shirts and two pairs of slacks. More precisely, let \(A = \{\textrm{blue shirt}, \textrm{tan shirt}, \textrm{mint green shirt}\}\) and \(B = \{\textrm{grey slacks}, \textrm{tan slacks}\}\text{.}\) Then \(A\times B\) is the set of all six possible combinations of shirts and slacks that the individual could wear. However, an individual may wish to restrict himself or herself to combinations which are color coordinated, or “related.” This may not be all possible pairs in \(A\times B\) but will certainly be a subset of \(A\times B\text{.}\) For example, one such subset may be

\begin{equation*}
\{(\textrm{blue shirt}, \textrm{grey slacks}), (\textrm{blue shirt},  \textrm{tan slacks}), (\textrm{mint green shirt}, \textrm{tan slacks})\}.
\end{equation*}

# Subsection 6.1.1 Relations between two sets

> **Definition 6.1.1 — Relation.**

> Let \(A\) and \(B\) be sets. A relation from \(A\) into \(B\) is any subset of \(A\times B\text{.}\)

> **Example 6.1.2 — A simple example.**

> Let \(A = \{1, 2, 3\}\) and \(B = \{4, 5\}\text{.}\) Then \(\{(1, 4), (2, 4), (3, 5)\}\) is a relation from \(A\) into \(B\text{.}\) Of course, there are many others we could describe; 64, to be exact.

> **Example 6.1.3 — Divisibility Example.**

> Let \(A = \{2, 3, 5, 6\}\) and define a relation \(r\) from \(A\) into \(A\) by \((a, b) \in r\) if and only if \(a\) divides evenly into \(b\text{.}\) The set of pairs that qualify for membership is \(r = \{(2, 2), (3, 3), (5, 5), (6, 6), (2, 6), (3, 6)\}\text{.}\)

# Subsection 6.1.2 Relations on a Set

> **Definition 6.1.4 — Relation on a Set.**

> A relation from a set \(A\) into itself is called a relation on \(A\text{.}\)

The relation “divides” in [Example 6.1.3 [UNRESOLVED_INTERNAL_LINK]](s-basic-definitions.html#ex-divides-example) will appear throughout the book. Here is a general definition on the whole set of integers.

> **Definition 6.1.5 — Divides.**

> Let \(a, b \in \mathbb{Z}\text{,}\) \(a \neq 0\text{.}\) We say that \(a\) divides \(b\text{,}\) denoted \(a \mid b\text{,}\)  if and only if there exists an integer \(k\) such that \(a k = b\text{.}\)

Be very careful in writing about the relation “divides.”  The vertical line symbol is used for this relation. If written carelessly, can look like division.  While \(a \mid b\) is either true or false, \(a/b\) is a number.

Based on the equation \(a k = b\text{,}\) we can say that \(a|b\) is equivalent to \(k= \frac{b}{a}\text{,}\) or \(a\) divides evenly into \(b\text{.}\) In fact the “divides” is short for “divides evenly into.” You might find the equation \(k= \frac{b}{a}\) initially easier to understand, but in the long run we will find the equation \(a k = b\) more convenient.

Sometimes it is helpful to illustrate a relation with a graph. Consider [Example 6.1.2 [UNRESOLVED_INTERNAL_LINK]](s-basic-definitions.html#ex-simple-relation).  A graph of \(r\) can be drawn as in [Figure 6.1.6 [UNRESOLVED_INTERNAL_LINK]](s-basic-definitions.html#graph-6-1-1-relation). The arrows indicate that 1 is related to 4 under \(r\text{.}\) Also, 2 is related to 4 under \(r\text{,}\) and 3 is related to 5, while the upper arrow denotes that \(r\) is a relation from the whole set \(A\) into the set \(B\text{.}\)

![MISSING FIGURE: described in detail following the image](GAP:external/images/graph-6-1-relation-graph.png)

A typical element in a relation \(r\) is an ordered pair \((x, y)\text{.}\) In some cases, \(r\) can be described by actually listing the pairs which are in \(r\text{,}\) as in the previous examples. This may not be convenient if \(r\) is relatively large. Other notations are used with certain well-known relations. Consider the “less than or equal” relation on the real numbers. We could define it as a set of ordered pairs this way:

\begin{equation*}
\le = \{(x, y) | x \leq  y\}
\end{equation*}

However, the notation \(x \leq  y\) is clear and self-explanatory; it is a more natural, and hence preferred, notation to use than \((x, y) \in \le\text{.}\)

Many of the relations we will work with “resemble” the relation \(\leq\text{,}\) so \(x s y\) is a common way to express the fact that \(x\) is related to \(y\) through the relation \(s\text{.}\)

*Relation Notation* Let \(s\) be a relation from a set \(A\) into a set \(B\text{.}\) Then the fact that \((x, y) \in s\) is frequently written \(x s y\text{.}\)

# Subsection 6.1.3 Composition of Relations

With \(A = \{2, 3, 5, 8\}\text{,}\) \(B = \{4, 6, 16\}\text{,}\) and \(C = \{1, 4, 5, 7\}\text{,}\) let \(r\) be the relation “divides,” from \(A\) into \(B\text{,}\) and let \(s\) be the relation \(\leq\) from \(B\) into \(C\text{.}\) So \(r = \{(2, 4), (2, 6), (2,16), (3, 6), (8, 16)\}\) and \(s = \{(4, 4), (4, 5), (4, 7), (6, 7)\}\text{.}\)

Notice that in [Figure 6.1.8 [UNRESOLVED_INTERNAL_LINK]](s-basic-definitions.html#graph-6-1-relation-composition) that we can, for certain elements of \(A\text{,}\) go through elements in \(B\) to results in \(C\text{.}\) That is:

![Table 6.1.7 . \(2 | 4 \textrm{ and } 4 \leq 4\) \(2 | 4 \textrm{ and } 4 \leq 5\) \(2 | 4 \textrm{ and } 4 \leq 7\) \(2| 6 \textrm{ and } 6 \leq 7\) \(3| 6 \textrm{ and } 6 \leq 7\)]()

![MISSING FIGURE: described in detail following the image](GAP:external/images/graph-6-1-relation-composition.png)

Based on this observation, we can define a new relation, call it \(rs\text{,}\) from \(A\) into \(C\text{.}\) In order for \((a, c)\) to be in \(rs\text{,}\) it must be possible to travel along a path in [Figure 6.1.8 [UNRESOLVED_INTERNAL_LINK]](s-basic-definitions.html#graph-6-1-relation-composition) from \(a\) to \(c\text{.}\) In other words, \((a, c) \in rs\) if and only if \((\exists b)_B(a r b \textrm{ and } b s c)\text{.}\) The name \(rs\) was chosen because it reminds us that this new relation was formed by the two previous relations \(r\) and \(s\text{.}\) The complete listing of all elements in \(rs\) is \(\{(2, 4), (2, 5), (2, 7), (3, 7)\}\text{.}\) We summarize in a definition.

> **Definition 6.1.9 — Composition of Relations.**

> Let \(r\) be a relation from a set \(A\) into a set \(B\text{,}\) and let \(s\) be a relation from \(B\) into a set \(C\text{.}\) The composition of \(r\) with \(s\text{,}\) written \(rs\text{,}\) is the set of pairs of the form \((a, c) \in A\times C\text{,}\) where \((a, c) \in rs\) if and only if there exists \(b \in B\) such that \((a, b) \in r\) and \((b, c) \in s\text{.}\)

Remark: A word of warning to those readers familiar with composition of functions. (For those who are not, disregard this remark. It will be repeated at an appropriate place in the next chapter.) As indicated above, the traditional way of describing a composition of two relations is \(rs\) where \(r\) is the first relation and \(s\) the second. However, function composition is traditionally expressed in the opposite order:  \(s\circ r\text{,}\) where \(r\) is the first function and \(s\) is the second.

> **Exercise 1 . —**

> For each of the following relations \(r\) defined on \(\mathbb{P}\text{,}\) determine which of the given ordered pairs belong to \(r\)

> \(x r y\) iff \(x|y\text{;}\)  (2, 3), (2, 4), (2, 8), (2, 17)
> 
> \(x r y\) iff \(x \leq  y\text{;}\) (2, 3), (3, 2), (2, 4), (5, 8)
> 
> \(x r y\) iff \(y =x^2\) ; (1,1), (2, 3), (2, 4), (2, 6)

> **Exercise 2 . —**

> The following relations are on \(P=\{0,1,2,\dots 8,9\}\text{.}\) Let
> 
> \begin{equation*}
> A=\{(9,8),(9,7),(6,5),(6,4),(3,2),(3,1)\}
> \end{equation*}
> 
> and
> 
> \begin{equation*}
> B=\{(8,6),(7,6),(5,3),(4,3),(2,0),(1,0)\}.
> \end{equation*}

> List all elements in  \(AB\text{.}\)
> 
> List all elements in  \(BA\text{.}\)
> 
> Illustrate \(AB\) and \(BA\) via a diagraph.
> In one version of the game of nim players A and B take turns removing one or two stones from a pile.  The player who manages to remove the last stone wins.  Explain how these two relations describe the winning moves for B if A plays first with nine stones in the pile at the start of the game.

> **Exercise 3 . —**

> Let \(A = \{1,2,3,4,5\}\) and define \(r\) on \(A\) by \(x r y\) iff \(x + 1 = y\text{.}\) We define \(r^2 = r r\) and \(r^3 = r^2 r\text{.}\) Find:
> 
> \(\displaystyle r\)
> \(\displaystyle r^2\)
> \(\displaystyle r^3\)

> **Exercise 4 . —**

> Given \(s\) and \(t\text{,}\) relations on \(\mathbb{Z}\text{,}\) \(s = \{(1, n) : n \in \mathbb{Z}\}\) and \(t= \{(n, 1) : n \in  \mathbb{Z}\}\text{,}\) what are \(st\) and \(ts\text{?}\) Hint: Even when a relation involves infinite sets, you can often get insights into them by drawing partial graphs.

> **Exercise 5 . —**

> Let \(\rho\) be the relation on the power set, \(\mathcal{P}(S )\text{,}\) of a finite set \(S\) of cardinality \(n\) defined \(\rho\) by \((A,B)
> \in \rho\) iff \(A\cap  B = \emptyset\text{.}\)

> Consider the specific case \(n = 3\text{,}\) and determine the cardinality of the set \(\rho\text{.}\)
> 
> What is the cardinality of \(\rho\) for an arbitrary \(n\text{?}\) Express your answer in terms of \(n\text{.}\) (Hint: There are three places that each element of S can go in building an element of \(\rho\text{.}\))

> **Exercise 6 . —**

> Consider the two relations on people: \(M\text{,}\) where \(aMb\) if \(a\)’s mother is \(b\text{;}\) and \(S\text{,}\) where  \(aSb\) if \(a\) and \(b\) are siblings.  Describe, in words, the two relations \(MS\) and \(SM\) in simple English terms.

> **Exercise 7 . —**

> Let \(r_1\text{,}\) \(r_2\text{,}\) and \(r_3\) be relations on any set \(A\text{.}\) Prove that if \(r_1\subseteq r_2\) then \(r_1r_3\subseteq r_2r_3\text{.}\)
