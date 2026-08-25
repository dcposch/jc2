#!/usr/bin/env python3
"""Independent exact FLINT Smith form for a serialized integer Jacobian."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import flint
from flint import fmpz_mat


source = Path(os.environ["MATRIX_JSON"])
payload = source.read_bytes()
matrix = json.loads(payload)
assert len(matrix) == 91 and all(len(row) == 72 for row in matrix)
smith = fmpz_mat(matrix).snf()
diagonal = [int(smith[index, index]) for index in range(72)
            if smith[index, index] != 0]
assert all(diagonal[index + 1] % diagonal[index] == 0
           for index in range(len(diagonal) - 1))


def valuation3(value):
    value = abs(value)
    answer = 0
    while value % 3 == 0:
        answer += 1
        value //= 3
    return answer


valuations = [valuation3(value) for value in diagonal]
assert valuations.count(0) == 27
result = {
    "status": "PASS-AS-D7-JACOBIAN-SNF-FLINT",
    "python_flint_version": flint.__version__,
    "matrix_file_sha256": hashlib.sha256(payload).hexdigest(),
    "shape": [91, 72],
    "rank_over_Q": len(diagonal),
    "smith_diagonal": diagonal,
    "smith_v3": valuations,
    "unit_invariant_count": valuations.count(0),
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("rank", len(diagonal))
print("v3", valuations)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
