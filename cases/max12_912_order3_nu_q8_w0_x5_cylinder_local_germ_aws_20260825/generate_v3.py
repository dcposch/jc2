#!/usr/bin/env python3
"""Fail-closed, diagnostic-free cylinder local-germ certificate generator.

V3 changes no polynomial or mathematical check from V2.  It declares the
temporary kernel-entry polynomial once, outside the Singular loop, so that
Singular emits no ``redefining`` diagnostic.
"""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate_v2.py"
BASE_SHA256 = "b8701038a53486deac7d648cc8c23d9097d543900093ea660d1daf137d1ec638"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_x5_cylinder_frozen_v2", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def corrected(engine: str, order: str) -> str:
    source = load_base().corrected(engine, order)
    old = (
        "int kyzero=1;\n"
        "for(int kk=1;kk<=6;kk++){\n"
        "  poly kyentry=-ib^2*Jy[kk,1]+Jy[kk,4]+Jy[kk,5];\n"
        "  if(reduce(kyentry,GE)!=0){kyzero=0;}\n"
        "}"
    )
    new = (
        "int kyzero=1;\n"
        "poly kyentry;\n"
        "for(int kk=1;kk<=6;kk++){\n"
        "  kyentry=-ib^2*Jy[kk,1]+Jy[kk,4]+Jy[kk,5];\n"
        "  if(reduce(kyentry,GE)!=0){kyzero=0;}\n"
        "}"
    )
    if old not in source:
        raise RuntimeError("V2 kernel source block not found")
    return source.replace(old, new)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(corrected(args.engine, args.order))
