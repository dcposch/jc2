#!/usr/bin/env python3
"""Lightweight custody check for the nonmutating V57 review repair."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ORIGINAL = ROOT / "cases/td6_c1_c2_c3_q2_generic_source_dag_v57_aws_20260825"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    expected = {
        ORIGINAL / "MANIFEST.sha256":
            "7d337a218b5436caad67ac2dc5b96349d2821262a7243c5750c82dc07903017b",
        ORIGINAL / "FREEZE.sha256":
            "c42633c4eeed8bfbfd388ba9c97a3c6c9aa9fee656b71f3f3256efac8a96f911",
        ORIGINAL / "aws_box03/artifacts/N13_PROOF_DAG.txt":
            "a906b803a3c0835630884a56e4e9546c7dffa277ba21c36bc3d75027b539da32",
        ORIGINAL / "aws_box03/artifacts/DAG_LEAF_DENOMINATORS.tsv":
            "69c1086b6e302910fe331e7f1c8cfa246a760f429507af2b9d0dd970d1c29ecf",
        HERE / "evidence/hostile-review-adapter.log":
            "e7b580724de2b95bf6a96a8c2e0e51d2e54ae4edff8eded95492bde4efbc617a",
    }
    for path, value in expected.items():
        assert digest(path) == value, path
    review = (HERE / "evidence/hostile-review-adapter.log").read_text()
    assert "CONFIRMED_WITH_REPAIRS" in review
    assert "exactly one `X-1` previous original row" in review
    assert "Pole original rows are not N13 summands" in review
    assert "exact localized source identity on **`D(U H B3)`" in review
    print("TD6 V57 review repair custody PASS")


if __name__ == "__main__":
    main()
