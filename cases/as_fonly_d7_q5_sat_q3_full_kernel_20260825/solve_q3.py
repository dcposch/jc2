#!/usr/bin/env python3
"""Solve Q3+terminal rows over the complete pointwise Q4 kernel."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825"
          / "solve_full68.py")
EXPECTED_PARENT_SHA = (
    "ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

parent_output = Path(os.environ["PARENT_OUTPUT_JSON"])
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
namespace = {"__file__": str(PARENT), "__name__": "__q3_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), namespace)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

assert namespace["consistent"]
nadd = namespace["nadd"]
nscale = namespace["nscale"]
degree_part = namespace["degree_part"]
divide_exact = namespace["divide_exact"]
homogeneous_numeric = namespace["homogeneous_numeric"]
row = namespace["row"]
determinant_minus_one = namespace["determinant_minus_one"]
P5, Q5 = namespace["P5"], namespace["Q5"]
q4_particular = list(namespace["particular"])
q4_kernel = [list(vector) for vector in namespace["kernel"]]
kdim = len(q4_kernel)
variable_count = kdim + 10


def candidate(values):
    assert len(values) == variable_count
    q4_values = list(q4_particular)
    for scalar, vector in zip(values[:kdim], q4_kernel):
        q4_values = [(entry + scalar * direction) % 3
                     for entry, direction in zip(q4_values, vector)]
    offset = kdim
    h4values = values[offset:offset + 5]
    j4values = values[offset + 5:offset + 10]
    H = nadd(homogeneous_numeric(5, q4_values[:6]),
             homogeneous_numeric(4, h4values))
    J = nadd(homogeneous_numeric(5, q4_values[6:]),
             homogeneous_numeric(4, j4values))
    P = nadd(P5, nscale(81, H))
    Q = nadd(Q5, nscale(81, J))
    return P, Q, q4_values, h4values, j4values


def equations(values):
    P, Q, _, _, _ = candidate(values)
    determinant = determinant_minus_one(P, Q)
    q3 = row(divide_exact(degree_part(determinant, 3), 81), 3)
    terminal = []
    for degree in range(7, 13):
        terminal.extend(
            row(divide_exact(degree_part(determinant, degree), 243), degree))
    assert len(q3) == 4 and len(terminal) == 63
    return [(value % 3) for value in q3 + terminal]


constant = equations([0] * variable_count)
columns = []
for index in range(variable_count):
    basis = [0] * variable_count
    basis[index] = 1
    at_one = equations(basis)
    columns.append([(value - base) % 3
                    for value, base in zip(at_one, constant)])

design_count = 1 + 2 * variable_count
for index in range(variable_count):
    twice = [0] * variable_count
    twice[index] = 2
    assert equations(twice) == [
        (base + 2 * delta) % 3
        for base, delta in zip(constant, columns[index])]
for left in range(variable_count):
    for right in range(left + 1, variable_count):
        pair = [0] * variable_count
        pair[left] = pair[right] = 1
        assert equations(pair) == [
            (base + ldelta + rdelta) % 3
            for base, ldelta, rdelta in zip(
                constant, columns[left], columns[right])]
        design_count += 1

matrix = [[columns[column][row_index] for column in range(variable_count)]
          for row_index in range(67)]
rhs = [(-value) % 3 for value in constant]


def rref_solve(left, right):
    work = [[value % 3 for value in row_values] + [target % 3]
            for row_values, target in zip(left, right)]
    pivots = []
    pivot_row = 0
    for column in range(variable_count):
        chosen = next((row_index for row_index in range(pivot_row, len(work))
                       if work[row_index][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        inverse = 1 if work[pivot_row][column] == 1 else 2
        work[pivot_row] = [(inverse * value) % 3
                           for value in work[pivot_row]]
        for row_index in range(len(work)):
            if row_index != pivot_row and work[row_index][column]:
                scalar = work[row_index][column]
                work[row_index] = [
                    (value - scalar * pivot) % 3
                    for value, pivot in zip(work[row_index], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
    contradictions = [row_values for row_values in work
                      if not any(row_values[:-1]) and row_values[-1]]
    if contradictions:
        return len(pivots), len(pivots) + 1, pivots, None, [], contradictions
    particular = [0] * variable_count
    for row_index, column in enumerate(pivots):
        particular[column] = work[row_index][-1]
    free = [column for column in range(variable_count) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * variable_count
        vector[free_column] = 1
        for row_index, pivot_column in enumerate(pivots):
            vector[pivot_column] = (-work[row_index][free_column]) % 3
        kernel.append(vector)
    return len(pivots), len(pivots), pivots, particular, kernel, []


(rank, augmented_rank, pivots, particular,
 kernel, contradictions) = rref_solve(matrix, rhs)
consistent = particular is not None


def v3(value):
    if value == 0:
        return None
    value = abs(value)
    exponent = 0
    while value % 3 == 0:
        value //= 3
        exponent += 1
    return exponent


def valuation_table(P, Q):
    determinant = determinant_minus_one(P, Q)
    answer = {}
    for degree in range(13):
        values = list(degree_part(determinant, degree).values())
        nonzero = [v3(value) for value in values if value]
        answer[str(degree)] = {
            "coefficient_count": len(values),
            "nonzero_coefficient_count": len(nonzero),
            "minimum_v3": (min(nonzero) if nonzero else None),
            "divisible_by_81": all(value % 81 == 0 for value in values),
            "divisible_by_243": all(value % 243 == 0 for value in values),
            "divisible_by_729": all(value % 729 == 0 for value in values),
        }
    return answer


zero_P, zero_Q, _, _, _ = candidate([0] * variable_count)
result = {
    "status": ("PASS-AS-Q5-Q3-FULL-KERNEL-SAT" if consistent
               else "PASS-AS-Q5-Q3-FULL-KERNEL-UNSAT"),
    "parent_sha256": EXPECTED_PARENT_SHA,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "parent_output_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "parent_stdout_sha256": hashlib.sha256(
        parent_stdout.getvalue().encode()).hexdigest(),
    "q4_kernel_dimension_consumed": kdim,
    "matrix_shape": [67, variable_count],
    "matrix_sha256": hashlib.sha256(bytes(
        value for row_values in matrix for value in row_values)).hexdigest(),
    "rhs_sha256": hashlib.sha256(bytes(rhs)).hexdigest(),
    "quadratic_design_point_count": design_count,
    "affine_whole_cube_proof_from_quadratic_design": True,
    "rank": rank,
    "augmented_rank": augmented_rank,
    "pivot_columns": pivots,
    "consistent": consistent,
    "particular": particular,
    "kernel_basis": kernel,
    "solution_count": (3 ** len(kernel) if consistent else 0),
    "contradictions": contradictions,
    "zero_h4_j4_control_nonzero_rows": [
        index for index, value in enumerate(constant) if value],
    "pre_q3_valuation_by_degree": valuation_table(zero_P, zero_Q),
    "full_integer_replay_passed": False,
    "scope": "one full Q4 affine fibre; exact Q3+terminal gate",
    "refusal_scope": [
        "not the whole Q5 locus",
        "not Q2 through Q0 or a complete map modulo 243",
        "not all-depth, counterexample, or JC2",
    ],
}

if consistent:
    assert equations(particular) == [0] * 67
    P, Q, q4_values, h4values, j4values = candidate(particular)
    determinant = determinant_minus_one(P, Q)
    q4 = row(divide_exact(degree_part(determinant, 4), 81), 4)
    q3 = row(divide_exact(degree_part(determinant, 3), 81), 3)
    terminal = []
    for degree in range(7, 13):
        terminal.extend(
            row(divide_exact(degree_part(determinant, degree), 243), degree))
    assert q4 == [0] * 5 and q3 == [0] * 4
    assert terminal == [0] * 63
    assert all(value % 729 == 0 for (i, j), value in determinant.items()
               if 7 <= i + j <= 12)
    result.update({
        "full_integer_replay_passed": True,
        "q4_values": q4_values,
        "h4_values": h4values,
        "j4_values": j4values,
        "q4_literal_div81_mod3": q4,
        "q3_literal_div81_mod3": q3,
        "terminal_literal_div243_mod3": terminal,
        "post_q3_valuation_by_degree": valuation_table(P, Q),
    })

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("variables", variable_count, "design_points", design_count)
print("rank", rank, "augmented_rank", augmented_rank,
      "consistent", consistent, "kernel", len(kernel))
print("pre_v3", {degree: row_data["minimum_v3"] for degree, row_data
                 in result["pre_q3_valuation_by_degree"].items()})
if consistent:
    print("post_v3", {degree: row_data["minimum_v3"] for degree, row_data
                     in result["post_q3_valuation_by_degree"].items()})
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])

