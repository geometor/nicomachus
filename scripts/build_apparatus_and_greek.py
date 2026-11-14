"""Deterministic generator for Book Codex apparatus RST pages and Hoche 1866 Greek tracks.

Reads ``resources/introductio_arithmetica/{concordance,citations,persons,glossary}.json``
and ``resources/introductio_arithmetica/sources/hoche_1866_1st1K_grc1.xml`` to build:

- ``docsrc/introductio_arithmetica/concordance.rst``
- ``docsrc/introductio_arithmetica/bibliography.rst``
- ``docsrc/introductio_arithmetica/persons.rst``
- ``docsrc/introductio_arithmetica/glossary.rst``
- ``docsrc/introductio_arithmetica/<unit>/<unit>-el.rst`` (4 Hoche 1866 Greek tracks)
"""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RES_DIR = ROOT / "resources" / "introductio_arithmetica"
BOOK_DIR = ROOT / "docsrc" / "introductio_arithmetica"
TEI_XML = RES_DIR / "sources" / "hoche_1866_1st1K_grc1.xml"
TEI_NS = {"t": "http://www.tei-c.org/ns/1.0"}

# Known TEI-XML keying artifacts verified against 300 DPI Hoche 1866 Teubner scans
GREEK_FIXES: tuple[tuple[str, str], ...] = (
    ("μεταβολ διὰ παντός", "μεταβολῇ διὰ παντός"),
    ("ἰδιό τητα", "ἰδιότητα"),
    ("παριπολαύει", "παραπολαύει"),
    ("περιληπιόν", "περιληπτόν"),
    ("διὰ παντὸς ὄμοια", "διὰ παντὸς ὅμοια"),
    ("προςηγόρευσεν", "προσηγόρευσεν"),
    ("προςήκοντος", "προσήκοντος"),
    ("ὡςαύτως", "ὡσαύτως"),
    ("ὡςαύτως", "ὡσαύτως"),
    ("ὥςπερ", "ὥσπερ"),
    ("εἰςαγωγή", "εἰσαγωγή"),
    ("εἰςαγωγῆς", "εἰσαγωγῆς"),
)


def apparatus_slug(key: str) -> str:
    """Match ``photon_platform.publish.roles.geometry._apparatus_slug``."""
    return re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")


def _rst_heading(title: str, char: str) -> str:
    line = char * len(title)
    return f"{title}\n{line}"


def _rst_overline_heading(title: str, char: str = "=") -> str:
    line = char * len(title)
    return f"{line}\n{title}\n{line}"


def build_concordance_rst() -> None:
    """Write ``docsrc/introductio_arithmetica/concordance.rst``."""
    data: dict[str, Any] = json.loads((RES_DIR / "concordance.json").read_text(encoding="utf-8"))
    loci: list[dict[str, Any]] = data["loci"]
    title = "Concordance"
    lines: list[str] = [
        ":navigation: footer",
        ":nav_title: Concordance",
        ":type: apparatus",
        f":title: {title}",
        "",
        ".. _concordance:",
        "",
        _rst_overline_heading(title),
        "",
        ".. rubric:: Hoche (1866) · D'Ooge (1926) · Boethius *De Institutione Arithmetica* (1867) · GEOMETOR Canon",

        "",
        (
            "Complete structural concordance mapping all **20 canonical chapter groups** across "
            "Books I–II of :person:`Nicomachus of Gerasa's <nicomachus>` *Introductio Arithmetica* "
            "to :person:`Richard Hoche's <hoche>` Teubner Greek pagination (:cite:`hoche:1866`), "
            ":person:`Martin Luther D'Ooge's <dooge>` English pagination (:cite:`dooge:1926`), "
            ":person:`Boethius's <boethius>` Latin *De Institutione Arithmetica* (:cite:`boethius:friedlein:1867`), "
            "and companion GEOMETOR Digital Scriptorium codices."
        ),
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 10 26 11 11 20 22",
        "",
        "   * - Chapters",
        "     - Theme & Codex Unit",
        "     - Hoche (1866)",
        "     - D'Ooge (1926)",
        "     - Boethius Parallel",
        "     - GEOMETOR Parallels",
    ]
    for item in loci:
        unit = item["unit"]
        unit_link = f":doc:`{item['title']} <{unit}/{unit}-en>`"
        parallels = "; ".join(f"``{p}``" for p in item["geometor_parallels"])
        lines.extend(
            [
                f"   * - **{item['locus']}**",
                f"     - {unit_link}",
                f"     - pp. {item['hoche_pages']}",
                f"     - pp. {item['dooge_pages']}",
                f"     - {item['boethius_parallel']}",
                f"     - {parallels}",
            ]
        )
    lines.append("")
    (BOOK_DIR / "concordance.rst").write_text("\n".join(lines), encoding="utf-8")


