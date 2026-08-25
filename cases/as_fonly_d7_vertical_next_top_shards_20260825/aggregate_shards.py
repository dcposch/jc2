#!/usr/bin/env python3
"""Fail-closed aggregate and Merkle certificate for ordered shard outputs."""
from __future__ import annotations

import ast
import hashlib
import sys
from collections import Counter
from pathlib import Path

result_dir = Path(sys.argv[1])
shard_count = int(sys.argv[2]) if len(sys.argv) > 2 else 27
required_scalar = (
    "visible_parent_total", "N12_visible_survivors", "N11_visible_states",
    "N11_full_spectator_solutions",
)
sums = Counter()
n12_hist = Counter()
n11_hist = Counter()
leaves = []
previous_stop = 0

for index in range(shard_count):
    path = result_dir / f"shard_{index:02d}.out"
    payload = path.read_bytes()
    lines = payload.decode().splitlines()
    assert lines[-1] == "PASS-NEXT-TOP-CARRY-SHARD"
    parsed = {}
    for line in lines:
        key, _, value = line.partition(" ")
        parsed[key] = value
    assert int(parsed["shard_index"]) == index
    assert int(parsed["shard_count"]) == shard_count
    start, stop = map(int, parsed["shard_range"].split())
    assert start == previous_stop and start < stop
    previous_stop = stop
    for key in required_scalar:
        sums[key] += int(parsed[key])
    n12_hist.update(dict(ast.literal_eval(parsed["N12_per_base_histogram"])))
    n11_hist.update(dict(ast.literal_eval(parsed["N11_per_base_histogram"])))
    payload_sha = hashlib.sha256(payload).hexdigest()
    leaf = hashlib.sha256(
        b"leaf" + index.to_bytes(4, "big") + bytes.fromhex(payload_sha)
    ).digest()
    leaves.append(leaf)
    print("shard_output_sha256", index, payload_sha)

assert previous_stop == 3 ** 7
assert sums["visible_parent_total"] == 1085103
assert sums["N11_full_spectator_solutions"] == 729 * sums["N11_visible_states"]
assert sum(n12_hist.values()) == 3 ** 7
assert sum(n11_hist.values()) == 3 ** 7

level = leaves
while len(level) > 1:
    if len(level) % 2:
        level.append(level[-1])
    level = [hashlib.sha256(b"node" + level[i] + level[i + 1]).digest()
             for i in range(0, len(level), 2)]

for key in required_scalar:
    print("aggregate_" + key, sums[key])
print("aggregate_N12_per_base_histogram", sorted(n12_hist.items()))
print("aggregate_N11_per_base_histogram", sorted(n11_hist.items()))
print("ordered_shard_merkle_sha256", level[0].hex())
print("PASS-NEXT-TOP-CARRY-SHARD-AGGREGATE")
