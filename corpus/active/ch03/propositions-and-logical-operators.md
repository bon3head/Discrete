---
source_relative_path: "DM TXT/3-Logic/ads Propositions and Logical Operators.html"
source_sha256: "cecb87407130d065b15e7d94bddeba4876b63fdd8e100462c3aa74f8743e7427"
scope_class: active_candidate
displayed_section_or_chapter: "Section 3.1 Propositions and Logical Operators"
---

# Section 3.1 Propositions and Logical Operators

# Subsection 3.1.1 Propositions

> **Definition 3.1.1 — Proposition.**

> A proposition is a sentence to which one and only one of the terms *true* or *false* can be meaningfully applied.

> **Example 3.1.2 — Some Propositions.**

> “Four is even,”, “\(4 \in  \{1,3, 5\}\)” and “\(43 > 21\)” are propositions.

In traditional logic, a declarative statement with a definite truth value is considered a proposition. Although our ultimate aim is to discuss mathematical logic, we won’t separate ourselves completely from the traditional setting. This is natural because the basic assumptions, or postulates, of mathematical logic are modeled after the logic we use in everyday life. Since compound sentences are frequently used in everyday speech, we expect that logical propositions contain connectives like the word “and.” The statement “Europa supports life or Mars supports life” is a proposition and, hence, must have a definite truth value. Whatever that truth value is, it should be the same as the truth value of “Mars supports life or Europa supports life.”

# Subsection 3.1.2 Logical Operations

There are several ways in which we commonly combine simple statements into compound ones. The words/phrases *and*, *or*, *not*, *if ... then...*, and *...if and only if ...* can be added to one or more propositions to create a new proposition. To avoid any confusion, we will precisely define each one’s meaning and introduce its standard symbol.  With the exception of negation (*not*), all of the operations act on pairs of propositions. Since each proposition has two possible truth values, there are four ways that truth can be assigned to two propositions. In defining the effect that a logical operation has on two propositions, the result must be specified for all four cases. The most convenient way of doing this is with a truth table, which we will illustrate by defining the word *and*.

> **Definition 3.1.3 — Logical Conjunction.**

> If \(p\) and \(q\) are propositions, their conjunction, \(p \textrm{ and } q\) (denoted \(p \land q\)), is defined by the truth table
> 
> \begin{equation*}
> \begin{array}{ccc}
> p & q & p\land q \\
> \hline
> 0 & 0 & 0 \\
> 0 & 1 & 0 \\
> 1 & 0 & 0 \\
> 1 & 1 & 1 \\
> \end{array}
> \end{equation*}

Notes:

The numbers 0 and 1 are used to denote false and true, respectively. This is consistent with the way that many programming languages treat logical, or Boolean, variables since a single bit, 0 or 1, can represent a truth value.  Many people use either False/True or F/T instead of 0/1 in truth table.  Although 0/1 usage seems to be in the minority, we prefer to use it in order make a connection with the binary representation of numbers, as pointed out below.
One notable case where False/True notation is used is in Sage, as can be seen in the following Sage cell.  Notice that Sage uses an ampersand for the conjunction symbol.


To read this truth table, you must realize that any one line represents a case: one possible set of truth values for \(p\) and \(q\text{.}\)

For each case, the symbol under \(p\) represents the truth value of \(p\text{.}\) The same is true for \(q\text{.}\) The symbol under \(p \land q\) represents its truth value for that case. For example, the second row of the truth table represents the case in which \(p\) is false, \(q\) is true, and the resulting truth value for \(p \land q\) is false. As in everyday speech, \(p \land q\) is true only when both propositions are true.
Just as the letters \(x\text{,}\) \(y\) and \(z\) are frequently used in algebra to represent numeric variables, \(p\text{,}\) \(q\) and \(r\) seem to be the most commonly used symbols for logical variables. When we say that \(p\) is a logical variable, we mean that any proposition can take the place of \(p\text{.}\)

One final comment: The order in which we list the cases in a truth table is standardized in this book. If the truth table involves two simple propositions, the numbers under the simple propositions can be interpreted as the two-digit binary integers in increasing order, 00, 01, 10, and 11, for 0, 1, 2, and 3, respectively.

