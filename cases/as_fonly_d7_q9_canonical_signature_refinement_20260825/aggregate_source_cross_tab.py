#!/usr/bin/env python3
"""Aggregate source-honest cross-tab shards with exact set union checks."""
from __future__ import annotations

import hashlib
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

TOTAL = 3 ** 13
results = Path(os.environ["INPUT_RESULTS_DIR"])
shards = Path(os.environ["CROSS_SHARD_RESULTS_DIR"])
output_dir = Path(os.environ["OUTPUT_DIR"])
output_dir.mkdir(parents=True, exist_ok=True)
shard_count = int(os.environ["SHARD_COUNT"])

class_metadata = {}
for line in (results / "classes.tsv").read_text().splitlines():
    signature, count, first, status = line.split("\t")
    class_metadata[signature] = {
        "count": int(count), "first": int(first), "status": status}

active_counts = Counter()
active_statuses = defaultdict(Counter)
active_sets = {
    name: defaultdict(set) for name in (
        "q8_particular_digests", "carry_digests", "full_signatures",
        "q8_rrefs", "q7_rrefs")}
class_representatives = {}
class_active = {}
class_active_mismatches = []
zero_subset_mismatches = Counter()
state729 = None
expected_start = 0
state_count = 0
shard_summary_stream = hashlib.sha256()

for shard_index in range(shard_count):
    summary_path = shards / f"source_cross_tab_summary_{shard_index:03d}.json"
    summary_bytes = summary_path.read_bytes()
    summary = json.loads(summary_bytes)
    assert summary["cross_shard_count"] == shard_count
    assert summary["cross_shard_index"] == shard_index
    assert summary["start"] == expected_start
    assert summary["state_count"] == summary["end"] - summary["start"]
    assert summary["source_record_reconstruction_failure_count"] == 0
    assert summary["full_signature_active4_homogeneity_failure_count"] == 0
    shard_summary_stream.update(hashlib.sha256(summary_bytes).digest())
    expected_start = summary["end"]
    state_count += summary["state_count"]
    zero_subset_mismatches.update(summary["zero_subset_mismatch_counts"])
    if summary["state729"] is not None:
        assert state729 is None
        state729 = summary["state729"]

    cross_lines = (shards / f"active4_cross_tab_{shard_index:03d}.tsv"
                   ).read_text().splitlines()
    assert cross_lines[0].startswith("s15\tt6\ts17\tt8\t")
    for line in cross_lines[1:]:
        fields = line.split("\t")
        active = tuple(map(int, fields[:4]))
        active_counts[active] += int(fields[4])
        active_statuses[active].update(json.loads(fields[5]))

    for line in (shards / f"active4_members_{shard_index:03d}.jsonl"
                 ).read_text().splitlines():
        payload = json.loads(line)
        active = tuple(payload.pop("active"))
        for name, values in payload.items():
            active_sets[name][active].update(values)

    rep_lines = (shards / f"presentation_representatives_{shard_index:03d}.tsv"
                 ).read_text().splitlines()
    assert rep_lines[0].startswith("signature\tfirst_state_index\tstatus\t")
    for line in rep_lines[1:]:
        fields = line.split("\t")
        signature = fields[0]
        state_index = int(fields[1])
        active = tuple(map(int, fields[4].split(",")))
        if signature in class_active and class_active[signature] != active:
            if len(class_active_mismatches) < 32:
                class_active_mismatches.append({
                    "signature": signature,
                    "first_active": class_active[signature],
                    "later_active": active,
                    "state_index": state_index})
        class_active.setdefault(signature, active)
        if (signature not in class_representatives
                or state_index < class_representatives[signature][0]):
            class_representatives[signature] = (state_index, line)

assert expected_start == TOTAL == state_count
assert state729 is not None
assert not class_active_mismatches
assert set(class_representatives) == set(class_metadata)
for signature, metadata in class_metadata.items():
    assert class_representatives[signature][0] == metadata["first"]

ordered_stream = hashlib.sha256()
for shard_index in range(shard_count):
    ordered_stream.update((results / f"records_{shard_index:03d}.bin").read_bytes())

def digest_set_sha256(values) -> str:
    hasher = hashlib.sha256()
    for value in sorted(values):
        hasher.update(bytes.fromhex(value))
    return hasher.hexdigest()

