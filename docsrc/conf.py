"""Sphinx configuration for GEOMETOR • nicomachus (Introductio Arithmetica)."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.nicomachus as module  # noqa: E402
from geometor.nicomachus.sphinx_ext import (  # noqa: E402
    configure_local_intersphinx,
    register_greek_book_track,
)

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "nicomachus"
repo_name = "nicomachus"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

project = "GEOMETOR • nicomachus"
author = "Nicomachus of Gerasa • Ed. GEOMETOR"
copyright = "2026, GEOMETOR • Hoche Teubner (1866) & D'Ooge Michigan (1926) Critical Codex"

register_greek_book_track()
if "geometor.nicomachus.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.nicomachus.sphinx_ext")  # noqa: F405

configure_local_intersphinx(intersphinx_mapping, _REPO_ROOT)  # noqa: F405

html_theme = "foundation"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_logo = None
autoapi_add_toctree_entry = False
autoapi_options = [opt for opt in autoapi_options if opt != "imported-members"]  # noqa: F405
napoleon_use_ivar = True
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]
