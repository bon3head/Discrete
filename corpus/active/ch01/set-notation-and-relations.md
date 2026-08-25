---
source_relative_path: "DM TXT/1-Set-Theory/ads Set Notation and Relations.html"
source_sha256: "cc91eaeba4a08295578fc384b69dbfc6361918c6fe92741baf6ec54cf97e9190"
scope_class: active_candidate
displayed_section_or_chapter: "Section 1.1 Set Notation and Relations"
---

# Section 1.1 Set Notation and Relations

# Subsection 1.1.1 The notion of a set

The term set is intuitively understood by most people to mean a collection of objects that are called elements (of the set). This concept is the starting point on which we will build more complex ideas, much as in geometry where the concepts of point and line are left undefined. Because a set is such a simple notion, you may be surprised to learn that it is one of the most difficult concepts for mathematicians to define to their own liking. For example, the description above is not a proper definition because it requires the definition of a collection. (How would you define “collection”?) Even deeper problems arise when you consider the possibility that a set could contain itself. Although these problems are of real concern to some mathematicians, they will not be of any concern to us. Our first concern will be how to describe a set; that is, how do we most conveniently describe a set and the elements that are in it? If we are going to discuss a set for any length of time, we usually give it a name in the form of a capital letter (or occasionally some other symbol). In discussing set \(A\text{,}\) if \(x\) is an element of \(A\text{,}\) then we will write \(x \in  A\text{.}\)  On the other hand, if \(x\) is not an element of \(A\text{,}\) we write \(x \notin  A\text{.}\)  The most convenient way of describing the elements of a set will vary depending on the specific set.

Enumeration. When the elements of a set are enumerated (or listed) it is traditional to enclose them in braces. For example, the set of binary digits is \(\{0, 1\}\) and the set of decimal digits is \(\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}\text{.}\) The choice of a name for these sets would be arbitrary; but it would be “logical” to call them \(B\) and \(D\text{,}\) respectively. The choice of a set name is much like the choice of an identifier name in programming.

Some large sets can be enumerated without actually listing all the elements. For example, the letters of the alphabet and the integers from 1 to 100 could be described as \(A = \{a, b, c,\ldots , x, y, z\}\text{,}\) and \(G = \{1, 2, \ldots  , 99, 100\}\text{.}\) The three consecutive “dots” are called an ellipsis. We use them when it is clear what elements are included but not listed. An ellipsis is used in two other situations. To enumerate the positive integers, we would write \(\{1, 2, 3,\ldots  \}\text{,}\) indicating that the list goes on infinitely. If we want to list a more general set such as the integers between 1 and \(n\text{,}\) where \(n\) is some undetermined positive integer, we might write \(\{1,\ldots ,n\}\text{.}\)

Standard Symbols. Sets that are frequently encountered are usually given symbols that are reserved for them alone. For example, since we will be referring to the positive integers throughout this book, we will use the symbol \(\mathbb{P}\) instead of writing \(\{1, 2, 3, \ldots \}\text{.}\) A few of the other sets of numbers that we will use are:


\(\mathbb{(N)}\text{:}\) the natural numbers, \(\{0, 1, 2, 3, \ldots \}\)


\(\mathbb{(Z)}\text{:}\) the integers, \(\{\ldots , -3, -2, -1, 0, 1, 2, 3,\ldots \}\)


\(\mathbb{(Q)}\text{:}\) the rational numbers

\(\mathbb{(R)}\text{:}\) the real numbers

\(\mathbb{(C)}\text{:}\) the complex numbers

Set-Builder Notation. Another way of describing sets is to use set-builder notation. For example, we could define the rational numbers as

\begin{equation*}
\mathbb{Q}=\{a/b \mid a, b \in  \mathbb{Z}, b\neq 0\}\text{.}
\end{equation*}

Note that in the set-builder description for the rational numbers:


\(a/b\) indicates that a typical element of the set is a “fraction.”
The vertical line, \(\mid\text{,}\) is read “such that” or “where,” and is used interchangeably with a colon.

\(a, b\in \mathbb{Z}\) is an abbreviated way of saying \(a\) and \(b\) are integers.
Commas in mathematics are read as “and.”

