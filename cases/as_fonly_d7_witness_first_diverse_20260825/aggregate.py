#!/usr/bin/env python3
"""Aggregate the 24 preregistered witness-first samples."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path

results = Path(os.environ["RESULTS_DIR"])
sample_count = int(os.environ["SAMPLE_COUNT"])
assert sample_count == 24
documents = []
stream = hashlib.sha256()
for index in range(sample_count):
    payload = (results / f"sample_{index:03d}.json").read_bytes()
    document = json.loads(payload)
    assert document["sample_index"] == index
    assert document["sample_count"] == sample_count
    stream.update(hashlib.sha256(payload).digest())
    documents.append(document)

rank_histogram = Counter(tuple(document["q7_rank_pair"])
                         for document in documents)
compatible = [document for document in documents
              if document["q7_compatible"]]
assert all(document["q7_states_exhausted"] == 3 ** 9
           and document["recursive_direct_mismatch_count"] == 0
           for document in compatible)
hits = [document for document in compatible if document["high_zero_count"]]
aggregate = {
    "sample_count": sample_count,
    "distinct_q9_state_count": len({document["q9_state_index"]
                                     for document in documents}),
    "q7_rank_histogram": {str(key): value
                           for key, value in sorted(rank_histogram.items())},
    "q7_compatible_sample_count": len(compatible),
    "q7_fibre_states_exhausted": sum(
        document.get("q7_states_exhausted", 0) for document in documents),
    "recursive_direct_mismatch_count": sum(
        document.get("recursive_direct_mismatch_count", 0)
        for document in documents),
    "high_zero_sample_count": len(hits),
    "high_zero_total_witness_count": sum(document.get("high_zero_count", 0)
                                          for document in documents),
    "high_zero_sample_indices": [document["sample_index"] for document in hits],
    "ordered_sample_sha_merkle_stream_sha256": stream.hexdigest(),
    "scope": "24 deterministic combined states; no full-fibre inference",
}
encoded = (json.dumps(aggregate, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(results / "aggregate.json").write_bytes(encoded)
print("sample_count", sample_count)
print("q7_rank_histogram", json.dumps(aggregate["q7_rank_histogram"],
                                      sort_keys=True))
print("q7_compatible_sample_count", len(compatible))
print("q7_fibre_states_exhausted",
      aggregate["q7_fibre_states_exhausted"])
print("high_zero_sample_count", len(hits))
print("high_zero_total_witness_count",
      aggregate["high_zero_total_witness_count"])
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-WITNESS-FIRST-DIVERSE-AGGREGATE")

