#!/usr/bin/env python3
"""Generate an exact fixed-w finite-field Q8 quotient fibre."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
PARENT_MANIFEST = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256"
PARENT_MANIFEST_SHA256 = "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4"
GENERIC_GENERATOR = ROOT / "cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py"
GENERIC_GENERATOR_SHA256 = "6b752b03d777c73de5d9ff729f30d01f5d81229d0ee467e9ad98a349d6234daf"


def load_compiler():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (PARENT_MANIFEST, PARENT_MANIFEST_SHA256),
        (GENERIC_GENERATOR, GENERIC_GENERATOR_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_fixed_fibre_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def specialize(value, w_value: int):
    out = {}
    for monomial, coefficient in value.items():
        key = monomial[1:]
        out[key] = out.get(key, Fraction(0)) + coefficient * (w_value ** monomial[0])
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def source(prime: int, w_value: int, engine: str) -> str:
    if prime <= 3 or w_value % prime == 0:
        raise RuntimeError("prime must exceed 3 and w must be nonzero")
    Q = load_compiler()
    ring, rows, imposed, names = Q.compile_quotient("approx")
    names_without_w = names[1:]
    internal = names_without_w + ["inv"]
    lines = [
        f"ring R={prime},({','.join(internal + ['v'])}),(dp(7),dp(1));",
        "option(redSB);",
    ]
    for ell in imposed:
        fixed = specialize(rows[ell], w_value % prime)
        lines.append(f"poly e{ell}={Q.M.coeff_string(fixed, names_without_w)};")
    lines.extend([
        "poly einv=inv*x5*(x3-2*x5)-1;",
        "poly ev=v*x5-x3+2*x5;",
        "ideal I=e1,e3,e5,e7,e2,e4,einv,ev;",
        f"ideal G={engine}(I);",
        'print("Q8-FIXED-W-FIBRE");',
        f'print("prime={prime}");',
        f'print("w_value={w_value % prime}");',
        'print("fibre_dim="+string(dim(G)));',
        'print("fibre_size="+string(size(G)));',
        'print("fibre_vdim="+string(vdim(G)));',
        "ideal E=eliminate(G,c*d2*d4*x1*x3*x5*inv);",
        "E=std(E);",
        'print("v_elimination_size="+string(size(E)));',
        "if (size(E)==1)",
        "{",
        "  poly H=E[1]/leadcoef(E[1]);",
        '  print("v_eliminant_degree="+string(deg(H)));',
        "  poly Hsquarefree=gcd(H,diff(H,v));",
        '  print("v_eliminant_squarefree_gcd_degree="+string(deg(Hsquarefree)));',
        "  list RF=factorize(H,1);",
        '  print("rational_factor_entries="+string(size(RF[1])));',
        "  RF;",
        "}",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--w-value", type=int, required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    args = parser.parse_args()
    print(source(args.prime, args.w_value, args.engine))


if __name__ == "__main__":
    main()

