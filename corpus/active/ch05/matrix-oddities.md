---
source_relative_path: "DM TXT/5-Intro_to_Matrix_Algebra/ads Matrix Oddities.html"
source_sha256: "9869356578f2776d2180a459b188394e20f382b64eb874a2c1460b31e3600337"
scope_class: active_candidate
displayed_section_or_chapter: "Section 5.4 Matrix Oddities"
---

# Section 5.4 Matrix Oddities

# Subsection 5.4.1 Dissimilarities with elementary algebra

We have seen that matrix algebra is similar in many ways to elementary algebra. Indeed, if we want to solve the matrix equation \(A X = B\) for the unknown \(X\text{,}\) we imitate the procedure used in elementary algebra for solving the equation \(a x = b\text{.}\) One assumption we need is that \(A\) is a square matrix that has an inverse.  Notice how exactly the same properties are used in the following detailed solutions of both equations.

![Table 5.4.1 . Equation in the algebra of real numbers Equation in matrix algebra \(a x = b\) \(A X = B\) \(a^{-1}(a x) =a^{-1}b\) if \(a \neq 0\) \(A^{-1}(A X) = A^{-1}B\) if \(A^{-1 }\) exists \(\left(a^{-1} a\right)x = a^{-1} b\) Associative Property \(\left(A^{-1} A\right)X = A^{-1} B\) \(1x = a^{-1} b\) Inverse Property \(I X = A^{-1} B\) \(x = a^{-1} b\) Identity Property \(X = A^{-1} B\)]()

Certainly the solution process for solving \(A X = B\) is the same as that of solving \(a x = b\text{.}\)

The solution of \(x a = b\) is \(x = b a^{-1} = a^{-1}b\text{.}\) In fact, we usually write the solution of both equations as  \(x =\frac{b}{a}\text{.}\) In matrix algebra, the solution of \(X A = B\) is \(X = B A^{-1}\) , which is not necessarily equal to \(A^{-1} B\text{.}\) So in matrix algebra, since the commutative law (under multiplication) is not true, we have to be more careful in the methods we use to solve equations.

It is clear from the above that if we wrote the solution of \(A X = B\) as \(X=\frac{B}{A}\text{,}\) we would not know how to interpret \(\frac{B}{A}\text{.}\) Does it mean \(A^{-1} B\) or \(B A^{-1}\text{?}\)  Because of this, \(A^{-1}\) is never written as \(\frac{I}{A}\text{.}\)

> **Exercise 1 . —**

> Discuss each of the “Matrix Oddities” with respect to elementary algebra.

> **Exercise 2 . —**

> Determine \(2\times 2\) matrices which show that each of the “Matrix Oddities” are true.

> **Exercise 3 . —**

> Prove or disprove the following implications.

> \(A^2= A\) and \(\det  A \neq  0 \Rightarrow  A =I\)
> 
> \(A^2 = I \textrm{ and } \det A \neq  0 \Rightarrow  A = I \textrm{ or } A = -I\text{.}\)

> **Exercise 4 . —**

> Let \(M_{n\times n}(\mathbb{R})\) be the set of real \(n\times n\) matrices. Let \(P \subseteq  M_{n\times n}(\mathbb{R})\) be the subset of matrices defined by \(A \in  P\) if and only if \(A^2 = A\text{.}\) Let \(Q \subseteq  P\) be defined by \(A\in Q\) if and only if \(\det A \neq  0\text{.}\)

> Determine the cardinality of \(Q\text{.}\)
> 
> Consider the special case \(n = 2\) and prove that a sufficient condition for \(A \in  P \subseteq  M_{2\times 2}(\mathbb{R})\) is that \(A\) has a zero determinant (i.e., \(A\) is singular) and \(tr(A) = 1\) where \(tr(A) = a_{11}+ a _{22}\) is the sum of the main diagonal elements of \(A\text{.}\)
> 
> Is the condition of part b a necessary condition?

> **Exercise 5 . —**

> Write each of the following systems in the form \(A X = B\text{,}\) and then solve the systems using matrices.

> \(\displaystyle \begin{array}{c}2x_1+x_2=3\\
> x_1-x_2= 1\\
> \end{array}\)
> \(\displaystyle \begin{array}{c}2x_1-x_2=4\\
> x_1 -x_2= 0\\
> \end{array}\)
> \(\displaystyle \begin{array}{c}2x_1+x_2=1\\
> x_1 -x_2= 1\\
> \end{array}\)
> \(\displaystyle \begin{array}{c}2x_1+x_2=1\\
> x_1 -x_2= -1\\
> \end{array}\)
> \(\displaystyle \begin{array}{c}3x_1+2x_2=1 \\
> 6 x_1 +4x_2= -1\\
> \end{array}\)

> **Exercise 6 . —**

> For those who know calculus:

> Write the series expansion for \(e^a\) centered around \(a=0\text{.}\)
> 
> Use the idea of exercise 6 to write what would be a plausible definition of \(e^A\) where \(A\) is an \(n \times  n\) matrix.
> If \(A=\left(
> \begin{array}{cc}
> 1 & 1 \\
> 0 & 0 \\
> \end{array}
> \right)\) and \(B =\left(
> \begin{array}{cc}
> 0 & -1 \\
> 0 & 0 \\
> \end{array}
> \right)\) , use the series in part (b) to show that \(e^A= \left(
> \begin{array}{cc}
> e & e-1 \\
> 0 & 1 \\
> \end{array}
> \right)\)and \(e^B= \left(
> \begin{array}{cc}
> 1 & -1 \\
> 0 & 1 \\
> \end{array}
> \right)\text{.}\)
> 
> Show that \(e^Ae^B\neq e^Be^A\text{.}\)
> 
> Show that  \(e^{A+B}= \left(
> \begin{array}{cc}
> e & 0 \\
> 0 & 1 \\
> \end{array}
> \right)\text{.}\)
> 
> Is \(e^Ae^B=e^{A+B}\text{?}\)
