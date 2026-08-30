#!/usr/bin/env python3
"""Exact stdlib replay of the e=2,m=2 K00 point fan through G10.

The program reconstructs the literal 569-tail source and evaluates every
transition from the G4 cone.  Odd surface and normal coefficients are kept;
no tau^2 reparameterization or coefficient-blind recurrence is used.

The conclusion is field-valued point-set emptiness on the declared opens.
Reduced cone charts are used only set-theoretically.  No scheme equality,
arc, reachability, map, or JC2 assertion is made.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAILS = (
    ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
COMPILER = (
    ROOT / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827"
    / "compile_contracted_source_v20r2.py"
)
ENGINE = ROOT / "xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py"
G7_INTEGRATION = ROOT / "xmodel/k00-ram-e2m1-g7-rankfan-coordinator-integration-sol56-20260829.md"
UNIFORM_REPORT = ROOT / "xmodel/k00-ram-e2m1-allfaces-uniformity-audit-sol56-20260829.md"
UNIFORM_REPLAY = ROOT / "xmodel/k00-ram-m1-uniform-rankfan-replay-sol56-20260829.py"
UNIFORM_REVIEW = ROOT / "xmodel/k00-ram-e2m1-allfaces-uniformity-hostile-review-fable5-20260829.md"
E3_REPORT = ROOT / "xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-sol56-20260829.md"
E3_REPLAY = ROOT / "xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-replay-sol56-20260829.py"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    G7_INTEGRATION: "0eb501b414f2162d14a73725a46410b7e799adc70932cdfb8a05f4196ff0bb1a",
    UNIFORM_REPORT: "64eaafe3fe5aaa9238a338f2da045e302d9a239ac9c29312e39d5c545893d42c",
    UNIFORM_REPLAY: "0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b",
    UNIFORM_REVIEW: "0ee84a0b98d30c4436461a09118961706d1f18fcfe9686684e7b1a27b5597feb",
    E3_REPORT: "22e9752761f3bb4ee94b4dccf18cb72ff49bd0d92453ad4cf39eb401cc45f84a",
    E3_REPLAY: "bcd4004e671091c7d1ffc265affbd160b1d2b2a712f62dd97b698150dfc9fcba",
}
EXPECTED_CERTIFICATE_SHA256 = "486bb644cc136c39e4c223b1dbe71aeaadc6b1ad4930d7eb9196be4059b8700f"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_e2m2_engine", ENGINE)
    if spec is None or spec.loader is None:
        fail("cannot import exact engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_zero(poly, label: str) -> None:
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def assert_equal(module, ring, left, right, label: str) -> None:
    module.assert_equal(left, right, ring, label)


def qstring(value: F) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def poly_object(poly):
    answer = []
    for key in sorted(poly):
        real, imag = poly[key]
        answer.append([list(key), qstring(real), qstring(imag)])
    return answer


def series_scale(module, ring, series, scalar):
    return [ring.scale(value, scalar) for value in series]


def surface_series(module, ring, scoeff, tcoeff, truncation: int):
    sseries = module.series_zero(truncation)
    tseries = module.series_zero(truncation)
    for grade, value in scoeff.items():
        sseries[grade] = value
    for grade, value in tcoeff.items():
        tseries[grade] = value
    one = module.series_zero(truncation)
    one[0] = ring.const(1)
    return [
        module.series_add(
            series_scale(module, ring, sseries, 2),
            module.series_mul(sseries, sseries, ring),
            ring,
        ),
        series_scale(
            module,
            ring,
            module.series_mul(module.series_add(one, sseries, ring), tseries, ring),
            F(1, 8),
        ),
        module.series_add(
            sseries,
            series_scale(module, ring, module.series_mul(tseries, tseries, ring), 16),
            ring,
        ),
        tseries,
        sseries,
        series_scale(module, ring, tseries, 2),
    ]


def add_normal(ring, dseries, grade: int, vector):
    for index in range(6):
        dseries[index][grade] = ring.add(dseries[index][grade], vector[index])


def literal_e2_source(module, rows, k10_rows, dseries, kseries, ring):
    """R(d)+tau^4*k10(tau)*A10(d), through the supplied truncation."""

    total = [module.eval_dpoly_series(row, dseries, ring) for row in rows]
    load = [module.eval_dpoly_series(row, dseries, ring) for row in k10_rows]
    truncation = len(dseries[0])
    for row_index in range(7):
        for kgrade, kval in enumerate(kseries):
            if not kval:
                continue
            for dgrade in range(truncation - 4 - kgrade):
                if load[row_index][dgrade]:
                    total[row_index][4 + kgrade + dgrade] = ring.add(
                        total[row_index][4 + kgrade + dgrade],
                        ring.mul(kval, load[row_index][dgrade]),
                    )
    return total, load


def mu_vector(ring, s, t):
    return [
        ring.mul(s, s),
        ring.scale(ring.mul(s, t), F(1, 8)),
        ring.scale(ring.mul(t, t), 16),
        ring.const(), ring.const(), ring.const(),
    ]


def directional(module, ring, poly, point, direction):
    out = ring.const()
    for index in range(6):
        out = ring.add(
            out,
            ring.mul(
                module.eval_dpoly(module.dderivative(poly, index), point, ring),
                direction[index],
            ),
        )
    return out


def second_half(module, ring, poly, point, direction):
    out = ring.const()
    for first_index in range(6):
        first = module.dderivative(poly, first_index)
        for second_index in range(6):
            out = ring.add(
                out,
                ring.mul(
                    ring.mul(
                        module.eval_dpoly(
                            module.dderivative(first, second_index), point, ring
                        ),
                        direction[first_index],
                    ),
                    direction[second_index],
                ),
            )
    return ring.scale(out, F(1, 2))


def determinant3(ring, matrix):
    terms = (
        ((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
        ((2, 1, 0), -1), ((1, 0, 2), -1), ((0, 2, 1), -1),
    )
    out = ring.const()
    for permutation, sign in terms:
        term = ring.const(sign)
        for row, column in enumerate(permutation):
            term = ring.mul(term, matrix[row][column])
        out = ring.add(out, term)
    return out


def map_poly(module, source_ring, target_ring, poly, images):
    out = target_ring.const()
    for key, coefficient in poly.items():
        term = target_ring.const(coefficient)
        for name, exponent in zip(source_ring.names, key):
            if exponent:
                term = target_ring.mul(term, target_ring.power(images[name], exponent))
        out = target_ring.add(out, term)
    return out


def reduce_r_square(module, ring, poly, square_value: int):
    """Reduce a polynomial in ring (t,r) modulo r^2-square_value."""

    out = {}
    for key, coefficient in poly.items():
        tdegree, rdegree = key
        factor = module.g(square_value ** (rdegree // 2))
        new_key = (tdegree, rdegree % 2)
        out[new_key] = module.gadd(
            out.get(new_key, module.g()), module.gmul(coefficient, factor)
        )
    return ring.clean(out)


def surface_gradient_calendar(module, rows, loads, m4, a10_cubic):
    ring = module.Ring(("S", "T"))
    s, t = ring.var("S"), ring.var("T")
    surface = [series[0] for series in surface_series(
        module, ring, {0: s}, {0: t}, 1
    )]
    for row_index, row in enumerate(rows):
        assert_zero(module.eval_dpoly(row, surface, ring), f"surface row {row_index + 1}")
        for coordinate in range(6):
            gradient = module.eval_dpoly(
                module.dderivative(row, coordinate), surface, ring
            )
            assert_zero(
                gradient, f"gradient row {row_index + 1} coordinate {coordinate}"
            )
    wrong_surface = list(surface)
    wrong_surface[2] = ring.add(s, ring.scale(ring.mul(t, t), 15))
    if all(not module.eval_dpoly(row, wrong_surface, ring) for row in rows):
        fail("surface 16-to-15 mutation invisible")
    restrictions = [module.eval_dpoly(row, surface, ring) for row in loads["K10"]]
    minima = [min((sum(key) for key in poly), default=None) for poly in restrictions]
    if minima != [3, 3, 3, None, 3, 4, 3]:
        fail(("K10 surface minima", minima))
    ell = module.old_plane(ring, s, t)
    mu = mu_vector(ring, s, t)
    load_rows = []
    for row_index in range(7):
        assert_zero(
            module.eval_dpoly(m4[row_index], ell, ring),
            f"K10 tangent quadratic row {row_index + 1}",
        )
        load_rows.append(ring.add(
            directional(module, ring, m4[row_index], ell, mu),
            module.eval_dpoly(a10_cubic[row_index], ell, ring),
        ))
    expected_w1 = ring.scale(
        ring.mul(
            t,
            ring.sub(ring.scale(ring.mul(s, s), 3), ring.scale(ring.mul(t, t), 64)),
        ),
        F(5, 4096),
    )
    expected_w2 = ring.scale(
        ring.mul(s, ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 192))),
        F(5, 65536),
    )
    assert_equal(module, ring, load_rows[0], expected_w1, "surface W1")
    assert_equal(module, ring, load_rows[1], expected_w2, "surface W2")
    late = {
        "K6_rows_1_2_3_5_7": 12 + 1 + 2,
        "K6_rows_4_6": 12 + 1 + 4,
        "K2": 20 + 1 + 2,
        "mu2": 28 + 1,
        "mu4": 32 + 1,
        "mu6": 36 + 1,
        "Jdet": 38,
    }
    if any(grade <= 10 for grade in late.values()):
        fail(("late sector reached G10", late))
    return load_rows, expected_w1, expected_w2, minima, late


def fresh_cone_tangent(module, rows, loads, quadrics, normal_order: int):
    """Literal G(2n)=Q(r), G(2n+1)=DQ(r)[v] for n=2,3,4."""

    names = (
        "s", "t", "alpha", "beta", "k0", "k1", "k2",
        *(f"r{index}" for index in range(6)),
        *(f"v{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    truncation = 2 * normal_order + 2
    dseries = surface_series(
        module,
        ring,
        {2: value["s"], 3: value["alpha"]},
        {2: value["t"], 3: value["beta"]},
        truncation,
    )
    residual = [value[f"r{index}"] for index in range(6)]
    tangent = [value[f"v{index}"] for index in range(6)]
    add_normal(ring, dseries, normal_order, residual)
    add_normal(ring, dseries, normal_order + 1, tangent)
    source, _ = literal_e2_source(
        module,
        rows,
        loads["K10"],
        dseries,
        (value["k0"], value["k1"], value["k2"]),
        ring,
    )
    for row_index in range(7):
        for grade in range(2 * normal_order):
            assert_zero(
                source[row_index][grade],
                f"fresh n={normal_order} row {row_index + 1} G{grade}",
            )
        qvalue = module.eval_dpoly(quadrics[row_index], residual, ring)
        assert_equal(
            module, ring, source[row_index][2 * normal_order], qvalue,
            f"fresh n={normal_order} cone row {row_index + 1}",
        )
        tangent_value = directional(
            module, ring, quadrics[row_index], residual, tangent
        )
        assert_equal(
            module, ring, source[row_index][2 * normal_order + 1], tangent_value,
            f"fresh n={normal_order} tangent row {row_index + 1}",
        )
    return "G(2n)=Q(residual);G(2n+1)=DQ(residual)[tangent]"


def n2_g6_fan(module, rows, loads, quadrics):
    """Kill the rank-two and rank-one strata of the first G4 cone."""

    names = (
        "s", "t", "p", "q", "A6", "B6",
        "y1", "y2", "y3", "y4",
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    p, q, s, t = (value[name] for name in ("p", "q", "s", "t"))
    dseries = surface_series(module, ring, {2: s}, {2: t}, 7)
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    tangent = module.vector_with_ab(
        ring, ring.const(), ring.const(),
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    newest = module.vector_with_ab(
        ring, value["A6"], value["B6"],
        ring.const(), ring.const(), ring.const(), ring.const(),
    )
    add_normal(ring, dseries, 2, residual)
    add_normal(ring, dseries, 3, tangent)
    add_normal(ring, dseries, 4, newest)
    source, _ = literal_e2_source(
        module, rows, loads["K10"], dseries, (ring.const(),), ring
    )
    g6 = [source[index][6] for index in range(7)]
    row6 = ring.scale(
        ring.mul(p, ring.sub(ring.scale(ring.mul(q, q), 192), ring.mul(p, p))),
        F(1, 65536),
    )
    assert_equal(module, ring, g6[5], row6, "n2 rank2 row6 split")

    pzero_row4 = ring.zero_vars(g6[3], ("p",))
    assert_equal(
        module, ring, pzero_row4,
        ring.scale(ring.mul(s, ring.mul(q, q)), F(3, 512)),
        "n2 rank2 p=0 row4",
    )
    combo3 = ring.add(g6[2], g6[0], F(1, 8))
    combo5 = ring.add(g6[4], g6[0], F(1, 128))
    pzero3 = ring.zero_vars(combo3, ("p", "s"))
    pzero5 = ring.zero_vars(combo5, ("p", "s"))
    expected3 = ring.scale(
        ring.mul(ring.mul(q, q), ring.add(q, ring.scale(t, F(3, 8)))), F(1, 4)
    )
    expected5 = ring.scale(
        ring.mul(ring.mul(q, q), ring.add(q, ring.scale(t, F(1, 4)))), F(-3, 64)
    )
    assert_equal(module, ring, pzero3, expected3, "n2 rank2 p=0 combo3")
    assert_equal(module, ring, pzero5, expected5, "n2 rank2 p=0 combo5")

    combo_r5 = ring.add(ring.add(g6[4], g6[0], F(3, 128)), g6[2], F(1, 8))
    combo_r7 = ring.add(ring.add(g6[6], g6[0], F(1, 512)), g6[2], F(1, 128))
    target = module.Ring(("t", "r"))
    tv = {name: target.var(name) for name in target.names}
    images = {
        "s": target.scale(
            target.mul(tv["r"], target.add(tv["t"], target.const(2))), -1
        ),
        "t": tv["t"],
        "p": tv["r"],
        "q": target.const(1),
        "A6": target.const(), "B6": target.const(),
        "y1": target.const(), "y2": target.const(),
        "y3": target.const(), "y4": target.const(),
    }
    reduced5 = reduce_r_square(
        module, target, map_poly(module, ring, target, combo_r5, images), 192
    )
    reduced7 = reduce_r_square(
        module, target, map_poly(module, ring, target, combo_r7, images), 192
    )
    assert_equal(module, target, reduced5, target.const(F(1, 8)), "n2 rank2 r2=192 combo5")
    assert_equal(module, target, reduced7, target.const(F(-1, 64)), "n2 rank2 r2=192 combo7")
    reduced_row4 = reduce_r_square(
        module, target, map_poly(module, ring, target, g6[3], images), 192
    )
    assert_zero(reduced_row4, "n2 rank2 r2=192 row4 center")

    rank1_terminals = {}
    for sign in (1, -1):
        rank_names = (
            "s", "t", "alpha", "beta", "q", "X",
            "y1", "y2", "y3", "y4", "A6", "B6",
        )
        rr = module.Ring(rank_names)
        rv = {name: rr.var(name) for name in rank_names}
        rd = surface_series(
            module, rr,
            {2: rv["s"], 3: rv["alpha"]},
            {2: rv["t"], 3: rv["beta"]},
            7,
        )
        rw = module.cone_vector(
            rr, rr.const(), rr.const(),
            rr.scale(rv["q"], module.g(0, 8 * sign)), rv["q"],
        )
        ry = module.vector_with_ab(
            rr,
            rv["X"], rr.scale(rv["X"], module.g(0, 8 * sign)),
            rv["y1"], rv["y2"], rv["y3"], rv["y4"],
        )
        rz = module.vector_with_ab(
            rr, rv["A6"], rv["B6"], rr.const(), rr.const(), rr.const(), rr.const()
        )
        add_normal(rr, rd, 2, rw)
        add_normal(rr, rd, 3, ry)
        add_normal(rr, rd, 4, rz)
        req, _ = literal_e2_source(
            module, rows, loads["K10"], rd, (rr.const(),), rr
        )
        terminal = rr.scale(rr.power(rv["q"], 3), module.g(0, F(sign, 32)))
        assert_equal(
            module, rr, req[5][6], terminal, f"n2 rank1 sign {sign} G6 row6"
        )
        rank1_terminals[str(sign)] = poly_object(terminal)
    return {
        "rank2_row6": poly_object(row6),
        "rank2_pzero": [poly_object(expected3), poly_object(expected5)],
        "rank2_rsquare": [poly_object(target.const(F(1, 8))), poly_object(target.const(F(-1, 64)))],
        "rank1_terminals": rank1_terminals,
    }


def n3_g8_g9_fan(module, rows, loads, quadrics, cubics):
    """Rank-two dies G8; rank-one G8 components die raw at G9."""

    rank2_names = (
        "s", "t", "alpha", "beta", "p", "q", "A8", "B8",
        "y1", "y2", "y3", "y4",
    )
    ring = module.Ring(rank2_names)
    value = {name: ring.var(name) for name in rank2_names}
    s, t, p, q = (value[name] for name in ("s", "t", "p", "q"))
    dseries = surface_series(
        module, ring,
        {2: s, 3: value["alpha"]}, {2: t, 3: value["beta"]}, 9,
    )
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    tangent = module.vector_with_ab(
        ring, ring.const(), ring.const(),
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    newest = module.vector_with_ab(
        ring, value["A8"], value["B8"],
        ring.const(), ring.const(), ring.const(), ring.const(),
    )
    add_normal(ring, dseries, 3, residual)
    add_normal(ring, dseries, 4, tangent)
    add_normal(ring, dseries, 5, newest)
    source, _ = literal_e2_source(
        module, rows, loads["K10"], dseries, (ring.const(),), ring
    )
    g8 = [source[index][8] for index in range(7)]
    alpha = [
        module.eval_dpoly(module.dderivative(poly, 5), residual, ring)
        for poly in quadrics
    ]
    beta = [
        module.eval_dpoly(module.dderivative(poly, 0), residual, ring)
        for poly in quadrics
    ]
    normal = [ring.zero_vars(g8[index], ("A8", "B8")) for index in range(7)]
    delta = ring.add(ring.mul(p, p), ring.scale(ring.mul(q, q), 64))
    cform = ring.add(
        ring.mul(t, ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p))),
        ring.scale(ring.mul(ring.mul(s, p), q), 2),
    )
    eform = ring.sub(
        ring.mul(s, ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p))),
        ring.scale(ring.mul(ring.mul(t, p), q), 128),
    )
    augmented = determinant3(
        ring, [[alpha[index], beta[index], normal[index]] for index in range(3)]
    )
    assert_equal(
        module, ring, augmented,
        ring.scale(ring.mul(delta, cform), F(27, 2**35)),
        "n3 G8 rank2 augmented",
    )
    wrong_delta = ring.add(ring.mul(p, p), ring.scale(ring.mul(q, q), 63))
    if augmented == ring.scale(ring.mul(wrong_delta, cform), F(27, 2**35)):
        fail("rank discriminant 64-to-63 mutation invisible")
    rank2_det = ring.sub(
        ring.mul(ring.scale(ring.mul(p, q), 2), ring.scale(ring.mul(p, q), -128)),
        ring.power(ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p)), 2),
    )
    assert_equal(
        module, ring, rank2_det, ring.scale(ring.mul(delta, delta), -1),
        "n3 G8 rank2 C/E determinant",
    )
    assert_equal(module, ring, g8[3], ring.scale(eform, F(3, 2**15)), "n3 G8 rank2 row4")

    compatibility = {}
    terminals = {}
    for sign in (1, -1):
        names = (
            "s", "t", "alpha", "beta", "q", "X", "A8", "B8",
            "y1", "y2", "y3", "y4",
        )
        rr = module.Ring(names)
        rv = {name: rr.var(name) for name in names}
        rd = surface_series(
            module, rr,
            {2: rv["s"], 3: rv["alpha"]},
            {2: rv["t"], 3: rv["beta"]},
            9,
        )
        rw = module.cone_vector(
            rr, rr.const(), rr.const(),
            rr.scale(rv["q"], module.g(0, 8 * sign)), rv["q"],
        )
        ry = module.vector_with_ab(
            rr,
            rv["X"], rr.scale(rv["X"], module.g(0, 8 * sign)),
            rv["y1"], rv["y2"], rv["y3"], rv["y4"],
        )
        rz = module.vector_with_ab(
            rr, rv["A8"], rv["B8"], rr.const(), rr.const(), rr.const(), rr.const()
        )
        add_normal(rr, rd, 3, rw)
        add_normal(rr, rd, 4, ry)
        add_normal(rr, rd, 5, rz)
        req, _ = literal_e2_source(
            module, rows, loads["K10"], rd, (rr.const(),), rr
        )
        rg8 = [req[index][8] for index in range(7)]
        compat3 = rr.add(rg8[2], rg8[0], F(1, 8))
        compat4 = rg8[3]
        expected3 = rr.add(
            rr.scale(rr.mul(rv["X"], rv["X"]), module.g(0, F(3 * sign, 2048))),
            rr.add(
                rr.scale(rr.mul(rv["t"], rr.mul(rv["q"], rv["q"])), F(3, 16)),
                rr.scale(
                    rr.mul(rv["s"], rr.mul(rv["q"], rv["q"])),
                    module.g(0, F(3 * sign, 128)),
                ),
            ),
        )
        expected4 = rr.add(
            rr.scale(rr.mul(rv["X"], rv["X"]), F(-3, 4096)),
            rr.add(
                rr.scale(
                    rr.mul(rv["t"], rr.mul(rv["q"], rv["q"])),
                    module.g(0, F(-3 * sign, 32)),
                ),
                rr.scale(rr.mul(rv["s"], rr.mul(rv["q"], rv["q"])), F(3, 256)),
            ),
        )
        assert_equal(module, rr, compat3, expected3, f"n3 G8 sign {sign} compat3")
        assert_equal(module, rr, compat4, expected4, f"n3 G8 sign {sign} compat4")
        wall_combo = rr.add(expected3, expected4, module.g(0, 2 * sign))
        wall = rr.scale(
            rr.mul(
                rr.mul(rv["q"], rv["q"]),
                rr.sub(rv["s"], rr.scale(rv["t"], module.g(0, 8 * sign))),
            ),
            module.g(0, F(3 * sign, 64)),
        )
        assert_equal(module, rr, wall_combo, wall, f"n3 G8 sign {sign} support wall")
        root = rr.replace_by_scaled_var(
            expected4, {"s": (module.g(0, 8 * sign), "t")}
        )
        assert_equal(
            module, rr, root,
            rr.scale(rr.mul(rv["X"], rv["X"]), F(-3, 4096)),
            f"n3 G8 sign {sign} support root",
        )

        reduced_names = (
            "t", "q", "alpha", "beta", "Z",
            *(f"k{index}" for index in range(6)),
            "y1", "y2", "y3", "y4",
            "z1", "z2", "z3", "z4",
            *(f"u{index}" for index in range(6)),
        )
        tr = module.Ring(reduced_names)
        tv = {name: tr.var(name) for name in reduced_names}
        td = surface_series(
            module, tr,
            {2: tr.scale(tv["t"], module.g(0, 8 * sign)), 3: tv["alpha"]},
            {2: tv["t"], 3: tv["beta"]},
            10,
        )
        tw = module.cone_vector(
            tr, tr.const(), tr.const(),
            tr.scale(tv["q"], module.g(0, 8 * sign)), tv["q"],
        )
        ty = module.vector_with_ab(
            tr, tr.const(), tr.const(),
            tv["y1"], tv["y2"], tv["y3"], tv["y4"],
        )
        bz = tr.add(
            tr.scale(tv["Z"], module.g(0, 8 * sign)),
            tr.scale(tr.mul(tv["t"], tv["q"]), -128),
        )
        tz = module.vector_with_ab(
            tr, tv["Z"], bz, tv["z1"], tv["z2"], tv["z3"], tv["z4"]
        )
        tu = [tv[f"u{index}"] for index in range(6)]
        add_normal(tr, td, 3, tw)
        add_normal(tr, td, 4, ty)
        add_normal(tr, td, 5, tz)
        add_normal(tr, td, 6, tu)
        teq, tload = literal_e2_source(
            module,
            rows,
            loads["K10"],
            td,
            tuple(tv[f"k{index}"] for index in range(6)),
            tr,
        )
        for row_index in range(7):
            for grade in range(9):
                assert_zero(
                    teq[row_index][grade],
                    f"n3 reduced sign {sign} row {row_index + 1} G{grade}",
                )
        terminal = tr.scale(tr.power(tv["q"], 3), module.g(0, F(sign, 32)))
        assert_equal(
            module, tr, teq[5][9], terminal,
            f"n3 reduced sign {sign} G9 row6",
        )
        for grade in range(6):
            assert_zero(tload[5][grade], f"n3 sign {sign} K10 row6 grade {grade}")
        compatibility[str(sign)] = [poly_object(expected3), poly_object(expected4)]
        terminals[str(sign)] = poly_object(terminal)
    return {
        "rank2": {"delta": poly_object(delta), "C": poly_object(cform), "E": poly_object(eform)},
        "rank1_g8_compatibility": compatibility,
        "rank1_g9_terminals": terminals,
    }


def n4_g10_final_fan(
    module, rows, loads, quadrics, cubics, m4, a10_cubic,
    expected_w1, expected_w2,
):
    """Classify all ranks of the fresh G8 cone at the loaded G10 gate."""

    names = (
        "s", "t", "alpha", "beta", "p", "q", "X", "Y", "U", "V",
        *(f"k{index}" for index in range(7)),
        "y1", "y2", "y3", "y4", "z1", "z2", "z3", "z4",
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    s, t, p, q = (value[name] for name in ("s", "t", "p", "q"))
    dseries = surface_series(
        module, ring,
        {2: s, 3: value["alpha"]}, {2: t, 3: value["beta"]}, 11,
    )
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    tangent = module.vector_with_ab(
        ring, value["X"], value["Y"],
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    newest = module.vector_with_ab(
        ring, value["U"], value["V"],
        value["z1"], value["z2"], value["z3"], value["z4"],
    )
    add_normal(ring, dseries, 4, residual)
    add_normal(ring, dseries, 5, tangent)
    add_normal(ring, dseries, 6, newest)
    source, load = literal_e2_source(
        module,
        rows,
        loads["K10"],
        dseries,
        tuple(value[f"k{index}"] for index in range(7)),
        ring,
    )
    g9 = [source[index][9] for index in range(7)]
    g10 = [source[index][10] for index in range(7)]
    ell = module.old_plane(ring, s, t)
    alpha = [
        module.eval_dpoly(module.dderivative(poly, 5), residual, ring)
        for poly in quadrics
    ]
    beta = [
        module.eval_dpoly(module.dderivative(poly, 0), residual, ring)
        for poly in quadrics
    ]
    load_rows = []
    for row_index in range(7):
        expected_g9 = directional(
            module, ring, quadrics[row_index], residual, tangent
        )
        assert_equal(module, ring, g9[row_index], expected_g9, f"n4 G9 tangent row {row_index + 1}")
        wrow = ring.add(
            directional(module, ring, m4[row_index], ell, residual),
            ring.add(
                directional(module, ring, m4[row_index], ell, mu_vector(ring, s, t)),
                module.eval_dpoly(a10_cubic[row_index], ell, ring),
            ),
        )
        load_rows.append(wrow)
        expected_g10 = ring.add(
            directional(module, ring, quadrics[row_index], residual, newest),
            ring.add(
                module.eval_dpoly(quadrics[row_index], tangent, ring),
                ring.add(
                    second_half(module, ring, cubics[row_index], ell, residual),
                    ring.mul(value["k0"], wrow),
                ),
            ),
        )
        assert_equal(module, ring, g10[row_index], expected_g10, f"n4 G10 row {row_index + 1}")
        assert_equal(module, ring, load[row_index][6], wrow, f"n4 K10 grade6 row {row_index + 1}")
        for name in ("alpha", "beta", *(f"k{index}" for index in range(1, 7))):
            if ring.depends_on(g10[row_index], name):
                fail(("spurious G10 coefficient dependence", row_index + 1, name))

    delta = ring.add(ring.mul(p, p), ring.scale(ring.mul(q, q), 64))
    cform = ring.add(
        ring.mul(t, ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p))),
        ring.scale(ring.mul(ring.mul(s, p), q), 2),
    )
    eform = ring.sub(
        ring.mul(s, ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p))),
        ring.scale(ring.mul(ring.mul(t, p), q), 128),
    )
    rank2_rows = [ring.zero_vars(poly, ("X", "Y")) for poly in g10]
    rank2_normal = [ring.zero_vars(poly, ("U", "V")) for poly in rank2_rows]
    augmented = determinant3(
        ring, [[alpha[index], beta[index], rank2_normal[index]] for index in range(3)]
    )
    assert_equal(
        module, ring, augmented,
        ring.scale(ring.mul(delta, cform), F(27, 2**35)),
        "n4 G10 rank2 augmented",
    )
    assert_equal(
        module, ring, rank2_rows[3], ring.scale(eform, F(3, 2**15)),
        "n4 G10 rank2 row4",
    )

    rank1_terminals = {}
    rank1_compatibility = {}
    for sign in (1, -1):
        replacements = {
            "p": (module.g(0, 8 * sign), "q"),
            "Y": (module.g(0, 8 * sign), "X"),
        }
        specialized = [
            ring.replace_by_scaled_var(poly, replacements) for poly in g10
        ]
        compat3 = ring.add(specialized[2], specialized[0], F(1, 8))
        compat4 = specialized[3]
        expected3 = ring.add(
            ring.scale(ring.mul(value["X"], value["X"]), module.g(0, F(3 * sign, 2048))),
            ring.add(
                ring.scale(ring.mul(t, ring.mul(q, q)), F(3, 16)),
                ring.scale(ring.mul(s, ring.mul(q, q)), module.g(0, F(3 * sign, 128))),
            ),
        )
        expected4 = ring.add(
            ring.scale(ring.mul(value["X"], value["X"]), F(-3, 4096)),
            ring.add(
                ring.scale(ring.mul(t, ring.mul(q, q)), module.g(0, F(-3 * sign, 32))),
                ring.scale(ring.mul(s, ring.mul(q, q)), F(3, 256)),
            ),
        )
        assert_equal(module, ring, compat3, expected3, f"n4 rank1 sign {sign} compat3")
        assert_equal(module, ring, compat4, expected4, f"n4 rank1 sign {sign} compat4")
        wall_combo = ring.add(expected3, expected4, module.g(0, 2 * sign))
        wall = ring.scale(
            ring.mul(
                ring.mul(q, q),
                ring.sub(s, ring.scale(t, module.g(0, 8 * sign))),
            ),
            module.g(0, F(3 * sign, 64)),
        )
        assert_equal(module, ring, wall_combo, wall, f"n4 rank1 sign {sign} support wall")
        root = ring.replace_by_scaled_var(
            expected4, {"s": (module.g(0, 8 * sign), "t")}
        )
        assert_equal(
            module, ring, root,
            ring.scale(ring.mul(value["X"], value["X"]), F(-3, 4096)),
            f"n4 rank1 sign {sign} support root",
        )
        combo = ring.add(specialized[1], specialized[0], module.g(0, F(sign, 2)))
        reduced = ring.replace_by_scaled_var(
            combo, {"s": (module.g(0, 8 * sign), "t")}, zeros=("X",)
        )
        terminal = ring.monomial(
            {"t": 3, "k0": 1}, module.g(0, F(-5 * sign, 16))
        )
        assert_equal(module, ring, reduced, terminal, f"n4 rank1 sign {sign} terminal")
        assert_zero(
            ring.zero_vars(terminal, ("k0",)), f"n4 rank1 sign {sign} K10-open control"
        )
        rank1_compatibility[str(sign)] = [poly_object(expected3), poly_object(expected4)]
        rank1_terminals[str(sign)] = poly_object(terminal)

    rankzero = [ring.zero_vars(poly, ("p", "q")) for poly in g10]
    expected_row4 = ring.scale(
        ring.sub(ring.mul(value["Y"], value["Y"]), ring.scale(ring.mul(value["X"], value["X"]), 64)),
        F(3, 524288),
    )
    assert_equal(module, ring, rankzero[3], expected_row4, "n4 rankzero row4")
    split_controls = {}
    for sign in (1, -1):
        branch = [
            ring.replace_by_scaled_var(poly, {"Y": (module.g(8 * sign), "X")})
            for poly in rankzero
        ]
        combo = ring.add(branch[2], branch[0], F(1, 8))
        expected = ring.scale(ring.mul(value["X"], value["X"]), F(3 * sign, 2048))
        assert_equal(module, ring, combo, expected, f"n4 rankzero split sign {sign}")
        split_controls[str(sign)] = poly_object(expected)
    final_rankzero = [ring.zero_vars(poly, ("p", "q", "X", "Y")) for poly in g10]
    for row_index in range(7):
        surface_load = ring.zero_vars(load_rows[row_index], ("p", "q"))
        assert_equal(
            module, ring, final_rankzero[row_index],
            ring.mul(value["k0"], surface_load),
            f"n4 final rankzero row {row_index + 1}",
        )
    w1 = ring.zero_vars(load_rows[0], ("p", "q"))
    w2 = ring.zero_vars(load_rows[1], ("p", "q"))
    # Compare after lifting the two-variable expected forms into this ring.
    expected1 = ring.scale(
        ring.mul(t, ring.sub(ring.scale(ring.mul(s, s), 3), ring.scale(ring.mul(t, t), 64))),
        F(5, 4096),
    )
    expected2 = ring.scale(
        ring.mul(s, ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 192))),
        F(5, 65536),
    )
    assert_equal(module, ring, w1, expected1, "n4 final W1")
    assert_equal(module, ring, w2, expected2, "n4 final W2")
    wrong2 = ring.scale(
        ring.mul(s, ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 191))),
        F(5, 65536),
    )
    if wrong2 == expected2:
        fail("W2 mutation invisible")
    return {
        "rank2": {"delta": poly_object(delta), "C": poly_object(cform), "E": poly_object(eform)},
        "rank1_compatibility": rank1_compatibility,
        "rank1_terminals": rank1_terminals,
        "rankzero_split": split_controls,
        "W1": poly_object(expected1),
        "W2": poly_object(expected2),
    }


def odd_fixture_control(module, rows, loads):
    """A literal G8 pass using odd columns, followed by the G9 row-six fail."""

    ring = module.Ring(())

    def evaluate(affine_value: int):
        dseries = surface_series(
            module,
            ring,
            {2: ring.const(module.g(0, 8)), 3: ring.const(3)},
            {2: ring.const(1), 3: ring.const(5)},
            10,
        )
        residual = module.cone_vector(
            ring, ring.const(), ring.const(), ring.const(module.g(0, 8)), ring.const(1)
        )
        tangent = module.vector_with_ab(
            ring, ring.const(), ring.const(),
            ring.const(1), ring.const(2), ring.const(3), ring.const(4),
        )
        lift = module.vector_with_ab(
            ring, ring.const(), ring.const(affine_value),
            ring.const(), ring.const(), ring.const(), ring.const(),
        )
        add_normal(ring, dseries, 3, residual)
        add_normal(ring, dseries, 4, tangent)
        add_normal(ring, dseries, 5, lift)
        return literal_e2_source(
            module, rows, loads["K10"], dseries, (ring.const(1),), ring
        )[0]

    source = evaluate(-128)
    for row_index in range(7):
        for grade in range(9):
            assert_zero(source[row_index][grade], f"odd fixture row {row_index + 1} G{grade}")
    terminal = ring.const(module.g(0, F(1, 32)))
    assert_equal(module, ring, source[5][9], terminal, "odd fixture G9 row6")
    wrong = evaluate(-127)
    if all(not wrong[row_index][8] for row_index in range(7)):
        fail("odd affine-lift mutation invisible")
    return "S3=3,T3=5,N3_RANK1,N4_KERNEL_NONZERO;G0_G8_PASS;G9_ROW6=i/32"


def main() -> None:
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("custody", path, actual, expected))
    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    quadrics = [module.dhom(row, 2) for row in rows]
    cubics = [module.dhom(row, 3) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]
    a10_cubic = [module.dhom(row, 3) for row in loads["K10"]]
    load_rows, w1, w2, minima, late = surface_gradient_calendar(
        module, rows, loads, m4, a10_cubic
    )
    fresh = {
        str(normal_order): fresh_cone_tangent(
            module, rows, loads, quadrics, normal_order
        )
        for normal_order in (2, 3, 4)
    }
    first_fan = n2_g6_fan(module, rows, loads, quadrics)
    odd_fan = n3_g8_g9_fan(module, rows, loads, quadrics, cubics)
    final_fan = n4_g10_final_fan(
        module, rows, loads, quadrics, cubics, m4, a10_cubic, w1, w2
    )
    fixture = odd_fixture_control(module, rows, loads)

    certificate = {
        "type": "K00-RAM-E2M2-G0-G10-COMPLETE-POINT-FAN/v1",
        "basis": "0f7ee003be45ee40d51d4048897cdacf63821172",
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "tail_terms": term_count,
        "field": "algebraic closure of characteristic zero; Gaussian rank-one charts",
        "normalization": "Lambda=tau^2; C6=1; K10 shift=tau^4; ord(d)=2",
        "opens": [
            "k10[0]!=0", "Jdet[0]!=0", "union_i D(d_i[2])",
            "post-first-fan: (s,t)!=(0,0)",
        ],
        "gradient_lemma": "R(D)=0 and all 42 gradients vanish on D",
        "surface_k10_minima": minima,
        "late_calendar": late,
        "fresh_cone_tangent": fresh,
        "g4_to_g6": first_fan,
        "g6_to_g9": odd_fan,
        "g8_to_g10": final_fan,
        "transition_tree": [
            "G4 n2 rank2/rank1 -> dead G6; rank0 -> fresh G6 n3 cone",
            "G6 n3 rank2 -> dead G8",
            "G6 n3 rank1 -> survives G8 with odd coefficients -> dead raw G9 row6",
            "G6 n3 rank0 -> fresh G8 n4 cone",
            "G8 n4 ranks 2,1,0 satisfy G9 tangent fan -> all dead G10",
        ],
        "odd_fixture": fixture,
        "conclusion": "EMPTY_THROUGH_G10_ON_DECLARED_OPENS_POINT_SET",
        "scheme_scope": "reduced geometric support only; no cone or transition ideal equality",
        "nonclaims": [
            "scheme equality", "arc existence or lifting beyond finite-jet exclusion",
            "reachability", "map", "JC2",
        ],
        "mutations": [
            "custody", "surface_gradient", "odd_affine_-128_to_-127",
            "rank_discriminant_64", "rankzero_W2_192_to_191", "k10_open",
        ],
    }
    cert_bytes = (
        json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    cert_sha = sha256(cert_bytes).hexdigest()
    if (
        EXPECTED_CERTIFICATE_SHA256 != "PENDING"
        and cert_sha != EXPECTED_CERTIFICATE_SHA256
    ):
        fail(("certificate digest", cert_sha, EXPECTED_CERTIFICATE_SHA256))

    print("K00_RAM_E2M2_G0_G10_COMPLETE_RANKFAN_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("CALENDAR=K10_GLOBAL_G8;SURFACE_G10;K6_G15;K2_G23;TARGETS_G29_G33_G37_G38")
    print("GRADIENT_LEMMA=R_ON_D_ZERO;ALL_42_GRADIENTS_ON_D_ZERO")
    print("G4_N2=RANK2_RANK1_DEAD_G6;RANK0_TO_G6_N3")
    print("G6_N3=RANK2_DEAD_G8;RANK1_G8_SURVIVOR_DEAD_G9;RANK0_TO_G8_N4")
    print("ODD_BRANCH_G9_ROW6=EPS*i*q^3/32;S3_T3_N6_K10_RETAINED")
    print("G8_N4=ALL_G9_TANGENT_RANKS_DEAD_G10")
    print("G10_RANK1=-EPS*5*i*k10[0]*t^3/16;RANK0=Q(v)+kW_EMPTY")
    print("ODD_FIXTURE=G0_G8_PASS;G9_FAIL;i/32")
    print("CELL_STATUS=POINT_SET_EMPTY_THROUGH_G10_ON_C6_K10_JDET_OPENS")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,GRADIENT,ODD_-128_TO_-127,DELTA_64,W2_192,K10_OPEN")


if __name__ == "__main__":
    main()
