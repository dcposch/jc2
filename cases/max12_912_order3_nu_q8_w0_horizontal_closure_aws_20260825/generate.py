#!/usr/bin/env python3
"""Generate exact Singular inputs for source-horizontal Q8 boundary splits."""

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
ORDER3 = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
ORDER3_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"
PARENT_MANIFEST = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/MANIFEST.sha256"
PARENT_MANIFEST_SHA256 = "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4"

KINDS = ("selected", "boundary")
STRATA = ("x5", "A", "overlap_loaded", "overlap_unloaded")


def load_compiler():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (ORDER3, ORDER3_SHA256),
        (PARENT_MANIFEST, PARENT_MANIFEST_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_horizontal_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def singular_source(kind: str, stratum: str, engine: str, order: str) -> str:
    if kind not in KINDS or stratum not in STRATA:
        raise RuntimeError((kind, stratum))
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)

    extras = ["ib"]
    if stratum == "overlap_loaded":
        extras.append("inu")
    variables = names + extras
    if order == "dp":
        ordering = "dp"
    else:
        ordering = f"(dp({len(names)}),dp({len(extras)}))"
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
        lines.extend([
            "list LS=sat(I,ideal(w*x5*A));",
            "ideal C=LS[1];",
        ])
    else:
        lines.extend([
            "ideal IB=I,x5*A;",
            "list LS=sat(IB,ideal(w));",
            "ideal C=LS[1];",
        ])

    branch = ["C", "w"]
    if stratum == "x5":
        branch += ["x5", "ib*x3-1"]
    elif stratum == "A":
        branch += ["A", "ib*x5-1"]
    else:
        branch += ["x5", "x3"]
        if stratum == "overlap_loaded":
            branch.append("inu*e6-1")
        else:
            branch.append("e6")
    lines.extend([
        f"ideal B={','.join(branch)};",
        f"ideal G={engine}(B);",
        "int source_remzero=1;",
        "for(int j=1;j<=size(I);j++){if(reduce(I[j],G)!=0){source_remzero=0;}}",
        "int branch_remzero=1;",
        "for(int k=1;k<=size(B);k++){if(reduce(B[k],G)!=0){branch_remzero=0;}}",
        "int unitideal=0;if(reduce(1,G)==0){unitideal=1;}",
        'print("Q8-W0-HORIZONTAL-CLOSURE");',
        f'print("kind={kind}");',
        f'print("stratum={stratum}");',
        f'print("engine={engine}");',
        f'print("order={order}");',
        'print("source_dim="+string(dim(I)));',
        'print("saturated_dim="+string(dim(C)));',
        'print("branch_dim="+string(dim(G)));',
        'print("branch_vdim="+string(vdim(G)));',
        'print("branch_size="+string(size(G)));',
        'print("unit_ideal="+string(unitideal));',
        'print("source_remainder_zero="+string(source_remzero));',
        'print("branch_remainder_zero="+string(branch_remzero));',
        'print("e6_normal_form="+string(reduce(e6,G)));',
        'print("e8_normal_form="+string(reduce(e8,G)));',
        'print("BASIS_BEGIN");',
        "G;",
        'print("BASIS_END");',
        'print("Q8_W0_HORIZONTAL_CLOSURE_PASS");',
        "exit;",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=KINDS, required=True)
    parser.add_argument("--stratum", choices=STRATA, required=True)
    parser.add_argument("--engine", choices=("std", "slimgb"), default="std")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    args = parser.parse_args()
    print(singular_source(args.kind, args.stratum, args.engine, args.order))


if __name__ == "__main__":
    main()
