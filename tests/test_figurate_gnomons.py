"""Tests for Sieve, Perfect Numbers, Polygonal Gnomons & Sum of Cubes (Book I.13–16; II.6–20)."""

from __future__ import annotations

import pytest
import sympy as sp
import sympy.geometry as spg

from geometor.nicomachus.figurate_gnomons import (
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


def test_odd_sieve_of_eratosthenes() -> None:
    """Verify Nicomachus's odd-sequence Koskinon up to 50."""
    res = sieve_of_eratosthenes(limit=50)
    assert 2 not in res["odd_sequence"]
    assert res["odd_primes"][:8] == (3, 5, 7, 11, 13, 17, 19, 23)
    assert res["witness_factors"][15] == (3, 5)
    assert res["witness_factors"][9] == (3,)
    with pytest.raises(ValueError):
        sieve_of_eratosthenes(limit=2)


def test_perfect_abundant_deficient_numbers() -> None:
    """Verify Euclid-Nicomachus perfect numbers 6, 28, 496, 8128 and aliquot classification."""
    perfs = euclid_nicomachus_perfect_numbers(4)
    assert [row["perfect_number"] for row in perfs] == [6, 28, 496, 8128]
    assert classify_abundant_deficient_perfect(6)["classification"] == "perfect"
    assert classify_abundant_deficient_perfect(12)["classification"] == "superabundant"
    assert classify_abundant_deficient_perfect(8)["classification"] == "deficient"


def test_polygonal_heteromecic_and_pyramidal_identities() -> None:
    """Verify symbolic polygonal decomposition into triangles and Same/Other identities."""
    n = sp.Symbol("n", integer=True, positive=True)
    for s in range(3, 9):
        lhs = polygonal_number(s, n)
        rhs = polygonal_number(3, n) + (s - 3) * polygonal_number(3, n - 1)
        assert sp.simplify(lhs - rhs) == 0
        diff = polygonal_gnomon(s, n + 1) - polygonal_gnomon(s, n)
        assert sp.simplify(diff - (s - 2)) == 0

    assert [int(heteromecic_number(k)) for k in range(1, 6)] == [2, 6, 12, 20, 30]
    assert [int(pyramidal_number(3, k)) for k in range(1, 6)] == [1, 4, 10, 20, 35]
    assert [int(pyramidal_number(4, k)) for k in range(1, 6)] == [1, 5, 14, 30, 55]

    checks = verify_figurate_identities()
    assert all(bool(v) for v in checks.values())


def test_planar_gnomon_and_cubes_models_zero_floats() -> None:
    """Verify exact planar gnomon and Nicomachus Sum-of-Cubes Models have zero floats."""
    for sides in (3, 4, 5):
        poly_res = construct_polygonal_gnomon_model(sides=sides, order=4)
        assert poly_res.cumulative_counts[-1] == int(polygonal_number(sides, 4))
        for elem in poly_res.model:
            if isinstance(elem, spg.Point2D):
                assert not elem.x.atoms(sp.Float)
                assert not elem.y.atoms(sp.Float)

    cubes = construct_nicomachus_cubes_model(order=4)
    assert cubes.odd_blocks[4] == (13, 15, 17, 19)
    assert [int(cubes.shell_areas[k]) for k in range(1, 5)] == [1, 8, 27, 64]
    assert int(cubes.total_area) == 100 == int(cubes.triangular_side) ** 2
    for elem in cubes.model:
        if isinstance(elem, spg.Point2D):
            assert not elem.x.atoms(sp.Float)
            assert not elem.y.atoms(sp.Float)
