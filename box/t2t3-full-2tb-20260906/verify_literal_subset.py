#!/usr/bin/env python3
"""Verify d2-z55 rowwise against the completed full direct presentation."""
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


def load(path: Path, expected: int):
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == expected
    assert [int(row["emitted_index"]) for row in rows] == list(range(expected))
    keyed = {
        (row["block"], row["label"]): (int(row["terms"]), row["primitive_sha256"])
        for row in rows
    }
    assert len(keyed) == expected
    return rows, keyed


def main() -> None:
    full_dir, subset_dir = map(Path, sys.argv[1:3])
    full_vars = (full_dir / "99-delta2.variables.json").read_bytes()
    subset_vars = (subset_dir / "99-delta2.variables.json").read_bytes()
    assert full_vars == subset_vars
    full_rows, full = load(full_dir / "99-delta2.labels.tsv", 2754)
    subset_rows, subset = load(subset_dir / "99-delta2.labels.tsv", 466)
    assert Counter(row["block"] for row in full_rows) == Counter(
        {"T2_upper": 462, "T2_strict": 1263, "T2_face": 17,
         "T3_recurrence": 1, "T3_strict": 962, "T3_face": 46, "inverse": 3}
    )
    assert Counter(row["block"] for row in subset_rows) == Counter(
        {"T2_upper": 462, "T2_face": 1, "inverse": 3}
    )
    assert [row["label"] for row in subset_rows if row["block"] == "T2_face"] == ["T2_face_55"]
    bad = [key for key, value in subset.items() if full.get(key) != value]
    assert not bad, bad[:5]
    digest = hashlib.sha256()
    matched_indices = []
    full_index = {(row["block"], row["label"]): int(row["emitted_index"]) for row in full_rows}
    for row in subset_rows:
        digest.update(
            f'{row["block"]}\t{row["label"]}\t{row["terms"]}\t{row["primitive_sha256"]}\n'.encode()
        )
        matched_indices.append(full_index[(row["block"], row["label"])])
    result = {
        "schema": "T2T3_LITERAL_SUBSET_CHECK/v1",
        "literal_subset": True,
        "variables_json_byte_identical": True,
        "matched": 466,
        "missing": 0,
        "mismatched": 0,
        "ordered_row_binding_sha256": digest.hexdigest(),
        "matched_full_indices_sha256": hashlib.sha256(
            "".join(f"{index}\n" for index in matched_indices).encode()
        ).hexdigest(),
        "matched_full_index_min": min(matched_indices),
        "matched_full_index_max": max(matched_indices),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
