#!/usr/bin/env python3
"""Reconstruct every V3 record and cross-tab its canonical Q8 particular.

This is intentionally a second source pass.  It does not infer anything about
nonzero Q8 fibre coordinates from the canonical RREF particular.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(os.environ["JC2_ROOT"])
V3 = (ROOT / "cases/as_fonly_d7_q9_canonical_signature_census_v3_20260825"
      / "compile_shard_v3.py")
EXPECTED_V3_SHA = (
    "32a9be0f6e09485bb60d2f5dbc75f24509ee6f0a17edc851a69e2517d7659f13")
payload = V3.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_V3_SHA
source = payload.decode()
marker = '\nshard_count = int(os.environ["SHARD_COUNT"])\n'
assert source.count(marker) == 1
scope = {"__file__": str(V3), "__name__": "__source_cross_tab_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(V3), "exec"), scope)

TOTAL = scope["TOTAL"]
RECORD_BYTES = scope["RECORD_BYTES"]
forced = scope["forced"]
free_q9 = scope["free_q9"]
ternary = scope["ternary"]
q9_origin = scope["q9_origin"]
q9_kernel = scope["q9_kernel"]
add_vector = scope["add_vector"]
source_data = scope["source_data"]
source_rows = scope["source_rows"]
matrix_and_rhs = scope["matrix_and_rhs"]
transition_rows = scope["transition_rows"]
q8_variable_count = scope["q8_variable_count"]
rref_solve = scope["rref_solve"]
kernel_basis = scope["kernel_basis"]
affine_matrix = scope["affine_matrix"]
q7_rows = scope["q7_rows"]
q7_parent_scope = scope["q7_parent_scope"]
source_trace = scope["source_trace"]
q8_trace = scope["q8_trace"]
q7_trace = scope["q7_trace"]
rref_digest = scope["rref_digest"]
update_vector = scope["update_vector"]

results = Path(os.environ["INPUT_RESULTS_DIR"])
output_dir = Path(os.environ["OUTPUT_DIR"])
output_dir.mkdir(parents=True, exist_ok=True)
shard_count = int(os.environ["SHARD_COUNT"])
cross_shard_count = int(os.environ["CROSS_SHARD_COUNT"])
cross_shard_index = int(os.environ["CROSS_SHARD_INDEX"])
assert cross_shard_count == shard_count
assert 0 <= cross_shard_index < cross_shard_count

class_metadata = {}
for line in (results / "classes.tsv").read_text().splitlines():
    signature, count, first, status = line.split("\t")
    class_metadata[bytes.fromhex(signature)] = {
        "count": int(count), "first": int(first), "status": status}

active_counts = Counter()
active_statuses = defaultdict(Counter)
active_particular_digests = defaultdict(set)
active_carry_digests = defaultdict(set)
active_full_signatures = defaultdict(set)
active_q8_rrefs = defaultdict(set)
active_q7_rrefs = defaultdict(set)
class_active = {}
class_active_mismatches = []
class_representatives = {}
zero_subset_mismatches = Counter()
state729 = None
ordered_stream = hashlib.sha256()
processed_count = 0
expected_start = None
expected_end = None

for shard_index in range(shard_count):
    if shard_index != cross_shard_index:
        continue
    shard_summary = json.loads(
        (results / f"summary_{shard_index:03d}.json").read_bytes())
    expected_start = shard_summary["start"]
    expected_end = shard_summary["end"]
    state_index = expected_start
    records = (results / f"records_{shard_index:03d}.bin").read_bytes()
    assert len(records) % RECORD_BYTES == 0
    assert len(records) == (expected_end - expected_start) * RECORD_BYTES
    ordered_stream.update(records)
    for offset in range(0, len(records), RECORD_BYTES):
        record = records[offset:offset + RECORD_BYTES]
        full, carry, rref8_record, rref7_record = (
            record[32 * index:32 * (index + 1)] for index in range(4))
        metadata = class_metadata[full]
        parameters = ternary(state_index, 13)
        t = [0] * 19
        for index, value in forced.items():
            t[index] = value
        for index, value in zip(free_q9, parameters):
            t[index] = value
        xvalues = add_vector(q9_origin, q9_kernel, t, reduce=True)
        assert source_rows(source_data, xvalues) == [0] * 23

        A8, b8 = matrix_and_rhs(transition_rows, xvalues, q8_variable_count)
        rank8, augmented8, pivots8, work8, y0 = rref_solve(A8, b8)
        kernel_rank8, kernel8 = kernel_basis(A8)
        assert (rank8, augmented8, kernel_rank8) == (13, 13, rank8)
        assert y0 is not None
        assert transition_rows(xvalues, y0) == [0] * 22
        rref8 = rref_digest("AS-Q8-RREF-V3", A8, b8, rank8,
                            augmented8, pivots8, work8, y0, kernel8)
        assert rref8 == rref8_record

        q7_parent_scope["xvalues"] = xvalues
        q7_parent_scope["yvalues"] = y0
        A7, b7 = affine_matrix(q7_rows, 18)
        rank7, augmented7, pivots7, work7, q7part = rref_solve(A7, b7)
        kernel_rank7, kernel7 = kernel_basis(A7)
        assert kernel_rank7 == rank7 == 9
        if q7part is None:
            assert augmented7 == 10
            status = "q7_incompatible"
            q7probe = (0,) * 18
            assert q7_rows(q7probe) == [value % 3 for value in b7]
            q7_carry = q7_trace(xvalues, y0, q7probe)
            rref7 = rref_digest("AS-Q7-RREF-V3", A7, b7, rank7,
                                augmented7, pivots7, work7, (), kernel7)
        else:
            assert augmented7 == 9
            status = "q7_compatible"
            assert q7_rows(q7part) == [0] * 19
            q7_carry = q7_trace(xvalues, y0, q7part)
            rref7 = rref_digest("AS-Q7-RREF-V3", A7, b7, rank7,
                                augmented7, pivots7, work7, q7part, kernel7)
        assert rref7 == rref7_record
        assert status == metadata["status"]

        q9_digest = source_trace(xvalues)
        q8_carry = q8_trace(xvalues, y0)
        carry_hasher = hashlib.sha256(b"AS-COMBINED-EXACT-CARRY-V3")
        carry_hasher.update(status.encode() + q9_digest + q8_carry + q7_carry)
        reconstructed_carry = carry_hasher.digest()
        assert reconstructed_carry == carry
        full_hasher = hashlib.sha256(b"AS-Q9-ZERO-SECTION-SIGNATURE-V3")
        full_hasher.update(status.encode() + carry + rref8 + rref7)
        assert full_hasher.digest() == full

        particular_hasher = hashlib.sha256(b"AS-Q8-AFFINE-PARTICULAR-V1")
        update_vector(particular_hasher, "y0", y0)
        particular_digest = particular_hasher.digest()
        t6, t8 = parameters[6], parameters[8]
        s15, s17 = y0[15], y0[17]
        active = (s15, t6, s17, t8)
        compatible = status == "q7_compatible"
        active_counts[active] += 1
        active_statuses[active][status] += 1
        active_particular_digests[active].add(particular_digest)
        active_carry_digests[active].add(carry)
        active_full_signatures[active].add(full)
        active_q8_rrefs[active].add(rref8)
        active_q7_rrefs[active].add(rref7)

        if full in class_active and class_active[full] != active:
            if len(class_active_mismatches) < 32:
                class_active_mismatches.append({
                    "signature": full.hex(), "first_active": class_active[full],
                    "later_active": active, "state_index": state_index})
        class_active.setdefault(full, active)
        class_representatives.setdefault(full, {
            "state_index": state_index, "parameters": parameters,
            "active": active, "particular_digest": particular_digest,
            "carry": carry, "rref8": rref8, "rref7": rref7})

        for mask in range(1, 16):
            predicted = all(value == 0 for bit, value in enumerate(active)
                            if mask & (1 << bit))
            if predicted != compatible:
                zero_subset_mismatches[mask] += 1

        if state_index == 729:
            state729 = {
                "state_index": state_index,
                "parameters": list(parameters),
                "active_s15_t6_s17_t8": list(active),
                "status": status,
                "q8_particular": list(y0),
                "q8_particular_sha256": particular_digest.hex(),
                "carry_sha256": carry.hex(),
                "q8_rref_sha256": rref8.hex(),
                "q7_rref_sha256": rref7.hex(),
                "scope": "canonical zero section dead; full Q8 fibre open",
            }
        state_index += 1
        processed_count += 1

assert expected_start is not None and expected_end is not None
assert state_index == expected_end
assert not class_active_mismatches
for signature, metadata in class_metadata.items():
    if signature in class_representatives:
        assert class_representatives[signature]["state_index"] >= metadata["first"]

def digest_set_sha256(values) -> str:
    hasher = hashlib.sha256()
    for value in sorted(values):
        hasher.update(value)
    return hasher.hexdigest()

suffix = f"_{cross_shard_index:03d}"
cross_tab_path = output_dir / f"active4_cross_tab{suffix}.tsv"
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
            + f"\t{len(active_particular_digests[active])}\t"
            + digest_set_sha256(active_particular_digests[active])
            + f"\t{len(active_carry_digests[active])}\t"
            + digest_set_sha256(active_carry_digests[active])
            + f"\t{len(active_full_signatures[active])}"
            + f"\t{len(active_q8_rrefs[active])}"
            + f"\t{len(active_q7_rrefs[active])}\n")

members_path = output_dir / f"active4_members{suffix}.jsonl"
with members_path.open("w") as handle:
    for active in sorted(active_counts):
        handle.write(json.dumps({
            "active": active,
            "q8_particular_digests": sorted(
                value.hex() for value in active_particular_digests[active]),
            "carry_digests": sorted(
                value.hex() for value in active_carry_digests[active]),
            "full_signatures": sorted(
                value.hex() for value in active_full_signatures[active]),
            "q8_rrefs": sorted(value.hex() for value in active_q8_rrefs[active]),
            "q7_rrefs": sorted(value.hex() for value in active_q7_rrefs[active]),
        }, sort_keys=True, separators=(",", ":")) + "\n")

representatives_path = output_dir / f"presentation_representatives{suffix}.tsv"
with representatives_path.open("w") as handle:
    handle.write(
        "signature\tfirst_state_index\tstatus\tparameters_t0_t9_t14_t16_t18\t"
        "s15_t6_s17_t8\tq8_particular_sha256\tcarry_sha256\t"
        "q8_rref_sha256\tq7_rref_sha256\n")
    for signature in sorted(class_representatives,
                            key=lambda item: class_metadata[item]["first"]):
        representative = class_representatives[signature]
        handle.write(
            f"{signature.hex()}\t{representative['state_index']}\t"
            f"{class_metadata[signature]['status']}\t"
            + ",".join(map(str, representative["parameters"])) + "\t"
            + ",".join(map(str, representative["active"])) + "\t"
            + representative["particular_digest"].hex() + "\t"
            + representative["carry"].hex() + "\t"
            + representative["rref8"].hex() + "\t"
            + representative["rref7"].hex() + "\n")

valid_zero_subsets = [
    [name for bit, name in enumerate(("s15", "t6", "s17", "t8"))
     if mask & (1 << bit)]
    for mask in range(1, 16) if zero_subset_mismatches[mask] == 0]
minimal_zero_subsets = [
    subset for subset in valid_zero_subsets
    if not any(set(other) < set(subset) for other in valid_zero_subsets)]
summary = {
    "state_count": processed_count,
    "start": expected_start,
    "end": expected_end,
    "cross_shard_count": cross_shard_count,
    "cross_shard_index": cross_shard_index,
    "source_record_reconstruction_failure_count": 0,
    "full_signature_active4_homogeneity_failure_count":
        len(class_active_mismatches),
    "active4_class_count": len(active_counts),
    "active4_cross_tab_sha256": hashlib.sha256(
        cross_tab_path.read_bytes()).hexdigest(),
    "active4_members_sha256": hashlib.sha256(
        members_path.read_bytes()).hexdigest(),
    "presentation_representatives_sha256": hashlib.sha256(
        representatives_path.read_bytes()).hexdigest(),
    "ordered_fixed_record_stream_sha256": ordered_stream.hexdigest(),
    "zero_subset_mismatch_counts": {
        ",".join(name for bit, name in enumerate(("s15", "t6", "s17", "t8"))
                 if mask & (1 << bit)): zero_subset_mismatches[mask]
        for mask in range(1, 16)},
    "valid_zero_subset_criteria": valid_zero_subsets,
    "minimal_zero_subset_criteria": minimal_zero_subsets,
    "state729": state729,
    "scope": "canonical RREF Q8 particular and Q7 zero section only",
    "full_19d_fibre_equivalence_proved": False,
    "v3_sha256": EXPECTED_V3_SHA,
}
encoded = (json.dumps(summary, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(output_dir / f"source_cross_tab_summary{suffix}.json").write_bytes(encoded)
print("cross_shard_range", cross_shard_index, expected_start, expected_end,
      processed_count)
print("active4_class_count", len(active_counts))
print("full_signature_active4_homogeneity_failure_count",
      len(class_active_mismatches))
print("valid_zero_subset_criteria",
      json.dumps(valid_zero_subsets, separators=(",", ":")))
print("minimal_zero_subset_criteria",
      json.dumps(minimal_zero_subsets, separators=(",", ":")))
print("ordered_fixed_record_stream_sha256", ordered_stream.hexdigest())
print("active4_cross_tab_sha256", summary["active4_cross_tab_sha256"])
print("presentation_representatives_sha256",
      summary["presentation_representatives_sha256"])
print("summary_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q9-SOURCE-CROSS-TAB-SHARD")
