#!/usr/bin/env python3
"""Exact 299x149 Jacobian/SNF at the normalized common-cubic witness."""

from __future__ import annotations

import gzip
import hashlib
import json
import math
import os
from pathlib import Path

import flint
from flint import fmpq_mat, fmpz_mat


MODULUS = 3 ** 11
witness_path = Path(os.environ["WITNESS_JSON"])
witness_payload = witness_path.read_bytes()
expected_witness = os.environ["EXPECTED_WITNESS_SHA256"]
assert hashlib.sha256(witness_payload).hexdigest() == expected_witness
witness = json.loads(witness_payload)
assert witness["all_299_integer_rows_zero_mod177147"]

support_p = [(i, degree - i) for degree in range(10)
             for i in range(degree + 1)]
support_q = [(i, degree - i) for degree in range(13)
             for i in range(degree + 1)]
slots = [(i, degree - i) for degree in range(23)
         for i in range(degree + 1)]
assert len(support_p) == 55 and len(support_q) == 91 and len(slots) == 276
slot_index = {xy: index for index, xy in enumerate(slots)}
p_index = {xy: index for index, xy in enumerate(support_p)}
q_index = {xy: index for index, xy in enumerate(support_q)}

P = {tuple(row[:2]): int(row[2]) for row in witness["P_support_mod177147"]}
Q = {tuple(row[:2]): int(row[2]) for row in witness["Q_support_mod177147"]}
h = [int(value) for value in witness["H_coefficients_mod177147"]]
assert h[0] == 1 and len(h) == 4


def convolution(left, right):
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def deriv(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[xy] = answer.get(xy, 0) + exponent * value
    return answer


def mul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            answer[xy] = answer.get(xy, 0) + a * b
    return answer


def add(left, right, right_scale=1):
    answer = dict(left)
    for xy, value in right.items():
        answer[xy] = answer.get(xy, 0) + right_scale * value
        if not answer[xy]:
            del answer[xy]
    return answer


Px, Py, Qx, Qy = deriv(P, 0), deriv(P, 1), deriv(Q, 0), deriv(Q, 1)
determinant = add(mul(Px, Qy), mul(Py, Qx), -1)
determinant[(0, 0)] = determinant.get((0, 0), 0) - 1

rows = []
residual = []
row_labels = []
for xy in slots:
    row = [0] * 149
    for index, (i, j) in enumerate(support_p):
        value = 0
        if i:
            value += i * Qy.get((xy[0] - i + 1, xy[1] - j), 0)
        if j:
            value -= j * Qx.get((xy[0] - i, xy[1] - j + 1), 0)
        row[index] = value
    for index, (k, ell) in enumerate(support_q):
        value = 0
        if ell:
            value += ell * Px.get((xy[0] - k, xy[1] - ell + 1), 0)
        if k:
            value -= k * Py.get((xy[0] - k + 1, xy[1] - ell), 0)
        row[55 + index] = value
    rows.append(row)
    residual.append(determinant.get(xy, 0))
    row_labels.append(["det", xy[0], xy[1]])

h2 = convolution(h, h)
h3 = convolution(h2, h)
h4 = convolution(h3, h)
py9 = P.get((0, 9), 0)
qy12 = Q.get((0, 12), 0)
for degree, power, scalar, support, offset, leading, tag in (
        (9, 3, py9, support_p, 0, p_index[(0, 9)], "P9"),
        (12, 4, qy12, support_q, 55, q_index[(0, 12)], "Q12")):
    hp = h3 if power == 3 else h4
    previous = h2 if power == 3 else h3
    for i in range(degree + 1):
        row = [0] * 149
        coefficient_index = (p_index if tag == "P9" else q_index)[
            (i, degree - i)]
        row[offset + coefficient_index] += 1
        row[offset + leading] -= hp[i]
        for j in range(1, 4):
            if 0 <= i - j < len(previous):
                row[146 + j - 1] -= scalar * power * previous[i - j]
        value = (P if tag == "P9" else Q).get((i, degree - i), 0)
        value -= scalar * hp[i]
        rows.append(row)
        residual.append(value)
        row_labels.append([tag, i, degree - i])

assert len(rows) == len(residual) == len(row_labels) == 299
assert all(value % MODULUS == 0 for value in residual)


def vp3(value):
    if value == 0:
        return None
    value = abs(value)
    answer = 0
    while value % 3 == 0:
        value //= 3
        answer += 1
    return answer


def rank_mod3(matrix):
    work = [[value % 3 for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        if work[rank][column] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            scalar = work[row][column]
            work[row] = [(a - scalar * b) % 3
                         for a, b in zip(work[row], work[rank])]
        rank += 1
    return rank


def pivot_columns(matrix):
    reduced, rank = fmpq_mat(matrix).rref()
    pivots = []
    for row in range(rank):
        pivot = next(column for column in range(reduced.ncols())
                     if reduced[row, column])
        pivots.append(pivot)
    return pivots


J = fmpz_mat(rows)
rank_q = J.rank()
rank_f3 = rank_mod3(rows)
smith = J.snf()
smith_nonzero = [abs(int(smith[index, index])) for index in range(rank_q)]
smith_v3 = [vp3(value) for value in smith_nonzero]
e_min = sum(smith_v3)
smith_histogram = {}
for value in smith_v3:
    key = str(value)
    smith_histogram[key] = smith_histogram.get(key, 0) + 1

valuations = [vp3(value) for value in residual]
finite = sorted({value for value in valuations if value is not None})
threshold_ranks = []
best_threshold = None
best_rows = None
for threshold in finite:
    selected = [index for index, value in enumerate(valuations)
                if value is None or value >= threshold]
    current_rank = fmpz_mat([rows[index] for index in selected]).rank()
    threshold_ranks.append([threshold, current_rank, len(selected)])
    if current_rank == rank_q:
        best_threshold = threshold
        best_rows = selected
assert best_threshold is not None

columns = pivot_columns(rows)
assert len(columns) == rank_q
restricted = [[rows[row][column] for column in columns]
              for row in best_rows]
relative_pivots = pivot_columns(fmpz_mat(restricted).transpose().tolist())
chosen_rows = [best_rows[index] for index in relative_pivots]
assert len(chosen_rows) == rank_q
square = fmpz_mat([[rows[row][column] for column in columns]
                   for row in chosen_rows])
minor = int(square.det())
assert minor
minor_v3 = vp3(minor)
selected_residual_min = min(
    value for row, value in enumerate(valuations)
    if row in chosen_rows and value is not None)

payload = {
    "rows": rows,
    "residual": residual,
    "row_labels": row_labels,
    "chosen_rows": chosen_rows,
    "chosen_columns": columns,
    "chosen_minor": str(minor),
}
payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":"))
                 + "\n").encode()
