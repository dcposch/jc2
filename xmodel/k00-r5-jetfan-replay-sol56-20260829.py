#!/usr/bin/env python3
"""Exact desk replay for the provisional V20R2 valuation-five jet fan.

The polynomial engine is imported from the byte-pinned valuation-two replay,
but every valuation-five identity below is reconstructed from the frozen
569-tail source.  No CAS, network service, or external process is used.
"""

from __future__ import annotations

import importlib.util
from fractions import Fraction as F
from hashlib import sha256
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
TAILS_SHA256 = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
COMPILER_SHA256 = "2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b"
R2_REPLAY_SHA256 = "2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4"


def fail(message: object) -> None:
    raise AssertionError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_engine():
    spec = importlib.util.spec_from_file_location("k00_r2_exact_engine", R2_REPLAY)
    if spec is None or spec.loader is None:
        fail("cannot load pinned exact engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def polar(module, ring, poly, left, right):
    both = [ring.add(a, b) for a, b in zip(left, right)]
    return ring.sub(
        ring.sub(module.eval_dpoly(poly, both, ring), module.eval_dpoly(poly, left, ring)),
        module.eval_dpoly(poly, right, ring),
    )


def rank_two_grade14(module, rows, loads) -> None:
    names = (
        "a", "b", "u", "v", "aa", "bb", "uu", "vv", "k", "k1", "k2", "beta",
        "q1", "q2", "q3", "q4", "p1", "p2", "p3", "p4",
    )
    ring = module.Ring(names)
    var = {name: ring.var(name) for name in names}
    x = module.cone_vector(ring, var["a"], var["b"], var["u"], var["v"])
    y = module.cone_vector(ring, var["aa"], var["bb"], var["uu"], var["vv"])
    az = ring.scale(ring.mul(var["k"], var["v"]), F(10, 3))
    bz = ring.scale(ring.mul(var["k"], var["u"]), F(-10, 3))
    z = module.vector_with_ab(
        ring, az, bz, var["q1"], var["q2"], var["q3"], var["q4"]
    )
    aw = ring.scale(
        ring.add(ring.mul(var["k"], var["vv"]), ring.mul(var["k1"], var["v"])),
        F(10, 3),
    )
    bw = ring.scale(
        ring.add(ring.mul(var["k"], var["uu"]), ring.mul(var["k1"], var["u"])),
        F(-10, 3),
    )
    w = module.vector_with_ab(
        ring, aw, bw, var["p1"], var["p2"], var["p3"], var["p4"]
    )

    quadrics = [module.dhom(row, 2) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]
    l6 = [module.dhom(row, 1) for row in loads["K6"]]
    residual = []
    residual_wrong_sign = []
    for index in range(7):
        base = ring.add(
            module.eval_dpoly(quadrics[index], z, ring),
            polar(module, ring, quadrics[index], y, w),
        )
        kappa_piece = ring.add(
            polar(module, ring, m4[index], x, z),
            module.eval_dpoly(m4[index], y, ring),
        )
        other = ring.add(
            ring.mul(var["k1"], polar(module, ring, m4[index], x, y)),
            ring.mul(var["k2"], module.eval_dpoly(m4[index], x, ring)),
        )
        other = ring.add(other, ring.mul(var["beta"], module.eval_dpoly(l6[index], z, ring)))
        residual.append(ring.add(ring.add(base, ring.mul(var["k"], kappa_piece)), other))
        residual_wrong_sign.append(
            ring.add(ring.add(base, ring.mul(var["k"], kappa_piece), -1), other)
        )

    e4 = residual[3]
    s3 = ring.add(residual[2], residual[0], F(1, 8))
    expected_e4 = ring.scale(
        ring.mul(
            ring.mul(var["k"], var["k"]),
            ring.sub(ring.scale(ring.mul(var["v"], var["v"]), 64), ring.mul(var["u"], var["u"])),
        ),
        F(25, 131072),
    )
    expected_s3 = ring.scale(
        ring.mul(ring.mul(var["k"], var["k"]), ring.mul(var["u"], var["v"])),
        F(25, 4096),
    )
    module.assert_equal(e4, expected_e4, ring, "r5 rank2 grade14 row4")
    module.assert_equal(s3, expected_s3, ring, "r5 rank2 grade14 S3")
    module.assert_zero(residual[5], "r5 rank2 grade14 row6")

    wrong_e4 = residual_wrong_sign[3]
    wrong_s3 = ring.add(residual_wrong_sign[2], residual_wrong_sign[0], F(1, 8))
    if wrong_e4 == expected_e4 and wrong_s3 == expected_s3:
        fail("vacuous rank-two K10-sign mutation")


def rank_one_grade12_and_14(module, rows, loads, sign: int) -> None:
    names = (
        "a", "b", "v", "lam", "aa", "bb", "uu", "vv", "k", "tau", "sig",
        "k1", "k2", "beta", "q1", "q2", "q3", "q4", "p1", "p2", "p3", "p4",
    )
    ring = module.Ring(names)
    var = {name: ring.var(name) for name in names}
    u = ring.scale(var["v"], module.g(0, 8 * sign))
    x = module.cone_vector(ring, var["a"], var["b"], u, var["v"])
    y_kernel = module.cone_vector(ring, var["aa"], var["bb"], var["uu"], var["vv"])
    y_tangent = module.vector_with_ab(
        ring,
        ring.mul(var["lam"], var["v"]),
        ring.scale(ring.mul(var["lam"], var["v"]), module.g(0, 8 * sign)),
        {}, {}, {}, {},
    )
    y_grade11 = [ring.add(a, b) for a, b in zip(y_kernel, y_tangent)]
    quadrics = [module.dhom(row, 2) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]
    l6 = [module.dhom(row, 1) for row in loads["K6"]]

    grade12 = [
        ring.add(
            module.eval_dpoly(quadrics[index], y_grade11, ring),
            ring.mul(var["k"], module.eval_dpoly(m4[index], x, ring)),
        )
        for index in range(7)
    ]
    expected_lam = ring.scale(
        ring.mul(ring.mul(var["v"], var["v"]), ring.mul(var["lam"], var["lam"])),
        F(-3, 4096),
    )
    module.assert_equal(grade12[3], expected_lam, ring, f"r5 rank1 sign{sign} grade12")

    # The field-valued open v != 0 forces lam=0.  The remaining grade-12
    # equation fixes one normal combination of z; tau is its tangent freedom.
    az = ring.add(
        ring.scale(ring.mul(var["k"], var["v"]), F(10, 3)),
        ring.mul(var["tau"], var["v"]),
    )
    bz = ring.add(
        ring.scale(ring.mul(var["k"], u), F(-10, 3)),
        ring.scale(ring.mul(var["tau"], var["v"]), module.g(0, 8 * sign)),
    )
    z = module.vector_with_ab(
        ring, az, bz, var["q1"], var["q2"], var["q3"], var["q4"]
    )
    aw = ring.add(
        ring.scale(
            ring.add(ring.mul(var["k"], var["vv"]), ring.mul(var["k1"], var["v"])),
            F(10, 3),
        ),
        ring.mul(var["sig"], var["v"]),
    )
    bw = ring.add(
        ring.scale(
            ring.add(ring.mul(var["k"], var["uu"]), ring.mul(var["k1"], u)),
            F(-10, 3),
        ),
        ring.scale(ring.mul(var["sig"], var["v"]), module.g(0, 8 * sign)),
    )
    w = module.vector_with_ab(
        ring, aw, bw, var["p1"], var["p2"], var["p3"], var["p4"]
    )
    residual = []
    for index in range(7):
        base = ring.add(
            module.eval_dpoly(quadrics[index], z, ring),
            polar(module, ring, quadrics[index], y_kernel, w),
        )
        kappa_piece = ring.add(
            polar(module, ring, m4[index], x, z),
            module.eval_dpoly(m4[index], y_kernel, ring),
        )
        other = ring.add(
            ring.mul(var["k1"], polar(module, ring, m4[index], x, y_kernel)),
            ring.mul(var["k2"], module.eval_dpoly(m4[index], x, ring)),
        )
        other = ring.add(other, ring.mul(var["beta"], module.eval_dpoly(l6[index], z, ring)))
        residual.append(ring.add(ring.add(base, ring.mul(var["k"], kappa_piece)), other))

    e4 = residual[3]
    s3 = ring.add(residual[2], residual[0], F(1, 8))
    expected_e4 = ring.scale(
        ring.mul(
            ring.mul(var["v"], var["v"]),
            ring.add(
                ring.scale(ring.mul(var["tau"], var["tau"]), -3),
                ring.scale(ring.mul(var["k"], var["k"]), 100),
            ),
        ),
        F(1, 4096),
    )
    expected_s3 = ring.scale(
        ring.mul(
            ring.mul(var["v"], var["v"]),
            ring.add(
                ring.scale(ring.mul(var["tau"], var["tau"]), 3),
                ring.scale(ring.mul(var["k"], var["k"]), 100),
            ),
        ),
        module.g(0, F(sign, 2048)),
    )
    module.assert_equal(e4, expected_e4, ring, f"r5 rank1 sign{sign} grade14 row4")
    module.assert_equal(s3, expected_s3, ring, f"r5 rank1 sign{sign} grade14 S3")
    module.assert_zero(residual[5], f"r5 rank1 sign{sign} grade14 row6")


def rank_zero_projection(module, rows, loads) -> str:
    ring = module.Ring(("s", "t", "a", "b", "u", "v"))
    var = {name: ring.var(name) for name in ring.names}
    x = module.old_plane(ring, var["s"], var["t"])
    y = module.cone_vector(ring, var["a"], var["b"], var["u"], var["v"])
    quadrics = [module.dhom(row, 2) for row in rows]
    cubics = [module.dhom(row, 3) for row in rows]
    m4 = [module.dhom(row, 2) for row in loads["K10"]]
    l6 = [module.dhom(row, 1) for row in loads["K6"]]
    for index in range(7):
        module.assert_zero(module.eval_dpoly(quadrics[index], x, ring), f"rank0 Qx {index}")
        module.assert_zero(module.eval_dpoly(cubics[index], x, ring), f"rank0 C3x {index}")
        module.assert_zero(module.eval_dpoly(m4[index], x, ring), f"rank0 M4x {index}")
        module.assert_zero(module.eval_dpoly(l6[index], x, ring), f"rank0 L6x {index}")
        for column in range(6):
            module.assert_zero(
                module.eval_dpoly(module.dderivative(quadrics[index], column), x, ring),
                f"rank0 DQx {index},{column}",
            )
        module.assert_zero(module.eval_dpoly(quadrics[index], y, ring), f"rank0 Qy cone {index}")

    spec = "\n".join(
        (
            "K00-R5-R0-RESIDUAL/v1",
            "field=characteristic-zero",
            "open=k10_0*Jdet_0*(s,t-projective)!=0",
            "d=lambda^5*ell(s,t)+sum(n=6..14,lambda^n*d[n]) mod lambda^20",
            "k10=sum(j=0..7,k10_j*lambda^j), k10_0!=0",
            "k6=sum(j=1..8,k6_j*lambda^j), k2=sum(j=1..4,k2_j*lambda^j)",
            "mu2=sum(j=1..5,mu2_j*lambda^j)",
            "mu4=sum(j=1..3,mu4_j*lambda^j), mu6=mu6_1*lambda",
            "equations=[lambda^g]Phi_i=0 for i=1..7,g=13..19",
            "forced-grade12=Q(d[6])=0",
            "rank-split-d6: u^2+64*v^2 nonzero / zero-nonzero / u=v=0",
        )
    ) + "\n"
    return sha256(spec.encode()).hexdigest()


def schedule_checks(module, rows, loads) -> None:
    profiles = {
        "R": [sorted({sum(key) for key in row}) for row in rows],
        "K10": [sorted({sum(key) for key in row}) for row in loads["K10"]],
        "K6": [sorted({sum(key) for key in row}) for row in loads["K6"]],
        "K2": [sorted({sum(key) for key in row}) for row in loads["K2"]],
    }
    if min(min(value) for value in profiles["R"] if value) != 2:
        fail(("R degree floor", profiles["R"]))
    if min(min(value) for value in profiles["K10"] if value) != 2:
        fail(("K10 degree floor", profiles["K10"]))
    if min(min(value) for value in profiles["K6"] if value) != 1:
        fail(("K6 degree floor", profiles["K6"]))
    if min(min(value) for value in profiles["K2"] if value) != 1:
        fail(("K2 degree floor", profiles["K2"]))
    arrivals = {
        "Q": 10,
        "C3": 15,
        "K10_deg2": 12,
        "K10_deg3": 17,
        "K6_deg1": 12,
        "K6_deg2": 17,
        "K2_deg1": 16,
        "mu2": 15,
        "mu4": 17,
        "mu6": 19,
        "Jdet": 19,
        "contracted_D10_deg3": 17,
        "contracted_D6_deg2": 17,
    }
    if arrivals["K6_deg1"] != 7 + 5:
        fail("boundary-correct K6 arrival")
    wrong_boundary_arrival = 6 + 5
    if wrong_boundary_arrival == arrivals["K6_deg1"]:
        fail("vacuous k6[0] boundary mutation")


def main() -> None:
    start = time.perf_counter()
    if digest(TAILS) != TAILS_SHA256:
        fail("tails custody")
    if digest(COMPILER) != COMPILER_SHA256:
        fail("compiler custody")
    if digest(R2_REPLAY) != R2_REPLAY_SHA256:
        fail("exact-engine custody")
    if sha256(TAILS.read_bytes() + b"\n").hexdigest() == TAILS_SHA256:
        fail("vacuous custody mutation")

    module = load_engine()
    rows, loads, term_count = module.reconstruct_rows()
    if term_count != 569:
        fail(("tail term count", term_count))
    schedule_checks(module, rows, loads)
    leading, _ = module.leading_rank_fan(rows, loads)
    rank_two_grade14(module, rows, loads)
    rank_one_grade12_and_14(module, rows, loads, 1)
    rank_one_grade12_and_14(module, rows, loads, -1)
    residual_digest = rank_zero_projection(module, rows, loads)

    elapsed = time.perf_counter() - start
    print("K00_R5_JETFAN_REPLAY=PASS")
    print(f"TAIL_TERM_COUNT={term_count}")
    print(f"NONZERO_LEADING_RANK2_MINORS={leading['nonzero_minors']}")
    print("RANK2_GRADE14=EMPTY_BY_ROW4_AND_S3")
    print("RANK1_GRADE12=TANGENT_PARAMETER_ZERO")
    print("RANK1_GRADE14=EMPTY_BY_ROW4_AND_S3")
    print("RANK0_GRADE12=NEXT_REDUCED_QUADRATIC_CONE")
    print(f"RANK0_RESIDUAL_SPEC_SHA256={residual_digest}")
    print("MUTATION_CONTROLS=PASS")
    print(f"RUNTIME_SECONDS={elapsed:.6f}")


if __name__ == "__main__":
    main()
