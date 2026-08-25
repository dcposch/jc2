#!/usr/bin/env python3
"""Exact rational blow-up tree for selected points of the pinned H curve.

This is a discovery/audit producer.  It follows every F_127-rational tangent
direction until the strict transform is smooth or ``--depth`` is reached.
Non-rational tangent directions cannot contain an F_127-rational branch.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import comb
from pathlib import Path


P = 127
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
Polynomial = dict[tuple[int, int], int]


def clean(poly: Polynomial) -> Polynomial:
    return {key: value % P for key, value in poly.items() if value % P}


def multiplicity(poly: Polynomial) -> int:
    if not poly:
        raise RuntimeError("zero strict transform")
    return min(i + j for i, j in poly)


def tangent_directions(poly: Polynomial) -> tuple[int, list[tuple[str, int]]]:
    order = multiplicity(poly)
    tangent = {(i, j): c for (i, j), c in poly.items() if i + j == order}
    directions: list[tuple[str, int]] = []
    # Finite slopes y=m*x, represented by [x:y]=[1:m].
    for slope in range(P):
        value = sum(c * pow(slope, j, P) for (i, j), c in tangent.items()) % P
        if value == 0:
            directions.append(("finite", slope))
    # The remaining projective direction [0:1], i.e. x=0.
    vertical = sum(c for (i, j), c in tangent.items() if i == 0) % P
    if vertical == 0:
        directions.append(("vertical", 0))
    return order, directions


def blow_up(poly: Polynomial, direction: tuple[str, int]) -> Polynomial:
    order = multiplicity(poly)
    output: defaultdict[tuple[int, int], int] = defaultdict(int)
    kind, slope = direction
    if kind == "finite":
        # x=t, y=t*(slope+u); output coordinates are (t,u).
        for (i, j), coefficient in poly.items():
            t_degree = i + j - order
            if t_degree < 0:
                raise RuntimeError("negative strict-transform exponent")
            for u_degree in range(j + 1):
                output[t_degree, u_degree] += (
                    coefficient
                    * comb(j, u_degree)
                    * pow(slope, j - u_degree, P)
                )
    elif kind == "vertical":
        # y=t, x=t*u; output coordinates are (t,u).
        for (i, j), coefficient in poly.items():
            t_degree = i + j - order
            if t_degree < 0:
                raise RuntimeError("negative strict-transform exponent")
            output[t_degree, i] += coefficient
    else:
        raise RuntimeError(direction)
    return clean(dict(output))


def affine_local(support: dict[str, list[list[int]]], w0: int, v0: int) -> Polynomial:
    output: defaultdict[tuple[int, int], int] = defaultdict(int)
    for raw_v_degree, entries in support.items():
        v_degree = int(raw_v_degree)
        for w_degree, coefficient in entries:
            # H(w0+x,v0+y).
            for x_degree in range(w_degree + 1):
                wx = comb(w_degree, x_degree) * pow(w0, w_degree - x_degree, P)
                if wx % P == 0:
                    continue
                for y_degree in range(v_degree + 1):
                    output[x_degree, y_degree] += (
                        coefficient
                        * wx
                        * comb(v_degree, y_degree)
                        * pow(v0, v_degree - y_degree, P)
                    )
    result = clean(dict(output))
    if result.get((0, 0), 0):
        raise RuntimeError((w0, v0, result[(0, 0)]))
    return result


def corner_local(support: dict[str, list[list[int]]]) -> Polynomial:
    # u^21*z^190*H(1/u,1/z), at (u,z)=(0,0).
    output: defaultdict[tuple[int, int], int] = defaultdict(int)
    for raw_v_degree, entries in support.items():
        v_degree = int(raw_v_degree)
        for w_degree, coefficient in entries:
            output[21 - w_degree, 190 - v_degree] += coefficient
    result = clean(dict(output))
    if result.get((0, 0), 0):
        raise RuntimeError("corner not on projective closure")
    return result


def follow(poly: Polynomial, depth: int, path: list[str], records: list[dict]) -> int:
    order, directions = tangent_directions(poly)
    record = {
        "path": path,
        "depth": len(path),
        "multiplicity": order,
        "term_count": len(poly),
        "rational_tangent_directions": [
            kind if kind == "vertical" else f"slope={slope}"
            for kind, slope in directions
        ],
    }
    records.append(record)
    if order == 1:
        record["status"] = "SMOOTH_RATIONAL_BRANCH"
        return 1
    if not directions:
        record["status"] = "NO_RATIONAL_TANGENT"
        return 0
    if len(path) >= depth:
        record["status"] = "DEPTH_LIMIT"
        return 0
    record["status"] = "BLOW_UP"
    count = 0
    for direction in directions:
        label = direction[0] if direction[0] == "vertical" else f"slope={direction[1]}"
        count += follow(blow_up(poly, direction), depth, path + [label], records)
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--depth", type=int, default=30)
    args = parser.parse_args()
    got = sha256(args.candidate.read_bytes()).hexdigest()
    if got != CANDIDATE_SHA256:
        raise RuntimeError((got, CANDIDATE_SHA256))
    payload = json.loads(args.candidate.read_text())
    support = payload["nonzero_support"]

    centers = {
        "affine_0_42": affine_local(support, 0, 42),
        "affine_39_89": affine_local(support, 39, 89),
        "corner_infinity_infinity": corner_local(support),
    }
    result = {
        "case": "max12_912_order3_nu_q8_p127_candidate_point_count_aws_20260825",
        "status": "PASS",
        "candidate_sha256": got,
        "prime": P,
        "depth_limit": args.depth,
        "centers": {},
    }
    for name, poly in centers.items():
        records: list[dict] = []
        branch_count = follow(poly, args.depth, [name], records)
        result["centers"][name] = {
            "resolved_rational_branch_count": branch_count,
            "all_rational_paths_resolved": all(
                record["status"] != "DEPTH_LIMIT" for record in records
            ),
            "records": records,
        }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
