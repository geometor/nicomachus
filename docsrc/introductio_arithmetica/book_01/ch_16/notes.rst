:order: 16
:layout: book
:breadcrumb_title: Ch. 16: Perfect Numbers (Notes)
:title: Chapter 16: Perfect Numbers & Their Method of Generation — Notes
:canonical_id: Book I, Ch. 16
:original_id: D'Ooge pp. 209–212 · Hoche pp. 39–44
:folio: introductio_arithmetica:0225
:hero: /_static/figures/sieve-perfect-numbers.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-notes-1-16:

================================================================
Chapter 16: Perfect Numbers & Their Method of Generation — Notes
================================================================

.. folio:: introductio_arithmetica:0225
   :page: p. 209

Archival Witnesses & Apparatus
------------------------------

* **English Witness**: D'Ooge (1926), pp. 209–212 (folios ``introductio_arithmetica:0225``–``0228``).
* **Greek Witness**: Hoche (1866), pp. 39–44 (folios ``hoche_1866:0057``–``0062``).
* **Boethius Parallel**: :person:`Boethius <boethius>`, *De Institutione Arithmetica* I.19–20 (:cite:`boethius:friedlein:1867`, pp. 41–45 Friedlein).
* **Euclid Parallel**: :person:`Euclid <euclid>`, *Elements* VII Def. 22 and IX.36 (:cite:`euclid:elements:vii-ix`).

Perfect Numbers & Nicomachus's Two Famous Conjectures
-----------------------------------------------------

In ``geometor.nicomachus.euclid_nicomachus_perfect_numbers``, :g:`Euclid's theorem (Elements IX.36) <sieve-perfect-numbers:MERSENNE>` generates even perfect numbers whenever :math:`M_p = 2^p - 1` is prime:

.. math::

   P_p = 2^{p-1}(2^p - 1) \quad \text{for } p \in \{2, 3, 5, 7\} \implies P_p \in \{6,\; 28,\; 496,\; 8128\}.

In I.16.3, however, Nicomachus extrapolates from these first four values two celebrated empirical generalizations (transmitted unchallenged through :person:`Boethius <boethius>` and medieval Europe for over a millennium; see :cite:`heath:hgm:1921`, Vol. I, p. 100 and :cite:`dooge:1926`, p. 210 n. 2):

1. **One perfect number per decimal order of magnitude** (units, tens, hundreds, thousands, ...): **False** from the fifth perfect number onward! Since :math:`M_{11} = 2^{11} - 1 = 2047 = 23 \times 89` is composite, there is **no** five-digit, six-digit, or seven-digit perfect number; the fifth perfect number (:math:`p = 13`) leaps to eight digits: :math:`2^{12}(2^{13} - 1) = 33{,}550{,}336`.
2. **Strict alternation of terminal digits** ``6, 8, 6, 8, ...``: **Partially true, partially false!** Every even perfect number **does** end in either ``6`` or ``8`` (provable mod :math:`10` from :math:`p \equiv 1` vs. :math:`3 \pmod{4}` for odd primes :math:`p`), **but they do not alternate strictly**: the fifth (:math:`p = 13`, :math:`33{,}550{,}336`) and sixth (:math:`p = 17`, :math:`8{,}589{,}869{,}056`) **both** end in ``6``.

* **Textual Note (Hoche p. 42.15)**: Hoche's Teubner edition prints *prōtos kai synthetos* ("prime and composite") at I.16.5 for :math:`7`, a typographical slip for *prōtos kai asynthetos* ("prime and incomposite").
