#!/usr/bin/env python3
"""V3: classify one shard without assuming the Q7 zero section survives."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from collections import Counter
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
V2 = (ROOT / "cases/as_fonly_d7_q9_canonical_signature_census_20260825"
      / "compile_shard.py")
EXPECTED_V2_SHA = (
    "77593519c7e47a67f8f2643f7d7f9eb636e51dbdcf1e7f6039ec88b839a14841")
payload = V2.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_V2_SHA
source = payload.decode()
marker = '\nshard_count = int(os.environ["SHARD_COUNT"])\n'
assert source.count(marker) == 1
scope = {"__file__": str(V2), "__name__": "__signature_v2_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(V2), "exec"), scope)

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
q7_parent_scope = scope["scope"]
source_trace = scope["source_trace"]
q8_trace = scope["q8_trace"]
q7_trace = scope["q7_trace"]
rref_digest = scope["rref_digest"]
update_vector = scope["update_vector"]

shard_count = int(os.environ["SHARD_COUNT"])
shard_index = int(os.environ["SHARD_INDEX"])
assert 1 <= shard_count <= TOTAL and 0 <= shard_index < shard_count
start = TOTAL * shard_index // shard_count
end = TOTAL * (shard_index + 1) // shard_count
results_dir = Path(os.environ["RESULTS_DIR"])
results_dir.mkdir(parents=True, exist_ok=True)

records_path = results_dir / f"records_{shard_index:03d}.bin"
classes = Counter()
class_status = {}
first_index = {}
status_counts = Counter()
q8_rank_counts = Counter()
q7_rank_counts = Counter()
q8_rref_counts = Counter()
q7_rref_counts = Counter()
carry_counts = Counter()
state_stream = hashlib.sha256()

with records_path.open("wb") as records:
    for state_index in range(start, end):
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
        assert kernel_rank8 == rank8
        q8_rank_counts[str((rank8, augmented8))] += 1
        q9_digest = source_trace(xvalues)

        if y0 is None:
            status = "q8_incompatible"
            yprobe = (0,) * q8_variable_count
            q8_carry = q8_trace(xvalues, yprobe)
            rref8 = rref_digest("AS-Q8-RREF-V3", A8, b8, rank8,
                                augmented8, pivots8, work8, (), kernel8)
            q7_carry = hashlib.sha256(b"AS-Q7-NOT-REACHED-V3").digest()
            rref7 = hashlib.sha256(b"AS-Q7-RREF-NOT-REACHED-V3").digest()
            q7_rank_counts["not_reached"] += 1
        else:
            assert transition_rows(xvalues, y0) == [0] * 22
            q8_carry = q8_trace(xvalues, y0)
            rref8 = rref_digest("AS-Q8-RREF-V3", A8, b8, rank8,
                                augmented8, pivots8, work8, y0, kernel8)
            q7_parent_scope["xvalues"] = xvalues
            q7_parent_scope["yvalues"] = y0
            A7, b7 = affine_matrix(q7_rows, 18)
            rank7, augmented7, pivots7, work7, q7part = rref_solve(A7, b7)
            kernel_rank7, kernel7 = kernel_basis(A7)
            assert kernel_rank7 == rank7
            q7_rank_counts[str((rank7, augmented7))] += 1
            if q7part is None:
                assert augmented7 == rank7 + 1
                status = "q7_incompatible"
                q7probe = (0,) * 18
                assert q7_rows(q7probe) == [value % 3 for value in b7]
                q7_carry = q7_trace(xvalues, y0, q7probe)
                rref7 = rref_digest("AS-Q7-RREF-V3", A7, b7, rank7,
                                    augmented7, pivots7, work7, (), kernel7)
            else:
                status = "q7_compatible"
                assert q7_rows(q7part) == [0] * 19
                q7_carry = q7_trace(xvalues, y0, q7part)
                rref7 = rref_digest("AS-Q7-RREF-V3", A7, b7, rank7,
                                    augmented7, pivots7, work7, q7part,
                                    kernel7)

        carry_hasher = hashlib.sha256(b"AS-COMBINED-EXACT-CARRY-V3")
        carry_hasher.update(status.encode() + q9_digest + q8_carry + q7_carry)
        carry_digest = carry_hasher.digest()
        full_hasher = hashlib.sha256(b"AS-Q9-ZERO-SECTION-SIGNATURE-V3")
        full_hasher.update(status.encode() + carry_digest + rref8 + rref7)
        signature = full_hasher.digest()
        record = signature + carry_digest + rref8 + rref7
        assert len(record) == RECORD_BYTES
        records.write(record)
        signature_hex = signature.hex()
        classes[signature_hex] += 1
        if signature_hex in class_status:
            assert class_status[signature_hex] == status
        class_status[signature_hex] = status
        first_index.setdefault(signature_hex, state_index)
        status_counts[status] += 1
        q8_rref_counts[rref8.hex()] += 1
        q7_rref_counts[rref7.hex()] += 1
        carry_counts[carry_digest.hex()] += 1
        update_vector(state_stream, "t", parameters)
        update_vector(state_stream, "x", xvalues)
        state_stream.update(record)

assert records_path.stat().st_size == (end - start) * RECORD_BYTES
classes_path = results_dir / f"classes_{shard_index:03d}.tsv"
with classes_path.open("w") as handle:
    for signature in sorted(classes):
        handle.write(f"{signature}\t{classes[signature]}\t"
                     f"{first_index[signature]}\t{class_status[signature]}\n")

summary = {
    "shard_count": shard_count,
    "shard_index": shard_index,
    "start": start,
    "end": end,
    "state_count": end - start,
    "record_bytes": RECORD_BYTES,
    "records_sha256": hashlib.sha256(records_path.read_bytes()).hexdigest(),
    "state_record_stream_sha256": state_stream.hexdigest(),
    "class_count": len(classes),
    "status_histogram": dict(sorted(status_counts.items())),
    "q8_rank_histogram": dict(sorted(q8_rank_counts.items())),
    "q7_rank_histogram": dict(sorted(q7_rank_counts.items())),
    "q8_rref_class_count": len(q8_rref_counts),
    "q7_rref_class_count": len(q7_rref_counts),
    "carry_class_count": len(carry_counts),
    "v2_sha256": EXPECTED_V2_SHA,
}
summary_bytes = (json.dumps(summary, sort_keys=True, separators=(",", ":"))
                 + "\n").encode()
(results_dir / f"summary_{shard_index:03d}.json").write_bytes(summary_bytes)
print("shard_range_count", shard_index, start, end, end - start)
print("status_histogram", json.dumps(summary["status_histogram"], sort_keys=True))
print("rank_histograms", json.dumps(summary["q8_rank_histogram"], sort_keys=True),
      json.dumps(summary["q7_rank_histogram"], sort_keys=True))
print("class_counts", len(classes), len(carry_counts),
      len(q8_rref_counts), len(q7_rref_counts))
print("records_sha256", summary["records_sha256"])
print("state_record_stream_sha256", summary["state_record_stream_sha256"])
print("summary_sha256", hashlib.sha256(summary_bytes).hexdigest())
print("PASS-AS-Q9-CANONICAL-SIGNATURE-V3-SHARD")
