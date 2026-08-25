#!/usr/bin/env python3
"""Aggregate the 19 Q7-kernel to Q6 samples."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path

result_dir = Path(os.environ["RESULT_DIR"])
records = []
merkle = hashlib.sha256()
for index in range(19):
    payload = (result_dir / f"sample_{index:02d}.json").read_bytes()
    merkle.update(hashlib.sha256(payload).digest())
    record = json.loads(payload)
    assert record["sample_index"] == index
    records.append(record)
rank_hist = Counter(tuple(record["q6_rank_pair"]) for record in records)
g6_hist = Counter(tuple(record["G6_before_fourth_digit"])
                  for record in records)
aggregate = {
    "sample_count": len(records),
    "rank_histogram": [[list(key), value]
                       for key, value in sorted(rank_hist.items())],
    "G6_histogram": [[list(key), value]
                     for key, value in sorted(g6_hist.items())],
    "ordered_merkle_sha256": merkle.hexdigest(),
    "records": records,
}
encoded = (json.dumps(aggregate, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(result_dir / "aggregate.json").write_bytes(encoded)
print("sample_count", len(records))
print("rank_histogram", sorted(rank_hist.items()))
print("G6_histogram", sorted(g6_hist.items()))
print("ordered_merkle_sha256", merkle.hexdigest())
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q7-KERNEL-Q6-AGGREGATE")
