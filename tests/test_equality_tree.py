"""Tests for Nicomachus's Five Species of Inequality & Equality Tree (Book I.17–23; II.1–2)."""

from __future__ import annotations

import sympy as sp
import sympy.geometry as spg

from geometor.nicomachus.equality_tree import (
    NICOMACHUS_INVERSE_MATRIX,
    NICOMACHUS_MATRIX_N1,
    NICOMACHUS_MATRIX_N2,
    classify_nicomachean_ratio,
    construct_equality_ray_model,
    generate_equality_tree,
    reduce_to_equality,
    unfold_five_species_from_equality,
    verify_equality_identities,
)


def test_matrices_are_unimodular_and_invertible() -> None:
    """Verify exact unimodularity and inverse relationship of N1, N2, and N1^-1."""
    assert NICOMACHUS_MATRIX_N1.det() == sp.Integer(1)
    assert NICOMACHUS_MATRIX_N2.det() == sp.Integer(-1)
    assert NICOMACHUS_MATRIX_N1 * NICOMACHUS_INVERSE_MATRIX == sp.eye(3)


def test_five_species_classification() -> None:
    """Verify Nicomachus's five species of greater inequality and sub-relations."""
    eq = classify_nicomachean_ratio(6, 6)
    assert eq["species_key"] == "equality"

    mult = classify_nicomachean_ratio(8, 4)
    assert mult["species_key"] == "multiplex"
    assert mult["greek_species"] == "πολλαπλάσιος"

    epim = classify_nicomachean_ratio(9, 8)
    assert epim["species_key"] == "superparticularis"
    assert "epogdoos" in epim["specific_name"]

    epip = classify_nicomachean_ratio(5, 3)
    assert epip["species_key"] == "superpartiens"

    m_epim = classify_nicomachean_ratio(5, 2)
    assert m_epim["species_key"] == "multiplex_superparticularis"

    m_epip = classify_nicomachean_ratio(8, 3)
    assert m_epip["species_key"] == "multiplex_superpartiens"

    lesser = classify_nicomachean_ratio(2, 3)
    assert lesser["species_key"].startswith("sub_")


def test_equality_tree_bijection_and_reduction() -> None:
    """Verify unique coprime ratio generation from (1, 1, 1) and inverse reduction."""
    nodes = generate_equality_tree(max_depth=4)
    assert len(nodes) == 16  # 1 (depth 0) + 1 (depth 1) + 2 + 4 + 8
    assert nodes[0].terms == (sp.Integer(1), sp.Integer(1), sp.Integer(1))

    seen_ratios: set[sp.Rational] = set()
    for node in nodes:
        a, b, c = node.terms
        assert a * c == b**2
        assert sp.gcd(node.root_pair[0], node.root_pair[1]) == 1
        assert node.ratio not in seen_ratios
        seen_ratios.add(node.ratio)
        if node.depth > 0:
            steps = reduce_to_equality(a, b, c)
            assert steps[-1].after == (sp.Integer(1), sp.Integer(1), sp.Integer(1))


def test_unfold_five_species_and_ray_model_zero_floats() -> None:
    """Verify all five canonical ratio species and zero sp.Float atoms in ray Model."""
    witnesses = unfold_five_species_from_equality()
    assert set(witnesses) == {
        "equality",
        "multiplex",
        "superparticularis",
        "superpartiens",
        "multiplex_superparticularis",
        "multiplex_superpartiens",
    }
    summary = verify_equality_identities()
    assert summary["discriminant_invariant"] is True
    assert summary["verified_tree_nodes"] == 16

    model = construct_equality_ray_model()
    for elem in model:
        if isinstance(elem, spg.Point2D):
            assert not elem.x.atoms(sp.Float)
            assert not elem.y.atoms(sp.Float)
