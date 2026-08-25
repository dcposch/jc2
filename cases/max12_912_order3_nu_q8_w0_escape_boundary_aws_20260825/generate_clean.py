#!/usr/bin/env python3
"""Diagnostic-free successor generator for the frozen escape source."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate.py"
BASE_SHA256 = "7439f408887ab9602964930e1c1d25c50c6e9f62f240a4bb326a00a0020b7a07"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_w0_escape_frozen_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


B = load_base()


def clean_finite(mode: str, engine: str, order: str, print_basis: bool) -> str:
    source = B.finite_source(mode, engine, order, print_basis)
    source = source.replace(
        "int ItoE=1;for(int i=1;i<=size(I);i++){if(reduce(I[i],GE)!=0){ItoE=0;}}",
        "int ItoE=1;for(int j=1;j<=size(I);j++){if(reduce(I[j],GE)!=0){ItoE=0;}}",
    )
    source = source.replace(
        "int EtoI=1;for(int i=1;i<=size(E);i++){if(reduce(E[i],G)!=0){EtoI=0;}}",
        "int EtoI=1;for(int k=1;k<=size(E);k++){if(reduce(E[k],G)!=0){EtoI=0;}}",
    )
    return source


def clean_tangent() -> str:
    Q = B.load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    yvars = names[1:]
    lines = [f"ring R=(0,a),({','.join(names)}),dp;", "option(redSB);"]
    for ell in imposed:
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    ordered = [f"e{ell}" for ell in imposed]
    lines.extend(["matrix J[6][6];", "matrix Aug[6][7];"])
    for i, row in enumerate(ordered, start=1):
        for j, variable in enumerate(yvars, start=1):
            value = B.substitution(f"diff({row},{variable})")
            lines.append(f"J[{i},{j}]={value};Aug[{i},{j}]={value};")
        lines.append(f"Aug[{i},7]={B.substitution(f'diff({row},w)')};")
    lines.extend([
        'print("Q8-W0-X5-GENERIC-TANGENT-CLEAN");',
        'print("rank_J="+string(rank(J)));',
        'print("rank_Aug="+string(rank(Aug)));',
    ])
    for drop_row in range(1, 7):
        for drop_col in range(1, 7):
            name = f"N_{drop_row}_{drop_col}"
            lines.append(f"matrix {name}[5][5];")
            rr = [i for i in range(1, 7) if i != drop_row]
            cc = [j for j in range(1, 7) if j != drop_col]
            for ii, i in enumerate(rr, start=1):
                for jj, j in enumerate(cc, start=1):
                    lines.append(f"{name}[{ii},{jj}]=J[{i},{j}];")
            lines.append(f'print("minor5_drop_{drop_row}_{drop_col}="+string(det({name})));')
    for drop_col in range(1, 8):
        name = f"D_{drop_col}"
        lines.append(f"matrix {name}[6][6];")
        cc = [j for j in range(1, 8) if j != drop_col]
        for i in range(1, 7):
            for jj, j in enumerate(cc, start=1):
                lines.append(f"{name}[{i},{jj}]=Aug[{i},{j}];")
        lines.append(f'print("minor6_aug_drop_{drop_col}="+string(det({name})));')
    lines.extend(['print("Q8_W0_X5_GENERIC_TANGENT_PASS");', "exit;"])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("finite", "tangent"), required=True)
    parser.add_argument("--mode", choices=B.FINITE_MODES)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    parser.add_argument("--print-basis", action="store_true")
    args = parser.parse_args()
    if args.kind == "tangent":
        print(clean_tangent())
    else:
        if args.mode is None:
            raise RuntimeError("--mode required")
        print(clean_finite(args.mode, args.engine, args.order, args.print_basis))


if __name__ == "__main__":
    main()
