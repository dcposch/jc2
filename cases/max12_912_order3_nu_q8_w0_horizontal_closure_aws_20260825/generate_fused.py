#!/usr/bin/env python3
"""Fuse the four post-saturation strata so each source saturation runs once."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "generate.py"
BASE_SHA256 = "d2f5628b8245d841cb1753eb0b5d26b1798cbf836219228ce1633998404ce9cc"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_horizontal_frozen_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


B = load_base()


def fused_source(kind: str, engine: str, order: str) -> str:
    Q = B.load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    variables = names + ["ib", "inu"]
    ordering = "dp" if order == "dp" else f"(dp({len(names)}),dp(2))"
    lines = [
        'LIB "elim.lib";',
        f"ring R=0,({','.join(variables)}),{ordering};",
        "option(redSB);",
    ]
    for ell in range(1, 9):
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "poly A=x3-2*x5;",
        f"ideal I={','.join(f'e{ell}' for ell in imposed)};",
    ])
    if kind == "selected":
        lines.extend(["list LS=sat(I,ideal(w*x5*A));", "ideal C=LS[1];"])
    elif kind == "boundary":
        lines.extend(["ideal IB=I,x5*A;", "list LS=sat(IB,ideal(w));", "ideal C=LS[1];"])
    else:
        raise RuntimeError(kind)

    branches = {
        "x5": ["C", "w", "x5", "ib*x3-1"],
        "A": ["C", "w", "A", "ib*x5-1"],
        "overlap_loaded": ["C", "w", "x5", "x3", "inu*e6-1"],
        "overlap_unloaded": ["C", "w", "x5", "x3", "e6"],
    }
    lines.extend([
        'print("Q8-W0-HORIZONTAL-CLOSURE-FUSED");',
        f'print("kind={kind}");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("source_dim="+string(dim(I)));',
        'print("saturated_dim="+string(dim(C)));',
    ])
    for idx, (stratum, generators) in enumerate(branches.items(), start=1):
        lines.extend([
            f"ideal B{idx}={','.join(generators)};",
            f"ideal G{idx}={engine}(B{idx});",
            f"int sr{idx}=1;for(int j{idx}=1;j{idx}<=size(I);j{idx}++){{if(reduce(I[j{idx}],G{idx})!=0){{sr{idx}=0;}}}}",
            f"int br{idx}=1;for(int k{idx}=1;k{idx}<=size(B{idx});k{idx}++){{if(reduce(B{idx}[k{idx}],G{idx})!=0){{br{idx}=0;}}}}",
            f"int ui{idx}=0;if(reduce(1,G{idx})==0){{ui{idx}=1;}}",
            f'print("STRATUM_BEGIN={stratum}");',
            f'print("branch_dim="+string(dim(G{idx})));',
            f'print("branch_vdim="+string(vdim(G{idx})));',
            f'print("branch_size="+string(size(G{idx})));',
            f'print("unit_ideal="+string(ui{idx}));',
            f'print("source_remainder_zero="+string(sr{idx}));',
            f'print("branch_remainder_zero="+string(br{idx}));',
            f'print("e6_normal_form="+string(reduce(e6,G{idx})));',
            f'print("e8_normal_form="+string(reduce(e8,G{idx})));',
            'print("BASIS_BEGIN");',
            f"G{idx};",
            'print("BASIS_END");',
            f'print("STRATUM_END={stratum}");',
        ])
    lines.extend(['print("Q8_W0_HORIZONTAL_CLOSURE_FUSED_PASS");', "exit;"])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=B.KINDS, required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(fused_source(args.kind, args.engine, args.order))


if __name__ == "__main__":
    main()
