:navigation: header
:order: 25
:nav_title: Demos

.. _demos:

Demonstrations
==============

.. rubric:: 100% Exact Symbolic SymPy & Rational Trigonometry Proofs of Nicomachus's Arithmetical Geometry

In strict accordance with **GEOMETOR's Content / Code Separation**, the historical Book Codex (:doc:`/introductio_arithmetica/index`) contains zero embedded Python scripts. All executable symbolic proofs, ratio trees, figurate gnomon dissections, semicircle mean constructions, and polyhedral cube models live in ``geometor.nicomachus`` and the runnable ``demos/*.py`` scripts documented below—verified over exact ``SymPy`` rationals :math:`\mathbb{Q}` and quadratic radicals :math:`\mathbb{Q}(\sqrt{ac})` with ``Model(..., auto_intersect=False)`` and **zero floating-point approximations**.

----

1. Book I, Chs. 13, 16, 17–23 & Book II, Chs. 1–2 — Ratio Taxonomy & the Equality Unfolding Tree
------------------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Unit II — Inequality & the Equality Tree (Critical Notes) </introductio_arithmetica/unit-2-inequality-equality-tree/unit-2-inequality-equality-tree-notes>` · *Script*: ``demos/equality_tree.py``

.. picture:: /_static/figures/equality-unfolding-tree.svg
   :alt: Nicomachus's Ternary Unfolding Tree from Equality (1, 1, 1)
   :caption: Book I, Ch. 23 & Book II, Chs. 1–2: Applying Nicomachus's three commands (a, b, c) -> (a, a+b, a+2b+c) directly and after sibling reversal (c, b, a) unfolds every rational inequality from primordial Equality (1, 1, 1).

* **Symbolic Verification**:
  Starting from :g:`Equality (1, 1, 1) <equality-unfolding-tree:ROOT111>`, direct application of ``NICOMACHUS_MATRIX_N1`` :math:`(a, a+b, a+2b+c)` generates the *multiple* spine :g:`(1, 2, 4) <equality-unfolding-tree:N124>`, :g:`(1, 3, 9) <equality-unfolding-tree:N139>`, :g:`(1, 4, 16) <equality-unfolding-tree:N1416>`. Reversing a multiple triple before applying the rule (``NICOMACHUS_MATRIX_N2``) births the *superparticulars* :g:`(4, 6, 9) <equality-unfolding-tree:N469>` (:term:`hemiolios <hemiolios>` :math:`3:2`) and :g:`(9, 12, 16) <equality-unfolding-tree:N91216>` (:term:`epitritos <epitritos>` :math:`4:3`), while direct vs. reversed children of superparticulars generate *multiple superparticulars* :g:`(4, 10, 25) <equality-unfolding-tree:N41025>` and *superpartients* :g:`(9, 15, 25) <equality-unfolding-tree:N91525>`. Conversely, :g:`reduce_to_equality <equality-unfolding-tree:REDUCE>` reduces every coprime geometric progression :math:`(p^2, pq, q^2)` back to ``(1, 1, 1)``.

.. code-block:: python

   from geometor.nicomachus import (
       classify_nicomachean_ratio,
       generate_equality_tree,
       reduce_to_equality,
       verify_equality_identities,
   )

   info = classify_nicomachean_ratio(9, 8)
   assert info["species_key"] == "superparticularis"
   tree = generate_equality_tree(max_depth=3)
   assert tree[0].terms == (1, 1, 1)
   steps = reduce_to_equality(9, 24, 64)
   assert steps[-1].after == (1, 1, 1)
   assert verify_equality_identities()["verified_tree_nodes"] == 16

----

2. Book II, Chs. 6–20 — Polygonal Alpha-Gnomons, Same/Other & Nicomachus's Sum-of-Cubes Theorem
-----------------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Unit III — Figurate Gnomons & Cubes (Critical Notes) </introductio_arithmetica/unit-3-figurate-gnomons-cubes/unit-3-figurate-gnomons-cubes-notes>` · *Script*: ``demos/figurate_gnomons.py``

.. picture:: /_static/figures/nicomachus-sum-of-cubes.svg
   :alt: Gnomonic Square Proof of Nicomachus's Sum-of-Cubes Theorem
   :caption: Book II, Ch. 20: Consecutive odd-number blocks {1}, {3, 5}, {7, 9, 11}, {13, 15, 17, 19} sum to cubes 1^3, 2^3, 3^3, 4^3 and tile the square of side T_4 = 10 as exact L-shaped gnomons.

