---
source_relative_path: "DM TXT/7-Functions_and_Probability/ads Basic Notions of Probability.html"
source_sha256: "deca76bfe75c4e672bc1e0fcd6cc7b35eaffb401f39fa0af08f621e30f619b4b"
scope_class: active_candidate
displayed_section_or_chapter: "Section 7.4 Basic Notions of Probability"
---

# Section 7.4 Basic Notions of Probability

# Subsection 7.4.1 Probabilities and Expectations

Assume we are about to observe some process, which we call an experiment, and which will have an outcome that can be any one of a set of possible results. In this chapter will will assume that the set of possible results, which we call the sample space, is finite. The simplest example of this is the toss of a coin, where the sample space is \(\{heads, tails\}\text{.}\)

> **Definition 7.4.1 — Sample Space for a Random Experiment.**

> The sample space for a random experiment is the set of all possible outcomes of the experiment such that when the outcome is determined, exactly one of the elements of the sample space will have occured.

Before the experiment takes place, the outcome is uncertain. We assume that every element of the sample space is a possible outcome. Furthermore we assume that *exactly one* of the elements of the sample space will be the outcome. We may not know exactly which elements sample space are more likely than others, but we often make assumptions that seem reasonable. In the case of flipping a coin it is reasonable to assume that the two outcomes are equally likely. Of course there are “unfair” coins that are weighted so that one of the two outcomes is more likely. It may also occur to you that the coin could land on its edge, but this would tend to be so unlikely as to simply ignore it as a possible outcome, which is why we didn’t include it in the sample space.

Assuming a fair coin, we assign a probability to the two outcomes to reflect an assumption that before flipping the coin they equally likely. We assign a probability of \(1/2\) to both outcomes. In general, the probability of an outcome is a measurement of the the likelihood of that outcome occurring in an experiment.

> **Definition 7.4.2 — Probability Distribution.**

> Give an experiment with sample space \(S\text{,}\) a probability distribution on \(S\) is a function \(Pr:S\rightarrow \mathbb{R}\) such that
> 
> \(\displaystyle \forall s \in S, \quad Pr(s) \geq 0 \)
> \(\displaystyle \sum_{s \in S} Pr(s)=1\)

You might notice that we do allow for the possibility of an outcome to have zero probability, which would reflect a situation where that outcome is impossible. We might leave that outcome in the sample space if we are considering different experiments with the same sample space.

> **Definition 7.4.3 — Random Variable.**

> Given a random experiment with sample space \(S\text{,}\) a random variable is a function \(X:S \rightarrow \mathbb{R}\) that associates a real number to each outcome.

> **Example 7.4.4 —**

> Consider the roll of a pair of standard six sided dice.  The sample space for this experiment is a pair in the set \(S=\{(i,j) \mid  1 \leq i,j \leq 6 \}\text{.}\)  A natural random variable associated with this experiment would map the pair \((i,j)\) to \(i+j\text{.}\)  We might have thought of the sample space to be the possible sums that make up the range of the random variable, \(\{2, 3, \dots,11,12\}\text{,}\) but the advantage to using the ordered pairs as the sample space is that each pair has an identical probability of \(\frac{1}{36}\text{.}\)  This is a uniform distribution, which we will define precisely below.

In the case of a coin flip the probability distribution \(Pr(heads)=Pr(tails)=\frac{1}{2}\) is reasonable. However, in real life probabilities are often unknown, and we need to make estimates. For experiments that involve the playing a game between two teams we might assign probabilities of each team winning, we can never know the true likelihood of the outcome. These probabilities are subjective - everyone has a different sense of what the outcome of a game is likely to be. Nevertheless, subjective probabilities can be a tool in assessing whether an individual should place a wager on the outcome of game.

> **Example 7.4.5 — Logical Gambling.**

> A simple example might be a wager on a game - we use a US football game here as our model. Suppose a game between the Jets and Patriots is to take place and we are going to wager on the final outcome of the game. The sample space consisting of \(\{\textrm{Jets win},\textrm{Patriots win}, \textrm{tie}\}\text{.}\) An individual might assign a probability to each of the outcomes. Under current rules in the National Football League, ties are quite rare and so if the Patriots are assessed as being a somewhat better teams the following probability distribution might be assumed by that individual.

