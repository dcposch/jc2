#!/usr/bin/env python3
"""Diagnostic-free correction of the frozen cylinder certificate generator."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate.py"
BASE_SHA256 = "d9577a096b2817929656028787698bc7a7c9e0706ea1a10ccecc0a956289c2bd"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_x5_cylinder_frozen_v1", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def corrected(engine: str, order: str) -> str:
    source = load_base().source(engine, order)
    source = source.replace(
        "poly det5_expected=1024*x3^6/1594323;",
        "poly det5_expected=(1024/1594323)*x3^6;",
    )
    old = (
        "matrix ky[6][1];\n"
        "ky[1,1]=-ib^2;ky[2,1]=0;ky[3,1]=0;ky[4,1]=1;ky[5,1]=1;ky[6,1]=0;\n"
        "matrix kyimage=Jy*ky;\n"
        "int kyzero=1;for(int s=1;s<=6;s++){if(reduce(kyimage[s,1],GE)!=0){kyzero=0;}}"
    )
    new = (
        "int kyzero=1;\n"
        "for(int kk=1;kk<=6;kk++){\n"
        "  poly kyentry=-ib^2*Jy[kk,1]+Jy[kk,4]+Jy[kk,5];\n"
        "  if(reduce(kyentry,GE)!=0){kyzero=0;}\n"
        "}"
    )
    if old not in source:
        raise RuntimeError("kernel source block not found")
    return source.replace(old, new)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(corrected(args.engine, args.order))
