#!/usr/bin/env python3
"""Independent staged/Kuranishi audit of the corrected B9 common-cubic gate.

This consumes the pinned parent source but does not consume the producer SMT.
All arithmetic through the final replay is over the integers; only the final
quadratic obstruction coefficients are reduced modulo three.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_b9_9_12_full_fibre_linear_window_20260825"
          / "solve_linear_window_9_12.py")
EXPECTED_PARENT = (
    "fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
saved_output = os.environ["OUTPUT_JSON"]
os.environ["OUTPUT_JSON"] = os.environ["LINEAR_REPLAY_JSON"]
scope = {"__file__": str(PARENT), "__name__": "__independent_cc_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output

p5, q5, one = scope["p5"], scope["q5"], scope["ONE"]
add, sc, jac = scope["add"], scope["sc"], scope["jac"]
correction = scope["correction"]
slots = list(scope["slots"])
support_p = [(i, degree - i) for degree in range(10)
             for i in range(degree + 1)]
support_q = [(i, degree - i) for degree in range(13)
             for i in range(degree + 1)]
assert len(support_p) == 55 and len(support_q) == 91


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def rref_solve(matrix, rhs):
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if not rows:
        return 0, [0] * columns, [
            [1 if i == j else 0 for i in range(columns)]
            for j in range(columns)
        ]
    work = [[value % 3 for value in row] + [target % 3]
            for row, target in zip(matrix, rhs)]
    pivots = []
    row = 0
    for column in range(columns):
        chosen = next((r for r in range(row, rows)
                       if work[r][column]), None)
        if chosen is None:
            continue
        work[row], work[chosen] = work[chosen], work[row]
        if work[row][column] == 2:
            work[row] = [(2 * value) % 3 for value in work[row]]
        for r in range(rows):
            if r == row or not work[r][column]:
                continue
            scalar = work[r][column]
            work[r] = [(a - scalar * b) % 3
                       for a, b in zip(work[r], work[row])]
        pivots.append(column)
        row += 1
        if row == rows:
            break
    if any(not any(current[:-1]) and current[-1] for current in work):
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


def matrix_rank(vectors):
    if not vectors:
        return 0
    transposed = [list(column) for column in zip(*vectors)]
    rank, _, _ = rref_solve(transposed, [0] * len(transposed))
    return rank


def convolution(left, right):
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def residual(values):
    """299 exact integer rows: determinant plus both normalized top forms."""
    assert len(values) == 149
    left, right = correction(values[:146])
    p = add(p5, sc(243, left))
    q = add(q5, sc(243, right))
    determinant = add(jac(p, q), sc(-1, one))
    h = [1, 81 + 243 * values[146], 243 * values[147],
         243 * values[148]]
    h2 = convolution(h, h)
    h3 = convolution(h2, h)
    h4 = convolution(h3, h)
    ptop = [p.get((i, 9 - i), 0) for i in range(10)]
    qtop = [q.get((i, 12 - i), 0) for i in range(13)]
    rows = [determinant.get(xy, 0) for xy in slots]
    rows += [value - ptop[0] * power
             for value, power in zip(ptop, h3)]
    rows += [value - qtop[0] * power
             for value, power in zip(qtop, h4)]
    assert len(rows) == 299
    return rows


coordinate_count = 149
origin = [0] * coordinate_count
r0 = residual(origin)
assert all(value % 243 == 0 for value in r0)
base_integer = [value // 243 for value in r0]
columns_integer = []
for column in range(coordinate_count):
    current = [0] * coordinate_count
    current[column] = 1
    delta = [value - base for value, base in zip(residual(current), r0)]
    assert all(value % 243 == 0 for value in delta)
    columns_integer.append([value // 243 for value in delta])
matrix_integer = [[columns_integer[column][row]
                   for column in range(coordinate_count)]
                  for row in range(299)]
a3 = [[value % 3 for value in row] for row in matrix_integer]

# Complete affine family through 3^10.  Nonlinear terms all carry 243^2 and
# hence vanish modulo 3^10, so the predivided system is linear modulo 243.
stages = []
base_values = [0] * coordinate_count
directions = []
for k in range(1, 6):
    power = 3 ** (k - 1)
    carry = []
    direction_carries = [[] for _ in directions]
    for row in range(299):
        numerator = base_integer[row] + dot(matrix_integer[row], base_values)
        assert numerator % power == 0
        carry.append((numerator // power) % 3)
        for column, direction in enumerate(directions):
            numerator = dot(matrix_integer[row], direction)
            assert numerator % power == 0
            direction_carries[column].append((numerator // power) % 3)
    matrix = [[direction_carries[column][row]
               for column in range(len(directions))] + a3[row]
              for row in range(299)]
    rank, particular, kernel = rref_solve(
        matrix, [(-value) % 3 for value in carry])
    assert particular is not None
    new_base = list(base_values)
    for scalar, direction in zip(particular[:len(directions)], directions):
        new_base = [value + scalar * delta
                    for value, delta in zip(new_base, direction)]
    new_base = [value + power * digit for value, digit in zip(
        new_base, particular[len(directions):])]
    new_directions = []
    for vector in kernel:
        direction = [0] * coordinate_count
        for scalar, old_direction in zip(vector[:len(directions)], directions):
            direction = [value + scalar * delta
                         for value, delta in zip(direction, old_direction)]
        direction = [value + power * digit for value, digit in zip(
            direction, vector[len(directions):])]
        new_directions.append(direction)
    modulus = 3 ** (5 + k)
    exact_base_rows = residual(new_base)
    assert all(value % modulus == 0 for value in exact_base_rows)
    # Basis replay controls the affine serialization at each stage.
    for direction in new_directions:
        for scalar in (1, 2):
            probe = [value + scalar * delta
                     for value, delta in zip(new_base, direction)]
            assert all(value % modulus == 0 for value in residual(probe))
    stages.append({
        "k": k,
        "modulus": modulus,
        "rank": rank,
        "family_dimension": len(new_directions),
        "literal_basis_replay": True,
    })
    base_values, directions = new_base, new_directions

# Invertible coordinate change: only directions visible modulo 3 can occur
# quadratically at the 3^10 -> 3^11 transition.
pivot_directions = []
dependent = []
for index, direction in enumerate(directions):
    target = [value % 3 for value in direction]
    if not pivot_directions:
        if any(target):
            pivot_directions.append(direction)
        else:
            dependent.append((index, []))
        continue
    basis = [[vector[row] % 3 for vector in pivot_directions]
             for row in range(coordinate_count)]
    _, expression, _ = rref_solve(basis, target)
    if expression is None:
        pivot_directions.append(direction)
    else:
        dependent.append((index, expression))
changed_directions = list(pivot_directions)
for index, expression in dependent:
    direction = list(directions[index])
    for scalar, pivot in zip(expression, pivot_directions):
        direction = [value - scalar * delta
                     for value, delta in zip(direction, pivot)]
    assert all(value % 3 == 0 for value in direction)
    changed_directions.append(direction)
directions = changed_directions
active_count = len(pivot_directions)
inactive_count = len(directions) - active_count

target_divisor = 3 ** 10


def final_value(values):
    rows = residual(values)
    assert all(value % target_divisor == 0 for value in rows)
    return [(value // target_divisor) % 3 for value in rows]


f0 = final_value(base_values)
linear = []
diagonal = []
f1_cache = []
for direction in directions:
    one_probe = [value + delta for value, delta in zip(base_values, direction)]
    two_probe = [value + 2 * delta for value, delta in zip(base_values, direction)]
    f1 = final_value(one_probe)
    f2 = final_value(two_probe)
    f1_cache.append(f1)
    d1 = [(value - base) % 3 for value, base in zip(f1, f0)]
    d2 = [(value - base) % 3 for value, base in zip(f2, f0)]
    quad = [(2 * (left + right)) % 3 for left, right in zip(d1, d2)]
    lin = [(left - qvalue) % 3 for left, qvalue in zip(d1, quad)]
    linear.append(lin)
    diagonal.append(quad)
assert all(not any(vector) for vector in diagonal[active_count:])

cross = []
cross_indices = []
for left in range(active_count):
    for right in range(left + 1, active_count):
        probe = [base + a + b for base, a, b in zip(
            base_values, directions[left], directions[right])]
        f11 = final_value(probe)
        vector = [(value - f1_cache[left][row] - f1_cache[right][row]
                   + f0[row]) % 3 for row, value in enumerate(f11)]
        cross.append(vector)
        cross_indices.append((left, right))

# Compute the literal fresh operator at order 3^10 independently of the
# earlier finite-difference matrix.
fresh_columns = []
base_rows = residual(base_values)
for column in range(coordinate_count):
    probe = list(base_values)
    probe[column] += 3 ** 5
    delta = [value - base for value, base in zip(residual(probe), base_rows)]
    assert all(value % target_divisor == 0 for value in delta)
    fresh_columns.append([(value // target_divisor) % 3 for value in delta])
fresh_matrix = [[fresh_columns[column][row]
                 for column in range(coordinate_count)]
                for row in range(299)]
transpose = [list(column) for column in zip(*fresh_matrix)]
fresh_rank, _, fresh_left_kernel = rref_solve(
    transpose, [0] * coordinate_count)


def project(vector):
    return [dot(functional, vector) % 3
            for functional in fresh_left_kernel]


raw_constant = project(f0)
raw_linear = [project(vector) for vector in linear]
raw_diagonal = [project(vector) for vector in diagonal[:active_count]]
raw_cross = [project(vector) for vector in cross]
cokernel_dimension = len(fresh_left_kernel)
inactive_matrix = [[raw_linear[column][row]
                    for column in range(active_count, len(directions))]
                   for row in range(cokernel_dimension)]
if inactive_count:
    inactive_transpose = [list(column) for column in zip(*inactive_matrix)]
    inactive_rank, _, inactive_left_kernel = rref_solve(
        inactive_transpose, [0] * inactive_count)
else:
    inactive_rank = 0
    inactive_left_kernel = [
        [1 if i == j else 0 for i in range(cokernel_dimension)]
        for j in range(cokernel_dimension)
    ]


def quotient(vector):
    return [dot(functional, vector) % 3
            for functional in inactive_left_kernel]


reduced_constant = quotient(raw_constant)
reduced_linear = [quotient(raw_linear[column])
                  for column in range(active_count)]
reduced_diagonal = [quotient(vector) for vector in raw_diagonal]
reduced_cross = [quotient(vector) for vector in raw_cross]
keep = []
for equation in range(len(inactive_left_kernel)):
    if (reduced_constant[equation]
            or any(vector[equation] for vector in reduced_linear)
            or any(vector[equation] for vector in reduced_diagonal)
            or any(vector[equation] for vector in reduced_cross)):
        keep.append(equation)


def restrict(vector):
    return [vector[index] for index in keep]


reduced_constant = restrict(reduced_constant)
reduced_linear = [restrict(vector) for vector in reduced_linear]
reduced_diagonal = [restrict(vector) for vector in reduced_diagonal]
reduced_cross = [restrict(vector) for vector in reduced_cross]

# A zero residual system must yield a literal target-depth witness.  Choose
# zero active coordinates, solve the spectator equation in the fresh
# cokernel, then solve the full fresh system and replay all 299 integer rows.
witness = None
if not keep:
    if inactive_count:
        _, inactive_solution, _ = rref_solve(
            inactive_matrix, [(-value) % 3 for value in raw_constant])
        assert inactive_solution is not None
    else:
        assert not any(raw_constant)
        inactive_solution = []
    predecessor = list(base_values)
    for scalar, direction in zip(inactive_solution,
                                 directions[active_count:]):
        predecessor = [value + scalar * delta
                       for value, delta in zip(predecessor, direction)]
    predecessor_rows = residual(predecessor)
    assert all(value % target_divisor == 0 for value in predecessor_rows)
    fresh_rhs = [(-(value // target_divisor)) % 3
                 for value in predecessor_rows]
    _, fresh_solution, fresh_kernel = rref_solve(fresh_matrix, fresh_rhs)
    assert fresh_solution is not None
    final_values = [value + (3 ** 5) * digit
                    for value, digit in zip(predecessor, fresh_solution)]
    final_rows = residual(final_values)
    target_modulus = 3 ** 11
    assert all(value % target_modulus == 0 for value in final_rows)
    left, right = correction(final_values[:146])
    witness_p = add(p5, sc(243, left))
    witness_q = add(q5, sc(243, right))
    witness_h = [1, 81 + 243 * final_values[146],
                 243 * final_values[147], 243 * final_values[148]]
    assert witness_p.get((0, 9), 0) % 3
    assert witness_q.get((0, 12), 0) % 3
    witness_payload = {
        "predecessor_values_mod243": [value % (3 ** 5)
                                       for value in predecessor],
        "fresh_digits": fresh_solution,
        "final_values_mod729": [value % (3 ** 6)
                                 for value in final_values],
        "P_support_mod177147": [[i, j, value % target_modulus]
                                 for (i, j), value in sorted(witness_p.items())
                                 if value % target_modulus],
        "Q_support_mod177147": [[i, j, value % target_modulus]
                                 for (i, j), value in sorted(witness_q.items())
                                 if value % target_modulus],
        "H_coefficients_mod177147": [value % target_modulus
                                      for value in witness_h],
        "fresh_kernel_dimension": len(fresh_kernel),
        "all_299_integer_rows_zero_mod177147": True,
    }
    witness_bytes = (json.dumps(witness_payload, sort_keys=True,
                                separators=(",", ":")) + "\n").encode()
    Path(os.environ["WITNESS_OUTPUT"]).write_bytes(witness_bytes)
    witness = {
        "payload_sha256": hashlib.sha256(witness_bytes).hexdigest(),
        "all_299_integer_rows_zero_mod177147": True,
        "P_y9_mod3": witness_p.get((0, 9), 0) % 3,
        "Q_y12_mod3": witness_q.get((0, 12), 0) % 3,
        "H_coefficients_mod177147": witness_payload[
            "H_coefficients_mod177147"],
    }

anf = {
    "constant": reduced_constant,
    "linear": reduced_linear,
    "diagonal": reduced_diagonal,
    "cross_indices": cross_indices,
    "cross": reduced_cross,
}
anf_bytes = (json.dumps(anf, sort_keys=True, separators=(",", ":"))
             + "\n").encode()
Path(os.environ["ANF_OUTPUT"]).write_bytes(anf_bytes)

result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-INDEPENDENT-KURANISHI",
    "parent_source_sha256": EXPECTED_PARENT,
    "row_count": 299,
    "coordinate_count": coordinate_count,
    "stages": stages,
    "predecessor_dimension_mod3p10": len(directions),
    "active_quadratic_dimension": active_count,
    "linear_spectator_dimension": inactive_count,
    "fresh_rank": fresh_rank,
    "fresh_kernel_dimension": coordinate_count - fresh_rank,
    "fresh_cokernel_dimension": cokernel_dimension,
    "spectator_rank_in_fresh_cokernel": inactive_rank,
    "final_equation_count": len(keep),
    "anf_sha256": hashlib.sha256(anf_bytes).hexdigest(),
    "witness": witness,
    "original_producer_smt_consumed": False,
    "integer_basis_replay_through_mod3p10": True,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("stage_dimensions", [stage["family_dimension"] for stage in stages])
print("predecessor_active_inactive", len(directions), active_count,
      inactive_count)
print("fresh_rank_kernel_cokernel", fresh_rank,
      coordinate_count - fresh_rank, cokernel_dimension)
print("spectator_rank_final_equations", inactive_rank, len(keep))
print("anf_sha256", result["anf_sha256"])
print("witness", witness)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
