#!/usr/bin/env python3
"""Exact active-four plus one Q7 compatibility shard over F3."""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e"
assert hashlib.sha256(PARENT.read_bytes()).hexdigest() == EXPECTED_PARENT_SHA

os.environ["STATE_FAMILY"] = "q8_kernel"
os.environ["SAMPLE_INDEX"] = "0"
os.environ["OUTPUT_JSON"] = os.environ["BOOTSTRAP_JSON"]
spec = importlib.util.spec_from_file_location("frozen_state_parent", PARENT)
parent = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(parent)


def ternary(index, width=5):
    values = []
    for _ in range(width):
        values.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(values)


forced_q9 = {10, 11, 12, 13, 15, 17}
free_q9 = tuple(i for i in range(19) if i not in forced_q9)
inactive_t = tuple(i for i in free_q9 if i not in (6, 8))
inactive_s = tuple(i for i in range(19) if i not in (15, 17))
coordinates = tuple(("t", i) for i in inactive_t) + tuple(("s", i) for i in inactive_s)
assert len(free_q9) == 13 and len(coordinates) == 28

shard = int(os.environ["SHARD_INDEX"])
assert 0 <= shard < len(coordinates)
kind, fifth_index = coordinates[shard]
fifth_name = f"{kind}{fifth_index}"

records = []
matrix_hashes = {}
rank_pairs = {}
for point_index in range(3 ** 5):
    t6, t8, s15, s17, u = ternary(point_index)
    t = [0] * 19
    t[17] = 1
    t[6], t[8] = t6, t8
    if kind == "t":
        t[fifth_index] = u
    xvalues = parent.add_vector(parent.q9_origin, parent.q9_kernel, t,
                                reduce=True)
    A22, b22 = parent.matrix_and_rhs(parent.transition_rows, xvalues,
                                     parent.q8_variable_count)
    rank22, augmented22, _p22, _w22, y0 = parent.rref_solve(A22, b22)
    assert (rank22, augmented22) == (13, 13) and y0 is not None
    full_rank, full_kernel = parent.kernel_basis(A22)
    assert full_rank == 13 and len(full_kernel) == 19
    s = [0] * 19
    s[15], s[17] = s15, s17
    if kind == "s":
        s[fifth_index] = u
    yvalues = parent.add_vector(y0, full_kernel, s, reduce=True)
    assert parent.source_rows(parent.source_data, xvalues) == [0] * 23
    assert parent.transition_rows(xvalues, yvalues) == [0] * 22
    parent.xvalues, parent.yvalues = xvalues, yvalues
    A7, b7 = parent.affine_matrix(parent.q7_rows, 18)
    rank7, augmented7, _p7, _w7, witness = parent.rref_solve(A7, b7)
    flat = bytes(value for line in A7 for value in line)
    matrix_hash = hashlib.sha256(flat).hexdigest()
    matrix_hashes[matrix_hash] = matrix_hashes.get(matrix_hash, 0) + 1
    rank_key = f"{rank7},{augmented7}"
    rank_pairs[rank_key] = rank_pairs.get(rank_key, 0) + 1
    parameters = (t6, t8, s15, s17, u)
    records.append({
        "parameters": list(parameters),
        "compatible": witness is not None,
        "rank_pair": [rank7, augmented7],
        "matrix_sha256": matrix_hash,
        "xvalues": list(xvalues),
        "yvalues": list(yvalues),
    })

compatible = [record for record in records if record["compatible"]]
mixed = [record for record in compatible
         if any(record["parameters"][:4])]
result = {
    "shard_index": shard,
    "fifth_coordinate": fifth_name,
    "point_count": len(records),
    "q7_matrix_hash_histogram": matrix_hashes,
    "q7_rank_pair_histogram": rank_pairs,
    "compatible_count": len(compatible),
    "mixed_cancellation_count": len(mixed),
    "compatible_parameters": [r["parameters"] for r in compatible],
    "mixed_cancellation_parameters": [r["parameters"] for r in mixed],
    "records": records,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("shard_coordinate", shard, fifth_name)
print("point_count", len(records))
print("matrix_hash_count", len(matrix_hashes))
print("rank_pair_histogram", json.dumps(rank_pairs, sort_keys=True))
print("compatible_count", len(compatible))
print("mixed_cancellation_count", len(mixed))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-ACTIVE4-PLUS-ONE-SHARD")

