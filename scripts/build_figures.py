"""Deterministic builder for all 9 theme-adaptive ``.euclid-graphic`` SVGs in GEOMETOR Nicomachus.

Generates crisp, self-contained scholarly diagrams into ``docsrc/_static/figures/`` with:

- ``class="euclid-graphic"`` root ``<svg>`` styling, SVG 1.1 fallback CSS, and CSS custom properties
  for dark/light themes (mirrored in ``docsrc/_static/custom.css`` for inline Sphinx ``.. picture::``)
- ``<defs>`` tick markers ``#geom-tick-1``, ``#geom-tick-2``, ``#geom-tick-3`` (``userSpaceOnUse``)
- 3-vertex midpoint ``<path d="M x1 y1 L mx my L x2 y2" fill="none" marker-mid="url(#geom-tick-k)"/>``
- ``data-ref`` attributes and ``<g id="highlights">`` layers wired to ``:g:`` tokens in RST prose
"""

from __future__ import annotations

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = ROOT / "docsrc" / "_static" / "figures"

SHARED_STYLE_AND_DEFS = """  <defs>
    <marker id="geom-tick-1" viewBox="-6 -8 12 16" refX="0" refY="0" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="16" orient="auto">
      <line x1="0" y1="-5.5" x2="0" y2="5.5" stroke="#e2b553" stroke-width="1.6" stroke-linecap="round"/>
    </marker>
    <marker id="geom-tick-2" viewBox="-8 -8 16 16" refX="0" refY="0" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto">
      <line x1="-2.4" y1="-5.5" x2="-2.4" y2="5.5" stroke="#e2b553" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="2.4" y1="-5.5" x2="2.4" y2="5.5" stroke="#e2b553" stroke-width="1.5" stroke-linecap="round"/>
    </marker>
    <marker id="geom-tick-3" viewBox="-10 -8 20 16" refX="0" refY="0" markerUnits="userSpaceOnUse" markerWidth="20" markerHeight="16" orient="auto">
      <line x1="-4.2" y1="-5.5" x2="-4.2" y2="5.5" stroke="#e2b553" stroke-width="1.4" stroke-linecap="round"/>
      <line x1="0" y1="-5.5" x2="0" y2="5.5" stroke="#e2b553" stroke-width="1.4" stroke-linecap="round"/>
      <line x1="4.2" y1="-5.5" x2="4.2" y2="5.5" stroke="#e2b553" stroke-width="1.4" stroke-linecap="round"/>
    </marker>
    <marker id="arrow-accent" viewBox="0 0 10 10" refX="8" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#e2b553"/>
    </marker>
    <marker id="arrow-muted" viewBox="0 0 10 10" refX="8" refY="5" markerUnits="userSpaceOnUse" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#9a9488"/>
    </marker>
  </defs>
  <style>
    .euclid-graphic { font-family: "Gentium Plus", "Palatino Linotype", "Book Antiqua", Georgia, serif; }
    .euclid-graphic .title { fill: #e8e2d5; font-size: 16px; font-weight: 700; letter-spacing: 0.02em; }
    .euclid-graphic .subtitle { fill: #a8a195; font-size: 12px; font-style: italic; }
    .euclid-graphic .lbl { fill: #e8e2d5; font-size: 13px; }
    .euclid-graphic .lbl-b { fill: #e8e2d5; font-size: 13.5px; font-weight: 700; }
    .euclid-graphic .lbl-sm { fill: #a8a195; font-size: 11.5px; }
    .euclid-graphic .lbl-gr { fill: #e2b553; font-size: 13px; font-style: italic; }
    .euclid-graphic .lbl-accent { fill: #e2b553; font-weight: 700; }
    .euclid-graphic .lbl-blue { fill: #6ba9d8; }
    .euclid-graphic .lbl-green { fill: #78c491; }
    .euclid-graphic .lbl-rose { fill: #dc7d7d; }
    .euclid-graphic .lbl-violet { fill: #b48ee0; }
    .euclid-graphic .mono { font-family: "JetBrains Mono", "Fira Code", monospace; font-size: 12px; fill: #e8e2d5; }
    .euclid-graphic .construct { stroke: #e8e2d5; stroke-width: 1.75; fill: none; }
    .euclid-graphic .guide { stroke: #9a9488; stroke-width: 1.2; stroke-dasharray: 5 4; fill: none; }
    .euclid-graphic .guide-accent { stroke: #e2b553; stroke-width: 1.6; stroke-dasharray: 5 4; fill: none; }
    .euclid-graphic .accent-line { stroke: #e2b553; stroke-width: 2.2; fill: none; }
    .euclid-graphic .blue-line { stroke: #6ba9d8; stroke-width: 2.0; fill: none; }
    .euclid-graphic .green-line { stroke: #78c491; stroke-width: 2.0; fill: none; }
    .euclid-graphic .rose-line { stroke: #dc7d7d; stroke-width: 2.0; fill: none; }
    .euclid-graphic .violet-line { stroke: #b48ee0; stroke-width: 2.0; fill: none; }
    .euclid-graphic .grid-line { stroke: #9a9488; stroke-opacity: 0.25; stroke-width: 0.85; fill: none; }
    .euclid-graphic .card { fill: #202026; fill-opacity: 0.72; stroke: #8e887c; stroke-width: 1.15; }
    .euclid-graphic .card-accent { fill: #202026; fill-opacity: 0.78; stroke: #e2b553; stroke-width: 1.85; }
    .euclid-graphic .card-blue { fill: #202026; fill-opacity: 0.78; stroke: #6ba9d8; stroke-width: 1.7; }
    .euclid-graphic .card-green { fill: #202026; fill-opacity: 0.78; stroke: #78c491; stroke-width: 1.7; }
    .euclid-graphic .card-violet { fill: #202026; fill-opacity: 0.78; stroke: #b48ee0; stroke-width: 1.7; }
    .euclid-graphic .card-rose { fill: #202026; fill-opacity: 0.78; stroke: #dc7d7d; stroke-width: 1.7; }
    .euclid-graphic .pt { fill: #e8e2d5; }
    .euclid-graphic .pt-accent { fill: #e2b553; stroke: #18181c; stroke-width: 1.1; }
    .euclid-graphic .alpha-pebble { font-size: 15px; font-weight: 700; text-anchor: middle; dominant-baseline: central; }
  </style>"""


def _tick_segment(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    ticks: int = 1,
    cls: str = "construct",
    data_ref: str = "",
) -> str:
    """Format a 3-vertex midpoint path carrying ``#geom-tick-k``."""
    mx = 0.5 * (x1 + x2)
    my = 0.5 * (y1 + y2)
    ref_attr = f' data-ref="{data_ref}"' if data_ref else ""
    return (
        f'<path d="M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}" '
        f'fill="none" class="{cls}" marker-mid="url(#geom-tick-{ticks})"{ref_attr}/>'
    )


def _wrap_svg(graphic_id: str, width: int, height: int, body: str, highlights: str = "") -> str:
    """Wrap body elements into a complete ``.euclid-graphic`` SVG."""
    hl_block = f'  <g id="highlights">\n{highlights}\n  </g>\n' if highlights else '  <g id="highlights"/>\n'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'data-graphic-id="{graphic_id}" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img">\n'
        f"{SHARED_STYLE_AND_DEFS}\n"
        f"{hl_block}"
        f"{body}\n"
        f"</svg>\n"
    )


