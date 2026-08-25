---
source_relative_path: "DM TXT/8-Recursion_and_Recurrence_Relations/ads Recurrence Relations.html"
source_sha256: "99130c72405d54780f50131b268c4715da906c4bad6fa39379425ca34b1e60a1"
scope_class: active_candidate
displayed_section_or_chapter: "Section 8.3 Recurrence Relations"
---

# Section 8.3 Recurrence Relations

In this section we will begin our study of recurrence relations and their solutions. Our primary focus will be on the class of finite order linear recurrence relations with constant coefficients (shortened to finite order linear relations). First, we will examine closed form expressions from which these relations arise. Second, we will present an algorithm for solving them. In later sections we will consider some other common relations (8.4) and introduce two additional tools for studying recurrence relations: generating functions (8.5) and matrix methods (Chapter 12).

# Subsection 8.3.1 Definition and Terminology

> **Definition 8.3.1 — Recurrence Relation.**

> Let \(S\) be a sequence of numbers.  A recurrence relation on \(S\) is a formula that relates all but a finite number of terms of \(S\) to previous terms of \(S\text{.}\) That is, there is a \(k_0\) in the domain of \(S\) such that if \(k \geq  k_0\text{,}\) then \(S(k)\) is expressed in terms of some (and possibly all) of the terms that precede \(S(k)\text{.}\) If the domain of \(S\) is \(\{0,1,2,\dots \}\text{,}\) the terms \(S(0), S(1), . . . , S\left(k_0-1\right)\) are not defined by the recurrence formula. Their values are the initial conditions (or boundary conditions, or basis) that complete the definition of \(S\text{.}\)

> **Example 8.3.2 — Some Examples of Recurrence Relations.**