* **Symbolic Verification**:
  In ``construct_nicomachus_cubes_model(order=4)``, a ``geometor.model.Model(auto_intersect=False)`` constructs the :math:`T_n \times T_n` square bordered at triangular coordinates :math:`T_k = \frac{k(k+1)}{2}`. Each :math:`k`-th L-gnomon has exact symbolic area :math:`T_k^2 - T_{k-1}^2 = k^3` and equals the sum of the :math:`k`-element odd block :g:`{13, 15, 17, 19} = 64 = 4^3 <nicomachus-sum-of-cubes:OD4>`, while ``sieve_of_eratosthenes`` and ``euclid_nicomachus_perfect_numbers`` verify Book I, Chs. 13 & 16.

.. code-block:: python

   from geometor.nicomachus import (
       construct_nicomachus_cubes_model,
       euclid_nicomachus_perfect_numbers,
       sieve_of_eratosthenes,
       verify_figurate_identities,
   )

   sieve = sieve_of_eratosthenes(35)
   assert sieve["odd_primes"][:6] == (3, 5, 7, 11, 13, 17)
   assert [row["perfect_number"] for row in euclid_nicomachus_perfect_numbers(4)] == [6, 28, 496, 8128]
   cubes = construct_nicomachus_cubes_model(order=4)
   assert cubes.total_area == cubes.triangular_side**2 == 100
   assert verify_figurate_identities()["nicomachus_cubes_verified"] is True

----

3. Book II, Chs. 21–29 — Semicircle Means, Ten Proportions & the Cube's *Teleiotatē Analogia*
---------------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Unit IV — Ten Means & Cube Harmony (Critical Notes) </introductio_arithmetica/unit-4-ten-means-cube-harmony/unit-4-ten-means-cube-harmony-notes>` · *Script*: ``demos/ten_means_and_cube.py``

.. picture:: /_static/figures/three-classical-means-semicircle.svg
   :alt: Exact Semicircle Construction of Arithmetic, Geometric, and Harmonic Means
   :caption: Book II, Chs. 21–28 & Pappus Synagoge III: Over diameter PR = a + c, radius OS = A, perpendicular ordinate QS = G, and radial projection SF = H satisfy H <= G <= A with exact right-triangle identity G^2 = A * H.

* **Symbolic Verification**:
  In ``construct_three_classical_means_model(6, 12)``, exact circle-line and line-line intersections over :math:`\mathbb{Q}(\sqrt{2})` establish :g:`radius OS = A = 9 <three-classical-means-semicircle:OS>` (:math:`Q(O, S) = 81`), :g:`ordinate QS = G = 6√2 <three-classical-means-semicircle:QS>` (:math:`Q(Q, S) = 72`), and :g:`radial projection SF = H = 8 <three-classical-means-semicircle:SF>` (:math:`Q(S, F) = 64`). In ``construct_cube_proportion_model()``, the Cube's :math:`6` faces, :math:`8` vertices, and :math:`12` edges embed :math:`6 : 8 :: 9 : 12` with projective harmonic cross-ratio ``-1`` and every Pythagorean consonance (:math:`2:1, 3:2, 4:3, 9:8`).

.. code-block:: python

   from geometor.model.invariants import quadrance
   from geometor.nicomachus import (
       compute_all_ten_means,
       construct_cube_proportion_model,
       construct_three_classical_means_model,
       verify_cube_proportion_identities,
       verify_ten_means_identities,
   )

   m = construct_three_classical_means_model(6, 12)
   assert quadrance(m.get_element_by_ID("O"), m.get_element_by_ID("S")) == 81  # A^2 = 9^2
   assert quadrance(m.get_element_by_ID("Q"), m.get_element_by_ID("S")) == 72  # G^2 = 6 * 12
   assert quadrance(m.get_element_by_ID("S"), m.get_element_by_ID("F")) == 64  # H^2 = 8^2

   assert len(compute_all_ten_means(4, 12)) == 10
   cube = construct_cube_proportion_model()
   assert cube.cube_counts == {"faces": 6, "vertices": 8, "edges": 12}
   assert cube.projective_cross_ratio == -1
   assert all(verify_ten_means_identities().values())
   assert all(verify_cube_proportion_identities().values())
