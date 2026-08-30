#!/usr/bin/env python3
"""Exact stdlib replay of the generic-K00 e=3,m=2 fan through G12.

The program reconstructs the literal 569-tail source.  It keeps every
surface, normal, and K10 coefficient capable of reaching G12 and classifies
the reduced field-valued transition fan.  No CAS is used.  Cone charts are
used only on reduced geometric support; no arc, attainment, map, or JC2
claim is made.
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
E3M1_REPORT = ROOT / "xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-sol56-20260829.md"
E3M1_REPLAY = ROOT / "xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-replay-sol56-20260829.py"
E3M1_REVIEW = ROOT / "xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-hostile-review-opus5-20260829.md"
E3M1_INTEGRATION = ROOT / "xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-coordinator-integration-sol56-20260830.md"
E2M2_REPORT = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-sol56-20260829.md"
E2M2_REPLAY = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-replay-sol56-20260829.py"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    E3M1_REPORT: "22e9752761f3bb4ee94b4dccf18cb72ff49bd0d92453ad4cf39eb401cc45f84a",
    E3M1_REPLAY: "bcd4004e671091c7d1ffc265affbd160b1d2b2a712f62dd97b698150dfc9fcba",
    E3M1_REVIEW: "0f7c18eb06dc2451fd4db668de7682a5d59f1c734509402b2537790b0408db87",
    E3M1_INTEGRATION: "6c7195218dcdac680d260d2db3e7bcff197a2ba7ee09055a8e6f67884ce27a38",
    E2M2_REPORT: "fa5a4ef6a1b2c0640c6363b84e6b547a044920b15249f7c72b25ffbcda2c1733",
    E2M2_REPLAY: "efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749",
}
EXPECTED_CERTIFICATE_SHA256 = "6ae3c1d9c7a51add533f08fcc4a23ea791a7cac9724add25d785380046007c70"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_e3m2_engine", ENGINE)
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
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_object(poly):
    return [
        [list(key), qstring(real), qstring(imag)]
        for key, (real, imag) in sorted(poly.items())
    ]


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


def add_normal(ring, dseries, grade: int, vector) -> None:
    for index in range(6):
        dseries[index][grade] = ring.add(dseries[index][grade], vector[index])


def literal_e3_source(module, rows, k10_rows, dseries, kseries, ring):
    """R(d)+tau^6*k10(tau)*A10(d), through the supplied truncation."""

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
    out = {}
    for key, coefficient in poly.items():
        tdegree, rdegree = key
        factor = module.g(square_value ** (rdegree // 2))
        new_key = (tdegree, rdegree % 2)
        out[new_key] = module.gadd(
            out.get(new_key, module.g()), module.gmul(coefficient, factor)
        )
    return ring.clean(out)


def common_forms(module, ring, p, q, s, t):
    delta = ring.add(ring.mul(p, p), ring.scale(ring.mul(q, q), 64))
    cform = ring.add(
        ring.mul(t, ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p))),
        ring.scale(ring.mul(ring.mul(s, p), q), 2),
    )
    eform = ring.sub(
        ring.mul(s, ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p))),
        ring.scale(ring.mul(ring.mul(t, p), q), 128),
    )
    return delta, cform, eform


def assert_rank2_compatibility(
    module, ring, rows_at_grade, quadrics, residual, tangent_names, p, q, s, t, label
):
    alpha = [
        module.eval_dpoly(module.dderivative(poly, 5), residual, ring)
        for poly in quadrics
    ]
    beta = [
        module.eval_dpoly(module.dderivative(poly, 0), residual, ring)
        for poly in quadrics
    ]
    rank2_rows = [ring.zero_vars(poly, tangent_names) for poly in rows_at_grade]
    normal = [ring.zero_vars(poly, ("U", "V")) for poly in rank2_rows]
    augmented = determinant3(
        ring, [[alpha[index], beta[index], normal[index]] for index in range(3)]
    )
    delta, cform, eform = common_forms(module, ring, p, q, s, t)
    assert_equal(
        module, ring, augmented,
        ring.scale(ring.mul(delta, cform), F(27, 2**35)),
        f"{label} augmented",
    )
    assert_equal(
        module, ring, rank2_rows[3], ring.scale(eform, F(3, 2**15)),
        f"{label} row4",
    )
    determinant = ring.sub(
        ring.mul(ring.scale(ring.mul(p, q), 2), ring.scale(ring.mul(p, q), -128)),
        ring.power(ring.sub(ring.scale(ring.mul(q, q), 64), ring.mul(p, p)), 2),
    )
    assert_equal(
        module, ring, determinant, ring.scale(ring.mul(delta, delta), -1),
        f"{label} C/E determinant",
    )
    return delta, cform, eform


def surface_calendar(module, rows, loads):
    ring = module.Ring(("s", "t", "alpha", "beta"))
    x = {name: ring.var(name) for name in ring.names}
    surface0 = [
        series[0]
        for series in surface_series(module, ring, {0: x["s"]}, {0: x["t"]}, 1)
    ]
    for row_index, row in enumerate(rows):
        assert_zero(module.eval_dpoly(row, surface0, ring), f"surface row {row_index + 1}")
        for coordinate in range(6):
            assert_zero(
                module.eval_dpoly(module.dderivative(row, coordinate), surface0, ring),
                f"gradient row {row_index + 1} coordinate {coordinate}",
            )
    restrictions = [module.eval_dpoly(row, surface0, ring) for row in loads["K10"]]
    minima = [min((sum(key) for key in poly), default=None) for poly in restrictions]
    if minima != [3, 3, 3, None, 3, 4, 3]:
        fail(("K10 surface minima", minima))

    series = surface_series(
        module,
        ring,
        {2: x["s"], 3: x["alpha"]},
        {2: x["t"], 3: x["beta"]},
        7,
    )
    raw = [module.eval_dpoly_series(row, series, ring) for row in loads["K10"]]
    for row_index in range(7):
        for grade in range(6):
            assert_zero(raw[row_index][grade], f"K10 exact-surface row {row_index + 1} G{grade}")
    w1 = ring.scale(
        ring.mul(
            x["t"],
            ring.sub(ring.scale(ring.mul(x["s"], x["s"]), 3), ring.scale(ring.mul(x["t"], x["t"]), 64)),
        ),
        F(5, 4096),
    )
    w2 = ring.scale(
        ring.mul(
            x["s"],
            ring.sub(ring.mul(x["s"], x["s"]), ring.scale(ring.mul(x["t"], x["t"]), 192)),
        ),
        F(5, 65536),
    )
    assert_equal(module, ring, raw[0][6], w1, "surface K10 W1")
    assert_equal(module, ring, raw[1][6], w2, "surface K10 W2")
    for row_index in range(7):
        if ring.depends_on(raw[row_index][6], "alpha") or ring.depends_on(raw[row_index][6], "beta"):
            fail(("spurious K10 G12 odd surface dependence", row_index + 1))

    load_minima = {
        label: [min((sum(key) for key in row), default=None) for row in sector]
        for label, sector in loads.items()
    }
    if load_minima["K6"] != [1, 1, 1, 2, 1, 2, 1]:
        fail(("K6 degree minima", load_minima["K6"]))
    if load_minima["K2"] != [1] * 7:
        fail(("K2 degree minima", load_minima["K2"]))
    late = {
        "K6_rows_1_2_3_5_7": 18 + 1 + 2,
        "K6_rows_4_6": 18 + 1 + 4,
        "K2": 30 + 1 + 2,
        "mu2": 42 + 1,
        "mu4": 48 + 1,
        "mu6": 54 + 1,
        "Jdet": 57,
    }
    if any(grade <= 12 for grade in late.values()):
        fail(("late sector reached G12", late))
    return minima, late, w1, w2


def fresh_cone_tangent(module, rows, loads, quadrics, normal_order: int):
    names = (
        "s", "t", "alpha", "beta", "k0", "k1",
        *(f"r{index}" for index in range(6)),
        *(f"v{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    truncation = 2 * normal_order + 2
    dseries = surface_series(
        module, ring,
        {2: x["s"], 3: x["alpha"]}, {2: x["t"], 3: x["beta"]},
        truncation,
    )
    residual = [x[f"r{index}"] for index in range(6)]
    tangent = [x[f"v{index}"] for index in range(6)]
    add_normal(ring, dseries, normal_order, residual)
    add_normal(ring, dseries, normal_order + 1, tangent)
    source, _ = literal_e3_source(
        module, rows, loads["K10"], dseries, (x["k0"], x["k1"]), ring
    )
    for row_index in range(7):
        for grade in range(2 * normal_order):
            assert_zero(source[row_index][grade], f"fresh n={normal_order} row {row_index + 1} G{grade}")
        qvalue = module.eval_dpoly(quadrics[row_index], residual, ring)
        tangent_value = directional(module, ring, quadrics[row_index], residual, tangent)
        assert_equal(module, ring, source[row_index][2 * normal_order], qvalue, f"fresh n={normal_order} cone row {row_index + 1}")
        assert_equal(module, ring, source[row_index][2 * normal_order + 1], tangent_value, f"fresh n={normal_order} tangent row {row_index + 1}")
    return f"G{2 * normal_order}=Q(N{normal_order});G{2 * normal_order + 1}=DQ(N{normal_order})N{normal_order + 1}"


def n2_fan(module, rows, loads):
    names = ("s", "t", "p", "q", "U", "V", "y1", "y2", "y3", "y4")
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    p, q, s, t = (x[name] for name in ("p", "q", "s", "t"))
    dseries = surface_series(module, ring, {2: s}, {2: t}, 7)
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    tangent = module.vector_with_ab(
        ring, ring.const(), ring.const(), x["y1"], x["y2"], x["y3"], x["y4"]
    )
    newest = module.vector_with_ab(
        ring, x["U"], x["V"], ring.const(), ring.const(), ring.const(), ring.const()
    )
    for grade, vector in ((2, residual), (3, tangent), (4, newest)):
        add_normal(ring, dseries, grade, vector)
    source, _ = literal_e3_source(module, rows, loads["K10"], dseries, (ring.const(),), ring)
    g6 = [source[index][6] for index in range(7)]
    row6 = ring.scale(
        ring.mul(p, ring.sub(ring.scale(ring.mul(q, q), 192), ring.mul(p, p))),
        F(1, 65536),
    )
    assert_equal(module, ring, g6[5], row6, "n2 rank2 row6 split")
    pzero_row4 = ring.zero_vars(g6[3], ("p",))
    assert_equal(module, ring, pzero_row4, ring.scale(ring.mul(s, ring.mul(q, q)), F(3, 512)), "n2 rank2 p=0 row4")
    combo3 = ring.add(g6[2], g6[0], F(1, 8))
    combo5 = ring.add(g6[4], g6[0], F(1, 128))
    expected3 = ring.scale(ring.mul(ring.mul(q, q), ring.add(q, ring.scale(t, F(3, 8)))), F(1, 4))
    expected5 = ring.scale(ring.mul(ring.mul(q, q), ring.add(q, ring.scale(t, F(1, 4)))), F(-3, 64))
    assert_equal(module, ring, ring.zero_vars(combo3, ("p", "s")), expected3, "n2 rank2 p=0 combo3")
    assert_equal(module, ring, ring.zero_vars(combo5, ("p", "s")), expected5, "n2 rank2 p=0 combo5")

    combo_r5 = ring.add(ring.add(g6[4], g6[0], F(3, 128)), g6[2], F(1, 8))
    combo_r7 = ring.add(ring.add(g6[6], g6[0], F(1, 512)), g6[2], F(1, 128))
    target = module.Ring(("t", "r"))
    tv = {name: target.var(name) for name in target.names}
    images = {
        "s": target.scale(target.mul(tv["r"], target.add(tv["t"], target.const(2))), -1),
        "t": tv["t"], "p": tv["r"], "q": target.const(1),
        "U": target.const(), "V": target.const(),
        "y1": target.const(), "y2": target.const(), "y3": target.const(), "y4": target.const(),
    }
    reduced5 = reduce_r_square(module, target, map_poly(module, ring, target, combo_r5, images), 192)
    reduced7 = reduce_r_square(module, target, map_poly(module, ring, target, combo_r7, images), 192)
    assert_equal(module, target, reduced5, target.const(F(1, 8)), "n2 rank2 p2=192 combo5")
    assert_equal(module, target, reduced7, target.const(F(-1, 64)), "n2 rank2 p2=192 combo7")

    terminals = {}
    for sign in (1, -1):
        specialized = ring.replace_by_scaled_var(g6[5], {"p": (module.g(0, 8 * sign), "q")})
        terminal = ring.monomial({"q": 3}, module.g(0, F(sign, 32)))
        assert_equal(module, ring, specialized, terminal, f"n2 rank1 sign {sign} terminal")
        terminals[str(sign)] = poly_object(terminal)
    return {"rank2_row6": poly_object(row6), "rank1_terminals": terminals}


def n3_fan(module, rows, loads, quadrics):
    names = (
        "s", "t", "alpha", "beta", "p", "q", "X", "Y", "U", "V",
        "y1", "y2", "y3", "y4",
    )
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    s, t, p, q = (x[name] for name in ("s", "t", "p", "q"))
    dseries = surface_series(module, ring, {2: s, 3: x["alpha"]}, {2: t, 3: x["beta"]}, 9)
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    tangent = module.vector_with_ab(
        ring, x["X"], x["Y"], x["y1"], x["y2"], x["y3"], x["y4"]
    )
    newest = module.vector_with_ab(ring, x["U"], x["V"], ring.const(), ring.const(), ring.const(), ring.const())
    for grade, vector in ((3, residual), (4, tangent), (5, newest)):
        add_normal(ring, dseries, grade, vector)
    source, _ = literal_e3_source(module, rows, loads["K10"], dseries, (ring.const(),), ring)
    g8 = [source[index][8] for index in range(7)]
    delta, cform, eform = assert_rank2_compatibility(
        module, ring, g8, quadrics, residual, ("X", "Y"), p, q, s, t, "n3 G8 rank2"
    )

    compatibility = {}
    terminals = {}
    for sign in (1, -1):
        replacements = {
            "p": (module.g(0, 8 * sign), "q"),
            "Y": (module.g(0, 8 * sign), "X"),
        }
        specialized = [ring.replace_by_scaled_var(poly, replacements) for poly in g8]
        combo3 = ring.add(specialized[2], specialized[0], F(1, 8))
        combo4 = specialized[3]
        expected3 = ring.add(
            ring.scale(ring.mul(x["X"], x["X"]), module.g(0, F(3 * sign, 2048))),
            ring.add(
                ring.scale(ring.mul(t, ring.mul(q, q)), F(3, 16)),
                ring.scale(ring.mul(s, ring.mul(q, q)), module.g(0, F(3 * sign, 128))),
            ),
        )
        expected4 = ring.add(
            ring.scale(ring.mul(x["X"], x["X"]), F(-3, 4096)),
            ring.add(
                ring.scale(ring.mul(t, ring.mul(q, q)), module.g(0, F(-3 * sign, 32))),
                ring.scale(ring.mul(s, ring.mul(q, q)), F(3, 256)),
            ),
        )
        assert_equal(module, ring, combo3, expected3, f"n3 G8 sign {sign} combo3")
        assert_equal(module, ring, combo4, expected4, f"n3 G8 sign {sign} combo4")
        compatibility[str(sign)] = [poly_object(expected3), poly_object(expected4)]

        rr_names = (
            "t", "q", "alpha", "beta", "Z",
            "y1", "y2", "y3", "y4", "z1", "z2", "z3", "z4",
            *(f"u{index}" for index in range(6)), "k0", "k1", "k2",
        )
        rr = module.Ring(rr_names)
        rv = {name: rr.var(name) for name in rr_names}
        rd = surface_series(
            module, rr,
            {2: rr.scale(rv["t"], module.g(0, 8 * sign)), 3: rv["alpha"]},
            {2: rv["t"], 3: rv["beta"]},
            10,
        )
        rw = module.cone_vector(rr, rr.const(), rr.const(), rr.scale(rv["q"], module.g(0, 8 * sign)), rv["q"])
        ry = module.vector_with_ab(rr, rr.const(), rr.const(), rv["y1"], rv["y2"], rv["y3"], rv["y4"])
        rz = module.vector_with_ab(
            rr,
            rv["Z"],
            rr.add(rr.scale(rv["Z"], module.g(0, 8 * sign)), rr.scale(rr.mul(rv["t"], rv["q"]), -128)),
            rv["z1"], rv["z2"], rv["z3"], rv["z4"],
        )
        ru = [rv[f"u{index}"] for index in range(6)]
        for grade, vector in ((3, rw), (4, ry), (5, rz), (6, ru)):
            add_normal(rr, rd, grade, vector)
        req, load = literal_e3_source(
            module, rows, loads["K10"], rd, (rv["k0"], rv["k1"], rv["k2"]), rr
        )
        for row_index in range(7):
            for grade in range(9):
                assert_zero(req[row_index][grade], f"n3 sign {sign} row {row_index + 1} G{grade}")
        terminal = rr.scale(rr.power(rv["q"], 3), module.g(0, F(sign, 32)))
        assert_equal(module, rr, req[5][9], terminal, f"n3 sign {sign} G9 row6")
        for grade in range(4):
            assert_zero(load[5][grade], f"n3 sign {sign} K10 row6 raw G{grade}")
        terminals[str(sign)] = poly_object(terminal)
    return {
        "rank2": {"delta": poly_object(delta), "C": poly_object(cform), "E": poly_object(eform)},
        "rank1_compatibility": compatibility,
        "rank1_terminals": terminals,
    }


def n4_fan(module, rows, loads, quadrics):
    names = (
        "s", "t", "alpha", "beta", "p", "q", "X", "Y", "U", "V",
        "y1", "y2", "y3", "y4", "z1", "z2", "z3", "z4",
        "k0", "k1", "k2",
    )
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    s, t, p, q = (x[name] for name in ("s", "t", "p", "q"))
    dseries = surface_series(module, ring, {2: s, 3: x["alpha"]}, {2: t, 3: x["beta"]}, 11)
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    tangent = module.vector_with_ab(ring, x["X"], x["Y"], x["y1"], x["y2"], x["y3"], x["y4"])
    newest = module.vector_with_ab(ring, x["U"], x["V"], x["z1"], x["z2"], x["z3"], x["z4"])
    for grade, vector in ((4, residual), (5, tangent), (6, newest)):
        add_normal(ring, dseries, grade, vector)
    source, load = literal_e3_source(
        module, rows, loads["K10"], dseries, (x["k0"], x["k1"], x["k2"]), ring
    )
    g10 = [source[index][10] for index in range(7)]
    for row_index in range(7):
        assert_zero(load[row_index][4], f"n4 K10 nominal G10 row {row_index + 1}")
        assert_zero(load[row_index][5], f"n4 K10 nominal G11 row {row_index + 1}")
    delta, cform, eform = assert_rank2_compatibility(
        module, ring, g10, quadrics, residual, ("X", "Y"), p, q, s, t, "n4 G10 rank2"
    )

    support_relations = {}
    terminals = {}
    for sign in (1, -1):
        replacements = {
            "p": (module.g(0, 8 * sign), "q"),
            "Y": (module.g(0, 8 * sign), "X"),
        }
        specialized = [ring.replace_by_scaled_var(poly, replacements) for poly in g10]
        combo3 = ring.add(specialized[2], specialized[0], F(1, 8))
        combo4 = specialized[3]
        expected3 = ring.add(
            ring.scale(ring.mul(x["X"], x["X"]), module.g(0, F(3 * sign, 2048))),
            ring.add(
                ring.scale(ring.mul(t, ring.mul(q, q)), F(3, 16)),
                ring.scale(ring.mul(s, ring.mul(q, q)), module.g(0, F(3 * sign, 128))),
            ),
        )
        expected4 = ring.add(
            ring.scale(ring.mul(x["X"], x["X"]), F(-3, 4096)),
            ring.add(
                ring.scale(ring.mul(t, ring.mul(q, q)), module.g(0, F(-3 * sign, 32))),
                ring.scale(ring.mul(s, ring.mul(q, q)), F(3, 256)),
            ),
        )
        assert_equal(module, ring, combo3, expected3, f"n4 sign {sign} combo3")
        assert_equal(module, ring, combo4, expected4, f"n4 sign {sign} combo4")

        reduced = [
            ring.replace_by_scaled_var(
                poly, {"s": (module.g(0, 8 * sign), "t")}, zeros=("X",)
            )
            for poly in specialized
        ]
        hform = ring.add(
            ring.sub(x["V"], ring.scale(x["U"], module.g(0, 8 * sign))),
            ring.scale(ring.mul(t, q), 128),
        )
        factors = (
            module.g(F(-3, 1024)), module.g(0, F(3 * sign, 2048)),
            module.g(F(3, 8192)), module.g(), module.g(F(3, 131072)),
            module.g(), module.g(F(3, 1048576)),
        )
        for row_index, factor in enumerate(factors):
            assert_equal(
                module, ring, reduced[row_index], ring.scale(ring.mul(q, hform), factor),
                f"n4 sign {sign} G10 H row {row_index + 1}",
            )
        support_relations[str(sign)] = poly_object(hform)

        rr_names = (
            "t", "q", "alpha", "beta", "gamma", "eta", "U", "P", "Q", "R", "W",
            "y1", "y2", "y3", "y4", "z1", "z2", "z3", "z4",
            "u1", "u2", "u3", "u4", "v1", "v2", "v3", "v4",
            "k0", "k1", "k2",
        )
        rr = module.Ring(rr_names)
        rv = {name: rr.var(name) for name in rr_names}
        rd = surface_series(
            module, rr,
            {
                2: rr.scale(rv["t"], module.g(0, 8 * sign)),
                3: rv["alpha"], 4: rv["gamma"],
            },
            {2: rv["t"], 3: rv["beta"], 4: rv["eta"]},
            13,
        )
        rn4 = module.cone_vector(rr, rr.const(), rr.const(), rr.scale(rv["q"], module.g(0, 8 * sign)), rv["q"])
        rn5 = module.vector_with_ab(rr, rr.const(), rr.const(), rv["y1"], rv["y2"], rv["y3"], rv["y4"])
        rn6 = module.vector_with_ab(
            rr,
            rv["U"],
            rr.add(rr.scale(rv["U"], module.g(0, 8 * sign)), rr.scale(rr.mul(rv["t"], rv["q"]), -128)),
            rv["z1"], rv["z2"], rv["z3"], rv["z4"],
        )
        rn7 = module.vector_with_ab(rr, rv["P"], rv["Q"], rv["u1"], rv["u2"], rv["u3"], rv["u4"])
        rn8 = module.vector_with_ab(rr, rv["R"], rv["W"], rv["v1"], rv["v2"], rv["v3"], rv["v4"])
        for grade, vector in ((4, rn4), (5, rn5), (6, rn6), (7, rn7), (8, rn8)):
            add_normal(rr, rd, grade, vector)
        req, rload = literal_e3_source(
            module, rows, loads["K10"], rd, (rv["k0"], rv["k1"], rv["k2"]), rr
        )
        for row_index in range(7):
            for grade in range(11):
                assert_zero(req[row_index][grade], f"n4 reduced sign {sign} row {row_index + 1} G{grade}")
        assert_zero(req[5][11], f"n4 reduced sign {sign} G11 row6")
        terminal = rr.scale(rr.power(rv["q"], 3), module.g(0, F(sign, 32)))
        assert_equal(module, rr, req[5][12], terminal, f"n4 reduced sign {sign} G12 row6")
        for grade in range(7):
            assert_zero(rload[5][grade], f"n4 sign {sign} K10 row6 raw G{grade}")
        terminals[str(sign)] = poly_object(terminal)

    rankzero = [ring.zero_vars(poly, ("p", "q")) for poly in g10]
    next_vector = [
        module.vector_with_ab(
            ring, x["X"], x["Y"], x["y1"], x["y2"], x["y3"], x["y4"]
        )[index]
        for index in range(6)
    ]
    for row_index, quadric in enumerate(quadrics):
        assert_equal(
            module, ring, rankzero[row_index], module.eval_dpoly(quadric, next_vector, ring),
            f"n4 rankzero recenter row {row_index + 1}",
        )
    return {
        "rank2": {"delta": poly_object(delta), "C": poly_object(cform), "E": poly_object(eform)},
        "rank1_G10_H": support_relations,
        "rank1_G12_terminals": terminals,
        "rankzero": "fresh n=5 cone at G10",
    }


def n5_final(module, rows, loads, quadrics, expected_w1, expected_w2):
    names = (
        "s", "t", "alpha", "beta", "p", "q", "X", "Y", "U", "V",
        "k0", "k1", "k2", "y1", "y2", "y3", "y4", "z1", "z2", "z3", "z4",
    )
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    s, t, p, q = (x[name] for name in ("s", "t", "p", "q"))
    dseries = surface_series(module, ring, {2: s, 3: x["alpha"]}, {2: t, 3: x["beta"]}, 13)
    residual = module.cone_vector(ring, ring.const(), ring.const(), p, q)
    tangent = module.vector_with_ab(ring, x["X"], x["Y"], x["y1"], x["y2"], x["y3"], x["y4"])
    newest = module.vector_with_ab(ring, x["U"], x["V"], x["z1"], x["z2"], x["z3"], x["z4"])
    for grade, vector in ((5, residual), (6, tangent), (7, newest)):
        add_normal(ring, dseries, grade, vector)
    source, load = literal_e3_source(
        module, rows, loads["K10"], dseries, (x["k0"], x["k1"], x["k2"]), ring
    )
    g10 = [source[index][10] for index in range(7)]
    g11 = [source[index][11] for index in range(7)]
    g12 = [source[index][12] for index in range(7)]
    for row_index, quadric in enumerate(quadrics):
        assert_equal(module, ring, g10[row_index], module.eval_dpoly(quadric, residual, ring), f"n5 G10 cone row {row_index + 1}")
        assert_equal(module, ring, g11[row_index], directional(module, ring, quadric, residual, tangent), f"n5 G11 tangent row {row_index + 1}")
        for name in ("alpha", "beta", "k1", "k2"):
            if ring.depends_on(g12[row_index], name):
                fail(("spurious n5 G12 dependence", row_index + 1, name))
    delta, cform, eform = assert_rank2_compatibility(
        module, ring, g12, quadrics, residual, ("X", "Y"), p, q, s, t, "n5 G12 rank2"
    )

    rank1_terminals = {}
    for sign in (1, -1):
        replacements = {
            "p": (module.g(0, 8 * sign), "q"),
            "Y": (module.g(0, 8 * sign), "X"),
        }
        specialized = [ring.replace_by_scaled_var(poly, replacements) for poly in g12]
        combo3 = ring.add(specialized[2], specialized[0], F(1, 8))
        combo4 = specialized[3]
        expected3 = ring.add(
            ring.scale(ring.mul(x["X"], x["X"]), module.g(0, F(3 * sign, 2048))),
            ring.add(
                ring.scale(ring.mul(t, ring.mul(q, q)), F(3, 16)),
                ring.scale(ring.mul(s, ring.mul(q, q)), module.g(0, F(3 * sign, 128))),
            ),
        )
        expected4 = ring.add(
            ring.scale(ring.mul(x["X"], x["X"]), F(-3, 4096)),
            ring.add(
                ring.scale(ring.mul(t, ring.mul(q, q)), module.g(0, F(-3 * sign, 32))),
                ring.scale(ring.mul(s, ring.mul(q, q)), F(3, 256)),
            ),
        )
        assert_equal(module, ring, combo3, expected3, f"n5 rank1 sign {sign} combo3")
        assert_equal(module, ring, combo4, expected4, f"n5 rank1 sign {sign} combo4")
        combo2 = ring.add(specialized[1], specialized[0], module.g(0, F(sign, 2)))
        reduced = ring.replace_by_scaled_var(
            combo2, {"s": (module.g(0, 8 * sign), "t")}, zeros=("X",)
        )
        terminal = ring.monomial({"k0": 1, "t": 3}, module.g(0, F(-5 * sign, 16)))
        assert_equal(module, ring, reduced, terminal, f"n5 rank1 sign {sign} terminal")
        assert_zero(ring.zero_vars(terminal, ("k0",)), f"n5 rank1 sign {sign} k0 control")
        rank1_terminals[str(sign)] = poly_object(terminal)

    rankzero = [ring.zero_vars(poly, ("p", "q")) for poly in g12]
    expected_row4 = ring.scale(
        ring.sub(ring.mul(x["Y"], x["Y"]), ring.scale(ring.mul(x["X"], x["X"]), 64)),
        F(3, 524288),
    )
    assert_equal(module, ring, rankzero[3], expected_row4, "n5 rankzero row4")
    split = {}
    for sign in (1, -1):
        branch = [
            ring.replace_by_scaled_var(poly, {"Y": (module.g(8 * sign), "X")})
            for poly in rankzero
        ]
        combo = ring.add(branch[2], branch[0], F(1, 8))
        expected = ring.scale(ring.mul(x["X"], x["X"]), F(3 * sign, 2048))
        assert_equal(module, ring, combo, expected, f"n5 rankzero split sign {sign}")
        split[str(sign)] = poly_object(expected)
    final_rankzero = [ring.zero_vars(poly, ("p", "q", "X", "Y")) for poly in g12]
    wrows = [ring.zero_vars(load[row_index][6], ("p", "q")) for row_index in range(7)]
    for row_index in range(7):
        assert_equal(
            module, ring, final_rankzero[row_index], ring.mul(x["k0"], wrows[row_index]),
            f"n5 final rankzero row {row_index + 1}",
        )
    expected1 = ring.scale(
        ring.mul(t, ring.sub(ring.scale(ring.mul(s, s), 3), ring.scale(ring.mul(t, t), 64))),
        F(5, 4096),
    )
    expected2 = ring.scale(
        ring.mul(s, ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 192))),
        F(5, 65536),
    )
    assert_equal(module, ring, wrows[0], expected1, "n5 final W1")
    assert_equal(module, ring, wrows[1], expected2, "n5 final W2")
    if F(64, 3) == F(192):
        fail("rankzero W contradiction collapsed")
    return {
        "rank2": {"delta": poly_object(delta), "C": poly_object(cform), "E": poly_object(eform)},
        "rank1_terminals": rank1_terminals,
        "rankzero_split": split,
        "W1": poly_object(expected1), "W2": poly_object(expected2),
    }


def fixtures(module, rows, loads):
    ring = module.Ring(())

    def n4_value(affine_value: int):
        dseries = surface_series(
            module, ring,
            {2: ring.const(module.g(0, 8))}, {2: ring.const(1)}, 13,
        )
        vectors = (
            (4, module.cone_vector(ring, ring.const(), ring.const(), ring.const(module.g(0, 8)), ring.const(1))),
            (5, module.vector_with_ab(ring, ring.const(), ring.const(), ring.const(), ring.const(), ring.const(), ring.const())),
            (6, module.vector_with_ab(ring, ring.const(), ring.const(affine_value), ring.const(), ring.const(), ring.const(), ring.const())),
        )
        for grade, vector in vectors:
            add_normal(ring, dseries, grade, vector)
        return literal_e3_source(module, rows, loads["K10"], dseries, (ring.const(1),), ring)[0]

    n4 = n4_value(-128)
    for row_index in range(7):
        for grade in range(12):
            assert_zero(n4[row_index][grade], f"n4 fixture row {row_index + 1} G{grade}")
    n4_terminal = ring.const(module.g(0, F(1, 32)))
    assert_equal(module, ring, n4[5][12], n4_terminal, "n4 fixture G12 row6")
    wrong_n4 = n4_value(-127)
    if all(not wrong_n4[row_index][10] for row_index in range(7)):
        fail("n4 affine -128 to -127 mutation invisible")

    def n5_value(kappa: int):
        dseries = surface_series(
            module, ring,
            {2: ring.const(module.g(0, 8))}, {2: ring.const(1)}, 13,
        )
        vectors = (
            (5, module.cone_vector(ring, ring.const(), ring.const(), ring.const(module.g(0, 8)), ring.const(1))),
            (6, module.vector_with_ab(ring, ring.const(), ring.const(), ring.const(), ring.const(), ring.const(), ring.const())),
            (7, module.vector_with_ab(ring, ring.const(), ring.const(-128), ring.const(), ring.const(), ring.const(), ring.const())),
        )
        for grade, vector in vectors:
            add_normal(ring, dseries, grade, vector)
        return literal_e3_source(module, rows, loads["K10"], dseries, (ring.const(kappa),), ring)[0]

    load_off = n5_value(0)
    load_on = n5_value(1)
    for row_index in range(7):
        for grade in range(13):
            assert_zero(load_off[row_index][grade], f"n5 load-off fixture row {row_index + 1} G{grade}")
        for grade in range(12):
            assert_zero(load_on[row_index][grade], f"n5 load-on fixture row {row_index + 1} G{grade}")
    if not any(load_on[row_index][12] for row_index in range(7)):
        fail("n5 K10 unit mutation invisible")
    return {
        "n4": "G0_G11_PASS;G12_ROW6=i/32;-128_TO_-127_FAILS_G10",
        "n5": "k10[0]=0_PASSES_G12;k10[0]=1_FAILS_G12",
    }


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
    minima, late, w1, w2 = surface_calendar(module, rows, loads)
    fresh = {
        str(order): fresh_cone_tangent(module, rows, loads, quadrics, order)
        for order in (2, 3, 4, 5)
    }
    first = n2_fan(module, rows, loads)
    third = n3_fan(module, rows, loads, quadrics)
    fourth = n4_fan(module, rows, loads, quadrics)
    fifth = n5_final(module, rows, loads, quadrics, w1, w2)
    controls = fixtures(module, rows, loads)

    certificate = {
        "type": "K00-RAM-E3M2-G0-G12-COMPLETE-POINT-FAN/v1",
        "basis": "0d7544ebd5cb12def6bac892646010301098be3c",
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "tail_terms": term_count,
        "field": "algebraic closure of characteristic zero; Gaussian rank-one charts",
        "normalization": "Lambda=tau^3; C6=1; K10 shift=tau^6; ord(d)=2",
        "opens": [
            "k10[0]!=0", "Jdet[0]!=0", "union_i D(d_i[2])",
            "after first rank-zero recentering: D(s) union D(t)",
        ],
        "surface_k10_minima": minima,
        "calendar": "K10 nominal G10 but exact G10/G11 zero; first actual G12; K6 G21/G23; K2 G33; targets G43/G49/G55/G57",
        "late_calendar": late,
        "fresh_cone_tangent": fresh,
        "n2": first,
        "n3": third,
        "n4": fourth,
        "n5": fifth,
        "transition_tree": [
            "G4 n2 rank2/rank1 dead G6; rank0 -> n3",
            "G6 n3 rank2 dead G8; rank1 survives G8 dead G9; rank0 -> n4",
            "G8 n4 rank2 dead G10; rank1 survives G10 and dies raw G12; rank0 -> n5",
            "G10 n5 rank2/rank1/rank0 all dead G12",
        ],
        "fixtures": controls,
        "conclusion": "EMPTY_THROUGH_G12_ON_DECLARED_OPENS_POINT_SET",
        "scope": "finite-jet field-valued point fan only; formal arcs excluded by truncation implication",
        "nonclaims": ["scheme equality", "converse lifting", "reachability", "attainment", "map", "JC2"],
        "mutations": ["custody", "calendar_G10_G11_zero", "n4_-128_to_-127", "n4_G12_row6", "n5_k10_open", "delta_64", "W2_192"],
    }
    cert_bytes = (json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n").encode()
    cert_sha = sha256(cert_bytes).hexdigest()
    if EXPECTED_CERTIFICATE_SHA256 != "PENDING" and cert_sha != EXPECTED_CERTIFICATE_SHA256:
        fail(("certificate digest", cert_sha, EXPECTED_CERTIFICATE_SHA256))

    print("K00_RAM_E3M2_G0_G12_COMPLETE_RANKFAN_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("CALENDAR=K10_NOMINAL_G10_BUT_EXACT_G10_G11_ZERO;FIRST_ACTUAL_G12;K6_G21_G23;K2_G33;TARGETS_G43_G49_G55_G57")
    print("G4_N2=RANK2_RANK1_DEAD_G6;RANK0_TO_N3")
    print("G6_N3=RANK2_DEAD_G8;RANK1_DEAD_G9;RANK0_TO_N4")
    print("G8_N4=RANK2_DEAD_G10;RANK1_G10_SURVIVOR_DEAD_RAW_G12;RANK0_TO_N5")
    print("N4_G12_ROW6=EPS*i*q^3/32;ALL_S3_T3_S4_T4_N5_N6_N7_N8_K10_RETAINED")
    print("G10_N5=RANK2_RANK1_RANK0_ALL_DEAD_G12")
    print("N5_G12_RANK1=-EPS*5*i*k10[0]*t^3/16;RANK0=Q(N6)+k10[0]*W_EMPTY")
    print("FIXTURES=N4_G0_G11_PASS_G12_FAIL;N5_K10_OFF_PASS_ON_FAIL")
    print("CELL_STATUS=POINT_SET_EMPTY_THROUGH_G12_ON_C6_K10_JDET_OPENS")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,CALENDAR,N4_-128_TO_-127,N4_ROW6,N5_K10_OPEN,DELTA_64,W2_192")


if __name__ == "__main__":
    main()
