#!/usr/bin/env python3
"""Emit exact special-fibre rank, normal obstruction, and IFT-jet checks."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from itertools import combinations
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
    spec = importlib.util.spec_from_file_location("q8_overlap_ift_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def minor_matrix(name: str, source: str, rows: tuple[int, ...], ncols: int) -> list[str]:
    lines = [f"matrix {name}[{len(rows)}][{ncols}];"]
    for ii, row in enumerate(rows, start=1):
        for col in range(1, ncols + 1):
            lines.append(f"{name}[{ii},{col}]={source}[{row},{col}];")
    return lines


def source(engine: str, order: str) -> str:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    variables = names + ["id2", "id4"]
    ordering = "dp" if order == "dp" else f"(dp({len(names)}),dp(2))"
    lines = [f"ring R=0,({','.join(variables)}),{ordering};", "option(redSB);"]
    for ell in range(1, 9):
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    ordered = [f"e{ell}" for ell in imposed]
    lines.extend([
        f"ideal I={','.join(ordered)};",
        "ideal A3=w,x1,x3,x5;",
        f"ideal GA3={engine}(A3);",
        "int a3rows=1;for(int i=1;i<=size(I);i++){if(reduce(I[i],GA3)!=0){a3rows=0;}}",
        "matrix M[6][3];",
        "matrix N[6][4];",
        "int tangentcols=1;",
    ])
    normal_vars = ("x1", "x3", "x5")
    tangent_vars = ("c", "d2", "d4")
    for i, row in enumerate(ordered, start=1):
        for j, var in enumerate(normal_vars, start=1):
            lines.append(f"M[{i},{j}]=reduce(diff({row},{var}),GA3);")
            lines.append(f"N[{i},{j}]=M[{i},{j}];")
        lines.append(f"N[{i},4]=reduce(diff({row},w),GA3);")
        for var in tangent_vars:
            lines.append(f"if(reduce(diff({row},{var}),GA3)!=0){{tangentcols=0;}}")
    three_names = []
    for idx, rows3 in enumerate(combinations(range(1, 7), 3), start=1):
        name = f"M3_{idx}"
        lines.extend(minor_matrix(name, "M", rows3, 3))
        lines.append(f"poly m3_{idx}=det({name});")
        three_names.append(f"m3_{idx}")
    lines.append(f"ideal IM3={','.join(three_names)};")
    lines.append(f"ideal GM3={engine}(IM3);")
    lines.append("int rank3_everywhere=0;if(reduce(1,GM3)==0){rank3_everywhere=1;}")
    four_names = []
    for idx, rows4 in enumerate(combinations(range(1, 7), 4), start=1):
        name = f"N4_{idx}"
        lines.extend(minor_matrix(name, "N", rows4, 4))
        lines.append(f"poly n4_{idx}=det({name});")
        four_names.append(f"n4_{idx}")
    lines.extend([
        f"ideal IN4={','.join(four_names)};",
        f"ideal GN4={engine}(IN4);",
        "ideal D0=d2,d4;",
        f"ideal GD0={engine}(D0);",
        "int obs_at_d0=1;for(int i=1;i<=size(IN4);i++){if(reduce(IN4[i],GD0)!=0){obs_at_d0=0;}}",
        "ideal ID2=IN4,id2*d2-1;",
        "ideal ID4=IN4,id4*d4-1;",
        f"ideal KD2={engine}(ID2);",
        f"ideal KD4={engine}(ID4);",
        "int obs_no_Dd2=0;if(reduce(1,KD2)==0){obs_no_Dd2=1;}",
        "int obs_no_Dd4=0;if(reduce(1,KD4)==0){obs_no_Dd4=1;}",
        "ideal Q0=w,d2,d4,x1,x3,x5;",
        f"ideal GQ0={engine}(Q0);",
        "matrix T[3][3];",
        "T[1,1]=reduce(diff(e1,x5),GQ0);T[1,2]=reduce(diff(e1,x3),GQ0);T[1,3]=reduce(diff(e1,x1),GQ0);",
        "T[2,1]=reduce(diff(e3,x5),GQ0);T[2,2]=reduce(diff(e3,x3),GQ0);T[2,3]=reduce(diff(e3,x1),GQ0);",
        "T[3,1]=reduce(diff(e5,x5),GQ0);T[3,2]=reduce(diff(e5,x3),GQ0);T[3,3]=reduce(diff(e5,x1),GQ0);",
        "int triangular=1;",
        "if(T[1,1]!=4/9||T[1,2]!=0||T[1,3]!=0){triangular=0;}",
        "if(T[2,1]!=-20/27||T[2,2]!=4/9||T[2,3]!=0){triangular=0;}",
        "if(T[3,1]!=40/81||T[3,2]!=-4/9||T[3,3]!=4/9){triangular=0;}",
        "poly detT=det(T);",
        "ideal S=d2,d4,x1,x3,x5;",
        f"ideal GS={engine}(S);",
        "int sheet=1;for(int i=1;i<=size(I);i++){if(reduce(I[i],GS)!=0){sheet=0;}}",
        "ideal XD=x1^2,x1*x3,x1*x5,x3^2,x3*x5,x5^2;",
        "ideal DX=d2*x1,d2*x3,d2*x5,d4*x1,d4*x3,d4*x5;",
        "ideal WD2=w*d2^2,w*d2*d4,w*d4^2;",
        "ideal J2=XD,DX,WD2;",
        "ideal J1=XD,DX,w*d2,w*d4;",
        f"ideal GJ2={engine}(J2);",
        f"ideal GJ1={engine}(J1);",
        "poly R1=e1-4/9*x5;",
        "poly R3=e3-(4/9*x3-20/27*x5);",
        "poly R5=e5-(4/9*x1-4/9*x3+40/81*x5);",
        "int support1=0;if(reduce(R1,GJ2)==0){support1=1;}",
        "int support3=0;if(reduce(R3,GJ2)==0){support3=1;}",
        "int support5=0;if(reduce(R5,GJ1)==0){support5=1;}",
        "int lower_x_linear=1;",
        "if(reduce(diff(e2,x1),GQ0)!=0||reduce(diff(e2,x3),GQ0)!=0||reduce(diff(e2,x5),GQ0)!=0){lower_x_linear=0;}",
        "if(reduce(diff(e4,x1),GQ0)!=0||reduce(diff(e4,x3),GQ0)!=0||reduce(diff(e4,x5),GQ0)!=0){lower_x_linear=0;}",
        "poly g2d2=reduce(diff(diff(e2,w),d2),GQ0);",
        "poly g2d4=reduce(diff(diff(e2,w),d4),GQ0);",
        "poly g4d2=reduce(diff(diff(e4,w),d2),GQ0);",
        "poly g4d4=reduce(diff(diff(e4,w),d4),GQ0);",
        "int residual_linear=0;if(g2d2==0&&g2d4==4/9&&g4d2==4/9&&g4d4==-16/27){residual_linear=1;}",
        "poly residual_det=g2d2*g4d4-g2d4*g4d2;",
        'print("Q8-W0-OVERLAP-FORMAL-IFT");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("a3_source_rows_zero="+string(a3rows));',
        'print("a3_tangent_columns_zero="+string(tangentcols));',
        'print("a3_normal_rank3_everywhere="+string(rank3_everywhere));',
        'print("obstruction_vanishes_at_d0="+string(obs_at_d0));',
        'print("obstruction_Dd2_empty="+string(obs_no_Dd2));',
        'print("obstruction_Dd4_empty="+string(obs_no_Dd4));',
        'print("triangular_block_identity="+string(triangular));',
        'print("triangular_block_det="+string(detT));',
        'print("exact_boundary_sheet="+string(sheet));',
        'print("x5_support_membership="+string(support1));',
        'print("x3_support_membership="+string(support3));',
        'print("x1_support_membership="+string(support5));',
        'print("lower_rows_x_linear_zero="+string(lower_x_linear));',
        'print("G2_d2="+string(g2d2));',
        'print("G2_d4="+string(g2d4));',
        'print("G4_d2="+string(g4d2));',
        'print("G4_d4="+string(g4d4));',
        'print("residual_linear_identity="+string(residual_linear));',
        'print("residual_linear_det="+string(residual_det));',
        'print("OBSTRUCTION_BASIS_BEGIN");',
        "GN4;",
        'print("OBSTRUCTION_BASIS_END");',
        'print("Q8_W0_OVERLAP_FORMAL_IFT_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.engine, args.order))
