#!/usr/bin/env python3
"""Emit exact unloaded-overlap horizontal-tangent certificates."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
ORDER3 = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
ORDER3_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_compiler():
    for path, expected in ((COMPILER, COMPILER_SHA256), (ORDER3, ORDER3_SHA256)):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_overlap_tangent_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(engine: str, order: str) -> str:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    tnames = ["tc", "td2", "td4", "tx1", "tx3", "tx5"]
    variables = names + tnames
    ordering = "dp" if order == "dp" else f"(dp({len(names)}),dp({len(tnames)}))"
    lines = [f"ring R=0,({','.join(variables)}),{ordering};", "option(redSB);"]
    for ell in range(1, 9):
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "ideal E=w,x1,x3,x5;",
        f"ideal GE={engine}(E);",
    ])
    tangent_names = dict(zip(names[1:], tnames))
    for ell in imposed:
        terms = [f"diff(e{ell},w)"]
        for name in names[1:]:
            terms.append(f"diff(e{ell},{name})*{tangent_names[name]}")
        lines.append(f"poly L{ell}=reduce({'+'.join(terms)},GE);")
    lines.extend([
        "poly u=d2-d4;",
        "poly F2=u^2+2*d4*(1-u);",
        "poly F4=2*u^2-3*u+d4*(1-u);",
        f"ideal GL24={engine}(L2,L4);",
        f"ideal GF24={engine}(F2,F4);",
        f"ideal GT={engine}(d2-2*d4,d4*(d4-2));",
        "int l_to_f=1;for(int i=1;i<=size(GL24);i++){if(reduce(GL24[i],GF24)!=0){l_to_f=0;}}",
        "int f_to_l=1;for(int i=1;i<=size(GF24);i++){if(reduce(GF24[i],GL24)!=0){f_to_l=0;}}",
        "int f_to_t=1;for(int i=1;i<=size(GF24);i++){if(reduce(GF24[i],GT)!=0){f_to_t=0;}}",
        "int t_to_f=1;for(int i=1;i<=size(GT);i++){if(reduce(GT[i],GF24)!=0){t_to_f=0;}}",
        f"ideal J0={engine}(L1,L3,L5,d2,d4);",
        f"ideal T0={engine}(d2,d4,tx1,tx3,tx5);",
        "int j0_to_t0=1;for(int i=1;i<=size(J0);i++){if(reduce(J0[i],T0)!=0){j0_to_t0=0;}}",
        "int t0_to_j0=1;for(int i=1;i<=size(T0);i++){if(reduce(T0[i],J0)!=0){t0_to_j0=0;}}",
        "poly L7at0=reduce(L7,T0);",
        f"ideal J42={engine}(L1,L3,L5,d2-4,d4-2);",
        f"ideal T42={engine}(d2-4,d4-2,tx1-8*c-8/3,tx3-20*c-88/9,tx5-12*c-16/3);",
        "int j42_to_t42=1;for(int i=1;i<=size(J42);i++){if(reduce(J42[i],T42)!=0){j42_to_t42=0;}}",
        "int t42_to_j42=1;for(int i=1;i<=size(T42);i++){if(reduce(T42[i],J42)!=0){t42_to_j42=0;}}",
        "poly L7at42=reduce(L7,T42);",
        "int residual42=0;if(L7at42==-16/27){residual42=1;}",
        'print("Q8-W0-OVERLAP-HORIZONTAL-TANGENT");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("L2="+string(L2));',
        'print("L4="+string(L4));',
        'print("L24_F24_ideal_identity="+string(l_to_f*f_to_l));',
        'print("F24_root_ideal_identity="+string(f_to_t*t_to_f));',
        'print("F24_vdim="+string(vdim(GF24)));',
        'print("branch0_linear_ideal_identity="+string(j0_to_t0*t0_to_j0));',
        'print("branch0_L7="+string(L7at0));',
        'print("branch42_linear_ideal_identity="+string(j42_to_t42*t42_to_j42));',
        'print("branch42_L7="+string(L7at42));',
        'print("branch42_scaled_L7="+string(729*L7at42));',
        'print("branch42_residual_identity="+string(residual42));',
        'print("F24_BASIS_BEGIN");',
        "GF24;",
        'print("F24_BASIS_END");',
        'print("BRANCH0_BASIS_BEGIN");',
        "J0;",
        'print("BRANCH0_BASIS_END");',
        'print("BRANCH42_BASIS_BEGIN");',
        "J42;",
        'print("BRANCH42_BASIS_END");',
        'print("Q8_W0_OVERLAP_HORIZONTAL_TANGENT_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.engine, args.order))
