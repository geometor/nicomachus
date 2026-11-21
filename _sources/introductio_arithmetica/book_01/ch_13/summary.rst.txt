:order: 13
:layout: book
:breadcrumb_title: Ch. 13: Relatively Prime Numbers & Eratosthenes's Sieve (Summary)
:title: Chapter 13: Relatively Prime Numbers & the Sieve of Eratosthenes — Summary
:canonical_id: Book I, Ch. 13
:original_id: D'Ooge pp. 203–206 · Hoche pp. 28–36
:folio: introductio_arithmetica:0219
:hero: /_static/figures/sieve-perfect-numbers.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-summary-1-13:

==========================================================================
Chapter 13: Relatively Prime Numbers & the Sieve of Eratosthenes — Summary
==========================================================================

.. folio:: introductio_arithmetica:0219
   :page: p. 203

Overview
--------

Nicomachus defines the intermediate third species of odd numbers, sets out Eratosthenes's **Sieve** (*Koskinon*) to separate all three species, and presents the **antaphairesis** (Euclidean subtraction) test for relative primality:

1. **The Intermediate Species (I.13.1)**: Numbers such as :math:`9` and :math:`25` are each secondary and composite in themselves, yet when compared to each other share only unity as a common measure and share no homonymous fractional part—so they are *relatively prime and incomposite*.
2. **The Odd Sieve of Eratosthenes (I.13.2–8)**: Listing all odd numbers from :math:`3` onward, each prime :math:`p` measures subsequent terms by skipping :math:`2k` places (where :math:`k` is its rank: :g:`stride 3 <sieve-perfect-numbers:SIEVE3>`, skipping 2; :g:`stride 5 <sieve-perfect-numbers:SIEVE5>`, skipping 4; :math:`7`, skipping 6), with multiplicities stepping through the odd sequence :math:`3, 5, 7, \dots`. Numbers untouched by any sieve stride are prime; squares of primes (:math:`9, 25, 49, \dots`) are composite yet mutually prime to one another; and numbers struck by multiple or non-square strides are fully composite.
3. **Antaphairesis Algorithm (I.13.9–13)**: Given two odd numbers, repeatedly subtracting the lesser from the greater (*antaphairesis*) terminates either at :math:`1` (proving them relatively prime, as with :math:`23` and :math:`45`) or at an odd number greater than :math:`1` (giving their greatest common measure, as :math:`7` for :math:`21` and :math:`49`).
