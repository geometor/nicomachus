:order: 30
:layout: book
:title: Unit III — Inverse Reduction, Polygonal Gnomons, Same/Other & Sum of Cubes
:canonical_id: Book II, Chs. 1–2, 6–20
:original_id: Hoche pp. 73–76, 82–119 · D'Ooge pp. 230–232, 237–263
:folio: Book II, Chs. 1–2, 6–20

.. _unit-3-figurate-gnomons-cubes:
.. _unit-3-figurate-gnomons-cubes-en:

==========================================================================
Unit III — Inverse Reduction, Polygonal Gnomons, Same/Other & Sum of Cubes
==========================================================================

.. rubric:: Reduction of All Ratios to Equality, Alpha-Pebble Polygonal Gnomons, Solid Pyramids, Plato's *Same* & *Other*, and Nicomachus's Sum-of-Cubes Theorem (Book II, Chs. 1–2, 6–20)

.. epigraph::

   *«ἐντεῦθεν ἐκφανέστατα κριθήσεται τό τε ταὐτοῦ καὶ τὸ θατέρου μετέχον…»*

   “From this will be judged most clearly what partakes of the Same and what partakes of the Other…” — **Book II, Ch. 18.1 (Hoche p. 112)**

.. picture:: /_static/figures/polygonal-alpha-gnomons.svg
   :alt: Polygonal Numbers Built by Alpha-Pebble Gnomons and Decomposed into Triangles
   :caption: Book II, Chs. 6–12: Alpha-pebble (α) layouts of Triangular (d=1), Square (d=2), and Pentagonal (d=3) numbers built by successive arithmetic gnomons, together with Nicomachus's decomposition table into elementary triangles.

.. _nicomachus-en-2-1:

Book II, Chs. 1–2 — Element as Minimum & Inverse Reduction to Equality (1, 1, 1)
--------------------------------------------------------------------------------

*English Translation by Martin Luther D'Ooge (1926) · Hoche pp. 73–76 · D'Ooge pp. 230–232*

.. folio:: D'Ooge p. 230 · Hoche p. 73

**II.1.1–2.** An **element** (*stoicheion*) is said to be, and is, the smallest thing which enters into the composition of an object and the least thing into which it can be analyzed. Letters, for example, are called the elements of literate speech, for out of them all articulate speech is composed and into them finally it is resolved; sounds are the elements of all melody, for out of them it begins to be composed and into them it is resolved; and the so-called four general elements of the universe in simple bodies are fire, water, air, and earth. We wish accordingly to prove that :term:`equality <isotes>` is the **primordial element** of relative number, because out of equality all the species of inequality are composed, as we showed at the end of Book I, and **into equality alone** every inequality is finally resolved!

.. folio:: D'Ooge p. 231 · Hoche p. 74

**II.2.1–3 (The Inverse Three-Subtraction Rule).** Suppose there are given to you **any three terms whatever** in continuous proportion in any species of inequality—multiple, superparticular, superpartient, multiple superparticular, or multiple superpartient—ordered so that if necessary the lesser extreme stands first (:math:`x < y < z` with :math:`x : y = y : z`). Perform continually these **three subtractions**:

1. Always set down the **least extreme** unchanged as first term: :math:`x' = x`
2. Subtract the **first from the middle** to form the new middle term: :math:`y' = y - x`
3. Subtract **the first and twice the new middle** from the greatest term to form the new third term: :math:`z' = z - x - 2(y - x)`

If the resulting triple is not yet in ascending order, rearrange it so the least stands first and repeat the exact same three subtractions; within a finite number of steps you will **invariably arrive at three equal terms**—and when reduced to root integers, at :math:`(1, 1, 1)` itself! Thus from :math:`(9, 24, 64)` (*duplex superbipartient*, :math:`8:3`), subtracting yields :math:`(9, 15, 25)` (*superbipartient*, :math:`5:3`); subtracting yields :math:`(9, 6, 4)`, which rearranged to :math:`(4, 6, 9)` (*sesquialter*, :math:`3:2`) yields :math:`(4, 2, 1)`, which rearranged to :math:`(1, 2, 4)` (*double*) yields :math:`(1, 1, 1)`!