def build_quadrivium_tetrad() -> str:
    """1. Book I, Ch. 3 — Ontological Bifurcation of Quantity & the Quadrivium."""
    body = [
        '  <text x="410" y="30" text-anchor="middle" class="title">Nicomachus I.3 — Ontological Division of Quantity &amp; the Four Mathemata</text>',
        '  <text x="410" y="50" text-anchor="middle" class="subtitle">Boethius\'s Quadrivium ("fourfold path" from sense-perception to intelligible wisdom)</text>',
        '  <g data-ref="QUANT">',
        '    <rect x="285" y="68" width="250" height="52" rx="8" class="card-accent"/>',
        '    <text x="410" y="90" text-anchor="middle" class="lbl-b">BEING / QUANTITY (τὸ ποσόν)</text>',
        '    <text x="410" y="109" text-anchor="middle" class="lbl-sm">Objects of Wisdom (σοφία)</text>',
        "  </g>",
        '  <path d="M 355 120 L 215 168" fill="none" class="accent-line" marker-end="url(#arrow-accent)"/>',
        '  <path d="M 465 120 L 605 168" fill="none" class="blue-line" marker-end="url(#arrow-muted)"/>',
        '  <g data-ref="MULT">',
        '    <rect x="90" y="172" width="250" height="56" rx="8" class="card-accent"/>',
        '    <text x="215" y="195" text-anchor="middle" class="lbl-b">MULTITUDE (τὸ πλῆθος)</text>',
        '    <text x="215" y="214" text-anchor="middle" class="lbl-sm">Discrete · Rooted in Monad, advancing infinitely</text>',
        "  </g>",
        '  <g data-ref="MAGN">',
        '    <rect x="480" y="172" width="250" height="56" rx="8" class="card-blue"/>',
        '    <text x="605" y="195" text-anchor="middle" class="lbl-b">MAGNITUDE (τὸ μέγεθος)</text>',
        '    <text x="605" y="214" text-anchor="middle" class="lbl-sm">Continuous · Bounded whole, infinitely divisible</text>',
        "  </g>",
        '  <path d="M 165 228 L 115 284" fill="none" class="accent-line" marker-end="url(#arrow-accent)"/>',
        '  <path d="M 265 228 L 315 284" fill="none" class="accent-line" marker-end="url(#arrow-accent)"/>',
        '  <path d="M 555 228 L 505 284" fill="none" class="blue-line" marker-end="url(#arrow-muted)"/>',
        '  <path d="M 655 228 L 705 284" fill="none" class="blue-line" marker-end="url(#arrow-muted)"/>',
        '  <g data-ref="ARITH">',
        '    <rect x="25" y="288" width="180" height="104" rx="8" class="card-accent"/>',
        '    <text x="115" y="311" text-anchor="middle" class="lbl-gr">I · καθ’ ἑαυτό (Per se)</text>',
        '    <text x="115" y="333" text-anchor="middle" class="lbl-b">ARITHMETIC</text>',
        '    <text x="115" y="351" text-anchor="middle" class="lbl-sm">Ἀριθμητική</text>',
        '    <text x="115" y="370" text-anchor="middle" class="lbl-sm">Even, Odd, Prime, Perfect</text>',
        '    <text x="115" y="385" text-anchor="middle" class="mono">Sovereign Mother (I.4–5)</text>',
        "  </g>",
        '  <g data-ref="MUSIC">',
        '    <rect x="225" y="288" width="180" height="104" rx="8" class="card-green"/>',
        '    <text x="315" y="311" text-anchor="middle" class="lbl-gr">II · πρὸς ἄλλο (Ad aliud)</text>',
        '    <text x="315" y="333" text-anchor="middle" class="lbl-b">MUSIC (HARMONICS)</text>',
        '    <text x="315" y="351" text-anchor="middle" class="lbl-sm">Μουσική</text>',
        '    <text x="315" y="370" text-anchor="middle" class="lbl-sm">2:1 · 3:2 · 4:3 · 9:8</text>',
        '    <text x="315" y="385" text-anchor="middle" class="mono">Relative Ratio</text>',
        "  </g>",
        '  <g data-ref="GEOM">',
        '    <rect x="420" y="288" width="180" height="104" rx="8" class="card-blue"/>',
        '    <text x="510" y="311" text-anchor="middle" class="lbl-gr">III · ἐν μονῇ (At rest)</text>',
        '    <text x="510" y="333" text-anchor="middle" class="lbl-b">GEOMETRY</text>',
        '    <text x="510" y="351" text-anchor="middle" class="lbl-sm">Γεωμετρία</text>',
        '    <text x="510" y="370" text-anchor="middle" class="lbl-sm">Triangle, Square, Cube</text>',
        '    <text x="510" y="385" text-anchor="middle" class="mono">Stationary Form</text>',
        "  </g>",
        '  <g data-ref="ASTRON">',
        '    <rect x="615" y="288" width="180" height="104" rx="8" class="card-violet"/>',
        '    <text x="705" y="311" text-anchor="middle" class="lbl-gr">IV · ἐν κινήσει (In motion)</text>',
        '    <text x="705" y="333" text-anchor="middle" class="lbl-b">ASTRONOMY</text>',
        '    <text x="705" y="351" text-anchor="middle" class="lbl-sm">Σφαιρική</text>',
        '    <text x="705" y="370" text-anchor="middle" class="lbl-sm">Ordered Revolutions</text>',
        '    <text x="705" y="385" text-anchor="middle" class="mono">Celestial Harmony</text>',
        "  </g>",
        '  <g data-ref="PRIORITY">',
        '    <path d="M 115 398 C 165 434, 265 434, 315 398" fill="none" class="guide-accent" marker-end="url(#arrow-accent)"/>',
        '    <path d="M 115 398 C 220 452, 410 452, 510 398" fill="none" class="guide-accent" marker-end="url(#arrow-accent)"/>',
        '    <path d="M 510 398 C 560 434, 655 434, 705 398" fill="none" class="guide" marker-end="url(#arrow-muted)"/>',
        '    <text x="410" y="462" text-anchor="middle" class="lbl-sm">Ontological Priority (συναναιρεῖ μὲν, οὐ συναναιρεῖται δέ): Arithmetic precedes Music, Geometry, and Sphaerics</text>',
        "  </g>",
    ]
    return _wrap_svg("quadrivium-tetrad", 820, 480, "\n".join(body))


