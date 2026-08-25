---
source_relative_path: "DM TXT/2-Combinatorics/ads Partitions of Sets and the Law of Addition.html"
source_sha256: "b1a26dc49dcff203466bf7cafba8904dd1320145f114d58f1768f01965eeb21d"
scope_class: active_candidate
displayed_section_or_chapter: "Section 2.3 Partitions of Sets and the Law of Addition"
content_gap: true
missing_assets:
  - "generated/sageplot/sageplot-venn-CS_Students.svg"
---

# Section 2.3 Partitions of Sets and the Law of Addition

# Subsection 2.3.1 Partitions

One way of counting the number of students in your class would be to count the number in each row and to add these totals. Of course this problem is simple because there are no duplications, no person is sitting in two different rows. The basic counting technique that you used involves an extremely important first step, namely that of partitioning a set. The concept of a partition must be clearly understood before we proceed further.

> **Definition 2.3.1 — Partition.**

> A partition of set \(A\) is a set of one or more nonempty subsets of \(A\text{:}\) \(A_1, A_2, A_3, \cdots\text{,}\) such that every element of \(A\) is in exactly one set.  Symbolically,

> \(\displaystyle A_1 \cup A_2 \cup A_3 \cup \cdots = A\)
> If  \(i \neq j\) then \(A_i \cap A_j = \emptyset\)

The subsets in a partition are often referred to as blocks. Note how our definition allows us to partition infinite sets, and to partition a set into an infinite number of subsets. Of course, if \(A\)  is finite the number of subsets can be no larger than \(\lvert A \rvert \text{.}\)

> **Example 2.3.2 — Some partitions of a four element set.**

> Let \(A = \{a, b, c, d\}\text{.}\) Examples of partitions of \(A\)  are:

> \(\displaystyle \{\{a\}, \{b\}, \{c, d\}\}\)
> \(\displaystyle \{\{a, b\}, \{c, d\}\}\)
> \(\displaystyle \{\{a\}, \{b\}, \{c\}, \{d\}\}\)

> How many others are there, do you suppose?

> There are 15 different partitions.  The most efficient way to count them all is to classify them by the size of blocks.   For example, the partition \(\{\{a\}, \{b\}, \{c, d\}\}\) has block sizes 1, 1, and 2.

> **Example 2.3.3 — Some Integer Partitions.**

> Two examples of partitions of the set of integers \(\mathbb{Z}\) are

> \(\{\{n\} \mid n \in \mathbb{Z}\}\) and
> \(\{\{ n \in \mathbb{Z} \mid n < 0\}, \{0\},\{ n \in \mathbb{Z} \mid 0 < n \}\}\text{.}\)

> The set of subsets \(\{\{n \in \mathbb{Z} \mid n \geq 0\},\{n \in \mathbb{Z} \mid  n \leq 0\}\}\) is not a partition because the two subsets have a nonempty intersection. A second example of a non-partition is \(\{\{n \in \mathbb{Z} \mid  \lvert n \rvert = k\} \mid k = -1, 0, 1, 2, \cdots\}\) because one of the blocks, when \(k=-1\) is empty.

One could also think of the concept of partitioning a set as a “packaging problem.” How can one “package” a carton of, say, twenty-four cans? We could use: four six-packs, three eight-packs, two twelve-packs, etc. In all cases: (a) the sum of all cans in all packs must be twenty-four, and (b) a can must be in one and only one pack.

# Subsection 2.3.2 Addition Laws

> **Theorem 2.3.4 — The Basic Law Of Addition:.**

> If \(A\) is a finite set, and if \(\{A_1,A_2,\ldots ,A_n\}\) is a partition of \(A\) , then
> 
> \begin{equation*}
> \lvert A \rvert = \lvert A_1 \rvert + \lvert A_2 \rvert + \cdots + \lvert A_n \rvert = \sum_{k=1}^n  \lvert A_k \rvert
> \end{equation*}

The basic law of addition can be rephrased as follows: If \(A\)  is a finite set where \(A_1 \cup A_2 \cup \cdots \cup A_n = A\) and where \(A_i \cap A_j = \emptyset\) whenever \(i \neq j\text{,}\) then

\begin{equation*}
\lvert A \rvert = \lvert A_1 \cup A_2 \cup  \cdots \cup A_n  \rvert = \lvert A_1 \rvert + \lvert A_2 \rvert + \cdots + \lvert A_n \rvert 
\end{equation*}

> **Example 2.3.5 — Counting All Students.**

> The number of students in a class could be determined by adding the numbers of students who are freshmen, sophomores, juniors, and seniors, and those who belong to none of these categories. However, you probably couldn’t add the students by major, since some students may have double majors.

