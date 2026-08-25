#!/usr/bin/env python3
"""Fail-closed aggregate for 28 active-four plus one shards."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

directory = Path(os.environ["RESULTS_DIR"])
records = []
stream = hashlib.sha256()
for shard in range(28):
    path = directory / f"shard_{shard:02d}.json"
    payload = path.read_bytes()
    stream.update(payload)
    data = json.loads(payload)
    assert data["shard_index"] == shard
    assert data["point_count"] == 243
    stdout = (directory / f"shard_{shard:02d}.stdout").read_text()
    assert "PASS-ACTIVE4-PLUS-ONE-SHARD" in stdout
    assert not (directory / f"shard_{shard:02d}.stderr").read_bytes()
    records.append({key: data[key] for key in (
        "shard_index", "fifth_coordinate", "point_count",
        "q7_matrix_hash_histogram", "q7_rank_pair_histogram",
        "compatible_count", "mixed_cancellation_count",
        "mixed_cancellation_parameters")})

mixed_shards = [record for record in records
                if record["mixed_cancellation_count"]]
aggregate = {
    "shard_count": 28,
    "total_points_with_overlapping_u0_faces": 28 * 243,
    "ordered_shard_json_stream_sha256": stream.hexdigest(),
    "mixed_cancellation_shard_count": len(mixed_shards),
    "mixed_cancellation_shards": mixed_shards,
    "shards": records,
}
encoded = (json.dumps(aggregate, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["AGGREGATE_JSON"]).write_bytes(encoded)
print("shard_count", len(records))
print("total_points_with_overlapping_u0_faces", 28 * 243)
print("ordered_shard_json_stream_sha256", stream.hexdigest())
print("mixed_cancellation_shard_count", len(mixed_shards))
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-ACTIVE4-PLUS-ONE-AGGREGATE")

