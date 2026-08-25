#!/usr/bin/env python3
"""Complete fixed-D12 B9 output-digit solve from mod243 to mod729."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = ROOT / "cases/as_b9_max12_w5_survivor_aws_20260825/replay.py"
EXPECTED_PARENT = (
    "f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
ns = {"__file__": str(PARENT), "__name__": "__b9_mod729_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), ns)

add, sc, jac, modp = ns["add"], ns["sc"], ns["jac"], ns["modp"]
p5, q5, ONE = ns["p5"], ns["q5"], ns["ONE"]
dydeg, tdeg = ns["dydeg"], ns["tdeg"]

support = [(i, degree - i) for degree in range(13)
           for i in range(degree + 1)]
slots = [(i, degree - i) for degree in range(23)
         for i in range(degree + 1)]
assert len(support) == 91 and len(slots) == 276


def coefficient(poly, xy):
    return poly.get(xy, 0)


def correction(values):
    assert len(values) == 182
    left = {xy: values[index] for index, xy in enumerate(support)
            if values[index]}
    right = {xy: values[91 + index] for index, xy in enumerate(support)
             if values[91 + index]}
    return left, right


def candidate(values):
    left, right = correction(values)
    return add(p5, sc(243, left)), add(q5, sc(243, right))


def rref_with_left(matrix, rhs):
    rows = len(matrix)
    columns = len(matrix[0])
    work = [[value % 3 for value in row] + [target % 3]
            for row, target in zip(matrix, rhs)]
    left = [[1 if i == j else 0 for j in range(rows)]
            for i in range(rows)]
    pivots = []
    pivot_row = 0
    for column in range(columns):
        chosen = next((row for row in range(pivot_row, rows)
                       if work[row][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        left[pivot_row], left[chosen] = left[chosen], left[pivot_row]
        if work[pivot_row][column] == 2:
            work[pivot_row] = [(2 * value) % 3
                               for value in work[pivot_row]]
            left[pivot_row] = [(2 * value) % 3
                               for value in left[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            scalar = work[row][column]
            work[row] = [(a - scalar * b) % 3
                         for a, b in zip(work[row], work[pivot_row])]
            left[row] = [(a - scalar * b) % 3
                         for a, b in zip(left[row], left[pivot_row])]
        pivots.append(column)
        pivot_row += 1
    contradictions = []
    for row in range(rows):
        if not any(work[row][:-1]) and work[row][-1]:
            inverse = 1 if work[row][-1] == 1 else 2
            witness = [(inverse * value) % 3 for value in left[row]]
            assert all(sum(witness[i] * matrix[i][j] for i in range(rows))
                       % 3 == 0 for j in range(columns))
            assert sum(witness[i] * rhs[i] for i in range(rows)) % 3 == 1
            contradictions.append(witness)
    if contradictions:
        return len(pivots), None, [], contradictions
    particular = [0] * columns
    for row, column in enumerate(pivots):
        particular[column] = work[row][-1]
    free = [column for column in range(columns) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-work[row][free_column]) % 3
        kernel.append(vector)
    return len(pivots), particular, kernel, []


d5 = jac(p5, q5)
residual = add(d5, sc(-1, ONE))
assert all(coefficient(residual, xy) % 243 == 0 for xy in slots)
base = [(coefficient(residual, xy) // 243) % 3 for xy in slots]
assert any(base), "parent unexpectedly already lifts modulo729"

columns = []
for column in range(182):
    values = [0] * 182
    values[column] = 1
    p, q = candidate(values)
    delta = add(jac(p, q), sc(-1, d5))
    assert all(coefficient(delta, xy) % 243 == 0 for xy in slots)
    columns.append([(coefficient(delta, xy) // 243) % 3
                    for xy in slots])
matrix = [[columns[column][row] for column in range(182)]
          for row in range(276)]
rank, particular, kernel, contradictions = rref_with_left(
    matrix, [(-value) % 3 for value in base])

result = {
    "status": ("PASS-AS-B9-D12-FULL-OUTPUT-MOD729-SAT"
               if particular is not None
               else "PASS-AS-B9-D12-FULL-OUTPUT-MOD729-UNSAT"),
    "parent_source_sha256": EXPECTED_PARENT,
    "slot_count": len(slots),
    "variable_count": 182,
    "rank": rank,
    "consistent": particular is not None,
    "kernel_dimension": len(kernel) if particular is not None else None,
    "parent_fails_mod729": True,
    "matrix_sha256": hashlib.sha256(json.dumps(
        matrix, separators=(",", ":")).encode()).hexdigest(),
    "rhs_sha256": hashlib.sha256(json.dumps(
        base, separators=(",", ":")).encode()).hexdigest(),
    "scope": "complete fixed-D12 fresh output digit over one B9 mod243 point",
    "refusal_scope": [
        "not the complete earlier fibre",
        "no modulus2187 or deeper/all-depth branch",
        "no characteristic-zero map, counterexample, maximum12 theorem, or JC2",
    ],
}

if particular is not None:
    p6, q6 = candidate(particular)
    d6 = jac(p6, q6)
    all_slots = sorted(set(slots) | set(d6))
    assert all(sum(xy) <= 22 for xy in all_slots)
    assert all(coefficient(add(d6, sc(-1, ONE)), xy) % 729 == 0
               for xy in all_slots)
    assert modp(p6, 3) == modp(ns["p0"], 3)
    assert modp(q6, 3) == modp(ns["q0"], 3)
    assert tdeg(p6) <= 12 and tdeg(q6) <= 12
    assert dydeg(p6) <= 12 and dydeg(q6) <= 12
    result.update({
        "literal_integer_replay_mod729_passed": True,
        "fresh_digit": particular,
        "determinant_sha256": hashlib.sha256(
            repr(sorted(d6.items())).encode()).hexdigest(),
        "P_support": [[i, j, value] for (i, j), value in sorted(p6.items())],
        "Q_support": [[i, j, value] for (i, j), value in sorted(q6.items())],
        "degrees_total": [tdeg(p6), tdeg(q6)],
        "degrees_y": [dydeg(p6), dydeg(q6)],
    })
else:
    witness = contradictions[0]
    result.update({
        "left_null_witness": witness,
        "left_null_support": [[slots[index][0], slots[index][1], value]
                              for index, value in enumerate(witness) if value],
        "left_null_pairing": 1,
    })

encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded + b"\n")
print("rows_columns", len(slots), 182)
print("rank", rank)
print("consistent", particular is not None)
print("kernel_dimension", len(kernel) if particular is not None else None)
print("matrix_sha256", result["matrix_sha256"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
print(result["status"])
