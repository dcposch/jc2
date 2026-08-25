#!/usr/bin/env python3
"""Classify the exact rational kernel of the common-cubic witness Jacobian."""

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

matrix = json.loads(gzip.decompress(matrix_bytes))
witness = json.loads(witness_bytes)
rows = matrix["rows"]
labels = matrix["row_labels"]
assert len(rows) == len(labels) == 299
assert all(len(row) == 149 for row in rows)

support_p = [(i, degree - i) for degree in range(10)
             for i in range(degree + 1)]
support_q = [(i, degree - i) for degree in range(13)
             for i in range(degree + 1)]
q_index = {xy: index for index, xy in enumerate(support_q)}
P = {tuple(entry[:2]): int(entry[2])
     for entry in witness["P_support_mod177147"]}
Q = {tuple(entry[:2]): int(entry[2])
     for entry in witness["Q_support_mod177147"]}


def primitive(vector):
    divisor = 0
    for value in vector:
        divisor = math.gcd(divisor, abs(int(value)))
    assert divisor
    answer = [int(value) // divisor for value in vector]
    if next(value for value in answer if value) < 0:
        answer = [-value for value in answer]
    return answer


def image(vector):
    return [sum(value * coefficient
                for value, coefficient in zip(row, vector))
            for row in rows]


J = fmpz_mat(rows)
raw_kernel, nullity = J.nullspace()
kernel = [primitive([raw_kernel[row, column]
                     for row in range(raw_kernel.nrows())])
          for column in range(nullity)]
assert J.rank() == 146
assert nullity == 3
assert all(not any(image(vector)) for vector in kernel)

p_translation = [0] * 149
p_translation[0] = 1
q_translation = [0] * 149
q_translation[55] = 1
q_shear_by_p = [0] * 149
for xy, coefficient in P.items():
    q_shear_by_p[55 + q_index[xy]] = coefficient
q_shear_by_p = primitive(q_shear_by_p)

gauges = [p_translation, q_translation, q_shear_by_p]
assert fmpz_mat(gauges).rank() == 3
assert all(not any(image(vector)) for vector in gauges)
# Three independent gauge vectors in the three-dimensional exact kernel are
# an exhaustion certificate; no basis matching or division is assumed.

scaling = [0] * 149
for index, xy in enumerate(support_p):
    scaling[index] = P.get(xy, 0)
for index, xy in enumerate(support_q):
    scaling[55 + index] = -Q.get(xy, 0)
scaling_image = image(scaling)
scaling_nonzero = [
    [index, labels[index], value, value // MODULUS]
    for index, value in enumerate(scaling_image) if value
]
assert scaling_nonzero
assert all(value % MODULUS == 0 for value in scaling_image)
assert all(label[0] in ("P9", "Q12")
           for _, label, _, _ in scaling_nonzero)


def sparse(vector):
    answer = []
    for index, value in enumerate(vector):
        if not value:
            continue
        if index < 55:
            name = ["P", *support_p[index]]
        elif index < 146:
            name = ["Q", *support_q[index - 55]]
        else:
            name = ["H", index - 145]
        answer.append([name, value])
    return answer


result = {
    "status": "PASS-AS-B9-9-12-COMMON-CUBIC-RATIONAL-KERNEL-GAUGE-CLASSIFICATION",
    "matrix_gzip_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
    "witness_sha256": hashlib.sha256(witness_bytes).hexdigest(),
    "rank_Q": 146,
    "right_kernel_dimension_Q": nullity,
    "source_defined_gauge_rank_Q": fmpz_mat(gauges).rank(),
    "kernel_exhausted_by_source_defined_gauges": True,
    "gauge_directions": {
        "target_P_translation": sparse(p_translation),
        "target_Q_translation": sparse(q_translation),
        "target_lower_shear_Q_plus_tP": sparse(q_shear_by_p),
    },
    "computed_primitive_kernel_basis": [sparse(vector) for vector in kernel],
    "scaling_negative_control": {
        "exact_kernel": False,
        "image_divisible_by_3p11": True,
        "nonzero_row_count": len(scaling_nonzero),
        "nonzero_rows": scaling_nonzero,
        "explanation": (
            "the stored representative satisfies the common-cubic top rows "
            "modulo 3^11 rather than literally over Z"
        ),
    },
    "scope": "exact rational right kernel at one displayed mod3^11 witness",
    "refusal_scope": [
        "the 55-dimensional mod-3 tangent kernel is not quotiented here",
        "no Hensel, all-depth, maximum12, counterexample, or JC2 conclusion",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("rank_kernel_gauge", 146, nullity, fmpz_mat(gauges).rank())
print("scaling_nonzero_rows", len(scaling_nonzero))
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
