#!/usr/bin/env python3
"""Exact full-row mod-3 tangent/cokernel gate from 3^11 to 3^12."""

from __future__ import annotations

import gzip
import hashlib
import json
import math
import os
import platform
from pathlib import Path


assert platform.system() == "Linux", "AWS-only gate refuses non-Linux host"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_mod3p12_"), job_tag

OLD_MODULUS = 3 ** 11
NEW_MODULUS = 3 ** 12
matrix_path = Path(os.environ["MATRIX_GZIP"])
witness_path = Path(os.environ["WITNESS_JSON"])
matrix_bytes = matrix_path.read_bytes()
witness_bytes = witness_path.read_bytes()
assert hashlib.sha256(matrix_bytes).hexdigest() == os.environ[
    "EXPECTED_MATRIX_GZIP_SHA256"]
assert hashlib.sha256(witness_bytes).hexdigest() == os.environ[
    "EXPECTED_WITNESS_SHA256"]
payload = json.loads(gzip.decompress(matrix_bytes))
witness = json.loads(witness_bytes)
rows_z = payload["rows"]
residual_z = payload["residual"]
assert len(rows_z) == len(residual_z) == 299
assert all(len(row) == 149 for row in rows_z)
assert all(value % OLD_MODULUS == 0 for value in residual_z)


