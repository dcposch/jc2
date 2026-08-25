#!/usr/bin/env python3
"""Aggregate deterministic Q9-rank-class Q8 sample shards."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path

result_dir = Path(os.environ["RESULT_DIR"])
shard_count = int(os.environ.get("SHARD_COUNT", "27"))
all_records = {}
ordered_digest = hashlib.sha256()
q10_seen = 0
for index in range(shard_count):
    path = result_dir / f"shard_{index:02d}.json"
    payload = path.read_bytes()
    ordered_digest.update(hashlib.sha256(payload).digest())
    data = json.loads(payload)
    assert data["shard_index"] == index
    assert data["shard_count"] == shard_count
    q10_seen += data["q10_seen"]
    for key, values in data["records"].items():
        all_records.setdefault(key, []).extend(values)

expected = {"13,13", "13,14", "15,15", "16,16", "16,17", "17,18"}
assert set(all_records) == expected
assert all(all_records[key] for key in expected)
q8_signatures = {}
for key in sorted(expected):
    counter = Counter()
    for record in all_records[key]:
        if record["q9_witness"] is None:
            counter[("Q9_INCOMPATIBLE",)] += 1
        else:
            counter[(tuple(record["q8_top_rank_pair"]),
                     tuple(record["q8_full_rank_pair"]),
                     record["q8_kuranishi_rank"],
                     record["q8_matrix_sha256"],
                     record["q8_full_rref_sha256"])] += 1
    q8_signatures[key] = [[list(signature), count]
                          for signature, count in sorted(counter.items(),
                                                         key=lambda x: str(x[0]))]

aggregate = {
    "shard_count": shard_count,
    "q10_seen": q10_seen,
    "record_counts": {key: len(values)
                      for key, values in sorted(all_records.items())},
    "q8_signatures": q8_signatures,
    "records": {key: values for key, values in sorted(all_records.items())},
    "ordered_shard_merkle_sha256": ordered_digest.hexdigest(),
}
encoded = (json.dumps(aggregate, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(result_dir / "aggregate.json").write_bytes(encoded)
print("q10_seen", q10_seen)
print("record_counts", sorted(aggregate["record_counts"].items()))
print("q8_signature_counts", {key: len(value)
                               for key, value in q8_signatures.items()})
print("ordered_shard_merkle_sha256", ordered_digest.hexdigest())
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q9-RANKCLASS-Q8-SAMPLE-AGGREGATE")
