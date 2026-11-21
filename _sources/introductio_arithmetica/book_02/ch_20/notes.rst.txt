:order: 20
:layout: book
:breadcrumb_title: Ch. 20: Cubes from Odd Blocks (Notes)
:title: Chapter 20: Generation of Cubes from Consecutive Odd Blocks — Notes
:canonical_id: Book II, Ch. 20
:original_id: D'Ooge pp. 261–263 · Hoche pp. 117–119
:folio: introductio_arithmetica:0277
:hero: /_static/figures/nicomachus-sum-of-cubes.svg
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _nicomachus-notes-2-20:

===================================================================
Chapter 20: Generation of Cubes from Consecutive Odd Blocks — Notes
===================================================================

.. folio:: introductio_arithmetica:0277
   :page: p. 261

Archival Witnesses & Apparatus
------------------------------

* **English Witness**: D'Ooge (1926), pp. 261–263 (folios ``introductio_arithmetica:0277``–``0279``).
* **Greek Witness**: Hoche (1866), pp. 117–119 (folios ``hoche_1866:0135``–``0137``).
* **Boethius Parallel**: :person:`Boethius <boethius>`, *De Institutione Arithmetica* II.36–39 (:cite:`boethius:friedlein:1867`, pp. 126–131 Friedlein).

Exact Symbolic Proof of Nicomachus's Sum-of-Cubes Theorem (II.20.5)
-------------------------------------------------------------------

Book II, Ch. 20.5 (:cite:`hoche:1866`, p. 118; :cite:`dooge:1926`, p. 263) contains the **oldest extant statement in world mathematics** of the odd-block generation of cubes, from which the closed-form sum of cubes follows immediately (explicitly completed by the Roman *agrimensores*, Abu Bakr al-Karaji, and Nilakantha, and inherent in combining Nicomachus II.9 with II.20; see :cite:`heath:hgm:1921`, Vol. I, pp. 109–110):

1. **Odd-Block Identity**: The :math:`k`-th block consists of :math:`k` consecutive odd integers beginning after the first :math:`T_{k-1} = \frac{k(k-1)}{2}` odd numbers:

   .. math::

      B_k = \bigl\{\, 2(T_{k-1} + j) - 1 \;\big|\; j = 1, \dots, k \,\bigr\}
          = \bigl\{\, k^2 - k + 1,\; k^2 - k + 3,\; \dots,\; k^2 + k - 1 \,\bigr\}.

   This block has :math:`k` terms symmetrically centered around arithmetic mean :math:`k^2`, so its sum is identically:

   .. math::

      \sum_{x \in B_k} x = k \cdot k^2 = k^3.

2. **Square-of-Triangle Gnomon Identity**: Together, the first :math:`n` blocks :math:`B_1 \sqcup B_2 \sqcup \dots \sqcup B_n` consist of the first :math:`T_n = \frac{n(n+1)}{2}` odd integers without gap or overlap. By Nicomachus II.9 (:math:`\sum_{m=1}^{M} (2m - 1) = M^2` with :math:`M = T_n`):

   .. math::

      \sum_{k=1}^n k^3 = \sum_{m=1}^{T_n} (2m - 1) = T_n^2 = \left(\frac{n(n+1)}{2}\right)^2.

3. **Geometric Gnomon Realization (`construct_nicomachus_cubes_model`)**: In :g:`the T_4 = 10 square <nicomachus-sum-of-cubes:TRISQ>`, bordering the :math:`T_{k-1} \times T_{k-1}` square by strip width :math:`T_k - T_{k-1} = k` creates two rectangles of area :math:`k \cdot T_{k-1}` plus a :math:`k \times k` corner square:

   .. math::

      T_k^2 - T_{k-1}^2 = 2 k \cdot \frac{k(k-1)}{2} + k^2 = k^2(k - 1) + k^2 = k^3,

   giving each cube :g:`1³ <nicomachus-sum-of-cubes:CUBE1>`, :g:`2³ <nicomachus-sum-of-cubes:CUBE2>`, :g:`3³ <nicomachus-sum-of-cubes:CUBE3>`, :g:`4³ <nicomachus-sum-of-cubes:CUBE4>` a visible two-dimensional L-gnomon realization!
