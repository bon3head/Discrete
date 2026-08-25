---
source_relative_path: "DM TXT/7-Functions_and_Probability/ads Binomial Processes.html"
source_sha256: "39d60a237ff2107257432bc9cb01e421c47c6d6422e9044855af709a4fe0474d"
scope_class: active_candidate
displayed_section_or_chapter: "Section 7.5 Binomial Processes"
content_gap: true
missing_assets:
  - "external/images/fig-bsc-example.png"
---

# Section 7.5 Binomial Processes

In this section we will concentrate of random processes that will involve one or more identical random experiments with two possible outcomes. The simplest such example would be one or more flips of a coin. Let’s jump into the formal definitions and then we’ll look at a few examples.

# Subsection 7.5.1 Basic Theory

> **Definition 7.5.1 — Binomial Trial.**

> A binomial trial is an experiment with a sample space having two elements \(\{\textrm{success},\textrm{failure}\}\) with probability distribution \(Pr(\textrm{success})=p\) and \(Pr(\textrm{failure}))=1-p\) for some real number \(p\text{,}\) \(0 \lt p \lt 1\text{.}\)

It is customary to use \(\{\textrm{success},\textrm{failure}\}\) as the generic sample space for a binomial trial, but in practice the sample space can be any set of cardinality two.

A fair coin flip is a binomial trial with \(p=1/2\text{.}\) If we roll a six sided die and interpret success as whether a six is rolled, this is a binomial trial with \(p=1/6\text{.}\)

A basketball player shooting a free throw, with success being whether they make the free thow, is probably not a binomial trial because the probability of success is not likely to be constant. Factors such as fatigue and game pressure are likely to change the probablity of success. However, we can think of free throw shooting as a binomial process as long as we understand that it is an approximation of reality.

In reality, each free throw can have some effect on the next free throw. We say that each free throw is not necessarily independent of previous ones. Independence is an important assumption when we define a binomial process. Intuitively, conditions associated with an experiment are independent if the likelihood of one does not affect the likelihood of the other. The formal definition follows and gives a precise condition.

> **Definition 7.5.2 —**

> Two logical conditions associated with a random experiment, \(A\) and \(B\text{,}\) are independent if
> 
> \begin{equation*}
> Pr(A \land B) = Pr(A) \cdot Pr(B)
> \end{equation*}

> **Definition 7.5.3 — Finite Binomial Process.**

> A finite *binomial process* is a sequence of identical independent Bernoulli trials \(X_1\text{,}\) \(X_2\text{,}\) \(X_3\text{,}\) \(\dots\text{,}\) \(X_n\) with probability of success \(p\text{.}\) We use the notation \(B(n,p)\) for an \(n\) step binomial process with probability of success \(p\text{.}\)

The probability of any number of successes in a finite binomial process is fairly easy to derive. Instead of a general proof, we will derive one specific probability for a \(B(6,p)\) and the correctness of the general formula should be clear from our logic. Let’s look at the probability of exactly four successes. If we were to record the outcome of six independent trials, writing S for success and F for failure, there as several ways in which we could observe four successes. One such case would be SFFSSS, and another is FSSSFS. The first these two occurred with probability \(p\cdot (1-p)\cdot (1-p)\cdot p\cdot p\cdot p\) while the second had probability \((1-p)\cdot p\cdot p\cdot p\cdot (1-p) \cdot p\text{.}\) But both of these products reduce to \(p^4 \cdot (1-p)^2\text{,}\) as do all of the other ways in which we can have four successes. The number of different orderings of four successes and two failures is \(\binom{6}{4}\text{;}\) think of how you have to select four positions in the sequence of six to get success. Therefore the probability of having four successes is

\begin{equation*}
\binom{6}{4}p^4 \cdot (1-p)^2\text{.}
\end{equation*}

We can generalize this result to give us a formula for \(k\) successes in a \(B(n,p)\text{.}\)

> **Theorem 7.5.4 — Binomial Process Probabilities.**

> Given a finite *binomial process,* \(B(n,p)\text{,}\) the probability of exactly \(k\) successes, \(0\leq k \leq n\) is
> 
> \begin{equation*}
> \binom{n}{k}p^k \cdot (1-p)^{n-k}\text{.}
> \end{equation*}

What follows isn’t a proof of the theorem above, but it should make it’s correctness even more convincing. We know that in a \(B(n,p)\) there must be anywhere from 0 to \(n\) successes. So let’s add the probabilities we’ve observed. The numbers of possible successes are mutually exclusive - you can’t get more than one of them to occur. So we should get a sum equal to \(1\text{.}\)


\begin{equation*}
\sum_{k=0}^n \binom{n}{k}p^k \cdot (1-p)^{n-k}= (p + (1-p))^n = 1^n=1
\end{equation*}

> **Example 7.5.5 — A Series of Red Bets.**

> In the previous section, we’ve seen that a bet on Red in roulette is a binomial trial with probability of success \(\frac{9}{19}\text{.}\)  Suppose we plan to bet on Red nine consecutive times, each time for the same amount.  What is the probability that we win at least five times?  This is a \(B(9,\frac{9}{19})\) and so we can use the formula directly, adding the probabilities for five through nine wins.

> ```sage
> 
> ```

> If we quit after nine games, we will walk away winners around 44 percent of the time.

# Subsection 7.5.2 A Model for Noise

> **Example 7.5.6 — The Distribution of transmission errors.**

> A binary symmetric channel is an approximation of a form of noise that is often observed in a communication channel. As individual bits are transmitted, we assume that there is some fixed, usually very small, probability \(p\) that the value of the bit will switch, creating an error. If \(N\) bits are to be transmitted, this is a \(B(N,p)\) binomial process.

> Suppose that 1024 bits are to be transmitted across a binary symmetric channel with \(p=0.002\text{.}\) For any single bit, the likelihood of an error is quite small, but we can compute the probability of having any number of errors in the full transmission. If there are to be \(k\) errors, then the number positions of those errors among all of the bits is \(\binom{1024}{k}\text{.}\) The probability of any single error pattern is \((0.002)^k \cdot (0.998)^{1024-k}\text{.}\) The product
> 
> \begin{equation*}
> \binom{1024}{k} (0.002)^k \cdot (0.998)^{1024-k}
> \end{equation*}
> 
> is then the probability of exactly \(k\) transmission errors.

> Here is a plot of these probabilities for \(k \leq 6\)

> Notice that the probability that there is no error among all bits is approximately \(0.13\) and it is more likely that there are 1, 2 or 3 errors in the data that is received. These error could be costly and motivates the topic of *coding theory*.

> ![MISSING FIGURE: source figure](GAP:external/images/fig-bsc-example.png)

> **Exercise 1 . —**

> A basketball player has made \(85\) percent of her free throws so far this year.  Estimate the probability that she will miss the next two free throws she attempts.  What is the probability the she makes five consecutive free throws?

> **Exercise 2 . —**

> What is the probablity of less than two errors in transmitting eight bits on a binary symmetric channel with error probability \(p\text{?}\)

> **Exercise 3 . —**

> How long does a sequence of random digits need to be so that the probability that a 6 had appeared is at least 2/3?

> **Exercise 4 . —**

> A bridge hand consists of 13 randomly dealt cards from a standard deck that contains four aces.   What is the probability that a bridge player does not get dealt an ace in four consecutive hands?

> **Exercise 5 . —**

> Teams A and B compete in a best of seven series of games.  The outcomes are independent and A has a probability of \(\frac{3}{5}\) of winning any single game.  What is the probability that the series lasts seven games, no matter who wins the series?
