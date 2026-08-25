#!/usr/bin/env python3
"""AWS-only structural checks for the D1 discriminant-point Newton chart.

This script keeps the moving common cubic in exact cusp coordinates

    p=-3*a^2,  c=2*a^3+h,
    K=(z-a)^2*(z+2*a)+h,

and uses Hermite coordinates at the double and simple roots for every normal
direction.  At a=1,h=0 it verifies the singular cubic cancellation and its
quartic successor, including arbitrary next corrections Q2,R3.
"""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import platform


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_double_root_newton_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def main() -> None:
    tag = require_aws()
    import sympy as sp

    z, a, h = sp.symbols("z a h")
    x = z - a
    p = -3 * a**2
    c = 2 * a**3 + h
    K = sp.expand(z**3 + p*z + c)
    expected_K = sp.expand(x**2 * (x + 3*a) + h)
    if sp.expand(K - expected_K) != 0:
        raise RuntimeError("cusp coordinate identity")
    Delta = sp.factor(-4*p**3 - 27*c**2)
    if Delta != -27*h*(4*a**3 + h):
        raise RuntimeError(("discriminant factor", Delta))
    jacobian = sp.det(sp.Matrix([[sp.diff(p, a), sp.diff(p, h)],
                                 [sp.diff(c, a), sp.diff(c, h)]]))
    if jacobian.subs({a: 1, h: 0}) != -6:
        raise RuntimeError(("chart Jacobian", jacobian))

    # Hermite coordinates P(a)=A, P'(a)=D, P(-2a)=B.
    A, D, B = sp.symbols("A D B")
    P = sp.expand(A + D*x + (B-A+3*a*D)*x**2/(9*a**2))
    hermite_checks = [sp.simplify(P.subs(z, a)-A),
                      sp.simplify(sp.diff(P, z).subs(z, a)-D),
                      sp.simplify(P.subs(z, -2*a)-B)]
    if any(hermite_checks):
        raise RuntimeError(("Hermite inversion", hermite_checks))

    # Normalized centre and its one-dimensional nilradical.
    L = sp.symbols("L")
    U = L + 3
    K0 = sp.expand(L**2 * U)
    nil = sp.expand(L * U)
    if sp.expand(nil**2 - K0*U) != 0:
        raise RuntimeError("nilradical square")

    # The alpha=2*beta leading cancellation and arbitrary next corrections.
    t, q = sp.symbols("t q", nonzero=True)
    u2, u1, u0, v2, v1, v0 = sp.symbols("u2 u1 u0 v2 v1 v0")
    Q2 = u2*L**2 + u1*L + u0
    R3 = v2*L**2 + v1*L + v0
    Q = t*q*nil + t**2*Q2
    R = t**2*q**2/3 + t**3*R3

    # Every negative f^(4/3) monomial that can contribute through t^4.
    tail = (sp.Rational(4, 9)*Q*R/K0
            + sp.Rational(2, 9)*R**2/K0**2
            - sp.Rational(4, 81)*Q**3/K0**2
            - sp.Rational(4, 27)*Q**2*R/K0**3
            + sp.Rational(5, 243)*Q**4/K0**4)
    t3 = sp.cancel(sp.expand(tail).coeff(t, 3))
    if sp.cancel(t3 + sp.Rational(4, 81)*q**3) != 0:
        raise RuntimeError(("cubic cancellation", t3))
    t4 = sp.cancel(sp.expand(tail).coeff(t, 4))
    numerator, denominator = sp.fraction(t4)
    common_numerator = sp.cancel(t4 * K0**2)
    if sp.denom(common_numerator) != 1:
        raise RuntimeError(("t4 common numerator denominator", common_numerator))
    common_numerator = sp.expand(common_numerator)
    residue = sp.rem(sp.Poly(common_numerator, L), sp.Poly(K0, L)).as_expr()
    expected_residue = sp.expand(q**4*(5*L**2+18*L+15)/243)
    if sp.expand(residue-expected_residue) != 0:
        raise RuntimeError(("quartic residue", residue, expected_residue,
                            numerator, denominator))
    if sp.rem(sp.Poly(5*L**2+18*L+15, L), sp.Poly(K0, L)).is_zero:
        raise RuntimeError("quartic obstruction unexpectedly zero")

    # A row-6 target subtracts only a scalar modulo K; H is not scalar.
    nu = sp.symbols("nu")
    target_residue = sp.rem(
        sp.Poly(expected_residue-nu, L), sp.Poly(K0, L)).as_expr()
    if sp.Poly(target_residue, L).degree() != 2:
        raise RuntimeError(("row6 scalar control", target_residue))

    payload = {
        "aws_tag": tag,
        "axis_cusp_chart": {
            "p": "-3*a^2",
            "c": "2*a^3+h",
            "K": "(z-a)^2*(z+2*a)+h",
            "Delta": "-27*h*(4*a^3+h)",
            "jacobian_at_a1_h0": str(jacobian.subs({a: 1, h: 0})),
            "meaning": "a is the discriminant-axis coordinate; h is transverse",
        },
        "all_normal_directions": {
            "coordinates": ["P(a)", "P'(a)", "P(-2*a)"],
            "inverse": str(P),
            "applied_separately_to": ["Q", "R"],
        },
        "normalized_residue_algebra": {
            "K0": "L^2*(L+3)",
            "nilradical_generator": "L*(L+3)",
            "nilradical_square": "K0*(L+3)",
        },
        "alpha_equals_2beta_control": {
            "Q1": "q*L*(L+3)",
            "R2": "q^2/3",
            "weight_3beta_tail": str(t3),
            "interpretation": "polynomial, so every negative tail vanishes at this order",
        },
        "quartic_successor": {
            "arbitrary_corrections": {
                "Q2": str(Q2),
                "R3": str(R3),
            },
            "common_denominator": "K0^2",
            "numerator_mod_K0": str(expected_residue),
            "nonzero_at_double_root": str(expected_residue.subs(L, 0)),
            "nonconstant_mod_K0": True,
            "row3_target_mod_K0": "0 (its numerator is a multiple of K0)",
            "row6_scalar_cannot_cancel": str(target_residue),
            "scope": "kills this singular leading branch one Newton order later; no claim that all tropical branches are classified",
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-DOUBLE-ROOT-NEWTON-STRUCTURE")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
