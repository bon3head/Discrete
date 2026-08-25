---
source_relative_path: "DM TXT/2-Combinatorics/ads Combinations and the Binomial Theorem.html"
source_sha256: "7bc2fbc10bb557a8eacddd432ba4f7279c9fb0565f03579b3954cb0d60f2a7b2"
scope_class: active_candidate
displayed_section_or_chapter: "Section 2.4 Combinations and the Binomial Theorem"
content_gap: true
missing_assets:
  - "external/images/fig-lattice-path-6.png"
---

# Section 2.4 Combinations and the Binomial Theorem

# Subsection 2.4.1 Combinations

In Section 2.1 we investigated the most basic concept in combinatorics, namely, the rule of products. It is of paramount importance to keep this fundamental rule in mind. In Section 2.2 we saw a subclass of rule-of-products problems, permutations, and we derived a formula as a computational aid to assist us. In this section we will investigate another counting formula, one that is used to count combinations, which are subsets of a certain size.

In many rule-of-products applications the ordering is important, such as the batting order of a baseball team. In other cases it is not important, as in placing coins in a vending machine or in the listing of the elements of a set. Order is important in permutations. Order is not important in combinations.

> **Example 2.4.1 — Counting Permutations.**

> How many different ways are there to permute three letters from the set \(A = \{a, b, c, d\}\text{?}\)  From the [Permutation Counting Formula [UNRESOLVED_INTERNAL_LINK]](s-permutations.html#permutations-counting-formula) there are \(P(4,3)=\frac{4!}{(4-3)!} = 24\) different orderings of three letters from \(A\)

> **Example 2.4.2 — Counting with No Order.**

> How many ways can we select a set of three letters from  \(A = \{a, b, c, d\}\text{?}\)  Note here that we are not concerned with the order of the three letters. By trial and error, abc, abd, acd, and bcd are the only listings possible. To repeat, we were looking for all three-element subsets of the set \(A\text{.}\) Order is not important in sets. The notation for choosing 3 elements from 4 is most commonly \(\binom{4}{3}\) or occasionally \(C(4,3)\text{,}\) either of which is read “4 choose 3” or the number of combinations for four objects taken three at a time.

> **Definition 2.4.3 — Binomial Coefficient.**

> Let \(n\) and \(k\) be nonnegative integers.  The binomial coefficient \(\binom{n}{k}\) represents the number of combinations of \(n\) objects taken \(k\) at a time, and is read “\(n\) choose \(k\text{.}\)”

We would now like to investigate the relationship between permutation and combination problems in order to derive a formula for \(\binom{n}{k}\)

Let us reconsider the [Counting with No Order [UNRESOLVED_INTERNAL_LINK]](s-combinations-and-the-binomial-theorem.html#four-choose-three). There are \(3 ! = 6\) different orderings for each of the three-element subsets. The table below lists each subset of \(A\)  and all permutations of each subset on the same line.

\begin{equation*}
\begin{array}{cc}
\textrm{subset} & \textrm{permutations} \\
\{a, b, c\} & abc,acb,bca,bac,cab,cba \\
\{a, b, d\} & abd,adb,bda,bad,dab,dba \\
\{a, c, d\} & acd,adc,cda,cad,dac,dca \\
\{b, c, d\} & bcd,bdc,cdb,cbd,dbc,dcb \\
\end{array}\text{.}
\end{equation*}

Hence, \(\binom{4}{3} = \frac{P(4,3)}{3!} = \frac{4!}{(4-3)! \cdot 3!} = 4\)

We generalize this result in the following theorem:

> **Theorem 2.4.4 — Binomial Coefficient Formula.**

> If \(n\) and \(k\) are nonnegative integers with \(0 \leq k \leq n\text{,}\) then the number \(k\)-element subsets of an \(n\) element set is equal to
> 
> \begin{equation*}
> \binom{n}{k} = \frac{n!}{(n-k)! \cdot k!} \text{.}
> \end{equation*}

> **Example 2.4.5 — Flipping Coins.**

> Assume an evenly balanced coin is tossed five times. In how many ways can three heads be obtained? This is a combination problem, because the order in which the heads appear does not matter. We can think of this as a situation involving sets by considering the set of flips of the coin, 1 through 5, in which heads comes up.   The number of ways to get three heads is \(\binom{5}{3}= \frac{5 \cdot 4}{2 \cdot 1} = 10\text{.}\)

> **Example 2.4.6 — Counting five ordered flips two ways.**

> We determine the total number of ordered ways a fair coin can land if tossed five consecutive times. The five tosses can produce any one of the following mutually exclusive, disjoint events: 5 heads, 4 heads, 3 heads, 2 heads, 1 head, or 0 heads.  For example, by the previous example, there are \(\binom{5}{3}=10\) sequences in which three heads appear. Counting the other possibilities in the same way, by the law of addition we have:
> 
> \begin{equation*}
> \binom{5}{5}+\binom{5}{4}+\binom{5}{3}+\binom{5}{2}+\binom{5}{1}+\binom{5}{0}= 1 + 5 +10+10+5+1 = 32
> \end{equation*}
> 
> ways to observe the five flips.

> Of course, we could also have applied the extended rule of products, and since there are two possible outcomes for each of the five tosses, we have \(2^5 = 32\) ways.

You might think that counting something two ways is a waste of time but solving a problem two different ways often is instructive and leads to valuable insights. In this case, it suggests a general formula for the sum \(\sum_{k=0}^n \binom{n}{k}\text{.}\) In the case of \(n = 5\text{,}\) we get \(2^5\) so it is reasonable to expect that the general sum is \(2^n\text{,}\) and it is.  A logical argument to prove the general statement simply involves generalizing the previous example to \(n\) coin flips.

> **Example 2.4.7 — A Committee of Five.**

> A committee usually starts as an unstructured set of people selected from a larger membership. Therefore, a committee can be thought of as a combination. If a club of 25 members has a five-member social committee, there are \(\binom{25}{5}=\frac{25\cdot 24\cdot 23\cdot 22\cdot 21}{5!} = 53130\) different possible social committees. If any structure or restriction is placed on the way the social committee is to be selected, the number of possible committees will probably change. For example, if the club has a rule that the treasurer must be on the social committee, then the number of possibilities is reduced to \(\binom{24}{4}=\frac{24\cdot 23\cdot 22\cdot 21}{4!} = 10626\text{.}\)

> If we further require that a chairperson other than the treasurer be selected for the social committee, we have  \(\binom{24}{4} \cdot 4 = 42504\) different possible social committees. The choice of the four non-treasurers accounts for the factor \(\binom{24}{4}\) while the need to choose a chairperson accounts for the 4.

> **Example 2.4.8 — Binomial Coefficients - Extreme Cases.**

> By simply applying the definition of a [Binomial Coefficient [UNRESOLVED_INTERNAL_LINK]](s-combinations-and-the-binomial-theorem.html#binomial-coefficient) as a number of subsets we see that there is \(\binom{n}{0} = 1\) way of choosing a combination of zero elements from a set of \(n\text{.}\) In addition, we see that   there is \(\binom{n}{n} = 1\) way of choosing a combination of \(n\) elements from a set of \(n\text{.}\)

> We could compute these values using the formula we have developed, but no arithmetic is really needed here.  Other properties of binomial coefficients that can be derived using the subset definition will be seen in the exercises

# Subsection 2.4.2 The Binomial Theorem

The binomial theorem gives us a formula for expanding \(( x + y )^{n}\text{,}\) where \(n\)  is a nonnegative integer. The coefficients of this expansion are precisely the binomial coefficients that we have used to count combinations. Using high school algebra we can  expand the expression for integers from 0 to 5:

\begin{equation*}
\begin{array}{cc}
n & (x + y)^n \\
0 & 1 \\
1 & x+y \\
2 & x^2+2 x y+y^2 \\
3 & x^3+3 x^2 y+3 x y^2+y^3 \\
4 & x^4+4 x^3 y+6 x^2 y^2+4 x y^3+y^4
\\
5 & x^5+5 x^4 y+10 x^3 y^2+10 x^2
y^3+5 x y^4+y^5 \\
\end{array}
\end{equation*}

In the expansion of \((x + y)^{5} \)  we note that the coefficient of the third term is \(\binom{5}{3} = 10\text{,}\) and that of the sixth term is  \(\binom{5}{5}=1\text{.}\) We can rewrite the expansion as

\begin{equation*}
\binom{5}{0} x^5+\binom{5}{1} x^4 y+\binom{5}{2} x^3 y^2+\binom{5}{3} x^2 y^3+\binom{5}{4} x y^4+ \binom{5}{5} y^5\text{.}
\end{equation*}

In summary, in the expansion of \(( x + y )^{n}\) we note:

The first term is \(x^n\) and the last term is \(y^n\text{.}\)

With each successive term, exponents of \(x\) decrease by 1 as those of \(y\) increase by 1. For any term the sum of the exponents is \(n\text{.}\)

The coefficient of \(x^{n-k} y^k\) is \(\binom{n}{k}\text{.}\)

The triangular array of binomial coefficients is called Pascal’s triangle after the seventeenth-century French mathematician Blaise Pascal. Note that each number in the triangle other than the 1’s at the ends of each row is the sum of the two numbers to the right and left of it in the row above.

> **Theorem 2.4.9 — The Binomial Theorem.**

> If \(n \geq  0\text{,}\) and \(x\) and \(y\) are numbers, then
> 
> \begin{equation*}
> (x+y)^{n} = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k\text{.}
> \end{equation*}

> **Example 2.4.10 — Identifying a term in an expansion.**

> Find the third term in the expansion of \((x-y)^{4} = (x+(-y))^{4}\text{.}\) The third term,  when \(k=2\text{,}\) is \(\binom{4}{2} x^{4-2} (-y)^2 = 6 x^2 y^2\text{.}\)

> **Example 2.4.11 — A Binomial Expansion.**

> Expand \((3 x - 2 )^{3}\text{.}\)  If we replace \(x\)  and \(y\)  in the Binomial Theorem with \(3x\) and \(-2\text{,}\) respectively, we get
> 
> \begin{equation*}
> \begin{split} 
> \sum_{k=0}^3 \binom{3}{k} (3x)^{n-k} (-2)^k & = \binom{3}{0} (3x)^{3} (-2)^0 + \binom{3}{1} (3x)^{2} (-2)^1 + \binom{3}{2} (3x)^{1} (-2)^2 + \binom{3}{3} (3x)^{0} (-2)^3 \\
> & = 27 x^3 - 54 x^2 + 36 x - 8 
> \end{split}\text{.}
> \end{equation*}

# Subsection 2.4.3 SageMath Note

A bridge hand is a 13 element subset of a standard 52 card deck. The order in which the cards come to the player doesn’t matter. From the point of view of a single player, the number of possible bridge hands is \(\binom{52}{13}\text{,}\) which can be easily computed with \(Sage\text{.}\)

```sage

```

In bridge, the location of a hand in relation to the dealer has some bearing on the game. An even truer indication of the number of possible hands takes into account \(each\)  player’s possible hand. It is customary  to refer to bridge positions as West, North, East and South. We can apply the rule of product to get the total number of bridge hands with the following logic. West can get any of the \(\binom{52}{13}\) hands identified above. Then North get 13 of the remaining 39 cards and so has  \(\binom{39}{13}\) possible hands. East then gets 13 of the 26 remaining cards, which has \(\binom{26}{13}\)  possibilities. South gets the remaining cards. Therefore the number of bridge hands is computed using the Product Rule.

```sage

```

> **Exercise 1 . —**

> The judiciary committee at a college is made up of three faculty members and four students. If ten faculty members and 25 students have been nominated for the committee, how many judiciary committees could be formed at this point?

> **Exercise 2 . —**

> Suppose that a single character is stored in a computer using eight bits.

> a. How many bit patterns have exactly three 1’s?

> b. How many bit patterns have at least two 1’s?

> **Exercise 3 . —**

> How many subsets of \(\{1, 2, 3, \dots , 10\}\) contain at least seven elements?

> **Exercise 4 . —**

> The congressional committees on mathematics and computer science are made up of five representatives each, and a congressional rule is that the two committees must be disjoint. If there are 385 members of congress, how many ways could the committees be selected?

> **Exercise 5 . —**

> The image below shows a 6 by 6 grid and an example of a lattice path that could be taken from \((0,0)\)  to \((6,6)\text{,}\) which is a path taken by traveling along grid lines going only to the right and up. How many different lattice paths are there of this type?  Generalize to the case of lattice paths from \((0,0)\) to \((m,n)\)  for any nonnegative integers \(m\) and \(n\text{.}\)

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/fig-lattice-path-6.png)

> **Exercise 6 . —**

> How many of the lattice paths from \((0,0)\) to \((6,6)\) pass through \((3,3)\) as the one in [Figure 12 [UNRESOLVED_INTERNAL_LINK]](s-combinations-and-the-binomial-theorem.html#fig-lattice-path-6) does?
> How many the paths pass through \((2,3)\) but not necessarily \((3,3)\text{?}\)
> 
> How many the paths pass through \((2,3)\) and avoid \((3,3)\text{?}\)

> **Exercise 7 . —**

> A poker game is played with 52 cards.  At the start of a game, each player gets five of the cards.  The order in which cards are dealt doesn’t matter.
> 
> How many “hands” of five cards are possible?
> If there are four people playing, how many initial five-card “hands” are possible, taking into account all players and their positions at the table?  Position with respect to the dealer does matter.

> **Exercise 8 . —**

> A flush in a five-card poker hand is five cards of the same suit. The suits are spades, clubs, diamonds and hearts.  How many spade flushes are possible in a 52-card deck? How many flushes are possible in any suit?

> **Exercise 9 . —**

> How many five-card poker hands using 52 cards contain exactly two aces?

> **Exercise 10 . —**

> In poker, a full house is three-of-a-kind and a pair in one hand; for example, three fives and two queens. How many full houses are possible from a 52-card deck?  You can use the sage cell in the [SageMath Note [UNRESOLVED_INTERNAL_LINK]](s-combinations-and-the-binomial-theorem.html#sage-bridge-hands) to do this calculation, but also write your answer in terms of binomial coefficients.

> **Exercise 11 . —**

> A class of twelve computer science students are to be divided into three groups of 3, 4, and 5 students to work on a project. How many ways can this be done if every student is to be in exactly one group?

> **Exercise 12 . —**

> Explain in words why the following equalities are true based on number of subsets,  and then verify the equalities using the formula for binomial coefficients.

> \(\displaystyle \binom{n}{1} = n\)
> 
> \(\binom{n}{k} = \binom{n}{n-k}\text{,}\) \(0 \leq k \leq n\text{.}\)

> **Exercise 13 . —**

> There are ten points, \(P_1, P_2, \dots , P_{10}\) on a plane, no three on the same line.

> How many lines are determined by the points?
> How many triangles are determined by the points?

> **Exercise 14 . —**

> How many ways can \(n\)  persons be grouped into pairs when \(n\)  is even? Assume the order of the pairs matters, but not the order within the pairs. For example, if \(n=4\text{,}\) the six different groupings would be
> 
> \begin{equation*}
> \begin{array}{cc}
> \{1,2\} & \{3,4\} \\
> \{1,3\} & \{2,4\} \\
> \{1,4\} & \{2,3\} \\
> \{2,3\} & \{1,4\} \\
> \{2,4\} & \{1,3\} \\
> \{3,4\} & \{1,2\} \\
> \end{array}
> \end{equation*}

> **Exercise 15 . —**

> Use the binomial theorem to prove that if \(A\) is a finite set, then \(\lvert P(A)\rvert =2^{\lvert A  \rvert}\)

> **Exercise 16 . —**

> A state’s lottery involves choosing six different numbers out of a possible 36. How many ways can a person choose six numbers?
> What is the probability of a person winning with one bet?

> **Exercise 17 . —**

> Use the binomial theorem to calculate \(9998^3\text{.}\)

> **Exercise 18 . —**

> In the card game Blackjack, there are one or more players and a dealer.  Initially, each player is dealt two cards and the dealer is dealt one card down and one facing up.  As in bridge, the order of the hands, but not the order of the cards in the hands, matters.  Starting with a single 52 card deck, and three players, how many ways can the first two cards be dealt out?  You can use the sage cell in the [SageMath Note [UNRESOLVED_INTERNAL_LINK]](s-combinations-and-the-binomial-theorem.html#sage-bridge-hands) to do this calculation.
