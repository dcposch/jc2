#!/usr/bin/env python3
"""Emit generic rank-drop loaded saturation or bounded weighted Rees screens."""

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
    spec = importlib.util.spec_from_file_location("q8_rankdrop_rees_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source_rows() -> tuple[list[str], tuple[int, ...]]:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    strings = [Q.M.coeff_string(rows[ell], names) for ell in range(1, 9)]
    return strings, tuple(imposed)


def source_ring(lines: list[str], rows: list[str], imposed: tuple[int, ...]) -> None:
    lines.append("ring S=0,(w,c,d2,d4,x1,x3,x5),dp;")
    for ell, row in enumerate(rows, start=1):
        lines.append(f"poly se{ell}={row};")
    lines.append("ideal SI=" + ",".join(f"se{i}" for i in imposed) + ";")


def loaded(engine: str, order: str) -> str:
    rows, imposed = source_rows()
    lines = ['LIB "elim.lib";']
    source_ring(lines, rows, imposed)
    ordering = "dp" if order == "dp" else "(dp(5))"
    lines.extend([
        f"ring R=(0,c,b),(w,u,x1,x3,x5),{ordering};",
        "option(redSB);",
        "map phi=S,w,c,b+1+u,b,x1,x3,x5;",
        "ideal I=phi(SI);",
        "poly A=x3-2*x5;",
        "ideal Load=w*x5*A;",
        "ideal Q=w,x1,x3,x5;",
        "list Lsel=sat(I,Load);ideal Csel=Lsel[1];",
        f"ideal GCsel={engine}(Csel);",
        "ideal Tsel=GCsel,w,u,x1,x3,x5;",
        f"ideal GTsel={engine}(Tsel);",
        "int selected_landing_empty=0;if(reduce(1,GTsel)==0){selected_landing_empty=1;}",
        "list Loff=sat(I,Q);ideal Coff=Loff[1];",
        f"ideal GCoff={engine}(Coff);",
        "ideal Toff=GCoff,w,u,x1,x3,x5;",
        f"ideal GToff={engine}(Toff);",
        "int off_boundary_landing_empty=0;if(reduce(1,GToff)==0){off_boundary_landing_empty=1;}",
        'print("Q8-W0-RANKDROP-LOADED-CLOSURE");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("selected_landing_empty="+string(selected_landing_empty));',
        'print("off_boundary_landing_empty="+string(off_boundary_landing_empty));',
        'print("SELECTED_LANDING_BASIS_BEGIN");GTsel;print("SELECTED_LANDING_BASIS_END");',
        'print("OFF_BOUNDARY_LANDING_BASIS_BEGIN");GToff;print("OFF_BOUNDARY_LANDING_BASIS_END");',
        'print("SELECTED_SAT_BASIS_BEGIN");GCsel;print("SELECTED_SAT_BASIS_END");',
        'print("Q8_W0_RANKDROP_LOADED_CLOSURE_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


def weighted(engine: str, order: str) -> str:
    rows, imposed = source_rows()
    lines = ['LIB "elim.lib";']
    source_ring(lines, rows, imposed)
    ordering = "dp" if order == "dp" else "(dp(6))"
    lines.extend([
        f"ring T=(0,c,b),(t,W,U,X1,X3,X5),{ordering};",
        "option(redSB);",
        "poly q;poly q0;",
        'print("Q8-W0-RANKDROP-WEIGHTED-REES");',
        f'print("engine={engine}");',
        f'print("order={order}");',
    ])
    for m in range(1, 9):
        lines.extend([
            f"map psi{m}=S,t^{m}*W,c,b+1+t*U,b,t*X1,t*X3,t*X5;",
            f"ideal J{m}=psi{m}(SI);",
            f"ideal In{m};",
            f"for(int i{m}=1;i{m}<=size(J{m});i{m}++){{q=J{m}[i{m}];while(subst(q,t,0)==0){{q=q/t;}}q0=subst(q,t,0);In{m}=In{m},q0;}}",
            f"ideal LeadLoad{m}=W*X5*(X3-2*X5);",
            f"list LW{m}=sat(In{m},LeadLoad{m});ideal CW{m}=LW{m}[1];",
            f"ideal GW{m}={engine}(CW{m});",
            f"int W{m}empty=0;if(reduce(1,GW{m})==0){{W{m}empty=1;}}",
            f'print("weight_m={m} loaded_initial_empty="+string(W{m}empty));',
            f'print("WEIGHT_{m}_BASIS_BEGIN");GW{m};print("WEIGHT_{m}_BASIS_END");',
        ])
        if m == 2:
            lines.extend([
                "poly E2q=J2[5];while(subst(E2q,t,0)==0){E2q=E2q/t;}",
                "poly E2in=subst(E2q,t,0);",
                "ideal Ker2=U,X1,X3-X5;",
                f"ideal GKer2={engine}(Ker2);",
                "int generic_slope2_e2_identity=0;if(reduce(E2in-2/9*W,GKer2)==0){generic_slope2_e2_identity=1;}",
                'print("generic_slope2_e2_identity="+string(generic_slope2_e2_identity));',
                'print("generic_slope2_e2_normal_form="+string(reduce(E2in,GKer2)));',
            ])
    lines.extend(['print("Q8_W0_RANKDROP_WEIGHTED_REES_PASS");', "exit;"])
    return "\n".join(lines)


def weighted_b1(engine: str, order: str) -> str:
    rows, imposed = source_rows()
    lines = ['LIB "elim.lib";']
    source_ring(lines, rows, imposed)
    ordering = "dp" if order == "dp" else "(dp(6))"
    lines.extend([
        f"ring T=(0,c),(t,W,U,X1,X3,X5),{ordering};",
        "option(redSB);",
        "map psi=S,t^2*W,c,2+t*U,1,t*X1,t*X3,t*X5;",
        "ideal J=psi(SI);",
        "ideal In;poly q;poly q0;",
        "for(int i=1;i<=size(J);i++){q=J[i];while(subst(q,t,0)==0){q=q/t;}q0=subst(q,t,0);In=In,q0;}",
        "ideal LeadLoad=W*X5*(X3-2*X5);",
        "list LW=sat(In,LeadLoad);ideal CW=LW[1];",
        f"ideal GW={engine}(CW);",
        "int loaded_initial_empty=0;if(reduce(1,GW)==0){loaded_initial_empty=1;}",
        'print("Q8-W0-RANKDROP-B1-SLOPE2");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("b1_slope2_loaded_initial_empty="+string(loaded_initial_empty));',
        'print("B1_SLOPE2_BASIS_BEGIN");GW;print("B1_SLOPE2_BASIS_END");',
        'print("Q8_W0_RANKDROP_B1_SLOPE2_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("loaded", "weighted", "weighted_b1"), required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    emitter = {"loaded": loaded, "weighted": weighted, "weighted_b1": weighted_b1}[args.mode]
    print(emitter(args.engine, args.order))
