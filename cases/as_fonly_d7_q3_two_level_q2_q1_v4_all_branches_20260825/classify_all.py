#!/usr/bin/env python3
"""Complete all 27 exact first-carry branches; retain inconsistent branches."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V3 = (ROOT / "cases/as_fonly_d7_q3_two_level_q2_q1_v3_branches_20260825"
      / "classify_branches.py")
EXPECTED = "4f6b94ce223e60b9023b8e3fe91a1113b0978a4ff74e986aa1227e01217006b9"
payload = V3.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
marker = b"\nbranches = []\n"
assert payload.count(marker) == 1
ns = {"__file__": str(V3), "__name__": "__all_branches_prefix__"}
exec(compile(payload.split(marker, 1)[0] + b"\n", str(V3), "exec"), ns)

accepted = ns["accepted"]
inactive1 = ns["inactive1"]
slots = ns["slots"]
high_slots = ns["high_slots"]
raw_rows = ns["raw_rows"]
place = ns["place"]
extract_affine = ns["extract_affine"]
rref_solve = ns["rref_solve"]
parameterize = ns["parameterize"]
affine_failure = ns["affine_failure"]
raw_candidate = ns["raw_candidate"]
determinant_minus_one = ns["determinant_minus_one"]

branches = []
sat_witnesses = []
for branch_index, (active_values, fixed) in enumerate(accepted):
    function2 = lambda x, fixed=fixed: raw_rows(place(fixed, x), 81, slots)
    c2, m2, design2 = extract_affine(function2, len(inactive1))
    r2, a2, p2, k2, bad2 = rref_solve(m2, c2)
    active2 = [inactive1[column] for column in range(len(inactive1))
               if any(row[column] for row in m2)]
    entry = {
        "branch_index": branch_index,
        "stage1_active_values": list(active_values),
        "stage2_input_dimension": len(inactive1),
        "stage2_rank": r2, "stage2_augmented_rank": a2,
        "stage2_consistent": p2 is not None,
        "stage2_kernel_dimension": len(k2),
        "stage2_design_count": design2,
        "stage2_matrix_sha256": hashlib.sha256(bytes(
            value for row in m2 for value in row)).hexdigest(),
        "stage2_rhs_sha256": hashlib.sha256(bytes((-x) % 3 for x in c2)).hexdigest(),
        "stage2_active_raw_columns": active2,
        "stage2_contradiction_rows": bad2,
    }
    if p2 is None:
        branches.append(entry)
        continue

    def stage2_raw(coordinates):
        return place(fixed, parameterize(p2, k2, coordinates))

    function3 = lambda x: raw_rows(stage2_raw(x), 243, high_slots)
    failure3 = affine_failure(function3, len(k2))
    entry.update({"stage3_affine": failure3 is None,
                  "stage3_first_affine_failure": failure3})
    if failure3 is None:
        c3, m3, design3 = extract_affine(function3, len(k2))
        r3, a3, p3, k3, bad3 = rref_solve(m3, c3)
        entry.update({"stage3_rank": r3, "stage3_augmented_rank": a3,
                      "stage3_consistent": p3 is not None,
                      "stage3_kernel_dimension": len(k3),
                      "stage3_design_count": design3,
                      "stage3_contradiction_rows": bad3})
        if p3 is not None:
            raw = stage2_raw(p3)
            P, Q, q3_values, blocks = raw_candidate(raw)
            determinant = determinant_minus_one(P, Q)
            assert all(determinant.get(xy, 0) % 243 == 0 for xy in slots)
            assert all(determinant.get(xy, 0) % 729 == 0 for xy in high_slots)
            assert determinant.get((0, 0), 0) == 0
            sat_witnesses.append({"branch_index": branch_index,
                                  "raw_particular": raw,
                                  "q3_values": q3_values,
                                  "blocks": blocks,
                                  "stage3_kernel_dimension": len(k3)})
    branches.append(entry)

histogram = Counter((b["stage2_rank"], b["stage2_augmented_rank"],
                     b.get("stage3_affine")) for b in branches)
result = {
    "status": "PASS-AS-Q2Q1-V4-ALL-27-BRANCHES",
    "v3_sha256": EXPECTED,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "accepted_branch_count": len(accepted),
    "stage2_consistent_branch_count": sum(
        b["stage2_consistent"] for b in branches),
    "stage2_inconsistent_branch_count": sum(
        not b["stage2_consistent"] for b in branches),
    "stage3_affine_branch_count": sum(
        b.get("stage3_affine") is True for b in branches),
    "stage3_nonaffine_branch_count": sum(
        b.get("stage3_affine") is False for b in branches),
    "sat_witness_count": len(sat_witnesses),
    "histogram": {str(key): value for key, value in sorted(histogram.items())},
    "branches": branches, "sat_witnesses": sat_witnesses,
    "scope": "all 27 first-carry branches of one displayed Q3 fibre",
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("branches", len(accepted), "stage2_consistent",
      result["stage2_consistent_branch_count"], "stage2_inconsistent",
      result["stage2_inconsistent_branch_count"])
print("stage3_affine", result["stage3_affine_branch_count"],
      "stage3_nonaffine", result["stage3_nonaffine_branch_count"],
      "sat", len(sat_witnesses))
print("histogram", dict(histogram))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
