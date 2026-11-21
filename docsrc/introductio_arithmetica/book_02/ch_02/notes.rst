:order: 2
:layout: book
:breadcrumb_title: Ch. 2: Inverse Reduction to Equality (Notes)
:title: Chapter 2: Inverse Three-Subtraction Reduction to Equality (1, 1, 1) — Notes
:canonical_id: Book II, Ch. 2
:original_id: D'Ooge pp. 230–232 · Hoche pp. 74–76
:folio: introductio_arithmetica:0246
:hero: /_static/figures/equality-unfolding-tree.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-notes-2-2:

============================================================================
Chapter 2: Inverse Three-Subtraction Reduction to Equality (1, 1, 1) — Notes
============================================================================

.. folio:: introductio_arithmetica:0246
   :page: p. 230

Archival Witnesses & Apparatus
------------------------------

* **English Witness**: D'Ooge (1926), pp. 230–232 (folios ``introductio_arithmetica:0246``–``0248``).
* **Greek Witness**: Hoche (1866), pp. 74–76 (folios ``hoche_1866:0092``–``0094``).
* **Boethius Parallel**: :person:`Boethius <boethius>`, *De Institutione Arithmetica* II.1 (:cite:`boethius:friedlein:1867`, pp. 79–80 Friedlein).

Mathematical & Textual Notes
----------------------------

* **Quadratic Anthyphairesis**: Applied to any coprime geometric progression :math:`(p^2, pq, q^2)` with :math:`0 < p < q`, the three subtractions yield :math:`(p^2, p(q-p), (q-p)^2)`—executing Euclid's reciprocal subtraction (*Elements* VII.1–2) on the generating roots :math:`(p, q)` until :math:`\gcd(p, q) = 1` reaches :math:`(1, 1)` and hence :math:`(1, 1, 1)` (verified symbolically in ``geometor.nicomachus.reduce_to_equality``).
* **Transition to Chapters 3–5**: The concluding remark on constructing consecutive :term:`sesquialter <hemiolios>`, :term:`sesquitertian <epitritos>`, and :term:`epogdoos <epogdoos>` ratios motivates the multiple–superparticular tables of Chapters 3–4.
