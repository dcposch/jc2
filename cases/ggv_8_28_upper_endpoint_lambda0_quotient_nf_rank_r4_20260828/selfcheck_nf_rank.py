#!/usr/bin/env python3
"""Stdlib-only source, reducer, and structural-rank selfcheck for r4."""

from __future__ import annotations

import argparse
import importlib.util
import re
import tempfile
from pathlib import Path


EXPECTED_COMPONENTS = {
    "p": "P",
    "c8p02": "C8P02",
    "q1p02": "Q1P02",
    "q1p03": "Q1P03",
    "triple02": "TRIPLE02",
    "triple03": "TRIPLE03",
}


def load(path: Path):
    spec = importlib.util.spec_from_file_location("nf_rank", path)
    if spec is None or spec.loader is None:
        raise SystemExit("COMPILER_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--r1-compiler", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--factor-archive", type=Path, required=True)
    args = parser.parse_args()

    compiler = load(args.case_dir / "build_nf_rank.py")
    assert compiler.COMPONENTS == EXPECTED_COMPONENTS
    assert compiler.max_matching((1, 2, 3), (1, 2, 3), {(1, 1), (2, 2)}) == 2
    assert compiler.max_matching((1, 2), (1, 2), {(1, 1), (1, 2), (2, 1)}) == 2
    assert not compiler.perfect((1, 2, 3), (1, 2, 3), {(1, 1), (2, 2)})

    q2_components = set()
    for component, expected_label in EXPECTED_COMPONENTS.items():
        label, zeros, factor, remaining, assignment, counts = compiler.inputs(
            args.r1_compiler, args.matrix, args.factor_archive, component
        )
        assert label == expected_label
        assert factor not in {"", "0", "1", "16"}
        assert set(remaining).isdisjoint(zeros)
        assert all(counts[variable] > 0 for variable in zeros)
        for variable in zeros:
            assert re.search(rf"\b{re.escape(variable)}\b", assignment) is None
            assert re.search(rf"\b{re.escape(variable)}\b", factor) is None
        generated = compiler.reduce_script(label, zeros, factor, remaining, assignment, counts)
        assert "qring" not in generated
        assert "BRANCH_SB=std(BRANCH_IDEAL)" in generated
        assert "EXPLICIT_NF_AFTER_EVERY_ENTRY_OPERATION=1" in generated
        assert "ADVERSARIAL_IDEAL_FACTOR_NF_ZERO" in generated
        assert "ADVERSARIAL_MUTATION_NF_NONZERO" in generated
        if factor == "q2":
            q2_components.add(component)
            assert "ADVERSARIAL_LITERAL_Q2_NF_ZERO" in generated
        else:
            assert "ADVERSARIAL_LITERAL_Q2_NF_ZERO" not in generated
    assert q2_components == {"q1p03", "triple03"}

    with tempfile.TemporaryDirectory(prefix="nf_rank_selfcheck_") as raw:
        root = Path(raw)
        residual = root / "fixture.tsv"
        residual.write_text(
            "rows|3|cols|3\n"
            "1|1|q0\n1|2|0\n1|3|0\n"
            "2|1|0\n2|2|1\n2|3|0\n"
            "3|1|0\n3|2|0\n3|3|0\n"
        )
        matrix = compiler.read_residual(residual)
        script, rank, candidates, higher = compiler.rank_script(
            "Q2_FIXTURE", "q2", ["q0", "q2"], matrix,
            root / "higher.tsv",
        )
        assert rank == 2
        assert candidates == 1
        assert higher == 1
        assert "qring" not in script
        assert "ADVERSARIAL_LITERAL_Q2_NF_ZERO" in script
        assert "poly DNF=reduce(DRAW,BRANCH_SB)" in script
        assert "EVERY_HIGHER_MINOR_STRUCTURALLY_ZERO_AFTER_NF=1" in script
        lines = (root / "higher.tsv").read_text().splitlines()
        assert lines == [
            "slot|rows|cols|classification",
            "1|1,2,3|1,2,3|STRUCTURAL_ZERO",
        ]

    print("COMPONENT_COUNT=6")
    print("Q2_ADVERSARIAL_COMPONENTS=q1p03,triple03")
    print("STRUCTURAL_HALL_FIXTURE_PASS=1")
    print("NO_QRING_SOURCE_PASS=1")
    print("NF_RANK_SELFCHECK_PASS")


if __name__ == "__main__":
    main()

