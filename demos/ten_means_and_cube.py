"""Standalone demonstration of Nicomachus's Ten Means & Cube Harmony (Book II, Chs. 21–29)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

import sympy as sp  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.nicomachus.ten_means_and_cube import (  # noqa: E402
    compute_all_ten_means,
    construct_cube_proportion_model,
    construct_three_classical_means_model,
    verify_cube_proportion_identities,
    verify_ten_means_identities,
)


def run_demo() -> None:
    """Execute and print Nicomachus's ten proportions and 6 : 8 :: 9 : 12 cube harmony."""
    console = Console()
    verify_ten_means_identities()
    verify_cube_proportion_identities()
    console.rule("[bold gold1]Nicomachus II.21–29 — Ten Proportions & Cube Harmony[/bold gold1]")

    table = Table(title="All Ten Means on (x=4, z=12) & Hoche Synoptic Decad Triples")
    table.add_column("#", justify="right", style="cyan")
    table.add_column("Proportion", style="bold")
    table.add_column("Decad (Hoche p. 144)", justify="right", style="yellow")
    table.add_column("Exact m on (4, 12)", justify="right", style="green")

    for row in compute_all_ten_means(4, 12):
        spec = row["spec"]
        table.add_row(
            str(spec.index),
            spec.name,
            f"{spec.canonical_triple} ({spec.greek_numerals})",
            sp.sstr(row["mean"]),
        )
    console.print(table)

    semi = construct_three_classical_means_model(6, 12)
    cube = construct_cube_proportion_model()
    console.print(
        f"\nSemicircle classical means model (6, 12) steps: {len(semi.steps)} | "
        f"Cube harmony 6:8::9:12 cross-ratio: {cube.projective_cross_ratio}"
    )
    for name, rat in cube.consonances.items():
        console.print(f"  {name}: {rat.p}:{rat.q}")


if __name__ == "__main__":
    run_demo()
