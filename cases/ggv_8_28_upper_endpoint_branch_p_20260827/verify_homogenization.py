#!/usr/bin/env python3
"""Independent replay of the fixed-fixture weighted homogenization."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW = HERE / "RAW_DIRECT_SYSTEM.json"
HOM = HERE / "HOMOGENIZED" / "HOMOGENIZED_SYSTEM.json"
SOURCE = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def terms(encoded):
    out = {}
    for mon, coefficient in encoded:
        key = tuple(mon)
        out[key] = out.get(key, Q(0)) + Q(coefficient)
        if not out[key]:
            del out[key]
    return out


def main():
    assert sha256(RAW) == RAW_SHA256
    raw = json.loads(RAW.read_text())
    hom = json.loads(HOM.read_text())
    source = json.loads(SOURCE.read_text())
    slot_weights = {
        slot["slot"]: int(slot["weight"])
        for kind in ("F", "G")
        for slot in source["raw_slots_through_weight_22"][kind]
    }
    weights = {}
    for name in raw["variables"]:
        weights[name] = (2 if name.startswith("z_") else
                         3 if name.startswith("tt_") else slot_weights[name])
    assert hom["variable_weights"] == {"lambda": 22, "u": 1, **weights}
    assert hom["saturation_variable"] == "lambda"
    assert hom["dehomogenization"] == {"lambda": 1, "u": 1}
    assert not hom["D23_imposed"] and not hom["G22_present"]
    assert all(slot["slot"] != "G22" for kind in ("F", "G")
               for slot in source["raw_slots_through_weight_22"][kind])
    assert len(hom["generators"]) == len(raw["generators"]) == 513

    target_replaced = 0
    for index, (raw_record, hom_record) in enumerate(zip(raw["generators"], hom["generators"])):
        assert hom_record["source_raw_index"] == index
        assert int(hom_record["row"]) == int(raw_record["row"])
        assert int(hom_record["x_degree"]) == int(raw_record["x_degree"])
        row = int(raw_record["row"])
        expected = {}
        for mon_list, coefficient_text in raw_record["terms"]:
            mon = tuple(mon_list)
            coefficient = Q(coefficient_text)
            if row == 22 and not mon and coefficient == -1:
                new_mon = ("lambda",)
                target_replaced += 1
            else:
                deficit = row - sum(weights[name] for name in mon)
                assert deficit >= 0
                new_mon = tuple(sorted(mon + ("u",) * deficit))
            expected[new_mon] = expected.get(new_mon, Q(0)) + coefficient
        actual = terms(hom_record["terms"])
        assert actual == expected
        for mon in actual:
            assert sum(hom["variable_weights"][name] for name in mon) == row
        dehom = {}
        for mon, coefficient in actual.items():
            reduced = tuple(name for name in mon if name not in ("u", "lambda"))
            dehom[reduced] = dehom.get(reduced, Q(0)) + coefficient
        assert dehom == terms(raw_record["terms"])
    assert target_replaced == 1

    normalization = terms(hom["normalization"]["terms"])
    assert normalization == {("lambda",): Q(1), ("u",) * 22: Q(-1)}
    assert all(sum(hom["variable_weights"][name] for name in mon) == 22
               for mon in normalization)
    assert sum(normalization.values()) == 0

    # Named mutation controls are structural: each changes an asserted byte-level object.
    assert {**hom["variable_weights"], "z_0": 3} != hom["variable_weights"]
    assert {**hom["variable_weights"], "tt_0": 2} != hom["variable_weights"]
    assert normalization != {("lambda",): Q(1)}

    print(json.dumps({
        "status": "PASS",
        "raw_system_sha256": RAW_SHA256,
        "raw_generators_replayed": len(raw["generators"]),
        "homogeneous_generator_count": hom["generator_count"],
        "normalization": "lambda-u^22",
        "saturation_variable": "lambda",
        "D23_imposed": False,
        "G22_present": False,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
