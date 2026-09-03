#!/usr/bin/env python3
"""Compact assertions for xu_sametree.py output."""
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "same_tree_results.json").read_text())
ROWS = DATA["rows"]


def stats(rows, field):
    groups = {}
    for row in rows:
        groups.setdefault(row["group_key"], []).append(row)
    return {
        "rows": len(rows),
        "groups": len(groups),
        "killed_rows": sum(not row[field] for row in rows),
        "killed_groups": sum(all(not row[field] for row in items) for items in groups.values()),
        "touched_groups": sum(any(not row[field] for row in items) for items in groups.values()),
    }


def unique(predicate, label):
    matches = [row for row in ROWS if predicate(row)]
    assert len(matches) == 1, f"{label}: expected one, got {len(matches)}"
    return matches[0]


assert DATA["failures"] == []
expected = {
    "rows": 1420,
    "groups": 686,
    "killed_rows": 48,
    "killed_groups": 33,
    "touched_groups": 42,
}
assert DATA["operative"]["policies"]["independent_sharp"] == expected
assert DATA["operative"]["policies"]["same_tree_cor53"] == expected
assert DATA["operative"]["policies"]["same_tree_all"] == expected
assert all(row["independent_ok"] == row["same_tree_all_ok"] for row in ROWS)
assert all(row["same_tree_c53_ok"] == row["same_tree_all_ok"] for row in ROWS)
assert all(row["same_tree_max_c53_slack"] == row["same_tree_max_t47i_slack"] for row in ROWS)
assert DATA["operative"]["killers_all_rows"] == {
    "Corollary 5.3 / Theorem 4.7(ii)": 48,
    "survives": 1372,
}
assert DATA["operative"]["killers_all_groups"] == {
    "Corollary 5.3 / Theorem 4.7(ii)": 33,
    "Theorem 3.4 + Theorem 4.7(i)": 0,
    "mixed": 0,
}

us1 = [row for row in ROWS if row["u_s"] == 1]
usgt = [row for row in ROWS if row["u_s"] > 1]
assert stats(us1, "same_tree_all_ok") == {
    "rows": 1110,
    "groups": 509,
    "killed_rows": 34,
    "killed_groups": 22,
    "touched_groups": 29,
}
assert stats(usgt, "same_tree_all_ok") == {
    "rows": 310,
    "groups": 177,
    "killed_rows": 14,
    "killed_groups": 11,
    "touched_groups": 13,
}
assert DATA["operative"]["new_same_tree_cor53_killed_groups_D_le_120_vs_independent"] == []
assert DATA["operative"]["new_same_tree_all_killed_groups_D_le_120_vs_independent"] == []
assert len(DATA["operative"]["same_tree_all_killed_groups_D_le_120"]) == 4

target_99 = unique(
    lambda row: row["n"] == 99 and row["m"] == 66
    and row["M"] == [77, 97] and row["V"] == {"2": 8, "3": 8},
    "99_66",
)
target_108 = unique(
    lambda row: row["n"] == 108 and row["m"] == 72
    and row["M"] == [81, 106] and row["V"] == {"2": 7, "3": 7},
    "108_72_V_7_7",
)
assert target_99["same_tree_all_ok"] and target_99["same_tree_max_c53_slack"] == "40/3"
assert target_108["same_tree_all_ok"] and target_108["same_tree_max_c53_slack"] == "35/2"

k16 = DATA["targets"]["K_16_entries"]
assert [row["same_tree_max_c53_slack"] for row in k16] == ["6", "12", "18"]
assert all(row["same_tree_all_ok"] for row in k16)
tp = DATA["targets"]["direct_two_point_list"]
assert tp["rows"] == 18 and tp["groups"] == 17
assert tp["same_tree_all"]["killed_rows"] == 0
assert tp["same_tree_all"]["killed_groups"] == 0

cal = DATA["calibration"]
assert (cal["75_50_split_i"]["IM"], cal["75_50_split_i"]["Im"], cal["75_50_split_i"]["excluded_by_all"]) == ("8", "4", False)
assert (cal["75_50_split_ii"]["IM"], cal["75_50_split_ii"]["Im"], cal["75_50_split_ii"]["excluded_by_all"]) == ("4", "6", True)
assert (cal["84_56_M2_64_V2_2"]["IM"], cal["84_56_M2_64_V2_2"]["Im"], cal["84_56_M2_64_V2_2"]["excluded_by_all"]) == ("4", "5", True)
assert (cal["84_56_M2_72_V2_5"]["IM"], cal["84_56_M2_72_V2_5"]["Im"], cal["84_56_M2_72_V2_5"]["excluded_by_all"]) == ("10", "4", False)

summary = {
    "policies": DATA["operative"]["policies"],
    "by_u_s_class": DATA["operative"]["by_u_s_class"],
    "killers": {
        "rows": DATA["operative"]["killers_all_rows"],
        "groups": DATA["operative"]["killers_all_groups"],
    },
    "new_same_tree_groups_D_le_120_vs_independent": 0,
    "targets": DATA["targets"],
    "calibration": {
        key: {
            "IM": value["IM"],
            "Im": value["Im"],
            "I": value["I"],
            "weighted_minor": value["weighted_minor"],
            "cor53_slack": value["cor53_slack"],
            "t47i_slack": value["t47i_slack"],
            "excluded_by_all": value["excluded_by_all"],
        }
        for key, value in cal.items()
    },
}
(HERE / "audit_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps(summary, indent=2, sort_keys=True))
