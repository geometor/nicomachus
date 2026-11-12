r"""Sieve, Perfect Numbers, Polygonal Gnomons & Nicomachus's Cubes Theorem (Book I.13–16; Book II.6–20).

Formalizes Nicomachus of Gerasa's theory of absolute number (*καθ' ἑαυτὸ ποσόν*) and figurate
geometry of arithmetic:

- **Sieve of Eratosthenes** (*κόσκινον Ἐρατοσθένους*, I.13): Sieving the odd progression
  :math:`3, 5, 7, 9, \dots` by arithmetic strides to separate prime & incomposite numbers
  from secondary & composite numbers.
- **Abundant, Deficient & Perfect Numbers** (I.14–16): Classification by aliquot sum
  :math:`\sigma'(n)` and the Euclid–Nicomachus generation of :math:`6, 28, 496, 8128`.
- **Polygonal Numbers & Gnomons** (II.7–12): Exact arithmetic gnomons
  :math:`g(s, k) = 1 + (s - 2)(k - 1)`, polygonal numbers :math:`P(s, n)`, triangular
  decomposition :math:`P(s, n) = T_n + (s - 3) T_{n-1}`, and planar :class:`~geometor.model.Model`
  constructions over :math:`\mathbb{Q}` and :math:`\mathbb{Q}(\sqrt{3})`.
- **Same & Other — Squares vs. Heteromecic Numbers** (II.17–19): Odd gnomons summing to
  :math:`n^2` (*ταὐτόν*, Same) vs. even gnomons summing to :math:`n(n + 1)` (*θάτερον*, Other).
- **Pyramidal Numbers & Nicomachus's Sum-of-Cubes Theorem** (II.13–16, II.20): Odd blocks of
  length :math:`k` summing to :math:`k^3` and L-gnomon square dissection proving
  :math:`\sum_{k=1}^n k^3 = T_n^2`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, proposition, quadrance, zero_test


@dataclass(frozen=True)
class PolygonalGnomonResult:
    """Result bundle for an exact planar polygonal-gnomon construction.

    Attributes:
        sides: Number of polygon sides ``s >= 3``.
        order: Number of gnomon shells ``n >= 1``.
        model: Verified :class:`~geometor.model.Model` containing the pebble lattice and
            gnomon shell chains.
        shell_points: Mapping from 1-based shell index ``k`` to the ordered list of exact
            :class:`sympy.geometry.Point` instances added in the ``k``-th gnomon.
        gnomon_counts: Tuple ``(g(s, 1), ..., g(s, n))`` of shell pebble counts.
        cumulative_counts: Tuple ``(P(s, 1), ..., P(s, n))`` of total polygonal counts.
    """

    sides: int
    order: int
    model: Model
    shell_points: dict[int, list[spg.Point]]
    gnomon_counts: tuple[int, ...]
    cumulative_counts: tuple[int, ...]


@dataclass(frozen=True)
class NicomachusCubesResult:
    r"""Result bundle for Nicomachus's Sum-of-Cubes square dissection (Book II, Ch. 20).

    Attributes:
        order: Highest base ``n >= 1`` in :math:`1^3 + 2^3 + \dots + n^3 = T_n^2`.
        triangular_side: Master square side :math:`T_n = n(n + 1) / 2`.
        model: Verified :class:`~geometor.model.Model` containing the master square and
            all ``n`` L-gnomon polygons.
        odd_blocks: Mapping from ``k`` (``1..n``) to the tuple of ``k`` consecutive odd
            integers whose sum equals ``k**3``.
        shell_areas: Mapping from ``k`` (``1..n``) to the exact symbolic area of the ``k``-th
            gnomon polygon in ``model``.
        total_area: Exact symbolic area :math:`T_n^2` of the master square.
    """

    order: int
    triangular_side: sp.Integer
    model: Model
    odd_blocks: dict[int, tuple[int, ...]]
    shell_areas: dict[int, sp.Expr]
    total_area: sp.Integer


def sieve_of_eratosthenes(limit: int = 100) -> dict[str, Any]:
    r"""Execute Nicomachus's odd-number *koskinon* of Eratosthenes up to ``limit`` (I.13).

    Nicomachus sets out the odd integers :math:`3, 5, 7, 9, \dots` (treating the dyad ``2`` as
    the principle of the even rather than an odd prime) and marks composite odd numbers by
    striding ``p`` places among the odds (i.e. step ``2*p`` in integer value) from each
    unmarked prime ``p``.

    Args:
        limit: Upper integer bound ``>= 3``.

    Returns:
        Dictionary containing ``odd_sequence``, ``odd_primes``, ``all_primes`` (including ``2``),
        ``odd_composites``, and ``witness_factors`` mapping each composite odd to the ordered
        tuple of sieving primes that strike it.

    Raises:
        ValueError: If ``limit < 3``.
    """
    if limit < 3:
        raise ValueError("limit must be at least 3 for Nicomachus's odd sieve.")

    odds = list(range(3, limit + 1, 2))
    witnesses: dict[int, list[int]] = {m: [] for m in odds}

    for m in odds:
        if not witnesses[m]:
            # m is prime; strike m*3, m*5, ... (and all odd multiples > m)
            for mult in range(3 * m, limit + 1, 2 * m):
                witnesses[mult].append(m)

    odd_primes = [m for m in odds if not witnesses[m]]
    odd_composites = [m for m in odds if witnesses[m]]
    return {
        "limit": limit,
        "odd_sequence": tuple(odds),
        "odd_primes": tuple(odd_primes),
        "all_primes": (2, *odd_primes),
        "odd_composites": tuple(odd_composites),
        "witness_factors": {m: tuple(witnesses[m]) for m in odd_composites},
    }


def classify_abundant_deficient_perfect(n: int) -> dict[str, Any]:
    """Classify a positive integer ``n >= 2`` by its proper aliquot parts (Book I, Chs. 14–16).

    Args:
        n: Integer ``>= 2`` to classify.

    Returns:
        Dictionary with ``n``, ``aliquot_parts``, ``aliquot_sum``, ``classification``
        (``"perfect"``, ``"superabundant"``, or ``"deficient"``), and Nicomachean Greek/Latin
        labels.

    Raises:
        ValueError: If ``n < 2``.
    """
    if n < 2:
        raise ValueError("Aliquot classification requires n >= 2.")

    divs = [int(d) for d in sp.divisors(n) if int(d) < n]
    s_val = sum(divs)
    if s_val == n:
        cls = "perfect"
        gr, la = "τέλειος", "perfectus"
    elif s_val > n:
        cls = "superabundant"
        gr, la = "ὑπερτελής", "superfluus"
    else:
        cls = "deficient"
        gr, la = "ἐλλιπής", "diminutus"

    return {
        "n": n,
        "aliquot_parts": tuple(divs),
        "aliquot_sum": s_val,
        "classification": cls,
        "greek_term": gr,
        "latin_term": la,
    }


def euclid_nicomachus_perfect_numbers(count: int = 4) -> list[dict[str, Any]]:
    r"""Generate the first ``count`` Euclid–Nicomachus even perfect numbers (I.16; *Elem.* IX.36).

    Accumulates dyadic powers :math:`1 + 2 + 4 + \dots + 2^{p-1} = 2^p - 1`; whenever the sum
    is prime, multiplies it by the final dyadic term :math:`2^{p-1}` to yield
    :math:`P = 2^{p-1}(2^p - 1)`. For ``count = 4``, yields Nicomachus's canonical tetrad
    ``6, 28, 496, 8128`` across units, tens, hundreds, and thousands.

    Args:
        count: Number of even perfect numbers to generate (``1 <= count <= 7``).

    Returns:
        List of dictionaries detailing ``exponent``, ``mersenne_prime``, ``last_dyadic_term``,
        ``perfect_number``, and verified ``aliquot_sum``.

    Raises:
        ValueError: If ``count < 1`` or ``count > 7``.
    """
    if count < 1 or count > 7:
        raise ValueError("count must satisfy 1 <= count <= 7.")

    results: list[dict[str, Any]] = []
    p = 2
    while len(results) < count:
        mersenne = (1 << p) - 1
        if sp.isprime(mersenne):
            last_power = 1 << (p - 1)
            perf = last_power * mersenne
            # Exact multiplicative sigma formula verification
            sigma_all = int(sp.divisor_sigma(perf, 1))
            aliquot_sum = sigma_all - perf
            assert aliquot_sum == perf
            results.append(
                {
                    "exponent": p,
                    "mersenne_prime": mersenne,
                    "last_dyadic_term": last_power,
                    "perfect_number": perf,
                    "aliquot_sum": aliquot_sum,
                }
            )
        p += 1
    return results


def polygonal_number(sides: int | sp.Expr, n: int | sp.Expr) -> sp.Expr:
    r"""Return the exact ``n``-th ``sides``-gonal number :math:`P(s, n)` (Book II, Chs. 8–12).

    .. math::

        P(s, n) = \frac{(s - 2) n^2 - (s - 4) n}{2} = n + (s - 2)\frac{n(n - 1)}{2}

    Args:
        sides: Number of sides ``s >= 3`` (concrete integer or symbolic expression).
        n: Term index ``n >= 1`` (concrete integer or symbolic expression).

    Returns:
        Exact :class:`sympy.Integer` (for integer inputs) or simplified :class:`sympy.Expr`.

    Raises:
        ValueError: If concrete integer inputs violate ``sides >= 3`` or ``n >= 0``.
    """
    if isinstance(sides, int) and sides < 3:
        raise ValueError(f"Polygonal numbers require sides >= 3; got {sides}.")
    if isinstance(n, int) and n < 0:
        raise ValueError(f"Polygonal index n must be non-negative; got {n}.")

    s_sym = sp.sympify(sides)
    n_sym = sp.sympify(n)
    expr = ((s_sym - 2) * n_sym**2 - (s_sym - 4) * n_sym) / sp.Integer(2)
    return sp.simplify(expr)


def polygonal_gnomon(sides: int | sp.Expr, k: int | sp.Expr) -> sp.Expr:
    """Return the ``k``-th arithmetic gnomon :math:`g(s, k) = 1 + (s - 2)(k - 1)` (II.7–11).

    Args:
        sides: Number of polygon sides ``s >= 3``.
        k: 1-based gnomon shell index ``k >= 1``.

    Returns:
        Exact :class:`sympy.Integer` or simplified :class:`sympy.Expr`.

    Raises:
        ValueError: If concrete integer inputs violate ``sides >= 3`` or ``k >= 1``.
    """
    if isinstance(sides, int) and sides < 3:
        raise ValueError(f"Polygonal gnomon requires sides >= 3; got {sides}.")
    if isinstance(k, int) and k < 1:
        raise ValueError(f"Gnomon shell index k must be >= 1; got {k}.")

    s_sym = sp.sympify(sides)
    k_sym = sp.sympify(k)
    return sp.simplify(sp.Integer(1) + (s_sym - 2) * (k_sym - 1))


def heteromecic_number(n: int | sp.Expr) -> sp.Expr:
    """Return the ``n``-th oblong (*heteromecic*, *ἑτερομήκης*) number :math:`n(n + 1)` (II.17).

    Args:
        n: Non-negative integer or symbolic expression.

    Returns:
        Exact :class:`sympy.Integer` or simplified :class:`sympy.Expr`.

    Raises:
        ValueError: If concrete integer ``n < 0``.
    """
    if isinstance(n, int) and n < 0:
        raise ValueError(f"Heteromecic index n must be >= 0; got {n}.")
    n_sym = sp.sympify(n)
    return sp.simplify(n_sym * (n_sym + 1))


def pyramidal_number(sides: int | sp.Expr, n: int | sp.Expr) -> sp.Expr:
    r"""Return the ``n``-th ``sides``-gonal pyramidal number :math:`\sum_{k=1}^n P(s, k)` (II.13–14).

    .. math::

        \Pi(s, n) = \frac{n(n + 1)\bigl((s - 2) n - (s - 5)\bigr)}{6}

    Args:
        sides: Number of base sides ``s >= 3``.
        n: Pyramid height / layer count ``n >= 0``.

    Returns:
        Exact :class:`sympy.Integer` or simplified :class:`sympy.Expr`.

    Raises:
        ValueError: If concrete integer inputs violate ``sides >= 3`` or ``n >= 0``.
    """
    if isinstance(sides, int) and sides < 3:
        raise ValueError(f"Pyramidal base requires sides >= 3; got {sides}.")
    if isinstance(n, int) and n < 0:
        raise ValueError(f"Pyramidal height n must be >= 0; got {n}.")

    s_sym = sp.sympify(sides)
    n_sym = sp.sympify(n)
    expr = n_sym * (n_sym + 1) * ((s_sym - 2) * n_sym - (s_sym - 5)) / sp.Integer(6)
    return sp.simplify(expr)


@proposition(
    "Nic.II.12",
    kind="theorem",
    title="Polygonal Gnomon Shells & Unit-Quadrance Pebble Lattice",
    hide_guides=False,
)
def _prove_polygonal_gnomon_shells(
    model: Model,
    sides: int,
    order: int,
) -> dict[int, list[spg.Point]]:
    """Construct nested ``sides``-gonal gnomon shells with exact unit edge quadrances."""
    shell_points: dict[int, list[spg.Point]] = {}
    o_pt = model.given_point(sp.Integer(0), sp.Integer(0), ID="G1P1")
    shell_points[1] = [o_pt]

    if sides == 4:
        # Exact rational square lattice in Q^2: (1, 0) and (0, 1)
        rays = [
            (sp.Integer(1), sp.Integer(0)),
            (sp.Integer(1), sp.Integer(1)),
            (sp.Integer(0), sp.Integer(1)),
        ]
    else:
        # Nicomachus II.12 sector fan over Q(sqrt(3)): (s - 2) equilateral 60-degree triangles
        # Every consecutive pebble along every gnomon shell has exact unit quadrance Q = 1!
        half = sp.Rational(1, 2)
        h_tri = sp.sqrt(3) / sp.Integer(2)
        unit_dirs = [
            (sp.Integer(1), sp.Integer(0)),
            (half, h_tri),
            (-half, h_tri),
            (sp.Integer(-1), sp.Integer(0)),
            (-half, -h_tri),
            (half, -h_tri),
        ]
        rays = unit_dirs[: sides - 1]

    sample_unit_segments: list[spg.Segment] = []
    for k in range(2, order + 1):
        m = k - 1
        pts_k: list[spg.Point] = []
        p_idx = 0
        for r_i in range(sides - 2):
            rx0, ry0 = rays[r_i]
            rx1, ry1 = rays[r_i + 1]
            vx0, vy0 = m * rx0, m * ry0
            vx1, vy1 = m * rx1, m * ry1
            j_start = 0 if r_i == 0 else 1
            for j in range(j_start, m + 1):
                t_rat = sp.Rational(j, m)
                px = vx0 + t_rat * (vx1 - vx0)
                py = vy0 + t_rat * (vy1 - vy0)
                p_idx += 1
                pt = model.set_point(
                    px,
                    py,
                    ID=f"G{k}P{p_idx}",
                    classes=[f"gnomon-{k}"],
                    by="Nic.II.8",
                )
                pts_k.append(pt)

        shell_points[k] = pts_k
        for idx_seg in range(len(pts_k) - 1):
            seg = model.construct_segment(
                pts_k[idx_seg],
                pts_k[idx_seg + 1],
                classes=[f"shell-{k}"],
                by="Post.1",
            )
            sample_unit_segments.append(seg)

    if len(sample_unit_segments) >= 2:
        model.assert_equal(
            *sample_unit_segments,
            by="Nic.II.12",
            label="Every pebble step along every gnomon shell has unit quadrance Q = 1",
        )

    conclude_items: list[Any] = [o_pt, *sample_unit_segments]
    model.conclude(
        *conclude_items,
        kind="qed",
        by="Nic.II.12",
        label=f"{sides}-gonal gnomon accumulation verified through order {order}",
    )
    return shell_points


def construct_polygonal_gnomon_model(
    sides: int = 4,
    order: int = 4,
) -> PolygonalGnomonResult:
    r"""Build an exact :class:`~geometor.model.Model` of ``sides``-gonal gnomon shells.

    Supports triangular (``3``), square (``4``), pentagonal (``5``), hexagonal (``6``), and
    heptagonal (``7``) lattices with ``auto_intersect=False``. For ``sides == 4`` uses the
    Gaussian integer lattice :math:`\mathbb{Q}^2`; for ``sides in {3, 5, 6, 7}`` uses
    Nicomachus's Book II, Ch. 12 decomposition into ``(sides - 2)`` equilateral triangular
    sectors in :math:`\mathbb{Q}(\sqrt{3})` so every shell step has exact unit quadrance.

    Args:
        sides: Number of polygon sides (``3 <= sides <= 7``).
        order: Number of gnomon shells to construct (``1 <= order <= 6``).

    Returns:
        Verified :class:`PolygonalGnomonResult`.

    Raises:
        ValueError: If ``sides`` is outside ``3..7`` or ``order < 1``.
    """
    if sides < 3 or sides > 7:
        raise ValueError(f"construct_polygonal_gnomon_model supports 3 <= sides <= 7; got {sides}.")
    if order < 1:
        raise ValueError(f"order must be >= 1; got {order}.")

    model = Model(f"nicomachus_{sides}_gon_order_{order}", auto_intersect=False, logger=False)
    shell_points = _prove_polygonal_gnomon_shells(model, sides, order)

    g_counts = tuple(len(shell_points[k]) for k in range(1, order + 1))
    cum_counts: list[int] = []
    running = 0
    for c in g_counts:
        running += c
        cum_counts.append(running)

    for k in range(1, order + 1):
        assert g_counts[k - 1] == int(polygonal_gnomon(sides, k))
        assert cum_counts[k - 1] == int(polygonal_number(sides, k))

    return PolygonalGnomonResult(
        sides=sides,
        order=order,
        model=model,
        shell_points=shell_points,
        gnomon_counts=g_counts,
        cumulative_counts=tuple(cum_counts),
    )


@proposition(
    "Nic.II.20",
    kind="theorem",
    title="Nicomachus Sum-of-Cubes Square Dissection",
    hide_guides=False,
)
def _prove_nicomachus_cubes(
    model: Model,
    order: int,
) -> tuple[spg.Polygon, dict[int, spg.Polygon]]:
    r"""Construct the master :math:`T_n \times T_n` square and its :math:`k^3` gnomon shells."""
    o_pt = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    u_pt = model.given_point(sp.Integer(1), sp.Integer(0), ID="X1")
    v_pt = model.given_point(sp.Integer(0), sp.Integer(1), ID="Y1")

    axis_x = model.construct_line(o_pt, u_pt, classes=["axis"], guide=True, by="Post.1")
    axis_y = model.construct_line(o_pt, v_pt, classes=["axis"], guide=True, by="Post.1")
    model.assert_perpendicular(axis_x, axis_y, by="Post.4", label="Orthogonal square axes")

    c_u = model.construct_circle(u_pt, o_pt, guide=True, by="Post.3")
    c_v = model.construct_circle(v_pt, o_pt, guide=True, by="Post.3")
    d1 = model.intersect(c_u, c_v, other_than=o_pt, ID="D1", by="I.46")
    diag = model.construct_line(o_pt, d1, classes=["diagonal"], guide=True, by="Post.1")

    x_pts: dict[int, spg.Point] = {0: o_pt, 1: u_pt}
    y_pts: dict[int, spg.Point] = {0: o_pt, 1: v_pt}
    d_pts: dict[int, spg.Point] = {0: o_pt, 1: d1}
    shells: dict[int, spg.Polygon] = {}

    # Shell 1: unit cube 1^3 = 1 as unit square < O X1 D1 Y1 >
    shells[1] = model.construct_polygon(
        [o_pt, u_pt, d1, v_pt],
        classes=["cube-shell-1"],
        ID="Cube1",
        by="Nic.II.20",
    )

    for k in range(2, order + 1):
        t_k = sp.Integer(k * (k + 1) // 2)
        xk = model.set_point(t_k, sp.Integer(0), ID=f"X{k}", by="Nic.II.8")
        yk = model.set_point(sp.Integer(0), t_k, ID=f"Y{k}", by="Nic.II.8")
        # Construct vertical & horizontal gauge lines and intersect diagonal to obtain Dk(T_k, T_k)
        xk_up = model.set_point(t_k, sp.Integer(1), ID=f"U{k}", guide=True, by="I.11")
        vert_k = model.construct_line(
            xk,
            xk_up,
            guide=True,
            by="I.11",
        )
        dk = model.intersect(vert_k, diag, ID=f"D{k}", by="Post.1")
        model.assert_equal(
            (o_pt, xk),
            (o_pt, yk),
            (xk, dk),
            (yk, dk),
            by="I.46",
            label=f"Square of side T_{k} = {t_k}",
        )
        x_pts[k] = xk
        y_pts[k] = yk
        d_pts[k] = dk

        shells[k] = model.construct_polygon(
            [x_pts[k - 1], xk, dk, yk, y_pts[k - 1], d_pts[k - 1]],
            classes=[f"cube-shell-{k}"],
            ID=f"Cube{k}",
            by="Nic.II.20",
        )

    master_sq = model.construct_polygon(
        [o_pt, x_pts[order], d_pts[order], y_pts[order]],
        classes=["master-triangular-square"],
        ID="TriSquare",
        by="I.46",
    )
    model.conclude(
        master_sq,
        *shells.values(),
        kind="qed",
        by="Nic.II.20",
        label=f"Sum of first {order} cubes equals T_{order}^2",
    )
    return master_sq, shells


def construct_nicomachus_cubes_model(order: int = 4) -> NicomachusCubesResult:
    r"""Build an exact :class:`~geometor.model.Model` proving :math:`\sum_{k=1}^n k^3 = T_n^2` (II.20).

    Pairs Nicomachus's odd-number block partition
    (:math:`1 = 1^3,\; 3 + 5 = 2^3,\; 7 + 9 + 11 = 3^3, \dots`) with the exact L-gnomon
    square dissection of :math:`[0, T_n]^2` at triangular coordinates
    :math:`T_k = k(k + 1) / 2`, verifying symbolically that the ``k``-th gnomon polygon has
    area :math:`T_k^2 - T_{k-1}^2 = k^3`.

    Args:
        order: Highest integer ``n >= 1`` (default ``4``, where :math:`T_4 = 10` and
            :math:`1 + 8 + 27 + 64 = 100`).

    Returns:
        Verified :class:`NicomachusCubesResult`.

    Raises:
        ValueError: If ``order < 1``.
    """
    if order < 1:
        raise ValueError(f"order must be >= 1; got {order}.")

    model = Model(f"nicomachus_cubes_{order}", auto_intersect=False, logger=False)
    master_sq, shells = _prove_nicomachus_cubes(model, order)

    odd_blocks: dict[int, tuple[int, ...]] = {}
    shell_areas: dict[int, sp.Expr] = {}
    for k in range(1, order + 1):
        first_odd = k * (k - 1) + 1
        block = tuple(first_odd + 2 * j for j in range(k))
        assert sum(block) == k**3
        odd_blocks[k] = block

        area_k = sp.simplify(abs(shells[k].area))
        assert zero_test(area_k - sp.Integer(k**3))
        shell_areas[k] = area_k

    t_n = sp.Integer(order * (order + 1) // 2)
    master_area = sp.simplify(abs(master_sq.area))
    assert zero_test(master_area - t_n**2)
    assert zero_test(sum(shell_areas.values(), sp.Integer(0)) - master_area)

    return NicomachusCubesResult(
        order=order,
        triangular_side=t_n,
        model=model,
        odd_blocks=odd_blocks,
        shell_areas=shell_areas,
        total_area=sp.Integer(master_area),
    )


def verify_figurate_identities() -> dict[str, Any]:
    """Verify symbolically all Nicomachean figurate, oblong, pyramidal, and cube laws.

    Returns:
        Summary dictionary of verified symbolic identities and perfect numbers.

    Raises:
        AssertionError: If any identity fails exact SymPy verification.
    """
    s, n, k = sp.symbols("s n k", integer=True, positive=True)

    # 1. Gnomon summation: sum_{k=1}^n g(s, k) == P(s, n)
    gnomon_sum = sp.summation(polygonal_gnomon(s, k), (k, 1, n))
    assert zero_test(sp.simplify(gnomon_sum - polygonal_number(s, n)))

    # 2. Nicomachus II.12 triangular decomposition: P(s, n) == T_n + (s - 3) * T_{n-1}
    decomp = polygonal_number(3, n) + (s - 3) * polygonal_number(3, n - 1)
    assert zero_test(sp.simplify(polygonal_number(s, n) - decomp))

    # 3. Consecutive triangles form a square: T_{n-1} + T_n == n^2
    assert zero_test(sp.simplify(polygonal_number(3, n - 1) + polygonal_number(3, n) - n**2))

    # 4. Same (squares) vs. Other (heteromecic oblongs) harmonic weave (II.17–19)
    sq_n = polygonal_number(4, n)
    sq_next = polygonal_number(4, n + 1)
    het_n = heteromecic_number(n)
    assert zero_test(sp.simplify(sq_n * sq_next - het_n**2))
    assert zero_test(sp.simplify(het_n - sq_n - n))
    assert zero_test(sp.simplify(sq_next - het_n - (n + 1)))
    assert zero_test(sp.simplify(heteromecic_number(n) - 2 * polygonal_number(3, n)))

    # 5. Pyramidal summation: sum_{k=1}^n P(s, k) == Pi(s, n)
    pyr_sum = sp.summation(polygonal_number(s, k), (k, 1, n))
    assert zero_test(sp.simplify(pyr_sum - pyramidal_number(s, n)))

    # 6. Nicomachus II.20 Sum of Cubes: sum_{k=1}^n k^3 == (T_n)^2
    cubes_sum = sp.summation(k**3, (k, 1, n))
    assert zero_test(sp.simplify(cubes_sum - polygonal_number(3, n) ** 2))

    # 7. Canonical 4 Perfect numbers & composite 2^11 - 1 = 2047 = 23 * 89 check
    perfs = [item["perfect_number"] for item in euclid_nicomachus_perfect_numbers(4)]
    assert perfs == [6, 28, 496, 8128]
    assert not sp.isprime((1 << 11) - 1)

    # 8. Planar unit-quadrance check in Q(sqrt(3)) for pentagonal gnomon shell
    pent = construct_polygonal_gnomon_model(sides=5, order=3)
    pts3 = pent.shell_points[3]
    assert all(quadrance(pts3[i], pts3[i + 1]) == sp.Integer(1) for i in range(len(pts3) - 1))

    return {
        "gnomon_sum_verified": True,
        "triangular_decomposition_verified": True,
        "same_other_geometric_mean_verified": True,
        "pyramidal_sum_verified": True,
        "nicomachus_cubes_verified": True,
        "canonical_perfect_numbers": tuple(perfs),
    }
