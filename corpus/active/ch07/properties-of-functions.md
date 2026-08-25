---
source_relative_path: "DM TXT/7-Functions_and_Probability/ads Properties of Functions.html"
source_sha256: "410acc8a947c86c2a101bcc900f1b17abe16ff6e484e73588e27a9e9c9782680"
scope_class: active_candidate
displayed_section_or_chapter: "Section 7.2 Properties of Functions"
content_gap: true
missing_assets:
  - "external/images/fig-sol-7-2-9.png"
---

# Section 7.2 Properties of Functions

# Subsection 7.2.1 Properties

Consider the following functions:

Let \(A = \{1, 2, 3, 4\}\) and \(B = \{a, b, c, d\}\text{,}\) and define \(f:A \rightarrow  B\) by

\begin{equation*}
f(1) = a, f(2) = b, f(3) = c \textrm{ and } f(4) = d
\end{equation*}

Let \(A = \{1, 2, 3, 4\}\) and \(B = \{a, b, c, d\}\text{,}\) and define \(g:A \rightarrow  B\) by

\begin{equation*}
g(1) = a , g(2) = b, g(3) = a \textrm{ and } g(4) = b.
\end{equation*}

The first function, \(f\text{,}\) gives us more information about the set \(B\) than the second function, \(g\text{.}\) Since \(A\) clearly has four elements, \(f\) tells us that \(B\) contains at least four elements since each element of \(A\) is mapped onto a different element of \(B\text{.}\) The properties that \(f\) has, and \(g\) does not have, are the most basic properties that we look for in a function. The following definitions summarize the basic vocabulary for function properties.

> **Definition 7.2.1 — Injective Function, Injection.**

> A function \(f: A \rightarrow B\) is injective if
> 
> \begin{equation*}
> \forall a, b\in  A, a\neq b \Rightarrow  f(a) \neq  f(b)
> \end{equation*}
> 
> An injective function is called an injection, or a one-to-one function.

Notice that the condition for an injective function is logically equivalent to

\begin{equation*}
f(a) = f(b) \Rightarrow   a = b\text{.}
\end{equation*}

for all \(a, b\in  A\text{.}\)  This is often a more convenient condition to prove than what is given in the definition.

> **Definition 7.2.2 — Surjective Function, Surjection.**

> A function \(f: A \rightarrow B\) is surjective if its range, \(f(A)\text{,}\) is equal to its codomain, \(B\text{.}\)  A surjective function is called a surjection, or an onto function.

Notice that the condition for a surjective function is equivalent to

\begin{equation*}
\textrm{For all } b \in  B\textrm{, there exists } a\in A \textrm{ such that } f(a)=b\text{.}
\end{equation*}

> **Definition 7.2.3 — Bijective Function, Bijection.**

> A function \(f: A \rightarrow B\) is bijective if it is both injective and surjective. Bijective functions are also called one-to-one, onto functions.

The function \(f\) that we opened this section with is bijective. The function \(g\) is neither injective nor surjective.

> **Example 7.2.4 — Injective but not surjective function.**

> Let \(A = \{1, 2, 3\}\) and \(B = \{a, b, c, d\}\text{,}\) and define \(f:A \rightarrow  B\) by \(f(1) = b\text{,}\) \(f(2) = c\text{,}\) and \(f(3)
> = a\text{.}\) Then \(f \) is injective but not surjective.

> **Example 7.2.5 — Characteristic Functions.**