> \begin{equation*}
> Pr(\textrm{Jets win})=0.44
> \end{equation*}
> 
> 
> \begin{equation*}
> Pr(\textrm{Patriots win})=0.55
> \end{equation*}
> 
> 
> \begin{equation*}
> Pr(\textrm{tie})=0.01
> \end{equation*}

> It’s important to emphasize that unlike the flip of a coin, there is no physical basis on which these probabilities can be justified and each individual will have their own distribution.

> To a fan of the teams the outcome is important, but to someone who is wagering on the outcome there is another thing to consider, the amount that is won or lost based on the outcome of the game. This is an example of a random variable that we will call \(Gain\text{.}\) An example of how a wager could be structured if one if to bet \(\$100\) on the Patriots in the game is
> 
> \(\displaystyle Gain(\textrm{Patriots win})= \$88\)
> \(\displaystyle Gain(\textrm{tie})= -\$100\)
> \(\displaystyle Gain(\textrm{Jets win})= -\$100\)

> Notice that the gain of \(\$88\) if the Patriots win is less than the loss of \(\$100\) if the Jets win or there is tie. This reflects the fact that the individual’s probability assessment is likely to to be similar to that of individual who structures the bet. How does one decide whether to actually make this bet? The answer is the expected value of \(Gain\text{.}\) In this case the *assessed* expectation of \(Gain\) is
> 
> \begin{equation*}
> E(Gain)=\$88 \cdot  0.55 + (-\$100)\cdot 0.44 + (-\$100)\cdot 0.01=\$3.40 
> \end{equation*}
> 
> Our hypothetical individual with their assessment of the probabilities for this game would expect to win \(\$3.40\text{,}\) on average, when placing a bet like this. So they probably would do so. A different person who assesses the probability that the Patriots would win to be only \(0.51\) with the probability for the Jets being \(0.48\) and a probability of 0.01 for a tie would have an expected gain of
> 
> \begin{equation*}
> \$88 \cdot  0.51 + (-\$100)\cdot 0.48 + (-\$100)\cdot 0.01=-\$4.12
> \end{equation*}
> 
> This negative expected gain should dissuade them from making the bet.

In general, here is the formula for the expected value of a random variable.

> **Definition 7.4.6 — Expected Value of a Random Variable.**

> Given an experiment with sample space \(S\) having probability distribution \(Pr:S\rightarrow \mathbb{R}\text{,}\) let \(X\) be a random variable: \(X: S\rightarrow \mathbb{R}\text{.}\) The expected value of \(X\text{,}\) denoted \(E(X)\) is
> 
> \begin{equation*}
> E(X)=\sum_{s \in S} X(s) Pr(s)
> \end{equation*}

For some wagering the expected value is subjective, but in other situations it’s not. Take the case of the classic casino game roulette. Normally, the sample space in in a game of roulette has 38 elements, the numbers from 1 to 36 together with two special outcomes 0 and 00. Each possible outcome has a pocket on the edge of a spinning wheel. The outcome of any experiment is determined by a ball that lands in one of the pockets to determine the outcome. For a fair roulette wheel, the probability of each of the 38 elements of the sample space is 1/38. Half of the numbers 1 to 36 are colored red and the other half are black. The 0 and 00 are green. There are many different ways to place a bet but one is to bet that the outcome is a red number. Whatever amount a person bets, they win that amount if the outcome is red and lose the same amount otherwise. For example if we bet \(\$50\) on red, the probability of winning the bet and the expected value of the outcome of the bet are

\begin{equation*}
Pr(\textrm{red})=18*(1/38)=9/19=0.47 
\end{equation*}


\begin{equation*}
X(\textrm{red}) =18*(1/38)* (\$50) + 20*(1/38)( -\$50) =-\$2.63 
\end{equation*}

Unlike the case of betting on a football game, this roulette wager is repeatable with the probabilities being reasonably certain. This is an example of a binomial trial, which we will consider in detail later.

# Subsection 7.4.2 The Uniform Distribution

The roulette example illustrates one of the most basic types of experiments in probability theory where all of the elements of a sample space have equal probability. Here is a general description of how probabilities and expected values of random variables can be computed in this situation.

Let \(S\) be a finite sample space with cardinality \(n\) so that \(Pr(s)=1/n\) for all \(s \in S\text{.}\) Let \(q(s)\) be a proposition on \(S\) and let \(Pr(q(s))\) be the probability that the outcome of the experiment makes \(q(s)\) true. If \(T_{q(s)}\) is the truth set of \(q(s)\text{,}\) then \(Pr(q(s)) =\frac{\lvert T_{q(s)}\rvert}{n}\text{.}\)

