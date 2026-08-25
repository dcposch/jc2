#!/usr/bin/env python3
"""Aggregate 66 sampled predecessor-state Q7-fibre classifications."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

result_dir = Path(os.environ["RESULT_DIR"])
paths = sorted(result_dir.glob("state_*.json"))
assert len(paths) == 66
documents = [json.loads(path.read_text()) for path in paths]
assert {(doc["family"], doc["sample_index"]) for doc in documents} == (
    {("q8_kernel", i) for i in range(39)}
    | {("q9_locus", i) for i in range(27)})
summary = {}
for family in ("q8_kernel", "q9_locus"):
    subset = sorted((doc for doc in documents if doc["family"] == family),
                    key=lambda doc: doc["sample_index"])
    rank_hist = Counter(tuple(doc.get("q7_rank_pair", [-1, -1]))
                        for doc in subset)
    zero_hist = Counter(doc.get("high_zero_count", -1) for doc in subset)
    signatures = defaultdict(list)
    for doc in subset:
        signature = (tuple(doc.get("q7_rank_pair", [-1, -1])),
                     doc.get("q7_fiber_dimension", -1),
                     doc.get("high_zero_count", -1),
                     doc.get("quadratic_exact", False),
                     doc.get("quadratic_coefficients_sha256", ""))
        signatures[signature].append(doc["sample_index"])
    summary[family] = {
        "sample_count": len(subset),
        "q8_compatible_count": sum(doc["q8_compatible"] for doc in subset),
        "q7_compatible_count": sum(doc.get("q7_compatible", False)
                                   for doc in subset),
        "q7_rank_histogram": {str(key): value for key, value in rank_hist.items()},
        "high_zero_count_histogram": {str(key): value for key, value in zero_hist.items()},
        "surviving_sample_indices": [doc["sample_index"] for doc in subset
            if doc.get("high_zero_count", 0) > 0],
        "signature_clusters": [
            {"rank_pair": list(signature[0]), "q7_fiber_dimension": signature[1],
             "high_zero_count": signature[2], "quadratic_exact": signature[3],
             "quadratic_coefficients_sha256": signature[4], "sample_indices": indices}
            for signature, indices in sorted(signatures.items(), key=lambda item: item[1])],
    }
stream = b"".join(path.read_bytes() for path in paths)
presentation = {"families": summary, "state_json_stream_sha256":
                hashlib.sha256(stream).hexdigest()}
encoded = (json.dumps(presentation, sort_keys=True, separators=(",", ":")) + "\n").encode()
(result_dir / "aggregate.json").write_bytes(encoded)
print("family_summary", json.dumps(summary, sort_keys=True))
print("state_json_stream_sha256", presentation["state_json_stream_sha256"])
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q8STATE-NEXT-HIGH-AGGREGATE")
