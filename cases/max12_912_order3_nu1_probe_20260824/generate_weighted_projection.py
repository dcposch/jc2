#!/usr/bin/env python3
"""Emit the homogeneous (p,rho,nu) projection of the k=mu=0 fibre.

The scaling weights are

    wt(x_i)=9-i, wt(q)=3, wt(p)=2, wt(nu)=18, wt(rho)=20.

Keeping ``nu`` until after elimination makes all eight equations weighted
homogeneous.  The normalized ``nu=1`` curve is obtained only after the
projected relation has been certified.  Finite-characteristic output is a
support-learning probe, never by itself an exact certificate.
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
    spec = importlib.util.spec_from_file_location("max12_order3_weighted_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=32003)
    parser.add_argument(
        "--engine", choices=("std", "slimgb", "modstd"), default="slimgb"
    )
    parser.add_argument(
        "--double-b", action="store_true",
        help="adjoin 3*nu*p+10*rho before the projection",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]
    coefficient_names = [name for name in source_names if name != "k"]
    coefficient_ring = M.Ring(coefficient_names)
    images = [
        M.cscale(0, coefficient_ring.one)
        if name == "k"
        else coefficient_ring.var(name)
        for name in source_names
    ]
    tails = {
        ell: parent.substitute_coeff(value, images, coefficient_ring)
        for ell, value in compiled["transverse_tails"].items()
    }

    weights = {
        **{f"x{i}": 9 - i for i in range(6)},
        "p": 2,
        "q": 3,
    }
    for ell, value in tails.items():
        seen = {
            sum(exponent * weights[name]
                for exponent, name in zip(monomial, coefficient_names))
            for monomial in value
        }
        if seen != {12 + ell}:
            raise RuntimeError(("weight mismatch", ell, seen))

    eliminated = [f"x{i}" for i in range(6)] + ["q"]
    retained = ["p", "rho", "nu"]
    variables = eliminated + retained
    lines = [
        'LIB "elim.lib";',
        *(['LIB "modstd.lib";'] if args.engine == "modstd" else []),
        (
            f"ring R={args.characteristic},({','.join(variables)}),"
            "(Wp(9,8,7,6,5,4,3),Wp(2,20,18));"
        ),
    ]
    for ell in range(1, 9):
        lines.append(
            f"poly r{ell}={M.coeff_string(tails[ell], coefficient_names)};"
        )
    lines.extend([
        "ideal I=r1,r2,r3,r4,r5,r6-nu,r7,r8-rho;",
        # B=54*nu*z^2+18*nu*p+60*rho.  Its discriminant vanishes
        # precisely on the retained weighted-linear factor below.
        "poly Bdisc=3*nu*p+10*rho;",
        (
            "ideal J=I,Bdisc;"
            if args.double_b
            else "ideal J=I;"
        ),
        (
            "ideal G=modStd(J,1);"
            if args.engine == "modstd"
            else f"ideal G={args.engine}(J);"
        ),
        "ideal E=eliminate(G,x0*x1*x2*x3*x4*x5*q);",
        "E=std(E);",
        'print("PASS-MAX12-912-ORDER3-WEIGHTED-PNU-RHO-PROJECTION");',
        f'print("double_b={int(args.double_b)}");',
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
