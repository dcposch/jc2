#!/usr/bin/env python3
"""Reproduce the C_FULL_TREE_POLYNOMIAL_ODE u_s>1 census.

This is a bounded, read-only driver for the frozen lane inputs.  It writes no
results file: the complete machine-readable result is emitted as JSON on
stdout.  Hash expectations are read mechanically from the lane receipt.

The grouping convention is the charged one:

    (n, m, (M_2,...,M_s), V_s).

Intermediate V_i are per-row paths and therefore do not enter the group key.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


DEFAULT_INPUTS = Path("/tmp/jc2-lane.7KOQB3/inputs")
DEFAULT_RECEIPT = Path(
    "/home/ubuntu/jc2/xmodel/minor-dichotomy-sol56-20260903.run.v2"
)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def receipt_fields(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in path.read_text().splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    return fields


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_frozen_inputs(inputs: Path, receipt: Path) -> list[dict[str, object]]:
    fields = receipt_fields(receipt)
    count = int(fields["charged_inputs"])
    result = []
    for index in range(1, count + 1):
        basename = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        path = inputs / basename
        actual = sha256(path)
        result.append(
            {
                "basename": basename,
                "expected": expected,
                "actual": actual,
                "ok": actual == expected,
            }
        )
    if not all(item["ok"] for item in result):
        raise SystemExit("frozen input hash mismatch")
    return result


def load_modules(inputs: Path):
    sys.path.insert(0, str(inputs))
    skeleton = importlib.import_module("moh_skeleton_full")
    tree = importlib.import_module("full_tree_partition")
    return skeleton, tree


def group_key(S):
    return (
        S.n,
        S.m,
        tuple(S.M[i] for i in range(2, S.s + 1)),
        S.V[S.s],
    )


def row_key(S):
    return group_key(S) + (
        tuple((i, S.V[i]) for i in range(2, S.s + 1)),
    )


def u_s(S) -> int:
    return S.d[S.s] - S.V[S.s]


def scan(M, FT, dlo: int, dhi: int):
    ode_rows = []
    poly_rows = []
    for n in range(dlo, dhi + 1):
        for m, Ms, V in M.census(n, Kmin=16, full=True):
            S = M.Skel(n, m, list(Ms), V)
            if FT.full_tree_ode_ok(S):
                ode_rows.append(S)
                if FT.full_tree_polynomial_ode_ok(S):
                    poly_rows.append(S)
    return ode_rows, poly_rows


def grouped(rows):
    groups = defaultdict(list)
    for S in rows:
        groups[group_key(S)].append(S)
    return groups


def serialize_group(key, rows):
    S = rows[0]
    us = u_s(S)
    vs = S.V[S.s]
    threshold = Fraction(vs, us)
    return {
        "D": S.n,
        "m": S.m,
        "s": S.s,
        "M_1_to_M_s": [S.M[i] for i in range(1, S.s + 1)],
        "M_2_to_M_s": [S.M[i] for i in range(2, S.s + 1)],
        "d_1_to_d_splus1": [S.d[i] for i in range(1, S.s + 2)],
        "V_2_to_V_s_group_representative": [
            S.V[i] for i in range(2, S.s + 1)
        ],
        "v_s_equals_V_s": vs,
        "u_s_equals_d_s_minus_v_s": us,
        "minor_bound_v_s_over_u_s": fraction_text(threshold),
        # Proposition 6.1 gives only delta* >= 1.  delta* is defined from
        # actual root distances, and is not Skel.delta[s-1].  Thus the
        # skeleton-level sufficient test succeeds exactly when v_s/u_s <= 1.
        "prop61_floor_suffices": threshold <= 1,
        "minor_radius_delta_star": "NOT_IN_SKELETON",
        "prop63_hypothesis_from_skeleton": (
            "HOLDS_BY_PROP6.1_FLOOR" if threshold <= 1 else "UNDETERMINED"
        ),
        "row_count": len(rows),
        "rows": [
            {
                "V_2_to_V_s": [T.V[i] for i in range(2, T.s + 1)],
                "Def5.1_delta_1_to_delta_s": [
                    fraction_text(T.delta[i]) for i in range(1, T.s + 1)
                ],
                "Def5.1_major_delta_sminus1": fraction_text(T.delta[T.s - 1]),
            }
            for T in sorted(
                rows,
                key=lambda item: tuple(item.V[i] for i in range(2, item.s + 1)),
            )
        ],
        "group_key": [S.n, S.m, list(key[2]), key[3]],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, default=DEFAULT_INPUTS)
    parser.add_argument("--receipt", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument("--dlo", type=int, default=48)
    parser.add_argument("--dhi", type=int, default=200)
    parser.add_argument("--focus-dhi", type=int, default=120)
    args = parser.parse_args()

    verification = verify_frozen_inputs(args.inputs, args.receipt)
    M, FT = load_modules(args.inputs)
    ode_rows, poly_rows = scan(M, FT, args.dlo, args.dhi)
    ode_groups = grouped(ode_rows)
    poly_groups = grouped(poly_rows)
    ode_us_rows = [S for S in ode_rows if u_s(S) > 1]
    poly_us_rows = [S for S in poly_rows if u_s(S) > 1]
    ode_us_groups = grouped(ode_us_rows)
    poly_us_groups = grouped(poly_us_rows)

    # Compare full row keys as well as charged group keys when asserting that
    # POLY makes no additional cut in this stratum.
    ode_us_row_keys = {row_key(S) for S in ode_us_rows}
    poly_us_row_keys = {row_key(S) for S in poly_us_rows}
    assert ode_us_row_keys == poly_us_row_keys
    assert set(ode_us_groups) == set(poly_us_groups)

    # Banked fail-closed controls apply to the default charged range.
    controls = {
        "POLY_ODE_rows_1420": len(poly_rows) == 1420,
        "POLY_ODE_groups_686": len(poly_groups) == 686,
        "u_s_gt_1_rows_310": len(poly_us_rows) == 310,
        "u_s_gt_1_groups_177": len(poly_us_groups) == 177,
        "POLY_does_not_cut_u_s_gt_1_rows": ode_us_row_keys == poly_us_row_keys,
        "POLY_does_not_cut_u_s_gt_1_groups": set(ode_us_groups) == set(poly_us_groups),
    }
    if (args.dlo, args.dhi) == (48, 200) and not all(controls.values()):
        raise SystemExit("banked census control failed")

    focus_keys = [key for key in poly_us_groups if key[0] <= args.focus_dhi]
    focus_poly_rows = [S for S in poly_rows if S.n <= args.focus_dhi]
    focus_poly_groups = grouped(focus_poly_rows)
    focus = [
        serialize_group(key, poly_us_groups[key])
        for key in sorted(focus_keys)
    ]
    full_serialized = [
        serialize_group(key, poly_us_groups[key])
        for key in sorted(poly_us_groups)
    ]
    skeleton_decided = sum(
        item["prop61_floor_suffices"] for item in full_serialized
    )
    focus_decided = sum(item["prop61_floor_suffices"] for item in focus)
    threshold_counts = Counter(
        item["minor_bound_v_s_over_u_s"] for item in full_serialized
    )

    payload = {
        "provenance": {
            "inputs": str(args.inputs),
            "receipt": str(args.receipt),
            "verified": all(item["ok"] for item in verification),
            "verified_count": len(verification),
            "module_files": [
                str(Path(M.__file__).resolve()),
                str(Path(FT.__file__).resolve()),
            ],
        },
        "screen": "C_FULL_TREE_POLYNOMIAL_ODE",
        "range": [args.dlo, args.dhi],
        "counts": {
            "POLY_ODE_rows": len(poly_rows),
            "POLY_ODE_groups": len(poly_groups),
            "u_s_gt_1_rows": len(poly_us_rows),
            "u_s_gt_1_groups": len(poly_us_groups),
            "ODE_u_s_gt_1_rows": len(ode_us_rows),
            "ODE_u_s_gt_1_groups": len(ode_us_groups),
        },
        "controls": controls,
        "skeleton_level_decision": {
            "criterion": "Prop6.1 floor delta*>=1 proves Prop6.3 if v_s/u_s<=1",
            "decided_groups": skeleton_decided,
            "total_u_s_gt_1_groups": len(full_serialized),
            "fraction": f"{skeleton_decided}/{len(full_serialized)}",
            "percent": 100 * skeleton_decided / len(full_serialized),
            "threshold_counts": dict(sorted(threshold_counts.items())),
        },
        "focus_D_le": args.focus_dhi,
        "focus": {
            "POLY_ODE_rows": len(focus_poly_rows),
            "POLY_ODE_groups": len(focus_poly_groups),
            "u_s_gt_1_rows": sum(item["row_count"] for item in focus),
            "u_s_gt_1_groups": len(focus),
            "skeleton_decided_groups": focus_decided,
            "fraction": f"{focus_decided}/{len(focus)}",
            "groups": focus,
        },
    }
    json.dump(payload, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
