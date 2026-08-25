#!/usr/bin/env python3
"""Exact Z/9 Bockstein solver for the complete fixed-D7 output-digit cone."""

from __future__ import annotations

import contextlib
import hashlib
import io
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
ns = {"__file__": str(PARENT), "__name__": "__z9_parent_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload.split(marker, 1)[0] + b"\n", str(PARENT), "exec"), ns)

nadd, nscale = ns["nadd"], ns["nscale"]
determinant_minus_one = ns["determinant_minus_one"]
q3_candidate = ns["q3_candidate"]
q3_particular = list(ns["q3_particular"])
q3_kernel = [list(vector) for vector in ns["q3_kernel"]]
slots = list(ns["slots"])
assert len(slots) == 91 and slots[8] == (2, 1)

P0, Q0, _, _, _ = q3_candidate(q3_particular)
D0 = determinant_minus_one(P0, Q0)

support = [(i, degree - i) for degree in range(8)
           for i in range(degree + 1)]
assert len(support) == 36
variable_names = ([f"P_{i}_{j}" for i, j in support]
                  + [f"Q_{i}_{j}" for i, j in support])
variable_degrees = [i + j for i, j in support] * 2
variable_count = len(variable_names)
assert variable_count == 72


def coefficient(poly, xy):
    return poly.get(xy, 0)


def correction(values):
    assert len(values) == variable_count
    left = {xy: values[index] for index, xy in enumerate(support)
            if values[index]}
    right = {xy: values[36 + index] for index, xy in enumerate(support)
             if values[36 + index]}
    return left, right


def candidate(values):
    left, right = correction(values)
    return nadd(P0, nscale(27, left)), nadd(Q0, nscale(27, right))


base = []
for xy in slots:
    value = coefficient(D0, xy)
    assert value % 27 == 0, (xy, value)
    base.append((value // 27) % 9)

columns = []
basis_determinants = []
for column in range(variable_count):
    values = [0] * variable_count
    values[column] = 1
    P, Q = candidate(values)
    determinant = determinant_minus_one(P, Q)
    basis_determinants.append(determinant)
    output_column = []
    for xy in slots:
        delta = coefficient(determinant, xy) - coefficient(D0, xy)
        assert delta % 27 == 0
        output_column.append((delta // 27) % 9)
    columns.append(output_column)

matrix9 = [[columns[column][row] for column in range(variable_count)]
           for row in range(len(slots))]

# Exact negative controls for the claimed Z/9 linearization.  Doubling a
# monomial and every P/Q monomial pair agree with the affine rebuild modulo 9
# after exact division by 27.  The pair remainder itself is divisible by 729.
for column in range(variable_count):
    values = [0] * variable_count
    values[column] = 2
    P, Q = candidate(values)
    determinant = determinant_minus_one(P, Q)
    for row, xy in enumerate(slots):
        actual = coefficient(determinant, xy)
        assert actual % 27 == 0
        assert (actual // 27) % 9 == (
            base[row] + 2 * matrix9[row][column]) % 9

pair_control_count = 0
for left_column in range(36):
    for right_column in range(36, 72):
        values = [0] * variable_count
        values[left_column] = values[right_column] = 1
        P, Q = candidate(values)
        determinant = determinant_minus_one(P, Q)
        left_det = basis_determinants[left_column]
        right_det = basis_determinants[right_column]
        for row, xy in enumerate(slots):
            remainder = (coefficient(determinant, xy)
                         - coefficient(left_det, xy)
                         - coefficient(right_det, xy)
                         + coefficient(D0, xy))
            assert remainder % 729 == 0, (left_column, right_column, xy)
            assert (coefficient(determinant, xy) // 27) % 9 == (
                base[row] + matrix9[row][left_column]
                + matrix9[row][right_column]) % 9
        pair_control_count += 1
assert pair_control_count == 36 * 36


def rref_with_left(matrix, rhs):
    rows = len(matrix)
    columns_count = len(matrix[0])
    work = [[value % 3 for value in row] + [target % 3]
            for row, target in zip(matrix, rhs)]
    left_ops = [[1 if i == j else 0 for j in range(rows)]
                for i in range(rows)]
    pivots = []
    pivot_row = 0
    for column in range(columns_count):
        chosen = next((row for row in range(pivot_row, rows)
                       if work[row][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        left_ops[pivot_row], left_ops[chosen] = (
            left_ops[chosen], left_ops[pivot_row])
        if work[pivot_row][column] == 2:
            work[pivot_row] = [(2 * value) % 3
                               for value in work[pivot_row]]
            left_ops[pivot_row] = [(2 * value) % 3
                                   for value in left_ops[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            scalar = work[row][column]
            work[row] = [(value - scalar * pivot) % 3
                         for value, pivot in zip(work[row], work[pivot_row])]
            left_ops[row] = [(value - scalar * pivot) % 3
                             for value, pivot in zip(
                                 left_ops[row], left_ops[pivot_row])]
        pivots.append(column)
        pivot_row += 1
    contradictions = []
    for row in range(rows):
        if not any(work[row][:-1]) and work[row][-1]:
            inverse = 1 if work[row][-1] == 1 else 2
            witness = [(inverse * value) % 3 for value in left_ops[row]]
            assert all(sum(witness[i] * matrix[i][j] for i in range(rows))
                       % 3 == 0 for j in range(columns_count))
            assert sum(witness[i] * rhs[i] for i in range(rows)) % 3 == 1
            contradictions.append(witness)
    if contradictions:
        return len(pivots), len(pivots) + 1, None, [], contradictions
    particular = [0] * columns_count
    for row, column in enumerate(pivots):
        particular[column] = work[row][-1]
    free = [column for column in range(columns_count)
            if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * columns_count
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-work[row][free_column]) % 3
        kernel.append(vector)
    return len(pivots), len(pivots), particular, kernel, []


matrix3 = [[value % 3 for value in row] for row in matrix9]
rhs3 = [(-value) % 3 for value in base]
(rank3, augmented3, particular3, kernel3,
 contradictions3) = rref_with_left(matrix3, rhs3)

result = {
    "status": "PASS-AS-Q3-FULL-OUTPUT-CONE-Z9",
    "parent_sha256": EXPECTED,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "q3_parent_output_sha256": hashlib.sha256(
        Path(os.environ["PARENT_OUTPUT_JSON"]).read_bytes()).hexdigest(),
    "slot_order": [list(xy) for xy in slots],
    "support": [list(xy) for xy in support],
    "combined_z9_variable_count": variable_count,
    "constant_columns": [index for index, degree in enumerate(variable_degrees)
                         if degree == 0],
    "constant_columns_identically_zero": all(
        not any(matrix9[row][column] for row in range(len(slots)))
        for column, degree in enumerate(variable_degrees) if degree == 0),
    "pair_control_count": pair_control_count,
    "linear_mod9_from_bilinearity_and_729_vanishing": True,
    "matrix_mod9_sha256": hashlib.sha256(bytes(
        value for row in matrix9 for value in row)).hexdigest(),
    "rhs_mod9_sha256": hashlib.sha256(bytes(base)).hexdigest(),
    "stage_mod3": {
        "rank": rank3,
        "augmented_rank": augmented3,
        "consistent": particular3 is not None,
        "kernel_dimension": len(kernel3),
        "left_null_witness": (contradictions3[0]
                              if contradictions3 else None),
    },
    "q3_kernel_dimension_absorbed": len(q3_kernel),
    "q3_kernel_absorbed_by_order81_output_space": True,
    "row8_nonzero_z9_columns": [
        {"column": column, "name": variable_names[column],
         "degree": variable_degrees[column],
         "coefficient_mod9": matrix9[8][column]}
        for column in range(variable_count) if matrix9[8][column]],
    "scope": ("complete fixed-D7 output coefficient digits at orders 27/81 "
              "over one pinned Q3 fibre"),
    "refusal_scope": [
        "no order243 digits or terminal-mod729 closure",
        "not the whole Q5/global predecessor scheme",
        "not all-depth/counterexample/JC2",
    ],
}

if particular3 is None:
    result["z9_consistent"] = False
    result["z9_left_null_stage"] = "mod3"
else:
    # Every mod-3 solution is p+K*s.  Do not reduce that integer expression
    # before lifting: quotient changes are absorbed by the free high digit.
    lift_base = []
    for row in range(len(slots)):
        numerator = base[row] + sum(
            matrix9[row][column] * particular3[column]
            for column in range(variable_count))
        assert numerator % 3 == 0
        lift_base.append((numerator // 3) % 3)
    kernel_carry_columns = []
    for vector in kernel3:
        column_values = []
        for row in range(len(slots)):
            numerator = sum(matrix9[row][column] * vector[column]
                            for column in range(variable_count))
            assert numerator % 3 == 0
            column_values.append((numerator // 3) % 3)
        kernel_carry_columns.append(column_values)
    bockstein_matrix = []
    for row in range(len(slots)):
        bockstein_matrix.append(
            [column[row] for column in kernel_carry_columns]
            + matrix3[row])
    bockstein_rhs = [(-value) % 3 for value in lift_base]
    (brank, baug, bparticular, bkernel,
     bcontradictions) = rref_with_left(bockstein_matrix, bockstein_rhs)
    result["bockstein"] = {
        "matrix_shape": [len(slots), len(kernel3) + variable_count],
        "rank": brank,
        "augmented_rank": baug,
        "consistent": bparticular is not None,
        "kernel_dimension": len(bkernel),
        "matrix_sha256": hashlib.sha256(bytes(
            value for row in bockstein_matrix for value in row)).hexdigest(),
        "rhs_sha256": hashlib.sha256(bytes(bockstein_rhs)).hexdigest(),
        "left_null_witness": (bcontradictions[0]
                              if bcontradictions else None),
    }
    result["z9_consistent"] = bparticular is not None
    if bparticular is None:
        result["z9_left_null_stage"] = "bockstein"
    else:
        parameters = bparticular[:len(kernel3)]
        high_digits = bparticular[len(kernel3):]
        combined = []
        for column in range(variable_count):
            value = (particular3[column]
                     + sum(scalar * vector[column]
                           for scalar, vector in zip(parameters, kernel3))
                     + 3 * high_digits[column]) % 9
            combined.append(value)
        assert all((base[row] + sum(
            matrix9[row][column] * combined[column]
            for column in range(variable_count))) % 9 == 0
                   for row in range(len(slots)))
        P, Q = candidate(combined)
        determinant = determinant_minus_one(P, Q)
        assert all(coefficient(determinant, xy) % 243 == 0 for xy in slots)
        low_digits = [value % 3 for value in combined]
        order81_digits = [value // 3 for value in combined]
        assert all(value == low + 3 * high for value, low, high in zip(
            combined, low_digits, order81_digits))
        result.update({
            "literal_integer_replay_mod243_passed": True,
            "combined_z9_particular": combined,
            "order27_digits": low_digits,
            "order81_digits": order81_digits,
            "solution_count": 3 ** len(bkernel),
            "determinant_sha256": hashlib.sha256(
                repr(sorted(determinant.items())).encode()).hexdigest(),
        })

# Directly prove absorption of every reviewed Q3-kernel direction by the
# arbitrary order-81 output space.  Differences are 81 times D7-supported
# polynomials, so they are T-increments divisible by three in Z/9.  Also run
# the complete mixed second-difference design against all 72 fresh bases:
# an 81*K by 27*E cross term must be divisible by 2187, not merely 243.
q3_fresh_mixed_control_count = 0
for direction in q3_kernel:
    values = [(entry + delta) % 3 for entry, delta in zip(
        q3_particular, direction)]
    P1, Q1, _, _, _ = q3_candidate(values)
    for poly1, poly0 in ((P1, P0), (Q1, Q0)):
        keys = set(poly1) | set(poly0)
        assert all(sum(xy) <= 7 for xy in keys)
        for xy in keys:
            assert (coefficient(poly1, xy) - coefficient(poly0, xy)) % 81 == 0
    D1 = determinant_minus_one(P1, Q1)
    for column in range(variable_count):
        fresh = [0] * variable_count
        fresh[column] = 1
        left, right = correction(fresh)
        D0fresh = determinant_minus_one(
            nadd(P0, nscale(27, left)), nadd(Q0, nscale(27, right)))
        D1fresh = determinant_minus_one(
            nadd(P1, nscale(27, left)), nadd(Q1, nscale(27, right)))
        for xy in slots:
            mixed = (coefficient(D1fresh, xy) - coefficient(D1, xy)
                     - coefficient(D0fresh, xy) + coefficient(D0, xy))
            assert mixed % 2187 == 0, (column, xy, mixed)
        q3_fresh_mixed_control_count += 1

result["q3_fresh_mixed_control_count"] = q3_fresh_mixed_control_count
result["q3_fresh_mixed_terms_divisible_by_2187"] = True

result["nonzero_column_degree_histogram"] = dict(sorted(Counter(
    variable_degrees[column] for column in range(variable_count)
    if any(matrix9[row][column] for row in range(len(slots)))).items()))
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("variables", variable_count, "mod3", rank3, augmented3,
      "kernel", len(kernel3))
if "bockstein" in result:
    print("bockstein", result["bockstein"]["rank"],
          result["bockstein"]["augmented_rank"],
          "kernel", result["bockstein"]["kernel_dimension"])
print("row8_columns", result["row8_nonzero_z9_columns"])
print("z9_consistent", result["z9_consistent"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
