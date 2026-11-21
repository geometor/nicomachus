:order: 13
:layout: book
:breadcrumb_title: Ch. 13: Relatively Prime Numbers & Eratosthenes's Sieve (Notes)
:title: Chapter 13: Relatively Prime Numbers & the Sieve of Eratosthenes — Notes
:canonical_id: Book I, Ch. 13
:original_id: D'Ooge pp. 203–206 · Hoche pp. 28–36
:folio: introductio_arithmetica:0219
:hero: /_static/figures/sieve-perfect-numbers.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-notes-1-13:

========================================================================
Chapter 13: Relatively Prime Numbers & the Sieve of Eratosthenes — Notes
========================================================================

.. folio:: introductio_arithmetica:0219
   :page: p. 203

Archival Witnesses & Apparatus
------------------------------

* **English Witness**: D'Ooge (1926), pp. 203–206 (folios ``introductio_arithmetica:0219``–``0222``).
* **Greek Witness**: Hoche (1866), pp. 28–36 (folios ``hoche_1866:0046``–``0054``).
* **Boethius Parallel**: :person:`Boethius <boethius>`, *De Institutione Arithmetica* I.16–18 (:cite:`boethius:friedlein:1867`, pp. 32–39 Friedlein).

Editorial & Mathematical Notes
------------------------------

* **The Odd-Only Sieve**: Notice that Nicomachus's version of Eratosthenes's :term:`Sieve <koskinon>` (*koskinon*) omits all even numbers and operates solely on the odd progression :math:`3, 5, 7, 9, \dots` starting at index :math:`k = 1, 2, 3, \dots`, where the :math:`k`-th odd number :math:`p = 2k + 1` steps by :math:`2k + 1` terms in the sequence (skipping :math:`2k` intermediate odd entries).
* **Mutual Subtraction (*Antaphairesis*)**: In §§9–13, Nicomachus gives the earliest surviving explicit arithmetic exposition of the Euclidean GCD algorithm (*antaphairesis*, cf. Euclid *Elements* VII.1–2) applied to concrete odd pairs: :math:`(23, 45) \to \gcd = 1` and :math:`(21, 49) \to \gcd = 7`.
