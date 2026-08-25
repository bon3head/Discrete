---
source_relative_path: "DM TXT/1-Set-Theory/ads Basic Set Operations.html"
source_sha256: "e778201b33235390a6e923cd87723309b4123db05dce1aa21ec690d27da6a0a3"
scope_class: active_candidate
displayed_section_or_chapter: "Section 1.2 Basic Set Operations"
content_gap: true
missing_assets:
  - "external/images/fig-sol-1-2-7.png"
  - "generated/sageplot/sageplot-venn-complement1.svg"
  - "generated/sageplot/sageplot-venn-complement2.svg"
  - "generated/sageplot/sageplot-venn-complement3.svg"
  - "generated/sageplot/sageplot-venn-intersection.svg"
  - "generated/sageplot/sageplot-venn-symmetric.svg"
  - "generated/sageplot/sageplot-venn-union.svg"
---

# Section 1.2 Basic Set Operations

# Subsection 1.2.1 Definitions

> **Definition 1.2.1 — Intersection.**

> Let \(A\) and \(B\) be sets. The intersection of \(A\) and \(B\) (denoted by \(A \cap  B\)) is the set of all elements that are in both \(A\) and \(B\text{.}\) That is, \(A \cap  B = \{x:x \in  A \textrm{ and } x \in  B\}\text{.}\)

> **Example 1.2.2 — Some Intersections.**

> Let \(A = \{1, 3, 8\}\) and \(B = \{-9, 22, 3\}\text{.}\) Then \(A \cap  B = \{3\}\text{.}\)
> 
> Solving a system of simultaneous equations such as \(x + y = 7\) and \(x - y = 3\) can be viewed as an intersection. Let \(A = \{(x,y): x + y = 7, x,y \in  \mathbb{R}\}\) and \(B = \{(x,y): x - y = 3, x,y\in  \mathbb{R}\}\text{.}\) These two sets are lines in the plane and their intersection, \(A \cap  B = \{(5, 2)\}\text{,}\) is the solution to the system.
> \(\mathbb{Z}\cap \mathbb{Q}=\mathbb{Z}\text{.}\)
> If \(A = \{3, 5, 9\}\) and \(B = \{-5, 8\}\text{,}\) then \(A\cap  B =\emptyset\text{.}\)

> **Definition 1.2.3 — Disjoint Sets.**

> Two sets are disjoint if they have no elements in common. That is, \(A\) and \(B\) are disjoint if \(A \cap  B = \emptyset\text{.}\)

> **Definition 1.2.4 — Union.**

> Let \(A\) and \(B\) be sets. The union of \(A\) and \(B\) (denoted by \(A \cup  B\)) is the set of all elements that are in \(A\) or in \(B\) or in both A and B. That is, \(A\cup B= \{x:x \in  A\textrm{ or } x\in  B\}\text{.}\)

It is important to note in the set-builder notation for \(A\cup B\text{,}\) the word “or” is used in the inclusive sense; it includes the case where \(x\) is in both \(A\) and \(B\text{.}\)

> **Example 1.2.5 — Some Unions.**

> If \(A = \{2, 5, 8\}\) and  \(B = \{7, 5, 22\}\text{,}\) then \(A \cup  B = \{2, 5, 8, 7, 22\}\text{.}\)
> 
> \(\displaystyle \mathbb{Z}\cup \mathbb{Q}=\mathbb{Q}.\)
> 
> \(A \cup \emptyset  = A\) for any set \(A\text{.}\)

Frequently, when doing mathematics, we need to establish a universe or set of elements under discussion. For example, the set \(A = \{x : 81x^4 -16 = 0 \}\) contains different elements depending on what kinds of numbers we allow ourselves to use in solving the equation \(81 x^4 -16 = 0\text{.}\) This set of numbers would be our universe. For example, if the universe is the integers, then \(A\) is empty. If our universe is the rational numbers, then \(A\) is \(\{2/3, -2/3\}\) and if the universe is the complex numbers, then \(A\) is \(\{2/3, -2/3, 2i/3, - 2i/3\}\text{.}\)

> **Definition 1.2.6 — Universe.**

> The universe, or universal set, is the set of all elements under discussion for possible membership in a set. We normally reserve the letter \(U\) for a universe in general discussions.

# Subsection 1.2.2 Set Operations and their Venn Diagrams

When working with sets, as in other branches of mathematics, it is often quite useful to be able to draw a picture or diagram of the situation under consideration. A diagram of a set is called a Venn diagram. The universal set \(U\) is represented by the interior of a rectangle and the sets by disks inside the rectangle.

> **Example 1.2.7 — Venn Diagram Examples.**

