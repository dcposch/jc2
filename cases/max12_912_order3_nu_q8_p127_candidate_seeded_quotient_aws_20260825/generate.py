#!/usr/bin/env python3
"""Generate exact candidate-seeded selected-Q8 inputs over F_127(w)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
GENERIC = ROOT / "cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py"
GENERIC_SHA256 = "6b752b03d777c73de5d9ff729f30d01f5d81229d0ee467e9ad98a349d6234daf"
CANDIDATE = ROOT / (
    "cases/max12_912_order3_nu_q8_p127_eliminant_interpolation_aws_20260825/"
    "aws/p127-eliminant-interpolation-root-v6/result.json"
)
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"

PERMUTATIONS = {
    "canonical": ["c", "d2", "d4", "x1", "x3", "x5", "inv", "v"],
    "reverse": ["x5", "x3", "x1", "d4", "d2", "c", "inv", "v"],
    "inv-first": ["inv", "x5", "x3", "x1", "d4", "d2", "c", "v"],
    "interleave": ["inv", "c", "x5", "d2", "x3", "d4", "x1", "v"],
}


def load_generic():
    for path, expected in (
        (GENERIC, GENERIC_SHA256),
        (CANDIDATE, CANDIDATE_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_seeded_generic", GENERIC)
    if spec is None or spec.loader is None:
        raise RuntimeError(GENERIC)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def monomial(coefficient: int, w_degree: int, v_degree: int) -> str:
    factors = []
    if coefficient != 1 or (w_degree == 0 and v_degree == 0):
        factors.append(str(coefficient))
    if w_degree:
        factors.append("w" if w_degree == 1 else f"w^{w_degree}")
    if v_degree:
        factors.append("v" if v_degree == 1 else f"v^{v_degree}")
    return "*".join(factors) if factors else "1"


def candidate_polynomial() -> str:
    payload = json.loads(CANDIDATE.read_text())
    assert payload["status"] == "PASS"
    assert payload["prime"] == 127
    assert payload["degree_v"] == 190
    assert payload["full_degree_fibre_count"] == 123
    assert payload["degree_drop_values"] == [39, 56, 125]
    assert payload["coefficient_table_sha256"] == (
        "bb61aff1688f3cdf347042db4146f133163fe609a3ef108d4e156219e62e6f5d"
    )
    support = payload["nonzero_support"]
    terms = []
    maximum_w_degree = 0
    for v_degree in range(191):
        for w_degree, coefficient in support[str(v_degree)]:
            assert 0 <= coefficient < 127
            maximum_w_degree = max(maximum_w_degree, w_degree)
            terms.append(monomial(coefficient, w_degree, v_degree))
    assert support["190"] == [[0, 1]]
    assert maximum_w_degree == 21
    return "+".join(terms)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), required=True)
    parser.add_argument("--order", choices=("dp", "lp", "block"), required=True)
    parser.add_argument("--permutation", choices=tuple(PERMUTATIONS), required=True)
    parser.add_argument("--placement", choices=("first", "last"), required=True)
    args = parser.parse_args()

    generic = load_generic()
    compiler = generic.load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    variables = PERMUTATIONS[args.permutation]
    assert set(variables) == {"c", "d2", "d4", "x1", "x3", "x5", "inv", "v"}
    assert variables[-1] == "v"
    ordering = "(dp(7),dp(1))" if args.order == "block" else args.order

    lines = [
        f"ring R=(127,w),({','.join(variables)}),{ordering};",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(f"poly e{ell}={compiler.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "poly einv=inv*x5*(x3-2*x5)-1;",
        "poly ev=v*x5-x3+2*x5;",
        f"poly H={candidate_polynomial()};",
        'print("Q8-P127-CANDIDATE-SEEDED-QUOTIENT");',
        f'print("engine={args.engine}");',
        f'print("order={args.order}");',
        f'print("permutation={args.permutation}");',
        f'print("placement={args.placement}");',
        'print("candidate_v_degree="+string(deg(H)));',
        'print("candidate_leadcoef="+string(leadcoef(H)));',
    ])
    generators = ["e1", "e3", "e5", "e7", "e2", "e4", "einv", "ev"]
    if args.placement == "first":
        generators.insert(0, "H")
    else:
        generators.append("H")
    lines.extend([
        f"ideal J={','.join(generators)};",
        f"ideal G={args.engine}(J);",
        'print("seeded_dim="+string(dim(G)));',
        'print("seeded_size="+string(size(G)));',
        'print("seeded_vdim="+string(vdim(G)));',
    ])
    print("\n".join(lines))


if __name__ == "__main__":
    main()

