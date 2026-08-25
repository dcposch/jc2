#!/usr/bin/env python3
"""Pinned wrapper for the exact fixed-w Q8 msolve input generator."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_nu_q8_fibre_msolve_aws_20260825/generate.py"
PARENT_SHA256 = "ac9ed3f6e3f093631ddec4ba0a9649ef06791ff986cfaf1525cb8f483f0af466"


def load_parent():
    got = sha256(PARENT.read_bytes()).hexdigest()
    if got != PARENT_SHA256:
        raise RuntimeError((str(PARENT), got, PARENT_SHA256))
    spec = importlib.util.spec_from_file_location("q8_box02_control_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(PARENT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--w-value", type=int, required=True)
    args = parser.parse_args()
    parent = load_parent()
    print(parent.source(args.prime, args.w_value))


if __name__ == "__main__":
    main()

