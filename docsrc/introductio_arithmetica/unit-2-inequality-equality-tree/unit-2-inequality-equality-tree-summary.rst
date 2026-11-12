:layout: book
:type: summary
:title: Unit II — Five Species of Inequality & the Equality Unfolding Tree — Summary
:canonical_id: Book I, Chs. 17–23
:original_id: Hoche pp. 44–72
:folio: Book I, Chs. 17–23

.. _unit-2-inequality-equality-tree-summary:

====================================================================================
Unit II — Five Species of Inequality & the Equality Unfolding Tree — Structural Map
====================================================================================

.. rubric:: Ratio Taxonomy & Ternary Tree Generation · Book I, Chs. 17–23

.. picture:: /_static/figures/equality-unfolding-tree.svg
   :alt: Nicomachus's Ternary Unfolding Tree from Equality (1, 1, 1)
   :caption: Every coprime rational ratio q : p > 1 appears uniquely as a three-term geometric progression (p^2, pq, q^2) unfolded from Equality (1, 1, 1).

Architectural Thesis
--------------------

Unit II transitions from absolute to relative quantity (*pros ti poson*), proving that every rational inequality is classified into five exact species and generated deterministically from :term:`Equality <isotes>`:

1. **Exhaustive Fivefold Classification of Ratios (I.17–22)**: Every reduced rational ratio :math:`a : b` (:math:`a > b`, :math:`\gcd(a, b) = 1`) written via Euclidean division :math:`a = m \cdot b + r` (:math:`m \ge 1, 0 \le r < b`) falls into one and only one of five species depending on whether :math:`m = 1` vs. :math:`m \ge 2` and :math:`r = 0`, :math:`r = 1`, or :math:`r \ge 2`.
2. **Nicomachus's Rule of Three Terms (I.23)**: Applying the linear operator :math:`L(a, b, c) = (a, a+b, a+2b+c)` directly (:math:`D = L`) and after reversal (:math:`R = L \circ \text{rev}`) to :g:`Equality (1, 1, 1) <equality-unfolding-tree:ROOT111>` unfolds a complete binary tree of three-term geometric progressions :math:`(p^2, pq, q^2)` isomorphic to the Calkin–Wilf / Stern–Brocot tree of positive rationals!

Taxonomy of the Five Species
----------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 20 22 36

   * - Species (Greek / Latin)
     - Reduced Form
     - Canonical Examples
     - Birthplace in the Equality Tree
   * - :g:`Multiple <five-species-ratios:SP1>` (*pollaplasios* / *multiplex*)
     - :math:`m : 1` (:math:`m \ge 2`)
     - :math:`2:1, 3:1, 4:1`
     - Direct spine from :g:`(1,1,1) <equality-unfolding-tree:ROOT111>`: :g:`(1,2,4) <equality-unfolding-tree:N124>`, :g:`(1,3,9) <equality-unfolding-tree:N139>`, :g:`(1,4,16) <equality-unfolding-tree:N1416>`
   * - :g:`Superparticular <five-species-ratios:SP2>` (*epimorios* / *superparticularis*)
     - :math:`(n + 1) : n` (:math:`n \ge 2`)
     - :math:`3:2, 4:3, 5:4, 9:8`
     - Reversed child of Multiple: :g:`(4,6,9) <equality-unfolding-tree:N469>`, :g:`(9,12,16) <equality-unfolding-tree:N91216>`
   * - :g:`Superpartient <five-species-ratios:SP3>` (*epimerēs* / *superpartiens*)
     - :math:`(n + r) : n` (:math:`1 < r < n`)
     - :math:`5:3, 7:4, 9:5`
     - Reversed child of Superparticular / higher node: :g:`(9,15,25) <equality-unfolding-tree:N91525>`
   * - :g:`Multiple Superparticular <five-species-ratios:SP4>` (*pollaplasiepimorios*)
     - :math:`(mn + 1) : n` (:math:`m, n \ge 2`)
     - :math:`5:2, 7:3, 7:2`
     - Direct child of Superparticular: :g:`(4,10,25) <equality-unfolding-tree:N41025>`
   * - :g:`Multiple Superpartient <five-species-ratios:SP5>` (*pollaplasiepimerēs*)
     - :math:`(mn + r) : n` (:math:`m \ge 2, r > 1`)
     - :math:`8:3, 11:4`
     - Direct child of Superpartient: :g:`(9,24,64) <equality-unfolding-tree:N92464>`
