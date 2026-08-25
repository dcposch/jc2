#!/usr/bin/env python3
"""Fail-closed aggregate/Merkle certificate for corrected Q10 shards."""
from __future__ import annotations

import ast
import hashlib
import sys
from collections import Counter
from pathlib import Path

result_dir = Path(sys.argv[1])
shard_count = int(sys.argv[2]) if len(sys.argv) > 2 else 27
keys = ("visible_parent_total", "N12_visible_survivors",
        "Q11_visible_states", "Q11_full_spectator_solutions",
        "Q10_visible_states", "Q10_full_spectator_solutions")
sums = Counter()
n12_hist, q11_hist, q10_hist = Counter(), Counter(), Counter()
leaves = []
previous_stop = 0
for index in range(shard_count):
    path = result_dir / f"shard_{index:02d}.out"
    payload = path.read_bytes()
    lines = payload.decode().splitlines()
    assert lines[-1] == "PASS-NEXT-TOP10-CARRY-CORRECTED-SHARD"
    parsed = dict(line.partition(" ")[::2] for line in lines)
    assert int(parsed["shard_index"]) == index
    assert int(parsed["shard_count"]) == shard_count
    start, stop = map(int, parsed["shard_range"].split())
    assert start == previous_stop and start < stop
    previous_stop = stop
    for key in keys:
        sums[key] += int(parsed[key])
    n12_hist.update(dict(ast.literal_eval(parsed["N12_per_base_histogram"])))
    q11_hist.update(dict(ast.literal_eval(parsed["Q11_per_base_histogram"])))
    q10_hist.update(dict(ast.literal_eval(parsed["Q10_per_base_histogram"])))
    payload_sha = hashlib.sha256(payload).hexdigest()
    leaves.append(hashlib.sha256(
        b"leaf" + index.to_bytes(4, "big") + bytes.fromhex(payload_sha)
    ).digest())
    print("shard_output_sha256", index, payload_sha)

assert previous_stop == 3 ** 7
assert sums["visible_parent_total"] == 1085103
assert sums["N12_visible_survivors"] == 629115
assert sums["Q11_visible_states"] == 260847
assert sums["Q11_full_spectator_solutions"] == 729 * sums["Q11_visible_states"]
assert sums["Q10_full_spectator_solutions"] == 729 * sums["Q10_visible_states"]
assert sum(n12_hist.values()) == 3 ** 7
assert sum(q11_hist.values()) == 3 ** 7
assert sum(q10_hist.values()) == 3 ** 7
level = leaves
while len(level) > 1:
    if len(level) % 2:
        level.append(level[-1])
    level = [hashlib.sha256(b"node" + level[i] + level[i + 1]).digest()
             for i in range(0, len(level), 2)]
for key in keys:
    print("aggregate_" + key, sums[key])
print("aggregate_N12_per_base_histogram", sorted(n12_hist.items()))
print("aggregate_Q11_per_base_histogram", sorted(q11_hist.items()))
print("aggregate_Q10_per_base_histogram", sorted(q10_hist.items()))
print("ordered_shard_merkle_sha256", level[0].hex())
print("PASS-NEXT-TOP10-CARRY-CORRECTED-SHARD-AGGREGATE")

