---
source_relative_path: "DM TXT/3-Logic/ads Quantifiers.html"
source_sha256: "458594b5ac0e39ad95afb25cec4794b1ae3a496a38aa0fc6fbb75e249f5b6fa0"
scope_class: active_candidate
displayed_section_or_chapter: "Section 3.8 Quantifiers"
---

# Section 3.8 Quantifiers

As we saw in Section 3.6, if \(p(n)\) is a proposition over a universe \(U\text{,}\) its truth set \(T_p\) is equal to a subset of \(U\text{.}\) In many cases, such as when \(p(n)\) is an equation, we are most concerned with whether \(T_p\) is empty or not. In other cases, we might be interested in whether \(T_p=U\text{;}\) that is, whether \(p(n)\) is a tautology. Since the conditions \(T_p\neq \emptyset\)  and \(T_p=U\) are so often an issue, we have a special system of notation for them.

# Subsection 3.8.1 The Existential Quantifier

> **Definition 3.8.1 — The Existential Quantifier.**

> If \(p(n)\) is a proposition over \(U\) with \(T_p\neq \emptyset\text{,}\) we commonly say “There exists an \(n\) in \(U\) such that \(p(n)\) (is true).” We abbreviate this with the symbols \((\exists  n)_U(p(n))\text{.}\) The symbol \(\exists\) is called the existential quantifier.   If the context is clear, the mention of \(U\) is dropped: \((\exists n)(p(n))\text{.}\)

> **Example 3.8.2 — Some examples of existential quantifiers.**

> \((\exists k)_{\mathbb{Z}}(k ^2- k - 12 = 0)\) is another way of saying that there is an integer that solves the equation \(k^2 - k - 12 = 0\text{.}\) The fact that two such integers exist doesn’t affect the truth of this proposition in any way.
> 
> \((\exists k)_{\mathbb{Z}}(3k=102)\) simply states that 102 is a multiple of 3, which is true. On the other hand, \((\exists  k)_{\mathbb{Z}}(3k=100)\) states that 100 is a multiple of 3, which is false.
> 
> \((\exists x)_{\mathbb{R}}(x^2 + 1 = 0)\) is false since the solution set of the equation \(x^2+ 1 = 0\) in the real numbers is empty.  It is common to write \((\nexists x)_{\mathbb{R}}(x^2 + 1 = 0)\)  in this case.

