"""Standalone demonstration of Nicomachus's Equality Tree & Reduction (I.17–23, II.1–2)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.nicomachus.equality_tree import (  # noqa: E402
    construct_equality_ray_model,
    generate_equality_tree,
    reduce_to_equality,
    unfold_five_species_from_equality,
    verify_equality_identities,
)


def run_demo() -> None:
    """Execute and print Nicomachus's three-term unfolding and reduction demonstration."""
    console = Console()
    summary = verify_equality_identities()
    console.rule("[bold gold1]Nicomachus I.23 & II.1–2 — Equality Tree Demonstration[/bold gold1]")

    table = Table(title="Binary Unfolding Tree from (1, 1, 1) through Depth 3")
    table.add_column("Depth", justify="right")
    table.add_column("Path", style="green")
    table.add_column("Triple (a, b, c)", justify="right", style="cyan")
    table.add_column("Root (u, v)", justify="right")
    table.add_column("Ratio", justify="right")
    table.add_column("Species", style="magenta")

    for node in generate_equality_tree(max_depth=3):
        table.add_row(
            str(node.depth),
            " -> ".join(node.path) if node.path else "Equality",
            str(tuple(int(v) for v in node.terms)),
            str(tuple(int(v) for v in node.root_pair)),
            f"{node.ratio.p}:{node.ratio.q}",
            f"{node.species_key} ({node.greek_species})",
        )
    console.print(table)

    witness = unfold_five_species_from_equality()["multiplex_superpartiens"]
    steps = reduce_to_equality(*witness.terms)
    console.print(f"\nReducing {tuple(int(x) for x in witness.terms)} back to (1, 1, 1):")
    for st in steps:
        b0 = tuple(int(x) for x in st.before)
        a0 = tuple(int(x) for x in st.after)
        console.print(f"  Step {st.step_index}: {b0} --(undo {st.undone_rule})--> {a0}")

    model = construct_equality_ray_model()
    console.print(
        f"\ngeometor.model ray construction steps: {len(model.steps)} | "
        f"verified tree nodes: {summary['verified_tree_nodes']}"
    )


if __name__ == "__main__":
    run_demo()
