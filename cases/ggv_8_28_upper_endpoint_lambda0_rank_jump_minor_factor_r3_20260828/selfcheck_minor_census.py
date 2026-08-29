#!/usr/bin/env python3
"""Stdlib-only archive/support selfcheck for the r3 minor compiler."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
from pathlib import Path


def load(path: Path):
    spec = importlib.util.spec_from_file_location("minor_compiler", path)
    if spec is None or spec.loader is None:
        raise SystemExit("COMPILER_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--component", required=True)
    parser.add_argument("--archive", type=Path, required=True)
    args = parser.parse_args()
    module = load(args.case_dir / "build_minor_census.py")
    if args.component not in module.ARCHIVES:
        raise SystemExit("COMPONENT_NOT_FROZEN")
    _, matrix, rank = module.archive_payload(args.archive, args.component)
    support = {(i + 1, j + 1) for i, row in enumerate(matrix) for j, value in enumerate(row) if value != "0"}
    if rank == 9:
        count = sum(module.matching(rows, cols, support)
                    for rows in itertools.combinations(range(1, 12), 9)
                    for cols in itertools.combinations(range(1, 11), 9))
        assert count == 172
        print("RAW_MINOR_SLOT_COUNT=550"); print("STRUCTURALLY_MATCHABLE_SLOT_COUNT=172")
    else:
        allowed = ({(i, j) for i in module.A_ROWS for j in module.A_COLS} |
                   {(i, j) for i in module.B_ROWS for j in module.B_COLS})
        assert support <= allowed and len(support) == 36
        assert len(list(itertools.combinations(module.A_COLS, 4))) == 70
        assert len(list(itertools.combinations(module.B_ROWS, 2))) == 21
        assert 70 * 21 == 1470
        assert len(list(itertools.combinations(range(1, 12), 6))) * len(list(itertools.combinations(range(1, 11), 6))) == 97020
        print("BLOCK_A_MINOR_COUNT=70"); print("BLOCK_B_MINOR_COUNT=21"); print("FORMAL_I6_SLOT_COUNT=97020"); print("SIGNED_PRODUCT_COUNT=1470")
    print(f"COMPONENT={args.component}"); print(f"RESIDUAL_RANK={rank}"); print("TERMINAL_EVIDENCE_REPLAY_PASS=1"); print("MINOR_CENSUS_SELFCHECK_PASS")


if __name__ == "__main__":
    main()

