#!/usr/bin/env python3
"""Fail-closed validator for V9 coefficient exports."""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V6_PREPARE = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v6_20260826/prepare_certificate.py"
V6_PREPARE_SHA256 = "d5f38037a2a1233ceba9e4102e3f65e3690b028d9c627f1dbff8fcee6ccd2e5f"
CHARACTERISTICS = (0, 32003, 65521, 1000033)
SAFE_POLY = re.compile(r"^[A-Za-z0-9_+*/^()\-\s]+$")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_helper():
    if digest(V6_PREPARE) != V6_PREPARE_SHA256:
        fail("V6 prepare helper hash mismatch")
    spec = importlib.util.spec_from_file_location("t_rs0_v6_prepare_frozen", V6_PREPARE)
    if spec is None or spec.loader is None:
        fail("cannot import V6 prepare helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def polynomial(path: Path) -> str:
    if not path.is_file() or path.stat().st_size == 0:
        fail(("missing/empty coefficient", str(path)))
    raw = path.read_text()
    if ";" in raw or '"' in raw or not SAFE_POLY.fullmatch(raw):
        fail(("unsafe coefficient serialization", str(path)))
    return "".join(line.strip() for line in raw.splitlines())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", type=Path, required=True)
    parser.add_argument("--compiler-result", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    helper = load_helper()
    v2 = helper.load_v2_validator()
    compiler = json.loads(args.compiler_result.read_text())
    for key, expected in {
        "status": "PASS-T-RS0-COEFFICIENT-EXPORT-V9-COMPILER",
        "implementation": "ROW_SHARD_INCREMENTAL_NF_V8",
        "export_implementation": "EXACT_COEFFICIENT_EXPORT_V9",
        "characteristic": args.characteristic,
        "qring_used": False,
        "incremental_reduction": True,
        "coefficient_file_count": 42,
    }.items():
        if compiler.get(key) != expected:
            fail(("compiler field mismatch", key, compiler.get(key), expected))
    tag = compiler.get("registered_aws_lane")
    if not isinstance(tag, str) or not tag.startswith("max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_"):
        fail("bad V9 tag")
    row_hashes = compiler.get("row_input_sha256")
    file_map = compiler.get("coefficient_files")
    if not isinstance(row_hashes, dict) or set(row_hashes) != {str(i) for i in range(1, 8)}:
        fail("bad row hash map")
    expected_keys = {f"{prefix}g{grade}_{row}" for prefix in ("T", "F") for grade in (10, 11, 12) for row in range(1, 8)}
    if not isinstance(file_map, dict) or set(file_map) != expected_keys:
        fail("bad coefficient file map")

    job = args.job.resolve()
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    row_records = {}
    for row in range(1, 8):
        program = job / "compiled" / f"t_rs0_row{row}_{label}.sing"
        if digest(program) != row_hashes[str(row)] or "qring " in program.read_text():
            fail(("row program hash/qring failure", row))
        row_tag = f"{tag}_row{row}"
        run = job / "run" / f"row{row}"
        stdout, stderr, meta_path = (run / f"{row_tag}.{suffix}" for suffix in ("stdout", "stderr", "meta"))
        meta = v2.parse_meta(meta_path)
        if meta.get("lane") != row_tag or meta.get("rc") != "0":
            fail(("row metadata mismatch", row, meta))
        if meta.get("stdout_sha256") != digest(stdout) or meta.get("stderr_sha256") != digest(stderr):
            fail(("row transcript hash mismatch", row))
        values = helper.transcript_values(stdout)
        for key, expected in {
            "T_RS0_SOURCE_HASHES": "PASS",
            "T_RS0_IMPLEMENTATION": "ROW_SHARD_INCREMENTAL_NF_V8",
            "T_RS0_PREFIX_ALGEBRA": "PARENT_RING_EXPLICIT_NORMAL_FORM",
            "T_RS0_QRING_DISABLED": "1",
            "T_RS0_COEFFICIENT_EXPORT": "V9",
            "T_RS0_EXPLICIT_NORMAL_FORM": "1",
            "T_RS0_INCREMENTAL_REDUCTION": "1",
            "T_RS0_PREFIX_SPECIALIZATION_MAP": "1",
            "T_RS0_RHO_DECK_INVARIANCE": "1",
            "T_RS0_EXTRACTION_IDENTITIES": "1",
            "T_RS0_EXTRACTED_SPECIALIZATION_MAP": "1",
            "T_RS0_ROW_SHARD_ENDPOINT": "PASS_NAVIGATION_ONLY",
        }.items():
            helper.unique(values, key, expected)
        for grade in (10, 11, 12):
            for prefix in ("T", "F"):
                helper.unique(values, f"T_RS0_EXPORT_{prefix}g{grade}_{row}", "1")
        row_records[str(row)] = {"input_sha256": digest(program), "stdout_sha256": digest(stdout), "stderr_sha256": digest(stderr), "meta_sha256": digest(meta_path)}

    coefficient_hashes = {}
    coefficient_terms = {}
    for key in sorted(expected_keys):
        path = Path(file_map[key]).resolve()
        expected_path = (job / "compiled" / f"{key}.poly").resolve()
        if path != expected_path:
            fail(("coefficient path mismatch", key, str(path), str(expected_path)))
        value = polynomial(path)
        coefficient_hashes[key] = digest(path)
        coefficient_terms[key] = 0 if value == "0" else value.count("+") + value.count("-") + 1
    result = {
        "status": "PASS-T-RS0-EXACT-COEFFICIENT-EXPORT-V9",
        "scope": "GRADES_10_11_12_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "characteristic": args.characteristic,
        "coefficient_file_count": 42,
        "coefficient_sha256": coefficient_hashes,
        "coefficient_term_telemetry": coefficient_terms,
        "row_records": row_records,
        "compiler_result_sha256": digest(args.compiler_result),
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
