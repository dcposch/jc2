#!/usr/bin/env python3
"""Emit the exact finite-x5-cylinder local-germ certificate."""

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
    spec = importlib.util.spec_from_file_location("q8_x5_cylinder_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(engine: str, order: str) -> str:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    variables = names + ["ib"]
    ordering = "dp" if order == "dp" else f"(dp({len(names)}),dp(1))"
    lines = [f"ring R=0,({','.join(variables)}),{ordering};", "option(redSB);"]
    for ell in range(1, 9):
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    ordered = [f"e{ell}" for ell in imposed]
    yvars = names[1:]
    lines.extend([
        "ideal I=" + ",".join(ordered) + ";",
        "ideal E=x5,x1-x3,d2,d4,c*x3-1,ib*x3-1;",
        f"ideal GE={engine}(E);",
        "int rowszero=1;for(int i=1;i<=size(I);i++){if(reduce(I[i],GE)!=0){rowszero=0;}}",
        "matrix J[6][7];",
        "matrix Jy[6][6];",
    ])
    for i, row in enumerate(ordered, start=1):
        for j, variable in enumerate(names, start=1):
            lines.append(f"J[{i},{j}]=diff({row},{variable});")
        for j, variable in enumerate(yvars, start=1):
            lines.append(f"Jy[{i},{j}]=diff({row},{variable});")
    lines.extend([
        "int fwzero=1;",
        "for(int r=1;r<=6;r++){if(reduce(J[r,1],GE)!=0){fwzero=0;}}",
        "int sixzero=1;",
    ])
    for drop_col in range(1, 8):
        name = f"D{drop_col}"
        lines.append(f"matrix {name}[6][6];")
        columns = [j for j in range(1, 8) if j != drop_col]
        for i in range(1, 7):
            for jj, j in enumerate(columns, start=1):
                lines.append(f"{name}[{i},{jj}]=J[{i},{j}];")
        lines.append(f"poly det6_{drop_col}=det({name});")
        lines.append(f"if(reduce(det6_{drop_col},GE)!=0){{sixzero=0;}}")
    # Drop source row e5 (third in imposed order) and coefficient column c
    # (first in yvars). This is the frozen nonzero minor from the tangent probe.
    lines.append("matrix M5[5][5];")
    rr = [1, 2, 4, 5, 6]
    cc = [2, 3, 4, 5, 6]
    for ii, i in enumerate(rr, start=1):
        for jj, j in enumerate(cc, start=1):
            lines.append(f"M5[{ii},{jj}]=Jy[{i},{j}];")
    lines.extend([
        "poly det5=det(M5);",
        "poly det5_expected=1024*x3^6/1594323;",
        "int det5ok=0;if(reduce(det5-det5_expected,GE)==0){det5ok=1;}",
        # y-kernel vector tangent to c*x3=1, x1=x3.
        "matrix ky[6][1];",
        "ky[1,1]=-ib^2;ky[2,1]=0;ky[3,1]=0;ky[4,1]=1;ky[5,1]=1;ky[6,1]=0;",
        "matrix kyimage=Jy*ky;",
        "int kyzero=1;for(int s=1;s<=6;s++){if(reduce(kyimage[s,1],GE)!=0){kyzero=0;}}",
        'print("Q8-W0-X5-CYLINDER-LOCAL-GERM");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("cylinder_dim="+string(dim(GE)));',
        'print("source_rows_zero="+string(rowszero));',
        'print("Fw_zero="+string(fwzero));',
        'print("all_6x6_minors_zero="+string(sixzero));',
        'print("rank5_minor_identity="+string(det5ok));',
        'print("rank5_minor_normal_form="+string(reduce(det5,GE)));',
        'print("a_kernel_zero="+string(kyzero));',
        'print("e6_normal_form="+string(reduce(e6,GE)));',
        'print("e8_normal_form="+string(reduce(e8,GE)));',
        'print("CYLINDER_BASIS_BEGIN");',
        "GE;",
        'print("CYLINDER_BASIS_END");',
        'print("Q8_W0_X5_CYLINDER_LOCAL_GERM_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.engine, args.order))


if __name__ == "__main__":
    main()
