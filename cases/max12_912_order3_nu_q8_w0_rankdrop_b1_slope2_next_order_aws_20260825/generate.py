#!/usr/bin/env python3
"""Emit the exact b=1 selected slope-two next coefficient ideal."""

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
    spec = importlib.util.spec_from_file_location("q8_b1_slope2_next_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def coeff(name: str, degree: int) -> str:
    out = name
    for _ in range(degree):
        out = f"diff({out},t)"
    factorial = 1
    for j in range(2, degree + 1):
        factorial *= j
    return f"subst({out},t,0)/{factorial}"


def source(engine: str, order: str) -> str:
    q = load_compiler()
    _, rows, imposed, names = q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    ordering = "dp" if order == "dp" else "(dp(1),dp(7))"
    lines = ['LIB "elim.lib";', 'ring S=0,(w,c,d2,d4,x1,x3,x5),dp;']
    for ell in range(1, 9):
        lines.append(f"poly se{ell}={q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "ideal SI=" + ",".join(f"se{i}" for i in imposed) + ";",
        f"ring R=0,(t,c,C1,B1,Q1,U2,X2,W3),{ordering};",
        "option(redSB);",
        "map phi=S,-4/9*t^2+W3*t^3,c+C1*t,2+(B1+Q1)*t,1+B1*t,U2*t^2,5/3*t+X2*t^2,t;",
    ])
    for ell in imposed:
        lines.append(f"poly f{ell}=phi(se{ell});")
    leading = [f"l{ell}" for ell in (1, 3, 5, 7, 2, 4)]
    for ell in (1, 3, 5, 7):
        lines.append(f"poly l{ell}={coeff(f'f{ell}', 1)};")
        lines.append(f"poly n{ell}={coeff(f'f{ell}', 2)};")
    for ell in (2, 4):
        lines.append(f"poly l{ell}={coeff(f'f{ell}', 2)};")
        lines.append(f"poly n{ell}={coeff(f'f{ell}', 3)};")
    lines.extend([
        "ideal Leading=" + ",".join(leading) + ";",
        f"ideal GLeading={engine}(Leading);",
        "int leading_zero=1;int ii;for(ii=1;ii<=size(Leading);ii++){if(Leading[ii]!=0){leading_zero=0;}}",
        "ideal Next=n1,n3,n5,n7,n2,n4;",
        f"ideal GNext={engine}(Next);",
        "int next_unit=0;if(reduce(1,GNext)==0){next_unit=1;}",
        "ideal Ec=eliminate(GNext,C1*B1*Q1*U2*X2*W3);",
        f"ideal GEc={engine}(Ec);",
        'print("Q8-W0-RANKDROP-B1-SLOPE2-NEXT");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("leading_zero="+string(leading_zero));',
        'print("next_unit="+string(next_unit));',
        'print("NEXT_COEFFICIENTS_BEGIN");n1;n3;n5;n7;n2;n4;print("NEXT_COEFFICIENTS_END");',
        'print("NEXT_BASIS_BEGIN");GNext;print("NEXT_BASIS_END");',
        'print("C_ELIMINANT_BEGIN");GEc;print("C_ELIMINANT_END");',
        'print("Q8_W0_RANKDROP_B1_SLOPE2_NEXT_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.engine, args.order))

