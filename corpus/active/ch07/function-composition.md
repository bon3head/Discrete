---
source_relative_path: "DM TXT/7-Functions_and_Probability/ads Function Composition.html"
source_sha256: "6b0d089a23206e0ea86ac4582919ea27187f0c51df2c44ae5c4087d6607a7912"
scope_class: active_candidate
displayed_section_or_chapter: "Section 7.3 Function Composition"
---

# Section 7.3 Function Composition

Now that we have a good understanding of what a function is, our next step is to consider an important operation on functions. Our purpose is not to develop the algebra of functions as completely as we did for the algebras of logic, matrices, and sets, but the reader should be aware of the similarities between the algebra of functions and that of matrices. We first define equality of functions.

# Subsection 7.3.1 Function Equality

> **Definition 7.3.1 — Equality of Functions.**

> Let \(f, g:A \rightarrow  B\text{;}\) that is, let \(f\) and \(g\) both be functions from \(A\) into \(B\text{.}\)  Then \(f\) is equal to \(g\) (denoted \(f=g\)) if and only if \(f(x) = g(x)\) for all \(x \in  A\text{.}\)

Two functions that have different domains cannot be equal. For example,  \(f: \mathbb{Z}\to \mathbb{Z}\) defined by \(f(x)=x^2\) and \(g: \mathbb{R}\to
\mathbb{R}\) defined by \(g(x)=x^2\) are not equal even though the formula that defines them is the same.

On the other hand, it is not uncommon for two functions to be equal even though they are defined differently. For example consider the functions \(h\) and \(k\text{,}\) where \(h: \{-1,0,1,2\}\to \{0,1,2\}\) is defined by \(h(x)=|x|\) and \(k: \{-1,0,1,2\}\to \{0,1,2\}\) is defined by \(k(x) = -\frac{x^3}{3}+x^2+\frac{x}{3}\) appear to be very different functions. However, they are equal because \(h(x)= k(x)\) for \(x = -1, 0, 1, \text{ and } 2\text{.}\)

# Subsection 7.3.2 Function Composition

One of the most important operations on functions is that of composition.

> **Definition 7.3.2 — Composition of Functions.**

> Let \(f:A \rightarrow  B\) and \(g:B \rightarrow  C\text{.}\) Then the composition of \(f\) followed by \(g\text{,}\) written \(g\circ f\text{,}\) is a function from \(A\) into \(C\) defined by \((g \circ f)(x) = g(f(x))\text{,}\) which is read “\(g\) of \(f\) of \(x\text{.}\)”

The reader should note that it is traditional to write the composition of functions from right to left. Thus, in the above definition, the first function performed in computing \(g \circ f\)  is \(f\text{.}\) On the other hand, for relations, the composition \(r s\) is read from left to right, so that the first relation is \(r\text{.}\)

> **Example 7.3.3 — A basic example.**

> Let \(f:\{1, 2, 3\}\rightarrow  \{a, b\}\) be defined by \(f(1) = a\text{,}\) \(f(2) = a\text{,}\) and \(f(3) = b\text{.}\) Let \(g:\{a, b\} \rightarrow  \{5, 6, 7\}\) be defined by \(g(a) = 5\) and \(g(b) = 7\text{.}\) Then \(g\circ f: \{1, 2, 3\}\rightarrow  \{5, 6, 7\}\) is defined by \((g\circ f)(1)= 5\text{,}\) \((g\circ f)(2)= 5,\) and \((g\circ f)(3)= 7\text{.}\) For example, \((g\circ f)(1)= g(f(l)) = g(a) = 5\text{.}\) Note that \(f\circ g\) is not defined. Why?

> Let \(f:\mathbb{R} \rightarrow  \mathbb{R}\) be defined by \(f(x) = x^3\) and let \(g:\mathbb{R} \rightarrow  \mathbb{R}\) be defined by \(g(x)
> = 3x+1\text{.}\) Then, since
> 
> \begin{equation*}
> (g\circ f)(x) = g(f(x)) = g\left(x^3\right) = 3x^3 + 1
> \end{equation*}
> 
> we have \(g\circ f: \mathbb{R} \rightarrow  \mathbb{R}\) is defined by \((g\circ f)(x)= 3x^3 + 1\text{.}\) Here \(f\circ g\) is also defined and \(f\circ
> g:\mathbb{R}\rightarrow \mathbb{R}\) is defined by \((f\circ g)(x)=(3x + 1)^3\) . Moreover, since \(3x ^3+ 1 \neq (3x + 1)^3\) for at least one real number, \(g\circ f \neq  f\circ g\text{.}\)  Therefore, the commutative law is not true for functions under the operation of composition. However, the associative law is true for functions under the operation of composition.

