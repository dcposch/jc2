#!/usr/bin/env python3
"""First exact quadratic Kuranishi gate for the full B9 D12 family."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_b9_max12_full_fibre_linear_window_20260825"
          / "solve_linear_window.py")
EXPECTED_PARENT = (
    "0bf4766d8e4840fb89661eaba6b8cb4661b554c7f8944f5eb55bac37298f2ac7")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
saved_output = os.environ["OUTPUT_JSON"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
ns = {"__file__": str(PARENT), "__name__": "__b9_quad_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), ns)
os.environ["OUTPUT_JSON"] = saved_output

add, sc, jac = ns["add"], ns["sc"], ns["jac"]
p5, q5, ONE = ns["p5"], ns["q5"], ns["ONE"]
support, slots = list(ns["support"]), list(ns["slots"])
correction, coefficient = ns["correction"], ns["coefficient"]
base_integer = list(ns["base_integer"])
matrix_integer = [list(row) for row in ns["matrix_integer"]]
A3 = [list(row) for row in ns["A3"]]
T_base = list(ns["base_T"])
old_directions = [list(vector) for vector in ns["directions"]]
assert len(old_directions) == 165


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def dydeg_mod(poly, modulus):
    return max((j for (i, j), value in poly.items() if value % modulus),
               default=-1)


def tdeg_mod(poly, modulus):
    return max((i + j for (i, j), value in poly.items() if value % modulus),
               default=-1)


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
    if any(not any(row[:-1]) and row[-1] for row in work):
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


# Choose an independent column basis for the predecessor image T mod 3 and
# replace every other direction by a congruent direction divisible by three.
pivot_directions = []
pivot_indices = []
dependent = []
for index, direction in enumerate(old_directions):
    target = [value % 3 for value in direction]
    if not pivot_directions:
        if any(target):
            pivot_directions.append(direction)
            pivot_indices.append(index)
        else:
            dependent.append((index, []))
        continue
    basis_matrix = [[direction[row] % 3
                     for direction in pivot_directions]
                    for row in range(182)]
    _, expression, _ = rref_solve(basis_matrix, target)
    if expression is None:
        pivot_directions.append(direction)
        pivot_indices.append(index)
    else:
        dependent.append((index, expression))

active_count = len(pivot_directions)
directions = list(pivot_directions)
for index, expression in dependent:
    direction = list(old_directions[index])
    for scalar, pivot in zip(expression, pivot_directions):
        direction = [value - scalar * delta
                     for value, delta in zip(direction, pivot)]
    assert all(value % 3 == 0 for value in direction)
    directions.append(direction)
assert len(directions) == 165
inactive_count = len(directions) - active_count
assert matrix_rank([[direction[row] % 3 for row in range(182)]
                    for direction in directions[:active_count]]) == active_count


def polynomial_deriv(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[xy] = answer.get(xy, 0) + exponent * value
    return {xy: value for xy, value in answer.items() if value}


def polynomial_mul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            answer[xy] = answer.get(xy, 0) + a * b
    return {xy: value for xy, value in answer.items() if value}


def jacobian_pair(values):
    left, right = correction(values)
    return add(polynomial_mul(polynomial_deriv(left, 0),
                              polynomial_deriv(right, 1)),
               sc(-1, polynomial_mul(polynomial_deriv(left, 1),
                                     polynomial_deriv(right, 0))))


def cross_pair(left_values, right_values):
    lp, lq = correction(left_values)
    rp, rq = correction(right_values)
    return add(polynomial_mul(polynomial_deriv(lp, 0),
                              polynomial_deriv(rq, 1)),
               polynomial_mul(polynomial_deriv(rp, 0),
                              polynomial_deriv(lq, 1)),
               sc(-1, polynomial_mul(polynomial_deriv(lp, 1),
                                     polynomial_deriv(rq, 0))),
               sc(-1, polynomial_mul(polynomial_deriv(rp, 1),
                                     polynomial_deriv(lq, 0))))


# Complete divided-linear carry at valuation 3^10.  The stored
# base_integer/matrix_integer arrays have already been divided by the outer
# 243 in F = F5 + 243*T, so the remaining exact divisor is 3^5, not 3^10.
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

# Eliminate the rank-108 fresh W operator by its exact ambient left cokernel.
transpose = [list(column) for column in zip(*A3)]
fresh_rank, _, fresh_left_kernel = rref_solve(transpose, [0] * 182)
assert fresh_rank == 108 and len(fresh_left_kernel) == 168

q_base_poly = jacobian_pair(T_base)
q_base = [coefficient(q_base_poly, xy) % 3 for xy in slots]
raw_constant = []
raw_linear = [[0] * 165 for _ in fresh_left_kernel]
for equation, functional in enumerate(fresh_left_kernel):
    raw_constant.append(sum(functional[row] * (
        carry_constant[row] + q_base[row]) for row in range(276)) % 3)

active_diagonal_polys = []
for column in range(active_count):
    direction = directions[column]
    mixed = cross_pair(T_base, direction)
    diagonal = jacobian_pair(direction)
    active_diagonal_polys.append(diagonal)
    for equation, functional in enumerate(fresh_left_kernel):
        raw_linear[equation][column] = sum(functional[row] * (
            carry_columns[column][row] + coefficient(mixed, slots[row]))
            for row in range(276)) % 3
for column in range(active_count, 165):
    for equation, functional in enumerate(fresh_left_kernel):
        raw_linear[equation][column] = sum(
            functional[row] * carry_columns[column][row]
            for row in range(276)) % 3

raw_diagonal_vectors = []
for column in range(active_count):
    raw_diagonal_vectors.append([
        sum(functional[row]
            * coefficient(active_diagonal_polys[column], slots[row])
            for row in range(276)) % 3
        for functional in fresh_left_kernel])

inactive_matrix = [row[active_count:] for row in raw_linear]
inactive_rank, _, inactive_left_kernel = rref_solve(
    [list(column) for column in zip(*inactive_matrix)],
    [0] * inactive_count)
assert len(inactive_left_kernel) == 168 - inactive_rank

reduced_constant = []
reduced_linear = []
reduced_diagonal = []
for functional in inactive_left_kernel:
    reduced_constant.append(dot(functional, raw_constant) % 3)
    reduced_linear.append([
        sum(functional[equation] * raw_linear[equation][column]
            for equation in range(168)) % 3
        for column in range(active_count)])
    reduced_diagonal.append([
        sum(functional[equation] * sum(
            fresh_left_kernel[equation][row]
            * coefficient(active_diagonal_polys[column], slots[row])
            for row in range(276)) for equation in range(168)) % 3
        for column in range(active_count)])

reduced_cross = []
raw_cross_vectors = []
for left in range(active_count):
    for right in range(left + 1, active_count):
        mixed = cross_pair(directions[left], directions[right])
        raw_values = [sum(functional[row] * coefficient(mixed, slots[row])
                          for row in range(276)) % 3
                      for functional in fresh_left_kernel]
        raw_cross_vectors.append(raw_values)
        values = [dot(functional, raw_values) % 3
                  for functional in inactive_left_kernel]
        if any(values):
            reduced_cross.append([left, right, values])

# Delete equations which are polynomially zero after both eliminations.
keep = []
for equation in range(len(inactive_left_kernel)):
    nonzero = (reduced_constant[equation]
               or any(reduced_linear[equation])
               or any(reduced_diagonal[equation])
               or any(values[equation] for _, _, values in reduced_cross))
    if nonzero:
        keep.append(equation)
reduced_constant = [reduced_constant[index] for index in keep]
reduced_linear = [reduced_linear[index] for index in keep]
reduced_diagonal = [reduced_diagonal[index] for index in keep]
reduced_cross = [[left, right, [values[index] for index in keep]]
                 for left, right, values in reduced_cross
                 if any(values[index] for index in keep)]
equation_count = len(keep)

# Exact containment certificate: after quotienting by the fresh rank-108
# image, every constant/linear/quadratic coefficient vector belongs to the
# rank-56 spectator image.  This explains the zero reduced Kuranishi system
# at this transition without any point enumeration.
inactive_columns = [list(column) for column in zip(*inactive_matrix)]
raw_polynomial_coefficients = [raw_constant]
raw_polynomial_coefficients.extend([
    [raw_linear[equation][column] for equation in range(168)]
    for column in range(active_count)])
raw_polynomial_coefficients.extend(raw_diagonal_vectors)
raw_polynomial_coefficients.extend(raw_cross_vectors)
raw_polynomial_coefficient_rank = matrix_rank(raw_polynomial_coefficients)
containment_augmented_rank = matrix_rank(
    inactive_columns + raw_polynomial_coefficients)
assert containment_augmented_rank == inactive_rank


def evaluate_reduced(active):
    values = list(reduced_constant)
    for equation in range(equation_count):
        for column, scalar in enumerate(active):
            values[equation] += reduced_linear[equation][column] * scalar
            values[equation] += reduced_diagonal[equation][column] * scalar * scalar
        for left, right, coeffs in reduced_cross:
            values[equation] += coeffs[equation] * active[left] * active[right]
        values[equation] %= 3
    return values


def solve_inactive(active):
    qpoly = jacobian_pair(T_base)
    T_partial = list(T_base)
    for scalar, direction in zip(active, directions[:active_count]):
        T_partial = [value + scalar * delta
                     for value, delta in zip(T_partial, direction)]
    qpoly = jacobian_pair(T_partial)
    raw_rhs = []
    for functional in fresh_left_kernel:
        value = 0
        for row, xy in enumerate(slots):
            affine = carry_constant[row]
            for column, scalar in enumerate(active):
                affine += scalar * carry_columns[column][row]
            value += functional[row] * (affine + coefficient(qpoly, xy))
        raw_rhs.append((-value) % 3)
    _, inactive, _ = rref_solve(inactive_matrix, raw_rhs)
    return inactive


def full_replay(active, inactive, finder):
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
    assert W is not None and len(fresh_kernel) == 74
    left_T, right_T = correction(T)
    left_W, right_W = correction(W)
    P = add(p5, sc(243, left_T), sc(3 ** 10, left_W))
    Q = add(q5, sc(243, right_T), sc(3 ** 10, right_W))
    determinant = add(jac(P, Q), sc(-1, ONE))
    assert all(coefficient(determinant, xy) % (3 ** 11) == 0
               for xy in slots)
    partial_y_degree_pair = (dydeg_mod(P, 3 ** 11),
                             dydeg_mod(Q, 3 ** 11))
    total_degree_pair = (tdeg_mod(P, 3 ** 11),
                         tdeg_mod(Q, 3 ** 11))
    assert max(total_degree_pair) <= 12
    return {
        "finder": finder,
        "active": active,
        "inactive": inactive,
        "T_mod729": [value % (3 ** 6) for value in T],
        "fresh_digit": W,
        "literal_integer_replay_mod177147_passed": True,
        "partial_y_degree_pair": list(partial_y_degree_pair),
        "total_degree_pair": list(total_degree_pair),
        "P_support": [[i, j, value] for (i, j), value in sorted(P.items())],
        "Q_support": [[i, j, value] for (i, j), value in sorted(Q.items())],
        "determinant_sha256": hashlib.sha256(
            repr(sorted(jac(P, Q).items())).encode()).hexdigest(),
    }


witness = None
finder_trials = []
trial_vectors = [[0] * active_count]
for index in range(active_count):
    for scalar in (1, 2):
        vector = [0] * active_count
        vector[index] = scalar
        trial_vectors.append(vector)
for trial_index, active in enumerate(trial_vectors):
    reduced = evaluate_reduced(active)
    if any(reduced):
        finder_trials.append([trial_index, "reduced_nonzero"])
        continue
    inactive = solve_inactive(active)
    if inactive is None:
        finder_trials.append([trial_index, "inactive_inconsistent"])
        continue
    witness = full_replay(active, inactive, "zero_or_weight_one")
    finder_trials.append([trial_index, "SAT"])
    break


def bv(value):
    return "#x" + format(value % 16, "x")


def mod3(term):
    return f"(bvurem {term} #x3)"


def scale3(value, term):
    value %= 3
    if value == 0:
        return "#x0"
    if value == 1:
        return term
    return mod3(f"(bvmul #x2 {term})")


def add3(terms):
    terms = [term for term in terms if term != "#x0"]
    if not terms:
        return "#x0"
    result = terms[0]
    for term in terms[1:]:
        result = mod3(f"(bvadd {result} {term})")
    return result


def evaluate_bv_encoding(active):
    """Independent integer emulation of the emitted four-bit BV gates."""
    values = []
    for equation in range(equation_count):
        terms = [reduced_constant[equation] % 3]
        for column in range(active_count):
            scalar = active[column]
            if reduced_linear[equation][column]:
                terms.append((reduced_linear[equation][column] * scalar) % 3)
            if reduced_diagonal[equation][column]:
                square = ((scalar * scalar) & 15) % 3
                terms.append((reduced_diagonal[equation][column] * square) % 3)
        for left, right, coeffs in reduced_cross:
            if coeffs[equation]:
                product = ((active[left] * active[right]) & 15) % 3
                terms.append((coeffs[equation] * product) % 3)
        accumulator = terms[0]
        for term in terms[1:]:
            assert 0 <= accumulator <= 2 and 0 <= term <= 2
            accumulator = ((accumulator + term) & 15) % 3
        values.append(accumulator)
    return values


# Degree-two design: zero, +/- basis, and all pair sums.  Equality here is a
# direct cross-check of every emitted BV arithmetic gate against the exact ANF
# evaluator; all intermediate four-bit products/sums are also range-checked.
encoding_design = [[0] * active_count]
for index in range(active_count):
    for scalar in (1, 2):
        vector = [0] * active_count
        vector[index] = scalar
        encoding_design.append(vector)
for left in range(active_count):
    for right in range(left + 1, active_count):
        vector = [0] * active_count
        vector[left] = vector[right] = 1
        encoding_design.append(vector)
for vector in encoding_design:
    assert evaluate_bv_encoding(vector) == evaluate_reduced(vector)


smt_path = Path(os.environ["SMT2_OUTPUT"])
with smt_path.open("w") as stream:
    stream.write("(set-logic QF_BV)\n(set-option :produce-models true)\n")
    for index in range(active_count):
        stream.write(f"(declare-fun a{index} () (_ BitVec 4))\n")
        stream.write(f"(assert (bvule a{index} #x2))\n")
    for equation in range(equation_count):
        terms = [bv(reduced_constant[equation])]
        for column in range(active_count):
            if reduced_linear[equation][column]:
                terms.append(scale3(reduced_linear[equation][column],
                                    f"a{column}"))
            if reduced_diagonal[equation][column]:
                square = mod3(f"(bvmul a{column} a{column})")
                terms.append(scale3(reduced_diagonal[equation][column], square))
        for left, right, values in reduced_cross:
            if values[equation]:
                product = mod3(f"(bvmul a{left} a{right})")
                terms.append(scale3(values[equation], product))
        stream.write(f"(assert (= {add3(terms)} #x0))\n")
    stream.write("(check-sat)\n(get-model)\n")

anf = {
    "constant": reduced_constant,
    "linear": reduced_linear,
    "diagonal": reduced_diagonal,
    "cross": reduced_cross,
}
anf_bytes = json.dumps(anf, sort_keys=True, separators=(",", ":")).encode()
Path(os.environ["ANF_OUTPUT"]).write_bytes(anf_bytes + b"\n")
monomial_columns = []
for equation in range(equation_count):
    monomial_columns.append([reduced_constant[equation]]
                            + reduced_linear[equation]
                            + reduced_diagonal[equation]
                            + [values[equation]
                               for _, _, values in reduced_cross])
coefficient_span_rank = matrix_rank(monomial_columns)

result = {
    "status": ("PASS-AS-B9-D12-QUADRATIC-3P11-SAT"
               if witness is not None
               else "PASS-AS-B9-D12-QUADRATIC-3P11-COMPILED"),
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_replay_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "slot_count": 276,
    "predecessor_dimension": 165,
    "fresh_variable_count": 182,
    "fresh_rank": fresh_rank,
    "fresh_cokernel_dimension": len(fresh_left_kernel),
    "active_quadratic_dimension": active_count,
    "linear_spectator_dimension": inactive_count,
    "spectator_linear_rank": inactive_rank,
    "spectator_kernel_dimension": inactive_count - inactive_rank,
    "predecessor_projection_dimension": (
        active_count + inactive_count - inactive_rank),
    "fresh_kernel_dimension": 182 - fresh_rank,
    "full_lift_family_dimension": (
        active_count + inactive_count - inactive_rank + 182 - fresh_rank),
    "full_lift_family_cardinality": "3^183",
    "raw_polynomial_coefficient_rank": raw_polynomial_coefficient_rank,
    "containment_augmented_rank": containment_augmented_rank,
    "all_polynomial_coefficients_in_spectator_image": True,
    "post_elimination_equation_count": equation_count,
    "quadratic_cross_support_count": len(reduced_cross),
    "coefficient_span_rank": coefficient_span_rank,
    "predivided_carry_divisor": power,
    "outer_correction_scale": 243,
    "full_target_modulus": 3 ** 11,
    "bv_encoding_crosscheck_design_size": len(encoding_design),
    "bv_encoding_crosscheck_passed": True,
    "anf_sha256": hashlib.sha256(anf_bytes + b"\n").hexdigest(),
    "smt2_sha256": hashlib.sha256(smt_path.read_bytes()).hexdigest(),
    "finder_trials": finder_trials,
    "witness": witness,
    "scope": "full 165D mod3^10 family over one fixed B9 mod243 point",
    "refusal_scope": [
        "no modulus3^12 or deeper/all-depth branch",
        "not the complete earlier mod243 fibre",
        "no characteristic-zero point, counterexample, maximum12 theorem, or JC2",
    ],
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(saved_output).write_bytes(encoded + b"\n")
print("active_inactive", active_count, inactive_count)
print("fresh_rank_cokernel", fresh_rank, len(fresh_left_kernel))
print("spectator_rank_reduced_equations", inactive_rank, equation_count)
print("cross_support_coefficient_rank", len(reduced_cross), coefficient_span_rank)
print("finder", None if witness is None else witness["finder"])
print("anf_sha256", result["anf_sha256"])
print("smt2_sha256", result["smt2_sha256"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
