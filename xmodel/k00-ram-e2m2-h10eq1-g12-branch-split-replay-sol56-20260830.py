#!/usr/bin/env python3
"""Exact replay for the provisional e=2,m=2, ord(k10)=1 G12 child.

The program reconstructs the 569 literal V20R2 tails, derives the complete
G12 arrival formulas on the old n=4 and fresh n=5 survivor mechanisms, and
checks exact old-pass/new-fail controls.  It uses only stdlib exact rational
and Gaussian-rational arithmetic and writes no files.

The G11 organization is a PROVISIONAL dependency.  Every G12 identity and
fixture below is nevertheless recomputed directly from the frozen tails; no
coefficient recurrence or grade shift is used.
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
ENGINE = ROOT / "xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py"
BASE_REPLAY = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-replay-sol56-20260829.py"
BASE_REPORT = ROOT / "xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-sol56-20260829.md"
G11_REPLAY = ROOT / "xmodel/k00-ram-e2m2-h10eq1-g11-survivor-replay-sol56-20260830.py"
G11_REPORT = ROOT / "xmodel/k00-ram-e2m2-h10eq1-g11-survivor-producer-sol56-20260830.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    BASE_REPLAY: "efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749",
    BASE_REPORT: "fa5a4ef6a1b2c0640c6363b84e6b547a044920b15249f7c72b25ffbcda2c1733",
    G11_REPLAY: "d5e458d2c430cc85be86b711e37355671090057881474458055dbf7f593609c3",
    G11_REPORT: "05e416fccb20b42a187f254995c021608e9060444660628d52a848d17f19b8e1",
}
EXPECTED_CERTIFICATE_SHA256 = "56ebd72c0b66326eeee7fc1148838d11212ad1ef049907291675959b5484538e"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import", path))
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


def bilinear_hessian(module, ring, poly, point, left, right):
    out = ring.const()
    for first_index in range(6):
        first = module.dderivative(poly, first_index)
        for second_index in range(6):
            coefficient = module.eval_dpoly(
                module.dderivative(first, second_index), point, ring
            )
            out = ring.add(
                out,
                ring.mul(
                    ring.mul(coefficient, left[first_index]),
                    right[second_index],
                ),
            )
    return out


def copy_series(series):
    return [list(row) for row in series]


def general_n4_g12(base, module, rows, loads, quadrics, cubics, quartics, m4):
    """Literal n=4 G12 and its full quadratic/cubic/quartic/load expansion."""

    names = (
        "s", "t", "alpha", "beta", "gamma", "eta", "p", "q",
        "kap", "k2", "k3",
        *(f"n5_{i}" for i in range(6)),
        *(f"n6_{i}" for i in range(6)),
        *(f"n7_{i}" for i in range(6)),
        *(f"n8_{i}" for i in range(6)),
    )
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    surface = base.surface_series(
        module,
        ring,
        {2: x["s"], 3: x["alpha"], 4: x["gamma"]},
        {2: x["t"], 3: x["beta"], 4: x["eta"]},
        13,
    )
    surface_load = [
        module.eval_dpoly_series(row, surface, ring) for row in loads["K10"]
    ]
    dseries = copy_series(surface)
    n4 = module.cone_vector(
        ring, ring.const(), ring.const(), x["p"], x["q"]
    )
    n5 = [x[f"n5_{i}"] for i in range(6)]
    n6 = [x[f"n6_{i}"] for i in range(6)]
    n7 = [x[f"n7_{i}"] for i in range(6)]
    n8 = [x[f"n8_{i}"] for i in range(6)]
    for grade, vector in ((4, n4), (5, n5), (6, n6), (7, n7), (8, n8)):
        base.add_normal(ring, dseries, grade, vector)
    source, load = base.literal_e2_source(
        module,
        rows,
        loads["K10"],
        dseries,
        (ring.const(), x["kap"], x["k2"], x["k3"]),
        ring,
    )

    ell2 = module.old_plane(ring, x["s"], x["t"])
    ell3 = module.old_plane(ring, x["alpha"], x["beta"])
    surface4 = [surface[index][4] for index in range(6)]
    term_counts = []
    load_counts = []
    for row_index in range(7):
        load6 = ring.add(
            base.directional(module, ring, m4[row_index], ell2, n4),
            surface_load[row_index][6],
        )
        load7 = ring.add(
            base.directional(module, ring, m4[row_index], ell2, n5),
            ring.add(
                base.directional(module, ring, m4[row_index], ell3, n4),
                surface_load[row_index][7],
            ),
        )
        assert_equal(module, ring, load[row_index][6], load6, f"n4 load6 row {row_index + 1}")
        assert_equal(module, ring, load[row_index][7], load7, f"n4 load7 row {row_index + 1}")

        expected = ring.add(
            base.directional(module, ring, quadrics[row_index], n4, n8),
            ring.add(
                base.directional(module, ring, quadrics[row_index], n5, n7),
                ring.add(
                    module.eval_dpoly(quadrics[row_index], n6, ring),
                    ring.add(
                        bilinear_hessian(module, ring, cubics[row_index], ell2, n4, n6),
                        ring.add(
                            base.second_half(module, ring, cubics[row_index], ell2, n5),
                            ring.add(
                                bilinear_hessian(module, ring, cubics[row_index], ell3, n4, n5),
                                ring.add(
                                    base.second_half(module, ring, cubics[row_index], surface4, n4),
                                    ring.add(
                                        module.eval_dpoly(cubics[row_index], n4, ring),
                                        ring.add(
                                            base.second_half(module, ring, quartics[row_index], ell2, n4),
                                            ring.add(
                                                ring.mul(x["kap"], load7),
                                                ring.mul(x["k2"], load6),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        )
        assert_equal(module, ring, source[row_index][12], expected, f"literal n4 G12 row {row_index + 1}")
        if ring.depends_on(source[row_index][12], "k3"):
            fail(("spurious k10[3] at n4 G12", row_index + 1))
        term_counts.append(len(source[row_index][12]))
        load_counts.append((len(load6), len(load7)))
    return {
        "retained": "S2..S4,T2..T4,N4..N8,k10[1..3]",
        "capable": "S2..S4,T2..T4,N4..N8,k10[1],k10[2]",
        "k10_3_absent": True,
        "row_term_counts": term_counts,
        "load6_load7_counts": load_counts,
        "formula": (
            "DQ(N4)N8+DQ(N5)N7+Q(N6)+D2R3(ell2)[N4,N6]+"
            "1/2D2R3(ell2)[N5,N5]+D2R3(ell3)[N4,N5]+"
            "1/2D2R3(surface4)[N4,N4]+R3(N4)+"
            "1/2D2R4(ell2)[N4,N4]+k1*load7+k2*load6"
        ),
    }


def general_n5_g12(base, module, rows, loads, quadrics, cubics, m4):
    """Literal fresh-n=5 G12 and complete capable-slot census."""

    names = (
        "s", "t", "alpha", "beta", "gamma", "eta", "p", "q",
        "kap", "k2", "k3",
        *(f"n6_{i}" for i in range(6)),
        *(f"n7_{i}" for i in range(6)),
        *(f"n8_{i}" for i in range(6)),
    )
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    surface = base.surface_series(
        module,
        ring,
        {2: x["s"], 3: x["alpha"], 4: x["gamma"]},
        {2: x["t"], 3: x["beta"], 4: x["eta"]},
        13,
    )
    surface_load = [
        module.eval_dpoly_series(row, surface, ring) for row in loads["K10"]
    ]
    dseries = copy_series(surface)
    n5 = module.cone_vector(
        ring, ring.const(), ring.const(), x["p"], x["q"]
    )
    n6 = [x[f"n6_{i}"] for i in range(6)]
    n7 = [x[f"n7_{i}"] for i in range(6)]
    n8 = [x[f"n8_{i}"] for i in range(6)]
    for grade, vector in ((5, n5), (6, n6), (7, n7), (8, n8)):
        base.add_normal(ring, dseries, grade, vector)
    source, load = base.literal_e2_source(
        module,
        rows,
        loads["K10"],
        dseries,
        (ring.const(), x["kap"], x["k2"], x["k3"]),
        ring,
    )

    ell2 = module.old_plane(ring, x["s"], x["t"])
    term_counts = []
    load_counts = []
    for row_index in range(7):
        load6 = surface_load[row_index][6]
        load7 = ring.add(
            base.directional(module, ring, m4[row_index], ell2, n5),
            surface_load[row_index][7],
        )
        assert_equal(module, ring, load[row_index][6], load6, f"n5 load6 row {row_index + 1}")
        assert_equal(module, ring, load[row_index][7], load7, f"n5 load7 row {row_index + 1}")
        expected = ring.add(
            base.directional(module, ring, quadrics[row_index], n5, n7),
            ring.add(
                module.eval_dpoly(quadrics[row_index], n6, ring),
                ring.add(
                    base.second_half(module, ring, cubics[row_index], ell2, n5),
                    ring.add(
                        ring.mul(x["kap"], load7),
                        ring.mul(x["k2"], load6),
                    ),
                ),
            ),
        )
        assert_equal(module, ring, source[row_index][12], expected, f"literal n5 G12 row {row_index + 1}")
        for absent in ("gamma", "eta", "k3", *(f"n8_{i}" for i in range(6))):
            if ring.depends_on(source[row_index][12], absent):
                fail(("spurious fresh-n5 G12 dependence", row_index + 1, absent))
        term_counts.append(len(source[row_index][12]))
        load_counts.append((len(load6), len(load7)))
    return {
        "retained": "S2..S4,T2..T4,N5..N8,k10[1..3]",
        "capable": "S2,S3,T2,T3,N5..N7,k10[1],k10[2]",
        "verified_absent": "S4,T4,N8,k10[3]",
        "row_term_counts": term_counts,
        "load6_load7_counts": load_counts,
        "formula": (
            "DQ(N5)N7+Q(N6)+1/2D2R3(ell2)[N5,N5]+"
            "k1*(DM4(ell2)N5+W7)+k2*W6"
        ),
    }


def n4_rankone_terminal(base, module, rows, loads):
    terminals = {}
    for sign in (1, -1):
        names = (
            "t", "q", "alpha", "beta", "gamma", "eta", "kap", "k2",
            "U", "P", "Q", "R", "W",
            *(f"y{i}" for i in range(1, 5)),
            *(f"z{i}" for i in range(1, 5)),
            *(f"u{i}" for i in range(1, 5)),
            *(f"v{i}" for i in range(1, 5)),
        )
        ring = module.Ring(names)
        x = {name: ring.var(name) for name in names}
        dseries = base.surface_series(
            module,
            ring,
            {
                2: ring.scale(x["t"], module.g(0, 8 * sign)),
                3: x["alpha"], 4: x["gamma"],
            },
            {2: x["t"], 3: x["beta"], 4: x["eta"]},
            13,
        )
        n4 = module.cone_vector(
            ring, ring.const(), ring.const(),
            ring.scale(x["q"], module.g(0, 8 * sign)), x["q"],
        )
        n5 = module.vector_with_ab(
            ring, ring.const(), ring.const(),
            x["y1"], x["y2"], x["y3"], x["y4"],
        )
        n6 = module.vector_with_ab(
            ring,
            x["U"],
            ring.add(
                ring.scale(x["U"], module.g(0, 8 * sign)),
                ring.scale(ring.mul(x["t"], x["q"]), -128),
            ),
            x["z1"], x["z2"], x["z3"], x["z4"],
        )
        n7 = module.vector_with_ab(
            ring, x["P"], x["Q"], x["u1"], x["u2"], x["u3"], x["u4"]
        )
        n8 = module.vector_with_ab(
            ring, x["R"], x["W"], x["v1"], x["v2"], x["v3"], x["v4"]
        )
        for grade, vector in ((4, n4), (5, n5), (6, n6), (7, n7), (8, n8)):
            base.add_normal(ring, dseries, grade, vector)
        source, load = base.literal_e2_source(
            module, rows, loads["K10"], dseries,
            (ring.const(), x["kap"], x["k2"]), ring,
        )
        for row_index in range(7):
            for grade in range(11):
                assert_zero(source[row_index][grade], f"n4 sign {sign} row {row_index + 1} G{grade}")
        assert_zero(source[5][11], f"n4 sign {sign} row6 G11")
        terminal = ring.scale(ring.power(x["q"], 3), module.g(0, F(sign, 32)))
        assert_equal(module, ring, source[5][12], terminal, f"n4 sign {sign} row6 G12")
        assert_zero(load[5][6], f"n4 sign {sign} K10 row6 raw6")
        assert_zero(load[5][7], f"n4 sign {sign} K10 row6 raw7")
        terminals[str(sign)] = poly_object(terminal)
    return terminals


def fixture_source(base, module, rows, loads, kind: str, sign: int = 1, mutation: bool = False):
    ring = module.Ring(())
    if kind == "n4_rank1":
        dseries = base.surface_series(
            module, ring,
            {2: ring.const(module.g(0, 8 * sign))},
            {2: ring.const(1)}, 13,
        )
        vectors = (
            (4, module.cone_vector(
                ring, ring.const(), ring.const(),
                ring.const(module.g(0, 8 * sign)), ring.const(1),
            )),
            (5, module.vector_with_ab(
                ring, ring.const(), ring.const(), ring.const(F(5, 72)),
                ring.const(), ring.const(), ring.const(),
            )),
            (6, module.vector_with_ab(
                ring, ring.const(), ring.const(-128),
                ring.const(), ring.const(), ring.const(), ring.const(),
            )),
            (7, module.vector_with_ab(
                ring, ring.const(), ring.const(F(320, 9)),
                ring.const(), ring.const(), ring.const(), ring.const(),
            )),
        )
        kseries = (ring.const(), ring.const(1))
    elif kind == "n5_rank2":
        dseries = base.surface_series(
            module, ring, {2: ring.const(1)}, {2: ring.const()}, 13
        )
        b7 = F(-1) if mutation else F(-2)
        vectors = (
            (5, module.cone_vector(
                ring, ring.const(), ring.const(), ring.const(1), ring.const(),
            )),
            (6, module.vector_with_ab(
                ring, ring.const(), ring.const(-4),
                ring.const(), ring.const(), ring.const(), ring.const(),
            )),
            (7, module.vector_with_ab(
                ring, ring.const(), ring.const(b7),
                ring.const(), ring.const(), ring.const(), ring.const(),
            )),
        )
        kseries = (ring.const(), ring.const(F(48, 5)))
    elif kind == "n5_rank1":
        dseries = base.surface_series(
            module, ring,
            {2: ring.const(8)},
            {2: ring.const(module.g(0, sign))}, 13,
        )
        b7_imag = 127 * sign if mutation else 128 * sign
        vectors = (
            (5, module.cone_vector(
                ring, ring.const(), ring.const(),
                ring.const(module.g(0, 8 * sign)), ring.const(1),
            )),
            (6, module.vector_with_ab(
                ring, ring.const(16), ring.const(module.g(0, -128 * sign)),
                ring.const(), ring.const(), ring.const(), ring.const(),
            )),
            (7, module.vector_with_ab(
                ring, ring.const(), ring.const(module.g(0, b7_imag)),
                ring.const(), ring.const(), ring.const(), ring.const(),
            )),
        )
        kseries = (ring.const(), ring.const(F(-12, 5)))
    else:
        fail(("unknown fixture", kind))

    for grade, vector in vectors:
        base.add_normal(ring, dseries, grade, vector)
    return base.literal_e2_source(
        module, rows, loads["K10"], dseries, kseries, ring
    )[0]


def fixtures(base, module, rows, loads):
    result = {}
    for sign in (1, -1):
        old = fixture_source(base, module, rows, loads, "n4_rank1", sign)
        for row_index in range(7):
            for grade in range(12):
                assert_zero(old[row_index][grade], f"n4 fixture sign {sign} row {row_index + 1} G{grade}")
        expected = module.g(0, F(sign, 32))
        if old[5][12] != {(): expected}:
            fail(("n4 fixture terminal", sign, old[5][12], expected))
        result[f"n4_sign_{sign}"] = "G0_G11_PASS;G12_ROW6_FAIL"

    rank2 = fixture_source(base, module, rows, loads, "n5_rank2")
    rank2_wrong = fixture_source(base, module, rows, loads, "n5_rank2", mutation=True)
    for row_index in range(7):
        for grade in range(13):
            assert_zero(rank2[row_index][grade], f"n5 rank2 row {row_index + 1} G{grade}")
        for grade in range(12):
            assert_zero(rank2_wrong[row_index][grade], f"n5 rank2 mutation row {row_index + 1} G{grade}")
    if all(not rank2_wrong[row_index][12] for row_index in range(7)):
        fail("n5 rank2 G12 mutation invisible")
    result["n5_rank2"] = "G0_G12_PASS;N7_B_-2_TO_-1_FAILS_ONLY_G12"

    for sign in (1, -1):
        rank1 = fixture_source(base, module, rows, loads, "n5_rank1", sign)
        rank1_wrong = fixture_source(
            base, module, rows, loads, "n5_rank1", sign, mutation=True
        )
        for row_index in range(7):
            for grade in range(13):
                assert_zero(rank1[row_index][grade], f"n5 rank1 sign {sign} row {row_index + 1} G{grade}")
            for grade in range(12):
                assert_zero(rank1_wrong[row_index][grade], f"n5 rank1 mutation sign {sign} row {row_index + 1} G{grade}")
        if all(not rank1_wrong[row_index][12] for row_index in range(7)):
            fail(("n5 rank1 G12 mutation invisible", sign))
        result[f"n5_rank1_sign_{sign}"] = "G0_G12_PASS;N7_B_128epsi_TO_127epsi_FAILS_ONLY_G12"
    return result


def main() -> None:
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("custody", path, actual, expected))
    base = load_module(BASE_REPLAY, "k00_e2m2_g12_base")
    module = base.load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    quadrics = [module.dhom(row, 2) for row in rows]
    cubics = [module.dhom(row, 3) for row in rows]
    quartics = [module.dhom(row, 4) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]

    n4_general = general_n4_g12(
        base, module, rows, loads, quadrics, cubics, quartics, m4
    )
    n5_general = general_n5_g12(
        base, module, rows, loads, quadrics, cubics, m4
    )
    terminals = n4_rankone_terminal(base, module, rows, loads)
    controls = fixtures(base, module, rows, loads)

    certificate = {
        "type": "K00-RAM-E2M2-H10EQ1-G12-BRANCH-SPLIT/v1",
        "basis": "0d7544ebd5cb12def6bac892646010301098be3c",
        "dependency": "G11 organization PROVISIONAL; all G12 identities literal from tails",
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "tail_terms": term_count,
        "field": "algebraic closure characteristic zero; displayed controls lie in Q(i)",
        "normalization": "Lambda=tau^2; C6=1; ord(d)=2; ord(k10)=1",
        "opens": ["k10[1]!=0", "Jdet[0]!=0", "d[2]!=0"],
        "general_n4_g12": n4_general,
        "general_n5_g12": n5_general,
        "n4_rankone_terminals": terminals,
        "fixtures": controls,
        "branch_decision": [
            "old n4 rank1 both signs dead at G12",
            "fresh n5 rank2 survives G12",
            "fresh n5 rank1 both signs survive G12",
        ],
        "conclusion": "POINT_SET_NONEMPTY_THROUGH_G12;NEXT_LITERAL_GATE_G13",
        "nonclaims": [
            "complete G13 fan", "formal arc", "lifting", "source reachability",
            "polynomial map", "JC2",
        ],
        "mutations": [
            "custody", "n4 row6 terminal", "n5 rank2 N7 B -2 to -1",
            "n5 rank1 N7 B 128epsi to 127epsi", "capable-slot absence",
        ],
    }
    cert_bytes = (
        json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    cert_sha = sha256(cert_bytes).hexdigest()
    if EXPECTED_CERTIFICATE_SHA256 != "PENDING" and cert_sha != EXPECTED_CERTIFICATE_SHA256:
        fail(("certificate digest", cert_sha, EXPECTED_CERTIFICATE_SHA256))

    print("K00_RAM_E2M2_H10EQ1_G12_BRANCH_SPLIT_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("DEPENDENCY=G11_PROVISIONAL;G12_LITERAL_FROM_569_TAILS")
    print("N4_G12=RANK1_BOTH_SIGNS_DEAD;ROW6=EPS*i*q^3/32")
    print("N5_G12=RANK2_SURVIVES;RANK1_BOTH_SIGNS_SURVIVE")
    print("ARRIVAL=N4_CUBIC_QUARTIC_K10_2_RETAINED;N5_CUBIC_K10_2_RETAINED")
    print("FIXTURE_N5_RANK2=S2=1;P5=1;B6=-4;B7=-2;K10_1=48/5")
    print("FIXTURE_N5_RANK1=S2=8;T2=EPS*i;P5=EPS*8i;Q5=1;A6=16;B6=-EPS*128i;B7=EPS*128i;K10_1=-12/5")
    print("CELL_STATUS=POINT_SET_NONEMPTY_THROUGH_G12;FORMAL_ARC_OPEN;NEXT_GATE_G13")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,N4_ROW6,N5_RANK2_B7,N5_RANK1_B7,CAPABLE_SLOT_ABSENCE")


if __name__ == "__main__":
    main()