> The Fibonacci sequence is defined by the recurrence relation \(F_k= F_{k-2}+ F_{k-1}\text{,}\) \(k\geq 2,\) with the initial conditions \(F_0=1\) and \(F_1=1\text{.}\) The recurrence relation is called a second-order relation because \(F_k\) depends on the two previous terms of \(F\text{.}\) Recall that the sequence \(C\) in Section 8.2, [Example 8.2.2 [UNRESOLVED_INTERNAL_LINK]](s-Sequences.html#ex-three-sequences), can be defined with the same recurrence relation, but with different initial conditions.
> The relation \(T(k) = 2T(k - 1)^2 - k T(k - 3)\) is a third-order recurrence relation. If values of \(T(0)\text{,}\) \(T(1)\text{,}\) and \(T(2)\) are specified, then \(T\) is completely defined.
> The recurrence relation \(S(n) = S(\lfloor n/2\rfloor ) + 5\text{,}\) \(n > 0\text{,}\) with \(S(0)=0\) has infinite order. To determine \(S(n)\) when \(n\) is even, you must go back \(n/2\) terms. Since \(n/2\) grows unbounded with \(n\text{,}\) no finite order can be given to \(S\text{.}\)

# Subsection 8.3.2 Solving Recurrence Relations

Sequences are often most easily defined with a recurrence relation; however, the calculation of terms by directly applying a recurrence relation can be time-consuming. The process of determining a closed form expression for the terms of a sequence from its recurrence relation is called solving the relation. There is no single technique or algorithm that can be used to solve all recurrence relations. In fact, some recurrence relations cannot be solved. The relation that defines \(T\) above is one such example. Most of the recurrence relations that you are likely to encounter in the future are classified as finite order linear recurrence relations with constant coefficients. This class is the one that we will spend most of our time with in this chapter.

> **Definition 8.3.3 — \(n^{th}\) Order Linear Recurrence Relation.**

> Let \(S\) be a sequence of numbers with domain \(k\geq 0\text{.}\) An \(n^{\textrm{th}}\) order linear recurrence relation on \(S\) with constant coefficients is a recurrence relation that can be written in the form
> 
> \begin{equation*}
> S(k) + C_1 S(k - 1) + . . . + C_n S(k - n) = f(k)\textrm{  for  }k \geq  n
> \end{equation*}
> 
> where \(C_1, C_2, \ldots , C_n\) are constants and \(f\) is a numeric function that is defined for \(k \geq n\text{.}\)

Note: We will shorten the name of this class of relations to \(n^{\textrm{th}}\) order linear relations. Therefore, in further discussions, \(S(k)
+ 2k S(k - 1) = 0\) would not be considered a first-order linear relation.

> **Example 8.3.4 — Some Finite Order Linear  Relations.**

> The Fibonacci sequence is defined by the second-order linear relation because \(F_k- F_{k-1}- F_{k-2}=0\)
> 
> The relation \(P(j) + 2P(j - 3) = j^2\) is a third-order linear relation. In this case, \(C_1= C_2= 0\text{.}\)
> 
> The relation \(A(k)= 2(A(k - 1) + k)\) can be written as \(A(k) - 2A(k - 1) = 2k\text{.}\) Therefore, it is a first-order linear relation.

# Subsection 8.3.3 Recurrence Relations Obtained from “Solutions”

Before giving an algorithm for solving finite order linear relations, we will examine recurrence relations that arise from certain closed form expressions. The closed form expressions are selected so that we will obtain finite order linear relations from them. This approach may seem a bit contrived, but if you were to write down a few simple algebraic expressions, chances are that most of them would be similar to the ones we are about to examine.

For our first example, consider \(D\text{,}\) defined by \(D(k) =5\cdot 2^k\text{,}\) \(k \geq  0\text{.}\) If \(k \geq  1\text{,}\) \(\quad\)\(D(k) =5\cdot 2^k = 2\cdot 5\cdot 2^{k-1} = 2 D(k - 1)\text{.}\) Therefore, \(D\) satisfies the first order linear relation \(D(k) - 2 D(k - 1) = 0\) and the initial condition \(D(0) = 5\) serves as an initial condition for \(D\text{.}\)

As a second example, consider \(C(k) =3^{k-1}+2^{k+1}+k\) , \(k \geq  0\text{.}\) Quite a bit more algebraic manipulation is required to get our result:

![Table 8.3.5 . \(C(k) =3^{k-1}+2^{k+1}+k\) \(\textrm{Original equation}\) \(3C(k-1) =3^{k-1}+3\cdot 2^k+3(k-1)\) \(\textrm{Substitute } k-1 \textrm{ for } k \) \(\textrm{ and multiply by } 3\) \(\) \(\textrm{Subtract the second equation}\) \(\textrm{from the first.}\) \(C(k)-3C(k-1)=-2^k-2k+3\) \(3^{k-1} \textrm{ term is eliminated.} \) \(\textrm{ This is a first order relation}\text{.}\) \(2C(k-1)-6C(k-2)=-2^k-2(2(k-1))+6\) \(\textrm{Substitute } k-1 \textrm{ for } k \textrm{ in the}\) \(\textrm{third equation, multiply by } 2\text{.}\) \(\) \(\textrm{Subtract the 4th equation from the 3rd.}\) \(C(k)-5C(k-1)+6C(k-2)=2k-7\) \(2^{k+1}\textrm{term is eliminated.}\) \(\textrm{This is 2nd order relation.}\)]()

The recurrence relation that we have just obtained, defined for \(k \geq  2\text{,}\) together with the initial conditions \(C(0) = 7/3\) and \(C(1) = 6\text{,}\) define \(C\text{.}\)

[Table 8.3.6 [UNRESOLVED_INTERNAL_LINK]](s-recurrence-relations.html#table-reverse-solutions-rr) summarizes our results together with a few other examples that we will let the reader derive. Based on these results, we might conjecture that any closed form expression for a sequence that combines exponential expressions and polynomial expressions will be solutions of finite order linear relations. Not only is this true, but the converse is true: a finite order linear relation defines a closed form expression that is similar to the ones that were just examined. The only additional information that is needed is a set of initial conditions.

![Table 8.3.6 . Recurrence Relations Obtained from Given Sequences Closed Form Expression Recurrence Relation \(D(k)=5\cdot 2^k\) \(D(k)-2D(k-1)=0\) \(C(k)=3^{k-1}+2^{k+1}+k\) \(C(k)-2C(k-1)-6C(k-2)=2k-7\) \(Q(k)=2k + 9\) \(Q(k)-Q(k-1)=2\) \(A(k)=k^2-k\) \(A(k)-2A(k-1)+A(k-2)=2\) \(B(k)=2 k^2+1\) \(B(k)-2B(k-1)+B(k-2)=4\) \(G(k)=2\cdot 4^k-5(-3)^k\) \(G(k)-G(k-1)+12G(k-2)=0\) \(J(k)=(3+k) 2^k\) \(J(k)-4J(k-1)+4J(k-2)=0\)]()

> **Definition 8.3.7 — Homogeneous Recurrence Relation.**

> An \(n^{th}\) order linear relation is homogeneous if \(f(k)
> = 0\) for all \(k\text{.}\) For each recurrence relation \(S(k) + C_1S(k - 1) +\ldots + C_n S(k - n) = f(k)\text{,}\) the associated homogeneous relation is \(S(k)
> + C_1S(k - 1) +\ldots + C_n S(k - n) =0\)

> **Example 8.3.8 — First Order Homogeneous Recurrence Relations.**

> \(D(k) - 2D(k - 1) = 0\) is a first-order homogeneous relation. Since it can also be written as \(D(k) = 2D(k - 1)\text{,}\) it should be no surprise that it arose from an expression that involves powers of 2. More generally, you would expect that the solution of \(L(k) - a L(k - 1)\) would involve \(a^k\text{.}\) Actually, the solution is \(L(k) = L(0)a^k\text{,}\) where the value of \(L(0)\) is given by the initial condition.

> **Example 8.3.9 — A Second Order Example.**

> Consider the second-order homogeneous relation \(S(k) - 7S(k - 1) + 12 S(k- 2) = 0\) together with the initial conditions \(S(0) = 4\) and \(S(1) = 4\text{.}\) From our discussion above, we can predict that the solution to this relation involves terms of the form \(b a^k\text{,}\) where \(b\) and \(a\) are nonzero constants that must be determined. If the solution were to equal this quantity exactly, then
> 
> \begin{equation*}
> \quad \quad \quad  \begin{array}{ccc}
> S(k)=b a^k &   &   \\
> S(k-1)=b a^{k-1} & \textrm{   } & \textrm{  } \\
> S(k-2)=b a^{k-2} &   &   \\
> \end{array}
> \end{equation*}
> 
> Substitute these expressions into the recurrence relation to get
> 
> \begin{equation*}
> b a^k-7 b a^{k-1}+12 b a^{k-2}=0
> \end{equation*}
> 
> Each term on the left-hand side of this equation has a factor of \(b a^{k-2}\text{,}\) which is nonzero. Dividing through by this common factor yields
> 
> \begin{gather}
> a^2 - 7a + 12 = (a - 3) (a - 4) = 0\tag{8.3.1}
> \end{gather}

> Therefore, the only possible values of \(a\) are 3 and 4. Equation [(8.3.1) [UNRESOLVED_INTERNAL_LINK]](s-recurrence-relations.html#ex-second-order-rr-2-10) is called the characteristic equation of the recurrence relation. The fact is that our original recurrence relation is true for any sequence of the form \(S(k) = b_1 3^k + b_24^k\text{,}\) where \(b_1\) and \(b_2\) are real numbers. This set of sequences is called the general solution of the recurrence relation. If we didn’t have initial conditions for \(S\text{,}\) we would stop here. The initial conditions make it possible for us to find definite values for \(b_1\) and \(b_2\text{.}\)
> 
> 
> \begin{equation*}
> \left\{
> \begin{array}{c}
> S(0)=4 \\
> S(1)=4 \\
> \end{array}
> \right\}\textrm{  }\Rightarrow \left\{
> \begin{array}{c}
> b_13^0+b_24^0=4 \\
> b_13^1+b_24^1=4 \\
> \end{array}
> \right\}\textrm{  }\Rightarrow \left\{
> \begin{array}{c}
> b_1+b_2=4 \\
> 3b_1+4b_2=4 \\
> \end{array}
> \right\}\textrm{  }
> \end{equation*}

> The solution of this set of simultaneous equations is \(b_1 = 12\) and \(b_2 = -8\) and so the solution is \(S(k) = 12 \cdot 3^k - 8 \cdot 4^k\text{.}\)

> **Definition 8.3.10 — Characteristic Equation.**

> The characteristic equation of the homogeneous \(n^{\textrm{th}}\) order linear relation \(S(k) + C_1 S(k- 1) +\ldots + C_n S(k - n) =0\) is the \(n\)th degree polynomial equation
> 
> \begin{equation*}
> a^n+\sum_{j=1}^n C_j a^{n-j}=a^n+ C_1a^{n-1}+\cdots +C_{n-1}a+C_n=0
> \end{equation*}
> 
> The left-hand side of this equation is called the characteristic polynomial.  The roots of the characteristic polynomial are called the characteristic roots of the equation.

> **Example 8.3.11 — Some characteristic equations.**

> The characteristic equation of \(F(k) - F(k - 1) - F(k - 2) = 0\) is \(a^2-a-1=0\text{.}\)
> 
> The characteristic equation of \(Q(k) + 2Q(k - 1) - 3Q(k - 2) - 6 Q(k- 4) = 0\) is \(a^4+ 2a^3 - 3a^2 - 6 = 0.\) Note that the absence of a \(Q(k - 3)\) term means that there is not an \(x^{4-3}=x\) term appearing in the characteristic equation.

Although this algorithm is valid for all values of \(n\text{,}\) there are limits to the size of \(n\) for which the algorithm is feasible. Using just a pencil and paper, we can always solve second-order equations. The quadratic formula for the roots of \(a x^2 + b x + c = 0\) is

\begin{equation*}
x=\frac{-b\pm \sqrt{b^2-4 a c}}{2 a}
\end{equation*}

The solutions of \(a^2+ C_1a + C_2 = 0\) are then

\begin{equation*}
\frac{1}{2}\left(-C_1+\sqrt{C_1{}^2-4 C_2}\right)\textrm{ and }\frac{1}{2}\left(-C_1-\sqrt{C_1{}^2-4 C_2}\right)
\end{equation*}

Although cubic and quartic formulas exist, they are too lengthy to introduce here. For this reason, the only higher-order relations (\(n\geq 3\)) that you could be expected to solve by hand are ones for which there is an easy factorization of the characteristic polynomial.

> **Example 8.3.13 — A solution using the algorithm.**

> Suppose that \(T\) is defined by \(T(k) =7T(k-1)-10T(k-2)\text{,}\) with \(T(0) = 4\) and \(T(1) = 17\text{.}\) We can solve this recurrence relation with [Algorithm 8.3.12 [UNRESOLVED_INTERNAL_LINK]](s-recurrence-relations.html#algorithm-linear-homogeneous-recurrence-relations):

> Note that we have written the recurrence relation in “nonstandard” form. To avoid errors in this easy step, you might consider a rearrangement of the equation to, in this case, \(T(k) -7T(k-1)+10T(k-2)=0\text{.}\) Therefore, the characteristic equation is \(a^2 -7a + 10 = 0\text{.}\)
> 
> The characteristic roots are \(\frac{1}{2}\left(7+\sqrt{49-40}\right)=5\) and \(\frac{1}{2}\left(7-\sqrt{49-40}\right)=2\text{.}\) These roots can be just as easily obtained by factoring the characteristic polynomial into \((a - 5)(a - 2)\text{.}\)
> 
> The general solution of the recurrence relation is \(T(k) =b_12^k+ b_25^k\text{.}\)
> 
> 
> \(\quad\) \(\left\{
> \begin{array}{c}
> T(0)=4 \\
> T(1)=17 \\
> \end{array}
> \right\}\textrm{  }\Rightarrow \left\{
> \begin{array}{c}
> b_12^0+b_25^0=4 \\
> b_12^1+b_25^1=17 \\
> \end{array}
> \right\}\textrm{  }\Rightarrow \left\{
> \begin{array}{c}
> b_1+b_2=4 \\
> 2b_1+5b_2=17 \\
> \end{array}
> \right\}\textrm{  }\) The simultaneous equations have the solution \(b_1=1\) and \(b_2=3\text{.}\) Therefore, \(T(k)=2^{k }+3\cdot 5^k\text{.}\)

Here is one rule that might come in handy: If the coefficients of the characteristic polynomial are all integers, with the constant term equal to \(m\text{,}\) then the only possible rational characteristic roots are divisors of \(m\) (both positive and negative).

With the aid of a computer (or possibly only a calculator), we can increase \(n\text{.}\) Approximations of the characteristic roots can be obtained by any of several well-known methods, some of which are part of standard software packages. There is no general rule that specifies the values of \(n\) for which numerical approximations will be feasible. The accuracy that you get will depend on the relation that you try to solve. (See Exercise 17 of this section.)

> **Example 8.3.14 — Solution of a Third Order Recurrence Relation.**

> Solve \(S(k) - 7S(k - 2) + 6S(k - 3) = 0\text{,}\) where \(S(0) =8\text{,}\) \(S(1) = 6\text{,}\) and \(S(2) = 22\text{.}\)

> The characteristic equation is \(a^3 - 7a + 6 = 0\text{.}\)
> 
> The only rational roots that we can attempt are \(\pm  1, \pm 2, \pm 3, \textrm{and} \pm 6\text{.}\) By checking these, we obtain the three roots 1, 2, and \(-3\text{.}\)
> 
> The general solution is \(S(k) =b_11^k+b_22^k+b_3(-3){}^k\text{.}\) The first term can simply be written \(b_1\) .
> 
> \(\left\{
> \begin{array}{c}
> S(0)=8 \\
> S(1)=6 \\
> S(2)=22 \\
> \end{array}
> \right\}\textrm{   }\Rightarrow \left\{
> \begin{array}{c}
> b_1+b_2+b_3=8 \\
> b_1+2b_2-3b_3=6 \\
> b_1+4b_2+9b_3=22 \\
> \end{array}
> \right\}\textrm{  }\) You can solve this system by elimination to obtain \(b_1=5\text{,}\) \(b_2=2\text{,}\) and \(b_3=1\text{.}\) Therefore, \(\quad\)\(S(k) = 5 + 2\cdot 2^k + (-3)^k = 5 + 2^{k+1} + (-3)^k\)

> **Example 8.3.15 — Solution with a Double Characteristic Root.**

> Solve \(D(k) - 8D(k - 1) + 16D(k - 2) = 0\text{,}\) where \(D(2) = 16\) and \(D(3) = 80\text{.}\)

> Characteristic equation: \(a^2- 8a + 16 = 0\text{.}\)
> 
> 
> \(a^2- 8a + 16 = (a - 4)^2\text{.}\) Therefore, there is a double characteristic root, 4.
> General solution: \(D(k) = \left(b_{1,0}+b_{1,1}k\right)4^k\text{.}\)
> 
> 
> 
> \begin{equation*}
> \begin{split}
> \left\{
> \begin{array}{c}
> D(2)=16 \\
> D(3)=80 \\
> \end{array}
> \right\}\textrm{  } \amp \Rightarrow 
> \left\{
> \begin{array}{c}
> \left(b_{1,0}+b_{1,1}2\right)4^2=16 \\
> \left(b_{1,0}+b_{1,1}3\right)4^3=80 \\
> \end{array}
> \right\}\textrm{  } \\ \amp \Rightarrow \left\{
> \begin{array}{c}
> 16b_{1,0}+32b_{1,1}=16 \\
> 64b_{1,0}+192b_{1,1}=80 \\
> \end{array}
> \right\} \Rightarrow  \left\{
> \begin{array}{c}
> b_{1,0}=\frac{1}{2} \\
> b_{1,1}=\frac{1}{4} \\
> \end{array}
> \right\}
> \end{split}
> \end{equation*}
> 
> Therefore \(D (k) = (1/2 + (1/4) k) 4^k= (2 + k)4^{k-1}\text{.}\)

# Subsection 8.3.4 Solution of Nonhomogeneous Finite Order Linear Relations

Our algorithm for nonhomogeneous relations will not be as complete as for the homogeneous case. This is due to the fact that different right-hand sides (\(f(k)\)’s) call for different rules in obtaining a particular solution.

![Table 8.3.17 . Particular solutions for given right-hand sides Right Hand Side, \(f(k)\) Form of Particular Solution, \(S^{(p)}(k)\) Constant, \(q\) Constant, \(d\) Linear Function, \(q_0+q_1 k\) Linear Function, \(d_0+d_1 k\) \(m^{th}\) degree polynomial, \(q_0+q_1k+\cdots +q_m k^m\) \(m^{th}\) degree polynomial, \(d_0+d_1k+\cdots +d_m k^m\) exponential function, \(q a^k\) exponential function, \(d a^k\)]()

> **Example 8.3.18 — Solution of a Nonhomogeneous First Order Recurrence Relation.**

> Solve \(S(k) + 5S(k - 1) = 9\text{,}\) with \(S(0) = 6\text{.}\)

> The associated homogeneous relation,\(S(k) + 5S(k - 1) = 0\) has the characteristic equation \(a + 5 = 0\text{;}\) therefore, \(a = -5\text{.}\) The homogeneous solution is \(S^{(h)}(k) =b (-5)^k\text{.}\)
> 
> Since the right-hand side is a constant, we guess that the particular solution will be a constant, \(d\text{.}\)
> 
> If we substitute \(S^{(p)}(k) = d\) into the recurrence relation, we get \(d + 5d = 9\text{,}\) or \(6d = 9\text{.}\) Therefore, \(S^{(p)}(k)=1.5\text{.}\)
> 
> The general solution of the recurrence relation is \(\quad\)\(S(k)= S^{(h)}(k)+S^{(p)}(k) =b (-5)^k+1.5\) The initial condition will give us one equation to solve in order to determine \(b\text{.}\) \(\quad\)\(S(0) = 6 \Rightarrow \textrm{   }b(-5)^0+ 1.5 = 6\textrm{   }\Rightarrow \textrm{    }b\textrm{  }+ 1.5 = 6\) Therefore, \(b = 4.5\) and \(S(k) = 4.5(-5)^k + 1.5\text{.}\)

> **Example 8.3.19 — Solution of a Nonhomogeneous Second Order Recurrence Relation.**

> Consider \(T(k) - 7T(k - 1) + 10T(k - 2) = 6 + 8k\) with \(T(0) = 1\) and \(T(1) = 2\text{.}\)

> From [Example 8.3.13 [UNRESOLVED_INTERNAL_LINK]](s-recurrence-relations.html#ex-hrr-solution-example-1), we know that \(T^{(h)}(k)=b_12^k+ b_25^k\text{.}\) Caution:Don’t apply the initial conditions to \(T^{(h)}\) until you add \(T^{(p)}\text{!}\)
> 
> Since the right-hand side is a linear polynomial, \(T^{(p)}\) is linear; that is, \(T^{(p)}(k)=d_0+d_1k\text{.}\)
> 
> Substitution into the recurrence relation yields: \(\left(d_0+d_1k\right)-7\left(d_0+d_1(k-1)\right)+10\left(d_0+d_1(k-2)\right)=6+8k\) \(\quad\)\(\Rightarrow  \left(4d_0-13d_1\right)+ \left(4d_1\right)k = 6 + 8 k\) Two polynomials are equal only if their coefficients are equal. Therefore, \(\quad\) \(\left\{
> \begin{array}{c}
> 4d_0-13d_1=6 \\
> 4d_1=8 \\
> \end{array}
> \right\}\Rightarrow \left\{
> \begin{array}{c}
> d_0=8 \\
> d_1=2 \\
> \end{array}
> \right\}\)
> 
> 
> Use the general solution \(T(k) =b_12^k+ b_25^k+8+2k\) and the initial conditions to get a final solution: \(\quad\) \(\left\{
> \begin{array}{c}
> T(0)=1 \\
> T(1)=2 \\
> \end{array}
> \right\}\textrm{  }\Rightarrow \left\{
> \begin{array}{c}
> b_1+ b_2+8=1 \\
> 2b_1+5b_2+10=2 \\
> \end{array}
> \right\}\textrm{  }\\
> \\
> \quad \quad \Rightarrow \left\{
> \begin{array}{c}
> b_1+b_2=-7 \\
> 2b_1+5b_2=-8 \\
> \end{array}
> \right\}\\
> \\
> \quad \quad \Rightarrow \left\{
> \begin{array}{c}
> b_1=-9 \\
> b_2=2 \\
> \end{array}
> \right\}\textrm{  }\)
> 
> Therefore,  \(T(k) =-9\cdot 2^k+ 2\cdot 5^k+8+2k\text{.}\)

> **Example 8.3.21 — A Sort of Annuity.**

> Suppose you open a savings account that pays an annual interest rate of \(8\%\text{.}\) In addition, suppose you decide to deposit one dollar when you open the account, and you intend to double your deposit each year. Let \(B(k)\) be your balance after \(k\) years. \(B\) can be described by the relation \(B(k) = 1.08 B(k - 1) + 2^k\text{,}\) with \(S(0) = 1\text{.}\) If, instead of doubling the deposit each year, you deposited a constant amount, \(q\text{,}\) the \(2^k\) term would be replaced with \(q\text{.}\)  A sequence of regular deposits such as this is called a simple annuity.

> Returning to the original situation,

> \(\displaystyle B^{(h)}(k)=b_1(1.08){}^k\)
> 
> \(B^{(p)}(k)\) should be of the form \(d 2^k\text{.}\)
> 
> 
> 
> \begin{equation*}
> \begin{split}
> d 2^k = 1.08d 2^{k-1}+2^k & \Rightarrow (2d) 2^{k-1} = 1.08d 2^{k-1}+ 2\cdot 2^{k-1}\\
> & \Rightarrow  2d = 1.08 d + 2\\
> &\Rightarrow .92d = 2 \\
> &\Rightarrow d= 2.174 \textrm{  to the nearest thousandth})
> \end{split}
> \end{equation*}
> 
> Therefore \(B^{(p)}(k)=2.174\cdot  2^k\text{.}\)
> 
> 
> 
> \(B(0) = 1 \Rightarrow \textrm{   }b_1+2.174 = 1\\
> \\ 
> \quad     \Rightarrow \textrm{   }b_1= -1.174\)
> Therefore,  \(B(k) = -1.174\cdot  1.08^k+ 2.174\cdot  2^k\text{.}\)

> **Example 8.3.22 — Matching Roots.**

> Find the general solution to \(S(k) - 3 S(k - 1) - 4 S(k - 2) = 4^k\text{.}\)

> The characteristic roots of the associated homogeneous relation are \(-1\) and 4. Therefore, \(S^{(h)}(k)=b_1(-1){}^k+ b_2 4^k\text{.}\)
> 
> A function of the form \(d 4^k\) will not be a particular solution of the nonhomogeneous relation since it solves the associated homogeneous relation. When the right-hand side involves an exponential function with a base that equals a characteristic root,you should multiply your guess at a particular solution by \(k\text{.}\) Our guess at \(S^{(p)}(k)\) would then be \(d k 4^k\) . See [Observation 8.3.23 [UNRESOLVED_INTERNAL_LINK]](s-recurrence-relations.html#obs-matching-base) for a more complete description of this rule.
> 
> Substitute \(d k 4^k\) into the recurrence relation for \(S(k)\text{:}\)
> 
> 
> \begin{equation*}
> \begin{array}{c}
> d k 4^k-3d (k-1) 4^{k-1}-4d (k-2) 4^{k-2}=4^k\\
> 16d k 4^{k-2}-12d (k-1) 4^{k-2}-4d (k-2) 4^{k-2}=4^k\\
> \end{array}
> \end{equation*}
> 
> Each term on the left-hand side has a factor of \(4^{k-2}\)
> 
> 
> \begin{equation*}
> 16 d k - 12d(k - 1) - 4d(k - 2) = 4^220 d = 16 \Rightarrow d=0.8
> \end{equation*}
> 
> Therefore, \(S^{(p)}(k) = 0.8 k 4^k\text{.}\)
> 
> 
> 
> The general solution to the recurrence relation is
> 
> \begin{equation*}
> S(k) =b_1(-1){}^k+ b_2 4^k +0.8 k 4^k
> \end{equation*}

> **Example 8.3.24 — Examples of matching bases.**

> If  \(S(k) - 9S(k - 1) + 20 S(k - 2) = 2\cdot 5^k\text{,}\) the characteristic roots are 4 and 5.  Since 5 matches the base of the right side, \(S^{(p)}(k)\) will take the form \(d k 5^k\text{.}\)
> 
> If \(S(n)- 6S(n - 1) + 9 S(n - 2) = 3^{n+1}\) the only characteristic root is 3, but it is a double root (multiplicity 2). Therefore, the form of the particular solution is \(d n^2 3^n\text{.}\)
> 
> If \(Q(j)-Q(j-1)-12Q(j-2)=(-3)^j+ 6\cdot 4^j\text{,}\) the characteristic roots are \(-3\) and 4. The form of the particular solution will be \(d_1j (-3)^j+ d_2j\cdot 4^j\text{.}\)
> 
> If \(S(k) - 9S(k - 1) + 8S(k- 2) = 9k + 1 = (9k + 1)1^k\text{,}\) the characteristic roots are 1 and 8. If the right-hand side is a polynomial, as it is in this case, then the exponential factor \(1^k\) can be introduced. The particular solution will take the form \(k\left(d_0+ d_1k\right)\text{.}\)

We conclude this section with a comment on the situation in which the characteristic equation gives rise to complex roots. If we restrict the coefficients of our finite order linear relations to real numbers, or even to integers, we can still encounter characteristic equations whose roots are complex. Here, we will simply take the time to point out that our algorithms are still valid with complex characteristic roots, but the customary method for expressing the solutions of these relations is different. Since an understanding of these representations requires some background in complex numbers, we will simply suggest that an interested reader can refer to a more advanced treatment of recurrence relations (see also difference equations).

Exercise Group.
Solve the following sets of recurrence relations and initial conditions:

1.

\(S(k) - 10S(k - 1) + 9S(k - 2) = 0\text{,}\) \(S(0) = 3\text{,}\) \(S(1) = 11\)

Answer.\(S(k)=2+9^k\)2.

\(S(k) - 9S(k - 1) + 18S(k - 2) = 0\text{,}\) \(S(0) = 0\text{,}\) \(S(1) = 3\)
3.

\(S(k) - 0.25S(k - 1) = 0\text{,}\) \(S(0) = 6\)

Answer.\(S(k)=6(1/4)^k\)4.

\(S(k) - 20S(k - 1) + 100S(k - 2) = 0\text{,}\) \(S(0) = 2\text{,}\) \(S(1) = 50\)
5.
\(S(k) - 2S(k - 1) + S(k - 2) = 2 \textrm{,  }S(0) = 25,\textrm{  }S(1) = 16\)
Answer.\(S(k)=k^2-10k+25\)6.

\(S(k) - S(k - 1) - 6S(k - 2) = -30\text{,}\) \(S(0) = 7\text{,}\) \(S(1) = 6\)
7.
\(S(k) - 5S (k - 1) = 5^k,\textrm{  }S(0) = 3\)
Answer.\(S(k)=(3+k)5^k\)8.
\(S(k) - 5S(k - 1) + 6S(k - 2) = 2,\textrm{  }S(0) = -1,\textrm{  }S(1) = 0\)9.
\(S(k) - 4S(k - 1) + 4S(k - 2) = 3k + 2^k \textrm{,  }S(0) = 1, S(1) = 1\)
Answer.\(S(k)=(12+3k)+\left(k^2+7k-22\right)2^{k-1}\)10.

\(S(k) = r S(k - 1) + a\text{,}\) \(S(0) = 0\text{,}\) \(r, a \geq  0, r \neq  1\)
11.

\(S(k) - 4S(k - 1) - 11S(k- 2)+ 30S(k - 3) = 0\text{,}\) \(S(0) = 0\text{,}\)\(S(1) = -35,\textrm{  }S(2) = -85\)

Answer.\(S(k)=4(-3)^k+2^k-5^{k+1}\)

> **Exercise 12 . —**

> Find a closed form expression for \(P(k)\) in [Exercise 8.2.3.3 [UNRESOLVED_INTERNAL_LINK]](s-Sequences.html#ex-lines-regions) of Section 8.2.

> **Exercise 13 . —**

> Find a closed form expression for the terms of the Fibonacci sequence (see [Example 8.1.8 [UNRESOLVED_INTERNAL_LINK]](s-faces-of-recursion.html#ex-fibonacci-sequence)).
> The sequence \(C\) was defined by \(C_r\) = the number of strings of zeros and ones with length \(r\) having no consecutive zeros ([Example 8.2.2 [UNRESOLVED_INTERNAL_LINK]](s-Sequences.html#ex-three-sequences)(c)). Its recurrence relation is the same as that of the Fibonacci sequence. Determine a closed form expression for \(C_r\text{,}\) \(r \geq  1\text{.}\)

> **Exercise 14 . —**

> If \(S(n)=\sum_{j=1}^n g(j)\text{,}\)\(n\geq 1\text{,}\) then \(S\) can be described with the recurrence relation \(S(n) = S(n-1) + g(n)\text{.}\) For each of the following sequences that are defined using a summation, find a closed form expression:

> \(S(n) =\sum_{j=1}^n j\text{,}\) \(n\geq 1\)
> 
> 
> \(Q(n) = \sum_{j=1}^n j^2\text{,}\) \(n\geq 1\)
> 
> 
> \(P(n) =\)\(\sum_{j=1}^n \left(\frac{1}{2}\right)^j\text{,}\) \(n\geq 1\)
> 
> 
> \(T(n)= \sum_{j=1}^n j^3\text{,}\) \(n\geq 1\)

> **Exercise 15 . —**

> Let \(D(n)\) be the number of ways that the set \(\{1, 2, . . . , n\}\text{,}\) \(n \geq  1\text{,}\) can be partitioned into two nonempty subsets.

> Find a recurrence relation for \(D\text{.}\) (Hint: It will be a first-order linear relation.)
> Solve the recurrence relation.

> **Exercise 16 . —**

> If you were to deposit a certain amount of money at the end of each year for a number of years, this sequence of payments would be called an annuity (see [Example 8.3.21 [UNRESOLVED_INTERNAL_LINK]](s-recurrence-relations.html#ex-a-novel-annuity)).
> 
> Find a closed form expression for the balance or value of an annuity that consists of payments of \(q\) dollars at a rate of interest of \(i\text{.}\) Note that for a normal annuity, the first payment is made after one year. However, assume that there is an initial balance \(b_0\text{.}\)  This will be convenient to apply our solution to the case of a loan.
> With an interest rate of 5.5 percent, how much would you need to deposit into an annuity to have a value of one million dollars after 18 years?
> The payment of a loan is a form of annuity in which the initial value is some negative amount (the amount of the loan) and the annuity ends when the value is raised to zero. How much could you borrow if you can afford to pay $5,000 per year for 25 years at 11 percent interest?

> **Exercise 17 . —**

> Suppose that \(C\) is a small positive number. Consider the recurrence relation \(B(k) - 2B(k - 1) + \left(1 - C ^2\right)B(k - 2)
> = C^2\text{,}\) with initial conditions \(B(0) = 1\) and \(B(1) = 1\text{.}\) If \(C\) is small enough, we might consider approximating the relation by replacing \(1 - C^2\) with 1 and \(C^2\) with 0. Solve the original relation and its approximation. Let \(B_a\) a be the solution of the approximation. Compare closed form expressions for \(B(k)\) and \(B_a(k)\text{.}\) Their forms are very different because the characteristic roots of the original relation were close together and the approximation resulted in one double characteristic root. If characteristic roots of a relation are relatively far apart, this problem will not occur. For example, compare the general solutions of \(S(k) + 1.001S(k - 1) - 2.004002 S(k - 2) = 0.0001\) and \(S_a(k) + S_a(k - 1) - 2S_a(k - 2) = 0\text{.}\)
