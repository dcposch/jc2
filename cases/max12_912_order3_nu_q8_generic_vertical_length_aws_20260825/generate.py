#!/usr/bin/env python3
"""Generate the saturated generic-w source ideal over F_127(w)."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
from math import comb
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
P = 127
VARIABLES = ("u", "c", "d2", "d4", "x1", "x5", "v")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_compiler():
    if digest(COMPILER) != COMPILER_SHA256:
        raise RuntimeError("compiler hash")
    spec = importlib.util.spec_from_file_location("q8_generic_vertical_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def mod_scalar(value: Fraction) -> int:
    value = Fraction(value)
    denominator = value.denominator % P
    if denominator == 0:
        raise RuntimeError(("bad denominator", value))
    return value.numerator % P * pow(denominator, P - 2, P) % P


def substitute(row: dict) -> dict[tuple[int, ...], dict[int, int]]:
    # Output monomial exponents in (u,c,d2,d4,x1,x5,v), with coefficients in F127[w].
    out: dict[tuple[int, ...], dict[int, int]] = {}
    for monomial, raw_scalar in row.items():
        ew, ec, ed2, ed4, ex1, ex3, ex5 = monomial
        scalar = mod_scalar(raw_scalar)
        for kv in range(ex3 + 1):
            exponent = (0, ec, ed2, ed4, ex1, ex3 + ex5, kv)
            coefficient = scalar * comb(ex3, kv) * pow(2, ex3 - kv, P) % P
            polynomial = out.setdefault(exponent, {})
            polynomial[ew] = (polynomial.get(ew, 0) + coefficient) % P
    cleaned = {}
    for exponent, polynomial in out.items():
        polynomial = {degree: coefficient for degree, coefficient in polynomial.items() if coefficient % P}
        if polynomial:
            cleaned[exponent] = polynomial
    return cleaned


def polynomial_string(row: dict[tuple[int, ...], dict[int, int]]) -> str:
    terms = []
    for exponent, coefficient_poly in sorted(row.items()):
        for w_degree, coefficient in sorted(coefficient_poly.items()):
            factors = []
            if coefficient != 1 or (w_degree == 0 and not any(exponent)):
                factors.append(str(coefficient))
            if w_degree:
                factors.append("w" if w_degree == 1 else f"w^{w_degree}")
            for name, power in zip(VARIABLES, exponent, strict=True):
                if power:
                    factors.append(name if power == 1 else f"{name}^{power}")
            terms.append("*".join(factors))
    return "+".join(terms) if terms else "0"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("dp", "lp"), required=True)
    args = parser.parse_args()
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    reduced = {ell: substitute(rows[ell]) for ell in imposed}
    print(f"ring R=(127,w),(u,c,d2,d4,x1,x5,v),{args.order};")
    for ell in imposed:
        print(f"poly e{ell}={polynomial_string(reduced[ell])};")
    print("poly eloc=u*x5*v-1;")
    print("ideal I=e1,e3,e5,e7,e2,e4,eloc;")
    print('print("Q8-GENERIC-VERTICAL-LENGTH");')
    print(f'print("term_order={args.order}");')
    print('print("input_term_counts=9,20,33,57,14,29,2");')
    print("ideal G=std(I);")
    print('print("std_size="+string(size(G)));')
    print('print("dimension="+string(dim(G)));')
    print("int source_fail=0; int ii;")
    print("for(ii=1;ii<=size(I);ii++){if(reduce(I[ii],G)!=0){source_fail=source_fail+1;}}")
    print('print("source_fail="+string(source_fail));')
    print("if(dim(G)==0){print(\"vdim=\"+string(vdim(G)));}")


if __name__ == "__main__":
    main()