def build_bibliography_rst() -> None:
    """Write ``docsrc/introductio_arithmetica/bibliography.rst``."""
    citations: dict[str, dict[str, str]] = json.loads(
        (RES_DIR / "citations.json").read_text(encoding="utf-8")
    )
    title = "Bibliography"
    lines: list[str] = [
        ":navigation: header",
        ":order: 6",
        ":nav_title: Bibliography",
        ":type: apparatus",
        f":title: {title}",
        "",
        ".. _bibliography:",
        "",
        _rst_overline_heading(title),
        "",
        ".. rubric:: Critical Greek & Latin Editions, Public-Domain Translations, Ancient Commentaries & Canon Sources",
        "",
        (
            f"Authoritative editions, ancient commentaries, and companion mathematical treatises "
            f"(**{len(citations)} entries**) cited across *Introductio Arithmetica*."
        ),
        "",
    ]
    for key, entry in citations.items():
        slug = apparatus_slug(key)
        lines.extend(
            [
                f".. _cite-{slug}:",
                "",
                f"**{entry['author']} — {entry['work']} ({entry['year']})**",
                "",
                f"- **Citation Key**: ``{key}``  |  **Locus**: ``{entry['locus']}``",
                f"- **Significance**: {entry['note']}",
                "",
            ]
        )
    (BOOK_DIR / "bibliography.rst").write_text("\n".join(lines), encoding="utf-8")


def build_persons_rst() -> None:
    """Write ``docsrc/introductio_arithmetica/persons.rst``."""
    persons: dict[str, dict[str, Any]] = json.loads(
        (RES_DIR / "persons.json").read_text(encoding="utf-8")
    )
    title = "People"
    lines: list[str] = [
        ":navigation: header",
        ":order: 5",
        ":nav_title: People",
        ":type: apparatus",
        f":title: {title}",
        "",
        ".. _persons:",
        "",
        _rst_overline_heading(title),
        "",
        ".. rubric:: Prosopography of Pythagorean, Academic, Neoplatonic, Scholastic & Modern Authorities",
        "",
        (
            f"Chronological and philological register of **{len(persons)} authorities** cited by "
            "Nicomachus or central to the transmission and mathematical analysis of the "
            "*Introductio Arithmetica*."
        ),
        "",
    ]
    for key, entry in persons.items():
        slug = apparatus_slug(key)
        heading = f"{entry['name']} ({entry['dates']})"
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                _rst_heading(heading, "-"),
                "",
                f"- **Greek / Latin**: *{entry['greek']}*  |  **Role**: {entry['role']}",
                f"- **Nicomachus Loci**: ``{entry['hoche_loci']}``",
                "",
                entry["summary"],
                "",
            ]
        )
    (BOOK_DIR / "persons.rst").write_text("\n".join(lines), encoding="utf-8")


