---
source_relative_path: "DM TXT/1-Set-Theory/ads Cartesian Products and Power Sets.html"
source_sha256: "1258e25597df960593f6d28e63db62860595d8bde00992d1d639832893162eeb"
scope_class: active_candidate
displayed_section_or_chapter: "Section 1.3 Cartesian Products and Power Sets"
---

# Section 1.3 Cartesian Products and Power Sets

# Subsection 1.3.1 Cartesian Products

> **Definition 1.3.1 — Cartesian Product.**

> Let \(A\) and \(B\) be sets. The Cartesian product of \(A\) and \(B\text{,}\) denoted by \(A\times B\text{,}\) is defined as follows: \(A\times B = \{(a, b) \mid a \in  A \quad\textrm{and}\quad b \in  B\}\text{,}\) that is, \(A\times B\) is the set of all possible ordered pairs whose first component comes from \(A\) and whose second component comes from \(B\text{.}\)

> **Example 1.3.2 — Some Cartesian Products.**

> Notation in mathematics is often developed for good reason. In this case, a few examples will make clear why the symbol \(\times\) is used for Cartesian products.

> Let \(A = \{1, 2, 3\}\) and \(B = \{4, 5\}\text{.}\) Then \(A \times  B = \{(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)\}\text{.}\) Note that \(|A \times B| = 6 = \lvert A \rvert  \times  \lvert B \rvert \text{.}\)
> 
> 
> \(A \times  A = \{(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)\}\text{.}\) Note that \(|A \times  A| = 9 = {\lvert A \rvert}^2\text{.}\)

These two examples illustrate the general rule that if \(A\) and \(B\) are finite sets, then \(\lvert A \times B \rvert = \lvert A \rvert  \times  \lvert B \rvert \text{.}\)

We can define the Cartesian product of three (or more) sets similarly. For example, \(A \times  B \times  C = \{(a, b, c):a \in  A, b \in  B, c \in C\}\text{.}\)

It is common to use exponents if the sets in a Cartesian product are the same:

\begin{equation*}
A^2= A \times  A
\end{equation*}


\begin{equation*}
A^3=A \times A \times A
\end{equation*}

and in general,

\begin{equation*}
A^n =  \underset{n \textrm{ factors}}{\underline{A \times A \times \ldots \times A}}\text{.}
\end{equation*}

# Subsection 1.3.2 Power Sets

> **Definition 1.3.3 — Power Set.**

> If \(A\) is any set, the power set of \(A\) is the set of all subsets of \(A\text{,}\) denoted \(\mathcal{P}(A)\text{.}\)

The two extreme cases, the empty set and all of \(A\text{,}\) are both included in \(\mathcal{P}(A)\text{.}\)

> **Example 1.3.4 — Some Power Sets.**

> \(\displaystyle \mathcal{P}(\emptyset )=\{\emptyset \}\)
> \(\displaystyle \mathcal{P}(\{1\}) = \{\emptyset , \{1\}\}\)
> \(\mathcal{P}(\{1,2\}) = \{\emptyset , \{1\}, \{2\}, \{1, 2\}\}\text{.}\)

> We will leave it to you to guess at a general formula for the number of elements in the power set of a finite set. In Chapter 2, we will discuss counting rules that will help us derive this formula.

# Subsection 1.3.3 SageMath Note: Cartesian Products and Power Sets

Here is a simple example of a cartesian product of two sets:

```sage

```

Here is the cardinality of the cartesian product.

```sage

```

The power set of a set is an iterable, as you can see from the output of this next cell

```sage

```

You can iterate over a powerset. Here is a trivial example.

```sage

```

> **Exercise 1 . —**

> Let \(A = \{0, 2, 3\}\text{,}\) \(B = \{2, 3\}\text{,}\) \(C = \{1, 4\}\text{,}\) and let the universal set be \(U = \{0, 1, 2, 3, 4\}\text{.}\) List the elements of

> \(\displaystyle A \times B\)
> \(\displaystyle B \times  A\)
> \(\displaystyle A \times B\times C\)
> \(\displaystyle U \times \emptyset\)
> \(\displaystyle A \times  A^c\)
> \(\displaystyle B^2\)
> \(\displaystyle B^3\)
> \(\displaystyle B\times \mathcal{P}(B)\)

> **Exercise 2 . —**

> Suppose that you are about to flip a coin and then roll a die. Let \(A = \{HEADS, TAILS\}\) and  \(B = \{1, 2, 3, 4, 5, 6\}\text{.}\)

> What is \(|A \times  B|\text{?}\)
> 
> How could you interpret the set \(A \times  B\) ?

> **Exercise 3 . —**

> List all two-element sets in \(\mathcal{P}(\{a,b,c,d\})\)

> **Exercise 4 . —**

> List all three-element sets in \(\mathcal{P}(\{a, b, c,d\})\text{.}\)

> **Exercise 5 . —**

> How many singleton (one-element) sets are there in \(\mathcal{P}(A)\) if \(\lvert A \rvert =n\) ?

> **Exercise 6 . —**

> A person has four coins in his pocket: a penny, a nickel, a dime, and a quarter. How many different sums of money can he take out if he removes 3 coins at a time?

> **Exercise 7 . —**

> Let \(A = \{+,-\}\) and \(B = \{00, 01, 10, 11\}\text{.}\)

> List the elements of \(A \times  B\)
> 
> How many elements do \(A ^4\) and \((A \times B)^3\) have?

> **Exercise 8 . —**

> Let \(A = \{\bullet,\square ,\otimes \}\) and \(B = \{\square ,\ominus ,\bullet\}\text{.}\)

> List the elements of \(A \times  B\) and \(B \times  A\text{.}\) The parentheses and comma in an ordered pair are not necessary in cases such as this where the elements of each set are individual symbols.
> Identify the intersection of \(A \times  B\) and \(B \times  A\) for the case above, and then guess at a general rule for the intersection of \(A \times  B\) and \(B \times  A\text{,}\) where \(A\) and \(B\) are any two sets.

> **Exercise 9 . —**

> Let \(A\) and \(B\) be nonempty sets. When are \(A \times  B\) and \(B \times  A\) equal?
