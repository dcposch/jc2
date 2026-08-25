#!/usr/bin/env python3
"""Generate the selected-Q8 generic-fibre primitive-element input."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
PARENT_MANIFEST = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256"
PARENT_MANIFEST_SHA256 = "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4"
PRIMITIVITY_FREEZE = ROOT / "cases/max12_912_order3_nu_q8_galois_primitivity_aws_20260825/FREEZE.txt"
PRIMITIVITY_FREEZE_SHA256 = "f25fa86f14d4b77585b127e952b15cfb57de2f08c810931b4fb7ed5f08dd8e85"


def load_compiler():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (PARENT_MANIFEST, PARENT_MANIFEST_SHA256),
        (PRIMITIVITY_FREEZE, PRIMITIVITY_FREEZE_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_generic_fibre_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(characteristic: int, engine: str, absolute: bool) -> str:
    if absolute and characteristic != 0:
        raise RuntimeError("absolute factorization is characteristic-zero only")
    Q = load_compiler()
    ring, rows, imposed, names = Q.compile_quotient("approx")
    internal = ["c", "d2", "d4", "x1", "x3", "x5", "inv"]
    coeff = f"({characteristic},w)"
    lines = [
        'LIB "primdec.lib";',
        f"ring R={coeff},({','.join(internal + ['v'])}),(dp(7),dp(1));",
        "option(redSB);",
    ]
    if absolute:
        lines.append('LIB "absfact.lib";')
    for ell in imposed:
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "poly einv=inv*x5*(x3-2*x5)-1;",
        "poly ev=v*x5-x3+2*x5;",
        "ideal I=e1,e3,e5,e7,e2,e4,einv,ev;",
        f"ideal G={engine}(I);",
        'print("Q8-GENERIC-FIBRE-GROUPING");',
        f'print("characteristic={characteristic}");',
        'print("generic_dim="+string(dim(G)));',
        'print("generic_size="+string(size(G)));',
        'print("generic_vdim="+string(vdim(G)));',
        "ideal E=eliminate(G,c*d2*d4*x1*x3*x5*inv);",
        "E=std(E);",
        'print("v_elimination_size="+string(size(E)));',
        "E;",
        "if (size(E)==1)",
        "{",
        "  poly H=E[1]/leadcoef(E[1]);",
        '  print("v_eliminant_degree="+string(deg(H)));',
        "  poly Hv=diff(H,v);",
        "  poly Hsquarefree=gcd(H,Hv);",
        '  print("v_eliminant_squarefree_gcd_degree="+string(deg(Hsquarefree)));',
        "  list RF=factorize(H,1);",
        '  print("rational_factor_entries="+string(size(RF[1])));',
        "  RF;",
    ])
    if absolute:
        lines.extend([
            '  print("absolute_factorization_begin");',
            '  def AF=absFactorize(H,"alpha");',
            "  setring AF;",
            '  print("absolute_factor_entries="+string(size(absolute_factors[1])));',
            '  print("absolute_nontrivial_factor_total="+string(absolute_factors[4]));',
            "  absolute_factors;",
        ])
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--characteristic", type=int, default=0)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    parser.add_argument("--absolute", action="store_true")
    args = parser.parse_args()
    print(source(args.characteristic, args.engine, args.absolute))


if __name__ == "__main__":
    main()

