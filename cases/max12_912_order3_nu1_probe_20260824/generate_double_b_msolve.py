#!/usr/bin/env python3
"""Emit the exact normalized double-B system in msolve input syntax.

The default saturated mode adjoins ``p*ip-1``.  It is a zero-dimensional
support/certificate target at every tested good prime; characteristic-zero
output remains subject to the campaign's msolve reconstruction caveat.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_parent():
    if sha256(PARENT.read_bytes()).hexdigest() != PARENT_SHA256:
        raise RuntimeError("parent compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("max12_double_b_msolve_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def lcm(left: int, right: int) -> int:
    return left // gcd(left, right) * right


def primitive_string(parent, value, names):
    denominator = 1
    for coefficient in value.values():
        denominator = lcm(denominator, Fraction(coefficient).denominator)
    scaled = parent.M.cscale(denominator, value)
    numerators = [abs(Fraction(c).numerator) for c in scaled.values() if c]
    content = 0
    for numerator in numerators:
        content = gcd(content, numerator)
    if content > 1:
        scaled = parent.M.cscale(Fraction(1, content), scaled)
    return parent.M.coeff_string(scaled, names)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=0)
    parser.add_argument("--mode", choices=("saturated", "p1"), default="saturated")
    parser.add_argument(
        "--order", choices=("p-last", "p-first"), default="p-last",
        help="change only the declared variable order for an independent FGLM race",
    )
    args = parser.parse_args()

    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]

    if args.mode == "saturated":
        coefficient_names = [name for name in source_names if name != "k"]
        ring = M.Ring(coefficient_names)
        images = [
            M.cscale(0, ring.one) if name == "k" else ring.var(name)
            for name in source_names
        ]
        tails = {
            ell: parent.substitute_coeff(value, images, ring)
            for ell, value in compiled["transverse_tails"].items()
        }
        variables = [f"x{i}" for i in range(6)] + ["q", "ip", "p"]
        if args.order == "p-first":
            variables = ["p"] + [f"x{i}" for i in range(6)] + ["q", "ip"]
        equations = [tails[i] for i in range(1, 6)]
        equations += [M.cadd(tails[6], M.cscale(-1, ring.one)), tails[7]]
        equations += [M.cadd(M.cscale(10, tails[8]), M.cscale(3, ring.var("p")))]
        polynomial_strings = [primitive_string(parent, value, coefficient_names)
                              for value in equations]
        polynomial_strings.append("p*ip-1")
    else:
        coefficient_names = [f"x{i}" for i in range(6)] + ["q"]
        ring = M.Ring(coefficient_names)
        images = []
        for name in source_names:
            if name in coefficient_names:
                images.append(ring.var(name))
            elif name == "p":
                images.append(ring.one)
            else:
                images.append(M.cscale(0, ring.one))
        tails = {
            ell: parent.substitute_coeff(value, images, ring)
            for ell, value in compiled["transverse_tails"].items()
        }
        variables = coefficient_names
        equations = [tails[i] for i in range(1, 6)]
        equations += [M.cadd(tails[6], M.cscale(-1, ring.one)), tails[7]]
        equations += [M.cadd(M.cscale(10, tails[8]), M.cscale(3, ring.one))]
        polynomial_strings = [primitive_string(parent, value, coefficient_names)
                              for value in equations]

    # msolve requires the variable declaration on the very first line.  Keep
    # provenance in the frozen wrapper/metadata rather than in-band here.
    print(", ".join(variables))
    print(args.characteristic)
    print(",\n".join(polynomial_strings))


if __name__ == "__main__":
    main()
