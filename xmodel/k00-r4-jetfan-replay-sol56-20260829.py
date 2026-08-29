#!/usr/bin/env python3
"""Exact desk replay for the provisional V20R2 valuation-four jet fan.

The arithmetic primitives and frozen-tail parser are imported from the pinned
valuation-two replay.  That import is custody-checked before it is used.  No
CAS, network service, AWS job, or file write is performed.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[1]
R2_REPLAY = ROOT / "xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py"
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
    R2_REPLAY: "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    COMPILER: "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b",
}


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_primitives():
    spec = importlib.util.spec_from_file_location("k00_r2_pinned", R2_REPLAY)
    if spec is None or spec.loader is None:
        fail("cannot load pinned arithmetic primitives")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def vec(m, ring, a, b, u, v, aval=None, bval=None):
    """Coordinates (a,b,u,v,A,B), agreeing with the leading-cone chart."""
    aval = ring.const(0) if aval is None else aval
    bval = ring.const(0) if bval is None else bval
    return m.vector_with_ab(
        ring,
        aval,
        bval,
        a,
        b,
        ring.add(ring.scale(a, 8), v),
        ring.sub(b, u),
    )


def full_rows(m, rows, loads, coefficients, source, ring, truncation):
    dseries = []
    for entries in coefficients:
        series = m.series_zero(truncation)
        for grade, value in entries.items():
            series[grade] = value
        dseries.append(series)

    def shifted(entries, amount):
        series = m.series_zero(truncation)
        for grade, value in entries.items():
            if grade + amount < truncation:
                series[grade + amount] = value
        return series

    kseries = {
        "K10": shifted(source.get("K10", {}), 2),
        "K6": shifted(source.get("K6", {}), 6),
        "K2": shifted(source.get("K2", {}), 10),
    }
    answer = []
    for index, unloaded in enumerate(rows):
        total = m.eval_dpoly_series(unloaded, dseries, ring)
        for label in ("K10", "K6", "K2"):
            load = m.eval_dpoly_series(loads[label][index], dseries, ring)
            total = m.series_add(
                total, m.series_mul(kseries[label], load, ring), ring
            )
        answer.append(total)
    return answer


def assert_zero(poly, label):
    if poly:
        fail((label, len(poly), next(iter(poly.items()))))


def assert_equal(ring, left, right, label):
    assert_zero(ring.sub(left, right), label)


def leading_maps(m, rows, loads):
    ring = m.Ring(("a", "b", "u", "v", "K"))
    a, b, u, v, kappa = (ring.var(name) for name in ring.names)
    x = m.cone_vector(ring, a, b, u, v)
    q2 = [m.dhom(row, 2) for row in rows]
    m2 = [m.dhom(row, 2) for row in loads["K10"]]
    alpha = [m.eval_dpoly(m.dderivative(q, 5), x, ring) for q in q2]
    beta = [m.eval_dpoly(m.dderivative(q, 0), x, ring) for q in q2]
    mvals = [m.eval_dpoly(q, x, ring) for q in m2]
    for index in range(7):
        assert_zero(m.eval_dpoly(q2[index], x, ring), f"Q cone row {index + 1}")
        expected = ring.add(
            ring.mul(alpha[index], ring.scale(v, F(-10, 3))),
            ring.mul(beta[index], ring.scale(u, F(10, 3))),
        )
        assert_equal(ring, mvals[index], expected, f"M2 image row {index + 1}")
    return q2, m2


def leading_rank_two(m, rows, loads):
    names = ("a", "b", "u", "v", "K", "ya", "yb", "yu", "yv",
             "za", "zb", "zu", "zv", "h")
    ring = m.Ring(names)
    var = {name: ring.var(name) for name in names}
    x = m.cone_vector(ring, var["a"], var["b"], var["u"], var["v"])
    y = m.cone_vector(ring, var["ya"], var["yb"], var["yu"], var["yv"])
    az = ring.scale(ring.mul(var["K"], var["v"]), F(10, 3))
    bz = ring.scale(ring.mul(var["K"], var["u"]), F(-10, 3))
    z = vec(m, ring, var["za"], var["zb"], var["zu"], var["zv"], az, bz)
    coeff = [{4: x[i], 5: y[i], 6: z[i]} for i in range(6)]
    equations = full_rows(
        m, rows, loads, coeff, {"K10": {0: var["K"], 1: var["h"]}},
        ring, 13,
    )
    g12 = [equation[12] for equation in equations]

    h6 = ring.scale(
        ring.mul(
            var["u"],
            ring.sub(ring.scale(ring.mul(var["v"], var["v"]), 192),
                     ring.mul(var["u"], var["u"])),
        ),
        F(1, 65536),
    )
    h4core = ring.linear(
        (1, ring.power(var["u"], 3)),
        (-448, ring.mul(var["u"], ring.power(var["v"], 2))),
        (64, ring.mul(var["b"], ring.power(var["v"], 2))),
        (-1, ring.mul(var["b"], ring.power(var["u"], 2))),
        (-1024, ring.mul(ring.mul(var["a"], var["u"]), var["v"])),
    )
    h4 = ring.add(
        ring.scale(h4core, F(3, 32768)),
        ring.scale(
            ring.mul(
                ring.mul(var["K"], var["K"]),
                ring.sub(ring.scale(ring.mul(var["v"], var["v"]), 64),
                         ring.mul(var["u"], var["u"])),
            ),
            F(25, 131072),
        ),
    )
    assert_equal(ring, g12[5], h6, "rank2 grade12 row6")
    assert_equal(ring, g12[3], h4, "rank2 grade12 row4")
    mutated_h6 = ring.scale(
        ring.mul(
            var["u"],
            ring.sub(ring.scale(ring.mul(var["v"], var["v"]), 193),
                     ring.mul(var["u"], var["u"])),
        ),
        F(1, 65536),
    )
    if not ring.sub(g12[5], mutated_h6):
        fail("vacuous 192-to-193 row-six mutation")

    # u=0: the two displayed cokernel rows force v+3a=v+2a=0.
    zero_u = ("u",)
    c3 = ring.add(g12[2], g12[0], F(1, 8))
    c5 = ring.add(g12[4], g12[0], F(1, 128))
    expected3 = ring.scale(
        ring.mul(ring.power(var["v"], 2),
                 ring.add(var["v"], ring.scale(var["a"], 3))), F(1, 4)
    )
    expected5 = ring.scale(
        ring.mul(ring.power(var["v"], 2),
                 ring.add(var["v"], ring.scale(var["a"], 2))), F(-3, 64)
    )
    assert_equal(ring, ring.zero_vars(c3, zero_u), expected3, "u0 c3")
    assert_equal(ring, ring.zero_vars(c5, zero_u), expected5, "u0 c5")

    # On u^2=192v^2 the exact four projection rows have RREF
    # v=0, a=0, b=-(25/12)K^2.  Verify the rational quadratic-field RREF.
    QP = tuple[F, F]

    def qa(x=0, y=0): return F(x), F(y)
    def qadd(x: QP, y: QP): return x[0] + y[0], x[1] + y[1]
    def qmul(x: QP, y: QP):
        return x[0] * y[0] + 192 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]
    def qinv(x: QP):
        den = x[0] * x[0] - 192 * x[1] * x[1]
        return x[0] / den, -x[1] / den
    def qdiv(x: QP, y: QP): return qmul(x, qinv(y))

    # Columns are (v,a,b,K^2).  These are the five-row minors divided by
    # their common nonzero powers of v; four nonzero rows suffice.
    matrix = [
        [qa(F(-63,524288)), qa(F(-27,131072)), qa(0,F(27,67108864)), qa(0,F(225,268435456))],
        [qa(0,F(-27,8388608)), qa(0,F(-27,2097152)), qa(F(-27,16777216)), qa(F(-225,67108864))],
        [qa(F(135,4194304)), qa(F(27,1048576)), qa(0,F(-27,536870912)), qa(0,F(-225,2147483648))],
        [qa(F(-81,67108864)), qa(F(27,16777216)), qa(0,F(-27,8589934592)), qa(0,F(-225,34359738368))],
    ]
    rank = 0
    pivots = []
    for column in range(4):
        pivot = next((r for r in range(rank, 4) if matrix[r][column] != qa()), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [qdiv(value, scale) for value in matrix[rank]]
        for row in range(4):
            if row != rank and matrix[row][column] != qa():
                scale = matrix[row][column]
                matrix[row] = [
                    qadd(left, (-qmul(scale, right)[0], -qmul(scale, right)[1]))
                    for left, right in zip(matrix[row], matrix[rank])
                ]
        pivots.append(column)
        rank += 1
    if rank != 3 or pivots != [0, 1, 2]:
        fail(("quadratic branch rref", rank, pivots))
    if matrix[2][3] != qa(F(25, 12)):
        fail(("quadratic branch K coefficient", matrix[2]))


def rank_one_row6(m, rows, loads, shift, old_plane_prefix):
    """Check the universal +/- rank-one cubic at grade 3*shift."""
    for sign in (1, -1):
        names = (
            "s", "t", "a", "b", "v", "K", "ca", "cb", "cu", "cv",
            "za", "zb", "zu", "zv", "tau", "b1", "c1",
        )
        ring = m.Ring(names)
        var = {name: ring.var(name) for name in names}
        u = ring.scale(var["v"], m.g(0, 8 * sign))
        lead = m.cone_vector(ring, var["a"], var["b"], u, var["v"])
        coeff = [{} for _ in range(6)]
        if old_plane_prefix:
            prefix = m.old_plane(ring, var["s"], var["t"])
            for index in range(6):
                coeff[index][4] = prefix[index]
        for index in range(6):
            coeff[index][shift] = lead[index]

        # The coefficient immediately after a rank-one cone point is forced
        # onto the cone by the preceding cokernel equations.  The following
        # coefficient has one transverse freedom tau in addition to the
        # particular K10 correction.  Including all of these variables makes
        # the row-six unit an identity, rather than a zero-tail sample.
        cone_next = m.cone_vector(
            ring, var["ca"], var["cb"], var["cu"], var["cv"]
        )
        correction_a = ring.add(
            ring.scale(ring.mul(var["K"], var["v"]), F(10, 3)),
            var["tau"],
        )
        correction_b = ring.add(
            ring.scale(
                ring.mul(var["K"], var["v"]),
                m.g(0, F(-80 * sign, 3)),
            ),
            ring.scale(var["tau"], m.g(0, 8 * sign)),
        )
        correction = vec(
            m, ring, var["za"], var["zb"], var["zu"], var["zv"],
            correction_a, correction_b,
        )
        for index in range(6):
            coeff[index][shift + 1] = cone_next[index]
            coeff[index][shift + 2] = correction[index]
        source = {"K10": {0: var["K"]}}
        if old_plane_prefix:
            source["K6"] = {0: ring.const(0), 1: var["b1"]}
            source["K2"] = {0: ring.const(0), 1: var["c1"]}
        equations = full_rows(
            m, rows, loads, coeff, source, ring,
            3 * shift + 1,
        )
        actual = equations[5][3 * shift]
        expected = ring.monomial(
            {"v": 3}, m.g(0, F(sign, 32))
        )
        assert_equal(ring, actual, expected, f"rank1 row6 shift {shift} sign {sign}")


def next_rank_two_row6(m, rows, loads):
    """Row-six grade-15 equation on the old-plane/next-cone branch."""
    names = (
        "s", "t", "a", "b", "u", "v", "K", "ca", "cb", "cu", "cv",
        "wa", "wb", "wu", "wv", "b1", "c1",
    )
    ring = m.Ring(names)
    var = {name: ring.var(name) for name in names}
    x = m.old_plane(ring, var["s"], var["t"])
    y = m.cone_vector(ring, var["a"], var["b"], var["u"], var["v"])
    z = m.cone_vector(ring, var["ca"], var["cb"], var["cu"], var["cv"])
    aw = ring.scale(ring.mul(var["K"], var["v"]), F(10, 3))
    bw = ring.scale(ring.mul(var["K"], var["u"]), F(-10, 3))
    w = vec(m, ring, var["wa"], var["wb"], var["wu"], var["wv"], aw, bw)
    coeff = [{4: x[i], 5: y[i], 6: z[i], 7: w[i]} for i in range(6)]
    equations = full_rows(
        m, rows, loads, coeff,
        {
            "K10": {0: var["K"]},
            "K6": {0: ring.const(0), 1: var["b1"]},
            "K2": {0: ring.const(0), 1: var["c1"]},
        },
        ring, 16,
    )
    expected = ring.scale(
        ring.mul(
            var["u"],
            ring.sub(ring.scale(ring.power(var["v"], 2), 192),
                     ring.power(var["u"], 2)),
        ),
        F(1, 65536),
    )
    assert_equal(ring, equations[5][15], expected, "next rank2 row6 grade15")


def main():
    start = time.perf_counter()
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("custody", str(path)))
    m = load_primitives()
    rows, loads, terms = m.reconstruct_rows()
    if terms != 569:
        fail(("tail census", terms))

    degree_ledger = {
        "R": [[d for d in range(1, 7) if m.dhom(row, d)] for row in rows],
        "K10": [[d for d in range(1, 7) if m.dhom(row, d)] for row in loads["K10"]],
        "K6": [[d for d in range(1, 7) if m.dhom(row, d)] for row in loads["K6"]],
        "K2": [[d for d in range(1, 7) if m.dhom(row, d)] for row in loads["K2"]],
    }
    if [min(ds) for ds in degree_ledger["R"]] != [2, 2, 2, 2, 2, 3, 2]:
        fail("unloaded degree ledger")
    if [min(ds) for ds in degree_ledger["K10"]] != [2] * 7:
        fail("K10 degree ledger")
    if [min(ds) for ds in degree_ledger["K6"]] != [1, 1, 1, 2, 1, 2, 1]:
        fail("K6 degree ledger")
    if [min(ds) for ds in degree_ledger["K2"]] != [1] * 7:
        fail("K2 degree ledger")

    leading_maps(m, rows, loads)
    rank_one_row6(m, rows, loads, 4, False)
    leading_rank_two(m, rows, loads)
    rank_one_row6(m, rows, loads, 5, True)
    next_rank_two_row6(m, rows, loads)

    elapsed = time.perf_counter() - start
    print("K00_R4_JETFAN_REPLAY=PASS")
    print("TAIL_TERM_COUNT=569")
    print("LEADING_RANK1_G12=EMPTY")
    print("LEADING_RANK2_G12=EMPTY")
    print("LEADING_RANK0_NEXT_RANK1_G15=EMPTY")
    print("RESIDUAL=LEADING_RANK0_NEXT_RANK0_OR_RANK2")
    print("LITERAL_WINDOW=GRADES_8_THROUGH_19")
    print("MUTATION_CONTROLS=CUSTODY_AND_ROW6_192_TO_193")
    print(f"RUNTIME_SECONDS={elapsed:.6f}")


if __name__ == "__main__":
    main()
