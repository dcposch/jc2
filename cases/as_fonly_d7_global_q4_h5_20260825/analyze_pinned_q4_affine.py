#!/usr/bin/env python3
"""Exact affine/cokernel certificate for one pinned Q5 -> Q4 transition.

This script source-pins and executes the direct integer Q5 replay, then
evaluates the newly licensed degree-five digit H5,J5 at zero and at an exact
affine design over F_3.  It emits a left-null certificate for the displayed
Q4 source row plus the recomputed terminal rows of degrees 12 through 7.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_h6_replay_erratum_20260825"
          / "replay_global_q5_h6_v2.py")
EXPECTED_PARENT_SHA = (
    "41e0e74ec4d318bdd33242dcb9053ce53572470570ab5d54f1431184eb789ffa")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

# The parent writes its own replay JSON.  Preserve it as part of the source
# chain rather than bypassing any of its assertions.
parent_output = Path(os.environ["PARENT_OUTPUT_JSON"])
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
namespace = {"__file__": str(PARENT), "__name__": "__q4_affine_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), namespace)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

scope = namespace["scope"]
while "homogeneous_numeric" not in scope:
    scope = scope["scope"]
homogeneous_numeric = scope["homogeneous_numeric"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]
G = scope["G"]
source_data = scope["source_data"]
Rmix = scope["Rmix"]
old_carry = scope["carry"]
P5 = scope["P5"]
Q5 = scope["Q5"]


def fourth_digit_cross(H, J):
    return nadd(nmul(source_data["A"], nderivative(J, 1)),
                nmul(nderivative(H, 0), source_data["vy"]),
                nscale(-1, nmul(source_data["uy"], nderivative(J, 0))),
                nscale(-1, nmul(nderivative(H, 1), source_data["vx"])))


def displayed_rows(values):
    assert len(values) == 12
    H5 = homogeneous_numeric(5, values[:6])
    J5 = homogeneous_numeric(5, values[6:])
    q4 = row(nadd(G(4), nderivative(H5, 0), nderivative(J5, 1)), 4)
    carry = nadd(old_carry, fourth_digit_cross(H5, J5))
    terminal_by_degree = {}
    terminal = []
    for degree in range(7, 13):
        terminal_by_degree[degree] = row(
            nadd(divide_exact(G(degree), 3),
                 degree_part(carry, degree),
                 degree_part(Rmix, degree)), degree)
        terminal.extend(terminal_by_degree[degree])

    # Literal integer determinant reconstruction is independent of the
    # recursive source formulas.  It fixes both orientation and quotient.
    P4 = nadd(P5, nscale(81, H5))
    Q4 = nadd(Q5, nscale(81, J5))
    det_minus_one = nadd(
        nmul(nderivative(P4, 0), nderivative(Q4, 1)),
        nscale(-1, nmul(nderivative(P4, 1), nderivative(Q4, 0))),
        {(0, 0): -1})
    literal_q4 = row(divide_exact(degree_part(det_minus_one, 4), 81), 4)
    assert literal_q4 == q4
    literal_terminal = {
        degree: row(divide_exact(degree_part(det_minus_one, degree), 243),
                    degree)
        for degree in range(7, 13)
    }
    assert literal_terminal == terminal_by_degree
    result = [value % 3 for value in q4 + terminal]
    assert len(result) == 68
    return result


def rank_mod3(rows):
    if not rows:
        return 0
    matrix = [[entry % 3 for entry in values] for values in rows]
    row_index = 0
    for column in range(len(matrix[0])):
        pivot = next((index for index in range(row_index, len(matrix))
                      if matrix[index][column]), None)
        if pivot is None:
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        inverse = 1 if matrix[row_index][column] == 1 else 2
        matrix[row_index] = [(inverse * entry) % 3
                             for entry in matrix[row_index]]
        for index in range(len(matrix)):
            if index == row_index or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [(left - factor * right) % 3
                             for left, right in
                             zip(matrix[index], matrix[row_index])]
        row_index += 1
        if row_index == len(matrix):
            break
    return row_index


def inconsistent(indices, coefficients, constant):
    matrix = [[coefficients[index][column] for column in range(12)]
              for index in indices]
    augmented = [values + [constant[index]]
                 for values, index in zip(matrix, indices)]
    return rank_mod3(augmented) > rank_mod3(matrix)


zero = [0] * 12
constant = displayed_rows(zero)
columns = []
for variable in range(12):
    basis = [0] * 12
    basis[variable] = 1
    values = displayed_rows(basis)
    columns.append([(value - base) % 3
                    for value, base in zip(values, constant)])
coefficients = [[columns[column][row_index] for column in range(12)]
                for row_index in range(68)]

# Exact affine-design checks.  These cover scalar multiplication and every
# mixed pair; the source expression itself contains the new digit linearly.
for variable in range(12):
    test = [0] * 12
    test[variable] = 2
    expected = [(constant[index] + 2 * coefficients[index][variable]) % 3
                for index in range(68)]
    assert displayed_rows(test) == expected
for left in range(12):
    for right in range(left + 1, 12):
        test = [0] * 12
        test[left] = test[right] = 1
        expected = [(constant[index] + coefficients[index][left]
                     + coefficients[index][right]) % 3
                    for index in range(68)]
        assert displayed_rows(test) == expected

rank = rank_mod3(coefficients)
augmented_rank = rank_mod3([values + [base]
                            for values, base in zip(coefficients, constant)])
assert augmented_rank == rank + 1

# Greedily shrink to an irredundant inconsistent row subset, then row-reduce
# while tracking row operations to recover lambda M=0, lambda b=1.
support = list(range(68))
changed = True
while changed:
    changed = False
    for index in support.copy():
        trial = [entry for entry in support if entry != index]
        if inconsistent(trial, coefficients, constant):
            support = trial
            changed = True

work = [coefficients[index] + [constant[index]] for index in support]
transform = [[1 if i == j else 0 for j in range(len(support))]
             for i in range(len(support))]
pivot_row = 0
for column in range(12):
    pivot = next((index for index in range(pivot_row, len(work))
                  if work[index][column]), None)
    if pivot is None:
        continue
    work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
    transform[pivot_row], transform[pivot] = (
        transform[pivot], transform[pivot_row])
    inverse = 1 if work[pivot_row][column] == 1 else 2
    work[pivot_row] = [(inverse * entry) % 3
                       for entry in work[pivot_row]]
    transform[pivot_row] = [(inverse * entry) % 3
                            for entry in transform[pivot_row]]
    for index in range(len(work)):
        if index == pivot_row or not work[index][column]:
            continue
        factor = work[index][column]
        work[index] = [(left - factor * right) % 3
                       for left, right in zip(work[index], work[pivot_row])]
        transform[index] = [(left - factor * right) % 3
                            for left, right in
                            zip(transform[index], transform[pivot_row])]
    pivot_row += 1

witness_row = next(index for index, values in enumerate(work)
                   if not any(values[:12]) and values[12])
inverse = 1 if work[witness_row][12] == 1 else 2
local_lambda = [(inverse * entry) % 3
                for entry in transform[witness_row]]
certificate = [0] * 68
for index, value in zip(support, local_lambda):
    certificate[index] = value
assert all(sum(certificate[index] * coefficients[index][column]
               for index in range(68)) % 3 == 0
           for column in range(12))
assert sum(certificate[index] * constant[index]
           for index in range(68)) % 3 == 1


def label(index):
    if index < 5:
        return {"family": "Q4", "degree": 4, "slot": index}
    offset = index - 5
    for degree in range(7, 13):
        if offset < degree + 1:
            return {"family": "terminal", "degree": degree,
                    "slot": offset}
        offset -= degree + 1
    raise AssertionError(index)


parent_bytes = parent_output.read_bytes()
result = {
    "status": "PASS-PINNED-Q4-AFFINE-COKERNEL-CERTIFICATE",
    "scope": ("single pinned base0513 Q5 parent; displayed Q4 source row "
              "and terminal degrees 12 through 7 only"),
    "parent_replay_sha256": EXPECTED_PARENT_SHA,
    "parent_output_sha256": hashlib.sha256(parent_bytes).hexdigest(),
    "parent_stdout_sha256": hashlib.sha256(
        parent_stdout.getvalue().encode()).hexdigest(),
    "matrix_shape": [68, 12],
    "matrix_rank": rank,
    "augmented_rank": augmented_rank,
    "constant_vector": constant,
    "coefficient_matrix": coefficients,
    "affine_design": {
        "zero": True,
        "basis": 12,
        "double_basis": 12,
        "pair_sums": 66,
    },
    "certificate": [
        {"row_index": index, "coefficient": certificate[index], **label(index)}
        for index in range(68) if certificate[index]
    ],
    "certificate_pairing": 1,
    "irredundant_support": all(
        not inconsistent([entry for entry in support if entry != index],
                         coefficients, constant)
        for index in support),
    "q4_only_ranks": [rank_mod3(coefficients[:5]),
                       rank_mod3([values + [base] for values, base in
                                  zip(coefficients[:5], constant[:5])])],
    "terminal_only_ranks": [rank_mod3(coefficients[5:]),
                             rank_mod3([values + [base] for values, base in
                                        zip(coefficients[5:], constant[5:])])],
    "refusal_scope": [
        "not the full Q5 fibre",
        "not Q4 through Q0 restoration",
        "not a complete determinant-one map modulo 243",
        "not a no-lift or Jacobian-conjecture inference",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("matrix_shape", 68, 12)
print("ranks", rank, augmented_rank)
print("certificate_support", len(result["certificate"]))
for entry in result["certificate"]:
    print("certificate_row", entry)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-PINNED-Q4-AFFINE-COKERNEL-CERTIFICATE")
