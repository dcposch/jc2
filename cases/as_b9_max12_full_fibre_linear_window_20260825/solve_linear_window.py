#!/usr/bin/env python3
"""Exact full-family Bockstein window for B9 from 3^6 through 3^10."""

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
ns = {"__file__": str(PARENT), "__name__": "__b9_window_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), ns)
os.environ["OUTPUT_JSON"] = saved_output

add, sc, jac = ns["add"], ns["sc"], ns["jac"]
p5, q5, d5, ONE = ns["p5"], ns["q5"], ns["d5"], ns["ONE"]
support, slots = list(ns["support"]), list(ns["slots"])
correction, coefficient = ns["correction"], ns["coefficient"]


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
    delta = add(jac(add(p5, sc(243, left)), add(q5, sc(243, right))),
                sc(-1, d5))
    current = []
    for xy in slots:
        value = coefficient(delta, xy)
        assert value % 243 == 0
        current.append(value // 243)
    columns_integer.append(current)
matrix_integer = [[columns_integer[column][row] for column in range(182)]
                  for row in range(276)]
A3 = [[value % 3 for value in row] for row in matrix_integer]

# Every P/Q fresh pair contributes exactly 243^2 times its Jacobian.  This is
# the source control for the entire linear window.
pair_controls = 0
for left_index in range(91):
    for right_index in range(91, 182):
        values = [0] * 182
        values[left_index] = values[right_index] = 1
        left, right = correction(values)
        delta = add(jac(add(p5, sc(243, left)), add(q5, sc(243, right))),
                    sc(-1, d5))
        linear = [base_integer[row] + matrix_integer[row][left_index]
                  + matrix_integer[row][right_index]
                  for row in range(276)]
        for row, xy in enumerate(slots):
            remainder = coefficient(delta, xy) // 243 - (
                matrix_integer[row][left_index]
                + matrix_integer[row][right_index])
            assert remainder % 243 == 0
        pair_controls += 1
assert pair_controls == 91 * 91


def replay(T, modulus):
    left, right = correction(T)
    P = add(p5, sc(243, left))
    Q = add(q5, sc(243, right))
    determinant = add(jac(P, Q), sc(-1, ONE))
    assert all(coefficient(determinant, xy) % modulus == 0 for xy in slots)
    assert max(i + j for i, j in P) <= 12
    assert max(i + j for i, j in Q) <= 12
    assert max(j for i, j in P) <= 12 and max(j for i, j in Q) <= 12
    return P, Q, determinant


stages = []
base_T = [0] * 182
directions = []
previous_particular_T = None
for k in range(1, 6):
    power = 3 ** (k - 1)
    carry = []
    direction_carries = [[] for _ in directions]
    for row in range(276):
        numerator = base_integer[row] + dot(matrix_integer[row], base_T)
        assert numerator % power == 0
        carry.append((numerator // power) % 3)
        for column, direction in enumerate(directions):
            numerator = dot(matrix_integer[row], direction)
            assert numerator % power == 0
            direction_carries[column].append((numerator // power) % 3)
    matrix = [[direction_carries[column][row]
               for column in range(len(directions))] + A3[row]
              for row in range(276)]
    stage_rank, particular, kernel = rref_solve(
        matrix, [(-value) % 3 for value in carry])
    stage = {
        "k": k,
        "determinant_modulus": 3 ** (5 + k),
        "rank": stage_rank,
        "consistent": particular is not None,
        "kernel_dimension": len(kernel) if particular is not None else None,
        "predecessor_dimension": len(directions),
    }
    if particular is None:
        stages.append(stage)
        break
    projected = [vector[:len(directions)] for vector in kernel]
    projection_dimension = matrix_rank(projected) if directions else 0
    stage["liftable_predecessor_dimension"] = projection_dimension
    new_base = list(base_T)
    for scalar, direction in zip(particular[:len(directions)], directions):
        new_base = [value + scalar * delta
                    for value, delta in zip(new_base, direction)]
    new_base = [value + power * digit for value, digit in zip(
        new_base, particular[len(directions):])]
    new_directions = []
    for vector in kernel:
        direction = [0] * 182
        for scalar, old_direction in zip(vector[:len(directions)], directions):
            direction = [value + scalar * delta
                         for value, delta in zip(direction, old_direction)]
        direction = [value + power * digit for value, digit in zip(
            direction, vector[len(directions):])]
        new_directions.append(direction)
    modulus = 3 ** (5 + k)
    P, Q, determinant = replay(new_base, modulus)
    stage.update({
        "literal_integer_replay_passed": True,
        "particular_T_sha256": hashlib.sha256(json.dumps(
            new_base, separators=(",", ":")).encode()).hexdigest(),
        "determinant_sha256": hashlib.sha256(
            repr(sorted(add(determinant, ONE).items())).encode()).hexdigest(),
    })
    stages.append(stage)
    previous_particular_T = base_T
    base_T, directions = new_base, new_directions

result = {
    "status": "PASS-AS-B9-D12-FULL-FIBRE-LINEAR-WINDOW",
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_replay_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "slot_count": 276,
    "coefficient_count": 182,
    "pair_control_count": pair_controls,
    "quadratic_coefficient_valuation": 10,
    "quadratic_invisible_modulo_3_power_through": 10,
    "quadratic_enters_divided_carry_for_transition": "3^10_to_3^11",
    "stages": stages,
    "all_requested_stages_consistent": len(stages) == 5 and all(
        stage["consistent"] for stage in stages),
    "matrix_integer_sha256": hashlib.sha256(json.dumps(
        matrix_integer, separators=(",", ":")).encode()).hexdigest(),
    "scope": "full affine fixed-D12 families over one fixed B9 mod243 point",
    "refusal_scope": [
        "not the complete earlier mod243 fibre",
        "no transition from 3^10 to 3^11 or all-depth branch",
        "no characteristic-zero point, counterexample, maximum12 theorem, or JC2",
    ],
}
if result["all_requested_stages_consistent"]:
    P, Q, determinant = replay(base_T, 3 ** 10)
    result.update({
        "final_T": [value % (3 ** 5) for value in base_T],
        "final_solution_exponent": len(directions),
        "P_support": [[i, j, value] for (i, j), value in sorted(P.items())],
        "Q_support": [[i, j, value] for (i, j), value in sorted(Q.items())],
        "final_determinant_sha256": hashlib.sha256(
            repr(sorted(add(determinant, ONE).items())).encode()).hexdigest(),
    })

encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(saved_output).write_bytes(encoded + b"\n")
for stage in stages:
    print("stage", stage["k"], stage["determinant_modulus"], stage["rank"],
          stage["kernel_dimension"],
          stage.get("liftable_predecessor_dimension"))
print("pair_controls", pair_controls)
print("all_consistent", result["all_requested_stages_consistent"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