> **Definition 3.1.4 — Logical Disjunction.**

> If \(p\) and \(q\) are propositions, their disjunction, \(p \textrm{ or } q\) (denoted \(p \lor q\)), is defined by the truth table
> 
> \begin{equation*}
> \begin{array}{ccc}
> p & q & p\lor q \\
> \hline
> 0 & 0 & 0 \\
> 0 & 1 & 1 \\
> 1 & 0 & 1 \\
> 1 & 1 & 1 \\
> \end{array}
> \end{equation*}

> **Definition 3.1.5 — Logical Negation.**

> If \(p\) is a proposition, its negation, \(\textrm{not } p\text{,}\)  denoted \(\neg p\text{,}\) and is defined by the truth table
> 
> \begin{equation*}
> \begin{array}{cc}
> p & \neg p \\
> \hline
> 0 & 1 \\
> 1 & 0 \\
> \end{array}
> \end{equation*}

Note: Negation is the only standard operator that acts on a single proposition; hence only two cases are needed.

Consider the following propositions from everyday speech:

I’m going to quit if I don’t get a raise.
If I pass the final, then I’ll graduate.
I’ll be going to the movies provided that my car starts.

All three propositions are conditional, they can all be restated to fit into the form  “If *Condition*, then *Conclusion*.” For example, the first statement can be rewritten as “If I don’t get a raise, then I’m going to quit.”

A conditional statement is meant to be interpreted as a guarantee; if the condition is true, then the conclusion is expected to be true. It says no more and no less.

> **Definition 3.1.6 — Conditional Statement.**

> The conditional statement “If \(p\) then \(q\text{,}\)” denoted \(p \rightarrow  q\text{,}\) is defined by the truth table

> ![Table 3.1.7 . Truth Table for \(p \rightarrow q\) \(p\) \(q\) \(p \rightarrow q \) 0 0 1 0 1 1 1 0 0 1 1 1]()

> **Example 3.1.8 — Analysis of a Conditional Proposition.**

> Assume your instructor told you “If you receive a grade of 95 or better in the final examination, then you will receive an A in this course.” Your instructor has made a promise to you. If you fulfill his condition, you expect the conclusion (getting an A) to be forthcoming. Suppose your graded final has been returned to you. Has your instructor told the truth or is your instructor guilty of a falsehood?

> Case I: Your final exam score was less than 95 (the condition is false) and you did not receive an A (the conclusion is false). The instructor told the truth.

> Case II: Your final exam score was less than 95, yet you received an A for the course. The instructor told the truth. (Perhaps your overall course average was excellent.)

> Case III: Your final exam score was greater than 95, but you did not receive an A. The instructor lied.

> Case IV: Your final exam score was greater than 95, and you received an A. The instructor told the truth.

> To sum up, the only case in which a conditional proposition is false is when the condition is true and the conclusion is false.

The order of the condition and conclusion in a conditional proposition is important. If the condition and conclusion are exchanged, a different proposition is produced.

> **Definition 3.1.9 — Converse.**

> The converse of the proposition \(p \rightarrow q\) is the proposition \(q \rightarrow p\text{.}\)

The converse of “If you receive a grade of 95 or better in the final exam, then you will receive an A in this course,” is “If you receive an A in this course, then you received a grade of 95 or better in the final exam.” It should be clear that these two statements say different things.

There *is* a proposition related to \(p \rightarrow q\) that does have the same logical meaning.  This is the contrapositive.

> **Definition 3.1.10 — Contrapositive.**

> The contrapositive of the proposition \(p \rightarrow q\) is the proposition \(\neg q \rightarrow \neg p\text{.}\)

As we will see when we discuss logical proofs, we can prove a conditional proposition by proving its contrapositive, which may be somewhat easier.

Finally, there is a third variation on the proposition \(p \rightarrow q\text{,}\) the inverse, which we will see that has the same logical meaning as the converse.

> **Definition 3.1.11 — Logical Inverse.**

> The inverse of the proposition \(p \rightarrow q\) is the proposition \(\neg p \rightarrow \neg q\text{.}\)

