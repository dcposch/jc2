#!/usr/bin/env python3
"""Exact remaining-fan replay for normalized V20R2 valuation three.

This is a desk-scale, standard-library-only certificate checker.  It rebuilds
the seven literal K00 rows from the byte-pinned 569-tail source, starts from
the twice-old-plane valuation-three prefix, solves the effective grade-11
normal block, and proves that every surviving effective-rank-one or
effective-rank-two branch is empty at grade 12.

No conclusion is borrowed from valuation two, four, or five.  The imported
valuation-two file is used only as a byte-pinned sparse exact-arithmetic
library and tail parser.  This program writes no files and invokes no CAS,
network service, git command, or subprocess.
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
ENGINE = ROOT / "xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py"
BASIS = "31777ce90994a106aade85064c0d868e32863f94"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
}


def fail(message: object) -> None:
    raise RuntimeError(message)


def need(condition: bool, message: object) -> None:
    if not condition:
        fail(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_r3_exact_library", ENGINE)
    if spec is None or spec.loader is None:
        fail("cannot import pinned exact library")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def full_rows(module, rows, loads, coefficients, source, ring, truncation):
    """Literal R+K10*A10+K6*A6+K2*A2 rows, with raw Lambda shifts."""
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


def vector_with_kernel(module, ring, aval, bval, a, b, u, v):
    return module.vector_with_ab(
        ring,
        aval,
        bval,
        a,
        b,
        ring.add(ring.scale(a, 8), v),
        ring.sub(b, u),
    )


def coker5(ring, vector):
    """Five universal left-kernel rows of the effective normal block."""
    return (
        vector[3],
        vector[5],
        ring.add(vector[2], vector[0], F(1, 8)),
        ring.add(vector[4], vector[0], F(1, 128)),
        ring.add(vector[6], vector[0], F(1, 1024)),
    )


def assert_zero(poly, label):
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def assert_equal(module, ring, left, right, label):
    module.assert_equal(left, right, ring, label)


def canonical_polys(ring, labelled):
    """Public deterministic sparse serialization for certificate hashing."""
    payload = {"variables": list(ring.names), "polynomials": []}
    for label, poly in labelled:
        terms = []
        for exponents, coefficient in sorted(poly.items()):
            real, imag = coefficient
            terms.append(
                {
                    "exponents": list(exponents),
                    "coefficient": {
                        "real": [real.numerator, real.denominator],
                        "imag": [imag.numerator, imag.denominator],
                    },
                }
            )
        payload["polynomials"].append({"label": label, "terms": terms})
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return payload, sha256(encoded).hexdigest()


def qv_normal_form(module, ring, poly):
    """Normal form modulo qV*V-1 (leading monomial qV*V)."""
    iv = ring.index["V"]
    iq = ring.index["qV"]
    out = {}
    for key, coefficient in poly.items():
        reduced = list(key)
        common = min(reduced[iv], reduced[iq])
        reduced[iv] -= common
        reduced[iq] -= common
        target = tuple(reduced)
        out[target] = module.gadd(out.get(target, module.g()), coefficient)
    return ring.clean(out)


def qdelta_normal_form(module, ring, poly):
    """Normal form modulo qD*(U^2+64*V^2)-1.

    The leading monomial is qD*U^2.  Each replacement strictly lowers the U
    exponent, so this small exact reducer terminates without a CAS.
    """
    iu = ring.index["U"]
    iv = ring.index["V"]
    iq = ring.index["qD"]
    pending = dict(poly)
    out = {}
    while pending:
        key, coefficient = pending.popitem()
        if key[iq] and key[iu] >= 2:
            first = list(key)
            first[iq] -= 1
            first[iu] -= 2
            first = tuple(first)
            pending[first] = module.gadd(
                pending.get(first, module.g()), coefficient
            )
            second = list(key)
            second[iu] -= 2
            second[iv] += 2
            second = tuple(second)
            pending[second] = module.gadd(
                pending.get(second, module.g()),
                module.gmul(module.g(-64), coefficient),
            )
        else:
            out[key] = module.gadd(out.get(key, module.g()), coefficient)
    return ring.clean(out)


def coefficient_in(module, ring, poly, name, exponent):
    index = ring.index[name]
    out = {}
    for key, coefficient in poly.items():
        if key[index] == exponent:
            reduced = list(key)
            reduced[index] = 0
            reduced = tuple(reduced)
            out[reduced] = module.gadd(out.get(reduced, module.g()), coefficient)
    return ring.clean(out)


def source_series(ring, var):
    # Every literal source column that can reach a row by grade 12 is present.
    return {
        "K10": {
            0: var["k"],
            1: var["k1"],
            2: var["k2"],
            3: var["k3"],
            4: var["k4"],
        },
        # k6[0] is boundary-fixed zero before any solve or saturation.
        "K6": {0: {}, 1: var["b1"], 2: var["b2"], 3: var["b3"]},
        # k2[0] is boundary-fixed zero; no free K2 coefficient reaches G12.
        "K2": {0: {}},
    }


def er1_branch(module, rows, loads, sign):
    names = (
        "t", "a", "b", "c", "d", "V", "qV", "eta", "T",
        "w1", "w2", "w3", "w4", "PA", "PB", "p1", "p2", "p3", "p4",
        "k", "k1", "k2", "k3", "k4", "b1", "b2", "b3",
    )
    ring = module.Ring(names)
    var = {name: ring.var(name) for name in names}
    j = module.g(0, sign)

    # Grade-11 effective rank-one branch and its forced opposite source ray.
    source_s = ring.scale(var["t"], module.g(0, -8 * sign))
    effective_u = ring.scale(var["V"], module.g(0, 8 * sign))
    raw_u = ring.add(
        effective_u,
        ring.scale(ring.mul(source_s, var["k"]), F(-5, 6)),
    )
    raw_v = ring.add(
        var["V"], ring.scale(ring.mul(var["t"], var["k"]), F(5, 6))
    )
    x = module.old_plane(ring, source_s, var["t"])
    y = module.old_plane(ring, var["a"], var["b"])
    z = module.cone_vector(ring, var["c"], var["d"], raw_u, raw_v)
    source = source_series(ring, var)

    # Recover the grade-11 inhomogeneity from a fresh literal expansion.
    arbitrary_w = module.vector_with_ab(
        ring, var["T"], var["PB"], var["w1"], var["w2"], var["w3"], var["w4"]
    )
    coefficients = [
        {3: x[i], 4: y[i], 5: z[i], 6: arbitrary_w[i]} for i in range(6)
    ]
    raw = full_rows(module, rows, loads, coefficients, source, ring, 13)
    h1 = ring.zero_vars(
        raw[0][11], ("T", "PB", "w1", "w2", "w3", "w4")
    )
    expected_h1 = ring.linear(
        (F(-5, 16), ring.mul(ring.power(var["t"], 3), var["k"])),
        (F(-3, 4), ring.mul(ring.power(var["t"], 2), var["V"])),
    )
    assert_equal(module, ring, h1, expected_h1, f"ER1{sign} grade11 h1")

    # L=8*sign*i*A(w)-B(w), solved on D(V) with qV=V^{-1}.
    image_coordinate = ring.scale(ring.mul(var["qV"], h1), F(-1024, 3))
    wa = var["T"]
    wb = ring.sub(ring.scale(wa, module.g(0, 8 * sign)), image_coordinate)
    w = module.vector_with_ab(
        ring, wa, wb, var["w1"], var["w2"], var["w3"], var["w4"]
    )
    p = module.vector_with_ab(
        ring, var["PA"], var["PB"], var["p1"], var["p2"], var["p3"], var["p4"]
    )
    coefficients = [
        {3: x[i], 4: y[i], 5: z[i], 6: w[i], 7: p[i]} for i in range(6)
    ]
    equations = full_rows(module, rows, loads, coefficients, source, ring, 13)
    for row in range(7):
        for grade in range(6, 11):
            assert_zero(equations[row][grade], f"ER1{sign} row{row + 1} G{grade}")
        assert_zero(
            qv_normal_form(module, ring, equations[row][11]),
            f"ER1{sign} solved row{row + 1} G11",
        )

    grade12 = [equation[12] for equation in equations]
    cokernel = [qv_normal_form(module, ring, value) for value in coker5(ring, grade12)]
    cokernel.append(
        qv_normal_form(
            module,
            ring,
            ring.add(grade12[1], grade12[0], module.g(0, F(sign, 2))),
        )
    )
    c1, c2, c3, c4, c5, _ = cokernel
    assert_zero(c2, f"ER1{sign} G12 row6")
    assert_equal(module, ring, c4, ring.scale(c3, F(-1, 8)), f"ER1{sign} C4")
    assert_equal(module, ring, c5, ring.scale(c3, F(-1, 128)), f"ER1{sign} C5")

    # A two-row unit obstruction in the localization D(k*t*V).
    combination = ring.add(
        ring.scale(c1, 12288), ring.scale(c3, module.g(0, -6144 * sign))
    )
    obstruction = ring.scale(
        ring.mul(
            ring.mul(ring.power(var["t"], 6), ring.power(var["k"], 2)),
            ring.power(var["qV"], 2),
        ),
        800,
    )
    assert_equal(
        module, ring, combination, obstruction, f"ER1{sign} grade12 unit identity"
    )

    # Explicit Bezout certificate with A=eta*k*t*V=1 and B=qV*V=1.
    aa = ring.mul(
        ring.mul(ring.mul(var["eta"], var["k"]), var["t"]), var["V"]
    )
    bb = ring.mul(var["qV"], var["V"])
    multiplier = ring.scale(
        ring.mul(
            ring.mul(ring.power(var["eta"], 6), ring.power(var["k"], 4)),
            ring.power(var["V"], 8),
        ),
        F(1, 800),
    )
    geometric = {}
    for exponent in range(6):
        geometric = ring.add(geometric, ring.power(aa, exponent))
    bezout = ring.mul(multiplier, combination)
    bezout = ring.add(
        bezout,
        ring.mul(ring.sub(aa, ring.const(1)), ring.mul(geometric, ring.power(bb, 2))),
        -1,
    )
    bezout = ring.add(
        bezout,
        ring.mul(ring.sub(bb, ring.const(1)), ring.add(bb, ring.const(1))),
        -1,
    )
    assert_equal(module, ring, bezout, ring.const(1), f"ER1{sign} Bezout unit")

    wrong = ring.add(
        ring.scale(c1, 12288), ring.scale(c3, module.g(0, -6143 * sign))
    )
    need(ring.sub(wrong, obstruction) != {}, f"ER1{sign} mutation survived")
    _, certificate_hash = canonical_polys(
        ring,
        [(f"ER1_{sign}_C{index}", value) for index, value in enumerate(cokernel, 1)]
        + [(f"ER1_{sign}_UNIT", combination)],
    )
    return certificate_hash


def er2_branch(module, rows, loads):
    names = (
        "s", "t", "a", "b", "c", "d", "U", "V", "qD",
        "w1", "w2", "w3", "w4", "PA", "PB", "p1", "p2", "p3", "p4",
        "k", "k1", "k2", "k3", "k4", "b1", "b2", "b3",
    )
    ring = module.Ring(names)
    var = {name: ring.var(name) for name in names}
    delta = ring.add(ring.power(var["U"], 2), ring.scale(ring.power(var["V"], 2), 64))
    raw_u = ring.add(
        var["U"], ring.scale(ring.mul(var["s"], var["k"]), F(-5, 6))
    )
    raw_v = ring.add(
        var["V"], ring.scale(ring.mul(var["t"], var["k"]), F(5, 6))
    )
    x = module.old_plane(ring, var["s"], var["t"])
    y = module.old_plane(ring, var["a"], var["b"])
    z = module.cone_vector(ring, var["c"], var["d"], raw_u, raw_v)
    source = source_series(ring, var)

    zero_normal_w = module.vector_with_ab(
        ring, {}, {}, var["w1"], var["w2"], var["w3"], var["w4"]
    )
    coefficients = [
        {3: x[i], 4: y[i], 5: z[i], 6: zero_normal_w[i]} for i in range(6)
    ]
    raw = full_rows(module, rows, loads, coefficients, source, ring, 13)
    h1, h2 = raw[0][11], raw[1][11]
    expected_h1 = ring.linear(
        (F(15, 4096), ring.mul(ring.mul(ring.power(var["s"], 2), var["t"]), var["k"])),
        (F(3, 1024), ring.mul(ring.power(var["s"], 2), var["V"])),
        (F(-3, 512), ring.mul(ring.mul(var["s"], var["t"]), var["U"])),
        (F(-5, 64), ring.mul(ring.power(var["t"], 3), var["k"])),
        (F(-3, 16), ring.mul(ring.power(var["t"], 2), var["V"])),
    )
    expected_h2 = ring.linear(
        (F(5, 65536), ring.mul(ring.power(var["s"], 3), var["k"])),
        (F(-3, 16384), ring.mul(ring.power(var["s"], 2), var["U"])),
        (F(-15, 1024), ring.mul(ring.mul(var["s"], ring.power(var["t"], 2)), var["k"])),
        (F(-3, 128), ring.mul(ring.mul(var["s"], var["t"]), var["V"])),
        (F(3, 256), ring.mul(ring.power(var["t"], 2), var["U"])),
    )
    assert_equal(module, ring, h1, expected_h1, "ER2 grade11 h1")
    assert_equal(module, ring, h2, expected_h2, "ER2 grade11 h2")
    for index, value in enumerate(coker5(ring, [raw[row][11] for row in range(7)]), 1):
        assert_zero(value, f"ER2 grade11 inhomogeneous coker {index}")

    # Exact inverse of [[U,-V],[64V,U]] on D(Delta).
    r1 = ring.scale(h1, F(-1024, 3))
    r2 = ring.scale(h2, F(-16384, 3))
    wa = ring.mul(
        var["qD"], ring.add(ring.mul(var["U"], r1), ring.mul(var["V"], r2))
    )
    wb = ring.mul(
        var["qD"],
        ring.add(ring.scale(ring.mul(var["V"], r1), -64), ring.mul(var["U"], r2)),
    )
    w = module.vector_with_ab(
        ring, wa, wb, var["w1"], var["w2"], var["w3"], var["w4"]
    )
    p = module.vector_with_ab(
        ring, var["PA"], var["PB"], var["p1"], var["p2"], var["p3"], var["p4"]
    )
    coefficients = [
        {3: x[i], 4: y[i], 5: z[i], 6: w[i], 7: p[i]} for i in range(6)
    ]
    equations = full_rows(module, rows, loads, coefficients, source, ring, 13)
    for row in range(7):
        for grade in range(6, 11):
            assert_zero(equations[row][grade], f"ER2 row{row + 1} G{grade}")
        assert_zero(
            qdelta_normal_form(module, ring, equations[row][11]),
            f"ER2 solved row{row + 1} G11",
        )

    cokernel = list(coker5(ring, [equation[12] for equation in equations]))
    assert_zero(cokernel[1], "ER2 G12 row6")
    assert_equal(module, ring, cokernel[3], ring.scale(cokernel[2], F(-1, 8)), "ER2 C4")
    assert_equal(module, ring, cokernel[4], ring.scale(cokernel[2], F(-1, 128)), "ER2 C5")
    for index, value in enumerate(cokernel, 1):
        need(
            max((key[ring.index["qD"]] for key in value), default=0) <= 2,
            ("unexpected qD degree", index),
        )

    def denominator_clear(value, denominator=delta):
        # Delta^2 * C(qD=1/Delta), with exact coefficient extraction.
        out = {}
        for exponent in range(3):
            part = coefficient_in(module, ring, value, "qD", exponent)
            out = ring.add(out, ring.mul(part, ring.power(denominator, 2 - exponent)))
        return out

    n1 = denominator_clear(cokernel[0])
    n3 = denominator_clear(cokernel[2])
    need(len(n1) == 11 and len(n3) == 10, ("cleared support census", len(n1), len(n3)))
    allowed = {"s", "t", "U", "V", "k"}
    for label, value in (("N1", n1), ("N3", n3)):
        for name in ring.names:
            if name not in allowed and ring.depends_on(value, name):
                fail((label, "unexpected dependency", name))

    def binary_coeff(value, u_degree, v_degree):
        iu, iv = ring.index["U"], ring.index["V"]
        out = {}
        for key, coefficient in value.items():
            if key[iu] == u_degree and key[iv] == v_degree:
                reduced = list(key)
                reduced[iu] = reduced[iv] = 0
                reduced = tuple(reduced)
                out[reduced] = module.gadd(out.get(reduced, module.g()), coefficient)
        return ring.clean(out)

    aa, bb, cc = (binary_coeff(n1, 2, 0), binary_coeff(n1, 1, 1), binary_coeff(n1, 0, 2))
    dd, ee, ff = (binary_coeff(n3, 2, 0), binary_coeff(n3, 1, 1), binary_coeff(n3, 0, 2))
    # Resultant of A U^2+B UV+C V^2 and D U^2+E UV+F V^2.
    resultant = ring.sub(
        ring.power(ring.sub(ring.mul(aa, ff), ring.mul(cc, dd)), 2),
        ring.mul(
            ring.sub(ring.mul(aa, ee), ring.mul(bb, dd)),
            ring.sub(ring.mul(bb, ff), ring.mul(cc, ee)),
        ),
    )
    sigma = ring.add(ring.power(var["s"], 2), ring.scale(ring.power(var["t"], 2), 64))
    expected_resultant = ring.scale(
        ring.mul(ring.power(var["k"], 8), ring.power(sigma, 12)),
        F(-(5**8), (2**76) * (3**4)),
    )
    assert_equal(module, ring, resultant, expected_resultant, "ER2 binary resultant")

    # The two Q(i) source rays both force the corresponding Delta factor.
    ray_records = []
    for sign in (1, -1):
        ray_n1 = ring.replace_by_scaled_var(
            n1, {"s": (module.g(0, 8 * sign), "t")}
        )
        ray_n3 = ring.replace_by_scaled_var(
            n3, {"s": (module.g(0, 8 * sign), "t")}
        )
        linear = ring.add(var["U"], ring.scale(var["V"], module.g(0, 8 * sign)))
        common = ring.mul(
            ring.mul(ring.power(var["t"], 6), ring.power(var["k"], 2)),
            ring.power(linear, 2),
        )
        assert_equal(module, ring, ray_n1, ring.scale(common, F(-25, 3)), f"ER2 ray{sign} N1")
        assert_equal(
            module,
            ring,
            ray_n3,
            ring.scale(common, module.g(0, F(50 * sign, 3))),
            f"ER2 ray{sign} N3",
        )
        ray_records.extend(((f"RAY_{sign}_N1", ray_n1), (f"RAY_{sign}_N3", ray_n3)))
    factor_plus = ring.add(var["U"], ring.scale(var["V"], module.g(0, 8)))
    factor_minus = ring.add(var["U"], ring.scale(var["V"], module.g(0, -8)))
    assert_equal(module, ring, delta, ring.mul(factor_plus, factor_minus), "Delta split")

    # Live mutation: use 63 instead of 64 in the inverse matrix itself.  The
    # first original grade-11 row then has a nonzero normal form modulo the
    # *correct* localization relation qD*Delta-1.
    wrong_wb = ring.mul(
        var["qD"],
        ring.add(ring.scale(ring.mul(var["V"], r1), -63), ring.mul(var["U"], r2)),
    )
    wrong_normalized_row1 = ring.add(
        h1,
        ring.scale(
            ring.sub(ring.mul(var["U"], wa), ring.mul(var["V"], wrong_wb)),
            F(3, 1024),
        ),
    )
    need(
        qdelta_normal_form(module, ring, wrong_normalized_row1) != {},
        "ER2 inverse-matrix 64-to-63 mutation survived",
    )

    _, certificate_hash = canonical_polys(
        ring,
        [("ER2_N1", n1), ("ER2_N3", n3), ("ER2_RESULTANT", resultant)]
        + ray_records,
    )
    return certificate_hash


def main() -> None:
    start = time.perf_counter()
    for path, expected in EXPECTED.items():
        need(digest(path) == expected, ("source custody", str(path)))
    need(sha256(TAILS.read_bytes() + b"\n").hexdigest() != EXPECTED[TAILS], "vacuous custody mutation")
    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    need(term_count == 569, ("tail term census", term_count))

    er1_plus = er1_branch(module, rows, loads, 1)
    er1_minus = er1_branch(module, rows, loads, -1)
    need(er1_plus != er1_minus, "conjugate branch serialization collision")
    er2 = er2_branch(module, rows, loads)
    combined = sha256((er1_plus + er1_minus + er2).encode()).hexdigest()

    elapsed = time.perf_counter() - start
    print("K00_R3_REMAINING_FAN=PASS")
    print(f"FROZEN_BASIS={BASIS}")
    print("FROZEN_TAIL_TERMS=569")
    print("ACTIVE_LITERAL_COLUMNS_THROUGH_G12=38")
    print("ER1_PLUS=EMPTY_AT_GRADE12")
    print("ER1_MINUS=EMPTY_AT_GRADE12")
    print("ER2=EMPTY_AT_GRADE12")
    print("GRADES_13_TO_19=UNREACHED_AFTER_CERTIFIED_EMPTY_GRADE12_PREFIX")
    print(f"ER1_PLUS_CANONICAL_SHA256={er1_plus}")
    print(f"ER1_MINUS_CANONICAL_SHA256={er1_minus}")
    print(f"ER2_CANONICAL_SHA256={er2}")
    print(f"COMBINED_CERTIFICATE_SHA256={combined}")
    print("PERIODICITY_ASSUMPTIONS=NONE")
    print("MUTATIONS=ER1_6144_TO_6143,ER2_DELTA_64_TO_63,CUSTODY_NEWLINE,CONJUGATE_COLLISION")
    print(f"RUNTIME_SECONDS={elapsed:.6f}")


if __name__ == "__main__":
    main()
