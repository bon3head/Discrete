---
source_relative_path: "DM TXT/8-Recursion_and_Recurrence_Relations/ads The Many Faces of Recursion.html"
source_sha256: "d7dc2213bf641ce23d14c74b0adbf1a592d4a4a5c6b040f1b481727ecc50ed86"
scope_class: active_candidate
displayed_section_or_chapter: "Section 8.1 The Many Faces of Recursion"
content_gap: true
missing_assets:
  - "external/images/fig-binsearch.png"
---

# Section 8.1 The Many Faces of Recursion

Consider the following definitions, all of which should be somewhat familiar to you. When reading them, concentrate on how they are similar.

# Subsection 8.1.1 Binomial Coefficients

Here is a recursive definition of binomial coefficients, which we introduced in Chapter 2.

> **Definition 8.1.1 — Binomial Coefficient - Recursion Definition.**

> Assume \(n\geq 0\) and \(n \geq  k \geq  0\text{.}\) We define \(\binom{n}{k} \) by

> \(\displaystyle \binom{n}{0}  = 1\)
> 
> \(\binom{n}{n} =1\) and
> 
> \(\binom{n}{k}  = \binom{n-1}{k}+\binom{n-1}{k-1}\) if \(n > k > 0\)

Here is how we can apply the recursive definition to compute \(\binom{5}{2} \text{.}\)


\begin{equation*}
\begin{split}
\binom{5}{2}  &=\binom{4}{2} +\binom{4}{1} \\
&=(\binom{3}{2} +\binom{3}{1} )+(\binom{3}{1} +\binom{3}{0} )\\
&=\binom{3}{2}  +2 \binom{3}{1}  + 1\\
&=(\binom{2}{2} +\binom{2}{1} )+ 2(\binom{2}{1} +\binom{2}{0} )+1\\
&=(1+\binom{2}{1} )+ 2( \binom{2}{1}   + 1) + 1\\
&=3 \binom{2}{1}  + 4\\
&=3(\binom{1}{1}  + \binom{1}{0} ) + 4\\
&=3(1+1)+4 = 10
\end{split}
\end{equation*}

# Subsection 8.1.2 Polynomials and Their Evaluation

> **Definition 8.1.3 — Polynomial Expression in \(x\) over \(S\) (Non-Recursive).**

> Let \(n\) be an integer, \(n\geq 0\text{.}\) An \(n^{\text{th}}\) degree polynomial in \(x\) is an expression of the form \(a_nx^n+ a_{n-1}x^{n-1}+ \cdots  + a_1x+a_0\text{,}\) where \(a_n, a_{n-1},\ldots ,a_1,a_0\) are elements of some designated set of numbers, \(S\text{,}\) called the set of coefficients and \(a_n\neq 0\text{.}\)

We refer to \(x\) as a variable here, although the more precise term for \(x\) is an *indeterminate*. There is a distinction between the terms indeterminate and variable, but that distinction will not come into play in our discussions.

Zeroth degree polynomials are called constant polynomials and are simply elements of the set of coefficients.

This definition is often introduced in algebra courses to describe expressions such as \(f(n) = 4n^3 + 2n^2 - 8n + 9\text{,}\) a third-degree, or cubic, polynomial in \(n\text{.}\) This definition has a drawback when the variable is given a value and the expression must be evaluated. For example, suppose that \(n = 7\text{.}\) Your first impulse is likely to do this:

\begin{equation*}
\begin{split}
f(7) &= 4\cdot 7^3 + 2\cdot 7^2 - 8\cdot 7 + 9\\
&=4\cdot 343 +2\cdot 49 -8\cdot 7+9 \\
&= 1423
\end{split}
\end{equation*}

A count of the number of operations performed shows that five multiplications and three additions/subtractions were performed. The first two multiplications compute \(7^2\) and \(7^3\text{,}\) and the last three multiply the powers of 7 times the coefficients. This gives you the four terms; and adding/subtracting a list of \(k\) numbers requires \(k-1\) addition/subtractions. The following definition of a polynomial expression suggests another more efficient method of evaluation.

