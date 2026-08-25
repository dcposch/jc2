#!/usr/bin/env python3
"""Generate an exact fixed-fibre lex-shape reconstruction input."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
FIXED = ROOT / "cases/max12_912_order3_nu_q8_fibre_specialization_aws_20260825/generate.py"
FIXED_SHA256 = "4af6f7eca198bcdf1e60151449e08099853669bd1d6965db3cddffa666032d2c"


def load_fixed():
    got = sha256(FIXED.read_bytes()).hexdigest()
    if got != FIXED_SHA256:
        raise RuntimeError((str(FIXED), got, FIXED_SHA256))
    spec = importlib.util.spec_from_file_location("q8_coordinate_fixed", FIXED)
    if spec is None or spec.loader is None:
        raise RuntimeError(FIXED)
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

    fixed = load_fixed()
    source = fixed.source(127, args.w_value, "std")
    old_ring = "ring R=127,(c,d2,d4,x1,x3,x5,inv,v),(dp(7),dp(1));"
    new_ring = "ring R=127,(c,d2,d4,x1,x3,x5,inv,v),lp;"
    if source.count(old_ring) != 1:
        raise RuntimeError("fixed-fibre ring marker mismatch")
    source = source.replace(old_ring, new_ring)
    old_basis = "ideal G=std(I);"
    new_basis = 'LIB "standard.lib";\nideal G=stdfglm(I,"std");\nG=redSB(G);'
    if source.count(old_basis) != 1:
        raise RuntimeError("fixed-fibre basis marker mismatch")
    source = source.replace(old_basis, new_basis)
    marker = 'print("Q8-FIXED-W-FIBRE");'
    insertion = "\n".join(
        [
            'print("Q8-P127-LEX-COORDINATE-RECONSTRUCTION");',
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
    source = source.replace(marker, insertion + "\n" + marker)
    print(source)


if __name__ == "__main__":
    main()
