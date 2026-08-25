#!/usr/bin/env python3
"""Emit the original-J lift/cofactor problem over Q(c)."""

from __future__ import annotations

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
    spec = importlib.util.spec_from_file_location("q8_rankdrop_b1_jlift_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    q = load_compiler()
    _, rows, imposed, names = q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    lines = ["ring S=0,(w,c,d2,d4,x1,x3,x5),dp;"]
    for ell in range(1, 9):
        lines.append(f"poly se{ell}={q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "ideal SI=se1,se3,se5,se7,se2,se4;",
        "ring R=(0,c),(inv,w,u,x1,x3,x5),(dp(1),dp(5));",
        "map phi=S,w,c,2+u,1,x1,x3,x5;",
        "ideal I=phi(SI);poly A=x3-2*x5;",
        "ideal J=I,inv*w*x5*A-1;",
        "ideal ONE=1;matrix U;matrix LT=lift(J,ONE,U);",
        "matrix LR=matrix(ONE)*U-matrix(J)*LT;",
        "int raw_residual_zero=0;if(LR==0){raw_residual_zero=1;}",
        "poly uu=U[1,1];",
        "int scalar_unit=0;if(uu!=0){if(deg(uu)==0){scalar_unit=1;}}",
        "matrix H;if(scalar_unit==1){H=(1/uu)*LT;}",
        "matrix NR;if(scalar_unit==1){NR=matrix(ONE)-matrix(J)*H;}",
        "int normalized_residual_zero=0;if(scalar_unit==1){if(NR==0){normalized_residual_zero=1;}}",
        'print("Q8-W0-RANKDROP-B1-ORIGINAL-J-LIFT");',
        'print("field=Q(c)");',
        'print("raw_residual_zero="+string(raw_residual_zero));',
        'print("scalar_unit="+string(scalar_unit));',
        'print("normalized_residual_zero="+string(normalized_residual_zero));',
        'print("U_BEGIN");U;print("U_END");',
        'print("LT_BEGIN");LT;print("LT_END");',
        'print("H_BEGIN");H;print("H_END");',
        'print("Q8_W0_RANKDROP_B1_ORIGINAL_J_LIFT_PASS");',
        "exit;",
    ])
    print("\n".join(lines))


if __name__ == "__main__":
    main()