def build_sieve_perfect_numbers() -> str:
    """2. Book I, Chs. 13 & 16 — Odd Sieve of Eratosthenes & Euclid–Nicomachus Perfect Numbers."""
    odds = list(range(3, 36, 2))  # 17 odd numbers: 3..35
    x0 = 42.0
    dx = 45.5
    y_row = 128.0
    parts = [
        '  <text x="410" y="28" text-anchor="middle" class="title">Nicomachus I.13 &amp; I.16 — The Odd Koskinon of Eratosthenes &amp; Perfect Numbers</text>',
        '  <text x="410" y="48" text-anchor="middle" class="subtitle">Top: Sieving odd numbers by strides of 3 and 5 · Bottom: Dyadic Euclid–Nicomachus generation of 6, 28, 496, 8128</text>',
        '  <rect x="20" y="62" width="780" height="148" rx="8" class="card"/>',
        '  <text x="36" y="84" class="lbl-b">I.13 · Odd Progression (3 … 35): Stride-3 arcs (rose) &amp; Stride-5 arcs (blue)</text>',
    ]

    # Stride-3 arcs: 3 -> 9 -> 15 -> 21 -> 27 -> 33 (indices 0, 3, 6, 9, 12, 15)
    parts.append('  <g data-ref="SIEVE3">')
    for idx_a, idx_b in ((0, 3), (3, 6), (6, 9), (9, 12), (12, 15)):
        xa = x0 + idx_a * dx
        xb = x0 + idx_b * dx
        xm = 0.5 * (xa + xb)
        parts.append(
            f'    <path d="M {xa:.1f} {y_row - 18:.1f} Q {xm:.1f} {y_row - 46:.1f} {xb:.1f} {y_row - 18:.1f}" fill="none" class="rose-line"/>'
        )
    parts.append("  </g>")

    # Stride-5 arcs: 5 -> 15 -> 25 -> 35 (indices 1, 6, 11, 16)
    parts.append('  <g data-ref="SIEVE5">')
    for idx_a, idx_b in ((1, 6), (6, 11), (11, 16)):
        xa = x0 + idx_a * dx
        xb = x0 + idx_b * dx
        xm = 0.5 * (xa + xb)
        parts.append(
            f'    <path d="M {xa:.1f} {y_row + 18:.1f} Q {xm:.1f} {y_row + 54:.1f} {xb:.1f} {y_row + 18:.1f}" fill="none" class="blue-line"/>'
        )
    parts.append("  </g>")

    primes_set = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
    for i, val in enumerate(odds):
        cx = x0 + i * dx
        is_p = val in primes_set
        ref = f"P{val}" if val in (3, 5, 7, 15) else ""
        ref_attr = f' data-ref="{ref}"' if ref else ""
        circle_cls = "card-accent" if is_p else ("card-violet" if val == 15 else "card")
        parts.append(f"  <g{ref_attr}>")
        parts.append(
            f'    <circle cx="{cx:.1f}" cy="{y_row:.1f}" r="16" class="{circle_cls}"/>'
        )
        if not is_p:
            parts.append(
                f'    <line x1="{cx - 10:.1f}" y1="{y_row + 10:.1f}" x2="{cx + 10:.1f}" y2="{y_row - 10:.1f}" stroke="#dc7d7d" stroke-width="1.4"/>'
            )
        parts.append(
            f'    <text x="{cx:.1f}" y="{y_row + 4:.1f}" text-anchor="middle" class="mono">{val}</text>'
        )
        parts.append("  </g>")

    parts.append(
        '  <text x="36" y="198" class="lbl-sm">Gold circles = Prime &amp; incomposite (πρῶτοι καὶ ἀσύνθετοι) · Crossed = Secondary &amp; composite (δεύτεροι καὶ σύνθετοι; 9 = 3², 15 = 3×5)</text>'
    )

    parts.extend(
        [
            '  <rect x="20" y="222" width="780" height="236" rx="8" class="card"/>',
            '  <text x="36" y="246" class="lbl-b">I.16 · Perfect Numbers (τέλειοι): Equal to the Sum of Their Proper Aliquot Parts</text>',
            '  <g data-ref="PERF6">',
            '    <text x="36" y="274" class="lbl-b">6 = 2¹(2² − 1) = 1 + 2 + 3</text>',
            '    <rect x="36" y="284" width="60" height="28" fill="#e2b553" fill-opacity="0.24" stroke="#e2b553" stroke-width="1.2"/>',
            '    <rect x="96" y="284" width="120" height="28" fill="#6ba9d8" fill-opacity="0.24" stroke="#6ba9d8" stroke-width="1.2"/>',
            '    <rect x="216" y="284" width="180" height="28" fill="#78c491" fill-opacity="0.24" stroke="#78c491" stroke-width="1.2"/>',
            '    <text x="66" y="303" text-anchor="middle" class="mono">1</text>',
            '    <text x="156" y="303" text-anchor="middle" class="mono">2</text>',
            '    <text x="306" y="303" text-anchor="middle" class="mono">3</text>',
            f"    {_tick_segment(36, 322, 396, 322, ticks=1, cls='accent-line')}",
            '    <text x="216" y="339" text-anchor="middle" class="lbl-sm">Whole = 6 (first perfect number, in units)</text>',
            "  </g>",
            '  <g data-ref="PERF28">',
            '    <text x="36" y="368" class="lbl-b">28 = 2²(2³ − 1) = 1 + 2 + 4 + 7 + 14</text>',
            '    <rect x="36" y="378" width="13" height="28" fill="#e2b553" fill-opacity="0.24" stroke="#e2b553" stroke-width="1.2"/>',
            '    <rect x="49" y="378" width="26" height="28" fill="#6ba9d8" fill-opacity="0.24" stroke="#6ba9d8" stroke-width="1.2"/>',
            '    <rect x="75" y="378" width="51" height="28" fill="#78c491" fill-opacity="0.24" stroke="#78c491" stroke-width="1.2"/>',
            '    <rect x="126" y="378" width="90" height="28" fill="#b48ee0" fill-opacity="0.24" stroke="#b48ee0" stroke-width="1.2"/>',
            '    <rect x="216" y="378" width="180" height="28" fill="#dc7d7d" fill-opacity="0.24" stroke="#dc7d7d" stroke-width="1.2"/>',
            '    <text x="55" y="397" text-anchor="middle" class="mono">1+2</text>',
            '    <text x="100" y="397" text-anchor="middle" class="mono">4</text>',
            '    <text x="171" y="397" text-anchor="middle" class="mono">7</text>',
            '    <text x="306" y="397" text-anchor="middle" class="mono">14</text>',
            f"    {_tick_segment(36, 416, 396, 416, ticks=2, cls='green-line')}",
            '    <text x="216" y="434" text-anchor="middle" class="lbl-sm">Whole = 28 (second perfect number, in tens)</text>',
            "  </g>",
            '  <g data-ref="MERSENNE">',
            '    <rect x="424" y="258" width="360" height="182" rx="8" class="card-accent"/>',
            '    <text x="604" y="280" text-anchor="middle" class="lbl-b">Dyadic Rule: P = 2ᵖ⁻¹ · (2ᵖ − 1)</text>',
            '    <text x="440" y="306" class="mono">p = 2 : 1+2 = 3 (prime)     → 2·3    = 6</text>',
            '    <text x="440" y="328" class="mono">p = 3 : 1+2+4 = 7 (prime)   → 4·7    = 28</text>',
            '    <text x="440" y="350" class="mono">p = 5 : 2⁵ − 1 = 31 (prime) → 16·31  = 496</text>',
            '    <text x="440" y="372" class="mono">p = 7 : 2⁷ − 1 = 127 (prime)→ 64·127 = 8128</text>',
            '    <line x1="440" y1="386" x2="768" y2="386" class="guide"/>',
            '    <text x="440" y="408" class="mono lbl-rose">p = 11: 2¹¹ − 1 = 2047 = 23 × 89</text>',
            '    <text x="440" y="426" class="lbl-sm">Composite! Breaks naive 10⁴ alternation</text>',
            "  </g>",
        ]
    )
    return _wrap_svg("sieve-perfect-numbers", 820, 474, "\n".join(parts))


def build_five_species_ratios() -> str:
    """3. Book I, Chs. 17–22 — The Five Species of Relative Inequality."""
    unit = 78.0
    x0 = 265.0
    rows = [
        ("EQ11", "0 · Equality (ἰσότης)", "1 : 1", 1, 1, "accent-line", 1),
        ("SP1", "1 · Multiplex (πολλαπλάσιος)", "2 : 1 (duple)", 2, 1, "blue-line", 1),
        ("SP2", "2 · Superparticularis (ἐπιμόριος)", "3 : 2 (hemiolios)", 3, 2, "green-line", 2),
        ("SP3", "3 · Superpartiens (ἐπιμερής)", "5 : 3 (epidimoiros)", 5, 3, "violet-line", 3),
        ("SP4", "4 · Mult. superparticularis", "5 : 2 (2 + 1/2)", 5, 2, "rose-line", 2),
        ("SP5", "5 · Mult. superpartiens", "8 : 3 (2 + 2/3)", 8, 3, "accent-line", 3),
    ]
    parts = [
        '  <text x="425" y="28" text-anchor="middle" class="title">Nicomachus I.17–22 — Equality &amp; the Five Species of Relative Inequality</text>',
        '  <text x="425" y="48" text-anchor="middle" class="subtitle">Every greater ratio m : n = q + r/n classifies uniquely by quotient q and remainder r</text>',
    ]
    for idx, (ref, title, ratio_lbl, m_val, n_val, cls, tick_k) in enumerate(rows):
        y = 82.0 + idx * 64.0
        scale = unit if m_val <= 5 else unit * 0.65
        w_m = m_val * scale
        w_n = n_val * scale
        parts.append(f'  <g data-ref="{ref}">')
        parts.append(f'    <text x="24" y="{y + 12:.1f}" class="lbl-b">{title}</text>')
        parts.append(f'    <text x="24" y="{y + 31:.1f}" class="mono">{ratio_lbl}</text>')
        for j in range(m_val):
            bx = x0 + j * scale
            is_excess = j >= n_val
            fill_hex = "#e2b553" if is_excess else "#8e887c"
            fill_op = "0.28" if is_excess else "0.18"
            parts.append(
                f'    <rect x="{bx:.1f}" y="{y - 2:.1f}" width="{scale:.1f}" height="18" fill="{fill_hex}" fill-opacity="{fill_op}" stroke="#c8c1b4" stroke-width="1.1"/>'
            )
        for j in range(n_val):
            bx = x0 + j * scale
            parts.append(
                f'    <rect x="{bx:.1f}" y="{y + 20:.1f}" width="{scale:.1f}" height="14" fill="#6ba9d8" fill-opacity="0.20" stroke="#9a9488" stroke-width="1.0"/>'
            )
        parts.append(f"    {_tick_segment(x0, y + 40, x0 + w_n, y + 40, ticks=tick_k, cls=cls)}")
        parts.append(
            f'    <text x="{x0 + w_m + 12:.1f}" y="{y + 13:.1f}" class="mono">m = {m_val}, n = {n_val}</text>'
        )
        parts.append("  </g>")
    return _wrap_svg("five-species-ratios", 850, 476, "\n".join(parts))


