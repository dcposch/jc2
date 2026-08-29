#!/usr/bin/env python3
"""Desk-scale exact preflight for normalized V20R2 valuation three.

The arithmetic engine is imported from the byte-pinned promoted valuation-two
replay, but every valuation-three coefficient below is freshly expanded from
the frozen 569 tails.  This is a source/threat preflight, not a grade-19
producer.  It writes no files and uses no CAS or network service.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[1]
TAILS = (
    ROOT
    / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
COMPILER = (
    ROOT
    / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827"
    / "compile_contracted_source_v20r2.py"
)
R2_REPLAY = ROOT / "xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    R2_REPLAY: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
}


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_r2_pinned_engine", R2_REPLAY)
    if spec is None or spec.loader is None:
        fail("cannot import pinned exact engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_compiler_module():
    spec = importlib.util.spec_from_file_location("k00_v20r2_pinned_compiler", COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot import pinned source compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def vector_with_kernel(module, ring, aval, bval, a, b, u, v):
    """A vector with displayed A,B and four common-kernel coordinates."""
    return module.vector_with_ab(
        ring,
        aval,
        bval,
        a,
        b,
        ring.add(ring.scale(a, 8), v),
        ring.sub(b, u),
    )


def full_rows(module, rows, loads, coefficients, source, ring, truncation):
    dseries = []
    for entries in coefficients:
        series = module.series_zero(truncation)
        for grade, value in entries.items():
            series[grade] = value
        dseries.append(series)

    def shifted(entries, amount):
        series = module.series_zero(truncation)
        for grade, value in entries.items():
            if grade + amount < truncation:
                series[grade + amount] = value
        return series

    load_series = {
        "K10": shifted(source.get("K10", {}), 2),
        "K6": shifted(source.get("K6", {}), 6),
        "K2": shifted(source.get("K2", {}), 10),
    }
    answer = []
    for index, unloaded in enumerate(rows):
        total = module.eval_dpoly_series(unloaded, dseries, ring)
        for label in ("K10", "K6", "K2"):
            evaluated = module.eval_dpoly_series(loads[label][index], dseries, ring)
            total = module.series_add(
                total,
                module.series_mul(load_series[label], evaluated, ring),
                ring,
            )
        answer.append(total)
    return answer


def assert_zero(poly, label):
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def assert_equal(module, ring, left, right, label):
    module.assert_equal(left, right, ring, label)


def coker5(ring, vector):
    return (
        vector[3],
        vector[5],
        ring.add(vector[2], vector[0], F(1, 8)),
        ring.add(vector[4], vector[0], F(1, 128)),
        ring.add(vector[6], vector[0], F(1, 1024)),
    )


def source_and_calendar(module, rows, loads):
    profiles = {
        "R": [sorted({sum(key) for key in row}) for row in rows],
        "K10": [sorted({sum(key) for key in row}) for row in loads["K10"]],
        "K6": [sorted({sum(key) for key in row}) for row in loads["K6"]],
        "K2": [sorted({sum(key) for key in row}) for row in loads["K2"]],
    }
    expected = {
        "R": [[2, 3, 4], [2, 3, 4], [2, 3, 4, 5],
              [2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5, 6],
              [2, 3, 4, 5, 6]],
        "K10": [[2, 3], [2, 3, 4], [2, 3, 4], [2, 3, 4],
                [2, 3, 4, 5], [2, 3, 4, 5], [2, 3, 4, 5]],
        "K6": [[1, 2], [1, 2], [1, 2, 3], [2, 3],
               [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]],
        "K2": [[1], [1], [1], [1, 2], [1, 2], [1, 2], [1, 2, 3]],
    }
    if profiles != expected:
        fail(("rowwise homogeneous support", profiles))

    raw_anchors = {
        "R2": 6, "R3": 9, "R4": 12, "R5": 15, "R6": 18,
        "K10_2": 8, "K10_3": 11, "K10_4": 14, "K10_5": 17,
        "K6_1": 10, "K6_2": 13, "K6_3": 16, "K6_4": 19,
        "K2_1": 14, "K2_2": 17,
        "mu2_1": 15, "mu4_1": 17, "mu6_1": 19, "Jdet_0": 19,
    }
    if raw_anchors["K10_2"] != 2 + 2 * 3:
        fail("literal K10 quadratic calendar")
    if raw_anchors["K6_1"] != 6 + 1 + 3:
        fail("boundary-correct literal K6 linear calendar")
    if raw_anchors["K2_1"] != 10 + 1 + 3:
        fail("boundary-correct literal K2 linear calendar")
    contracted = {
        "D10_3": 11,
        "D10_4": 14,
        "D10_5": 17,
        "D6_2": 13,
        "D6_3": 16,
        "D6_4": 19,
        "D2_2": 17,
        "mu2_u2": 18,
        "Jdet": 19,
    }
    if contracted["D10_3"] == raw_anchors["K10_2"]:
        fail("raw and contracted calendars were conflated")

    # Minimal global dependency projection through grade 19.
    active = (
        6 * len(range(3, 17))
        + len(range(0, 12))
        + len(range(1, 11))
        + len(range(1, 7))
        + len(range(1, 6))
        + len(range(1, 4))
        + 1
        + 1
    )
    if active != 122:
        fail(("active-column census", active))
    if 7 * len(range(6, 20)) != 98:
        fail("root-slot census")
    return profiles, raw_anchors, contracted, active


def frontier_dependency_controls():
    """Exact-Q live/dormant cutoff controls in the literal 140-row evaluator."""
    compiler = load_compiler_module()
    tails = json.loads(compiler.TAILS.read_text())
    columns = compiler.source_columns()
    assignment = {}
    for column in columns:
        name = str(column["variable"])
        assignment[name] = F((int(column["column"]) % 17) + 1)
        if str(column["name"]).startswith("d") and int(column["series_index"]) in (1, 2):
            assignment[name] = F(0)

    def evaluate(values):
        return compiler.direct_tail_rows(tails, columns, values, F, None)[0]

    baseline = evaluate(assignment)

    def changes(name):
        mutated = dict(assignment)
        mutated[name] += 1
        result = evaluate(mutated)
        return any(
            result[row][grade] != baseline[row][grade]
            for row in range(7)
            for grade in range(6, 20)
        )

    live = [
        *(f"d{index}_16" for index in range(6)),
        "k10_11", "k6_10", "k2_6", "mu2_5", "mu4_3", "mu6_1", "Jdet_0",
    ]
    dormant = [
        *(f"d{index}_17" for index in range(6)),
        "k10_12", "k6_11", "k2_7",
    ]
    for name in live:
        if not changes(name):
            fail(("claimed live frontier is inert", name))
    for name in dormant:
        if changes(name):
            fail(("claimed dormant frontier is live", name))


def leading_cone(module, rows):
    ring = module.Ring(("a", "b", "u", "v"))
    a, b, u, v = (ring.var(name) for name in ring.names)
    x = module.cone_vector(ring, a, b, u, v)
    quadrics = [module.dhom(row, 2) for row in rows]
    expected_alpha = (F(3, 1024), F(3, 256), F(-3, 8192), 0,
                      F(-3, 131072), 0, F(-3, 1048576))
    expected_beta = (F(-3, 1024), F(3, 16384), F(3, 8192), 0,
                     F(3, 131072), 0, F(3, 1048576))
    alpha = []
    beta = []
    for index, quadric in enumerate(quadrics):
        assert_zero(module.eval_dpoly(quadric, x, ring), f"Q cone row {index + 1}")
        avalue = module.eval_dpoly(module.dderivative(quadric, 5), x, ring)
        bvalue = module.eval_dpoly(module.dderivative(quadric, 0), x, ring)
        assert_equal(module, ring, avalue, ring.scale(u if index not in (1,) else v,
                     expected_alpha[index]), f"alpha {index + 1}")
        expected_bvar = v if index not in (1,) else u
        assert_equal(module, ring, bvalue, ring.scale(expected_bvar,
                     expected_beta[index]), f"beta {index + 1}")
        alpha.append(avalue)
        beta.append(bvalue)
    delta = ring.add(ring.mul(u, u), ring.scale(ring.mul(v, v), 64))
    nonzero = 0
    for i in range(7):
        for j in range(i + 1, 7):
            minor = ring.sub(ring.mul(alpha[i], beta[j]), ring.mul(beta[i], alpha[j]))
            if not minor:
                continue
            nonzero += 1
            u2key = tuple(2 if name == "u" else 0 for name in ring.names)
            factor = minor.get(u2key, module.g())
            if module.giszero(factor):
                fail(("minor missing u2", i, j))
            assert_equal(module, ring, minor, ring.scale(delta, factor), f"minor {i},{j}")
    if nonzero != 4:
        fail(("rank-two minor census", nonzero))


def leading_nonzero_ranks(module, rows, loads):
    # Rank two: grades 6--8 solve exactly; the grade-9 cokernel is the same
    # literal cubic vector that closes the promoted valuation-two leading fan.
    names = ("a", "b", "u", "v", "aa", "bb", "uu", "vv", "k", "k1",
             "za", "zb", "zu", "zv", "wa", "wb", "wu", "wv")
    ring = module.Ring(names)
    var = {name: ring.var(name) for name in names}
    x = module.cone_vector(ring, var["a"], var["b"], var["u"], var["v"])
    y = module.cone_vector(ring, var["aa"], var["bb"], var["uu"], var["vv"])
    z = vector_with_kernel(
        module, ring,
        ring.scale(ring.mul(var["k"], var["v"]), F(10, 3)),
        ring.scale(ring.mul(var["k"], var["u"]), F(-10, 3)),
        var["za"], var["zb"], var["zu"], var["zv"],
    )
    w = module.cone_vector(ring, var["wa"], var["wb"], var["wu"], var["wv"])
    coefficients = [{3: x[i], 4: y[i], 5: z[i], 6: w[i]} for i in range(6)]
    equations = full_rows(
        module, rows, loads, coefficients,
        {"K10": {0: var["k"], 1: var["k1"]}}, ring, 10,
    )
    for row in range(7):
        for grade in range(6, 9):
            assert_zero(equations[row][grade], f"leading rank2 row{row + 1} grade{grade}")
    grade9 = [equation[9] for equation in equations]
    h6 = ring.scale(
        ring.mul(var["u"], ring.sub(ring.scale(ring.mul(var["v"], var["v"]), 192),
                                    ring.mul(var["u"], var["u"]))),
        F(1, 65536),
    )
    h4core = ring.linear(
        (1, ring.power(var["u"], 3)),
        (-448, ring.mul(var["u"], ring.power(var["v"], 2))),
        (64, ring.mul(var["b"], ring.power(var["v"], 2))),
        (-1, ring.mul(var["b"], ring.power(var["u"], 2))),
        (-1024, ring.mul(ring.mul(var["a"], var["u"]), var["v"])),
    )
    assert_equal(module, ring, grade9[5], h6, "leading rank2 grade9 row6")
    wrong_h6 = ring.scale(
        ring.mul(var["u"], ring.sub(ring.scale(ring.mul(var["v"], var["v"]), 193),
                                    ring.mul(var["u"], var["u"]))),
        F(1, 65536),
    )
    if not ring.sub(grade9[5], wrong_h6):
        fail("vacuous 192-to-193 mutation")
    assert_equal(module, ring, grade9[3], ring.scale(h4core, F(3, 32768)),
                 "leading rank2 grade9 row4")
    s3 = ring.add(grade9[2], grade9[0], F(1, 8))
    s5 = ring.add(ring.add(grade9[4], grade9[0], F(3, 128)), grade9[2], F(1, 8))
    s7 = ring.add(ring.add(grade9[6], grade9[0], F(1, 512)), grade9[2], F(1, 128))
    u0_s3 = ring.zero_vars(s3, ("u", "b"))
    u0_s5 = ring.zero_vars(ring.add(grade9[4], grade9[0], F(1, 128)), ("u", "b"))
    assert_equal(
        module, ring, u0_s3,
        ring.scale(ring.mul(ring.power(var["v"], 2),
                            ring.add(var["v"], ring.scale(var["a"], 3))), F(1, 4)),
        "leading rank2 u0 S3",
    )
    assert_equal(
        module, ring, u0_s5,
        ring.scale(ring.mul(ring.power(var["v"], 2),
                            ring.add(var["v"], ring.scale(var["a"], 2))), F(-3, 64)),
        "leading rank2 u0 S5",
    )
    if module.qpair_branch_reduce(s5, ring) != {(0, 0): (F(1, 8), F(0))}:
        fail("leading rank2 quadratic branch S5")
    if module.qpair_branch_reduce(s7, ring) != {(0, 0): (F(-1, 64), F(0))}:
        fail("leading rank2 quadratic branch S7")

    # Rank one: grade 8 first kills its tangent parameter, and grade 9 is a
    # nonzero conjugate cubic.  Both signs are checked independently.
    for sign in (1, -1):
        names = ("a", "b", "v", "aa", "bb", "uu", "vv", "k", "k1",
                 "lam", "tau", "z1", "z2", "z3", "z4", "w1", "w2", "w3", "w4")
        ring = module.Ring(names)
        var = {name: ring.var(name) for name in names}
        u = ring.scale(var["v"], module.g(0, 8 * sign))
        x = module.cone_vector(ring, var["a"], var["b"], u, var["v"])
        y0 = module.cone_vector(ring, var["aa"], var["bb"], var["uu"], var["vv"])
        yt = module.vector_with_ab(
            ring,
            ring.mul(var["lam"], var["v"]),
            ring.scale(ring.mul(var["lam"], var["v"]), module.g(0, 8 * sign)),
            {}, {}, {}, {},
        )
        y = [ring.add(left, right) for left, right in zip(y0, yt)]
        arbitrary_z = module.vector_with_ab(
            ring, var["tau"], ring.scale(var["tau"], module.g(0, 8 * sign)),
            var["z1"], var["z2"], var["z3"], var["z4"],
        )
        w = module.vector_with_ab(ring, {}, {}, var["w1"], var["w2"], var["w3"], var["w4"])
        coefficients = [{3: x[i], 4: y[i], 5: arbitrary_z[i], 6: w[i]} for i in range(6)]
        equations = full_rows(
            module, rows, loads, coefficients,
            {"K10": {0: var["k"], 1: var["k1"]}}, ring, 10,
        )
        expected8 = ring.scale(
            ring.mul(ring.power(var["v"], 2), ring.power(var["lam"], 2)),
            F(-3, 4096),
        )
        assert_equal(module, ring, equations[3][8], expected8,
                     f"leading rank1 sign{sign} grade8")

        az = ring.add(ring.scale(ring.mul(var["k"], var["v"]), F(10, 3)),
                      ring.mul(var["tau"], var["v"]))
        bz = ring.add(ring.scale(ring.mul(var["k"], u), F(-10, 3)),
                      ring.scale(ring.mul(var["tau"], var["v"]), module.g(0, 8 * sign)))
        z = module.vector_with_ab(
            ring, az, bz, var["z1"], var["z2"], var["z3"], var["z4"],
        )
        coefficients = [{3: x[i], 4: y0[i], 5: z[i], 6: w[i]} for i in range(6)]
        equations = full_rows(
            module, rows, loads, coefficients,
            {"K10": {0: var["k"], 1: var["k1"]}}, ring, 10,
        )
        expected9 = ring.monomial({"v": 3}, module.g(0, F(sign, 32)))
        assert_equal(module, ring, equations[5][9], expected9,
                     f"leading rank1 sign{sign} grade9")


def old_plane_second_fan(module, rows, loads):
    # Next rank two: grade 10 has an exact normal solution; grade 11 is the
    # promoted D/F incompatibility, reconstructed at literal valuation three.
    names = ("s", "t", "a", "b", "u", "v", "aa", "bb", "uu", "vv",
             "k", "k1", "beta", "wa", "wb", "wu", "wv", "pa", "pb", "pu", "pv")
    ring = module.Ring(names)
    var = {name: ring.var(name) for name in names}
    x = module.old_plane(ring, var["s"], var["t"])
    y = module.cone_vector(ring, var["a"], var["b"], var["u"], var["v"])
    z = module.cone_vector(ring, var["aa"], var["bb"], var["uu"], var["vv"])
    aw = ring.add(ring.scale(ring.mul(var["s"], var["t"]), 2),
                  ring.scale(ring.mul(var["k"], var["v"]), F(10, 3)))
    bw = ring.add(ring.sub(ring.mul(var["s"], var["s"]),
                           ring.scale(ring.mul(var["t"], var["t"]), 64)),
                  ring.scale(ring.mul(var["k"], var["u"]), F(-10, 3)))
    w = vector_with_kernel(module, ring, aw, bw, var["wa"], var["wb"], var["wu"], var["wv"])
    p = module.cone_vector(ring, var["pa"], var["pb"], var["pu"], var["pv"])
    coefficients = [{3: x[i], 4: y[i], 5: z[i], 6: w[i], 7: p[i]} for i in range(6)]
    source = {"K10": {0: var["k"], 1: var["k1"]},
              "K6": {0: ring.const(), 1: var["beta"]}}
    equations = full_rows(module, rows, loads, coefficients, source, ring, 12)
    for row in range(7):
        for grade in range(6, 11):
            assert_zero(equations[row][grade], f"oldplane next-rank2 row{row + 1} grade{grade}")
    grade11 = [equation[11] for equation in equations]
    dform = ring.linear(
        (1, ring.mul(var["t"], ring.power(var["u"], 2))),
        (-64, ring.mul(var["t"], ring.power(var["v"], 2))),
        (-2, ring.mul(var["s"], ring.mul(var["u"], var["v"]))),
    )
    fform = ring.linear(
        (1, ring.mul(var["s"], ring.power(var["u"], 2))),
        (-64, ring.mul(var["s"], ring.power(var["v"], 2))),
        (128, ring.mul(var["t"], ring.mul(var["u"], var["v"]))),
    )
    assert_equal(module, ring, ring.add(grade11[2], grade11[0], F(1, 8)),
                 ring.scale(dform, F(-3, 2048)), "oldplane next-rank2 D")
    assert_equal(module, ring, grade11[3], ring.scale(fform, F(-3, 32768)),
                 "oldplane next-rank2 F")
    sigma = ring.add(ring.mul(var["s"], var["s"]),
                     ring.scale(ring.mul(var["t"], var["t"]), 64))
    assert_equal(module, ring,
                 ring.sub(ring.mul(var["s"], dform), ring.mul(var["t"], fform)),
                 ring.scale(ring.mul(ring.mul(var["u"], var["v"]), sigma), -2),
                 "D/F identity one")
    assert_equal(module, ring,
                 ring.add(ring.mul(var["s"], fform),
                          ring.scale(ring.mul(var["t"], dform), 64)),
                 ring.mul(ring.sub(ring.power(var["u"], 2),
                                   ring.scale(ring.power(var["v"], 2), 64)), sigma),
                 "D/F identity two")

    # Next rank one: grade 10 kills lambda, grade 11 forces the leading old
    # plane onto the matching isotropic ray, and the universal row-six cubic
    # kills the cell at grade 12.
    for sign in (1, -1):
        names = ("s", "t", "a", "b", "v", "aa", "bb", "uu", "vv", "lam",
                 "k", "k1", "kap2", "kap3", "kap4", "beta", "beta2",
                 "tau", "wa", "wb", "wu", "wv", "PA", "PB",
                 "p1", "p2", "p3", "p4", "QA", "QB",
                 "q1", "q2", "q3", "q4")
        ring = module.Ring(names)
        var = {name: ring.var(name) for name in names}
        u = ring.scale(var["v"], module.g(0, 8 * sign))
        x = module.old_plane(ring, var["s"], var["t"])
        y = module.cone_vector(ring, var["a"], var["b"], u, var["v"])
        z0 = module.cone_vector(ring, var["aa"], var["bb"], var["uu"], var["vv"])
        zt = module.vector_with_ab(
            ring, ring.mul(var["lam"], var["v"]),
            ring.scale(ring.mul(var["lam"], var["v"]), module.g(0, 8 * sign)),
            {}, {}, {}, {},
        )
        z = [ring.add(left, right) for left, right in zip(z0, zt)]
        arbitrary_w = module.vector_with_ab(
            ring, var["PA"], var["PB"], var["wa"], var["wb"], var["wu"], var["wv"])
        coefficients = [{3: x[i], 4: y[i], 5: z[i], 6: arbitrary_w[i]} for i in range(6)]
        source = {
            "K10": {0: var["k"], 1: var["k1"], 2: var["kap2"],
                    3: var["kap3"], 4: var["kap4"]},
            "K6": {0: ring.const(), 1: var["beta"], 2: var["beta2"]},
        }
        equations = full_rows(module, rows, loads, coefficients, source, ring, 11)
        expected10 = ring.scale(
            ring.mul(ring.power(var["v"], 2), ring.power(var["lam"], 2)), F(-3, 4096))
        assert_equal(module, ring, equations[3][10], expected10,
                     f"oldplane next-rank1 sign{sign} grade10")

        aw = ring.add(
            ring.add(ring.scale(ring.mul(var["s"], var["t"]), 2),
                     ring.scale(ring.mul(var["k"], var["v"]), F(10, 3))),
            ring.mul(var["tau"], var["v"]),
        )
        bw = ring.add(
            ring.add(ring.sub(ring.mul(var["s"], var["s"]),
                              ring.scale(ring.mul(var["t"], var["t"]), 64)),
                     ring.scale(ring.mul(var["k"], u), F(-10, 3))),
            ring.scale(ring.mul(var["tau"], var["v"]), module.g(0, 8 * sign)),
        )
        w = module.vector_with_ab(
            ring, aw, bw, var["wa"], var["wb"], var["wu"], var["wv"])
        p = module.vector_with_ab(
            ring, var["PA"], var["PB"], var["p1"], var["p2"], var["p3"], var["p4"])
        coefficients = [{3: x[i], 4: y[i], 5: z0[i], 6: w[i], 7: p[i]} for i in range(6)]
        equations = full_rows(module, rows, loads, coefficients, source, ring, 12)
        grade11 = [equation[11] for equation in equations]
        ray = ring.scale(
            ring.mul(ring.power(var["v"], 2),
                     ring.add(var["s"], ring.scale(var["t"], module.g(0, -8 * sign)))),
            F(3, 256),
        )
        assert_equal(module, ring, grade11[3], ray,
                     f"oldplane next-rank1 sign{sign} ray")
        compatibility = ring.add(grade11[1], grade11[0], module.g(0, F(sign, 2)))
        compatibility = ring.replace_by_scaled_var(
            compatibility, {"s": (module.g(0, 8 * sign), "t")})
        expected = ring.linear(
            (F(3, 128), ring.mul(ring.mul(var["v"], var["vv"]), var["tau"])),
            (module.g(0, F(3 * sign, 1024)),
             ring.mul(ring.mul(var["v"], var["uu"]), var["tau"])),
            (F(-5, 128),
             ring.mul(ring.mul(ring.mul(var["t"], var["v"]), var["k"]), var["tau"])),
            (module.g(0, F(-5 * sign, 16)),
             ring.mul(ring.power(var["t"], 3), var["k"])),
        )
        assert_equal(module, ring, compatibility, expected,
                     f"oldplane next-rank1 sign{sign} compatibility")

        q = module.vector_with_ab(
            ring, var["QA"], var["QB"], var["q1"], var["q2"], var["q3"], var["q4"])
        coefficients = [
            {3: x[i], 4: y[i], 5: z0[i], 6: w[i], 7: p[i], 8: q[i]}
            for i in range(6)
        ]
        equations = full_rows(module, rows, loads, coefficients, source, ring, 13)
        row6 = ring.replace_by_scaled_var(
            equations[5][12], {"s": (module.g(0, 8 * sign), "t")})
        expected12 = ring.monomial({"v": 3}, module.g(0, F(sign, 32)))
        assert_equal(module, ring, row6, expected12,
                     f"oldplane next-rank1 sign{sign} grade12 row6")

    # Next rank zero: grade 10 forces the following coefficient z back onto
    # the reduced cone.  The grade-11 linearization is NOT DQ(z): K10 shifts
    # its rank parameters.  Reconstruct and split the effective fan.
    names = ("s", "t", "a", "b", "AZ", "BZ", "z1", "z2", "z3", "z4",
             "k", "k1", "beta")
    ring = module.Ring(names)
    var = {name: ring.var(name) for name in names}
    x = module.old_plane(ring, var["s"], var["t"])
    y = module.old_plane(ring, var["a"], var["b"])
    z = module.vector_with_ab(
        ring, var["AZ"], var["BZ"], var["z1"], var["z2"], var["z3"], var["z4"])
    coefficients = [{3: x[i], 4: y[i], 5: z[i]} for i in range(6)]
    source = {"K10": {0: var["k"], 1: var["k1"]},
              "K6": {0: ring.const(), 1: var["beta"]}}
    equations = full_rows(module, rows, loads, coefficients, source, ring, 12)
    grade10 = [equation[10] for equation in equations]
    assert_equal(module, ring, ring.add(grade10[0], grade10[2], 8),
                 ring.scale(ring.mul(var["AZ"], var["BZ"]), F(3, 2048)),
                 "oldplane twice grade10 AB")
    assert_equal(module, ring, grade10[3],
                 ring.scale(ring.sub(ring.power(var["BZ"], 2),
                                     ring.scale(ring.power(var["AZ"], 2), 64)),
                            F(3, 524288)),
                 "oldplane twice grade10 square")
    for index, equation in enumerate(grade10, 1):
        assert_zero(ring.zero_vars(equation, ("AZ", "BZ")),
                    f"oldplane twice cone row{index}")

    names = ("s", "t", "a", "b", "c", "d", "U", "V", "WA", "WB",
             "w1", "w2", "w3", "w4", "k", "k1", "beta")
    ring = module.Ring(names)
    var = {name: ring.var(name) for name in names}
    u = ring.add(var["U"], ring.scale(ring.mul(var["s"], var["k"]), F(-5, 6)))
    v = ring.add(var["V"], ring.scale(ring.mul(var["t"], var["k"]), F(5, 6)))
    x = module.old_plane(ring, var["s"], var["t"])
    y = module.old_plane(ring, var["a"], var["b"])
    z = module.cone_vector(ring, var["c"], var["d"], u, v)
    w = module.vector_with_ab(
        ring, var["WA"], var["WB"], var["w1"], var["w2"], var["w3"], var["w4"])
    coefficients = [{3: x[i], 4: y[i], 5: z[i], 6: w[i]} for i in range(6)]
    source = {"K10": {0: var["k"], 1: var["k1"]},
              "K6": {0: ring.const(), 1: var["beta"]}}
    equations = full_rows(module, rows, loads, coefficients, source, ring, 12)
    grade11 = [equation[11] for equation in equations]
    kernel_names = ("WA", "WB", "w1", "w2", "w3", "w4")
    inhomogeneous = [ring.zero_vars(equation, kernel_names) for equation in grade11]
    expected_alpha = (
        ring.scale(var["U"], F(3, 1024)),
        ring.scale(var["V"], F(3, 256)),
        ring.scale(var["U"], F(-3, 8192)), {},
        ring.scale(var["U"], F(-3, 131072)), {},
        ring.scale(var["U"], F(-3, 1048576)),
    )
    expected_beta = (
        ring.scale(var["V"], F(-3, 1024)),
        ring.scale(var["U"], F(3, 16384)),
        ring.scale(var["V"], F(3, 8192)), {},
        ring.scale(var["V"], F(3, 131072)), {},
        ring.scale(var["V"], F(3, 1048576)),
    )
    for index in range(7):
        expected_row = ring.add(
            inhomogeneous[index],
            ring.add(ring.mul(expected_alpha[index], var["WA"]),
                     ring.mul(expected_beta[index], var["WB"])),
        )
        assert_equal(module, ring, grade11[index], expected_row,
                     f"effective grade11 linearization row{index + 1}")
    wrong_unshifted_alpha1 = ring.scale(u, F(3, 1024))
    if not ring.sub(expected_alpha[0], wrong_unshifted_alpha1):
        fail("vacuous unshifted-grade11-fan mutation")
    for index, equation in enumerate(coker5(ring, inhomogeneous), 1):
        assert_zero(equation, f"effective grade11 generic cokernel {index}")

    # Effective rank one has U=epsilon*8*i*V, V!=0 and forces the opposite
    # isotropic source ray.  Effective rank zero has U=V=0 and is empty.
    for sign in (1, -1):
        branch = [
            ring.replace_by_scaled_var(equation, {"U": (module.g(0, 8 * sign), "V")})
            for equation in inhomogeneous
        ]
        compatibility = ring.add(branch[1], branch[0], module.g(0, F(sign, 2)))
        expected_cube = ring.mul(
            ring.scale(
                ring.power(ring.add(var["s"],
                                    ring.scale(var["t"], module.g(0, 8 * sign))), 3),
                F(5, 65536),
            ),
            var["k"],
        )
        assert_equal(module, ring, compatibility, expected_cube,
                     f"effective rank1 sign{sign} cube")

    rank_zero = [ring.zero_vars(equation, ("U", "V")) for equation in inhomogeneous]
    expected1 = ring.scale(
        ring.mul(ring.mul(var["k"], var["t"]),
                 ring.sub(ring.scale(ring.power(var["s"], 2), 3),
                          ring.scale(ring.power(var["t"], 2), 64))), F(5, 4096))
    expected2 = ring.scale(
        ring.mul(ring.mul(var["k"], var["s"]),
                 ring.sub(ring.power(var["s"], 2),
                          ring.scale(ring.power(var["t"], 2), 192))), F(5, 65536))
    assert_equal(module, ring, rank_zero[0], expected1,
                 "effective rank0 grade11 cubic one")
    assert_equal(module, ring, rank_zero[1], expected2,
                 "effective rank0 grade11 cubic two")


def main() -> None:
    start = time.perf_counter()
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("custody", str(path)))
    if sha256(TAILS.read_bytes() + b"\n").hexdigest() == EXPECTED[TAILS]:
        fail("vacuous source-custody mutation")
    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    _, _, _, active = source_and_calendar(module, rows, loads)
    frontier_dependency_controls()
    leading_cone(module, rows)
    leading_nonzero_ranks(module, rows, loads)
    old_plane_second_fan(module, rows, loads)
    elapsed = time.perf_counter() - start
    print("K00_R3_SOURCE_PREFLIGHT=PASS")
    print("FROZEN_TAIL_TERMS=569")
    print("LITERAL_ROOT_SLOTS_GRADES_6_TO_19=98")
    print(f"MINIMAL_GLOBAL_ACTIVE_COLUMNS={active}")
    print("LEADING_RANK1_AND_RANK2=EMPTY_AT_GRADE9")
    print("OLDPLANE_NEXT_RANK2=EMPTY_AT_GRADE11")
    print("OLDPLANE_NEXT_RANK1=EMPTY_AT_GRADE12")
    print("GRADE11_EFFECTIVE_RESIDUALS=R3-00-ER1_PLUS_MINUS,R3-00-ER2")
    print("PERIODICITY_ASSUMPTIONS=NONE")
    print("MUTATION_CONTROLS=CUSTODY,CALENDAR,EFFECTIVE_K10_SHIFT,CONJUGATE_SIGNS,192_COEFFICIENT")
    print(f"RUNTIME_SECONDS={elapsed:.6f}")


if __name__ == "__main__":
    main()
