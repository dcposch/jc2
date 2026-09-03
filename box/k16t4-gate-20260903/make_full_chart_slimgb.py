#!/usr/bin/env python3
"""Create full-chart modular slimgb jobs from the charged emitted jobs."""

from __future__ import annotations

import hashlib
import pathlib


OUT = pathlib.Path("/home/ubuntu/jc2/box/k16t4-gate-20260903")


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for prime in (32003, 65521, 1000003):
        src = OUT / f"t4_full_gauged_p{prime}.sing"
        dst = OUT / f"t4_full_gauged_p{prime}_slimgb.sing"
        text = src.read_text(encoding="utf-8")
        old = "ideal G=std(I);"
        new = f'print("METHOD_SLIMGB_GF{prime}");\nideal G=slimgb(I);'
        if text.count(old) != 1:
            raise RuntimeError(f"unexpected main method count in {src}")
        dst.write_text(text.replace(old, new), encoding="utf-8")
        print(f"{dst.name} sha256={sha256(dst)} bytes={dst.stat().st_size}")


if __name__ == "__main__":
    main()
