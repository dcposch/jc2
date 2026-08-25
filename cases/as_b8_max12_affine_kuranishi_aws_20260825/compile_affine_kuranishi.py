#!/usr/bin/env python3
"""Complete B8 fixed-D12 W2->W3 affine Kuranishi compiler (AWS only)."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = ROOT / "cases/as_b8_max12_w3_gate_aws_20260825/replay_v2.py"
EXPECTED_PARENT = (
    "691c89fc78dbbdb053449e0c26df326a5b459ab8de28b333cbd5329f48168a13")
parent_bytes = PARENT.read_bytes()
assert hashlib.sha256(parent_bytes).hexdigest() == EXPECTED_PARENT
namespace = {"__file__": str(PARENT), "__name__": "__b8_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(parent_bytes, str(PARENT), "exec"), namespace)

add = namespace["add"]
sc = namespace["sc"]
jac = namespace["jac"]
modp = namespace["modp"]
P0, Q0, ONE = namespace["P0"], namespace["Q0"], namespace["ONE"]
mons_r, mons_s, rows = (list(namespace["mons_r"]),
                        list(namespace["mons_s"]), list(namespace["rows"]))
parent_columns = list(namespace["columns"])
parent_sol2 = list(namespace["sol2"])
parent_R3, parent_S3 = namespace["R3"], namespace["S3"]


def coefficient(poly, monomial):
    return poly.get(monomial, 0)


def correction(vector):
    split = len(mons_r)
    left = {monomial: value for monomial, value
            in zip(mons_r, vector[:split]) if value}
    right = {monomial: value for monomial, value
             in zip(mons_s, vector[split:]) if value}
    return left, right


def lin_integer(vector):
    left, right = correction(vector)
    return add(jac(P0, right), jac(left, Q0))


def jac_digit(vector):
    left, right = correction(vector)
    return jac(left, right)


def cross_digit(left_vector, right_vector):
    lp, lq = correction(left_vector)
    rp, rq = correction(right_vector)
    return add(jac(lp, rq), jac(rp, lq))


def vector_of(poly, modulus=None):
    values = [coefficient(poly, monomial) for monomial in rows]
    return values if modulus is None else [value % modulus for value in values]


def combine(base, directions, scalars):
    answer = list(base)
    for scalar, direction in zip(scalars, directions):
        if scalar:
            answer = [value + scalar * delta
                      for value, delta in zip(answer, direction)]
    return answer


def rref_solve(matrix, rhs):
    if not matrix:
        return 0, [], []
    columns = len(matrix[0])
    work = [[value % 3 for value in row] + [target % 3]
            for row, target in zip(matrix, rhs)]
    pivots = []
    row = 0
    for column in range(columns):
        chosen = next((r for r in range(row, len(work))
                       if work[r][column]), None)
        if chosen is None:
            continue
        work[row], work[chosen] = work[chosen], work[row]
        if work[row][column] == 2:
            work[row] = [(2 * value) % 3 for value in work[row]]
        for r in range(len(work)):
            if r == row or not work[r][column]:
                continue
            scalar = work[r][column]
            work[r] = [(a - scalar * b) % 3
                       for a, b in zip(work[r], work[row])]
        pivots.append(column)
        row += 1
    if any(not any(line[:-1]) and line[-1] for line in work):
        return len(pivots), None, []
    particular = [0] * columns
    for r, column in enumerate(pivots):
        particular[column] = work[r][-1]
    free = [column for column in range(columns) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = (-work[r][free_column]) % 3
        kernel.append(vector)
    return len(pivots), particular, kernel


def matrix_rank(matrix):
    if not matrix:
        return 0
    rank, _, _ = rref_solve(matrix, [0] * len(matrix))
    return rank


def project(left_kernel, vector):
    return [sum(a * b for a, b in zip(functional, vector)) % 3
            for functional in left_kernel]


def residual_at(first_digit):
    left, right = correction(first_digit)
    determinant = add(jac(add(P0, sc(3, left)),
                          add(Q0, sc(3, right))), sc(-1, ONE))
    assert all(value % 9 == 0 for value in determinant.values())
    return [coefficient(determinant, monomial) // 9 % 3
            for monomial in rows]


def add_vectors(*vectors):
    return [sum(values) % 3 for values in zip(*vectors)]


def scale_vector(scalar, vector):
    return [(scalar * value) % 3 for value in vector]


def canonical_equation_basis(equations):
    if not equations:
        return []
    work = [[value % 3 for value in equation] for equation in equations]
    columns = len(work[0])
    row = 0
    for column in range(columns):
        chosen = next((r for r in range(row, len(work))
                       if work[r][column]), None)
        if chosen is None:
            continue
        work[row], work[chosen] = work[chosen], work[row]
        if work[row][column] == 2:
            work[row] = [(2 * value) % 3 for value in work[row]]
        for r in range(len(work)):
            if r != row and work[r][column]:
                scalar = work[r][column]
                work[r] = [(a - scalar * b) % 3
                           for a, b in zip(work[r], work[row])]
        row += 1
    return work[:row]


# Direct 276-by-172 integer linearization and complete W2 affine fibre.
slot_count = len(mons_r) + len(mons_s)
assert (len(mons_r), len(mons_s), slot_count, len(rows)) == (81, 91, 172, 276)
integer_columns = []
for column in range(slot_count):
    basis = [0] * slot_count
    basis[column] = 1
    integer_columns.append(vector_of(lin_integer(basis)))
A3 = [[integer_columns[column][row] % 3
       for column in range(slot_count)] for row in range(len(rows))]
assert A3 == [[parent_columns[column].get(monomial, 0) % 3
               for column in range(slot_count)]
              for monomial in rows]
rhs_w2 = vector_of(namespace["pw"](namespace["u"], 2), 3)
w2_rank, T0, kernel = rref_solve(A3, rhs_w2)
assert T0 is not None and T0 == parent_sol2
assert w2_rank == 104 and len(kernel) == 68
assert all(all(sum(A3[row][column] * direction[column]
                       for column in range(slot_count)) % 3 == 0
                   for row in range(len(rows))) for direction in kernel)

# Full ambient cokernel of the fresh-digit operator.
transpose = [list(column) for column in zip(*A3)]
transpose_rank, _, left_kernel = rref_solve(transpose, [0] * slot_count)
assert transpose_rank == w2_rank and len(left_kernel) == len(rows) - w2_rank

# Analytic ANF of the cokernel-valued first quadratic obstruction.  Monomial
# order is 1, t_i, t_i^2, t_i*t_j (i<j).
n = len(kernel)
constant_raw = residual_at(T0)
constant = project(left_kernel, constant_raw)
analytic_linear = []
analytic_diagonal = []
for direction in kernel:
    linearized = lin_integer(direction)
    assert all(value % 3 == 0 for value in linearized.values())
    carry = [coefficient(linearized, monomial) // 3 % 3
             for monomial in rows]
    mixed = vector_of(cross_digit(T0, direction), 3)
    analytic_linear.append(project(left_kernel, add_vectors(carry, mixed)))
    analytic_diagonal.append(project(left_kernel,
                                      vector_of(jac_digit(direction), 3)))
analytic_cross = []
for left in range(n):
    for right in range(left + 1, n):
        analytic_cross.append(project(
            left_kernel, vector_of(cross_digit(kernel[left], kernel[right]), 3)))

# Independent exact-determinant interpolation of the same ANF.
interp_constant = project(left_kernel, residual_at(T0))
interp_linear = []
interp_diagonal = []
unit_values = []
for direction in kernel:
    f1 = project(left_kernel, residual_at(combine(T0, [direction], [1])))
    f2 = project(left_kernel, residual_at(combine(T0, [direction], [2])))
    linear = add_vectors(f2, scale_vector(-1, f1))
    diagonal = add_vectors(f1, scale_vector(-1, interp_constant),
                           scale_vector(-1, linear))
    interp_linear.append(linear)
    interp_diagonal.append(diagonal)
    unit_values.append(f1)
interp_cross = []
pair_index = 0
for left in range(n):
    for right in range(left + 1, n):
        fij = project(left_kernel, residual_at(combine(
            T0, [kernel[left], kernel[right]], [1, 1])))
        interp_cross.append(add_vectors(
            fij, scale_vector(-1, unit_values[left]),
            scale_vector(-1, unit_values[right]), interp_constant))
        pair_index += 1
assert pair_index == n * (n - 1) // 2
assert constant == interp_constant
assert analytic_linear == interp_linear
assert analytic_diagonal == interp_diagonal
assert analytic_cross == interp_cross

# Turn the 172 cokernel coordinates into a canonical polynomial basis.
equations = []
for equation in range(len(left_kernel)):
    equations.append(
        [constant[equation]]
        + [analytic_linear[column][equation] for column in range(n)]
        + [analytic_diagonal[column][equation] for column in range(n)]
        + [values[equation] for values in analytic_cross])
equation_basis = canonical_equation_basis(equations)
equation_rank = len(equation_basis)
quadratic_start = 1 + n
quadratic_rank = matrix_rank([row[quadratic_start:] for row in equation_basis])
linear_jacobian = [row[1:1+n] for row in equation_basis]
tangent_rank = matrix_rank(linear_jacobian)

# Pure-linear consequences are combinations of the canonical equations whose
# quadratic part cancels.
quadratic_transpose = [list(column) for column in zip(
    *[row[quadratic_start:] for row in equation_basis])]
_, _, pure_linear_combinations = rref_solve(
    quadratic_transpose, [0] * len(quadratic_transpose))
pure_linear_rows = []
for combination in pure_linear_combinations:
    row = [sum(combination[e] * equation_basis[e][column]
               for e in range(equation_rank)) % 3
           for column in range(1+n)]
    if any(row):
        pure_linear_rows.append(row)
pure_linear_basis = canonical_equation_basis(pure_linear_rows)
pure_linear_rank = len(pure_linear_basis)

# Exact literal t=0 W3 fibre and replay.  This is one witness attached to the
# complete family calculation, not a substitute for solving its zero locus.
assert not any(constant)
fresh_rank, W0, fresh_kernel = rref_solve(A3,
    [(-value) % 3 for value in constant_raw])
assert fresh_rank == w2_rank and W0 is not None and len(fresh_kernel) == 68
assert W0 == list(namespace["sol3"])
left_T0, right_T0 = correction(T0)
left_W0, right_W0 = correction(W0)
P3 = add(P0, sc(3, left_T0), sc(9, left_W0))
Q3 = add(Q0, sc(3, right_T0), sc(9, right_W0))
det3 = jac(P3, Q3)
assert modp(det3, 27) == ONE
assert namespace["dydeg"](P3) == 8 and namespace["dydeg"](Q3) == 12
assert namespace["tdeg"](P3) == 8 and namespace["tdeg"](Q3) == 12

def digest_vector(vector):
    encoded = json.dumps(vector, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


anf = {
    "monomial_order": {
        "constant": 0,
        "linear": [[i, 1+i] for i in range(n)],
        "squares": [[i, 1+n+i] for i in range(n)],
        "cross_order": [[i, j] for i in range(n) for j in range(i+1, n)],
    },
    "equations": equation_basis,
}
anf_bytes = json.dumps(anf, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(os.environ["ANF_OUTPUT"]).write_bytes(anf_bytes)

result = {
    "status": "PASS-AS-B8-D12-W2-W3-AFFINE-KURANISHI-COMPILED",
    "parent_source_sha256": EXPECTED_PARENT,
    "coordinate_slots": [len(mons_r), len(mons_s)],
    "determinant_rows": len(rows),
    "w2_rank": w2_rank,
    "w2_kernel_dimension": len(kernel),
    "w2_particular_sha256": digest_vector(T0),
    "kernel_basis_sha256": digest_vector(kernel),
    "fresh_rank": fresh_rank,
    "fresh_kernel_dimension": len(fresh_kernel),
    "ambient_cokernel_dimension": len(left_kernel),
    "analytic_interpolation_match": True,
    "obstruction_polynomial_span_rank": equation_rank,
    "obstruction_quadratic_coefficient_rank": quadratic_rank,
    "obstruction_tangent_rank_at_frozen_point": tangent_rank,
    "pure_linear_consequence_rank": pure_linear_rank,
    "genuinely_quadratic": quadratic_rank > 0,
    "anf_sha256": hashlib.sha256(anf_bytes).hexdigest(),
    "literal_witness": {
        "predecessor_parameters": [0] * n,
        "fresh_free_parameters": [0] * len(fresh_kernel),
        "T0": T0,
        "W0": W0,
        "actual_y_degrees": [8, 12],
        "actual_total_degrees": [8, 12],
        "determinant_modulus": 27,
        "all_276_rows_replayed": True,
    },
    "projection_statement": {
        "w2_affine_dimension": len(kernel),
        "w3_fresh_fibre_dimension_over_each_compatible_w2_point": len(fresh_kernel),
        "w3_projection_image": "the exact kappa=0 scheme in A^68",
    },
    "scope": "complete fixed-D12 W2 fibre and its W3 compatibility scheme",
    "refusal_scope": [
        "quadratic zero locus not yet classified by this compiler",
        "no W4 or deeper/all-depth branch",
        "no Z3 or characteristic-zero map, counterexample, max12 theorem, or JC2",
    ],
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)

print("slots_rows", slot_count, len(rows))
print("w2_rank_kernel", w2_rank, len(kernel))
print("cokernel", len(left_kernel))
print("analytic_interpolation_match", True)
print("obstruction_span_quadratic_rank", equation_rank, quadratic_rank)
print("tangent_pure_linear_rank", tangent_rank, pure_linear_rank)
print("genuinely_quadratic", quadratic_rank > 0)
print("literal_witness_degrees_y_total", "8,12", "8,12")
print("anf_sha256", result["anf_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])