> **Theorem 7.3.4 — Function composition is associative.**

> If \(f:A\rightarrow B\text{,}\) \(g:B\to C\text{,}\) and \(h:C\rightarrow D\text{,}\) then \(h\circ (g\circ f) = (h\circ g)\circ f\text{.}\)

If \(f\) is a function on a set \(A\text{,}\) then the compositions \(f\circ  f\text{,}\) \(f\circ  f\circ  f, \dots \) are valid, and we denote them as \(f^2\) , \(f^3, \dots \text{.}\) Repeated compositions of \(f\) with itself can be defined recursively.  We will discuss this form of definition in detail in [Section 8.1 [UNRESOLVED_INTERNAL_LINK]](s-faces-of-recursion.html).

> **Definition 7.3.5 — Powers of Functions.**

> Let \(f: A\to A\text{.}\)

> \(f^1= f\text{;}\)  that is, \(f^1(a) = f(a)\text{,}\) for \(a \in A\text{.}\)
> 
> For \(n\geq 1\text{,}\) \(f^{n+1}= f\circ f^n\text{;}\)  that is, \(f^{n+1}(a)=f\left( f^n(a)\right)\) for \(a \in A\text{.}\)

Two useful theorems concerning composition are given below. The proofs are left for the exercises.

> **Theorem 7.3.6 — The composition of injections is an injection.**

> If \(f: A \rightarrow  B\) and \(g : B \rightarrow  C\) are injections, then \(g\circ f : A \rightarrow  C\) is an injection.

> **Theorem 7.3.7 — The composition of surjections is a surjection.**

> If \(f : A \rightarrow  B\) and \(g: B \rightarrow C\) are surjections, then \(g\circ f: A \rightarrow  C\) is a surjection.

We would now like to define the concepts of identity and inverse for functions under composition. The motivation and descriptions of the definitions of these terms come from the definitions of the terms in the set of real numbers and for matrices. For real numbers, the numbers 0 and 1 play the unique role that \(x + 0 = 0 + x = x\) and \(x \cdot 1 = 1 \cdot  x = x\) for any real number \(x\text{.}\)  0 and 1 are the identity elements for the reals under the operations of addition and multiplication, respectively. Similarly, the \(n \times  n\) zero matrix \(0\) and the \(n \times
n\) identity matrix \(I\) are such that for any \(n \times  n\) matrix \(A\text{,}\) \(A + 0 = 0 + A=A\) and \(A I = I A = A\text{.}\) Hence, an elegant way of defining the identity function under the operation of composition would be to imitate the above well-known facts.

> **Definition 7.3.8 — Identity Function.**

> For any set \(A\text{,}\) the identity function on \(A\) is a function from \(A\) onto \(A\text{,}\) denoted by \(i\) (or, more specifically, \(i_A\)) such that \(i(a) = a\)  for all \(a\in A\text{.}\)

Based on the definition of \(i\text{,}\) we can show that for all functions \(f:A\to A\text{,}\) \(f\circ i=i\circ f = f\text{.}\)

> **Example 7.3.9 — The identity function on \(\{1,2,3\}\) .**

> If \(A = \{1, 2, 3\}\text{,}\) then the identity function \(i:A \to  A\) is defined by \(i(1) = 1\text{,}\) \(i(2) = 2,\) and \(i(3)= 3\text{.}\)

> **Example 7.3.10 — The identity function on \(\mathbb{R}\) .**

> The identity function on \(\mathbb{R}\) is \(i : \mathbb{R} \rightarrow  \mathbb{R}\) defined by \(i(x) = x\text{.}\)

# Subsection 7.3.3 Inverse Functions

