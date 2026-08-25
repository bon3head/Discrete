---
source_relative_path: "DM TXT/2-Combinatorics/ads Basic Counting Techniques - The Rule of Products.html"
source_sha256: "824ad8a851401c437c15c68aa072795264808e7624b07f5b09f31164130ec98c"
scope_class: active_candidate
displayed_section_or_chapter: "Section 2.1 Basic Counting Techniques - The Rule of Products"
content_gap: true
missing_assets:
  - "external/images/fig-sol-2-1-17.png"
  - "external/images/lunch.png"
---

# Section 2.1 Basic Counting Techniques - The Rule of Products

# Subsection 2.1.1 What is Combinatorics?

One of the first concepts our parents taught us was the “art of counting.” We were taught to raise three fingers to indicate that we were three years old. The question of “how many” is a natural and frequently asked question. Combinatorics is the “art of counting.” It is the study of techniques that will help us to count the number of objects in a set quickly. Highly sophisticated results can be obtained with this simple concept. The following examples will illustrate that many questions concerned with counting involve the same process.

> **Example 2.1.1 — How many lunches can you have?.**

> A snack bar serves five different sandwiches and three different beverages. How many different lunches can a person order? One way of determining the number of possible lunches is by listing or enumerating all the possibilities. One systematic way of doing this is by means of a tree, as in the following figure.

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/lunch.png)

> Every path that begins at the position labeled START and goes to the right can be interpreted as a choice of one of the five sandwiches followed by a choice of one of the three beverages. Note that considerable work is required to arrive at the number fifteen this way; but we also get more than just a number. The result is a complete list of all possible lunches. If we need to answer a question that starts with “How many . . . ,” enumeration would be done only as a last resort. In a later chapter we will examine more enumeration techniques.

> An alternative method of solution for this example is to make the simple observation that there are five different choices for sandwiches and three different choices for beverages, so there are \(5 \cdot 3 = 15\) different lunches that can be ordered.

> **Example 2.1.3 — Counting elements in a cartesian product.**

> Let \(A = \{a, b, c, d, e\}\) and \(B = \{1,2,3\}\text{.}\) From Chapter 1 we know how to list the elements in \(A \times B = \{(a, 1), (a, 2), (a, 3), ..., (e, 3)\}\text{.}\)  Since the first entry of each pair can be any one of the five elements \(a, b, c, d\text{,}\) and \(e\text{,}\) and since the second can be any one of the three numbers 1, 2, and 3, it is quite clear there are \(5 \cdot 3 = 15\) different elements in \(A \times B\text{.}\)

> **Example 2.1.4 — A True-False Questionnaire.**

> A person is to complete a true-false questionnaire consisting of ten questions. How many different ways are there to answer the questionnaire? Since each question can be answered in either of two ways (true or false), and there are ten questions, there are
> 
> \begin{equation*}
> 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 2^{10} = 1024
> \end{equation*}
> 
> different ways of answering the questionnaire. The reader is encouraged to visualize the tree diagram of this example, but not to draw it!

We formalize the procedures developed in the previous examples with the following rule and its extension.

# Subsection 2.1.2 The Rule Of Products

> **Theorem 2.1.5 — The Rule Of Products.**

> If two operations must be performed, and if the first operation can always be performed \(p_1\) different ways and the second operation can always be performed \(p_2\) different ways, then there are \(p_1 p_2\) different ways that the two operations can be performed.

Note: It is important that \(p_2\) does not depend on the option that is chosen in the first operation. Another way of saying this is that \(p_2\) is independent of the first operation. If \(p_2\) is dependent on the first operation, then the rule of products does not apply.

> **Example 2.1.6 — Reduced Lunch Possibilities.**

