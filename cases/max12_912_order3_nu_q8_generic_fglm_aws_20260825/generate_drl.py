#!/usr/bin/env python3
"""Generate the exact generic p=127 quotient in pure DRL."""

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
    spec = importlib.util.spec_from_file_location("q8_drl_generic", GENERIC)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    generic = load_generic()
    source = generic.source(127, "std", False)
    old_ring = "ring R=(127,w),(c,d2,d4,x1,x3,x5,inv,v),(dp(7),dp(1));"
    new_ring = "ring R=(127,w),(c,d2,d4,x1,x3,x5,inv,v),dp;"
    assert source.count(old_ring) == 1
    source = source.replace(old_ring, new_ring)
    marker = "ideal G=std(I);"
    assert source.count(marker) == 1
    prefix = source.split(marker, 1)[0]
    print(prefix, end="")
    print("ideal G=std(I);")
    print('print(\"Q8-GENERIC-P127-DRL\");')
    print('print(\"generic_dim=\"+string(dim(G)));')
    print('print(\"generic_size=\"+string(size(G)));')
    print('print(\"generic_vdim=\"+string(vdim(G)));')
    print('print(\"leading_ideal_begin\");')
    print("lead(G);")
    print('print(\"leading_ideal_end\");')


if __name__ == "__main__":
    main()

