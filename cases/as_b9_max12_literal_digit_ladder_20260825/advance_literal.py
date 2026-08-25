#!/usr/bin/env python3
"""Advance one literal fixed-D12 B9 map by one ternary determinant digit."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


Poly = dict[tuple[int, int], int]


def clean(poly: Poly) -> Poly:
    return {xy: value for xy, value in poly.items() if value}


def add(*polys: Poly) -> Poly:
    answer: Poly = {}
    for poly in polys:
        for xy, value in poly.items():
            answer[xy] = answer.get(xy, 0) + value
    return clean(answer)


def scale(scalar: int, poly: Poly) -> Poly:
    return clean({xy: scalar * value for xy, value in poly.items()})


def mul(left: Poly, right: Poly) -> Poly:
    answer: Poly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            answer[xy] = answer.get(xy, 0) + a * b
    return clean(answer)


def deriv(poly: Poly, axis: int) -> Poly:
    answer: Poly = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[xy] = answer.get(xy, 0) + exponent * value
    return clean(answer)


def jac(left: Poly, right: Poly) -> Poly:
    return add(mul(deriv(left, 0), deriv(right, 1)),
               scale(-1, mul(deriv(left, 1), deriv(right, 0))))


def coefficient(poly: Poly, xy):
    return poly.get(xy, 0)


def rref(matrix, rhs):
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


input_path = Path(os.environ["INPUT_JSON"])
payload = input_path.read_bytes()
input_sha = hashlib.sha256(payload).hexdigest()
assert input_sha == os.environ["EXPECTED_INPUT_SHA256"]
source = json.loads(payload)
modulus = int(os.environ["INPUT_MODULUS"])
assert modulus >= 3 and modulus % 3 == 0


def parse_support(name):
    return {(i, j): value for i, j, value in source[name]}


P, Q = parse_support("P_support"), parse_support("Q_support")
assert max(i + j for i, j in P) <= 12
assert max(i + j for i, j in Q) <= 12
assert max(j for i, j in P) <= 12 and max(j for i, j in Q) <= 12
support = [(i, degree - i) for degree in range(13)
           for i in range(degree + 1)]
slots = [(i, degree - i) for degree in range(23)
         for i in range(degree + 1)]
ONE = {(0, 0): 1}
D = add(jac(P, Q), scale(-1, ONE))
assert all(coefficient(D, xy) % modulus == 0 for xy in slots)
base = [(coefficient(D, xy) // modulus) % 3 for xy in slots]
assert any(base), "input already survives the requested next modulus"


def correction(values):
    left = {xy: values[index] for index, xy in enumerate(support)
            if values[index]}
    right = {xy: values[91 + index] for index, xy in enumerate(support)
             if values[91 + index]}
    return left, right


columns = []
for column in range(182):
    values = [0] * 182
    values[column] = 1
    left, right = correction(values)
    current = add(jac(add(P, scale(modulus, left)),
                      add(Q, scale(modulus, right))), scale(-1, jac(P, Q)))
    assert all(coefficient(current, xy) % modulus == 0 for xy in slots)
    columns.append([(coefficient(current, xy) // modulus) % 3
                    for xy in slots])
matrix = [[columns[column][row] for column in range(182)]
          for row in range(276)]
rank, particular, kernel = rref(matrix, [(-value) % 3 for value in base])

result = {
    "status": ("PASS-AS-B9-D12-LITERAL-NEXT-DIGIT-SAT"
               if particular is not None
               else "PASS-AS-B9-D12-LITERAL-NEXT-DIGIT-UNSAT"),
    "input_sha256": input_sha,
    "input_modulus": modulus,
    "output_modulus": 3 * modulus,
    "slot_count": len(slots),
    "variable_count": 182,
    "rank": rank,
    "consistent": particular is not None,
    "kernel_dimension": len(kernel) if particular is not None else None,
    "input_fails_output_modulus": True,
    "matrix_sha256": hashlib.sha256(json.dumps(
        matrix, separators=(",", ":")).encode()).hexdigest(),
    "rhs_sha256": hashlib.sha256(json.dumps(
        base, separators=(",", ":")).encode()).hexdigest(),
    "scope": "one literal fixed-D12 B9 branch, one ternary digit",
    "refusal_scope": [
        "not the complete preceding affine fibre",
        "no deeper/all-depth or characteristic-zero point",
        "no counterexample, maximum12 theorem, or JC2",
    ],
}

if particular is not None:
    left, right = correction(particular)
    next_P = add(P, scale(modulus, left))
    next_Q = add(Q, scale(modulus, right))
    next_D = add(jac(next_P, next_Q), scale(-1, ONE))
    assert all(coefficient(next_D, xy) % (3 * modulus) == 0
               for xy in slots)
    result.update({
        "fresh_digit": particular,
        "literal_integer_replay_passed": True,
        "P_support": [[i, j, value]
                      for (i, j), value in sorted(next_P.items())],
        "Q_support": [[i, j, value]
                      for (i, j), value in sorted(next_Q.items())],
        "determinant_sha256": hashlib.sha256(
            repr(sorted(jac(next_P, next_Q).items())).encode()).hexdigest(),
        "degrees_total": [max(i + j for i, j in next_P),
                          max(i + j for i, j in next_Q)],
        "degrees_y": [max(j for i, j in next_P),
                      max(j for i, j in next_Q)],
    })

encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded + b"\n")
print("moduli", modulus, 3 * modulus)
print("rank", rank)
print("consistent", particular is not None)
print("kernel_dimension", len(kernel) if particular is not None else None)
print("matrix_sha256", result["matrix_sha256"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
