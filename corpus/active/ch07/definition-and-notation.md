---
source_relative_path: "DM TXT/7-Functions_and_Probability/ads Definition and Notation.html"
source_sha256: "65168f84621c296a2da5776f3dcea99bd893306ce1afa3f010c4a11b336e4405"
scope_class: active_candidate
displayed_section_or_chapter: "Section 7.1 Definition and Notation"
---

# Section 7.1 Definition and Notation

# Subsection 7.1.1 Fundamentals

> **Definition 7.1.1 — Function.**

> A function from a set \(A\) into a set \(B\) is a relation from \(A\) into \(B\) such that each element of \(A\) is related to exactly one element of the set \(B\text{.}\) The set \(A\) is called the domain of the function and the set \(B\) is called the codomain.

The reader should note that a function \(f\) is a relation from \(A\) into \(B\) with two important restrictions:

Each element in the set \(A\text{,}\) the domain of \(f\text{,}\) must be related to some element of \(B\text{,}\) the codomain.
The phrase “is related to exactly one element of the set \(B\)” means that if \((a, b)\in f\) and \((a, c)\in f\text{,}\) then \(b = c\text{.}\)

> **Example 7.1.2 — A function as a list of ordered pairs.**

> Let \(A = \{-2, -1,0, 1, 2\}\) and \(B = \{0, 1, 2, 3, 4\}\text{,}\) and if \(s = \{(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)\}\text{,}\) then \(s\) is a function from \(A\) into \(B\text{.}\)

> **Example 7.1.4 — A function as a set of ordered pairs in set-builder notation.**

> Let \(\mathbb{R}\) be the real numbers. Then \(L = \{(x, 3x) \mid x \in \mathbb{R}\}\) is a function from \(\mathbb{R}\) into \(\mathbb{R}\text{,}\) or, more simply, \(L\) is a function on \(\mathbb{R}\text{.}\)

It is customary to use a different system of notation for functions than the one we used for relations. If \(f\) is a function from the set  \(A\) into the set \(B\text{,}\) we will write \(f:A \rightarrow B\text{.}\)

The reader is probably more familiar with the notation for describing functions that is used in basic algebra or calculus courses. For example, \(y =\frac{1}{x}\) or \(f(x) =\frac{1}{x}\) both define the function \(\left\{\left.\left(x,\frac{1}{x}\right)\right| x\in \mathbb{R}, x\neq
0\right\}\text{.}\) Here the domain was assumed to be those elements of \(\mathbb{R}\) whose substitutions for \(x\) make sense, the nonzero real numbers, and the codomain was assumed to be \(\mathbb{R}\text{.}\) In most cases, we will make a point of listing the domain and codomain in addition to describing what the function does in order to define a function.

The terms mapping, map, and transformation are also used for functions.

> **Definition 7.1.5 — The Set of Functions Between Two Sets.**

> Given two sets,  \(A\) and \(B\text{,}\) the set of all functions from \(A\) into \(B\) is denoted  \(B^A\text{.}\)