def build_equality_unfolding_tree() -> str:
    """4. Book I, Ch. 23 & Book II, Chs. 1–2 — Binary Tree of Equality Unfolding & Reduction."""
    parts = [
        '  <text x="430" y="28" text-anchor="middle" class="title">Nicomachus I.23 &amp; II.1–2 — Unfolding All Inequality from Equality (1, 1, 1)</text>',
        '  <text x="430" y="48" text-anchor="middle" class="subtitle">Direct rule N₁: (a, a+b, a+2b+c) · Anastrophe rule N₂ = N₁R · Inverse reduction N₁⁻¹ (gold dashed)</text>',
        '  <path d="M 430 112 L 430 156" fill="none" class="accent-line" marker-end="url(#arrow-accent)"/>',
        '  <text x="444" y="140" class="mono">N₁</text>',
        '  <path d="M 380 210 L 225 262" fill="none" class="blue-line" marker-end="url(#arrow-muted)"/>',
        '  <text x="275" y="232" class="mono">N₁ (direct)</text>',
        '  <path d="M 480 210 L 635 262" fill="none" class="green-line" marker-end="url(#arrow-accent)"/>',
        '  <text x="560" y="232" class="mono">N₂ (anastrophe)</text>',
        '  <path d="M 190 316 L 115 368" fill="none" class="blue-line" marker-end="url(#arrow-muted)"/>',
        '  <path d="M 255 316 L 325 368" fill="none" class="green-line" marker-end="url(#arrow-muted)"/>',
        '  <path d="M 600 316 L 535 368" fill="none" class="rose-line" marker-end="url(#arrow-accent)"/>',
        '  <path d="M 670 316 L 745 368" fill="none" class="violet-line" marker-end="url(#arrow-accent)"/>',
        '  <path d="M 745 422 L 665 464" fill="none" class="accent-line" marker-end="url(#arrow-accent)"/>',
        '  <text x="724" y="450" class="mono">N₁</text>',
        '  <g data-ref="REDUCE">',
        '    <path d="M 538 486 C 220 518, 8 440, 332 90" fill="none" class="guide-accent" marker-end="url(#arrow-accent)"/>',
        '    <text x="278" y="508" text-anchor="middle" class="lbl-gr">Book II.1–2 Inverse Subtraction N₁⁻¹ returns every ratio to (1, 1, 1)</text>',
        "  </g>",
    ]

    nodes = [
        ("ROOT111", 430, 86, "(1, 1, 1) · α, α, α", "Equality · 1:1", "card-accent"),
        ("N124", 430, 184, "(1, 2, 4) · α, β, δ", "1. Multiplex · 2:1", "card-blue"),
        ("N139", 225, 290, "(1, 3, 9) · α, γ, ϑ", "Multiplex · 3:1", "card-blue"),
        ("N469", 635, 290, "(4, 6, 9) · δ, ϛ, ϑ", "2. Superparticularis · 3:2", "card-green"),
        ("N1416", 115, 396, "(1, 4, 16)", "Multiplex · 4:1", "card-blue"),
        ("N91216", 325, 396, "(9, 12, 16)", "Epitritos · 4:3", "card-green"),
        ("N41025", 535, 396, "(4, 10, 25) · δ, ι, κε", "4. Mult. superpartic. · 5:2", "card-rose"),
        ("N91525", 745, 396, "(9, 15, 25) · ϑ, ιε, κε", "3. Superpartiens · 5:3", "card-violet"),
        ("N92464", 635, 480, "(9, 24, 64)", "5. Mult. superpartiens · 8:3", "card-accent"),
    ]
    for ref, cx, cy, top_txt, bot_txt, card_cls in nodes:
        w = 192 if len(top_txt) > 15 else 158
        parts.extend(
            [
                f'  <g data-ref="{ref}">',
                f'    <rect x="{cx - w / 2:.1f}" y="{cy - 26:.1f}" width="{w}" height="52" rx="8" class="{card_cls}"/>',
                f'    <text x="{cx:.1f}" y="{cy - 4:.1f}" text-anchor="middle" class="mono">{top_txt}</text>',
                f'    <text x="{cx:.1f}" y="{cy + 16:.1f}" text-anchor="middle" class="lbl-sm">{bot_txt}</text>',
                "  </g>",
            ]
        )
    return _wrap_svg("equality-unfolding-tree", 860, 524, "\n".join(parts))


def build_polygonal_alpha_gnomons() -> str:
    """5. Book II, Chs. 8–12 — Hoche-style alpha-pebble Triangular, Square & Pentagonal Gnomons."""
    shell_hex = ["#e2b553", "#6ba9d8", "#78c491", "#dc7d7d"]
    parts = [
        '  <text x="430" y="28" text-anchor="middle" class="title">Nicomachus II.8–12 — Polygonal α-Pebble Lattices &amp; Arithmetic Gnomons</text>',
        '  <text x="430" y="48" text-anchor="middle" class="subtitle">Hoche 1866 (pp. 87–89) unit-alpha notation · Each s-gon adds gnomon g(s, k) = 1 + (s − 2)(k − 1)</text>',
    ]

    # Panel 1: Triangular (1, 3, 6, 10)
    parts.append('  <g data-ref="TRI">')
    parts.append('    <rect x="20" y="66" width="255" height="275" rx="8" class="card"/>')
    parts.append('    <text x="147" y="90" text-anchor="middle" class="lbl-b">Triangular (s = 3)</text>')
    parts.append('    <text x="147" y="108" text-anchor="middle" class="mono">1, 3, 6, 10 · g = 1, 2, 3, 4</text>')
    for k in range(1, 5):
        col = shell_hex[k - 1]
        pts = []
        for j in range(k):
            px = 147.0 + (j - 0.5 * (k - 1)) * 42.0
            py = 138.0 + (k - 1) * 44.0
            pts.append((px, py))
        for i_seg in range(len(pts) - 1):
            parts.append(
                f'    <line x1="{pts[i_seg][0]:.1f}" y1="{pts[i_seg][1]:.1f}" x2="{pts[i_seg + 1][0]:.1f}" y2="{pts[i_seg + 1][1]:.1f}" stroke="{col}" stroke-width="1.4" opacity="0.65"/>'
            )
        for px, py in pts:
            parts.append(
                f'    <text x="{px:.1f}" y="{py:.1f}" class="alpha-pebble" fill="{col}">α</text>'
            )
    parts.append('    <text x="147" y="324" text-anchor="middle" class="lbl-sm">Natural gnomons: 1 + 2 + 3 + 4 = 10</text>')
    parts.append("  </g>")

    # Panel 2: Square (1, 4, 9, 16)
    parts.append('  <g data-ref="SQR">')
    parts.append('    <rect x="292" y="66" width="265" height="275" rx="8" class="card"/>')
    parts.append('    <text x="424" y="90" text-anchor="middle" class="lbl-b">Square (s = 4)</text>')
    parts.append('    <text x="424" y="108" text-anchor="middle" class="mono">1, 4, 9, 16 · g = 1, 3, 5, 7</text>')
    sx0, sy0, step = 356.0, 270.0, 44.0
    for k in range(1, 5):
        col = shell_hex[k - 1]
        m = k - 1
        pts = [(sx0 + m * step, sy0 - j * step) for j in range(m + 1)]
        pts.extend((sx0 + (m - 1 - j) * step, sy0 - m * step) for j in range(m))
        for i_seg in range(len(pts) - 1):
            parts.append(
                f'    <line x1="{pts[i_seg][0]:.1f}" y1="{pts[i_seg][1]:.1f}" x2="{pts[i_seg + 1][0]:.1f}" y2="{pts[i_seg + 1][1]:.1f}" stroke="{col}" stroke-width="1.5" opacity="0.7"/>'
            )
        for px, py in pts:
            parts.append(
                f'    <text x="{px:.1f}" y="{py:.1f}" class="alpha-pebble" fill="{col}">α</text>'
            )
    parts.append(f"    {_tick_segment(sx0, sy0 + 18, sx0 + 3 * step, sy0 + 18, ticks=2, cls='accent-line')}")
    parts.append('    <text x="424" y="324" text-anchor="middle" class="lbl-sm">Odd gnomons: 1 + 3 + 5 + 7 = 4² = 16</text>')
    parts.append("  </g>")

    # Panel 3: Pentagonal (1, 5, 12, 22) via Nicomachus II.12 3-sector fan
    parts.append('  <g data-ref="PENT">')
    parts.append('    <rect x="574" y="66" width="266" height="275" rx="8" class="card"/>')
    parts.append('    <text x="707" y="90" text-anchor="middle" class="lbl-b">Pentagonal (s = 5)</text>')
    parts.append('    <text x="707" y="108" text-anchor="middle" class="mono">1, 5, 12, 22 · g = 1, 4, 7, 10</text>')
    ox, oy, r_unit = 707.0, 276.0, 42.0
    angles_deg = [0.0, 60.0, 120.0, 180.0]
    unit_rays = [(math.cos(math.radians(a)), -math.sin(math.radians(a))) for a in angles_deg]
    parts.append(f'    <text x="{ox:.1f}" y="{oy:.1f}" class="alpha-pebble" fill="{shell_hex[0]}">α</text>')
    for k in range(2, 5):
        col = shell_hex[k - 1]
        m = k - 1
        pts = []
        for r_i in range(3):
            vx0, vy0 = ox + m * r_unit * unit_rays[r_i][0], oy + m * r_unit * unit_rays[r_i][1]
            vx1, vy1 = ox + m * r_unit * unit_rays[r_i + 1][0], oy + m * r_unit * unit_rays[r_i + 1][1]
            j_start = 0 if r_i == 0 else 1
            for j in range(j_start, m + 1):
                t = j / m
                pts.append((vx0 + t * (vx1 - vx0), vy0 + t * (vy1 - vy0)))
        for i_seg in range(len(pts) - 1):
            parts.append(
                f'    <line x1="{pts[i_seg][0]:.1f}" y1="{pts[i_seg][1]:.1f}" x2="{pts[i_seg + 1][0]:.1f}" y2="{pts[i_seg + 1][1]:.1f}" stroke="{col}" stroke-width="1.5" opacity="0.7"/>'
            )
        for px, py in pts:
            parts.append(
                f'    <text x="{px:.1f}" y="{py:.1f}" class="alpha-pebble" fill="{col}">α</text>'
            )
    parts.append('    <text x="707" y="324" text-anchor="middle" class="lbl-sm">Step +3 gnomons: 1 + 4 + 7 + 10 = 22</text>')
    parts.append("  </g>")

    parts.extend(
        [
            '  <g data-ref="DECOMP">',
            '    <rect x="20" y="356" width="820" height="78" rx="8" class="card-accent"/>',
            '    <text x="430" y="382" text-anchor="middle" class="lbl-b">Book II.12 Universal Triangular Decomposition: P(s, n) = P(s − 1, n) + Tₙ₋₁ = Tₙ + (s − 3)·Tₙ₋₁</text>',
            '    <text x="430" y="408" text-anchor="middle" class="mono">Square S₄ = T₄ + T₃ = 10 + 6 = 16   |   Pentagon P(5,4) = T₄ + 2·T₃ = 10 + 12 = 22   |   Hexagon P(6,4) = T₄ + 3·T₃ = 28</text>',
            "  </g>",
        ]
    )
    return _wrap_svg("polygonal-alpha-gnomons", 860, 450, "\n".join(parts))


