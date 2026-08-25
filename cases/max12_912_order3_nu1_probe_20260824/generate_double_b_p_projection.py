#!/usr/bin/env python3
"""Emit the normalized double-B leaf projected to p alone.

The decisive certificate sought here is any nonzero polynomial in the
elimination ideal over characteristic zero.  Such a relation makes p
algebraic over the constant field, while the double-B equation gives
``r8=-3*p/10``; the terminal row would then be impossible.  Finite-prime
output is used only to discover the support of that polynomial.
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
        "max12_order3_double_b_p_parent", PARENT
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
    parser.add_argument(
        "--engine", choices=("std", "slimgb", "modstd"), default="slimgb"
    )
    parser.add_argument(
        "--saturate-p", action="store_true",
        help="adjoin ip with p*ip-1 to isolate the nonzero-p locus",
    )
    args = parser.parse_args()

    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]
    names = [name for name in source_names if name != "k"]
    ring = M.Ring(names)
    images = [
        M.cscale(0, ring.one) if name == "k" else ring.var(name)
        for name in source_names
    ]
    tails = {
        ell: parent.substitute_coeff(value, images, ring)
        for ell, value in compiled["transverse_tails"].items()
    }

    eliminated = [f"x{i}" for i in range(6)] + ["q"]
    if args.saturate_p:
        eliminated.append("ip")
    variables = eliminated + ["p"]
    elimination_block_size = len(eliminated)
    lines = [
        'LIB "elim.lib";',
        *(['LIB "modstd.lib";'] if args.engine == "modstd" else []),
        (
            f"ring R={args.characteristic},({','.join(variables)}),"
            f"(dp({elimination_block_size}),dp(1));"
        ),
    ]
    for ell in range(1, 9):
        lines.append(f"poly r{ell}={M.coeff_string(tails[ell], names)};")
    generators = "r1,r2,r3,r4,r5,r6-1,r7,10*r8+3*p"
    if args.saturate_p:
        generators += ",p*ip-1"
    eliminate_monomial = "*".join(eliminated)
    lines.extend([
        f"ideal I={generators};",
        (
            "ideal G=modStd(I,1);"
            if args.engine == "modstd"
            else f"ideal G={args.engine}(I);"
        ),
        f"ideal E=eliminate(G,{eliminate_monomial});",
        "E=std(E);",
        'print("PASS-MAX12-912-ORDER3-NU1-DOUBLE-B-P-PROJECTION");',
        f'print("saturate_p={int(args.saturate_p)}");',
        'print("full_basis_size="+string(size(G)));',
        'print("full_dimension="+string(dim(G)));',
        'print("full_degree="+string(mult(G)));',
        'print("projection_size="+string(size(E)));',
        'print("projection_basis=");',
        "E;",
        "quit;",
    ])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