To clarify this general rule, consider the wager in roulette that the outcome is a prime number. We have already established that the sample space has 38 equally likely outcomes. The proposition \(q(s)\) equal to “\(s\) is prime” has truth set \(\{2,3,5,7,11,13,17, 19,23,29,31\}\) which has cardinality 11. Therefore the probability \(Pr(s\textrm{ is prime}) = \frac{11}{38}\text{.}\) Although there are many standard bets in roulette, this one isn’t likely to be one. If it were, let’s consider what the payoff would need to be on a wager of \(\$100\) in order for the bet to be a fair one, where the expected value is zero. Let’s assume the payoff for winning is \(\$x\) with the payoff for losing being \(-\$100\text{.}\) The expected value of the payoff is then

\begin{equation*}
\$x(11/38) + (-\$100)(27/38) 
\end{equation*}

If we set this quantity to zero and solve for \(\$x\) we find the value \(\$245.45\text{.}\) Casinos are in the business of extracting money from their customers and so if this wager were to real, the payoff for winning might be something like \(\$200\text{,}\) or double a bet of \(\$100\text{.}\)

> **Theorem 7.4.7 — Probability Formulae For Uniform Distribution.**

> Based on formulas for the truth sets of compound propositions over a universe \(S\) with cardinality \(n\text{,}\) we can derive the following. If \(p(s)\) and \(q(s)\) are propositions over a sample space,
> 
> \begin{equation*}
> Pr(\neg p(s))= 1-Pr(p(s))
> \end{equation*}
> 
> 
> \begin{equation*}
> Pr(p(s) \land q(s)) = \frac{\lvert T_{p(s)} \cap T_{q(s)} \rvert}{n}
> \end{equation*}
> 
> 
> \begin{equation*}
> Pr(p(s) \lor q(s)) = \frac{\lvert T_{p(s)} \cup T_{q(s)} \rvert}{n}
> \end{equation*}

We can use the inclusion-exclusion for \(T_{p(s}) \cup T_{q(s)}\) to derive the following basic probability formula.

> **Corollary 7.4.8 —**

> If \(p(s)\) and \(q(s)\) are propositions over a sample space space \(S\text{,}\)
> 
> 
> \begin{equation*}
> Pr(p(s) \lor q(s))= Pr(p(s))+Pr(q(s))-Pr(p(s)\land q(s))
> \end{equation*}

> **Exercise 1 . —**

> Three fair coins are tossed up in the air, one at a time. What is the sample space for this experiment? What is the probability that two of them will land heads up and one will land tails up?

> **Exercise 2 . —**

> What is the expected value of wagering that the outcome in roulette is prime if you get a payoff of \(\$200\) for a \(\$100\) bet.

> **Exercise 3 . —**

> Your team is a favorite to win the big game and if you bet \(\$100\) on them and they win, you will get \(\$65\text{.}\) How high must the probability be that your team will win, in your assessment, in order for this bet to have a positive expected value? Assume there can be no tie possible for this game.

> **Exercise 4 . —**

> There are 8 blue marbles numbered 1 through 8, 3 red marbles numbered 1 through 3, and 6 yellow marbles numbered 1 through 6 in a bag. What is the probability that if one ball is drawn at random, it is red or even?

> **Exercise 5 . —**

> What is the probability that if you examine 8 random bits in your computer’s memory that there are exactly three ones and five zeros?

> **Exercise 6 . —**

> An experiment consists of rolling a standard six sided die with sides numbered 1 through 6. What is the expected value of the random variable \(X(k)=k^2-10\text{?}\)

> **Exercise 7 . —**

> A fair twelve sided die with faces numbered 1 through 12 is rolled once. What is the probability that the number that comes up is even or a prime?

> **Exercise 8 . —**

> Two six-sided dice are rolled. What is the probability that the sum of the numbers that come up is even or a prime?

> **Exercise 9 . —**

> Regarding the aside describing moneyline and point spread bets, gambling companies decide on a point spread and it’s not directly related to the probability of a team winning or losing. The spread is selected with the objective of luring as many betters to bet on one team as the other, balancing the bets so that equal amounts of money is bet on each team. The gambling company automatically profits based on a fee called vigorish, that skims off some of the winnings. How is the possibility of setting a balanced point spread related to the Intermediate Value Theorem in calculus?
