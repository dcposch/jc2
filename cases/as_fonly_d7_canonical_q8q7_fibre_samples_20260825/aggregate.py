#!/usr/bin/env python3
"""Aggregate 64 canonical Q8-to-Q7 fibre samples."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path

directory = Path(os.environ["RESULTS_DIR"])
records = []
stream = hashlib.sha256()
for sample_index in range(64):
    path = directory / f"sample_{sample_index:02d}.json"
    payload = path.read_bytes()
    stream.update(payload)
    data = json.loads(payload)
    assert data["sample_index"] == sample_index
    assert "PASS-CANONICAL-Q8Q7-FIBRE-SAMPLE" in (
        directory / f"sample_{sample_index:02d}.stdout").read_text()
    assert not (directory / f"sample_{sample_index:02d}.stderr").read_bytes()
    records.append(data)

status = Counter(record["status"] for record in records)
q8_ranks = Counter(str(record.get("q8_rank_pair")) for record in records)
q7_ranks = Counter(str([record.get("q7_rank"),
                        record.get("q7_cokernel_dimension")])
                   for record in records if record.get("q7_rank") is not None)
survivors = [{
    "sample_index": record["sample_index"],
    "q9_parameters": record["q9_parameters"],
    "zero_count": record.get("zero_count"),
    "first_witness": record.get("first_witness"),
    "support_dimension": record.get("support_dimension"),
    "nonlinear": record.get("nonlinear"),
} for record in records if record.get("zero_count")]

aggregate = {
    "sample_count": 64,
    "axis_sample_count": 22,
    "off_axis_sample_count": 41,
    "status_histogram": dict(sorted(status.items())),
    "q8_rank_pair_histogram": dict(sorted(q8_ranks.items())),
    "q7_rank_cokernel_histogram": dict(sorted(q7_ranks.items())),
    "survivor_sample_count": len(survivors),
    "survivors": survivors,
    "ordered_sample_json_stream_sha256": stream.hexdigest(),
}
encoded = (json.dumps(aggregate, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["AGGREGATE_JSON"]).write_bytes(encoded)
print("sample_count", 64)
print("status_histogram", json.dumps(dict(sorted(status.items())), sort_keys=True))
print("q8_rank_pair_histogram", json.dumps(dict(sorted(q8_ranks.items())), sort_keys=True))
print("q7_rank_cokernel_histogram", json.dumps(dict(sorted(q7_ranks.items())), sort_keys=True))
print("survivor_sample_count", len(survivors))
print("survivors", json.dumps(survivors, sort_keys=True))
print("ordered_sample_json_stream_sha256", stream.hexdigest())
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-CANONICAL-Q8Q7-FIBRE-SAMPLE-AGGREGATE")