Path(os.environ["MATRIX_GZIP"]).write_bytes(
    gzip.compress(payload_bytes, compresslevel=9, mtime=0))

result = {
    "status": "PASS-AS-B9-9-12-COMMON-CUBIC-WITNESS-JACOBIAN-SNF",
    "witness_sha256": expected_witness,
    "flint_version": flint.__version__,
    "equation_count": 299,
    "variable_count": 149,
    "rank_Q": rank_q,
    "rank_F3": rank_f3,
    "tangent_dimension_F3": 149 - rank_f3,
    "smith_v3_histogram": smith_histogram,
    "maximal_rank_determinantal_ideal_v3": e_min,
    "nonzero_residual_min_v3": min(finite),
    "nonzero_residual_max_v3": max(finite),
    "exact_zero_residual_count": sum(value is None for value in valuations),
    "threshold_rank_table": threshold_ranks,
    "best_full_rank_residual_threshold": best_threshold,
    "classical_hensel_impossible_at_current_precision": (
        best_threshold <= 2 * e_min),
    "chosen_minor_v3": minor_v3,
    "chosen_rows_residual_min_v3": selected_residual_min,
    "chosen_minor_hensel_inequality": selected_residual_min > 2 * minor_v3,
    "chosen_rows": chosen_rows,
    "chosen_columns": columns,
    "matrix_payload_sha256": hashlib.sha256(payload_bytes).hexdigest(),
    "matrix_gzip_sha256": hashlib.sha256(
        Path(os.environ["MATRIX_GZIP"]).read_bytes()).hexdigest(),
    "local_row_ideal_generation": (
        "not attempted because the optimal-threshold/minimal-determinantal "
        "necessary Hensel inequality already fails"
        if best_threshold <= 2 * e_min else "required before Hensel use"),
    "scope": "one literal normalized common-cubic mod3^11 witness",
    "refusal_scope": [
        "failure of this Hensel criterion is not nonexistence",
        "no all-depth point, maximum12 theorem, counterexample, or JC2",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("rank_Q_F3_tangent", rank_q, rank_f3, 149 - rank_f3)
print("e_min_best_threshold", e_min, best_threshold)
print("chosen_minor_v3_residual", minor_v3, selected_residual_min)
print("hensel_impossible", result["classical_hensel_impossible_at_current_precision"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
