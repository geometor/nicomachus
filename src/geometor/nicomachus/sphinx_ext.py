"""Runtime Sphinx & photon-platform/publish integration for GEOMETOR Nicomachus.

Registers the ``el`` ("Greek (Hoche 1866)") companion track in ``photon_platform.publish.book``
at build time (without modifying any sibling repository) and configures offline-safe local
``intersphinx`` inventories for companion GEOMETOR codices.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

_PATCHED_ATTR = "_geometor_nicomachus_el_patched"
_EL_LABEL = "Greek (Hoche 1866)"
_EL_SUFFIX_ENTRY = (r"^(.+)[._-]el$", "el", _EL_LABEL)
_EL_AUX_PATTERN = re.compile(r"^.+[._-]el$")

SISTER_REPOS: tuple[str, ...] = (
    "plato",
    "euclid",
    "elements",
    "pappus",
    "proclus",
    "aristotle",
    "aquinas",
    "fibonacci",
    "pacioli",
    "kepler",
    "hoenen",
)


def register_greek_book_track(book_mod: Any = None) -> bool:
    """Extend ``photon_platform.publish.book`` to recognize ``<stem>-el`` Greek tracks.

    Args:
        book_mod: Optional pre-imported ``photon_platform.publish.book`` module (or mock
            object in unit tests). When ``None``, imports it dynamically.

    Returns:
        ``True`` if ``photon_platform.publish.book`` is available and patched, ``False``
        otherwise.
    """
    if book_mod is None:
        try:
            from photon_platform.publish import book as imported_book
        except ImportError:
            return False
        book_mod = imported_book

    if getattr(book_mod, _PATCHED_ATTR, False):
        return True

    suffix_patterns = getattr(book_mod, "_TRACK_SUFFIX_PATTERNS", None)
    if isinstance(suffix_patterns, list) and not any(k == "el" for _, k, _ in suffix_patterns):
        suffix_patterns.append(_EL_SUFFIX_ENTRY)

    aux_basenames = getattr(book_mod, "_AUX_TRACK_BASENAMES", None)
    if isinstance(aux_basenames, set):
        aux_basenames.add("el")

    aux_patterns = getattr(book_mod, "_AUX_TRACK_PATTERNS", None)
    if isinstance(aux_patterns, list) and not any(p.pattern == _EL_AUX_PATTERN.pattern for p in aux_patterns):
        aux_patterns.append(_EL_AUX_PATTERN)

    orig_detect = getattr(book_mod, "detect_companion_tracks")
    extract_stem = getattr(book_mod, "_extract_unit_stem")

    def _detect_with_greek(env: Any, pagename: str) -> list[dict[str, Any]]:
        found_docs: set[str] = set(getattr(env, "found_docs", set()))
        if not found_docs:
            return []

        doc_dir = os.path.dirname(pagename)
        basename = os.path.basename(pagename)
        stem = str(extract_stem(basename, doc_dir))
        if basename == "el" and doc_dir:
            stem = os.path.basename(doc_dir)

        def _qual(local_name: str) -> str:
            return f"{doc_dir}/{local_name}" if doc_dir else local_name

        is_unit_dir = not doc_dir or stem == os.path.basename(doc_dir)
        el_cands = [_qual(f"{stem}.el"), _qual(f"{stem}_el"), _qual(f"{stem}-el"), _qual(f"{stem}-greek")]
        if is_unit_dir:
            el_cands.extend([_qual("el"), _qual("greek")])

        el_doc = next((cand for cand in el_cands if cand in found_docs), None)
        probe_page = pagename
        if el_doc and pagename == el_doc:
            en_cand = next(
                (
                    c
                    for c in (_qual(f"{stem}-en"), _qual(f"{stem}_en"), _qual(f"{stem}.en"), _qual("index"), _qual("en"))
                    if c in found_docs
                ),
                None,
            )
            if en_cand:
                probe_page = en_cand

        tracks: list[dict[str, Any]] = list(orig_detect(env, probe_page))
        if el_doc is None:
            return tracks

        if not tracks:
            en_cands = [_qual(f"{stem}.en"), _qual(f"{stem}_en"), _qual(f"{stem}-en")]
            if is_unit_dir:
                en_cands.extend([_qual("index"), _qual("en")])
            en_doc = next((cand for cand in en_cands if cand in found_docs), None)
            if en_doc and en_doc != el_doc:
                return [
                    {
                        "key": "en",
                        "label": "English",
                        "docname": en_doc,
                        "active": en_doc == pagename,
                    },
                    {
                        "key": "el",
                        "label": _EL_LABEL,
                        "docname": el_doc,
                        "active": el_doc == pagename,
                    },
                ]
            return []

        updated: list[dict[str, Any]] = []
        inserted_el = False
        el_entry: dict[str, Any] = {
            "key": "el",
            "label": _EL_LABEL,
            "docname": el_doc,
            "active": el_doc == pagename,
        }
        for tr in tracks:
            if tr.get("docname") == el_doc:
                continue
            item = dict(tr)
            item["active"] = item.get("docname") == pagename
            updated.append(item)
            if (item.get("key") in ("en", "index") or item.get("label") == "English") and not inserted_el:
                updated.append(el_entry)
                inserted_el = True

        if not inserted_el:
            updated.insert(0, el_entry)

        return updated if len(updated) >= 2 else []

    setattr(book_mod, "detect_companion_tracks", _detect_with_greek)
    setattr(book_mod, _PATCHED_ATTR, True)
    return True


def configure_local_intersphinx(intersphinx_mapping: dict[str, Any], project_root: Path) -> None:
    """Bind local ``objects.inv`` files for sister GEOMETOR codices and drop unreachable remote targets.

    Args:
        intersphinx_mapping: Sphinx ``intersphinx_mapping`` dictionary to update in place.
        project_root: Root directory of ``geometor/nicomachus``.
    """
    geometor_dir = project_root.parent
    for sister in SISTER_REPOS:
        inv = geometor_dir / sister / "docs" / "objects.inv"
        if inv.is_file():
            intersphinx_mapping[sister] = (
                f"https://geometor.github.io/{sister}",
                str(inv.resolve()),
            )
    for key in list(intersphinx_mapping.keys()):
        _uri, inv_target = intersphinx_mapping[key]
        if inv_target is None:
            intersphinx_mapping.pop(key, None)


def setup(app: Any) -> dict[str, Any]:
    """Sphinx extension entry point.

    Args:
        app: Active Sphinx application instance.

    Returns:
        Sphinx extension metadata dictionary.
    """
    _ = app
    register_greek_book_track()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
