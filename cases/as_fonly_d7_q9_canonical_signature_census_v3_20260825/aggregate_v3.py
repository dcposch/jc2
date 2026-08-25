#!/usr/bin/env python3
"""Aggregate V3 zero-section classifier shards."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter
from pathlib import Path

TOTAL = 3 ** 13
RECORD_BYTES = 4 * 32
results_dir = Path(os.environ["RESULTS_DIR"])
shard_count = int(os.environ["SHARD_COUNT"])

classes = Counter()
class_status = {}
first_index = {}
status_counts = Counter()
q8_rank_counts = Counter()
q7_rank_counts = Counter()
ordered_stream = hashlib.sha256()
shard_payload_stream = hashlib.sha256()
expected_start = 0
state_count = 0
for shard_index in range(shard_count):
    summary_path = results_dir / f"summary_{shard_index:03d}.json"
    records_path = results_dir / f"records_{shard_index:03d}.bin"
    classes_path = results_dir / f"classes_{shard_index:03d}.tsv"
    summary_bytes = summary_path.read_bytes()
    summary = json.loads(summary_bytes)
    assert summary["shard_count"] == shard_count
    assert summary["shard_index"] == shard_index
    assert summary["start"] == expected_start
    assert summary["state_count"] == summary["end"] - summary["start"]
    records = records_path.read_bytes()
    assert len(records) == summary["state_count"] * RECORD_BYTES
    assert hashlib.sha256(records).hexdigest() == summary["records_sha256"]
    ordered_stream.update(records)
    shard_payload_stream.update(hashlib.sha256(summary_bytes).digest())
    shard_payload_stream.update(hashlib.sha256(records).digest())
    shard_payload_stream.update(hashlib.sha256(classes_path.read_bytes()).digest())
    status_counts.update(summary["status_histogram"])
    q8_rank_counts.update(summary["q8_rank_histogram"])
    q7_rank_counts.update(summary["q7_rank_histogram"])
    for line in classes_path.read_text().splitlines():
        signature, count_text, first_text, status = line.split("\t")
        count, first = int(count_text), int(first_text)
        classes[signature] += count
        first_index[signature] = min(first, first_index.get(signature, first))
        if signature in class_status:
            assert class_status[signature] == status
        class_status[signature] = status
    expected_start = summary["end"]
    state_count += summary["state_count"]

assert expected_start == TOTAL and state_count == TOTAL
assert sum(classes.values()) == TOTAL == sum(status_counts.values())

global_classes = results_dir / "classes.tsv"
with global_classes.open("w") as handle:
    for signature in sorted(classes):
        handle.write(f"{signature}\t{classes[signature]}\t"
                     f"{first_index[signature]}\t{class_status[signature]}\n")
representatives = results_dir / "representatives.tsv"
with representatives.open("w") as handle:
    handle.write("signature\tfirst_state_index\tclass_size\tstatus\n")
    for signature in sorted(classes, key=lambda item: first_index[item]):
        handle.write(f"{signature}\t{first_index[signature]}\t"
                     f"{classes[signature]}\t{class_status[signature]}\n")

histogram = Counter(classes.values())
largest = sorted(classes.items(), key=lambda item: (-item[1], first_index[item[0]]))[:64]
aggregate = {
    "total_expected": TOTAL,
    "state_count": state_count,
    "shard_count": shard_count,
    "record_bytes": RECORD_BYTES,
    "status_histogram": dict(sorted(status_counts.items())),
    "q8_rank_histogram": dict(sorted(q8_rank_counts.items())),
    "q7_rank_histogram": dict(sorted(q7_rank_counts.items())),
    "signature_class_count": len(classes),
    "class_size_histogram": {str(size): count
                              for size, count in sorted(histogram.items())},
    "largest_classes": [{"signature": signature, "size": size,
                          "first_state_index": first_index[signature],
                          "status": class_status[signature]}
                         for signature, size in largest],
    "ordered_fixed_record_stream_sha256": ordered_stream.hexdigest(),
    "shard_payload_merkle_stream_sha256": shard_payload_stream.hexdigest(),
    "classes_tsv_sha256": hashlib.sha256(global_classes.read_bytes()).hexdigest(),
    "representatives_tsv_sha256": hashlib.sha256(
        representatives.read_bytes()).hexdigest(),
    "scope": "exact zero-section integer-carry/source/RREF presentation only",
    "full_19d_fibre_equivalence_proved": False,
}
encoded = (json.dumps(aggregate, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(results_dir / "aggregate.json").write_bytes(encoded)
print("state_count", state_count)
print("status_histogram", json.dumps(aggregate["status_histogram"], sort_keys=True))
print("rank_histograms", json.dumps(aggregate["q8_rank_histogram"], sort_keys=True),
      json.dumps(aggregate["q7_rank_histogram"], sort_keys=True))
print("signature_class_count", len(classes))
print("class_size_histogram", json.dumps(aggregate["class_size_histogram"],
                                          sort_keys=True))
print("ordered_fixed_record_stream_sha256",
      aggregate["ordered_fixed_record_stream_sha256"])
print("classes_tsv_sha256", aggregate["classes_tsv_sha256"])
print("aggregate_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q9-CANONICAL-SIGNATURE-V3-AGGREGATE")