def build_heteromecic_same_other() -> str:
    """6. Book II, Chs. 17–19 — Squares (Same) vs. Heteromecic Oblongs (Other)."""
    parts = [
        '  <text x="420" y="28" text-anchor="middle" class="title">Nicomachus II.17–19 — Same (ταὐτόν) vs. Other (θάτερον): Squares &amp; Heteromecic Oblongs</text>',
        '  <text x="420" y="48" text-anchor="middle" class="subtitle">Odd gnomons preserve side ratio 1 : 1 (n²) · Even gnomons shift side ratio n : (n + 1) at every step</text>',
        '  <g data-ref="SAME">',
        '    <rect x="25" y="68" width="370" height="246" rx="8" class="card-accent"/>',
        '    <text x="210" y="92" text-anchor="middle" class="lbl-b">THE SAME (ταὐτόν) · Square S₄ = 4 × 4 = 16</text>',
        '    <text x="210" y="111" text-anchor="middle" class="mono">Sum of Odds: 1 + 3 + 5 + 7 = 16 (ratio 1 : 1)</text>',
    ]
    cell = 38.0
    gx, gy = 134.0, 128.0
    shell_fills = ["#e2b553", "#6ba9d8", "#78c491", "#dc7d7d"]
    for r in range(4):
        for c in range(4):
            sh = max(r, c)
            parts.append(
                f'    <rect x="{gx + c * cell:.1f}" y="{gy + r * cell:.1f}" width="{cell:.1f}" height="{cell:.1f}" fill="{shell_fills[sh]}" fill-opacity="0.30" stroke="#c8c1b4" stroke-width="1.2"/>'
            )
    parts.append(f"    {_tick_segment(gx, gy + 4 * cell + 12, gx + 4 * cell, gy + 4 * cell + 12, ticks=1, cls='accent-line')}")
    parts.append(f"    {_tick_segment(gx - 12, gy, gx - 12, gy + 4 * cell, ticks=1, cls='accent-line')}")
    parts.append("  </g>")

    parts.extend(
        [
            '  <g data-ref="OTHER">',
            '    <rect x="425" y="68" width="390" height="246" rx="8" class="card-blue"/>',
            '    <text x="620" y="92" text-anchor="middle" class="lbl-b">THE OTHER (θάτερον) · Heteromecic H₄ = 4 × 5 = 20</text>',
            '    <text x="620" y="111" text-anchor="middle" class="mono">Sum of Evens: 2 + 4 + 6 + 8 = 20 (sides 4 : 5)</text>',
        ]
    )
    ox, oy = 525.0, 128.0
    for r in range(4):
        for c in range(5):
            sh = max(r, c - 1 if c > 0 else 0)
            parts.append(
                f'    <rect x="{ox + c * cell:.1f}" y="{oy + r * cell:.1f}" width="{cell:.1f}" height="{cell:.1f}" fill="{shell_fills[min(sh, 3)]}" fill-opacity="0.30" stroke="#c8c1b4" stroke-width="1.2"/>'
            )
    parts.append(f"    {_tick_segment(ox, oy + 4 * cell + 12, ox + 5 * cell, oy + 4 * cell + 12, ticks=2, cls='blue-line')}")
    parts.append(f"    {_tick_segment(ox - 12, oy, ox - 12, oy + 4 * cell, ticks=1, cls='accent-line')}")
    parts.append("  </g>")

    weave_vals = [
        ("S₁=1", "card-accent"),
        ("H₁=2", "card-blue"),
        ("S₂=4", "card-accent"),
        ("H₂=6", "card-blue"),
        ("S₃=9", "card-accent"),
        ("H₃=12", "card-blue"),
        ("S₄=16", "card-accent"),
        ("H₄=20", "card-blue"),
        ("S₅=25", "card-accent"),
    ]
    parts.extend(
        [
            '  <g data-ref="WEAVE">',
            '    <rect x="25" y="330" width="790" height="118" rx="8" class="card"/>',
            '    <text x="420" y="354" text-anchor="middle" class="lbl-b">Book II.19 Alternating Weave: Every Heteromecic Hₙ = n(n+1) is the Geometric Mean of Sₙ = n² and Sₙ₊₁ = (n+1)²</text>',
        ]
    )
    for i, (txt, card_cls) in enumerate(weave_vals):
        wx = 68.0 + i * 88.0
        parts.append(
            f'    <rect x="{wx - 34:.1f}" y="368" width="68" height="32" rx="6" class="{card_cls}"/>'
        )
        parts.append(f'    <text x="{wx:.1f}" y="389" text-anchor="middle" class="mono">{txt}</text>')
    parts.append(
        '    <text x="420" y="430" text-anchor="middle" class="mono">Sₙ · Sₙ₊₁ = Hₙ²   (e.g. 4 × 9 = 6²,  9 × 16 = 12²,  16 × 25 = 20²)   &amp;   Hₙ = 2 · Tₙ</text>'
    )
    parts.append("  </g>")
    return _wrap_svg("heteromecic-same-other", 840, 464, "\n".join(parts))


