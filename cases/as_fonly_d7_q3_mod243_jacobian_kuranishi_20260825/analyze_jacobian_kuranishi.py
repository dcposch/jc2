#!/usr/bin/env python3
"""Exact Jacobian/SNF and quadratic Kuranishi data for a frozen D7 point."""

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
source_payload = SOURCE.read_bytes()
assert hashlib.sha256(source_payload).hexdigest() == EXPECTED_SOURCE
marker = b"\nbase = []\n"
assert source_payload.count(marker) == 1
namespace = {"__file__": str(SOURCE), "__name__": "__jacobian_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source_payload.split(marker, 1)[0] + b"\n",
                 str(SOURCE), "exec"), namespace)

nadd = namespace["nadd"]
nscale = namespace["nscale"]
candidate = namespace["candidate"]
support = list(namespace["support"])
slots = list(namespace["slots"])
assert len(support) == 36 and len(slots) == 91

frozen = json.loads(Path(os.environ["FROZEN_RESULT_JSON"]).read_text())
combined = list(frozen["combined_z9_particular"])
assert len(combined) == 72
P, Q = candidate(combined)


def coefficient(poly, xy):
    return poly.get(xy, 0)


def derivative(poly, axis):
    result = {}
    for (i, j), value in poly.items():
        exponent = (i, j)[axis]
        if exponent:
            xy = (i - (axis == 0), j - (axis == 1))
            result[xy] = result.get(xy, 0) + exponent * value
    return {xy: value for xy, value in result.items() if value}


def multiply(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            result[xy] = result.get(xy, 0) + a * b
    return {xy: value for xy, value in result.items() if value}


def bracket(left, right):
    return nadd(multiply(derivative(left, 0), derivative(right, 1)),
                nscale(-1, multiply(derivative(left, 1),
                                    derivative(right, 0))))


def determinant_residual(left, right):
    answer = bracket(left, right)
    answer[(0, 0)] = answer.get((0, 0), 0) - 1
    return {xy: value for xy, value in answer.items() if value}


def monomial(xy):
    return {xy: 1}


def matrix_columns_at(left, right):
    columns = ([bracket(monomial(xy), right) for xy in support]
               + [bracket(left, monomial(xy)) for xy in support])
    return [[coefficient(columns[column], xy)
             for column in range(72)] for xy in slots]


def rref(matrix, modulus=3):
    work = [[value % modulus for value in row] for row in matrix]
    row_ids = list(range(len(work)))
    pivots = []
    pivot_rows_original = []
    row = 0
    for column in range(len(work[0])):
        chosen = next((r for r in range(row, len(work))
                       if work[r][column] % modulus), None)
        if chosen is None:
            continue
        work[row], work[chosen] = work[chosen], work[row]
        row_ids[row], row_ids[chosen] = row_ids[chosen], row_ids[row]
        inverse = pow(work[row][column], -1, modulus)
        work[row] = [(inverse * value) % modulus for value in work[row]]
        for r in range(len(work)):
            if r == row or not work[r][column]:
                continue
            scalar = work[r][column]
            work[r] = [(a - scalar * b) % modulus
                       for a, b in zip(work[r], work[row])]
        pivots.append(column)
        pivot_rows_original.append(row_ids[row])
        row += 1
        if row == len(work):
            break
    return work, pivots, pivot_rows_original


def nullspace(matrix, modulus=3):
    work, pivots, _ = rref(matrix, modulus)
    free = [column for column in range(len(matrix[0]))
            if column not in pivots]
    basis = []
    for free_column in free:
        vector = [0] * len(matrix[0])
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-work[row][free_column]) % modulus
        basis.append(vector)
    return basis, pivots


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def matvec(matrix, vector, modulus=3):
    return [sum(a * b for a, b in zip(row, vector)) % modulus
            for row in matrix]


def vector_poly(vector):
    left = {xy: vector[index] for index, xy in enumerate(support)
            if vector[index] % 3}
    right = {xy: vector[36 + index] for index, xy in enumerate(support)
             if vector[36 + index] % 3}
    return left, right


