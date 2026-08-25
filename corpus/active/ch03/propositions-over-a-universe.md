---
source_relative_path: "DM TXT/3-Logic/ads Propositions over a Universe.html"
source_sha256: "70522605a44817f25ac432f6442526002194b34119d4dce0b5e0852d06f9a4ad"
scope_class: active_candidate
displayed_section_or_chapter: "Section 3.6 Propositions over a Universe"
content_gap: true
missing_assets:
  - "generated/sageplot/sageplot-venn-truth-set-conditional.svg"
---

# Section 3.6 Propositions over a Universe

# Subsection 3.6.1 Propositions over a Universe

Consider the sentence “He was a member of the Boston Red Sox.” There is no way that we can assign a truth value to this sentence unless “he” is specified. For that reason, we would not consider it a proposition. However, “he” can be considered a variable that holds a place for any name. We might want to restrict the value of “he” to all names in the major-league baseball record books. If that is the case, we say that the sentence is a proposition over the set of major-league baseball players, past and present.

> **Definition 3.6.1 — Proposition over a Universe.**

> Let \(U\) be a nonempty set. A proposition over \(U\) is a sentence that contains a variable that can take on any value in \(U\) and that has a definite truth value as a result of any such substitution.

A proposition over a universe is also referred to as a predicate.

> **Example 3.6.2 — Some propositions over a variety of universes.**

> A few propositions over the integers are \(4x^2 - 3x = 0\text{,}\) \(0 \leq  n \leq 5\text{,}\) and “\(k\) is a multiple of 3.”
> A few propositions over the rational numbers are \(4x^2 - 3x = 0\text{,}\) \(y^2=2\text{,}\) and  \((s - 1)(s + 1) = s^2 - 1\text{.}\)
> 
> A few propositions over the subsets of \(\mathbb{P}\) are \((A =\emptyset ) \lor  (A = \mathbb{P} )\text{,}\) \(3 \in  A\text{,}\) and  \(A \cap  \{1, 2, 3\}\neq  \emptyset\text{.}\)

All of the laws of logic that we listed in Section 3.4 are valid for propositions over a universe. For example, if \(p\) and \(q\) are propositions over the integers, we can be certain that \(p \land  q \Rightarrow  p\text{,}\) because \((p \land  q) \to  p\) is a tautology and is true no matter what values the variables in \(p\) and \(q\) are given. If we specify \(p\) and \(q\) to be \(p(n) : n < 4\) and \(q(n) : n < 8\text{,}\) we can also say that \(p\) implies \(p \land  q\text{.}\) This is not a usual implication, but for the propositions under discussion, it is true. One way of describing this situation in general is with truth sets.

# Subsection 3.6.2 Truth Sets

> **Definition 3.6.3 — Truth Set.**

> If \(p\) is a proposition over \(U\text{,}\) the truth set of \(p\) is \(T_p = \{a \in  U \mid p(a) \textrm{ is true}\}\text{.}\)

> **Example 3.6.4 — Truth Set Example.**

> The truth set of the proposition \(\{1, 2\} \cap A = \emptyset\text{,}\) taken as a proposition over the power set of \(\{1, 2, 3, 4\}\) is \(\{\emptyset , \{3\}, \{4\}, \{3, 4\}\}\text{.}\)

> **Example 3.6.5 — Truth sets depend on the universe.**

> Over the universe \(\mathbb{Z}\) (the integers), the truth set of \(4x^2- 3x = 0\) is \(\{0\}\text{.}\) If the universe is expanded to the rational numbers, the truth set becomes \(\{0, 3/4\}\text{.}\) The term *solution set* is often used for the truth set of an equation such as the one in this example.

> **Definition 3.6.6 — Tautologies and Contradictions over a Universe.**

> A proposition over \(U\) is a tautology if its truth set is \(U\text{.}\) It is a contradiction if its truth set is empty.

> **Example 3.6.7 — Tautology, Contradiction over \(\mathbb{Q}\) .**

> \((s - 1)(s + 1) = s^2 - 1\) is a tautology over the rational numbers. \(x^2-2 = 0\) is a contradiction over the rationals.

The truth sets of compound propositions can be expressed in terms of the truth sets of simple propositions. For example, if \(a \in  T_{p\land q}\) if and only if \(a\) makes \(p \land  q\) true. This is true if and only if  \(a\) makes both \(p\) and \(q\) true,  which, in turn, is true if and only if  \(a \in  T_p\cap T_q\text{.}\) This explains why the truth set of the conjunction of two propositions equals the intersection of the truth sets of the two propositions. The following list summarizes the connection between compound and simple truth sets

![Table 3.6.8 . Truth Sets of Compound Statements \(T_{p\land q}=T_p\cap T_q\) \(T_{p\lor q}=T_p\cup T_q\) \(T_{\neg p}=T_p{}^c\) \(T_{p\leftrightarrow q}=\left(T_p\cap T_q\right)\cup \left(T_p{}^c\cap T_q{}^c\right)\) \(T_{p\to q}=T_p{}^c\cup T_q\)]()

