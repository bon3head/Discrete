---
source_relative_path: "DM TXT/1-Set-Theory/ads Summation Notation and Generalizations.html"
source_sha256: "1e543d78aed518c0e222207247643fa167f8cf28bb68385ed8ce4a44d7fd18ab"
scope_class: active_candidate
displayed_section_or_chapter: "Section 1.5 Summation Notation and Generalizations"
---

# Section 1.5 Summation Notation and Generalizations

# Subsection 1.5.1 Sums

Most operations such as addition of numbers are introduced as binary operations. That is, we are taught that two numbers may be added together to give us a single number. Before long, we run into situations where more than two numbers are to be added. For example, if four numbers, \(a_1\text{,}\) \(a_2\text{,}\) \(a_3\text{,}\) and \(a_4\) are to be added, their sum may be written down in several ways, such as\(\) \(((a_1+a_2)+a_3)+a_4\) or \(\left(a_1+a_2\right)+\left(a_3+a_4\right)\text{.}\) In the first expression, the first two numbers are added, the result is added to the third number, and that result is added to the fourth number. In the second expression the first two numbers and the last two numbers are added and the results of these additions are added. Of course, we know that the final results will be the same. This is due to the fact that addition of numbers is an associative operation. For such operations, there is no need to describe how more than two objects will be operated on. A sum of numbers such as \(a_1+a_2+a_3+a_4\) is called a series and is often written \(\sum_{k=1}^4 a_k\) in what is called *summation notation*.

We first recall some basic facts about series that you probably have seen before. A more formal treatment of sequences and series is covered in Chapter 8. The purpose here is to give the reader a working knowledge of summation notation and to carry this notation through to intersection and union of sets and other mathematical operations.

A *finite series* is an expression such as \(a_1+a_2+a_3 +\dots +a_n=\sum_{k=1}^{n} a_k\)

In the expression \(\sum_{k=1}^{n} a_k\text{:}\)

The variable \(k\) is referred to as the *index*, or the index of summation.
The expression \(a_k\) is the *general term* of the series. It defines the numbers that are being added together in the series.
The value of \(k\) below the summation symbol is the *initial index* and the value above the summation symbol is the *terminal index*.
It is understood that the series is a sum of the general terms where the index starts with the initial index and increases by one up to and including the terminal index.

> **Example 1.5.1 — Some finite series.**

> \(\displaystyle \sum_{i=1}^4 a_i= a_1+ a_2+a_3+a_4\)
> \(\displaystyle \sum_{k=0}^5 b_k=b_0+b_1+b_2+b_3+b_4+b_5\)
> \(\displaystyle \sum_{i=-2}^2 c_i=c_{-2}+c_{-1}+c_0+c_1+c_2\)

> **Example 1.5.2 — More finite series.**

> If the general terms in a series are more specific, the sum can often be simplified. For example,

> \(\displaystyle \sum_{i=1}^4 i^2=1^2+2^2+3^2+4^2=30\)
> 
> \begin{equation*}
> \begin{split}
> \sum_{i=1}^5 (2i-1)&=(2\cdot 1-1)+(2\cdot 2-1)+(2\cdot 3-1)+(2\cdot 4-1)+(2\cdot 5-1)\\
> & =1+3+5+7+9\\
> & =25\\
> \end{split}\text{.}
> \end{equation*}

# Subsection 1.5.2 Generalizations

Summation notation can be generalized to many mathematical operations, for example, \(A_1\cap A_2\cap A_3\cap A_4=\underset{i=1}{\overset{4}{\cap }}A_i\)

> **Definition 1.5.3 — Generalized Set Operations.**

> Let \(A_1, A_2, \ldots , A_n\) be sets. Then:

> \(\displaystyle A_1\cap A_2\cap \cdots \cap A_n=\underset{i=1}{\overset{n}{\cap }}A_i\)
> \(\displaystyle A_1\cup A_2\cup \cdots \cup A_n=\underset{i=1}{\overset{n}{\cup }}A_i\)
> \(\displaystyle A_1\times A_2\times \cdots \times A_n=\underset{i=1}{\overset{n}{\times }}A_i\)
> \(\displaystyle A_1\oplus A_2\oplus \cdots \oplus A_n=\underset{i=1}{\overset{n}{\oplus }}A_i\)

> **Example 1.5.4 — Some generalized operations.**

> If \(A_1 = \{0, 2, 3\}\text{,}\) \(A_2 = \{1, 2, 3, 6\}\text{,}\) and \(A_3 = \{-1, 0, 3, 9\}\text{,}\) then
> 
> \begin{equation*}
> \underset{i=1}{\overset{3}{\cap }}A_i=A_1\cap A_2\cap A_3=\{3\}
> \end{equation*}
> 
> and
> 
> \begin{equation*}
> \underset{i=1}{\overset{3}{\cup }}A_i=A_1\cup A_2\cup A_3=\{-1,0,1,2,3,6,9\}\text{.}
> \end{equation*}
> 
> With this notation it is quite easy to write lengthy expressions in a fairly compact form. For example, the statement
> 
> \begin{equation*}
> A\cap \left(B_1\cup B_2\cup \cdots \cup B_n\right)= \left(A\cap B_1\right)\cup \left(A\cap B_2\right)\cup \cdots \cup \left(A\cap
> B_n\right)
> \end{equation*}
> 
> becomes
> 
> \begin{equation*}
> A \cap \left(\underset{i=1}{\overset{n}{\cup }}B_i\right)= \underset{i=1}{\overset{n}{\cup }}\left(A\cap B_i\right)\text{.}
> \end{equation*}

