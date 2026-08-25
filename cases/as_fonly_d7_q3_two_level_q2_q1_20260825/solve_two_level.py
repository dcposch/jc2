#!/usr/bin/env python3
"""Exact triangular affine carry compiler for Q2 and Q1."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q5_sat_q3_full_kernel_20260825"
          / "solve_q3.py")
EXPECTED_PARENT_SHA = (
    "14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

parent_output = Path(os.environ["PARENT_OUTPUT_JSON"])
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
namespace = {"__file__": str(PARENT), "__name__": "__two_level_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), namespace)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

assert namespace["consistent"]
nadd = namespace["nadd"]
nscale = namespace["nscale"]
homogeneous_numeric = namespace["homogeneous_numeric"]
determinant_minus_one = namespace["determinant_minus_one"]
q3_candidate = namespace["candidate"]
q3_particular = list(namespace["particular"])
q3_kernel = [list(vector) for vector in namespace["kernel"]]
q3_kdim = len(q3_kernel)

slots = [(i, total - i) for total in range(13)
         for i in range(total + 1)]
assert len(slots) == 91
high_slots = [xy for xy in slots if 7 <= sum(xy) <= 12]
assert len(high_slots) == 63
fresh_count = 28
raw_variable_count = q3_kdim + fresh_count


def raw_candidate(values):
    assert len(values) == raw_variable_count
    q3_values = list(q3_particular)
    for scalar, vector in zip(values[:q3_kdim], q3_kernel):
        q3_values = [(entry + scalar * direction) % 3
                     for entry, direction in zip(q3_values, vector)]
    P, Q, _, _, _ = q3_candidate(q3_values)
    offset = q3_kdim

    def block(degree):
        nonlocal offset
        width = degree + 1
        left = values[offset:offset + width]
        offset += width
        right = values[offset:offset + width]
        offset += width
        return (homogeneous_numeric(degree, left),
                homogeneous_numeric(degree, right), left, right)

    W3, Z3, w3values, z3values = block(3)
    W2, Z2, w2values, z2values = block(2)
    H3, J3, h3values, j3values = block(3)
    H2, J2, h2values, j2values = block(2)
    assert offset == raw_variable_count
    P = nadd(P, nscale(27, nadd(W3, W2)),
             nscale(81, nadd(H3, H2)))
    Q = nadd(Q, nscale(27, nadd(Z3, Z2)),
             nscale(81, nadd(J3, J2)))
    blocks = {
        "W3": w3values, "Z3": z3values,
        "W2": w2values, "Z2": z2values,
        "H3": h3values, "J3": j3values,
        "H2": h2values, "J2": j2values,
    }
    return P, Q, q3_values, blocks


def raw_rows(values, divisor, selected_slots):
    P, Q, _, _ = raw_candidate(values)
    determinant = determinant_minus_one(P, Q)
    result = []
    for xy in selected_slots:
        coefficient = determinant.get(xy, 0)
        assert coefficient % divisor == 0, (xy, coefficient, divisor)
        result.append((coefficient // divisor) % 3)
    return result


def parameterize(particular, kernel, coordinates):
    assert len(coordinates) == len(kernel)
    values = list(particular)
    for scalar, vector in zip(coordinates, kernel):
        values = [(entry + scalar * direction) % 3
                  for entry, direction in zip(values, vector)]
    return values


def extract_affine(function, variable_count):
    constant = function([0] * variable_count)
    columns = []
    for index in range(variable_count):
        basis = [0] * variable_count
        basis[index] = 1
        at_one = function(basis)
        columns.append([(value - base) % 3
                        for value, base in zip(at_one, constant)])
    design_count = 1 + 2 * variable_count
    for index in range(variable_count):
        twice = [0] * variable_count
        twice[index] = 2
        assert function(twice) == [
            (base + 2 * delta) % 3
            for base, delta in zip(constant, columns[index])]
    for left in range(variable_count):
        for right in range(left + 1, variable_count):
            pair = [0] * variable_count
            pair[left] = pair[right] = 1
            assert function(pair) == [
                (base + ldelta + rdelta) % 3
                for base, ldelta, rdelta in zip(
                    constant, columns[left], columns[right])]
            design_count += 1
    matrix = [[columns[column][row_index]
               for column in range(variable_count)]
              for row_index in range(len(constant))]
    return constant, matrix, design_count


def rref_solve(matrix, constant):
    variable_count = len(matrix[0])
    work = [[value % 3 for value in row_values] + [(-base) % 3]
            for row_values, base in zip(matrix, constant)]
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
        return len(pivots), len(pivots) + 1, None, [], contradictions
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
    return len(pivots), len(pivots), particular, kernel, []


stages = []

# Stage 27 -> 81 on all determinant slots.
stage1_function = lambda values: raw_rows(values, 27, slots)
c1, m1, design1 = extract_affine(stage1_function, raw_variable_count)
r1, a1, p1, k1, bad1 = rref_solve(m1, c1)
stages.append({"divisor": 27, "row_count": 91,
               "input_dimension": raw_variable_count,
               "design_count": design1, "rank": r1,
               "augmented_rank": a1, "consistent": p1 is not None,
               "kernel_dimension": len(k1), "contradictions": bad1,
               "matrix_sha256": hashlib.sha256(bytes(
                   value for row_values in m1 for value in row_values)).hexdigest()})

if p1 is not None:
    stage2_function = lambda coordinates: raw_rows(
        parameterize(p1, k1, coordinates), 81, slots)
    c2, m2, design2 = extract_affine(stage2_function, len(k1))
    r2, a2, p2, k2, bad2 = rref_solve(m2, c2)
    stages.append({"divisor": 81, "row_count": 91,
                   "input_dimension": len(k1),
                   "design_count": design2, "rank": r2,
                   "augmented_rank": a2, "consistent": p2 is not None,
                   "kernel_dimension": len(k2), "contradictions": bad2,
                   "matrix_sha256": hashlib.sha256(bytes(
                       value for row_values in m2 for value in row_values)).hexdigest()})
else:
    p2, k2 = None, []

if p2 is not None:
    stage2_raw_particular = parameterize(p1, k1, p2)

    def stage2_raw(coordinates):
        stage2_coordinates = parameterize(p2, k2, coordinates)
        return parameterize(p1, k1, stage2_coordinates)

    stage3_function = lambda coordinates: raw_rows(
        stage2_raw(coordinates), 243, high_slots)
    c3, m3, design3 = extract_affine(stage3_function, len(k2))
    r3, a3, p3, k3, bad3 = rref_solve(m3, c3)
    stages.append({"divisor": 243, "row_count": 63,
                   "input_dimension": len(k2),
                   "design_count": design3, "rank": r3,
                   "augmented_rank": a3, "consistent": p3 is not None,
                   "kernel_dimension": len(k3), "contradictions": bad3,
                   "matrix_sha256": hashlib.sha256(bytes(
                       value for row_values in m3 for value in row_values)).hexdigest()})
else:
    p3, k3 = None, []

consistent = p3 is not None
result = {
    "status": ("PASS-AS-Q3-TWO-LEVEL-Q2-Q1-SAT" if consistent
               else "PASS-AS-Q3-TWO-LEVEL-Q2-Q1-UNSAT"),
    "parent_sha256": EXPECTED_PARENT_SHA,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "parent_output_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "parent_stdout_sha256": hashlib.sha256(
        parent_stdout.getvalue().encode()).hexdigest(),
    "q3_kernel_dimension_consumed": q3_kdim,
    "fresh_variable_count": fresh_count,
    "raw_variable_count": raw_variable_count,
    "staged_affine_not_single_unconditional_affine": True,
    "stages": stages,
    "consistent": consistent,
    "full_integer_replay_passed": False,
    "scope": "one Q3 affine fibre; exact accepted-digit Q2/Q1 tower",
    "refusal_scope": [
        "not the whole Q5 locus",
        "not an all-depth tower, Q3-adic/Qbar/C point, counterexample, or JC2",
    ],
}

if consistent:
    stage2_coordinates = parameterize(p2, k2, p3)
    raw_particular = parameterize(p1, k1, stage2_coordinates)
    P, Q, q3_values, blocks = raw_candidate(raw_particular)
    determinant = determinant_minus_one(P, Q)
    assert all(determinant.get(xy, 0) % 243 == 0 for xy in slots)
    assert all(determinant.get(xy, 0) % 729 == 0 for xy in high_slots)
    assert determinant.get((0, 0), 0) == 0
    assert max(i + j for i, j in P) <= 7
    assert max(i + j for i, j in Q) <= 7
    result.update({
        "full_integer_replay_passed": True,
        "raw_particular": raw_particular,
        "q3_values": q3_values,
        "new_blocks": blocks,
        "literal_all_degrees_divisible_by_243": True,
        "literal_high_degrees_divisible_by_729": True,
        "degree_zero_exactly_zero": True,
        "final_kernel_dimension": len(k3),
        "solution_count": 3 ** len(k3),
    })

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
for index, stage in enumerate(stages, 1):
    print("stage", index, "divisor", stage["divisor"],
          "input", stage["input_dimension"], "rank", stage["rank"],
          "augmented", stage["augmented_rank"],
          "kernel", stage["kernel_dimension"],
          "consistent", stage["consistent"],
          "design", stage["design_count"])
print("consistent", consistent)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])

