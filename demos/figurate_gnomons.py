"""Standalone demonstration of Figurate Gnomons, Perfect Numbers & Sum of Cubes (I.13–16, II.6–20)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.nicomachus.figurate_gnomons import (  # noqa: E402
    construct_nicomachus_cubes_model,
    construct_polygonal_gnomon_model,
    euclid_nicomachus_perfect_numbers,
    heteromecic_number,
    polygonal_number,
    sieve_of_eratosthenes,
    verify_figurate_identities,
)


def run_demo() -> None:
    """Execute and print Nicomachus's sieve, figurate gnomons, and sum-of-cubes proof."""
    console = Console()
    verify_figurate_identities()
    console.rule("[bold gold1]Nicomachus I.13–16 & II.6–20 — Figurate Gnomons & Cubes[/bold gold1]")

    sieve = sieve_of_eratosthenes(limit=45)
    console.print(f"Odd Koskinon primes <= 45: {sieve['odd_primes']}")
    perfs = euclid_nicomachus_perfect_numbers(4)
    console.print(
        "Canonical Perfect Tetrad (I.16): "
        + ", ".join(f"{p['perfect_number']} = 2^{p['exponent']-1}*(2^{p['exponent']}-1)" for p in perfs)
    )

    poly_table = Table(title="Polygonal & Heteromecic Table (Book II, Chs. 8–19)")
    poly_table.add_column("Series", style="cyan")
    for idx in range(1, 7):
        poly_table.add_column(f"n={idx}", justify="right")

    for label, sides in (
        ("Triangular (s=3)", 3),
        ("Square / Same (s=4)", 4),
        ("Pentagonal (s=5)", 5),
        ("Hexagonal (s=6)", 6),
        ("Heptagonal (s=7)", 7),
    ):
        vals = [str(int(polygonal_number(sides, k))) for k in range(1, 7)]
        poly_table.add_row(label, *vals)
    poly_table.add_row(
        "Heteromecic / Other n(n+1)",
        *[str(int(heteromecic_number(k))) for k in range(1, 7)],
    )
    console.print(poly_table)

    pent = construct_polygonal_gnomon_model(sides=5, order=4)
    cubes = construct_nicomachus_cubes_model(order=4)
    console.print(
        f"Pentagonal gnomons (s=5, order=4): gnomons={pent.gnomon_counts}, totals={pent.cumulative_counts}"
    )
    for k, block in cubes.odd_blocks.items():
        odd_expr = " + ".join(str(v) for v in block)
        console.print(
            f"  Cube shell k={k}: {odd_expr} = {k}^3 = {int(cubes.shell_areas[k])}"
        )
    console.print(
        f"Master square area = {int(cubes.total_area)} = T_4^2 = {int(cubes.triangular_side)}^2."
    )


if __name__ == "__main__":
    run_demo()
