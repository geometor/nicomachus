# GEOMETOR • nicomachus

Context and architectural guide for **Nicomachus of Gerasa (c. 60–120 CE): *Introduction to Arithmetic* (*Ἀριθμητικὴ Εἰσαγωγή* / *Introductio Arithmetica*, Books I–II)**.

## Purpose & Canon Role

`geometor/nicomachus` anchors Neo-Pythagorean number theory, the ontological charter of the **Four Mathematical Sciences** (*Mathemata* / Boethius's *Quadrivium*), ratio generation from Equality `(1, 1, 1)`, figurate gnomon geometry, the Ten Means, and the Cube's *Most Perfect Proportion* (`6 : 8 :: 9 : 12`) across the GEOMETOR Digital Scriptorium—bridging `plato`, `aristotle`, `euclid`/`elements`, `pappus`, `proclus`, `aquinas`, `fibonacci`, `pacioli`, `kepler`, and `wildberger`.

## Architecture & Strict Mandates

1. **4-Track Synchronized Book Codex (`docsrc/introductio_arithmetica/`)**:
   - `:layout: book` compiled via `publish build` with runtime Greek track registration (`geometor.nicomachus.sphinx_ext`).
   - Four tracks per unit: `-en.rst` (D'Ooge 1926 PD English), `-el.rst` (Hoche 1866 Teubner Greek), `-summary.rst`, and `-notes.rst` (commentary, Boethius *De Inst. Arith.* parallels, and interactive `.euclid-graphic` SVGs wired with `:g:` / `:eq:`).
   - **Zero `py_file` directives inside `docsrc/introductio_arithmetica/`**.
2. **100% Exact Symbolic Precision (`src/geometor/nicomachus/`)**:
   - Every coordinate, quadrance, spread, cross-ratio, ratio classification, figurate number, mean, and perfect number uses exact `SymPy` rationals (`sp.Integer`, `sp.Rational`) and algebraic radicals (`sp.sqrt`)—zero `float` or `sp.Float` in `Model`.
   - `Model(..., auto_intersect=False)` with alphanumeric point IDs (no underscores).
3. **Multimodal Scan Vision Over OCR**:
   - Archival PDFs (`resources/introductio_arithmetica/pdfs/`, git-ignored) are verified strictly by inspecting rendered 300 DPI page images (`view_file`), never via `pdftotext` or OCR text extraction.
   - Page offsets: Hoche 1866 (`PDF = Hoche + 18`), D'Ooge 1926 (`PDF = DOoge + 16`).

## Key Modules & Commands

- `src/geometor/nicomachus/equality_tree.py` — Ratio species, Equality tree `(1,1,1)`, inverse reduction, Odd Sieve, perfect numbers.
- `src/geometor/nicomachus/figurate_gnomons.py` — Polygonal gnomons, triangle decomposition, Same/Other, Sum-of-Cubes theorem & `Model` proof.
- `src/geometor/nicomachus/ten_means_and_cube.py` — Semicircle `A, G, H` construction, 10 Neo-Pythagorean means, Cube `6 : 8 :: 9 : 12` harmony.
- `scripts/build_figures.py` — Generates all 9 theme-adaptive `.euclid-graphic` SVGs into `docsrc/_static/figures/`.
