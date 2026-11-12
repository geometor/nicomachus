:layout: book
:type: notes
:title: Unit III — Inverse Reduction, Polygonal Gnomons, Same/Other & Sum of Cubes — Notes
:canonical_id: Book II, Chs. 1–2, 6–20
:original_id: Hoche pp. 73–76, 82–119
:folio: Book II, Chs. 1–2, 6–20

.. _unit-3-figurate-gnomons-cubes-notes:

=================================================================================================
Unit III — Inverse Reduction, Polygonal Gnomons, Same/Other & Sum of Cubes — Critical Commentary
=================================================================================================

.. rubric:: Euclidean Anthyphairesis, Polygonal Identities & Exact Gnomonic Proof of Sum of Cubes · Book II, Chs. 1–2, 6–20

.. picture:: /_static/figures/heteromecic-same-other.svg
   :alt: Plato's Same (Squares) and Other (Heteromecics)
   :caption: Exact comparison of odd-gnomon Squares (Same) and even-gnomon Heteromecics (Other) verified in geometor.nicomachus.verify_figurate_identities.

I. Book II, Chs. 1–2 as Quadratic Euclidean *Anthyphairesis*
------------------------------------------------------------

In ``geometor.nicomachus.reduce_to_equality``, Book II's inverse rule :math:`(x, y, z) \mapsto (x, y - x, z - x - 2(y - x))` applied to any ascending coprime geometric progression :math:`(p^2, pq, q^2)` (:math:`0 < p < q`) evaluates to:

.. math::

   \bigl(p^2,\; p(q - p),\; (q - p)^2\bigr).

If :math:`p \le q - p`, the triple remains ascending and represents :math:`(p,\; q - p)`; if :math:`q - p < p`, Nicomachus's instruction to place the lesser extreme first reverses it to :math:`\bigl((q - p)^2,\; (q - p)p,\; p^2\bigr)`, representing :math:`(q - p,\; p)`. Thus Nicomachus's three subtractions execute **Euclid's reciprocal subtraction algorithm** (*Elements* VII.1–2, *anthyphairesis*) simultaneously on the quadratic forms :math:`(p^2, pq, q^2)` until :math:`\gcd(p, q) = 1` terminates at :math:`(1, 1, 1)`! This provides a rigorous constructive proof of Nicomachus's philosophical thesis (echoing :person:`Plato's <plato>` *Timaeus* and *Philebus*) that :term:`Equality <isotes>` is both the **generative origin** and the **terminal element** (*stoicheion*) of all numerical relation.

II. Exact Symbolic Proof of Nicomachus's Sum-of-Cubes Theorem (II.20)
---------------------------------------------------------------------

Book II, Ch. 20.5 (:cite:`hoche:1866`, p. 118; :cite:`dooge:1926`, p. 263) contains the **oldest extant statement in world mathematics** of the odd-block generation of cubes, from which the closed-form sum of cubes follows immediately (explicitly completed by the Roman agrimensores, Abu Bakr al-Karaji, and Nilakantha, and inherent in combining Nicomachus II.9 with II.20; see :cite:`heath:hgm:1921`, Vol. I, pp. 109–110):

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
