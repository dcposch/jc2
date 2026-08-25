#!/usr/bin/env python3
"""Exact third-Bockstein solver for the complete fixed-D7 output cone."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
SOURCE = (ROOT / "cases/as_fonly_d7_q3_full_output_cone_z9_20260825"
          / "solve_full_output_cone_z9.py")
EXPECTED_SOURCE = "2d2e0f5fa03c663201157d109a961055ebe1b3daad552b34954f20a633de32f7"
payload = SOURCE.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_SOURCE
marker = b"\nbase = []\n"
assert payload.count(marker) == 1
ns = {"__file__": str(SOURCE), "__name__": "__z27_parent_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload.split(marker, 1)[0] + b"\n",
                 str(SOURCE), "exec"), ns)

nadd, nscale = ns["nadd"], ns["nscale"]
determinant_minus_one = ns["determinant_minus_one"]
q3_candidate = ns["q3_candidate"]
q3_particular = list(ns["q3_particular"])
q3_kernel = [list(vector) for vector in ns["q3_kernel"]]
slots = list(ns["slots"])
support = list(ns["support"])
candidate = ns["candidate"]
correction = ns["correction"]
P0, Q0, _, _, _ = q3_candidate(q3_particular)
D0 = determinant_minus_one(P0, Q0)
assert len(slots) == 91 and len(support) == 36


def coefficient(poly, xy):
    return poly.get(xy, 0)


def dot(row, vector):
    return sum(a * b for a, b in zip(row, vector))


def rref_solve(matrix, rhs, modulus=3):
    work = [[value % modulus for value in row] + [target % modulus]
            for row, target in zip(matrix, rhs)]
    pivots = []
    row = 0
    for column in range(len(matrix[0])):
        chosen = next((r for r in range(row, len(work))
                       if work[r][column]), None)
        if chosen is None:
            continue
        work[row], work[chosen] = work[chosen], work[row]
        inverse = pow(work[row][column], -1, modulus)
        work[row] = [(inverse * value) % modulus for value in work[row]]
        for r in range(len(work)):
            if r == row or not work[r][column]:
                continue
            scalar = work[r][column]
            work[r] = [(a - scalar * b) % modulus
                       for a, b in zip(work[r], work[row])]
        pivots.append(column)
        row += 1
    contradictions = [r for r in range(len(work))
                      if not any(work[r][:-1]) and work[r][-1]]
    if contradictions:
        return len(pivots), None, []
    particular = [0] * len(matrix[0])
    for r, column in enumerate(pivots):
        particular[column] = work[r][-1]
    free = [column for column in range(len(matrix[0]))
            if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * len(matrix[0])
        vector[free_column] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = (-work[r][free_column]) % modulus
        kernel.append(vector)
    return len(pivots), particular, kernel


def rank(matrix):
    if not matrix:
        return 0
    zero = [0] * len(matrix)
    # Transpose because rref_solve expects equations as rows.
    transposed = [list(column) for column in zip(*matrix)]
    answer, _, _ = rref_solve(transposed, [0] * len(transposed))
    return answer


base_integer = []
for xy in slots:
    value = coefficient(D0, xy)
    assert value % 27 == 0
    base_integer.append(value // 27)

column_polys = []
columns_integer = []
for column in range(72):
    values = [0] * 72
    values[column] = 1
    P, Q = candidate(values)
    determinant = determinant_minus_one(P, Q)
    column_polys.append(determinant)
    current = []
    for xy in slots:
        delta = coefficient(determinant, xy) - coefficient(D0, xy)
        assert delta % 27 == 0
        current.append(delta // 27)
    columns_integer.append(current)
matrix_integer = [[columns_integer[column][row] for column in range(72)]
                  for row in range(91)]

# Exact linearity modulo 27 after division by 27: only a P/Q fresh pair can
# contribute a quadratic term, and it is a multiple of 729 before division.
pair_controls = 0
for left_column in range(36):
    for right_column in range(36, 72):
        values = [0] * 72
        values[left_column] = values[right_column] = 1
        P, Q = candidate(values)
        determinant = determinant_minus_one(P, Q)
        for row, xy in enumerate(slots):
            remainder = (coefficient(determinant, xy)
                         - coefficient(column_polys[left_column], xy)
                         - coefficient(column_polys[right_column], xy)
                         + coefficient(D0, xy))
            assert remainder % 729 == 0
            assert (coefficient(determinant, xy) // 27) % 27 == (
                base_integer[row] + matrix_integer[row][left_column]
                + matrix_integer[row][right_column]) % 27
        pair_controls += 1
assert pair_controls == 1296

# The reviewed Q3 fibre directions are literal order-81 D7-supported output
# changes.  Their product with any order-27 fresh basis is order 2187, so the
# absorption into T by a multiple of three remains exact modulo 729.
q3_fresh_controls = 0
for direction in q3_kernel:
    q3_values = [(value + delta) % 3 for value, delta in zip(
        q3_particular, direction)]
    P1, Q1, _, _, _ = q3_candidate(q3_values)
    for poly1, poly0 in ((P1, P0), (Q1, Q0)):
        assert all(sum(xy) <= 7 for xy in set(poly1) | set(poly0))
        assert all((coefficient(poly1, xy) - coefficient(poly0, xy)) % 81 == 0
                   for xy in set(poly1) | set(poly0))
    D1 = determinant_minus_one(P1, Q1)
    for column in range(72):
        values = [0] * 72
        values[column] = 1
        left, right = correction(values)
        D0fresh = determinant_minus_one(
            nadd(P0, nscale(27, left)), nadd(Q0, nscale(27, right)))
        D1fresh = determinant_minus_one(
            nadd(P1, nscale(27, left)), nadd(Q1, nscale(27, right)))
        assert all((coefficient(D1fresh, xy) - coefficient(D1, xy)
                    - coefficient(D0fresh, xy) + coefficient(D0, xy))
                   % 2187 == 0 for xy in slots)
        q3_fresh_controls += 1

A3 = [[value % 3 for value in row] for row in matrix_integer]
rhs0 = [(-value) % 3 for value in base_integer]
rank0, p0, K0 = rref_solve(A3, rhs0)
assert p0 is not None and rank0 == 27 and len(K0) == 45

# First Bockstein: T = p0 + K0*s0 + 3*x1.
carry0 = []
for row in range(91):
    numerator = base_integer[row] + dot(matrix_integer[row], p0)
    assert numerator % 3 == 0
    carry0.append((numerator // 3) % 3)
K0_carries = []
for vector in K0:
    current = []
    for row in range(91):
        numerator = dot(matrix_integer[row], vector)
        assert numerator % 3 == 0
        current.append((numerator // 3) % 3)
    K0_carries.append(current)
matrix1 = [[K0_carries[column][row] for column in range(len(K0))]
           + A3[row] for row in range(91)]
rank1, p1, K1 = rref_solve(matrix1, [(-value) % 3 for value in carry0])
assert p1 is not None

def stage1_to_T(vector):
    assert len(vector) == len(K0) + 72
    answer = list(p0)
    for scalar, direction in zip(vector[:len(K0)], K0):
        answer = [value + scalar * delta
                  for value, delta in zip(answer, direction)]
    answer = [value + 3 * digit
              for value, digit in zip(answer, vector[len(K0):])]
    return answer


T9_base = stage1_to_T(p1)
T9_directions = [stage1_to_T(direction) for direction in K1]
# stage1_to_T includes p0 even on a direction; remove its affine constant.
T9_directions = [[value - base for value, base in zip(direction, p0)]
                 for direction in T9_directions]

for row in range(91):
    assert (base_integer[row] + dot(matrix_integer[row], T9_base)) % 9 == 0
for direction in T9_directions:
    assert all(dot(row, direction) % 9 == 0 for row in matrix_integer)

# Second Bockstein: T = T9_base + K1tilde*s1 + 9*x2.
carry1 = []
for row in range(91):
    numerator = base_integer[row] + dot(matrix_integer[row], T9_base)
    assert numerator % 9 == 0
    carry1.append((numerator // 9) % 3)
K1_carries = []
for direction in T9_directions:
    current = []
    for row in range(91):
        numerator = dot(matrix_integer[row], direction)
        assert numerator % 9 == 0
        current.append((numerator // 9) % 3)
    K1_carries.append(current)
matrix2 = [[K1_carries[column][row] for column in range(len(K1))]
           + A3[row] for row in range(91)]
rank2, p2, K2 = rref_solve(matrix2, [(-value) % 3 for value in carry1])

result = {
    "status": "PASS-AS-Q3-FULL-OUTPUT-CONE-Z27",
    "source_sha256": EXPECTED_SOURCE,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "q3_parent_output_sha256": hashlib.sha256(
        Path(os.environ["PARENT_OUTPUT_JSON"]).read_bytes()).hexdigest(),
    "previous_z9_result_sha256": hashlib.sha256(
        Path(os.environ["PREVIOUS_Z9_RESULT_JSON"]).read_bytes()).hexdigest(),
    "slot_count": 91,
    "variable_count_over_z27": 72,
    "pair_control_count": pair_controls,
    "q3_fresh_mixed_control_count": q3_fresh_controls,
    "q3_fresh_mixed_terms_divisible_by2187": True,
    "exact_linearity_mod27_after_division_by27": True,
    "matrix_integer_sha256": hashlib.sha256(json.dumps(
        matrix_integer, separators=(",", ":")).encode()).hexdigest(),
    "stage_mod3": {"rank": rank0, "kernel_dimension": len(K0)},
    "stage_mod9": {"rank": rank1, "kernel_dimension": len(K1)},
    "stage_mod27": {"rank": rank2, "consistent": p2 is not None,
                    "kernel_dimension": (len(K2) if p2 is not None else None)},
    "previous_mod243_solution_exponent": len(K1),
    "scope": "complete fixed-D7 output cone modulo729 over one pinned Q3 fibre",
    "refusal_scope": [
        "not the whole predecessor scheme",
        "no order729 digit or deeper/all-depth lift",
        "no collision, characteristic-zero point, counterexample, or JC2",
    ],
}

previous = json.loads(Path(os.environ["PREVIOUS_Z9_RESULT_JSON"]).read_text())
stored9 = list(previous["combined_z9_particular"])
assert all((base_integer[row] + dot(matrix_integer[row], stored9)) % 9 == 0
           for row in range(91))
stored_carry = [((base_integer[row] + dot(matrix_integer[row], stored9)) // 9)
                % 3 for row in range(91)]
stored_rank, stored_w, _ = rref_solve(A3, [(-value) % 3
                                          for value in stored_carry])
result["stored_z9_particular_lifts"] = stored_w is not None
result["stored_z9_particular_next_rank"] = stored_rank

if p2 is not None:
    lower_projection_columns = [vector[:len(K1)] for vector in K2]
    projection_dimension = rank(lower_projection_columns)
    assert len(K2) == projection_dimension + len(K0)
    result["liftable_previous_mod243_dimension"] = projection_dimension
    result["liftable_previous_mod243_count"] = 3 ** projection_dimension
    result["liftable_previous_fraction_power_of_3"] = (
        projection_dimension - len(K1))
    result["new_mod729_solution_exponent"] = len(K2)
    result["new_mod729_solution_count"] = 3 ** len(K2)

    T = list(T9_base)
    for scalar, direction in zip(p2[:len(K1)], T9_directions):
        T = [value + scalar * delta for value, delta in zip(T, direction)]
    T = [value + 9 * digit for value, digit in zip(T, p2[len(K1):])]
    T = [value % 27 for value in T]
    assert all((base_integer[row] + dot(matrix_integer[row], T)) % 27 == 0
               for row in range(91))
    P, Q = candidate(T)
    determinant = determinant_minus_one(P, Q)
    all_keys = set(determinant)
    assert all(sum(xy) <= 12 for xy in all_keys)
    assert all(coefficient(determinant, xy) % 729 == 0 for xy in slots)
    assert all(coefficient(P, xy) % 3 == coefficient({(1, 0): 1,
                                                      (3, 0): -1}, xy) % 3
               for xy in set(P) | {(1, 0), (3, 0)})
    assert all(coefficient(Q, xy) % 3 == coefficient({(0, 1): 1}, xy) % 3
               for xy in set(Q) | {(0, 1)})
    result.update({
        "combined_z27_particular": T,
        "literal_integer_replay_mod729_passed": True,
        "determinant_sha256": hashlib.sha256(
            repr(sorted(determinant.items())).encode()).hexdigest(),
        "P_support": [[i, j, value] for (i, j), value in sorted(P.items())],
        "Q_support": [[i, j, value] for (i, j), value in sorted(Q.items())],
    })

encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("stages", rank0, len(K0), rank1, len(K1), rank2,
      (len(K2) if p2 is not None else None))
print("stored_lifts", result["stored_z9_particular_lifts"])
if p2 is not None:
    print("liftable_previous_dimension",
          result["liftable_previous_mod243_dimension"], "of", len(K1))
    print("new_solution_exponent", result["new_mod729_solution_exponent"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