> **Example 2.3.6 — Counting Students in Disjoint Classes.**

> The sophomore computer science majors were told they must take one and only one of the following courses that are open only to them: Cryptography, Data Structures, or JavaScript. The numbers in each course, respectively, for sophomore CS majors, were 75, 60, 55. How many sophomore CS majors are there? The Law of Addition applies here. There are exactly \(75 + 60 + 55 = 190\) CS majors since the rosters of the three courses listed above would be a partition of the CS majors.

> **Example 2.3.7 — Counting Students in Non-disjoint Classes.**

> It was determined that all junior computer science majors take at least one of the following courses: Algorithms, Logic Design, and Compiler Construction. Assume the number in each course was 75, 60 and 55, respectively for the three courses listed. Further investigation indicated ten juniors took all three courses, twenty-five took  Algorithms and Logic Design, twelve took Algorithms and Compiler Construction, and fifteen took Logic Design and Compiler Construction. How many junior C.S. majors are there?

> [Example 2.3.6 [UNRESOLVED_INTERNAL_LINK]](s-partitions-and-law-of-addition.html#student-counting-disjoint) was a simple application of the law of addition, however in this example some students are taking two or more courses, so a simple application of the law of addition would lead to double or triple counting. We rephrase information in the language of sets to describe the situation more explicitly.

> \(A\) = the set of all junior computer science majors

> \(A_1\) = the set of all junior computer science majors who took Algorithms

> \(A_2\) = the set of all junior computer science majors who took Logic Design

> \(A_3\) = the set of all junior computer science majors who took Compiler Construction

> Since all junior CS majors must take at least one of the courses, the number we want is:
> 
> \begin{equation*}
> \lvert A \rvert = \lvert A_1 \cup A_2 \cup A_3 \rvert = \lvert A_1 \rvert + \lvert A_2 \rvert + \lvert A_3 \rvert - \textrm{repeats}.
> \end{equation*}

> A Venn diagram is helpful to visualize the problem. In this case the universal set \(U\)  can stand for 	all students in the university.

> ![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/sageplot-venn-CS_Students.svg)

> We see that the whole universal set is naturally partitioned into subsets that are labeled by the numbers 1 through 8, and the set \(A\)  is  partitioned into subsets labeled 1 through 7. The region labeled 8 represents all students who are not junior CS majors.  Note also that students in the subsets labeled 2, 3, and 4 are double counted, and those in the subset labeled 1 are triple counted. To adjust, we must subtract the numbers in regions 2, 3 and 4.  This can be done by subtracting the numbers in the intersections of each pair of sets.  However, the individuals in region 1 will have been removed three times, just as they had been originally added three times.  Therefore, we must finally add their number back in.

> \begin{equation*}
> \begin{split}
> \lvert A \rvert & =  \lvert A_1 \cup A_2 \cup A_3 \rvert \\ 
> & = \lvert A_1 \rvert + \lvert A_2 \rvert + \lvert A_3 \rvert - \textrm{repeats} \\
> & = \lvert A_1 \rvert + \lvert A_2 \rvert + \lvert A_3 \rvert - \textrm{duplicates} + \textrm{triplicates}  \\
> & = \lvert A_1 \rvert + \lvert A_2 \rvert + \lvert A_3 \rvert - \left(\lvert A_1 \cap A_2 \rvert + \lvert A_1 \cap A_3 \rvert+ \lvert A_2 \cap A_3 \rvert \right) + \lvert A_1 \cap A_2 \cap A_3 \rvert  \\
> & = 75 + 60 + 55 - 25 - 12 - 15 + 10 = 148 
> \end{split}
> \end{equation*}

The ideas used in this latest example gives rise to a basic counting technique:

> **Theorem 2.3.9 — Laws of Inclusion-Exclusion.**

> Given finite sets \(A_1, A_2, A_3\text{,}\) then
> 
> 
> The Two Set Inclusion-Exclusion Law:
> 
> \begin{equation*}
> \lvert A_1 \cup A_2 \rvert =\lvert A_1 \rvert + \lvert A_2 \rvert - \lvert A_1 \cap A_2 \rvert  
> \end{equation*}
> 
> 
> 
> The Three Set Inclusion-Exclusion Law:
> 
> \begin{equation*}
> \begin{split}
> \lvert A_1 \cup A_2 \cup A_3 \rvert & =\lvert A_1 \rvert + \lvert A_2 \rvert + \lvert A_3 \rvert\\
> &\quad - (\lvert A_1 \cap A_2 \rvert + \lvert A_1 \cap A_3 \rvert+ \lvert A_2 \cap A_3 \rvert)\\
> &\quad + \lvert A_1 \cap A_2 \cap A_3 \rvert
> \end{split} 
> \end{equation*}

The inclusion-exclusion laws extend to more than three sets, as will be explored in the exercises.

In this section we saw that being able to partition a set into disjoint subsets gives rise to a handy counting technique. Given a set, there are many ways to partition depending on what one would wish to accomplish. One natural partitioning of sets is apparent when one draws a Venn diagram. This particular partitioning of a set will be discussed further in Chapters 4 and 13.

> **Exercise 1 . —**

> List all partitions of the set \(A =\{a, b, c\}\text{.}\)

> **Exercise 2 . —**

> Which of the following collections of subsets of the plane, \(\mathbb{R}^2\text{,}\) are partitions?

> \(\displaystyle \{ \{(x, y) \mid x + y = c \} \mid c \in \mathbb{R} \}\)
> The set of all circles in \(\mathbb{R}^2 \)
> 
> The set of all circles in \(\mathbb{R}^2\) centered at the origin together with the set \(\{(0,0)\}\)
> 
> \(\displaystyle \{\{(x, y)\} \mid (x, y) \in \mathbb{R}^2  \} \)

> **Exercise 3 . —**

> A student, on an exam paper, defined the term partition the following way: “Let \(A\)  be a set. A partition of \(A\) is any set of nonempty subsets \(A_1, A_2, A_3, \dots\)  of \(A\) such that each element of \(A\) is in one of the subsets.”  Is this definition correct? Why?

> **Exercise 4 . —**

> Let \(A_1\) and \(A_2\) be subsets of a set \(U\text{.}\)   Draw a Venn diagram of this situation and shade in the subsets \(A_1 \cap A_2\text{,}\) \(A_1^c \cap A_2\text{,}\) \(A_1 \cap A_2^c\text{,}\) and \(A_1^c \cap A_2^c\) . Use the resulting diagram and the definition of partition to convince yourself that the subset of these four subsets that are nonempty form a partition of \(U\text{.}\)

> **Exercise 5 . —**

> Show that \(\{\{2 n \mid n \in \mathbb{Z}\}, \{2 n + 1 \mid n \in \mathbb{Z}\}\}\) is a partition of \(\mathbb{Z}\text{.}\) Describe this partition using only words.

> **Exercise 6 . —**

> A group of 30 students were surveyed and it was found that 18 of them took Calculus and 12 took Physics. If all students took at least one course, how many took both Calculus and Physics? Illustrate using a Venn diagram.
> What is the answer to the question in part (a) if five students did not take either of the two courses? Illustrate using a Venn diagram.

> **Exercise 7 . —**

> A survey of 90 people, 47 of them played tennis and 42 of them swam. If 17 of them participated in both activities, how many of them participated in neither?

> **Exercise 8 . —**

> A survey of 300 people found that 60 owned an iPhone, 75 owned a Blackberry, and 30 owned an Android phone. Furthermore, 40 owned both an iPhone and a Blackberry, 12 owned both an iPhone and an Android phone, and 8 owned a Blackberry and an Android phone. Finally, 3 owned all three phones.

> How many people surveyed owned none of the three phones?
> How many people owned a Blackberry but not an iPhone?
> How many owned a Blackberry but not an Android?

> **Exercise 9 . —**

> Regarding [Theorem 2.3.9 [UNRESOLVED_INTERNAL_LINK]](s-partitions-and-law-of-addition.html#inclusion-exclusion),
> 
> Use the two set inclusion-exclusion law  to derive the  three set inclusion-exclusion law. Note: A knowledge of basic set laws is needed for this exercise.
> State and derive the inclusion-exclusion law for four sets.

> **Exercise 10 . —**

> To complete your spring schedule, you must add Calculus and Physics. At 9:30, there are three Calculus sections and two Physics sections; while at 11:30, there are two Calculus sections and three Physics sections.  How many ways can you complete your schedule if your only open periods are 9:30 and 11:30?

> **Exercise 11 . —**

> The definition of \(\mathbb{Q}  = \{a/b \mid a, b \in \mathbb{Z}, b \neq 0\}\) given in Chapter 1 is  awkward. If we use the definition to list elements in \(\mathbb{Q}\text{,}\) we will have duplications such as \(\frac{1}{2}\text{,}\) \(\frac{-2}{-4}\) and \(\frac{300}{600}\)   Try to write a more precise definition of the rational numbers so that there is no duplication of elements.
