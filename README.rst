=====================
GEOMETOR • nicomachus
=====================

**Critical Four-Track Digital Scriptorium Book Codex & Exact Symbolic Arithmetical Geometry Suite for Nicomachus of Gerasa's** *Introduction to Arithmetic* (*Ἀριθμητικὴ Εἰσαγωγή* / *Introductio Arithmetica*, Books I–II).

Overview
--------

``geometor/nicomachus`` pairs a folio-verified, public-domain four-track **Book Codex** (``:layout: book`` compiled via ``photon-platform/publish``) with a 100% exact ``SymPy`` and ``geometor.model`` constructive proof library:

* **Primary Textual Witnesses**:
  - **Greek (``-el``)**: Richard Hoche (ed.), *Nicomachi Geraseni Pythagorei Introductionis Arithmeticae Libri II* (Leipzig: B. G. Teubner, 1866).
  - **English (``-en``)**: Martin Luther D'Ooge (trans.), F. E. Robbins & L. C. Karpinski, *Nicomachus of Gerasa: Introduction to Arithmetic* (New York: Macmillan / University of Michigan Studies, Vol. XVI, 1926).
  - **Latin Quadrivium Parallel**: Boethius, *De Institutione Arithmetica* (ed. Gottfried Friedlein, Leipzig: B. G. Teubner, 1867).
* **Exact Symbolic Modules (`src/geometor/nicomachus/`)**:
  - ``equality_tree``: Five species of relative inequality, Nicomachus's Rule of Three Terms unfolding every ratio from Equality ``(1, 1, 1)`` (Book I, Ch. 23), inverse reduction ``(x, y, z) -> (1, 1, 1)`` (Book II, Chs. 1–2), Odd Sieve of Eratosthenes (I.13), and Euclid–Nicomachus perfect numbers ``6, 28, 496, 8128`` (I.16).
  - ``figurate_gnomons``: General :math:`s`-gonal numbers by arithmetic gnomons, polygonal decomposition into triangles, Plato's *Same* (:math:`n^2`) & *Other* (:math:`n(n+1)`), solid pyramidal numbers, and Nicomachus's Sum-of-Cubes Theorem (:math:`\sum_{k=1}^n k^3 = T_n^2`, Book II, Ch. 20).
  - ``ten_means_and_cube``: Exact ``geometor.model`` semicircle construction of Arithmetic, Geometric, and Harmonic means over :math:`\mathbb{Q}(\sqrt{ab})`, complete system of all 10 Neo-Pythagorean means (Book II, Chs. 21–28), and the Cube's *Most Perfect Proportion* ``6 : 8 :: 9 : 12`` (Book II, Ch. 29).

Development & Verification (Python 3.13 + ``uv``)
-------------------------------------------------

.. code-block:: bash

   # Lint & type/docstring check
   ruff check src scripts demos tests

   # Run symbolic & codex test suite
   uv run --no-sync pytest

   # Regenerate deterministic .euclid-graphic SVGs
   uv run --no-sync python3 scripts/build_figures.py

   # Compile Sphinx Book Codex into docs/
   publish build
