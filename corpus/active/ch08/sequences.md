---
source_relative_path: "DM TXT/8-Recursion_and_Recurrence_Relations/ads Sequences.html"
source_sha256: "7aa103c830d14f2d317ef9a087a8b029e31dfe819b111a81844ec459ab643b84"
scope_class: active_candidate
displayed_section_or_chapter: "Section 8.2 Sequences"
content_gap: true
missing_assets:
  - "external/images/exercise-8-2-3.png"
---

# Section 8.2 Sequences

# Subsection 8.2.1 Sequences and Ways They Are Defined

> **Definition 8.2.1 — Sequence.**

> A sequence is a function from the natural numbers into some predetermined set. The image of any natural number \(k\) can be written  as \(S(k)\) or \(S_k\) and is called the \(k^{th}\) *term*  of \(S\text{.}\) The variable \(k\) is called the  *index*  or  *argument*  of the sequence.

For example, a sequence of integers would be a function \(S:\mathbb{N}\to \mathbb{Z}\text{.}\)

> **Example 8.2.2 — Three sequences defined in different ways.**

> The sequence \(A\) defined by \(A(k) = k^2 - k\text{,}\) \(k \geq  0\text{,}\) is a sequence of integers.
> 
> The sequence \(B\) defined recursively by \(B(0) = 2\) and \(B(k) = B(k - 1) + 3\) for \(k \geq  1\) is a sequence of integers. The terms of \(B\) can be computed either by applying the recursion formula or by iteration. For example,
> 
> \begin{equation*}
> \begin{split}
> B(3)  &= B(2) + 3\\
> & =(B(1)+3)+3\\
> & = ((B(0)+3)+3)+3\\
> &=((2+3)+3)+3=11
> \end{split}
> \end{equation*}
> 
> or
> 
> \begin{equation*}
> \begin{array}{c}
> B(1) = B(0) + 3 = 2 + 3 = 5\\
> B(2) = B(1) + 3 = 5 + 3 = 8\\
> B(3) = B(2) + 3 = 8 + 3 = 11
> \end{array}
> \end{equation*}
> 
> 
> Let \(C_r\) be the number of strings of 0’s and 1’s of length \(r\) having no consecutive zeros. These terms define a sequence \(C\) of integers.

Remarks:

A sequence is often called a  *discrete function*.
Although it is important to keep in mind that a sequence is a function, another useful way of visualizing a sequence is as a list. For example, the sequence \(A\) in the previous example could be written as \((0, 0, 2, 6, 12, 20, \dots )\text{.}\) Finite sequences can appear much the same way when they are the input to or output from a computer. The index of a sequence can be thought of as a time variable. Imagine the terms of a sequence flashing on a screen every second. Then \(A_k\) would be what you see in the \(k^{th}\) second. It is convenient to use terminology like this in describing sequences. For example, the terms that precede the \(k^{th}\) term of \(A\) would be \(A (0), A(1), . . . , A(k -1)\text{.}\)  They might be called the earlier terms.

# Subsection 8.2.2 A Fundamental Problem

Given the definition of any sequence, a fundamental problem that we will concern ourselves with is to devise a method for determining any specific term in a minimum amount of time. Generally, time can be equated with the number of operations needed. In counting operations, the application of a recursive formula would be considered an operation.

