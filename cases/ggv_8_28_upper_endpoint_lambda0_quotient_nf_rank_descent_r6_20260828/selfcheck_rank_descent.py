#!/usr/bin/env python3
"""Stdlib-only source and combinatorial selfcheck for r6 rank descent."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
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
    parser.add_argument("--r5-compiler", type=Path, required=True)
    parser.add_argument("--r1-compiler", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--factor-archive", type=Path, required=True)
    args = parser.parse_args()

    descent = load(args.case_dir / "build_rank_descent.py", "descent")
    r5 = descent.load_r5(args.r5_compiler)
    assert descent.COMPONENTS == {"p": "P", "c8p02": "C8P02"}
    assert len(list(itertools.combinations(range(1, 12), 10))) == 11
    assert len(list(itertools.combinations(range(1, 11), 10))) == 1
    assert len(list(itertools.combinations(range(1, 12), 9))) * len(
        list(itertools.combinations(range(1, 11), 9))
    ) == 550

    tiny_support = {(1, 1), (2, 2)}
    tiny_slots = descent.formal_slots(3, 3, 3, tiny_support, r5.perfect)
    assert len(tiny_slots) == 1 and tiny_slots[0][2] is False
    assert r5.max_matching((1, 2, 3), (1, 2, 3), tiny_support) == 2

    for component, expected_label in descent.COMPONENTS.items():
        label, zeros, factor, remaining, assignment, counts = r5.inputs(
            args.r1_compiler, args.matrix, args.factor_archive, component
        )
        assert label == expected_label
        assert factor not in {"", "0", "1", "16"}
        assert set(remaining).isdisjoint(zeros)
        assert all(counts[variable] > 0 for variable in zeros)
        reduce_source = r5.reduce_script(label, zeros, factor, remaining, assignment, counts)
        assert "qring" not in reduce_source
        assert "BRANCH_SB=std(BRANCH_IDEAL)" in reduce_source
        assert "EXPLICIT_NF_AFTER_EVERY_ENTRY_OPERATION=1" in reduce_source

    source = (args.case_dir / "build_rank_descent.py").read_text()
    assert "poly NORMALDET=reduce(RAWDET,BRANCH_SB)" in source
    assert "EVERY_SIZE10_MINOR_NF_ZERO=1" in source
    assert "EXACT_SIZE9_NF_WITNESS=1" in source
    assert "qring " not in source
    print("COMPONENT_COUNT=2")
    print("FORMAL_SIZE10_SLOT_COUNT=11")
    print("FORMAL_SIZE9_SLOT_COUNT=550")
    print("R5_REDUCER_SOURCE_PIN_PASS=1")
    print("RANK_DESCENT_SELFCHECK_PASS")


if __name__ == "__main__":
    main()

