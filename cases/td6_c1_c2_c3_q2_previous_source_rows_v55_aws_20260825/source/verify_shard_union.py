#!/usr/bin/env python3
"""Fail-closed exact union check for immutable V55 or V56 run directories."""

import argparse
import ast
from hashlib import sha256
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=("previous", "current"))
parser.add_argument("runs", nargs="+")
args = parser.parse_args()

prefix = args.mode
expected_total = 54 if args.mode == "previous" else 40
expected_marker = (
    "TD6-A3-Q2-SOURCE-ROW-SHARD-V55 PASS"
    if args.mode == "previous"
    else "TD6-A3-Q2-SOURCE-ROW-SHARD-V56 PASS"
)
records = []
archive_values = set()
for name in args.runs:
    run = Path(name).resolve()
    assert (run / "rc").read_text().strip() == "0", run
    text = (run / "shard.stdout").read_text()
    assert expected_marker in text, run
    fields = {}
    for line in text.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    assert fields["shard_mode"] == args.mode, run
    index = int(fields["shard_index"])
    count = int(fields["shard_count"])
    total = int(fields[f"{prefix}_total_original_row_count"])
    selected = ast.literal_eval(fields[f"{prefix}_shard_indices"])
    assert total == expected_total, (run, total)
    assert selected == [i for i in range(expected_total) if i % count == index]
    assert int(fields[f"{prefix}_shard_selected_count"]) == len(selected)
    assert fields[f"{prefix}_shard_original_row_replay"] == "true"
    archive_values.add((run / "archive.sha256").read_text().strip())
    records.append((index, count, tuple(selected), sha256(text.encode()).hexdigest()))

counts = {record[1] for record in records}
assert len(counts) == 1
count = counts.pop()
assert len(records) == count
assert {record[0] for record in records} == set(range(count))
assert len(archive_values) == 1
covered = [item for record in records for item in record[2]]
assert len(covered) == len(set(covered)) == expected_total
assert sorted(covered) == list(range(expected_total))
records.sort()
digest = sha256(repr(records).encode()).hexdigest()
print(f"mode={args.mode}")
print(f"shard_count={count}")
print(f"total_original_row_count={expected_total}")
print("disjoint=true")
print("exhaustive=true")
print(f"archive_sha256={archive_values.pop()}")
print(f"stdout_union_sha256={digest}")
print("TD6-SOURCE-ROW-SHARD-UNION PASS")
