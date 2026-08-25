#!/usr/bin/env python3
"""Exact Q8 Kuranishi system on the first predecessor's Q9 affine fibre."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import json
import os
import sys
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
V1 = (ROOT / "cases/as_fonly_d7_q9_kuranishi_q8_20260825"
      / "compile_witness.py")
EXPECTED_V1_SHA = "fbf327fb04beb2fa929f3b46a5df035244ec838793bc1f596801935adae09d4b"
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_V1_SHA
source = payload.decode()
marker = "\nA22, b22 = matrix_and_rhs(transition_rows, q9_vector, len(y_names))\n"
assert source.count(marker) == 1
scope = {"__file__": str(V1), "__name__": "__q8_v1_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(V1), "exec"), scope)

source_rows = scope["source_rows"]
source_data = scope["source_data"]
q9_vector = tuple(scope["q9_vector"])
transition_rows = scope["transition_rows"]
matrix_and_rhs = scope["matrix_and_rhs"]
y_names = tuple(scope["y_names"])
new_names = tuple(scope["new_names"])


def affine_matrix(function, variable_count):
    zero = (0,) * variable_count
    b = function(zero)
    columns = []
    for index in range(variable_count):
        basis = [0] * variable_count
        basis[index] = 1
        value = function(tuple(basis))
        columns.append([(a - c) % 3 for a, c in zip(value, b)])
    A = [[columns[col][row] for col in range(variable_count)]
         for row in range(len(b))]
    ones = (1,) * variable_count
    assert function(ones) == [
        (b[row] + sum(A[row])) % 3 for row in range(len(b))]
    return A, [value % 3 for value in b]


def rref_solve(A, b):
    rows = len(A)
    cols = len(A[0]) if rows else 0
    work = [[value % 3 for value in line] + [(-constant) % 3]
            for line, constant in zip(A, b)]
    rank = 0
    pivots = []
    for col in range(cols):
        pivot = next((row for row in range(rank, rows)
                      if work[row][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
        for row in range(rows):
            if row != rank and work[row][col]:
                scalar = work[row][col]
                work[row] = [(x - scalar * y) % 3
                             for x, y in zip(work[row], work[rank])]
        pivots.append(col)
        rank += 1
    bad = any(all(value == 0 for value in line[:-1]) and line[-1]
              for line in work)
    witness = None
    if not bad:
        answer = [0] * cols
        for row, pivot in enumerate(pivots):
            answer[pivot] = work[row][-1]
        witness = tuple(answer)
        assert all((sum(A[row][col] * witness[col]
                        for col in range(cols)) + b[row]) % 3 == 0
                   for row in range(rows))
    return rank, rank + int(bad), tuple(pivots), work, witness


def kernel_basis(A):
    zero = [0] * len(A)
    rank, augmented, pivots, work, witness = rref_solve(A, zero)
    assert rank == augmented and witness is not None
    free = [col for col in range(len(A[0])) if col not in pivots]
    basis = []
    for free_col in free:
        vector = [0] * len(A[0])
        vector[free_col] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-work[row][free_col]) % 3
        assert all(sum(A[row][col] * vector[col]
                       for col in range(len(vector))) % 3 == 0
                   for row in range(len(A)))
        basis.append(tuple(vector))
    return rank, tuple(basis)


def add_vector(base, basis, parameters, reduce=False):
    result = [base[col] + sum(parameters[j] * basis[j][col]
                              for j in range(len(parameters)))
              for col in range(len(base))]
    if reduce:
        result = [value % 3 for value in result]
    return tuple(result)


q9_A, q9_b = affine_matrix(lambda values: source_rows(source_data, values),
                           len(new_names))
q9_rank, q9_kernel = kernel_basis(q9_A)
assert q9_rank == 13 and len(q9_kernel) == 19
assert source_rows(source_data, q9_vector) == [0] * 23
assert all(sum(q9_A[row][col] * q9_vector[col]
                   for col in range(len(q9_vector))) % 3
               == (-q9_b[row]) % 3 for row in range(len(q9_A)))

A0, b0 = matrix_and_rhs(transition_rows, q9_vector, len(y_names))
A13 = A0[:13]
top_rank, top_kernel = kernel_basis(A13)
assert top_rank == 13 and len(top_kernel) == 19


def fibre_data(parameters, canonical=False):
    xvalues = add_vector(q9_vector, q9_kernel, parameters, reduce=canonical)
    assert source_rows(source_data, xvalues) == [0] * 23
    A22, b22 = matrix_and_rhs(transition_rows, xvalues, len(y_names))
    assert A22[:13] == A13
    rank, augmented, _, _, section = rref_solve(A13, b22[:13])
    assert (rank, augmented) == (13, 13) and section is not None
    B = [[sum(A22[13 + row][col] * top_kernel[j][col]
              for col in range(len(y_names))) % 3
          for j in range(len(top_kernel))] for row in range(9)]
    kappa = [(b22[13 + row]
              + sum(A22[13 + row][col] * section[col]
                    for col in range(len(y_names)))) % 3
             for row in range(9)]
    return xvalues, A22, b22, section, B, kappa


def madd(left, right, scalar=1):
    return [[(left[i][j] + scalar * right[i][j]) % 3
             for j in range(len(left[0]))] for i in range(len(left))]


def mscale(scalar, matrix):
    return [[scalar * value % 3 for value in line] for line in matrix]


def vadd(*vectors):
    return [sum(vector[i] for vector in vectors) % 3
            for i in range(len(vectors[0]))]


parameter_count = len(q9_kernel)
zero_t = (0,) * parameter_count
_, _, _, section0, B_const, kappa_const = fibre_data(zero_t)
B_linear = []
kappa_linear = []
kappa_square = []
single_data = []
for i in range(parameter_count):
    one = [0] * parameter_count
    two = [0] * parameter_count
    one[i] = 1
    two[i] = 2
    data1 = fibre_data(tuple(one))
    data2 = fibre_data(tuple(two))
    B1, B2 = data1[4], data2[4]
    linear_matrix = madd(B1, B_const, scalar=-1)
    assert B2 == madd(B_const, mscale(2, linear_matrix))
    B_linear.append(linear_matrix)
    k1, k2 = data1[5], data2[5]
    linear = [(k2[row] - k1[row]) % 3 for row in range(9)]
    square = [(k1[row] - kappa_const[row] - linear[row]) % 3
              for row in range(9)]
    kappa_linear.append(linear)
    kappa_square.append(square)
    single_data.append(data1)

kappa_cross = []
for i in range(parameter_count):
    for j in range(i + 1, parameter_count):
        point = [0] * parameter_count
        point[i] = point[j] = 1
        data = fibre_data(tuple(point))
        expected_B = madd(madd(B_const, B_linear[i]), B_linear[j])
        assert data[4] == expected_B
        cross = [(data[5][row] - kappa_const[row]
                  - kappa_linear[i][row] - kappa_square[i][row]
                  - kappa_linear[j][row] - kappa_square[j][row]) % 3
                 for row in range(9)]
        kappa_cross.append((i, j, cross))


def evaluate_presentation(parameters):
    B = [line[:] for line in B_const]
    for i, value in enumerate(parameters):
        if value:
            B = madd(B, mscale(value, B_linear[i]))
    kappa = list(kappa_const)
    for i, value in enumerate(parameters):
        if value:
            kappa = vadd(kappa,
                         [(value * entry) % 3 for entry in kappa_linear[i]],
                         [((value * value) * entry) % 3
                          for entry in kappa_square[i]])
    for i, j, coefficient in kappa_cross:
        scalar = parameters[i] * parameters[j] % 3
        if scalar:
            kappa = vadd(kappa,
                         [(scalar * entry) % 3 for entry in coefficient])
    return B, kappa


# Deterministic off-grid interpolation controls.
control_digest = hashlib.sha256()
state = 20260825
for _ in range(64):
    point = []
    for _j in range(parameter_count):
        state = (1103515245 * state + 12345) & 0x7fffffff
        point.append(state % 3)
    actual = fibre_data(tuple(point))
    predicted = evaluate_presentation(tuple(point))
    assert (actual[4], actual[5]) == predicted
    control_digest.update(bytes(point + actual[5]))


def low_weight_points():
    yield zero_t
    for i in range(parameter_count):
        for a in (1, 2):
            point = [0] * parameter_count
            point[i] = a
            yield tuple(point)
    for i in range(parameter_count):
        for j in range(i + 1, parameter_count):
            for a in (1, 2):
                for b in (1, 2):
                    point = [0] * parameter_count
                    point[i], point[j] = a, b
                    yield tuple(point)


def deterministic_random_points(count):
    value = 314159265
    for _ in range(count):
        point = []
        for _j in range(parameter_count):
            value = (1664525 * value + 1013904223) & 0xffffffff
            point.append(value % 3)
        yield tuple(point)


survivor = None
lift_mismatch = None
searched = 0
seen = set()
rank_histogram = {}
for point in itertools.chain(low_weight_points(),
                             deterministic_random_points(2048)):
    if point in seen:
        continue
    seen.add(point)
    searched += 1
    x_linear, _, _, section, B, kappa = fibre_data(point)
    ls_rank, ls_augmented, _, _, s_witness = rref_solve(B, kappa)
    key = f"{ls_rank},{ls_augmented}"
    rank_histogram[key] = rank_histogram.get(key, 0) + 1
    x_canonical, A_can, b_can, _, _, _ = fibre_data(point, canonical=True)
    can_rank, can_augmented, _, _, y_canonical = rref_solve(A_can, b_can)
    if (s_witness is not None) != (y_canonical is not None):
        lift_mismatch = {
            "parameters": list(point),
            "linear_lift_rank_pair": [ls_rank, ls_augmented],
            "canonical_lift_rank_pair": [can_rank, can_augmented],
        }
        break
    if s_witness is None:
        continue
    y_linear = [section[col] + sum(
        top_kernel[j][col] * s_witness[j]
        for j in range(len(top_kernel))) for col in range(len(y_names))]
    y_linear = tuple(value % 3 for value in y_linear)
    assert transition_rows(x_linear, y_linear) == [0] * 22
    assert transition_rows(x_canonical, y_canonical) == [0] * 22
    survivor = {
        "parameters": list(point),
        "x_linear": list(x_linear),
        "x_canonical": list(x_canonical),
        "s_witness": list(s_witness),
        "y_linear": list(y_linear),
        "y_canonical": list(y_canonical),
        "ls_rank_pair": [ls_rank, ls_augmented],
        "canonical_full_rank_pair": [can_rank, can_augmented],
    }
    break

presentation = {
    "field": 3,
    "q9_origin": list(q9_vector),
    "q9_rank": q9_rank,
    "q9_kernel_basis": [list(vector) for vector in q9_kernel],
    "q8_top_rank": top_rank,
    "q8_top_section_at_origin": list(section0),
    "q8_top_kernel_basis": [list(vector) for vector in top_kernel],
    "B_constant": B_const,
    "B_linear": B_linear,
    "kappa_constant": kappa_const,
    "kappa_linear": kappa_linear,
    "kappa_square": kappa_square,
    "kappa_cross": [[i, j, values] for i, j, values in kappa_cross],
    "control_digest_sha256": control_digest.hexdigest(),
    "search_points_checked": searched,
    "search_rank_histogram": rank_histogram,
    "lift_mismatch": lift_mismatch,
    "first_survivor": survivor,
}
encoded = (json.dumps(presentation, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
output = Path(os.environ["OUTPUT_JSON"])
output.write_bytes(encoded)

nonzero_B = sum(value != 0 for matrix in B_linear
                for line in matrix for value in line)
nonzero_kappa = (sum(value != 0 for value in kappa_const)
                 + sum(value != 0 for line in kappa_linear for value in line)
                 + sum(value != 0 for line in kappa_square for value in line)
                 + sum(value != 0 for _i, _j, line in kappa_cross
                       for value in line))
print("source_shapes", 23, 32, 13, 9, 32)
print("q9_rank_kernel", q9_rank, len(q9_kernel))
print("q8_top_rank_kernel", top_rank, len(top_kernel))
print("presentation_degrees", 1, 2)
print("nonzero_B_linear_coefficients", nonzero_B)
print("nonzero_kappa_coefficients", nonzero_kappa)
print("off_grid_control_sha256", control_digest.hexdigest())
print("search_points_checked", searched)
print("search_rank_histogram", sorted(rank_histogram.items()))
print("lift_mismatch", lift_mismatch)
print("first_survivor", survivor)
print("presentation_sha256", hashlib.sha256(encoded).hexdigest())
if lift_mismatch is not None:
    print("FAIL-CANONICAL-LIFT-TRANSLATION-STATE")
    sys.exit(2)
print("PASS-Q9-FIBRE-Q8-KURANISHI-PRESENTATION")
