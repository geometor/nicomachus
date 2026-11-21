"""Tests for Book Codex integrity, Sphinx Greek track, SVGs, apparatus, and CLI."""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from types import SimpleNamespace

from geometor.nicomachus.__main__ import main as cli_main
from geometor.nicomachus.sphinx_ext import register_greek_book_track

ROOT = Path(__file__).resolve().parents[1]
RES_DIR = ROOT / "resources" / "introductio_arithmetica"
BOOK_DIR = ROOT / "docsrc" / "introductio_arithmetica"
FIGURES_DIR = ROOT / "docsrc" / "_static" / "figures"

EXPECTED_FIGURES = (
    "quadrivium-tetrad.svg",
    "sieve-perfect-numbers.svg",
    "five-species-ratios.svg",
    "equality-unfolding-tree.svg",
    "polygonal-alpha-gnomons.svg",
    "heteromecic-same-other.svg",
    "nicomachus-sum-of-cubes.svg",
    "three-classical-means-semicircle.svg",
    "cube-most-perfect-proportion.svg",
)

EXPECTED_BOOKS = {
    "book_01": [f"ch_{i:02d}" for i in range(1, 24)],
    "book_02": [f"ch_{i:02d}" for i in range(1, 30)],
}


def _slug(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")


def test_sources_manifest_and_tei_sha256() -> None:
    """Verify Hoche 1866 TEI-XML witness SHA-256 matches sources_manifest.json."""
    manifest = json.loads((RES_DIR / "sources_manifest.json").read_text(encoding="utf-8"))
    tei_entry = manifest["primary_sources"][0]
    tei_path = ROOT / tei_entry["local_path"]
    assert tei_path.is_file()
    raw = tei_path.read_bytes()
    assert len(raw) == tei_entry["bytes"]
    assert hashlib.sha256(raw).hexdigest() == tei_entry["sha256"]


def test_apparatus_jsons_and_rst_anchors() -> None:
    """Verify every citation, person, and glossary entry has its exact RST anchor target."""
    citations = json.loads((RES_DIR / "citations.json").read_text(encoding="utf-8"))
    persons = json.loads((RES_DIR / "persons.json").read_text(encoding="utf-8"))
    glossary = json.loads((RES_DIR / "glossary.json").read_text(encoding="utf-8"))
    concordance = json.loads((RES_DIR / "concordance.json").read_text(encoding="utf-8"))
    assert len(citations) >= 15
    assert len(persons) >= 25
    assert len(glossary) >= 25
    assert len(concordance["loci"]) >= 20

    bib_rst = (BOOK_DIR / "bibliography.rst").read_text(encoding="utf-8")
    per_rst = "\n".join(p.read_text(encoding="utf-8") for p in sorted((BOOK_DIR / "people").glob("*.rst")))
    glo_rst = (BOOK_DIR / "glossary.rst").read_text(encoding="utf-8")

    for key in citations:
        assert f".. _cite-{_slug(key)}:" in bib_rst
    for key in persons:
        assert f".. _person-{_slug(key)}:" in per_rst
    for key in glossary:
        assert f".. _term-{_slug(key)}:" in glo_rst


def test_all_nine_svgs_valid_xml_and_wired_refs() -> None:
    """Verify all 9 .euclid-graphic SVGs parse cleanly and carry every :g: data-ref target."""
    svg_refs: dict[str, set[str]] = {}
    for fname in EXPECTED_FIGURES:
        fpath = FIGURES_DIR / fname
        assert fpath.is_file(), f"Missing {fname}"
        tree = ET.parse(fpath)
        root = tree.getroot()
        assert "euclid-graphic" in root.attrib.get("class", "")
        gid = root.attrib.get("data-graphic-id", "")
        assert gid == fname.removesuffix(".svg")
        refs = {el.attrib["data-ref"] for el in root.iter() if "data-ref" in el.attrib}
        assert len(refs) >= 3
        svg_refs[gid] = refs

    # Verify every :g:`label <gid:REF>` in docsrc/ resolves to an actual data-ref in gid.svg
    g_pattern = re.compile(r":g:`[^`]*<([a-z0-9-]+):([A-Z0-9_]+)>`")
    for rst_path in (ROOT / "docsrc").rglob("*.rst"):
        text = rst_path.read_text(encoding="utf-8")
        for gid, ref_id in g_pattern.findall(text):
            assert gid in svg_refs, f"Unknown graphic id {gid} in {rst_path}"
            assert ref_id in svg_refs[gid], f"Missing data-ref={ref_id} on {gid}.svg in {rst_path}"


def test_four_track_units_and_zero_py_file_in_codex() -> None:
    """Verify Books I-II containers, 4 atomic section directories, tracks, and zero py_file."""
    for book, sections in EXPECTED_BOOKS.items():
        book_index = BOOK_DIR / book / "index.rst"
        assert book_index.is_file(), f"Missing book index {book_index}"
        assert book_index.stat().st_size > 500

        for sec in sections:
            sec_dir = BOOK_DIR / book / sec
            assert sec_dir.is_dir(), f"Missing section dir {sec_dir}"
            for track_file_name in ("index.rst", "el.rst", "summary.rst", "notes.rst"):
                track_file = sec_dir / track_file_name
                assert track_file.is_file(), f"Missing track {track_file}"
                assert track_file.stat().st_size > 500

    for rst_path in BOOK_DIR.rglob("*.rst"):
        content = rst_path.read_text(encoding="utf-8")
        assert ".. py_file::" not in content, f"Forbidden py_file directive in {rst_path}"


def test_sphinx_ext_greek_track_and_cli(capsys: object) -> None:
    """Verify runtime Greek track registration on a mock book module and CLI execution."""
    mock_book = SimpleNamespace(
        _TRACK_SUFFIX_PATTERNS=[(r"^(.+)[._-]en$", "en", "English")],
        _AUX_TRACK_BASENAMES={"summary", "notes"},
        _AUX_TRACK_PATTERNS=[],
        _extract_unit_stem=lambda base, _d: re.sub(r"-(en|el|summary|notes)$", "", base),
        detect_companion_tracks=lambda _env, page: [
            {"key": "en", "label": "English", "docname": page, "active": True},
            {
                "key": "summary",
                "label": "Summary",
                "docname": page.replace("-en", "-summary"),
                "active": False,
            },
        ],
    )
    assert register_greek_book_track(mock_book) is True
    env = SimpleNamespace(
        found_docs={
            "introductio_arithmetica/u1/u1-en",
            "introductio_arithmetica/u1/u1-el",
            "introductio_arithmetica/u1/u1-summary",
        }
    )
    tracks = mock_book.detect_companion_tracks(env, "introductio_arithmetica/u1/u1-el")
    keys = [t["key"] for t in tracks]
    assert keys == ["en", "el", "summary"]
    assert tracks[1]["active"] is True

    cli_main()
    out = getattr(capsys, "readouterr")().out
    assert "Nicomachus" in out
