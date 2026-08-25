#!/usr/bin/env python3
"""Generate the pure-Singular rational-point and relative-Jacobian replay."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
FIXED = ROOT / "cases/max12_912_order3_nu_q8_fibre_specialization_aws_20260825/generate.py"
FIXED_SHA256 = "4af6f7eca198bcdf1e60151449e08099853669bd1d6965db3cddffa666032d2c"


def load_fixed():
    assert sha256(FIXED.read_bytes()).hexdigest() == FIXED_SHA256
    spec = importlib.util.spec_from_file_location("q8_etale_fixed_generator", FIXED)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    fixed = load_fixed()
    base = fixed.source(127, 71, "std")
    marker = "ideal G=std(I);"
    assert base.count(marker) == 1
    prefix = base.split(marker, 1)[0]
    print(prefix, end="")
    print("ideal P=I,v-50;")
    print("ideal GP=std(P);")
    print('print(\"Q8-P127-W71-V50-ETALE\");')
    print('print(\"point_dim=\"+string(dim(GP)));')
    print('print(\"point_vdim=\"+string(vdim(GP)));')
    print('print(\"point_basis_begin\");')
    print("GP;")
    print('print(\"point_basis_end\");')
    print("matrix J=jacob(I);")
    print("poly detJ=det(J);")
    print("poly detJatP=reduce(detJ,GP);")
    print('print(\"relative_jacobian_determinant_at_point=\"+string(detJatP));')
    print("ideal original_remainders=reduce(I,GP);")
    print('print(\"original_remainders_begin\");')
    print("original_remainders;")
    print('print(\"original_remainders_end\");')


if __name__ == "__main__":
    main()