.. _nicomachus-en-2-6:

Book II, Chs. 6–12 — Alpha-Pebble Notation, Polygonal Gnomons & Triangular Decomposition
----------------------------------------------------------------------------------------

*Hoche pp. 82–99 · D'Ooge pp. 237–248*

.. folio:: D'Ooge p. 237 · Hoche p. 82

**II.6–7 (Alpha-Graphia, Point, Line & Primordial Triangle).** Having treated relative number, we return to linear, plane, and solid configurations of units, representing each unit not by ordinary numeral value (where :math:`\iota` denotes ten and :math:`\kappa` twenty), but visually by repeating the single letter **alpha** (``α``) like pebbles set out upon a reckoning board. Unity (:term:`monas <monas>`), occupying the place of a **point** (*sēmeion*), is the beginning of intervals and numbers, though itself without interval; **2** is the principle of **line** (*grammē*, one dimension: length without breadth); and **3** is the first principle of **plane surface** (*epipedon*, length and breadth), since in rectilinear geometry three lines are the minimum capable of bounding a plane region—namely the **triangle**!

.. folio:: D'Ooge p. 240 · Hoche p. 86

**II.8–11 (Polygonal Numbers & the Universal Gnomon Law).** Every :term:`polygonal number <polygonos>` is generated from unity by summing an arithmetic progression whose successive added borders are its :term:`gnomons <gnomon>`:

* :g:`Triangular numbers <polygonal-alpha-gnomons:TRI>` (:math:`1, 3, 6, 10, 15, 21, \dots`) arise by summing the natural series :math:`1 + 2 + 3 + 4 + \dots` (gnomons differing by **1**).
* :g:`Square numbers <polygonal-alpha-gnomons:SQR>` (:math:`1, 4, 9, 16, 25, 36, \dots`) arise by summing the **odd** numbers :math:`1 + 3 + 5 + 7 + \dots` (L-shaped gnomons differing by **2**, each having side :math:`n` and area :math:`n^2`).
* :g:`Pentagonal numbers <polygonal-alpha-gnomons:PENT>` (:math:`1, 5, 12, 22, 35, 51, \dots`) arise by summing the progression :math:`1 + 4 + 7 + 10 + \dots` (gnomons differing by **3**).
* **Hexagonal** (:math:`1, 6, 15, 28, 45, \dots`, difference **4**), **Heptagonal** (:math:`1, 7, 18, 34, 55, \dots`, difference **5**), and in general **every s-gonal number** sums an arithmetic progression from :math:`1` whose gnomons have constant difference :math:`d = s - 2`—two less than the number of angles of the polygon!

.. folio:: D'Ooge p. 246 · Hoche p. 96

**II.12 (Decomposition of Every Polygon into Triangles).** Just as in plane geometry drawing diagonals from a vertex resolves every rectilinear figure into triangles, so in arithmetic :g:`every polygonal number resolves into elementary triangular numbers <polygonal-alpha-gnomons:DECOMP>`:

* Every **square** is the sum of **two consecutive triangular numbers**: :math:`S_n = T_n + T_{n-1}` (:math:`4 = 3 + 1,\; 9 = 6 + 3,\; 16 = 10 + 6,\; 25 = 15 + 10`).
* Every **pentagon** equals the square of the same rank plus the preceding triangle: :math:`P(5, n) = S_n + T_{n-1} = T_n + 2 T_{n-1}` (:math:`5 = 4 + 1,\; 12 = 9 + 3,\; 22 = 16 + 6`).
* Generally, stacking polygonal rows side-by-side shows :math:`P(s + 1, n) = P(s, n) + T_{n-1}`, and hence :math:`P(s, n) = T_n + (s - 3) T_{n-1}`!

.. _nicomachus-en-2-13:

