:order: 2
:layout: book
:breadcrumb_title: Ten Means & Cube Harmony (Notes)
:title: The Ten Neo-Pythagorean Means & the Cube's Most Perfect Proportion — Notes
:canonical_id: Book II, Chs. 21–29
:original_id: Hoche pp. 119–147
:folio: Book II, Chs. 21–29
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _unit-4-ten-means-cube-harmony-notes:
.. _sec_02_ten_means_cube_harmony-notes:

===================================================================================================
Unit IV — The Ten Neo-Pythagorean Means & the Cube's Most Perfect Proportion — Critical Commentary
===================================================================================================

.. rubric:: Pappus Semicircle Geometry, Robbins's Textual Corrections on Means 8–9 & Euler–Philolaus Cube Duality · Book II, Chs. 21–29

.. picture:: /_static/figures/three-classical-means-semicircle.svg
   :alt: Semicircle Construction of Arithmetic, Geometric, and Harmonic Means
   :caption: Exact Rational Trigonometry verification over Q(sqrt(2)) for a=6, c=12: Q(O,S) = 81 (A=9), Q(Q,S) = 72 (G=6*sqrt(2)), and Q(S,F) = 64 (H=8) with A * H = G^2.

I. Exact Rational Trigonometry of the Semicircle of Means (II.21–27 & Pappus III)
---------------------------------------------------------------------------------

In ``geometor.nicomachus.construct_three_classical_means_model``, we model :person:`Pappus of Alexandria's <pappus>` celebrated semicircle construction (:cite:`pappus:synagoge:iii`, *Synagoge* III.12–16) for Nicomachus's canonical extremes :math:`a = 6, c = 12`:

* On diameter :math:`PR` of length :math:`a + c = 18` with :math:`P(0, 0), Q(6, 0), R(18, 0)` bisected at center :math:`O(9, 0)`, the three radii :g:`PO <three-classical-means-semicircle:PO>`, :g:`OR <three-classical-means-semicircle:OR>`, and :g:`OS <three-classical-means-semicircle:OS>` are :eq:`strictly equal <three-classical-means-semicircle:PO = three-classical-means-semicircle:OR>` with exact quadrance :math:`Q(O, S) = A^2 = 81` (:math:`A = 9`).
* Erecting the perpendicular chord at :math:`Q(6, 0)` meets :g:`semicircle PR <three-classical-means-semicircle:SEMICIRC>` at :math:`S(6, 6\sqrt{2})` over :math:`\mathbb{Q}(\sqrt{2})`, giving :g:`ordinate QS <three-classical-means-semicircle:QS>` exact quadrance :math:`Q(Q, S) = G^2 = a \cdot c = 72` (:math:`G = 6\sqrt{2}`, Euclid *Elements* VI.13).
* Dropping the altitude from :math:`Q(6, 0)` onto radius :math:`OS` meets :math:`OS` at exact foot :math:`F\bigl(\frac{26}{3}, \frac{2\sqrt{2}}{3}\bigr)`: by right-triangle similarity :math:`\triangle SQF \sim \triangle OQS`, :g:`radial segment SF <three-classical-means-semicircle:SF>` satisfies :math:`|SF| = \frac{QS^2}{OS} = \frac{G^2}{A} = \frac{72}{9} = \mathbf{8} = H` with exact quadrance :math:`Q(S, F) = H^2 = 64` and spread :math:`s(OS, PR) = \frac{72}{81} = \frac{8}{9}`!
* Simultaneously, in ``construct_cube_proportion_model``, Euclidean bisection constructs :math:`T_9` and complete-quadrilateral harmonic conjugation constructs :math:`T_8` with exact projective cross-ratio :math:`(T_6, T_{12}; T_8, Z) = -1`.

II. Textual & Mathematical Critique of Means 8, 9 & 10 (II.28)
--------------------------------------------------------------

