#!/usr/bin/env python3
"""Generate the p=127 generic quotient using DRL-to-block FGLM."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
GENERIC = ROOT / "cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py"
GENERIC_SHA256 = "6b752b03d777c73de5d9ff729f30d01f5d81229d0ee467e9ad98a349d6234daf"


def load_generic():
    assert sha256(GENERIC.read_bytes()).hexdigest() == GENERIC_SHA256
    spec = importlib.util.spec_from_file_location("q8_stdfglm_generic", GENERIC)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    generic = load_generic()
    source = generic.source(127, "std", False)
    old = "ideal G=std(I);"
    new = 'LIB "standard.lib";\nideal G=stdfglm(I,"std");'
    assert source.count(old) == 1
    print(source.replace(old, new))


if __name__ == "__main__":
    main()

