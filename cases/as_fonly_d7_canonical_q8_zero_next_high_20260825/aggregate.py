#!/usr/bin/env python3
"""Aggregate the 64 canonical zero-section next-high classifications."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

result_dir = Path(os.environ["RESULT_DIR"])
paths = sorted(result_dir.glob("sample_*.json"))
assert len(paths) == 64
documents = [json.loads(path.read_text()) for path in paths]
assert [doc["sample_index"] for doc in documents] == list(range(64))
assert {doc["family"] for doc in documents} == {"canonical_q8_zero_section"}

rank_hist = Counter(tuple(doc.get("q7_rank_pair", [-1, -1]))
                    for doc in documents)
dimension_hist = Counter(doc.get("q7_fiber_dimension", -1)
                         for doc in documents)
zero_hist = Counter(doc.get("high_zero_count", -1) for doc in documents)
signatures = defaultdict(list)
for doc in documents:
    signature = (tuple(doc.get("q7_rank_pair", [-1, -1])),
                 doc.get("q7_fiber_dimension", -1),
                 doc.get("high_zero_count", -1),
                 doc.get("quadratic_exact", False),
                 doc.get("quadratic_coefficients_sha256", ""))
    signatures[signature].append(doc["sample_index"])

stream = b"".join(path.read_bytes() for path in paths)
presentation = {
    "sample_count": len(documents),
    "q7_compatible_count": sum(doc.get("q7_compatible", False)
                               for doc in documents),
    "q7_rank_histogram": {str(key): value for key, value in rank_hist.items()},
    "q7_fibre_dimension_histogram": {str(key): value
                                      for key, value in dimension_hist.items()},
    "high_zero_count_histogram": {str(key): value for key, value in zero_hist.items()},
    "surviving_sample_indices": [doc["sample_index"] for doc in documents
                                  if doc.get("high_zero_count", 0) > 0],
    "signature_clusters": [
        {"rank_pair": list(signature[0]),
         "q7_fibre_dimension": signature[1],
         "high_zero_count": signature[2],
         "quadratic_exact": signature[3],
         "quadratic_coefficients_sha256": signature[4],
         "sample_indices": indices}
        for signature, indices in sorted(signatures.items(), key=lambda item: item[1])
    ],
    "ordered_sample_json_stream_sha256": hashlib.sha256(stream).hexdigest(),
}
encoded = (json.dumps(presentation, sort_keys=True,
                      separators=(",", ":")) + "\n").encode()
(result_dir / "aggregate.json").write_bytes(encoded)
print("sample_count", presentation["sample_count"])
print("q7_compatible_count", presentation["q7_compatible_count"])
print("q7_rank_histogram", json.dumps(presentation["q7_rank_histogram"], sort_keys=True))
print("q7_fibre_dimension_histogram",
      json.dumps(presentation["q7_fibre_dimension_histogram"], sort_keys=True))
print("high_zero_count_histogram",
      json.dumps(presentation["high_zero_count_histogram"], sort_keys=True))
print("surviving_sample_indices", presentation["surviving_sample_indices"])
print("ordered_sample_json_stream_sha256",
      presentation["ordered_sample_json_stream_sha256"])
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-CANONICAL-Q8-ZERO-NEXT-HIGH-AGGREGATE")

