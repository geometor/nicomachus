:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: *Reader's Guide to the GEOMETOR Interactive Digital Codex of Nicomachus's Introduction to Arithmetic*

Welcome to the **GEOMETOR Digital Scriptorium** edition of :person:`Nicomachus of Gerasa's <nicomachus>` *Introductio Arithmetica* (*Ἀριθμητικὴ Εἰσαγωγή*). This edition unites the standard Teubner Greek critical text, Martin Luther D'Ooge's definitive English translation, and exact symbolic models of Pythagorean arithmetic.

----

1. Synchronized Reading Tracks
------------------------------

The treatise is organized across synchronized reading tracks switchable directly in the book header on any chapter page:

* **English**: Segmented English translation of :person:`Martin Luther D'Ooge <dooge>` (:cite:`1926 <dooge:1926>`).
* **Greek (``-el``)**: Verbatim polytonic Greek from :person:`Richard Hoche's <hoche>` Teubner critical edition (:cite:`1866 <hoche:1866>`).
* **Summary**: Structural mathematical synopses highlighting core ratio theorems, figurate gnomons, and the Ten Means.
* **Critical Notes**: Mathematical formalizations with exact ``SymPy`` and Rational Trigonometry proofs, alongside :person:`Boethius's <boethius>` Latin *De Institutione Arithmetica* parallels (:cite:`1867 <boethius:friedlein:1867>`).

2. Primary-Source Folio Milestones
----------------------------------

Marginal folio links anchor the text to primary print witnesses:

* **Hoche (1866)**: Clickable ``[Hoche p. N]`` markers correlate directly with Richard Hoche's 1866 Teubner Greek page numbering (pp. 1–147).
* **D'Ooge (1926)**: Page markers align with the University of Michigan Humanistic Series edition (pp. 181–286).
* **Folio Directives**: Header folio badges open high-resolution primary-source scans and verified facsimile pages.

3. Interactive Diagrams & Deductive Links
-----------------------------------------

* **Geometric Elements (``:g:``)**: Hovering or clicking any ``:g:`` reference illuminates corresponding vertices, polygonal pebble arrays, or cube edges in interactive SVGs.
* **Mathematical Assertions (``:eq:``)**: Inline formulas, such as Nicomachus's three unfolding rules :math:`(a, a+b, a+2b+c)` or the Sum-of-Cubes identity :math:`\sum k^3 = T_n^2`, connect directly to symbolic algebraic statements.
* **Justifications (``:just:``)**: Explicit deductive links cite foundational axioms or Euclidean predecessors (e.g. *Elements* IX.36 for perfect numbers).

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

The site search engine indexes ancient Greek terms, Boethian Latin vocabulary, and English analysis:

* Queries append ``?highlight=`` to URL paths.
* Matched terms are highlighted directly within the chapter and proposition text for rapid discovery.

5. Categories, Tags & Collection Views
--------------------------------------

Browse content through structured multi-dimensional taxonomy facets:

* Sidebar facets group material by domain: ratio theory, figurate numbers, means and proportions, and philosophy.
* Collection index views support **Cards**, **Banners**, and **List** presentation modes.

6. Scholarly Hover Cards & Dark Mode
------------------------------------

* **Prosopography (``:person:``)**: Hover over any ancient or modern authority to view historical dates, roles, and loci.
* **Bibliography (``:cite:``)**: Hover over citation keys for bibliographic records and library call numbers.
* **Glossary (``:term:``)**: Hover over technical terms for multilingual polytonic Greek, Boethian Latin, and English definitions.
* **Theme Toggle**: Switch effortlessly between Classical Light and Dark reading environments.

----

Python API & Command-Line Interface
-----------------------------------

The companion Python package :mod:`geometor.nicomachus` provides exact symbolic generation of ratio unfolding trees, figurate number gnomons, and the Ten Means:

.. code-block:: bash

   # Install within the GEOMETOR environment
   uv pip install -e .

.. code-block:: python

   from geometor.nicomachus.equality_tree import generate_equality_tree
   from geometor.nicomachus.ten_means_and_cube import verify_ten_means

   # Unfold inequality species from primordial Equality (1, 1, 1)
   tree = generate_equality_tree(depth=3)
   print("Equality tree roots verified:", len(tree) > 0)
