#!/usr/bin/env python3
"""Normalize the first carry by its eight-variable source cone."""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from collections import Counter
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V1 = (ROOT / "cases/as_fonly_d7_q3_two_level_q2_q1_20260825"
      / "solve_two_level.py")
EXPECTED = "cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd"
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
marker = b"\nstages = []\n"
assert payload.count(marker) == 1
ns = {"__file__": str(V1), "__name__": "__carry_v3_prefix__"}
exec(compile(payload.split(marker, 1)[0] + b"\n", str(V1), "exec"), ns)

slots = ns["slots"]
high_slots = ns["high_slots"]
raw_n = ns["raw_variable_count"]
raw_rows = ns["raw_rows"]
raw_candidate = ns["raw_candidate"]
determinant_minus_one = ns["determinant_minus_one"]
extract_affine = ns["extract_affine"]
rref_solve = ns["rref_solve"]
parameterize = ns["parameterize"]

c1, m1, design1 = extract_affine(lambda x: raw_rows(x, 27, slots), raw_n)
r1, a1, p1, k1, bad1 = rref_solve(m1, c1)
assert p1 is not None and not bad1
active1 = [column for column in range(raw_n)
           if any(row[column] for row in m1)]
inactive1 = [column for column in range(raw_n) if column not in active1]

accepted = []
for values in itertools.product(range(3), repeat=len(active1)):
    raw = [0] * raw_n
    for column, value in zip(active1, values):
        raw[column] = value
    if raw_rows(raw, 27, slots) == [0] * len(slots):
        accepted.append((values, raw))
assert len(accepted) == 3 ** (len(active1) - r1)

def place(fixed, coordinates):
    raw = list(fixed)
    assert len(coordinates) == len(inactive1)
    for column, value in zip(inactive1, coordinates):
        raw[column] = value
    return raw

def affine_failure(function, variable_count):
    constant = function([0] * variable_count)
    columns = []
    for index in range(variable_count):
        e = [0] * variable_count
        e[index] = 1
        at_one = function(e)
        columns.append([(x - y) % 3 for x, y in zip(at_one, constant)])
    for index in range(variable_count):
        x = [0] * variable_count
        x[index] = 2
        observed = function(x)
        predicted = [(base + 2 * delta) % 3
                     for base, delta in zip(constant, columns[index])]
        bad = [row for row, pair in enumerate(zip(observed, predicted))
               if pair[0] != pair[1]]
        if bad:
            return {"kind": "twice", "coordinates": [index], "rows": bad,
                    "observed": [observed[i] for i in bad],
                    "predicted": [predicted[i] for i in bad]}
    for left in range(variable_count):
        for right in range(left + 1, variable_count):
            x = [0] * variable_count
            x[left] = x[right] = 1
            observed = function(x)
            predicted = [(base + dl + dr) % 3
                         for base, dl, dr in zip(
                             constant, columns[left], columns[right])]
            bad = [row for row, pair in enumerate(zip(observed, predicted))
                   if pair[0] != pair[1]]
            if bad:
                return {"kind": "pair", "coordinates": [left, right],
                        "rows": bad, "observed": [observed[i] for i in bad],
                        "predicted": [predicted[i] for i in bad]}
    return None

branches = []
sat_witnesses = []
for branch_index, (active_values, fixed) in enumerate(accepted):
    function2 = lambda x, fixed=fixed: raw_rows(place(fixed, x), 81, slots)
    c2, m2, design2 = extract_affine(function2, len(inactive1))
    r2, a2, p2, k2, bad2 = rref_solve(m2, c2)
    assert p2 is not None and not bad2
    active2 = [inactive1[column] for column in range(len(inactive1))
               if any(row[column] for row in m2)]

    def stage2_raw(coordinates):
        remaining = parameterize(p2, k2, coordinates)
        return place(fixed, remaining)

    function3 = lambda x: raw_rows(stage2_raw(x), 243, high_slots)
    failure3 = affine_failure(function3, len(k2))
    entry = {
        "branch_index": branch_index,
        "stage1_active_values": list(active_values),
        "stage2_input_dimension": len(inactive1),
        "stage2_rank": r2, "stage2_augmented_rank": a2,
        "stage2_kernel_dimension": len(k2),
        "stage2_design_count": design2,
        "stage2_matrix_sha256": hashlib.sha256(bytes(
            value for row in m2 for value in row)).hexdigest(),
        "stage2_rhs_sha256": hashlib.sha256(bytes((-x) % 3 for x in c2)).hexdigest(),
        "stage2_active_raw_columns": active2,
        "stage3_affine": failure3 is None,
        "stage3_first_affine_failure": failure3,
    }
    if failure3 is None:
        c3, m3, design3 = extract_affine(function3, len(k2))
        r3, a3, p3, k3, bad3 = rref_solve(m3, c3)
        entry.update({"stage3_rank": r3, "stage3_augmented_rank": a3,
                      "stage3_consistent": p3 is not None,
                      "stage3_kernel_dimension": len(k3),
                      "stage3_design_count": design3})
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

signature_histogram = Counter((b["stage2_rank"], b["stage2_kernel_dimension"],
                               b["stage3_affine"])
                              for b in branches)
result = {
    "status": "PASS-AS-Q2Q1-V3-BRANCH-CLASSIFIER",
    "v1_sha256": EXPECTED,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "stage1": {"raw_variable_count": raw_n, "row_count": len(slots),
               "rank": r1, "augmented_rank": a1,
               "kernel_dimension": len(k1), "design_count": design1,
               "active_raw_columns": active1,
               "inactive_raw_columns": inactive1,
               "accepted_active_assignment_count": len(accepted)},
    "branches": branches,
    "signature_histogram": {str(key): value
                            for key, value in sorted(signature_histogram.items())},
    "sat_witnesses": sat_witnesses,
    "scope": "exact first-carry branches; nonlinear later branches remain open",
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("stage1_active", active1, "accepted", len(accepted))
print("signature_histogram", dict(signature_histogram))
print("stage3_affine_count", sum(b["stage3_affine"] for b in branches))
print("sat_witness_count", len(sat_witnesses))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
