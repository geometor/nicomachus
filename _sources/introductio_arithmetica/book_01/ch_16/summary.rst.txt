:order: 16
:layout: book
:breadcrumb_title: Ch. 16: Perfect Numbers (Summary)
:title: Chapter 16: Perfect Numbers & Their Method of Generation — Summary
:canonical_id: Book I, Ch. 16
:original_id: D'Ooge pp. 209–212 · Hoche pp. 39–44
:folio: introductio_arithmetica:0225
:hero: /_static/figures/sieve-perfect-numbers.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-summary-1-16:

==================================================================
Chapter 16: Perfect Numbers & Their Method of Generation — Summary
==================================================================

.. folio:: introductio_arithmetica:0225
   :page: p. 209

Overview
--------

Between the extremes of excess and defect stands the :term:`perfect <teleios>` (*teleios*) number, equal to the sum of its proper aliquot parts:

1. **Definition & First Four Perfect Numbers (I.16.1–3)**: A number equal to the sum of all its divisors (excluding itself) is perfect: :g:`6 <sieve-perfect-numbers:PERF6>` (:math:`1+2+3`), :g:`28 <sieve-perfect-numbers:PERF28>` (:math:`1+2+4+7+14`), :math:`496`, and :math:`8128`—one each among units, tens, hundreds, and thousands, ending alternately in ``6`` and ``8``.
2. **Euclid–Nicomachus Generative Method (I.16.4–7)**: Summing the powers of two :math:`1 + 2 + 4 + \dots + 2^{k-1} = 2^k - 1`, whenever the cumulative sum is :term:`prime and incomposite <protos-asynthetos>`, :g:`multiplying by the last power added <sieve-perfect-numbers:MERSENNE>` yields :math:`2^{k-1}(2^k - 1)` (skipping composite sums such as :math:`15 = 3 \times 5`).
3. **The Monad as Potentially Perfect (I.16.8–10)**: Starting the series with :math:`1` alone yields :math:`1 \times 1 = 1`, making the :term:`monad <monas>` perfect *potentially* (*dynamei*), whereas :math:`6, 28, 496, 8128` are perfect *in actuality* (*energeiāi*).