def build_nicomachus_sum_of_cubes() -> str:
    """7. Book II, Ch. 20 — Sum of Cubes = Squared Triangular Number (1^3 + 2^3 + 3^3 + 4^3 = 10^2)."""
    s = 32.0
    x0, y0 = 64.0, 392.0  # origin O(0,0) bottom-left, y upwards

    def _pt(u: float, v: float) -> tuple[float, float]:
        return x0 + u * s, y0 - v * s

    parts = [
        '  <text x="430" y="28" text-anchor="middle" class="title">Nicomachus II.20 — Sum of Consecutive Cubes Equals the Squared Triangle</text>',
        '  <text x="430" y="48" text-anchor="middle" class="subtitle">1³ + 2³ + 3³ + 4³ = (1 + 2 + 3 + 4)² = 10² = 100 · Odd-block sums &amp; L-gnomon square dissection</text>',
    ]

    shells = [
        ("CUBE1", 0, 1, "#e2b553", "#e2b553", "1³ = 1"),
        ("CUBE2", 1, 3, "#6ba9d8", "#6ba9d8", "2³ = 8"),
        ("CUBE3", 3, 6, "#78c491", "#78c491", "3³ = 27"),
        ("CUBE4", 6, 10, "#b48ee0", "#b48ee0", "4³ = 64"),
    ]

    parts.append('  <g data-ref="TRISQ">')
    for ref, t_prev, t_cur, fill_hex, stroke_hex, lbl in shells:
        if t_prev == 0:
            p_a = _pt(0, 0)
            p_b = _pt(1, 0)
            p_c = _pt(1, 1)
            p_d = _pt(0, 1)
            poly_pts = f"{p_a[0]:.1f},{p_a[1]:.1f} {p_b[0]:.1f},{p_b[1]:.1f} {p_c[0]:.1f},{p_c[1]:.1f} {p_d[0]:.1f},{p_d[1]:.1f}"
        else:
            coords = [
                _pt(t_prev, 0),
                _pt(t_cur, 0),
                _pt(t_cur, t_cur),
                _pt(0, t_cur),
                _pt(0, t_prev),
                _pt(t_prev, t_prev),
            ]
            poly_pts = " ".join(f"{px:.1f},{py:.1f}" for px, py in coords)
        lx, ly = _pt(0.5 * (t_prev + t_cur), 0.5 * (t_prev + t_cur))
        parts.append(f'    <g data-ref="{ref}">')
        parts.append(
            f'      <polygon points="{poly_pts}" fill="{fill_hex}" fill-opacity="0.30" stroke="{stroke_hex}" stroke-width="2.0"/>'
        )
        if t_cur >= 3:
            parts.append(f'      <text x="{lx + 16:.1f}" y="{ly + 18:.1f}" class="mono">{lbl}</text>')
        parts.append("    </g>")

    for i in range(11):
        gx1, gy1 = _pt(i, 0)
        gx2, gy2 = _pt(i, 10)
        hx1, hy1 = _pt(0, i)
        hx2, hy2 = _pt(10, i)
        parts.append(f'    <line x1="{gx1:.1f}" y1="{gy1:.1f}" x2="{gx2:.1f}" y2="{gy2:.1f}" class="grid-line"/>')
        parts.append(f'    <line x1="{hx1:.1f}" y1="{hy1:.1f}" x2="{hx2:.1f}" y2="{hy2:.1f}" class="grid-line"/>')

    ox, oy = _pt(0, 0)
    dx4, dy4 = _pt(10, 10)
    parts.append(f'    <line x1="{ox:.1f}" y1="{oy:.1f}" x2="{dx4:.1f}" y2="{dy4:.1f}" class="guide-accent" data-ref="OD4"/>')
    axis_ticks = (
        (0, "0", "end", -4.0),
        (1, "T₁=1", "middle", 4.0),
        (3, "T₂=3", "middle", 0.0),
        (6, "T₃=6", "middle", 0.0),
        (10, "T₄=10", "middle", 0.0),
    )
    for tk, tick_lbl, anchor, dx_off in axis_ticks:
        px, _ = _pt(tk, 0)
        parts.append(
            f'    <text x="{px + dx_off:.1f}" y="{y0 + 21:.1f}" text-anchor="{anchor}" class="mono">{tick_lbl}</text>'
        )
    parts.append("  </g>")

    parts.extend(
        [
            '  <g data-ref="ODDBLOCKS">',
            '    <rect x="424" y="72" width="416" height="338" rx="8" class="card"/>',
            '    <text x="632" y="98" text-anchor="middle" class="lbl-b">Nicomachus\'s Consecutive Odd-Block Theorem (II.20)</text>',
            '    <text x="444" y="132" class="mono lbl-accent">k = 1 :  1                     =   1 = 1³</text>',
            '    <text x="444" y="162" class="mono lbl-blue">k = 2 :  3 + 5                 =   8 = 2³</text>',
            '    <text x="444" y="192" class="mono lbl-green">k = 3 :  7 + 9 + 11            =  27 = 3³</text>',
            '    <text x="444" y="222" class="mono lbl-violet">k = 4 : 13 + 15 + 17 + 19      =  64 = 4³</text>',
            '    <text x="444" y="252" class="mono lbl-rose">k = 5 : 21 + 23 + 25 + 27 + 29 = 125 = 5³</text>',
            '    <line x1="442" y1="272" x2="820" y2="272" class="guide"/>',
            '    <text x="632" y="300" text-anchor="middle" class="lbl-b">Why Shell k Has Exact Area k³:</text>',
            '    <text x="632" y="326" text-anchor="middle" class="mono">Tₖ² − Tₖ₋₁² = (Tₖ − Tₖ₋₁) · (Tₖ + Tₖ₋₁)</text>',
            '    <text x="632" y="352" text-anchor="middle" class="mono">            =      k      ·     k²     = k³</text>',
            '    <text x="632" y="384" text-anchor="middle" class="lbl-sm">(By II.12, two consecutive triangles Tₖ₋₁ + Tₖ = k²!)</text>',
            "  </g>",
        ]
    )
    return _wrap_svg("nicomachus-sum-of-cubes", 860, 440, "\n".join(parts))


