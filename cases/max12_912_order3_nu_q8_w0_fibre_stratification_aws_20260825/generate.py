#!/usr/bin/env python3
"""Generate exact Singular sources for the localized six-row w=0 fibre."""

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

Q8_ASCENDING = [
    24,
    296,
    1548,
    4428,
    7320,
    6498,
    1782,
    -1539,
    -999,
]

MODES = (
    "base",
    "nu0",
    "loaded",
    "q8",
    "q8_smooth",
    "q8_singular",
    "nonq8",
    "nonq8_smooth",
    "nonq8_singular",
    "nonq8_rho0",
    "nonq8_rho_loaded",
)


def load_compiler():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (PARENT_MANIFEST, PARENT_MANIFEST_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_w0_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def specialize_w0(value):
    out = {}
    for monomial, coefficient in value.items():
        if monomial[0] != 0:
            continue
        key = monomial[1:]
        out[key] = out.get(key, Fraction(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def q8_string() -> str:
    terms = []
    for degree, coefficient in enumerate(Q8_ASCENDING):
        if not coefficient:
            continue
        monomial = "1" if degree == 0 else ("v" if degree == 1 else f"v^{degree}")
        terms.append(f"({coefficient})*({monomial})")
    return "+".join(terms)


def source(prime: int, mode: str, engine: str, order: str, print_basis: bool) -> str:
    if prime != 0 and prime <= 3:
        raise RuntimeError("characteristic must be zero or a prime greater than three")
    if mode not in MODES:
        raise RuntimeError(mode)
    Q = load_compiler()
    _ring, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(("imposed-row mismatch", imposed))
    names_w0 = names[1:]
    base_variables = names_w0 + ["inv", "v"]
    extra_variables = []
    if mode not in ("base", "nu0"):
        extra_variables.append("inu")
    if mode.startswith("nonq8"):
        extra_variables.append("iq")
    if mode.endswith("_smooth"):
        extra_variables.append("idet")
    if mode == "nonq8_rho_loaded":
        extra_variables.append("irho")
    # Keep v last so the block order and elimination target are literal.
    variables = names_w0 + ["inv"] + extra_variables + ["v"]
    if order == "dp":
        ordering = "dp"
    else:
        ordering = f"(dp({len(variables)-1}),dp(1))"

    lines = [
        'LIB "primdec.lib";',
        f"ring R={prime},({','.join(variables)}),{ordering};",
        "option(redSB);",
    ]
    row_names = []
    for ell in imposed:
        fixed = specialize_w0(rows[ell])
        name = f"e{ell}"
        row_names.append(name)
        lines.append(f"poly {name}={Q.M.coeff_string(fixed, names_w0)};")
    r6 = specialize_w0(rows[6])
    r8 = specialize_w0(rows[8])
    lines.extend(
        [
            f"poly e6={Q.M.coeff_string(r6, names_w0)};",
            f"poly e8={Q.M.coeff_string(r8, names_w0)};",
            "poly ev=v*x5-x3+2*x5;",
            "poly einv=inv*x5*(x3-2*x5)-1;",
            f"poly eq8={q8_string()};",
            f"ideal Ibase={','.join(row_names + ['ev', 'einv'])};",
            "matrix J[8][8];",
        ]
    )
    jac_rows = row_names + ["ev", "einv"]
    for i, row_name in enumerate(jac_rows, start=1):
        for j, variable in enumerate(base_variables, start=1):
            lines.append(f"J[{i},{j}]=diff({row_name},{variable});")
    lines.append("poly detJ=det(J);")

    generators = jac_rows[:]
    if mode == "nu0":
        generators.append("e6")
    elif mode not in ("base",):
        generators.append("inu*e6-1")
    if mode in ("q8", "q8_smooth", "q8_singular"):
        generators.append("eq8")
    if mode.startswith("nonq8"):
        generators.append("iq*eq8-1")
    if mode.endswith("_smooth"):
        generators.append("idet*detJ-1")
    if mode.endswith("_singular"):
        generators.append("detJ")
    if mode == "nonq8_rho0":
        generators.append("e8")
    if mode == "nonq8_rho_loaded":
        generators.append("irho*e8-1")

    lines.extend(
        [
            f"ideal I={','.join(generators)};",
            f"ideal G={engine}(I);",
            "int remzero=1;",
            "for (int remindex=1; remindex<=size(I); remindex++)",
            "{",
            "  if (reduce(I[remindex],G)!=0){remzero=0;}",
            "}",
            'print("Q8-W0-FIBRE-STRATUM");',
            f'print("prime={prime}");',
            f'print("mode={mode}");',
            f'print("engine={engine}");',
            f'print("order={order}");',
            'print("original_remainder_zero="+string(remzero));',
            'print("dim="+string(dim(G)));',
            'print("size="+string(size(G)));',
            'print("vdim="+string(vdim(G)));',
            "if (dim(G)==0)",
            "{",
            f"  ideal E=eliminate(G,{'*'.join(variables[:-1])});",
            "  E=std(E);",
            '  print("v_elimination_size="+string(size(E)));',
            "  if (size(E)==1)",
            "  {",
            "    poly H=E[1]/leadcoef(E[1]);",
            '    print("v_eliminant_degree="+string(deg(H)));',
            "    poly Hsf=gcd(H,diff(H,v));",
            '    print("v_eliminant_squarefree_gcd_degree="+string(deg(Hsf)));',
            "    poly HQ=gcd(H,eq8);",
            '    print("v_eliminant_q8_gcd_degree="+string(deg(HQ)));',
            "    list RF=factorize(H,1);",
            '    print("rational_factor_entries="+string(size(RF[1])));',
            "    RF;",
            "  }",
            "}",
        ]
    )
    if print_basis:
        lines.extend(['print("REDUCED_BASIS_BEGIN");', "G;", 'print("REDUCED_BASIS_END");'])
    lines.extend(['print("Q8_W0_FIBRE_STRATUM_PASS");', "exit;"])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=0)
    parser.add_argument("--mode", choices=MODES, required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="block")
    parser.add_argument("--print-basis", action="store_true")
    args = parser.parse_args()
    print(source(args.prime, args.mode, args.engine, args.order, args.print_basis))


if __name__ == "__main__":
    main()
