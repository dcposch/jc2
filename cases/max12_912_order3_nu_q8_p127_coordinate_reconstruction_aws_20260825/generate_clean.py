#!/usr/bin/env python3
"""Generate the corrected fixed-fibre lex-shape control (no redSB call)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
HISTORICAL = HERE / "generate.py"
HISTORICAL_SHA256 = "c3fdecc05dae965961e93612bd2e28f2623d10694c81eb717a15d215bdd89003"


def load_historical():
    got = sha256(HISTORICAL.read_bytes()).hexdigest()
    if got != HISTORICAL_SHA256:
        raise RuntimeError((str(HISTORICAL), got, HISTORICAL_SHA256))
    spec = importlib.util.spec_from_file_location("q8_coordinate_historical", HISTORICAL)
    if spec is None or spec.loader is None:
        raise RuntimeError(HISTORICAL)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--w-value", type=int, required=True)
    args = parser.parse_args()
    if not 1 <= args.w_value <= 126:
        raise RuntimeError("w-value must lie in 1..126")
    historical = load_historical()
    fixed = historical.load_fixed()
    source = fixed.source(127, args.w_value, "std")
    old_ring = "ring R=127,(c,d2,d4,x1,x3,x5,inv,v),(dp(7),dp(1));"
    new_ring = "ring R=127,(c,d2,d4,x1,x3,x5,inv,v),lp;"
    if source.count(old_ring) != 1:
        raise RuntimeError("fixed-fibre ring marker mismatch")
    source = source.replace(old_ring, new_ring)
    old_basis = "ideal G=std(I);"
    new_basis = 'LIB "standard.lib";\nideal G=stdfglm(I,"std");'
    if source.count(old_basis) != 1:
        raise RuntimeError("fixed-fibre basis marker mismatch")
    source = source.replace(old_basis, new_basis)
    marker = 'print("Q8-FIXED-W-FIBRE");'
    insertion = "\n".join(
        [
            'print("Q8-P127-LEX-COORDINATE-RECONSTRUCTION-CLEAN");',
            f'print("w_value={args.w_value}");',
            'print("shape_basis_begin");',
            "G;",
            'print("shape_basis_end");',
            "ideal original_remainders=reduce(I,G);",
            'print("original_remainders_begin");',
            "original_remainders;",
            'print("original_remainders_end");',
        ]
    )
    if source.count(marker) != 1:
        raise RuntimeError("fixed-fibre print marker mismatch")
    print(source.replace(marker, insertion + "\n" + marker))


if __name__ == "__main__":
    main()

