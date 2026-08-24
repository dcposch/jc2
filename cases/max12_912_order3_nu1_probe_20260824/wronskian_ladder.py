#!/usr/bin/env python3
"""Exact symbolic check of the k=0 order-three Wronskian tail ladder."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_parent():
    if sha256(PARENT.read_bytes()).hexdigest() != PARENT_SHA256:
        raise RuntimeError("parent compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("max12_order3_wronskian_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parent = load_parent()
    M = parent.M
    ring = M.Ring([f"a{i}" for i in range(8)])
    one = ring.one
    f = {9: one}
    U = {}
    for i in range(8):
        ai = ring.var(f"a{i}")
        f[i] = ai
        U[i - 9] = ai
    g = parent.faber(ring, 9, 12, U)

    z_of_w = parent.inverse_root(ring, 9, 19)
    tails = {}
    for ell in range(1, 9):
        coefficient = {}
        for z_exponent, g_coefficient in g.items():
            coefficient = M.cadd(
                coefficient,
                M.cmul(
                    g_coefficient,
                    M.zpower_coefficient(z_of_w, z_exponent, -ell, one),
                ),
            )
        tails[ell] = M.cscale(-1, coefficient)

    B = M.zadd(
        M.zscale(3, M.zmul(M.zderivative(g), f)),
        M.zscale(-4, M.zmul(g, M.zderivative(f))),
    )
    rhs = {}
    coefficients = {}
    for ell in range(1, 9):
        j = 9 - ell
        scalar = Fraction(3 * (ell + 12), j)
        coefficients[str(ell)] = str(scalar)
        derivative = M.zderivative(parent.faber(ring, 9, j, U))
        term = {
            exponent: M.cmul(M.cscale(scalar, tails[ell]), coeff)
            for exponent, coeff in derivative.items()
        }
        rhs = M.zadd(rhs, term)
    if B != rhs:
        raise RuntimeError("Wronskian tail identity mismatch")

    F3 = parent.faber(ring, 9, 3, U)
    expected_F3 = {
        3: one,
        1: M.cscale(Fraction(1, 3), ring.var("a7")),
        0: M.cscale(Fraction(1, 3), ring.var("a6")),
    }
    if F3 != expected_F3:
        raise RuntimeError("F3 mismatch")
    if parent.faber(ring, 9, 1, U) != {1: one}:
        raise RuntimeError("F1 mismatch")

    payload = {
        "case": "max12_912_order3_spectral_wronskian_ladder_20260824",
        "exact_identity": (
            "B=3*f*g_z-4*g*f_z="
            "sum_(l=1)^8 3*(l+12)/(9-l)*r_l*F_(9-l)'"
        ),
        "coefficient_table": coefficients,
        "order3_specialization": (
            "B=(15/2)*mu*F6'+18*nu*F3'+60*r8"
        ),
        "F3": "z^3+(a7/3)*z+a6/3=z^3+p*z+q",
        "mu0_nu_nonzero": "B=54*nu*z^2+18*nu*p+60*r8",
        "degree_ladder": {
            "mu_nonzero": 5,
            "mu_zero_nu_nonzero": 2,
            "mu_zero_nu_zero_r8_nonzero": 0,
        },
        "scope": (
            "k=0 algebraic Wronskian identity only; no component, trajectory, "
            "Taylor-boundary, maximum-12, or JC2 conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
