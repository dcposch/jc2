#!/usr/bin/env python3
"""Independent exact replay of every row-RREF generator from raw bytes."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
RAW = HERE / "RAW_DIRECT_SYSTEM.json"
RREF = HERE / "ROW_RREF/ROW_RREF_SYSTEM.json"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
RREF_SHA256 = "9b1d9f83e369bbd43a329d98f450a525052ec526fcd72fbd40195ccc43849759"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(encoded):
    return {tuple(monomial): Q(coefficient) for monomial, coefficient in encoded}


def add_scaled(target, source, scalar):
    for monomial, coefficient in source.items():
        target[monomial] = target.get(monomial, Q(0)) + scalar * coefficient
        if not target[monomial]:
            del target[monomial]


def main():
    assert sha256(RAW) == RAW_SHA256
    assert sha256(RREF) == RREF_SHA256
    raw = json.loads(RAW.read_text())
    rref = json.loads(RREF.read_text())
    assert rref["authoritative_raw_system_sha256"] == RAW_SHA256
    assert rref["variables"] == rref["pivot_variables"] + rref["free_variables"]
    assert set(rref["variables"]) == set(raw["variables"])
    assert rref["pivot_count"] == 202
    assert rref["free_variable_count"] == 101
    raw_polys = [decode(record["terms"]) for record in raw["generators"]]
    row_counts = {}
    for record in rref["generators"]:
        replay = {}
        for raw_index, coefficient in record["raw_combination"]:
            assert 0 <= raw_index < len(raw_polys)
            add_scaled(replay, raw_polys[raw_index], Q(coefficient))
            assert raw["generators"][raw_index]["row"] == record["source_row"]
        assert replay == decode(record["terms"]), (record["source_row"], record["rref_row"])
        row_counts[str(record["source_row"])] = row_counts.get(str(record["source_row"]), 0) + 1
    assert sum(row_counts.values()) == rref["generator_count"] == 497
    print(json.dumps({
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-ROW-RREF-REPLAY-v1",
        "status": "PASS",
        "raw_system_sha256": RAW_SHA256,
        "row_rref_system_sha256": RREF_SHA256,
        "generator_combinations_replayed": rref["generator_count"],
        "pivots": rref["pivot_count"],
        "free_variables": rref["free_variable_count"],
        "row_counts": row_counts,
        "D23_imposed": False,
        "G22_present": False,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
