#!/usr/bin/env python3
"""Emit a pinned good-prime routing version of the fused saturation source."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate_fused.py"
BASE_SHA256 = "217586ca9c0f8d2f069899240eb172d57394e71f68b5d021b149abfce92235b8"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_horizontal_fused_frozen", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(prime: int, kind: str, engine: str, order: str) -> str:
    if prime not in (127, 32003):
        raise RuntimeError(prime)
    text = load_base().fused_source(kind, engine, order)
    old = "ring R=0,("
    new = f"ring R={prime},("
    if text.count(old) != 1:
        raise RuntimeError((old, text.count(old)))
    text = text.replace(old, new)
    return text.replace(
        'print("Q8-W0-HORIZONTAL-CLOSURE-FUSED");',
        f'print("Q8-W0-HORIZONTAL-CLOSURE-FUSED-MOD-{prime}");',
    ).replace(
        'print("Q8_W0_HORIZONTAL_CLOSURE_FUSED_PASS");',
        f'print("Q8_W0_HORIZONTAL_CLOSURE_FUSED_MOD_{prime}_PASS");',
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(127, 32003), required=True)
    parser.add_argument("--kind", choices=("selected", "boundary"), required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.prime, args.kind, args.engine, args.order))
