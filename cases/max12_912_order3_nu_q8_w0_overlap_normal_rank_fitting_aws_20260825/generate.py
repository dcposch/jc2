#!/usr/bin/env python3
"""Emit exact-Q Fitting/rank-stratified overlap tangent incidence."""

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
    spec = importlib.util.spec_from_file_location("q8_overlap_fitting_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def emit_minors(matrix: str, nrows: int, ncols: int, size: int, prefix: str) -> tuple[list[str], list[str]]:
    lines: list[str] = []
    names: list[str] = []
    idx = 0
    for rows in combinations(range(1, nrows + 1), size):
        for cols in combinations(range(1, ncols + 1), size):
            idx += 1
            mat = f"{prefix}A{idx}"
            pol = f"{prefix}m{idx}"
            lines.append(f"matrix {mat}[{size}][{size}];")
            for ii, row in enumerate(rows, start=1):
                for jj, col in enumerate(cols, start=1):
                    lines.append(f"{mat}[{ii},{jj}]={matrix}[{row},{col}];")
            lines.append(f"poly {pol}=det({mat});")
            names.append(pol)
    return lines, names


def source(engine: str, order: str) -> str:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    variables = names + ["id2", "id4"]
    ordering = "dp" if order == "dp" else f"(dp({len(names)}),dp(2))"
    lines = ['LIB "elim.lib";', f"ring R=0,({','.join(variables)}),{ordering};", "option(redSB);"]
    for ell in range(1, 9):
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    ordered = [f"e{ell}" for ell in imposed]
    lines.extend([
        f"ideal I={','.join(ordered)};",
        "ideal A3=w,x1,x3,x5;",
        f"ideal GA3={engine}(A3);",
        "int rowszero=1;for(int ir=1;ir<=size(I);ir++){if(reduce(I[ir],GA3)!=0){rowszero=0;}}",
        "int tangentzero=1;",
        "matrix M[6][3];",
        "matrix N[6][4];",
    ])
    for i, row in enumerate(ordered, start=1):
        for j, var in enumerate(("x1", "x3", "x5"), start=1):
            lines.append(f"M[{i},{j}]=reduce(diff({row},{var}),GA3);")
            lines.append(f"N[{i},{j}]=M[{i},{j}];")
        lines.append(f"N[{i},4]=reduce(diff({row},w),GA3);")
        for var in ("c", "d2", "d4"):
            lines.append(f"if(reduce(diff({row},{var}),GA3)!=0){{tangentzero=0;}}")

    all_sets: dict[str, list[str]] = {}
    for matrix, ncols, size, prefix in (
        ("M", 3, 3, "M3"),
        ("M", 3, 2, "M2"),
        ("M", 3, 1, "M1"),
        ("N", 4, 4, "N4"),
        ("N", 4, 3, "N3"),
        ("N", 4, 2, "N2"),
    ):
        block, polys = emit_minors(matrix, 6, ncols, size, prefix)
        lines.extend(block)
        all_sets[prefix] = polys
        lines.append(f"ideal I{prefix}={','.join(polys)};")
    fw_names = [f"N[{i},4]" for i in range(1, 7)]
    lines.extend([
        "list LS3=sat(IN4,IM3);ideal K3=LS3[1];",
        "ideal P2=IM3,IN3;list LS2=sat(P2,IM2);ideal K2=LS2[1];",
        "ideal P1=IM2,IN2;list LS1=sat(P1,IM1);ideal K1=LS1[1];",
        f"ideal K0=IM1,{','.join(fw_names)};",
        f"ideal GM3={engine}(IM3);",
        f"ideal GK3={engine}(K3);",
        f"ideal GK2={engine}(K2);",
        f"ideal GK1={engine}(K1);",
        f"ideal GK0={engine}(K0);",
    ])
    for rank in (3, 2, 1, 0):
        lines.extend([
            f"ideal K{rank}d2=GK{rank},id2*d2-1;",
            f"ideal K{rank}d4=GK{rank},id4*d4-1;",
            f"ideal GK{rank}d2={engine}(K{rank}d2);",
            f"ideal GK{rank}d4={engine}(K{rank}d4);",
            f"int K{rank}unit=0;if(reduce(1,GK{rank})==0){{K{rank}unit=1;}}",
            f"int K{rank}Dd2empty=0;if(reduce(1,GK{rank}d2)==0){{K{rank}Dd2empty=1;}}",
            f"int K{rank}Dd4empty=0;if(reduce(1,GK{rank}d4)==0){{K{rank}Dd4empty=1;}}",
        ])
    lines.extend([
        'print("Q8-W0-OVERLAP-NORMAL-RANK-FITTING");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("a3_source_rows_zero="+string(rowszero));',
        'print("a3_tangent_columns_zero="+string(tangentzero));',
    ])
    for rank in (3, 2, 1, 0):
        lines.extend([
            f'print("K{rank}_unit="+string(K{rank}unit));',
            f'print("K{rank}_Dd2_empty="+string(K{rank}Dd2empty));',
            f'print("K{rank}_Dd4_empty="+string(K{rank}Dd4empty));',
            f'print("K{rank}_BASIS_BEGIN");',
            f"GK{rank};",
            f'print("K{rank}_BASIS_END");',
        ])
    lines.extend([
        'print("RANKDROP_BASIS_BEGIN");',
        "GM3;",
        'print("RANKDROP_BASIS_END");',
        'print("Q8_W0_OVERLAP_NORMAL_RANK_FITTING_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.engine, args.order))