The important fact to keep in mind in set notation, or in any mathematical notation, is that it is meant to be a help, not a hindrance. We hope that notation will assist us in a more complete understanding of the collection of objects under consideration and will enable us to describe it in a concise manner. However, brevity of notation is not the aim of sets. If you prefer to write \(a\in \mathbb{Z}\) and \(b\in \mathbb{Z}\) instead of \(a, b\in \mathbb{Z}\text{,}\) you should do so. Also, there are frequently many different, and equally good, ways of describing sets. For example, \(\{x\in
\mathbb{R} \mid x^{2}-5x+6 =0\}\) and \(\{x \mid x \in \mathbb{R}, x^{2}-5x+6=0\}\) both describe the solution set \(\{2, 3\}\text{.}\)

A proper definition of the real numbers is beyond the scope of this text. It is sufficient to think of the real numbers as the set of points on a number line. The complex numbers can be defined using set-builder notation as \(\mathbb{C} = \{a + b i:a, b \in \mathbb{R}\}\text{,}\) where \(i^2 = -1\text{.}\)

In the following definition we will leave the word “finite” undefined.

> **Definition 1.1.1 — Finite Set.**

> A set is a finite set if it has a finite number of elements. Any set that is not finite is an infinite set.

> **Definition 1.1.2 — Cardinality.**

> Let \(A\) be a finite set. The number of different elements in \(A\) is called its cardinality.  The cardinality of a finite set \(A\) is denoted \(\lvert A \rvert\text{.}\)

As we will see later, there are different infinite cardinalities. We can’t make this distinction until Chapter 7, so we will restrict cardinality to finite sets for now.

# Subsection 1.1.2 Subsets

> **Definition 1.1.3 — Subset.**

> Let \(A\) and \(B\) be sets. We say that \(A\) is a subset of \(B\)  if and only if every element of \(A\) is an element of \(B\text{.}\) We write \(A \subseteq B\) to denote the fact that \(A\) is a subset of \(B\text{.}\)

> **Example 1.1.4 — Some Subsets.**

> If \(A = \{3, 5, 8\}\) and \(B = \{5, 8, 3, 2, 6\}\text{,}\) then \(A\subseteq B\text{.}\)
> 
> \(\displaystyle \mathbb{N}\subseteq \mathbb{Z}\subseteq \mathbb{Q}\subseteq \mathbb{R}\subseteq \mathbb{C}\)
> If \(S = \{3, 5, 8\}\) and \(T = \{5, 3, 8\}\text{,}\) then \(S \subseteq  T\) and \(T \subseteq  S\text{.}\)

> **Definition 1.1.5 — Set Equality.**

> Let \(A\) and \(B\) be sets. We say that \(A\) is equal to \(B\) (notation \(A = B\)) if and only if every element of \(A\) is an element of \(B\) and conversely every element of \(B\) is an element of \(A\text{;}\) that is, \(A \subseteq  B\) and \(B \subseteq  A\text{.}\)

> **Example 1.1.6 — Examples illustrating set equality.**