Book II, Chs. 13–17 — Solid Pyramids, Cubes, Scalenes & Heteromecic Numbers
---------------------------------------------------------------------------

*Hoche pp. 99–112 · D'Ooge pp. 248–257*

.. folio:: D'Ooge p. 248 · Hoche p. 99

**II.13–15 (Pyramids, Truncations & Three-Dimensional Solids).** Advancing into the third dimension (length, breadth, and depth), stacking successive polygonal numbers from unity upward produces **solid pyramids**: triangular-based pyramids (:math:`1, 4, 10, 20, 35, \dots`), square-based pyramids (:math:`1, 5, 14, 30, 55, \dots`), pentagonal pyramids (:math:`1, 6, 18, 40, \dots`), and so forth. Omitting unity at the apex produces **truncated** (*kolouroi*) pyramids; omitting :math:`1` and the second layer produces **bi-truncated** (*dikolouroi*), and so on. Equally-equal-equally solids (:math:`n \times n \times n`) are **cubes** (:math:`1, 8, 27, 64, 125, \dots`); solids with two equal dimensions and one lesser (:math:`n \times n \times m`, :math:`m < n`) are **bricks** (*plinthides*); two equal and one greater (:math:`m > n`) are **beams** (*dokides*); cubes ending in the same digit as their side (such as :math:`5^3 = 125` and :math:`6^3 = 216`, mirroring plane circular :math:`5^2 = 25, 6^2 = 36`) are **spherical** or **recurrent** (*apokatastatikoi*); and solids of three unequal sides (:math:`2 \times 3 \times 4 = 24`) are **wedges** (*sphēniskoi*) or **scalenes**.

.. folio:: D'Ooge p. 254 · Hoche p. 106

**II.16–17 (Heteromecic Numbers vs. Squares).** Opposite in nature to the **square** (:math:`n \times n`, equal-sided) stands the :term:`heteromecic <heteromekes>` (*heteromēkēs*, "of other length" or oblong) number, whose sides differ by **exact unity** (:math:`n(n + 1)`): :math:`2 = 1 \times 2,\; 6 = 2 \times 3,\; 12 = 3 \times 4,\; 20 = 4 \times 5,\; 30 = 5 \times 6`—generated by summing the successive **even** numbers :math:`2 + 4 + 6 + 8 + \dots` (whereas numbers like :math:`2 \times 4 = 8` or :math:`3 \times 6 = 18` whose sides differ by :math:`2` or more are called **promecic**, *promēkeis*).

.. _nicomachus-en-2-18:

Book II, Chs. 18–19 — Plato's *Same* & *Other* and the Square–Oblong Weave
--------------------------------------------------------------------------

*Hoche pp. 112–117 · D'Ooge pp. 257–261*

.. picture:: /_static/figures/heteromecic-same-other.svg
   :alt: Squares as Plato's Same (Odd Gnomons) vs. Heteromecics as Other (Even Gnomons)
   :caption: Book II, Chs. 17–19: Squares n^2 (sum of odds, Same) and Heteromecics n(n+1) (sum of evens, Other) interleave with alternating differences, ratios, and triangular halves.

.. folio:: D'Ooge p. 257 · Hoche p. 112

**II.18.1–4.** From this we discern most clearly why the ancients—:person:`Philolaus <philolaus>` and :person:`Plato <plato>` in the *Timaeus* (:cite:`plato:timaeus:27d-36d`, 35a)—posited the :term:`Same and the Other <tauton-thateron>` (*tauton kai thateron*) as the two primary cosmic principles: **Unity and the odd** partake of the nature of the **Same** (bounded, indivisible, generating :g:`equal-sided squares n^2 <heteromecic-same-other:SAME>` whose side ratio :math:`n : n = 1 : 1` is unchanging :term:`equality <isotes>`), whereas **the dyad and the even** partake of the **Other** (divisible, generating :g:`oblong heteromecics n(n+1) <heteromecic-same-other:OTHER>` whose side ratios :math:`2:1, 3:2, 4:3, 5:4, \dots` run through infinite species of inequality!).

