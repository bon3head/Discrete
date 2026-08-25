---
source_relative_path: "DM TXT/5-Intro_to_Matrix_Algebra/ads Special Types of Matrices.html"
source_sha256: "2b530046e33e528fbe0c6cb30a6dc254c6136f580b474a6f846d560e699ba703"
scope_class: active_candidate
displayed_section_or_chapter: "Section 5.2 Special Types of Matrices"
---

# Section 5.2 Special Types of Matrices

# Subsection 5.2.1 Diagonal Matrices

We have already investigated, in exercises in the previous section, one special type of matrix. That was the  zero matrix, and found that it behaves in matrix algebra in an analogous fashion to the real number 0; that is, as the additive identity. We will now investigate the properties of a few other special matrices.

> **Definition 5.2.1 — Diagonal Matrix.**

> A square matrix D is called a diagonal matrix if \(d_{i j}\) = 0 whenever \(i \neq  j\text{.}\)

> **Example 5.2.2 — Some diagonal matrices.**

> \(A = \left(
> \begin{array}{ccc}
> 1 & 0 & 0 \\
> 0 & 2 & 0 \\
> 0 & 0 & 5 \\
> \end{array}
> \right)\text{,}\) \(B= \left(
> \begin{array}{ccc}
> 3 & 0 & 0 \\
> 0 & 0 & 0 \\
> 0 & 0 & -5 \\
> \end{array}
> \right)\text{,}\) and \(I = \left(
> \begin{array}{ccc}
> 1 & 0 & 0 \\
> 0 & 1 & 0 \\
> 0 & 0 & 1 \\
> \end{array}
> \right)\) are all diagonal matrices.

# Subsection 5.2.2 The Identity Matrix and Matrix Inverses

In the example above, the \(3\times 3\) diagonal matrix \(I\) whose diagonal entries are all 1’s has the distinctive property that for any other \(3\times 3\) matrix \(A\) we have \(A I = I A = A\text{.}\) For example:

> **Example 5.2.3 — Multiplying by the Identity Matrix.**

> If \(A = \left(
> \begin{array}{ccc}
> 1 & 2 & 5 \\
> 6 & 7 & -2 \\
> 3 & -3 & 0 \\
> \end{array}
> \right)\text{,}\) then \(A I =\left(
> \begin{array}{ccc}
> 1 & 2 & 5 \\
> 6 & 7 & -2 \\
> 3 & -3 & 0 \\
> \end{array}
> \right)\) and \(I A = \left(
> \begin{array}{ccc}
> 1 & 2 & 5 \\
> 6 & 7 & -2 \\
> 3 & -3 & 0 \\
> \end{array}
> \right)\text{.}\)

In other words, the matrix \(I\) behaves in matrix algebra like the real number 1; that is, as a multiplicative identity. In matrix algebra, the matrix \(I\) is called simply the identity matrix. Convince yourself that if \(A\) is any \(n\times n\) matrix \(A I = I A = A\text{.}\)

> **Definition 5.2.4 — Identity Matrix.**

> The \(n\times n\) diagonal matrix \(I_n\) whose diagonal components are all 1’s is called the identity matrix.  If the context is clear, we simply use \(I\text{.}\)

In the set of real numbers we recall that, given a nonzero real number \(x\text{,}\) there exists a real number \(y\) such that \(x y = y x
=1\text{.}\) We know that real numbers commute under multiplication so that the two equations can be summarized as \(x y = 1\text{.}\) Further we know that \(y =x^{-1}= \frac{1}{x}\text{.}\) Do we have an analogous situation in \(M_{n\times n}(\mathbb{R})\text{?}\) Can we define the multiplicative inverse of an \(n\times n\) matrix \(A\text{?}\) It seems natural to imitate the definition of multiplicative inverse in the real numbers.

> **Definition 5.2.5 — Matrix Inverse.**

> Let \(A\) be an \(n\times n\) matrix. If there exists an \(n\times n\) matrix \(B\) such that \(A B = B A =I\text{,}\) then \(B\) is a multiplicative inverse of \(A\) (called simply an inverse of \(A\)) and is denoted by \(A^{-1}\)

When we are doing computations involving matrices, it would be helpful to know that when we find \(A^{-1}\text{,}\) the answer we obtain is the only inverse of the given matrix.  This would let us refer to *the* inverse of a matrix.  We refrained from saying that in the definition, but the theorem below justifies it.

Remark: Those unfamiliar with the laws of matrix algebra should return to the following proof after they have familiarized themselves with the Laws of Matrix Algebra in Section 5.5.

> **Theorem 5.2.6 — Inverses are unique.**

> The inverse of an \(n\times n\) matrix A, when it exists, is unique.

Let \(A =\left(
\begin{array}{cc}
2 & 0 \\
0 & 3  \\
\end{array}
\right)\) .  What is \(A^{-1}\) ? Without too much difficulty, by trial and error, we determine that \(A^{-1}= \left(
\begin{array}{cc}
\frac{1}{2} & 0 \\
0 & \frac{1}{3} \\
\end{array}
\right)\) . This might lead us to guess that the inverse is found by taking the reciprocal of all nonzero entries of a matrix. Alas, it isn’t that easy!