def rref(matrix):
    work = [[value % 3 for value in row] for row in matrix]
    pivot_columns = []
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = 1 if work[pivot_row][column] == 1 else 2
        work[pivot_row] = [(inverse * value) % 3
                           for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            scalar = work[row][column]
            work[row] = [(a - scalar * b) % 3
                         for a, b in zip(work[row], work[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return work, pivot_columns


def kernel_basis(matrix):
    reduced, pivots = rref(matrix)
    free = [column for column in range(len(matrix[0]))
            if column not in pivots]
    basis = []
    for free_column in free:
        vector = [0] * len(matrix[0])
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-reduced[row][free_column]) % 3
        basis.append(vector)
    return basis, pivots


rows = [[value % 3 for value in row] for row in rows_z]
rhs = [(-value // OLD_MODULUS) % 3 for value in residual_z]
augmented = [row + [value] for row, value in zip(rows, rhs)]
reduced_augmented, pivot_augmented = rref(augmented)
rank = len(rref(rows)[1])
inconsistent_rows = [
    index for index, row in enumerate(reduced_augmented)
    if not any(row[:-1]) and row[-1]
]
consistent = not inconsistent_rows
augmented_rank = rank + (0 if consistent else 1)

kernel, pivots = kernel_basis(rows)
assert len(kernel) == 149 - rank
transpose = [[rows[row][column] for row in range(299)]
             for column in range(149)]
left_cokernel, _ = kernel_basis(transpose)
assert len(left_cokernel) == 299 - rank
projections = [sum(a * b for a, b in zip(vector, rhs)) % 3
               for vector in left_cokernel]
assert consistent == (not any(projections))

particular = None
if consistent:
    particular = [0] * 149
    for row, pivot in enumerate(pivot_augmented):
        if pivot < 149:
            particular[pivot] = reduced_augmented[row][-1]
    assert all(sum(a * b for a, b in zip(row, particular)) % 3 == value
               for row, value in zip(rows, rhs))

support_p = [(i, degree - i) for degree in range(10)
             for i in range(degree + 1)]
support_q = [(i, degree - i) for degree in range(13)
             for i in range(degree + 1)]
slots = [(i, degree - i) for degree in range(23)
         for i in range(degree + 1)]
P0 = {tuple(entry[:2]): int(entry[2])
      for entry in witness["P_support_mod177147"]}
Q0 = {tuple(entry[:2]): int(entry[2])
      for entry in witness["Q_support_mod177147"]}
h0 = [int(value) for value in witness["H_coefficients_mod177147"]]


def primitive_mod3(vector):
    first = next(value for value in vector if value % 3)
    inverse = 1 if first % 3 == 1 else 2
    return [(inverse * value) % 3 for value in vector]


q_index = {xy: index for index, xy in enumerate(support_q)}
gauges = []
for index in (0, 55):
    vector = [0] * 149
    vector[index] = 1
    gauges.append(vector)
shear = [0] * 149
for xy, coefficient in P0.items():
    shear[55 + q_index[xy]] = coefficient % 3
gauges.append(primitive_mod3(shear))
assert len(rref(gauges)[1]) == 3
assert all(all(sum(a * b for a, b in zip(row, gauge)) % 3 == 0
               for row in rows) for gauge in gauges)


def deriv(poly, axis):
    answer = {}
    for (i, j), coefficient in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[xy] = answer.get(xy, 0) + exponent * coefficient
    return answer


def multiply(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            answer[xy] = answer.get(xy, 0) + a * b
    return answer


def convolution(left, right):
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def equations(P, Q, h):
    Px, Py = deriv(P, 0), deriv(P, 1)
    Qx, Qy = deriv(Q, 0), deriv(Q, 1)
    determinant = multiply(Px, Qy)
    for xy, value in multiply(Py, Qx).items():
        determinant[xy] = determinant.get(xy, 0) - value
    determinant[(0, 0)] = determinant.get((0, 0), 0) - 1
    answer = [determinant.get(xy, 0) for xy in slots]
    h2 = convolution(h, h)
    h3 = convolution(h2, h)
    h4 = convolution(h3, h)
    py9 = P.get((0, 9), 0)
    qy12 = Q.get((0, 12), 0)
    answer.extend(P.get((i, 9 - i), 0) - py9 * h3[i]
                  for i in range(10))
    answer.extend(Q.get((i, 12 - i), 0) - qy12 * h4[i]
                  for i in range(13))
    return answer


replay = None
if consistent:
    P = dict(P0)
    Q = dict(Q0)
    h = list(h0)
    for index, xy in enumerate(support_p):
        P[xy] = P.get(xy, 0) + OLD_MODULUS * particular[index]
    for index, xy in enumerate(support_q):
        Q[xy] = Q.get(xy, 0) + OLD_MODULUS * particular[55 + index]
    for index in range(3):
        h[index + 1] += OLD_MODULUS * particular[146 + index]
    literal = equations(P, Q, h)
    assert all(value % NEW_MODULUS == 0 for value in literal)
    replay = {
        "all_299_rows_zero_mod3p12": True,
        "P_support_mod3p12": [[*xy, value % NEW_MODULUS]
                               for xy, value in sorted(P.items())
                               if value % NEW_MODULUS],
        "Q_support_mod3p12": [[*xy, value % NEW_MODULUS]
                               for xy, value in sorted(Q.items())
                               if value % NEW_MODULUS],
        "H_coefficients_mod3p12": [value % NEW_MODULUS for value in h],
    }

obstruction = None
if not consistent:
    index = next(i for i, value in enumerate(projections) if value)
    vector = left_cokernel[index]
    assert all(sum(vector[row] * rows[row][column]
                   for row in range(299)) % 3 == 0
               for column in range(149))
    pairing = sum(a * b for a, b in zip(vector, rhs)) % 3
    assert pairing
    obstruction = {
        "left_cokernel_basis_index": index,
        "sparse_vector": [[row, value] for row, value in enumerate(vector)
                           if value],
        "rhs_pairing_mod3": pairing,
    }

certificate = {
    "kernel_basis": kernel,
    "left_cokernel_basis": left_cokernel,
    "rhs_projection": projections,
}
certificate_bytes = (json.dumps(certificate, sort_keys=True,
                                separators=(",", ":")) + "\n").encode()
certificate_gzip = gzip.compress(certificate_bytes, compresslevel=9, mtime=0)
Path(os.environ["CERTIFICATE_GZIP"]).write_bytes(certificate_gzip)

result = {
    "status": ("PASS-AS-B9-COMMON-CUBIC-MOD3P12-SAT" if consistent else
               "PASS-AS-B9-COMMON-CUBIC-MOD3P12-UNSAT"),
    "aws_job_tag": job_tag,
    "matrix_gzip_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
    "witness_sha256": hashlib.sha256(witness_bytes).hexdigest(),
    "equation_count": 299,
    "variable_count": 149,
    "rank_F3": rank,
    "augmented_rank_F3": augmented_rank,
    "consistent": consistent,
    "kernel_dimension": len(kernel),
    "gauge_dimension": 3,
    "non_gauge_kernel_dimension": len(kernel) - 3,
    "left_cokernel_dimension": len(left_cokernel),
    "nonzero_rhs_cokernel_coordinates": sum(bool(value)
                                             for value in projections),
    "particular": particular,
    "obstruction": obstruction,
    "literal_replay": replay,
    "certificate_uncompressed_sha256": hashlib.sha256(
        certificate_bytes).hexdigest(),
    "certificate_gzip_sha256": hashlib.sha256(
        certificate_gzip).hexdigest(),
    "scope": "one complete 299-row lift gate from mod3^11 to mod3^12",
    "refusal_scope": [
        "not the complete normalized family or B9 family",
        "not all-depth, maximum12, counterexample, or JC2",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("rank_aug_kernel_cokernel", rank, augmented_rank,
      len(kernel), len(left_cokernel))
print("non_gauge_kernel", len(kernel) - 3)
print("consistent", consistent)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
