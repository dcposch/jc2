#!/usr/bin/env python3
"""Aggregate fresh-elimination and overlapping Kuranishi map shards."""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import platform
from collections import Counter
from pathlib import Path


assert platform.system() == "Linux", "AWS-only aggregate refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_aggregate_"), job_tag
root = Path(os.environ["CUSTODY_ROOT"])

fresh_records = []
fresh_results = []
for path in sorted((root / "AWS_BOX02_FRESH_ELIM_V2").glob(
        "shard_*/records_*.json.gz")):
    fresh_records.extend(json.load(gzip.open(path, "rt")))
for path in sorted((root / "AWS_BOX02_FRESH_ELIM_V2").glob(
        "shard_*/result_*.json")):
    fresh_results.append(json.loads(path.read_text()))
assert len(fresh_results) == 9
assert len(fresh_records) == 447
assert sorted(record["global_index"] for record in fresh_records) == list(
    range(447))
assert Counter(record["fresh_cokernel_rank"]
               for record in fresh_records) == {29: 447}
assert not any(record["consistent_after_fresh_elimination"]
               for record in fresh_records)
matrix_hashes = Counter(record["matrix_sha256"]
                        for record in fresh_records)
assert matrix_hashes == {
    "9b1ae5b0f64bb3d7fccd27f7d8a3d2cae141c297fd531fd6fff1c302a48fb7d5":
    447}
ordered_fresh_bytes = (json.dumps(
    sorted(fresh_records, key=lambda record: record["global_index"]),
    sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["FRESH_RECORDS_GZIP"]).write_bytes(
    gzip.compress(ordered_fresh_bytes, compresslevel=9, mtime=0))

blocks = [
    ("BOX02", "b000_032", 0, 32),
    ("BOX03", "b030_062", 30, 62),
    ("R6D", "b060_092", 60, 92),
    ("BOX02", "b090_122", 90, 122),
    ("BOX03", "b120_152", 120, 152),
    ("R6D", "b150_176", 150, 176),
]
loaded = []
for host, label, start, end in blocks:
    directory = root / "AWS_KURANISHI_MAP" / host / label
    result = json.loads((directory / "result.json").read_text())
    assert (result["row_start"], result["row_end"]) == (start, end)
    assert hashlib.sha256((directory / "map.smt2").read_bytes()).hexdigest() == (
        result["smt_sha256"])
    loaded.append((start, end, result))

overlaps = []
for (left_start, left_end, left), (right_start, right_end, right) in zip(
        loaded, loaded[1:]):
    for row in range(max(left_start, right_start), min(left_end, right_end)):
        left_hash = left["coordinate_hashes"][row - left_start]
        right_hash = right["coordinate_hashes"][row - right_start]
        assert left_hash == right_hash
        overlaps.append([row, left_hash])
assert [row for row, _ in overlaps] == [30, 31, 60, 61, 90, 91,
                                        120, 121, 150, 151]
all_hashes = {result["all_coordinate_hashes_sha256"]
              for _, _, result in loaded}
assert all_hashes == {
    "557123112e5c3e4ea5d3a5a95709d816254080e0eeef2d995d028013db468b48"}
full_directory = root / "AWS_KURANISHI_MAP" / "BOX02" / "full_000_176"
full_result = json.loads((full_directory / "result.json").read_text())
full_formula_hash = hashlib.sha256(
    (full_directory / "map.smt2").read_bytes()).hexdigest()
assert full_formula_hash == full_result["smt_sha256"] == (
    "108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c")
assert full_result["row_start"] == 0 and full_result["row_end"] == 176

result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-KURANISHI-AGGREGATE",
    "aws_job_tag": job_tag,
    "fresh_control_count": 447,
    "fresh_control_rank_histogram": {"29": 447},
    "fresh_control_sat_count": 0,
    "fresh_block_sha256": next(iter(matrix_hashes)),
    "fresh_records_uncompressed_sha256": hashlib.sha256(
        ordered_fresh_bytes).hexdigest(),
    "coordinate_block_count": 6,
    "overlap_checks": overlaps,
    "all_coordinate_hashes_sha256": next(iter(all_hashes)),
    "full_formula_sha256": full_formula_hash,
    "full_formula_size": (full_directory / "map.smt2").stat().st_size,
    "full_dag_node_count": full_result["dag_node_count"],
    "family_dimensions": [17, 78, 95],
    "fresh_block_shape_rank_kernel_quotient": [205, 55, 29, 26, 176],
    "scope": "exact map construction plus sampled predecessor diagnostics",
    "refusal_scope": [
        "447 UNSAT controls are not family-wide exclusion",
        "formula SAT requires literal source replay",
        "formula UNSAT requires a checked proof/certificate",
        "no all-depth, maximum12, counterexample, or JC2 claim",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("fresh_controls_rank_sat", 447, 29, 0)
print("coordinate_overlap_count", len(overlaps))
print("all_coordinate_hashes_sha256", result["all_coordinate_hashes_sha256"])
print("full_formula_sha256", full_formula_hash)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
