#!/usr/bin/env python3
"""Generate an exact fixed-w finite-field Q8 quotient fibre for msolve."""

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
FIXED_GENERATOR = ROOT / "cases/max12_912_order3_nu_q8_fibre_specialization_aws_20260825/generate.py"
FIXED_GENERATOR_SHA256 = "4af6f7eca198bcdf1e60151449e08099853669bd1d6965db3cddffa666032d2c"


def load_compiler():
    for path, expected in (
        (COMPILER, COMPILER_SHA256),
        (PARENT_MANIFEST, PARENT_MANIFEST_SHA256),
        (GENERIC_GENERATOR, GENERIC_GENERATOR_SHA256),
        (FIXED_GENERATOR, FIXED_GENERATOR_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_msolve_fibre_compiler", COMPILER)
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


def source(prime: int, w_value: int) -> str:
    if prime <= 3 or w_value % prime == 0:
        raise RuntimeError("prime must exceed 3 and w must be nonzero")
    Q = load_compiler()
    _ring, rows, imposed, names = Q.compile_quotient("approx")
    base_names = names[1:]
    variables = base_names + ["inv", "v"]
    equations = []
    for ell in imposed:
        fixed = specialize(rows[ell], w_value % prime)
        equations.append(Q.M.coeff_string(fixed, base_names))
    equations.extend([
        "inv*x5*(x3-2*x5)-1",
        "v*x5-x3+2*x5",
    ])
    lines = [",".join(variables), str(prime)]
    for index, equation in enumerate(equations):
        lines.append(equation + ("," if index + 1 < len(equations) else ""))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--w-value", type=int, required=True)
    args = parser.parse_args()
    print(source(args.prime, args.w_value))


if __name__ == "__main__":
    main()

