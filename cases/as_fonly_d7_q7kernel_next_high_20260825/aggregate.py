#!/usr/bin/env python3
"""Aggregate and classify the exact 27-shard Q7-kernel high-carry census."""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from collections import Counter
from pathlib import Path

result_dir = Path(os.environ["RESULT_DIR"])
paths = sorted(result_dir.glob("shard_*.json"))
assert len(paths) == 27
documents = [json.loads(path.read_text()) for path in paths]
assert {doc["shard_index"] for doc in documents} == set(range(27))
assert {doc["shard_count"] for doc in documents} == {27}
assert {doc["q7_rank"] for doc in documents} == {9}
assert {doc["q6_rank"] for doc in documents} == {7}
assert {doc["q6_kernel_dimension"] for doc in documents} == {9}
assert len({doc["q7_kernel_sha256"] for doc in documents}) == 1
assert len({json.dumps(doc["q6_high_support_by_basis"])
            for doc in documents}) == 1

records = {}
for doc in documents:
    for record in doc["records"]:
        index = record["index"]
        assert index not in records
        records[index] = tuple(record["high"])
assert set(records) == set(range(3 ** 9))
width = len(records[0])
assert width == sum(degree + 1 for degree in range(12, 8, -1))


def ternary(index, width=9):
    values = []
    for _ in range(width):
        values.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(values)


def index_of(values):
    return sum(value * 3 ** i for i, value in enumerate(values))


zero = records[0]
linear = [[0] * 9 for _ in range(width)]
square = [[0] * 9 for _ in range(width)]
cross = [[0] * 9 for _ in range(width)]
pairs = list(itertools.combinations(range(9), 2))
cross = [[0] * len(pairs) for _ in range(width)]
for variable in range(9):
    e = [0] * 9
    e[variable] = 1
    one = records[index_of(e)]
    e[variable] = 2
    two = records[index_of(e)]
    for coordinate in range(width):
        linear[coordinate][variable] = (two[coordinate] - one[coordinate]) % 3
        square[coordinate][variable] = (
            one[coordinate] - zero[coordinate]
            - linear[coordinate][variable]) % 3
for pair_index, (left, right) in enumerate(pairs):
    e = [0] * 9
    e[left] = e[right] = 1
    both = records[index_of(e)]
    for coordinate in range(width):
        cross[coordinate][pair_index] = (
            both[coordinate] - zero[coordinate]
            - linear[coordinate][left] - linear[coordinate][right]
            - square[coordinate][left] - square[coordinate][right]) % 3


def predicted(parameters):
    result = []
    for coordinate in range(width):
        value = zero[coordinate]
        value += sum(linear[coordinate][i] * parameters[i]
                     + square[coordinate][i] * parameters[i] ** 2
                     for i in range(9))
        value += sum(cross[coordinate][k]
                     * parameters[left] * parameters[right]
                     for k, (left, right) in enumerate(pairs))
        result.append(value % 3)
    return tuple(result)


quadratic_exact = all(predicted(ternary(index)) == records[index]
                      for index in range(3 ** 9))
zero_indices = [index for index, value in records.items()
                if not any(value)]
first_nonzero_histogram = Counter()
degree_offsets = []
offset = 0
for degree in range(12, 8, -1):
    degree_offsets.append((degree, offset, offset + degree + 1))
    offset += degree + 1
for value in records.values():
    first = next((degree for degree, start, end in degree_offsets
                  if any(value[start:end])), 0)
    first_nonzero_histogram[first] += 1

terms = []
if quadratic_exact:
    for coordinate in range(width):
        degree = next(degree for degree, start, end in degree_offsets
                      if start <= coordinate < end)
        start = next(start for d, start, end in degree_offsets if d == degree)
        exponent_x = coordinate - start
        nonzero = []
        if zero[coordinate]:
            nonzero.append(["constant", zero[coordinate]])
        nonzero += [[f"t{i}", value] for i, value
                    in enumerate(linear[coordinate]) if value]
        nonzero += [[f"t{i}^2", value] for i, value
                    in enumerate(square[coordinate]) if value]
        nonzero += [[f"t{left}*t{right}", cross[coordinate][k]]
                    for k, (left, right) in enumerate(pairs)
                    if cross[coordinate][k]]
        if nonzero:
            terms.append({"degree": degree, "x_exponent": exponent_x,
                          "y_exponent": degree - exponent_x,
                          "terms": nonzero})

stream = bytes(value for index in range(3 ** 9) for value in records[index])
presentation = {
    "state_count": 3 ** 9,
    "q7_rank": 9,
    "q7_kernel_dimension": 9,
    "q7_kernel_sha256": documents[0]["q7_kernel_sha256"],
    "q6_divergence_rank": 7,
    "q6_divergence_rows": 7,
    "q6_fiber_dimension": 9,
    "q6_high_max_degree": max(max(x, default=-1)
                                for x in documents[0]["q6_high_support_by_basis"]),
    "high_stream_sha256": hashlib.sha256(stream).hexdigest(),
    "quadratic_exact": quadratic_exact,
    "quadratic_nonzero_coordinates": terms,
    "high_zero_count": len(zero_indices),
    "high_zero_first_indices": zero_indices[:100],
    "first_nonzero_degree_histogram": dict(sorted(first_nonzero_histogram.items())),
}
encoded = (json.dumps(presentation, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(result_dir / "aggregate.json").write_bytes(encoded)
print("state_count", presentation["state_count"])
print("q7_rank_kernel_dimension", 9, 9)
print("q6_rank_rows_fiber", 7, 7, 9)
print("q6_high_max_degree", presentation["q6_high_max_degree"])
print("high_stream_sha256", presentation["high_stream_sha256"])
print("quadratic_exact", quadratic_exact)
print("quadratic_nonzero_coordinates", json.dumps(terms, sort_keys=True))
print("high_zero_count", len(zero_indices))
print("high_zero_first_indices", zero_indices[:100])
print("first_nonzero_degree_histogram",
      dict(sorted(first_nonzero_histogram.items())))
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q7KERNEL-NEXT-HIGH-AGGREGATE")
