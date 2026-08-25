#!/usr/bin/env python3
"""Emit exact series-coefficient checks for the b=1 slope-three candidate."""

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
    spec = importlib.util.spec_from_file_location("q8_slope3_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def differentiated(name: str, order: int) -> str:
    out = name
    for _ in range(order):
        out = f"diff({out},t)"
    factorial = 1
    for i in range(2, order + 1):
        factorial *= i
    return f"subst({out},t,0)/{factorial}"


def source(engine: str, order: str) -> str:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    ordering1 = "dp" if order == "dp" else "(dp(9))"
    ordering2 = "dp" if order == "dp" else "(dp(11))"
    lines = ["ring S=0,(w,c,d2,d4,x1,x3,x5),dp;"]
    for ell in range(1, 9):
        lines.append(f"poly se{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.append("ideal SI=" + ",".join(f"se{i}" for i in imposed) + ";")

    # Leading slope-three chart.
    lines.extend([
        f"ring L=0,(t,c,b,z,Q1,W,U2,X2,Z2),{ordering1};",
        "option(redSB);",
        "map leadmap=S,t^3*W,c,b+1+Q1*t,b,U2*t^2,z*t+X2*t^2,z*t+Z2*t^2;",
    ])
    for ell in imposed:
        lines.append(f"poly le{ell}=leadmap(se{ell});")
    coeff_names: list[str] = []
    for ell in imposed:
        max_degree = 2 if ell in (1, 3, 5, 7) else 3
        for degree in range(1, max_degree + 1):
            name = f"l{ell}_{degree}"
            lines.append(f"poly {name}={differentiated(f'le{ell}', degree)};")
            coeff_names.append(name)
    lines.extend([
        "ideal Lead=" + ",".join(coeff_names) + ";",
        "ideal ELead=b-1,U2,3*Q1-(3*c-1)*z,3*(X2-Z2)+z^2,9*W-2*z^3;",
        f"ideal GLead={engine}(Lead);",
        f"ideal GELead={engine}(ELead);",
        "int lead_to_expected=1;for(int il=1;il<=size(GLead);il++){if(reduce(GLead[il],GELead)!=0){lead_to_expected=0;}}",
        "int expected_to_lead=1;for(int jl=1;jl<=size(GELead);jl++){if(reduce(GELead[jl],GLead)!=0){expected_to_lead=0;}}",
    ])

    # Unramified continuation chart.  A fresh ring avoids coefficient carry.
    lines.extend([
        f"ring C=0,(t,c,C1,Q2,U3,B1,B2,X3,W4,A,aux),{ordering2};",
        "option(redSB);",
        "map contmap=S,2/9*t^3+W4*t^4,c+C1*t,2+(B1+c-1/3)*t+(B2+Q2)*t^2,1+B1*t+B2*t^2,U3*t^3,t-1/3*t^2+X3*t^3,t;",
        "poly ce1=contmap(se1);poly ce5=contmap(se5);poly ce7=contmap(se7);",
        f"poly C1e={differentiated('ce1',3)};",
        f"poly C5e={differentiated('ce5',3)};",
        f"poly C7e={differentiated('ce7',3)};",
        "ideal Actual=C1e,C5e,C7e,A-C1+Q2;",
        "ideal Expected=9*(A+U3)+c+1,-26*c-27*B1+9*(A+U3)-15,83*c+81*B1+18*(A+U3)-58,A-C1+Q2;",
        f"ideal GActual={engine}(Actual);",
        f"ideal GExpected={engine}(Expected);",
        "int actual_to_expected=1;for(int ia=1;ia<=size(GActual);ia++){if(reduce(GActual[ia],GExpected)!=0){actual_to_expected=0;}}",
        "int expected_to_actual=1;for(int ja=1;ja<=size(GExpected);ja++){if(reduce(GExpected[ja],GActual)!=0){expected_to_actual=0;}}",
        "int actual_unit=0;if(reduce(1,GActual)==0){actual_unit=1;}",
        "poly P1=9*(A+U3)+c+1;",
        "poly P5=-26*c-27*B1+9*(A+U3)-15;",
        "poly P7=83*c+81*B1+18*(A+U3)-58;",
        f"ideal G12={engine}(P1,P5,A-C1+Q2);",
        "poly third_residual=reduce(P7,G12);",
        'print("Q8-W0-RANKDROP-SLOPE3-CONTINUATION");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("leading_ideal_identity="+string(lead_to_expected*expected_to_lead));',
        'print("actual_expected_ideal_identity="+string(actual_to_expected*expected_to_actual));',
        'print("continuation_unit="+string(actual_unit));',
        'print("third_residual="+string(third_residual));',
        'print("ACTUAL_COEFFICIENTS_BEGIN");C1e;C5e;C7e;print("ACTUAL_COEFFICIENTS_END");',
        'print("LEADING_BASIS_BEGIN");GLead;print("LEADING_BASIS_END");',
        'print("Q8_W0_RANKDROP_SLOPE3_CONTINUATION_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.engine, args.order))
