#!/usr/bin/env python3
"""Final tangent generator: fixes the ambient-ring vdim display only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate_v2.py"
BASE_SHA256 = "9edab6362281613bd0246be47a6156e413e6b197fbc14f62bb0cd29f87a1b915"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_overlap_tangent_frozen_v2", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def corrected(engine: str, order: str) -> str:
    text = load_base().corrected(engine, order)
    old = 'print("F24_vdim="+string(vdim(GF24)));'
    new = 'print("F24_two_point_scheme="+string(f_to_t*t_to_f));'
    if text.count(old) != 1:
        raise RuntimeError((old, text.count(old)))
    return text.replace(old, new)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(corrected(args.engine, args.order))
