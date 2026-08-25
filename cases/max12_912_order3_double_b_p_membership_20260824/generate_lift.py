#!/usr/bin/env python3
"""Emit an exact Singular lift for the frozen double-B elimination polynomial."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_CASE = ROOT / "cases/max12_912_order3_double_b_p_elimination_20260824"
INPUT = SOURCE_CASE / "input.ms"
RESULT = SOURCE_CASE / "result.out"
INPUT_SHA256 = "1bde828bfe3cddb7342a10436b34913c6cf1adebb4d668f0947b3a1f1ad1f287"
RESULT_SHA256 = "50d71a0b76239db801e5c75ff9497f33d62086c4b8f7b5fd0a3e1bfb67852a75"
VARIABLES = ("x0", "x1", "x2", "x3", "x4", "x5", "q", "ip", "p")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if sha256(INPUT) != INPUT_SHA256 or sha256(RESULT) != RESULT_SHA256:
        raise RuntimeError("frozen source hash mismatch")

    input_lines = INPUT.read_text().splitlines()
    if input_lines[:2] != [", ".join(VARIABLES), "0"]:
        raise RuntimeError("unexpected frozen input header")
    equations = [line.removesuffix(",") for line in input_lines[2:]]
    if len(equations) != 9 or equations[-1] != "p*ip-1":
        raise RuntimeError("unexpected frozen equation list")

    result = RESULT.read_text()
    polynomial = result.split("#---\n[", 1)[1]
    if not polynomial.endswith("]:\n"):
        raise RuntimeError("unexpected frozen result framing")
    polynomial = polynomial[:-3]

    print('option(redSB);')
    print('ring R=0,(x0,x1,x2,x3,x4,x5,q,ip,p),(dp(8),dp(1));')
    for index, equation in enumerate(equations, start=1):
        print(f"poly f{index}={equation};")
    print("ideal I=" + ",".join(f"f{index}" for index in range(1, 10)) + ";")
    print(f"poly P={polynomial};")
    print("ideal target=P;")
    print("matrix U;")
    print('matrix T=lift(I,target,U,"slimgb");')
    print("matrix residual=matrix(target)*U-matrix(I)*T;")
    print('print("PASS-DOUBLE-B-P-LIFT");')
    print('print("residual_zero="+string(residual==0));')
    print('print("rows="+string(nrows(T)));')
    print('print("cols="+string(ncols(T)));')
    print('print("TRANSFORMATION=");')
    print("T;")
    print('print("UNIT_MATRIX=");')
    print("U;")
    print("quit;")


if __name__ == "__main__":
    main()