> In [Example 1.1.4 [UNRESOLVED_INTERNAL_LINK]](s-set-Notation-and-Relations.html#some-subsets), \(S = T\text{.}\) Note that the ordering of the elements is unimportant.
> The number of times that an element appears in an enumeration doesn’t affect a set. For example, if \(A = \{1, 5, 3, 5\}\) and \(B = \{1, 5, 3\}\text{,}\) then \(A = B\text{.}\)  Warning to readers of other texts: Some books introduce the concept of a multiset, in which the number of occurrences of an element matters.

A few comments are in order about the expression “if and only if” as used in our definitions. This expression means “is equivalent to saying,” or more exactly, that the word (or concept) being defined can at any time be replaced by the defining expression. Conversely, the expression that defines the word (or concept) can be replaced by the word.

Occasionally there is need to discuss the set that contains no elements, namely the empty set, which is denoted by \(\emptyset\) . This set is also called the null set. Another acceptable way to denote the empty set is \(\{\,\}\text{.}\)

It is clear, we hope, from the definition of a subset, that given any set \(A\) we have \(A\subseteq A\) and \(\emptyset \subseteq A\text{.}\) If \(A\) is nonempty, then \(A\) is called an improper subset of \(A\text{.}\)  All other subsets of \(A\text{,}\) including the empty set, are called proper subsets of \(A\text{.}\) The empty set is an improper subset of itself.

> **Exercise 1 . —**

> List four elements of each of the following sets:

> \(\displaystyle \{k \in  \mathbb{P} \mid {k - 1} \textrm{ is a multiple of 7}\}\)
> \(\displaystyle \{x \mid x \textrm{ is a fruit and its skin is normally eaten}\}\)
> \(\displaystyle \{x \in \mathbb{Q}\mid \frac{1}{x} \in \mathbb{Z}\}\)
> \(\displaystyle \{2n \mid n \in \mathbb{Z}, n < 0 \}\)
> \(\displaystyle \{s \mid s = 1 + 2 + \cdots  + n \textrm{ for some } n \in \mathbb{P}\}\)

> **Exercise 2 . —**

> List all elements of the following sets:

> \(\displaystyle \{\frac{1}{n} \mid n \in \{3,4,5,6\}\}\)
> \(\displaystyle \{\alpha \in  \textrm{ the alphabet } \mid  \alpha \textrm{ precedes F}\}\)
> \(\displaystyle \{x \in \mathbb{Z} \mid x = x+1 \}\)
> \(\displaystyle \{n^2 \mid  n = -2, -1, 0, 1, 2\}\)
> \(\displaystyle \{n \in  \mathbb{P} \mid n \textrm{ is a  factor of  24 }\}\)

> **Exercise 3 . —**

> Describe the following sets using set-builder notation.
> 
> \(\displaystyle \{ 5, 7, 9, \dots , 77, 79\}\)
> the rational numbers that are strictly between \(-1\) and \(1\)
> 
> the even integers
> \(\displaystyle \{-18, -9,0,9, 18,27, \dots \}\)

> **Exercise 4 . —**

> Use set-builder notation to describe the following sets:
> 
> \(\displaystyle \{1, 2, 3, 4, 5, 6, 7\}\)
> \(\displaystyle \{1, 10, 100, 1000, 10000\}\)
> \(\displaystyle \{1, 1/2, 1/3, 1/4, 1/5, . . .\}\)
> \(\displaystyle \{0\}\)

> **Exercise 5 . —**

> Let \(A = \{0, 2, 3\}\text{,}\) \(B = \{2, 3\}\text{,}\) and \(C = \{1, 5, 9\}\text{.}\) Determine which of the following statements are true. Give reasons for your answers.

> \(\displaystyle 3 \in  A\)
> \(\displaystyle \{3\} \in  A\)
> \(\displaystyle \{3\} \subseteq A\)
> \(\displaystyle B\subseteq A\)
> \(\displaystyle A\subseteq B\)
> \(\displaystyle \emptyset \subseteq C\)
> \(\displaystyle \emptyset \in A\)
> \(\displaystyle A\subseteq A\)

> **Exercise 6 . —**

> (From [[28] [UNRESOLVED_INTERNAL_LINK]](backmatter-7.html#biblio-levin-2020)) Explain why there is no set \(A\)  which satisfies \(A=\{2,\mid A \mid \}\text{.}\)

> **Exercise 7 . —**

> We introduced the empty set in this section and pointed out the two standard ways to denote this set, \(\emptyset\) and \(\{\,\}\text{.}\)  Explain why \(\{\emptyset\}\) is not a correct way to denote the empty set.

> **Exercise 8 . —**

> One reason that we left the definition of a set vague is Russell’s Paradox. Many mathematics and logic books contain an account of this paradox. Two references are [[42] [UNRESOLVED_INTERNAL_LINK]](backmatter-7.html#biblio-stoll-1961) and [[37] [UNRESOLVED_INTERNAL_LINK]](backmatter-7.html#biblio-quine-1966). Find one such reference and read it. If you don’t have access to a book, you could Google "Russell’s Paradox" and there are several sites that describe it.