> **Definition 3.6.9 — Equivalence of propositions over a universe.**

> Two propositions, \(p\) and \(q\text{,}\) are equivalent if \(p \leftrightarrow  q\) is a tautology. In terms of truth sets, this means that \(p\) and \(q\) are equivalent if \(T_p=T_q\) .

> **Example 3.6.10 — Some pairs of equivalent propositions.**

> \(n + 4 = 9\) and \(n = 5\) are equivalent propositions over the integers.
> 
> \(A \cap  \{4\} \neq  \emptyset\) and \(4 \in  A\) are equivalent propositions over the power set of the natural numbers.

> **Definition 3.6.11 — Implication for propositions over a universe.**

> If \(p\) and \(q\) are propositions over \(U\text{,}\) \(p\) implies \(q\) if \(p \rightarrow q\) is a tautology.

Since the truth set of \(p \rightarrow  q\) is \(T_p{}^c\cup T_q\text{,}\) the Venn diagram for \(T_{p\to q}\) in [Figure 12 [UNRESOLVED_INTERNAL_LINK]](s-propositions-over-universe.html#venn_diagram_truth_set_conditional) shows that \(p \Rightarrow  q\) when \(T_p\subseteq T_q\text{.}\)

![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/sageplot-venn-truth-set-conditional.svg)

> **Example 3.6.13 — Examples of Implications.**

> Over the natural numbers: \(n \leq 4 \Rightarrow  n \leq 8\) since \(\{0, 1, 2, 3, 4\} \subseteq  \{0, 1, 2, 3, 4, 5, 6, 7, 8\}\)
> 
> Over the power set of the integers: \(\lvert A^c \rvert=1\) implies \(A\cap \{0,1\}\neq \emptyset\)
> 
> Over the power set of the integers,  \(A \subseteq  \textrm{ even integers } \Rightarrow  A\cap  \textrm{ odd integers } =\emptyset\)

> **Exercise 1 . —**

> If \(U = \mathcal{P}( \{1, 2, 3, 4\})\text{,}\) what are the truth sets of the following propositions?

> \(A \cap  \{2, 4\} = \emptyset\text{.}\)
> 
> \(3 \in  A\) and \(1 \notin  A\text{.}\)
> 
> \(A \cup  \{1\} = A\text{.}\)
> 
> \(A\) is a proper subset of \(\{2, 3, 4\}\text{.}\)
> 
> \(\lvert A \rvert=\lvert A^c \rvert\text{.}\)

> **Exercise 2 . —**

> Over the universe of positive integers, define

> ![Table 3.6.14 . \(p(n)\text{:}\) \(n\) is prime and \(n < 32\text{.}\) \(q(n)\text{:}\) \(n\) is a power of 3. \(r(n)\text{:}\) \(n\) is a divisor of 27.]()

> What are the truth sets of these propositions?
> Which of the three propositions implies one of the others?

> **Exercise 3 . —**

> If \(U = \{0, 1, 2\}\text{,}\) how many propositions over \(U\) could you list without listing two that are equivalent?

> **Exercise 4 . —**

> Given the propositions over the natural numbers:

> ![Table 3.6.15 . \(p : n < 4\text{,}\) \(q : 2n > 17\text{,}\) and \(r : n \textrm{ is a divisor of } 18\)]()

> What are the truth sets of:
> 
> \(\displaystyle q\)
> \(\displaystyle p\land q\)
> \(\displaystyle r\)
> \(\displaystyle q\to r\)

> **Exercise 5 . —**

> Suppose that \(s\) is a proposition over \(\{1, 2,\dots, 8\}\text{.}\) If \(T_s = \{1, 3, 5, 7\}\text{,}\) give two examples of propositions that are equivalent to \(s\text{.}\)

> **Exercise 6 . —**

> Determine the truth sets of the following propositions over the positive integers:
> 
> \begin{equation*}
> p(n) : n \textrm{ is a perfect square and }  n < 100
> \end{equation*}
> 
> 
> \begin{equation*}
> q(n) : n = \lvert \mathcal{P}(A) \rvert \textrm{ for some set } A\text{.}
> \end{equation*}
> 
> 
> Determine \(T_{p\land q}\) for \(p\) and \(q\) above.

> **Exercise 7 . —**

> Let the universe be \(\mathbb{Z}\text{,}\) the set of integers. Which of the following propositions are equivalent over \(\mathbb{Z}\text{?}\)

> ![Table 3.6.16 . \(a\text{:}\) \(0 < n^2 < 9\) \(b\text{:}\) \(0 < n^3 < 27\) \(c\text{:}\) \(0 < n < 3\)]()
