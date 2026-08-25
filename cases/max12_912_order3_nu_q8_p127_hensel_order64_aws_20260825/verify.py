#!/usr/bin/env python3
"""Fail-closed custody verification for the order-64 moving-v lift."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUN = HERE / "aws_order64_box02_v1"
EXPECTED = {
    "generator.stderr": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "input.sing": "27d27100e1ed0b3dda870a38709e68126d1d493fea572853f2af8a116e6e3f26",
    "result.out": "f750d965a48634d2b47b442b47577b67b900a810ab208c2dc08f03fd5cd299aa",
    "run.meta": "3cd0c3ca50dd6f3f956c8271b317ced35a2e3ca637ab2f6ce6f37cf99840bc9d",
    "stderr.log": "e162236c51ac27eb87a3ef3159de4319e1cc2137600730372458d9ac80e2debe",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def once(lines: list[str], item: str) -> None:
    if lines.count(item) != 1:
        raise AssertionError((item, lines.count(item)))


def main() -> None:
    for name, expected in EXPECTED.items():
        got = digest(RUN / name)
        if got != expected:
            raise AssertionError((name, got, expected))
    meta = (RUN / "run.meta").read_text().splitlines()
    for item in (
        "characteristic=127",
        "base_w=25",
        "hensel_order=64",
        "generator_rc=0",
        "rc=0",
        "endpoint=PASS",
        "stdout_sha256=" + EXPECTED["result.out"],
        "stderr_sha256=" + EXPECTED["stderr.log"],
    ):
        once(meta, item)
    result = (RUN / "result.out").read_text().splitlines()
    for item in (
        "Q8-P127-HENSEL-BASE",
        "base_fail=0",
        "H0_degree=190",
        "gcd_detJ_H0_degree=0",
        "gcd_Hv_H0_degree=0",
        "Q8-P127-MOVING-BASIS",
        "_[1]=s64",
        "_[2]=v190",
        "moving_dimension=0",
        "moving_vdim=12160",
        "Q8-P127-HENSEL-MOVING-COORDINATE-LIFT",
        "order=64",
        "final_fail=0",
    ):
        once(result, item)
    for order in range(1, 64):
        once(result, f"coefficient_order={order}")
    for name in ("c", "d2", "d4", "x1", "x3", "x5", "inv"):
        if sum(line.startswith(f"series_{name}=") for line in result) != 1:
            raise AssertionError(("series", name))
    stderr = (RUN / "stderr.log").read_text()
    for item in (
        "Maximum resident set size (kbytes): 158512",
        "Elapsed (wall clock) time (h:mm:ss or m:ss): 1:08:07",
        "Exit status: 0",
    ):
        if item not in stderr:
            raise AssertionError(item)
    print("PASS-Q8-P127-MOVING-HENSEL-ORDER64-CUSTODY")


if __name__ == "__main__":
    main()

