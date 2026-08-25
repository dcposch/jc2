#!/usr/bin/env python3
"""Accepted V3: compare the leading chart on the preregistered D(z) open."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate_v2.py"
BASE_SHA256 = "acb68c7c1f9ab5d36e396504bb3cf265f96a2b098db419ab78c93cd9eeccfcaf"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_slope3_v2", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(engine: str, order: str) -> str:
    text = load_base().source(engine, order)
    text = 'LIB "elim.lib";\n' + text
    old = f"ideal GLead={engine}(Lead);"
    new = f"list LLead=sat(Lead,ideal(z));ideal LeadOpen=LLead[1];ideal GLead={engine}(LeadOpen);"
    if text.count(old) != 1:
        raise RuntimeError((old, text.count(old)))
    return text.replace(old, new)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.engine, args.order))