cross_tab_path = output_dir / "active4_cross_tab.tsv"
with cross_tab_path.open("w") as handle:
    handle.write(
        "s15\tt6\ts17\tt8\tcount\tstatus_histogram\t"
        "q8_particular_class_count\tq8_particular_set_sha256\t"
        "carry_class_count\tcarry_set_sha256\tfull_signature_class_count\t"
        "q8_rref_class_count\tq7_rref_class_count\n")
    for active in sorted(active_counts):
        handle.write(
            "\t".join(map(str, active)) + f"\t{active_counts[active]}\t"
            + json.dumps(dict(sorted(active_statuses[active].items())),
                         separators=(",", ":"))
            + f"\t{len(active_sets['q8_particular_digests'][active])}\t"
            + digest_set_sha256(active_sets["q8_particular_digests"][active])
            + f"\t{len(active_sets['carry_digests'][active])}\t"
            + digest_set_sha256(active_sets["carry_digests"][active])
            + f"\t{len(active_sets['full_signatures'][active])}"
            + f"\t{len(active_sets['q8_rrefs'][active])}"
            + f"\t{len(active_sets['q7_rrefs'][active])}\n")

representatives_path = output_dir / "presentation_representatives.tsv"
with representatives_path.open("w") as handle:
    first_header = (shards / "presentation_representatives_000.tsv"
                    ).read_text().splitlines()[0]
    handle.write(first_header + "\n")
    for signature in sorted(class_representatives,
                            key=lambda item: class_metadata[item]["first"]):
        handle.write(class_representatives[signature][1] + "\n")

coordinate_names = ("s15", "t6", "s17", "t8")
valid_zero_subsets = []
for mask in range(1, 16):
    name = ",".join(coordinate_names[bit] for bit in range(4)
                    if mask & (1 << bit))
    if zero_subset_mismatches[name] == 0:
        valid_zero_subsets.append(name.split(","))
minimal_zero_subsets = [
    subset for subset in valid_zero_subsets
    if not any(set(other) < set(subset) for other in valid_zero_subsets)]

label_histogram = Counter(metadata["status"]
                          for metadata in class_metadata.values())
summary = {
    "state_count": state_count,
    "shard_count": shard_count,
    "source_record_reconstruction_failure_count": 0,
    "full_signature_active4_homogeneity_failure_count": 0,
    "full_signature_label_class_histogram": dict(sorted(label_histogram.items())),
    "active4_class_count": len(active_counts),
    "active4_cross_tab_sha256": hashlib.sha256(
        cross_tab_path.read_bytes()).hexdigest(),
    "presentation_representatives_sha256": hashlib.sha256(
        representatives_path.read_bytes()).hexdigest(),
    "ordered_fixed_record_stream_sha256": ordered_stream.hexdigest(),
    "shard_summary_merkle_stream_sha256": shard_summary_stream.hexdigest(),
    "zero_subset_mismatch_counts": dict(sorted(zero_subset_mismatches.items())),
    "valid_zero_subset_criteria": valid_zero_subsets,
    "minimal_zero_subset_criteria": minimal_zero_subsets,
    "state729": state729,
    "scope": "canonical RREF Q8 particular and Q7 zero section only",
    "full_19d_fibre_equivalence_proved": False,
}
encoded = (json.dumps(summary, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(output_dir / "source_cross_tab_summary.json").write_bytes(encoded)
print("state_count", state_count)
print("full_signature_label_class_histogram",
      json.dumps(summary["full_signature_label_class_histogram"], sort_keys=True))
print("active4_class_count", len(active_counts))
print("full_signature_active4_homogeneity_failure_count", 0)
print("valid_zero_subset_criteria",
      json.dumps(valid_zero_subsets, separators=(",", ":")))
print("minimal_zero_subset_criteria",
      json.dumps(minimal_zero_subsets, separators=(",", ":")))
print("ordered_fixed_record_stream_sha256", ordered_stream.hexdigest())
print("active4_cross_tab_sha256", summary["active4_cross_tab_sha256"])
print("presentation_representatives_sha256",
      summary["presentation_representatives_sha256"])
print("summary_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q9-SOURCE-CROSS-TAB-AGGREGATE")
