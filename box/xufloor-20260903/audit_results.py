#!/usr/bin/env python3
"""Fail-closed checks and compact extraction for results.json.

This is a census audit only.  It does not assert that the candidate principal
floor is mathematically valid.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "results.json").read_text())
ROWS = DATA["rows"]


def groups(rows):
    out = defaultdict(list)
    for row in rows:
        out[row["group_key"]].append(row)
    return out


def stats(rows, ok_field):
    by_group = groups(rows)
    killed_rows = [row for row in rows if not row[ok_field]]
    killed_groups = {
        key: items for key, items in by_group.items()
        if all(not row[ok_field] for row in items)
    }
    touched_groups = {
        key: items for key, items in by_group.items()
        if any(not row[ok_field] for row in items)
    }
    return {
        "rows": len(rows),
        "groups": len(by_group),
        "killed_rows": len(killed_rows),
        "killed_groups": len(killed_groups),
        "touched_groups": len(touched_groups),
    }


def compact(row):
    return {
        key: row[key]
        for key in (
            "n", "m", "M", "V", "V_s", "u_s", "IM_max",
            "tree_minor_min", "principal_minor_floor_promoted",
            "principal_minor_floor_candidate", "Im_min_promoted",
            "Im_min_candidate", "xu_ok_promoted", "xu_ok_candidate",
        )
    }


def unique_row(predicate, label):
    matches = [row for row in ROWS if predicate(row)]
    assert len(matches) == 1, f"{label}: expected one row, got {len(matches)}"
    return matches[0]


overall_promoted = stats(ROWS, "xu_ok_promoted")
overall_candidate = stats(ROWS, "xu_ok_candidate")
assert overall_promoted == {
    "rows": 1420, "groups": 686, "killed_rows": 43,
    "killed_groups": 29, "touched_groups": 37,
}
assert overall_candidate == {
    "rows": 1420, "groups": 686, "killed_rows": 48,
    "killed_groups": 33, "touched_groups": 42,
}

changed = [
    row for row in ROWS
    if row["xu_ok_promoted"] and not row["xu_ok_candidate"]
]
assert len(changed) == 5
assert all(row["u_s"] > 1 for row in changed)
us_eq_1 = [row for row in ROWS if row["u_s"] == 1]
assert len(us_eq_1) == 1110
assert all(
    row["principal_minor_floor_promoted"]
    == row["principal_minor_floor_candidate"]
    and row["xu_ok_promoted"] == row["xu_ok_candidate"]
    and row["Im_min_promoted"] == row["Im_min_candidate"]
    for row in us_eq_1
)

us_gt_1 = [row for row in ROWS if row["u_s"] > 1]
us_promoted = stats(us_gt_1, "xu_ok_promoted")
us_candidate = stats(us_gt_1, "xu_ok_candidate")
assert us_promoted == {
    "rows": 310, "groups": 177, "killed_rows": 9,
    "killed_groups": 7, "touched_groups": 8,
}
assert us_candidate == {
    "rows": 310, "groups": 177, "killed_rows": 14,
    "killed_groups": 11, "touched_groups": 13,
}

by_group = groups(us_gt_1)
candidate_killed_groups = [
    items for items in by_group.values()
    if all(not row["xu_ok_candidate"] for row in items)
]
candidate_killed_groups.sort(
    key=lambda items: (items[0]["n"], items[0]["m"], items[0]["M"], items[0]["V_s"])
)
candidate_killed_group_rows = [
    {
        "n": items[0]["n"],
        "m": items[0]["m"],
        "M": items[0]["M"],
        "V_s": items[0]["V_s"],
        "u_s": items[0]["u_s"],
        "rows": len(items),
        "bounds": sorted({
            (row["IM_max"], row["Im_min_candidate"]) for row in items
        }),
    }
    for items in candidate_killed_groups
]

two_point = [
    row for row in ROWS
    if row["u_s"] == 1
    and row["phi_eff"].get("s_eff") == 2
    and row["phi_eff"].get("two_point") is True
]
two_point_summary = {
    **stats(two_point, "xu_ok_candidate"),
    "promoted_killed_rows": sum(not row["xu_ok_promoted"] for row in two_point),
}
assert two_point_summary == {
    "rows": 18, "groups": 17, "killed_rows": 0,
    "killed_groups": 0, "touched_groups": 0, "promoted_killed_rows": 0,
}

k16_specs = (
    (64, 48, [52, 62], {"2": 3, "3": 3}),
    (112, 80, [100, 110], {"2": 3, "3": 3}),
    (160, 112, [148, 158], {"2": 3, "3": 3}),
)
k16_rows = [
    unique_row(
        lambda row, n=n, m=m, M=M, V=V:
            row["n"] == n and row["m"] == m and row["M"] == M and row["V"] == V,
        f"K=16 D={n}",
    )
    for n, m, M, V in k16_specs
]
assert [
    (row["IM_max"], row["Im_min_promoted"], row["Im_min_candidate"],
     row["xu_ok_promoted"], row["xu_ok_candidate"])
    for row in k16_rows
] == [
    ("9", "3", "3", True, True),
    ("15", "3", "3", True, True),
    ("21", "3", "3", True, True),
]

target_108 = unique_row(
    lambda row: row["n"] == 108 and row["m"] == 72
    and row["M"] == [81, 106] and row["V"] == {"2": 7, "3": 7},
    "(108,72;(-72,81,106);V=(7,7))",
)
target_99 = unique_row(
    lambda row: row["n"] == 99 and row["m"] == 66
    and row["M"] == [77, 97] and row["V"] == {"2": 8, "3": 8},
    "(99,66)",
)
assert (
    target_99["IM_max"], target_99["principal_minor_floor_promoted"],
    target_99["principal_minor_floor_candidate"], target_99["Im_min_promoted"],
    target_99["Im_min_candidate"], target_99["xu_ok_promoted"],
    target_99["xu_ok_candidate"],
) == ("16", "0", "5/3", "1", "8/3", True, True)
assert (
    target_108["IM_max"], target_108["principal_minor_floor_promoted"],
    target_108["principal_minor_floor_candidate"], target_108["Im_min_promoted"],
    target_108["Im_min_candidate"], target_108["xu_ok_promoted"],
    target_108["xu_ok_candidate"],
) == ("21", "0", "5/2", "1", "7/2", True, True)

cal = DATA["controls"]["calibration"]
calibration = {
    "75_50_split_ii": {"IM": "4", "Im": "6", "excluded": True},
    "84_56_M2_64_V2_2": {"IM": "4", "Im": "5", "excluded": True},
    "84_56_M2_72_V2_5": {"IM": "10", "Im": "4", "excluded": False},
}
for label, expected in calibration.items():
    assert {key: cal[label][key] for key in expected} == expected

summary = {
    "candidate_is_computational_only": True,
    "calibration_3_of_3": calibration,
    "overall": {"promoted": overall_promoted, "candidate": overall_candidate},
    "u_s_eq_1_unchanged_rows": len(us_eq_1),
    "u_s_gt_1": {"promoted": us_promoted, "candidate": us_candidate},
    "delta": {"newly_killed_rows": 5, "newly_killed_groups": 4},
    "newly_killed_rows": [compact(row) for row in changed],
    "newly_killed_groups": DATA["candidate_newly_killed_groups"],
    "all_candidate_killed_u_s_gt_1_groups": candidate_killed_group_rows,
    "targets": {
        "99_66": compact(target_99),
        "108_72_M_minus72_81_106_V_7_7": compact(target_108),
        "direct_two_point_list": two_point_summary,
        "K_16_ray": [compact(row) for row in k16_rows],
    },
}
print(json.dumps(summary, indent=2, sort_keys=True))
