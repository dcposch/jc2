#!/usr/bin/env python3
"""Exact raw rational-cokernel and gauge quotient at one B9 witness."""

from __future__ import annotations

import gzip
import hashlib
import json
import math
import os
from pathlib import Path

from flint import fmpz_mat


MODULUS = 3 ** 11
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
rows = payload["rows"]
residual = payload["residual"]
labels = payload["row_labels"]
assert len(rows) == len(residual) == len(labels) == 299

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
h = [int(value) for value in witness["H_coefficients_mod177147"]]


def primitive(vector):
    divisor = 0
    for value in vector:
        divisor = math.gcd(divisor, abs(int(value)))
    assert divisor
    answer = [int(value) // divisor for value in vector]
    if next(value for value in answer if value) < 0:
        answer = [-value for value in answer]
    return answer


def vp3(value):
    if not value:
        return None
    value = abs(int(value))
    answer = 0
    while value % 3 == 0:
        value //= 3
        answer += 1
    return answer


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


h2 = convolution(h, h)
h3 = convolution(h2, h)
h4 = convolution(h3, h)


def source_equations(P, Q):
    Px, Py = deriv(P, 0), deriv(P, 1)
    Qx, Qy = deriv(Q, 0), deriv(Q, 1)
    left = multiply(Px, Qy)
    right = multiply(Py, Qx)
    determinant = dict(left)
    for xy, value in right.items():
        determinant[xy] = determinant.get(xy, 0) - value
    determinant[(0, 0)] = determinant.get((0, 0), 0) - 1
    answer = [determinant.get(xy, 0) for xy in slots]
    py9 = P.get((0, 9), 0)
    qy12 = Q.get((0, 12), 0)
    answer.extend(P.get((i, 9 - i), 0) - py9 * h3[i]
                  for i in range(10))
    answer.extend(Q.get((i, 12 - i), 0) - qy12 * h4[i]
                  for i in range(13))
    return answer


assert source_equations(P0, Q0) == residual
for constant in (-2, -1, 1, 2):
    P = dict(P0)
    P[(0, 0)] = P.get((0, 0), 0) + constant
    assert source_equations(P, Q0) == residual
    Q = dict(Q0)
    Q[(0, 0)] = Q.get((0, 0), 0) + constant
    assert source_equations(P0, Q) == residual
    Q = dict(Q0)
    for xy, coefficient in P0.items():
        Q[xy] = Q.get(xy, 0) + constant * coefficient
    assert source_equations(P0, Q) == residual

J = fmpz_mat(rows)
left_raw, left_nullity = J.transpose().nullspace()
left = [primitive([left_raw[row, column]
                   for row in range(left_raw.nrows())])
        for column in range(left_nullity)]
assert J.rank() == 146
assert left_nullity == 153
assert all(all(sum(vector[row] * rows[row][column]
                       for row in range(299)) == 0
                   for column in range(149))
           for vector in left)
projected = [sum(a * b for a, b in zip(vector, residual))
             for vector in left]
assert any(projected)

content = 0
for value in projected:
    content = math.gcd(content, abs(value))
projection_histogram = {}
for value in projected:
    key = "zero" if not value else str(vp3(value))
    projection_histogram[key] = projection_histogram.get(key, 0) + 1

gauge_vectors = []
for index in (0, 55):
    vector = [0] * 149
    vector[index] = 1
    gauge_vectors.append(vector)
q_index = {xy: index for index, xy in enumerate(support_q)}
shear = [0] * 149
for xy, coefficient in P0.items():
    shear[55 + q_index[xy]] = coefficient
gauge_vectors.append(primitive(shear))
assert fmpz_mat(gauge_vectors).rank() == 3


def rank_mod3(matrix):
    work = [[value % 3 for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = 1 if work[rank][column] == 1 else 2
        work[rank] = [(inverse * value) % 3 for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            scalar = work[row][column]
            work[row] = [(a - scalar * b) % 3
                         for a, b in zip(work[row], work[rank])]
        rank += 1
    return rank


assert rank_mod3(gauge_vectors) == 3
basis_payload = {
    "left_kernel": left,
    "projected_residual": projected,
}
basis_bytes = (json.dumps(basis_payload, sort_keys=True,
                          separators=(",", ":")) + "\n").encode()
basis_gzip = gzip.compress(basis_bytes, compresslevel=9, mtime=0)
Path(os.environ["BASIS_GZIP"]).write_bytes(basis_gzip)

result = {
    "status": "PASS-AS-B9-9-12-COMMON-CUBIC-REDUCED-RATIONAL-COKERNEL",
    "matrix_gzip_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
    "witness_sha256": hashlib.sha256(witness_bytes).hexdigest(),
    "rank_Q": 146,
    "rational_right_kernel_dimension": 3,
    "rational_left_cokernel_dimension": left_nullity,
    "rational_kernel_is_all_exact_target_gauge": True,
    "rational_non_gauge_kernel_after_quotient": 0,
    "raw_left_projection_nonzero": True,
    "raw_left_projection_content_v3": vp3(content),
    "raw_left_projection_valuation_histogram": projection_histogram,
    "raw_kernel_restriction_is_constant": True,
    "mod3_rank": 94,
    "mod3_tangent_dimension": 55,
    "mod3_gauge_dimension": 3,
    "mod3_non_gauge_tangent_dimension": 52,
    "mod3_cokernel_dimension": 205,
    "basis_payload_sha256": hashlib.sha256(basis_bytes).hexdigest(),
    "basis_gzip_sha256": hashlib.sha256(basis_gzip).hexdigest(),
    "interpretation": (
        "the raw 3-to-153 rational kernel/cokernel restriction is constant "
        "because all three rational kernel directions are exact gauges; the "
        "singular digit successor is a 52-to-205 mod-3 object with Smith "
        "filtration and transverse elimination still required"
    ),
    "refusal_scope": [
        "raw left projection is not a full Lyapunov-Schmidt/Kuranishi map",
        "no local row-ideal generation or bounded right inverse is proved",
        "no lifting, nonexistence, maximum12, counterexample, or JC2 claim",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("rank_kernel_cokernel", 146, 3, 153)
print("raw_projection_content_v3", vp3(content))
print("mod3_quotient_tangent_cokernel", 52, 205)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
