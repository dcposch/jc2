#!/usr/bin/env python3
"""Lightweight, non-algebraic custody check for the V73K review repair."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ORIGINAL = ROOT / "cases/td6_c1_c2_c3_q2_cminus5_previous_x11_v73_aws_20260825"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    expected = {
        ORIGINAL / "MANIFEST.sha256":
            "1282f908eb5e09543e1f5e6f97e0fce5fdac09873fb12ba1f9ff856d9b01b50f",
        ORIGINAL / "FREEZE.sha256":
            "d50d8844d930f56b66d72c64d50ca213895e140c5a1aa96456f8bdd61092851e",
        HERE / "evidence/hostile-review-adapter.log":
            "ee85b05c39d94a68406a5d4892a3b7875c915a0a0326d5198858c9880b6ad262",
        HERE / "evidence/predecessor-qprime.stdout":
            "c698dca9cf042dfae331e502422644b7e38aed17b29ae91e74acbbaec8c5fa46",
        HERE / "evidence/predecessor-qprime.stderr":
            "12994f401a70692743ddc7a5830b0b244516e64857bced5c09d5b65159b563e8",
    }
    for path, value in expected.items():
        assert digest(path) == value, path
    control = (HERE / "evidence/predecessor-qprime.stdout").read_text()
    assert "aws_run_tag=td6_v73_cminus5_x11_b_qprime_box03_20260825T1927Z" in control
    assert "direct_qprime_retained=false" in control
    assert "Xminus1_11_dependency_row_count=6" in control
    assert "Xminus1_11_dependency_keys=[('X-1', 1), ('X-1', 3), ('X-1', 5), ('X-1', 7), ('X-1', 9), ('X-1', 11)]" in control
    review = (HERE / "evidence/hostile-review-adapter.log").read_text()
    assert "CONFIRMED_WITH_REPAIRS" in review
    assert "predecessor producer, not V73K" in review
    print("TD6 V73K review custody repair PASS")


if __name__ == "__main__":
    main()
