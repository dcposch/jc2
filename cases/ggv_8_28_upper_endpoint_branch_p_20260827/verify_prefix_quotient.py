#!/usr/bin/env python3
"""Independent exact-Q replay of the reviewed-prefix quotient certificates."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
RAW = HERE / "RAW_DIRECT_SYSTEM.json"
SYSTEM = HERE / "PREFIX_QUOTIENT/PREFIX_QUOTIENT_SYSTEM.json"
SINGULAR = HERE / "PREFIX_QUOTIENT/prefix_quotient_q.sing"

RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
SYSTEM_SHA256 = "8e25502c5f8e7b7397d1799f0502fc3088fd0cb8d3425b832b31aa3cd902b611"
SINGULAR_SHA256 = "afd9565d128417924cb74c46a306bf8d72136a51e2e4f13f695d859eea9837fa"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(encoded):
    return {tuple(monomial): Q(coefficient) for monomial, coefficient in encoded}


def add_scaled(target, source, scalar):
    for monomial, coefficient in source.items():
        value = target.get(monomial, Q(0)) + scalar * coefficient
        if value:
            target[monomial] = value
        elif monomial in target:
            del target[monomial]


def multiply(left, right):
    out = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            value = out.get(monomial, Q(0)) + left_coefficient * right_coefficient
            if value:
                out[monomial] = value
            elif monomial in out:
                del out[monomial]
    return out


def main():
    assert sha256(RAW) == RAW_SHA256
    assert sha256(SYSTEM) == SYSTEM_SHA256
    assert sha256(SINGULAR) == SINGULAR_SHA256
    raw = json.loads(RAW.read_text())
    system = json.loads(SYSTEM.read_text())

    assert system["authoritative_raw_system_sha256"] == RAW_SHA256
    assert system["field"] == "Q"
    assert system["variable_count"] == raw["variable_count"] == 303
    assert system["variables"] == raw["variables"]
    assert system["raw_generator_count"] == raw["generator_count"] == 513
    assert system["retained_generator_count"] == 466
    assert system["omitted_generator_count"] == 47
    assert system["endpoint_generator_count"] == 18
    assert not system["D23_imposed"]
    assert not system["G22_present"]

    retained = system["retained_generators"]
    retained_indices = [record["raw_index"] for record in retained]
    assert retained_indices == sorted(retained_indices)
    assert len(retained_indices) == len(set(retained_indices)) == 466
    retained_set = set(retained_indices)
    for quotient_index, record in enumerate(retained):
        assert record["quotient_index"] == quotient_index
        raw_record = raw["generators"][record["raw_index"]]
        assert record["row"] == raw_record["row"]
        assert record["x_degree"] == raw_record["x_degree"]
        assert record["raw_generator_sha256"] == raw_record["sha256"]

    expected_omitted = {
        (4, degree) for degree in range(20, 36)
    } | {
        (5, degree) for degree in range(20, 35)
    } | {
        (6, degree) for degree in range(18, 34)
    }
    certificates = system["omitted_certificates"]
    omitted_indices = {record["raw_index"] for record in certificates}
    assert retained_set.isdisjoint(omitted_indices)
    assert retained_set | omitted_indices == set(range(513))
    assert {(record["row"], record["x_degree"]) for record in certificates} == expected_omitted

    raw_polynomials = [decode(record["terms"]) for record in raw["generators"]]
    cofactor_entries = 0
    cofactor_terms = 0
    replayed = 0
    for record in certificates:
        raw_index = record["raw_index"]
        raw_record = raw["generators"][raw_index]
        assert record["row"] == raw_record["row"]
        assert record["x_degree"] == raw_record["x_degree"]
        assert record["raw_generator_sha256"] == raw_record["sha256"]
        replay = {}
        seen = set()
        for cofactor in record["cofactors"]:
            retained_raw_index = cofactor["retained_raw_index"]
            assert retained_raw_index in retained_set
            assert retained_raw_index not in seen
            seen.add(retained_raw_index)
            encoded = cofactor["terms"]
            digest = hashlib.sha256(
                (json.dumps(encoded, sort_keys=True, separators=(",", ":")) + "\n").encode()
            ).hexdigest()
            assert digest == cofactor["sha256"]
            product = multiply(decode(encoded), raw_polynomials[retained_raw_index])
            add_scaled(replay, product, Q(1))
            cofactor_entries += 1
            cofactor_terms += len(encoded)
        assert replay == raw_polynomials[raw_index], (record["row"], record["x_degree"])
        replayed += 1

    assert replayed == system["omitted_generator_count"] == 47
    assert cofactor_entries == system["cofactor_entry_count"]
    assert cofactor_terms == system["cofactor_term_count"]
    for row in range(7, 23):
        assert all(index in retained_set for index, raw_record in enumerate(raw["generators"])
                   if raw_record["row"] == row)

    print(json.dumps({
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-PREFIX-QUOTIENT-REPLAY-v1",
        "status": "PASS",
        "raw_system_sha256": RAW_SHA256,
        "prefix_quotient_system_sha256": SYSTEM_SHA256,
        "singular_sha256": SINGULAR_SHA256,
        "retained_original_raw_generators": len(retained_indices),
        "omitted_generators_replayed": replayed,
        "cofactor_entries_replayed": cofactor_entries,
        "cofactor_terms_replayed": cofactor_terms,
        "endpoint_generators_retained": 18,
        "D23_imposed": False,
        "G22_present": False,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