If \(A =\left(
\begin{array}{cc}
1 & 2 \\
-3 & 5 \\
\end{array}
\right)\) , the “reciprocal rule” would tell us that the inverse of \(A\) is \(B=\left(
\begin{array}{cc}
1 & \frac{1}{2} \\
\frac{-1}{3} & \frac{1}{5} \\
\end{array}
\right)\text{.}\) Try computing \(A B\) and you will see that you don’t get the identity matrix.  So, what *is* \(A^{-1}\text{?}\) In order to understand more completely the notion of the inverse of a matrix, it would be beneficial to have a formula that would enable us to compute the inverse of at least a \(2\times 2\) matrix. To do this, we introduce the definition of the determinant of a \(2\times 2\) matrix.

> **Definition 5.2.7 — Determinant of a 2 by 2 matrix.**

> Let \(A =\left(
> \begin{array}{cc}
> a & b \\
> c & d \\
> \end{array}
> \right)\text{.}\) The determinant of \(A\) is the number \(\det  A = a d - b c\text{.}\)

In addition to \(\det  A\text{,}\) common notation for the determinant of matrix \(A\) is \(\lvert A \rvert\text{.}\)  This is particularly common when writing out the whole matrix, which case we would write \(\left|
\begin{array}{cc}
a & b \\
c & d \\
\end{array}
\right|\) for the determinant of the general \(2 \times 2\) matrix.

> **Example 5.2.8 — Some determinants of two by two matrices.**

> If \(A =\left(
> \begin{array}{cc}
> 1 & 2 \\
> -3 & 5 \\
> \end{array}
> \right)\)  then \(\det  A = 1\cdot 5 -2\cdot  (-3)=11\text{.}\) If \(B =\left(
> \begin{array}{cc}
> 1 & 2 \\
> 2 & 4 \\
> \end{array}
> \right)\)  then \(\det  B = 1\cdot 4 -2\cdot 2=0.\)

> **Theorem 5.2.9 — Inverse of 2 by 2 matrix.**

> Let \(A =\left(
> \begin{array}{cc}
> a & b \\
> c & d \\
> \end{array}
> \right)\text{.}\)  If \(\det  A\neq  0\text{,}\) then \(A^{-1} =\frac{1}{\det  A}\left(
> \begin{array}{cc}
> d & -b \\
> -c & a \\
> \end{array}
> \right)\text{.}\)

> **Example 5.2.10 — Finding Inverses.**

> Can we find the inverses of the matrices in [Example 5.2.8 [UNRESOLVED_INTERNAL_LINK]](s-special-matrices.html#ex-some-determinants)? If \(A =\left(
> \begin{array}{cc}
> 1 & 2 \\
> -3 & 5 \\
> \end{array}
> \right)\)  then
> 
> \begin{equation*}
> A^{-1}= \frac{1}{11}\left(
> \begin{array}{cc}
> 5 & -2 \\
> 3 & 1 \\
> \end{array}
> \right)=\left(
> \begin{array}{cc}
> \frac{5}{11} & -\frac{2}{11} \\
> \frac{3}{11} & \frac{1}{11} \\
> \end{array}
> \right)
> \end{equation*}
> 
> The reader should verify that \(A A^{-1}=A^{-1}A = I\text{.}\)

