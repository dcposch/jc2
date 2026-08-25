#!/usr/bin/env python3
"""Independent structural verifier for the frozen degree-one audit outputs."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


CASE = Path(__file__).resolve().parent
RESULT_ROOT = Path(os.environ.get("RESULT_ROOT", CASE / "aws_run_v2"))
EXPECTED = {
    "0000_0000000": {
        "json_sha256": "9afa22f0c886bab3d5a2f4dbeb0f81c0e309b0cf0065fb360abe49c0ae2acf0f",
        "model_sha256": "dbb405ac9ab12b9d4b01df6e934ac6979609dfd4eabbe2ccf65a65aaf8cdcb81",
        "base_raw": 42, "extended_raw": 50,
        "rank_pair": (7, 8), "row8_constant": 2,
        "stage1_added": [43, 44], "stage2_added_count": 3,
    },
    "0270_0101000": {
        "json_sha256": "d9a96fb1962e0505d2eab2acd53ac7c9f072725a3201c7ad89016aff4236f12d",
        "model_sha256": "05627048aa3e648b975acc1ed47e97a451241c3544e7fa5b58a7c42a1cd4be03",
        "base_raw": 38, "extended_raw": 46,
        "rank_pair": (9, 10), "row8_constant": 2,
        "stage1_added": [39, 40], "stage2_added_count": 4,
    },
    "0513_0201000": {
        "json_sha256": "6ad3142aff123e5fbc01aa77c56295119a5d3f16d2eb6c5c71785d826d6baa27",
        "model_sha256": "9c319fe4d1a576569869cbccbcc7411fee5eb12dedaa4e6a820a395263820200",
        "base_raw": 38, "extended_raw": 46,
        "rank_pair": (9, 10), "row8_constant": 1,
        "stage1_added": [39, 40], "stage2_added_count": 4,
    },
}

slots = [[i, total - i] for total in range(13)
         for i in range(total + 1)]
assert len(slots) == 91 and slots[8] == [2, 1]

for spec, expected in EXPECTED.items():
    path = RESULT_ROOT / f"base_{spec}" / "degree1.json"
    payload = path.read_bytes()
    assert hashlib.sha256(payload).hexdigest() == expected["json_sha256"]
    result = json.loads(payload)
    assert result["status"] == "PASS-AS-Q3-Q2Q1-DEGREE1-INFLUENCE-AUDIT"
    assert result["parent_sha256"] == (
        "cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd")
    assert result["model_sha256"] == expected["model_sha256"]
    assert result["base_raw_variable_count"] == expected["base_raw"]
    assert result["extended_raw_variable_count"] == expected["extended_raw"]
    assert result["added_degree1_raw_columns"] == list(
        range(expected["base_raw"], expected["extended_raw"]))
    assert result["row_count"] == 91 and result["slot_order"] == slots

    stage1 = result["stage1"]
    assert (stage1["rank"], stage1["augmented_rank"]) == (6, 6)
    assert stage1["active_solution_dimension"] == 4
    assert stage1["accepted_active_assignment_count"] == 81
    assert stage1["added_degree1_active_raw_columns"] == expected["stage1_added"]
    stage1_support = stage1["added_degree1_nonzero_support"]
    assert sorted(map(int, stage1_support)) == expected["stage1_added"]
    for entries in stage1_support.values():
        assert entries == [{"coefficient": 1, "row_index": 0,
                            "slot": [0, 0]}]

    pair = expected["rank_pair"]
    assert result["rank_histogram"] == {str(pair): 81}
    assert result["row8_constant_histogram"] == {
        str(expected["row8_constant"]): 81}
    assert result["row8_nonzero_column_count_histogram"] == {"0": 81}
    assert result["added_degree1_stage2_nonzero_column_count_histogram"] == {
        str(expected["stage2_added_count"]): 81}
    assert result["branches_with_nonzero_added_degree1_stage2_column"] == 81
    assert result["consistent_branch_count"] == 0
    assert result["consistent_witnesses"] == []
    assert result["constant_digit_influence"] == (
        "exactly zero because partial derivatives vanish")

    branches = result["branches"]
    assert len(branches) == 81
    assert [branch["branch_index"] for branch in branches] == list(range(81))
    for branch in branches:
        assert (branch["rank"], branch["augmented_rank"]) == pair
        assert not branch["consistent"]
        assert branch["row8_constant"] == expected["row8_constant"]
        assert branch["row8_nonzero_raw_columns"] == []
        support = branch["added_degree1_stage2_nonzero_support"]
        assert len(support) == expected["stage2_added_count"]
        # Negative control: degree-one columns really occur in the stage-two
        # matrix, but their exact support avoids the obstructing row 8.
        assert support
        assert all(entry["row_index"] != 8
                   for entries in support.values() for entry in entries)

print("PASS-AS-Q3-Q2Q1-DEGREE1-INFLUENCE-OUTPUT-VERIFY-V2")
