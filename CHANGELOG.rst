=========
changelog
=========

0.1.5 (2026-11-15)
------------------

- Rebuilt codex documentation with ``photon-platform/publish`` ``v0.4.6`` so every inline ``.euclid-graphic`` SVG carries explicit ``viewBox`` pixel dimensions, per-diagram scoped ``<style>`` rules, and Nocturnal Codex dark/light theme parity.

0.1.4 (2026-11-15)
------------------

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.3 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2 (2026-11-14)
------------------

- Standardized Book Title Page, top-level header navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author and Translator profiles in People, and English structural terminology.

0.1.1 (2026-11-13)
------------------

- Curated and mapped primary-source folio links across *Introduction to Arithmetic* Books I–II (96/96 directives and 16/16 badges resolved).

0.1.0 (2026-11-12)
------------------

* **Initial Critical Book Codex (`:layout: book`)**: Synchronized four-track Digital Scriptorium edition of **Nicomachus of Gerasa's *Introduction to Arithmetic* (*Ἀριθμητικὴ Εἰσαγωγή*, Books I–II)** uniting **Richard Hoche's 1866 Teubner Greek critical edition** (`-el`), **Martin Luther D'Ooge's 1926 University of Michigan English translation** (`-en`), structural synopses (`-summary`), and mathematical-philological commentary (`-notes`) cross-referenced to **Boethius's *De Institutione Arithmetica*** (ed. Friedlein 1867) and the GEOMETOR canon.
* **Exact Symbolic Engine (`geometor.nicomachus`)**: Implemented 100% exact `SymPy` and `geometor.model` modules (`equality_tree`, `figurate_gnomons`, `ten_means_and_cube`) proving Nicomachus's Rule of Three Terms (Book I, Ch. 23) and inverse reduction to Equality `(1, 1, 1)` (Book II, Chs. 1–2), Odd Sieve of Eratosthenes (I.13), Euclid–Nicomachus perfect numbers (I.16), polygonal gnomon generation and triangular decomposition (II.7–12), Same/Other square–heteromecic weave (II.17–19), Nicomachus's Sum-of-Cubes Theorem (II.20), the Ten Neo-Pythagorean Means & Pappus semicircle construction (II.21–28), and the Cube's *Most Perfect Proportion* `6 : 8 :: 9 : 12` (II.29).
* **9 Theme-Adaptive `.euclid-graphic` Diagrams**: Deterministic vector builder (`scripts/build_figures.py`) producing nine interactive light/dark SVGs wired via `:g:` and `:eq:` roles with zero embedded `py_file` scripts in treatise tracks.
* **Critical Apparatus & Concordances**: Added `persons.json` (27 authorities), `citations.json` (17 primary editions & treatises), `glossary.json` (27 technical Greek/Latin terms), `concordance.json` (20 canonical chapter loci), and SHA-256 `sources_manifest.json`.
