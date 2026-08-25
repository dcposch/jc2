#!/usr/bin/env python3
"""Exact aggregate and interpolation for the global Q7 design."""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from pathlib import Path

directory = Path(os.environ["RESULTS_DIR"])
payloads = []
stream = hashlib.sha256()
for shard in range(36):
    path = directory / f"shard_{shard:02d}.json"
    payload = path.read_bytes()
    stream.update(payload)
    data = json.loads(payload)
    assert data["shard_index"] == shard
    assert data["q7_rank"] == 9 and data["q7_cokernel_dimension"] == 10
    assert data["q7_matrix_sha256"] == (
        "f30baed043492c723d80a787571d6cb743626da643a20f031da5b95091e6dd50")
    assert "PASS-GLOBAL-Q7-KURANISHI-DESIGN-SHARD" in (
        directory / f"shard_{shard:02d}.stdout").read_text()
    assert not (directory / f"shard_{shard:02d}.stderr").read_bytes()
    payloads.append(data)

basis = payloads[0]
names = tuple(basis["coordinate_names"])
assert len(names) == 32 and basis["kind"] == "basis"
basis_records = {tuple(record["parameters"]): tuple(record["kappa"])
                 for record in basis["records"]}
zero = (0,) * 32
constant = basis_records[zero]
linear = [[0] * 32 for _ in range(10)]
square = [[0] * 32 for _ in range(10)]
for variable in range(32):
    one = [0] * 32
    two = [0] * 32
    one[variable] = 1
    two[variable] = 2
    value1 = basis_records[tuple(one)]
    value2 = basis_records[tuple(two)]
    for coordinate in range(10):
        linear[coordinate][variable] = (value2[coordinate] - value1[coordinate]) % 3
        square[coordinate][variable] = (value1[coordinate] - constant[coordinate]
                                        - linear[coordinate][variable]) % 3

pairs = list(itertools.combinations(range(32), 2))
pair_records = {}
for payload in payloads[1:32]:
    assert payload["kind"] == "pairs"
    for record in payload["records"]:
        pair_index = record["pair_index"]
        assert tuple(record["pair"]) == pairs[pair_index]
        assert pair_index not in pair_records
        pair_records[pair_index] = tuple(record["kappa"])
assert set(pair_records) == set(range(len(pairs)))

cross = [[0] * len(pairs) for _ in range(10)]
for pair_index, (left, right) in enumerate(pairs):
    value = pair_records[pair_index]
    for coordinate in range(10):
        cross[coordinate][pair_index] = (value[coordinate]
            - constant[coordinate]
            - linear[coordinate][left] - square[coordinate][left]
            - linear[coordinate][right] - square[coordinate][right]) % 3


def predict(parameters):
    answer = []
    for coordinate in range(10):
        value = constant[coordinate]
        value += sum(linear[coordinate][i] * parameters[i]
                     + square[coordinate][i] * parameters[i] ** 2
                     for i in range(32))
        value += sum(cross[coordinate][k] * parameters[i] * parameters[j]
                     for k, (i, j) in enumerate(pairs))
        answer.append(value % 3)
    return tuple(answer)

control_count = 0
control_stream = hashlib.sha256()
seen_controls = set()
canonical_control_histogram = {}
for payload in payloads[32:]:
    assert payload["kind"] == "controls"
    for record in payload["records"]:
        control_index = record["control_index"]
        assert control_index not in seen_controls
        seen_controls.add(control_index)
        parameters = tuple(record["parameters"])
        actual = tuple(record["kappa"])
        assert predict(parameters) == actual
        control_stream.update(bytes(parameters + actual))
        canonical = record["canonical_direct_reduction"]
        key = (f"q9={int(canonical['q9_rows_zero'])},"
               f"q8={int(canonical['q8_rows_zero'])},"
               f"q7={canonical['q7_rank_pair']}")
        canonical_control_histogram[key] = (
            canonical_control_histogram.get(key, 0) + 1)
        control_count += 1
assert seen_controls == set(range(64))

terms = []
support = set()
for coordinate in range(10):
    nonzero = []
    if constant[coordinate]:
        nonzero.append(["constant", constant[coordinate]])
    for variable in range(32):
        if linear[coordinate][variable]:
            nonzero.append([names[variable], linear[coordinate][variable]])
            support.add(variable)
        if square[coordinate][variable]:
            nonzero.append([f"{names[variable]}^2", square[coordinate][variable]])
            support.add(variable)
    for pair_index, (left, right) in enumerate(pairs):
        if cross[coordinate][pair_index]:
            nonzero.append([
                f"{names[left]}*{names[right]}",
                cross[coordinate][pair_index]])
            support.update((left, right))
    if nonzero:
        terms.append({"cokernel_coordinate": coordinate, "terms": nonzero})

presentation = {
    "field": 3,
    "coordinate_names": names,
    "source_degree_bound": 2,
    "q7_matrix_sha256": payloads[0]["q7_matrix_sha256"],
    "q7_rank": 9,
    "q7_cokernel_dimension": 10,
    "constant": constant,
    "linear": linear,
    "square": square,
    "pairs": pairs,
    "cross": cross,
    "nonzero_terms": terms,
    "support_indices": sorted(support),
    "support_names": [names[index] for index in sorted(support)],
    "design_point_count": 1 + 2 * 32 + len(pairs),
    "pair_coverage_count": len(pair_records),
    "off_grid_control_count": control_count,
    "off_grid_control_stream_sha256": control_stream.hexdigest(),
    "canonical_direct_reduction_control_histogram": canonical_control_histogram,
    "ordered_shard_json_stream_sha256": stream.hexdigest(),
}
encoded = (json.dumps(presentation, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["AGGREGATE_JSON"]).write_bytes(encoded)
coefficient_count = sum(len(item["terms"]) for item in terms)
print("design_point_count", presentation["design_point_count"])
print("pair_coverage_count", len(pair_records))
print("off_grid_control_count", control_count)
print("canonical_direct_reduction_control_histogram",
      json.dumps(canonical_control_histogram, sort_keys=True))
print("q7_rank_cokernel", 9, 10)
print("nonzero_cokernel_coordinates", len(terms))
print("nonzero_coefficient_count", coefficient_count)
print("support_variable_count", len(support))
print("support_names", [names[index] for index in sorted(support)])
print("nonzero_terms", json.dumps(terms, sort_keys=True))
print("ordered_shard_json_stream_sha256", stream.hexdigest())
print("presentation_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-GLOBAL-Q7-KURANISHI-QUADRATIC-PRESENTATION")
