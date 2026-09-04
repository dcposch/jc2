#!/usr/bin/env python3
"""Recheck Hilbert data from a previously printed certified lead ideal.

This is a bridge/control only: the new computations use the prompt-order ring.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int)
    ap.add_argument("source", type=Path)
    args = ap.parse_args()
    text = args.source.read_text(encoding="utf-8")
    match = re.search(r"^JPLUS_LEAD=(.*)$", text, re.MULTILINE)
    if not match:
        raise SystemExit("JPLUS_LEAD line not found")
    generators = []
    for raw in match.group(1).split(","):
        monomial = re.sub(r"^-?\d+\*", "", raw.strip())
        generators.append(monomial)
    variables = ["b3", "b4"] + [f"q({j})" for j in range(2, args.t)]
    weights = [args.t + 1, 1] + list(range(2, args.t))
    lines = [
        f"ring R=32003,({','.join(variables)}),wp({','.join(map(str, weights))});",
        f"intvec w={','.join(map(str, weights))};",
        "ideal M=" + ",".join(generators) + ";",
        f'print("LEGACY_T={args.t}");',
        'print("LEGACY_SIZE="+string(size(M)));',
        'print("LEGACY_DIM="+string(dim(M)));',
        'print("LEGACY_VDIM="+string(vdim(M)));',
        'print("LEGACY_HNUM");',
        'hilb(M,1,w);',
        "quit;",
    ]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
