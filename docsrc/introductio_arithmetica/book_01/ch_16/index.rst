:order: 16
:layout: book
:breadcrumb_title: Ch. 16: Perfect Numbers
:title: Chapter 16: Perfect Numbers & Their Method of Generation
:canonical_id: Book I, Ch. 16
:original_id: D'Ooge pp. 209–212 · Hoche pp. 39–44
:folio: introductio_arithmetica:0225
:hero: /_static/figures/sieve-perfect-numbers.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-en-1-16:

========================================================
Chapter 16: Perfect Numbers & Their Method of Generation
========================================================

.. picture:: /_static/figures/sieve-perfect-numbers.svg
   :alt: Nicomachus's Odd Sieve of Eratosthenes and Euclid-Nicomachus Perfect Numbers
   :caption: Bottom (Book I, Ch. 16): Mersenne prime sums of powers of two generate perfect numbers 6, 28, 496, 8128.

.. folio:: introductio_arithmetica:0225
   :page: p. 209

**1.** While these two varieties are opposed after the manner of extremes, the so-called :term:`perfect number <teleios>` appears as a mean, which is discovered to be in the realm of :term:`equality <isotes>`, and neither makes its parts greater than itself, added together, nor shows itself greater than its parts, but is always equal to its own parts. For the equal is always conceived of as in the mid-ground between greater and less, and is, as it were, moderation between excess and deficiency, and that which is in tune, between pitches too high and too low.

**2.** Now when a number, comparing with itself the sum and combination of all the factors whose presence it will admit, neither exceeds them in multitude nor is exceeded by them, then such a number is properly said to be perfect, as one which is equal to its own parts. Such numbers are :g:`6 <sieve-perfect-numbers:PERF6>` and :g:`28 <sieve-perfect-numbers:PERF28>`; for 6 has the factors half, third, and sixth, 3, 2, and 1, respectively, and these added together make 6 and are equal to the original number, and neither more nor less. Twenty-eight has the factors half, fourth, seventh, fourteenth, and twenty-eighth, which are 14, 7, 4, 2 and 1; these added together make 28, and so neither are the parts greater than the whole nor the whole greater than the parts, but their comparison is in equality, which is the peculiar quality of the perfect number.

**3.** It comes about that even as fair and excellent things are few and easily enumerated, while ugly and evil ones are widespread, so also the superabundant and deficient numbers are found in great multitude and irregularly placed—for the method of their discovery is irregular—but the perfect numbers are easily enumerated and arranged with suitable order; for only one is found among the units, :g:`6 <sieve-perfect-numbers:PERF6>`, only one other among the tens, :g:`28 <sieve-perfect-numbers:PERF28>`, and a third in the rank of the hundreds, 496 alone, and a fourth within the limits of the thousands, that is, below ten thousand, 8,128. And it is their

.. folio:: introductio_arithmetica:0226
   :page: p. 210

accompanying characteristic to end alternately in 6 or 8, and always to be even.

**4.** There is a method of producing them, neat and unfailing, which neither passes by any of the perfect numbers nor fails to differentiate any of those that are not such, which is carried out in the following way.

You must set forth the even-times even numbers from unity, advancing in order in one line, as far as you please: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1,024, 2,048, 4,096. . . . Then you must add them together, one at a time, and each time you make a summation observe the result to see what it is. If you find that it is a :term:`prime, incomposite <protos-asynthetos>` number, :g:`multiply it by the quantity of the last number added <sieve-perfect-numbers:MERSENNE>`, and the result will always be a perfect number. If, however, the result is secondary and composite, do not multiply, but add the next and observe again what the resulting number is; if it is secondary and composite, again pass it by and do not multiply; but add the next; but if it is prime and incomposite, multiply it by the last term added, and the result will be a perfect number; and so on to infinity. In similar fashion you will produce all the perfect numbers in succession, overlooking none.

For example, to 1 I add 2, and observe the sum, and find that it is 3, a prime and incomposite number in accordance with our previous demonstrations; for it has no factor with denominator different from the number itself, but only that with denominator agreeing. Therefore I multiply it by the last number to be taken into the sum, that is, 2; I get :g:`6 <sieve-perfect-numbers:PERF6>`, and this I declare to be the first perfect number in actuality, and to have those parts which are beheld in the numbers of which it is composed. For it will have unity as the factor with denominator the same as itself, that is, its sixth part; and 3 as the half, which is seen in 2, and conversely 2 as its third part.

**5.** Twenty-eight likewise is produced by the same method when another number, 4, is added to the previous ones. For the sum of the three, 1,

.. folio:: introductio_arithmetica:0227
   :page: p. 211

2, and 4, is 7, and is found to be prime and incomposite, for it admits only the factor with denominator like itself, the seventh part. Therefore I multiply it by the quantity of the term last taken into the summation, and my result is :g:`28 <sieve-perfect-numbers:PERF28>`, equal to its own parts, and having its factors derived from the numbers already adduced, a half corresponding to 2; a fourth, to 7; a seventh, to 4; a fourteenth to offset the half; and a twenty-eighth, in accordance with its own nomenclature, which is 1 in all numbers.

**6.** When these have been discovered, 6 among the units and 28 in the tens, you must do the same to fashion the next.

**7.** Again add the next number, 8, and the sum is 15. Observing this, I find that we no longer have a prime and incomposite number, but in addition to the factor with denominator like the number itself, it has also a fifth and a third, with unlike denominators. Hence I do not multiply it by 8, but add the next number, 16, and 31 results. As this is a prime, incomposite number, of necessity it will be multiplied, in accordance with the general rule of the process, by the last number added, 16, and the result is 496, in the hundreds; and then comes 8,128 in the thousands, and so on, as far as it is convenient for one to follow.

**8.** Now unity is potentially a perfect number, but not actually; for taking it from the series as the very first I observe what sort it is, according to the rule, and find it prime and incomposite; for it is so in very truth, not by participation like the rest, but it is the primary

.. folio:: introductio_arithmetica:0228
   :page: p. 212

**9.** number of all, and alone incomposite. I multiply it, therefore, by the last term taken into the summation, that is, by itself, and my result

**10.** is 1; for 1 times 1 equals 1. Thus unity is perfect potentially; for it is potentially equal to its own parts, the others actually.

.. toctree::
   :hidden:

   el
   summary
   notes
