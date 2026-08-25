#!/usr/bin/env python3
"""Independent localizer/elimination implementation of the b=1 saturation."""

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
    spec = importlib.util.spec_from_file_location("q8_rankdrop_b1_elim_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(engine: str) -> str:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    lines = ["ring S=0,(w,c,d2,d4,x1,x3,x5),dp;"]
    for ell in range(1, 9):
        lines.append(f"poly se{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "ideal SI=" + ",".join(f"se{i}" for i in imposed) + ";",
        "ring R=(0,c),(inv,w,u,x1,x3,x5),(dp(1),dp(5));",
        "option(redSB);",
        "map phi=S,w,c,2+u,1,x1,x3,x5;",
        "ideal I=phi(SI);poly A=x3-2*x5;",
        "ideal J=I,inv*w*x5*A-1;",
        f"ideal GJ={engine}(J);",
        "ideal C=eliminate(GJ,inv);",
        f"ideal GC={engine}(C);",
        "ideal Landing=GC,w,u,x1,x3,x5;",
        f"ideal GL={engine}(Landing);",
        "int landing_empty=0;if(reduce(1,GL)==0){landing_empty=1;}",
        'print("Q8-W0-RANKDROP-B1-LOCALIZER-ELIMINATION");',
        f'print("engine={engine}");',
        'print("order=inv-elimination-block");',
        'print("landing_empty="+string(landing_empty));',
        'print("LANDING_BASIS_BEGIN");GL;print("LANDING_BASIS_END");',
        'print("CONTRACTION_BASIS_BEGIN");GC;print("CONTRACTION_BASIS_END");',
        'print("Q8_W0_RANKDROP_B1_LOCALIZER_ELIMINATION_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    args = parser.parse_args()
    print(source(args.engine))