There are a wide variety of ways that you can write a proposition with an existential quantifier. [Table 3.8.5 [UNRESOLVED_INTERNAL_LINK]](s-quantifiers.html#table-quantifier-variations) contains a list of different variations that could be used for both the existential and universal quantifiers.

# Subsection 3.8.2 The Universal Quantifier

> **Definition 3.8.3 — The Universal Quantifier.**

> If \(p(n)\) is a proposition over \(U\) with \(T_p=U\text{,}\) we commonly say “For all \(n\) in \(U\text{,}\) \(p(n)\) (is true).” We abbreviate this with the symbols \((\forall n)_U(p(n))\text{.}\) The symbol \(\forall\) is called the universal quantifier.  If the context is clear, the mention of \(U\) is dropped: \((\forall n)(p(n))\text{.}\)

> **Example 3.8.4 — Some Universal Quantifiers.**

> We can say that the square of every real number is non-negative symbolically with a universal quantifier:  \((\forall x)
> _{\mathbb{R}}(x ^2 \geq  0)\text{.}\)
> 
> 
> \((\forall n) _{\mathbb{Z}} (n + 0 = 0 + n =n)\) says that the sum of zero and any integer \(n\) is \(n\text{.}\) This fact is called the identity property of zero for addition.

![Table 3.8.5 . Notational Variations with Quantified Expressions Universal Quantifier Existential Quantifier \((\forall n)_U(p(n))\) \((\exists n)_U(p(n))\) \((\forall n\in U)(p(n))\) \((\exists n\in U)(p(n))\) \(\forall n\in U, p(n)\) \(\exists n\in U \textrm{ such that } p(n)\) \(p(n), \forall n \in U\) \(p(n)\) is true for some \(n \in U\) \(p(n)\) is true for all \(n \in U\)]()

# Subsection 3.8.3 The Negation of Quantified Propositions

When you negate a quantified proposition, the existential and universal quantifiers complement one another.

> **Example 3.8.6 — Negation of an Existential Quantifier.**

> Over the universe of animals, define \(F(x)\text{:}\) \(x\) is a fish and \(W(x)\text{:}\) \(x\) lives in the water. We know that the proposition \(W(x) \rightarrow F(x)\) is not always true. In other words, \((\forall x)(W(x) \rightarrow  F(x))\) is false. Another way of stating this fact is that there exists an animal that lives in the water and is not a fish; that is,
> 
> \begin{equation*}
> \begin{split}
> \neg (\forall x)(W(x) \to  F(x)) & \Leftrightarrow (\exists  x)(\neg (W(x) \rightarrow  F(x))) \\
> &  \Leftrightarrow (\exists  x)(W(x) \land  \neg F(x))
> \end{split}\text{.}
> \end{equation*}

Note that the negation of a universally quantified proposition is an existentially quantified proposition. In addition, when you negate an existentially quantified proposition, you get a universally quantified proposition.   Symbolically,

![Table 3.8.7 . Negation of Quantified Expressions \(\neg ((\forall n)_U(p(n)) )\Leftrightarrow (\exists n)_U (\neg p(n))\) \(\neg ((\exists n)_U(p(n)) )\Leftrightarrow (\forall n)_U (\neg p(n))\)]()

> **Example 3.8.8 — More Negations of Quantified Expressions.**

> The ancient Greeks first discovered that \(\sqrt{2}\) is an irrational number; that is, \(\sqrt{2}\) is not a rational number. \(\neg ((\exists r)_{\mathbb{Q}}(r^2 = 2))\) and \((\forall r)_{\mathbb{Q}} (r^2\neq  2)\) both state this fact symbolically.
> 
> \(\neg ((\forall n)_{\mathbb{P}}(n ^2- n + 41 \textrm{ is prime}))\) is equivalent to \((\exists  n)_{\mathbb{P}} (n^2
> - n + 41 \textrm{ is composite})\text{.}\) They are either both true or both  false.

# Subsection 3.8.4 Multiple Quantifiers

If a proposition has more than one variable, then you can quantify it more than once. For example, \(p(x, y):x^2 - y^2 = (x + y)(x - y)\) is a tautology over the set of all pairs of real numbers because it is true for each pair \((x, y)\) in \(\mathbb{R} \times  \mathbb{R}\text{.}\) Another way to look at this proposition is as a proposition with two variables. The assertion that \(p(x,y)\) is a tautology could be quantified as \((\forall x)_{\mathbb{R}} ((\forall y) _{\mathbb{R}}(p(x, y)))\) or \((\forall y)_{\mathbb{R}} ((\forall x) _{\mathbb{R}}(p(x, y)))\)

In general, multiple universal quantifiers can be arranged in any order without logically changing the meaning of the resulting proposition. The same is true for multiple existential quantifiers. For example, \(p(x, y) : x + y = 4 \textrm{ and } x - y = 2\) is a proposition over \(\mathbb{R} \times \mathbb{R}\text{.}\) \((\exists x)_{\mathbb{R}} ((\exists y) _{\mathbb{R}} (x + y = 4 \textrm{ and } x - y = 2))\) and \((\exists y)_{\mathbb{R}}\textrm{ } ((\exists x) _{\mathbb{R}} (x + y = 4 \textrm{ and } x - y = 2))\) are equivalent. A proposition with multiple existential quantifiers such as this one says that there are simultaneous values for the quantified variables that make the proposition true. A similar example is \(q(x, y) : 2x - y = 2 \textrm{ and }4x - 2y = 5\text{,}\) which is always false; and the following are all equivalent:

\begin{equation*}
\begin{split}
\neg ((\exists  x)_{\mathbb{R}}((\exists  y)_{\mathbb{R}}(q(x, y)))) 
& \Leftrightarrow  \neg (\exists  y)_{\mathbb{R}}((\exists x)_{\mathbb{R}}(q(x, y))) \\
& \Leftrightarrow (\forall y)_{\mathbb{R}} (\neg ((\exists  x)_{\mathbb{R}}(q(x,y)))) \\
& \Leftrightarrow ((\forall y)_{\mathbb{R}} ((\forall x)_{\mathbb{R}} (\neg q(x, y))))\\
& \Leftrightarrow ((\forall x)_{\mathbb{R}} ((\forall y)_{\mathbb{R}} (\neg q(x, y))))
\end{split}
\end{equation*}

When existential and universal quantifiers are mixed, the order cannot be exchanged without possibly changing the meaning of the proposition. For example, let \(\mathbb{R}^+\) be the positive real numbers, \(x : (\forall a)_{\mathbb{R}^+} ((\exists  b)_{\mathbb{R}^+} (a b = 1))\) and \(y : (\exists  b)_{\mathbb{R}^+} ((\forall a)_{\mathbb{R}^+}(a b = 1))\) have different logical values; \(x\) is true, while \(y\) is false.

*Tips on Reading Multiply-Quantified Propositions.* It is understandable that you would find propositions such as \(x\) difficult to read. The trick to deciphering these expressions is to “peel” one quantifier off the proposition just as you would peel off the layers of an onion (but quantifiers shouldn’t make you cry!). Since the outermost quantifier in \(x\) is universal, \(x\) says that \(z(a) : (\exists  b)_{\mathbb{R}^+}(a b = 1)\) is true for each value that \(a\) can take on. Now take the time to select a value for \(a\text{,}\) like 6. For the value that we selected, we get \(z(6) : (\exists b)_{\mathbb{R}^+}(6b = 1)\text{,}\) which is obviously true since \(6b = 1\) has a solution in the positive real numbers. We will get that same truth value no matter which positive real number we choose for \(a\text{;}\) therefore, \(z(a)\) is a tautology over \(\mathbb{R}^+\) and we are justified in saying that \(x\) is true. The key to understanding propositions like \(x\) on your own is to experiment with actual values for the outermost variables as we did above.

Now consider \(y\text{.}\) To see that \(y\) is false, we peel off the outer quantifier. Since it is an existential quantifier, all that \(y\) says is that some positive real number makes \(w(b)\) : \((\forall a) _{\mathbb{R}^+} (a b = 1)\) true. Choose a few values of \(b\) to see if you can find one that makes \(w(b)\) true. For example, if we pick \(b = 2\text{,}\) we get \((\forall a) _{\mathbb{R}^+}(2a = 1)\text{,}\) which is false, since \(2a\) is almost always different from 1. You should be able to convince yourself that no value of \(b\) will make \(w(b)\) true.  Therefore, \(y\) is false.

Another way of convincing yourself that \(y\) is false is to convince yourself that \(\neg y\) is true:

\begin{equation*}
\begin{split}
\neg ((\exists  b)_{\mathbb{R}^+} ((\forall a)_{\mathbb{R}^+}(a b = 1))) 
&\Leftrightarrow (\forall  b)_{\mathbb{R}^+}\neg ((\forall a)_{\mathbb{R}^+}(a b = 1))\\
& \Leftrightarrow (\forall  b)_{\mathbb{R}^+} ((\exists a)_{\mathbb{R}^+}(a b \neq  1))
\end{split}
\end{equation*}

In words, for each value of \(b\text{,}\) there is a value for \(a\) that makes \(a b \neq  1\text{.}\)  One such value is \(a=\frac{1}{b}+1\text{.}\)  Therefore,  \(\neg y\) is true.

One final example that serves as a preview to how quantifiers appear in calculus.

> **Example 3.8.9 — The Limit of a Sequence.**

> What does it mean that 0.999… = 1?  The ellipsis (\(\dots\)) implies that there are an infinite number of 9’s on the left of the equals sign. Any way to try to justify this equality boils down to the idea of limits.  After many years of struggling with what this means, mathematicians have come up with a universally accepted interpretation involving quantifiers.  It is that
> 
> \begin{equation*}
> (\forall \epsilon)_{\mathbb{R}^+} ((\exists N)_{\mathbb{P}})(n\geq N \Rightarrow  |1- 0.\underbrace{99..9}_{n\,9’s}| \lt \epsilon))
> \end{equation*}
> 
> In calculus, the symbol \(\epsilon\) is usually reserved for small positive real numbers. Let’s pick a value for \(\epsilon\) and peel the universal quantifier off the statement above.  Let’s try  \(\epsilon\) equal to \(\frac{1}{2^{10}}=\frac{1}{1024}\text{.}\)  In addition we note that \(0.\underbrace{99..9}_{n\,9’s}=1-\frac{1}{10^n}\text{.}\)  With our choice of \(\epsilon\) we get
> 
> \begin{equation*}
> (\exists N)_{\mathbb{P}}(n\geq N \Rightarrow  |1- 0.\underbrace{99..9}_{n\,9’s}| \lt \frac{1}{1024}) 
> \end{equation*}
> 
> or
> 
> \begin{equation*}
> (\exists N)_{\mathbb{P}}(n\geq N \Rightarrow \frac{1}{10^n} \lt \frac{1}{1024}) 
> \end{equation*}
> 
> This last statement is true - one value of  \(N\) that would work is \(11\text{.}\) You just have to convince yourself that any positive value of \(\epsilon\text{,}\) no matter how small, will produce a true statement.  If you see that, you’ve convinced yourself that \(0.999\dots  = 1\text{!}\)

