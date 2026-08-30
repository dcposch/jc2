#!/usr/bin/env python3
"""Desk-scale replay for the D3 two-support Halphen weighted boundary gate."""

from __future__ import annotations

import ast
import json
import sys

import sympy as sp


def fail(message: str) -> None:
    raise SystemExit(f"FAIL:{message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


allowed = {"--mutate-discriminant-sign"}
if any(arg not in allowed for arg in sys.argv[1:]):
    fail("unknown command-line argument")
mutate_discriminant_sign = "--mutate-discriminant-sign" in sys.argv[1:]

with open(__file__, "r", encoding="utf-8") as source_handle:
    source_tree = ast.parse(source_handle.read(), filename=__file__)
require(
    not any(isinstance(node, ast.Assert) for node in ast.walk(source_tree)),
    "source contains an assert node",
)

x, y, z, t = sp.symbols("x y z t")
a, ell, m, q0, q1, q2 = sp.symbols("a ell m q0 q1 q2")

monomials = [
    x**3,
    x**2 * y,
    x**2 * z,
    x * y**2,
    x * y * z,
    x * z**2,
    y**3,
    y**2 * z,
    y * z**2,
    z**3,
]
f2_coeffs = sp.symbols("A2 P2 V2 T2 M2 R2 B2 Q2 U2 C2")
f3_coeffs = sp.symbols("A3 P3 V3 T3 M3 R3 B3 Q3 U3 C3")
C2 = f2_coeffs[-1]

F1 = (
    a * x**3
    + ell * x**2 * y
    + m * x**2 * z
    + x * (q0 * y**2 + q1 * y * z + q2 * z**2)
    + y**3
)
F2 = sum(coefficient * monomial for coefficient, monomial in zip(f2_coeffs, monomials))
F3 = sum(coefficient * monomial for coefficient, monomial in zip(f3_coeffs, monomials))
F = sp.expand(x**3 + t * F1 + t**2 * F2 + t**3 * F3)

E1 = sp.cancel(F.subs(x, t * x) / t)
E2 = sp.cancel(E1.subs(y, t * y) / t)
E3 = sp.cancel(E2.subs(z, t * z) / t)

require(sp.expand(E1.subs(t, 0) - y**3) == 0, "first line-move reduction failed")
require(
    sp.expand(E2.subs(t, 0) - z**2 * (q2 * x + C2 * z)) == 0,
    "second line-move reduction failed",
)
require(sp.expand(E3 - F) == 0, "three-line cycle failed")

affine = sp.Poly(sp.expand(F.subs({z: 1, q2: 0})), x, y, t)
weighted_face = 0
lower_weight_terms = 0
for powers, coefficient in affine.terms():
    weight = 2 * powers[0] + powers[1] + 3 * powers[2]
    term = coefficient * x ** powers[0] * y ** powers[1] * t ** powers[2]
    if weight == 6:
        weighted_face += term
    if weight < 6:
        lower_weight_terms += term

P = x**3 + t * (y**3 + q1 * x * y) + C2 * t**2
require(sp.expand(weighted_face - P) == 0, "weight-six face failed")
require(sp.expand(lower_weight_terms) == 0, "unexpected term below weight six")

linear_t = y**3 + q1 * x * y
completed_square = C2 * (t + linear_t / (2 * C2)) ** 2 + x**3 - linear_t**2 / (4 * C2)
require(sp.cancel(P - completed_square) == 0, "weighted square completion failed")

h = sp.expand((1 + q1 * x) ** 2 - 4 * C2 * x**3)
h_discriminant = sp.factor(sp.discriminant(h, x))
expected_discriminant = -16 * C2 * (q1**3 + 27 * C2)
if mutate_discriminant_sign:
    expected_discriminant = -expected_discriminant
require(
    sp.expand(h_discriminant - expected_discriminant) == 0,
    "Weierstrass discriminant failed",
)

h_equality = sp.expand(h.subs(C2, -q1**3 / 27))
equality_factor = (q1 * x + 3) ** 2 * (4 * q1 * x + 3)
require(sp.expand(27 * h_equality - equality_factor) == 0, "nodal factorization failed")
double_root = -3 / q1
require(sp.cancel(h_equality.subs(x, double_root)) == 0, "double root value failed")
require(
    sp.cancel(sp.diff(h_equality, x).subs(x, double_root)) == 0,
    "double root derivative failed",
)
second_derivative = sp.factor(sp.diff(h_equality, x, 2).subs(x, double_root))
require(sp.expand(second_derivative + 2 * q1**2 / 3) == 0, "ordinary-node test failed")

require(sp.expand(P.subs({x: 1, y: 0, t: 0}) - 1) == 0, "weight-two orbifold point test failed")
require(sp.expand(P.subs({x: 0, y: 0, t: 1}) - C2) == 0, "weight-three orbifold point test failed")

control = x**3 + t * y**3 + t**2 * z**3
control_E1 = sp.cancel(control.subs(x, t * x) / t)
control_E2 = sp.cancel(control_E1.subs(y, t * y) / t)
control_E3 = sp.cancel(control_E2.subs(z, t * z) / t)
require(control_E1.subs(t, 0) == y**3, "control first reduction failed")
require(control_E2.subs(t, 0) == z**3, "control second reduction failed")
require(sp.expand(control_E3 - control) == 0, "control cycle failed")

result = {
    "control_cycle": ["x^3", "y^3", "z^3", "x^3"],
    "control_term_valuation_classes_mod_3": [0, 1, 2],
    "line_move_1_reduction": str(sp.expand(E1.subs(t, 0))),
    "line_move_2_reduction": str(sp.expand(E2.subs(t, 0))),
    "line_move_3_returns_input": True,
    "nodal_equality": "q1^3 + 27*C2 = 0 (hence q1 != 0 when C2 != 0)",
    "nodal_factorization_27h": str(sp.expand(equality_factor)),
    "nodal_second_derivative": str(second_derivative),
    "orbifold_coordinate_values": ["1", "C2"],
    "sympy_version": sp.__version__,
    "weighted_face": str(sp.expand(weighted_face)),
    "weierstrass_discriminant": str(h_discriminant),
}
print(json.dumps(result, sort_keys=True, separators=(",", ":")))
