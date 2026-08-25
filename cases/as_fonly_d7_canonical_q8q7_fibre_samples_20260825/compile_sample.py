#!/usr/bin/env python3
"""Compile and solve one sampled canonical Q8-to-Q7 fibre."""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e"
assert hashlib.sha256(PARENT.read_bytes()).hexdigest() == EXPECTED_PARENT_SHA
final_output = Path(os.environ["OUTPUT_JSON"])
os.environ["STATE_FAMILY"] = "q8_kernel"
os.environ["SAMPLE_INDEX"] = "0"
os.environ["OUTPUT_JSON"] = os.environ["BOOTSTRAP_JSON"]
spec = importlib.util.spec_from_file_location("frozen_state_parent", PARENT)
parent = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(parent)


def rref_left_cokernel(matrix):
    rows, cols = len(matrix), len(matrix[0])
    work = [[value % 3 for value in line] for line in matrix]
    transform = [[int(i == j) for j in range(rows)] for i in range(rows)]
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        transform[rank], transform[pivot] = transform[pivot], transform[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
            transform[rank] = [(2 * value) % 3 for value in transform[rank]]
        for row_index in range(rows):
            if row_index != rank and work[row_index][col]:
                scalar = work[row_index][col]
                work[row_index] = [(a - scalar * b) % 3
                    for a, b in zip(work[row_index], work[rank])]
                transform[row_index] = [(a - scalar * b) % 3
                    for a, b in zip(transform[row_index], transform[rank])]
        rank += 1
    left = tuple(tuple(line) for line in transform[rank:])
    assert all(all(sum(vector[r] * matrix[r][col] for r in range(rows)) % 3 == 0
                   for col in range(cols)) for vector in left)
    return rank, left


free_q9 = tuple(i for i in range(19)
                if i not in {10, 11, 12, 13, 15, 17})
sample_q9 = tuple(i for i in free_q9 if i not in (6, 8))
assert len(free_q9) == 13 and len(sample_q9) == 11


def sample_parameters(sample_index):
    if sample_index == 0:
        return (0,) * 11, "zero"
    if sample_index < 23:
        direction = (sample_index - 1) // 2
        scalar = 1 + (sample_index - 1) % 2
        point = [0] * 11
        point[direction] = scalar
        return tuple(point), "axis"
    state = 202608250401 + sample_index
    point = []
    for _ in range(11):
        state = (1664525 * state + 1013904223) & 0xffffffff
        point.append(state % 3)
    return tuple(point), "off_axis"


sample_index = int(os.environ["SAMPLE_INDEX_CANONICAL"])
assert 0 <= sample_index < 64
t_sample, sample_kind = sample_parameters(sample_index)
t = [0] * 19
t[17] = 1
for index, value in zip(sample_q9, t_sample):
    t[index] = value
xvalues = parent.add_vector(parent.q9_origin, parent.q9_kernel, t,
                            reduce=True)
q9_ok = parent.source_rows(parent.source_data, xvalues) == [0] * 23

result = {
    "sample_index": sample_index,
    "sample_kind": sample_kind,
    "q9_parameter_indices": sample_q9,
    "q9_parameters": t_sample,
    "xvalues": xvalues,
    "q9_rows_zero": q9_ok,
    "status": "q9_incompatible",
}

if q9_ok:
    A22, b22 = parent.matrix_and_rhs(parent.transition_rows, xvalues,
                                     parent.q8_variable_count)
    rank22, augmented22, _p22, _w22, y0 = parent.rref_solve(A22, b22)
    result["q8_rank_pair"] = [rank22, augmented22]
    if y0 is None:
        result["status"] = "q8_incompatible"
    else:
        full_rank, kernel = parent.kernel_basis(A22)
        assert full_rank == rank22
        dimension = len(kernel)
        result["q8_fibre_dimension"] = dimension
        result["q8_particular"] = y0
        if dimension != 19:
            result["status"] = "q8_dimension_not_19"
        else:
            pairs = list(itertools.combinations(range(dimension), 2))

            def point_index(values):
                return sum(value * 3 ** i for i, value in enumerate(values))

            def q7_data(parameters):
                yvalues = parent.add_vector(y0, kernel, parameters, reduce=True)
                assert parent.transition_rows(xvalues, yvalues) == [0] * 22
                parent.xvalues, parent.yvalues = xvalues, yvalues
                return parent.affine_matrix(parent.q7_rows, 18)

            zero_s = (0,) * dimension
            A0, b0 = q7_data(zero_s)
            rank7, left = rref_left_cokernel(A0)
            matrix_sha = hashlib.sha256(
                bytes(value for line in A0 for value in line)).hexdigest()
            result["q7_rank"] = rank7
            result["q7_cokernel_dimension"] = len(left)
            result["q7_matrix_sha256"] = matrix_sha

            def evaluate(parameters):
                matrix, rhs = q7_data(parameters)
                assert matrix == A0
                return tuple(sum(vector[row] * rhs[row] for row in range(19)) % 3
                             for vector in left)

            records = {zero_s: evaluate(zero_s)}
            for variable in range(dimension):
                for scalar in (1, 2):
                    point = [0] * dimension
                    point[variable] = scalar
                    records[tuple(point)] = evaluate(tuple(point))
            for left_index, right_index in pairs:
                point = [0] * dimension
                point[left_index] = point[right_index] = 1
                records[tuple(point)] = evaluate(tuple(point))

            width = len(left)
            constant = records[zero_s]
            linear = [[0] * dimension for _ in range(width)]
            square = [[0] * dimension for _ in range(width)]
            cross = [[0] * len(pairs) for _ in range(width)]
            for variable in range(dimension):
                one = [0] * dimension
                two = [0] * dimension
                one[variable] = 1
                two[variable] = 2
                value1, value2 = records[tuple(one)], records[tuple(two)]
                for coordinate in range(width):
                    linear[coordinate][variable] = (
                        value2[coordinate] - value1[coordinate]) % 3
                    square[coordinate][variable] = (
                        value1[coordinate] - constant[coordinate]
                        - linear[coordinate][variable]) % 3
            for pair_index, (left_index, right_index) in enumerate(pairs):
                point = [0] * dimension
                point[left_index] = point[right_index] = 1
                value = records[tuple(point)]
                for coordinate in range(width):
                    cross[coordinate][pair_index] = (value[coordinate]
                        - constant[coordinate]
                        - linear[coordinate][left_index]
                        - square[coordinate][left_index]
                        - linear[coordinate][right_index]
                        - square[coordinate][right_index]) % 3

            def predict(parameters):
                answer = []
                for coordinate in range(width):
                    value = constant[coordinate]
                    value += sum(linear[coordinate][i] * parameters[i]
                        + square[coordinate][i] * parameters[i] ** 2
                        for i in range(dimension))
                    value += sum(cross[coordinate][k] * parameters[i]
                        * parameters[j] for k, (i, j) in enumerate(pairs))
                    answer.append(value % 3)
                return tuple(answer)

            control_mismatches = []
            control_stream = hashlib.sha256()
            state = 202608250402 + sample_index
            for control_index in range(64):
                point = []
                for _ in range(dimension):
                    state = (1103515245 * state + 12345) & 0x7fffffff
                    point.append(state % 3)
                actual = evaluate(tuple(point))
                predicted = predict(tuple(point))
                control_stream.update(bytes(point + list(actual)))
                if actual != predicted and not control_mismatches:
                    control_mismatches.append({
                        "control_index": control_index,
                        "parameters": point,
                        "actual": actual,
                        "predicted": predicted,
                    })
            result["quadratic_control_stream_sha256"] = control_stream.hexdigest()
            result["quadratic_control_mismatches"] = control_mismatches
            if control_mismatches:
                result["status"] = "q7_not_quadratic_on_controls"
            else:
                support = sorted({variable
                    for coordinate in range(width)
                    for variable in range(dimension)
                    if linear[coordinate][variable] or square[coordinate][variable]}
                    | {variable for coordinate in range(width)
                       for pair_index, pair in enumerate(pairs)
                       if cross[coordinate][pair_index] for variable in pair})
                nonlinear = any(value for line in square for value in line) or any(
                    value for line in cross for value in line)
                result["quadratic_exact_on_controls"] = True
                result["support_indices"] = support
                result["support_dimension"] = len(support)
                result["nonlinear"] = nonlinear
                result["constant"] = constant
                result["linear"] = linear
                result["square"] = square
                result["pairs"] = pairs
                result["cross"] = cross
                solved = False
                zero_count = None
                witness = None
                if not nonlinear:
                    rank_k, augmented_k, _p, _w, witness = parent.rref_solve(
                        linear, constant)
                    solved = True
                    zero_count = 0 if witness is None else 3 ** (dimension - rank_k)
                    result["linear_rank_pair"] = [rank_k, augmented_k]
                elif len(support) <= 12:
                    support_zero_count = 0
                    for index in range(3 ** len(support)):
                        values = [0] * dimension
                        work = index
                        for variable in support:
                            values[variable] = work % 3
                            work //= 3
                        if not any(predict(values)):
                            support_zero_count += 1
                            if witness is None:
                                witness = tuple(values)
                    solved = True
                    zero_count = support_zero_count * 3 ** (dimension - len(support))
                    result["support_zero_count"] = support_zero_count
                result["zero_locus_solved"] = solved
                result["zero_count"] = zero_count
                result["first_witness"] = witness
                result["status"] = "q7_zero_locus_solved" if solved else (
                    "q7_quadratic_large_support")

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
final_output.write_bytes(encoded)
print("sample_kind_index", sample_kind, sample_index)
print("q9_rows_zero", q9_ok)
print("status", result["status"])
print("q8_rank_pair", result.get("q8_rank_pair"))
print("q8_fibre_dimension", result.get("q8_fibre_dimension"))
print("q7_rank_cokernel", result.get("q7_rank"),
      result.get("q7_cokernel_dimension"))
print("support_dimension", result.get("support_dimension"))
print("nonlinear", result.get("nonlinear"))
print("zero_count", result.get("zero_count"))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-CANONICAL-Q8Q7-FIBRE-SAMPLE")