> **Exercise 1 . —**

> Let \(C(x)\) be “\(x\) is cold-blooded,” let \(F(x)\) be “\(x\) is a fish,” and let \(S(x)\) be “\(x\) lives in the sea.”

> Translate into a formula: Every fish is cold-blooded.
> Translate into English: \((\exists x)(S(x) \land  \neg F(x))\text{.}\)
> 
> Translate into English: \((\forall x)(F(x) \rightarrow  S(x))\text{.}\)

> **Exercise 2 . —**

> Let \(M(x)\) be “\(x\) is a mammal,” let \(A(x)\) be “\(x\) is an animal,” and let \(W(x)\) be “\(x\) is warm-blooded.”

> Translate into a formula: Every mammal is warm-blooded.
> Translate into English: \((\exists x)(A(x) \land  (\neg M(x)))\text{.}\)

> **Exercise 3 . —**

> Over the universe of books, define the propositions \(B(x)\text{:}\) \(x\) has a blue cover, \(M(x)\text{:}\) \(x\) is a mathematics book, \(U(x)\text{:}\) \(x\) is published in the United States, and \(R(x, y)\) : The bibliography of \(x\) includes \(y\text{.}\)

> Translate into words:

> \((\exists x)(\neg B(x))\text{.}\)
> \((\forall x)(M(x) \land  U(x) \rightarrow  B(x))\text{.}\)
> \((\exists x)(M(x) \land  \neg B(x))\text{.}\)
> \((\exists y)((\forall x)(M(x)\to R(x,y)))\text{.}\)
> Express using quantifiers: Every book with a blue cover is a mathematics book.
> Express using quantifiers: There are mathematics books that are published outside the United States.
> Express using quantifiers: Not all books have bibliographies.

