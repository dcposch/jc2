#!/usr/bin/env python3
"""Fail-closed parser for the row-streaming T-rs-0 AWS transcript."""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path


CANDIDATES = (
    "ell1", "ell2", "ell3", "ell4", "ell5", "ell6", "ell7", "ell8", "ell9", "ell10", "ell11", "ell12",
    "cs", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "cs8", "cs9", "cs10",
    "rs", "rs1", "rs2", "rs3", "rs4", "rs5", "rs6", "rs7", "rs8", "rs9", "rs10",
    "a1", "aa1", "aaa1", "az3", "az4", "az5", "az6", "az7",
    "a0", "aa0", "aaa0", "ac3", "ac4", "ac5", "ac6", "ac7",
    "c1", "e1", "ee1", "ez3", "ez4", "ez5", "ez6", "ez7",
    "c0", "e0", "ee0", "ec3", "ec4", "ec5", "ec6", "ec7",
    "k", "k1", "k2c", "k10_3", "k10_4", "k10_5", "k10_6", "k10_7", "k10_8", "k6",
)
INACTIVE = ("k6_1", "k2", "k2_1", "mu2", "mu4", "mu6", "J")
CHARACTERISTICS = (0, 32003, 65521, 1000033)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def unique(values: dict[str, list[str]], key: str, expected: str) -> None:
    if values.get(key) != [expected]:
        fail(("missing, duplicate, or wrong sentinel", key, values.get(key), expected))


def parse_meta(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        if "=" not in raw:
            continue
        key, value = raw.split("=", 1)
        if key in result:
            fail(("duplicate AWS metadata key", key))
        result[key] = value
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdout", type=Path, required=True)
    parser.add_argument("--meta", type=Path, required=True)
    parser.add_argument("--compiler-result", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    args = parser.parse_args()

    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("status") != "PASS-T-RS0-DISCOVERY-COMPILER":
        fail("compiler status mismatch")
    if compiler.get("implementation") != "ROW_STREAM_V2":
        fail("compiler implementation mismatch")
    if compiler.get("characteristic") != args.characteristic:
        fail("compiler characteristic mismatch")
    if compiler.get("input_sha256") != digest(args.input):
        fail("compiled Singular input hash mismatch")
    if tuple(compiler.get("candidate_manifest", ())) != CANDIDATES:
        fail("compiler candidate list differs from hard-coded reviewed ceiling")
    if tuple(compiler.get("inactive_custody", ())) != INACTIVE:
        fail("compiler inactive list differs from hard-coded reviewed ceiling")
    if compiler.get("candidate_manifest_count") != 76 or compiler.get("ring_variable_count") != 85:
        fail("compiler census mismatch")

    meta = parse_meta(args.meta)
    stdout_digest = digest(args.stdout)
    if meta.get("rc") != "0":
        fail(("AWS lane did not record rc=0", meta.get("rc")))
    if meta.get("stdout_sha256") != stdout_digest:
        fail(("stdout is not the transcript bound by AWS metadata", stdout_digest, meta.get("stdout_sha256")))

    transcript = args.stdout.read_text()
    if "T_RS0_FAIL=" in transcript or any(line.startswith("? ") for line in transcript.splitlines()):
        fail("Singular failure sentinel or diagnostic")
    values: dict[str, list[str]] = defaultdict(list)
    for raw in transcript.splitlines():
        line = raw.strip()
        if line.startswith("T_RS0_") and "=" in line:
            key, value = line.split("=", 1)
            values[key].append(value)

    required = {
        "T_RS0_SOURCE_HASHES": "PASS",
        "T_RS0_SCOPE": "DISCOVERY_ONLY_MOD_SIGMA13_NO_REES_OR_CHART_VERDICT",
        "T_RS0_IMPLEMENTATION": "ROW_STREAM_V2",
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
        unique(values, key, expected)
    for row in range(1, 8):
        unique(values, f"T_RS0_ROW_{row}_STREAM_RELEASED", "1")

    common_raw = values.get("T_RS0_COMMON_ORDER")
    if common_raw is None or len(common_raw) != 1:
        fail("common-order sentinel missing or duplicate")
    common_order = int(common_raw[0])
    if not 0 <= common_order <= 12:
        fail(("no nonzero row through grade 12", common_order))

    grade_pattern: dict[str, int] = {}
    term_counts: dict[str, int] = {}
    for grade in range(13):
        key = f"T_RS0_GRADE_{grade}_NONZERO"
        if values.get(key) not in (["0"], ["1"]):
            fail(("bad grade support sentinel", key, values.get(key)))
        bit = int(values[key][0])
        grade_pattern[str(grade)] = bit
        grade_sum = 0
        for row in range(1, 8):
            term_key = f"T_RS0_TERMS_{grade}_{row}"
            if term_key not in values or len(values[term_key]) != 1:
                fail(("term-count sentinel missing or duplicate", term_key))
            count = int(values[term_key][0])
            if count < 0:
                fail(("negative term count", term_key, count))
            term_counts[f"{grade}:{row}"] = count
            grade_sum += count
        if bit != int(grade_sum > 0):
            fail(("grade bit disagrees with row term counts", grade, bit, grade_sum))
    if any(grade_pattern[str(grade)] for grade in range(common_order)):
        fail(("nonzero grade below common order", common_order, grade_pattern))
    if grade_pattern[str(common_order)] != 1:
        fail(("advertised common order is zero", common_order, grade_pattern))

    dependencies: dict[str, int] = {}
    for name in CANDIDATES + INACTIVE:
        key = f"T_RS0_DEP_{name}"
        if values.get(key) not in (["0"], ["1"]):
            fail(("dependency bit missing, duplicate, or non-Boolean", key, values.get(key)))
        dependencies[name] = int(values[key][0])
    if any(dependencies[name] for name in INACTIVE):
        fail(("inactive source unexpectedly occurs", {name: dependencies[name] for name in INACTIVE}))
    discovered = [name for name in CANDIDATES if dependencies[name]]
    if not discovered:
        fail("empty discovered source manifest")

    delta_nonzero_raw = values.get("T_RS0_DELTA_NONZERO")
    quotient_terms_raw = values.get("T_RS0_DELTA_QUOTIENT_TERMS")
    if delta_nonzero_raw not in (["0"], ["1"]) or quotient_terms_raw is None or len(quotient_terms_raw) != 1:
        fail("delta support sentinel missing or malformed")
    delta_nonzero = bool(int(delta_nonzero_raw[0]))
    quotient_terms = int(quotient_terms_raw[0])
    if quotient_terms < 0 or delta_nonzero != (quotient_terms > 0):
        fail(("delta flag disagrees with quotient term count", delta_nonzero, quotient_terms))

    result = {
        "status": "PASS-T-RS0-STREAM-V2-NAVIGATION-ONLY",
        "scope": "SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "implementation": "ROW_STREAM_V2",
        "characteristic": args.characteristic,
        "common_sigma_order": common_order,
        "grade_nonzero": grade_pattern,
        "term_counts": term_counts,
        "candidate_manifest": list(CANDIDATES),
        "discovered_manifest": discovered,
        "inactive_custody": list(INACTIVE),
        "dependencies": dependencies,
        "delta_nonzero": delta_nonzero,
        "delta_quotient_terms": quotient_terms,
        "stdout_sha256": stdout_digest,
        "meta_sha256": digest(args.meta),
        "input_sha256": digest(args.input),
        "compiler_result_sha256": digest(args.compiler_result),
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