> Assume in [Example 2.1.1 [UNRESOLVED_INTERNAL_LINK]](s-the-rule-of-products.html#lunch-possibilies1), coffee is not served with a beef or chicken sandwiches. Then by inspection of [Figure 2.1.2 [UNRESOLVED_INTERNAL_LINK]](s-the-rule-of-products.html#lunch) we see that there are only thirteen different choices for lunch. The rule of products does not apply, since the choice of beverage depends on one’s choice of a sandwich.

The rule of products can be extended to include sequences of more than two operations.

> **Theorem 2.1.7 — Extended Rule Of Products.**

> If \(n\) operations must be performed, and the number of options for each operation is \(p_1\text{,}\) \(p_2, \dots, p_n\) respectively, with each \(p_i\)  independent of previous choices, then the \(n\) operations can be performed \(p_1 \cdot p_2 \cdot \cdots \cdot p_n\) different ways.

> **Example 2.1.8 — A Multiple Choice Questionnaire.**

> A questionnaire contains four questions that have two possible answers and three questions with five possible answers. Since the answer to each question is independent of the answers to the other questions, the extended rule of products applies and there are \(2 \cdot 2 \cdot 2 \cdot 2 \cdot 5 \cdot 5 \cdot 5 = 2^4 \cdot 5^3 = 2000 \) different ways to answer the questionnaire.

In Chapter 1 we introduced the power set of a set \(A\text{,}\) \(\mathcal{P}(A)\text{,}\) which is the set of all subsets of \(A\text{.}\) Can we predict how many elements are in \(\mathcal{P}(A)\) for a given finite set \(A\text{?}\) The answer is yes, and in fact if \(\lvert A \rvert  = n\text{,}\) then \(\lvert \mathcal{P}(A) \rvert = 2^{n}\text{.}\)  The ease with which we can prove this fact demonstrates the power and usefulness of the rule of products. Do not underestimate the usefulness of simple ideas.

> **Theorem 2.1.9 — Power Set Cardinality Theorem.**

> If \(A\) is a finite set, then \(\lvert \mathcal{P}(A) \rvert = 2^{\lvert A \rvert }\text{.}\)

> **Exercise 1 . —**

> In horse racing, to bet the “daily double” is to select the winners of the first two races of the day. You win only if both selections are correct. In terms of the number of horses that are entered in the first two races, how many different daily double bets could be made?

> **Exercise 2 . —**

> Professor Shortcut records his grades using only his students’ first and last initials. What is the smallest class size that will definitely force Prof. S. to use a different system?

> **Exercise 3 . —**

> A certain shirt comes in four sizes and six colors. One also has the choice of a dragon, an alligator, or no emblem on the pocket. How many different shirts could you order?

> **Exercise 4 . —**

> A builder of modular homes would like to impress his potential customers with the variety of styles of his houses. For each house there are blueprints for three different living rooms, four different bedroom configurations, and two different garage styles. In addition, the outside can be finished in cedar shingles or brick. How many different houses can be designed from these plans?

> **Exercise 5 . —**

> The Pi Mu Epsilon mathematics honorary society of Outstanding University wishes to have a picture taken of its six officers. There will be two rows of three people. How many different way can the six officers be arranged?

> **Exercise 6 . —**

> An automobile dealer has several options available for each of three different packages of a particular model car: a choice of two styles of seats in three different colors, a choice of four different radios, and five different exteriors. How many choices of automobile does a customer have?

> **Exercise 7 . —**

> A clothing manufacturer has put out a mix-and-match collection consisting of two blouses, two pairs of pants, a skirt, and a blazer. How many outfits can you make? Did you consider that the blazer is optional? How many outfits can you make if the manufacturer adds a sweater to the collection?

> **Exercise 8 . —**

> As a freshman, suppose you had to take two of four lab science courses, one of two literature courses, two of three math courses, and one of seven physical education courses. Disregarding possible time conflicts, how many different schedules do you have to choose from?

> **Exercise 9 . —**

> (a) Suppose each single character stored in a computer uses eight bits. Then each character is represented by a different sequence of eight 0’s and 1’s called a bit pattern. How many different bit patterns are there? (That is, how many different characters could be represented?)

> (b) How many bit patterns are palindromes (the same backwards as forwards)?

> (c) How many different bit patterns have an even number of 1’s?

> **Exercise 10 . —**

> Automobile license plates in Massachusetts usually consist of three digits followed by three letters. The first digit is never zero. How many different plates of this type could be made?

> **Exercise 11 . —**

> Let \(A = \{1, 2, 3, 4\}\text{.}\) Determine the number of different subsets of \(A\text{.}\)
> 
> Let \(A = \{1, 2, 3, 4, 5\}\text{.}\) Determine the number of proper subsets of \(A\text{.}\)

> **Exercise 12 . —**

> How many integers from 100 to 999 can be written in base ten without using the digit 7?

> **Exercise 13 . —**

> Consider three persons, A, B, and C, who are to be seated in a row of three chairs. Suppose A and B are identical twins. How many seating arrangements of these persons can there be

> If you are a total stranger?
> If you are A and B’s mother?

> This problem is designed to show you that different people can have different correct answers to the same problem.

> **Exercise 14 . —**

> How many ways can a student do a ten-question true-false exam if he or she can choose not to answer any number of questions?

> **Exercise 15 . —**

> Suppose you have a choice of fish, lamb, or beef for a main course, a choice of peas or carrots for a vegetable, and a choice of pie, cake, or ice cream for dessert. If you must order one item from each category, how many different dinners are possible?

> **Exercise 16 . —**

> Suppose you have a choice of vanilla, chocolate, maple walnut or strawberry for ice cream, a choice of peanuts or walnuts for chopped nuts, and a choice of hot fudge or marshmallow for topping. You don’t have to order nuts.   How many different sundaes are possible?

> **Exercise 17 . —**

> A questionnaire contains six questions each having yes-no answers. For each yes response, there is a follow-up question with four possible responses.

> Draw a tree diagram that illustrates how many ways a single question in the questionnaire can be answered.
> How many ways can the questionnaire be answered?

> ![MISSING FIGURE: described in detail following the image](GAP:external/images/fig-sol-2-1-17.png)

> **Exercise 18 . —**

> Six people are invited to a dinner party. How many ways are there of seating them at a round table? If the six people consist of three who identify as male and three who identify as female, how many ways are there of seating them if each male must be surrounded by two females?  Assume we are only concerned with the relative positions around the table.  So if we rotate everyone we wouldn’t consider this a change in the seating.

> **Exercise 19 . —**

> How many ways can you separate a set with \(n\)  elements into two nonempty subsets if the order of the subsets is immaterial? What if the order of the subsets is important?

> **Exercise 20 . —**

> A gardener has three flowering shrubs and four nonflowering shrubs, where all shrubs are distinguishable from one another. He must plant these shrubs in a row using an alternating pattern, that is, a shrub must be of a different type from that on either side. How many ways can he plant these shrubs? If he has to plant these shrubs in a circle using the same pattern, how many ways can he plant this circle? Note that one nonflowering shrub will be left out at the end.
