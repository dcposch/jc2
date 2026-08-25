#!/usr/bin/env python3
"""Generate one raw projective-boundary chart over the exact Q8 source."""

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
    spec = importlib.util.spec_from_file_location("q8_projective_boundary_compiler", COMPILER)
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
    """Substitute x3=(v+2)x5; coefficients remain in F127[w]."""
    out: dict[tuple[int, ...], dict[int, int]] = {}
    for monomial, raw_scalar in row.items():
        ew, ec, ed2, ed4, ex1, ex3, ex5 = monomial
        scalar = mod_scalar(raw_scalar)
        for kv in range(ex3 + 1):
            exponent = (0, ec, ed2, ed4, ex1, ex3 + ex5, kv)
            coefficient = scalar * comb(ex3, kv) * pow(2, ex3 - kv, P) % P
            polynomial = out.setdefault(exponent, {})
            polynomial[ew] = (polynomial.get(ew, 0) + coefficient) % P
    return {
        exponent: {degree: coefficient for degree, coefficient in polynomial.items() if coefficient % P}
        for exponent, polynomial in out.items()
        if any(coefficient % P for coefficient in polynomial.values())
    }


def polynomial_string(row: dict[tuple[int, ...], dict[int, int]], homogeneous: bool) -> str:
    internal_degree = max(sum(exponent) for exponent in row) if row else 0
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
            if homogeneous:
                t_power = internal_degree - sum(exponent)
                if t_power:
                    factors.append("t" if t_power == 1 else f"t^{t_power}")
            terms.append("*".join(factors))
    return "+".join(terms) if terms else "0"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chart", choices=VARIABLES, required=True)
    parser.add_argument("--w-value", type=int, default=25)
    args = parser.parse_args()
    if args.w_value % P == 0:
        raise RuntimeError("w must be nonzero")
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    reduced = {ell: substitute(rows[ell]) for ell in imposed}
    print("ring R=127,(w,u,c,d2,d4,x1,x5,v,t),dp;")
    for ell in imposed:
        print(f"poly a{ell}={polynomial_string(reduced[ell], False)};")
        print(f"poly e{ell}={polynomial_string(reduced[ell], True)};")
    print("poly aloc=u*x5*v-1;")
    print("poly eloc=u*x5*v-t^3;")
    print("int homogenization_fail=0;")
    for ell in imposed:
        print(f"if(subst(e{ell},t,1)-a{ell}!=0){{homogenization_fail=homogenization_fail+1;}}")
    print("if(subst(eloc,t,1)-aloc!=0){homogenization_fail=homogenization_fail+1;}")
    print("ideal J=e1,e3,e5,e7,e2,e4,eloc;")
    print(f"ideal B=J,w-{args.w_value % P},t,{args.chart}-1;")
    print("ideal G=std(B);")
    print("int boundary_empty=0;if(reduce(1,G)==0){boundary_empty=1;}")
    print('print("Q8-PROJECTIVE-FIBRE-RAW-BOUNDARY");')
    print(f'print("w_value={args.w_value % P}");')
    print(f'print("chart={args.chart}");')
    print('print("homogenization_fail="+string(homogenization_fail));')
    print('print("boundary_empty="+string(boundary_empty));')
    print('print("basis_size="+string(size(G)));')


if __name__ == "__main__":
    main()

