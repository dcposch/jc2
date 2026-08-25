#!/usr/bin/env python3
"""Exact degree-one influence audit on one displayed Q3 fibre."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import json
import os
from collections import Counter
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q3_two_level_q2_q1_20260825"
          / "solve_two_level.py")
EXPECTED = "cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd"
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
marker = b"\nstages = []\n"
assert payload.count(marker) == 1
ns = {"__file__": str(PARENT), "__name__": "__degree1_parent_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload.split(marker, 1)[0] + b"\n", str(PARENT), "exec"), ns)

base_candidate = ns["raw_candidate"]
base_raw_n = ns["raw_variable_count"]
nadd, nscale = ns["nadd"], ns["nscale"]
homogeneous_numeric = ns["homogeneous_numeric"]
determinant_minus_one = ns["determinant_minus_one"]
extract_affine, rref_solve = ns["extract_affine"], ns["rref_solve"]
parameterize = ns["parameterize"]
slots = ns["slots"]
assert len(slots) == 91
assert slots == [(i, total - i) for total in range(13)
                 for i in range(total + 1)]
assert slots[8] == (2, 1)

raw_n = base_raw_n + 8


def extended_candidate(values):
    assert len(values) == raw_n
    P, Q, q3_values, blocks = base_candidate(values[:base_raw_n])
    extra = values[base_raw_n:]
    W1 = homogeneous_numeric(1, extra[0:2])
    Z1 = homogeneous_numeric(1, extra[2:4])
    H1 = homogeneous_numeric(1, extra[4:6])
    J1 = homogeneous_numeric(1, extra[6:8])
    P = nadd(P, nscale(27, W1), nscale(81, H1))
    Q = nadd(Q, nscale(27, Z1), nscale(81, J1))
    return P, Q, q3_values, dict(blocks, W1=extra[0:2], Z1=extra[2:4],
                                  H1=extra[4:6], J1=extra[6:8])


def rows(values, divisor):
    P, Q, _, _ = extended_candidate(values)
    determinant = determinant_minus_one(P, Q)
    answer = []
    for xy in slots:
        coefficient = determinant.get(xy, 0)
        assert coefficient % divisor == 0, (xy, coefficient, divisor)
        answer.append((coefficient // divisor) % 3)
    return answer


def place(active_columns, active_values, inactive_columns, coordinates):
    result = [0] * raw_n
    for column, value in zip(active_columns, active_values):
        result[column] = value
    for column, value in zip(inactive_columns, coordinates):
        result[column] = value
    return result


c1, m1, design1 = extract_affine(lambda x: rows(x, 27), raw_n)
r1, a1, p1, k1, bad1 = rref_solve(m1, c1)
assert p1 is not None and not bad1
active = [column for column in range(raw_n) if any(row[column] for row in m1)]
inactive = [column for column in range(raw_n) if column not in active]
active_matrix = [[m1[row][column] for column in active]
                 for row in range(len(slots))]
arank, aaug, apart, akernel, abad = rref_solve(active_matrix, c1)
assert apart is not None and not abad and arank == r1

accepted = []
for parameters in itertools.product(range(3), repeat=len(akernel)):
    values = parameterize(apart, akernel, parameters)
    raw = place(active, values, inactive, [0] * len(inactive))
    assert rows(raw, 27) == [0] * len(slots)
    accepted.append(values)
assert len({tuple(values) for values in accepted}) == len(accepted)

rank_histogram = Counter()
row8_constant_histogram = Counter()
row8_nonzero_column_histogram = Counter()
degree1_stage2_nonzero_column_histogram = Counter()
branches_with_nonzero_degree1_stage2_column = 0
consistent = []
branch_records = []
for branch_index, active_values in enumerate(accepted):
    function = lambda x, av=active_values: rows(
        place(active, av, inactive, x), 81)
    constant, matrix, design2 = extract_affine(function, len(inactive))
    rank, augmented, particular, kernel, bad = rref_solve(matrix, constant)
    row8 = matrix[8]
    row8_nonzero = [inactive[index] for index, value in enumerate(row8) if value]
    degree1_stage2_support = {}
    for raw_column in range(base_raw_n, raw_n):
        if raw_column not in inactive:
            continue
        matrix_column = inactive.index(raw_column)
        support = [
            {"row_index": row_index, "slot": list(slots[row_index]),
             "coefficient": matrix[row_index][matrix_column]}
            for row_index in range(len(slots))
            if matrix[row_index][matrix_column]
        ]
        if support:
            degree1_stage2_support[str(raw_column)] = support
    degree1_stage2_nonzero_column_histogram[
        len(degree1_stage2_support)] += 1
    if degree1_stage2_support:
        branches_with_nonzero_degree1_stage2_column += 1
    rank_histogram[(rank, augmented)] += 1
    row8_constant_histogram[constant[8]] += 1
    row8_nonzero_column_histogram[len(row8_nonzero)] += 1
    record = {
        "branch_index": branch_index,
        "active_values": active_values,
        "rank": rank,
        "augmented_rank": augmented,
        "consistent": particular is not None,
        "kernel_dimension": len(kernel),
        "design_count": design2,
        "row8_constant": constant[8],
        "row8_nonzero_raw_columns": row8_nonzero,
        "added_degree1_stage2_nonzero_support": degree1_stage2_support,
        "matrix_sha256": hashlib.sha256(bytes(
            value for row in matrix for value in row)).hexdigest(),
        "rhs_sha256": hashlib.sha256(bytes((-value) % 3
                                             for value in constant)).hexdigest(),
    }
    if particular is not None:
        raw = place(active, active_values, inactive, particular)
        assert rows(raw, 27) == [0] * len(slots)
        assert rows(raw, 81) == [0] * len(slots)
        P, Q, q3_values, blocks = extended_candidate(raw)
        consistent.append({"branch_index": branch_index, "raw": raw,
                           "q3_values": q3_values, "blocks": blocks,
                           "kernel_dimension": len(kernel),
                           "determinant_sha256": hashlib.sha256(
                               repr(sorted(determinant_minus_one(P, Q).items())).encode()
                           ).hexdigest()})
    branch_records.append(record)

result = {
    "status": "PASS-AS-Q3-Q2Q1-DEGREE1-INFLUENCE-AUDIT",
    "parent_sha256": EXPECTED,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "base_raw_variable_count": base_raw_n,
    "extended_raw_variable_count": raw_n,
    "row_count": len(slots),
    "slot_order": [list(xy) for xy in slots],
    "added_degree1_raw_columns": list(range(base_raw_n, raw_n)),
    "stage1": {
        "rank": r1, "augmented_rank": a1,
        "design_count": design1,
        "active_raw_columns": active,
        "inactive_raw_columns": inactive,
        "active_solution_dimension": len(akernel),
        "accepted_active_assignment_count": len(accepted),
        "added_degree1_active_raw_columns": [
            column for column in active if column >= base_raw_n],
        "added_degree1_nonzero_support": {
            str(column): [
                {"row_index": row_index, "slot": list(slots[row_index]),
                 "coefficient": m1[row_index][column]}
                for row_index in range(len(slots))
                if m1[row_index][column]
            ]
            for column in range(base_raw_n, raw_n)
            if any(m1[row_index][column] for row_index in range(len(slots)))
        },
    },
    "rank_histogram": {str(key): value
                       for key, value in sorted(rank_histogram.items())},
    "row8_constant_histogram": {str(key): value
                                for key, value in sorted(row8_constant_histogram.items())},
    "row8_nonzero_column_count_histogram": {
        str(key): value for key, value in sorted(
            row8_nonzero_column_histogram.items())},
    "added_degree1_stage2_nonzero_column_count_histogram": {
        str(key): value for key, value in sorted(
            degree1_stage2_nonzero_column_histogram.items())},
    "branches_with_nonzero_added_degree1_stage2_column": (
        branches_with_nonzero_degree1_stage2_column),
    "consistent_branch_count": len(consistent),
    "consistent_witnesses": consistent,
    "branches": branch_records,
    "constant_digit_influence": "exactly zero because partial derivatives vanish",
    "scope": "one complete displayed Q3 fibre plus all degree-one order27/order81 digits",
    "refusal_scope": ["not the global Q5 scheme", "not all-depth",
                      "not a counterexample or JC2"],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("stage1_rank", r1, "active", active, "accepted", len(accepted))
print("rank_histogram", sorted(rank_histogram.items()))
print("row8_constants", sorted(row8_constant_histogram.items()))
print("row8_nonzero_columns", sorted(row8_nonzero_column_histogram.items()))
print("consistent_branches", len(consistent))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q3-Q2Q1-DEGREE1-INFLUENCE-AUDIT")
