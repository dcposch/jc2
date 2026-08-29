#!/usr/bin/env python3
"""Compiler-census repair for the frozen V6 row-shard implementation."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V6_COMPILER = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v6_20260826/compile_t_rs0_rowshard.py"
V6_COMPILER_SHA256 = "9937fcfc61dff1d39029e6653b2be73ab3f835c2bc8bc81405876e54ef10b6bf"
PREREG = HERE / "PREREGISTRATION.md"
CHARACTERISTICS = (0, 32003, 65521, 1000033)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v6():
    actual = digest(V6_COMPILER)
    if actual != V6_COMPILER_SHA256:
        fail(("V6 compiler hash mismatch", actual, V6_COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs0_rowshard_v6_frozen", V6_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V6 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_rows(output: Path, characteristic: int, tag: str) -> dict[str, object]:
    v6 = load_v6()
    stream = v6.load_stream()
    old = stream.load_old()
    for source, expected in old.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("transitive frozen source mismatch", str(source), actual, expected))
    tails = json.loads(old.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != old.EXPECTED_CANONICAL_TAILS:
        fail("canonical tails mismatch")
    max_factors, max_loads, exponent_bound = v6.derivative_bound(tails)
    if characteristic and characteristic <= exponent_bound:
        fail(("characteristic does not license derivative support test", characteristic, exponent_bound))

    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if characteristic == 0 else f"p{characteristic}"
    full_path = output / f"full_stream_source_{label}.sing"
    manifest = stream.emit(full_path, characteristic, tails, old)
    full_lines = full_path.read_text().splitlines()
    header, blocks = v6.split_rows(full_lines)
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
        program = header + body_text.rstrip("\n").splitlines() + v6.row_footer(row, names, keeps)
        formula_assignments = sum(
            line.startswith("TPhi=") and not line.startswith("TPhi=0;")
            for line in program
        )
        release_assignments = sum(line.startswith("TPhi=0;") for line in program)
        if (formula_assignments, release_assignments) != (1, 1):
            fail(("row shard TPhi formula/release census", row, formula_assignments, release_assignments))
        path = output / f"t_rs0_row{row}_{label}.sing"
        path.write_text("\n".join(program) + "\n")
        row_hashes[str(row)] = digest(path)
    full_path.unlink()

    result = {
        "status": "PASS-T-RS0-ROW-SHARD-COMPILER",
        "scope": "SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "implementation": "ROW_SHARD_DIFFSCAN_V6",
        "compiler_successor": "ROW_SHARD_COMPILER_V7",
        "registered_aws_lane": tag,
        "characteristic": characteristic,
        "tails_sha256": digest(old.TAILS),
        "canonical_tails_sha256": old.EXPECTED_CANONICAL_TAILS,
        "reviewed_compiler_sha256": stream.OLD_SHA256,
        "implementation_review_sha256": stream.REVIEW_SHA256,
        "streaming_compiler_sha256": v6.STREAM_SHA256,
        "v6_compiler_sha256": V6_COMPILER_SHA256,
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
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    args = parser.parse_args()
    v6 = load_v6()
    tag = v6.require_aws()
    result = compile_rows(args.output, args.characteristic, tag)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