> **Exercise 1 . —**

> Calculate the following series:

> \(\displaystyle \sum_{i=1}^3 (2 + 3i)\)
> \(\displaystyle \sum_{i=-2}^1 i^2\)
> 
> \(\sum_{j=0}^n 2^j\text{   }\) for \(n= 1, 2, 3, 4\)
> 
> 
> \(\sum_{k=1}^n (2k-1)\) for \(n = 1, 2, 3, 4\)

> **Exercise 2 . —**

> Calculate the following series:

> \(\sum_{k=1}^3 k^n\) for \(n = 1, 2, 3, 4\)
> 
> \(\displaystyle \sum_{i=1}^5 20\)
> 
> \(\sum_{j=0}^3 \left(n^j+1\right)\) for \(n = 1, 2, 3,4\)
> 
> 
> \(\sum_{k=-n}^n k\) for \(n = 1, 2, 3, 4\)

> **Exercise 3 . —**

> Express the formula \(\sum_{i=1}^n \frac{1}{i(i+1)}= \frac{n}{n+1}\)  without using summation notation.
> Verify this formula for \(n=3\text{.}\)
> 
> Repeat parts (a) and (b) for \(\sum_{i=1}^n i^3=\frac{n^2(n+1)^2}{4}\)

> **Exercise 4 . —**

> Verify the following properties for \(n = 3\text{.}\)

> \(\displaystyle \sum_{i=1}^n \left(a_i+ b_i\right) =\sum_{i=1}^n a_i +\sum_{i=1}^n  b_i\)
> \(\displaystyle c\left(\sum_{i=1}^n a_i\right) = \sum_{i=1}^n c a_i\)

> **Exercise 5 . —**

> Rewrite the following without summation sign for \(n = 3\text{.}\) It is not necessary that you understand or expand the notation \(\left(
> \begin{array}{c}
> n \\
> k \\
> \end{array}
> \right)\) at this point. \((x + y)^n= \sum_{k=0}^n \left(
> \begin{array}{c}
> n \\
> k \\
> \end{array}
> \right)x^{n-k}y^k\text{.}\)

> **Exercise 6 . —**

> Draw the Venn diagram for \(\underset{i=1}{\overset{3}{\cap }}A_i\text{.}\)
> 
> Express in “expanded format”: \(A\cup (\underset{i=1}{\overset{n}{\cap }}B_i)= \underset{i=1}{\overset{n}{\cap }}(A \cup B_i)\text{.}\)

> **Exercise 7 . —**

> For any positive integer \(k\text{,}\) let \(A_k = \{x \in \mathbb{Q}:k-1 < x \leq k\}\) and \(B_k = \{x \in \mathbb{Q}: -k < x < k\}\text{.}\) What are the following sets?

> \(\displaystyle \underset{i=1}{\overset{5}{\cup }}A_i\)
> \(\displaystyle \underset{i=1}{\overset{5}{\cup }}B_i\)
> \(\displaystyle \underset{i=1}{\overset{5}{\cap }}A_i\)
> \(\displaystyle \underset{i=1}{\overset{5}{\cap }}B_i\)

> **Exercise 8 . —**

> For any positive integer \(k\text{,}\) let \(A_k = \{x \in \mathbb{Q}:\text0 < x < 1/k\}\) and \(B _k = \{x \in \mathbb{Q}:\,0 < x < k\}\text{.}\) What are the following sets?

> \(\displaystyle \underset{i=1}{\overset{\infty }{\cup }}A_i\)
> \(\displaystyle \underset{i=1}{\overset{\infty }{\cup }}B_i\)
> \(\displaystyle \underset{i=1}{\overset{\infty }{\cap }}A_i\)
> \(\displaystyle \underset{i=1}{\overset{\infty }{\cap }}B_i\)

> **Exercise 9 . —**

> The symbol \(\Pi\) is used for the product of numbers in the same way that \(\Sigma\) is used for sums. For example, \(\prod _{i=1}^5 x_i=x_1 x_2 x_3 x_4 x_5\text{.}\) Evaluate the following:

> \(\displaystyle \prod _{i=1}^3 i^2\)
> \(\displaystyle \prod _{i=1}^3 (2i+1)\)

> **Exercise 10 . —**

> Evaluate

> \(\displaystyle \prod _{k=0}^3 2^k\)
> \(\displaystyle \prod _{k=1}^{100} \frac{k}{k+1}\)