def build_glossary_rst() -> None:
    """Write ``docsrc/introductio_arithmetica/glossary.rst``."""
    glossary: dict[str, dict[str, str]] = json.loads(
        (RES_DIR / "glossary.json").read_text(encoding="utf-8")
    )
    title = "Glossary"
    lines: list[str] = [
        ":navigation: footer",
        ":nav_title: Glossary",
        ":type: apparatus",
        f":title: {title}",
        "",
        ".. _glossary:",
        "",
        _rst_overline_heading(title),
        "",
        ".. rubric:: Polytonic Greek, Boethian Latin & Arithmetical Lexicon of *Introductio Arithmetica*",
        "",
        (
            f"Systematic lexicon of **{len(glossary)} technical concepts** governing discrete multitude "
            "(*poson*), continuous magnitude (*pēlikon*), the four *mathemata* (*quadrivium*), "
            "ratio species, figurate *gnomons*, *Same* and *Other*, and the Ten Means."
        ),
        "",
    ]
    for key, entry in glossary.items():
        slug = apparatus_slug(key)
        heading = entry["headword"]
        lines.extend(
            [
                f".. _term-{slug}:",
                "",
                _rst_heading(heading, "-"),
                "",
                f"- **Greek**: *{entry['greek']}*  |  **Boethian Latin**: *{entry['latin']}*",
                f"- **Rendering**: {entry['english']}  |  **Hoche Loci**: ``{entry['hoche_loci']}``",
                "",
                entry["definition"],
                "",
            ]
        )
    (BOOK_DIR / "glossary.rst").write_text("\n".join(lines), encoding="utf-8")


def _extract_chapter_blocks(book_div: ET.Element, chapter_num: int) -> list[tuple[str | None, str]]:
    """Extract ``(hoche_pb, paragraph_greek)`` blocks for ``(book, chapter_num)``, omitting apparatus notes."""
    sec = book_div.find(f"t:div[@subtype='section'][@n='{chapter_num}']", TEI_NS)
    if sec is None:
        raise ValueError(f"Missing chapter {chapter_num} in TEI-XML")

    blocks: list[tuple[str | None, str]] = []
    current_pb: str | None = None

    def _walk(node: ET.Element, buf: list[str], pbs: list[str]) -> None:
        nonlocal current_pb
        local = node.tag.split("}")[-1]
        if local in ("note", "del"):
            return
        if local == "pb":
            pb_val = node.get("n")
            if pb_val:
                current_pb = pb_val
                pbs.append(pb_val)
        elif local == "lb":
            buf.append(" ")
        if local != "note" and local != "del" and node.text:
            buf.append(node.text)
        for child in node:
            _walk(child, buf, pbs)
            if child.tail:
                buf.append(child.tail)

    for child in sec:
        local = child.tag.split("}")[-1]
        if local == "pb" and child.get("n"):
            current_pb = child.get("n")
        elif local in ("p", "lg"):
            buf: list[str] = []
            pbs: list[str] = []
            pb_at_start = current_pb
            _walk(child, buf, pbs)
            raw = "".join(buf)
            # Rejoin hyphenated line breaks across <lb/> or <pb/>
            raw = re.sub(r"([α-ωΑ-Ωἀ-ῷ])[-‐]\s+([α-ωΑ-Ωἀ-ῷ])", r"\1\2", raw)
            text = re.sub(r"\s+", " ", raw).strip()
            for wrong, right in GREEK_FIXES:
                text = text.replace(wrong, right)
            if text:
                blocks.append((pb_at_start or (pbs[0] if pbs else None), text))
    return blocks