def bareiss_determinant(matrix):
    work = [list(map(int, row)) for row in matrix]
    n = len(work)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        chosen = next((r for r in range(k, n) if work[r][k]), None)
        if chosen is None:
            return 0
        if chosen != k:
            work[k], work[chosen] = work[chosen], work[k]
            sign = -sign
        pivot = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = work[i][j] * pivot - work[i][k] * work[k][j]
                assert numerator % previous == 0
                work[i][j] = numerator // previous
        previous = pivot
        for i in range(k + 1, n):
            work[i][k] = 0
    return sign * work[-1][-1]


def valuation3(value):
    if value == 0:
        return None
    value = abs(value)
    answer = 0
    while value % 3 == 0:
        answer += 1
        value //= 3
    return answer


def encode_matrix(matrix):
    return json.dumps(matrix, separators=(",", ":"), sort_keys=False).encode()


integer_matrix = matrix_columns_at(P, Q)
seedP = {(1, 0): 1, (3, 0): -1}
seedQ = {(0, 1): 1}
assert all((coefficient(P, xy) - coefficient(seedP, xy)) % 3 == 0
           for xy in set(P) | set(seedP))
assert all((coefficient(Q, xy) - coefficient(seedQ, xy)) % 3 == 0
           for xy in set(Q) | set(seedQ))
seed_matrix = matrix_columns_at(seedP, seedQ)
assert [[value % 3 for value in row] for row in integer_matrix] == [
    [value % 3 for value in row] for row in seed_matrix]

_, pivot_columns, pivot_rows = rref(seed_matrix)
assert len(pivot_columns) == len(pivot_rows) == 27
pivot_minor = [[integer_matrix[row][column] for column in pivot_columns]
               for row in pivot_rows]
pivot_det = bareiss_determinant(pivot_minor)
assert pivot_det % 3
assert all(sum(slots[row]) <= 6 for row in pivot_rows)

tangent_kernel, _ = nullspace(seed_matrix)
left_cokernel, _ = nullspace(transpose(seed_matrix))
assert len(tangent_kernel) == 45
assert len(left_cokernel) == 64


def obstruction_class(vector):
    return matvec(left_cokernel, vector)


quadratic_columns = []
quadratic_labels = []
q_basis = []
for index, tangent in enumerate(tangent_kernel):
    left, right = vector_poly(tangent)
    values = [coefficient(bracket(left, right), xy) % 3 for xy in slots]
    q_basis.append(values)
    quadratic_columns.append(obstruction_class(values))
    quadratic_labels.append([index, index])
for left_index in range(len(tangent_kernel)):
    left_u, left_v = vector_poly(tangent_kernel[left_index])
    for right_index in range(left_index + 1, len(tangent_kernel)):
        right_u, right_v = vector_poly(tangent_kernel[right_index])
        polar_poly = nadd(bracket(left_u, right_v),
                          bracket(right_u, left_v))
        values = [coefficient(polar_poly, xy) % 3 for xy in slots]
        quadratic_columns.append(obstruction_class(values))
        quadratic_labels.append([left_index, right_index])
quadratic_matrix = transpose(quadratic_columns)
_, quadratic_pivots, _ = rref(quadratic_matrix)

# In this source ordering the cokernel has a simpler canonical realization:
# the Cartier slot (2,2) and every total degree 7..12 slot.  The divergence
# image is zero there and is all of the other 27 rows.
canonical_cokernel_slots = [(2, 2)] + [xy for xy in slots if sum(xy) >= 7]
assert len(canonical_cokernel_slots) == 64
canonical_indices = [slots.index(xy) for xy in canonical_cokernel_slots]
assert all(not any(seed_matrix[index]) for index in canonical_indices)
canonical_quadratic_matrix = [
    [column[index] for column in quadratic_columns]
    for index in canonical_indices]
_, canonical_quadratic_pivots, _ = rref(canonical_quadratic_matrix)
assert len(canonical_quadratic_pivots) == len(quadratic_pivots)
degree_ranks = {}
for degree in [4] + list(range(7, 13)):
    row_indices = [index for index, xy in enumerate(canonical_cokernel_slots)
                   if sum(xy) == degree]
    block = [canonical_quadratic_matrix[index] for index in row_indices]
    _, block_pivots, _ = rref(block)
    degree_ranks[str(degree)] = len(block_pivots)