> \(A \cap  B\) is illustrated in [Figure 1.2.8 [UNRESOLVED_INTERNAL_LINK]](s-basic_Set_Operations.html#venn_diagram_intersection) by shading the appropriate region.

> ![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/sageplot-venn-intersection.svg)

> The union \(A \cup  B\) is illustrated in [Figure 1.2.9 [UNRESOLVED_INTERNAL_LINK]](s-basic_Set_Operations.html#venn_diagram_union).

> ![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/sageplot-venn-union.svg)

> In a Venn diagram, the region representing \(A \cap  B\) does not appear empty; however, in some instances it will represent the empty set. The same is true for any other region in a Venn diagram.

> **Definition 1.2.10 — Complement of a set.**

> Let \(A\) and \(B\) be sets. The complement of \(A\) relative to \(B\) (notation \(B - A\)) is the set of elements that are in \(B\) and not in \(A\text{.}\) That is, \(B-A=\{x: x\in B \textrm{ and } x\notin A\}\text{.}\) If \(U\) is the universal set, then \(U-A\) is denoted by \(A^c\) and is called simply the complement of \(A\text{.}\) \(A^c=\{x\in U : x\notin A\}\text{.}\)

![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/sageplot-venn-complement1.svg)

> **Example 1.2.12 — Some Complements.**

> Let \(U = \{1,2, 3, \text{...} , 10\}\) and \(A = \{2,4,6,8, 10\}\text{.}\) Then \(U-A = \{1, 3, 5, 7, 9\}\) and \(A - U= \emptyset\text{.}\)
> 
> If \(U = \mathbb{R}\text{,}\) then the complement of the set of rational numbers is the set of irrational numbers.
> 
> \(U^c= \emptyset\) and \(\emptyset ^c= U\text{.}\)
> 
> The Venn diagram of \(B - A\) is represented in [Figure 1.2.11 [UNRESOLVED_INTERNAL_LINK]](s-basic_Set_Operations.html#venn_diagram_complement1).
> The Venn diagram of \(A^c\) is represented in [Figure 1.2.13 [UNRESOLVED_INTERNAL_LINK]](s-basic_Set_Operations.html#venn_diagram_complement2).
> If \(B\subseteq A\text{,}\) then the Venn diagram of \(A- B\) is as shown in [Figure 1.2.14 [UNRESOLVED_INTERNAL_LINK]](s-basic_Set_Operations.html#venn_diagram_complement3).
> In the universe of integers, the set of even integers, \(\{\ldots  , - 4,-2, 0, 2, 4,\ldots \}\text{,}\) has the set of odd integers as its complement.

> ![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/sageplot-venn-complement2.svg)

> ![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/sageplot-venn-complement3.svg)

> **Definition 1.2.15 — Symmetric Difference.**

> Let \(A\) and \(B\) be sets. The symmetric difference of \(A\) and \(B\) (denoted by \(A\oplus B\)) is the set of all elements that are in \(A\) and \(B\) but not in both. That is, \(A \oplus  B = (A \cup  B) - (A \cap  B)\text{.}\)

> **Example 1.2.16 — Some Symmetric Differences.**

> Let \(A = \{1, 3, 8\}\) and \(B = \{2, 4, 8\}\text{.}\) Then \(A \oplus  B = \{1, 2, 3, 4\}\text{.}\)
> 
> 
> \(A \oplus  \emptyset = A\) and \(A \oplus  A = \emptyset\) for any set \(A\text{.}\)
> 
> 
> \(\mathbb{R} \oplus  \mathbb{Q}\) is the set of irrational numbers.
> The Venn diagram of \(A \oplus  B\) is represented in [Figure 1.2.17 [UNRESOLVED_INTERNAL_LINK]](s-basic_Set_Operations.html#venn_diagram_symmetric).

> ![MISSING FIGURE: described in detail following the image](GAP:generated/sageplot/sageplot-venn-symmetric.svg)

# Subsection 1.2.3 SageMath Note: Sets

To work with sets in Sage, a set is an expression of the form  Set(*list*).  By wrapping a list with `Set( )`, the order of elements appearing in the list and their duplication are ignored.  For example, L1 and L2 are two different lists, but notice how as sets they are considered equal:

```sage

```

The standard set operations are all methods and/or functions that can act on Sage sets. *You need to evaluate the following cell to use the subsequent cell.*

```sage

```

We can test membership, asking whether 10 is in each of the sets:

```sage

```

The ampersand is used for the intersection of sets.  Change it to the vertical bar, |, for union.

```sage

```

Symmetric difference and set complement are defined as “methods” in Sage. Here is how to compute the symmetric difference of \(A\)  with  \(B\text{,}\) followed by their differences.

```sage

```

> **Exercise 1 . —**

> Let \(A = \{0, 2, 3\}\text{,}\) \(B = \{2, 3\}\text{,}\) \(C = \{1, 5, 9\}\text{,}\) and let the universal set be \(U = \{0, 1, 2, . . . , 9\}\text{.}\) Determine:
> 
> \(\displaystyle A \cap  B\)
> \(\displaystyle A \cup  B\)
> \(\displaystyle B \cup  A\)
> \(\displaystyle A \cup  C\)
> \(\displaystyle A - B\)
> \(\displaystyle B - A\)
> \(\displaystyle A^c\)
> \(\displaystyle C^c\)
> \(\displaystyle A\cap C\)
> \(\displaystyle A\oplus B\)

> **Exercise 2 . —**

> Let \(A\text{,}\) \(B\text{,}\) and \(C\) be as in Exercise 1, let \(D = \{3, 2\}\text{,}\) and let \(E = \{2, 3, 2\}\text{.}\) Determine which of the following are true. Give reasons for your decisions.
> 
> \(\displaystyle A = B\)
> \(\displaystyle B = C\)
> \(\displaystyle B = D\)
> \(\displaystyle E=D\)
> \(\displaystyle A\cap B = B\cap A\)
> \(\displaystyle A \cup  B = B \cup  A\)
> \(\displaystyle A-B = B-A\)
> \(\displaystyle A \oplus  B = B \oplus  A\)

> **Exercise 3 . —**

> Let \(U= \{1, 2, 3, . . . , 9\}\text{.}\) Give examples of sets \(A\text{,}\) \(B\text{,}\) and \(C\) for which:
> 
> \(\displaystyle A\cap (B\cap C)=(A\cap B)\cap C\)
> \(\displaystyle A\cap (B\cup C)=(A\cap B)\cup (A\cap C)\)
> \(\displaystyle (A \cup  B)^c= A^c\cap B^c\)
> \(\displaystyle A \cup  A^c = U\)
> \(\displaystyle A \subseteq A\cup B\)
> \(\displaystyle A\cap B \subseteq A\)

> **Exercise 4 . —**

> Let \(U= \{1, 2, 3, . . . , 9\}\text{.}\) Give examples to illustrate the following facts:
> 
> If \(A \subseteq  B\) and \(B \subseteq C\text{,}\) then \(A\subseteq C\text{.}\)
> 
> There are sets \(A\) and \(B\) such that \(A - B \neq  B - A\)
> 
> If \(U = A\cup  B\) and \(A \cap  B = \emptyset\text{,}\) it always follows that \(A = U - B\text{.}\)

> **Exercise 5 . —**

> What can you say about \(A\) if \(U = \{1, 2, 3, 4, 5\}\text{,}\) \(B = \{2, 3\}\text{,}\) and (separately)
> 
> \(\displaystyle A \cup B = \{1, 2, 3,4\}\)
> \(\displaystyle A \cap  B = \{2\}\)
> \(\displaystyle A \oplus  B = \{3, 4, 5\}\)

> **Exercise 6 . —**

> Suppose that \(U\) is an infinite universal set, and \(A\) and \(B\) are infinite subsets of \(U\text{.}\) Answer the following questions with a brief explanation.

> Must \(A^c\) be finite?
> Must \(A\cup B\) be infinite?
> Must \(A\cap B\) be infinite?

> **Exercise 7 . —**

> Given that \(U\) = all students at a university, \(D\) = day students, \(M\) = mathematics majors, and \(G\) = graduate students. Draw Venn diagrams illustrating this situation and shade in the following sets:

> evening students
> undergraduate mathematics majors
> non-math graduate students
> non-math undergraduate students

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/fig-sol-1-2-7.png)

> **Exercise 8 . —**

> Let the sets \(D\text{,}\) \(M\text{,}\) \(G\text{,}\) and \(U\) be as in exercise 7.  Let \(\lvert U \rvert  = 16,000\text{,}\) \(\lvert D \rvert = 9,000\text{,}\) \(|M|=
> 300\text{,}\) and \(\lvert G \rvert = 1,000\text{.}\) Also assume that the number of day students who are mathematics majors is 250, 50 of whom are graduate students, that there are 95 graduate mathematics majors, and that the total number of day graduate students is 700. Determine the number of students who are:
> 
> evening students
> nonmathematics majors
> undergraduates (day or evening)
> day graduate nonmathematics majors
> evening graduate students
> evening graduate mathematics majors
> evening undergraduate nonmathematics majors
