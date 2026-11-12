"""Command-line overview for ``geometor.nicomachus``."""

from __future__ import annotations

from rich.console import Console
from rich.table import Table

from geometor.nicomachus.equality_tree import (
    reduce_to_equality,
    unfold_five_species_from_equality,
    verify_equality_identities,
)
from geometor.nicomachus.figurate_gnomons import (
    construct_nicomachus_cubes_model,
    euclid_nicomachus_perfect_numbers,
    verify_figurate_identities,
)
from geometor.nicomachus.ten_means_and_cube import (
    NICOMACHEAN_TEN_MEANS,
    construct_cube_proportion_model,
    verify_cube_proportion_identities,
    verify_ten_means_identities,
)


def main() -> None:
    """Run and display a Rich summary of Nicomachus's exact symbolic theorems."""
    console = Console()
    console.rule("[bold gold1]GEOMETOR • Nicomachus of Gerasa (Introductio Arithmetica)[/bold gold1]")

    eq_summary = verify_equality_identities()
    fig_summary = verify_figurate_identities()
    means_summary = verify_ten_means_identities()
    cube_summary = verify_cube_proportion_identities()

    t1 = Table(title="Book I.23 & II.1–2 — Five Species Unfolded from Equality (1, 1, 1)")
    t1.add_column("Species", style="cyan")
    t1.add_column("Greek / Boethian Latin", style="magenta")
    t1.add_column("Triple", justify="right")
    t1.add_column("Ratio", justify="right")
    t1.add_column("Rule Path", style="green")
    for key, node in unfold_five_species_from_equality().items():
        path_str = " -> ".join(node.path) if node.path else "root"
        t1.add_row(
            key,
            f"{node.greek_species} / {node.latin_species}",
            str(tuple(int(v) for v in node.terms)),
            f"{node.ratio.p}:{node.ratio.q}",
            path_str,
        )
    console.print(t1)

    red = reduce_to_equality(9, 24, 64)
    console.print(
        f"Inverse reduction (9, 24, 64) -> Equality in {len(red)} steps "
        f"(verified {eq_summary['verified_tree_nodes']} tree nodes)."
    )

    perfs = [str(p["perfect_number"]) for p in euclid_nicomachus_perfect_numbers(4)]
    cubes = construct_nicomachus_cubes_model(order=4)
    console.print(
        f"Book I.16 Perfect Tetrad: {', '.join(perfs)} | "
        f"Book II.20 Sum of Cubes (n=4): sum={int(cubes.total_area)} = T_4^2 = {int(cubes.triangular_side)}^2 "
        f"(identities={fig_summary['nicomachus_cubes_verified']})."
    )

    t2 = Table(title="Book II.28 — Nicomachus's Synoptic Table of the Ten Proportions")
    t2.add_column("#", justify="right", style="cyan")
    t2.add_column("Proportion", style="bold")
    t2.add_column("Hoche p. 144", style="yellow")
    t2.add_column("Decad Witness", justify="right", style="green")
    for spec in NICOMACHEAN_TEN_MEANS:
        t2.add_row(
            str(spec.index),
            spec.name,
            spec.greek_numerals,
            str(spec.canonical_triple),
        )
    console.print(t2)

    cube_res = construct_cube_proportion_model()
    console.print(
        f"Book II.29 Teleiotate Analogia {tuple(int(v) for v in cube_res.terms)}: "
        f"Cube={cube_res.cube_counts}, CR(T6,T12;T8,Z)={cube_res.projective_cross_ratio}, "
        f"verified means={means_summary['verified_means_count']}, "
        f"product={cube_summary['geometric_product']}."
    )


if __name__ == "__main__":
    main()