def build_three_classical_means_semicircle() -> str:
    """8. Book II, Chs. 21–28 — Semicircle Construction of A, G, H & Synoptic Table of 10 Means."""
    scale = 20.0
    px0, py0 = 42.0, 356.0

    def _m(x: float, y: float) -> tuple[float, float]:
        return px0 + x * scale, py0 - y * scale

    p_xy = _m(0.0, 0.0)
    q_xy = _m(6.0, 0.0)
    o_xy = _m(9.0, 0.0)
    r_xy = _m(18.0, 0.0)
    s_xy = _m(6.0, 6.0 * math.sqrt(2.0))
    f_xy = _m(26.0 / 3.0, 2.0 * math.sqrt(2.0) / 3.0)
    rad = 9.0 * scale

    parts = [
        '  <text x="435" y="28" text-anchor="middle" class="title">Nicomachus II.21–28 — The Three Classical Archetypes &amp; Synoptic Decad of Ten Means</text>',
        '  <text x="435" y="48" text-anchor="middle" class="subtitle">Left: Semicircle on PQ = 6, QR = 12 proving A ≥ G ≥ H &amp; A · H = G² · Right: Hoche p. 144 Ten Means</text>',
        '  <rect x="20" y="66" width="405" height="356" rx="8" class="card"/>',
        '  <text x="222" y="90" text-anchor="middle" class="lbl-b">Semicircle Construction (a = 6, c = 12)</text>',
        f'  <path d="M {p_xy[0]:.2f} {p_xy[1]:.2f} A {rad:.2f} {rad:.2f} 0 0 1 {r_xy[0]:.2f} {r_xy[1]:.2f}" fill="none" class="construct" data-ref="SEMICIRC"/>',
        f"  {_tick_segment(p_xy[0], p_xy[1], o_xy[0], o_xy[1], ticks=1, cls='construct', data_ref='PO')}",
        f"  {_tick_segment(o_xy[0], o_xy[1], r_xy[0], r_xy[1], ticks=1, cls='construct', data_ref='OR')}",
        f"  {_tick_segment(o_xy[0], o_xy[1], s_xy[0], s_xy[1], ticks=1, cls='accent-line', data_ref='OS')}",
        f'  <line x1="{q_xy[0]:.2f}" y1="{q_xy[1]:.2f}" x2="{s_xy[0]:.2f}" y2="{s_xy[1]:.2f}" class="green-line" data-ref="QS"/>',
        f'  <line x1="{q_xy[0]:.2f}" y1="{q_xy[1]:.2f}" x2="{f_xy[0]:.2f}" y2="{f_xy[1]:.2f}" class="guide"/>',
        f"  {_tick_segment(s_xy[0], s_xy[1], f_xy[0], f_xy[1], ticks=2, cls='blue-line', data_ref='SF')}",
    ]

    for lbl, (cx, cy), dy in (
        ("P(0)", p_xy, 20),
        ("Q(6)", q_xy, 20),
        ("O(9)", o_xy, 20),
        ("R(18)", r_xy, 20),
        ("S", s_xy, -12),
        ("F", f_xy, -8),
    ):
        parts.append(f'  <circle cx="{cx:.2f}" cy="{cy:.2f}" r="3.8" class="pt-accent"/>')
        parts.append(f'  <text x="{cx:.2f}" y="{cy + dy:.2f}" text-anchor="middle" class="mono">{lbl}</text>')

    parts.extend(
        [
            f'  <text x="{s_xy[0] - 62:.1f}" y="{0.5 * (q_xy[1] + s_xy[1]):.1f}" class="mono lbl-green">G = 6√2</text>',
            f'  <text x="{o_xy[0] + 24:.1f}" y="{0.5 * (o_xy[1] + s_xy[1]) + 22:.1f}" class="mono lbl-accent">A = 9</text>',
            f'  <text x="{f_xy[0] + 24:.1f}" y="{0.5 * (s_xy[1] + f_xy[1]) - 8:.1f}" class="mono lbl-blue">H = 8</text>',
            '  <text x="222" y="404" text-anchor="middle" class="mono">A = 9 &gt; G = √72 ≈ 8.49 &gt; H = 8  ·  A·H = 72 = G²</text>',
        ]
    )

    ten_rows = [
        ("1. Arithmetic", "α, β, γ", "(1, 2, 3)", "(z−m):(m−x) = 1"),
        ("2. Geometric", "α, β, δ", "(1, 2, 4)", "(z−m):(m−x) = z:m"),
        ("3. Harmonic", "γ, δ, ϛ", "(3, 4, 6)", "(z−m):(m−x) = z:x"),
        ("4. Subcontr. Harmonic", "γ, ε, ϛ", "(3, 5, 6)", "(m−x):(z−m) = z:x"),
        ("5. Subcontr. Geom. I", "β, δ, ε", "(2, 4, 5)", "(m−x):(z−m) = m:x"),
        ("6. Subcontr. Geom. II", "α, δ, ϛ", "(1, 4, 6)", "(m−x):(z−m) = z:m"),
        ("7. Neo-Pythagorean I", "ϛ, η, ϑ", "(6, 8, 9)", "(z−x):(m−x) = z:x"),
        ("8. Neo-Pythagorean II", "ϛ, ζ, ϑ", "(6, 7, 9)", "(z−x):(z−m) = z:x"),
        ("9. Neo-Pythagorean III", "δ, ϛ, ζ", "(4, 6, 7)", "(z−x):(m−x) = m:x"),
        ("10. Additive / Fibonacci", "γ, ε, η", "(3, 5, 8)", "(z−x):(z−m) = m:x"),
    ]
    parts.extend(
        [
            '  <g data-ref="TENMEANS">',
            '    <rect x="440" y="66" width="420" height="356" rx="8" class="card"/>',
            '    <text x="650" y="90" text-anchor="middle" class="lbl-b">Synoptic Decad Table (Book II.28.11, Hoche p. 144)</text>',
        ]
    )
    for i, (m_name, gr_num, dec_trip, eq_str) in enumerate(ten_rows):
        ry = 118.0 + i * 29.5
        is_10 = i == 9
        ref_attr = ' data-ref="MEAN10"' if is_10 else ""
        cls_name = "lbl-sm lbl-accent" if is_10 else "lbl-sm"
        mono_cls = "mono lbl-accent" if is_10 else "mono"
        parts.append(f"    <g{ref_attr}>")
        parts.append(f'      <text x="454" y="{ry:.1f}" class="{cls_name}">{m_name}</text>')
        parts.append(f'      <text x="620" y="{ry:.1f}" class="lbl-gr">{gr_num}</text>')
        parts.append(f'      <text x="680" y="{ry:.1f}" class="{mono_cls}">{dec_trip}</text>')
        parts.append(f'      <text x="750" y="{ry:.1f}" class="lbl-sm">{eq_str}</text>')
        parts.append("    </g>")
    parts.append("  </g>")
    return _wrap_svg("three-classical-means-semicircle", 880, 440, "\n".join(parts))


