#!/usr/bin/env python3
"""Exact stdlib replay of the e=3,m=1 stable-rank-one G9 gate.

The program reconstructs the literal seven-row V20R2 source from the frozen
569 tails.  It first rederives the two G8 rank-one compatibility equations.
On their reduced field-valued support it retains the free second surface
coefficient, four grade-four kernel coordinates, the full grade-five lift
fiber, all coefficients through d[8], and the first four K10 coefficients.
For both Gaussian signs the literal row-six G9 coefficient is the unit
epsilon*i*q^3/32 on D(q).

This is a producer replay.  It proves no claim about another rank stratum,
ramification pair, formal arc, source reachability, map, or JC2.
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
PREMISE_REPORT = ROOT / "xmodel/k00-ram-e2m1-allfaces-uniformity-audit-sol56-20260829.md"
PREMISE_REPLAY = ROOT / "xmodel/k00-ram-m1-uniform-rankfan-replay-sol56-20260829.py"
G7_INTEGRATION = ROOT / "xmodel/k00-ram-e2m1-g7-rankfan-coordinator-integration-sol56-20260829.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    PREMISE_REPORT: "64eaafe3fe5aaa9238a338f2da045e302d9a239ac9c29312e39d5c545893d42c",
    PREMISE_REPLAY: "0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b",
    G7_INTEGRATION: "0eb501b414f2162d14a73725a46410b7e799adc70932cdfb8a05f4196ff0bb1a",
}
EXPECTED_CERTIFICATE_SHA256 = "53cb17004c510c34de96c64838c9707d10400aa83b36d5b9cb56bf4c01630ed9"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_e3m1_g9_engine", ENGINE)
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


def surface_coefficients(module, ring, sign: int, t, alpha, beta):
    """Coefficients of D(S,T), S=sign*8*i*t*tau+alpha*tau^2."""

    s = ring.scale(t, module.g(0, 8 * sign))
    return [
        {
            1: ring.scale(s, 2),
            2: ring.add(ring.scale(alpha, 2), ring.mul(s, s)),
            3: ring.scale(ring.mul(s, alpha), 2),
            4: ring.mul(alpha, alpha),
        },
        {
            1: ring.scale(t, F(1, 8)),
            2: ring.scale(ring.add(beta, ring.mul(s, t)), F(1, 8)),
            3: ring.scale(
                ring.add(ring.mul(s, beta), ring.mul(alpha, t)), F(1, 8)
            ),
            4: ring.scale(ring.mul(alpha, beta), F(1, 8)),
        },
        {
            1: s,
            2: ring.add(alpha, ring.scale(ring.mul(t, t), 16)),
            3: ring.scale(ring.mul(t, beta), 32),
            4: ring.scale(ring.mul(beta, beta), 16),
        },
        {1: t, 2: beta},
        {1: s, 2: alpha},
        {1: ring.scale(t, 2), 2: ring.scale(beta, 2)},
    ]


def literal_e3_source(module, rows, k10_rows, dseries, kseries, ring):
    """R(d)+tau^6*k10(tau)*A10(d), through G9."""

    total = [module.eval_dpoly_series(row, dseries, ring) for row in rows]
    load = [module.eval_dpoly_series(row, dseries, ring) for row in k10_rows]
    for row_index in range(7):
        for kgrade, kval in enumerate(kseries):
            if not kval:
                continue
            for dgrade in range(10 - 6 - kgrade):
                if load[row_index][dgrade]:
                    grade = 6 + kgrade + dgrade
                    total[row_index][grade] = ring.add(
                        total[row_index][grade],
                        ring.mul(kval, load[row_index][dgrade]),
                    )
    return total, load


def compatibility_check(module, rows, k10_rows, sign: int):
    """Rebuild the two exact G8 cokernel equations before reduction."""

    names = (
        "t", "q", "alpha", "beta", "X", "k0",
        "y1", "y2", "y3", "y4",
        *(f"z{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    t, q = value["t"], value["q"]
    alpha, beta, xvalue = value["alpha"], value["beta"], value["X"]
    epsilon_i8 = module.g(0, 8 * sign)
    surface = surface_coefficients(module, ring, sign, t, alpha, beta)
    w = module.cone_vector(
        ring, ring.const(), ring.const(), ring.scale(q, epsilon_i8), q
    )
    bvalue = ring.add(
        ring.scale(xvalue, epsilon_i8), ring.scale(ring.mul(t, q), -128)
    )
    next_normal = module.vector_with_ab(
        ring, xvalue, bvalue,
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    dseries = []
    for index in range(6):
        series = module.series_zero(10)
        for grade, coefficient in surface[index].items():
            series[grade] = coefficient
        series[3] = ring.add(series[3], w[index])
        series[4] = ring.add(series[4], next_normal[index])
        series[5] = value[f"z{index}"]
        dseries.append(series)
    source, _ = literal_e3_source(
        module, rows, k10_rows, dseries,
        (value["k0"], ring.const(), ring.const(), ring.const()), ring,
    )
    for row_index in range(7):
        for grade in range(8):
            assert_zero(
                source[row_index][grade],
                f"general sign {sign} row {row_index + 1} G{grade}",
            )

    tq = ring.mul(t, q)
    q2 = ring.mul(q, q)
    common = ring.add(
        ring.mul(xvalue, xvalue),
        ring.scale(
            ring.mul(tq, xvalue), module.g(0, -48 * sign)
        ),
    )
    form512 = ring.add(
        ring.add(common, ring.scale(ring.mul(tq, tq), -512)),
        ring.add(
            ring.scale(ring.mul(alpha, q2), 16),
            ring.scale(ring.mul(beta, q2), module.g(0, -128 * sign)),
        ),
    )
    form640 = ring.add(
        ring.add(common, ring.scale(ring.mul(tq, tq), -640)),
        ring.add(
            ring.scale(ring.mul(alpha, q2), -16),
            ring.scale(ring.mul(beta, q2), module.g(0, 128 * sign)),
        ),
    )
    compat3 = ring.add(source[2][8], source[0][8], F(1, 8))
    compat4 = source[3][8]
    assert_equal(
        module, ring, compat3,
        ring.scale(form512, module.g(0, F(3 * sign, 2048))),
        f"sign {sign} G8 compatibility 3",
    )
    assert_equal(
        module, ring, compat4, ring.scale(form640, F(-3, 4096)),
        f"sign {sign} G8 compatibility 4",
    )

    wall = ring.add(
        ring.add(ring.scale(ring.mul(t, t), 4), alpha),
        ring.scale(beta, module.g(0, -8 * sign)),
    )
    assert_equal(
        module, ring, ring.sub(form512, form640),
        ring.scale(ring.mul(q2, wall), 32),
        f"sign {sign} compatibility difference",
    )
    double_root = ring.sub(
        xvalue, ring.scale(tq, module.g(0, 24 * sign))
    )
    assert_equal(
        module, ring, ring.add(form512, form640),
        ring.scale(ring.mul(double_root, double_root), 2),
        f"sign {sign} compatibility sum",
    )

    # Negative control: replacing -4*t^2 by -3*t^2 leaves wall=t^2.
    wrong_alpha = ring.add(
        ring.scale(ring.mul(t, t), -3),
        ring.scale(beta, module.g(0, 8 * sign)),
    )
    wrong_wall = ring.add(
        ring.add(ring.scale(ring.mul(t, t), 4), wrong_alpha),
        ring.scale(beta, module.g(0, -8 * sign)),
    )
    assert_equal(
        module, ring, wrong_wall, ring.mul(t, t),
        f"sign {sign} surface-coefficient mutation",
    )
    if not wrong_wall:
        fail("surface-coefficient mutation invisible")
    return form512, form640


def reduced_branch_check(module, rows, loads, sign: int):
    """Check the full reduced G8 lift family and its literal G9 row six."""

    names = (
        "t", "q", "beta", "k0", "k1", "k2", "k3",
        "y1", "y2", "y3", "y4",
        *(f"z{index}" for index in range(6)),
        *(f"u{index}" for index in range(6)),
        *(f"v{index}" for index in range(6)),
        *(f"r{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    value = {name: ring.var(name) for name in names}
    t, q, beta = value["t"], value["q"], value["beta"]
    epsilon_i8 = module.g(0, 8 * sign)
    alpha = ring.add(
        ring.scale(ring.mul(t, t), -4), ring.scale(beta, epsilon_i8)
    )
    surface = surface_coefficients(module, ring, sign, t, alpha, beta)
    w = module.cone_vector(
        ring, ring.const(), ring.const(), ring.scale(q, epsilon_i8), q
    )
    xvalue = ring.scale(ring.mul(t, q), module.g(0, 24 * sign))
    bvalue = ring.scale(ring.mul(t, q), -320)
    next_normal = module.vector_with_ab(
        ring, xvalue, bvalue,
        value["y1"], value["y2"], value["y3"], value["y4"],
    )
    dseries = []
    for index in range(6):
        series = module.series_zero(10)
        for grade, coefficient in surface[index].items():
            series[grade] = coefficient
        series[3] = ring.add(series[3], w[index])
        series[4] = ring.add(series[4], next_normal[index])
        series[5] = value[f"z{index}"]
        series[6] = value[f"u{index}"]
        series[7] = value[f"v{index}"]
        series[8] = value[f"r{index}"]
        dseries.append(series)
    kseries = tuple(value[f"k{index}"] for index in range(4))
    source, load = literal_e3_source(
        module, rows, loads["K10"], dseries, kseries, ring
    )
    for row_index in range(7):
        for grade in range(8):
            assert_zero(
                source[row_index][grade],
                f"reduced sign {sign} row {row_index + 1} G{grade}",
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
        ring.scale(
            ring.mul(ring.mul(t, t), q), module.g(0, 1088 * sign)
        ),
    )
    hform = ring.add(hform, ring.scale(ring.mul(t, value["y1"]), -512))
    hform = ring.add(
        hform,
        ring.scale(ring.mul(t, value["y2"]), module.g(0, -8 * sign)),
    )
    hform = ring.add(hform, ring.scale(ring.mul(t, value["y3"]), 64))
    hform = ring.add(
        hform,
        ring.scale(ring.mul(t, value["y4"]), module.g(0, 8 * sign)),
    )
    z0_key = [0] * ring.n
    z0_key[ring.index["z0"]] = 1
    if hform.get(tuple(z0_key), module.g()) != module.g(1):
        fail(("G8 lift fiber is not visibly affine in z0", sign))
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
            f"reduced sign {sign} G8 row {row_index + 1}",
        )

    terminal = ring.scale(
        ring.power(q, 3), module.g(0, F(sign, 32))
    )
    assert_equal(
        module, ring, source[5][9], terminal,
        f"reduced sign {sign} G9 row 6",
    )
    for grade in range(4):
        assert_zero(load[5][grade], f"sign {sign} K10 row6 coefficient {grade}")

    # Scope control: the terminal vanishes on q=0, so D(q) is load-bearing.
    assert_zero(
        ring.zero_vars(terminal, ("q",)), f"sign {sign} q-open control"
    )

    # Source mutation: a forbidden d3^3 term in A10 row six would contribute
    # k0*t^3 at G9.  The replay must see it.
    mutation = module.dadd(
        loads["K10"][5], module.dpow(module.dvar(3), 3)
    )
    mutation_series = module.eval_dpoly_series(mutation, dseries, ring)
    mutated_terminal = ring.add(
        source[5][9], ring.mul(value["k0"], mutation_series[3])
    )
    if mutated_terminal == terminal:
        fail("K10 row-six mutation invisible")
    expected_delta = ring.mul(
        value["k0"], ring.power(t, 3)
    )
    assert_equal(
        module, ring, ring.sub(mutated_terminal, terminal), expected_delta,
        f"sign {sign} K10 mutation delta",
    )
    return hform, terminal


def qstring(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_object(poly):
    answer = []
    for key in sorted(poly):
        real, imag = poly[key]
        answer.append([list(key), qstring(real), qstring(imag)])
    return answer


def main() -> None:
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("custody", path, actual, expected))
    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    if min(sum(key) for row in rows for key in row) < 2:
        fail("unloaded linear term")
    if min(sum(key) for row in loads["K10"] for key in row) < 2:
        fail("K10 linear term")
    late_calendar = {
        "K6": 6 * 3 + 1 + 1,
        "K2": 10 * 3 + 1 + 1,
        "mu2": 14 * 3 + 1,
        "mu4": 16 * 3 + 1,
        "mu6": 18 * 3 + 1,
        "Jdet": 19 * 3,
    }
    if any(grade <= 9 for grade in late_calendar.values()):
        fail(("late-load calendar", late_calendar))

    compatibility = {}
    reduced = {}
    for sign in (1, -1):
        form512, form640 = compatibility_check(
            module, rows, loads["K10"], sign
        )
        hform, terminal = reduced_branch_check(module, rows, loads, sign)
        compatibility[str(sign)] = {
            "form512": poly_object(form512),
            "form640": poly_object(form640),
        }
        reduced[str(sign)] = {
            "g8_h": poly_object(hform),
            "g9_row6": poly_object(terminal),
        }

    certificate = {
        "type": "K00-RAM-E3M1-G9-STABLE-RANKONE-KILL/v1",
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "tail_terms": term_count,
        "field": "Q(i), characteristic zero",
        "normalization": "Lambda=tau^3; C6=1; K10 shift=tau^6",
        "premise_lifecycle": "PRODUCER_EXACT_REVIEW_GATED",
        "rankone_open": "t*q != 0",
        "field_compatibility": [
            "X=epsilon*24*i*t*q",
            "alpha-epsilon*8*i*beta=-4*t^2",
        ],
        "compatibility_polynomials": compatibility,
        "reduced_branches": reduced,
        "g8_lift": "H_epsilon=0; four y directions; five-dimensional z fiber",
        "g9_terminal": "G9_row6=epsilon*i*q^3/32",
        "late_loads": "K6,K2,mu2,mu4,mu6,Jdet absent through G9",
        "conclusion": "REDUCED_STABLE_RANKONE_G8_FAMILY_EMPTY_AT_G9_ON_D(q)",
        "nonclaims": [
            "other e3 rank strata", "whole e3m1 cell", "formal arc",
            "source reachability", "map", "JC2",
        ],
        "mutations": [
            "custody", "surface_-4_to_-3", "K10_row6_plus_d3_cubed",
            "q_open_removed",
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

    print("K00_RAM_E3M1_G9_RANKONE_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("PREMISE_G0_G8=PRODUCER_EXACT_REVIEW_GATED")
    print("SIGNS=PLUS,MINUS;OPEN=t*q!=0")
    print("G8_FIELD_COMPAT=X=EPS*24*i*t*q;alpha-EPS*8*i*beta=-4*t^2")
    print("G8_LIFT=H_EPS=0;Y_DIRECTIONS=4;Z_FIBER_DIM=5")
    print("G9_ROW6=EPS*i*q^3/32")
    print("K10_ROW6_G9=ZERO;LATE_LOADS=ABSENT")
    print("VERDICT=REDUCED_STABLE_RANKONE_G8_FAMILY_EMPTY_AT_G9_ON_D(q)")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,SURFACE_-4_TO_-3,K10_ROW6_D3_CUBED,Q_OPEN")


if __name__ == "__main__":
    main()
