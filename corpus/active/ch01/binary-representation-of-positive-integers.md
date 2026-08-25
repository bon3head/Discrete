---
source_relative_path: "DM TXT/1-Set-Theory/ads Binary Representation of Positive Integers.html"
source_sha256: "4ef2d4879c8d0979c3366990350d2cabf0e4d0998effab819a303dfc42a5af7b"
scope_class: active_candidate
displayed_section_or_chapter: "Section 1.4 Binary Representation of Positive Integers"
content_gap: true
missing_assets:
  - "external/images/1_to_10.png"
---

# Section 1.4 Binary Representation of Positive Integers

# Subsection 1.4.1 Grouping by Twos

Recall that the set of positive integers, \(\mathbb{P}\text{,}\) is \(\{1, 2, 3, . . . \}\text{.}\) Positive integers are naturally used to count things. There are many ways to count and many ways to record, or represent, the results of counting. For example, if we wanted to count five hundred twenty-three apples, we might group the apples by tens. There would be fifty-two groups of ten with three single apples left over. The fifty-two groups of ten could be put into five groups of ten tens (hundreds), with two tens left over. The five hundreds, two tens, and three units is recorded as 523. This system of counting is called the base ten positional system, or decimal system. It is quite natural for us to do grouping by tens, hundreds, thousands, \(\dots\) since it is the method that all of us use in everyday life.

The term positional refers to the fact that each digit in the decimal representation of a number has a significance based on its position. Of course this means that rearranging digits will change the number being described. You may have learned of numeration systems in which the position of symbols does not have any significance (e.g., the ancient Egyptian system). Most of these systems are merely curiosities to us now.

The binary number system differs from the decimal number system in that units are grouped by twos, fours, eights, etc. That is, the group sizes are powers of two instead of powers of ten. For example, twenty-three can be grouped into eleven groups of two with one left over. The eleven twos can be grouped into five groups of four with one group of two left over. Continuing along the same lines, we find that twenty-three can be described as one sixteen, zero eights, one four, one two, and one one, which is abbreviated \(10111_{\textrm{two}}\text{,}\) or simply \(10111\) if the context is clear.

# Subsection 1.4.2 A Conversion Algorithm

The process that we used to determine the binary representation of \(23\) can be described in general terms to determine the binary representation of any positive integer \(n\text{.}\) A general description of a process such as this one is called an algorithm. Since this is the first algorithm in the book, we will first write it out using less formal language than usual, and then introduce some “algorithmic notation.”  If you are unfamiliar with algorithms, we refer you to [Section A.1 [UNRESOLVED_INTERNAL_LINK]](app-alg1.html)

Start with an empty list of bits.
Assign the variable \(k\) the value \(n\text{.}\)


While \(k\)’s value is positive, continue performing the following three steps until \(k\) becomes zero and then stop.

divide \(k\) by 2, obtaining a quotient \(q\) (often denoted \(k \textrm{ div } 2\)) and a remainder \(r\) (denoted \((k \bmod 2)\)).
attach \(r\) to the left-hand side of the list of bits.
assign the variable \(k\) the value \(q\text{.}\)

> **Example 1.4.1 — An example of conversion to binary.**

> To determine the binary representation of 41 we take the following steps:

> \(\displaystyle 41 = 2 \times  20+ 1 \quad List = 1 \)
> \(\displaystyle 20 = 2 \times  10+0 \quad List = 01 \)
> \(\displaystyle 10 = 2\times 5 + 0 \quad List = 001 \)
> \(\displaystyle 5 =\text2\times  2+ 1 \quad List =1001\)
> \(\displaystyle 2 =2\times  1+ 0 \quad List = 01001 \)
> \(\displaystyle 1 =\text2 \times 0\text+1  \quad List = 101001\)

> Therefore, \(41=101001_{\textrm{two}}\)

The notation that we will use to describe this algorithm and all others is called pseudocode, an informal variation of the instructions that are commonly used in many computer languages. Read the following description carefully, comparing it with the informal description above. Appendix B, which contains a general discussion of the components of the algorithms in this book, should clear up any lingering questions. Anything after // are comments.

Here is a Sage version of the algorithm with two alterations. It outputs the binary representation as a string, and it handles all integers, not just positive ones.

```sage

```

Now that you’ve read this section, you should get this joke.

![MISSING FIGURE: described in detail following the image](GAP:external/images/1_to_10.png)

> **Exercise 1 . —**

> Find the binary representation of each of the following positive integers by working through the algorithm by hand.  You can check your answer using the sage cell above.

> 31
> 32
> 10
> 100

> **Exercise 2 . —**

> Find the binary representation of each of the following positive integers by working through the algorithm by hand.  You can check your answer using the sage cell above.

> 64
> 67
> 28
> 256

> **Exercise 3 . —**

> What positive integers have the following binary representations?

> 10010
> 10011
> 101010
> 10011110000

> **Exercise 4 . —**

> What positive integers have the following binary representations?
> 
> 100001
> 1001001
> 1000000000
> 1001110000

> **Exercise 5 . —**

> The number of bits in the binary representations of integers increases by one as the numbers double.  Using this fact, determine how many bits the binary representations of the following decimal numbers have without actually doing the full conversion.
> 
> 2017
> 4000
> 4500
> \(\displaystyle 2^{50}\)

> **Exercise 6 . —**

> Let \(m\) be a positive integer with \(n\)-bit binary representation: \(a_{n-1}a_{n-2}\cdots  a_1a_0\) with \(a_{n-1}=1\) What are the smallest and largest values that \(m\) could have?

> **Exercise 7 . —**

> If a positive integer is a multiple of 100, we can identify this fact from its decimal representation, since it will end with two zeros. What can you say about a positive integer if its binary representation ends with two zeros? What if it ends in \(k\) zeros?

> **Exercise 8 . —**

> Can a multiple of ten be easily identified from its binary representation?