We will introduce the inverse of a function with a special case: the inverse of a function on a set. After you’ve taken the time to understand this concept, you can read about the inverse of a function from one set into another. The reader is encouraged to reread the definition of the inverse of a matrix in Section 5.2 ([Definition 5.2.5 [UNRESOLVED_INTERNAL_LINK]](s-special-matrices.html#def-matrix-inverse)) to see that the following definition of the inverse function is a direct analogue of that definition.

> **Definition 7.3.11 — Inverse of a Function on a Set.**

> Let \(f: A\rightarrow  A\text{.}\) If there exists a function \(g : A \rightarrow  A\) such that \(g\circ f = f\circ g = i\text{,}\) then \(g\) is called the inverse of \(f\) and is denoted by \(f^{-1}\) , read “\(f\) inverse.”

Notice that in the definition we refer to “the inverse” as opposed to “an inverse.”  It can be proven that a function can never have more than one inverse (see exercises).

An alternate description of the inverse of a function, which can be proven from the definition, is as follows:  Let \(f: A \rightarrow  A\) be such that \(f(a) = b\text{.}\) Then when it exists, \(f^{-1}\) is a function from \(A\) to \(A\) such that \(f^{-1}(b)=a\text{.}\) Note that \(f^{-1}\) “undoes” what \(f\) does.

> **Example 7.3.12 — The inverse of a function on \(\{1,2,3\}\) .**

> Let \(A = \{1, 2, 3\}\) and let \(f\) be the function defined on \(A\) such that \(f(1) = 2\text{,}\) \(f(2) = 3\text{,}\) and \(f(3) = 1\text{.}\) Then \(f^{-1} : A \rightarrow  A\) is defined by \(f^{-1}(1) = 3\text{,}\) \(f^{-1}(2) = 1\text{,}\) and \(f^{-1}(3) = 2\text{.}\)

> **Example 7.3.13 — Inverse of a real function.**

> If \(g : \mathbb{R} \rightarrow  \mathbb{R}\) is defined by \(g(x) =x^3\) , then \(g^{-1}\) is the function that undoes what \(g\) does. Since \(g\) cubes real numbers, \(g^{-1}\) must be the “reverse” process, namely, takes cube roots. Therefore, \(g^{-1}
> : \mathbb{R} \rightarrow  \mathbb{R}\) is defined by \(g^{-1}(x)=\sqrt[3]{x}\text{.}\) We should show that \(g^{-1}\circ g = i\) and \(g\circ g^{-1}=i\text{.}\) We will do the first, and the reader is encouraged to do the second.
> 
> \begin{equation*}
> \begin{split}
> \left(g^{-1}\circ g\right)(x) &= g^{-1}(g(x)) \quad \textrm{ Definition of composition}\\
> &= g^{-1}\left(x^3\right)\quad \text{Definition of } g\\	
> &=\sqrt[3]{x^3}\quad\textrm{Definition of } g^{-1}\\
> & = x\quad\text{Definition of cube root}\\
> &= i(x)\quad\text{Definition of the identity function}
> \end{split}
> \end{equation*}
> 
> Therefore, \(g^{-1}\circ g = i\text{.}\) Why?

The definition of the inverse of a function alludes to the fact that not all functions have inverses. How do we determine when the inverse of a function exists?

> **Theorem 7.3.14 — Bijections have inverses.**

> Let \(f: A\rightarrow  A\text{.}\) \(f^{-1}\) exists if and only if f is a bijection; i. e. f is one-to-one and onto.

> **Definition 7.3.15 — Permutation.**

> A bijection of a set \(A\) into itself is called a permutation of \(A\text{.}\)

Next, we will consider the functions for which the domain and codomain are not necessarily equal. How do we define the inverse in this case?

> **Definition 7.3.16 — Inverse of a Function (General Case).**

> Let \(f:A \rightarrow  B\text{,}\) If there exists a function \(g:B \rightarrow  A\) such that \(g \circ f = i_A\) and \(f\circ  g = i_B\) , then \(g\) is called the inverse of \(f\) and is denoted by \(f^{-1}\) , read “\(f\) inverse.”

Note the slightly more complicated condition for the inverse in this case because the domains of \(f\circ  g\) and \(g \circ f\) are different if \(A\) and \(B\) are different. The proof of the following theorem isn’t really very different from the special case where \(A=B\text{.}\)

> **Theorem 7.3.17 — When does a function have an inverse?.**

> Let \(f:A \rightarrow  B\text{.}\) \(f^{-1}\) exists if and only if f is a bijection.

> **Example 7.3.18 — Another inverse.**

> Let \(A =\{1,2, 3\}\) and \(B = \{a, b, c\}\text{.}\) Define \(f:A \rightarrow  B\) by \(f(1) = a\text{,}\) \(f(2) = b\text{,}\) and \(f(3) = c\text{.}\) Then \(g: B \rightarrow  A\) defined by \(g(a) = 1\text{,}\) \(g(b) = 2\text{,}\) and \(g(c) = 3\) is the inverse of \(f\text{.}\)
> 
> 
> \begin{equation*}
> \left.
> \begin{array}{c}
> (g\circ f)(1)= 1 \\
> (g\circ f)(2)=2 \\
> (g\circ f)(3)=3 \\
> \end{array}
> \right\}\Rightarrow \text{  }g\circ f = i_A \textrm{ and } \left.
> \begin{array}{c}
> (f\circ g)(a)=a \\
> (f\circ g)(b)=b \\
> (f\circ g)(c)=c \\
> \end{array}
> \right\}\Rightarrow \text{  }f\circ g = i_B
> \end{equation*}

