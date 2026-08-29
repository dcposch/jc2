#!/usr/bin/env python3
"""Validate the V8 ordinary-ring recombination certificate."""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V6_FINALIZE = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v6_20260826/finalize_discovery.py"
V6_FINALIZE_SHA256 = "3a68a6d0d61f9a211f40de80fbdd767006c76a4c25ae8f88482d9002ceb84bfd"
CHARACTERISTICS = (0, 32003, 65521, 1000033)
IMPLEMENTATION = "ROW_SHARD_INCREMENTAL_NF_V8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v6_finalize():
    actual = digest(V6_FINALIZE)
    if actual != V6_FINALIZE_SHA256:
        fail(("V6 finalize hash mismatch", actual, V6_FINALIZE_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs0_v6_finalize_frozen", V6_FINALIZE)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V6 finalizer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pre", type=Path, required=True)
    parser.add_argument("--compiler-result", type=Path, required=True)
    parser.add_argument("--certificate-input", type=Path, required=True)
    parser.add_argument("--certificate-stdout", type=Path, required=True)
    parser.add_argument("--certificate-stderr", type=Path, required=True)
    parser.add_argument("--certificate-meta", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    helper = load_v6_finalize()
    v2 = helper.load_v2_validator()
    pre = json.loads(args.pre.read_text())
    compiler = json.loads(args.compiler_result.read_text())
    if pre.get("status") != "PASS-T-RS0-ROW-SHARDS-V8-PREPARED-CERTIFICATE":
        fail("pre-certificate status mismatch")
    for payload, name in ((pre, "pre"), (compiler, "compiler")):
        if payload.get("implementation") != IMPLEMENTATION:
            fail(("implementation mismatch", name, payload.get("implementation")))
        if payload.get("characteristic") != args.characteristic:
            fail(("characteristic mismatch", name))
    if pre.get("compiler_result_sha256") != digest(args.compiler_result):
        fail("pre-certificate compiler hash mismatch")
    if pre.get("certificate_input_sha256") != digest(args.certificate_input):
        fail("certificate input hash mismatch")
    if "qring " in args.certificate_input.read_text() or "quit(" in args.certificate_input.read_text():
        fail("forbidden qring or numeric quit in certificate input")
    if pre.get("candidate_manifest") != list(v2.CANDIDATES) or pre.get("inactive_custody") != list(v2.INACTIVE):
        fail("pre-certificate manifest mismatch")

    meta = v2.parse_meta(args.certificate_meta)
    tag = compiler.get("registered_aws_lane")
    cert_tag = f"{tag}_certificate"
    if meta.get("lane") != cert_tag or meta.get("rc") != "0":
        fail(("certificate AWS metadata mismatch", meta))
    if meta.get("stdout_sha256") != digest(args.certificate_stdout) or meta.get("stderr_sha256") != digest(args.certificate_stderr):
        fail("certificate transcript not bound by AWS metadata")
    transcript = args.certificate_stdout.read_text()
    if "T_RS0_FAIL=" in transcript or any(line.startswith("? ") or line.startswith("   ?") for line in transcript.splitlines()):
        fail("certificate transcript contains failure or Singular diagnostic")
    values: dict[str, list[str]] = defaultdict(list)
    for raw in transcript.splitlines():
        line = raw.strip()
        if line.startswith("T_RS0_") and "=" in line:
            key, value = line.split("=", 1)
            values[key].append(value)
    for key, expected in {
        "T_RS0_CERTIFICATE_SCOPE": "RECOMBINATION_ONLY_NO_REES_OR_CHART_VERDICT",
        "T_RS0_CERTIFICATE_PREFIX_ALGEBRA": "PARENT_RING_NO_QRING",
        "T_RS0_FROZEN_CUSP_CERTIFICATE": "1",
        "T_RS0_FROZEN_OMIT_G10_3_NEGATIVE_CONTROL": "1",
        "T_RS0_DELTA_SPECIAL_FIBRE_ZERO": "1",
        "T_RS0_DELTA_EVEN": "1",
        "T_RS0_DELTA_RHO2_DIVISIBLE": "1",
        "T_RS0_DELTA_MULTIPLY_BACK": "1",
        "T_RS0_CERTIFICATE_ENDPOINT": "PASS_NAVIGATION_ONLY",
    }.items():
        helper.unique(values, key, expected)
    delta_raw = values.get("T_RS0_DELTA_NONZERO")
    terms_raw = values.get("T_RS0_DELTA_QUOTIENT_TERMS")
    if delta_raw not in (["0"], ["1"]) or terms_raw is None or len(terms_raw) != 1:
        fail("certificate Delta support sentinel malformed")
    delta_nonzero = bool(int(delta_raw[0]))
    quotient_terms = int(terms_raw[0])
    if quotient_terms < 0 or delta_nonzero != (quotient_terms > 0):
        fail(("certificate Delta flag/term-count mismatch", delta_nonzero, quotient_terms))

    result = {
        "status": "PASS-T-RS0-ROW-SHARD-INCREMENTAL-NF-V8-NAVIGATION-ONLY",
        "scope": pre["scope"],
        "implementation": IMPLEMENTATION,
        "prefix_algebra": pre["prefix_algebra"],
        "characteristic": args.characteristic,
        "common_sigma_order": pre["common_sigma_order"],
        "grade_nonzero": pre["grade_nonzero"],
        "term_counts": pre["term_counts"],
        "candidate_manifest": pre["candidate_manifest"],
        "discovered_manifest": pre["discovered_manifest"],
        "inactive_custody": pre["inactive_custody"],
        "dependencies": pre["dependencies"],
        "delta_nonzero": delta_nonzero,
        "delta_quotient_terms": quotient_terms,
        "wrong_literal_negative_control": pre["wrong_literal_negative_control"],
        "synthetic_omission_negative_control": pre["synthetic_omission_negative_control"],
        "row_records": pre["row_records"],
        "keep_sha256": pre["keep_sha256"],
        "pre_certificate_sha256": digest(args.pre),
        "certificate_input_sha256": digest(args.certificate_input),
        "certificate_stdout_sha256": digest(args.certificate_stdout),
        "certificate_stderr_sha256": digest(args.certificate_stderr),
        "certificate_meta_sha256": digest(args.certificate_meta),
        "compiler_result_sha256": digest(args.compiler_result),
        "v6_finalize_helper_sha256": V6_FINALIZE_SHA256,
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