.. folio:: D'Ooge p. 259 · Hoche p. 115

**II.19.1–4 (The Alternating Harmony of Squares and Oblongs).** Yet when :g:`Squares and Heteromecics are woven into a single alternating sequence <heteromecic-same-other:WEAVE>`:

.. math::

   1,\; 2,\; 4,\; 6,\; 9,\; 12,\; 16,\; 20,\; 25,\; 30,\; 36, \dots

they exhibit astonishing friendship and concord:

* Each heteromecic :math:`H_n = n(n+1)` is the exact **geometric mean** between consecutive squares :math:`S_n = n^2` and :math:`S_{n+1} = (n+1)^2` (:math:`n^2 : n(n+1) = n(n+1) : (n+1)^2`), while :math:`S_n + S_{n+1} + 2 H_n = (2n + 1)^2` is always an odd square!
* Their consecutive differences :math:`1, 2, 2, 3, 3, 4, 4, \dots` repeat every integer twice, while their ratios alternate in paired superparticulars (:math:`2:1, 2:1;\; 3:2, 3:2;\; 4:3, 4:3; \dots`), and half of every heteromecic is a triangular number (:math:`\frac{1}{2} H_n = T_n`)!

.. _nicomachus-en-2-20:

Book II, Ch. 20 — Nicomachus's Sum-of-Cubes Theorem from Odd Blocks
-------------------------------------------------------------------

*Hoche pp. 117–119 · D'Ooge pp. 261–263*

.. picture:: /_static/figures/nicomachus-sum-of-cubes.svg
   :alt: Nicomachus's Sum-of-Cubes Theorem and Gnomonic Square Proof
   :caption: Book II, Ch. 20: Consecutive odd blocks {1}, {3,5}, {7,9,11}, {13,15,17,19} sum to cubes 1^3, 2^3, 3^3, 4^3 and tile the square of side T_4 = 10 as exact L-shaped gnomons.

.. folio:: D'Ooge p. 263 · Hoche p. 118

**II.20.5 (Generation of All Cubes from Odd Numbers, Not Even!).** And how must one not marvel even more at this supreme token that **cubes** belong to the nature of the **Same** rather than the **Other**? Although cubes are three-dimensional solids and might seem related to the even, **every cube is generated from the consecutive odd numbers alone**, never from the even! Set forth the successive odd numbers indefinitely from unity:

.. math::

   1,\quad 3,\; 5,\quad 7,\; 9,\; 11,\quad 13,\; 15,\; 17,\; 19,\quad 21,\; 23,\; 25,\; 27,\; 29, \dots

Then:

* The **first** odd number makes the potential first cube: :math:`1 =` :g:`1³ = 1 <nicomachus-sum-of-cubes:CUBE1>`
* The **next two** added together make the second cube: :math:`3 + 5 =` :g:`2³ = 8 <nicomachus-sum-of-cubes:CUBE2>`
* The **next three** added together make the third cube: :math:`7 + 9 + 11 =` :g:`3³ = 27 <nicomachus-sum-of-cubes:CUBE3>`
* The **next four** added together make the fourth cube: :g:`13 + 15 + 17 + 19 = 64 <nicomachus-sum-of-cubes:OD4>` :math:`=` :g:`4³ = 64 <nicomachus-sum-of-cubes:CUBE4>`
* The **next five** added together make the fifth cube: :math:`21 + 23 + 25 + 27 + 29 = 5^3 = 125`, and so on forever!

And because the first :math:`k` blocks contain :math:`1 + 2 + \dots + n = T_n` consecutive odd numbers starting from :math:`1`, and the sum of the first :math:`M` odd numbers is always the **square** :math:`M^2` (Book II, Ch. 9), :g:`summing all odd blocks up to the n-th cube tiles the exact square of the n-th triangular number <nicomachus-sum-of-cubes:TRISQ>`:

.. math::

   1^3 + 2^3 + 3^3 + \dots + n^3 = (1 + 2 + 3 + \dots + n)^2 = T_n^2.
