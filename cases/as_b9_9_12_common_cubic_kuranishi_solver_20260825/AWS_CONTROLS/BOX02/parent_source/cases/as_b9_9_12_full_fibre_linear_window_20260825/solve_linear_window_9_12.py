#!/usr/bin/env python3
"""Complete B9 (9,12) linear Bockstein window through modulus 3^10."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_b9_9_12_full_output_mod729_20260825"
          / "solve_9_12_mod729.py")
EXPECTED_PARENT = (
    "d0c6fd4b62350b0d115aefd60846613ca7484dd3e5bdafdcd9339316b944a848")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
saved_output = os.environ["OUTPUT_JSON"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
scope = {"__file__": str(PARENT), "__name__": "__b9_9_12_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output

parent = scope["ns"]
allowed = list(scope["allowed"])
support, slots = list(parent["support"]), list(parent["slots"])
p5, q5, d5, ONE = parent["p5"], parent["q5"], parent["d5"], parent["ONE"]
add, sc, jac = parent["add"], parent["sc"], parent["jac"]
coefficient = parent["coefficient"]
tdeg, dydeg = parent["tdeg"], parent["dydeg"]
rref_with_left = parent["rref_with_left"]


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def correction(values):
    assert len(values) == 146
    full = [0] * 182
    for index, value in zip(allowed, values):
        full[index] = value
    return parent["correction"](full)


def solve(matrix, rhs):
    rank, particular, kernel, contradictions = rref_with_left(matrix, rhs)
    return rank, particular, kernel


def matrix_rank(vectors):
    if not vectors:
        return 0
    transposed = [list(column) for column in zip(*vectors)]
    value, _, _ = solve(transposed, [0] * len(transposed))
    return value


residual5 = add(d5, sc(-1, ONE))
base_integer = []
for xy in slots:
    value = coefficient(residual5, xy)
    assert value % 243 == 0
    base_integer.append(value // 243)

columns_integer = []
for column in range(146):
    values = [0] * 146
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
matrix_integer = [[columns_integer[column][row] for column in range(146)]
                  for row in range(276)]
A3 = [[value % 3 for value in row] for row in matrix_integer]

# Exact source control: only P-Q pairs contribute a quadratic correction,
# always with the outer factor 243^2=3^10.
pair_controls = 0
for left_index in range(55):
    for right_index in range(55, 146):
        values = [0] * 146
        values[left_index] = values[right_index] = 1
        left, right = correction(values)
        delta = add(jac(add(p5, sc(243, left)), add(q5, sc(243, right))),
                    sc(-1, d5))
        for row, xy in enumerate(slots):
            remainder = coefficient(delta, xy) // 243 - (
                matrix_integer[row][left_index]
                + matrix_integer[row][right_index])
            assert remainder % 243 == 0
        pair_controls += 1
assert pair_controls == 55 * 91


def replay(T, modulus):
    left, right = correction(T)
    P = add(p5, sc(243, left))
    Q = add(q5, sc(243, right))
    determinant = add(jac(P, Q), sc(-1, ONE))
    assert all(coefficient(determinant, xy) % modulus == 0 for xy in slots)
    assert tdeg(P) <= 9 and dydeg(P) <= 9
    assert tdeg(Q) <= 12 and dydeg(Q) <= 12
    return P, Q, determinant


stages = []
base_T = [0] * 146
directions = []
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
    rank, particular, kernel = solve(
        matrix, [(-value) % 3 for value in carry])
    stage = {
        "k": k,
        "determinant_modulus": 3 ** (5 + k),
        "rank": rank,
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
        direction = [0] * 146
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
    base_T, directions = new_base, new_directions

result = {
    "status": "PASS-AS-B9-9-12-FULL-FIBRE-LINEAR-WINDOW",
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_replay_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "slot_count": 276,
    "coefficient_count": 146,
    "pair_control_count": pair_controls,
    "quadratic_coefficient_valuation": 10,
    "quadratic_enters_divided_carry_for_transition": "3^10_to_3^11",
    "stages": stages,
    "all_requested_stages_consistent": len(stages) == 5 and all(
        stage["consistent"] for stage in stages),
    "matrix_integer_sha256": hashlib.sha256(json.dumps(
        matrix_integer, separators=(",", ":")).encode()).hexdigest(),
    "scope": "full fixed-(9,12) affine families over one B9 mod243 point",
    "refusal_scope": [
        "not the complete earlier mod243 fibre",
        "no transition 3^10 to 3^11 or all-depth branch",
        "no characteristic-zero point, maximum12 theorem, counterexample, or JC2",
    ],
}
if result["all_requested_stages_consistent"]:
    P, Q, determinant = replay(base_T, 3 ** 10)
    result.update({
        "final_T": [value % (3 ** 5) for value in base_T],
        "final_solution_exponent": len(directions),
        "degrees_total": [tdeg(P), tdeg(Q)],
        "degrees_y": [dydeg(P), dydeg(Q)],
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
