#!/usr/bin/env python3
"""Exact desk replay for the D3 sectioned two-support global control.

The script checks only finite symbolic identities and projective Jacobian
tests over QQ.  It neither searches a parameter space nor infers a proper
block from the exhibited incidence surface.
"""

from __future__ import annotations

import json

import sympy as sp


S, T, s, t = sp.symbols("S T s t")
x, y, z = sp.symbols("x y z")
X, Y, Z, q = sp.symbols("X Y Z q")
U, V = sp.symbols("U V")


def is_zero(poly: sp.Expr) -> bool:
    return sp.expand(poly) == 0


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(f"replay check failed: {label}")


def projectively_smooth(cubic: sp.Expr, variables: tuple[sp.Symbol, ...]) -> bool:
    """Check that the homogeneous Jacobian has no projective zero over QQbar."""

    derivatives = [sp.diff(cubic, variable) for variable in variables]
    for chart in variables:
        chart_variables = tuple(variable for variable in variables if variable != chart)
        chart_ideal = [derivative.subs(chart, 1) for derivative in derivatives]
        basis = sp.groebner(chart_ideal, *chart_variables, order="lex")
        if not any(poly.as_expr() == 1 for poly in basis.polys):
            return False
    return True


# The affine and bihomogeneous presentations.
F = (x + t * z) ** 3 + t * y**3 + t * (t * x + z) ** 2 * y
G = (S * x + T * z) ** 3 + S**2 * T * (y**3 + z**2 * y) + 2 * S * T**2 * x * z * y + T**3 * x**2 * y
require(is_zero(G.subs({S: 1, T: t}) - F), "bihomogeneous dehomogenization")

coefficients = tuple(sp.expand(G).coeff(S, 3 - index).coeff(T, index) for index in range(4))
expected_coefficients = (
    x**3,
    3 * x**2 * z + y**3 + z**2 * y,
    3 * x * z**2 + 2 * x * z * y,
    z**3 + x**2 * y,
)
require(
    all(is_zero(left - right) for left, right in zip(coefficients, expected_coefficients)),
    "binary-cubic coefficient expansion",
)

# Basepoint freeness has a triangular proof: c0=0 gives x=0, c3=0 then
# gives z=0, and c1=0 then gives y=0.  The following substitutions replay it.
c0, c1, c2, c3 = coefficients
require(c0 == x**3, "basepoint step x")
require(sp.expand(c3.subs(x, 0)) == z**3, "basepoint step z")
require(sp.expand(c1.subs({x: 0, z: 0})) == y**3, "basepoint step y")

# Two reverse (1,1) CFS moves, at t=1 and t=-1, followed by X=x+tz.
u = t - 1
v = t + 1
H0 = X**3 + t * Y**3 + t * (t * X - Z) ** 2 * Y
RuvH0 = X**3 + t * Y**3 + t * (t * X - u * v * Z) ** 2 * Y
require(
    is_zero(RuvH0.subs({X: x + t * z, Y: y, Z: z}) - F),
    "two reverse CFS moves and shear",
)

# The minimal pointed generic cubic is V^2=U^3-t^4 on the chart Y=1:
# U=-tX and V=t^2(tX-Z).
W = sp.symbols("W")
affine_H0 = X**3 + t + t * W**2
weierstrass = V**2 - U**3 + t**4
require(
    is_zero(weierstrass.subs({U: -t * X, V: t**2 * W}) - t**3 * affine_H0),
    "generic Weierstrass identity",
)

# Away from t=0, the transformed fibre is U^3+tY^3+tV^2Y.  Its three
# projective partials have no common zero: U=0 and VY=0, while
# 3Y^2+V^2=0.  Record the exact identities used in that argument.
generic_normal_form = U**3 + t * Y**3 + t * V**2 * Y
generic_partials = tuple(sp.diff(generic_normal_form, variable) for variable in (U, Y, V))
expected_partials = (3 * U**2, t * (V**2 + 3 * Y**2), 2 * V * Y * t)
require(
    all(is_zero(left - right) for left, right in zip(generic_partials, expected_partials)),
    "generic fibre Jacobian",
)

# At t=0 in z=1, F=x^3+t*A.  A(0,y,0)=y^3+y has three simple roots, so
# (x,t,A) are local coordinates at each point and the germ is x^3+t*A=A2.
F_z1 = sp.expand(F.subs(z, 1))
A = sp.cancel((F_z1 - x**3) / t)
root_polynomial = sp.expand(A.subs({x: 0, t: 0}))
require(root_polynomial == y**3 + y, "t=0 transverse polynomial")
require(
    sp.gcd(root_polynomial, sp.diff(root_polynomial, y)) == 1,
    "three simple t=0 roots",
)

# At infinity, s^3 F(1/s) has the exact A2 form after the invertible local
# coordinates U=sx+z and V=x+sz (determinant s^2-1).
H_inf = (s * x + z) ** 3 + s**2 * y**3 + (x + s * z) ** 2 * y
require(
    is_zero(sp.expand(s**3 * F.subs(t, 1 / s)) - H_inf),
    "infinity chart",
)
require(
    sp.det(sp.Matrix([[s, 1], [1, s]])) == s**2 - 1,
    "infinity coordinate determinant",
)

# At t=+/-1 the tangent cones at the two contracted points are smooth plane
# cubics.  Hence an ordinary blowup resolves each germ along a smooth elliptic
# exceptional curve (the simple-elliptic cubic-cone case).
C_plus = X**3 + Y**3 + (X - 2 * q) ** 2 * Y
C_minus = X**3 - Y**3 - (X - 2 * q) ** 2 * Y
require(projectively_smooth(C_plus, (X, Y, q)), "smooth plus tangent cubic")
require(projectively_smooth(C_minus, (X, Y, q)), "smooth minus tangent cubic")

# Mutation gates: deleting z^3 introduces the projective basepoint [0:0:1],
# deleting q from the tangent cone makes it singular at [0:0:1], and changing
# the double reverse factor destroys the construction identity.
mutated_coefficients = (c0, c1, c2, x**2 * y)
require(
    all(poly.subs({x: 0, y: 0, z: 1}) == 0 for poly in mutated_coefficients),
    "basepoint mutation detected",
)
require(
    not projectively_smooth(X**3 + Y**3, (X, Y, q)),
    "singular tangent mutation detected",
)
mutated_reverse = X**3 + t * Y**3 + t * (t * X - (u * v + 1) * Z) ** 2 * Y
require(
    not is_zero(mutated_reverse.subs({X: x + t * z, Y: y, Z: z}) - F),
    "reverse-factor mutation detected",
)

print(
    json.dumps(
        {
            "a2_points_at_t0": 3,
            "base_coefficients": [str(poly) for poly in coefficients],
            "cfs_centres": ["t-1", "t+1"],
            "finite_flat_rank": 3,
            "infinity_type": "A2",
            "minimal_weierstrass": "V^2=U^3-t^4",
            "mutation_gates": "PASS",
            "tangent_cones_smooth": [True, True],
        },
        sort_keys=True,
    )
)
