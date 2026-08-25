#!/usr/bin/env python3
"""Compute exact global sub-signature classes from a completed V3 census."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

TOTAL = 3 ** 13
WIDTH = 128
PARAMETER_NAMES = tuple([f"t{i}" for i in range(10)] + ["t14", "t16", "t18"])
results = Path(os.environ["INPUT_RESULTS_DIR"])
output_dir = Path(os.environ["OUTPUT_DIR"])
output_dir.mkdir(parents=True, exist_ok=True)
shard_count = int(os.environ["SHARD_COUNT"])

full_expected = {}
for line in (results / "classes.tsv").read_text().splitlines():
    signature, count, first, status = line.split("\t")
    full_expected[bytes.fromhex(signature)] = (int(count), int(first), status)

names = ("carry", "q8_rref", "q7_rref")
counts = {name: Counter() for name in names}
firsts = {name: {} for name in names}
statuses = {name: defaultdict(Counter) for name in names}
full_seen = Counter()
full_coordinate_masks = {digest: [0] * len(PARAMETER_NAMES)
                         for digest in full_expected}
stream = hashlib.sha256()
state_index = 0
criterion_mismatches = []
criterion_mismatch_count = 0
for shard_index in range(shard_count):
    payload = (results / f"records_{shard_index:03d}.bin").read_bytes()
    assert len(payload) % WIDTH == 0
    stream.update(payload)
    for offset in range(0, len(payload), WIDTH):
        full, carry, q8, q7 = (payload[offset + 32 * i:offset + 32 * (i + 1)]
                               for i in range(4))
        assert full in full_expected
        status = full_expected[full][2]
        t6 = (state_index // (3 ** 6)) % 3
        t8 = (state_index // (3 ** 8)) % 3
        predicted_status = "q7_compatible" if t6 == t8 == 0 else "q7_incompatible"
        if status != predicted_status:
            criterion_mismatch_count += 1
            if len(criterion_mismatches) < 32:
                criterion_mismatches.append({
                    "state_index": state_index, "t6": t6, "t8": t8,
                    "actual": status, "predicted": predicted_status})
        full_seen[full] += 1
        coordinate_masks = full_coordinate_masks[full]
        quotient = state_index
        for coordinate in range(len(PARAMETER_NAMES)):
            coordinate_masks[coordinate] |= 1 << (quotient % 3)
            quotient //= 3
        assert quotient == 0
        for name, digest in zip(names, (carry, q8, q7)):
            counts[name][digest] += 1
            firsts[name].setdefault(digest, state_index)
            statuses[name][digest][status] += 1
        state_index += 1

assert state_index == TOTAL
assert len(full_seen) == len(full_expected)
for digest, (count, _first, _status) in full_expected.items():
    assert full_seen[digest] == count

full_label_class_histogram = Counter()
variation_profile_histogram = Counter()
full_class_failures = []
for digest, (count, first, status) in full_expected.items():
    full_label_class_histogram[status] += 1
    masks = full_coordinate_masks[digest]
    varying = tuple(PARAMETER_NAMES[index] for index, mask in enumerate(masks)
                    if mask & (mask - 1))
    variation_profile_histogram[varying] += 1
    if (count != 27 or len(varying) != 3
            or any(mask not in (1, 2, 4, 7) for mask in masks)):
        full_class_failures.append({
            "signature": digest.hex(), "count": count, "first": first,
            "status": status, "coordinate_masks": masks})

summary = {
    "state_count": state_index,
    "shard_count": shard_count,
    "full_signature_class_count": len(full_seen),
    "full_signature_label_class_histogram":
        dict(sorted(full_label_class_histogram.items())),
    "full_signature_class_size_27_and_coordinate_cube_failure_count":
        len(full_class_failures),
    "full_signature_class_first_failures": full_class_failures[:32],
    "full_signature_variation_profile_histogram": {
        ",".join(profile): count
        for profile, count in sorted(variation_profile_histogram.items())},
    "ordered_fixed_record_stream_sha256": stream.hexdigest(),
    "q7_zero_section_criterion": "q7_compatible iff t6=t8=0",
    "q7_zero_section_criterion_mismatch_count": criterion_mismatch_count,
    "q7_zero_section_criterion_first_mismatches": criterion_mismatches,
    "scope": "subsignature incidence only; no full-19d equivalence",
}
for name in names:
    path = output_dir / f"{name}_classes.tsv"
    with path.open("w") as handle:
        handle.write("signature\tcount\tfirst_state_index\tstatus_histogram\n")
        for digest in sorted(counts[name], key=lambda item: firsts[name][item]):
            handle.write(f"{digest.hex()}\t{counts[name][digest]}\t"
                         f"{firsts[name][digest]}\t"
                         f"{json.dumps(dict(sorted(statuses[name][digest].items())), separators=(',', ':'))}\n")
    histogram = Counter(counts[name].values())
    summary[f"{name}_class_count"] = len(counts[name])
    summary[f"{name}_class_size_histogram"] = {
        str(size): number for size, number in sorted(histogram.items())}
    summary[f"{name}_classes_tsv_sha256"] = hashlib.sha256(
        path.read_bytes()).hexdigest()

encoded = (json.dumps(summary, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(output_dir / "subsignature_summary.json").write_bytes(encoded)
print("state_count", state_index)
print("full_signature_class_count", len(full_seen))
print("full_signature_label_class_histogram",
      json.dumps(summary["full_signature_label_class_histogram"], sort_keys=True))
print("full_signature_class_size_27_and_coordinate_cube_failure_count",
      len(full_class_failures))
print("full_signature_variation_profile_histogram",
      json.dumps(summary["full_signature_variation_profile_histogram"],
                 sort_keys=True))
for name in names:
    print(name + "_class_count", summary[name + "_class_count"])
    print(name + "_class_size_histogram",
          json.dumps(summary[name + "_class_size_histogram"], sort_keys=True))
print("ordered_fixed_record_stream_sha256", stream.hexdigest())
print("q7_zero_section_criterion_mismatch_count", criterion_mismatch_count)
print("summary_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q9-SUBSIGNATURE-REFINEMENT")
