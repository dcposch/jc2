#!/usr/bin/env python3
"""Add exact grade-10--12 coefficient export to frozen V8 row shards."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
from tempfile import TemporaryDirectory


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V8_COMPILER = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/compile_t_rs0_rowshard_v8.py"
V8_COMPILER_SHA256 = "41484e92ac2c3433562b8f120c922cb8d2bff5bff736c4b5664989c692dc85fa"
PREREG = HERE / "PREREGISTRATION.md"
CHARACTERISTICS = (0, 32003, 65521, 1000033)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v8():
    actual = digest(V8_COMPILER)
    if actual != V8_COMPILER_SHA256:
        fail(("V8 compiler hash mismatch", actual, V8_COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs0_v8_frozen", V8_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V8 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_")
    ):
        fail("V9 coefficient exporter requires a registered AWS EC2 lane")
    return tag


def compile_export(output: Path, characteristic: int, tag: str) -> dict[str, object]:
    v8 = load_v8()
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if characteristic == 0 else f"p{characteristic}"
    coefficient_files: dict[str, str] = {}
    row_hashes: dict[str, str] = {}
    with TemporaryDirectory(prefix="t_rs0_v9_") as temporary:
        staging = (Path(temporary) / "v8_baseline").resolve()
        baseline = v8.compile_rows(staging, characteristic, tag)
        for row in range(1, 8):
            source = staging / f"t_rs0_row{row}_{label}.sing"
            lines: list[str] = []
            export_count = 0
            for line in source.read_text().splitlines():
                line = line.replace(str(staging), str(output))
                lines.append(line)
                if line == 'print("T_RS0_QRING_DISABLED=1");':
                    lines.append('print("T_RS0_COEFFICIENT_EXPORT=V9");')
                for grade in (10, 11, 12):
                    marker = f'print("T_RS0_TERMS_{grade}_{row}="+string(size(Tg)));'
                    if line != marker:
                        continue
                    for prefix, poly in (("T", "Tg"), ("F", "Fg")):
                        key = f"{prefix}g{grade}_{row}"
                        path = output / f"{key}.poly"
                        coefficient_files[key] = str(path)
                        lines += [
                            f'write("{path}",{poly});',
                            f'print("T_RS0_EXPORT_{key}=1");',
                        ]
                        export_count += 1
            if export_count != 6:
                fail(("row export census", row, export_count, 6))
            destination = output / source.name
            text = "\n".join(lines) + "\n"
            if text.count("T_RS0_COEFFICIENT_EXPORT=V9") != 1 or "qring " in text:
                fail(("V9 sentinel or qring census", row))
            destination.write_text(text)
            row_hashes[str(row)] = digest(destination)

    if len(coefficient_files) != 42:
        fail(("coefficient file census", len(coefficient_files), 42))
    keep_files = {
        key: str(output / f"{key}.poly")
        for key in ("KeepT10_2", "KeepF10_2", "KeepT10_3", "KeepF10_3", "KeepT12_6", "KeepF12_6")
    }
    result = {
        **baseline,
        "status": "PASS-T-RS0-COEFFICIENT-EXPORT-V9-COMPILER",
        "registered_aws_lane": tag,
        "export_implementation": "EXACT_COEFFICIENT_EXPORT_V9",
        "v8_compiler_sha256": V8_COMPILER_SHA256,
        "preregistration_sha256": digest(PREREG),
        "row_input_sha256": row_hashes,
        "coefficient_files": coefficient_files,
        "coefficient_file_count": 42,
        "keep_files": keep_files,
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    args = parser.parse_args()
    print(json.dumps(compile_export(args.output, args.characteristic, require_aws()), sort_keys=True))


if __name__ == "__main__":
    main()

