:layout: book
:type: summary
:title: Unit III — Inverse Reduction, Polygonal Gnomons, Same/Other & Sum of Cubes — Summary
:canonical_id: Book II, Chs. 1–2, 6–20
:original_id: Hoche pp. 73–76, 82–119
:folio: Book II, Chs. 1–2, 6–20

.. _unit-3-figurate-gnomons-cubes-summary:

===============================================================================================
Unit III — Inverse Reduction, Polygonal Gnomons, Same/Other & Sum of Cubes — Structural Summary
===============================================================================================

.. rubric:: Figurate Arithmetical Geometry & Gnomonic Identities · Book II, Chs. 1–2, 6–20

.. picture:: /_static/figures/nicomachus-sum-of-cubes.svg
   :alt: Nicomachus's Sum-of-Cubes Theorem
   :caption: Book II, Ch. 20: Odd blocks summing to k^3 and L-gnomons of width k tiling the square of side T_n.

Architectural Thesis
--------------------

Unit III completes Nicomachus's philosophy of :term:`Equality <isotes>` by proving the inverse reduction theorem (II.1–2) and then constructs the entire hierarchy of plane and solid figurate numbers from alpha-pebble :term:`gnomons <gnomon>` (II.6–20):

1. **Inverse Reduction to Equality (II.1–2)**: Subtracting :math:`(x, y, z) \mapsto (x, y-x, z-x-2(y-x))` and sorting if needed reduces every geometric progression uniquely back to ``(1, 1, 1)``.
2. **Universal Polygonal Gnomon & Triangle Decomposition Laws (II.6–12)**: Summing arithmetic progressions with difference :math:`d = s - 2` builds all :math:`s`-gonal numbers :math:`P(s, n) = n + (s-2)\frac{n(n-1)}{2}`, each decomposing into elementary triangles via :g:`P(s, n) = T_n + (s - 3)T_{n-1} <polygonal-alpha-gnomons:DECOMP>`.
3. **Plato's Same & Other and Nicomachus's Cube Theorem (II.16–20)**: Odd gnomons build :g:`Squares n^2 (Same) <heteromecic-same-other:SAME>`, even gnomons build :g:`Heteromecics n(n+1) (Other) <heteromecic-same-other:OTHER>`, and :g:`consecutive odd blocks of length k sum to k^3 <nicomachus-sum-of-cubes:ODDBLOCKS>`, proving :math:`\sum_{k=1}^n k^3 = T_n^2`.

Summary of Figurate Sequences
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 18 28 32

   * - Figurate Class
     - Gnomon :math:`g_k`
     - Closed Formula
     - Initial Terms (:math:`n = 1, \dots, 6`)
   * - :g:`Triangular (s = 3) <polygonal-alpha-gnomons:TRI>`
     - :math:`k` (:math:`d = 1`)
     - :math:`T_n = \frac{n(n+1)}{2}`
     - :math:`1, 3, 6, 10, 15, 21`
   * - :g:`Square / Same (s = 4) <polygonal-alpha-gnomons:SQR>`
     - :math:`2k - 1` (:math:`d = 2`)
     - :math:`S_n = n^2 = T_n + T_{n-1}`
     - :math:`1, 4, 9, 16, 25, 36`
   * - :g:`Pentagonal (s = 5) <polygonal-alpha-gnomons:PENT>`
     - :math:`3k - 2` (:math:`d = 3`)
     - :math:`\frac{n(3n - 1)}{2} = T_n + 2T_{n-1}`
     - :math:`1, 5, 12, 22, 35, 51`
   * - :g:`Heteromecic / Other <heteromecic-same-other:OTHER>`
     - :math:`2k` (evens)
     - :math:`H_n = n(n+1) = 2 T_n`
     - :math:`2, 6, 12, 20, 30, 42`
   * - :g:`Cubes from Odd Blocks <nicomachus-sum-of-cubes:ODDBLOCKS>`
     - :math:`k` odds after :math:`T_{k-1}`
     - :math:`k^3,\quad \sum_{k=1}^n k^3 = T_n^2`
     - :math:`1, 8, 27, 64, 125, 216`