The notation used for sets of functions makes sense in light of [Exercise 5 [UNRESOLVED_INTERNAL_LINK]](s-function-def-notation.html#exercise-counting-functions).

One way to imagine a function and what it does is to think of it as a machine. The machine could be mechanical, electronic, hydraulic, or abstract. Imagine that the machine only accepts certain objects as raw materials or input. The possible raw materials make up the domain. Given some input, the machine produces a finished product that depends on the input. The possible finished products that we imagine could come out of this process make up the codomain.

> **Example 7.1.6 — A definition based on images.**

> We can define a function based on specifying the codomain element to which each domain element is related.   For example, \(f: \mathbb{R} \rightarrow \mathbb{R}\) defined by \(f(x) = x^2\) is an alternate description of \(f= \left\{\left.\left(x,
> x ^2\right)\right|x \in  \mathbb{R}\right\}\text{.}\)

> **Definition 7.1.7 — Image of an element under a function.**

> Let \(f:A \rightarrow  B\text{,}\) read “Let \(f\) be a function from the set \(A\) into the set \(B\text{.}\)” If \(a \in  A\text{,}\) then \(f(a)\) is used to denote that element of \(B\) to which \(a\) is related. \(f(a)\) is called the image of \(a\text{,}\) or, more precisely, the image of \(a\) under \(f\text{.}\) We write \(f(a) = b\) to indicate that the image of \(a\) is \(b\text{.}\)

In [Example 7.1.6 [UNRESOLVED_INTERNAL_LINK]](s-function-def-notation.html#ex-non-pair-description), the image of 2 under \(f\) is 4; that is, \(f(2) = 4\text{.}\) In [Example 7.1.2 [UNRESOLVED_INTERNAL_LINK]](s-function-def-notation.html#ex-function-1), the image of \(-1\) under \(s\) is 1; that is, \(s(-1) = 1\text{.}\)

> **Definition 7.1.8 — Range of a Function.**

> The range of a function is the set of images of its domain. If \(f:X \rightarrow Y\text{,}\) then the range of \(f\) is denoted \(f(X)\text{,}\) and
> 
> \begin{equation*}
> f(X) = \{f(a) \mid a \in X\} = \{b \in Y \mid  \exists a \in X\textrm{ such that } f(a) = b\}\text{.}
> \end{equation*}

Note that the range of a function is a subset of its codomain. \(f(X)\) is also read as “the image of the set \(X\) under the function \(f\)” or simply “the image of \(f\text{.}\)”

In [Example 7.1.2 [UNRESOLVED_INTERNAL_LINK]](s-function-def-notation.html#ex-function-1), \(s(A)= \{0, 1, 4\}\text{.}\) Notice that 2 and 3 are not images of any element of \(A\text{.}\) In addition, note that both 1 and 4 are related to more than one element of the domain: \(s(1) = s(-1) = 1\) and \(s(2) = s(-2) = 4\text{.}\) This does not violate the definition of a function. Go back and read the definition if this isn’t clear to you.

In [Example 7.1.4 [UNRESOLVED_INTERNAL_LINK]](s-function-def-notation.html#ex-function-2), the range of \(L\) is equal to its codomain, \(\mathbb{R}\text{.}\) If \(b\) is any real number, we can demonstrate that it belongs to \(L(\mathbb{R})\) by finding a real number \(x\) for which \(L(x) = b\text{.}\) By the definition of \(L\text{,}\) \(L(x) = 3x\text{,}\) which leads us to the equation \(3x = b\text{.}\) This equation always has a solution, \(\frac{b}{3}\text{;}\) thus \(L(\mathbb{R}) = \mathbb{R}\text{.}\)

The formula that we used to describe the image of a real number under \(L\text{,}\) \(L(x) = 3x\text{,}\) is preferred over the set notation for \(L\) due to its brevity. Any time a function can be described with a rule or formula, we will use this form of description. In [Example 7.1.2 [UNRESOLVED_INTERNAL_LINK]](s-function-def-notation.html#ex-function-1), the image of each element of \(A\) is its square. To describe that fact, we write \(s(a) = a^2\) (\(a \in  A\)), or \(S:A \rightarrow  B\) defined by \(S(a) = a^2\text{.}\)

There are many ways that a function can be described. Many factors, such as the complexity of the function, dictate its representation.

> **Example 7.1.9 — Data as a function.**

> Suppose a survey of 1,000 persons is done asking how many hours of television each watches per day. Consider the function \(W:
> \{0,1,\ldots , 24\} \rightarrow  \{0,1,2,\ldots ,1000\}\) defined by
> 
> \begin{equation*}
> W(t) = \textrm{the number of persons who gave a response of } t \textrm{ hours}
> \end{equation*}
> 
> This function will probably have no formula such as the ones for \(s\) and \(L\) above.

> **Example 7.1.10 — Conditional definition of a function.**

> Consider the function \(m:\mathbb{P} \rightarrow  \mathbb{Q}\) defined by the set
> 
> \begin{equation*}
> m = \{(1, 1), (2, 1/2), (3, 9), (4, 1/4), (5, 25), . . . \} 
> \end{equation*}
> 
> No simple single formula could describe \(m\text{,}\) but if we assume that the pattern given continues, we can write
> 
> \begin{equation*}
> m(x) =\left\{
> \begin{array}{cc}
> x^2 &  \textrm{if } x \textrm{ is odd} \\
> 1/x & \textrm{if } x \textrm{ is even} \\
> \end{array}
> \right.
> \end{equation*}

# Subsection 7.1.2 Functions of Two Variables

If the domain of a function is the Cartesian product of two sets, then our notation and terminology changes slightly. For example, consider the function \(G:\mathbb{N} \times \mathbb{N}\rightarrow \mathbb{N}\) defined by \(G\left(\left(n_1,n_2\right)\right)=n_1^2+n_2^2- n_1n_2+10\text{.}\)  For this function, we would drop one set of parentheses and write \(G(4, 2) = 22\text{,}\) not \(G((4, 2)) = 22\text{.}\) We call \(G\) a function of two variables. From one point of view, this function is no different from any others that we have seen. The elements of the domain happen to be slightly more complicated. On the other hand, we can look at the individual components of the ordered pairs as being separate. If we interpret \(G\) as giving us the cost of producing quantities of two products, we can imagine varying \(n_1\) while \(n_2\) is fixed, or vice versa.

The same observations can be made for function of three or more variables.

# Subsection 7.1.3 SageMath Note

There are several ways to define a function in Sage. The simplest way to implement \(f\) is as follows.

```sage

```

```sage

```

Sage is built upon the programming language Python, which is a *strongly typed language* and so you can’t evaluate expressions such as `f('Hello')`. However a function such as \(f\text{,}\) as defined above, will accept any type of number, so a bit more work is needed to restrict the inputs of \(f\) to the integers.

A second way to define a function in Sage is based on Python syntax.

```sage

```

# Subsection 7.1.4 Non-Functions

We close this section with two examples of relations that are not functions.

> **Example 7.1.11 — A non-function.**

> Let \(A = B = \{1, 2, 3\}\) and let \(f= \{(1, 2), (2, 3)\}\text{.}\) Here \(f\) is not a function from \(A\) into \(B\)  because \(3\) is not related to anything in the codomain.  In other words, \(f\) does not act on, or “use,” all elements of \(A\text{.}\)

> **Example 7.1.12 — Another non-function.**

> Let \(A = B = \{1,2, 3\}\) and let \(g = \{(1, 2), (2, 3), (2, 1),(3, 2)\}\text{.}\) We note that \(g\) acts on all of \(A\text{.}\)  However, \(g\) is still not a function since \((2, 3) \in  g\) and \((2, 1) \in  g\) and the condition on each domain element being related to exactly one element of the codomain is violated.

> **Exercise 1 . —**

> Let \(A = \{1, 2, 3, 4\}\) and \(B = \{a, b, c, d\}\text{.}\) Determine which of the following are functions from \(A\) into \(B\text{.}\) Explain.

> \(f \subseteq  A \times  B\text{,}\) where \(f = \{(1, a), (2, b), (3, c), (4, d)\}\text{.}\)
> 
> 
> \(g\subseteq A\times B\text{,}\) where \(g = \{(1, a), (2, a), (3,b), (4,d)\}\text{.}\)
> 
> 
> \(h \subseteq A \times  B\text{,}\) where \(h = \{(1, a), (2, b), (3, c)\}\text{.}\)
> 
> 
> \(k \subseteq A\times  B\text{,}\) where \(k = \{(1, a), (2, b), (2, c), (3, a), (4, a)\}\text{.}\)
> 
> 
> \(L\subseteq A\times A\text{,}\) where \(L = \{(1, 1), (2, 1), (3, 1), (4, 1)\}\text{.}\)

> **Exercise 2 . —**

> Find the ranges of the following functions on \(\mathbb{Z}\text{:}\)

> \(g = \{(x, 4x +1)|x \in  \mathbb{Z}\}\text{.}\)
> \(h(x) = \textrm{the least integer that is greater than or equal to } \sqrt{|x|}\text{.}\)
> \(P(x) = x + 10\text{.}\)

> **Exercise 3 . —**

> Find the ranges of each of the relations that are functions in Exercise 1.

> **Exercise 4 . —**

> Let \(U\) be a set and let \(S\) be any subset of \(U\text{.}\) Let \(\chi_S: U\to \{0,1\}\) be defined by
> 
> \begin{equation*}
> \chi_S(x)= \left\{
> \begin{array}{cc}
> 1 & \textrm{if } x\in S \\
> 0 & \textrm{if } x\notin S \\
> \end{array}
> \right.
> \end{equation*}

> The function \(\chi_S\) is called the characteristic function of \(S\text{.}\)

> If \(U = \{a, b, c\}\) and \(S = \{a, b\}\text{,}\) list the elements of \(\chi_S\) .
> If \(U = \{a, b, c, d, e\}\) and \(S = \{a, c, e\}\text{,}\) list the elements of \(\chi_S\text{.}\)
> 
> If \(U = \{a, b, c\}\text{,}\) what are \(\chi_{\emptyset}\) and \(\chi_U\text{?}\)

> **Exercise 5 . —**

> If \(A\) and \(B\) are finite sets, how many different functions are there from \(A\) into \(B\text{?}\)

> **Exercise 6 . —**

> Let \(U\) be a set with subsets \(A\) and \(B\text{.}\)

> Show that \(g:U\to \{0,1\}\) defined by \(g(a)=\min \left(\chi_A(a),\chi_B(a)\right)\) is the characteristic function of \(A\cap B\text{.}\)
> 
> What characteristic function is \(h:U\to \{0,1\}\) defined by \(h(a)=\max \left(\chi_A(a),\chi_B(a)\right)\text{?}\)
> 
> How are the characteristic functions of \(A\) and \(A^c\) related?

> **Exercise 7 . —**

> Let \(f\) be a function with domain \(A\) and codomain \(B\text{.}\) Consider the relation \(K \subseteq  A \times  A\) defined on the domain of \(f\) by \((x, y) \in  K\) if and only if \(f(x) = f(y)\text{.}\) The relation \(K\) is called the kernel of \(f\text{.}\)

> Prove that \(K\) is an equivalence relation.
> For the specific case of \(A = \mathbb{Z}\text{,}\) where \(\mathbb{Z}\) is the set of integers, let \(f: \mathbb{Z} \rightarrow  \mathbb{Z}\) be defined by \(f(x) = x^2\text{.}\) Describe the equivalence classes of the kernel for this specific function.

> **Exercise 8 . —**

> Let \(f:\mathbb{P}\to \mathbb{P}\text{,}\) where \(f(a)\) is the largest power of two that evenly divides \(a\text{;}\) for example, \(f(12)=4,f(9)=1,\text{and}
> f(8)=8\text{.}\) Describe the equivalence classes of the kernel of \(f\text{.}\)
