#!/usr/bin/env python3
"""Fail-closed custody verification for the order-32 moving-v lift."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUN = HERE / "aws_order32_box03_v1"
EXPECTED = {
    "generator.stderr": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "input.sing": "db053e1985483dfc752ac6422e194fd927950d15fdd764984aa39d7245302d03",
    "result.out": "a2934a4f02f8e5fad42154dcd69a80cb953db8666761945b9282f45326c92eaa",
    "run.meta": "665b596463958d57076d43530b738ce396c77bb346eba3195fc0bcbb5fbfeced",
    "stderr.log": "7ed3a251468189eb143595b290ecc08a5e8fe6a09f024abfbe66a0ad43b26ab4",
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
        "hensel_order=32",
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
        "_[1]=s32",
        "_[2]=v190",
        "moving_dimension=0",
        "moving_vdim=6080",
        "Q8-P127-HENSEL-MOVING-COORDINATE-LIFT",
        "order=32",
        "final_fail=0",
    ):
        once(result, item)
    for order in range(1, 32):
        once(result, f"coefficient_order={order}")
    for name in ("c", "d2", "d4", "x1", "x3", "x5", "inv"):
        if sum(line.startswith(f"series_{name}=") for line in result) != 1:
            raise AssertionError(("series", name))
    stderr = (RUN / "stderr.log").read_text()
    for item in (
        "Maximum resident set size (kbytes): 90120",
        "Elapsed (wall clock) time (h:mm:ss or m:ss): 16:17.41",
        "Exit status: 0",
    ):
        if item not in stderr:
            raise AssertionError(item)
    print("PASS-Q8-P127-MOVING-HENSEL-ORDER32-CUSTODY")


if __name__ == "__main__":
    main()

