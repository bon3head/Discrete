---
source_relative_path: "DM TXT/5-Intro_to_Matrix_Algebra/ads Laws of Matrix Algebra.html"
source_sha256: "fd2d8aab9e334e64bc4d9e476f22799dcb87d5dce04e553a1f9ec0661241ee7b"
scope_class: active_candidate
displayed_section_or_chapter: "Section 5.3 Laws of Matrix Algebra"
---

# Section 5.3 Laws of Matrix Algebra

# Subsection 5.3.1 The Laws

The following is a summary of the basic laws of matrix operations. Assume that the indicated operations are defined; that is, that the orders of the matrices \(A\text{,}\) \(B\) and \(C\) are such that the operations make sense.

![Table 5.3.1 . Laws of Matrix Algebra (1) Commutative Law of Addition \(A + B = B + A\) (2) Associative Law of Addition \(A + (B + C) = (A + B) + C\) (3) Distributive Law of a Scalar over Matrices \(c(A + B) = c A + c B\text{,}\) where \(c \in \mathbb{R}\text{.}\) (4) Distributive Law of Scalars over a Matrix \(\left(c_1 + c_2 \right)A = c_1A +c_2 A\text{,}\) where \(c_1, c_2 \in \mathbb{R}\text{.}\) (5) Associative Law of Scalar Multiplication \(c_1 \left(c_2 A\right) =\left(c_1 \cdot c_2 \right)A\text{,}\) where \(c_1, c_2 \in \mathbb{R}\text{.}\) (6) Zero Matrix Annihilates all Products \(\pmb{0}A = \pmb{0}\text{,}\) where \(\pmb{0}\) is the zero matrix. (7) Zero Scalar Annihilates all Products \(0 A =\pmb{0}\text{,}\) where 0 on the left is the scalar zero. (8) Zero Matrix is an identity for Addition \(A + \pmb{0} = A\text{.}\) (9) Negation produces additive inverses \(A + (-1)A = \pmb{0}\text{.}\) (10) Right Distributive Law of Matrix Multiplication \((B + C)A = B A + C A\text{.}\) (11) Left Distributive Law of Matrix Multiplication \(A(B + C) = A B + A C\text{.}\) (12) Associative Law of Multiplication \(A(B C) = (A B)C\text{.}\) (13) Identity Matrix is a Multiplicative Identity \(I A = A\) and \(A I = A\text{.}\) (14) Involution Property of Inverses If \(A^{-1}\) exists, \(\left(A^{-1} \right)^{-1} = A\text{.}\) (15) Inverse of Product Rule If \(A^{-1}\) and \(B^{-1}\) exist, \((A B)^{-1}= B^{-1}A^{-1}\)]()

# Subsection 5.3.2 Commentary

> **Example 5.3.2 — More Precise Statement of one Law.**

> If we wished to write out each of the above laws more completely, we would specify the orders of the matrices. For example, Law 10 should read:

Remarks:

Notice the absence of the “law” \(A B = B A\text{.}\) Why?
Is it really necessary to have both a right (No. 11) and a left (No. 10) distributive law? Why?

> **Exercise 1 . —**

> Rewrite the above laws specifying as in [Example 5.3.2 [UNRESOLVED_INTERNAL_LINK]](s-laws-of-matrix-algebra.html#ex-statement-precise) the orders of the matrices.

> **Exercise 2 . —**

> Verify each of the Laws of Matrix Algebra using examples.

> **Exercise 3 . —**

> Let \(A = \left(
> \begin{array}{cc}
> 1 & 2 \\
> 0 & -1 \\
> \end{array}
> \right)\text{,}\) \(B= \left(
> \begin{array}{ccc}
> 3 & 7 & 6 \\
> 2 & -1 & 5 \\
> \end{array}
> \right)\text{,}\) and \(C= \left(
> \begin{array}{ccc}
> 0 & -2 & 4 \\
> 7 & 1 & 1 \\
> \end{array}
> \right)\text{.}\) Compute the following as efficiently as possible by using any of the Laws of Matrix Algebra:

> \(\displaystyle A B + A C\)
> \(\displaystyle A^{-1}\)
> \(\displaystyle A(B + C)\)
> \(\displaystyle \left(A^2\right)^{-1}\)
> \(\displaystyle (C + B)^{-1}A^{-1}\)

> **Exercise 4 . —**

> Let \(A =\left(
> \begin{array}{cc}
> 7 & 4 \\
> 2 & 1 \\
> \end{array}
> \right)\) and \(B =\left(
> \begin{array}{cc}
> 3 & 5 \\
> 2 & 4 \\
> \end{array}
> \right)\text{.}\) Compute the following as efficiently as possible by using any of the Laws of Matrix Algebra:

> \(\displaystyle A B\)
> \(\displaystyle A + B\)
> \(\displaystyle A^2 + A B + B A + B ^2\)
> \(\displaystyle B^{-1}A^{-1}\)
> \(\displaystyle A^2 + B A\)

> **Exercise 5 . —**

> Let \(A\) and \(B\) be \(n\times n\) matrices of real numbers. Is \(A^2-B^2= (A-B)(A+B)\text{?}\)  Explain.
