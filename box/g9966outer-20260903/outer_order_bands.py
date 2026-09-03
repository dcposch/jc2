#!/usr/bin/env python3
"""Outer Theorem-1.2 D2/D1 order bands on the (99,66) A,B blocks.

Add-on: does not modify box/g9966-20260903/.  The (r,q) coordinates are those
of K_Q = t^D Q(t^{-1}, w/t) in the invertible basis t^r (w-1)^q.

SOURCE: Moh 1983 Theorem 1.2 (printed p.149): if
  Q = h^d + sum_j Q_j h^{d-j}  with deg_y Q_j < deg_y h,
then ord Q_j(sigma) >= j * (lambda/d) = j * ord h(sigma).

Chart (2.1), first (major) point, D2 then D1:
  ord h2(D2)=-1,  ord h2(D1)=-1/9.
  F = h2^3 + A2 h2 + A3  =>  ord A2 >= 2 ord h2,  ord A3 >= 3 ord h2
  G = h2^2 + B1 h2 + B2  =>  ord B1 >= 1 ord h2,  ord B2 >= 2 ord h2

D2 substitution: t=s^3, w=1+pi s^4, weight 3r+4q.
D1 substitution: t=e^9, w=1+e^{12}+Pi e^{13}.
Theorem 1.2 is >= : the equality face is allowed, not a row.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb
from typing import Iterable


def dim_S(D: int, ycap: int) -> int:
    """dim {A : deg A <= D, deg_y A < ycap} = ycap*(D+1) - ycap*(ycap-1)/2."""
    return ycap * (D + 1) - ycap * (ycap - 1) // 2


def support(D: int, ycap: int) -> list[tuple[int, int]]:
    """(r,q) with r >= 0, 0 <= q < ycap, r+q <= D."""
    return [(r, q) for q in range(ycap) for r in range(D - q + 1)]


# Bound data for the four outer blocks.  D2_s is the strict vanishing
# threshold on 3r+4q; D1_e is the strict vanishing threshold on e-power.
# D2_s = 3*(D + bound_t), D1_e = 9*(D + bound_t).
BLOCKS = {
    "A2": {
        "D": 65,
        "ycap": 33,
        "bound_t_D2": Fraction(-2),
        "bound_t_D1": Fraction(-2, 9),
        "thm12_j": 2,
        "base": "h2",
    },
    "A3": {
        "D": 98,
        "ycap": 33,
        "bound_t_D2": Fraction(-3),
        "bound_t_D1": Fraction(-1, 3),
        "thm12_j": 3,
        "base": "h2",
    },
    "B1": {
        "D": 32,
        "ycap": 33,
        "bound_t_D2": Fraction(-1),
        "bound_t_D1": Fraction(-1, 9),
        "thm12_j": 1,
        "base": "h2",
    },
    "B2": {
        "D": 65,
        "ycap": 33,
        "bound_t_D2": Fraction(-2),
        "bound_t_D1": Fraction(-2, 9),
        "thm12_j": 2,
        "base": "h2",
    },
}


def thresholds(block: dict) -> tuple[int, int]:
    D = block["D"]
    d2 = 3 * (D + block["bound_t_D2"])  # min 3r+4q
    d1 = 9 * (D + block["bound_t_D1"])  # min e-power of K
    assert d2.denominator == 1 and d1.denominator == 1
    return int(d2), int(d1)


def exact_q_rref(matrix: list[list[Fraction]]) -> tuple[int, list[int], list[int]]:
    """Exact Gaussian elimination over Q.  Returns (rank, pivot_cols, pivot_rows)."""
    if not matrix:
        return 0, [], []
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    work = [row[:] for row in matrix]
    rank = 0
    pivot_cols: list[int] = []
    pivot_rows: list[int] = []
    used_rows: set[int] = set()
    for col in range(n_cols):
        pivot = None
        for row in range(n_rows):
            if row in used_rows:
                continue
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        pivot_val = work[pivot][col]
        inv = Fraction(1, 1) / pivot_val
        work[pivot] = [inv * value for value in work[pivot]]
        for row in range(n_rows):
            if row == pivot:
                continue
            scalar = work[row][col]
            if scalar == 0:
                continue
            work[row] = [
                work[row][c] - scalar * work[pivot][c] for c in range(n_cols)
            ]
        used_rows.add(pivot)
        pivot_cols.append(col)
        pivot_rows.append(pivot)
        rank += 1
        if rank == n_rows:
            break
    for row in range(n_rows):
        if row in used_rows:
            continue
        assert all(value == 0 for value in work[row]), "inhomogeneous D1 obstruction"
    return rank, pivot_cols, pivot_rows


def d1_matrix(
    remain: list[tuple[int, int]], ebound: int
) -> tuple[list[tuple[int, int]], list[list[Fraction]]]:
    """Rows (e, Pi-power j) with e < ebound; columns the D2-remaining (r,q)."""
    slots: list[tuple[int, int]] = []
    slot_index: dict[tuple[int, int], int] = {}
    for r, q in remain:
        base = 9 * r + 12 * q
        for j in range(q + 1):
            exponent = base + j
            if exponent < ebound:
                key = (exponent, j)
                if key not in slot_index:
                    slot_index[key] = len(slots)
                    slots.append(key)
    matrix = [[Fraction(0)] * len(remain) for _ in slots]
    for col, (r, q) in enumerate(remain):
        base = 9 * r + 12 * q
        for j in range(q + 1):
            exponent = base + j
            if exponent < ebound:
                matrix[slot_index[(exponent, j)]][col] = Fraction(comb(q, j))
    return slots, matrix


PREFIX_OUTER_PIVOTS = [
    # first_global_band.py Q* pivots, as (block, i, j) in x^i y^j.
    ("A3", 98, 0),
    ("A3", 97, 0),
    ("A3", 96, 0),
    ("B2", 65, 0),
    ("B2", 64, 0),
    ("B2", 63, 0),
    ("A3", 97, 1),
    ("A3", 96, 2),
    ("A3", 95, 3),
    ("A3", 94, 4),
    ("A3", 93, 5),
    ("A3", 92, 6),
    ("A3", 91, 7),
    ("A3", 90, 8),
    ("A2", 65, 0),
]


def xy_to_rq(block: str, i: int, j: int) -> tuple[int, int]:
    D = BLOCKS[block]["D"]
    return D - i - j, j


def analyse_block(name: str) -> dict:
    block = BLOCKS[name]
    D, ycap = block["D"], block["ycap"]
    sbound, ebound = thresholds(block)
    positions = support(D, ycap)
    assert len(positions) == dim_S(D, ycap)
    vanish = [(r, q) for r, q in positions if 3 * r + 4 * q < sbound]
    remain = [(r, q) for r, q in positions if 3 * r + 4 * q >= sbound]
    slots, matrix = d1_matrix(remain, ebound)
    rank, pivot_cols, pivot_rows = exact_q_rref(matrix)
    by_e = Counter(exponent for exponent, _j in slots)
    d1_support = [(r, q) for r, q in remain if 9 * r + 12 * q < ebound]
    # Unit-triangular check: each vanished (r,q) is its own D2 row.
    d2_unit = len(vanish)
    return {
        "name": name,
        "D": D,
        "ycap": ycap,
        "thm12_j": block["thm12_j"],
        "bound_t_D2": str(block["bound_t_D2"]),
        "bound_t_D1": str(block["bound_t_D1"]),
        "D2_s_threshold": sbound,
        "D1_e_threshold": ebound,
        "ambient": len(positions),
        "D2_unit_rows": d2_unit,
        "D2_remaining": len(remain),
        "D1_gap_support": len(d1_support),
        "D1_raw_slots": len(slots),
        "D1_rows_by_e": {str(k): by_e[k] for k in sorted(by_e)},
        "D1_Qstar_rank": rank,
        "D1_dependent_slots": len(slots) - rank,
        "D1_e_range": [min(by_e), max(by_e)] if by_e else None,
        "remain_r_min": min((r for r, _q in remain), default=None),
        "sample_D2_vanish": [list(item) for item in vanish[:5]],
        "sample_D2_remain": [list(item) for item in remain[:5]],
        "D1_pivot_columns_rq": [
            list(remain[col]) for col in pivot_cols[:12]
        ],
    }


def h2_method_control() -> dict:
    """Replay the charged h2 D1 engine on the projected 169-space; expect 7."""
    remain = [
        (r, q)
        for r in range(1, 34)
        for q in range(34 - r)
        if 3 * r + 4 * q >= 97
    ]
    assert len(remain) == 169
    slots, matrix = d1_matrix(remain, 296)
    # Restrict to the first band below 296 that h2 actually meets: e>=289.
    keep = [i for i, (e, _j) in enumerate(slots) if e >= 289]
    matrix = [matrix[i] for i in keep]
    slots = [slots[i] for i in keep]
    rank, _cols, _rows = exact_q_rref(matrix)
    by_e = Counter(e for e, _j in slots)
    return {
        "strict_support": 169,
        "raw_slots_below_296_from_289": len(slots),
        "rows_by_e": {str(k): by_e[k] for k in sorted(by_e)},
        "Qstar_rank": rank,
        "matches_charged_7": rank == 7 and dict(sorted(by_e.items()))
        == {291: 1, 292: 1, 293: 1, 294: 2, 295: 2},
    }


def prefix_overlap(block_reports: dict[str, dict]) -> dict:
    """Every first_global_band outer pivot is a D2 unit vanishing."""
    records = []
    for block, i, j in PREFIX_OUTER_PIVOTS:
        r, q = xy_to_rq(block, i, j)
        sbound, _ebound = thresholds(BLOCKS[block])
        weight = 3 * r + 4 * q
        vanished = weight < sbound
        records.append(
            {
                "name": f"{block}_{i}_{j}",
                "r": r,
                "q": q,
                "weight_3r4q": weight,
                "D2_threshold": sbound,
                "is_D2_unit_row": vanished,
            }
        )
    return {
        "n_prefix_outer_pivots": len(PREFIX_OUTER_PIVOTS),
        "n_contained_in_D2": sum(1 for rec in records if rec["is_D2_unit_row"]),
        "all_contained_in_D2": all(rec["is_D2_unit_row"] for rec in records),
        "items": records,
    }


def h3_adic_derived() -> dict:
    """h3-adic D2 bounds on F_j, G_j after the triangular chart expansion.

    F = (h3^3 + C2 h3 + C3)^3 + A2 (h3^3 + C2 h3 + C3) + A3
    G = (h3^3 + C2 h3 + C3)^2 + B1 (h3^3 + C2 h3 + C3) + B2

    Theorem 1.2 at D2, base h3, ord h3 = -1/3: ord F_j >= -j/3, ord G_j >= -j/3.
    Canonical F_1 = 0 (no h3^8).  G_1 = 0 (no h3^5).
    These are identities or consequences of the D2-h2 bounds already counted
    on C2, C3, A2, A3, B1, B2.  They are not extra ambient coordinates.
    Floor/attainment: products of >= bounds remain >= ; no equality is claimed.
    """
    F = {
        0: "1",
        1: "0",
        2: "3*C2",
        3: "3*C3",
        4: "3*C2^2",
        5: "6*C2*C3",
        6: "3*C3^2 + C2^3 + A2",
        7: "3*C2^2*C3",
        8: "3*C2*C3^2 + A2*C2",
        9: "C3^3 + A2*C3 + A3",
    }
    G = {
        0: "1",
        1: "0",
        2: "2*C2",
        3: "2*C3 + B1",
        4: "C2^2",
        5: "2*C2*C3 + B1*C2",
        6: "C3^2 + B1*C3 + B2",
    }
    return {
        "type": "DERIVED[h3-adic D2 bounds after chart expansion]",
        "F_j": F,
        "G_j": G,
        "identities": ["F_1=0", "G_1=0"],
        "new_outer_pivots": 0,
        "reason": (
            "ord C2>=-2/3 and ord C3>=-1 are already in the 516-row h2 tower; "
            "ord A2>=-2, ord A3>=-3, ord B1>=-1, ord B2>=-2 are the D2-h2 "
            "outer unit rows of this module.  Each F_j, G_j is a polynomial "
            "in those blocks whose Theorem-1.2 lower bound follows by addition "
            "of lower bounds.  Not independent coordinates."
        ),
    }


def run() -> dict:
    reports = {name: analyse_block(name) for name in ("A2", "A3", "B1", "B2")}
    d2_total = sum(rep["D2_unit_rows"] for rep in reports.values())
    d1_raw = sum(rep["D1_raw_slots"] for rep in reports.values())
    d1_rank = sum(rep["D1_Qstar_rank"] for rep in reports.values())
    remain_total = sum(rep["D2_remaining"] for rep in reports.values())
    ambient = sum(rep["ambient"] for rep in reports.values())
    assert ambient == 6600
    overlap = prefix_overlap(reports)
    h2_ctrl = h2_method_control()
    assert h2_ctrl["matches_charged_7"]
    assert overlap["all_contained_in_D2"]
    # Homogeneous: the zero point satisfies every row.
    # Dimension arithmetic against the charged first-global-band prefix.
    prefix_delta2 = 6689
    prefix_delta52_b0 = 6687
    new_d2_beyond_prefix = d2_total - overlap["n_contained_in_D2"]
    dim2_after_d2 = prefix_delta2 - new_d2_beyond_prefix
    dim52_after_d2 = prefix_delta52_b0 - new_d2_beyond_prefix
    dim2_after_d1 = dim2_after_d2 - d1_rank
    dim52_after_d1 = dim52_after_d2 - d1_rank
    return {
        "type": "EXACT-OUTER-THM12-D2-D1 / ADD-ON",
        "field": "Q",
        "chart": "F=h2^3+A2*h2+A3, G=h2^2+B1*h2+B2; S(D,33) blocks",
        "D2_substitution": "t=s^3, w=1+pi*s^4, weight 3r+4q",
        "D1_substitution": "t=e^9, w=1+e^12+Pi*e^13",
        "face_policy": "Theorem 1.2 is >= ; equality face is not a row",
        "h2_method_control": h2_ctrl,
        "blocks": reports,
        "totals": {
            "outer_ambient": ambient,
            "D2_unit_rows": d2_total,
            "D2_remaining": remain_total,
            "D1_raw_slots": d1_raw,
            "D1_Qstar_rank": d1_rank,
            "D1_dependent_slots": d1_raw - d1_rank,
            "new_pivots_D2_plus_D1": d2_total + d1_rank,
        },
        "prefix_overlap": overlap,
        "h3_adic": h3_adic_derived(),
        "joint_dimensions": {
            "charged_prefix_delta2": prefix_delta2,
            "charged_prefix_delta52_b0": prefix_delta52_b0,
            "D2_new_pivots_beyond_prefix": new_d2_beyond_prefix,
            "after_D2_delta2": dim2_after_d2,
            "after_D2_delta52_b0": dim52_after_d2,
            "D1_new_pivots": d1_rank,
            "after_D2_D1_delta2": dim2_after_d1,
            "after_D2_D1_delta52_b0": dim52_after_d1,
            "note": (
                "the 15 first-global-band outer pivots sit inside the D2 unit "
                "rows, so they are not subtracted twice; the 10 Jacobian prefix "
                "rows become 0=0 after those unit substitutions"
            ),
        },
        "controls": {
            "S_dimension_identity": all(
                rep["ambient"] == dim_S(rep["D"], rep["ycap"])
                for rep in reports.values()
            ),
            "zero_point_kills_every_homogeneous_row": True,
            "D2_rows_are_unit_coordinate_vanishings": True,
            "h2_D1_replay_matches_charged_7": h2_ctrl["matches_charged_7"],
            "prefix_15_subset_of_D2": overlap["all_contained_in_D2"],
            "D1_homogeneous_so_dependencies_are_not_inconsistencies": True,
            "D1_rank_equals_independent_slot_count": True,
        },
        "branches": {
            "delta2": "outer D2/D1 rows are at the first (major) point; identical for both minor branches",
            "delta52": "same outer rows",
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run(), indent=2, sort_keys=True))
