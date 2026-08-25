#!/usr/bin/env python3
"""Fail-closed hash and endpoint verification for the frozen order-16 run."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUN = HERE / "aws_order16_r6d_v1"
EXPECTED = {
    "generator.stderr": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "input.sing": "518d9c643009dcb1df8651e687fe8d869d7bc04f21c6902041f62155d3e99f62",
    "result.out": "d4a00d5f5922022fa6de0e2e32398e923128b297100a37e1b688f067b4bfc1cb",
    "run.meta": "b1f91f21b45c50992550cb33231411b1de8fce7f81793f2fdf81c4229dbb5697",
    "stderr.log": "23a57f40539d29f12f00bccc5e662715b5698f05066d34b04dfb7e6c2c2d260b",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_once(lines: list[str], value: str) -> None:
    count = lines.count(value)
    if count != 1:
        raise AssertionError((value, count))


def main() -> None:
    for name, expected in EXPECTED.items():
        got = digest(RUN / name)
        if got != expected:
            raise AssertionError((name, got, expected))

    meta = (RUN / "run.meta").read_text().splitlines()
    for item in (
        "characteristic=127",
        "base_w=25",
        "hensel_order=16",
        "generator_rc=0",
        "rc=0",
        "endpoint=PASS",
        "stdout_sha256=" + EXPECTED["result.out"],
        "stderr_sha256=" + EXPECTED["stderr.log"],
    ):
        require_once(meta, item)

    result = (RUN / "result.out").read_text().splitlines()
    for item in (
        "Q8-P127-HENSEL-BASE",
        "base_fail=0",
        "H0_degree=190",
        "gcd_detJ_H0_degree=0",
        "gcd_Hv_H0_degree=0",
        "Q8-P127-MOVING-BASIS",
        "_[1]=s16",
        "_[2]=v190",
        "moving_dimension=0",
        "moving_vdim=3040",
        "Q8-P127-HENSEL-MOVING-COORDINATE-LIFT",
        "order=16",
        "final_fail=0",
    ):
        require_once(result, item)
    for order in range(1, 16):
        require_once(result, f"coefficient_order={order}")
    for name in ("c", "d2", "d4", "x1", "x3", "x5", "inv"):
        if sum(line.startswith(f"series_{name}=") for line in result) != 1:
            raise AssertionError(("series", name))

    stderr = (RUN / "stderr.log").read_text()
    for item in (
        "Maximum resident set size (kbytes): 55908",
        "Elapsed (wall clock) time (h:mm:ss or m:ss): 3:48.39",
        "Exit status: 0",
    ):
        if item not in stderr:
            raise AssertionError(item)
    print("PASS-Q8-P127-MOVING-HENSEL-ORDER16-CUSTODY")


if __name__ == "__main__":
    main()

