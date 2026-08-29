#!/usr/bin/env python3
"""Compile seven independent AWS row shards from frozen streaming V2."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STREAM = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826/compile_t_rs0_stream.py"
STREAM_SHA256 = "5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112"
PREREG = HERE / "PREREGISTRATION.md"
CHARACTERISTICS = (0, 32003, 65521, 1000033)
SOURCE_COEFFICIENT_TOTAL_DEGREE_BOUND = 8


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_rs0_rowshard_v6_")
    ):
        fail("rowshard V6 compiler requires a registered AWS EC2 lane")
    return tag


def load_stream():
    actual = digest(STREAM)
    if actual != STREAM_SHA256:
        fail(("streaming compiler hash mismatch", actual, STREAM_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs0_stream_frozen", STREAM)
    if spec is None or spec.loader is None:
        fail("cannot import frozen streaming compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def derivative_bound(tails: dict[str, list[list[object]]]) -> tuple[int, int, int]:
    max_factors = 0
    max_loads = 0
    exponent_bound = 0
    for row in range(1, 8):
        for raw_monomial, _ in tails[str(row)]:
            monomial = [int(value) for value in raw_monomial]
            if len(monomial) != 10:
                fail(("tail monomial length", row, monomial))
            factors = sum(monomial[:7])
            loads = sum(monomial[7:])
            max_factors = max(max_factors, factors)
            max_loads = max(max_loads, loads)
            exponent_bound = max(exponent_bound, SOURCE_COEFFICIENT_TOTAL_DEGREE_BOUND * factors + loads)
    if (max_factors, max_loads, exponent_bound) != (9, 1, 72):
        fail(("derivative safety census drift", max_factors, max_loads, exponent_bound))
    return max_factors, max_loads, exponent_bound


def split_rows(lines: list[str]) -> tuple[list[str], dict[int, list[str]]]:
    starts = [
        index for index, line in enumerate(lines)
        if line.startswith("TPhi=") and not line.startswith("TPhi=0;")
    ]
    if len(starts) != 7:
        fail(("stream row-start census", len(starts), 7))
    header = lines[: starts[0]]
    blocks: dict[int, list[str]] = {}
    for row, start in enumerate(starts, 1):
        marker = f'print("T_RS0_ROW_{row}_STREAM_RELEASED=1");'
        try:
            end = lines.index(marker, start) + 1
        except ValueError as exc:
            raise RuntimeError(("missing row release marker", row)) from exc
        if row < 7 and end != starts[row]:
            fail(("unexpected text between row blocks", row, end, starts[row]))
        blocks[row] = lines[start:end]
    if not any(line.startswith('print("T_RS0_PREFIX_SPECIALIZATION_MAP=') for line in lines[starts[-1] :]):
        fail("frozen streaming footer not found")
    return header, blocks


def row_footer(row: int, names: list[str], keep_paths: dict[str, Path]) -> list[str]:
    lines = [
        f'print("T_RS0_SHARD_ROW={row}");',
        'print("T_RS0_PREFIX_SPECIALIZATION_MAP="+string(prefixMap));',
        'print("T_RS0_RHO_DECK_INVARIANCE="+string(deck));',
        'print("T_RS0_WRONG_LITERAL_P_NEGATIVE_CONTROL="+string(wrongLiteralDetected));',
        'print("T_RS0_EXTRACTION_IDENTITIES="+string(extraction));',
        'print("T_RS0_EXTRACTED_SPECIALIZATION_MAP="+string(coefficientMap));',
        'print("T_RS0_SYNTHETIC_ELL1_OMISSION_DETECTED="+string(syntheticOmission));',
    ]
    for grade in range(13):
        lines.append(f'print("T_RS0_GRADE_{grade}_NONZERO="+string(NZ{grade}));')
    for name in names:
        lines.append(f'print("T_RS0_DEP_{name}="+string(dep_{name}));')
    for key, path in keep_paths.items():
        lines += [f'write("{path}",{key});', f'print("T_RS0_KEEP_{key}_WRITTEN=1");']
    lines += [
        'if (prefixMap*deck*extraction*coefficientMap!=1) { print("T_RS0_FAIL=ROW_SOURCE_FIDELITY"); quit(91); }',
        'print("T_RS0_ROW_SHARD_ENDPOINT=PASS_NAVIGATION_ONLY");',
        "quit;",
    ]
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    args = parser.parse_args()
    tag = require_aws()
    stream = load_stream()
    old = stream.load_old()
    for source, expected in old.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("transitive frozen source mismatch", str(source), actual, expected))
    tails = json.loads(old.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != old.EXPECTED_CANONICAL_TAILS:
        fail("canonical tails mismatch")
    max_factors, max_loads, exponent_bound = derivative_bound(tails)
    if args.characteristic and args.characteristic <= exponent_bound:
        fail(("characteristic does not license derivative support test", args.characteristic, exponent_bound))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    full_path = output / f"full_stream_source_{label}.sing"
    manifest = stream.emit(full_path, args.characteristic, tails, old)
    full_lines = full_path.read_text().splitlines()
    header, blocks = split_rows(full_lines)
    implementation_line = 'print("T_RS0_IMPLEMENTATION=ROW_STREAM_V2");'
    if header.count(implementation_line) != 1:
        fail(("implementation sentinel census", header.count(implementation_line), 1))
    header = [
        'print("T_RS0_IMPLEMENTATION=ROW_SHARD_DIFFSCAN_V6");' if line == implementation_line else line
        for line in header
    ]
    names = manifest["candidate_manifest"] + manifest["inactive_custody"]
    row_hashes: dict[str, str] = {}
    keep_files: dict[str, str] = {}
    for row in range(1, 8):
        body_text = "\n".join(blocks[row]) + "\n"
        replacements = 0
        for name in names:
            before = f"if (subst(TPhi,{name},0)-TPhi!=0) {{ dep_{name}=1; }}"
            after = f"if (diff(TPhi,{name})!=0) {{ dep_{name}=1; }}"
            if body_text.count(before) != 1:
                fail(("row dependency source census", row, name, body_text.count(before)))
            body_text = body_text.replace(before, after)
            replacements += 1
        if replacements != 83 or body_text.count("if (diff(TPhi,") != 83:
            fail(("row derivative replacement census", row, replacements, body_text.count("if (diff(TPhi,")))
        keeps: dict[str, Path] = {}
        for grade, keep_row in ((10, 2), (10, 3), (12, 6)):
            if row == keep_row:
                for prefix in ("KeepT", "KeepF"):
                    key = f"{prefix}{grade}_{row}"
                    path = output / f"{key}.poly"
                    keeps[key] = path
                    keep_files[key] = str(path)
        program = header + body_text.rstrip("\n").splitlines() + row_footer(row, names, keeps)
        if sum(line.startswith("TPhi=") for line in program) != 1:
            fail(("row shard TPhi census", row))
        path = output / f"t_rs0_row{row}_{label}.sing"
        path.write_text("\n".join(program) + "\n")
        row_hashes[str(row)] = digest(path)
    full_path.unlink()

    result = {
        "status": "PASS-T-RS0-ROW-SHARD-COMPILER",
        "scope": "SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "implementation": "ROW_SHARD_DIFFSCAN_V6",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(old.TAILS),
        "canonical_tails_sha256": old.EXPECTED_CANONICAL_TAILS,
        "reviewed_compiler_sha256": stream.OLD_SHA256,
        "implementation_review_sha256": stream.REVIEW_SHA256,
        "streaming_compiler_sha256": STREAM_SHA256,
        "preregistration_sha256": digest(PREREG),
        "dependency_scan": "FORMAL_DERIVATIVE_WITH_CHARACTERISTIC_BOUND",
        "max_tail_coefficient_factors": max_factors,
        "max_tail_load_factors": max_loads,
        "tested_atom_exponent_bound": exponent_bound,
        "row_input_sha256": row_hashes,
        "keep_files": keep_files,
        **manifest,
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
