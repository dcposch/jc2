#!/usr/bin/env python3
"""Emit exact pointed moving-d4 localizer problems."""

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
    spec = importlib.util.spec_from_file_location("q8_rankdrop_b1_pointed_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(field: str, engine: str) -> str:
    q = load_compiler()
    _, rows, imposed, names = q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    lines = ["ring S=0,(w,c,d2,d4,x1,x3,x5),dp;"]
    for ell in range(1, 9):
        lines.append(f"poly se{ell}={q.M.coeff_string(rows[ell], names)};")
    lines.append("ideal SI=se1,se3,se5,se7,se2,se4;")
    if field == "QQc":
        lines.append("ring R=(0,c),(inv,v,w,u,x1,x3,x5),(dp(1),dp(6));")
    else:
        lines.append("ring R=0,(inv,c,v,w,u,x1,x3,x5),(dp(1),dp(7));")
    lines.extend([
        "option(redSB);",
        "map phi=S,w,c,2+v+u,1+v,x1,x3,x5;",
        "ideal I=phi(SI);poly A=x3-2*x5;",
        "ideal J=I,inv*w*x5*A-1;",
        f"ideal GJ={engine}(J);",
        "ideal C=eliminate(GJ,inv);",
        f"ideal GC={engine}(C);",
        "ideal Landing=GC,v,w,u,x1,x3,x5;",
        f"ideal GL={engine}(Landing);",
        "int selected_empty=0;if(reduce(1,GJ)==0){selected_empty=1;}",
        "int landing_empty=0;if(reduce(1,GL)==0){landing_empty=1;}",
        'print("Q8-W0-RANKDROP-B1-POINTED-DRIFT");',
        f'print("field={field}");',
        f'print("engine={engine}");',
        'print("selected_empty="+string(selected_empty));',
        'print("landing_empty="+string(landing_empty));',
        'print("J_BASIS_BEGIN");GJ;print("J_BASIS_END");',
        'print("CONTRACTION_BASIS_BEGIN");GC;print("CONTRACTION_BASIS_END");',
        'print("LANDING_BASIS_BEGIN");GL;print("LANDING_BASIS_END");',
        'print("Q8_W0_RANKDROP_B1_POINTED_DRIFT_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--field", choices=("QQc", "Qc"), required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    args = parser.parse_args()
    print(source(args.field, args.engine))
