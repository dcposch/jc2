#!/usr/bin/env python3
"""Exact cubic-root order chart with the a1-curved radius-two centre.

This is a linear order-space calculation, not Moh's omitted full lift.  It
keeps the face parameter ``a`` and the unrecoverable jet ``u=a1`` symbolic.
The harmless polynomial translation has set a0=0, while a2 is absorbed into
the radius-two coordinate z so that the double root of H is at zero.
"""

from __future__ import annotations

import json
from math import ceil

import sympy as sp


x, w, z, a, u = sp.symbols("x w z a u")
D = 11
# The normalized top face has integralized weight 32.  Perturbations must be
# strict, hence weight at least 33; equality would change that face.
MAJOR_THRESHOLD = 33
MINOR_THRESHOLD = 9
H = sp.expand(z**2 * (z + 3 * a))


def constant_pivot(rows, tags, variables):
    """Apply only affine pivots whose coefficient lies in Q*."""
    rows = list(rows)
    tags = list(tags)
    variables = list(variables)
    pivots = []
    while True:
        choice = None
        for row_index, (tag, expression) in enumerate(zip(tags, rows)):
            for variable_index, variable in enumerate(variables):
                coefficient = sp.expand(sp.diff(expression, variable))
                remainder = sp.expand(expression - coefficient * variable)
                if (coefficient.is_Rational and coefficient != 0
                        and variable not in remainder.free_symbols):
                    choice = (row_index, variable_index, tag, variable,
                              coefficient, remainder)
                    break
            if choice is not None:
                break
        if choice is None:
            break
        row_index, variable_index, tag, variable, coefficient, remainder = choice
        rhs = sp.expand(-remainder / coefficient)
        assert sp.expand(rows[row_index].subs(variable, rhs)) == 0
        pivots.append((tag, variable, coefficient, rhs))
        del rows[row_index]
        del tags[row_index]
        del variables[variable_index]
        next_rows = []
        next_tags = []
        for tag_i, expression in zip(tags, rows):
            reduced = sp.expand(expression.subs(variable, rhs))
            if reduced != 0:
                next_rows.append(reduced)
                next_tags.append(tag_i)
        rows, tags = next_rows, next_tags
    return rows, tags, variables, pivots


# K=x^11*h(x^-1,w/x).  Its x^0 term is the normalized top face.  At the
# selected major direction w=1, ord(h)>=-1/3 has boundary weight 32.
# Requiring 3*r+4*ord_(w-1)(P_r)>=33 keeps the fixed face unchanged.
# Parameterizing each P_r by the corresponding divisibility avoids the raw
# 78-coefficient triangular array.
K = w**3 * (w - 1)**8
parameters = []
major_rows = []
for r in range(1, D + 1):
    cap = D - r
    vanish_at_one = max(0, ceil((MAJOR_THRESHOLD - 3 * r) / 4))
    for degree in range(vanish_at_one, cap + 1):
        coefficient = sp.Symbol(f"c_{r}_{degree}")
        parameters.append(coefficient)
        K += coefficient * x**r * (w - 1)**vanish_at_one \
            * w**(degree - vanish_at_one)
        major_rows.append((r, cap, vanish_at_one, degree))

# The curved minor centre is w=u*x^2+x^3*z.  Since Omega(h) has radius-two
# order -2, x^11*Omega(h) must have x-order at least 9.  Its x^9 coefficient
# is fixed to H; all lower coefficients vanish.
minor_expansion = sp.Poly(sp.expand(K.subs(w, u * x**2 + x**3 * z)), x, z)
equations = []
tags = []
for x_degree in range(MINOR_THRESHOLD + 1):
    for z_degree in range(D + 1):
        coefficient = minor_expansion.coeff_monomial(x**x_degree * z**z_degree)
        target = H.coeff(z, z_degree) if x_degree == MINOR_THRESHOLD else 0
        equation = sp.expand(coefficient - target)
        if equation != 0:
            equations.append(equation)
            tags.append((x_degree, z_degree))

remaining_rows, remaining_tags, free_parameters, pivots = constant_pivot(
    equations, tags, parameters
)
assert not remaining_rows
assert len(parameters) == 21
assert len(equations) == 18
assert len(pivots) == 18
assert [str(v) for v in free_parameters] == [
    "c_7_4", "c_10_1", "c_11_0"
]
assert all(sp.sympify(coefficient).is_Rational and coefficient != 0
           for _, _, coefficient, _ in pivots)

# Verify the triangular map on all original rows after resolving pivot right
# sides in reverse order.  No division by a or u occurs.
resolved = {}
for tag, variable, coefficient, rhs in reversed(pivots):
    resolved[variable] = sp.expand(rhs.subs(resolved, simultaneous=True))
assert all(sp.expand(equation.subs(resolved, simultaneous=True)) == 0
           for equation in equations)

output = {
    "scope": "H-ORDER-SPACE; NOT THE FULL 11-VARIABLE LIFT",
    "coordinates": {
        "K_definition": "K=x^11*h(x^-1,w/x)",
        "minor_centre": "w=u*x^2+x^3*z, u=a1",
        "minor_face": "x^-9*K(...)=H+O(x), H=z^2*(z+3*a)",
        "major_weight": "strict fixed-face kernel: 3*r+4*q>=33 at w=1 (boundary weight 32)",
        "minor_weight": "r+2*j+3*q after curved-centre expansion; terms <9 vanish",
    },
    "counts": {
        "major_filtered_coefficients_before_minor_rows": len(parameters),
        "minor_face_equations": len(equations),
        "Qstar_pivots": len(pivots),
        "free_h_tail_coefficients_over_Q[a,u]": len(free_parameters),
        "family_dimension_including_a_and_u": len(free_parameters) + 2,
    },
    "free_parameters": [str(v) for v in free_parameters],
    "pivots": [
        {
            "band_tag": list(tag),
            "variable": str(variable),
            "coefficient": str(coefficient),
            "rhs": str(sp.factor(rhs)),
        }
        for tag, variable, coefficient, rhs in pivots
    ],
    "checks": {
        "all_rows_zero_after_resolved_map": True,
        "no_parameter_inverted": True,
        "a_and_u_remain_symbolic": True,
    },
}
print(json.dumps(output, indent=2, sort_keys=True))
