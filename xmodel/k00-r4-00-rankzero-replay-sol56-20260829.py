#!/usr/bin/env python3
"""Exact frozen-tail replay for the R4-00 effective-rank-zero cell.

This is deliberately narrow.  It reconstructs the seven V20R2 rows from the
frozen 569-tail source, verifies the grade-12 entry and grade-13 transverse
matrix, and follows only U=V=0 through its first obstruction at grade 18.
The imported file supplies only exact sparse-polynomial/series primitives and
the frozen-tail parser; no R4-00 producer output is imported.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[1]
PRIMITIVES = ROOT / "xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py"
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
EXPECTED = {
    PRIMITIVES: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
}


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_primitives():
    spec = importlib.util.spec_from_file_location("k00_r2_exact", PRIMITIVES)
    if spec is None or spec.loader is None:
        fail("cannot load exact arithmetic primitives")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_zero(poly, label: str) -> None:
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def assert_equal(ring, actual, expected, label: str) -> None:
    assert_zero(ring.sub(actual, expected), label)


def product(ring, *factors):
    out = ring.const(1)
    for factor in factors:
        out = ring.mul(out, factor)
    return out


def transverse_vector(m, ring, a, b, u, v, aval, bval):
    """cone(a,b,u,v)+(B,0,0,0,0,A), with A/B kept typed."""
    return m.vector_with_ab(
        ring,
        aval,
        bval,
        a,
        b,
        ring.add(ring.scale(a, 8), v),
        ring.sub(b, u),
    )


def substitute(ring, poly, replacements):
    """Exact polynomial substitution; omitted names remain unchanged."""
    out = ring.const()
    variables = {name: ring.var(name) for name in ring.names}
    for key, coefficient in poly.items():
        term = ring.const(coefficient)
        for name, exponent in zip(ring.names, key):
            if exponent:
                term = ring.mul(
                    term,
                    ring.power(replacements.get(name, variables[name]), exponent),
                )
        out = ring.add(out, term)
    return out


def full_rows(m, rows, loads, coefficients, source, ring, truncation):
    """Evaluate unloaded rows plus all three shifted load families."""
    dseries = []
    for entries in coefficients:
        series = m.series_zero(truncation)
        for grade, value in entries.items():
            if grade < truncation:
                series[grade] = value
        dseries.append(series)

    shifted_loads = {}
    for label, shift in (("K10", 2), ("K6", 6), ("K2", 10)):
        series = m.series_zero(truncation)
        for index, value in source.get(label, {}).items():
            if shift + index < truncation:
                series[shift + index] = value
        shifted_loads[label] = series

    answer = []
    for row_index, unloaded in enumerate(rows):
        total = m.eval_dpoly_series(unloaded, dseries, ring)
        for label in ("K10", "K6", "K2"):
            load = m.eval_dpoly_series(loads[label][row_index], dseries, ring)
            total = m.series_add(
                total,
                m.series_mul(shifted_loads[label], load, ring),
                ring,
            )
        answer.append(total)
    return answer


def entry_and_fan(m, rows, loads):
    names = (
        "s", "t", "s1", "t1", "k", "a", "b", "u", "v", "A", "B",
        "a7", "b7", "u7", "v7", "A7", "B7", "h1",
    )
    ring = m.Ring(names)
    zvar = {name: ring.var(name) for name in names}
    x = m.old_plane(ring, zvar["s"], zvar["t"])
    y = m.old_plane(ring, zvar["s1"], zvar["t1"])
    z = transverse_vector(
        m, ring, zvar["a"], zvar["b"], zvar["u"], zvar["v"],
        zvar["A"], zvar["B"],
    )
    z7 = transverse_vector(
        m, ring, zvar["a7"], zvar["b7"], zvar["u7"], zvar["v7"],
        zvar["A7"], zvar["B7"],
    )
    coefficients = [
        {4: x[index], 5: y[index], 6: z[index], 7: z7[index]}
        for index in range(6)
    ]
    equations = full_rows(
        m,
        rows,
        loads,
        coefficients,
        {"K10": {0: zvar["k"], 1: zvar["h1"]}},
        ring,
        14,
    )

    s, t, k = (zvar[name] for name in ("s", "t", "k"))
    u, v, A, B = (zvar[name] for name in ("u", "v", "A", "B"))
    kold = ring.mul(k, ring.add(ring.mul(s, A), ring.mul(t, B)))
    uv = ring.sub(ring.mul(u, A), ring.mul(v, B))
    bracket = ring.linear((F(5, 2048), kold), (F(3, 1024), uv))
    expected12 = [
        ring.add(bracket, ring.mul(A, B), F(-3, 2048)),
        ring.linear(
            (F(5, 32768), product(ring, k, s, B)),
            (F(-5, 512), product(ring, k, t, A)),
            (F(3, 16384), ring.mul(u, B)),
            (F(3, 256), ring.mul(v, A)),
            (F(15, 2048), ring.power(A, 2)),
        ),
        ring.add(ring.scale(bracket, F(-1, 8)), ring.mul(A, B), F(3, 8192)),
        ring.linear(
            (F(-3, 8192), ring.power(A, 2)),
            (F(3, 524288), ring.power(B, 2)),
        ),
        ring.add(ring.scale(bracket, F(-1, 128)), ring.mul(A, B), F(-3, 262144)),
        ring.const(),
        ring.scale(bracket, F(-1, 1024)),
    ]
    for index in range(7):
        assert_equal(ring, equations[index][12], expected12[index], f"grade12 row {index + 1}")

    c31 = ring.add(equations[2][12], equations[0][12], F(1, 8))
    assert_equal(ring, c31, ring.scale(ring.mul(A, B), F(3, 16384)), "grade12 AB certificate")
    assert_equal(
        ring,
        equations[3][12],
        ring.scale(ring.sub(ring.power(B, 2), ring.scale(ring.power(A, 2), 64)), F(3, 524288)),
        "grade12 square certificate",
    )
    a_cube_rhs = ring.scale(
        ring.sub(
            ring.scale(ring.mul(B, c31), F(16384, 3)),
            ring.scale(ring.mul(A, equations[3][12]), F(524288, 3)),
        ),
        F(1, 64),
    )
    b_cube_rhs = ring.add(
        ring.scale(ring.mul(B, equations[3][12]), F(524288, 3)),
        ring.scale(ring.mul(A, c31), F(1048576, 3)),
    )
    assert_equal(ring, a_cube_rhs, ring.power(A, 3), "grade12 A cube certificate")
    assert_equal(ring, b_cube_rhs, ring.power(B, 3), "grade12 B cube certificate")

    solved = {"A": ring.const(), "B": ring.const()}
    grade13 = [substitute(ring, equation[13], solved) for equation in equations]
    p = ring.linear((6, u), (5, ring.mul(k, s)))
    q = ring.linear((-6, v), (5, ring.mul(k, t)))
    row1 = ring.scale(
        ring.add(ring.mul(p, zvar["A7"]), ring.mul(q, zvar["B7"])),
        F(1, 2048),
    )
    row2 = ring.scale(
        ring.add(
            ring.scale(ring.mul(q, zvar["A7"]), -4),
            ring.scale(ring.mul(p, zvar["B7"]), F(1, 16)),
        ),
        F(1, 2048),
    )
    expected13 = [
        row1,
        row2,
        ring.scale(row1, F(-1, 8)),
        ring.const(),
        ring.scale(row1, F(-1, 128)),
        ring.const(),
        ring.scale(row1, F(-1, 1024)),
    ]
    for index in range(7):
        assert_equal(ring, grade13[index], expected13[index], f"grade13 row {index + 1}")
    determinant = ring.sub(
        ring.mul(ring.scale(p, F(1, 2048)), ring.scale(p, F(1, 32768))),
        ring.mul(ring.scale(q, F(1, 2048)), ring.scale(q, F(-1, 512))),
    )
    assert_equal(
        ring,
        determinant,
        ring.scale(ring.add(ring.power(p, 2), ring.scale(ring.power(q, 2), 64)), F(1, 2**26)),
        "grade13 determinant",
    )
    return {"grade12_terms": tuple(len(equations[index][12]) for index in range(7))}


def rank_zero_rows(m, rows, loads):
    # These are exactly the source variables that can arrive in G_*,<=18 on
    # this stratum.  Extra compiler columns have grade too high to contribute.
    names = ["s", "t", "k", "s1", "t1", "a6", "b6"]
    for grade in range(7, 13):
        names += [f"a{grade}", f"b{grade}", f"u{grade}", f"v{grade}", f"A{grade}", f"B{grade}"]
    names += [f"h{j}" for j in range(1, 9)]
    names += [f"n{j}" for j in range(1, 5)]
    names += [f"r{j}" for j in range(1, 5)]
    ring = m.Ring(tuple(names))
    zvar = {name: ring.var(name) for name in names}
    s, t, k = (zvar[name] for name in ("s", "t", "k"))
    x = m.old_plane(ring, s, t)
    y = m.old_plane(ring, zvar["s1"], zvar["t1"])
    u6 = ring.scale(product(ring, k, s), F(-5, 6))
    v6 = ring.scale(product(ring, k, t), F(5, 6))
    z6 = m.cone_vector(ring, zvar["a6"], zvar["b6"], u6, v6)
    coefficients = [{} for _ in range(6)]
    for index in range(6):
        coefficients[index][4] = x[index]
        coefficients[index][5] = y[index]
        coefficients[index][6] = z6[index]
    for grade in range(7, 13):
        value = transverse_vector(
            m,
            ring,
            zvar[f"a{grade}"], zvar[f"b{grade}"],
            zvar[f"u{grade}"], zvar[f"v{grade}"],
            zvar[f"A{grade}"], zvar[f"B{grade}"],
        )
        for index in range(6):
            coefficients[index][grade] = value[index]
    source = {
        "K10": {0: k, **{j: zvar[f"h{j}"] for j in range(1, 9)}},
        "K6": {j: zvar[f"n{j}"] for j in range(1, 5)},
        "K2": {j: zvar[f"r{j}"] for j in range(1, 5)},
    }
    equations = full_rows(m, rows, loads, coefficients, source, ring, 19)

    # U=u6+5ks/6 and V=v6-5kt/6 are zero by construction.  Therefore grade
    # 13 has no transverse image even before A7,B7 are forced.
    for index in range(7):
        assert_zero(equations[index][13], f"rankzero grade13 row {index + 1}")

    c31_14 = ring.add(equations[2][14], equations[0][14], F(1, 8))
    c51_14 = ring.add(equations[4][14], equations[0][14], F(1, 128))
    c71_14 = ring.add(equations[6][14], equations[0][14], F(1, 1024))
    a7, b7 = zvar["A7"], zvar["B7"]
    assert_equal(ring, c31_14, ring.scale(ring.mul(a7, b7), F(3, 16384)), "R0 grade14 c31")
    assert_equal(ring, c51_14, ring.scale(ring.mul(a7, b7), F(-3, 131072)), "R0 grade14 c51")
    assert_equal(ring, c71_14, ring.scale(ring.mul(a7, b7), F(-3, 2097152)), "R0 grade14 c71")
    assert_equal(
        ring,
        equations[3][14],
        ring.scale(ring.sub(ring.power(b7, 2), ring.scale(ring.power(a7, 2), 64)), F(3, 524288)),
        "R0 grade14 row4 certificate",
    )
    assert_zero(equations[5][14], "R0 grade14 row6")

    force7 = {"A7": ring.const(), "B7": ring.const()}
    f1 = ring.linear(
        (27, ring.power(s, 2)),
        (100, product(ring, s, ring.power(k, 2))),
        (-576, ring.power(t, 2)),
    )
    f2 = ring.linear(
        (9, ring.power(s, 3)),
        (50, product(ring, ring.power(s, 2), ring.power(k, 2))),
        (-1728, product(ring, s, ring.power(t, 2))),
        (-3200, product(ring, ring.power(t, 2), ring.power(k, 2))),
    )
    grade14 = [substitute(ring, equation[14], force7) for equation in equations]
    assert_equal(
        ring,
        grade14[0],
        ring.scale(product(ring, k, t, f1), F(5, 36864)),
        "R0 grade14 source row1",
    )
    assert_equal(
        ring,
        grade14[1],
        ring.scale(ring.mul(k, f2), F(5, 589824)),
        "R0 grade14 source row2",
    )
    identity = ring.sub(
        ring.sub(ring.scale(f2, 576), ring.mul(ring.linear((1728, s), (3200, ring.power(k, 2))), f1)),
        ring.scale(product(ring, s, ring.power(ring.linear((9, s), (25, ring.power(k, 2))), 2)), -512),
    )
    assert_zero(identity, "ray decomposition identity")

    k2 = ring.power(k, 2)
    rays = {
        "P0": {
            "s": ring.scale(k2, F(-50, 9)),
            "t": ring.const(),
        },
        "P+": {
            "s": ring.scale(k2, F(-25, 9)),
            "t": ring.scale(k2, m.g(0, F(25, 72))),
        },
        "P-": {
            "s": ring.scale(k2, F(-25, 9)),
            "t": ring.scale(k2, m.g(0, F(-25, 72))),
        },
    }

    c31_16 = ring.add(equations[2][16], equations[0][16], F(1, 8))
    a8, b8 = zvar["A8"], zvar["B8"]
    expected_c31_16 = ring.scale(ring.mul(a8, b8), F(3, 16384))
    expected_row4_16 = ring.scale(
        ring.sub(ring.power(b8, 2), ring.scale(ring.power(a8, 2), 64)),
        F(3, 524288),
    )
    for label, ray in rays.items():
        replacements = {**force7, **ray}
        for index in range(7):
            assert_zero(substitute(ring, equations[index][14], replacements), f"{label} grade14 row {index + 1}")
        assert_equal(
            ring,
            substitute(ring, c31_16, replacements),
            expected_c31_16,
            f"{label} grade16 c31",
        )
        assert_equal(
            ring,
            substitute(ring, equations[3][16], replacements),
            expected_row4_16,
            f"{label} grade16 row4",
        )

    force78 = {**force7, "A8": ring.const(), "B8": ring.const()}
    row6_18 = substitute(ring, equations[5][18], force78)
    expected18 = ring.linear(
        (F(-25, 2048), product(ring, ring.power(t, 4), k)),
        (F(125, 36864), product(ring, s, ring.power(t, 2), ring.power(k, 3))),
        (F(75, 65536), product(ring, ring.power(s, 2), ring.power(t, 2), k)),
        (F(-125, 7077888), product(ring, ring.power(s, 3), ring.power(k, 3))),
        (F(-25, 8388608), product(ring, ring.power(s, 4), k)),
    )
    assert_equal(ring, row6_18, expected18, "R0 generic grade18 row6")
    units = {
        "P0": ring.scale(ring.power(k, 9), F(1953125, 10319560704)),
        "P+": ring.scale(ring.power(k, 9), F(1953125, 20639121408)),
        "P-": ring.scale(ring.power(k, 9), F(1953125, 20639121408)),
    }
    for label, ray in rays.items():
        assert_equal(
            ring,
            substitute(ring, row6_18, ray),
            units[label],
            f"{label} grade18 unit",
        )
    return {"equations": equations, "ring": ring, "rays": rays, "units": units}


def explicit_lifts_and_mutation(m, rows, loads):
    """Exhibit full raw lifts through 17, then require the grade-18 unit."""
    mutation_key = None
    for label, sval, tval, h2val, mu2val in (
        ("P0", m.g(F(-50, 9)), m.g(), m.g(), m.g(F(-390625, 35831808))),
        ("P+", m.g(F(-25, 9)), m.g(0, F(25, 72)), m.g(F(5, 6)), m.g()),
        ("P-", m.g(F(-25, 9)), m.g(0, F(-25, 72)), m.g(F(5, 6)), m.g()),
    ):
        ring = m.Ring(("k",))
        k = ring.var("k")
        k2 = ring.power(k, 2)
        s = ring.scale(k2, sval)
        t = ring.scale(k2, tval)
        u = ring.scale(product(ring, k, s), F(-5, 6))
        v = ring.scale(product(ring, k, t), F(5, 6))
        x = m.old_plane(ring, s, t)
        z = m.cone_vector(ring, ring.const(), ring.const(), u, v)
        coefficients = [{4: x[index], 6: z[index]} for index in range(6)]
        source = {"K10": {0: k}}
        if h2val != m.g():
            source["K10"][2] = ring.scale(k2, h2val)
        equations = full_rows(m, rows, loads, coefficients, source, ring, 19)
        # Target sign in the frozen compiler is -Lambda^14*mu2.  Only P0
        # needs mu2_2; all other target coefficients through grade 17 are 0.
        equations[1][16] = ring.add(
            equations[1][16],
            ring.scale(ring.power(k, 8), mu2val),
            -1,
        )
        for grade in range(18):
            for index in range(7):
                assert_zero(equations[index][grade], f"{label} lift row {index + 1} grade {grade}")
        expected = ring.scale(
            ring.power(k, 9),
            F(1953125, 10319560704) if label == "P0" else F(1953125, 20639121408),
        )
        assert_equal(ring, equations[5][18], expected, f"{label} explicit grade18")

        if label == "P0":
            # Deterministic in-memory source mutation: perturb one existing
            # reconstructed row-6 coefficient that actually reaches grade 18.
            for key in sorted(rows[5]):
                mutated_rows = list(rows)
                mutated_row6 = dict(rows[5])
                mutated_row6[key] += F(1)
                mutated_rows[5] = mutated_row6
                bad = full_rows(m, mutated_rows, loads, coefficients, source, ring, 19)[5][18]
                if bad != equations[5][18]:
                    mutation_key = key
                    break
            if mutation_key is None:
                fail("no grade18-sensitive row6 mutation found")
    return mutation_key


def main() -> None:
    started = time.time()
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("custody", str(path), actual, expected))
    m = load_primitives()
    rows, loads, term_count = m.reconstruct_rows()
    if term_count != 569:
        fail(("tail census", term_count))
    entry = entry_and_fan(m, rows, loads)
    rank_zero_rows(m, rows, loads)
    mutation_key = explicit_lifts_and_mutation(m, rows, loads)
    print("R4-00 EFFECTIVE-RANK-ZERO REPLAY PASS")
    print("tails=569; grade12_terms=", entry["grade12_terms"])
    print("grade13_matrix=p,q fan; rankzero_rays=P0,P+,P-")
    print("first_obstruction=grade18_row6; mutation_key=", mutation_key)
    print(f"runtime_seconds={time.time() - started:.3f}")


if __name__ == "__main__":
    main()
