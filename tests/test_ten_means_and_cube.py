"""Tests for Nicomachus's Ten Means, Semicircle Construction & Cube Harmony (Book II.21–29)."""

from __future__ import annotations

import sympy as sp
import sympy.geometry as spg
from geometor.model.invariants import line_spread, quadrance

from geometor.nicomachus.ten_means_and_cube import (
    CUBE_PROPORTION_TERMS,
    NICOMACHEAN_TEN_MEANS,
    compute_all_ten_means,
    compute_nicomachean_mean,
    construct_cube_proportion_model,
    construct_three_classical_means_model,
    verify_cube_proportion_identities,
    verify_ten_means_identities,
)


def test_all_ten_nicomachean_means() -> None:
    """Verify all ten Nicomachean means on canonical triples and on (4, 12)."""
    assert len(NICOMACHEAN_TEN_MEANS) == 10
    for spec in NICOMACHEAN_TEN_MEANS:
        a, b, c = spec.canonical_triple
        computed = compute_nicomachean_mean(spec.index, a, c)
        assert sp.simplify(computed - b) == 0

    rows = compute_all_ten_means(4, 12)
    assert len(rows) == 10
    assert rows[0]["mean"] == sp.Integer(8)  # Arithmetic mean of (4, 12)
    assert rows[1]["mean"] == 4 * sp.sqrt(3)  # Geometric mean of (4, 12)
    assert rows[2]["mean"] == sp.Integer(6)  # Harmonic mean of (4, 12)
    assert rows[9]["mean"] == sp.Integer(8)  # 10th mean: z - x = 12 - 4 = 8

    checks = verify_ten_means_identities()
    assert all(bool(v) for v in checks.values())


def test_semicircle_classical_means_exact_radicals() -> None:
    """Verify Pappus/Nicomachus semicircle construction over Q(sqrt(2)) with zero floats."""
    model = construct_three_classical_means_model(6, 12)
    o_pt = model.get_element_by_ID("O")
    p_pt = model.get_element_by_ID("P")
    q_pt = model.get_element_by_ID("Q")
    s_pt = model.get_element_by_ID("S")
    f_pt = model.get_element_by_ID("F")

    q_a = quadrance(o_pt, s_pt)
    q_g = quadrance(q_pt, s_pt)
    q_h = quadrance(s_pt, f_pt)
    assert q_a == sp.Integer(81)
    assert q_g == sp.Integer(72)
    assert q_h == sp.Integer(64)
    assert q_a * q_h == q_g**2

    base = model.construct_line(p_pt, o_pt, guide=True)
    rad = model.construct_line(o_pt, s_pt, guide=True)
    assert line_spread(base, rad) == sp.Rational(8, 9)

    for elem in model:
        if isinstance(elem, spg.Point2D):
            assert not elem.x.atoms(sp.Float)
            assert not elem.y.atoms(sp.Float)


def test_cube_most_perfect_proportion() -> None:
    """Verify Book II, Ch. 29 Teleiotatē Analogia 6 : 8 :: 9 : 12 and Cube topology."""
    assert CUBE_PROPORTION_TERMS == (6, 8, 9, 12)
    cube = construct_cube_proportion_model()
    assert cube.cube_counts == {"faces": 6, "vertices": 8, "edges": 12}
    assert cube.arithmetic_mean == sp.Integer(9)
    assert cube.harmonic_mean == sp.Integer(8)
    assert cube.geometric_product == sp.Integer(72)
    assert cube.projective_cross_ratio == sp.Integer(-1)
    assert sp.Rational(2, 1) in cube.consonances.values()
    assert sp.Rational(3, 2) in cube.consonances.values()
    assert sp.Rational(4, 3) in cube.consonances.values()
    assert sp.Rational(9, 8) in cube.consonances.values()

    checks = verify_cube_proportion_identities()
    assert all(bool(v) for v in checks.values())
    for elem in cube.model:
        if isinstance(elem, spg.Point2D):
            assert not elem.x.atoms(sp.Float)
            assert not elem.y.atoms(sp.Float)
