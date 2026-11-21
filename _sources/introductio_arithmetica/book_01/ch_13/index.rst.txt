:order: 13
:layout: book
:breadcrumb_title: Ch. 13: Relatively Prime Numbers & Eratosthenes's Sieve
:title: Chapter 13: Relatively Prime Numbers & the Sieve of Eratosthenes
:canonical_id: Book I, Ch. 13
:original_id: D'Ooge pp. 203–206 · Hoche pp. 28–36
:folio: introductio_arithmetica:0219
:hero: /_static/figures/sieve-perfect-numbers.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-en-1-13:

================================================================
Chapter 13: Relatively Prime Numbers & the Sieve of Eratosthenes
================================================================

.. picture:: /_static/figures/sieve-perfect-numbers.svg
   :alt: Nicomachus's Odd Sieve of Eratosthenes and Euclid-Nicomachus Perfect Numbers
   :caption: Top (Book I, Ch. 13): Eratosthenes's Koskinon operates strictly on the odd sequence 3, 5, 7, 9, 11, 13, 15, ...

.. folio:: introductio_arithmetica:0219
   :page: p. 203

**1.** While these two species of the odd stand opposed to one another, a third is discerned in the middle between them, taking its form as it were from both—that which in itself is secondary and composite, yet relative to another is prime and incomposite.
This occurs whenever a number, besides unity as its common measure, is also measured by some other measure and is therefore able to admit a part or parts with a different name alongside the part sharing its own name; yet

.. folio:: introductio_arithmetica:0220
   :page: p. 204

when set alongside another number similarly constituted, it proves unable to be measured by any common measure with that other, nor does it hold any part sharing the same name as those strictly contained in that other. For instance, 9 compared with 25: each on its own is secondary and composite, yet toward each other they have unity alone as a common measure,
and no fractional part shares the same name in both—the third that lies in 9 is not in 25, nor is the fifth that lies in 25 found in 9.

**2.** Their mode of generation is named by Eratosthenes a :term:`Sieve <koskinon>`, since we take the odd numbers mixed together and indistinguishable and separate them out by this generative procedure as through a sieve or sifting instrument, finding by themselves the prime and incomposite, by themselves the secondary and composite, and apart from them the mixed class.

**3.** The working of the sieve is this: setting out in order all the odd numbers from :g:`3 <sieve-perfect-numbers:P3>` in as long a row as possible, I start from the first term and examine which ones it is able to measure, and I find that it can :g:`measure those that skip two intervening places <sieve-perfect-numbers:SIEVE3>` as far as we care to go—not measuring at random or carelessly, but measuring the very first reached (passing over two terms) according to the quantity of the first number in the row, namely itself, three times;
the one skipping two places beyond that according to the second term in order, five times; the one again skipping two places further according to the third, seven times; the one lying still two places beyond according to the fourth, nine times; and so onward without end.

**4.** Next, turning afresh to the second term, :g:`5 <sieve-perfect-numbers:P5>`, I inspect which numbers it can measure, and I find :g:`all those skipping four intervening places <sieve-perfect-numbers:SIEVE5>`: the first according to the quantity of the first in the row, three times;
the second according to the second, five times; the third according to the third, seven times; and so on forever.

**5.** Again starting from the top, the third number, :g:`7 <sieve-perfect-numbers:P7>`, takes over the measuring and will measure those skipping six intervening places: the very first according to the quantity of 3 standing first, the second according to 5 (which holds second place), and the third according to 7 (for it too holds third rank in the row).

**6.** By the same proportion this will advance throughout without in-

.. folio:: introductio_arithmetica:0221
   :page: p. 205

terruption: they will succeed to the task of measuring according to the order of their position in the row; the count of terms skipped follows the regular progression of even numbers from 2 upward—that is, doubling the rank where the measurer stands; and how many times each is measured follows the regular advance of the odd numbers from 3 upward.

**7.** If, then, you mark the numbers with distinguishing signs, you will discover that those taking turns at measuring never all measure the same number together—sometimes not even two measure the same one—nor do all the numbers set down fall under some measure of theirs; rather, some completely escape being measured by any whatever, some are measured by one alone, and some by two or even more.

**8.** Those never measured at all, having escaped this process, are prime and incomposite, separated out as by a sieve; those measured by a single factor according to its own quantity will have only one differently named part in addition to the part sharing their own name; while those measured either by one factor in another's quantity (not its own), or by two factors together (such as :g:`15 <sieve-perfect-numbers:P15>`), will have several differently named parts besides the one sharing their name, and these will be secondary and composite.
As for the third division common to both—that which in itself is secondary and composite, yet relative to another is prime and incomposite—it will consist of those numbers formed when a prime and incomposite number measures by its own quantity, whenever any number so generated is compared against another generated in the same way: for example, 9 (which came from 3 measuring by its own quantity, three times), if compared with 25 (which came from 5 measuring by its own quantity, five times), has no common measure with it except unity.

.. folio:: introductio_arithmetica:0222
   :page: p. 206

**9.** Now, that we may also possess a diagnostic method for numbers that are either prime and incomposite or secondary and composite relative to each other—since unity is the common measure of the former, while of the latter some other number besides unity is, and to find what number this is: if two odd numbers are set before us and someone asks us to determine whether they are relatively prime and incomposite or secondary and composite, and if secondary and composite, what number is their common measure,
we must compare the proposed numbers against each other and continually subtract the lesser from the greater as many times as possible, then after subtracting it, subtract in turn from the remainder as often as possible; for this alternating reversal and mutual subtraction (*antaphairesis*) must of necessity terminate either at unity or at one and the same number, necessarily odd. Whenever the subtractions end at unity, they show the numbers to be relatively prime and incomposite;
but whenever they terminate at some other odd number repeated as the same quantity, declare them relatively secondary and composite, and that repeated number itself to be their common measure.

**10.** For instance, if 23 and 45 are proposed to us, subtract 23 from 45, and 22 will remain; subtracting this in turn from 23, 1 remains; subtracting 1 from 22 as many times as possible, you will end at 1. Therefore they are relatively prime and incomposite, and the remaining unity is their common measure.

**11.** If someone proposes other numbers, 21 and 49, I subtract the lesser from the greater, leaving 28; then again from this I subtract the same 21 (for this is possible), leaving 7; this I subtract in turn from 21, leaving 14; from which again I subtract 7 (for this is possible), and 7 will remain, and 7 cannot be subtracted from 7. Their end therefore came to rest at the repeated 7; declare the original 21 and 49 relatively secondary and composite, and 7 their common measure alongside universal unity.

.. toctree::
   :hidden:

   el
   summary
   notes
