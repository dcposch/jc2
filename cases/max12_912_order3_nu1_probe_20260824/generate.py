#!/usr/bin/env python3
"""Emit fail-closed (p,r8)-elimination inputs for the nu=1 fibre.

The seven fibre rows are r1=...=r5=r7=0 and r6=1.  We adjoin rho=r8
and eliminate the six transverse coefficients and the cubic translation q.
The default finite characteristic is only a support-learning probe; pass
``--characteristic 0`` for a rational certificate after the support is known.
"""

from __future__ import annotations

from hashlib import sha256
import argparse
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_parent():
    if sha256(PARENT.read_bytes()).hexdigest() != PARENT_SHA256:
        raise RuntimeError("parent compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("max12_order3_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=1000003)
    parser.add_argument(
        "--mode", choices=("project", "standard"), default="project",
        help="project directly to Q[p,rho], or retain the full block basis",
    )
    parser.add_argument(
        "--engine", choices=("std", "slimgb"), default="slimgb",
        help="Groebner engine for the block computation",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]
    coefficient_names = [name for name in source_names if name != "k"]
    target_ring = M.Ring(coefficient_names)
    images = [
        M.cscale(0, target_ring.one) if name == "k" else target_ring.var(name)
        for name in source_names
    ]
    tails = {
        ell: parent.substitute_coeff(value, images, target_ring)
        for ell, value in compiled["transverse_tails"].items()
    }

    # The elimination block is x0,...,x5,q.  The two retained Kummer-
    # character coordinates p and rho form the second block.
    eliminated = [f"x{i}" for i in range(6)] + ["q"]
    retained = ["p", "rho"]
    singular_names = eliminated + retained
    lines = [
        'LIB "elim.lib";',
        (
            f"ring R={args.characteristic},({','.join(singular_names)}),"
            "(dp(7),dp(2));"
        ),
    ]
    for ell in range(1, 8):
        value = tails[ell]
        if ell == 6:
            value = M.cadd(value, M.cscale(-1, target_ring.one))
        lines.append(
            f"poly r{ell}={M.coeff_string(value, coefficient_names)};"
        )
    lines.append(
        "poly r8="
        + M.coeff_string(tails[8], coefficient_names)
        + ";"
    )
    lines.extend([
        "ideal I=r1,r2,r3,r4,r5,r6,r7,r8-rho;",
        # This identity is independent of the elimination and records the
        # exact multiple-root boundary of B=54*z^2+18*p+60*rho.
        "poly Bdisc=3*p+10*rho;",
    ])
    if args.mode == "project":
        lines.extend([
            f"ideal G={args.engine}(I);",
            "ideal E=eliminate(G,x0*x1*x2*x3*x4*x5*q);",
            "E=std(E);",
            'print("PASS-MAX12-912-ORDER3-NU1-PRHO-PROJECTION");',
            'print("projection_size="+string(size(E)));',
            'print("projection_dimension="+string(dim(E)));',
            'print("projection_basis=");',
            "E;",
        ])
    else:
        lines.extend([
            f"ideal G={args.engine}(I);",
            'print("PASS-MAX12-912-ORDER3-NU1-BLOCK-BASIS");',
            'print("groebner_size="+string(size(G)));',
            'print("dimension="+string(dim(G)));',
            'print("degree="+string(mult(G)));',
            "ideal E=eliminate(G,x0*x1*x2*x3*x4*x5*q);",
            'print("projection_basis=");',
            "E;",
        ])
    lines.append("quit;")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
