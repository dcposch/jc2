#!/usr/bin/env python3
"""Generate the exact global t-saturation and all boundary charts."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/max12_912_order3_nu_q8_projective_fibre_boundary_aws_20260825/generate.py"
BASE_SHA256 = "db3eb90879a41efa045a0bd7ce8fe0220d66b2de409ff06ca96d1bfeb21538d5"


def load_base():
    raw = BASE.read_bytes()
    if sha256(raw).hexdigest() != BASE_SHA256:
        raise RuntimeError("base generator hash")
    spec = importlib.util.spec_from_file_location("q8_projective_boundary_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--w-value", type=int, default=25)
    args = parser.parse_args()
    B = load_base()
    if args.w_value % B.P == 0:
        raise RuntimeError("w must be nonzero")
    Q = B.load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    reduced = {ell: B.substitute(rows[ell]) for ell in imposed}
    print("ring R=127,(z,w,u,c,d2,d4,x1,x5,v,t),(lp(1),dp(9));")
    for ell in imposed:
        print(f"poly a{ell}={B.polynomial_string(reduced[ell], False)};")
        print(f"poly e{ell}={B.polynomial_string(reduced[ell], True)};")
    print("poly aloc=u*x5*v-1;")
    print("poly eloc=u*x5*v-t^3;")
    print("int homogenization_fail=0;")
    for ell in imposed:
        print(f"if(subst(e{ell},t,1)-a{ell}!=0){{homogenization_fail=homogenization_fail+1;}}")
    print("if(subst(eloc,t,1)-aloc!=0){homogenization_fail=homogenization_fail+1;}")
    print("ideal J=e1,e3,e5,e7,e2,e4,eloc;")
    print("ideal K=J,z*t-1;")
    print("ideal C=eliminate(K,z);")
    print('print("Q8-PROJECTIVE-FIBRE-SATURATED-BOUNDARY");')
    print(f'print("w_value={args.w_value % B.P}");')
    print('print("homogenization_fail="+string(homogenization_fail));')
    print('print("closure_basis_size="+string(size(C)));')
    print("int empty_count=0;")
    for chart in B.VARIABLES:
        label = chart.replace("x", "x")
        print(f"ideal B_{label}=C,w-{args.w_value % B.P},t,{chart}-1;")
        print(f"ideal G_{label}=std(B_{label});")
        print(f"int empty_{label}=0;if(reduce(1,G_{label})==0){{empty_{label}=1;empty_count=empty_count+1;}}")
        print(f'print("chart_{chart}_empty="+string(empty_{label}));')
        print(f'print("chart_{chart}_basis_size="+string(size(G_{label})));')
    print('print("empty_count="+string(empty_count));')


if __name__ == "__main__":
    main()