> The second matrix, \(B\text{,}\) has a determinant equal to zero. If we tried to apply the formula in [Theorem 5.2.9 [UNRESOLVED_INTERNAL_LINK]](s-special-matrices.html#theorem-inverse-two-by-two), we would be dividing by zero. For this reason, the formula can’t be applied and in fact \(B^{-1}\) does not exist.

Remarks:

In general, if \(A\) is a \(2\times 2\) matrix and if \(\det  A = 0\text{,}\) then \(A^{-1}\) does not exist.
A formula for the inverse of \(n\times n\) matrices \(n\geq  3\) can be derived that also involves \(\det  A\text{.}\) Hence, in general, if the determinant of a matrix is zero, the matrix does not have an inverse. However the formula for even a \(3 \times  3\) matrix is very long and is not the most efficient way to compute the inverse of a matrix.
In Chapter 12 we will develop a technique to compute the inverse of a higher-order matrix, if it exists.
Matrix inversion comes first in the hierarchy of matrix operations; therefore, \(A B^{-1}\) is \(A (B^{-1})\text{.}\)

> **Exercise 1 . —**

> For the given matrices \(A\) find \(A^{-1}\) if it exists and verify that \(A A^{-1}=A^{-1}A = I\text{.}\)  If \(A^{-1}\) does not exist explain why.

> \(\displaystyle A = \left(
> \begin{array}{cc}
> 1 & 3 \\
> 2 & 1 \\
> \end{array}
> \right)\)
> \(\displaystyle A=\left(
> \begin{array}{cc}
> 6 & -3 \\
> 8 & -4 \\
> \end{array}
> \right)\)
> \(\displaystyle A = \left(
> \begin{array}{cc}
> 1 & -3 \\
> 0 & 1 \\
> \end{array}
> \right)\)
> \(\displaystyle A = \left(
> \begin{array}{cc}
> 1 & 0 \\
> 0 & 1 \\
> \end{array}
> \right)\)
> Use the definition of the inverse of a matrix to find \(A^{-1}\text{:}\) \(A=\left(
> \begin{array}{ccc}
> 3 & 0 & 0 \\
> 0 & \frac{1}{2} & 0 \\
> 0 & 0 & -5 \\
> \end{array}
> \right)\)

> **Exercise 2 . —**

> For the given matrices \(A\) find \(A^{-1}\) if it exists and verify that \(A A^{-1}=A^{-1}A = I\text{.}\) If \(A^{-1}\) does not exist explain why.

> \(\displaystyle A =\left(
> \begin{array}{cc}
> 2 & -1 \\
> -1 & 2 \\
> \end{array}
> \right)\)
> \(\displaystyle A = \left(
> \begin{array}{cc}
> 0 & 1 \\
> 0 & 2 \\
> \end{array}
> \right)\)
> \(\displaystyle A= \left(
> \begin{array}{cc}
> 1 & c \\
> 0 & 1 \\
> \end{array}
> \right)\)
> 
> \(A = \left(
> \begin{array}{cc}
> a & b \\
> b & a \\
> \end{array}
> \right)\text{,}\) where \(\lvert a \rvert \neq \lvert b \rvert\text{.}\)

> **Exercise 3 . —**

> Let \(A = \left(
> \begin{array}{cc}
> 2 & 3 \\
> 1 & 4 \\
> \end{array}
> \right)\) and \(B =\left(
> \begin{array}{cc}
> 3 & -3 \\
> 2 & 1 \\
> \end{array}
> \right)\text{.}\) Verify that \((A B)^{-1}= B^{-1}A^{-1}\text{.}\)
> 
> Let \(A\) and \(B\) be \(n\times n\) invertible matrices. Prove that \((A B)^{-1}= B^{-1}A^{-1}\text{.}\) Why is the right side of the above statement written “backwards”? Is this necessary? Hint: Use [Theorem 5.2.6 [UNRESOLVED_INTERNAL_LINK]](s-special-matrices.html#theorem-unique-inverse)

> **Exercise 4 . —**

> Let \(A =\left(
> \begin{array}{cc}
> a & b \\
> c & d \\
> \end{array}
> \right)\text{.}\) Derive the formula for \(A^{-1}\text{.}\)

> **Exercise 5 . — Linearity of Determinants.**

> Let \(A\) and \(B\) be 2-by-2 matrices. Show that \(\det (A B) =(\det  A)(\det  B)\text{.}\)
> 
> It can be shown that the statement in part (a) is true for all \(n\times n\) matrices. Let \(A\) be any invertible \(n\times n\) matrix. Prove that \(\det \left(A^{-1}\right) =(\det  A)^{-1}\text{.}\) Note: The determinant of the identity matrix \(I_n\) is 1 for all \(n\text{.}\)
> 
> Verify that the equation in part (b) is true for the matrix in exercise 1(a) of this section.

> **Exercise 6 . —**

> Prove by induction that for \(n \geq 1\text{,}\) \(\left(
> \begin{array}{cc}
> a & 0 \\
> 0 & b \\
> \end{array}
> \right)^n= \left(
> \begin{array}{cc}
> a^n & 0 \\
> 0 & b^n \\
> \end{array}
> \right)\text{.}\)

> **Exercise 7 . —**

> Use the assumptions in [Exercise 5.2.3.5 [UNRESOLVED_INTERNAL_LINK]](s-special-matrices.html#prob-5-2-5) to prove by induction that if \(n \geq 1\text{,}\) \(\det \left(A^n\right) = (\det  A)^n\text{.}\)

> **Exercise 8 . —**

> Prove: If the determinant of a matrix \(A\) is zero, then \(A\) does not have an inverse. Hint: Use the indirect method of proof and exercise 5.

> **Exercise 9 . —**

> Let \(A, B, \textrm{ and } D\) be \(n\times n\) matrices. Assume that \(B\) is invertible. If \(A = B D B^{-1}\) , prove by induction that \(A^m= B D^m B^{-1}\) is true for \(m \geq  1\text{.}\)
> 
> Given that \(A = \left(
> \begin{array}{cc}
> -8 & 15 \\
> -6 & 11 \\
> \end{array}
> \right) = B \left(
> \begin{array}{cc}
> 1 & 0 \\
> 0 & 2 \\
> \end{array}
> \right) B^{-1}\) where \(B=\left(
> \begin{array}{cc}
> 5 & 3 \\
> 3 & 2 \\
> \end{array}
> \right)\) what is \(A^{10}\text{?}\)
