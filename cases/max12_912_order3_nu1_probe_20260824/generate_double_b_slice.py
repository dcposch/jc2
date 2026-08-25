#!/usr/bin/env python3
"""Emit a finite-field p-slice of the normalized double-B leaf.

This is support learning only.  It projects the exact source rows to q after
fixing p, so several slices can distinguish a dominant double-B curve from
vertical or exceptional components before characteristic-zero reconstruction.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_parent():
    if sha256(PARENT.read_bytes()).hexdigest() != PARENT_SHA256:
        raise RuntimeError("parent compiler hash mismatch")
    spec = importlib.util.spec_from_file_location(
        "max12_order3_double_b_slice_parent", PARENT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=1000003)
    parser.add_argument("--p-value", type=int, required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    args = parser.parse_args()

    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]
    names = [f"x{i}" for i in range(6)] + ["q"]
    ring = M.Ring(names)
    images = []
    for name in source_names:
        if name in names:
            images.append(ring.var(name))
        elif name == "p":
            images.append(M.cscale(args.p_value, ring.one))
        else:
            images.append(M.cscale(0, ring.one))
    tails = {
        ell: parent.substitute_coeff(value, images, ring)
        for ell, value in compiled["transverse_tails"].items()
    }

    lines = [
        'LIB "elim.lib";',
        (
            f"ring R={args.characteristic},({','.join(names)}),"
            "(dp(6),dp(1));"
        ),
    ]
    for ell in range(1, 9):
        lines.append(f"poly r{ell}={M.coeff_string(tails[ell], names)};")
    lines.extend([
        f"ideal I=r1,r2,r3,r4,r5,r6-1,r7,10*r8+3*({args.p_value});",
        f"ideal G={args.engine}(I);",
        "ideal E=eliminate(G,x0*x1*x2*x3*x4*x5);",
        "E=std(E);",
        'print("PASS-MAX12-912-ORDER3-NU1-DOUBLE-B-P-SLICE");',
        f'print("p_value={args.p_value}");',
        'print("basis_size="+string(size(G)));',
        'print("dimension="+string(dim(G)));',
        'print("degree="+string(mult(G)));',
        'print("q_projection_size="+string(size(E)));',
        'print("q_projection_basis=");',
        "E;",
        "quit;",
    ])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