residual = determinant_residual(P, Q)
assert all(coefficient(residual, xy) % 243 == 0 for xy in slots)
residual_digit = [(coefficient(residual, xy) // 243) % 3 for xy in slots]
affine_class = obstruction_class(residual_digit)
canonical_affine_class = [residual_digit[index] for index in canonical_indices]

# Formal source-supported obstruction through the special-fibre seed.  This is
# checked in F3[t,x,y], with keys (x exponent, y exponent, t exponent).
def tri_add(*polys):
    answer = {}
    for poly in polys:
        for key, value in poly.items():
            answer[key] = (answer.get(key, 0) + value) % 3
    return {key: value for key, value in answer.items() if value}


def tri_derivative(poly, axis):
    answer = {}
    for key, value in poly.items():
        exponent = key[axis]
        if exponent:
            target = list(key)
            target[axis] -= 1
            target = tuple(target)
            answer[target] = (answer.get(target, 0) + exponent * value) % 3
    return {key: value for key, value in answer.items() if value}


def tri_multiply(left, right):
    answer = {}
    for a, avalue in left.items():
        for b, bvalue in right.items():
            key = tuple(x + y for x, y in zip(a, b))
            answer[key] = (answer.get(key, 0) + avalue * bvalue) % 3
    return {key: value for key, value in answer.items() if value}


formalP = {(1, 0, 0): 1, (3, 0, 0): 2, (7, 0, 1): 1}
formalQ = {(0, 1, 0): 1, (6, 1, 1): 2}
formal_det = tri_add(
    tri_multiply(tri_derivative(formalP, 0),
                 tri_derivative(formalQ, 1)),
    {key: -value for key, value in tri_multiply(
        tri_derivative(formalP, 1), tri_derivative(formalQ, 0)).items()},
    {(0, 0, 0): 2})
assert formal_det == {(12, 0, 2): 2}
assert all(not any(key[0:2] == slots[row] for key in formal_det)
           for row in pivot_rows)
assert not any(seed_matrix[slots.index((12, 0))])

# The explicit tangent is also reconstructed in the computed 45-dimensional
# kernel and has the asserted nonzero quadratic cokernel class.
explicit_tangent = [0] * 72
explicit_tangent[support.index((7, 0))] = 1
explicit_tangent[36 + support.index((6, 1))] = 2
assert not any(matvec(seed_matrix, explicit_tangent))
explicit_u, explicit_v = vector_poly(explicit_tangent)
explicit_q = [coefficient(bracket(explicit_u, explicit_v), xy) % 3
              for xy in slots]
explicit_class = obstruction_class(explicit_q)
assert explicit_q[slots.index((12, 0))] == 2
assert any(explicit_class)

# Two exact positive-dimensional strata of the Kuranishi zero locus.  They
# are not asserted exhaustive: either U=0 with V_y=0, or V=0 with U_x=0.
u_zero_v_dy_zero = []
v_zero_u_dx_zero = []
for index, (i, j) in enumerate(support):
    if j % 3 == 0:
        vector = [0] * 72
        vector[36 + index] = 1
        u_zero_v_dy_zero.append(vector)
    if i % 3 == 0:
        vector = [0] * 72
        vector[index] = 1
        v_zero_u_dx_zero.append(vector)
assert len(u_zero_v_dy_zero) == len(v_zero_u_dx_zero) == 15
for family in (u_zero_v_dy_zero, v_zero_u_dx_zero):
    assert all(not any(matvec(seed_matrix, vector)) for vector in family)
    for left_index, left_vector in enumerate(family):
        left_u, left_v = vector_poly(left_vector)
        assert not bracket(left_u, left_v)
        for right_vector in family[left_index + 1:]:
            right_u, right_v = vector_poly(right_vector)
            assert not nadd(bracket(left_u, right_v),
                            bracket(right_u, left_v))

# Smith computation is deliberately on AWS.  The import is explicit so a
# missing pinned dependency fails closed rather than silently weakening output.
skip_snf = os.environ.get("SKIP_SNF") == "1"
if skip_snf:
    smith_diagonal = []
else:
    from sympy import Matrix, ZZ  # noqa: E402
    from sympy.matrices.normalforms import smith_normal_form  # noqa: E402

    smith = smith_normal_form(Matrix(integer_matrix), domain=ZZ)
    smith_diagonal = [int(smith[i, i])
                      for i in range(min(smith.rows, smith.cols))
                      if smith[i, i] != 0]

matrix_bytes = encode_matrix(integer_matrix)
Path(os.environ["MATRIX_JSON"]).write_bytes(matrix_bytes + b"\n")
result = {
    "status": "PASS-AS-D7-JACOBIAN-KURANISHI",
    "source_sha256": EXPECTED_SOURCE,
    "frozen_result_sha256": hashlib.sha256(
        Path(os.environ["FROZEN_RESULT_JSON"]).read_bytes()).hexdigest(),
    "integer_jacobian_shape": [91, 72],
    "integer_jacobian_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
    "integer_smith_computed": not skip_snf,
    "integer_smith_rank": (len(smith_diagonal) if not skip_snf else None),
    "integer_smith_diagonal": smith_diagonal,
    "integer_smith_v3": [valuation3(value) for value in smith_diagonal],
    "mod3_rank": 27,
    "tangent_kernel_dimension": 45,
    "cokernel_dimension": 64,
    "pivot_rows": [list(slots[row]) for row in pivot_rows],
    "pivot_columns": pivot_columns,
    "pivot_minor_determinant": pivot_det,
    "pivot_minor_v3": valuation3(pivot_det),
    "residual_minimum_v3": min(valuation3(value) for value in residual.values()
                           if value),
    "next_digit_affine_obstruction_nonzero": any(affine_class),
    "next_digit_affine_obstruction": affine_class,
    "next_digit_affine_obstruction_sha256": hashlib.sha256(
        bytes(affine_class)).hexdigest(),
    "kuranishi_domain_dimension": 45,
    "kuranishi_target_dimension": 64,
    "kuranishi_quadratic_column_count": len(quadratic_columns),
    "kuranishi_coefficient_span_rank": len(quadratic_pivots),
    "canonical_cokernel_slots": [list(xy) for xy in canonical_cokernel_slots],
    "canonical_affine_obstruction": canonical_affine_class,
    "canonical_affine_obstruction_support": [
        {"slot": list(xy), "value": value}
        for xy, value in zip(canonical_cokernel_slots, canonical_affine_class)
        if value],
    "canonical_kuranishi_coefficient_span_rank": len(
        canonical_quadratic_pivots),
    "canonical_kuranishi_degree_block_ranks": degree_ranks,
    "kuranishi_zero_locus_certified_linear_strata": [
        {"dimension": 15, "equations": "U=0 and V_y=0"},
        {"dimension": 15, "equations": "V=0 and U_x=0"},
    ],
    "kuranishi_zero_locus_strata_exhaustive": False,
    "kuranishi_matrix_sha256": hashlib.sha256(
        bytes(value for row in quadratic_matrix for value in row)).hexdigest(),
    "kuranishi_labels_sha256": hashlib.sha256(
        json.dumps(quadratic_labels, separators=(",", ":")).encode()).hexdigest(),
    "explicit_obstructed_tangent": {
        "U": "x^7",
        "V": "2*x^6*y",
        "determinant_residual_over_F3t": "2*t^2*x^12",
        "cokernel_class": explicit_class,
        "cokernel_class_sha256": hashlib.sha256(bytes(explicit_class)).hexdigest(),
        "no_second_order_linear_correction_at_x12": True,
    },
    "relative_smoothness_rank27_shortcut": "REFUTED",
    "relative_smoothness_reason": (
        "a source-supported tangent direction has nonzero second-order "
        "x^12 cokernel obstruction; the other 64 rows are not locally "
        "generated by the rank-27 linear subsystem"),
    "scope": "one frozen literal D7 mod243 representative",
    "refusal_scope": [
        "affine obstruction concerns only this particular representative",
        "no classification of the full mod243 solution fibre",
        "no all-depth, collision, counterexample, or JC2 conclusion",
    ],
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("smith_rank", result["integer_smith_rank"])
print("smith_v3", result["integer_smith_v3"])
print("pivot_v3", result["pivot_minor_v3"])
print("kuranishi_span_rank", len(quadratic_pivots))
print("affine_obstruction", any(affine_class))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
