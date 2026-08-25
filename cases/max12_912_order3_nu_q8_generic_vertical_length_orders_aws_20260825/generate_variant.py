#!/usr/bin/env python3
"""Hash-pinned term-order/algorithm adapter for the generic vertical ideal."""

from __future__ import annotations

import argparse
from hashlib import sha256
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/max12_912_order3_nu_q8_generic_vertical_length_aws_20260825/generate.py"
BASE_SHA256 = "e688fffc13e74441962226a055d6ebeb513f80ba46b13eea45e187736a0d17ac"
CHOICES_OLD = 'choices=("dp", "lp")'
CHOICES_NEW = 'choices=("dp", "lp", "Dp")'
RING_OLD = 'print(f"ring R=(127,w),(u,c,d2,d4,x1,x5,v),{args.order};")'
STD_OLD = 'print("ideal G=std(I);")'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", choices=("dp", "lp", "Dp"), required=True)
    parser.add_argument("--algorithm", choices=("std", "slimgb"), required=True)
    parser.add_argument("--variables", choices=("original", "vfirst", "ulast"), required=True)
    args = parser.parse_args()
    raw = BASE.read_bytes()
    if sha256(raw).hexdigest() != BASE_SHA256:
        raise RuntimeError("base generator hash")
    source = raw.decode("utf-8")
    if source.count(CHOICES_OLD) != 1 or source.count(RING_OLD) != 1 or source.count(STD_OLD) != 1:
        raise RuntimeError("adapter anchor")
    source = source.replace(CHOICES_OLD, CHOICES_NEW)
    variables = {
        "original": "u,c,d2,d4,x1,x5,v",
        "vfirst": "v,u,c,d2,d4,x1,x5",
        "ulast": "c,d2,d4,x1,x5,v,u",
    }[args.variables]
    source = source.replace(
        RING_OLD,
        f'print(f"ring R=(127,w),({variables}),{{args.order}};")',
    )
    if args.algorithm == "slimgb":
        source = source.replace(STD_OLD, 'print("ideal G=slimgb(I);")')
    source = source.replace(
        'print(f\'print("term_order={args.order}");\')',
        'print(f\'print("term_order={args.order}");\')\n'
        f'    print(\'print("algorithm={args.algorithm}");\')\n'
        f'    print(\'print("variable_order={args.variables}");\')',
    )
    sys.argv = [str(BASE), "--order", args.order]
    namespace = {"__name__": "__main__", "__file__": str(BASE), "__package__": None}
    exec(compile(source, str(BASE), "exec"), namespace)


if __name__ == "__main__":
    main()
