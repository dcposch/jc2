#!/usr/bin/env python3
"""First exact quadratic gate for the complete normalized B9 (9,12) family."""

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
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
ns = {"__file__": str(PARENT), "__name__": "__b9_9_12_quad_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), ns)
os.environ["OUTPUT_JSON"] = saved_output

add, sc, jac = ns["add"], ns["sc"], ns["jac"]
p5, q5, ONE = ns["p5"], ns["q5"], ns["ONE"]
slots = list(ns["slots"])
correction, coefficient = ns["correction"], ns["coefficient"]
base_integer = list(ns["base_integer"])
matrix_integer = [list(row) for row in ns["matrix_integer"]]
A3 = [list(row) for row in ns["A3"]]
T_base = list(ns["base_T"])
old_directions = [list(vector) for vector in ns["directions"]]
assert len(T_base) == 146 and len(old_directions) == 145


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def rref_solve(matrix, rhs):
    if not matrix:
        return 0, [], []
    columns = len(matrix[0])
    if columns == 0:
        return 0, ([] if not any(value % 3 for value in rhs) else None), []
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
    value, _, _ = rref_solve(transposed, [0] * len(transposed))
    return value


# Invertible predecessor coordinate change: visible mod-three image first,
# then exact directions divisible by three.
pivot_directions = []
dependent = []
for index, direction in enumerate(old_directions):
    target = [value % 3 for value in direction]
    if not pivot_directions:
        if any(target):
            pivot_directions.append(direction)
        else:
            dependent.append((index, []))
        continue
    basis = [[vector[row] % 3 for vector in pivot_directions]
             for row in range(146)]
    _, expression, _ = rref_solve(basis, target)
    if expression is None:
        pivot_directions.append(direction)
    else:
        dependent.append((index, expression))
directions = list(pivot_directions)
for index, expression in dependent:
    direction = list(old_directions[index])
    for scalar, pivot in zip(expression, pivot_directions):
        direction = [value - scalar * delta
                     for value, delta in zip(direction, pivot)]
    assert all(value % 3 == 0 for value in direction)
    directions.append(direction)
assert len(directions) == 145
active_count = len(pivot_directions)
inactive_count = 145 - active_count


def deriv(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[xy] = answer.get(xy, 0) + exponent * value
    return {xy: value for xy, value in answer.items() if value}


def mul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            answer[xy] = answer.get(xy, 0) + a * b
    return {xy: value for xy, value in answer.items() if value}


def jacobian_pair(values):
    left, right = correction(values)
    return add(mul(deriv(left, 0), deriv(right, 1)),
               sc(-1, mul(deriv(left, 1), deriv(right, 0))))


def cross_pair(left_values, right_values):
    lp, lq = correction(left_values)
    rp, rq = correction(right_values)
    return add(mul(deriv(lp, 0), deriv(rq, 1)),
               mul(deriv(rp, 0), deriv(lq, 1)),
               sc(-1, mul(deriv(lp, 1), deriv(rq, 0))),
               sc(-1, mul(deriv(rp, 1), deriv(lq, 0))))


# Stored arrays are predivided by the outer 243, so divide by 3^5 here.
power = 3 ** 5
carry_constant = []
carry_columns = [[] for _ in directions]
for row in range(276):
    numerator = base_integer[row] + dot(matrix_integer[row], T_base)
    assert numerator % power == 0
    carry_constant.append((numerator // power) % 3)
    for column, direction in enumerate(directions):
        numerator = dot(matrix_integer[row], direction)
        assert numerator % power == 0
        carry_columns[column].append((numerator // power) % 3)

transpose = [list(column) for column in zip(*A3)]
fresh_rank, _, fresh_left_kernel = rref_solve(transpose, [0] * 146)
fresh_kernel_dimension = 146 - fresh_rank

q_base_poly = jacobian_pair(T_base)
q_base = [coefficient(q_base_poly, xy) % 3 for xy in slots]
raw_constant = [sum(functional[row] * (
    carry_constant[row] + q_base[row]) for row in range(276)) % 3
                for functional in fresh_left_kernel]
raw_linear = [[0] * 145 for _ in fresh_left_kernel]
active_diagonal_polys = []
for column in range(active_count):
    mixed = cross_pair(T_base, directions[column])
    diagonal = jacobian_pair(directions[column])
    active_diagonal_polys.append(diagonal)
    for equation, functional in enumerate(fresh_left_kernel):
        raw_linear[equation][column] = sum(functional[row] * (
            carry_columns[column][row] + coefficient(mixed, slots[row]))
            for row in range(276)) % 3
for column in range(active_count, 145):
    for equation, functional in enumerate(fresh_left_kernel):
        raw_linear[equation][column] = sum(
            functional[row] * carry_columns[column][row]
            for row in range(276)) % 3

raw_diagonal = [[sum(functional[row] * coefficient(poly, slots[row])
                         for row in range(276)) % 3
                 for functional in fresh_left_kernel]
                for poly in active_diagonal_polys]
raw_cross = []
cross_indices = []
for left in range(active_count):
    for right in range(left + 1, active_count):
        poly = cross_pair(directions[left], directions[right])
        raw_cross.append([sum(functional[row] * coefficient(poly, slots[row])
                              for row in range(276)) % 3
                          for functional in fresh_left_kernel])
        cross_indices.append((left, right))

inactive_matrix = [row[active_count:] for row in raw_linear]
inactive_rank, _, inactive_left_kernel = rref_solve(
    [list(column) for column in zip(*inactive_matrix)],
    [0] * inactive_count)

def project(vector):
    return [dot(functional, vector) % 3 for functional in inactive_left_kernel]

reduced_constant = project(raw_constant)
reduced_linear = [project([raw_linear[e][column]
                           for e in range(len(fresh_left_kernel))])
                  for column in range(active_count)]
reduced_diagonal = [project(vector) for vector in raw_diagonal]
reduced_cross = [project(vector) for vector in raw_cross]

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
equation_count = len(keep)

inactive_columns = [list(column) for column in zip(*inactive_matrix)]
raw_coefficients = [raw_constant]
raw_coefficients += [[raw_linear[e][column]
                      for e in range(len(fresh_left_kernel))]
                     for column in range(active_count)]
raw_coefficients += raw_diagonal + raw_cross
raw_coefficient_rank = matrix_rank(raw_coefficients)
containment_augmented_rank = matrix_rank(inactive_columns + raw_coefficients)


def evaluate(active):
    values = list(reduced_constant)
    for equation in range(equation_count):
        for column, scalar in enumerate(active):
            values[equation] += reduced_linear[column][equation] * scalar
            values[equation] += reduced_diagonal[column][equation] * scalar * scalar
        for (left, right), vector in zip(cross_indices, reduced_cross):
            values[equation] += vector[equation] * active[left] * active[right]
        values[equation] %= 3
    return values


def solve_inactive(active):
    T = list(T_base)
    for scalar, direction in zip(active, directions[:active_count]):
        T = [value + scalar * delta for value, delta in zip(T, direction)]
    qpoly = jacobian_pair(T)
    rhs = []
    for functional in fresh_left_kernel:
        value = 0
        for row, xy in enumerate(slots):
            affine = carry_constant[row] + sum(
                scalar * carry_columns[column][row]
                for column, scalar in enumerate(active))
            value += functional[row] * (affine + coefficient(qpoly, xy))
        rhs.append((-value) % 3)
    _, particular, kernel = rref_solve(inactive_matrix, rhs)
    return particular, kernel


def replay(active, inactive):
    parameters = active + inactive
    T = list(T_base)
    for scalar, direction in zip(parameters, directions):
        T = [value + scalar * delta for value, delta in zip(T, direction)]
    qpoly = jacobian_pair(T)
    residual = []
    for row, xy in enumerate(slots):
        numerator = base_integer[row] + dot(matrix_integer[row], T)
        assert numerator % power == 0
        residual.append(((numerator // power) + coefficient(qpoly, xy)) % 3)
    _, W, fresh_kernel = rref_solve(A3, [(-value) % 3 for value in residual])
    assert W is not None and len(fresh_kernel) == fresh_kernel_dimension
    left_T, right_T = correction(T)
    left_W, right_W = correction(W)
    P = add(p5, sc(243, left_T), sc(3 ** 10, left_W))
    Q = add(q5, sc(243, right_T), sc(3 ** 10, right_W))
    determinant = add(jac(P, Q), sc(-1, ONE))
    assert all(coefficient(determinant, xy) % (3 ** 11) == 0 for xy in slots)
    assert ns["tdeg"](P) <= 9 and ns["dydeg"](P) <= 9
    assert ns["tdeg"](Q) <= 12 and ns["dydeg"](Q) <= 12
    return {
        "active": active,
        "inactive": inactive,
        "fresh_digit": W,
        "literal_integer_replay_mod177147_passed": True,
        "degrees_total": [ns["tdeg"](P), ns["tdeg"](Q)],
        "degrees_y": [ns["dydeg"](P), ns["dydeg"](Q)],
        "determinant_sha256": hashlib.sha256(
            repr(sorted(jac(P, Q).items())).encode()).hexdigest(),
    }


witness = None
finder_trials = []
trials = [[0] * active_count]
for index in range(active_count):
    for scalar in (1, 2):
        vector = [0] * active_count
        vector[index] = scalar
        trials.append(vector)
for index, active in enumerate(trials):
    if any(evaluate(active)):
        finder_trials.append([index, "reduced_nonzero"])
        continue
    inactive, _ = solve_inactive(active)
    if inactive is None:
        finder_trials.append([index, "inactive_inconsistent"])
        continue
    witness = replay(active, inactive)
    finder_trials.append([index, "SAT"])
    break


def bv(value):
    return "#x" + format(value % 16, "x")


def mod3(term):
    return f"(bvurem {term} #x3)"


def add3(terms):
    answer = "#x0"
    for term in terms:
        answer = mod3(f"(bvadd {answer} {term})")
    return answer


smt = Path(os.environ["SMT2_OUTPUT"])
with smt.open("w") as stream:
    stream.write("(set-logic QF_BV)\n(set-option :produce-models true)\n")
    for index in range(active_count):
        stream.write(f"(declare-fun a{index} () (_ BitVec 4))\n")
        stream.write(f"(assert (bvule a{index} #x2))\n")
    for equation in range(equation_count):
        terms = [bv(reduced_constant[equation])]
        for column in range(active_count):
            if reduced_linear[column][equation]:
                terms.append(mod3(f"(bvmul {bv(reduced_linear[column][equation])} a{column})"))
            if reduced_diagonal[column][equation]:
                terms.append(mod3(f"(bvmul {bv(reduced_diagonal[column][equation])} (bvmul a{column} a{column}))"))
        for (left, right), vector in zip(cross_indices, reduced_cross):
            if vector[equation]:
                terms.append(mod3(f"(bvmul {bv(vector[equation])} (bvmul a{left} a{right}))"))
        stream.write(f"(assert (= {add3(terms)} #x0))\n")
    stream.write("(check-sat)\n(get-model)\n")

anf = {
    "constant": reduced_constant,
    "linear": reduced_linear,
    "diagonal": reduced_diagonal,
    "cross_indices": cross_indices,
    "cross": reduced_cross,
}
anf_bytes = json.dumps(anf, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(os.environ["ANF_OUTPUT"]).write_bytes(anf_bytes)

projection_dimension = active_count + inactive_count - inactive_rank
full_dimension = projection_dimension + fresh_kernel_dimension
result = {
    "status": ("PASS-AS-B9-9-12-QUADRATIC-3P11-SAT"
               if witness is not None
               else "PASS-AS-B9-9-12-QUADRATIC-3P11-COMPILED"),
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_replay_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "slot_count": 276,
    "predecessor_dimension": 145,
    "fresh_variable_count": 146,
    "fresh_rank": fresh_rank,
    "fresh_cokernel_dimension": len(fresh_left_kernel),
    "fresh_kernel_dimension": fresh_kernel_dimension,
    "active_quadratic_dimension": active_count,
    "linear_spectator_dimension": inactive_count,
    "spectator_linear_rank": inactive_rank,
    "spectator_kernel_dimension": inactive_count - inactive_rank,
    "post_elimination_equation_count": equation_count,
    "raw_polynomial_coefficient_rank": raw_coefficient_rank,
    "containment_augmented_rank": containment_augmented_rank,
    "all_polynomial_coefficients_in_spectator_image": (
        containment_augmented_rank == inactive_rank),
    "predecessor_projection_dimension": projection_dimension,
    "full_lift_family_dimension_if_residual_zero": (
        full_dimension if equation_count == 0 else None),
    "finder_trials": finder_trials,
    "witness": witness,
    "anf_sha256": hashlib.sha256(anf_bytes).hexdigest(),
    "smt2_sha256": hashlib.sha256(smt.read_bytes()).hexdigest(),
    "scope": "complete displayed (9,12) mod3^10 family over one B9 mod243 point",
    "refusal_scope": [
        "no mod3^12 or all-depth branch",
        "not the complete earlier mod243 fibre",
        "no counterexample, maximum12 theorem, or JC2",
    ],
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(saved_output).write_bytes(encoded + b"\n")
print("active_inactive", active_count, inactive_count)
print("fresh_rank_cokernel", fresh_rank, len(fresh_left_kernel))
print("spectator_rank_equations", inactive_rank, equation_count)
print("coefficient_augmented_rank", raw_coefficient_rank,
      containment_augmented_rank)
print("projection_full_if_zero", projection_dimension,
      result["full_lift_family_dimension_if_residual_zero"])
print("finder", None if witness is None else "SAT")
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
