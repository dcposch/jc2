#!/usr/bin/env python3
"""Exact outer Theorem-1.2 bands for the D=108 joint chart.

The coordinate convention is

    K_Q=t^D Q(t^-1,w/t)=sum c[r,q] t^r (w-1)^q.

After the top forms are fixed, q<36 and r+q<=D.  At D2 we use the
primitive weight W=2*r+3*q (the charged report's 4*r+6*q divided by two).
At D1, t=e^8 and w-1=e^12(1+Pi*e), so a coefficient at (r,q)
contributes binomial(q,k) at exponent 8*r+12*q+k = 4*W+k.

Only rational Gaussian elimination is used.  There is no specialization and
no parameter-dependent pivot.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path
from typing import Iterable


# D is the fixed-top slot degree, not the raw degree printed in the design.
SPECS = {
    "A2": (71, 166, 680),
    "A3": (107, 250, 1024),
    "B1": (35, 82, 336),
    "B2": (71, 166, 680),
}


def positions(degree: int) -> list[tuple[int, int]]:
    return [
        (r, q)
        for r in range(degree + 1)
        for q in range(min(35, degree - r) + 1)
    ]


def rational_rank(rows: Iterable[Iterable[int | Fraction]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    if not work:
        return 0
    nrows, ncols = len(work), len(work[0])
    pivot_row = 0
    for column in range(ncols):
        selected = next(
            (index for index in range(pivot_row, nrows) if work[index][column]),
            None,
        )
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        pivot = work[pivot_row][column]
        work[pivot_row] = [value / pivot for value in work[pivot_row]]
        for index in range(nrows):
            if index == pivot_row or not work[index][column]:
                continue
            scalar = work[index][column]
            work[index] = [
                left - scalar * right
                for left, right in zip(work[index], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def rows_at_weight(
    degree: int, weight: int, threshold: int
) -> tuple[list[tuple[int, int]], list[list[int]]]:
    cols = [position for position in positions(degree) if 2 * position[0] + 3 * position[1] == weight]
    rows: list[list[int]] = []
    for k in range(max(0, threshold - 4 * weight)):
        row = [comb(q, k) if q >= k else 0 for _r, q in cols]
        if any(row):
            rows.append(row)
    return cols, rows


def build_audit() -> dict:
    blocks: dict[str, dict] = {}
    redundant_total = 0
    d2_rank_total = 0
    retained_total = 0
    d1_raw_total = 0
    d1_rank_total = 0

    for name, (degree, w0, threshold) in SPECS.items():
        all_positions = positions(degree)
        kept = [p for p in all_positions if 2 * p[0] + 3 * p[1] >= w0]
        deleted = [p for p in all_positions if 2 * p[0] + 3 * p[1] < w0]
        redundant_labels = {
            (8 * r + 12 * q + k, k)
            for r, q in deleted
            for k in range(q + 1)
            if 8 * r + 12 * q + k < threshold
        }
        offset_rows = []
        offset = 0
        while True:
            cols, rows = rows_at_weight(degree, w0 + offset, threshold)
            if not rows and offset >= 4:
                break
            rank = rational_rank(rows)
            offset_rows.append(
                {
                    "offset": offset,
                    "primitive_weight": w0 + offset,
                    "positions": len(cols),
                    "q_values": [q for _r, q in cols],
                    "raw_rows": len(rows),
                    "rank": rank,
                    "dependent_rows": len(rows) - rank,
                }
            )
            offset += 1
        d1_raw = sum(row["raw_rows"] for row in offset_rows)
        d1_rank = sum(row["rank"] for row in offset_rows)
        blocks[name] = {
            "fixed_top_degree": degree,
            "ambient": len(all_positions),
            "D2": {
                "primitive_threshold": w0,
                "strict_coordinate_rows": len(deleted),
                "rank": len(deleted),
                "retained": len(kept),
            },
            "D1": {
                "exponent_threshold": threshold,
                "raw_rows": d1_raw,
                "rank": d1_rank,
                "dependent_rows": d1_raw - d1_rank,
                "offsets": offset_rows,
            },
            "redundant_D1_labels_on_D2_deleted_support": len(redundant_labels),
        }
        redundant_total += len(redundant_labels)
        d2_rank_total += len(deleted)
        retained_total += len(kept)
        d1_raw_total += d1_raw
        d1_rank_total += d1_rank

    stage_offsets = []
    for offset in range(4):
        raw = sum(
            next(row for row in blocks[name]["D1"]["offsets"] if row["offset"] == offset)["raw_rows"]
            for name in SPECS
        )
        rank = sum(
            next(row for row in blocks[name]["D1"]["offsets"] if row["offset"] == offset)["rank"]
            for name in SPECS
        )
        stage_offsets.append({"offset": offset, "raw_rows": raw, "rank": rank})

    result = {
        "type": "EXACT-Q / OUTER-THEOREM-1.2-BANDS / D108",
        "conventions": {
            "basis": "K_Q=t^D Q(t^-1,w/t)=sum c[r,q] t^r (w-1)^q",
            "support": "r>=0, 0<=q<36, r+q<=D",
            "D2_weight": "4*r+6*q; primitive W=2*r+3*q",
            "D1_map": "t=e^8, w-1=e^12*(1+Pi*e)",
            "D1_exponent": "8*r+12*q+k=4*W+k",
            "pivot_field": "Q* only",
        },
        "blocks": blocks,
        "totals": {
            "ambient": sum(block[0] for block in []),
            "fixed_outer_ambient": sum(blocks[name]["ambient"] for name in SPECS),
            "D2_rank": d2_rank_total,
            "retained_after_D2": retained_total,
            "D1_raw_rows": d1_raw_total,
            "D1_rank": d1_rank_total,
            "D1_dependent_rows": d1_raw_total - d1_rank_total,
            "rank_D2_plus_D1": d2_rank_total + d1_rank_total,
            "outer_free_dimension": retained_total - d1_rank_total,
            "redundant_D1_labels_on_D2_deleted_support": redundant_total,
        },
        "primitive_weight_offsets": stage_offsets,
        "controls": {
            "all_ranks_exact_over_Q": True,
            "at_level_D2_coordinates_retained": True,
            "blocks_have_disjoint_coordinates": True,
        },
    }
    # Remove an intentionally empty construction before serialization.
    result["totals"].pop("ambient")

    assert [blocks[name]["ambient"] for name in SPECS] == [1962, 3258, 666, 1962]
    assert [blocks[name]["D2"]["rank"] for name in SPECS] == [1920, 3258, 558, 1920]
    assert [blocks[name]["D1"]["raw_rows"] for name in SPECS] == [40, 0, 12, 40]
    assert [blocks[name]["D1"]["rank"] for name in SPECS] == [21, 0, 12, 21]
    assert result["totals"] == {
        "fixed_outer_ambient": 7848,
        "D2_rank": 7656,
        "retained_after_D2": 192,
        "D1_raw_rows": 92,
        "D1_rank": 54,
        "D1_dependent_rows": 38,
        "rank_D2_plus_D1": 7710,
        "outer_free_dimension": 138,
        "redundant_D1_labels_on_D2_deleted_support": 16057,
    }
    assert [(item["raw_rows"], item["rank"]) for item in stage_offsets] == [
        (40, 20), (28, 16), (16, 10), (8, 8)
    ]
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_audit()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