> **Definition 8.1.4 — Polynomial Expression in \(x\) over \(S\) (Recursive).**

> Let \(S\) be a set of coefficients and \(x\) a variable.

> A zeroth degree polynomial expression in \(x\) over \(S\) is a nonzero element of \(S\text{.}\)
> 
> For \(n\geq 1\text{,}\) an \(n^{th}\) degree polynomial expression in \(x\) over \(S\) is an expression of the form \(p(x)x + a\) where \(p(x)\) is an \((n-1)^{st}\) degree polynomial expression in \(x\) and \(a\in  S\text{.}\)

We can easily verify that \(f(n) = 4n^3 + 2n^2 - 8n + 9\) is a third-degree polynomial expression in  \(n\) over \(\mathbb{Z}\) based on this definition:

\begin{equation*}
f(n)= 4n^3 + 2n^2 - 8n + 9 = ((4n+2)n-8)n+9
\end{equation*}

Notice that 4 is a zeroth degree polynomial since it is an integer. Therefore \(4n + 2\) is a first-degree polynomial; therefore, \((4n + 2) n - 8\) is a second-degree polynomial in \(n\) over \(\mathbb{Z}\text{;}\) therefore, \(f(n)\) is a third-degree polynomial in \(n\) over \(\mathbb{Z}\text{.}\) The final expression for \(f(n)\) is called its telescoping form. If we use it to calculate \(f(7)\text{,}\) we need only three multiplications and three additions/subtractions. This is called Horner’s method for evaluating a polynomial expression.

> **Example 8.1.5 — More Telescoping Polynomials.**

> The telescoping form of \(p(x) = 5x^4 + 12x^3 -6x^2 + x + 6\) is \((((5x + 12) x - 6) x + 1) x + 6\text{.}\) Using Horner’s method, computing the value of \(p(c)\) requires four multiplications and four additions/subtractions for any real number \(c\text{.}\)
> 
> 
> \(g(x) = -x^5 + 3x^4 + 2x^2 + x\) has the telescoping form \(((((- x + 3) x ) x + 2) x + 1) x\text{.}\)

Many computer languages represent polynomials as lists of coefficients, usually starting with the constant term. For example, \(g(x) = -x^5 +
3x^4 +\text{  }2x^2 + x\)  would be represented with the list \(\{0,1,2,0,3,-1\}\text{.}\) In both Mathematica and Sage, polynomial expressions can be entered and manipulated, so the list representation is only internal. Some programming languages require users to program polynomial operations with lists. We will leave these programming issues to another source.

# Subsection 8.1.3 Recursive Searching - The Binary Search

