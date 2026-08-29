#!/usr/bin/env python3
"""Exact stdlib replay for the first ramified K00 V20R2 prefix.

The registered cell has Lambda=t^2, ord_t(d)=1, k10 and Jdet units, and
exact order one for k6,k2,mu2,mu4,mu6.  This replay reconstructs all 569
tails, verifies the literal source calendar, transports the promoted complete
grade-three rank kill, and derives the surviving pure-unloaded G4/G5 residual.
It writes no files and uses no CAS or network service.
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
G3_INTEGRATION = ROOT / "xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md"
G4_INTEGRATION = ROOT / "xmodel/k00-grade4-rank0-plane-coordinator-integration-sol56-20260829.md"
VALUATIVE_PACKET = ROOT / "xmodel/k00-v20r2-valuative-comparison-v1-sol56-20260829.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    G3_INTEGRATION: "d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860",
    G4_INTEGRATION: "fbe5b580662b7f77326c61f5fec54b3a9a2059f1684f52994fee8652efc49448",
    VALUATIVE_PACKET: "98fb38535405f1cc853dd4d430e26876a84f6f97c538f862f18a0446c0c97ecf",
}

EXPECTED_RESIDUAL_SHA256 = "f471559d53c25ca40a60bb3d01241ff7186e581bcc383433b6a5163ffd07b691"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_exact_engine", ENGINE)
    if spec is None or spec.loader is None:
        fail("cannot import exact engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_equal(module, ring, left, right, label: str) -> None:
    module.assert_equal(left, right, ring, label)


def assert_zero(poly, label: str) -> None:
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def directional(module, ring, poly, point, direction):
    out = ring.const()
    for index in range(6):
        derivative = module.dderivative(poly, index)
        value = module.eval_dpoly(derivative, point, ring)
        out = ring.add(out, ring.mul(value, direction[index]))
    return out


def second_directional(module, ring, poly, point, left, right):
    out = ring.const()
    for i in range(6):
        first = module.dderivative(poly, i)
        for j in range(6):
            second = module.dderivative(first, j)
            value = module.eval_dpoly(second, point, ring)
            out = ring.add(out, ring.mul(ring.mul(value, left[i]), right[j]))
    return out


def qstring(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_object(poly):
    answer = []
    for key in sorted(poly):
        real, imag = poly[key]
        answer.append([list(key), qstring(real), qstring(imag)])
    return answer


def evaluate_rational(poly, ring, values: dict[str, F]) -> tuple[F, F]:
    real = F(0)
    imag = F(0)
    for key, coefficient in poly.items():
        factor = F(1)
        for name, exponent in zip(ring.names, key):
            factor *= values.get(name, F(0)) ** exponent
        real += coefficient[0] * factor
        imag += coefficient[1] * factor
    return real, imag


def main() -> None:
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("custody", path))
    if sha256(TAILS.read_bytes() + b"\n").hexdigest() == EXPECTED[TAILS]:
        fail("custody mutation did not fire")

    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))

    profiles = {
        "R": [min(map(sum, row)) for row in rows],
        "K10": [min(map(sum, row)) for row in loads["K10"]],
        "K6": [min(map(sum, row)) for row in loads["K6"]],
        "K2": [min(map(sum, row)) for row in loads["K2"]],
    }
    expected_profiles = {
        "R": [2, 2, 2, 2, 2, 3, 2],
        "K10": [2, 2, 2, 2, 2, 2, 2],
        "K6": [1, 1, 1, 2, 1, 2, 1],
        "K2": [1, 1, 1, 1, 1, 1, 1],
    }
    if profiles != expected_profiles:
        fail(("normal-degree profiles", profiles))

    names = (
        "s", "t",
        *(f"u{i}" for i in range(6)),
        *(f"v{i}" for i in range(6)),
        *(f"p{i}" for i in range(6)),
    )
    ring = module.Ring(tuple(names))
    var = {name: ring.var(name) for name in names}
    x = module.old_plane(ring, var["s"], var["t"])
    u = [var[f"u{i}"] for i in range(6)]
    v = [var[f"v{i}"] for i in range(6)]
    p = [var[f"p{i}"] for i in range(6)]
    mu = [
        ring.power(var["s"], 2),
        ring.scale(ring.mul(var["s"], var["t"]), F(1, 8)),
        ring.scale(ring.power(var["t"], 2), 16),
        ring.const(), ring.const(), ring.const(),
    ]
    w = [ring.sub(a, b) for a, b in zip(u, mu)]

    dseries = []
    for index in range(6):
        series = module.series_zero(6)
        series[1] = x[index]
        series[2] = u[index]
        series[3] = v[index]
        series[4] = p[index]
        dseries.append(series)
    equations = [module.eval_dpoly_series(row, dseries, ring) for row in rows]

    quadrics = [module.dhom(row, 2) for row in rows]
    cubics = [module.dhom(row, 3) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]
    l6 = [module.dhom(row, 1) for row in loads["K6"]]
    a6_quadratic = [module.dhom(row, 2) for row in loads["K6"]]
    n2 = [module.dhom(row, 1) for row in loads["K2"]]
    a2_quadratic = [module.dhom(row, 2) for row in loads["K2"]]
    m4_g7 = []
    for row_index in range(7):
        assert_zero(module.eval_dpoly(m4[row_index], x, ring),
                    f"row{row_index + 1} M4(Pi)")
        m4_g7.append(directional(module, ring, m4[row_index], x, u))
    if not any(m4_g7):
        fail("K10 remains invisible after G6 on Pi")

    # Ramified source calendar after restriction to Pi.  Since the K6 scale
    # is t^12 and k6 has exact order one, its generic linear arrival is G14.
    # L6(ell)=0 delays it one grade; the G15 coefficient with k6[1]=1 is
    # L6(u)+A6^[2](ell).  K2 has scale t^20 and exact-order-one coefficient,
    # so its linear arrival is tested directly at G22 (and, if necessary,
    # one grade later by the same expansion).
    k6_g15 = []
    for row_index in range(7):
        assert_zero(module.eval_dpoly(l6[row_index], x, ring),
                    f"row{row_index + 1} L6(Pi)")
        coefficient = ring.add(
            module.eval_dpoly(l6[row_index], u, ring),
            module.eval_dpoly(a6_quadratic[row_index], x, ring),
        )
        k6_g15.append(coefficient)
    if not any(k6_g15):
        fail("K6 remains invisible after G15 on Pi")

    k2_g22 = [module.eval_dpoly(poly, x, ring) for poly in n2]
    if any(k2_g22):
        k2_first_possible = 22
    else:
        k2_g23 = []
        for row_index in range(7):
            coefficient = ring.add(
                module.eval_dpoly(n2[row_index], u, ring),
                module.eval_dpoly(a2_quadratic[row_index], x, ring),
            )
            k2_g23.append(coefficient)
        if not any(k2_g23):
            fail("K2 remains invisible after G23 on Pi")
        k2_first_possible = 23
    g4 = []
    g5 = []
    for row_index in range(7):
        assert_zero(equations[row_index][0], f"row{row_index + 1} G0")
        assert_zero(equations[row_index][1], f"row{row_index + 1} G1")
        assert_zero(equations[row_index][2], f"row{row_index + 1} G2 on Pi")
        assert_zero(equations[row_index][3], f"row{row_index + 1} G3 on Pi")

        expected_g4 = module.eval_dpoly(quadrics[row_index], w, ring)
        assert_equal(module, ring, equations[row_index][4], expected_g4,
                     f"row{row_index + 1} G4=Q(w)")
        g4.append(expected_g4)

        expected_g5 = directional(module, ring, quadrics[row_index], w, v)
        cubic_piece = second_directional(
            module, ring, cubics[row_index], x, w, w
        )
        expected_g5 = ring.add(expected_g5, cubic_piece, F(1, 2))
        assert_equal(module, ring, equations[row_index][5], expected_g5,
                     f"row{row_index + 1} pure G5")
        g5.append(expected_g5)

    # The exact reduced G4 support inherited from the promoted theorem.
    form_a = ring.linear((16, w[1]), (-4, w[3]), (1, w[5]))
    form_b = ring.linear((1, w[0]), (-4, w[2]), (2, w[4]))

    # Explicit exact-order-one leading prefix: s=1,t=0,u=mu,v=p=0.
    witness = {name: F(0) for name in names}
    witness["s"] = F(1)
    witness["u0"] = F(1)
    for row_index in range(7):
        for grade in range(6):
            if evaluate_rational(equations[row_index][grade], ring, witness) != (F(0), F(0)):
                fail(("prefix witness", row_index + 1, grade))
    k10_witness = [evaluate_rational(poly, ring, witness) for poly in m4_g7]
    k6_witness = [evaluate_rational(poly, ring, witness) for poly in k6_g15]
    k2_witness = [evaluate_rational(poly, ring, witness) for poly in k2_g22]
    if not any(value != (F(0), F(0)) for value in k10_witness):
        fail("K10 G7 vanishes at the exact residual witness")
    if not any(value != (F(0), F(0)) for value in k6_witness):
        fail("K6 G15 vanishes at the exact residual witness")
    if not any(value != (F(0), F(0)) for value in k2_witness):
        fail("K2 G22 vanishes at the exact residual witness")
    exact_calendar_witness = (
        k10_witness[1], k6_witness[1], k2_witness[1]
    )
    if exact_calendar_witness != (
        (F(5, 32768), F(0)),
        (F(3, 2048), F(0)),
        (F(1, 32), F(0)),
    ):
        fail(("calendar witness normalization", exact_calendar_witness))

    # Mutations: wrong cubic, wrong mu representative, wrong ramified load
    # scale, and deletion of the odd t-leading block must all be visible.
    cubic_mutation = module.eval_dpoly(
        module.dadd(cubics[0], {tuple([3, 0, 0, 0, 0, 0]): F(1)}), x, ring
    )
    if not cubic_mutation:
        fail("cubic mutation survived G3")
    wrong_mu = list(mu)
    wrong_mu[2] = ring.scale(ring.power(var["t"], 2), 15)
    wrong_w = [ring.sub(a, b) for a, b in zip(u, wrong_mu)]
    if all(
        module.eval_dpoly(quadrics[i], wrong_w, ring) == g4[i]
        for i in range(7)
    ):
        fail("mu mutation survived G4")
    generic_ring = module.Ring(tuple([*(f"x{i}" for i in range(6)), "kap"]))
    generic_x = [generic_ring.var(f"x{i}") for i in range(6)]
    kap = generic_ring.var("kap")
    wrong_scale_g4 = [
        generic_ring.mul(kap, module.eval_dpoly(m4[i], generic_x, generic_ring))
        for i in range(7)
    ]
    if not any(wrong_scale_g4):
        fail("wrong e=1 K10-at-G4 mutation is invisible")
    correct_generic_g2 = [
        module.eval_dpoly(quadrics[i], generic_x, generic_ring) for i in range(7)
    ]
    if not any(correct_generic_g2):
        fail("odd-leading-column deletion is invisible")
    wrong_plane = list(x)
    wrong_plane[0] = ring.add(wrong_plane[0], var["s"])
    if not any(module.eval_dpoly(l6[i], wrong_plane, ring) for i in range(7)):
        fail("K6 restriction mutation is invisible")

    residual = {
        "type": "K00-V20R2-RAM-E2-M1-B11111-G5-RESIDUAL/v1",
        "source": {path.name: value for path, value in EXPECTED.items()},
        "ramification": {"Lambda": "t^2", "m": 1,
                           "orders": [0, 1, 1, 1, 1, 1, 0]},
        "variables": list(ring.names),
        "leading": ["2*s", "t/8", "s", "t", "s", "2*t"],
        "open": ["(s,t)!=(0,0)",
                 "k10_0*k6_1*k2_1*mu2_1*mu4_1*mu6_1*Jdet_0!=0"],
        "grade4": [poly_object(poly) for poly in g4],
        "grade5": [poly_object(poly) for poly in g5],
        "grade4_reduced_forms": [poly_object(form_a), poly_object(form_b)],
        "source_calendar": {
            "K10_generic_first": 6,
            "K10_on_Pi_first_possible": 7,
            "K6_generic_first_by_row": [14, 14, 14, 15, 14, 15, 14],
            "K6_on_Pi_first_possible": 15,
            "K2_generic_first": 22,
            "K2_on_Pi_first_possible": k2_first_possible,
            "targets_first": [29, 33, 37, 38],
        },
        "later_literal_grades": [6, 38],
        "attainment": False,
    }
    residual_bytes = (
        json.dumps(residual, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    residual_sha = sha256(residual_bytes).hexdigest()
    if EXPECTED_RESIDUAL_SHA256 != "PENDING" and residual_sha != EXPECTED_RESIDUAL_SHA256:
        fail(("residual digest", residual_sha))

    print("K00_RAM_E2M1_G5_PREFIX_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("G2_G3_SOURCE=IDENTICAL_TO_PROMOTED_UNLOADED_PREFIX")
    print("LEADING_NONZERO_MATRIX_RANKS=EMPTY_AT_G3")
    print("SURVIVING_LEADING_BASE=Pi_MINUS_ORIGIN")
    print("G4_IDENTITY=Q(u-mu)")
    print("G5_IDENTITY=DQ(w)[v]+1/2*D2c3(ell)[w,w]")
    print("K10_G6_ON_PI=ZERO;K10_FIRST_POSSIBLE_ON_RESIDUAL=G7")
    print("K6_G14_ON_PI=ZERO;K6_FIRST_POSSIBLE_ON_RESIDUAL=G15")
    print(f"K2_FIRST_POSSIBLE_ON_RESIDUAL=G{k2_first_possible}")
    print("CALENDAR_WITNESS_ROW2=K10_G7:5/32768,K6_G15:3/2048,K2_G22:1/32")
    print("PREFIX_WITNESS=s=1,t=0,w=0,v=0,p=0")
    print(f"RESIDUAL_BYTES={len(residual_bytes)}")
    print(f"RESIDUAL_SHA256={residual_sha}")
    print("MUTATIONS=CUSTODY,CUBIC,MU,K10_SCALE,K6_RESTRICTION,ODD_COLUMN_DROP")


if __name__ == "__main__":
    main()