> **Exercise 1 . —**

> Let \(A = \{1,2, 3, 4, 5\}\text{,}\) \(B = \{a, b, c, d, e,f\}\text{,}\) and \(C = \{+, -\}\text{.}\) Define \(f: A \to  B\) by \(f(k)\) equal to the \(k^{th}\) letter in the alphabet, and define \(g : B \rightarrow  C\) by \(g(\alpha ) = +\) if \(\alpha\) is a vowel and \(g(\alpha ) = -\) if \(\alpha\) is a consonant.

> Find \(g\circ  f\text{.}\)
> 
> Does it make sense to discuss \(f\circ g\text{?}\) If not, why not?
> Does \(f^{-1}\) exist? Why?
> Does \(g^{-1}\) exist? Why?

> **Exercise 2 . —**

> Let \(A = \{1, 2, 3\}\text{.}\) Define\(f:A\rightarrow A\) by \(f(1) = 2\text{,}\) \(f(2) = 1\text{,}\) and \(f(3) = 3\text{.}\) Find \(f^2\text{,}\) \(f^3\text{,}\) \(f^4\) and \(f^{-1}\text{.}\)

> **Exercise 3 . —**

> Let \(A = \{1, 2, 3\}\text{.}\)

> List all permutations of \(A\text{.}\)
> 
> Find the inverse and square of each of the permutations of part a, where the square of a permutation, \(f\text{,}\) is the composition \(f \circ f\text{.}\)
> 
> Show that the composition of any two permutations of \(A\) is a permutation of \(A\text{.}\)
> 
> Prove that if \(A\) is any set where \(\lvert A\rvert= n\text{,}\) then the number of permutations of \(A\) is \(n!\text{.}\)

> **Exercise 4 . —**

> Define \(s\text{,}\) \(u\text{,}\) and \(d\text{,}\) all functions on the integers, by \(s(n) = n^2\) , \(u(n) = n + 1\text{,}\) and \(d(n) = n-1\text{.}\) Determine:

> \(\displaystyle u \circ  s \circ  d\)
> \(\displaystyle s \circ  u\circ  d\)
> \(\displaystyle d \circ  s \circ  u\)

> **Exercise 5 . —**

> Consider the following functions on the set of bit strings of length 4. In these definitions, addition is done modulo 2, so that \(1+1=0\text{.}\)  Which of these functions has an inverse?  For those that have an inverse, what is it?  For those that don’t explain why.

> \(\displaystyle f_1(b_1 b_2 b_3 b_4) = b_2 b_3 b_4 b_1\)
> \(\displaystyle f_2(b_1 b_2 b_3 b_4) = b_4 b_3 b_2 b_1\)
> \(\displaystyle f_3(b_1 b_2 b_3 b_4) = (b_1+b_2)(b_2+b_3)(b_3+b_4)(b_4+b_1)\)
> \(\displaystyle f_4(b_1 b_2 b_3 b_4) = b_1(b_1+b_2)(b_1+b_2+b_3)(b_1+b_2+b_3+b_4)\)

> **Exercise 6 . —**

> Inverse images. If \(f\) is any function from \(A\) into \(B\text{,}\) we can describe the inverse image as a function from \(B\) into \(\mathcal{P}(A)\text{,}\) which is also commonly denoted \(f^{-1}\text{.}\) If \(b \in  B\text{,}\) \(f^{-1}(b) = \{a \in A\mid f(a) = b\}\text{.}\) If \(f\) does have an inverse, the inverse image of \(b\) is \(\left\{f^{-1}(b)\right\}\text{.}\)

