#!/usr/bin/env python3
"""Generate direct generic candidate-reduction lanes under varied orders."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_GENERATOR = ROOT / (
    "cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/"
    "generate.py"
)
CANDIDATE_GENERATOR_SHA256 = "7436f8df2a8683b20aed49176e3217fd229abb5be96b564c20204b3fc439f584"

PERMUTATIONS = {
    "canonical": ["c", "d2", "d4", "x1", "x3", "x5", "inv", "v"],
    "reverse": ["x5", "x3", "x1", "d4", "d2", "c", "inv", "v"],
    "inv-first": ["inv", "x5", "x3", "x1", "d4", "d2", "c", "v"],
    "interleave": ["inv", "c", "x5", "d2", "x3", "d4", "x1", "v"],
}


def load_candidate():
    got = sha256(CANDIDATE_GENERATOR.read_bytes()).hexdigest()
    if got != CANDIDATE_GENERATOR_SHA256:
        raise RuntimeError((str(CANDIDATE_GENERATOR), got, CANDIDATE_GENERATOR_SHA256))
    spec = importlib.util.spec_from_file_location("q8_candidate_order_race", CANDIDATE_GENERATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(CANDIDATE_GENERATOR)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), required=True)
    parser.add_argument("--order", choices=("dp", "lp", "block"), required=True)
    parser.add_argument("--permutation", choices=tuple(PERMUTATIONS), required=True)
    args = parser.parse_args()

    candidate = load_candidate()
    generic = candidate.load_generic()
    compiler = generic.load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    variables = PERMUTATIONS[args.permutation]
    ordering = "(dp(7),dp(1))" if args.order == "block" else args.order
    lines = [
        f"ring R=(127,w),({','.join(variables)}),{ordering};",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(f"poly e{ell}={compiler.M.coeff_string(rows[ell], names)};")
    lines.extend(
        [
            "poly einv=inv*x5*(x3-2*x5)-1;",
            "poly ev=v*x5-x3+2*x5;",
            "ideal I=e1,e3,e5,e7,e2,e4,einv,ev;",
            f"ideal G={args.engine}(I);",
            'print("Q8-P127-GENERIC-CANDIDATE-ORDER-RACE");',
            f'print("engine={args.engine}");',
            f'print("order={args.order}");',
            f'print("permutation={args.permutation}");',
            'print("generic_dim="+string(dim(G)));',
            'print("generic_size="+string(size(G)));',
            'print("generic_vdim="+string(vdim(G)));',
            f"poly H={candidate.candidate_source()};",
            'print("candidate_v_degree="+string(deg(H)));',
            'print("candidate_leadcoef="+string(leadcoef(H)));',
            "poly candidate_remainder=reduce(H,G);",
            'print("candidate_remainder="+string(candidate_remainder));',
        ]
    )
    print("\n".join(lines))


if __name__ == "__main__":
    main()

