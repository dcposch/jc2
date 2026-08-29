#!/usr/bin/env python3
"""Stdlib-only selfcheck for the one-component dispatcher."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"IMPORT_FAILURE:{name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--r1-compiler", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--r6-archive", type=Path, required=True)
    parser.add_argument("--component", required=True)
    args = parser.parse_args()
    dispatch = load(args.case_dir / "build_component.py", "dispatch")
    if args.component not in dispatch.COMPONENTS:
        raise SystemExit("COMPONENT_NOT_FROZEN")
    r1 = dispatch.load_r1(args.r1_compiler)
    assignment = r1.matrix_assignment(args.matrix)
    factors, empty = r1.factor_lookup(r1.archive_members(args.r6_archive))
    label = dispatch.COMPONENTS[args.component]
    zeros, factor = r1.component_spec(label, factors)
    text = r1.script(label, assignment, zeros, factor)
    assert "ENDPOINT_RESERVED=x14*x72+x1*x97" in text
    assert "UNIT_PIVOT_INVARIANTS_PASS=1" in text
    assert "UNIT_PIVOT_CENSUS_COMPLETE=1" in text
    assert len(empty) == 3 and all("EMPTY_UNIT_FACTOR" in item for item in empty)
    if factor is not None:
        assert factor not in {"1", "16"}
        assert "AMBIENT_BRANCH_IDEAL_PROPER" in text
    print(f"COMPONENT={args.component}")
    print(f"LABEL={label}")
    print("SINGLE_COMPONENT_DISPATCH=1")
    print("FITTING_COMPONENT_SELFCHECK_PASS")


if __name__ == "__main__":
    main()

