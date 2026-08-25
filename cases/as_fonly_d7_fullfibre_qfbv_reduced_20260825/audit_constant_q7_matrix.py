#!/usr/bin/env python3
"""Audit the proposed constant rank-nine Q7 restoration matrix over F3."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = (
    "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()
family_marker = '\nfamily = os.environ["STATE_FAMILY"]\n'
restored_marker = "\ndef restored(values):\n"
result_marker = '\nresult = {"family": family, "sample_index": sample_index,\n'
assert source.count(family_marker) == source.count(restored_marker) == 1
assert source.count(result_marker) == 1
scope = {"__file__": str(PARENT), "__name__": "__q7_matrix_audit__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(family_marker, 1)[0], str(PARENT), "exec"), scope)
fragment = (restored_marker
            + source.split(restored_marker, 1)[1].split(result_marker, 1)[0])
exec(compile(fragment, str(PARENT), "exec"), scope)

source_data = scope["source_data"]
source_rows = scope["source_rows"]
transition_rows = scope["transition_rows"]
matrix_and_rhs = scope["matrix_and_rhs"]
q9_origin = tuple(scope["q9_origin"])
q9_kernel = tuple(scope["q9_kernel"])
q8_variable_count = scope["q8_variable_count"]
add_vector = scope["add_vector"]
rref_solve = scope["rref_solve"]
kernel_basis = scope["kernel_basis"]
q7_rows = scope["q7_rows"]


def ternary(index: int, width: int) -> tuple[int, ...]:
    answer = []
    for _ in range(width):
        answer.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(answer)


def affine_matrix(function, variable_count):
    zero = (0,) * variable_count
    b = function(zero)
    columns = []
    for column in range(variable_count):
        basis = [0] * variable_count
        basis[column] = 1
        value = function(tuple(basis))
        columns.append(tuple((left - right) % 3
                             for left, right in zip(value, b)))
    matrix = tuple(tuple(columns[column][row]
                         for column in range(variable_count))
                   for row in range(len(b)))
    ones = (1,) * variable_count
    assert function(ones) == [
        (b[row] + sum(matrix[row])) % 3 for row in range(len(b))]
    return matrix, tuple(value % 3 for value in b)


representatives = (ROOT / "cases/as_fonly_d7_fullfibre_qfbv_20260825"
                   / "STATE_REPRESENTATIVES.tsv")
rows = [line.split("\t") for line in representatives.read_text().splitlines()[1:]]
forced = {10: 0, 11: 0, 12: 0, 13: 0, 15: 0, 17: 1}
free_q9 = tuple(index for index in range(19) if index not in forced)
common_matrix = None
common_matrix_sha = None
state_records = []
pair_controls = ((0, 1), (0, 18), (5, 13), (7, 17), (11, 12))

for state_text, label, signature in rows:
    state_index = int(state_text)
    parameters = ternary(state_index, 13)
    t = [0] * 19
    for index, value in forced.items():
        t[index] = value
    for index, value in zip(free_q9, parameters):
        t[index] = value
    xvalues = add_vector(q9_origin, q9_kernel, t, reduce=True)
    assert source_rows(source_data, xvalues) == [0] * 23
    A8, b8 = matrix_and_rhs(transition_rows, xvalues, q8_variable_count)
    rank8, augmented8, _p8, _w8, y0 = rref_solve(A8, b8)
    assert (rank8, augmented8) == (13, 13) and y0 is not None
    kernel_rank8, kernel8 = kernel_basis(A8)
    assert kernel_rank8 == 13 and len(kernel8) == 19

    tested = []
    parameter_points = [(0,) * 19]
    for index in range(19):
        for scalar in (1, 2):
            point = [0] * 19
            point[index] = scalar
            parameter_points.append(tuple(point))
    for left, right in pair_controls:
        point = [0] * 19
        point[left] = 1
        point[right] = 2
        parameter_points.append(tuple(point))

    first_b = None
    for svalues in parameter_points:
        yvalues = add_vector(y0, kernel8, svalues, reduce=True)
        assert transition_rows(xvalues, yvalues) == [0] * 22
        scope["xvalues"] = xvalues
        scope["yvalues"] = yvalues
        matrix7, b7 = affine_matrix(q7_rows, 18)
        if common_matrix is None:
            common_matrix = matrix7
            matrix_bytes = (json.dumps(common_matrix, separators=(",", ":"))
                            + "\n").encode()
            common_matrix_sha = hashlib.sha256(matrix_bytes).hexdigest()
        assert matrix7 == common_matrix
        if first_b is None:
            first_b = b7
        tested.append(hashlib.sha256(bytes(b7)).hexdigest())
    state_records.append({
        "state_index": state_index,
        "canonical_label": label,
        "presentation_signature": signature,
        "q8_rank_pair": [rank8, augmented8],
        "tested_q8_parameter_points": len(parameter_points),
        "q7_rhs_hashes_sha256": hashlib.sha256("".join(tested).encode()).hexdigest(),
        "q7_zero_rhs_sha256": hashlib.sha256(bytes(first_b)).hexdigest(),
    })

assert common_matrix is not None and common_matrix_sha is not None
rank7, augmented7, pivot_columns, rref7, zero_witness = rref_solve(
    [list(row) for row in common_matrix], [0] * len(common_matrix))
assert rank7 == augmented7 == 9 and zero_witness is not None
kernel_rank7, kernel7 = kernel_basis([list(row) for row in common_matrix])
assert kernel_rank7 == 9 and len(kernel7) == 9
pivot_rows = []
seen = 0
for row_index in range(len(common_matrix)):
    trial = [list(row) for row in common_matrix[:row_index + 1]]
    rank, _augmented, _pivots, _rref, _witness = rref_solve(
        trial, [0] * len(trial))
    if rank > seen:
        pivot_rows.append(row_index)
        seen = rank
assert seen == 9

result = {
    "selected_state_count": len(state_records),
    "q8_points_per_state": 44,
    "q7_matrix_shape": [len(common_matrix), len(common_matrix[0])],
    "q7_matrix_rank_mod3": rank7,
    "q7_pivot_columns": list(pivot_columns),
    "q7_pivot_rows": pivot_rows,
    "q7_kernel_dimension": len(kernel7),
    "q7_matrix_sha256": common_matrix_sha,
    "q7_kernel_sha256": hashlib.sha256(
        (json.dumps(kernel7, separators=(",", ":")) + "\n").encode()).hexdigest(),
    "state_records": state_records,
    "degree_bound": (
        "source formula: restoration coefficients are affine-linear in Q8; "
        "zero plus both multiples of every basis direction proves constancy"),
    "pair_sum_controls_per_state": len(pair_controls),
    "scope": "24 selected Q9 states and their entire canonical Q8 affine fibres",
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
output = Path(os.environ["OUTPUT_JSON"])
output.write_bytes(encoded)
matrix_output = Path(os.environ["MATRIX_JSON"])
matrix_output.write_text(json.dumps({
    "matrix": common_matrix,
    "pivot_columns": list(pivot_columns),
    "pivot_rows": pivot_rows,
    "kernel": kernel7,
}, sort_keys=True, separators=(",", ":")) + "\n")
print("selected_state_count", len(state_records))
print("q8_points_per_state", 44)
print("q7_matrix_rank_mod3", rank7)
print("q7_pivot_columns", list(pivot_columns))
print("q7_pivot_rows", pivot_rows)
print("q7_kernel_dimension", len(kernel7))
print("q7_matrix_sha256", common_matrix_sha)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q7-CONSTANT-MATRIX-AUDIT")

