#!/usr/bin/env python3
"""Extend the pinned moving-v generator to high truncation orders."""

from __future__ import annotations

import argparse
from hashlib import sha256
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LOW = ROOT / "cases/max12_912_order3_nu_q8_p127_hensel_coordinate_lift_aws_20260825/generate_moving.py"
LOW_SHA256 = "ae3eafd0faa1d36817434cb2cb849a6ee62f4fec7bc8af46a1c3a90643bfff53"


def replace_once(source: str, old: str, new: str) -> str:
    count = source.count(old)
    if count != 1:
        raise RuntimeError((old, count))
    return source.replace(old, new, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--order", type=int, choices=(256, 512, 1024), required=True)
    args = parser.parse_args()
    got = sha256(LOW.read_bytes()).hexdigest()
    if got != LOW_SHA256:
        raise RuntimeError((str(LOW), got, LOW_SHA256))
    completed = subprocess.run(
        [sys.executable, str(LOW), "--samples", str(args.samples), "--order", "128"],
        check=True,
        capture_output=True,
        text=True,
    )
    if completed.stderr:
        raise RuntimeError(("low generator stderr", completed.stderr))
    source = completed.stdout
    source = replace_once(source, "ideal QT=Hmoving,s^128;", f"ideal QT=Hmoving,s^{args.order};")
    source = replace_once(
        source,
        "for (coefficient_order=1;coefficient_order<128;coefficient_order++)",
        f"for (coefficient_order=1;coefficient_order<{args.order};coefficient_order++)",
    )
    source = replace_once(source, 'print("order=128");', f'print("order={args.order}");')
    if "s^128" in source or "order=128" in source or "coefficient_order<128" in source:
        raise RuntimeError("unreplaced order-128 literal")
    print(source, end="")


if __name__ == "__main__":
    main()

