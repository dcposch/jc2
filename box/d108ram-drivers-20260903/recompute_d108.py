#!/usr/bin/env python3
"""Recompute D=108 Moh rows and full-tree statuses from frozen charged inputs.

The loader registers the frozen ``moh_skeleton_full.py`` under the exact module
name expected by ``full_tree_partition.py``.  Nothing outside this driver lane
is imported.  The script is read-only apart from its stdout.
"""
from __future__ import annotations

import importlib.util
import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path


INPUTS = Path("/tmp/jc2-lane.ELsjAE/inputs")


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


M = load("moh_skeleton_full", INPUTS / "moh_skeleton_full.py")
T = load("frozen_full_tree_partition", INPUTS / "full_tree_partition.py")


def ftxt(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def row_record(S, group_mixed_hit, group_mixed_capped):
    vals = [(S.V[2], S.q(), S.u)]
    return {
        "n": S.n,
        "m": S.m,
        "s": S.s,
        "M": [S.M[i] for i in range(2, S.s + 1)],
        "V": [S.V[i] for i in range(2, S.s + 1)],
        "d": [S.d[i] for i in range(1, S.s + 2)],
        "descent_u_s": S.d[S.s] - S.V[S.s],
        "integration_capacity_u": ftxt(S.u),
        "delta": [ftxt(S.delta[i]) for i in range(1, S.s + 1)],
        "q": ftxt(S.q()),
        "row_uni_N_6_16": sorted(M.uni_hits(vals, 6, 16)),
        "group_mixed_N_6_16": group_mixed_hit,
        "group_mixed_capped": group_mixed_capped,
        "tree": T.full_tree_ok(S),
        "tree_ode": T.full_tree_ode_ok(S),
        "tree_passport": T.full_tree_passport_ok(S),
        "tree_polynomial": T.full_tree_polynomial_ok(S),
        "tree_polynomial_ode": T.full_tree_polynomial_ode_ok(S),
        "tree_polynomial_passport": T.full_tree_polynomial_passport_ok(S),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="also emit all (1)-(13) rows")
    args = ap.parse_args()
    skeletons = []
    for m, Ms, V in M.census(108, Kmin=16, full=True):
        skeletons.append(M.Skel(108, m, list(Ms), V))
    groups = {}
    for S in skeletons:
        key = (S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])
        groups.setdefault(key, []).append(S)
    group_status = {}
    for key, group in groups.items():
        items = [(S.V[2], S.q(), S.u) for S in group]
        group_status[key] = M.mixed_hit(items, 6, 16)
    rows = []
    for S in skeletons:
        key = (S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])
        hit, capped = group_status[key]
        rows.append(row_record(S, hit, capped))
    rows.sort(key=lambda r: (r["m"], r["M"], r["V"]))
    strong = [r for r in rows if r["tree_polynomial_passport"]]
    selected = [r for r in strong if r["descent_u_s"] == 1]
    payload = {
        "source_moh": str(INPUTS / "moh_skeleton_full.py"),
        "source_tree": str(INPUTS / "full_tree_partition.py"),
        "D": 108,
        "counts": {
            "conditions_1_13_rows": len(rows),
            "descent_u_s_1": sum(r["descent_u_s"] == 1 for r in rows),
            "tree": sum(r["tree"] for r in rows),
            "tree_ode": sum(r["tree_ode"] for r in rows),
            "tree_passport": sum(r["tree_passport"] for r in rows),
            "tree_passport_descent_u_s_1": sum(
                r["tree_passport"] and r["descent_u_s"] == 1 for r in rows
            ),
            "tree_passport_group_mixed": sum(
                r["tree_passport"] and (r["group_mixed_N_6_16"] or r["group_mixed_capped"])
                for r in rows
            ),
            "tree_passport_group_mixed_descent_u_s_1": sum(
                r["tree_passport"] and r["descent_u_s"] == 1
                and (r["group_mixed_N_6_16"] or r["group_mixed_capped"])
                for r in rows
            ),
            "tree_polynomial": sum(r["tree_polynomial"] for r in rows),
            "tree_polynomial_ode": sum(r["tree_polynomial_ode"] for r in rows),
            "tree_polynomial_passport": sum(r["tree_polynomial_passport"] for r in rows),
            "tree_polynomial_passport_descent_u_s_1": len(selected),
        },
        "tree_polynomial_passport_rows": strong,
        "tree_polynomial_passport_descent_u_s_1_rows": selected,
    }
    if args.all:
        payload["all_rows"] = rows
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
