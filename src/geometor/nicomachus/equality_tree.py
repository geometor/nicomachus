r"""Nicomachus's Rule of Three Terms & Reduction to Equality (Book I, Chs. 17–23; Book II, Chs. 1–2).

Formalizes Nicomachus of Gerasa's foundational theorem of Pythagorean arithmetic philosophy:
**Equality** (:math:`1 : 1 : 1`) is the primordial mother and root (*μήτηρ καὶ ῥίζα*) of all
five species of relative inequality (*πολλαπλάσιος*, *ἐπιμόριος*, *ἐπιμερής*,
*πολλαπλασιεπιμόριος*, *πολλαπλασιεπιμερής*), and every geometric triple reduces back to
Equality by finite Euclidean subtraction.

Algebraically, Nicomachus's three-term unfolding rule

.. math::

    (a, b, c) \longmapsto (a,\; a + b,\; a + 2b + c)

is the unimodular matrix :math:`N_1 \in \mathrm{SL}_3(\mathbb{Z})` acting on the second
symmetric Veronese cone :math:`a c = b^2`, while his reversed (*ἀναστρέψαντι*) sibling rule is
:math:`N_2 = N_1 R`. Together :math:`(N_1, N_2)` generate a bijection from :math:`(1, 1, 1)`
onto all primitive integer geometric progressions :math:`(u^2, u v, v^2)` with
:math:`1 \le u < v` and :math:`\gcd(u, v) = 1`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, intersect_2d, proposition, quadrance, zero_test

NICOMACHUS_MATRIX_N1: sp.Matrix = sp.Matrix(
    [
        [1, 0, 0],
        [1, 1, 0],
        [1, 2, 1],
    ]
)

REVERSAL_MATRIX_R: sp.Matrix = sp.Matrix(
    [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
    ]
)

NICOMACHUS_MATRIX_N2: sp.Matrix = NICOMACHUS_MATRIX_N1 * REVERSAL_MATRIX_R

NICOMACHUS_INVERSE_MATRIX: sp.Matrix = sp.Matrix(
    [
        [1, 0, 0],
        [-1, 1, 0],
        [1, -2, 1],
    ]
)

_NAMED_SUPERPARTICULARS: dict[tuple[int, int], tuple[str, str, str]] = {
    (3, 2): ("ἡμιόλιος", "sesquialtera", "hemiolios (fifth, 3:2)"),
    (4, 3): ("ἐπίτριτος", "sesquitertia", "epitritos (fourth, 4:3)"),
    (5, 4): ("ἐπιτέταρτος", "sesquiquarta", "epitetartos (5:4)"),
    (6, 5): ("ἐπίπεμπτος", "sesquiquinta", "epipemptos (6:5)"),
    (9, 8): ("ἐπόγδοος", "sesquioctava", "epogdoos (whole tone, 9:8)"),
}

_NAMED_MULTIPLES: dict[int, tuple[str, str, str]] = {
    2: ("διπλάσιος", "dupla", "duple (octave, 2:1)"),
    3: ("τριπλάσιος", "tripla", "triple (twelfth, 3:1)"),
    4: ("τετραπλάσιος", "quadrupla", "quadruple (double octave, 4:1)"),
    5: ("πενταπλάσιος", "quintupla", "quintuple (5:1)"),
}


@dataclass(frozen=True)
class EqualityNode:
    """Single node in Nicomachus's binary unfolding tree from Equality ``(1, 1, 1)``.

    Attributes:
        terms: Exact ascending geometric triple ``(a, b, c)`` with ``a * c == b**2``.
        root_pair: Coprime positive integer root pair ``(u, v)`` such that
            ``terms == (u**2, u * v, v**2)``.
        ratio: Common geometric ratio ``sp.Rational(v, u)``.
        species_key: Canonical Nicomachean species identifier (``"equality"``,
            ``"multiplex"``, ``"superparticularis"``, ``"superpartiens"``,
            ``"multiplex_superparticularis"``, or ``"multiplex_superpartiens"``).
        greek_species: Greek technical name from Nicomachus I.17–22.
        latin_species: Boethian Latin technical name (*De Inst. Arith.* I.22–28).
        path: Sequence of ``"N1"`` (direct) and ``"N2"`` (*anastrophe*) rule applications
            from ``(1, 1, 1)``.
        depth: Tree depth (``0`` at ``(1, 1, 1)``).
    """

    terms: tuple[sp.Integer, sp.Integer, sp.Integer]
    root_pair: tuple[sp.Integer, sp.Integer]
    ratio: sp.Rational
    species_key: str
    greek_species: str
    latin_species: str
    path: tuple[str, ...]
    depth: int


@dataclass(frozen=True)
class ReductionStep:
    """Single inverse subtraction step in Nicomachus's Book II, Chs. 1–2 algorithm.

    Attributes:
        step_index: 1-based step index along the reduction back to Equality.
        before: Ascending geometric triple ``(a, b, c)`` entering this step.
        raw_subtracted: Raw triple ``N1^-1 * before = (a, b - a, a - 2*b + c)`` prior to
            optional reversal.
        reversed_order: ``True`` if ``raw_subtracted`` had descending order and was
            reversed via ``R`` to restore ascending order (undoing an ``N2`` step).
        after: Resulting ascending triple ``(a', b', c')``.
        undone_rule: ``"N2"`` when ``reversed_order`` is ``True``, else ``"N1"``.
    """

    step_index: int
    before: tuple[sp.Integer, sp.Integer, sp.Integer]
    raw_subtracted: tuple[sp.Integer, sp.Integer, sp.Integer]
    reversed_order: bool
    after: tuple[sp.Integer, sp.Integer, sp.Integer]
    undone_rule: str


def classify_nicomachean_ratio(
    antecedent: int | sp.Expr,
    consequent: int | sp.Expr,
) -> dict[str, Any]:
    """Classify a positive ratio ``antecedent : consequent`` into Nicomachus's species (I.17–22).

    Args:
        antecedent: Positive integer or exact positive rational first term.
        consequent: Positive integer or exact positive rational second term.

    Returns:
        Dictionary with exact ``ratio`` (:class:`sympy.Rational`), reduced coprime pair
        ``coprime_terms``, ``direction`` (``"equal"``, ``"greater"``, or ``"lesser"``),
        ``species_index`` (``0``, ``1..5``, or ``-1..-5``), ``species_key``,
        ``greek_species``, ``latin_species``, ``english_species``, and optional
        ``specific_name``.

    Raises:
        ValueError: If either term is non-positive or non-rational.
    """
    ant = sp.Rational(antecedent)
    con = sp.Rational(consequent)
    if ant <= 0 or con <= 0:
        raise ValueError(f"Nicomachean ratios require strictly positive terms; got {ant}:{con}.")

    ratio = sp.Rational(ant, con)
    p = int(ratio.p)
    q = int(ratio.q)

    if p == q:
        return {
            "ratio": ratio,
            "coprime_terms": (1, 1),
            "direction": "equal",
            "species_index": 0,
            "species_key": "equality",
            "greek_species": "ἰσότης",
            "latin_species": "aequalitas",
            "english_species": "Equality",
            "specific_name": "monadic equality (1:1)",
        }

    is_greater = p > q
    major, minor = (p, q) if is_greater else (q, p)
    quot, rem = divmod(major, minor)

    if quot >= 2 and rem == 0:
        idx = 1
        key = "multiplex"
        gr, la, en = "πολλαπλάσιος", "multiplex", "Multiple"
        spec = _NAMED_MULTIPLES.get(quot, ("", "", f"{quot}-fold multiple ({major}:{minor})"))[2]
    elif quot == 1 and rem == 1:
        idx = 2
        key = "superparticularis"
        gr, la, en = "ἐπιμόριος", "superparticularis", "Superparticular (Epimoric)"
        spec = _NAMED_SUPERPARTICULARS.get(
            (major, minor), ("", "", f"superparticular ({major}:{minor})")
        )[2]
    elif quot == 1 and rem >= 2:
        idx = 3
        key = "superpartiens"
        gr, la, en = "ἐπιμερής", "superpartiens", "Superpartient (Epimeric)"
        spec = f"super-{rem}-partient ({major}:{minor})"
    elif quot >= 2 and rem == 1:
        idx = 4
        key = "multiplex_superparticularis"
        gr, la, en = (
            "πολλαπλασιεπιμόριος",
            "multiplex superparticularis",
            "Multiple Superparticular",
        )
        spec = f"{quot}-fold superparticular ({major}:{minor})"
    else:
        idx = 5
        key = "multiplex_superpartiens"
        gr, la, en = (
            "πολλαπλασιεπιμερής",
            "multiplex superpartiens",
            "Multiple Superpartient",
        )
        spec = f"{quot}-fold super-{rem}-partient ({major}:{minor})"

    if not is_greater:
        idx = -idx
        key = f"sub_{key}"
        gr = f"ὑπο{gr}"
        la = f"sub{la}"
        en = f"Sub-{en.lower()}"
        spec = f"sub-({spec})"

    return {
        "ratio": ratio,
        "coprime_terms": (p, q),
        "direction": "greater" if is_greater else "lesser",
        "species_index": idx,
        "species_key": key,
        "greek_species": gr,
        "latin_species": la,
        "english_species": en,
        "specific_name": spec,
    }


def _make_node(
    vec: sp.Matrix,
    path: tuple[str, ...],
) -> EqualityNode:
    """Build an :class:`EqualityNode` from a 3-element column vector ``vec``."""
    a, b, c = (sp.Integer(vec[0]), sp.Integer(vec[1]), sp.Integer(vec[2]))
    u = sp.Integer(sp.integer_nthroot(int(a), 2)[0])
    v = sp.Integer(sp.integer_nthroot(int(c), 2)[0])
    info = classify_nicomachean_ratio(c, b)
    return EqualityNode(
        terms=(a, b, c),
        root_pair=(u, v),
        ratio=sp.Rational(c, b),
        species_key=str(info["species_key"]),
        greek_species=str(info["greek_species"]),
        latin_species=str(info["latin_species"]),
        path=path,
        depth=len(path),
    )


def generate_equality_tree(max_depth: int = 3) -> list[EqualityNode]:
    """Generate Nicomachus's binary unfolding tree up to ``max_depth`` from ``(1, 1, 1)``.

    At the root ``(1, 1, 1)``, ``N1`` and ``N2`` coincide (since ``R * (1, 1, 1) = (1, 1, 1)``),
    producing the first multiple ``(1, 2, 4)`` at depth ``1``. From depth ``1`` onward, each
    node branches cleanly into its direct ``N1`` child and its reversed (*anastrophe*) ``N2``
    child without duplicates.

    Args:
        max_depth: Non-negative maximum depth of rule applications (default ``3``).

    Returns:
        Breadth-first list of :class:`EqualityNode` instances from depth ``0`` to ``max_depth``.

    Raises:
        ValueError: If ``max_depth < 0``.
    """
    if max_depth < 0:
        raise ValueError("max_depth must be non-negative.")

    root_vec = sp.Matrix([1, 1, 1])
    root = _make_node(root_vec, ())
    nodes: list[EqualityNode] = [root]
    if max_depth == 0:
        return nodes

    first_vec = NICOMACHUS_MATRIX_N1 * root_vec
    first_node = _make_node(first_vec, ("N1",))
    nodes.append(first_node)
    frontier: list[tuple[sp.Matrix, tuple[str, ...]]] = [(first_vec, ("N1",))]

    for _depth in range(2, max_depth + 1):
        next_frontier: list[tuple[sp.Matrix, tuple[str, ...]]] = []
        for vec, path in frontier:
            v1 = NICOMACHUS_MATRIX_N1 * vec
            p1 = (*path, "N1")
            nodes.append(_make_node(v1, p1))
            next_frontier.append((v1, p1))

            v2 = NICOMACHUS_MATRIX_N2 * vec
            p2 = (*path, "N2")
            nodes.append(_make_node(v2, p2))
            next_frontier.append((v2, p2))
        frontier = next_frontier

    return nodes


def unfold_five_species_from_equality() -> dict[str, EqualityNode]:
    """Exhibit Nicomachus's canonical derivation of all five species of inequality (I.23).

    Follows Hoche pp. 64–70 step-by-step:

    1. **Equality**: ``(1, 1, 1)`` (ratio ``1:1``)
    2. **Multiplex**: ``N1(1, 1, 1) = (1, 2, 4)`` (duple ``2:1``)
    3. **Superparticularis**: ``N2(1, 2, 4) = (4, 6, 9)`` (*hemiolios* ``3:2``)
    4. **Multiplex superparticularis**: ``N1(4, 6, 9) = (4, 10, 25)`` (``5:2``)
    5. **Superpartiens**: ``N2(4, 6, 9) = (9, 15, 25)`` (*epidimoiros* ``5:3``)
    6. **Multiplex superpartiens**: ``N1(9, 15, 25) = (9, 24, 64)`` (``8:3``)

    Returns:
        Mapping from canonical species key to its :class:`EqualityNode` witness.
    """
    v_eq = sp.Matrix([1, 1, 1])
    v_mult = NICOMACHUS_MATRIX_N1 * v_eq
    v_sup_partic = NICOMACHUS_MATRIX_N2 * v_mult
    v_mult_sup_partic = NICOMACHUS_MATRIX_N1 * v_sup_partic
    v_sup_partiens = NICOMACHUS_MATRIX_N2 * v_sup_partic
    v_mult_sup_partiens = NICOMACHUS_MATRIX_N1 * v_sup_partiens

    return {
        "equality": _make_node(v_eq, ()),
        "multiplex": _make_node(v_mult, ("N1",)),
        "superparticularis": _make_node(v_sup_partic, ("N1", "N2")),
        "multiplex_superparticularis": _make_node(v_mult_sup_partic, ("N1", "N2", "N1")),
        "superpartiens": _make_node(v_sup_partiens, ("N1", "N2", "N2")),
        "multiplex_superpartiens": _make_node(
            v_mult_sup_partiens, ("N1", "N2", "N2", "N1")
        ),
    }


def reduce_to_equality(
    a: int | sp.Integer,
    b: int | sp.Integer,
    c: int | sp.Integer,
) -> list[ReductionStep]:
    """Reduce any positive geometric triple ``(a, b, c)`` back to Equality (II.1–2).

    Applies Nicomachus's inverse subtraction matrix ``NICOMACHUS_INVERSE_MATRIX``
    (:math:`N_1^{-1}`) iteratively, reversing descending intermediate triples via
    ``REVERSAL_MATRIX_R`` until ``(g, g, g)`` is reached (``(1, 1, 1)`` for primitive triples).

    Args:
        a: First positive integer term of the geometric progression.
        b: Mean positive integer term satisfying ``b**2 == a * c``.
        c: Third positive integer term of the geometric progression.

    Returns:
        Chronological list of :class:`ReductionStep` records ending at Equality.

    Raises:
        ValueError: If ``(a, b, c)`` are non-positive or not in geometric progression.
    """
    ai, bi, ci = sp.Integer(a), sp.Integer(b), sp.Integer(c)
    if ai <= 0 or bi <= 0 or ci <= 0:
        raise ValueError(f"Triple must consist of positive integers; got {(ai, bi, ci)}.")
    if ai * ci != bi**2:
        raise ValueError(
            f"Triple {(ai, bi, ci)} is not in geometric progression: {ai}*{ci} != {bi}^2."
        )

    cur = (ci, bi, ai) if ai > ci else (ai, bi, ci)
    steps: list[ReductionStep] = []
    idx = 0

    while not (cur[0] == cur[1] == cur[2]):
        idx += 1
        vec = sp.Matrix([cur[0], cur[1], cur[2]])
        raw_vec = NICOMACHUS_INVERSE_MATRIX * vec
        raw = (sp.Integer(raw_vec[0]), sp.Integer(raw_vec[1]), sp.Integer(raw_vec[2]))
        if raw[0] > raw[2]:
            after = (raw[2], raw[1], raw[0])
            rev = True
            undone = "N2"
        else:
            after = raw
            rev = False
            undone = "N1"
        steps.append(
            ReductionStep(
                step_index=idx,
                before=cur,
                raw_subtracted=raw,
                reversed_order=rev,
                after=after,
                undone_rule=undone,
            )
        )
        cur = after

    return steps


@proposition(
    "Nic.I.23",
    kind="theorem",
    title="Nicomachus Equality Unfolding Rays & Unit Cross-Section",
    hide_guides=False,
)
def _prove_equality_rays(model: Model) -> list[spg.Point]:
    """Construct and verify the coprime root rays of Nicomachus's five species in ``model``."""
    o_pt = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    u_pt = model.given_point(sp.Integer(1), sp.Integer(0), ID="U")
    v_pt = model.given_point(sp.Integer(0), sp.Integer(1), ID="V")

    axis_x = model.construct_line(o_pt, u_pt, classes=["axis"], guide=True, by="Post.1")
    axis_y = model.construct_line(o_pt, v_pt, classes=["axis"], guide=True, by="Post.1")
    c_u = model.construct_circle(u_pt, o_pt, guide=True, by="Post.3")
    c_v = model.construct_circle(v_pt, o_pt, guide=True, by="Post.3")

    # Equality root E = (1, 1) representing (1, 1, 1) via circle intersection
    e_pt = model.intersect(c_u, c_v, other_than=o_pt, ID="E", by="Nic.I.17")
    unit_line = model.construct_line(u_pt, e_pt, classes=["unit-gauge"], by="Post.1")
    model.assert_perpendicular(axis_x, unit_line, by="I.11", label="Unit gauge x = 1")
    model.assert_equal((o_pt, u_pt), (u_pt, e_pt), by="Def.15", label="Monadic equality 1 : 1")

    # Duple root D = (1, 2) on x = 1 via circle centered at E through U -> (1, 1, 1) -> (1, 2, 4)
    c_e = model.construct_circle(e_pt, u_pt, guide=True, by="Post.3")
    d_pt = model.intersect(unit_line, c_e, other_than=u_pt, ID="D", by="Nic.I.23")
    model.assert_equal((u_pt, e_pt), (e_pt, d_pt), by="Def.15", label="Duple step 2 : 1")

    # Triple root T = (1, 3) on x = 1 -> (1, 3, 9)
    c_d = model.construct_circle(d_pt, e_pt, guide=True, by="Post.3")
    t_pt = model.intersect(unit_line, c_d, other_than=e_pt, ID="T", by="Nic.I.23")

    # Coprime lattice nodes for the remaining species:
    # H = (2, 3) hemiolios (4, 6, 9); M = (2, 5) mult.-superparticular (4, 10, 25);
    # S = (3, 5) superpartient (9, 15, 25); P = (3, 8) mult.-superpartient (9, 24, 64)
    h_pt = model.set_point(sp.Integer(2), sp.Integer(3), ID="H", classes=["species"], by="Nic.I.19")
    m_pt = model.set_point(sp.Integer(2), sp.Integer(5), ID="M", classes=["species"], by="Nic.I.21")
    s_pt = model.set_point(sp.Integer(3), sp.Integer(5), ID="S", classes=["species"], by="Nic.I.20")
    p_pt = model.set_point(sp.Integer(3), sp.Integer(8), ID="P", classes=["species"], by="Nic.I.22")

    ray_eq = model.construct_line(o_pt, e_pt, classes=["ray-equality"], by="Post.1")
    ray_dup = model.construct_line(o_pt, d_pt, classes=["ray-multiplex"], by="Post.1")
    ray_hem = model.construct_line(o_pt, h_pt, classes=["ray-superparticularis"], by="Post.1")
    ray_msp = model.construct_line(o_pt, m_pt, classes=["ray-multiplex-superparticularis"], by="Post.1")
    ray_spt = model.construct_line(o_pt, s_pt, classes=["ray-superpartiens"], by="Post.1")
    ray_mpr = model.construct_line(o_pt, p_pt, classes=["ray-multiplex-superpartiens"], by="Post.1")
    _ = (ray_eq, ray_dup, axis_y)

    # Intersect each species ray with the unit gauge line x = 1 to realize exact rational ratios
    q_hem = model.intersect(unit_line, ray_hem, ID="Q1", by="Nic.I.19")
    q_spt = model.intersect(unit_line, ray_spt, ID="Q2", by="Nic.I.20")
    q_msp = model.intersect(unit_line, ray_msp, ID="Q3", by="Nic.I.21")
    q_mpr = model.intersect(unit_line, ray_mpr, ID="Q4", by="Nic.I.22")

    model.assert_collinear(
        u_pt,
        e_pt,
        q_hem,
        q_spt,
        d_pt,
        q_msp,
        q_mpr,
        t_pt,
        by="Nic.I.23",
        label="All five species cut the unit gauge x = 1 in exact rational order",
    )

    seg_eq = model.construct_segment(o_pt, e_pt, classes=["equality"])
    seg_hem = model.construct_segment(o_pt, h_pt, classes=["superparticularis"])
    seg_spt = model.construct_segment(o_pt, s_pt, classes=["superpartiens"])
    model.conclude(
        e_pt,
        d_pt,
        t_pt,
        q_hem,
        q_spt,
        q_msp,
        q_mpr,
        seg_eq,
        seg_hem,
        seg_spt,
        kind="qed",
        by="Nic.I.23",
        label="Five species of inequality unfolded from monadic Equality",
    )
    return [e_pt, d_pt, t_pt, q_hem, q_spt, q_msp, q_mpr]


def construct_equality_ray_model() -> Model:
    """Build an exact :class:`~geometor.model.Model` of Nicomachus's five-species ratio rays.

    Constructs the root lattice ``(u, v)`` of coprime geometric triples ``(u^2, u v, v^2)``
    with ``auto_intersect=False``, cuts every species ray against the unit gauge line
    ``x = 1`` via :meth:`~geometor.model.Model.intersect`, and verifies the exact rational
    cross-sections ``1, 3/2, 5/3, 2, 5/2, 8/3, 3``.

    Returns:
        Verified exact symbolic :class:`~geometor.model.Model`.
    """
    model = Model("nicomachus_equality_rays", auto_intersect=False, logger=False)
    _prove_equality_rays(model)
    return model


def verify_equality_identities() -> dict[str, Any]:
    """Verify symbolically that ``N1, R, N2, N1^-1`` preserve the conic :math:`a c - b^2 = 0`.

    Returns:
        Summary dictionary of exact symbolic matrix and discriminant identities.

    Raises:
        AssertionError: If any algebraic invariant fails exact symbolic verification.
    """
    u, v = sp.symbols("u v", positive=True)
    a, b, c = sp.symbols("a b c")

    # 1. Unimodular & inverse identities
    assert NICOMACHUS_MATRIX_N1.det() == sp.Integer(1)
    assert REVERSAL_MATRIX_R.det() == sp.Integer(-1)
    assert NICOMACHUS_MATRIX_N2.det() == sp.Integer(-1)
    assert NICOMACHUS_MATRIX_N1 * NICOMACHUS_INVERSE_MATRIX == sp.eye(3)

    # 2. Preservation of geometric-mean discriminant b^2 - a*c for arbitrary triples (a, b, c)
    vec_abc = sp.Matrix([a, b, c])
    img1 = NICOMACHUS_MATRIX_N1 * vec_abc
    img2 = NICOMACHUS_MATRIX_N2 * vec_abc
    disc_orig = b**2 - a * c
    disc_img1 = sp.expand(img1[1] ** 2 - img1[0] * img1[2])
    disc_img2 = sp.expand(img2[1] ** 2 - img2[0] * img2[2])
    assert zero_test(disc_img1 - disc_orig)
    assert zero_test(disc_img2 - disc_orig)

    # 3. Veronese root-pair action (u^2, u*v, v^2) -> (u^2, u*(u+v), (u+v)^2) & (v^2, v*(u+v), (u+v)^2)
    veronese = sp.Matrix([u**2, u * v, v**2])
    v_n1 = sp.simplify(NICOMACHUS_MATRIX_N1 * veronese)
    v_n2 = sp.simplify(NICOMACHUS_MATRIX_N2 * veronese)
    assert zero_test(v_n1[0] - u**2)
    assert zero_test(v_n1[1] - u * (u + v))
    assert zero_test(v_n1[2] - (u + v) ** 2)
    assert zero_test(v_n2[0] - v**2)
    assert zero_test(v_n2[1] - v * (u + v))
    assert zero_test(v_n2[2] - (u + v) ** 2)

    # 4. Round-trip tree generation & reduction to (1, 1, 1) through depth 4
    tree = generate_equality_tree(max_depth=4)
    for node in tree:
        t0, t1, t2 = node.terms
        assert t0 * t2 == t1**2
        steps = reduce_to_equality(t0, t1, t2)
        if node.depth == 0:
            assert steps == []
        else:
            assert steps[-1].after == (sp.Integer(1), sp.Integer(1), sp.Integer(1))
            undone_forward = tuple(reversed([s.undone_rule for s in steps]))
            assert undone_forward == node.path

    # 5. Geometric ray gauge check
    ray_model = construct_equality_ray_model()
    u_pt = ray_model.get_element_by_ID("U")
    q_hem = ray_model.get_element_by_ID("Q1")
    assert quadrance(u_pt, q_hem) == sp.Rational(9, 4)
    assert intersect_2d(
        spg.Line(spg.Point(0, 0), spg.Point(3, 8)),
        spg.Line(spg.Point(1, 0), spg.Point(1, 1)),
    ) == [spg.Point(1, sp.Rational(8, 3))]

    return {
        "det_N1": int(NICOMACHUS_MATRIX_N1.det()),
        "det_N2": int(NICOMACHUS_MATRIX_N2.det()),
        "discriminant_invariant": True,
        "verified_tree_nodes": len(tree),
        "ray_model_steps": len(ray_model.steps),
    }
