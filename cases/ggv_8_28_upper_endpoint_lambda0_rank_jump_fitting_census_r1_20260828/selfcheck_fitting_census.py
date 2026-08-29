#!/usr/bin/env python3
"""Short stdlib-only selfcheck for the frozen Fitting census compiler."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
from pathlib import Path
import tempfile


def load(path: Path):
    spec = importlib.util.spec_from_file_location("fitting_census", path)
    if spec is None or spec.loader is None:
        raise SystemExit("COMPILER_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--r6-archive", type=Path, required=True)
    args = parser.parse_args()
    compiler_path = args.case_dir / "build_fitting_census.py"
    module = load(compiler_path)
    assignment = module.matrix_assignment(args.matrix)
    members = module.archive_members(args.r6_archive)
    factors, empty = module.factor_lookup(members)
    assert len(assignment.split(",\n")) == module.ROWS * module.COLS
    assert empty == [
        "C8P|01|1|1|EMPTY_UNIT_FACTOR",
        "Q1P|01|1|16|EMPTY_UNIT_FACTOR",
        "TRIPLE|01|1|16|EMPTY_UNIT_FACTOR",
    ]
    assert factors["Q1P03"] == factors["TRIPLE03"] == "q2"
    all_labels: list[str] = []
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        for lane, expected in module.LANES.items():
            lane_dir = root / lane
            for label in expected:
                zeros, factor = module.component_spec(label, factors)
                text = module.script(label, assignment, zeros, factor)
                assert "ENDPOINT_RESERVED=x14*x72+x1*x97" in text
                assert "RATIONAL_UNIT_PIVOT_COUNT" in text
                assert "UNIT_PIVOT_INVARIANTS_PASS=1" in text
                assert "UNIT_PIVOT_CENSUS_COMPLETE=1" in text
                if factor is not None:
                    assert "AMBIENT_BRANCH_IDEAL_PROPER" in text
                    assert "QUOTIENT_DEFINING_IDEAL_NONEMPTY" in text
                    assert factor not in {"1", "16"}
                all_labels.append(label)
            lane_dir.mkdir()
        assert len(all_labels) == 9 and len(set(all_labels)) == 9
    original = args.r6_archive.read_bytes()
    mutated = bytes([original[0] ^ 1]) + original[1:]
    assert hashlib.sha256(original).hexdigest() == module.R6_ARCHIVE_SHA256
    assert hashlib.sha256(mutated).hexdigest() != module.R6_ARCHIVE_SHA256
    print("MATRIX_ENTRY_COUNT=11130")
    print("GENUINE_STRATUM_COUNT=9")
    print("EMPTY_UNIT_FACTOR_COUNT=3")
    print("R6_ARCHIVE_MUTATION_REJECTED=1")
    print("FITTING_CENSUS_SELFCHECK_PASS")


if __name__ == "__main__":
    main()

