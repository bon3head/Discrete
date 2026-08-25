---
source_relative_path: "DM TXT/6-Relations/ads Matrices of Relations.html"
source_sha256: "e40bcdd5150afc9852b14e01110fd3c250fa48e00e34f373fe759d3076817e0e"
scope_class: active_candidate
displayed_section_or_chapter: "Section 6.4 Matrices of Relations"
content_gap: true
missing_assets:
  - "external/images/fig-ex-6-4-2a.png"
  - "external/images/fig-ex-6-4-2b.png"
---

# Section 6.4 Matrices of Relations

We have discussed two of the many possible ways of representing a relation, namely as a digraph or as a set of ordered pairs. In this section we will discuss the representation of relations by matrices.

# Subsection 6.4.1 Representing a Relation with a Matrix

> **Definition 6.4.1 — Relation Matrix.**

> Let \(A = \{a_1,a_2,\ldots , a_m\}\) and \(B= \{b_1,b_2,\ldots , b_n\}\) be finite sets of cardinality \(m\) and \(n\text{,}\) respectively. Let \(r\) be a relation from \(A\) into \(B\text{.}\) Then \(r\) can be represented by the \(m\times n\) matrix \(R\) defined by
> 
> \begin{equation*}
> R_{ij}= \left\{
> \begin{array}{cc}
> 1 & \textrm{   if } a_i r b_j \\
> 0 & \textrm{   otherwise}     \\
> \end{array}\right.
> \end{equation*}
> 
> 
> \(R\) is called the relation matrix (or simply the matrix) of \(r\text{.}\)

> **Example 6.4.3 — A simple example.**

> Let \(A = \{2, 5, 6\}\) and let \(r\) be the relation \(\{(2, 2), (2, 5), (5, 6), (6, 6)\}\) on \(A\text{.}\) Since \(r\) is a relation from \(A\) into the same set \(A\) (the \(B\) of the definition), we have \(a_1= 2\text{,}\) \(a_2=5\text{,}\) and \(a_3=6\text{,}\) while \(b_1= 2\text{,}\) \(b_2=5\text{,}\) and \(b_3=6\text{.}\) Next, since

> \(2 r 2\text{,}\) we have \(R_{11}= 1\)
> 
> 
> \(2 r 5\text{,}\) we have \(R_{12}= 1\)
> 
> 
> \(5 r 6\text{,}\) we have \(R_{23}= 1\)
> 
> 
> \(6 r 6\text{,}\) we have \(R_{33}= 1\)

> All other entries of \(R\) are zero, so
> 
> \begin{equation*}
> R =\left(
> \begin{array}{ccc}
> 1 & 1 & 0 \\
> 0 & 0 & 1 \\
> 0 & 0 & 1 \\
> \end{array}
> \right)
> \end{equation*}

# Subsection 6.4.2 Composition as Matrix Multiplication

From the definition of \(r\) and of composition, we note that

\begin{equation*}
r^2 = \{(2, 2), (2, 5), (2, 6), (5, 6), (6, 6)\}
\end{equation*}

The matrix of \(r^2\) is

\begin{equation*}
R^2 =\left(
\begin{array}{ccc}
1 & 1 & 1 \\
0 & 0 & 1 \\
0 & 0 & 1 \\
\end{array}
\right)\text{.}
\end{equation*}

We do not write \(R^2\) only for notational purposes. In fact, \(R^2\) can be obtained from the matrix product \(R R\text{;}\) however, we must use a slightly different form of arithmetic.

> **Definition 6.4.4 — Boolean Arithmetic.**

> Boolean arithmetic is the arithmetic defined on \(\{0,1\}\) using Boolean addition and Boolean multiplication, defined by

> ![Table 6.4.5 . \(0 + 0 = 0\) \(0+1 = 1 + 0=1\) \(1 + 1 = 1\) \(0\cdot 0=0\) \(0 \cdot 1 = 1 \cdot 0 = 0\) \(1 \cdot 1 = 1\)]()

Notice that from Chapter 3, this is the “arithmetic of logic,” where \(+\) replaces “or” and \(\cdot\) replaces “and.”

> **Example 6.4.6 — Composition by Multiplication.**

> Suppose that \(R=\left(
> \begin{array}{cccc}
> 0 & 1 & 0 & 0 \\
> 1 & 0 & 1 & 0 \\
> 0 & 1 & 0 & 1 \\
> 0 & 0 & 1 & 0 \\
> \end{array}
> \right)\)  and  \(S=\left(
> \begin{array}{cccc}
> 0 & 1 & 1 & 1 \\
> 0 & 0 & 1 & 1 \\
> 0 & 0 & 0 & 1 \\
> 0 & 0 & 0 & 0 \\
> \end{array}
> \right)\text{.}\) Then using Boolean arithmetic, \(R S =\left(
> \begin{array}{cccc}
> 0 & 0 & 1 & 1 \\
> 0 & 1 & 1 & 1 \\
> 0 & 0 & 1 & 1 \\
> 0 & 0 & 0 & 1 \\
> \end{array}
> \right)\)  and \(S R=\left(
> \begin{array}{cccc}
> 1 & 1 & 1 & 1 \\
> 0 & 1 & 1 & 1 \\
> 0 & 0 & 1 & 0 \\
> 0 & 0 & 0 & 0 \\
> \end{array}
> \right)\text{.}\)

> **Theorem 6.4.7 — Composition is Matrix Multiplication.**

> Let \(A_1\text{,}\) \(A_2\text{,}\) and \(A_3\) be finite sets where \(r_1\) is a relation from \(A_1\) into \(A_2\) and \(r_2\) is a relation from \(A_2\) into \(A_3\text{.}\) If \(R_1\) and \(R_2\) are the adjacency matrices of \(r_1\) and \(r_2\text{,}\) respectively, then the product \(R_1R_2\) using Boolean arithmetic is the relation matrix of the composition \(r_1r_2\text{.}\)

Remark: A convenient help in constructing the matrix of a relation from a set \(A\) into a set \(B\) is to write the elements from \(A\) in a column preceding the first column of the  matrix, and the elements of \(B\) in a row above the first row. Initially, \(R\) in [Example 3 [UNRESOLVED_INTERNAL_LINK]](s-matrices-of-relations.html#ex-first-6-4) would be

\begin{equation*}
\begin{array}{cc}
& 
\begin{array}{ccc}
2 & 5 & 6 \\
\end{array}
\\
\begin{array}{c}
2 \\
5 \\
6 \\
\end{array}
& \left(
\begin{array}{ccc}
&   &   \\
&   &   \\
&   &   \\
\end{array}
\right) \\
\end{array}
\end{equation*}

To fill in the matrix, \(R_{ij}\) is 1 if and only if \(\left(a_i,b_j\right) \in r\text{.}\) So that, since the pair \((2, 5) \in r\text{,}\) the entry of \(R\) corresponding to the row labeled 2 and the column labeled 5 in the matrix is a 1.

> **Example 6.4.8 — Relations and Information.**

> This final example gives an insight into how relational data base programs can systematically answer questions pertaining to large masses of information. Matrices \(R\) (on the left) and \(S\) (on the right) define the relations \(r\) and \(s\) where \(a r b\) if software \(a\) can be run with operating system \(b\text{,}\) and \(b s c\) if operating system \(b\) can run on computer \(c\text{.}\)
> 
> 
> \begin{equation*}
> \begin{array}{cc}
> \begin{array}{cc}
> & 
> \begin{array}{cccc}
> \text{OS1} & \text{OS2} & \text{OS3} & \text{OS4} 
> \end{array} \\ 
> \begin{array}{c}
> \text{P1} \\
> \text{P2} \\
> \text{P3} \\
> \text{P4}
> \end{array}
> &
> \left(
> \begin{array}{cccc}
> 1  &  0  &  1  &  0  \\
> 1  &  1  & 0 & 0 \\
> 0 & 0 & 0 &  1  \\
> 0 & 0 &  1  &  1
> \end{array}
> \right) 
> \end{array}
> \begin{array}{cc}
> & 
> \begin{array}{ccc}
> \text{C1} & \text{C2} & \text{C3}
> \end{array} \\
> \begin{array}{c}
> \text{OS1} \\
> \text{OS2} \\
> \text{OS3} \\
> \text{OS4} \\
> \end{array}
> & \left(
> \begin{array}{ccc}
> 1  &  1  & 0 \\
> 0 &  1  & 0 \\
> 0 & 0 &  1  \\
> 0 &  1  &  1 
> \end{array}
> \right)
> \end{array}
> \end{array}
> \end{equation*}
> 
> Although the relation between the software and computers is not implicit from the data given, we can easily compute this information. The matrix of \(rs\) is \(RS\text{,}\) which is
> 
> \begin{equation*}
> \begin{array}{cc}
> & 
> \begin{array}{ccc}
> \text{C1} & \text{C2} & \text{C3}
> \end{array}
> \\
> \begin{array}{c}
> \text{P1} \\
> \text{P2} \\
> \text{P3} \\
> \text{P4}
> \end{array}
> & \left(
> \begin{array}{ccc}
> 1  &  1  & 1 \\
> 1 &  1  & 0 \\
> 0 & 1 &  1  \\
> 0 &  1  &  1 
> \end{array}
> \right) 
> \end{array}
> \end{equation*}
> 
> This matrix tells us at a glance which software will run on the computers listed. In this case, all software will run on all computers with the exception of program P2, which will not run on the computer C3, and programs P3 and P4, which will not run on the computer C1.

> **Exercise 1 . —**

> Let \(A_1 = \{1,2, 3, 4\}\text{,}\) \(A_2 = \{4, 5, 6\}\text{,}\) and \(A_3 = \{6, 7, 8\}\text{.}\) Let \(r_1\) be the relation from \(A_1\) into \(A_2\) defined by \(r_1 = \{(x, y)  \mid  y - x = 2\}\text{,}\) and let \(r_2\) be the relation from \(A_2\) into \(A_3\) defined by \(r_2 = \{(x, y) \mid  y - x = 1\}\text{.}\)

> Determine the adjacency matrices of \(r_1\) and \(r_2\text{.}\)
> 
> Use the definition of composition to find \(r_1r_2\text{.}\)
> 
> Verify the result in part b by finding the product of the adjacency matrices of \(r_1\) and \(r_2\text{.}\)

> **Exercise 2 . —**

> Determine the matrix of each relation given by the following digraphs.
> 
> 
> Directed graph of the relation \(r_1\) on \(\{1,2,3\}\) with edges \((1,2),(1,3),(3,1)\text{.}\)
> 
> 
> 
> Directed graph of the relation \(r_2\) on \(\{1,2,3\}\) with edges \((1,2),(2,3),(3,1)\text{.}\)
> 
> 
> 
> 
> Using the matrices found in part (a), determine the matrices of \(r_1^2\) and \(r_2^2\text{.}\)
> 
> Draw the digraphs of \(r_1^2\) and \(r_2^2\) directly from the definition of the square of  relation and compare your results with those of part (b).

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/fig-ex-6-4-2a.png)

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/fig-ex-6-4-2b.png)

