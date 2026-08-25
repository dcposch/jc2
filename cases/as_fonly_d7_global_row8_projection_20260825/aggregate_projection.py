#!/usr/bin/env python3
"""Fail-closed ordered aggregate for the 27 row-8 projection shards."""

import argparse
import collections
import hashlib
import json
from pathlib import Path


EXPECTED_PARENT = (
    "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2"
)
EXPECTED_Q10 = 33_225
EXPECTED_Q9_STATES = 11_881
EXPECTED_Q9_COMPLETIONS = 8_096_356_425_843


def add_counter(target, source):
    for key, value in source.items():
        target[str(key)] += int(value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("shard_root", type=Path)
    parser.add_argument("output_json", type=Path)
    parser.add_argument("--require-v3-controls", action="store_true")
    args = parser.parse_args()

    files = sorted(args.shard_root.glob("shard_*/result.json"))
    assert len(files) == 27, len(files)
    records = [json.loads(path.read_text()) for path in files]
    assert [record["shard_index"] for record in records] == list(range(27))
    assert all(record["shard_count"] == 27 for record in records)
    assert all(record["status"] ==
               "PASS-AS-GLOBAL-ROW8-Q9-PROJECTION-SHARD"
               for record in records)
    assert all(record["parent_sha256"] == EXPECTED_PARENT
               for record in records)
    assert all(record["source_omega_replayed_on_every_projected_point"]
               for record in records)
    assert all(not record["old_13_trit_canonical_chart_reused"]
               for record in records)
    assert [record["structural_range"] for record in records] == [
        [2187 * index // 27, 2187 * (index + 1) // 27]
        for index in range(27)
    ]

    q10 = sum(record["q10_source_state_count"] for record in records)
    q9_states = sum(record["q9_nonempty_predecessor_state_count"]
                    for record in records)
    completions = sum(record["q9_completion_total"] for record in records)
    omega = [sum(record["omega_histogram"][index] for record in records)
             for index in range(3)]
    classes = collections.Counter()
    rank_hist = collections.Counter()
    rank_pair_hist = collections.Counter()
    fibre_hist = collections.Counter()
    per_base = {}
    ordered_stream = hashlib.sha256()
    first_zero = None
    for record in records:
        add_counter(classes, record["zero_locus_classification"])
        if "q9_rank_histogram" in record:
            add_counter(rank_hist, record["q9_rank_histogram"])
        if "q9_rank_pair_histogram" in record:
            add_counter(rank_pair_hist, record["q9_rank_pair_histogram"])
        if "q9_fibre_histogram" in record:
            add_counter(fibre_hist, record["q9_fibre_histogram"])
        for key, value in record["per_base"].items():
            assert key not in per_base
            per_base[key] = value
        ordered_stream.update(record["shard_index"].to_bytes(2, "little"))
        ordered_stream.update(bytes.fromhex(record["stream_sha256"]))
        if first_zero is None and record["first_zero_witness"] is not None:
            first_zero = record["first_zero_witness"]

    assert q10 == EXPECTED_Q10, q10
    assert q9_states == EXPECTED_Q9_STATES, q9_states
    assert completions == EXPECTED_Q9_COMPLETIONS, completions
    assert sum(omega) == completions
    assert omega[0] == omega[1] == omega[2], omega
    assert classes == {"zero-partial": EXPECTED_Q9_STATES}, classes
    assert len(per_base) == 79, len(per_base)
    assert first_zero is not None
    if args.require_v3_controls:
        assert rank_pair_hist
        assert fibre_hist
        assert not rank_hist
    else:
        assert rank_hist

    output = {
        "status": "PASS-AS-GLOBAL-ROW8-Q9-PROJECTION-AGGREGATE",
        "source_shard_count": len(records),
        "parent_sha256": EXPECTED_PARENT,
        "q10_source_state_count": q10,
        "q9_nonempty_predecessor_state_count": q9_states,
        "q9_completion_total": completions,
        "omega_histogram": omega,
        "zero_locus_classification": dict(sorted(classes.items())),
        "compatible_structural_base_count": len(per_base),
        "q9_rank_histogram": dict(sorted(rank_hist.items())),
        "q9_rank_pair_histogram": dict(sorted(rank_pair_hist.items())),
        "q9_fibre_histogram": dict(sorted(fibre_hist.items(),
                                             key=lambda item: int(item[0]))),
        "ordered_shard_stream_digest": ordered_stream.hexdigest(),
        "first_zero_witness": first_zero,
        "source_omega_replayed_on_every_projected_point": True,
        "old_13_trit_canonical_chart_reused": False,
        "preregistration_erratum_required": True,
        "refusal_scope": [
            "no Q8/Q7/Q6/Q5/Q4/Q3 restoration",
            "no all-depth/counterexample/JC2 inference",
        ],
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(output, indent=2, sort_keys=True)
                                + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
