#!/usr/bin/env python3
"""Exact 3^4 active-coordinate Q7 compatibility cube."""
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

# Importing the parent also runs its fully checked base state once.  Keep the
# bootstrap artifact separate and silence only presentation stdout.
os.environ["STATE_FAMILY"] = "q8_kernel"
os.environ["SAMPLE_INDEX"] = "0"
os.environ["OUTPUT_JSON"] = os.environ["BOOTSTRAP_JSON"]
spec = importlib.util.spec_from_file_location("frozen_state_parent", PARENT)
parent = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(parent)


def rref_left_cokernel(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
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
        for r in range(rows):
            if r != rank and work[r][col]:
                scalar = work[r][col]
                work[r] = [(x - scalar * y) % 3
                           for x, y in zip(work[r], work[rank])]
                transform[r] = [(x - scalar * y) % 3
                                for x, y in zip(transform[r], transform[rank])]
        rank += 1
    left = tuple(tuple(line) for line in transform[rank:])
    assert all(all(sum(vector[r] * matrix[r][col] for r in range(rows)) % 3 == 0
                   for col in range(cols)) for vector in left)
    return rank, left


def ternary(index, width=4):
    result = []
    for _ in range(width):
        result.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(result)


def index_of(values):
    return sum(value * 3 ** i for i, value in enumerate(values))


def build_state(parameters):
    t6, t8, s15, s17 = parameters
    t = [0] * 19
    t[17] = 1
    t[6], t[8] = t6, t8
    xvalues = parent.add_vector(parent.q9_origin, parent.q9_kernel, t,
                                reduce=True)
    A22, b22 = parent.matrix_and_rhs(parent.transition_rows, xvalues,
                                     parent.q8_variable_count)
    rank22, augmented22, _p, _w, y0 = parent.rref_solve(A22, b22)
    assert (rank22, augmented22) == (13, 13) and y0 is not None
    full_rank, full_kernel = parent.kernel_basis(A22)
    assert full_rank == 13 and len(full_kernel) == 19
    assert full_kernel == parent.q8_kernel_at_origin
    s = [0] * 19
    s[15], s[17] = s15, s17
    yvalues = parent.add_vector(y0, full_kernel, s, reduce=True)
    assert parent.source_rows(parent.source_data, xvalues) == [0] * 23
    assert parent.transition_rows(xvalues, yvalues) == [0] * 22
    parent.xvalues, parent.yvalues = xvalues, yvalues
    A7, b7 = parent.affine_matrix(parent.q7_rows, 18)
    return xvalues, yvalues, A7, b7


x0, y0, A0, b0 = build_state((0, 0, 0, 0))
rank0, left = rref_left_cokernel(A0)
assert rank0 == 9 and len(left) == 10
matrix_sha = hashlib.sha256(bytes(value for line in A0 for value in line)).hexdigest()

records = {}
for index in range(3 ** 4):
    parameters = ternary(index)
    xvalues, yvalues, matrix, rhs = build_state(parameters)
    assert matrix == A0
    kappa = tuple(sum(vector[r] * rhs[r] for r in range(19)) % 3
                  for vector in left)
    rank, augmented, _p, _w, witness = parent.rref_solve(matrix, rhs)
    assert rank == 9
    assert (witness is not None) == (not any(kappa))
    records[index] = {"parameters": list(parameters), "kappa": list(kappa),
                      "compatible": witness is not None,
                      "xvalues": list(xvalues), "yvalues": list(yvalues)}

width = 10
constant = tuple(records[0]["kappa"])
linear = [[0] * 4 for _ in range(width)]
square = [[0] * 4 for _ in range(width)]
pairs = list(itertools.combinations(range(4), 2))
cross = [[0] * len(pairs) for _ in range(width)]
for variable in range(4):
    point = [0] * 4
    point[variable] = 1
    one = records[index_of(point)]["kappa"]
    point[variable] = 2
    two = records[index_of(point)]["kappa"]
    for coordinate in range(width):
        linear[coordinate][variable] = (two[coordinate] - one[coordinate]) % 3
        square[coordinate][variable] = (one[coordinate] - constant[coordinate]
                                        - linear[coordinate][variable]) % 3
for pair_index, (left_index, right_index) in enumerate(pairs):
    point = [0] * 4
    point[left_index] = point[right_index] = 1
    both = records[index_of(point)]["kappa"]
    for coordinate in range(width):
        cross[coordinate][pair_index] = (both[coordinate] - constant[coordinate]
            - linear[coordinate][left_index] - square[coordinate][left_index]
            - linear[coordinate][right_index] - square[coordinate][right_index]) % 3


def predicted(parameters):
    answer = []
    for coordinate in range(width):
        value = constant[coordinate]
        value += sum(linear[coordinate][i] * parameters[i]
                     + square[coordinate][i] * parameters[i] ** 2
                     for i in range(4))
        value += sum(cross[coordinate][k] * parameters[i] * parameters[j]
                     for k, (i, j) in enumerate(pairs))
        answer.append(value % 3)
    return tuple(answer)


assert all(predicted(ternary(index)) == tuple(records[index]["kappa"])
           for index in range(3 ** 4))
names = ("t6", "t8", "s15", "s17")
terms = []
for coordinate in range(width):
    nonzero = []
    if constant[coordinate]:
        nonzero.append(["constant", constant[coordinate]])
    nonzero += [[names[i], value] for i, value in enumerate(linear[coordinate]) if value]
    nonzero += [[f"{names[i]}^2", value] for i, value in enumerate(square[coordinate]) if value]
    nonzero += [[f"{names[i]}*{names[j]}", cross[coordinate][k]]
                for k, (i, j) in enumerate(pairs) if cross[coordinate][k]]
    if nonzero:
        terms.append({"cokernel_coordinate": coordinate, "terms": nonzero})
compatible_indices = [index for index, record in records.items()
                      if record["compatible"]]
presentation = {
    "coordinate_names": names,
    "q7_matrix_sha256": matrix_sha,
    "q7_rank": rank0,
    "q7_cokernel_dimension": len(left),
    "quadratic_exact_on_cube": True,
    "nonzero_kappa_coordinates": terms,
    "compatible_count": len(compatible_indices),
    "compatible_parameters": [records[index]["parameters"]
                              for index in compatible_indices],
    "records": [records[index] for index in range(3 ** 4)],
}
encoded = (json.dumps(presentation, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("cube_size", 3 ** 4)
print("q7_rank_cokernel", rank0, len(left))
print("q7_matrix_sha256", matrix_sha)
print("nonzero_kappa_coordinates", json.dumps(terms, sort_keys=True))
print("compatible_count", len(compatible_indices))
print("compatible_parameters", [records[index]["parameters"]
                                for index in compatible_indices])
print("presentation_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-ACTIVE4-Q7-COMPATIBILITY-CUBE")
