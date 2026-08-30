#!/usr/bin/env python3
"""Exact stdlib replay of the complete e=3,m=1 G0--G9 point fan.

The replay reconstructs the literal 569-tail K00 source.  It imports only
the promoted set-theoretic G3 incidence theorem; every transition from the
leading plane through G9 is then extracted again from the literal rows.
All surface and normal coefficients capable of reaching G9 are retained.

The conclusion is point-set emptiness over an algebraic closure on the
declared C6/K10/Jdet opens.  Reduced cone parameterizations are not asserted
as scheme-theoretic equalities, and no arc, reachability, map, or JC2 claim
is made.
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
G3_PROMOTION = ROOT / "xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md"
G7_INTEGRATION = ROOT / "xmodel/k00-ram-e2m1-g7-rankfan-coordinator-integration-sol56-20260829.md"
UNIFORM_REPLAY = ROOT / "xmodel/k00-ram-m1-uniform-rankfan-replay-sol56-20260829.py"
UNIFORM_REVIEW = ROOT / "xmodel/k00-ram-e2m1-allfaces-uniformity-hostile-review-fable5-20260829.md"
G9_REPLAY = ROOT / "xmodel/k00-ram-e3m1-g9-rankone-kill-replay-sol56-20260829.py"
G9_REPORT = ROOT / "xmodel/k00-ram-e3m1-g9-rankone-kill-sol56-20260829.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    G3_PROMOTION: "d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860",
    G7_INTEGRATION: "0eb501b414f2162d14a73725a46410b7e799adc70932cdfb8a05f4196ff0bb1a",
    UNIFORM_REPLAY: "0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b",
    UNIFORM_REVIEW: "0ee84a0b98d30c4436461a09118961706d1f18fcfe9686684e7b1a27b5597feb",
    G9_REPLAY: "3ef20945b4a009bba4dccbbf7a43461718feb8155e84f513f14c736ce45182e2",
    G9_REPORT: "bbe6ac2fa8ca7b53634e3c477d1cb2f4128e4e22e2a1cf5d4049db82402fe685",
}
EXPECTED_CERTIFICATE_SHA256 = "96279f6994f3af485913d33d3f0a175c582b02da450a0b344fb82fc65f2129a0"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_e3m1_complete_engine", ENGINE)
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
    """Return D(S,T) for arbitrary supplied coefficients of S and T."""

    sseries = module.series_zero(truncation)
    tseries = module.series_zero(truncation)
    for grade, value in scoeff.items():
        sseries[grade] = value
    for grade, value in tcoeff.items():
        tseries[grade] = value
    one = module.series_zero(truncation)
    one[0] = ring.const(1)
    ssquare = module.series_mul(sseries, sseries, ring)
    tsquare = module.series_mul(tseries, tseries, ring)
    return [
        module.series_add(series_scale(module, ring, sseries, 2), ssquare, ring),
        series_scale(
            module,
            ring,
            module.series_mul(module.series_add(one, sseries, ring), tseries, ring),
            F(1, 8),
        ),
        module.series_add(sseries, series_scale(module, ring, tsquare, 16), ring),
        tseries,
        sseries,
        series_scale(module, ring, tseries, 2),
    ]


def add_normal(module, ring, dseries, grade: int, vector):
    for index in range(6):
        dseries[index][grade] = ring.add(dseries[index][grade], vector[index])


def literal_source(module, rows, k10_rows, dseries, kseries, ring):
    """R(d)+tau^6*k10(tau)*A10(d), at e=3."""

    total = [module.eval_dpoly_series(row, dseries, ring) for row in rows]
    load = [module.eval_dpoly_series(row, dseries, ring) for row in k10_rows]
    truncation = len(dseries[0])
    for row_index in range(7):
        for kgrade, kval in enumerate(kseries):
            if not kval:
                continue
            for dgrade in range(truncation - 6 - kgrade):
                if load[row_index][dgrade]:
                    total[row_index][6 + kgrade + dgrade] = ring.add(
                        total[row_index][6 + kgrade + dgrade],
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


def surface_and_calendar_check(module, rows, loads):
    ring = module.Ring(("S", "T"))
    s, t = ring.var("S"), ring.var("T")
    surface = [series[0] for series in surface_series(
        module, ring, {0: s}, {0: t}, 1
    )]
    for row_index, row in enumerate(rows):
        assert_zero(module.eval_dpoly(row, surface, ring), f"surface row {row_index + 1}")
    restrictions = [module.eval_dpoly(row, surface, ring) for row in loads["K10"]]
    minima = [min((sum(key) for key in poly), default=None) for poly in restrictions]
    if minima != [3, 3, 3, None, 3, 4, 3]:
        fail(("K10 surface minima", minima))
    late = {
        "K6": 6 * 3 + 1 + 1,
        "K2": 10 * 3 + 1 + 1,
        "mu2": 14 * 3 + 1,
        "mu4": 16 * 3 + 1,
        "mu6": 18 * 3 + 1,
        "Jdet": 19 * 3,
    }
    if any(grade <= 9 for grade in late.values()):
        fail(("late load reached G9", late))
    return minima, late


def fresh_cone_check(module, rows, loads, quadrics, normal_order: int):
    """After exact recentering, grade 2n is the literal fresh Q-cone."""

    names = ("s", "t", "k0", *(f"r{index}" for index in range(6)))
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    truncation = 2 * normal_order + 1
    dseries = surface_series(
        module, ring, {1: value["s"]}, {1: value["t"]}, truncation
    )
    residual = [value[f"r{index}"] for index in range(6)]
    add_normal(module, ring, dseries, normal_order, residual)
    source, _ = literal_source(
        module, rows, loads["K10"], dseries, (value["k0"],), ring
    )
    for row_index in range(7):
        for grade in range(2 * normal_order):
            assert_zero(
                source[row_index][grade],
                f"fresh n={normal_order} row {row_index + 1} G{grade}",
            )
        assert_equal(
            module,
            ring,
            source[row_index][2 * normal_order],
            module.eval_dpoly(quadrics[row_index], residual, ring),
            f"fresh n={normal_order} Q row {row_index + 1}",
        )
    return [poly_object(source[index][2 * normal_order]) for index in range(7)]


def stable_odd_fan(module, rows, loads, quadrics, cubics, normal_order: int):
    """Exact grade 2n+1 fan for n=2 and n=3, after plane absorption."""

    names = (
        "s", "t", "p", "q", "X", "Y",
        "y1", "y2", "y3", "y4", "k0",
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    s, t, p, q = (value[name] for name in ("s", "t", "p", "q"))
    truncation = 2 * normal_order + 2
    dseries = surface_series(module, ring, {1: s}, {1: t}, truncation)
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    newest = module.vector_with_ab(
        ring, value["X"], value["Y"],
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    add_normal(module, ring, dseries, normal_order, residual)
    add_normal(module, ring, dseries, normal_order + 1, newest)
    source, _ = literal_source(
        module, rows, loads["K10"], dseries, (value["k0"],), ring
    )
    odd_grade = 2 * normal_order + 1
    for row_index in range(7):
        for grade in range(odd_grade):
            assert_zero(
                source[row_index][grade],
                f"stable n={normal_order} row {row_index + 1} G{grade}",
            )
    ell = module.old_plane(ring, s, t)
    alpha = [
        module.eval_dpoly(module.dderivative(poly, 5), residual, ring)
        for poly in quadrics
    ]
    beta = [
        module.eval_dpoly(module.dderivative(poly, 0), residual, ring)
        for poly in quadrics
    ]
    normal = [second_half(module, ring, cubics[i], ell, residual) for i in range(7)]
    odd = [source[index][odd_grade] for index in range(7)]
    for row_index in range(7):
        expected = ring.add(
            ring.add(normal[row_index], ring.mul(alpha[row_index], value["X"])),
            ring.mul(beta[row_index], value["Y"]),
        )
        assert_equal(
            module, ring, odd[row_index], expected,
            f"stable n={normal_order} odd row {row_index + 1}",
        )
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
        f"stable n={normal_order} augmented determinant",
    )
    assert_equal(
        module, ring, odd[3], ring.scale(eform, F(3, 2**15)),
        f"stable n={normal_order} row4",
    )
    rank2_det = ring.sub(
        ring.mul(ring.scale(ring.mul(p, q), 2), ring.scale(ring.mul(p, q), -128)),
        ring.power(ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p)), 2),
    )
    assert_equal(
        module, ring, rank2_det, ring.scale(ring.mul(delta, delta), -1),
        f"stable n={normal_order} rank2 determinant",
    )
    wrong_delta = ring.add(ring.mul(p, p), ring.scale(ring.mul(q, q), 63))
    if rank2_det == ring.scale(ring.mul(wrong_delta, wrong_delta), -1):
        fail(("rank discriminant mutation invisible", normal_order))
    for sign in (1, -1):
        target_names = ("t", "q", "X", "y1", "y2", "y3", "y4", "k0")
        target = module.Ring(target_names)
        tv = {name: target.var(name) for name in target_names}
        images = {name: tv[name] for name in target_names}
        images.update({
            "s": target.scale(tv["t"], module.g(0, 8 * sign)),
            "p": target.scale(tv["q"], module.g(0, 8 * sign)),
            "Y": target.add(
                target.scale(tv["X"], module.g(0, 8 * sign)),
                target.scale(target.mul(tv["t"], tv["q"]), -128),
            ),
        })
        for row_index, poly in enumerate(odd):
            assert_zero(
                map_poly(module, ring, target, poly, images),
                f"stable n={normal_order} rank1 sign {sign} row {row_index + 1}",
            )
    for row_index, poly in enumerate(odd):
        assert_zero(
            ring.zero_vars(poly, ("p", "q")),
            f"stable n={normal_order} rankzero row {row_index + 1}",
        )
    return {
        "delta": poly_object(delta),
        "C": poly_object(cform),
        "E": poly_object(eform),
        "odd_rows": [poly_object(poly) for poly in odd],
    }


def order2_rankone_kill(module, rows, loads, sign: int):
    """The n=2 rank-one G5 survivor dies in unloaded row six at G6."""

    names = (
        "t", "q", "A", "B", "X", "k0",
        "y1", "y2", "y3", "y4", *(f"z{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    t, q = value["t"], value["q"]
    dseries = surface_series(
        module,
        ring,
        {1: ring.scale(t, module.g(0, 8 * sign)), 2: value["A"]},
        {1: t, 2: value["B"]},
        7,
    )
    residual = module.cone_vector(
        ring, ring.const(), ring.const(), ring.scale(q, module.g(0, 8 * sign)), q
    )
    bvalue = ring.add(
        ring.scale(value["X"], module.g(0, 8 * sign)),
        ring.scale(ring.mul(t, q), -128),
    )
    next_normal = module.vector_with_ab(
        ring, value["X"], bvalue,
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    add_normal(module, ring, dseries, 2, residual)
    add_normal(module, ring, dseries, 3, next_normal)
    add_normal(
        module, ring, dseries, 4, [value[f"z{index}"] for index in range(6)]
    )
    source, _ = literal_source(
        module, rows, loads["K10"], dseries, (value["k0"],), ring
    )
    for row_index in range(7):
        for grade in range(6):
            assert_zero(
                source[row_index][grade],
                f"n2 rank1 sign {sign} row {row_index + 1} G{grade}",
            )
    q3 = ring.power(q, 3)
    g6 = [source[index][6] for index in range(7)]
    combo5 = ring.add(ring.add(g6[4], g6[0], F(3, 128)), g6[2], F(1, 8))
    combo7 = ring.add(ring.add(g6[6], g6[0], F(1, 512)), g6[2], F(1, 128))
    assert_equal(module, ring, combo5, ring.scale(q3, F(-1, 16)), f"n2 sign {sign} G6 S5")
    terminal = ring.scale(q3, module.g(0, F(sign, 32)))
    assert_equal(module, ring, g6[5], terminal, f"n2 sign {sign} G6 row6")
    assert_equal(module, ring, combo7, ring.scale(q3, F(1, 128)), f"n2 sign {sign} G6 S7")
    return poly_object(terminal)


def order3_compatibility(module, rows, loads, sign: int):
    """Classify the reduced support of the complete n=3 rank-one G8 gate."""

    names = (
        "t", "q", "alpha", "beta", "X", "k0",
        "y1", "y2", "y3", "y4", *(f"z{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    t, q = value["t"], value["q"]
    dseries = surface_series(
        module,
        ring,
        {1: ring.scale(t, module.g(0, 8 * sign)), 2: value["alpha"]},
        {1: t, 2: value["beta"]},
        9,
    )
    residual = module.cone_vector(
        ring, ring.const(), ring.const(), ring.scale(q, module.g(0, 8 * sign)), q
    )
    bvalue = ring.add(
        ring.scale(value["X"], module.g(0, 8 * sign)),
        ring.scale(ring.mul(t, q), -128),
    )
    next_normal = module.vector_with_ab(
        ring, value["X"], bvalue,
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    add_normal(module, ring, dseries, 3, residual)
    add_normal(module, ring, dseries, 4, next_normal)
    add_normal(
        module, ring, dseries, 5, [value[f"z{index}"] for index in range(6)]
    )
    source, _ = literal_source(
        module, rows, loads["K10"], dseries, (value["k0"],), ring
    )
    for row_index in range(7):
        for grade in range(8):
            assert_zero(
                source[row_index][grade],
                f"n3 compat sign {sign} row {row_index + 1} G{grade}",
            )
    tq = ring.mul(t, q)
    q2 = ring.mul(q, q)
    common = ring.add(
        ring.mul(value["X"], value["X"]),
        ring.scale(ring.mul(tq, value["X"]), module.g(0, -48 * sign)),
    )
    form512 = ring.add(
        ring.add(common, ring.scale(ring.mul(tq, tq), -512)),
        ring.add(
            ring.scale(ring.mul(value["alpha"], q2), 16),
            ring.scale(ring.mul(value["beta"], q2), module.g(0, -128 * sign)),
        ),
    )
    form640 = ring.add(
        ring.add(common, ring.scale(ring.mul(tq, tq), -640)),
        ring.add(
            ring.scale(ring.mul(value["alpha"], q2), -16),
            ring.scale(ring.mul(value["beta"], q2), module.g(0, 128 * sign)),
        ),
    )
    compat3 = ring.add(source[2][8], source[0][8], F(1, 8))
    compat4 = source[3][8]
    assert_equal(
        module, ring, compat3,
        ring.scale(form512, module.g(0, F(3 * sign, 2048))),
        f"n3 compat sign {sign} form512",
    )
    assert_equal(
        module, ring, compat4, ring.scale(form640, F(-3, 4096)),
        f"n3 compat sign {sign} form640",
    )
    wall = ring.add(
        ring.add(ring.scale(ring.mul(t, t), 4), value["alpha"]),
        ring.scale(value["beta"], module.g(0, -8 * sign)),
    )
    double = ring.sub(
        value["X"], ring.scale(tq, module.g(0, 24 * sign))
    )
    assert_equal(
        module, ring, ring.sub(form512, form640),
        ring.scale(ring.mul(q2, wall), 32),
        f"n3 compat sign {sign} difference",
    )
    assert_equal(
        module, ring, ring.add(form512, form640),
        ring.scale(ring.mul(double, double), 2),
        f"n3 compat sign {sign} double root",
    )
    return {
        "F512": poly_object(form512),
        "F640": poly_object(form640),
        "support": [
            "X=epsilon*24*i*t*q",
            "alpha-epsilon*8*i*beta=-4*t^2",
        ],
        "localized_scheme_pair": "(wall,(X-epsilon*24*i*t*q)^2) on D(q)",
    }


def order3_reduced_kill(module, rows, loads, sign: int):
    """Retain every surface/normal coefficient capable of reaching G9."""

    names = (
        "t", "q", "beta", "gamma", "eta",
        "k0", "k1", "k2", "k3",
        "y1", "y2", "y3", "y4",
        *(f"z{index}" for index in range(6)),
        *(f"u{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    t, q, beta = value["t"], value["q"], value["beta"]
    alpha = ring.add(
        ring.scale(ring.mul(t, t), -4),
        ring.scale(beta, module.g(0, 8 * sign)),
    )
    dseries = surface_series(
        module,
        ring,
        {
            1: ring.scale(t, module.g(0, 8 * sign)),
            2: alpha,
            3: value["gamma"],
        },
        {1: t, 2: beta, 3: value["eta"]},
        10,
    )
    residual = module.cone_vector(
        ring, ring.const(), ring.const(), ring.scale(q, module.g(0, 8 * sign)), q
    )
    xvalue = ring.scale(ring.mul(t, q), module.g(0, 24 * sign))
    bvalue = ring.scale(ring.mul(t, q), -320)
    next_normal = module.vector_with_ab(
        ring, xvalue, bvalue,
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    add_normal(module, ring, dseries, 3, residual)
    add_normal(module, ring, dseries, 4, next_normal)
    add_normal(
        module, ring, dseries, 5, [value[f"z{index}"] for index in range(6)]
    )
    add_normal(
        module, ring, dseries, 6, [value[f"u{index}"] for index in range(6)]
    )
    source, load = literal_source(
        module,
        rows,
        loads["K10"],
        dseries,
        tuple(value[f"k{index}"] for index in range(4)),
        ring,
    )
    for row_index in range(7):
        for grade in range(8):
            assert_zero(
                source[row_index][grade],
                f"n3 reduced sign {sign} row {row_index + 1} G{grade}",
            )
    az = ring.linear(
        (1, value["z5"]), (16, value["z1"]), (-4, value["z3"])
    )
    bz = ring.linear(
        (1, value["z0"]), (-4, value["z2"]), (2, value["z4"])
    )
    hform = ring.add(bz, az, module.g(0, -8 * sign))
    hform = ring.add(hform, ring.scale(ring.mul(q, beta), 128))
    hform = ring.add(
        hform,
        ring.scale(ring.mul(ring.mul(t, t), q), module.g(0, 1088 * sign)),
    )
    hform = ring.add(hform, ring.scale(ring.mul(t, value["y1"]), -512))
    hform = ring.add(
        hform, ring.scale(ring.mul(t, value["y2"]), module.g(0, -8 * sign))
    )
    hform = ring.add(hform, ring.scale(ring.mul(t, value["y3"]), 64))
    hform = ring.add(
        hform, ring.scale(ring.mul(t, value["y4"]), module.g(0, 8 * sign))
    )
    z0_key = [0] * ring.n
    z0_key[ring.index["z0"]] = 1
    if hform.get(tuple(z0_key), module.g()) != module.g(1):
        fail(("G8 lift form not monic in z0", sign))
    qh = ring.mul(q, hform)
    expected_g8 = (
        ring.scale(qh, F(-3, 1024)),
        ring.scale(qh, module.g(0, F(3 * sign, 2048))),
        ring.scale(qh, F(3, 8192)),
        ring.const(),
        ring.scale(qh, F(3, 131072)),
        ring.const(),
        ring.scale(qh, F(3, 1048576)),
    )
    for row_index in range(7):
        assert_equal(
            module, ring, source[row_index][8], expected_g8[row_index],
            f"n3 reduced sign {sign} G8 row {row_index + 1}",
        )
    terminal = ring.scale(ring.power(q, 3), module.g(0, F(sign, 32)))
    assert_equal(
        module, ring, source[5][9], terminal,
        f"n3 reduced sign {sign} G9 row6 with S3,T3,N6",
    )
    for name in ("beta", "gamma", "eta", *(f"k{index}" for index in range(4))):
        if ring.depends_on(source[5][9], name):
            fail(("spurious G9 row6 dependence", sign, name))
    for grade in range(4):
        assert_zero(load[5][grade], f"n3 sign {sign} K10 row6 coefficient {grade}")
    return {
        "H": poly_object(hform),
        "terminal": poly_object(terminal),
        "retained": "S2,T2,S3,T3,N4,N5,N6,k10[0..3]",
    }


def fresh_order4_g9_fan(module, rows, loads, quadrics, cubics, m4, a10_cubic):
    """Complete G9 fan after the n=3 rank-zero recentering."""

    names = (
        "s", "t", "A", "B", "C", "D", "p", "q", "X", "Y",
        "k0", "k1", "k2", "k3",
        "y1", "y2", "y3", "y4", *(f"z{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    s, t, p, q = (value[name] for name in ("s", "t", "p", "q"))
    dseries = surface_series(
        module,
        ring,
        {1: s, 2: value["A"], 3: value["C"]},
        {1: t, 2: value["B"], 3: value["D"]},
        10,
    )
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    newest = module.vector_with_ab(
        ring, value["X"], value["Y"],
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    add_normal(module, ring, dseries, 4, residual)
    add_normal(module, ring, dseries, 5, newest)
    add_normal(
        module, ring, dseries, 6, [value[f"z{index}"] for index in range(6)]
    )
    source, load = literal_source(
        module,
        rows,
        loads["K10"],
        dseries,
        tuple(value[f"k{index}"] for index in range(4)),
        ring,
    )
    for row_index in range(7):
        for grade in range(9):
            assert_zero(
                source[row_index][grade],
                f"fresh n4 row {row_index + 1} G{grade}",
            )
    ell = module.old_plane(ring, s, t)
    mu = mu_vector(ring, s, t)
    alpha = [
        module.eval_dpoly(module.dderivative(poly, 5), residual, ring)
        for poly in quadrics
    ]
    beta = [
        module.eval_dpoly(module.dderivative(poly, 0), residual, ring)
        for poly in quadrics
    ]
    normal = [second_half(module, ring, cubics[index], ell, residual) for index in range(7)]
    load_rows = [
        ring.add(
            directional(module, ring, m4[index], ell, mu),
            module.eval_dpoly(a10_cubic[index], ell, ring),
        )
        for index in range(7)
    ]
    g9 = [source[index][9] for index in range(7)]
    for row_index in range(7):
        expected = ring.add(
            ring.add(
                ring.add(normal[row_index], ring.mul(alpha[row_index], value["X"])),
                ring.mul(beta[row_index], value["Y"]),
            ),
            ring.mul(value["k0"], load_rows[row_index]),
        )
        assert_equal(module, ring, g9[row_index], expected, f"fresh n4 G9 row {row_index + 1}")
        assert_equal(
            module, ring, load[row_index][3], load_rows[row_index],
            f"fresh n4 K10 cubic row {row_index + 1}",
        )
        for name in (
            "A", "B", "C", "D", "k1", "k2", "k3",
            *(f"z{index}" for index in range(6)),
        ):
            if ring.depends_on(g9[row_index], name):
                fail(("fresh G9 spurious later dependence", row_index + 1, name))
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
        ring,
        [[
            alpha[index], beta[index],
            ring.add(normal[index], ring.mul(value["k0"], load_rows[index])),
        ] for index in range(3)],
    )
    assert_equal(
        module, ring, augmented,
        ring.scale(ring.mul(delta, cform), F(27, 2**35)),
        "fresh n4 rank2 augmented determinant",
    )
    assert_equal(
        module, ring, g9[3], ring.scale(eform, F(3, 2**15)),
        "fresh n4 row4",
    )
    rank1_terminals = {}
    for sign in (1, -1):
        combo = ring.add(g9[1], g9[0], module.g(0, F(sign, 2)))
        specialized = ring.replace_by_scaled_var(
            combo,
            {
                "p": (module.g(0, 8 * sign), "q"),
                "s": (module.g(0, 8 * sign), "t"),
            },
        )
        terminal = ring.monomial(
            {"t": 3, "k0": 1}, module.g(0, F(-5 * sign, 16))
        )
        assert_equal(module, ring, specialized, terminal, f"fresh n4 rank1 sign {sign}")
        if not terminal:
            fail(("vacuous K10 terminal", sign))
        assert_zero(
            ring.zero_vars(terminal, ("k0",)),
            f"fresh n4 rank1 sign {sign} K10-open control",
        )
        rank1_terminals[str(sign)] = poly_object(terminal)
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
    assert_equal(module, ring, load_rows[0], expected_w1, "fresh n4 rankzero W1")
    assert_equal(module, ring, load_rows[1], expected_w2, "fresh n4 rankzero W2")
    for row_index in range(7):
        rankzero = ring.zero_vars(g9[row_index], ("p", "q"))
        assert_equal(
            module, ring, rankzero, ring.mul(value["k0"], load_rows[row_index]),
            f"fresh n4 rankzero row {row_index + 1}",
        )
    wrong_w2 = ring.scale(
        ring.mul(s, ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 191))),
        F(5, 65536),
    )
    if wrong_w2 == expected_w2:
        fail("fresh rankzero cubic mutation invisible")
    return {
        "delta": poly_object(delta),
        "C": poly_object(cform),
        "E": poly_object(eform),
        "W1": poly_object(expected_w1),
        "W2": poly_object(expected_w2),
        "rank1_terminals": rank1_terminals,
        "g9_rows": [poly_object(poly) for poly in g9],
    }


def old_fixture_control(module, rows, loads):
    """Mandatory old pass through G8 and fail at G9, plus -4 -> -3."""

    ring = module.Ring(())

    def evaluate(second_s: int):
        dseries = surface_series(
            module,
            ring,
            {1: ring.const(module.g(0, 8)), 2: ring.const(second_s)},
            {1: ring.const(1)},
            10,
        )
        add_normal(
            module,
            ring,
            dseries,
            3,
            [ring.const(value) for value in (
                module.g(0, 16), 0, 0, 1, module.g(0, -8), 4
            )],
        )
        add_normal(
            module,
            ring,
            dseries,
            4,
            [ring.const(value) for value in (-320, 0, 0, 0, 0, module.g(0, 24))],
        )
        add_normal(
            module,
            ring,
            dseries,
            5,
            [ring.const(value) for value in (module.g(0, -1088), 0, 0, 0, 0, 0)],
        )
        return literal_source(
            module, rows, loads["K10"], dseries, (ring.const(1),), ring
        )[0]

    old = evaluate(-4)
    for row_index in range(7):
        for grade in range(9):
            assert_zero(old[row_index][grade], f"old fixture row {row_index + 1} G{grade}")
    expected = ring.const(module.g(0, F(1, 32)))
    assert_equal(module, ring, old[5][9], expected, "old fixture G9 row6")
    wrong = evaluate(-3)
    if all(not wrong[row_index][8] for row_index in range(7)):
        fail("old fixture -4 to -3 mutation invisible")
    return "G0..G8_PASS;G9_ROW6=i/32;SECOND_SURFACE_-3_FAILS_G8"


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
    surface_minima, late_calendar = surface_and_calendar_check(module, rows, loads)
    fresh = {
        str(normal_order): fresh_cone_check(
            module, rows, loads, quadrics, normal_order
        )
        for normal_order in (2, 3, 4)
    }
    stable = {
        str(normal_order): stable_odd_fan(
            module, rows, loads, quadrics, cubics, normal_order
        )
        for normal_order in (2, 3)
    }
    n2_terminals = {
        str(sign): order2_rankone_kill(module, rows, loads, sign)
        for sign in (1, -1)
    }
    n3_compatibility = {}
    n3_reduced = {}
    for sign in (1, -1):
        n3_compatibility[str(sign)] = order3_compatibility(
            module, rows, loads, sign
        )
        n3_reduced[str(sign)] = order3_reduced_kill(
            module, rows, loads, sign
        )
    final_fan = fresh_order4_g9_fan(
        module, rows, loads, quadrics, cubics, m4, a10_cubic
    )
    old_fixture = old_fixture_control(module, rows, loads)

    certificate = {
        "type": "K00-RAM-E3M1-G0-G9-COMPLETE-POINT-FAN/v1",
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "basis": "0f7ee003be45ee40d51d4048897cdacf63821172",
        "tail_terms": term_count,
        "field": "algebraic closure of characteristic zero; Q(i) charts",
        "normalization": "Lambda=tau^3; C6=1; K10 shift=tau^6",
        "opens": ["k10[0]!=0", "Jdet[0]!=0", "(s,t)!=(0,0)"],
        "g0_g3": "promoted set-theoretic incidence: leading coefficient ell(s,t)",
        "g0_g8_lifecycle": "Fable different-model CONFIRM_WITH_CORRECTIONS",
        "surface_k10_minima": surface_minima,
        "late_calendar": late_calendar,
        "fresh_cones": fresh,
        "stable_odd_fans": stable,
        "n2_rankone_g6_terminals": n2_terminals,
        "n3_rankone_g8_compatibility": n3_compatibility,
        "n3_rankone_g9_kills": n3_reduced,
        "n4_g9_final_fan": final_fan,
        "transition_tree": [
            "G4 n2 rank2 -> dead G5",
            "G4 n2 rank1 -> survives G5 -> dead G6",
            "G4 n2 rank0 -> recenter -> fresh G6 n3 cone",
            "G6 n3 rank2 -> dead G7",
            "G6 n3 rank1 -> survives G7; unique reduced G8 support per sign -> dead G9",
            "G6 n3 rank0 -> recenter -> fresh G8 n4 cone",
            "G8 n4 ranks 2,1,0 -> all dead G9",
        ],
        "old_fixture": old_fixture,
        "conclusion": "EMPTY_THROUGH_G9_ON_DECLARED_OPENS_POINT_SET",
        "scheme_scope": "cone and G8 component parameterizations used only on reduced geometric support",
        "nonclaims": ["scheme equality", "formal arc", "reachability", "map", "JC2"],
        "mutations": [
            "custody", "old_fixture_pass_fail", "surface_-4_to_-3",
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

    print("K00_RAM_E3M1_G0_G9_COMPLETE_RANKFAN_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("G0_G3=IMPORTED_PROMOTED_SET_THEORETIC_LEADING_PLANE")
    print("G0_G8_PREMISE=DIFFERENT_MODEL_CONFIRMED_WITH_DOCUMENTATION_CORRECTIONS")
    print("N2=RANK2_DEAD_G5;RANK1_DEAD_G6;RANK0_TO_N3")
    print("N3=RANK2_DEAD_G7;RANK1_G8_COMPONENTS_DEAD_G9;RANK0_TO_N4")
    print("N3_G9_ROW6=EPS*i*q^3/32;S3_T3_N6_RETAINED")
    print("N4=FRESH_G8_CONE;RANK2_RANK1_RANK0_ALL_DEAD_G9")
    print("OLD_FIXTURE=G0_G8_PASS;G9_FAIL;i/32")
    print("CELL_STATUS=POINT_SET_EMPTY_THROUGH_G9_ON_C6_K10_JDET_OPENS")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,OLD_PASS_FAIL,SURFACE_-4_TO_-3,DELTA_64,W2_192,K10_OPEN")


if __name__ == "__main__":
    main()
