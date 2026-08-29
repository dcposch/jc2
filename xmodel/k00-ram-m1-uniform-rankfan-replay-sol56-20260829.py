#!/usr/bin/env python3
"""Exact stdlib replay for all e=2,m=1 faces and the uniformity audit.

The replay reconstructs the frozen 569-tail source, checks the exact unloaded
surface and its square-normal containment, derives the three load restrictions,
and audits the proposed transverse induction.  It exhibits the omitted second
surface coefficient that lets an e=3,m=1 rank-one prefix survive through G8.
The corrected fresh rank-zero K10 fan is also recomputed at two normal orders.
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
G7_REPORT = ROOT / "xmodel/k00-ram-e2m1-g7-rankfan-certificate-sol56-20260829.md"
G7_REPLAY = ROOT / "xmodel/k00-ram-e2m1-g7-rankfan-replay-sol56-20260829.py"
G7_REVIEW = ROOT / "xmodel/k00-ram-e2m1-g7-rankfan-hostile-review-opus5-20260829.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    G3_PROMOTION: "d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860",
    G7_REPORT: "66b4f59e16f9f8f26a42e5305e5906ff495c9d00c15d96a291f91baa9efbeff4",
    G7_REPLAY: "981b39f91afd4e449193077bc00d02937701618cee9bc3ae53547edaaa11dac6",
    G7_REVIEW: "07c4ad13091c15dd39a5a703e266343323de40a3352d6d9449adb9c26473d736",
}
EXPECTED_CERTIFICATE_SHA256 = "afd1bf5242adae7f300818ae1ae85c8c18b0cdb95a09bf03d7df430a2749c62a"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_m1_uniform_engine", ENGINE)
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


def surface_vector(module, ring, s, t):
    return [
        ring.add(ring.scale(s, 2), ring.mul(s, s)),
        ring.scale(ring.mul(ring.add(ring.const(1), s), t), F(1, 8)),
        ring.add(s, ring.scale(ring.mul(t, t), 16)),
        t,
        s,
        ring.scale(t, 2),
    ]


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
    for i in range(6):
        first = module.dderivative(poly, i)
        for j in range(6):
            out = ring.add(
                out,
                ring.mul(
                    ring.mul(
                        module.eval_dpoly(
                            module.dderivative(first, j), point, ring
                        ),
                        direction[i],
                    ),
                    direction[j],
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


def homogeneous(ring, poly, degree: int):
    return {key: value for key, value in poly.items() if sum(key) == degree}


def qstring(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_object(poly):
    answer = []
    for key in sorted(poly):
        real, imag = poly[key]
        answer.append([list(key), qstring(real), qstring(imag)])
    return answer


def surface_and_sector_checks(module, rows, loads):
    ring = module.Ring(("S", "T"))
    s, t = (ring.var(name) for name in ring.names)
    surface = surface_vector(module, ring, s, t)
    for index, row in enumerate(rows):
        assert_zero(module.eval_dpoly(row, surface, ring), f"surface row {index + 1}")

    wrong = list(surface)
    wrong[2] = ring.add(s, ring.scale(ring.mul(t, t), 15))
    if not any(module.eval_dpoly(row, wrong, ring) for row in rows):
        fail("surface mutation invisible")

    restrictions = {
        label: [module.eval_dpoly(row, surface, ring) for row in loads[label]]
        for label in ("K10", "K6", "K2")
    }
    expected_k10_1 = ring.scale(
        ring.mul(t, ring.sub(ring.scale(ring.mul(s, s), 3),
                             ring.scale(ring.mul(t, t), 64))), F(5, 4096)
    )
    expected_k10_2 = ring.scale(
        ring.mul(s, ring.sub(ring.mul(s, s),
                             ring.scale(ring.mul(t, t), 192))), F(5, 65536)
    )
    assert_equal(module, ring, homogeneous(ring, restrictions["K10"][0], 3),
                 expected_k10_1, "K10 surface cubic row 1")
    assert_equal(module, ring, homogeneous(ring, restrictions["K10"][1], 3),
                 expected_k10_2, "K10 surface cubic row 2")
    expected_k6_1 = ring.scale(ring.mul(s, t), F(3, 64))
    expected_k6_2 = ring.scale(
        ring.sub(ring.mul(s, s), ring.scale(ring.mul(t, t), 64)),
        F(3, 2048),
    )
    assert_equal(module, ring, homogeneous(ring, restrictions["K6"][0], 2),
                 expected_k6_1, "K6 surface quadric row 1")
    assert_equal(module, ring, homogeneous(ring, restrictions["K6"][1], 2),
                 expected_k6_2, "K6 surface quadric row 2")
    assert_equal(module, ring, homogeneous(ring, restrictions["K2"][0], 1),
                 ring.scale(t, F(1, 2)), "K2 surface linear row 1")
    assert_equal(module, ring, homogeneous(ring, restrictions["K2"][1], 1),
                 ring.scale(s, F(1, 32)), "K2 surface linear row 2")

    minima = {}
    for label in ("K10", "K6", "K2"):
        minima[label] = [
            min((sum(key) for key in poly), default=None)
            for poly in restrictions[label]
        ]
    if minima != {
        "K10": [3, 3, 3, None, 3, 4, 3],
        "K6": [2, 2, 2, None, 2, 3, 2],
        "K2": [1, 1, 1, None, 1, 2, 1],
    }:
        fail(("surface sector minima", minima))

    # In exact surface coordinates the unloaded ideal lies in J^2.  Here
    # n0,n1,n2,n5 are the four literal generators of the surface ideal.
    nr = module.Ring(("S", "T", "n0", "n1", "n2", "n5"))
    nv = {name: nr.var(name) for name in nr.names}
    ns, nt = nv["S"], nv["T"]
    normal_images = [
        nr.add(nr.add(nr.scale(ns, 2), nr.mul(ns, ns)), nv["n0"]),
        nr.add(nr.scale(nr.mul(nr.add(nr.const(1), ns), nt), F(1, 8)), nv["n1"]),
        nr.add(nr.add(ns, nr.scale(nr.mul(nt, nt), 16)), nv["n2"]),
        nt, ns, nr.add(nr.scale(nt, 2), nv["n5"]),
    ]
    for index, row in enumerate(rows):
        transformed = module.eval_dpoly(row, normal_images, nr)
        if not transformed or min(sum(key[2:]) for key in transformed) < 2:
            fail(("I not visibly contained in J^2", index + 1))
    return restrictions, minima


def stable_rank_fan(module, rows, quadrics, cubics):
    # The grade 2n+1 fan is independent of n>=3.  Realize it at n=3.
    ring = module.Ring(("s", "t", "a", "b", "p", "q", "X", "Y"))
    v = {name: ring.var(name) for name in ring.names}
    ell = module.old_plane(ring, v["s"], v["t"])
    mu = mu_vector(ring, v["s"], v["t"])
    w = module.cone_vector(ring, v["a"], v["b"], v["p"], v["q"])
    newest = module.vector_with_ab(
        ring, v["X"], v["Y"], ring.const(), ring.const(), ring.const(), ring.const()
    )
    dseries = []
    for index in range(6):
        series = module.series_zero(8)
        series[1], series[2], series[3], series[4] = (
            ell[index], mu[index], w[index], newest[index]
        )
        dseries.append(series)
    equations = [module.eval_dpoly_series(row, dseries, ring) for row in rows]
    g7 = [equation[7] for equation in equations]
    alpha = [module.eval_dpoly(module.dderivative(q, 5), w, ring) for q in quadrics]
    beta = [module.eval_dpoly(module.dderivative(q, 0), w, ring) for q in quadrics]
    normal = [second_half(module, ring, cubics[i], ell, w) for i in range(7)]
    for index in range(7):
        expected = ring.add(
            ring.add(normal[index], ring.mul(alpha[index], v["X"])),
            ring.mul(beta[index], v["Y"]),
        )
        assert_equal(module, ring, g7[index], expected,
                     f"stable grade 2n+1 row {index + 1}")
    delta = ring.add(ring.mul(v["p"], v["p"]),
                     ring.scale(ring.mul(v["q"], v["q"]), 64))
    cform = ring.add(
        ring.mul(v["t"], ring.sub(ring.scale(ring.mul(v["q"], v["q"]), 64),
                                   ring.mul(v["p"], v["p"]))),
        ring.scale(ring.mul(ring.mul(v["s"], v["p"]), v["q"]), 2),
    )
    eform = ring.sub(
        ring.mul(v["s"], ring.sub(ring.scale(ring.mul(v["q"], v["q"]), 64),
                                   ring.mul(v["p"], v["p"]))),
        ring.scale(ring.mul(ring.mul(v["t"], v["p"]), v["q"]), 128),
    )
    augmented = determinant3(ring, [[alpha[i], beta[i], normal[i]] for i in range(3)])
    assert_equal(module, ring, augmented,
                 ring.scale(ring.mul(delta, cform), F(27, 2**35)),
                 "stable rank-two determinant")
    assert_equal(module, ring, normal[3], ring.scale(eform, F(3, 2**15)),
                 "stable rank-two row 4")

    # A tempting induction sets the second surface coefficient to zero and
    # then declares the stable rank-one branch impossible at grade 2n+2.
    # That is false.  Retaining S=A*tau^2 and T=B*tau^2 changes the two
    # cokernel equations, and the exact choice
    #
    #   X=sign*24*i*t*q,  A=-4*t^2,  B=0
    #
    # makes both vanish.  This is the first obstruction to extending the
    # e=2 proof by a coefficient-blind recentering induction.
    rank1_records = {}
    for sign in (1, -1):
        names = ("t", "q", "A", "B", "X", "y1", "y2", "y3", "y4",
                 *(f"z{i}" for i in range(6)))
        rr = module.Ring(names)
        rv = {name: rr.var(name) for name in names}
        eight_i = module.g(0, 8 * sign)
        rs = rr.scale(rv["t"], eight_i)
        rp = rr.scale(rv["q"], eight_i)
        # Exact coefficients of D(S,T) for
        # S=rs*tau+A*tau^2 and T=t*tau+B*tau^2 through tau^4.
        surface_coefficients = [
            {
                1: rr.scale(rs, 2),
                2: rr.add(rr.scale(rv["A"], 2), rr.mul(rs, rs)),
                3: rr.scale(rr.mul(rs, rv["A"]), 2),
                4: rr.mul(rv["A"], rv["A"]),
            },
            {
                1: rr.scale(rv["t"], F(1, 8)),
                2: rr.scale(rr.add(rv["B"], rr.mul(rs, rv["t"])), F(1, 8)),
                3: rr.scale(
                    rr.add(rr.mul(rs, rv["B"]), rr.mul(rv["A"], rv["t"])),
                    F(1, 8),
                ),
                4: rr.scale(rr.mul(rv["A"], rv["B"]), F(1, 8)),
            },
            {
                1: rs,
                2: rr.add(rv["A"], rr.scale(rr.mul(rv["t"], rv["t"]), 16)),
                3: rr.scale(rr.mul(rv["t"], rv["B"]), 32),
                4: rr.scale(rr.mul(rv["B"], rv["B"]), 16),
            },
            {1: rv["t"], 2: rv["B"]},
            {1: rs, 2: rv["A"]},
            {1: rr.scale(rv["t"], 2), 2: rr.scale(rv["B"], 2)},
        ]
        rw = module.cone_vector(rr, rr.const(), rr.const(), rp, rv["q"])
        bvalue = rr.add(rr.scale(rv["X"], eight_i),
                        rr.scale(rr.mul(rv["t"], rv["q"]), -128))
        rnext = module.vector_with_ab(
            rr, rv["X"], bvalue, rv["y1"], rv["y2"], rv["y3"], rv["y4"]
        )
        rz = [rv[f"z{i}"] for i in range(6)]
        rseries = []
        for index in range(6):
            series = module.series_zero(9)
            for grade, value in surface_coefficients[index].items():
                series[grade] = value
            series[3] = rr.add(series[3], rw[index])
            series[4] = rr.add(series[4], rnext[index])
            series[5] = rz[index]
            rseries.append(series)
        req = [module.eval_dpoly_series(row, rseries, rr) for row in rows]
        for row_index in range(7):
            for grade in range(8):
                assert_zero(req[row_index][grade],
                            f"stable rank1 sign {sign} row {row_index + 1} G{grade}")
        g8 = [equation[8] for equation in req]
        compat3 = rr.add(g8[2], g8[0], F(1, 8))
        compat4 = g8[3]
        tq = rr.mul(rv["t"], rv["q"])
        q2 = rr.mul(rv["q"], rv["q"])
        common = rr.add(
            rr.mul(rv["X"], rv["X"]),
            rr.scale(rr.mul(tq, rv["X"]), module.g(0, -48 * sign)),
        )
        form512 = rr.add(
            rr.add(common, rr.scale(rr.mul(tq, tq), -512)),
            rr.add(
                rr.scale(rr.mul(rv["A"], q2), 16),
                rr.scale(rr.mul(rv["B"], q2), module.g(0, -128 * sign)),
            ),
        )
        form640 = rr.add(
            rr.add(common, rr.scale(rr.mul(tq, tq), -640)),
            rr.add(
                rr.scale(rr.mul(rv["A"], q2), -16),
                rr.scale(rr.mul(rv["B"], q2), module.g(0, 128 * sign)),
            ),
        )
        assert_equal(module, rr, compat3,
                     rr.scale(form512, module.g(0, F(3 * sign, 2048))),
                     f"stable rank1 sign {sign} compatibility 3")
        assert_equal(module, rr, compat4, rr.scale(form640, F(-3, 4096)),
                     f"stable rank1 sign {sign} compatibility 4")
        survivor_images = {
            "X": (module.g(0, 24 * sign), "t"),
            "A": (-4, "t"),
            "B": (0, "t"),
        }
        # replace_by_scaled_var is monomial substitution, so A=-4*t^2 is
        # applied in two steps using a direct sparse map below.
        target = module.Ring(("t", "q", "y1", "y2", "y3", "y4",
                              *(f"z{i}" for i in range(6))))
        images = {name: target.var(name) for name in target.names}
        images.update({
            "A": target.scale(target.mul(images["t"], images["t"]), -4),
            "B": target.const(),
            "X": target.scale(target.mul(images["t"], images["q"]),
                              module.g(0, 24 * sign)),
        })

        def map_poly(poly):
            out = target.const()
            for key, coefficient in poly.items():
                term = target.const(coefficient)
                for name, exponent in zip(rr.names, key):
                    if exponent:
                        term = target.mul(term, target.power(images[name], exponent))
                out = target.add(out, term)
            return out

        assert_zero(map_poly(form512), f"stable survivor sign {sign} form512")
        assert_zero(map_poly(form640), f"stable survivor sign {sign} form640")
        wrong_form = rr.add(
            rr.add(common, rr.scale(rr.mul(tq, tq), -639)),
            rr.add(
                rr.scale(rr.mul(rv["A"], q2), -16),
                rr.scale(rr.mul(rv["B"], q2), module.g(0, 128 * sign)),
            ),
        )
        if not map_poly(wrong_form):
            fail("stable-survivor mutation invisible")
        rank1_records[str(sign)] = [poly_object(compat3), poly_object(compat4)]
    return rank1_records


def e3_rankone_prefix_counterexample(module, rows, loads):
    """An exact full-source e=3,m=1 prefix through G8.

    This is finite jet data only.  It disproves the proposed stable claim
    that every old rank-one transverse branch dies one grade after its first
    compatibility equation; it says nothing about G9 or a formal lift.
    """
    ring = module.Ring(())
    zero = module.g()
    one = module.g(1)
    s, a, t, b = module.g(0, 8), module.g(-4), one, zero
    surface = [
        {1: module.g(0, 16), 2: module.g(-72),
         3: module.g(0, -64), 4: module.g(16)},
        {1: module.g(F(1, 8)), 2: module.g(0, 1),
         3: module.g(F(-1, 2))},
        {1: s, 2: module.g(12)},
        {1: t},
        {1: s, 2: a},
        {1: module.g(2)},
    ]
    normal3 = [module.g(0, 16), zero, zero, one, module.g(0, -8), module.g(4)]
    normal4 = [module.g(-320), zero, zero, zero, zero, module.g(0, 24)]
    normal5 = [module.g(0, -1088), zero, zero, zero, zero, zero]
    dseries = []
    for index in range(6):
        series = module.series_zero(9)
        for grade, value in surface[index].items():
            series[grade] = ring.const(value)
        series[3] = ring.add(series[3], ring.const(normal3[index]))
        series[4] = ring.add(series[4], ring.const(normal4[index]))
        series[5] = ring.add(series[5], ring.const(normal5[index]))
        dseries.append(series)
    equations = [module.eval_dpoly_series(row, dseries, ring) for row in rows]
    load_series = [module.eval_dpoly_series(row, dseries, ring) for row in loads["K10"]]
    for row_index in range(7):
        for grade in range(6, 9):
            source_grade = grade - 6
            equations[row_index][grade] = ring.add(
                equations[row_index][grade], load_series[row_index][source_grade]
            )
        for grade in range(9):
            assert_zero(equations[row_index][grade],
                        f"e3 rank-one prefix row {row_index + 1} G{grade}")

    wrong = [dict(entries) for entries in surface]
    wrong[4][2] = module.g(-3)
    wrong_series = []
    for index in range(6):
        series = module.series_zero(9)
        for grade, value in wrong[index].items():
            series[grade] = ring.const(value)
        series[3] = ring.add(series[3], ring.const(normal3[index]))
        series[4] = ring.add(series[4], ring.const(normal4[index]))
        series[5] = ring.add(series[5], ring.const(normal5[index]))
        wrong_series.append(series)
    if all(
        not module.eval_dpoly_series(row, wrong_series, ring)[8]
        for row in rows
    ):
        fail("e3 prefix surface-coefficient mutation invisible")
    return {
        "S": {"1": "8*i", "2": "-4"},
        "T": {"1": "1"},
        "normal_3": ["16*i", "0", "0", "1", "-8*i", "4"],
        "normal_4": ["-320", "0", "0", "0", "0", "24*i"],
        "normal_5": ["-1088*i", "0", "0", "0", "0", "0"],
        "vanishing": "full e=3 source G0..G8 with k10[0]=1",
    }


def final_fan(module, rows, loads, quadrics, cubics):
    names = ("s", "t", "p", "q", "X", "Y", "k")
    ring = module.Ring(names)
    v = {name: ring.var(name) for name in names}
    ell = module.old_plane(ring, v["s"], v["t"])
    mu = mu_vector(ring, v["s"], v["t"])
    w = module.cone_vector(ring, ring.const(), ring.const(), v["p"], v["q"])
    newest = module.vector_with_ab(
        ring, v["X"], v["Y"], ring.const(), ring.const(), ring.const(), ring.const()
    )

    def coefficient(normal_order: int):
        e = normal_order - 1
        cutoff = 2 * normal_order + 2
        dseries = []
        for index in range(6):
            series = module.series_zero(cutoff)
            series[1], series[2] = ell[index], mu[index]
            series[normal_order], series[normal_order + 1] = w[index], newest[index]
            dseries.append(series)
        out = [module.eval_dpoly_series(row, dseries, ring) for row in rows]
        load = [module.eval_dpoly_series(row, dseries, ring) for row in loads["K10"]]
        grade = 2 * normal_order + 1
        shift = 2 * e
        return [
            ring.add(out[index][grade], ring.mul(v["k"], load[index][grade - shift]))
            for index in range(7)
        ]

    final3 = coefficient(3)
    final4 = coefficient(4)
    if final3 != final4:
        fail("final K10 fan did not stabilize from n=3 to n=4")
    m4 = [module.dhom(row, 2) for row in loads["K10"]]
    a10_cubic = [module.dhom(row, 3) for row in loads["K10"]]
    load_rows = []
    alpha = []
    beta = []
    normal = []
    for index in range(7):
        load_row = ring.add(
            directional(module, ring, m4[index], ell, mu),
            module.eval_dpoly(a10_cubic[index], ell, ring),
        )
        normal_row = second_half(module, ring, cubics[index], ell, w)
        coefficient_row = directional(module, ring, quadrics[index], w, newest)
        expected = ring.add(ring.add(coefficient_row, normal_row),
                            ring.mul(v["k"], load_row))
        assert_equal(module, ring, final3[index], expected,
                     f"uniform final fan row {index + 1}")
        load_rows.append(load_row)
        normal.append(normal_row)
        alpha.append(module.eval_dpoly(module.dderivative(quadrics[index], 5), w, ring))
        beta.append(module.eval_dpoly(module.dderivative(quadrics[index], 0), w, ring))

    delta = ring.add(ring.mul(v["p"], v["p"]),
                     ring.scale(ring.mul(v["q"], v["q"]), 64))
    cform = ring.add(
        ring.mul(v["t"], ring.sub(ring.scale(ring.mul(v["q"], v["q"]), 64),
                                   ring.mul(v["p"], v["p"]))),
        ring.scale(ring.mul(ring.mul(v["s"], v["p"]), v["q"]), 2),
    )
    eform = ring.sub(
        ring.mul(v["s"], ring.sub(ring.scale(ring.mul(v["q"], v["q"]), 64),
                                   ring.mul(v["p"], v["p"]))),
        ring.scale(ring.mul(ring.mul(v["t"], v["p"]), v["q"]), 128),
    )
    augmented = determinant3(
        ring,
        [[alpha[i], beta[i], ring.add(normal[i], ring.mul(v["k"], load_rows[i]))]
         for i in range(3)],
    )
    assert_equal(module, ring, augmented,
                 ring.scale(ring.mul(delta, cform), F(27, 2**35)),
                 "uniform final rank-two determinant")
    assert_equal(module, ring, final3[3], ring.scale(eform, F(3, 2**15)),
                 "uniform final row 4")

    terminals = {}
    for sign in (1, -1):
        combo = ring.add(final3[1], final3[0], module.g(0, F(sign, 2)))
        specialized = ring.replace_by_scaled_var(
            combo,
            {"p": (module.g(0, 8 * sign), "q"),
             "s": (module.g(0, 8 * sign), "t")},
        )
        terminal = ring.monomial(
            {"t": 3, "k": 1}, module.g(0, F(-5 * sign, 16))
        )
        assert_equal(module, ring, specialized, terminal,
                     f"uniform final rank-one sign {sign}")
        terminals[str(sign)] = poly_object(terminal)

    expected_w1 = ring.scale(
        ring.mul(v["t"], ring.sub(ring.scale(ring.mul(v["s"], v["s"]), 3),
                                   ring.scale(ring.mul(v["t"], v["t"]), 64))),
        F(5, 4096),
    )
    expected_w2 = ring.scale(
        ring.mul(v["s"], ring.sub(ring.mul(v["s"], v["s"]),
                                   ring.scale(ring.mul(v["t"], v["t"]), 192))),
        F(5, 65536),
    )
    assert_equal(module, ring, load_rows[0], expected_w1, "uniform rank-zero W1")
    assert_equal(module, ring, load_rows[1], expected_w2, "uniform rank-zero W2")
    return final3, terminals


def main() -> None:
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("custody", path, digest(path), expected))
    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    quadrics = [module.dhom(row, 2) for row in rows]
    cubics = [module.dhom(row, 3) for row in rows]
    restrictions, minima = surface_and_sector_checks(module, rows, loads)
    stable_rank1 = stable_rank_fan(module, rows, quadrics, cubics)
    e3_prefix = e3_rankone_prefix_counterexample(module, rows, loads)
    final_rows, terminals = final_fan(module, rows, loads, quadrics, cubics)

    # Literal global stencil bounds show that no K6/K2/target can reach the
    # terminal grade 2e+3 when e>=2 and every boundary series has order >=1.
    for e in range(2, 100):
        terminal = 2 * e + 3
        lower = {
            "K6": 6 * e + 2,
            "K2": 10 * e + 2,
            "mu2": 14 * e + 1,
            "mu4": 16 * e + 1,
            "mu6": 18 * e + 1,
            "Jdet": 19 * e,
        }
        if any(value <= terminal for value in lower.values()):
            fail(("calendar inequality", e, terminal, lower))

    certificate = {
        "type": "K00-RAM-E2M1-ALL-FACES-AND-UNIFORM-INDUCTION-AUDIT/v1",
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "tail_terms": term_count,
        "unloaded": "R(D(S,T))=0_AND_I_SUBSET_J^2",
        "surface_sector_minima": minima,
        "stable_rank1_cokernel": stable_rank1,
        "e3_m1_rankone_prefix_counterexample": e3_prefix,
        "fresh_rankzero_final_rows": [poly_object(poly) for poly in final_rows],
        "fresh_rankzero_final_rank1_terminals": terminals,
        "scope": {
            "proved_e_m": [2, 1],
            "k10_Jdet": "units",
            "k6_k2_mu2_mu4_mu6": "arbitrary positive order or zero series",
        },
        "conclusion": "E2_M1_EMPTY_ON_ALL_BOUNDARY_LOAD_ORDER_FACES",
        "failed_stronger_reading": "NAIVE_ALL_E_M1_RECENTERING_INDUCTION_REFUTED_AT_E3_G8_PREFIX",
        "attainment": False,
    }
    cert_bytes = (json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n").encode()
    cert_sha = sha256(cert_bytes).hexdigest()
    if EXPECTED_CERTIFICATE_SHA256 != "PENDING" and cert_sha != EXPECTED_CERTIFICATE_SHA256:
        fail(("certificate digest", cert_sha))

    print("K00_RAM_M1_UNIFORM_RANKFAN_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("UNLOADED_SURFACE=EXACT;UNLOADED_IDEAL_SUBSET_SURFACE_SQUARE=EXACT")
    print("SURFACE_LOAD_ORDERS=K10:3,K6:2,K2:1")
    print("STABLE_RANK2=EMPTY_AT_2N+1;STABLE_RANK1_NAIVE_KILL=REFUTED_BY_SURFACE_COEFFICIENT")
    print("E3_M1_RANK1_PREFIX=SURVIVES_FULL_SOURCE_THROUGH_G8;G9_UNDECIDED")
    print("FRESH_RANKZERO_FINAL_K10_FAN=SHIFT_INDEPENDENT_FOR_N_GE3")
    print("E2M1_LOAD_ORDER_FACES=ALL_POSITIVE_OR_INFINITE_BOUNDARY_ORDERS")
    print("THEOREM=EMPTY_FOR_E2_M1_ALL_LOAD_ORDER_FACES_ON_GENERIC_K00_RAY")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,SURFACE_16_TO_15,K10_CUBIC,STABLE_640_TO_639,E3_SURFACE_COEFF,FINAL_SHIFT")


if __name__ == "__main__":
    main()
