#!/usr/bin/env python3
"""Additive fail-closed census repair for the exact V43C5 converter."""

from __future__ import annotations

import copy
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREREG = HERE / "PREREGISTRATION.md"
BASE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_20260827/replay_total_converter_v43c5.py"
BASE_SHA256 = "00d3912a283aaac5319f3e1a6e541ab5e149851c5569663d0b963bf8373d7c1a"
BASE_PREREG = BASE.parent / "PREREGISTRATION.md"
BASE_PREREG_SHA256 = "93328781388f06e47933e193a1be10a5d86b52f3edd422bde0228f38e5364ac0"
V1_FAILURE = BASE.parent / (
    "evidence/v1_failclosed_r6b/run/"
    "max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_"
    "20260827T132557Z_exact_r6b_exact_total_converter.stderr"
)
V1_FAILURE_SHA256 = "7ee399df9a76105ac321aff599fa7109ef062f9f44dc0f62d0031ad10de88d85"
V2_STATUS = "PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5-V2"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_base():
    for path, expected in (
        (BASE, BASE_SHA256),
        (BASE_PREREG, BASE_PREREG_SHA256),
        (V1_FAILURE, V1_FAILURE_SHA256),
    ):
        actual = digest(path) if path.is_file() else "MISSING"
        if actual != expected:
            fail(("V43C5 V1 custody", str(path), actual, expected))
    spec = importlib.util.spec_from_file_location("frozen_v43c5_v1_for_v2", BASE)
    if spec is None or spec.loader is None:
        fail("V43C5 V1 import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


BASE_MODULE = load_base()
ORIGINAL_BUILD_RECORD = BASE_MODULE.build_record
ORIGINAL_RECONSTRUCT = BASE_MODULE.reconstruct_converter


def corrected_total_context(p):
    base = BASE_MODULE
    base.verify_freeze(base.G4_FREEZE, base.G4_FREEZE_SHA256)
    for path, expected in (
        (base.G4_CERTIFICATE, base.G4_CERTIFICATE_SHA256),
        (base.G4_RESULT, base.G4_RESULT_SHA256),
        (base.G4_REVIEW, base.G4_REVIEW_SHA256),
    ):
        actual = digest(path) if path.is_file() else "MISSING"
        if actual != expected:
            fail(("G4 evidence pin", str(path), actual, expected))
    g4 = base.load_module(base.G4_SOURCE, base.G4_SOURCE_SHA256,
                          "frozen_v43g4_converter_v2")
    v43 = base.load_module(g4.V43, g4.V43_SHA256,
                           "frozen_v43_total_converter_v2")
    (parser, _, total_items, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = v43.reconstruct_rows()

    expected_names = {
        f"Tg{grade}_{row}" for grade in range(10, 20) for row in v43.ROWS
    }
    item_names = [item["name"] for item in total_items]
    item_name_set = set(item_names)
    named_set = set(total_hashes)
    if len(expected_names) != 70 or named_set != expected_names:
        fail(("literal named-slot alphabet", len(expected_names),
              sorted(expected_names - named_set), sorted(named_set - expected_names)))
    if len(item_names) != len(item_name_set) or len(item_names) != 59:
        fail(("literal nonzero-row names", len(item_names), len(item_name_set)))
    if not item_name_set < named_set:
        fail("nonzero rows are not a strict subset of named slots")
    zero_names = sorted(named_set - item_name_set)
    if len(zero_names) != 11 or nonzero_general != 59:
        fail(("literal zero/nonzero census", len(zero_names), nonzero_general))

    empty_hash = sha256(v43.canonical_t_polynomial({})).hexdigest()
    zero_hashes = {name: total_hashes[name] for name in zero_names}
    if set(zero_hashes.values()) != {empty_hash}:
        fail(("literal zero-row hash", zero_hashes, empty_hash))
    for item in total_items:
        actual = sha256(v43.canonical_t_polynomial(item["polynomial"])).hexdigest()
        if actual != total_hashes[item["name"]]:
            fail(("literal nonzero-row hash", item["name"], actual,
                  total_hashes[item["name"]]))
    if (len(frozen_hashes), len(variables), len(frozen_variables), general_only) != (
            70, 66, 65, ["ez9"]):
        fail(("literal total census", len(frozen_hashes), len(variables),
              len(frozen_variables), general_only))

    total_rows = {
        item["name"]: g4.ordinary_t_polynomial(item["polynomial"])
        for item in total_items
    }
    if len(total_rows) != 59:
        fail(("literal total nonzero map", len(total_rows)))
    generic = json.loads(base.G4_CERTIFICATE.read_text())
    if (generic.get("identity") != "5*t^6*a1^4=sum_i H_i*Tg_i"
            or generic.get("t_valuation") != 6
            or generic.get("q_t") != 5
            or generic.get("q_at_zero") != 5
            or len(generic.get("multipliers", {})) != 11):
        fail("G4 certificate contract")
    generic_multipliers = {
        name: base.decode_polynomial(encoded)
        for name, encoded in generic["multipliers"].items()
    }
    direct = {}
    for name, multiplier in generic_multipliers.items():
        if name not in total_rows:
            fail(("generic row name", name))
        direct = p.add(direct, p.multiply(multiplier, total_rows[name]))
    target = p.scale(
        p.multiply(p.power(p.variable("t"), 6),
                   p.power(p.variable("a1"), 4)),
        5,
    )
    p.assert_equal("reviewed G4 direct replay V2", direct, target)
    BASE_MODULE._v2_census = {
        "named_names": sorted(named_set),
        "nonzero_names": sorted(item_name_set),
        "zero_names": zero_names,
        "named_hashes": dict(total_hashes),
        "nonzero_hashes": {name: total_hashes[name]
                           for name in sorted(item_name_set)},
        "zero_hashes": zero_hashes,
        "canonical_zero_hash": empty_hash,
    }
    return (g4, total_rows, total_hashes, variables, frozen_variables,
            nonzero_general, generic, generic_multipliers)


def validate_v2_census(record: dict) -> None:
    census = BASE_MODULE._v2_census
    checks = (
        (record.get("literal_named_row_slot_count"), 70, "named slots"),
        (record.get("literal_nonzero_row_count"), 59, "nonzero rows"),
        (record.get("literal_zero_row_count"), 11, "zero rows"),
        (record.get("literal_zero_row_names"), census["zero_names"], "zero names"),
        (record.get("literal_nonzero_row_sha256"), census["nonzero_hashes"],
         "nonzero hashes"),
        (record.get("literal_zero_row_sha256"), census["zero_hashes"],
         "zero hashes"),
        (record.get("canonical_zero_row_sha256"), census["canonical_zero_hash"],
         "canonical zero hash"),
        (record.get("total_row_sha256"), census["named_hashes"], "all hashes"),
    )
    for actual, expected, label in checks:
        if actual != expected:
            fail(("V2 census replay", label, actual, expected))


def census_mutation_rejected(record: dict, operation) -> bool:
    candidate = copy.deepcopy(record)
    operation(candidate)
    try:
        validate_v2_census(candidate)
    except Exception:
        return True
    return False


def patched_build_record(*args, **kwargs):
    record = ORIGINAL_BUILD_RECORD(*args, **kwargs)
    census = BASE_MODULE._v2_census
    record.update({
        "literal_named_row_slot_count": 70,
        "literal_nonzero_row_count": 59,
        "literal_zero_row_count": 11,
        "literal_zero_row_names": census["zero_names"],
        "literal_nonzero_row_sha256": census["nonzero_hashes"],
        "literal_zero_row_sha256": census["zero_hashes"],
        "canonical_zero_row_sha256": census["canonical_zero_hash"],
    })
    validate_v2_census(record)
    zero_name = census["zero_names"][0]
    controls = {
        "deleted_zero_row_name": census_mutation_rejected(
            record, lambda item: item["literal_zero_row_names"].remove(zero_name)),
        "corrupted_zero_row_hash": census_mutation_rejected(
            record, lambda item: item["literal_zero_row_sha256"].__setitem__(
                zero_name, "0" * 64)),
    }
    if not all(controls.values()):
        fail(("V2 census mutation accepted", controls))
    record["v2_census_mutations"] = controls
    return record


def patched_reconstruct(record, *args, **kwargs):
    validate_v2_census(record)
    controls = record.get("v2_census_mutations")
    if controls != {
            "deleted_zero_row_name": True,
            "corrupted_zero_row_hash": True}:
        fail(("V2 census mutation commitment", controls))
    return ORIGINAL_RECONSTRUCT(record, *args, **kwargs)


def main() -> None:
    if digest(PREREG) == digest(BASE_PREREG):
        fail("V2 preregistration did not change")
    BASE_MODULE.PREREG = PREREG
    BASE_MODULE.total_context = corrected_total_context
    BASE_MODULE.build_record = patched_build_record
    BASE_MODULE.reconstruct_converter = patched_reconstruct
    BASE_MODULE.main()

    if len(sys.argv) != 2:
        fail("V2 output argument")
    output = Path(sys.argv[1]).resolve()
    proof_path = output / "total_a1_628_circuit_certificate.json"
    result_path = output / "result.json"
    proof = json.loads(proof_path.read_text())
    result = json.loads(result_path.read_text())
    validate_v2_census(proof)
    if result.get("status") != "PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5":
        fail(("V1 algebra status", result.get("status")))
    census = BASE_MODULE._v2_census
    result.update({
        "status": V2_STATUS,
        "literal_named_row_slot_count": 70,
        "literal_nonzero_row_count": 59,
        "literal_zero_row_count": 11,
        "literal_zero_row_names": census["zero_names"],
        "canonical_zero_row_sha256": census["canonical_zero_hash"],
        "v2_census_mutations": proof["v2_census_mutations"],
        "v2_preregistration_sha256": digest(PREREG),
        "v2_producer_sha256": digest(Path(__file__)),
        "base_v1_producer_sha256": BASE_SHA256,
        "base_v1_failclosed_stderr_sha256": V1_FAILURE_SHA256,
    })
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(V2_STATUS)
    print("V2_PROOF_SHA256=" + digest(proof_path))
    print("V2_RESULT_SHA256=" + digest(result_path))
    print("V2_ZERO_ROWS=" + ",".join(census["zero_names"]))


if __name__ == "__main__":
    main()
