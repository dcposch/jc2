#!/usr/bin/env python3
"""Small custody verifier for the frozen two-host Z/27 outputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_SOURCE = "f6eaa0a0f1dabb785bdd4358fa84739d907820bc539cc619a1b692ad5755cb19"
assert hashlib.sha256((ROOT / "solve_full_output_cone_z27.py").read_bytes()).hexdigest() == EXPECTED_SOURCE

expected = {
    "base_0000_0000000": {
        "sha": "007b3f097cec491d480c7f240e02cedf61175d3d92ca865436ba6cf1bc2ed21d",
        "stages": [(27, 45), (36, 81), (47, 106)],
        "prior": 81, "liftable": 61, "new": 106, "mixed": 1008,
    },
    "base_0270_0101000": {
        "sha": "b7d571a23bb7e75b25d6540768b248b6935a35a16d903ec1c0cc71f69a079966",
        "stages": [(27, 45), (43, 74), (49, 97)],
        "prior": 74, "liftable": 52, "new": 97, "mixed": 720,
    },
    "base_0513_0201000": {
        "sha": "5d109dde446f5202b2e16024873a504db75c0fef82eb3bfee9927038dbfcbc74",
        "stages": [(27, 45), (43, 74), (49, 97)],
        "prior": 74, "liftable": 52, "new": 97, "mixed": 720,
    },
}

for base, wanted in expected.items():
    left = ROOT / "aws_box02" / base / "result.json"
    right = ROOT / "aws_r6d" / base / "result.json"
    assert left.read_bytes() == right.read_bytes()
    payload = left.read_bytes()
    assert hashlib.sha256(payload).hexdigest() == wanted["sha"]
    data = json.loads(payload)
    stages = [(data["stage_mod3"]["rank"],
               data["stage_mod3"]["kernel_dimension"]),
              (data["stage_mod9"]["rank"],
               data["stage_mod9"]["kernel_dimension"]),
              (data["stage_mod27"]["rank"],
               data["stage_mod27"]["kernel_dimension"])]
    assert stages == wanted["stages"]
    assert data["previous_mod243_solution_exponent"] == wanted["prior"]
    assert data["liftable_previous_mod243_dimension"] == wanted["liftable"]
    assert data["new_mod729_solution_exponent"] == wanted["new"]
    assert data["q3_fresh_mixed_control_count"] == wanted["mixed"]
    assert data["pair_control_count"] == 1296
    assert data["stored_z9_particular_lifts"] is False
    assert data["literal_integer_replay_mod729_passed"] is True
    assert data["exact_linearity_mod27_after_division_by27"] is True
    assert (ROOT / "aws_box02" / base / "solver.rc").read_text().strip() == "0"
    assert (ROOT / "aws_r6d" / base / "solver.rc").read_text().strip() == "0"

print("PASS-AS-Q3-FULL-OUTPUT-CONE-Z27-FROZEN")