> **Exercise 4 . —**

> Let the universe of discourse, \(U\text{,}\) be the set of all people, and let \(M(x, y)\) be “\(x\) is the mother of \(y\text{.}\)”

> Which of the following is a true statement? Translate it into English.

> \(\displaystyle (\exists  x)_U((\forall y)_U(M(x,y)))\)
> \(\displaystyle (\forall y)_U((\exists  x)_U(M(x,y)))\)
> Translate the following statement into logical notation using quantifiers and the proposition \(M(x, y)\) :  “Everyone has a maternal grandmother.”

> **Exercise 5 . —**

> Translate into your own words and indicate whether it is true or false that \((\exists u) _{\mathbb{Z}} (4 u^2 -9 = 0)\text{.}\)

> **Exercise 6 . —**

> Use quantifiers to say that \(\sqrt{3}\) is an irrational number.

> **Exercise 7 . —**

> What do the following propositions say, where \(U\) is the power set of \(\{1,2,\dots , 9\}\text{?}\) Which of these propositions are true?

> \((\forall A)_U \lvert A \rvert \neq \lvert A^c \rvert\text{.}\)
> \((\exists A)_U(\exists B)_U (\lvert A \rvert =5, \lvert B \rvert=5, \textrm{ and } A\cap B=\emptyset )\text{.}\)
> \((\forall A)_U(\forall B)_U (A-B=B^c-A^c)\text{.}\)

> **Exercise 8 . —**

> Use quantifiers to state that for every positive integer, there is a larger positive integer.

> **Exercise 9 . —**

> Use  quantifiers to state that the sum of any two rational numbers is rational.

> **Exercise 10 . —**

> Over the universe of real numbers, use quantifiers to say that the equation \(a + x = b\) has a solution for all values of \(a\) and \(b\text{.}\)

> **Exercise 11 . —**

> Let \(n\) be a positive integer.  Describe using quantifiers:

> \(\displaystyle x \in \underset{k=1}{\overset{n}{\cup }}A_k\)
> \(\displaystyle x \in \underset{k=1}{\overset{n}{\cap }}A_k\)

> **Exercise 12 . —**

> Prove that \((\exists x)(\forall y)(p(x, y)) \Rightarrow  (\forall y)(\exists x)(p(x, y))\text{,}\) but that converse is not true.
