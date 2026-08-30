#!/usr/bin/env python3
"""Desk replay for the D3 sectioned two-support universal dichotomy.

This replay checks only finite arithmetic and the explicit additive local
control.  The geometric inputs (Hodge/discrepancy factorisation, Kodaira
classification, Shioda--Tate, and the morphic rational-forest theorem) remain
report-layer mathematics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from itertools import combinations_with_replacement

import sympy as sp


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-local-control", action="store_true")
    args = parser.parse_args()

    # symbol, minimal discriminant order, root rank, lower v(c4), lower v(c6)
    kodaira = (
        ("II", 2, 0, 1, 1),
        ("III", 3, 1, 1, 2),
        ("IV", 4, 2, 2, 2),
        ("I0*", 6, 4, 2, 3),
        ("I1*", 7, 5, 2, 3),
        ("I2*", 8, 6, 2, 3),
        ("IV*", 8, 6, 3, 4),
        ("I3*", 9, 7, 2, 3),
        ("III*", 9, 7, 3, 5),
        ("I4*", 10, 8, 2, 3),
        ("II*", 10, 8, 4, 5),
    )

    pairs = []
    for left, right in combinations_with_replacement(kodaira, 2):
        delta_sum = left[1] + right[1]
        root_sum = left[2] + right[2]
        if delta_sum <= 12 and root_sum <= 8:
            pairs.append(
                {
                    "types": [left[0], right[0]],
                    "delta_sum": delta_sum,
                    "delta_remainder": 12 - delta_sum,
                    "root_sum": root_sum,
                    "c4_lower_sum": left[3] + right[3],
                    "c6_lower_sum": left[4] + right[4],
                }
            )
    require(len(pairs) == 25, "the refined additive Kodaira-pair count changed")
    require(
        all(row["root_sum"] == row["delta_sum"] - 4 for row in pairs),
        "additive root-rank/discriminant identity failed",
    )

    order_pairs = sorted({tuple(sorted((left[1], right[1]))) for left, right in
                          combinations_with_replacement(kodaira, 2)
                          if left[1] + right[1] <= 12})
    require(len(order_pairs) == 19, "discriminant-order pair count changed")

    forced_c4_zero = [row["types"] for row in pairs if row["c4_lower_sum"] > 4]
    forced_c6_zero = [row["types"] for row in pairs if row["c6_lower_sum"] > 6]
    require(forced_c4_zero == [["II", "II*"], ["IV", "IV*"]],
            "c4 degree-budget exceptions changed")
    require(forced_c6_zero == [["III", "III*"]],
            "c6 degree-budget exception changed")

    j0_types = {"II", "IV", "I0*", "IV*", "II*"}
    j1728_types = {"III", "I0*", "III*"}
    j0_pairs = [row["types"] for row in pairs
                if set(row["types"]) <= j0_types]
    j1728_pairs = [row["types"] for row in pairs
                   if set(row["types"]) <= j1728_types]
    require(len(j0_pairs) == 9, "j=0 pair count changed")
    require(len(j1728_pairs) == 4, "j=1728 pair count changed")

    local_partitions = ((3,), (2, 1), (1, 1, 1))
    marked_cluster_pairs = list(combinations_with_replacement(local_partitions, 2))
    require(len(marked_cluster_pairs) == 6, "marked cluster-pair count changed")
    require(all(sum(a) == sum(b) == 3 for a, b in marked_cluster_pairs),
            "local plane-net mass is not three")
    require((2, 2, 2) not in [tuple(sorted(a + b, reverse=True))
                              for a, b in marked_cluster_pairs],
            "the forbidden unmarked 2+2+2 partition reappeared")

    # CFS Lemma 4.4 leaves these four nontrivial canonical lowering slopes
    # once v(F)=0 rules out (0,0).  For positive a, the weighted exceptional
    # face has degree equal to the sum of weights (a,b,1).
    slopes = ((0, 1), (1, 1), (1, 2), (2, 3))
    require(all(a + b + 1 == sum((a, b, 1)) for a, b in slopes if a > 0),
            "weighted anticanonical identity failed")

    tau, x, y, z = sp.symbols("tau x y z")
    H = y**2 * z - x**3 - tau * x * z**2
    F = sp.expand(tau**3 * H.subs({x: x / tau, y: y / tau}, simultaneous=True))
    expected = tau * y**2 * z - x**3 - tau**3 * x * z**2
    if args.mutate_local_control:
        expected += tau**2 * z**3
    require(sp.expand(F - expected) == 0, "reverse-(1,1) local control identity failed")

    # The total-degree-three tangent cone at [0:0:1], tau=0 is cuspidal.
    affine = sp.expand(F.subs(z, 1))
    tangent = sum(
        coeff * x**i * y**j * tau**k
        for (i, j, k), coeff in sp.Poly(affine, x, y, tau).terms()
        if i + j + k == 3
    )
    require(sp.expand(tangent - (tau * y**2 - x**3)) == 0,
            "additive control tangent cone changed")

    # Its only affine singular point is the origin.  Saturating the gradient
    # ideal by tau shows that no singular point lies over tau != 0.
    q = sp.symbols("q")
    grad = [sp.diff(affine, variable) for variable in (x, y, tau)]
    gb_generic = sp.groebner(grad + [q * tau - 1], q, x, y, tau, order="lex")
    require(len(gb_generic.polys) == 1 and gb_generic.polys[0].as_expr() == 1,
            "generic-fibre singularity appeared")
    require(all(g.subs({x: 0, y: 0, tau: 0}) == 0 for g in grad),
            "declared defect point is not singular")

    # Standard short-Weierstrass ledger for H: a4=tau, a6=0.
    c4 = -48 * tau
    c6 = sp.Integer(0)
    disc = -64 * tau**3
    require(sp.Poly(c4, tau).as_dict() == {(1,): -48}, "minimal c4 changed")
    require(c6 == 0, "minimal c6 changed")
    require(sp.Poly(disc, tau).as_dict() == {(3,): -64},
            "minimal discriminant changed")

    payload = {
        "schema": "jc2.d3-sectioned-two-support-universal-dichotomy/v1",
        "kodaira_pair_count": len(pairs),
        "discriminant_order_pair_count": len(order_pairs),
        "kodaira_pairs": pairs,
        "marked_cluster_pairs": [[list(a), list(b)] for a, b in marked_cluster_pairs],
        "forced_c4_zero_pairs": forced_c4_zero,
        "forced_c6_zero_pairs": forced_c6_zero,
        "j0_pair_count": len(j0_pairs),
        "j1728_pair_count": len(j1728_pairs),
        "cfs_slopes": [list(slope) for slope in slopes],
        "local_additive_control": {
            "minimal_kodaira": "III",
            "minimal_orders": {"c4": 1, "c6": "infinity", "Delta": 3},
            "plane_orders": {"c4": 5, "c6": "infinity", "Delta": 15},
            "tangent_cone": "tau*y^2-x^3 (cuspidal cubic)",
        },
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    envelope = {
        "payload": payload,
        "payload_sha256": hashlib.sha256(encoded).hexdigest(),
        "status": "D3_SECTIONED_TWO_SUPPORT_UNIVERSAL_DICHOTOMY_PASS",
    }
    sys.stdout.write(json.dumps(envelope, sort_keys=True, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # fail closed with a stable short diagnostic
        sys.stderr.write(f"FAIL:{exc}\n")
        raise SystemExit(1)
