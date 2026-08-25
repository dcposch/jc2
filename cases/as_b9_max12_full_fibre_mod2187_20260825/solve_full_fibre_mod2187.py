#!/usr/bin/env python3
"""Exact Bockstein projection of the full B9 mod729 affine fibre."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_b9_max12_full_output_mod729_20260825"
          / "solve_full_output_mod729.py")
EXPECTED_PARENT = (
    "4deb7fe07acef4f37bb14735493b0d20b6c7ac66bb10633f81b7bc1a48264bd4")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
saved_output = os.environ["OUTPUT_JSON"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
ns = {"__file__": str(PARENT), "__name__": "__b9_full2187_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), ns)
os.environ["OUTPUT_JSON"] = saved_output

add, sc, jac, modp = ns["add"], ns["sc"], ns["jac"], ns["modp"]
p5, q5, d5, ONE = ns["p5"], ns["q5"], ns["d5"], ns["ONE"]
support, slots = list(ns["support"]), list(ns["slots"])
correction = ns["correction"]
coefficient = ns["coefficient"]
parent_particular = list(ns["particular"])
parent_kernel = [list(vector) for vector in ns["kernel"]]
assert len(parent_kernel) == 74


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def rref_solve(matrix, rhs):
    work = [[value % 3 for value in row] + [target % 3]
            for row, target in zip(matrix, rhs)]
    pivots = []
    row = 0
    for column in range(len(matrix[0])):
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
    if any(not any(row[:-1]) and row[-1] for row in work):
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
            vector[pivot] = (-work[r][free_column]) % 3
        kernel.append(vector)
    return len(pivots), particular, kernel


def matrix_rank(vectors):
    if not vectors:
        return 0
    transposed = [list(column) for column in zip(*vectors)]
    value, _, _ = rref_solve(transposed, [0] * len(transposed))
    return value


residual5 = add(d5, sc(-1, ONE))
base_integer = []
for xy in slots:
    value = coefficient(residual5, xy)
    assert value % 243 == 0
    base_integer.append(value // 243)

columns_integer = []
for column in range(182):
    values = [0] * 182
    values[column] = 1
    left, right = correction(values)
    current = add(jac(add(p5, sc(243, left)), add(q5, sc(243, right))),
                  sc(-1, d5))
    output = []
    for xy in slots:
        value = coefficient(current, xy)
        assert value % 243 == 0
        output.append(value // 243)
    columns_integer.append(output)
matrix_integer = [[columns_integer[column][row] for column in range(182)]
                  for row in range(276)]
A3 = [[value % 3 for value in row] for row in matrix_integer]
assert all((base_integer[row] + dot(matrix_integer[row], parent_particular))
           % 3 == 0 for row in range(276))
assert all(dot(row, direction) % 3 == 0
           for row in matrix_integer for direction in parent_kernel)

# Carry affine function on the complete 74D predecessor fibre.
carry_constant = []
carry_columns = [[] for _ in parent_kernel]
for row in range(276):
    numerator = base_integer[row] + dot(
        matrix_integer[row], parent_particular)
    assert numerator % 3 == 0
    carry_constant.append((numerator // 3) % 3)
    for column, direction in enumerate(parent_kernel):
        numerator = dot(matrix_integer[row], direction)
        assert numerator % 3 == 0
        carry_columns[column].append((numerator // 3) % 3)

# Canonical left-cokernel basis and its affine obstruction equations.
transpose = [list(column) for column in zip(*A3)]
fresh_rank, _, left_kernel = rref_solve(transpose, [0] * 182)
assert fresh_rank == 108 and len(left_kernel) == 168
obstruction_matrix = []
obstruction_rhs = []
for functional in left_kernel:
    row = [sum(functional[index] * carry_columns[column][index]
               for index in range(276)) % 3
           for column in range(74)]
    value = sum(functional[index] * carry_constant[index]
                for index in range(276)) % 3
    if any(row) or value:
        obstruction_matrix.append(row)
        obstruction_rhs.append((-value) % 3)
obstruction_rank, obstruction_particular, obstruction_kernel = rref_solve(
    obstruction_matrix, obstruction_rhs)

matrix1 = [[carry_columns[column][row] for column in range(74)] + A3[row]
           for row in range(276)]
rank1, p1, K1 = rref_solve(
    matrix1, [(-value) % 3 for value in carry_constant])
assert (p1 is not None) == (obstruction_particular is not None)

# The frozen deterministic parent is s=0.  It was independently observed to
# fail; reproduce that pointwise negative control source-honestly.
stored_rank, stored_fresh, _ = rref_solve(
    A3, [(-value) % 3 for value in carry_constant])
assert stored_rank == 108 and stored_fresh is None

result = {
    "status": ("PASS-AS-B9-D12-FULL-FIBRE-MOD2187-SAT"
               if p1 is not None
               else "PASS-AS-B9-D12-FULL-FIBRE-MOD2187-UNSAT"),
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_replay_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "slot_count": 276,
    "fresh_variable_count": 182,
    "predecessor_parameter_count": 74,
    "fresh_rank": fresh_rank,
    "fresh_cokernel_dimension": len(left_kernel),
    "effective_obstruction_count": len(obstruction_matrix),
    "effective_obstruction_rank": obstruction_rank,
    "obstruction_consistent": obstruction_particular is not None,
    "combined_rank": rank1,
    "consistent": p1 is not None,
    "combined_kernel_dimension": len(K1) if p1 is not None else None,
    "stored_particular_lifts": False,
    "matrix_integer_sha256": hashlib.sha256(json.dumps(
        matrix_integer, separators=(",", ":")).encode()).hexdigest(),
    "obstruction_sha256": hashlib.sha256(json.dumps(
        [obstruction_matrix, obstruction_rhs],
        separators=(",", ":")).encode()).hexdigest(),
    "scope": "full 74D mod729 affine fibre over one fixed B9 mod243 point",
    "refusal_scope": [
        "not the complete earlier mod243 fibre",
        "no modulus6561 or deeper/all-depth branch",
        "no characteristic-zero point, counterexample, maximum12 theorem, or JC2",
    ],
}

if p1 is not None:
    projected = [vector[:74] for vector in K1]
    projection_dimension = matrix_rank(projected)
    result["liftable_predecessor_dimension"] = projection_dimension
    result["new_solution_exponent"] = len(K1)
    T = list(parent_particular)
    for scalar, direction in zip(p1[:74], parent_kernel):
        T = [value + scalar * delta
             for value, delta in zip(T, direction)]
    V = p1[74:]
    left_T, right_T = correction(T)
    left_V, right_V = correction(V)
    P = add(p5, sc(243, left_T), sc(729, left_V))
    Q = add(q5, sc(243, right_T), sc(729, right_V))
    determinant = add(jac(P, Q), sc(-1, ONE))
    assert all(coefficient(determinant, xy) % 2187 == 0 for xy in slots)
    assert max(i + j for i, j in P) <= 12
    assert max(i + j for i, j in Q) <= 12
    assert max(j for i, j in P) <= 12 and max(j for i, j in Q) <= 12
    result.update({
        "literal_integer_replay_mod2187_passed": True,
        "predecessor_parameters": p1[:74],
        "fresh_digit": V,
        "T": [value % 3 for value in T],
        "P_support": [[i, j, value] for (i, j), value in sorted(P.items())],
        "Q_support": [[i, j, value] for (i, j), value in sorted(Q.items())],
        "determinant_sha256": hashlib.sha256(
            repr(sorted(jac(P, Q).items())).encode()).hexdigest(),
        "degrees_total": [max(i + j for i, j in P),
                          max(i + j for i, j in Q)],
        "degrees_y": [max(j for i, j in P), max(j for i, j in Q)],
    })

encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(saved_output).write_bytes(encoded + b"\n")
print("fresh_rank_cokernel", fresh_rank, len(left_kernel))
print("effective_obstruction", len(obstruction_matrix), obstruction_rank,
      obstruction_particular is not None)
print("combined", rank1, None if p1 is None else len(K1))
print("stored_particular_lifts", False)
if p1 is not None:
    print("liftable_predecessor_dimension",
          result["liftable_predecessor_dimension"])
    print("new_solution_exponent", result["new_solution_exponent"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