> **Exercise 3 . —**

> Suppose that the matrices in [Example 6.4.6 [UNRESOLVED_INTERNAL_LINK]](s-matrices-of-relations.html#ex-composition-matrices) are relations on \(\{1, 2, 3, 4\}\text{.}\) What relations do \(R\) and \(S\) describe?

> **Exercise 4 . —**

> Let \(D\) be the set of weekdays, Monday through Friday, let \(W\) be a set of employees \(\{1, 2, 3\}\) of a tutoring center, and let \(V\) be a set of computer languages for which tutoring is offered,  \(\{A(PL), B(asic), C(++), J(ava), L(isp), P(ython)\}\text{.}\) We define \(s\) (schedule) from \(D\) into \(W\) by \(d s w\) if \(w\) is scheduled to work on day \(d\text{.}\) We also define \(r\) from \(W\) into \(V\) by \(w r l\) if \(w\) can tutor students in language \(l\text{.}\) If \(s\) and \(r\) are defined by matrices

> \begin{equation*}
> S = 
> \begin{array}{cc}
> & 
> \begin{array}{ccc}
> 1 & 2 & 3 \\
> \end{array}
> \\
> \begin{array}{c}
> M \\
> T \\
> W \\
> R \\
> F \\
> \end{array}
> & 
> \left(
> \begin{array}{ccc}
> 1 & 0 & 1 \\
> 0 & 1 & 1 \\
> 1 & 0 & 1 \\
> 0 & 1 & 0 \\
> 1 & 1 & 0 \\
> \end{array}
> \right) \\
> \end{array}
> \textrm{ and }R=
> \begin{array}{cc}
> & 
> \begin{array}{cccccc}
> A & B & C & J & L & P \\
> \end{array}
> \\
> \begin{array}{c}
> 1 \\
> 2 \\
> 3 \\
> \end{array}
> & \left(
> \begin{array}{cccccc}
> 0 & 1 & 1 & 0 & 0 & 1 \\
> 1 & 1 & 0 & 1 & 0 & 1 \\
> 0 & 1 & 0 & 0 & 1 & 1 \\
> \end{array}
> \right) \\
> \end{array}
> \end{equation*}

> Compute \(S R\) using Boolean arithmetic and give an interpretation of the relation it defines, and
> Compute \(S R\) using regular arithmetic and give an interpretation of what the result describes.

> **Exercise 5 . —**

> How many different reflexive, symmetric relations are there on a set with three elements?

> **Exercise 6 . —**

> Let \(A = \{a, b, c, d\}\text{.}\)  Let \(r\) be the relation on \(A\) with relation matrix \(R=\begin{array}{cc}
> & 
> \begin{array}{cccc}
> a & b & c & d \\
> \end{array}
> \\
> \begin{array}{c}
> a \\
> b \\
> c \\
> d \\
> \end{array}
> & \left(
> \begin{array}{cccc}
> 1 & 0 & 0 & 0 \\
> 0 & 1 & 0 & 0 \\
> 1 & 1 & 1 & 0 \\
> 0 & 1 & 0 & 1 \\
> \end{array}
> \right) \\
> \end{array}\)

> Explain why \(r\) is a partial ordering on \(A\text{.}\)
> 
> Draw its Hasse diagram.

> **Exercise 7 . —**

> Define relations \(p\) and \(q\) on \(\{1, 2, 3, 4\}\) by \(p = \{(a, b) \mid \lvert a-b\rvert=1\}\) and \(q=\{(a,b) \mid a-b \textrm{ is even}\}\text{.}\)

> Represent \(p\) and \(q\) as both graphs and matrices.
> Determine \(p q\text{,}\) \(p^2\text{,}\) and \(q^2\text{;}\) and represent them clearly in any way.

> **Exercise 8 . —**

> Let \(r\) be a relation on a set \(A\text{.}\)

> Prove that if \(r\) is a transitive if and only if \(r^2 \subseteq  r\text{.}\)
> 
> Find an example of a transitive relation for which \(r^2\neq r\text{.}\)

> **Exercise 9 . —**

> We define \(\leq\) on the set of all \(n\times n\) relation matrices by the rule that if \(R\) and \(S\) are any two \(n\times n\) relation matrices, \(R \leq  S\) if and only if \(R_{ij} \leq S_{ij}\) for all \(1 \leq  i, j \leq  n\text{.}\)

> Prove that \(\leq\) is a partial ordering on all \(n\times n\) relation matrices.
> Prove that \(R \leq  S  \Rightarrow   R^2\leq S^2\) , but the converse is not true.
> If \(R\) and \(S\) are matrices of equivalence relations and \(R \leq  S\text{,}\) how are the equivalence classes defined by \(R\) related to the equivalence classes defined by \(S\text{?}\)