The terms of \(A\) in [Example 8.2.2 [UNRESOLVED_INTERNAL_LINK]](s-Sequences.html#ex-three-sequences) are very easy to compute because of the closed form expression. No matter what term you decide to compute, only three operations need to be performed.

How to compute the terms of \(B\) is not so clear. Suppose that you wanted to know \(B(100)\text{.}\) One approach would be to apply the definition recursively:

\begin{equation*}
B(100) = B(99) + 3 = (B(98) + 3) + 3 =\cdots
\end{equation*}

The recursion equation for \(B\) would be applied 100 times and 100 additions would then follow. To compute \(B(k)\) by this method, \(2k\) operations are needed. An iterative computation of \(B(k)\) is an improvement: \(B(1) =B(0) +3 = 2 + 3 = 5\\
\\
B(2) =B(1)+3= 5 + 3 = 8\\
\\
\text{etc}.\) Only \(k\) additions are needed. This still isn’t a good situation. As \(k\) gets large, we take more and more time to compute \(B(k)\text{.}\)  The formula \(B(k)=B(k-1)+3\) is called a recurrence relation on \(B\text{.}\) The process of finding a closed form expression for \(B(k)\text{,}\) one that requires no more than some fixed number of operations, is called solving the recurrence relation.

The determination of \(C_k\) is a standard kind of problem in combinatorics. One solution is by way of a recurrence relation. In fact, many problems in combinatorics are most easily solved by first searching for a recurrence relation and then solving it. The following observation will suggest the recurrence relation that we need to determine \(C_k\text{.}\) If \(k \geq  2\text{,}\) then every string of 0’s and 1’s with length \(k\) and no two consecutive 0’s is either \(1s_{k-1}\) or \(01s_{k-2}\text{,}\) where \(s_{k-1}\) and \(s_{k-2}\) are strings with no two consecutive 0’s of length \(k - 1\) and \(k - 2\) respectively. From this observation we can see that \(C_k= C_{k-2}+C_{k-1}\) for \(k\geq 2\text{.}\) The terms \(C_0=
1\) and \(C_1 = 2\) are easy to determine by enumeration. Now, by iteration, any \(C_k\) can be easily determined. For example, \(C_5 = 21\) can be computed with five additions. A closed form expression for \(C_k\) would be an improvement. Note that the recurrence relation for \(C_k\) is identical to the one for [The Fibonacci Sequence [UNRESOLVED_INTERNAL_LINK]](s-faces-of-recursion.html#ex-fibonacci-sequence). Only the basis is different.

> **Exercise 1 . —**

> Prove by induction that \(B(k) = 3k + 2,\) \(k\geq 0\text{,}\) is a closed form expression for the sequence \(B\) in [Example 8.2.2 [UNRESOLVED_INTERNAL_LINK]](s-Sequences.html#ex-three-sequences)

> **Exercise 2 . —**

> The sequence of first differences of any sequence \(S\) is the sequence \(S(k+1)-S(k)\text{.}\)  The sequence of second differences is the sequence of first differences of the first differences:
> 
> \begin{equation*}
> (S(k+2)-S(k+1))-(S(k+1)-S(k))=S(k+2)-2 S(k+1)+S(k).
> \end{equation*}
> 
> 
> Consider sequence \(Q\) defined by \(Q(k) = 2k + 9\text{,}\) \(k \geq  1\text{.}\) Complete the table below and determine a recurrence relation that describes \(Q\text{.}\) \(\begin{array}{c|c|c}
> k & Q(k)  & Q(k+1)-Q(k) \\
> \hline
> 0 & \quad\quad  &   \\
> 1 &   &   \\
> 2 &   &   \\
> 3 &   &   \\
> 4 &   &   \\
> 5 &   &   \\
> \end{array}\)
> 
> 
> Let \(A(k) = k^2 - k\text{,}\) \(k \geq  0\text{.}\) Complete the table below and determine a recurrence relation for \(A\text{.}\)
> 
> 
> \begin{equation*}
> \begin{array}{c|c|c|c}
> k & A(k) & A(k+1)-A(k) & A(k+2)-2A(k+1)+A(k) \\
> \hline
> 0 &   &   &   \\
> 1 &   &   &   \\
> 2 &   &   &   \\
> 3 & \quad\quad    &   &   \\
> 4 &   &   &   \\
> 5 &   &   &   \\
> \end{array}
> \end{equation*}

> **Exercise 3 . —**

> Given \(k\) lines (\(k\geq 0\)) on a plane such that no two lines are parallel and no three lines meet at the same point, let \(P(k)\) be the number of regions into which the lines divide the plane (including the infinite ones (see [Figure 8.2.3 [UNRESOLVED_INTERNAL_LINK]](s-Sequences.html#exercise-8-2-3)). Describe how the recurrence relation \(P(k) = P(k - 1) + k\) can be derived. Given that \(P(0) = 1\text{,}\) determine \(P(5)\text{.}\)

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/exercise-8-2-3.png)

> **Exercise 4 . —**

> A sample of a radioactive substance is expected to decay by 0.15 percent each hour. If \(w_t,\) \(t \geq  0\text{,}\) is the weight of the sample \(t\) hours into an experiment, write a recurrence relation for \(w\text{.}\)

> **Exercise 5 . —**

> Let \(M(n)\) be the number of multiplications needed to evaluate an \(n^{th}\) degree polynomial. Use the recursive definition of a polynomial expression to define \(M\) recursively.

> **Exercise 6 . —**

> Let \(S\) be sequence of integers.   Using short English sentences, not symbols, describe what the following propositions say  about \(S\text{.}\)  Are the two propositions equivalent?
> 
> \(\displaystyle (\forall M)_{\mathbb{N}}((\exists  n)_{\mathbb{N}}(S(n)\geq M))\)
> \(\displaystyle (\forall M)_{\mathbb{N}}((\exists  N)_{\mathbb{N}}((\forall  n)_{\mathbb{N}}(n \geq N \rightarrow S(n)\geq M)))\)