Next, we consider a recursive algorithm for a binary search within a sorted list of items.  Suppose  \(r=\{r(1),r(2), \ldots  , r(n)\}\) represent a list of \(n\) items sorted by a numeric key in descending order. The \(j^{th}\) item is denoted \(r(j)\) and its key value by \(r(j).\texttt{key}\text{.}\) For example, each item might contain data on the buildings in a city and the key value might be the height of the building. Then \(r(1)\) would be the item for the tallest building and  \(r(1).\texttt{key}\) would be its height. The algorithm \(\texttt{BinarySearch}(j, k)\) can be applied to search for an item in \(r\) with key value \(C\text{.}\) This would be accomplished by the execution of \(\texttt{BinarySearch}(1, n)\text{.}\) When the algorithm is completed, the variable \(\texttt{Found}\) will have a value of \(\texttt{true}\) if an item with the desired key value was found, and the value of \(\textrm{location}\) will be the index of an item whose key is \(C\text{.}\) If \(\texttt{Found}\) keeps the value \(\texttt{false}\text{,}\) no such item exists in the list. The general idea behind the algorithm is illustrated in [Figure 8.1.6 [UNRESOLVED_INTERNAL_LINK]](s-faces-of-recursion.html#fig-binsearch)

![MISSING FIGURE: described in detail following the image](GAP:external/images/fig-binsearch.png)

In the following implementation of the Binary Search in SageMath, we search within a sorted list of integers. Therefore, the items themselves are the keys.

```sage

```

# Subsection 8.1.4 Recursively Defined Sequences

For the next two examples, consider a sequence of numbers to be a list of numbers consisting of a zeroth number, first number, second number, ... . If a sequence is given the name \(S\text{,}\) the \(k^{th}\) number of \(S\) is usually written \(S_k\)  or \(S(k)\text{.}\)

> **Example 8.1.7 — Geometric Growth Sequence.**

> Define the sequence of numbers \(B\) by
> 
> \begin{equation*}
> B_0 = 100\textrm{ and }
> \end{equation*}
> 
> 
> \begin{equation*}
> B_k = 1.08 B_{k-1} \textrm{ for } k\geq 1 \text{.}
> \end{equation*}

> These rules stipulate that each number in the list is 1.08 times the previous number, with the starting number equal to 100. For example
> 
> \begin{equation*}
> \begin{split}
> B_3 &= 1.08 B_2 \\
> &=1.08\left(1.08B_1\right)\\
> &= 1.08\left(1.08\left(1.08 B_0\right)\right)\\
> & = 1.08(1.08(1.08\cdot 100))\\
> &= 1.08^3 \cdot 100 = 125.971
> \end{split}
> \end{equation*}

> **Example 8.1.8 — The Fibonacci Sequence.**

> The Fibonacci sequence is the sequence \(F\) defined by
> 
> \begin{equation*}
> F_0= 1 \textrm{, } F_1= 1\textrm{ and}
> \end{equation*}
> 
> 
> \begin{equation*}
> F_k = F_{k-2} + F_{k-1} \textrm{ for }k\geq 2
> \end{equation*}

# Subsection 8.1.5 Recursion

All of the previous examples were presented recursively. That is, every “object” is described in one of two forms. One form is by a simple definition, which is usually called the basis for the recursion. The second form is by a recursive description in which objects are described in terms of themselves, with the following qualification. What is essential for a proper use of recursion is that the objects can be expressed in terms of simpler objects, where “simpler” means closer to the basis of the recursion. To avoid what might be considered a circular definition, the basis must be reached after a finite number of applications of the recursion.

To determine, for example, the fourth item in the Fibonacci sequence we repeatedly apply the recursive rule for \(F\) until we are left with an expression involving \(F_0\) and \(F_1\text{:}\)


\begin{equation*}
\begin{split}
F_4 &= F_2+F_3\\	
&=\left(F_0+F_1\right)+\left(F_1+F_2\right)\\
&=\left(F_0+F_1\right)+\left(F_1+\left(F_0+F_1\right)\right)\\
&=(1+1)+(1+(1+1))\\
&=5
\end{split}
\end{equation*}

# Subsection 8.1.6 Iteration

On the other hand, we could compute a term in the Fibonacci sequence such as \(F_5\) by starting with the basis terms and working forward as follows:

![Table 8.1.9 . \(F_2= F_0+ F_1 =1 + 1 =2\) \(F_3= F_1+ F_2=1+ 2=3\) \(F_4= F_2+F_3=2+3=5\) \(F_5=F_3+F_4= 3+5=8\)]()

This is called an iterative computation of the Fibonacci sequence. Here we start with the basis and work our way forward to a less simple number, such as 5. Try to compute \(F_5\) using the recursive definition for \(F\) as we did for \(F_4\text{.}\) It will take much more time than it would have taken to do the computations above. Iterative computations usually tend to be faster than computations that apply recursion. Therefore, one useful skill is being able to convert a recursive formula into a nonrecursive formula, such as one that requires only iteration or a faster method, if possible.

An iterative formula for \(\binom{n}{k} \) is also much more efficient than an application of the recursive definition. The recursive definition is not without its merits, however. First, the recursive equation is often useful in manipulating algebraic expressions involving binomial coefficients. Second, it gives us an insight into the combinatoric interpretation of \(\binom{n}{k}\text{.}\) In choosing \(k\) elements from \(\{1, 2,
. . . , n\}\text{,}\) there are \(\binom{n-1}{k}\) ways of choosing all \(k\) from \(\{1,2, . . . ,n - 1\}\text{,}\) and there are \(\binom{n-1}{k-1}\) ways of choosing the \(k\) elements if \(n\) is to be selected and the remaining \(k - 1\) elements come from \(\{1, 2, . . . , n - 1\}\text{.}\) Note how we used the Law of Addition from Chapter 2 in our reasoning.

*BinarySearch Revisited.* In the binary search algorithm, the place where recursion is used is easy to pick out. When an item is examined and the key is not the one you want, the search is cut down to a sublist of no more than half the number of items that you were searching in before. Obviously, this is a simpler search. The basis is hidden in the algorithm. The two cases that complete the search can be thought of as the basis. Either you find an item that you want, or the sublist that you have been left to search in is empty, when \(j > k\text{.}\)

BinarySearch can be translated without much difficulty into any language that allows recursive calls to its subprograms. The advantage to such a program is that its coding would be much shorter than a nonrecursive program that does a binary search. However, in most cases the recursive version will be slower and require more memory at execution time.

# Subsection 8.1.7 Induction and Recursion

The definition of the positive integers in terms of Peano’s Postulates is a recursive definition. The basis element is the number 1 and the recursion is that if \(n\) is a positive integer, then so is its successor. In this case, \(n\) is the simple object and the recursion is of a forward type. Of course, the validity of an induction proof is based on our acceptance of this definition. Therefore, the appearance of induction proofs when recursion is used is no coincidence.

> **Example 8.1.10 — Proof of a formula for \(B\) .**

> A formula for the sequence \(B\) in [Example 8.1.7 [UNRESOLVED_INTERNAL_LINK]](s-faces-of-recursion.html#ex-geometric-growth) is \(B = 100(1.08)^k\) for \(k\geq 0\text{.}\) A proof by induction follow.

> If \(k= 0\text{,}\) then \(B = 100(1.08)^0 = 100\text{,}\) as defined. Now assume that for some \(k\geq 1\text{,}\) the formula for \(B_k\) is true.
> 
> \begin{equation*}
> \begin{split}
> B_{k+1} &= 1.08B_k \textrm{  by the recursive definition}\\
> &=1.08\left(100 (1.08)^k\right) \textrm{  by the induction hypothesis}\\ 
> &= 100 (1.08)^{k+1}
> \end{split}
> \end{equation*}
> 
> hence the formula is true for \(k+1\)

> The formula that we have just proven for \(B\) is called a closed form expression. It involves no recursion or summation signs.

> **Definition 8.1.11 — Closed Form Expression.**

> Let \(E = E\left(x_1, x_2, \ldots ,x_n\right)\) be an algebraic expression involving variables \(x_1, x_2, \ldots ,x_n\) which are allowed to take on values from some predetermined set. \(E\) is a closed form expression if there exists a number \(T\) such that the evaluation of \(E\) with any allowed values of the variables will take no more than \(T\) operations (alternatively, \(T\) time units).

> **Example 8.1.12 — Reducing a summation to closed form.**

> The sum \(E(n)=\sum_{k=1}^n k\) is not a closed form expression because the number of additions needed to evaluate \(E(n)\) grows indefinitely with \(n\text{.}\) A closed form expression that computes the value of \(E(n)\) is \(\frac{n(n+1)}{2}\text{,}\) which only requires \(T=3\) operations.

# Subsection 8.1.8 Recursion in Probability

Recursion can frequently be used to simplify computations relating to random variables. We illustrate this with an example.

> **Example 8.1.13 — Waiting for a Six.**

> Consider a simple game in which the outcome involves rolling a standard, fair six-side die until a 6 is rolled. For any positive integer \(k\) isn’t too difficult to compute the probability that exactly \(k\) rolls are needed to see a 6.  Rolls of a die are independent and each roll is a [Binomial Trial [UNRESOLVED_INTERNAL_LINK]](sec-binomial-processes.html#def-binomial-trial).  If we view rolling a 6 as success the probability that we have \(k-1\) failures followed by a success is \(p(k)=\left(\frac{5}{6}\right)^{k-1}\cdot \frac{1}{6}\text{.}\) If we define the random variable \(K\) to be the number rolls need to get a 6, then the expected values of \(K\) is
> 
> \begin{equation*}
> E(K)=\sum_{k=1}^{\infty} k \cdot p(k)= \sum_{k=1}^{\infty} k \cdot \left(\frac{5}{6}\right)^{k-1}\cdot \frac{1}{6}
> \end{equation*}
> 
> This expression for \(E(K)\) can be simplified in several ways, but probably the simplest is to observe that whatever the expected value of \(K\) is, if you roll the die and don’t get a 6 the expected additional rolls to get a 6 is still \(E(K)\text{.}\)  In other words, the die doesn’t remember what it rolls.  We can write this observation in an equation:
> 
> \begin{equation*}
> E(K) = \frac{1}{6} + \frac{5}{6} (1+E(K)).
> \end{equation*}
> 
> The first term of the right side of this equation recognizes that exactly one roll is needed with probability \(\frac{1}{6}\text{.}\)  We can easily solve this equation for our unknown \(E(K)=6\text{.}\)

> **Exercise 1 . —**

> By the recursive definition of binomial coefficients, \(\binom{7}{2}=\binom{6}{2} +\binom{6}{1}\text{.}\) Continue expanding \(\binom{7}{2}\) to express it in terms of quantities defined by the basis. Check your result by applying the factorial definition of \(\binom{n}{k}\text{.}\)

> **Exercise 2 . —**

> Define the sequence \(L\) by \(L_0 = 5\) and for \(k\geq 1\text{,}\) \(L _k = 2L_{k-1}-7\text{.}\)  Determine \(L_4\) and prove by induction that \(L_k=7-2^{k+1}\text{.}\)

> **Exercise 3 . —**

> Let \(p(x) = x^5+ 3x^4 - 15x^3 + x - 10\text{.}\)

> Write \(p(x)\) in telescoping form.
> Use a calculator to compute \(p(3)\) using the original form of \(p(x)\text{.}\)
> 
> Use a calculator to compute \(p(3)\) using the telescoping form of \(p(x)\text{.}\)
> 
> Compare your speed in parts b and c.

> **Exercise 4 . —**

> Suppose that a list of nine items, \((r(l), r(2), . . . , r(9))\text{,}\) is sorted by key in descending order so that \(r(3).\texttt{key} = 12\) and \(r(4).\texttt{key} = 10\text{.}\) List the executions of the BinarySearch algorithms that would be needed to complete BinarySearch(1,9) when:
> 
> The search key is C = 12
> The search key is C = 11

> Assume that distinct items have distinct keys.

> **Exercise 5 . —**

> What is wrong with the following definition of \(f:\mathbb{R}\to \mathbb{R}\text{?}\) \(f(0) = 1\) and \(f(x) = f(x/2)/2\) if \(x\neq 0\text{.}\)

> **Exercise 6 . —**

> Prove the two definitions of binomials coefficients, [Definition 2.4.3 [UNRESOLVED_INTERNAL_LINK]](s-combinations-and-the-binomial-theorem.html#binomial-coefficient) and [Definition 8.1.1 [UNRESOLVED_INTERNAL_LINK]](s-faces-of-recursion.html#def-binomial-coefficient-recursive), are equivalent.

> **Exercise 7 . —**

> Prove by induction that if \(n \geq 0\text{,}\) \(\sum_{k=0}^n \binom{n}{k} = 2^n\)

> **Exercise 8 . —**

> Consider a game for which you pay some entry fee that is to be determined.  The game consists of flipping a fair coin until Tails occurs.  Based on the number of Heads, \(n\text{,}\) that are observed in this process, you are paid \(1.5^n\) dollars. If \(P\) is the payoff you receive in this game, use recursion to determine the expected payoff, \(E(P)\text{.}\)
