:order: 2
:layout: book
:breadcrumb_title: Five Species & Equality Tree (Notes)
:title: Five Species of Inequality & the Equality Unfolding Tree — Notes
:canonical_id: Book I, Chs. 17–23
:original_id: Hoche pp. 44–72
:folio: Book I, Chs. 17–23
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _unit-2-inequality-equality-tree-notes:
.. _sec_02_inequality_equality_tree-notes:

=========================================================================================
Unit II — Five Species of Inequality & the Equality Unfolding Tree — Critical Commentary
=========================================================================================

.. rubric:: Algebraic Proof of the Three Commands, SL(2, Z) Projective Action & Canon Reception · Book I, Chs. 17–23

.. picture:: /_static/figures/five-species-ratios.svg
   :alt: Nicomachus's Five Species of Relative Inequality
   :caption: Exact bar-length comparison of Equality (1:1) and the five Nicomachean species of greater inequality, computed in geometor.nicomachus.classify_nicomachean_ratio.

I. Why Every Node Has Square Extremes & Bijects with Coprime Rationals (I.23)
-----------------------------------------------------------------------------

Nicomachus observes with wonder at the close of Book I (I.23.16, Hoche p. 71; D'Ooge p. 229) that in every triple generated from :g:`Equality (1, 1, 1) <equality-unfolding-tree:ROOT111>`, the first and third terms are **squares** while the middle term is their geometric mean. Exact algebra reveals why Nicomachus's three *prostagmata* (attributed by :person:`Iamblichus <iamblichus>` [:cite:`iamblichus:pistelli:1894`] and :person:`Theon of Smyrna <theon-of-smyrna>` [:cite:`theon:hiller:1878`, p. 107] to :person:`Eratosthenes <eratosthenes>` and Adrastus) are nothing less than the **symmetric square representation** :math:`\mathrm{Sym}^2(\mathbb{Z}^2)` of the Euclidean unimodular group :math:`\mathrm{SL}_2(\mathbb{Z}_{\ge 0})`!

Let a coprime pair :math:`(p, q)` with :math:`0 < p \le q` represent the three-term geometric progression:

.. math::

   (a, b, c) = (p^2,\; p q,\; q^2).

1. **Direct Command** :math:`D(a, b, c) = (a,\; a + b,\; a + 2b + c)`:

   .. math::

      D(p^2, pq, q^2) = \bigl(p^2,\; p(p + q),\; (p + q)^2\bigr),

   which acts on the underlying root ratio :math:`\frac{q}{p}` by :math:`(p, q) \mapsto (p,\; p + q)`, i.e. :math:`\frac{q}{p} \mapsto \frac{q}{p} + 1`! Hence if :math:`\frac{q}{p} = m : 1` is a multiple, :math:`D` increments it to :math:`(m+1) : 1`; if :math:`\frac{q}{p} = \frac{n+1}{n}` is superparticular (:g:`(4,6,9) <equality-unfolding-tree:N469>`), :math:`D` adds :math:`1` to produce :math:`\frac{2n+1}{n}`, a **multiple superparticular** (:g:`(4,10,25) <equality-unfolding-tree:N41025>`); and if :math:`\frac{q}{p} = \frac{n+r}{n}` is superpartient (:g:`(9,15,25) <equality-unfolding-tree:N91525>`), :math:`D` adds :math:`1` to produce :math:`\frac{2n+r}{n}`, a **multiple superpartient** (:g:`(9,24,64) <equality-unfolding-tree:N92464>`).

2. **Reversed (*Anastrophe*) Command** :math:`R(a, b, c) = D(c, b, a)`:

   .. math::

      R(p^2, pq, q^2) = D(q^2, pq, p^2) = \bigl(q^2,\; q(q + p),\; (q + p)^2\bigr),

   which acts on the root pair by :math:`(p, q) \mapsto (q,\; p + q)`, mapping the ratio :math:`\frac{q}{p} > 1` to :math:`\frac{p + q}{q} = 1 + \frac{p}{q} \in (1, 2)`! When :math:`p = 1` (a multiple :math:`q : 1`), :math:`1 + \frac{1}{q} = \frac{q + 1}{q}` is **strictly superparticular** (:g:`(4,6,9) <equality-unfolding-tree:N469>`, :g:`(9,12,16) <equality-unfolding-tree:N91216>`); when :math:`p \ge 2` (any non-multiple :math:`\frac{q}{p}` with :math:`\gcd(p, q) = 1`), :math:`1 + \frac{p}{q} = \frac{q + p}{q}` has remainder :math:`1 < p < q` and is **strictly superpartient** (:g:`(9,15,25) <equality-unfolding-tree:N91525>`)!

Because :math:`(p, q) \mapsto (p, p+q)` and :math:`(p, q) \mapsto (q, p+q)` are the exact generators of the **Calkin–Wilf / Stern–Brocot binary tree** restricted to ratios :math:`\ge 1` (since at the root :math:`(1, 1)` both branches coincide at :g:`(1, 2, 4) <equality-unfolding-tree:N124>`), **every coprime rational inequality** :math:`q : p > 1` appears **once and only once** in Nicomachus's tree (`geometor.nicomachus.generate_equality_tree`)!

II. Archytas's Theorem on Superparticular Ratios & Timaeus Harmonics (I.19)
---------------------------------------------------------------------------

Among the five species, the :g:`superparticular (*epimorios*) <five-species-ratios:SP2>` :math:`(n + 1) : n` holds supreme status in Pythagorean harmonics (:cite:`plato:timaeus:27d-36d`; :cite:`archytas:dk47b1`):

* The first three superparticulars are the musical **fifth** (:math:`3:2`, *hēmiolios*), **fourth** (:math:`4:3`, *epitritos*), and major third (:math:`5:4`, *epitetartos*), while :math:`9:8` (*epogdoos*) is the **whole tone**.
* As :person:`Archytas <archytas>` proved (preserved in :person:`Boethius <boethius>`, *De Institutione Musica* III.11, and *Euclid's Sectio Canonis* Prop. 3), **no geometric mean in rational integers exists between two terms in a superparticular ratio**—because in Nicomachus's tree every superparticular node :math:`(n^2, n(n+1), (n+1)^2)` has adjacent integer roots :math:`n` and :math:`n+1` with no integer between them, proving immediately that neither the octave's fifth/fourth nor the whole tone :math:`9:8` can be halved rationally!
