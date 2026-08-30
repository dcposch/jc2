#!/usr/bin/env python3
"""Exact G13 closure replay for the K00 e=2,m=2, ord(k10)=1 child.

The program reconstructs all 569 frozen tails.  It derives the literal
fresh-n=5 G13 coefficient, proves two exact cokernel identities which kill
the rank-one and rank-two G12 survivors, and checks old-pass/new-fail
controls.  Arithmetic is stdlib exact Q(i) sparse polynomial arithmetic,
including explicit denominator clearing on the rank-two open.

Every conclusion is about field-valued finite jets.  No recurrence, formal
arc, source reachability, polynomial map, or JC2 conclusion is asserted.
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
G11_INTEGRATION = ROOT / "xmodel/k00-ram-e2m2-h10eq1-g11-coordinator-integration-sol56-20260830.md"
G12_REPORT = ROOT / "xmodel/k00-ram-e2m2-h10eq1-g12-branch-split-producer-sol56-20260830.md"
G12_REPLAY = ROOT / "xmodel/k00-ram-e2m2-h10eq1-g12-branch-split-replay-sol56-20260830.py"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ENGINE: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    BASE_REPLAY: "efd2f4fea4f58ee4783d9b373ee68f2ff191a9923b08bf2ead8dd1c59a4d3749",
    G11_INTEGRATION: "8ba031e87032a007beade2eda7f97f94802eac0bfa561addf90d8f5fb3df8307",
    G12_REPORT: "eda4f40b452ef1f68d53d82ff22c5ec6a4a74147b7f6785b3dc9cc1148137db8",
    G12_REPLAY: "cc8d84f8d5deeb8ee3852901b657e65b7499c397fbff66ba2b8361ad8cd4db15",
}
EXPECTED_CERTIFICATE_SHA256 = "3bb22822763ecdf6cb19e083786fffbd0f1ad4f4a3f83b937f7ef69d8ca4202e"


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


def copy_series(series):
    return [list(row) for row in series]


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


def clear_inverse(poly, ring, inverse_name: str, delta):
    """Return Delta^m*poly|inverse=1/Delta and the used exponent m."""

    inverse_index = ring.index[inverse_name]
    maximum = max((key[inverse_index] for key in poly), default=0)
    out = ring.const()
    for key, coefficient in poly.items():
        exponent = key[inverse_index]
        new_key = list(key)
        new_key[inverse_index] = 0
        term = {tuple(new_key): coefficient}
        term = ring.mul(term, ring.power(delta, maximum - exponent))
        out = ring.add(out, term)
    return out, maximum


def reduce_p4(poly, ring, s_name: str, t_name: str):
    """Remainder for s^4=384*s^2*t^2-4096*t^4, degree_s < 4."""

    s_index = ring.index[s_name]
    t_index = ring.index[t_name]
    work = list(poly.items())
    out = ring.const()
    while work:
        key, coefficient = work.pop()
        if key[s_index] < 4:
            out = ring.add(out, {key: coefficient})
            continue
        base = list(key)
        base[s_index] -= 4
        first = list(base)
        first[s_index] += 2
        first[t_index] += 2
        second = list(base)
        second[t_index] += 4
        work.append((tuple(first), module_global.gmul(coefficient, module_global.g(384))))
        work.append((tuple(second), module_global.gmul(coefficient, module_global.g(-4096))))
    return out


def general_n5_g13(base, module, rows, loads, quadrics, cubics, m4):
    """Literal fresh-n=5 G13 coefficient and complete arrival census."""

    names = (
        "s", "t", "alpha", "beta", "gamma", "eta", "p", "q",
        "k1", "k2", "k3", "k4",
        *(f"n6_{index}" for index in range(6)),
        *(f"n7_{index}" for index in range(6)),
        *(f"n8_{index}" for index in range(6)),
        *(f"n9_{index}" for index in range(6)),
    )
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    surface = base.surface_series(
        module,
        ring,
        {2: x["s"], 3: x["alpha"], 4: x["gamma"]},
        {2: x["t"], 3: x["beta"], 4: x["eta"]},
        14,
    )
    surface_load = [
        module.eval_dpoly_series(row, surface, ring) for row in loads["K10"]
    ]
    dseries = copy_series(surface)
    w = module.cone_vector(
        ring, ring.const(), ring.const(), x["p"], x["q"]
    )
    n6 = [x[f"n6_{index}"] for index in range(6)]
    n7 = [x[f"n7_{index}"] for index in range(6)]
    n8 = [x[f"n8_{index}"] for index in range(6)]
    n9 = [x[f"n9_{index}"] for index in range(6)]
    for grade, vector in ((5, w), (6, n6), (7, n7), (8, n8), (9, n9)):
        base.add_normal(ring, dseries, grade, vector)
    source, load = base.literal_e2_source(
        module,
        rows,
        loads["K10"],
        dseries,
        (ring.const(), x["k1"], x["k2"], x["k3"], x["k4"]),
        ring,
    )

    ell2 = module.old_plane(ring, x["s"], x["t"])
    ell3 = module.old_plane(ring, x["alpha"], x["beta"])
    term_counts = []
    load_counts = []
    for row_index in range(7):
        load6 = surface_load[row_index][6]
        load7 = ring.add(
            base.directional(module, ring, m4[row_index], ell2, w),
            surface_load[row_index][7],
        )
        load8 = ring.add(
            base.directional(module, ring, m4[row_index], ell2, n6),
            ring.add(
                base.directional(module, ring, m4[row_index], ell3, w),
                surface_load[row_index][8],
            ),
        )
        assert_equal(module, ring, load[row_index][6], load6, f"load6 row {row_index + 1}")
        assert_equal(module, ring, load[row_index][7], load7, f"load7 row {row_index + 1}")
        assert_equal(module, ring, load[row_index][8], load8, f"load8 row {row_index + 1}")
        expected = ring.add(
            base.directional(module, ring, quadrics[row_index], w, n8),
            ring.add(
                base.directional(module, ring, quadrics[row_index], n6, n7),
                ring.add(
                    bilinear_hessian(
                        module, ring, cubics[row_index], ell2, w, n6
                    ),
                    ring.add(
                        base.second_half(
                            module, ring, cubics[row_index], ell3, w
                        ),
                        ring.add(
                            ring.mul(x["k1"], load8),
                            ring.add(
                                ring.mul(x["k2"], load7),
                                ring.mul(x["k3"], load6),
                            ),
                        ),
                    ),
                ),
            ),
        )
        assert_equal(
            module, ring, source[row_index][13], expected,
            f"literal fresh-n5 G13 row {row_index + 1}",
        )
        for absent in ("k4", *(f"n9_{index}" for index in range(6))):
            if ring.depends_on(source[row_index][13], absent):
                fail(("spurious G13 dependence", row_index + 1, absent))
        term_counts.append(len(source[row_index][13]))
        load_counts.append((len(load6), len(load7), len(load8)))

    if len(source[5][13]) != 15:
        fail(("row6 first arrival census", len(source[5][13])))
    return {
        "retained": "S2..S4,T2..T4,N5..N9,k10[1..4]",
        "capable": "S2..S4,T2..T4,N5..N8,k10[1..3]",
        "verified_absent": "N9,k10[4]",
        "row_term_counts": term_counts,
        "load6_load7_load8_counts": load_counts,
        "formula": (
            "DQ(N5)[N8]+DQ(N6)[N7]+D2R3(ell2)[N5,N6]+"
            "1/2D2R3(ell3)[N5,N5]+k1*L8+k2*L7+k3*L6"
        ),
        "row6_raw_terms": 15,
    }


def obstruction_identities(base, module, rows, loads):
    """Prove the row-six wall and the rank-two second terminal."""

    # First terminal: an identity before any rank specialization.
    names = (
        "s", "t", "alpha", "beta", "gamma", "eta",
        "p", "q", "k", "k2", "k3", "A", "B", "C", "D",
        *(f"y{index}" for index in range(1, 5)),
        *(f"z{index}" for index in range(1, 5)),
    )
    ring = module.Ring(names)
    x = {name: ring.var(name) for name in names}
    dseries = base.surface_series(
        module,
        ring,
        {2: x["s"], 3: x["alpha"], 4: x["gamma"]},
        {2: x["t"], 3: x["beta"], 4: x["eta"]},
        14,
    )
    w = module.cone_vector(
        ring, ring.const(), ring.const(), x["p"], x["q"]
    )
    n6 = module.vector_with_ab(
        ring, x["A"], x["B"], *(x[f"y{index}"] for index in range(1, 5))
    )
    n7 = module.vector_with_ab(
        ring, x["C"], x["D"], *(x[f"z{index}"] for index in range(1, 5))
    )
    base.add_normal(ring, dseries, 5, w)
    base.add_normal(ring, dseries, 6, n6)
    base.add_normal(ring, dseries, 7, n7)
    source, _ = base.literal_e2_source(
        module, rows, loads["K10"], dseries,
        (ring.const(), x["k"], x["k2"], x["k3"]), ring,
    )
    p4 = ring.add(
        ring.power(x["s"], 4),
        ring.add(
            ring.scale(
                ring.mul(ring.power(x["s"], 2), ring.power(x["t"], 2)),
                -384,
            ),
            ring.scale(ring.power(x["t"], 4), 4096),
        ),
    )
    row6_expected = ring.add(
        ring.scale(ring.mul(x["t"], source[0][11]), F(1, 8)),
        ring.add(
            ring.scale(ring.mul(x["s"], source[1][11]), F(-1, 32)),
            ring.scale(ring.mul(x["k"], p4), F(35, 8388608)),
        ),
    )
    assert_equal(module, ring, source[5][13], row6_expected, "G13 row6 wall identity")

    # Second terminal on D(Delta).  Keep every lower free slot which could
    # contaminate it; the exact reduction cancels all of them.
    names2 = (
        "s", "t", "p", "q", "k", "k2", "k3",
        "alpha", "beta", "gamma", "eta", "di",
        *(f"y{index}" for index in range(1, 5)),
        *(f"z{index}" for index in range(1, 5)),
    )
    rank = module.Ring(names2)
    y = {name: rank.var(name) for name in names2}
    ell_s = y["s"]
    ell_t = y["t"]
    w1 = rank.scale(
        rank.mul(
            ell_t,
            rank.sub(
                rank.scale(rank.power(ell_s, 2), 3),
                rank.scale(rank.power(ell_t, 2), 64),
            ),
        ),
        F(5, 4096),
    )
    w2 = rank.scale(
        rank.mul(
            ell_s,
            rank.sub(
                rank.power(ell_s, 2),
                rank.scale(rank.power(ell_t, 2), 192),
            ),
        ),
        F(5, 65536),
    )
    rhs_u = rank.scale(rank.mul(y["k"], w1), F(-1024, 3))
    rhs_v = rank.scale(rank.mul(y["k"], w2), F(-16384, 3))
    a_num = rank.add(
        rank.mul(y["p"], rhs_u), rank.mul(y["q"], rhs_v)
    )
    b_num = rank.add(
        rank.scale(rank.mul(y["q"], rhs_u), -64),
        rank.mul(y["p"], rhs_v),
    )
    aval = rank.mul(y["di"], a_num)
    bval = rank.mul(y["di"], b_num)
    leading = module.cone_vector(
        rank, rank.const(), rank.const(), y["p"], y["q"]
    )
    tangent = module.vector_with_ab(
        rank, aval, bval, *(y[f"y{index}"] for index in range(1, 5))
    )

    def rank_source(cval=None, dval=None):
        series = base.surface_series(
            module,
            rank,
            {2: y["s"], 3: y["alpha"], 4: y["gamma"]},
            {2: y["t"], 3: y["beta"], 4: y["eta"]},
            14,
        )
        base.add_normal(rank, series, 5, leading)
        base.add_normal(rank, series, 6, tangent)
        if cval is not None:
            next_normal = module.vector_with_ab(
                rank,
                cval,
                dval,
                *(y[f"z{index}"] for index in range(1, 5)),
            )
            base.add_normal(rank, series, 7, next_normal)
        return base.literal_e2_source(
            module,
            rows,
            loads["K10"],
            series,
            (rank.const(), y["k"], y["k2"], y["k3"]),
            rank,
        )[0]

    before_u = rank_source()
    u2 = rank.scale(before_u[0][12], F(-1024, 3))
    v2 = rank.scale(before_u[1][12], F(-16384, 3))
    c_num = rank.add(
        rank.mul(y["p"], u2), rank.mul(y["q"], v2)
    )
    d_num = rank.add(
        rank.scale(rank.mul(y["q"], u2), -64),
        rank.mul(y["p"], v2),
    )
    cval = rank.mul(y["di"], c_num)
    dval = rank.mul(y["di"], d_num)
    solved = rank_source(cval, dval)
    delta = rank.add(
        rank.power(y["p"], 2), rank.scale(rank.power(y["q"], 2), 64)
    )

    # The inverse formulas really solve the two independent G11/G12 rows.
    for row_index in (0, 1):
        numerator, _ = clear_inverse(solved[row_index][11], rank, "di", delta)
        assert_zero(numerator, f"rank2 solved G11 row {row_index + 1}")
        numerator, _ = clear_inverse(solved[row_index][12], rank, "di", delta)
        assert_zero(numerator, f"rank2 solved G12 row {row_index + 1}")

    c3 = rank.add(solved[2][13], solved[0][13], F(1, 8))
    c5 = rank.add(solved[4][13], solved[0][13], F(1, 128))
    terminal_combo = rank.add(c5, c3, F(1, 8))
    cleared, inverse_power = clear_inverse(terminal_combo, rank, "di", delta)
    if inverse_power != 1:
        fail(("unexpected inverse power in second terminal", inverse_power))
    reduced = reduce_p4(cleared, rank, "s", "t")
    terminal = rank.scale(
        rank.mul(
            rank.mul(
                rank.mul(y["k"], y["s"]), y["t"]
            ),
            rank.sub(rank.power(y["s"], 2), rank.scale(rank.power(y["t"], 2), 64)),
        ),
        F(35, 131072),
    )
    assert_equal(
        module,
        rank,
        reduced,
        rank.mul(delta, terminal),
        "rank2 G13 second terminal modulo P4",
    )

    # Check directly that the chosen combination kills every new N8 image.
    image_names = ("p", "q", "A8", "B8", "u1", "u2", "u3", "u4")
    image_ring = module.Ring(image_names)
    z = {name: image_ring.var(name) for name in image_names}
    image_w = module.cone_vector(
        image_ring, image_ring.const(), image_ring.const(), z["p"], z["q"]
    )
    n8 = module.vector_with_ab(
        image_ring,
        z["A8"], z["B8"], z["u1"], z["u2"], z["u3"], z["u4"],
    )
    quadrics = [module.dhom(row, 2) for row in rows]
    image_rows = [
        base.directional(module, image_ring, quad, image_w, n8)
        for quad in quadrics
    ]
    image_combo = image_ring.add(
        image_ring.add(image_rows[4], image_rows[0], F(1, 128)),
        image_ring.add(image_rows[2], image_rows[0], F(1, 8)),
        F(1, 8),
    )
    assert_zero(image_combo, "second terminal annihilates arbitrary N8 image")

    return {
        "P4": poly_object(p4),
        "row6_identity": "G13_6=t*G11_1/8-s*G11_2/32+35*k1*P4/2^23",
        "rank1_substitution": "P4(-epsilon*8*i*t,t)=32768*t^4",
        "rank2_combo": "G13_5+G13_3/8+3*G13_1/128",
        "rank2_terminal_mod_P4": "35*k1*s*t*(s^2-64*t^2)/2^17",
        "rank2_inverse_power": inverse_power,
        "rank2_free_slots_cancelled": (
            "alpha,beta,gamma,eta,k10[2],k10[3],N6-kernel,N7-kernel"
        ),
    }


def sharp_controls(base, module, rows, loads):
    """Q(i) old-pass/new-fail controls on every surviving rank type."""

    controls = {}
    constant_ring = module.Ring(())
    for sign in (1, -1):
        surface = base.surface_series(
            module,
            constant_ring,
            {2: constant_ring.const(8)},
            {2: constant_ring.const(module.g(0, sign))},
            14,
        )
        n5 = module.cone_vector(
            constant_ring,
            constant_ring.const(),
            constant_ring.const(),
            constant_ring.const(module.g(0, 8 * sign)),
            constant_ring.const(1),
        )
        n6 = module.vector_with_ab(
            constant_ring,
            constant_ring.const(16),
            constant_ring.const(module.g(0, -128 * sign)),
            constant_ring.const(), constant_ring.const(),
            constant_ring.const(), constant_ring.const(),
        )
        n7 = module.vector_with_ab(
            constant_ring,
            constant_ring.const(),
            constant_ring.const(module.g(0, 128 * sign)),
            constant_ring.const(), constant_ring.const(),
            constant_ring.const(), constant_ring.const(),
        )
        for grade, vector in ((5, n5), (6, n6), (7, n7)):
            base.add_normal(constant_ring, surface, grade, vector)
        source, _ = base.literal_e2_source(
            module,
            rows,
            loads["K10"],
            surface,
            (constant_ring.const(), constant_ring.const(F(-12, 5))),
            constant_ring,
        )
        for row_index in range(7):
            for grade in range(13):
                assert_zero(
                    source[row_index][grade],
                    f"rank1 sign {sign} row {row_index + 1} G{grade}",
                )
        expected = {(): module.g(F(-21, 64))}
        if source[5][13] != expected:
            fail(("rank1 G13 row6 terminal", sign, source[5][13], expected))
        controls[f"rank1_sign_{sign}"] = "G0_G12_PASS;G13_ROW6=-21/64"

    # The rational rank-two G12 fixture from the parent packet, augmented by
    # the unique image coordinate B(N8)=32 which kills rows 1 and 2 at G13.
    # Row 6 is outside the quadratic N8 image and remains 21/524288.
    ring = module.Ring(())
    surface = base.surface_series(
        module, ring, {2: ring.const(1)}, {2: ring.const()}, 14
    )
    n5 = module.cone_vector(
        ring, ring.const(), ring.const(), ring.const(1), ring.const()
    )
    n6 = module.vector_with_ab(
        ring, ring.const(), ring.const(-4),
        ring.const(), ring.const(), ring.const(), ring.const(),
    )
    n7 = module.vector_with_ab(
        ring, ring.const(), ring.const(-2),
        ring.const(), ring.const(), ring.const(), ring.const(),
    )
    n8 = module.vector_with_ab(
        ring, ring.const(), ring.const(32),
        ring.const(), ring.const(), ring.const(), ring.const(),
    )
    for grade, vector in ((5, n5), (6, n6), (7, n7), (8, n8)):
        base.add_normal(ring, surface, grade, vector)
    source, _ = base.literal_e2_source(
        module, rows, loads["K10"], surface,
        (ring.const(), ring.const(F(48, 5))), ring,
    )
    for row_index in range(7):
        for grade in range(13):
            assert_zero(
                source[row_index][grade],
                f"rank2 rational control row {row_index + 1} G{grade}",
            )
    expected_row6 = {(): module.g(F(21, 524288))}
    for row_index in range(7):
        expected = expected_row6 if row_index == 5 else {}
        if source[row_index][13] != expected:
            fail(("rank2 isolated G13 row6 control", row_index + 1, source[row_index][13]))
    controls["rank2"] = (
        "G0_G12_PASS;N8_B=32;ONLY_G13_ROW6=21/524288"
    )
    return controls


def main() -> None:
    global module_global
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("custody", path, actual, expected))
    base = load_module(BASE_REPLAY, "k00_e2m2_g13_base")
    module = base.load_engine()
    module_global = module
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    quadrics = [module.dhom(row, 2) for row in rows]
    cubics = [module.dhom(row, 3) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]

    general = general_n5_g13(base, module, rows, loads, quadrics, cubics, m4)
    identities = obstruction_identities(base, module, rows, loads)
    controls = sharp_controls(base, module, rows, loads)

    certificate = {
        "type": "K00-RAM-E2M2-H10EQ1-G13-CLOSURE/v1",
        "basis": "a619157b73c1dee1ca0599db47321ffd7588d748",
        "dependency": (
            "old n4 death imported from provisional G12 producer; "
            "fresh n5 G13 closure independently literal"
        ),
        "source": {path.name: expected for path, expected in EXPECTED.items()},
        "tail_terms": term_count,
        "field": "algebraic closure characteristic zero; Q(i) and algebraic exact controls",
        "normalization": "Lambda=tau^2; C6=1; ord(d)=2; ord(k10)=1",
        "opens": ["k10[1]!=0", "Jdet[0]!=0", "d[2]!=0"],
        "general_n5_g13": general,
        "obstruction_identities": identities,
        "controls": controls,
        "branch_decision": [
            "old n4 rank1 both signs dead at G12 (provisional imported dependency)",
            "fresh n5 rank1 both signs dead at G13 by row6 P4 wall",
            "every fresh n5 rank2 G12 survivor dead at G13 by paired P4/second terminal",
            "fresh n5 rank0 dead at G11 (reviewed parent)",
        ],
        "conclusion": (
            "FRESH_N5_EMPTY_AT_G13; CONDITIONAL_ON_G12_PARENT_FULL_H10EQ1_CELL_EMPTY"
        ),
        "nonclaims": [
            "formal arc", "source reachability", "polynomial map", "other h10 face",
            "other (e,m)", "other K00 support", "counterexample", "JC2",
        ],
        "mutations": [
            "custody", "literal G13 formula", "row6 first arrival",
            "rank1 both signs", "rank2 inverse clearing", "rank2 rational control",
            "N8 image annihilation", "capable-slot absence",
        ],
    }
    cert_bytes = (
        json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()
    cert_sha = sha256(cert_bytes).hexdigest()
    if EXPECTED_CERTIFICATE_SHA256 != "PENDING" and cert_sha != EXPECTED_CERTIFICATE_SHA256:
        fail(("certificate digest", cert_sha, EXPECTED_CERTIFICATE_SHA256))

    print("K00_RAM_E2M2_H10EQ1_G13_CLOSURE_REPLAY=PASS")
    print(f"TAIL_TERMS={term_count}")
    print("GENERAL_G13=LITERAL_FRESH_N5;ROWS=51,55,57,33,56,15,51")
    print("ROW6_WALL=P4=s^4-384*s^2*t^2+4096*t^4")
    print("N5_RANK1=BOTH_SIGNS_DEAD_G13;P4=32768*t^4")
    print("N5_RANK2=ALL_G12_SURVIVORS_DEAD_G13;SECOND_TERMINAL=s*t*(s^2-64*t^2)")
    print("CONTROL_RANK1=G0_G12_PASS;G13_ROW6=-21/64;BOTH_SIGNS")
    print("CONTROL_RANK2=G0_G12_PASS;N8_B=32;ONLY_G13_ROW6=21/524288")
    print("CELL_STATUS=FRESH_N5_EMPTY_G13;FULL_H10EQ1_CLOSURE_CONDITIONAL_ON_G12_PARENT")
    print(f"CERTIFICATE_BYTES={len(cert_bytes)}")
    print(f"CERTIFICATE_SHA256={cert_sha}")
    print("MUTATIONS=CUSTODY,G13_FORMULA,ROW6,RANK1_SIGNS,RANK2_INVERSE,RANK2_CONTROL,N8_IMAGE")


module_global = None


if __name__ == "__main__":
    main()