As :person:`Frank Egleston Robbins <robbins>` and :person:`Martin Luther D'Ooge <dooge>` establish in their critical notes (:cite:`dooge:1926`, pp. 282–284 nn.; cf. :cite:`heath:hgm:1921`, Vol. I, pp. 86–89), the manuscript tradition of Book II, Ch. 28.3–4 preserves two instructive slips in Nicomachus's preliminary summary list (corrected in Ch. 28.9–10 and in :person:`Iamblichus <iamblichus>` / :person:`Pappus <pappus>`):

1. **8th & 9th Means**: In the preliminary list at II.28.3 (Hoche p. 140), the manuscripts give :math:`4, 7, 8` and :math:`3, 5, 6` alongside compressed verbal phrasing ("middle among the differences"), whereas in the detailed exposition at II.28.9–10 (Hoche pp. 142–143) the 8th mean :math:`(c - a) : (c - b) = c : a` is illustrated properly by **6, 7, 9** (:math:`(9-6):(9-7) = 3:2 = 9:6`) and the 9th mean :math:`(c - a) : (b - a) = b : a` is satisfied by **4, 6, 7** (:math:`(7-4):(6-4) = 3:2 = 6:4`). All ten canonical proportions and closed forms are verified symbolically in ``geometor.nicomachus.compute_all_ten_means`` and ``verify_ten_means_identities``.
2. **10th Mean as the Fibonacci Recurrence**: The 10th mean :math:`(c - a) : (c - b) = b : a` expands to :math:`a(c - a) = b(c - b) \iff (b - a)(b + a - c) = 0`. Since :math:`a < b < c` guarantees :math:`b \neq a`, this reduces identically to **the Fibonacci additive law** :math:`a + b = c`, which is why Nicomachus's exemplar :g:`(3, 5, 8) <three-classical-means-semicircle:MEAN10>` consists of three consecutive Fibonacci numbers!

III. Why the Cube Embodies 6 : 8 :: 9 : 12 (II.26 & II.29)
----------------------------------------------------------

Nicomachus's finale (II.29, echoed by :person:`Boethius <boethius>`, *De Inst. Arith.* II.54 *maxima et perfecta symphonia*, :person:`Luca Pacioli <pacioli>`, and :person:`Johannes Kepler <kepler>`, verified in ``verify_cube_proportion_identities``) brings together three mathematical worlds in a single proportion:

* **Polyhedral Topology**: Every combinatorial cube has :math:`F = 6` faces, :math:`V = 8` vertices, and :math:`E = 12` edges (satisfying Euler's polyhedral invariant :math:`V - E + F = 8 - 12 + 6 = 2`). Because :math:`\frac{1}{6} + \frac{1}{12} = \frac{2}{8} \iff H(6, 12) = 8`, the vertex count :math:`V = 8` is literally the **harmonic mean** of faces :math:`F = 6` and edges :math:`E = 12`! (Dually, for the **octahedron**, :math:`V = 6, F = 8, E = 12` exhibits the exact same harmonic triple!)
* **Duality of Arithmetic and Harmonic Means**: Inserting the arithmetic mean :math:`A(6, 12) = 9` alongside :math:`H(6, 12) = 8` satisfies the universal identity :math:`A \cdot H = G^2 \implies 9 \times 8 = 6 \times 12 = 72`, turning the four terms :math:`6, 8, 9, 12` into a **disjunct geometric proportion** :math:`6 : 8 :: 9 : 12` (:math:`3 : 4`) and :math:`6 : 9 :: 8 : 12` (:math:`2 : 3`).
* **Complete Diatonic Scale Scaffolding**: Dividing a string of length :math:`12` at :math:`9, 8, 6` sounds the root, fourth (:math:`12:9 = 4:3`), fifth (:math:`12:8 = 3:2`), and octave (:math:`12:6 = 2:1`), separated centrally by the Pythagorean whole tone (:math:`9:8`, *epogdoos*)—the exact harmonic framework upon which :person:`Plato <plato>` constructed the World-Soul in *Timaeus* 35b–36b (:cite:`plato:timaeus:27d-36d`).