def build_cube_most_perfect_proportion() -> str:
    """9. Book II, Ch. 29 — Teleiotatē Analogia 6 : 8 :: 9 : 12 (Cube & Musical Harmony)."""
    cx, cy, r = 175.0, 212.0, 92.0
    hex_pts = [
        (cx + r * math.cos(math.radians(-90 + 60 * i)), cy + r * math.sin(math.radians(-90 + 60 * i)))
        for i in range(6)
    ]
    front_center = (cx, cy + 8.0)
    back_center = (cx, cy - 8.0)

    parts = [
        '  <text x="440" y="28" text-anchor="middle" class="title">Nicomachus II.29 — The Most Perfect Proportion (Τελειοτάτη Ἀναλογία): 6 : 8 :: 9 : 12</text>',
        '  <text x="440" y="48" text-anchor="middle" class="subtitle">ϛ, η, ϑ, ιβ · Cube Topology (6 Faces, 8 Vertices, 12 Edges) &amp; Pythagorean Musical Consonances</text>',
        '  <rect x="20" y="66" width="310" height="378" rx="8" class="card"/>',
        '  <text x="175" y="90" text-anchor="middle" class="lbl-b">Philolaus\'s "Geometric Harmony"</text>',
        '  <g data-ref="FACES6">',
        f'    <polygon points="{hex_pts[5][0]:.1f},{hex_pts[5][1]:.1f} {hex_pts[0][0]:.1f},{hex_pts[0][1]:.1f} {hex_pts[1][0]:.1f},{hex_pts[1][1]:.1f} {front_center[0]:.1f},{front_center[1]:.1f}" fill="#e2b553" fill-opacity="0.22"/>',
        f'    <polygon points="{hex_pts[1][0]:.1f},{hex_pts[1][1]:.1f} {hex_pts[2][0]:.1f},{hex_pts[2][1]:.1f} {hex_pts[3][0]:.1f},{hex_pts[3][1]:.1f} {front_center[0]:.1f},{front_center[1]:.1f}" fill="#6ba9d8" fill-opacity="0.20"/>',
        f'    <polygon points="{hex_pts[3][0]:.1f},{hex_pts[3][1]:.1f} {hex_pts[4][0]:.1f},{hex_pts[4][1]:.1f} {hex_pts[5][0]:.1f},{hex_pts[5][1]:.1f} {front_center[0]:.1f},{front_center[1]:.1f}" fill="#78c491" fill-opacity="0.20"/>',
        "  </g>",
        '  <g data-ref="EDGES12">',
    ]
    for i in range(6):
        p1 = hex_pts[i]
        p2 = hex_pts[(i + 1) % 6]
        parts.append(f"    {_tick_segment(p1[0], p1[1], p2[0], p2[1], ticks=1, cls='construct')}")
    for idx_f in (1, 3, 5):
        parts.append(
            f"    {_tick_segment(front_center[0], front_center[1], hex_pts[idx_f][0], hex_pts[idx_f][1], ticks=1, cls='accent-line')}"
        )
    for idx_b in (0, 2, 4):
        parts.append(
            f'    <line x1="{back_center[0]:.1f}" y1="{back_center[1]:.1f}" x2="{hex_pts[idx_b][0]:.1f}" y2="{hex_pts[idx_b][1]:.1f}" class="guide"/>'
        )
    parts.append("  </g>")

    parts.append('  <g data-ref="VERTS8">')
    for px, py in [*hex_pts, front_center, back_center]:
        parts.append(f'    <circle cx="{px:.1f}" cy="{py:.1f}" r="4.2" class="pt-accent"/>')
    parts.append("  </g>")

    parts.extend(
        [
            '  <text x="175" y="336" text-anchor="middle" class="lbl-b">6 Faces · 8 Vertices · 12 Edges</text>',
            '  <text x="175" y="360" text-anchor="middle" class="mono">Harmonic Cube: 8 = 2·6·12 / (6 + 12)</text>',
            '  <text x="175" y="384" text-anchor="middle" class="lbl-sm">6 = 1×2×3 (scalene) · 8 = 2×2×2 (cube)</text>',
            '  <text x="175" y="404" text-anchor="middle" class="lbl-sm">9 = 1×3×3 (brick)   · 12 = 2×2×3 (beam)</text>',
            '  <text x="175" y="426" text-anchor="middle" class="mono">Euler: F − E + V = 6 − 12 + 8 = 2</text>',
        ]
    )

    mx0 = 376.0
    m_scale = 36.5
    my = 274.0

    def _mp(u: float, v: float = 0.0) -> tuple[float, float]:
        return mx0 + u * m_scale, my - v * 20.5

    z_p = _mp(0)
    t6_p = _mp(6)
    t8_p = _mp(8)
    t9_p = _mp(9)
    t12_p = _mp(12)
    k_p = _mp(9, 6)
    p1_p = _mp(36 / 5, 12 / 5)
    p2_p = _mp(72 / 7, 24 / 7)
    x_p = _mp(108 / 13, 24 / 13)

    parts.extend(
        [
            '  <rect x="346" y="66" width="514" height="378" rx="8" class="card"/>',
            '  <text x="603" y="90" text-anchor="middle" class="lbl-b">Projective Harmonic Conjugate &amp; Monochord Consonances</text>',
            f'  <line x1="{k_p[0]:.1f}" y1="{k_p[1]:.1f}" x2="{t6_p[0]:.1f}" y2="{t6_p[1]:.1f}" class="guide"/>',
            f'  <line x1="{k_p[0]:.1f}" y1="{k_p[1]:.1f}" x2="{t12_p[0]:.1f}" y2="{t12_p[1]:.1f}" class="guide"/>',
            f'  <line x1="{z_p[0]:.1f}" y1="{z_p[1]:.1f}" x2="{p2_p[0]:.1f}" y2="{p2_p[1]:.1f}" class="guide"/>',
            f'  <line x1="{t6_p[0]:.1f}" y1="{t6_p[1]:.1f}" x2="{p2_p[0]:.1f}" y2="{p2_p[1]:.1f}" class="guide"/>',
            f'  <line x1="{t12_p[0]:.1f}" y1="{t12_p[1]:.1f}" x2="{p1_p[0]:.1f}" y2="{p1_p[1]:.1f}" class="guide"/>',
            f'  <line x1="{k_p[0]:.1f}" y1="{k_p[1]:.1f}" x2="{t8_p[0]:.1f}" y2="{t8_p[1]:.1f}" class="blue-line" stroke-dasharray="4 3"/>',
            f'  <circle cx="{k_p[0]:.1f}" cy="{k_p[1]:.1f}" r="3.4" class="pt"/>',
            f'  <text x="{k_p[0] + 10:.1f}" y="{k_p[1] + 4:.1f}" class="lbl-sm">K (Steiner apex)</text>',
            f'  <circle cx="{x_p[0]:.1f}" cy="{x_p[1]:.1f}" r="3.2" class="pt"/>',
            f'  <line x1="{z_p[0]:.1f}" y1="{my:.1f}" x2="{t12_p[0]:.1f}" y2="{my:.1f}" class="construct" data-ref="MONOCHORD"/>',
            f"  {_tick_segment(t6_p[0], my, t9_p[0], my, ticks=2, cls='accent-line')}",
            f"  {_tick_segment(t9_p[0], my, t12_p[0], my, ticks=2, cls='accent-line')}",
        ]
    )

    for lbl, (px, py), dx_lbl in (
        ("Z=0", z_p, 0.0),
        ("6 (ϛ)", t6_p, 0.0),
        ("8 (η)", t8_p, -7.0),
        ("9 (ϑ)", t9_p, 7.0),
        ("12 (ιβ)", t12_p, 0.0),
    ):
        parts.append(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" class="pt-accent"/>')
        parts.append(f'  <text x="{px + dx_lbl:.1f}" y="{py - 11:.1f}" text-anchor="middle" class="mono">{lbl}</text>')

    parts.extend(
        [
            '  <g data-ref="TONE">',
            f'    <path d="M {t8_p[0]:.1f} {my + 6:.1f} Q {0.5 * (t8_p[0] + t9_p[0]):.1f} {my + 32:.1f} {t9_p[0]:.1f} {my + 6:.1f}" fill="none" class="rose-line"/>',
            f'    <text x="{0.5 * (t8_p[0] + t9_p[0]):.1f}" y="{my + 35:.1f}" text-anchor="middle" class="mono lbl-rose">9:8 Tone</text>',
            "  </g>",
            '  <g data-ref="FOURTH">',
            f'    <path d="M {t6_p[0]:.1f} {my + 6:.1f} Q {0.5 * (t6_p[0] + t8_p[0]):.1f} {my + 58:.1f} {t8_p[0]:.1f} {my + 6:.1f}" fill="none" class="blue-line"/>',
            f'    <path d="M {t9_p[0]:.1f} {my + 6:.1f} Q {0.5 * (t9_p[0] + t12_p[0]):.1f} {my + 58:.1f} {t12_p[0]:.1f} {my + 6:.1f}" fill="none" class="blue-line"/>',
            f'    <text x="{0.5 * (t6_p[0] + t8_p[0]) - 8:.1f}" y="{my + 54:.1f}" text-anchor="middle" class="lbl-sm">4:3 Fourth</text>',
            f'    <text x="{0.5 * (t9_p[0] + t12_p[0]) + 10:.1f}" y="{my + 54:.1f}" text-anchor="middle" class="lbl-sm">12:9 = 4:3</text>',
            "  </g>",
            '  <g data-ref="FIFTH">',
            f'    <path d="M {t6_p[0]:.1f} {my + 6:.1f} Q {0.5 * (t6_p[0] + t9_p[0]):.1f} {my + 94:.1f} {t9_p[0]:.1f} {my + 6:.1f}" fill="none" class="green-line"/>',
            f'    <path d="M {t8_p[0]:.1f} {my + 6:.1f} Q {0.5 * (t8_p[0] + t12_p[0]):.1f} {my + 94:.1f} {t12_p[0]:.1f} {my + 6:.1f}" fill="none" class="green-line"/>',
            f'    <text x="{0.5 * (t6_p[0] + t12_p[0]):.1f}" y="{my + 92:.1f}" text-anchor="middle" class="mono lbl-green">Diapente (Fifth) 9:6 = 12:8 = 3:2</text>',
            "  </g>",
            '  <g data-ref="OCTAVE">',
            f'    <path d="M {t6_p[0]:.1f} {my + 6:.1f} Q {0.5 * (t6_p[0] + t12_p[0]):.1f} {my + 132:.1f} {t12_p[0]:.1f} {my + 6:.1f}" fill="none" class="accent-line"/>',
            '    <text x="603" y="428" text-anchor="middle" class="mono lbl-accent">Diapason 12:6 = 2:1 · 6×12 = 8×9 = 72 · CR(6,12;8,0) = −1</text>',
            "  </g>",
        ]
    )
    return _wrap_svg("cube-most-perfect-proportion", 880, 460, "\n".join(parts))


FIGURE_BUILDERS = {
    "quadrivium-tetrad.svg": build_quadrivium_tetrad,
    "sieve-perfect-numbers.svg": build_sieve_perfect_numbers,
    "five-species-ratios.svg": build_five_species_ratios,
    "equality-unfolding-tree.svg": build_equality_unfolding_tree,
    "polygonal-alpha-gnomons.svg": build_polygonal_alpha_gnomons,
    "heteromecic-same-other.svg": build_heteromecic_same_other,
    "nicomachus-sum-of-cubes.svg": build_nicomachus_sum_of_cubes,
    "three-classical-means-semicircle.svg": build_three_classical_means_semicircle,
    "cube-most-perfect-proportion.svg": build_cube_most_perfect_proportion,
}


def build_all_figures(output_dir: Path | None = None) -> list[Path]:
    """Render all 9 ``.euclid-graphic`` SVGs to ``output_dir``.

    Args:
        output_dir: Destination directory (defaults to ``docsrc/_static/figures``).

    Returns:
        Sorted list of written SVG file paths.
    """
    dest = output_dir if output_dir is not None else FIGURES_DIR
    dest.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for filename, fn in FIGURE_BUILDERS.items():
        out_path = dest / filename
        out_path.write_text(fn(), encoding="utf-8")
        written.append(out_path)
    return sorted(written)


def main() -> None:
    """CLI entrypoint building all 9 codex SVGs."""
    paths = build_all_figures()
    for p in paths:
        print(f"wrote {p.relative_to(ROOT)} ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
