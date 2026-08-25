#!/usr/bin/env python3
"""Emit a finite-field p-slice of the normalized parity fibre.

This is support learning only.  It distinguishes genuine projection factors
from the two pairwise-resultant factors before any characteristic-zero lift.
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
    spec = importlib.util.spec_from_file_location("max12_order3_parity_slice_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=32003)
    parser.add_argument("--p-value", type=int, required=True)
    args = parser.parse_args()

    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]
    names = ["x1", "x3", "x5"]
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
    assert all(not tails[ell] for ell in (1, 3, 5, 7))

    lines = [
        'LIB "elim.lib";',
        f"ring R={args.characteristic},(x1,x3,x5,rho),(dp(3),dp(1));",
    ]
    for ell in (2, 4, 6, 8):
        lines.append(f"poly r{ell}={M.coeff_string(tails[ell], names)};")
    lines.extend([
        "ideal I=r2,r4,r6-1,r8-rho;",
        "ideal G=slimgb(I);",
        "ideal E=eliminate(G,x1*x3*x5);",
        "E=std(E);",
        'print("PASS-PARITY-P-SLICE");',
        f'print("p_value={args.p_value}");',
        'print("full_dimension="+string(dim(G)));',
        'print("projection_size="+string(size(E)));',
        'print("projection_factorization="); factorize(E[1]);',
        "quit;",
    ])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
