#!/usr/bin/env python3
"""Exact audit of the b3-axis coefficient in the b4=0 terminal recurrence.

This is deliberately only a symbolic identity check.  It performs no
Groebner-basis computation and makes no claim about the full residual ideal.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


t, d, y, a = sp.symbols("t d y a")
q = 2 * t + 1
e = 3 * t + 1
relation_d = 3 * d**2 - (t + 1)
y_from_d = (d + t + 1) / (2 * q)


def numerator_mod_d(expression):
    """Return the numerator modulo 3*d**2-(t+1), over Q(t)."""
    numerator = sp.fraction(sp.cancel(expression))[0]
    return sp.factor(sp.rem(sp.Poly(numerator, d), sp.Poly(relation_d, d)).as_expr())


# Laurent/Euler spine constants.
g1 = e / q
g2 = e * y / q + e * t / (2 * q**2)
g = e * t * y / q**2 - e * t * (t + 1) / (6 * q**3)

# On the b3-axis, weighted homogeneity leaves
# C=h^(t-1), U=h^q+a*b3*h^t, T=g2*h^t, and
# S=g1*h^(2t)+Db*b3*h^(t-1).
Db = g * (6 * a * t + 5 * t + 2) / (2 * y * (2 * t - 1))
K = Db - g2

# If P0'=e*h^(3t)+X1*b3*h^(2t-1)+X2*b3^2*h^(t-2), direct
# coefficient extraction from its numerator gives these two scalars.
X1 = (K + y * e - 2 * q * g + 2 * a * t * g2) / (2 * y)
X2 = t * (y * K - 2 * a * g) / (2 * y)

# The sole surviving high row is [h^(3t)]R/b3.  It solves q_{t+1,0}=a*b3.
high = X1 - y * e - q * K - a * t * g1
a_closed = -(6 * d * t - 3 * d + 9 * t**2 + 2 * t - 1) / (6 * t * (3 * t - 1))
assert numerator_mod_d(high.subs({a: a_closed, y: y_from_d})) == 0

# The top residual row is [h^(2t-1)]R/b3^2.
top = X2 - y * X1 - a * t * K
A = 27 * t**3 - 30 * t**2 + t - 2
B = 6 * t**3 + 13 * t**2 - 3 * t + 2
lambda_closed = t * (3 * t + 1) * (A * d + B) / (
    12 * q**2 * (3 * t - 1) ** 2 * (3 * t + 2)
)
assert numerator_mod_d(
    (top - lambda_closed).subs({a: a_closed, y: y_from_d})
) == 0

# Unit check in A_t=Q[y]/(H_t): resultant of the primitive linear class.
H = 12 * q**2 * y**2 - 12 * q * (t + 1) * y + (t + 1) * (3 * t + 2)
linear_y = sp.expand(A * (2 * q * y - (t + 1)) + B)
resultant = sp.factor(sp.resultant(H, linear_y, y))
resultant_closed = -4 * q**2 * (t - 2) * (3 * t - 1) ** 2 * (3 * t + 2) * (
    27 * t**3 + 17 * t**2 + t + 2
)
assert sp.factor(resultant - resultant_closed) == 0

payload = {
    "typing": "exact symbolic b3-axis identity audit; not a full-ideal proof",
    "axis_high_solution_a": str(sp.factor(a_closed)),
    "stored_R_top_coefficient": str(sp.factor(lambda_closed)) + "*b3^2",
    "primitive_resultant_with_H_t": str(resultant),
    "assertions": {
        "high_row_vanishes_mod_3d2_minus_t_plus_1": True,
        "top_coefficient_matches_mod_3d2_minus_t_plus_1": True,
        "resultant_factorization_matches": True,
    },
    "exception_note": "For positive integer t, the resultant vanishes only at t=2.",
}

if __name__ == "__main__":
    output = Path(__file__).with_name("residual_b3_axis_exact_audit.json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
