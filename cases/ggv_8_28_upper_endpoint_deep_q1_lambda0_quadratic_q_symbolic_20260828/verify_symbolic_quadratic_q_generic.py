#!/usr/bin/env python3
"""Custody and shape verifier for the exact arbitrary-quadratic-Q AWS run.

The heavy coefficient-field Gaussian elimination is intentionally not replayed
locally.  This checker pins its generated input, dependencies, transcript and
complete row ideal, then exercises three mutations of those frozen claims.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
EVIDENCE = HERE / "aws_symbolic_generic"

EXPECTED = {
    HERE / "compile_symbolic_quadratic_q.py": "58a26a4bf2c2045b96ea8c91de92648d21bda2712840e74b1ea0f09b872ccfa7",
    HERE / "symbolic_quadratic_q_gauss.sing": "100b4c12bfca51f133c36cf5f17ee4a8088feb75a8165d1074fa59dc9caeecbc",
    HERE / "equation_names.txt": "8d476d225af6c9c35f737d858dfc613913c727fc71ddb9e275d9509cfde86dd5",
    ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py": "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1",
    ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_q15_20260828/verify_lambda0_q15.py": "6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a",
    EVIDENCE / "stdout.txt": "965024b915610c9b96787faa6b91215a28f7a7496b22b306ceea6cc41ca3e27c",
    EVIDENCE / "meta.txt": "5e6f159245e15a14e05836ba96bb1b13daa197e06d9c93b4afe2484d28ddf89f",
    EVIDENCE / "row_reduced_ideal.txt": "f95fd2f7b0960191c4d53b4a80159d0e6afab83c45242301b26026cbf7da3c13",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def variables() -> list[str]:
    out: list[str] = []
    for prefix, degrees in (
        ("f", range(6)), ("f9", range(1, 8)),
        ("f11", range(1, 6)), ("f13", range(2, 4)),
        ("d7", range(3)), ("d9", range(5)), ("d11", range(7)),
        ("d13", range(9)), ("d15", range(11)),
        ("g9", range(16)), ("g11", range(14)),
        ("g13", range(1, 12)), ("g15", range(1, 10)),
    ):
        out.extend(f"{prefix}_{degree}" for degree in degrees)
    return out


def verify(mutation: str) -> None:
    for path, expected in EXPECTED.items():
        actual = sha256(path)
        if mutation == "source-hash" and path.name == "symbolic_quadratic_q_gauss.sing":
            actual = "0" * 64
        assert actual == expected, (path, actual, expected)

    names = [line.split(maxsplit=1)[1] for line in
             (HERE / "equation_names.txt").read_text().splitlines()]
    assert len(names) == len(set(names)) == 106
    assert names[0].startswith("q7_") and names[-1].startswith("G15_")

    source = (HERE / "symbolic_quadratic_q_gauss.sing").read_text()
    assert "ring r=(0,q0,q1,q2,c4,c6,c8)" in source
    assert "matrix M[106][105]=" in source
    assert "poly E=(1)*f11_1*g11_0+(1)*f_0*g15_1;" in source
    assert "c10" not in source

    stdout = (EVIDENCE / "stdout.txt").read_text()
    if mutation == "rank":
        stdout = stdout.replace("ROW_RANK=105", "ROW_RANK=104")
    assert "VARIABLES=105 EQUATIONS=106" in stdout
    assert "ROW_RANK=105" in stdout
    assert "ENDPOINT_NORMAL_FORM=0" in stdout
    assert "ENDPOINT_IDEAL_MEMBER=1" in stdout

    expected_variables = variables()
    assert len(expected_variables) == len(set(expected_variables)) == 105
    actual_variables = (EVIDENCE / "row_reduced_ideal.txt").read_text().strip().split(",")
    if mutation == "row-ideal":
        actual_variables.pop()
    assert actual_variables == expected_variables

    meta = (EVIDENCE / "meta.txt").read_text()
    assert "rc=0" in meta
    assert "stdout_sha256=" + EXPECTED[EVIDENCE / "stdout.txt"] in meta
    print("PASS symbolic arbitrary-quadratic-Q generic custody/shape audit")
    print("The exact AWS coefficient-field row ideal is all 105 receiver variables.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=("none", "source-hash", "rank", "row-ideal"), default="none")
    args = parser.parse_args()
    verify(args.mutation)


if __name__ == "__main__":
    main()
