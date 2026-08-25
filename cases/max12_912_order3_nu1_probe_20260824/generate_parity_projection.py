#!/usr/bin/env python3
"""Emit the exact odd/even component probe in retained (p,rho,nu).

On ``q=x0=x2=x4=k=0``, ``f`` is odd and its Faber ``g`` is even.  The
odd-index tail rows vanish identically.  This script eliminates the remaining
three transverse variables from ``r2=r4=0, r6=nu, r8=rho``.  It is a
component/falsifier probe, not an exhaustion of the full fibre.
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
    spec = importlib.util.spec_from_file_location("max12_order3_parity_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=32003)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    args = parser.parse_args()

    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]
    names = ["x1", "x3", "x5", "p"]
    ring = M.Ring(names)
    images = [
        ring.var(name) if name in names else M.cscale(0, ring.one)
        for name in source_names
    ]
    tails = {
        ell: parent.substitute_coeff(value, images, ring)
        for ell, value in compiled["transverse_tails"].items()
    }
    for ell in (1, 3, 5, 7):
        if tails[ell]:
            raise RuntimeError(("odd tail survives parity specialization", ell))

    lines = [
        'LIB "elim.lib";',
        (
            f"ring R={args.characteristic},(x1,x3,x5,p,rho,nu),"
            "(Wp(8,6,4),Wp(2,20,18));"
        ),
    ]
    for ell in (2, 4, 6, 8):
        lines.append(f"poly r{ell}={M.coeff_string(tails[ell], names)};")
    lines.extend([
        "ideal I=r2,r4,r6-nu,r8-rho;",
        f"ideal G={args.engine}(I);",
        "ideal E=eliminate(G,x1*x3*x5);",
        "E=std(E);",
        'print("PASS-MAX12-912-ORDER3-PARITY-PNU-RHO-PROJECTION");',
        'print("full_dimension="+string(dim(G)));',
        'print("projection_size="+string(size(E)));',
        'print("projection_dimension="+string(dim(E)));',
        'print("projection_basis=");',
        "E;",
        "quit;",
    ])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