The inverse of “If it snows today, we have a day off.”  would be “If it doesn’t snow today, we don’t have a day off.”  Can you see that the original proposition and the inverse are saying different things?

Our final logical operator is a conjunction of two conditionals

> **Definition 3.1.12 — Biconditional Proposition.**

> If \(p\) and \(q\) are propositions, the biconditional statement “\(p\) if and only if \(q\text{,}\)” denoted \(p \leftrightarrow q\text{,}\) is defined by the truth table
> 
> \begin{equation*}
> \begin{array}{ccc}
> p & q & p\leftrightarrow q \\
> \hline
> 0 & 0 & 1 \\
> 0 & 1 & 0 \\
> 1 & 0 & 0 \\
> 1 & 1 & 1 \\
> \end{array}
> \end{equation*}

Note that \(p \leftrightarrow q\) is true when \(p\) and \(q\) have the same truth values. It is common to abbreviate “if and only if” to “iff.”

Although “if ... then...” and “...if and only if ...” are frequently used in everyday speech, there are several alternate forms that you should be aware of. They are summarized in the following lists.

All of the following are equivalent to “If \(p\) then \(q\)”:

\(p\) implies \(q\text{.}\)


\(q\) follows from \(p\text{.}\)


\(p\text{,}\) only if \(q\text{.}\)


\(q\text{,}\) if \(p\text{.}\)


\(p\) is sufficient for \(q\text{.}\)


\(q\) is necessary for \(p\text{.}\)

All of the following are equivalent to “\(p\) if and only if \(q\)”:

\(p\) is necessary and sufficient for \(q\text{.}\)


\(p\) is equivalent to \(q\text{.}\)

If \(p\text{,}\) then \(q\text{,}\) and if \(q\text{,}\) then \(p\text{.}\)

If \(p\text{,}\) then \(q\) and conversely.

> **Exercise 1 . —**

> Let \(d\) = “I like discrete structures”, \(c\) = “I will pass this course” and \(s\) = “I will do my assignments.”  Express each of the following propositions in symbolic form:

> I like discrete structures and I will pass this course.
> I will do my assignments or I will not pass this course.
> It is not true that I both like discrete structures, and will do my assignments.
> I will not do my assignment and I will not pass this course.

> **Exercise 2 . —**

> For each of the following propositions, identify simple propositions, express the compound proposition in symbolic form, and determine whether it is true or false:

> The world is flat or zero is an even integer.
> If 432,802 is a multiple of 4, then 432,802 is even.
> 5 is a prime number and 6 is not divisible by 4.
> 
> \(3 \in \mathbb{Z}\) and \(3 \in  \mathbb{Q}\text{.}\)
> 
> 
> \(2/3 \in  \mathbb{Z}\) and \(2/3 \in  \mathbb{Q}\text{.}\)
> 
> The sum of two even integers is even and the sum of two odd integers is odd.

> **Exercise 3 . —**

> Let \(p =\)“\(2 \leq 5\)”, \(q\) = “8 is an even integer,” and \(r\) = “11 is a prime number.” Express the following as a statement in English and determine whether the statement is true or false:

> \(\displaystyle \neg  p \land  q\)
> \(\displaystyle p\rightarrow q\)
> \(\displaystyle (p \land q)\to r\)
> \(\displaystyle p \rightarrow (q \lor  (\neg r))\)
> \(\displaystyle p \rightarrow ((\neg q)\lor  (\neg r))\)
> \(\displaystyle (\neg q) \rightarrow  (\neg p)\)

> **Exercise 4 . —**

> Rewrite each of the following statements using the other conditional forms:

> It is sufficient for an integer to be even that it is a multiple of four.
> The fact that a polygon is a square is a sufficient condition that it is a rectangle.
> If \(x = 5\text{,}\) then \(x^2=25\text{.}\)
> 
> If \(x^2 - 5x + 6 = 0\text{,}\) then \(x = 2\) or \(x = 3\text{.}\)
> 
> 
> \(x^2=y^2\) is a necessary condition for \(x = y\text{.}\)

> **Exercise 5 . —**

> Write the converse of the propositions in exercise 4. Compare the truth of each proposition and its converse.
