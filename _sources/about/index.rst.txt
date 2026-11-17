:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.nicomachus`` establishes a definitive Digital Scriptorium edition of **Nicomachus of Gerasa's** (*c.* 60–120 CE) *Introductio Arithmetica* (*Ἀριθμητικὴ Εἰσαγωγή*). Standing at the historical watershed between the rigorous axiomatic deductions of Euclid's *Elements* (Books VII–IX) and the medieval European university curriculum inaugurated by Boethius, Nicomachus composed the foundational treatise that defined *number* as the active cosmic exemplar in the Mind of the Creator, unifying discrete arithmetic with musical consonance, figurate geometry, and three-dimensional polyhedral symmetry.

Through this digital edition, the mathematical and philosophical architecture of the *Introductio* is extracted into addressable semantic elements across four synchronized codex tracks. This includes Nicomachus's ontological charter of the Quadrivium (bifurcating Quantity into discrete Multitude [*poson*] and continuous Magnitude [*pelikon*] and establishing Arithmetic's priority through *synanairein* co-removal); the deterministic unfolding of all ten species of rational inequality from primordial Equality (:math:`1 : 1 : 1`) via the three commands (*prostagmata*) and sibling reversal (*anastrophe*); the construction of polygonal numbers via arithmetic gnomons and the discovery of the Sum-of-Cubes theorem (:math:`\sum k^3 = T_n^2`); and the expansion of musical means into the ten Neo-Pythagorean proportions culminating in the **Cube's Most Perfect Proportion** (:math:`6 : 8 :: 9 : 12`), which unites the face-vertex-edge topology of the hexahedron with the fundamental musical intervals (:math:`2:1, 3:2, 4:3, 9:8`).

Within the wider GEOMETOR ecosystem, *Introductio Arithmetica* serves as the primordial arithmetic ground for the constructive canon of Euclid's *Elements* (:external+elements:doc:`index`), the projective harmonic configurations of Pappus of Alexandria (:external+pappus:doc:`index`), the geometric proportions catalogued in the *Encyclopedia of Triangle Centers* (``geometor.etc``), and the operational complexity measures of Émile Lemoine's *Géométrographie* (``geometor.lemoine``). Every ratio unfolding tree, figurate pebble arrangement, and harmonic mean relation is formalized in exact symbolic algebra through ``geometor.model`` over :math:`\mathbb{Q}`.

The GEOMETOR Mission
--------------------

The GEOMETOR project, conceived and directed by **phi ARCHITECT**, is dedicated to a multi-generational synthesis of geometry, computation, and symbolic reasoning. At its core, the project operates across three foundational pillars:

Extracting Historical Semantic Knowledge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Moving beyond passive page scans and superficial OCR, GEOMETOR recovers the living deductive architecture of more than 2,300 years of geometric, axiomatic, and philosophical treatises. From ancient Greek codices and Renaissance folios to nineteenth-century synthetic treatises, our Digital Scriptorium elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic knowledge graphs. Every proposition, step, enunciation, and justification is isolated, verified, and interconnected across history.

Exact Symbolic Grounding (``geometor.model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Geometry in GEOMETOR is never approximated through floating-point fuzz or numerical instability. Constructions are anchored in 100% exact symbolic algebra via `SymPy` and Norman Wildberger's Rational Trigonometry invariants (quadrance, spread, and cross-ratio) over exact algebraic number fields. By eliminating rounding errors entirely, geometric configurations retain absolute fidelity, allowing geometric proofs, collinearities, and concyclicities to be verified symbolically with mathematical certainty.

Repurposing Knowledge Across Mediums
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The extracted semantic graphs and exact algebraic models are re-deployed across a unified computational medium: synchronized multi-track **Book Codices** and EPUB 3 editions published with `photon-platform/publish`; computable deductive canons (such as ``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, and ``geometor.divine``); interactive SVG laboratories powered by ``geometor.explorer``; ultra-high-definition (QHD) visual broadcasts; and neuro-symbolic program synthesis guided by ``geometor.seer`` across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This Digital Scriptorium edition of Nicomachus of Gerasa's *Introductio Arithmetica* rests on three public-domain pillars documented in ``resources/introductio_arithmetica/sources_manifest.json``:

1. **Greek Critical Edition — Richard Hoche (Teubner, 1866)**:
   :person:`Richard Hoche <hoche>`, *Nicomachi Geraseni Pythagorei Introductionis Arithmeticae Libri II* (Leipzig: B. G. Teubner, 1866; :cite:`hoche:1866`). Established from the oldest extant witnesses—notably **Codex Cizensis** (11th/12th c.), **Göttingensis** (*G*), and **Monacensis** (*M*)—Hoche's pagination (pp. 1–72 for Book I, pp. 73–147 for Book II) remains the universal scholarly reference standard. Our Greek ``-el`` track stages the SHA-256 verified Open Greek and Latin *First1KGreek* TEI-XML witness (``tlg0358.tlg001.1st1K-grc1.xml``) audited directly against 300 DPI scans of Hoche's 1866 facsimile.
2. **English Translation & Mathematical Studies — D'Ooge, Robbins & Karpinski (Michigan / Macmillan, 1926)**:
   *Nicomachus of Gerasa: Introduction to Arithmetic*, translated into English by :person:`Martin Luther D'Ooge <dooge>`, with studies in Greek arithmetic by :person:`Frank Egleston Robbins <robbins>` and Louis Charles Karpinski (*University of Michigan Studies, Humanistic Series*, Vol. XVI, New York: Macmillan, 1926; :cite:`dooge:1926`, public domain in the United States). D'Ooge's lucid translation (pp. 181–286) and Robbins's critical footnotes (such as correcting the transmitted exemplars :math:`4, 7, 8` and :math:`3, 5, 6` in II.28.3–4 to :math:`4, 6, 7` and :math:`4, 6, 9`) anchor our ``-en`` and ``-notes`` tracks.
3. **Latin Quadrivium Parallel — Boethius (ed. Friedlein, Teubner, 1867)**:
   Around 500 CE, :person:`Anicius Manlius Severinus Boethius <boethius>` adapted Nicomachus's Greek treatise into Latin as *De Institutione Arithmetica Libri Duo* (:cite:`boethius:friedlein:1867`), coining the enduring Latin noun *quadruvium* ("fourfold way") at I.1 (p. 7.25 Friedlein) to translate Nicomachus's four "bridges" (*gephyrai*) and "ladders" (*klimakes*) of I.3.6. Every Codex unit cross-references Boethius's corresponding chapters alongside :person:`Iamblichus <iamblichus>` (:cite:`iamblichus:pistelli:1894`), :person:`John Philoponus <philoponus>` (:cite:`philoponus:hoche:1864`), :person:`Thomas Aquinas <aquinas>` (:cite:`aquinas:in-boethium-trinitate`), :person:`Luca Pacioli <pacioli>` (:cite:`pacioli:divina-proportione:1509`), and :person:`Johannes Kepler <kepler>`.

Archival Folio Pagination Key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Hoche 1866 Teubner Facsimile** (``hoche_1866_teubner.pdf``): ``PDF page = Hoche page + 18`` (Book I begins on Hoche p. 1 = PDF p. 19; Book II begins on Hoche p. 73 = PDF p. 91).
* **D'Ooge 1926 Michigan Edition** (``dooge_1926_michigan.pdf``): ``PDF page = D'Ooge page + 16`` (Translation Book I begins on D'Ooge p. 181 = PDF p. 197; Book II begins on D'Ooge p. 230 = PDF p. 246).
