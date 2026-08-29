#!/usr/bin/env python3
"""Minimal replay of the blocked Ore/PassageMath constructor interface."""

from sage.all__sagemath_symbolics import ZZ, PolynomialRing
from ore_algebra import OreAlgebra


outer = PolynomialRing(ZZ, names=("ss", "xx", "yy"))
algebra = OreAlgebra(outer, "Dss", "Dxx", "Dyy")
print("OUTER", outer)
print("ORE", algebra)
try:
    print("GENS", algebra.gens())
except Exception as exc:
    print("FAIL_ORE_ASSOCIATED_COMMUTATIVE_ALGEBRA")
    print(type(exc).__name__, repr(exc))
    raise