> Let \(g : \mathbb{R} \to  \mathbb{R}\) be defined by \(g(x) = x^2\text{.}\) What are \(g^{-1}(4)\text{,}\) \(g^{-1}(0)\) and \(g^{-1}(-1)\text{?}\)
> 
> If \(r: \mathbb{R}\to \mathbb{Z}\text{,}\) where \(r(x) = \lceil x\rceil\text{,}\)  what is \(r^{-1}(1)\text{?}\)

> **Exercise 7 . —**

> Let \(f,\) \(g\text{,}\) and \(h\) all be functions from \(\mathbb{Z}\) into \(\mathbb{Z}\) defined by \(f(n) = n + 5\text{,}\) \(g(n) = n - 2,\) and \(h(n)=n^2\text{.}\) Define:

> \(\displaystyle f\circ g\)
> \(\displaystyle f^3\)
> \(\displaystyle f\circ h\)

> **Exercise 8 . —**

> Define the following functions on the integers by \(f(k) = k + 1\text{,}\) \(g(k) = 2k\text{,}\) and \(h(k)=\lceil k/2\rceil\)

> Which of these functions are one-to-one?
> Which of these functions are onto?
> Express in simplest terms the compositions \(f\circ g\text{,}\) \(g \circ f\text{,}\) \(g \circ  h\text{,}\) \(h \circ  g\text{,}\) and \(h^2\text{.}\)

> **Exercise 9 . —**

> Let \(A\) be a nonempty set. Prove that if \(f \) is a bijection on \(A\) and \(f \circ f=f\text{,}\) then \(f\) is the identity function, \(i\)

> **Exercise 10 . —**

> For the real matrix \(A=\left(
> \begin{array}{cc}
> a & b \\
> c & d 
> \end{array}
> \right)\text{,}\) \(\det(A)= a d-b c\text{.}\)

> Recall that a  bijection from a set to itself is also referred to as a permutation of the set. Let \(\pi\) be a permutation of \(\{a,b,c,d\}\) such that \(a\) becomes \(\pi (a)\text{,}\) \(b\) becomes \(\pi (b)\text{,}\) etc.

> Let \(B=\left(
> \begin{array}{cc}
> \pi(a)& \pi(b)\\
> \pi(c)& \pi(d)\\
> \end{array}
> \right)\text{.}\) How many permutations of \(\pi\) leave the determinant of \(A\) invariant, that is, \(\det  A = \det  B\text{?}\)

> **Exercise 11 . —**

> State and prove a theorem on inverse functions analogous to the one that says that if a matrix has an inverse, that inverse is unique.

> **Exercise 12 . —**

> Let \(f\) and \(g\) be functions whose inverses exist. Prove that \((f\circ g)^{-1}= g^{-1}\circ f^{-1}\text{.}\)

> **Exercise 13 . —**

> Prove [Theorem 7.3.6 [UNRESOLVED_INTERNAL_LINK]](s-function-composition.html#theorem-composition-of-injections) and [Theorem 7.3.7 [UNRESOLVED_INTERNAL_LINK]](s-function-composition.html#theorem-composition-of-surjections).

> **Exercise 14 . —**

> Prove the second half of [Theorem 7.3.14 [UNRESOLVED_INTERNAL_LINK]](s-function-composition.html#theorem-bijections-have-inverses).

> **Exercise 15 . —**

> Prove by induction that if \(n\geq  2\) and \(f_1\text{,}\) \(f_2, \dots, f_n\) are invertible functions on some nonempty set \(A\text{,}\) then \(\left( f_1\circ  f_2\circ  \cdots  \circ  f_n \right){}^{-1}= f_n^{-1}\circ \cdots \circ f_2^{-1}\circ f_1^{-1}\text{.}\) The basis has been taken care of in [Exercise 7.3.4.12 [UNRESOLVED_INTERNAL_LINK]](s-function-composition.html#exercise-composition-inverse-basis).

> **Exercise 16 . —**

> Our definition of cardinality states that two sets, \(A\) and \(B\text{,}\) have the same cardinality if there exists a bijection between the two sets. Why does it not matter whether the bijection is from \(A\) into \(B\) or \(B\) into \(A\text{?}\)
> 
> Prove that “has the same cardinality as” is an equivalence relation on sets.

> **Exercise 17 . —**

> Construct a table listing as many “Laws of Function Composition” as you can identify. Use previous lists of laws as a guide.

> **Exercise 18 . —**

> Based on the definition of the identity function, show that for all functions \(f:A\to A\text{,}\) \(f\circ i=i\circ f = f\text{.}\)
