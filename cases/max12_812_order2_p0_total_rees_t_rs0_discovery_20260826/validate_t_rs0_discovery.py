#!/usr/bin/env python3
"""Fail-closed parser for the T-rs-0 discovery output."""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdout", type=Path, required=True)
    parser.add_argument("--compiler-result", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003, 65521), required=True)
    args = parser.parse_args()

    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("status") != "PASS-T-RS0-DISCOVERY-COMPILER":
        fail("compiler status mismatch")
    if compiler.get("characteristic") != args.characteristic:
        fail("compiler characteristic mismatch")
    if compiler.get("input_sha256") != digest(args.input):
        fail("compiled Singular input hash mismatch")

    text = args.stdout.read_text()
    if "T_RS0_FAIL=" in text or any(line.startswith("? ") for line in text.splitlines()):
        fail("Singular failure sentinel or diagnostic")
    values: dict[str, list[str]] = defaultdict(list)
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("T_RS0_") and "=" in line:
            key, value = line.split("=", 1)
            values[key].append(value)

    required = {
        "T_RS0_SOURCE_HASHES": "PASS",
        "T_RS0_SCOPE": "DISCOVERY_ONLY_MOD_SIGMA13_NO_REES_OR_CHART_VERDICT",
        "T_RS0_PREFIX_SPECIALIZATION_MAP": "1",
        "T_RS0_RHO_DECK_INVARIANCE": "1",
        "T_RS0_WRONG_LITERAL_P_NEGATIVE_CONTROL": "1",
        "T_RS0_EXTRACTION_IDENTITIES": "1",
        "T_RS0_EXTRACTED_SPECIALIZATION_MAP": "1",
        "T_RS0_FROZEN_CUSP_CERTIFICATE": "1",
        "T_RS0_FROZEN_OMIT_G10_3_NEGATIVE_CONTROL": "1",
        "T_RS0_DELTA_SPECIAL_FIBRE_ZERO": "1",
        "T_RS0_DELTA_EVEN": "1",
        "T_RS0_DELTA_RHO2_DIVISIBLE": "1",
        "T_RS0_DELTA_MULTIPLY_BACK": "1",
        "T_RS0_SYNTHETIC_ELL1_OMISSION_DETECTED": "1",
        "T_RS0_DISCOVERY_ENDPOINT": "PASS_NAVIGATION_ONLY_MANIFEST_NOT_FROZEN",
    }
    for key, expected in required.items():
        if values.get(key) != [expected]:
            fail(("missing, duplicate, or wrong sentinel", key, values.get(key), expected))

    common_values = values.get("T_RS0_COMMON_ORDER")
    if common_values is None or len(common_values) != 1:
        fail("common-order sentinel missing or duplicate")
    common_order = int(common_values[0])
    if not 0 <= common_order <= 12:
        fail(("no nonzero source row through grade 12", common_order))

    grade_pattern: dict[str, int] = {}
    term_counts: dict[str, int] = {}
    for grade in range(13):
        key = f"T_RS0_GRADE_{grade}_NONZERO"
        if values.get(key) not in (["0"], ["1"]):
            fail(("bad grade support sentinel", key, values.get(key)))
        grade_pattern[str(grade)] = int(values[key][0])
        for row in range(1, 8):
            term_key = f"T_RS0_TERMS_{grade}_{row}"
            if term_key not in values or len(values[term_key]) != 1:
                fail(("term-count sentinel missing or duplicate", term_key))
            count = int(values[term_key][0])
            if count < 0:
                fail(("negative term count", term_key, count))
            term_counts[f"{grade}:{row}"] = count
    if any(grade_pattern[str(grade)] for grade in range(common_order)):
        fail(("nonzero grade below advertised common order", common_order, grade_pattern))
    if grade_pattern[str(common_order)] != 1:
        fail(("advertised common order is zero", common_order, grade_pattern))

    candidates = compiler.get("candidate_manifest")
    inactive = compiler.get("inactive_custody")
    if not isinstance(candidates, list) or not isinstance(inactive, list):
        fail("compiler manifest lists missing")
    if len(candidates) != compiler.get("candidate_manifest_count"):
        fail("compiler candidate count mismatch")
    dependencies: dict[str, int] = {}
    for name in candidates + inactive:
        key = f"T_RS0_DEP_{name}"
        if values.get(key) not in (["0"], ["1"]):
            fail(("dependency sentinel missing, duplicate, or non-Boolean", key, values.get(key)))
        dependencies[name] = int(values[key][0])
    if any(dependencies[name] for name in inactive):
        fail(("a source declared beyond grade 12 unexpectedly occurs", {name: dependencies[name] for name in inactive}))
    discovered = [name for name in candidates if dependencies[name]]
    if not discovered:
        fail("empty discovered source manifest")

    delta_nonzero_values = values.get("T_RS0_DELTA_NONZERO")
    if delta_nonzero_values not in (["0"], ["1"]):
        fail(("delta nonzero sentinel missing or malformed", delta_nonzero_values))

    result = {
        "status": "PASS-T-RS0-DISCOVERY-NAVIGATION-ONLY",
        "scope": "SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "characteristic": args.characteristic,
        "common_sigma_order": common_order,
        "grade_nonzero": grade_pattern,
        "term_counts": term_counts,
        "candidate_manifest": candidates,
        "discovered_manifest": discovered,
        "inactive_custody": inactive,
        "dependencies": dependencies,
        "delta_nonzero": bool(int(delta_nonzero_values[0])),
        "stdout_sha256": digest(args.stdout),
        "input_sha256": digest(args.input),
        "compiler_result_sha256": digest(args.compiler_result),
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
