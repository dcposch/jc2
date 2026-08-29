#!/usr/bin/env python3
"""Dispatch exactly one component through the frozen r1 compiler."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
from pathlib import Path


R1_COMPILER_SHA256 = "409d0f586e14750df2792ab9c0027dfc4678f4fe1848eba1087dbefbd5ef9ce9"
COMPONENTS = {
    "c8": "C8", "q1": "Q1", "p": "P", "c8_q1": "C8_Q1",
    "c8p02": "C8P02", "q1p02": "Q1P02", "q1p03": "Q1P03",
    "triple02": "TRIPLE02", "triple03": "TRIPLE03",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_r1(path: Path):
    if sha256(path) != R1_COMPILER_SHA256:
        raise SystemExit("R1_COMPILER_SOURCE_DRIFT")
    spec = importlib.util.spec_from_file_location("fitting_census_r1", path)
    if spec is None or spec.loader is None:
        raise SystemExit("R1_COMPILER_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r1-compiler", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--r6-archive", type=Path, required=True)
    parser.add_argument("--component", choices=sorted(COMPONENTS), required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    r1 = load_r1(args.r1_compiler)
    assignment = r1.matrix_assignment(args.matrix)
    members = r1.archive_members(args.r6_archive)
    factors, empty = r1.factor_lookup(members)
    label = COMPONENTS[args.component]
    zeros, factor = r1.component_spec(label, factors)
    content = r1.script(label, assignment, zeros, factor)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    script_name = args.component + ".sing"
    (args.output_dir / script_name).write_text(content)
    prefix = content.split("matrix B=M;", 1)[0]
    (args.output_dir / (args.component + "_parse.sing")).write_text(
        prefix + f'print("FULL_MATRIX_PARSE_PASS={label}");\nquit;\n'
    )
    factor_sha = "NONE" if factor is None else hashlib.sha256(factor.encode()).hexdigest()
    (args.output_dir / "COMPONENT_MANIFEST.tsv").write_text(
        "component|label|zero_variables|factor_sha256|factor|script\n"
        f"{args.component}|{label}|{','.join(zeros) if zeros else 'NONE'}|{factor_sha}|{factor or 'NONE'}|{script_name}\n"
    )
    (args.output_dir / "EMPTY_UNIT_FACTORS.tsv").write_text(
        "family|entry|multiplicity|factor|classification\n" + "\n".join(empty) + "\n"
    )
    print(f"R1_COMPILER_SHA256={sha256(args.r1_compiler)}")
    print(f"COMPONENT={args.component}")
    print(f"LABEL={label}")
    print("COMPONENT_COUNT=1")
    print("UNIT_FACTOR_CENSUS_EXACT=1")
    print("FITTING_COMPONENT_BUILD_PASS")


if __name__ == "__main__":
    main()

