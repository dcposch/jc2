#!/usr/bin/env python3
"""Generate direct absolute decomposition of the Q8 generic fibre."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
GENERIC_GENERATOR = ROOT / "cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py"
GENERIC_GENERATOR_SHA256 = "6b752b03d777c73de5d9ff729f30d01f5d81229d0ee467e9ad98a349d6234daf"


def load_compiler():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (GENERIC_GENERATOR, GENERIC_GENERATOR_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_generic_abs_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source(engine: str) -> str:
    Q = load_compiler()
    ring, rows, imposed, names = Q.compile_quotient("approx")
    variables = ["c", "d2", "d4", "x1", "x3", "x5", "inv", "v"]
    lines = [
        'LIB "primdec.lib";',
        f"ring R=(0,w),({','.join(variables)}),(dp(7),dp(1));",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(f"poly e{ell}={Q.M.coeff_string(rows[ell], names)};")
    lines.extend([
        "poly einv=inv*x5*(x3-2*x5)-1;",
        "poly ev=v*x5-x3+2*x5;",
        "ideal I=e1,e3,e5,e7,e2,e4,einv,ev;",
        f"ideal G={engine}(I);",
        'print("Q8-GENERIC-ABSPRIMDEC");',
        'print("generic_dim="+string(dim(G)));',
        'print("generic_size="+string(size(G)));',
        'print("generic_vdim="+string(vdim(G)));',
        "def ABS=absPrimdecGTZ(G);",
        "setring ABS;",
        'print("rational_primary_count="+string(size(primary_decomp)));',
        'print("absolute_class_count="+string(size(absolute_primes)));',
        "for (int component=1; component<=size(absolute_primes); component++)",
        "{",
        "  ideal P=std(absolute_primes[component][1]);",
        "  int conjugates=absolute_primes[component][2];",
        "  ideal EV=eliminate(P,c*d2*d4*x1*x3*x5*inv);",
        "  EV=std(EV);",
        '  print("ABSOLUTE_CLASS="+string(component));',
        '  print("conjugates="+string(conjugates));',
        '  print("prime_dim="+string(dim(P)));',
        '  print("prime_size="+string(size(P)));',
        '  print("v_elimination_size="+string(size(EV)));',
        "  EV;",
        "}",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), default="slimgb")
    args = parser.parse_args()
    print(source(args.engine))


if __name__ == "__main__":
    main()

