#!/usr/bin/env python3
"""Fail-closed aggregate/Merkle certificate for Q9 source-state shards."""
from __future__ import annotations

import ast
import hashlib
import sys
from collections import Counter
from pathlib import Path

result_dir = Path(sys.argv[1])
shard_count = int(sys.argv[2]) if len(sys.argv) > 2 else 27
keys = ("visible_parent_total", "N12_visible_survivors",
        "Q11_visible_states", "Q10_visible_states",
        "Q10_states_with_nonzero_M9_quotient",
        "Q9_compatible_predecessor_states", "Q9_relevant_completion_total",
        "Q9_with_C6_spectator_factor")
sums = Counter()
rank_pairs, fiber_hist = Counter(), Counter()
compatible_hist, completion_hist = Counter(), Counter()
leaves = []
previous_stop = 0
first_witness = None
for index in range(shard_count):
    path = result_dir / f"shard_{index:02d}.out"
    payload = path.read_bytes()
    lines = payload.decode().splitlines()
    assert lines[-1] == "PASS-Q9-SOURCE-STATE-SHARD"
    parsed = dict(line.partition(" ")[::2] for line in lines)
    assert int(parsed["shard_index"]) == index
    assert int(parsed["shard_count"]) == shard_count
    start, stop = map(int, parsed["shard_range"].split())
    assert start == previous_stop and start < stop
    previous_stop = stop
    for key in keys:
        sums[key] += int(parsed[key])
    rank_pairs.update(dict(ast.literal_eval(parsed["Q9_rank_pairs"])))
    fiber_hist.update(dict(ast.literal_eval(parsed["Q9_relevant_fiber_histogram"])))
    compatible_hist.update(dict(ast.literal_eval(parsed["Q9_compatible_states_per_base"])))
    completion_hist.update(dict(ast.literal_eval(parsed["Q9_completion_total_per_base"])))
    witness = ast.literal_eval(parsed["Q9_first_witness"])
    if first_witness is None and witness is not None:
        first_witness = witness
    payload_sha = hashlib.sha256(payload).hexdigest()
    leaves.append(hashlib.sha256(
        b"leaf" + index.to_bytes(4, "big") + bytes.fromhex(payload_sha)
    ).digest())
    print("shard_output_sha256", index, payload_sha)

assert previous_stop == 3 ** 7
assert sums["visible_parent_total"] == 1085103
assert sums["N12_visible_survivors"] == 629115
assert sums["Q11_visible_states"] == 260847
assert sums["Q10_visible_states"] == 33225
assert sums["Q9_with_C6_spectator_factor"] == 729 * sums["Q9_relevant_completion_total"]
assert sum(rank_pairs.values()) == sums["Q10_visible_states"]
assert sum(fiber_hist.values()) == sums["Q10_visible_states"]
assert sum(compatible_hist.values()) == 3 ** 7
assert sum(completion_hist.values()) == 3 ** 7
level = leaves
while len(level) > 1:
    if len(level) % 2:
        level.append(level[-1])
    level = [hashlib.sha256(b"node" + level[i] + level[i + 1]).digest()
             for i in range(0, len(level), 2)]
for key in keys:
    print("aggregate_" + key, sums[key])
print("aggregate_Q9_rank_pairs", sorted(rank_pairs.items()))
print("aggregate_Q9_relevant_fiber_histogram", sorted(fiber_hist.items()))
print("aggregate_Q9_compatible_states_per_base", sorted(compatible_hist.items()))
print("aggregate_Q9_completion_total_per_base", sorted(completion_hist.items()))
print("aggregate_Q9_first_witness", first_witness)
print("ordered_shard_merkle_sha256", level[0].hex())
print("PASS-Q9-SOURCE-STATE-AGGREGATE")

