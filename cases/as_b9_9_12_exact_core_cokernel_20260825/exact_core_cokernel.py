#!/usr/bin/env python3
"""Exact FLINT/SNF and rational-cokernel diagnostic for normalized B9."""

from __future__ import annotations

import contextlib
import gzip
import hashlib
import io
import json
import math
import os
from pathlib import Path

import flint
from flint import fmpq_mat, fmpz_mat


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_b9_9_12_full_fibre_linear_window_20260825"
          / "solve_linear_window_9_12.py")
EXPECTED_PARENT = (
    "fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT
saved_output = os.environ["OUTPUT_JSON"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
scope = {"__file__": str(PARENT), "__name__": "__b9_9_12_core_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output

A_rows = [[int(value) for value in row] for row in scope["matrix_integer"]]
b = [int(value) for value in scope["base_integer"]]
slots = list(scope["slots"])
assert len(A_rows) == len(b) == len(slots) == 276
assert all(len(row) == 146 for row in A_rows)


def sha_json(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def primitive(vector):
    divisor = 0
    for value in vector:
        divisor = math.gcd(divisor, abs(value))
    assert divisor
    answer = [value // divisor for value in vector]
    first = next(value for value in answer if value)
    if first < 0:
        answer = [-value for value in answer]
    return answer


def kernel_basis(matrix):
    raw, nullity = matrix.nullspace()
    basis = []
    for column in range(nullity):
        basis.append(primitive([int(raw[row, column])
                                for row in range(raw.nrows())]))
    return basis


def vp3(value):
    if not value:
        return None
    value = abs(value)
    answer = 0
    while value % 3 == 0:
        value //= 3
        answer += 1
    return answer


A = fmpz_mat(A_rows)
rank = A.rank()
right = kernel_basis(A)
left = kernel_basis(A.transpose())
assert len(right) == 146 - rank
assert len(left) == 276 - rank
for vector in right:
    assert all(sum(row[column] * vector[column] for column in range(146)) == 0
               for row in A_rows)
for vector in left:
    assert all(sum(vector[row] * A_rows[row][column] for row in range(276)) == 0
               for column in range(146))

smith = A.snf()
smith_diagonal = [abs(int(smith[index, index]))
                  for index in range(min(smith.nrows(), smith.ncols()))]
smith_nonzero = [value for value in smith_diagonal if value]
assert len(smith_nonzero) == rank
smith_v3 = [vp3(value) for value in smith_nonzero]
smith_v3_histogram = {}
for value in smith_v3:
    key = str(value)
    smith_v3_histogram[key] = smith_v3_histogram.get(key, 0) + 1

augmented_rows = [row + [-b[row_index]]
                  for row_index, row in enumerate(A_rows)]
augmented = fmpq_mat(augmented_rows)
augmented_rank = augmented.rank()
rational_solvable = augmented_rank == rank
particular = None
particular_denominator_lcm = None
if rational_solvable:
    reduced, reduced_rank = augmented.rref()
    assert reduced_rank == rank
    particular = ["0"] * 146
    for row in range(reduced_rank):
        pivot = next((column for column in range(146)
                      if reduced[row, column]), None)
        assert pivot is not None
        particular[pivot] = str(reduced[row, 146])
    denominator_lcm = 1
    for value in particular:
        denominator_lcm = math.lcm(
            denominator_lcm, int(flint.fmpq(value).denominator))
    particular_denominator_lcm = str(denominator_lcm)

constant = [sum(vector[row] * b[row] for row in range(276))
            for vector in left]
slot_index = {tuple(xy): index for index, xy in enumerate(slots)}
support_p = [(i, degree - i) for degree in range(10)
             for i in range(degree + 1)]
support_q = [(i, degree - i) for degree in range(13)
             for i in range(degree + 1)]
projected_terms = []
coefficient_columns = []
valuation_histogram = {}
for p_index, (i, j) in enumerate(support_p):
    for q_index, (k, ell) in enumerate(support_q):
        scalar = i * ell - j * k
        if scalar == 0:
            continue
        target = (i + k - 1, j + ell - 1)
        row = slot_index[target]
        vector = [243 * scalar * functional[row] for functional in left]
        if not any(vector):
            continue
        coefficient_columns.append(vector)
        content = 0
        for value in vector:
            content = math.gcd(content, abs(value))
        valuation = vp3(content)
        key = str(valuation)
        valuation_histogram[key] = valuation_histogram.get(key, 0) + 1
        projected_terms.append({
            "p_index": p_index,
            "q_index": q_index,
            "target": list(target),
            "jacobian_scalar": scalar,
            "coefficient": vector,
        })

if coefficient_columns:
    coefficient_matrix = fmpz_mat([
        [coefficient_columns[column][row]
         for column in range(len(coefficient_columns))]
        for row in range(len(left))
    ])
    projected_coefficient_rank = coefficient_matrix.rank()
else:
    projected_coefficient_rank = 0

bases = {
    "left_basis": left,
    "right_basis": right,
    "particular_rational": particular,
}
bases_payload = (json.dumps(bases, sort_keys=True, separators=(",", ":"))
                 + "\n").encode()
Path(os.environ["BASES_JSON"]).write_bytes(bases_payload)
projected = {
    "constant": constant,
    "quadratic_terms": projected_terms,
}
projected_payload = (json.dumps(
    projected, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["PROJECTED_GZIP"]).write_bytes(
    gzip.compress(projected_payload, compresslevel=9, mtime=0))

result = {
    "status": "PASS-AS-B9-9-12-EXACT-CORE-COKERNEL",
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_replay_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "flint_version": flint.__version__,
    "rows": 276,
    "columns": 146,
    "rank_Q": rank,
    "right_kernel_dimension": len(right),
    "left_kernel_dimension": len(left),
    "right_kernel_exactly_checked": True,
    "left_kernel_exactly_checked": True,
    "smith_nonzero_diagonal": [str(value) for value in smith_nonzero],
    "smith_v3_histogram": smith_v3_histogram,
    "augmented_rank_Q": augmented_rank,
    "rational_linear_equation_solvable": rational_solvable,
    "particular_denominator_lcm": particular_denominator_lcm,
    "projected_constant_zero": not any(constant),
    "projected_constant_content_v3": vp3(math.gcd(
        *[abs(value) for value in constant])) if any(constant) else None,
    "projected_quadratic_term_count": len(projected_terms),
    "projected_quadratic_coefficient_rank_Q": projected_coefficient_rank,
    "projected_quadratic_content_v3_histogram": valuation_histogram,
    "projected_polynomial_identically_zero": (
        not any(constant) and not projected_terms),
    "A_sha256": sha_json(A_rows),
    "b_sha256": sha_json(b),
    "bases_sha256": hashlib.sha256(bases_payload).hexdigest(),
    "projected_uncompressed_sha256": hashlib.sha256(
        projected_payload).hexdigest(),
    "projected_gzip_sha256": hashlib.sha256(
        Path(os.environ["PROJECTED_GZIP"]).read_bytes()).hexdigest(),
    "scope": "exact normalized (9,12) operator over one fixed B9 parent",
    "refusal_scope": [
        "projected compatibility system is not automatically an emptiness theorem",
        "no all-depth point, maximum12 theorem, counterexample, or JC2",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("rank_right_left", rank, len(right), len(left))
print("augmented_solvable", augmented_rank, rational_solvable)
print("smith_v3_histogram", json.dumps(smith_v3_histogram, sort_keys=True))
print("projected_constant_zero", result["projected_constant_zero"])
print("projected_terms_rank", len(projected_terms), projected_coefficient_rank)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
