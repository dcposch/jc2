#!/usr/bin/env python3
"""Desk replay for the cubic block Euler/forest arithmetic.

This script checks only the finite combinatorics consumed by the theorem
report.  It does not certify the cited nonproper-value theorem or the
morphic rational-forest theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def integer_partitions(n: int, maximum: int | None = None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-rank-four", action="store_true")
    parser.add_argument("--mutate-drop-one-place", action="store_true")
    args = parser.parse_args()

    partitions = list(integer_partitions(3))
    if args.mutate_rank_four:
        partitions.append((2, 2))

    fibre_rows = []
    for part in partitions:
        require(sum(part) == 3, "FAIL:cubic fibre length is not three")
        ramified = sum(length >= 2 for length in part)
        require(ramified <= 1, "FAIL:cubic fibre has two ramified points")
        if ramified:
            u = sum(length == 1 for length in part)
            require(u in (0, 1), "FAIL:cubic branch has invalid unramified count")
            fibre_rows.append({"partition": part, "ramified_points": ramified, "u": u})

    forest_checks = 0
    for components in range(1, 13):
        for singular_vertices in range(0, 13):
            for graph_components in range(1, components + 1):
                edges = components + singular_vertices - graph_components
                if edges < 0:
                    continue
                branch_excess = edges - singular_vertices
                normalization_euler = components
                if args.mutate_drop_one_place and components == 1 and singular_vertices == 0:
                    normalization_euler = 0
                curve_euler = normalization_euler - branch_excess
                require(
                    curve_euler == graph_components,
                    "FAIL:one-place normalization is required for forest Euler positivity",
                )
                forest_checks += 1

    a1_solutions = []
    p1_solutions = []
    for branch_components in range(1, 13):
        for sheetless in range(0, 28):
            for ruling_defect in range(0, 28):
                lhs = 2 * branch_components + sheetless + ruling_defect
                if lhs == 2:
                    a1_solutions.append((branch_components, sheetless, ruling_defect))
                if lhs == 1:
                    p1_solutions.append((branch_components, sheetless, ruling_defect))

    require(a1_solutions == [(1, 0, 0)], "FAIL:affine-base survivor arithmetic changed")
    require(p1_solutions == [], "FAIL:projective-base branch survived positive branch Euler")

    payload = {
        "rank": 3,
        "branch_fibre_rows": fibre_rows,
        "forest_checks": forest_checks,
        "a1_solutions": a1_solutions,
        "p1_solutions": p1_solutions,
        "result": "BD-A1-CUBIC-EULER PASS",
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("payload_sha256=" + hashlib.sha256(encoded).hexdigest())
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