> The characteristic function, \(\chi _S\text{,}\) in [Exercise 7.1.5.4 [UNRESOLVED_INTERNAL_LINK]](s-function-def-notation.html#exercise-characteristic-function)  is surjective if \(S\) is a proper subset of \(A\text{,}\) but never injective if \(\lvert A \rvert \gt 2\text{.}\)

# Subsection 7.2.2 Counting

> **Example 7.2.6 — Seating Students.**

> Let \(A\) be the set of students who are sitting in a classroom,  let \(B\) be the set of seats in the classroom, and let \(s\) be the function which maps each student into the chair he or she is sitting in. When is \(s\) one to one? When is it onto? Under normal circumstances, \(s\)  would always be injective since no two different students would be in the same seat.  In order for \(s\) to be surjective, we need all seats to be used, so \(s\)  is a surjection if the classroom is filled to capacity.

Functions can also be used for counting the elements in large finite sets or in infinite sets. Let’s say we wished to count the occupants in an auditorium containing 1,500 seats. If each seat is occupied, the answer is obvious, 1,500 people. What we have done is to set up a one-to-one correspondence, or bijection, from seats to people. We formalize in a definition.

> **Definition 7.2.7 — Cardinality.**

> Two sets are said to have the same cardinality if there exists a bijection between them. If a set has the same cardinality as the set \(\{1,2,3,\ldots , n\}\text{,}\) then we say its cardinality is \(n\text{.}\)

The function \(f\) that opened this section serves to show that the two sets \(A=\{1, 2, 3, 4\}\) and \(B=\{a, b, c, d\}\) have the same cardinality. Notice in applying the definition of cardinality, we don’t actually appear to count either set, we just match up the elements. However, matching the letters in \(B\) with the numbers 1, 2, 3, and 4 is precisely how we count the letters.

> **Definition 7.2.8 — Countable Set.**

> If a set is finite or has the same cardinality as the set of positive integers, it is called a countable set.

> **Example 7.2.9 — Counting the Alphabet.**

> The alphabet \(\{A, B, C, . . . , Z\}\) has cardinality 26 through the following bijection into the set \(\{1,2,3,\ldots ,26\}\text{.}\)
> 
> 
> \begin{equation*}
> \begin{array}{ccccc}
> A & B & C & \cdots  & Z \\
> \downarrow  & \downarrow  & \downarrow  & \cdots  & \downarrow  \\
> 1 & 2 & 3 & \cdots  & 26 \\
> \end{array}\text{.}
> \end{equation*}

> **Example 7.2.10 — As many evens as all positive integers.**

> Recall that \(2\mathbb{P}= \{b\in \mathbb{P} \mid b= 2k \textrm{ for some } k \in \mathbb{P} \}\text{.}\)  Paradoxically, \(2\mathbb{P}\)  has the same cardinality as the set \(\mathbb{P}\) of positive integers. To prove this, we must find a bijection from \(\mathbb{P}\) to \(2\mathbb{P}\text{.}\)  Such a function isn’t unique, but this one is the simplest: \(f:\mathbb{P} \rightarrow  2\mathbb{P}\) where \(f(m) = 2m\text{.}\)  Two statements must be proven to justify our claim that \(f\) is a bijection:

> \(f\) is one-to-one.
> 
> Proof: Let \(a, b \in  \mathbb{P}\) and assume that \(f(a) = f(b)\text{.}\) We must prove that \(a = b\text{.}\)
> 
> 
> \begin{equation*}
> f(a) = f(b) \Longrightarrow  2a = 2b \Longrightarrow  a = b.
> \end{equation*}
> 
> 
> 
> 
> 
> \(f \) is onto.
> Proof:  Let \(b \in  2\mathbb{P}\text{.}\) We want to show that there exists an element \(a \in  \mathbb{P}\) such that \(f(a) = b\text{.}\) If \(b \in 
> 2\mathbb{P}\text{,}\) \(b = 2k\) for some \(k \in  \mathbb{P}\) by the definition of \(2\mathbb{P}\text{.}\) So we have \(f(k) = 2k = b\text{.}\) Hence, each element of 2\(\mathbb{P}\) is the image of some element of \(\mathbb{P}\text{.}\)

Another way to look at any function with \(\mathbb{P}\) as its domain is creating a list of the form \(f(1),f(2), f(3), \ldots\text{.}\)  In the previous example, the list  is \(2, 4, 6, \ldots\text{.}\)  This infinite list clearly has no duplicate entries and every even positive integer appears in the list eventually.

A function \(f:\mathbb{P}\to A\) is a bijection if the infinite list \(f(1), f(2), f(3), \ldots\) contains no duplicates, and every element of \(A\) appears once in the list.  In this case, we say the \(A\) is countably infinite, or simply countable.

> **Example 7.2.11 — A First Paradox of Infinity.**

> When studying infinity, paradoxes abound.  One of the first instances of this is when we observe that the set of even positive integers, in spite of the fact that they make up only half of the positive integers, has the same cardinality as the whole set of positive integers.  This follows from our definition of cardinality  with the function \(f(k)=2k\text{,}\) which is a bijection from the positive integers to the even positive integers. We can make a similar observation that the seemingly smaller set of powers of \(10\text{,}\) \(\{10^0,10^1,10^2,10^3,\dots\}\text{,}\) also has the same cardinality as the positive integer. Here, the function \(g(k)=10^k\) serves as our justification.

> Going in the opposite direction, there are seemingly larger sets than the positive integer that are countably infinite.  One such example is the Cartesian product of the positive integers with itself, \(\mathbb{P}\times \mathbb{P}\text{.}\) A function that justifies this claim doesn’t have such a neat formula, but it would start like this:

> ![Table 7.2.12 . \(f(1)=(1,1)\) \(f(2)=(1,2)\) \(f(3)=(2,1)\) \(f(4)=(1,3)\) \(f(5)=(2,2)\) \(f(6)=(3,1)\) \(f(7)=(1,4)\) \(f(8)=(2,3)\) \(f(9)=(3,2)\) \(f(10)=(4,1)\)]()

> See the pattern?  If it continues, every positive integer will map to a different pair and every pair of positive integer will be in the range of \(f\text{.}\)

Readers who have studied real analysis should recall that the set of rational numbers is a countable set, while the set of real numbers is not a countable set. See the exercises at the end of this section for an another example of such a set.

We close this section with a theorem called the Pigeonhole Principle, which has numerous applications even though it is an obvious, common-sense statement. Never underestimate the importance of simple ideas. The Pigeonhole Principle states that if there are more pigeons than pigeonholes, then two or more pigeons must share the same pigeonhole. A more rigorous mathematical statement of the principle follows.

> **Theorem 7.2.13 — The Pigeonhole Principle.**

> Let \(f\) be a function from a finite set \(X\) into a finite set \(Y\text{.}\) If \(n\geq 1\) and \(\lvert X\rvert > n\lvert Y\rvert\text{,}\) then there exists an element of \(Y\) that is the image under \(f\) of at least \(n + 1\) elements of X.

> **Example 7.2.14 — A duplicate name is assured.**

> Assume that a room contains four students with the first names John, James, and Mary. Prove that two students have the same first name. We can visualize a mapping from the set of students to the set of first names; each student has a first name. The pigeonhole principle applies with \(n = 1\text{,}\) and we can conclude that at least two of the students have the same first name.

> **Exercise 1 . —**

> Determine which of the functions in [Exercise 7.1.5.1 [UNRESOLVED_INTERNAL_LINK]](s-function-def-notation.html#exercise-7-1-1) of Section 7.1 are one- to-one and which are onto.

> **Exercise 2 . —**

> Determine all bijections from \(\{1, 2, 3\}\) into \(\{a, b, c\}\text{.}\)
> 
> Determine all bijections from \(\{1, 2, 3\}\) into \(\{a, b, c, d\}\text{.}\)

> **Exercise 3 . —**

> Which of the following are one-to-one, onto, or both?

> \(f_1:\mathbb{R} \rightarrow \mathbb{R}\) defined by \(f_1(x) = x^3 - x\text{.}\)
> 
> 
> \(f_2 :\mathbb{Z} \rightarrow  \mathbb{Z}\) defined by \(f_2(x)= -x + 2\text{.}\)
> 
> 
> \(f_3:\mathbb{N} \times \mathbb{N}\to \mathbb{N}\) defined by \(f_3(j, k) =2^j3^k\text{.}\)
> 
> 
> \(f_4 :\mathbb{P} \rightarrow  \mathbb{P}\) defined by \(f_4(n)=\lceil n/2\rceil\text{,}\) where \(\lceil x\rceil\) is the ceiling of \(x\text{,}\) the smallest integer greater than or equal to \(x\text{.}\)
> 
> 
> \(f_5 :\mathbb{N} \rightarrow  \mathbb{N}\) defined by \(f_5(n)=n^2+n\text{.}\)
> 
> 
> \(f_6:\mathbb{N} \rightarrow  \mathbb{N} \times  \mathbb{N}\) defined by \(f_6(n)= (2n, 2n+1)\text{.}\)

> **Exercise 4 . —**

> Which of the following are injections, surjections, or bijections on \(\mathbb{R}\text{,}\) the set of real numbers?

> \(f(x) = -2x\text{.}\)
> \(g(x) = x^2- 1\text{.}\)
> \(\displaystyle h(x)=\left\{ \begin{array}{cc}
> x & x < 0 \\
> x^2 & x\geq 0 \\
> \end{array} \right.\)
> \(\displaystyle q(x)=2^x\)
> \(\displaystyle r(x) =x^3\)
> \(\displaystyle s(x) = x^3-x\)

> **Exercise 5 . —**

> Suppose that \(m\) pairs of socks are mixed up in your sock drawer. Use the Pigeonhole Principle to explain why, if you pick \(m + 1\) socks at random, at least two will make up a matching pair.

> **Exercise 6 . —**

> Given five points on the unit square, \(\{(x,y) \mid 0 \leq x, y \leq 1 \}\text{,}\) prove that there are two of the points a distance of no more than \(\frac{\sqrt{2}}{2}\) from one another.

> **Exercise 7 . —**

> Let \(A =\text{  }\{1, 2, 3, 4, 5\}\text{.}\) Find functions, if they exist that have the properties specified below.

> A function that is one-to-one and onto.
> A function that is neither one-to-one nor onto.
> A function that is one-to-one but not onto.
> A function that is onto but not one-to-one.

> **Exercise 8 . —**

> Define functions, if they exist, on the positive integers, \(\mathbb{P}\text{,}\) with the same properties as in Exercise 7 (if possible).
> Let \(A\) and \(B\) be finite sets where \(|A|=|B|\text{.}\) Is it possible to define a function \(f:A \rightarrow  B\) that is one-to-one but not onto? Is it possible to find a function  \(g:A \rightarrow  B\) that is onto but not one-to-one?

> **Exercise 9 . —**

> Prove that the set of natural numbers is countable.
> Prove that the set of integers is countable.
> Prove that the set of rational numbers is countable.

> ![MISSING FIGURE: source figure](GAP:external/images/fig-sol-7-2-9.png)

> **Exercise 10 . —**

> Prove that the set of finite strings of 0’s and 1’s is countable.
> Prove that the set of odd integers is countable.
> Prove that the set  \(\mathbb{N}\times  \mathbb{N}\) is countable.
> Prove that the set  \(\mathbb{N}\times  \mathbb{N}\times  \mathbb{N}\) is countable.

> **Exercise 11 . —**

> Use the Pigeonhole Principle to prove that an injection cannot exist between a finite set \(A\) and a finite set \(B\) if the cardinality of \(A\) is greater than the cardinality of \(B\text{.}\)

> **Exercise 12 . —**

> The important properties of relations are not generally of interest for functions. Most functions are not reflexive, symmetric, antisymmetric, or transitive. Can you give examples of functions that do have these properties?

> **Exercise 13 . —**

> Prove that the set of all infinite sequences of 0’s and 1’s is not a countable set.

> **Exercise 14 . —**

> Prove that the set of all functions on the integers is an uncountable set.
