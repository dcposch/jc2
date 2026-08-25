#!/usr/bin/env python3
"""Emit the six generic internal Newton supports in PHCpack syntax."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
VARIABLES = ["qc", "d2", "d4", "x1", "x3", "x5"]


def load_compiler():
    assert sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256
    spec = importlib.util.spec_from_file_location("q8_phc_support_compiler", COMPILER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def monomial(exponents: tuple[int, ...]) -> str:
    factors = []
    for variable, exponent in zip(VARIABLES, exponents):
        if exponent:
            factors.append(variable if exponent == 1 else f"{variable}^{exponent}")
    return "*".join(factors) if factors else "1"


def main() -> None:
    compiler = load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    assert names == ["w", "c", "d2", "d4", "x1", "x3", "x5"]
    print(len(imposed))
    for ell in imposed:
        support = sorted({tuple(monomial_value[1:]) for monomial_value in rows[ell]})
        print(" + ".join(monomial(item) for item in support) + ";")


if __name__ == "__main__":
    main()
