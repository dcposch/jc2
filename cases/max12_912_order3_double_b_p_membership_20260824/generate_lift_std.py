#!/usr/bin/env python3
"""Emit the frozen double-B membership lift using Singular's default std."""

from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate_lift.py"
BASE_SHA256 = "403883070c06d3d489bd0408a85f913338b9c4b1fdff1dad852f16efc6520e31"


def main() -> None:
    if hashlib.sha256(BASE.read_bytes()).hexdigest() != BASE_SHA256:
        raise RuntimeError("base lift generator hash mismatch")
    source = subprocess.run(
        [sys.executable, str(BASE)], check=True, capture_output=True, text=True
    ).stdout
    old = 'matrix T=lift(I,target,U,"slimgb");'
    new = "matrix T=lift(I,target,U);"
    if source.count(old) != 1:
        raise RuntimeError("unexpected base lift source")
    print(source.replace(old, new), end="")


if __name__ == "__main__":
    main()
