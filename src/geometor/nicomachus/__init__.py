"""GEOMETOR • nicomachus: Digital Scriptorium Codex & exact symbolic demonstrations.

Covers Nicomachus of Gerasa's *Introduction to Arithmetic* (*Ἀριθμητικὴ Εἰσαγωγή*,
Books I–II, c. 100 CE), grounded in Richard Hoche's 1866 Teubner Greek critical edition
and Martin Luther D'Ooge's 1926 English translation, paired with exact ``SymPy`` and
``geometor.model`` constructions:

- :mod:`geometor.nicomachus.equality_tree`: Nicomachus's Rule of Three Terms (I.23 & II.1–2)
  unfolding all five species of inequality from Equality ``(1, 1, 1)`` and reducing any
  geometric triple back to ``(1, 1, 1)``.
- :mod:`geometor.nicomachus.figurate_gnomons`: Exact ``geometor.model`` planar lattice
  constructions of polygonal gnomons, oblong (*heteromecic*) numbers, Sieve & Perfect
  numbers, and Nicomachus's Sum-of-Cubes Theorem (II.20).
- :mod:`geometor.nicomachus.ten_means_and_cube`: Exact ``SymPy`` & ``geometor.model``
  constructions of all ten Nicomachean means (II.21–28) and the *Teleiotatē Analogia*
  Cube Proportion ``6 : 8 :: 9 : 12`` (II.29).
"""

from __future__ import annotations

__version__ = "0.1.3"

from geometor.nicomachus.equality_tree import (
    NICOMACHUS_INVERSE_MATRIX,
    NICOMACHUS_MATRIX_N1,
    NICOMACHUS_MATRIX_N2,
    REVERSAL_MATRIX_R,
    EqualityNode,
    ReductionStep,
    classify_nicomachean_ratio,
    construct_equality_ray_model,
    generate_equality_tree,
    reduce_to_equality,
    unfold_five_species_from_equality,
    verify_equality_identities,
)
from geometor.nicomachus.figurate_gnomons import (
    NicomachusCubesResult,
    PolygonalGnomonResult,
    classify_abundant_deficient_perfect,
    construct_nicomachus_cubes_model,
    construct_polygonal_gnomon_model,
    euclid_nicomachus_perfect_numbers,
    heteromecic_number,
    polygonal_gnomon,
    polygonal_number,
    pyramidal_number,
    sieve_of_eratosthenes,
    verify_figurate_identities,
)
from geometor.nicomachus.ten_means_and_cube import (
    CUBE_PROPORTION_TERMS,
    NICOMACHEAN_TEN_MEANS,
    CubeHarmonicResult,
    MeanSpec,
    compute_all_ten_means,
    compute_nicomachean_mean,
    construct_cube_proportion_model,
    construct_three_classical_means_model,
    verify_cube_proportion_identities,
    verify_ten_means_identities,
)

__all__ = [
    "__version__",
    "CUBE_PROPORTION_TERMS",
    "NICOMACHEAN_TEN_MEANS",
    "CubeHarmonicResult",
    "EqualityNode",
    "MeanSpec",
    "NICOMACHUS_INVERSE_MATRIX",
    "NICOMACHUS_MATRIX_N1",
    "NICOMACHUS_MATRIX_N2",
    "NicomachusCubesResult",
    "PolygonalGnomonResult",
    "REVERSAL_MATRIX_R",
    "ReductionStep",
    "classify_abundant_deficient_perfect",
    "classify_nicomachean_ratio",
    "compute_all_ten_means",
    "compute_nicomachean_mean",
    "construct_cube_proportion_model",
    "construct_equality_ray_model",
    "construct_nicomachus_cubes_model",
    "construct_polygonal_gnomon_model",
    "construct_three_classical_means_model",
    "euclid_nicomachus_perfect_numbers",
    "generate_equality_tree",
    "heteromecic_number",
    "polygonal_gnomon",
    "polygonal_number",
    "pyramidal_number",
    "reduce_to_equality",
    "sieve_of_eratosthenes",
    "unfold_five_species_from_equality",
    "verify_cube_proportion_identities",
    "verify_equality_identities",
    "verify_figurate_identities",
    "verify_ten_means_identities",
]