def build_greek_tracks() -> None:
    """Generate the four verbatim Hoche 1866 Greek ``-el.rst`` unit tracks."""
    root = ET.parse(TEI_XML).getroot()
    ed = root.find(".//t:div[@type='edition']", TEI_NS)
    if ed is None:
        raise RuntimeError("Missing edition div in Hoche TEI-XML")
    book1 = ed.find("t:div[@subtype='chapter'][@n='1']", TEI_NS)
    book2 = ed.find("t:div[@subtype='chapter'][@n='2']", TEI_NS)
    if book1 is None or book2 is None:
        raise RuntimeError("Missing Book I or Book II div in Hoche TEI-XML")

    units: list[dict[str, Any]] = [
        {
            "slug": "unit-1-philosophy-quadrivium-primes",
            "title": "Unit I — Philosophy, the Quadrivium, the Odd Sieve & Perfect Numbers — Greek (Hoche 1866)",
            "canonical_id": "Book I, Chs. 1–7, 13, 16",
            "folio": "Hoche pp. 1–14, 29–36, 39–44",
            "rubric": "Editio Teubneriana (Ricardus Hoche, 1866) · Book I, Chs. 1–7, 13, 16",
            "figure": "quadrivium-tetrad.svg",
            "figure_alt": "Nicomachus's Quadrivium Bifurcation of Quantity",
            "figure_caption": "Book I, Chs. 3–5: Ontological division of Quantity into Multitude (poson) and Magnitude (pēlikon), generating Arithmetic, Music, Geometry, and Astronomy.",
            "chapters": [
                (1, 1, "Book I, Ch. 1 — Philosophy as Love of Wisdom & Immaterial Reality (Hoche pp. 1–3)"),
                (1, 2, "Book I, Ch. 2 — Eternal Being vs. Bodily Flux; Magnitude & Multitude (Hoche pp. 3–5)"),
                (1, 3, "Book I, Ch. 3 — The Four Sister Sciences (Mathemata / Quadrivium) & Archytas (Hoche pp. 5–9)"),
                (1, 4, "Book I, Ch. 4 — Ontological Priority of Arithmetic via Co-Removal (Hoche pp. 9–11)"),
                (1, 5, "Book I, Ch. 5 — Arithmetic Prior to Music as Mother of Sciences (Hoche pp. 11–12)"),
                (1, 6, "Book I, Ch. 6 — Number as Cosmic Exemplar in the Mind of the Creator (Hoche p. 12)"),
                (1, 7, "Book I, Ch. 7 — Definition of Number, Even, and Odd (Hoche pp. 13–14)"),
                (1, 13, "Book I, Ch. 13 — Prime Numbers & the Odd Sieve (Koskinon) of Eratosthenes (Hoche pp. 29–36)"),
                (1, 16, "Book I, Ch. 16 — Perfect Numbers (6, 28, 496, 8128) & Euclid's Law (Hoche pp. 39–44)"),
            ],
        },
        {
            "slug": "unit-2-inequality-equality-tree",
            "title": "Unit II — Five Species of Inequality & the Equality Unfolding Tree — Greek (Hoche 1866)",
            "canonical_id": "Book I, Chs. 17–23",
            "folio": "Hoche pp. 44–72",
            "rubric": "Editio Teubneriana (Ricardus Hoche, 1866) · Book I, Chs. 17–23",
            "figure": "equality-unfolding-tree.svg",
            "figure_alt": "Nicomachus's Equality Unfolding Tree from (1, 1, 1)",
            "figure_caption": "Book I, Ch. 23: The three prostagma commands (a, a+b, a+2b+c) and sibling reversal unfolding every inequality species from primordial Equality (1, 1, 1).",
            "chapters": [
                (1, 17, "Book I, Ch. 17 — Absolute vs. Relative Quantity; Equality & Five Species of Inequality (Hoche pp. 44–46)"),
                (1, 18, "Book I, Ch. 18 — The Multiple Species (Pollaplasios: Double, Triple, Quadruple) (Hoche pp. 46–49)"),
                (1, 19, "Book I, Ch. 19 — The Superparticular Species (Epimorios: 3:2, 4:3, 9:8) (Hoche pp. 49–55)"),
                (1, 20, "Book I, Ch. 20 — The Superpartient Species (Epimerēs) (Hoche pp. 55–58)"),
                (1, 21, "Book I, Ch. 21 — The Multiple Superparticular Species (Hoche pp. 58–61)"),
                (1, 22, "Book I, Ch. 22 — The Multiple Superpartient Species & Tabular Synthesis (Hoche pp. 61–64)"),
                (1, 23, "Book I, Ch. 23 — The Rule of Three Terms Unfolding All Inequalities from Equality (Hoche pp. 64–72)"),
            ],
        },
        {
            "slug": "unit-3-figurate-gnomons-cubes",
            "title": "Unit III — Inverse Reduction, Polygonal Gnomons, Same/Other & Sum of Cubes — Greek (Hoche 1866)",
            "canonical_id": "Book II, Chs. 1–2, 6–20",
            "folio": "Hoche pp. 73–76, 82–119",
            "rubric": "Editio Teubneriana (Ricardus Hoche, 1866) · Book II, Chs. 1–2, 6–20",
            "figure": "nicomachus-sum-of-cubes.svg",
            "figure_alt": "Nicomachus's Sum-of-Cubes Theorem via Odd Blocks and Gnomons",
            "figure_caption": "Book II, Ch. 20: Consecutive odd-number blocks {1}, {3,5}, {7,9,11}, {13,15,17,19} sum to cubes k^3 and tile the squared triangular number T_n^2.",
            "chapters": [
                (2, 1, "Book II, Ch. 1 — Element as Minimum & Equality as Mother of All Ratios (Hoche pp. 73–74)"),
                (2, 2, "Book II, Ch. 2 — Inverse Three-Subtraction Reduction to Equality (1, 1, 1) (Hoche pp. 74–76)"),
                (2, 6, "Book II, Ch. 6 — Alpha-Pebble Notation, Monad, and Dimensional Progression (Hoche pp. 82–84)"),
                (2, 7, "Book II, Ch. 7 — Point, Line, Interval, and Triangle as Primordial Plane Figure (Hoche pp. 84–86)"),
                (2, 8, "Book II, Ch. 8 — Triangular Numbers & Natural-Number Gnomons (Hoche pp. 86–88)"),
                (2, 9, "Book II, Ch. 9 — Square Numbers & Odd-Number Gnomons (Hoche pp. 88–91)"),
                (2, 10, "Book II, Ch. 10 — Pentagonal Numbers & Arithmetic Gnomons of Difference 3 (Hoche pp. 91–93)"),
                (2, 11, "Book II, Ch. 11 — Hexagonal, Heptagonal & General s-Gonal Gnomon Law (s - 2) (Hoche pp. 93–96)"),
                (2, 12, "Book II, Ch. 12 — Decomposition of Squares and Polygons into Triangles (Hoche pp. 96–99)"),
                (2, 13, "Book II, Ch. 13 — Solid Pyramidal Numbers on Polygonal Bases (Hoche pp. 99–102)"),
                (2, 14, "Book II, Ch. 14 — Truncated, Bi-Truncated & Tri-Truncated Pyramids (Hoche pp. 102–104)"),
                (2, 15, "Book II, Ch. 15 — Cubes, Beams, Bricks, Wedges & Scalene Solids (Hoche pp. 104–106)"),
                (2, 16, "Book II, Ch. 16 — Promecic & Heteromecic Numbers vs. Squares (Hoche pp. 106–109)"),
                (2, 17, "Book II, Ch. 17 — Spherical/Circular Numbers (5, 6) & Plato's Same and Other (Hoche pp. 109–112)"),
                (2, 18, "Book II, Ch. 18 — Pythagorean Dualities of Same (Odd/Square) & Other (Even/Oblong) (Hoche pp. 112–115)"),
                (2, 19, "Book II, Ch. 19 — Alternating Weave & Harmonic Identities of Squares and Oblongs (Hoche pp. 115–117)"),
                (2, 20, "Book II, Ch. 20 — Generation of Cubes from Consecutive Odd Blocks (Hoche pp. 117–119)"),
            ],
        },
        {
            "slug": "unit-4-ten-means-cube-harmony",
            "title": "Unit IV — The Ten Neo-Pythagorean Means & the Cube's Most Perfect Proportion — Greek (Hoche 1866)",
            "canonical_id": "Book II, Chs. 21–29",
            "folio": "Hoche pp. 119–147",
            "rubric": "Editio Teubneriana (Ricardus Hoche, 1866) · Book II, Chs. 21–29",
            "figure": "cube-most-perfect-proportion.svg",
            "figure_alt": "The Cube and Most Perfect Proportion 6 : 8 :: 9 : 12",
            "figure_caption": "Book II, Ch. 29: The Cube's 6 faces, 8 vertices, and 12 edges embody the Most Perfect Proportion 6 : 8 :: 9 : 12 uniting arithmetic (9), harmonic (8), and geometric (6*12 = 8*9 = 72) symmetry with the musical octave.",
            "chapters": [
                (2, 21, "Book II, Ch. 21 — Proportion (Analogia) Strictly & Broadly; The Three Classical Means (Hoche pp. 119–122)"),
                (2, 22, "Book II, Ch. 22 — Continuous & Disjunct Proportion; Three vs. Four Terms (Hoche pp. 122–123)"),
                (2, 23, "Book II, Ch. 23 — The Arithmetic Proportion & Difference Laws (a*c + d^2 = b^2) (Hoche pp. 123–126)"),
                (2, 24, "Book II, Ch. 24 — The Geometric Proportion, Platonic Solid Bonding & Square Differences (Hoche pp. 126–131)"),
                (2, 25, "Book II, Ch. 25 — The Harmonic Proportion (Subcontrary) & Extreme-Product Law (Hoche pp. 131–134)"),
                (2, 26, "Book II, Ch. 26 — Musical Consonances & Philolaus's Cube as Geometric Harmony (Hoche pp. 134–136)"),
                (2, 27, "Book II, Ch. 27 — Insertion of the Three Classical Means Between Two Extremes (Hoche pp. 136–139)"),
                (2, 28, "Book II, Ch. 28 — The Seven Additional Means Completing the Ten Proportions (Hoche pp. 139–144)"),
                (2, 29, "Book II, Ch. 29 — The Most Perfect Proportion (6 : 8 :: 9 : 12) (Hoche pp. 144–147)"),
            ],
        },
    ]

    for unit in units:
        slug = unit["slug"]
        unit_dir = BOOK_DIR / slug
        unit_dir.mkdir(parents=True, exist_ok=True)
        lines: list[str] = [
            ":layout: book",
            ":type: el",
            f":title: {unit['title']}",
            f":canonical_id: {unit['canonical_id']}",
            f":original_id: {unit['folio']}",
            f":folio: {unit['folio']}",
            "",
            f".. _{slug}-el:",
            "",
            _rst_overline_heading(unit["title"]),
            "",
            f".. rubric:: {unit['rubric']}",
            "",
            f".. picture:: /_static/figures/{unit['figure']}",
            f"   :alt: {unit['figure_alt']}",
            f"   :caption: {unit['figure_caption']}",
            "",
        ]
        seen_pb: str | None = None
        for bnum, cnum, ch_heading in unit["chapters"]:
            bdiv = book1 if bnum == 1 else book2
            blocks = _extract_chapter_blocks(bdiv, cnum)
            lines.extend(
                [
                    f".. _nicomachus-el-{bnum}-{cnum}:",
                    "",
                    _rst_heading(ch_heading, "-"),
                    "",
                    f"*Nicomachi Geraseni Introductionis Arithmeticae Liber {'I' if bnum == 1 else 'II'}, Cap. {cnum} (ed. R. Hoche, Teubner, 1866)*",
                    "",
                ]
            )
            for pb, para in blocks:
                if pb and pb != seen_pb:
                    seen_pb = pb
                    lines.extend(
                        [
                            f".. _hoche-el-p-{pb}:",
                            "",
                            f".. folio:: Hoche p. {pb}",
                            "",
                        ]
                    )
                lines.extend([para, ""])
        (unit_dir / f"{slug}-el.rst").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """Build all four apparatus RST pages and all four Hoche Greek ``-el.rst`` tracks."""
    build_concordance_rst()
    build_bibliography_rst()
    build_persons_rst()
    build_glossary_rst()
    build_greek_tracks()
    print("Built 4 apparatus RST pages and 4 Hoche 1866 Greek -el.rst tracks.")


if __name__ == "__main__":
    main()
