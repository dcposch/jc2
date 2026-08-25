#!/usr/bin/env python3
"""Fail-closed V2: preserve the leading-ring output and fix ideal syntax."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate.py"
BASE_SHA256 = "49e5d96b4f8dd48e53d91fba8129ba9d6af734222437b87f8a13cb418e9cc420"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_slope3_v1", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(engine: str, order: str) -> str:
    text = load_base().source(engine, order)
    ring_c = "ring C=0,(t,c,C1,Q2,U3,B1,B2,X3,W4,A,aux),"
    pos = text.find(ring_c)
    if pos < 0:
        raise RuntimeError("continuation ring marker missing")
    insert = (
        'print("LEADING_CHART_BEGIN");\n'
        'print("leading_ideal_identity="+string(lead_to_expected*expected_to_lead));\n'
        'print("LEADING_BASIS_BEGIN");GLead;print("LEADING_BASIS_END");\n'
        'print("LEADING_CHART_END");\n'
    )
    text = text[:pos] + insert + text[pos:]
    old = f"ideal G12={engine}(P1,P5,A-C1+Q2);"
    new = f"ideal J12=P1,P5,A-C1+Q2;ideal G12={engine}(J12);"
    if text.count(old) != 1:
        raise RuntimeError((old, text.count(old)))
    text = text.replace(old, new)
    for old_line in (
        'print("leading_ideal_identity="+string(lead_to_expected*expected_to_lead));\n',
        'print("LEADING_BASIS_BEGIN");GLead;print("LEADING_BASIS_END");\n',
    ):
        # Remove only the later inherited occurrence, retaining the inserted one.
        last = text.rfind(old_line)
        first = text.find(old_line)
        if last == first:
            raise RuntimeError((old_line, first, last))
        text = text[:last] + text[last + len(old_line):]
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(source(args.engine, args.order))

