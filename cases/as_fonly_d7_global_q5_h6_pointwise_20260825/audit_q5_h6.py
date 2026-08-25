#!/usr/bin/env python3
"""Exact affine Q5/H6,J6 gate at one global Q6/high SAT state."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q6_high_20260825"
          / "replay_global_q6_high.py")
EXPECTED_PARENT_SHA = (
    "e8361c81609afe6365d5eba8d4fda9bdf4b3dd4a44869fbcba330c614847c77c")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

result_dir = Path(os.environ["RESULT_DIR"])
result_dir.mkdir(parents=True, exist_ok=True)
parent_output = result_dir / "parent_replay.json"
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
scope = {"__file__": str(PARENT), "__name__": "__q5_h6_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), scope)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]
homogeneous = scope["homogeneous_numeric"]
G = scope["G"]
source_data = scope["source_data"]
Rmix = scope["Rmix"]
P = scope["P"]
Q = scope["Q"]
H7 = scope["H7"]
J7 = scope["J7"]


def determinant_minus_one(left, right):
    return nadd(nmul(nderivative(left, 0), nderivative(right, 1)),
                nscale(-1, nmul(nderivative(left, 1),
                                nderivative(right, 0))),
                {(0, 0): -1})


def cross_carry(H, J):
    return nadd(nmul(source_data["A"], nderivative(J, 1)),
                nmul(nderivative(H, 0), source_data["vy"]),
                nscale(-1, nmul(source_data["uy"], nderivative(J, 0))),
                nscale(-1, nmul(nderivative(H, 1), source_data["vx"])))


def charged_rows(values):
    H6 = homogeneous(6, values[:7])
    J6 = homogeneous(6, values[7:])
    q5 = row(nadd(G(5), nderivative(H6, 0), nderivative(J6, 1)), 5)
    carry = nadd(cross_carry(H7, J7), cross_carry(H6, J6))
    terminal = []
    for degree in range(12, 6, -1):
        terminal.extend(row(nadd(divide_exact(G(degree), 3),
                                  degree_part(carry, degree),
                                  degree_part(Rmix, degree)), degree))
    assert len(q5) == 6 and len(terminal) == 63
    return [(value % 3) for value in q5 + terminal]


def rref_solve(matrix, rhs):
    rows = [[entry % 3 for entry in line] + [value % 3]
            for line, value in zip(matrix, rhs)]
    pivot_columns = []
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((index for index in range(pivot_row, len(rows))
                      if rows[index][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = 1 if rows[pivot_row][column] == 1 else 2
        rows[pivot_row] = [(inverse * entry) % 3
                           for entry in rows[pivot_row]]
        for index in range(len(rows)):
            if index == pivot_row:
                continue
            scalar = rows[index][column]
            if scalar:
                rows[index] = [(left - scalar * right) % 3
                               for left, right in zip(rows[index],
                                                      rows[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
    inconsistent = next((line for line in rows
                         if not any(line[:-1]) and line[-1]), None)
    solution = None
    if inconsistent is None:
        solution = [0] * len(matrix[0])
        for index, column in enumerate(pivot_columns):
            solution[column] = rows[index][-1]
    return len(pivot_columns), inconsistent is not None, solution


zero = [0] * 14
constant = charged_rows(zero)
columns = []
for index in range(14):
    point = list(zero)
    point[index] = 1
    value = charged_rows(point)
    columns.append([(right - left) % 3
                    for left, right in zip(constant, value)])
matrix = [[columns[column][row_index] for column in range(14)]
          for row_index in range(69)]

# Exhaustive pairwise affine-linearity control.
for left in range(14):
    for right in range(left, 14):
        point = list(zero)
        point[left] = (point[left] + 1) % 3
        point[right] = (point[right] + 1) % 3
        expected = [(constant[index] + columns[left][index]
                     + columns[right][index]) % 3 for index in range(69)]
        assert charged_rows(point) == expected

rhs = [(-value) % 3 for value in constant]
rank_matrix, inconsistent, solution = rref_solve(matrix, rhs)
augmented_rank = rank_matrix + int(inconsistent)

# Build a sparse exact left-null certificate by tracking row operations.
aug = [[entry % 3 for entry in line] + [value % 3]
       for line, value in zip(matrix, rhs)]
transform = [[int(i == j) for j in range(69)] for i in range(69)]
pivot_row = 0
for column in range(14):
    pivot = next((index for index in range(pivot_row, 69)
                  if aug[index][column]), None)
    if pivot is None:
        continue
    aug[pivot_row], aug[pivot] = aug[pivot], aug[pivot_row]
    transform[pivot_row], transform[pivot] = transform[pivot], transform[pivot_row]
    inverse = 1 if aug[pivot_row][column] == 1 else 2
    aug[pivot_row] = [(inverse * entry) % 3 for entry in aug[pivot_row]]
    transform[pivot_row] = [(inverse * entry) % 3
                            for entry in transform[pivot_row]]
    for index in range(69):
        if index == pivot_row:
            continue
        scalar = aug[index][column]
        if scalar:
            aug[index] = [(a - scalar * b) % 3
                          for a, b in zip(aug[index], aug[pivot_row])]
            transform[index] = [(a - scalar * b) % 3
                                for a, b in zip(transform[index],
                                                transform[pivot_row])]
    pivot_row += 1

certificate = None
if inconsistent:
    index = next(i for i, line in enumerate(aug)
                 if not any(line[:-1]) and line[-1])
    certificate = {
        "pairing": aug[index][-1],
        "nonzero_rows": [[row_index, value]
                         for row_index, value in enumerate(transform[index])
                         if value],
    }
    # Direct certificate check against original A and rhs.
    weights = transform[index]
    assert all(sum(weights[i] * matrix[i][j] for i in range(69)) % 3 == 0
               for j in range(14))
    assert sum(weights[i] * rhs[i] for i in range(69)) % 3 == certificate["pairing"]

result = {
    "status": "UNSAT-AFFINE-CERTIFICATE" if inconsistent else "SAT-DIRECT-REPLAY-PASS",
    "parent_model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "parent_replay_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "row_inventory": {"G5": 6, "R12_to_R7": 63},
    "matrix_shape": [69, 14],
    "rank_matrix": rank_matrix,
    "rank_augmented": augmented_rank,
    "matrix_sha256": hashlib.sha256(json.dumps(matrix,
        separators=(",", ":")).encode()).hexdigest(),
    "rhs_sha256": hashlib.sha256(json.dumps(rhs,
        separators=(",", ":")).encode()).hexdigest(),
    "left_null_certificate": certificate,
    "solution_H6_J6": solution,
}

if solution is not None:
    assert charged_rows(solution) == [0] * 69
    H6 = homogeneous(6, solution[:7])
    J6 = homogeneous(6, solution[7:])
    P5 = nadd(P, nscale(81, H6))
    Q5 = nadd(Q, nscale(81, J6))
    literal = determinant_minus_one(P5, Q5)
    degree5 = degree_part(literal, 5)
    assert all(value % 243 == 0 for value in degree5.values())
    high = {str(degree): [divide_exact(degree_part(literal, degree), 243)
                          .get((i, degree - i), 0) % 3
                          for i in range(degree + 1)]
            for degree in range(7, 13)}
    assert all(not any(values) for values in high.values())
    result["literal_degree5_divisible_243"] = True
    result["literal_terminal_rows"] = high

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("parent_model_sha256", result["parent_model_sha256"])
print("matrix_shape_rank_pair", 69, 14, rank_matrix, augmented_rank)
print("matrix_sha256", result["matrix_sha256"])
print("rhs_sha256", result["rhs_sha256"])
print("status", result["status"])
if certificate:
    print("left_null_nonzero_count", len(certificate["nonzero_rows"]))
    print("left_null_pairing", certificate["pairing"])
if solution is not None:
    print("solution_H6_J6", solution)
    print("literal_degree5_divisible_243", True)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-Q5-H6-AUDIT")

