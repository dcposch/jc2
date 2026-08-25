#!/usr/bin/env python3
"""Diagnostic-free repair of the frozen V1 tangent generator."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate.py"
BASE_SHA256 = "3624d3ee17a85176b45a592434c34c0a16a89cb294897de2d1e4d13fd2c15bf7"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_overlap_tangent_frozen_v1", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def corrected(engine: str, order: str) -> str:
    text = load_base().source(engine, order)
    replacements = {
        f"ideal GL24={engine}(L2,L4);": f"ideal IL24=L2,L4;\nideal GL24={engine}(IL24);",
        f"ideal GF24={engine}(F2,F4);": f"ideal IF24=F2,F4;\nideal GF24={engine}(IF24);",
        f"ideal GT={engine}(d2-2*d4,d4*(d4-2));": f"ideal IT=d2-2*d4,d4*(d4-2);\nideal GT={engine}(IT);",
        f"ideal J0={engine}(L1,L3,L5,d2,d4);": f"ideal IJ0=L1,L3,L5,d2,d4;\nideal J0={engine}(IJ0);",
        f"ideal T0={engine}(d2,d4,tx1,tx3,tx5);": f"ideal IT0=d2,d4,tx1,tx3,tx5;\nideal T0={engine}(IT0);",
        f"ideal J42={engine}(L1,L3,L5,d2-4,d4-2);": f"ideal IJ42=L1,L3,L5,d2-4,d4-2;\nideal J42={engine}(IJ42);",
        f"ideal T42={engine}(d2-4,d4-2,tx1-8*c-8/3,tx3-20*c-88/9,tx5-12*c-16/3);": (
            "ideal IT42=d2-4,d4-2,tx1-8*c-8/3,tx3-20*c-88/9,tx5-12*c-16/3;\n"
            f"ideal T42={engine}(IT42);"
        ),
        "for(int i=1;i<=size(GL24);i++){if(reduce(GL24[i],GF24)!=0){l_to_f=0;}}": (
            "for(int ilf=1;ilf<=size(GL24);ilf++){if(reduce(GL24[ilf],GF24)!=0){l_to_f=0;}}"
        ),
        "for(int i=1;i<=size(GF24);i++){if(reduce(GF24[i],GL24)!=0){f_to_l=0;}}": (
            "for(int ifl=1;ifl<=size(GF24);ifl++){if(reduce(GF24[ifl],GL24)!=0){f_to_l=0;}}"
        ),
        "for(int i=1;i<=size(GF24);i++){if(reduce(GF24[i],GT)!=0){f_to_t=0;}}": (
            "for(int ift=1;ift<=size(GF24);ift++){if(reduce(GF24[ift],GT)!=0){f_to_t=0;}}"
        ),
        "for(int i=1;i<=size(GT);i++){if(reduce(GT[i],GF24)!=0){t_to_f=0;}}": (
            "for(int itf=1;itf<=size(GT);itf++){if(reduce(GT[itf],GF24)!=0){t_to_f=0;}}"
        ),
        "for(int i=1;i<=size(J0);i++){if(reduce(J0[i],T0)!=0){j0_to_t0=0;}}": (
            "for(int ij0=1;ij0<=size(J0);ij0++){if(reduce(J0[ij0],T0)!=0){j0_to_t0=0;}}"
        ),
        "for(int i=1;i<=size(T0);i++){if(reduce(T0[i],J0)!=0){t0_to_j0=0;}}": (
            "for(int it0=1;it0<=size(T0);it0++){if(reduce(T0[it0],J0)!=0){t0_to_j0=0;}}"
        ),
        "for(int i=1;i<=size(J42);i++){if(reduce(J42[i],T42)!=0){j42_to_t42=0;}}": (
            "for(int ij42=1;ij42<=size(J42);ij42++){if(reduce(J42[ij42],T42)!=0){j42_to_t42=0;}}"
        ),
        "for(int i=1;i<=size(T42);i++){if(reduce(T42[i],J42)!=0){t42_to_j42=0;}}": (
            "for(int it42=1;it42<=size(T42);it42++){if(reduce(T42[it42],J42)!=0){t42_to_j42=0;}}"
        ),
    }
    for old, new in replacements.items():
        if text.count(old) != 1:
            raise RuntimeError((old, text.count(old)))
        text = text.replace(old, new)
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(corrected(args.engine, args.order))
