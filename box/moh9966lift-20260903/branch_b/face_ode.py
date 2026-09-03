#!/usr/bin/env python3
"""Exact localized leading-face system for Moh's radius-two branch B."""

from __future__ import annotations

import json

import sympy as sp


z, x, y = sp.symbols("z x y")
a, k, q3, q2, q1, q0, T = sp.symbols("a k q3 q2 q1 q0 T")
H = z**2 * (z + 3 * a)
q = z**4 + q3 * z**3 + q2 * z**2 + q1 * z + q0
R = sp.expand(H**12 * q)

# Dividing 2*H*R'-25*H'*R=k*H^14 by H^12 gives this degree-six
# polynomial.  Its constant row is twice a times the z-row, so retain one.
reduced_ode = sp.Poly(sp.expand(2 * H * sp.diff(q, z)
                                - sp.diff(H, z) * q - k * H**2), z)
raw_rows = [reduced_ode.coeff_monomial(z**degree)
            for degree in range(6, 0, -1)]
assert sp.expand(raw_rows[-1] - 2 * a * raw_rows[-2]) == 0
rows = raw_rows[:-1]

variables = (T, q0, q1, q2, q3, k, a)
wrapper = T * a * k - 1
main = sp.groebner(rows + [wrapper], *variables, order="lex")
wrapper_only = sp.groebner([wrapper], *variables, order="lex")
unsaturated = sp.groebner(rows, *variables, order="lex")
control_a = sp.groebner(rows + [wrapper, a], *variables, order="lex")
control_k = sp.groebner(rows + [wrapper, k], *variables, order="lex")
assert not main.contains(sp.Integer(1))
assert not wrapper_only.contains(sp.Integer(1))
assert not unsaturated.contains(sp.Integer(1))
assert control_a.contains(sp.Integer(1))
assert control_k.contains(sp.Integer(1))

solution = {
    k: 5,
    q3: 4 * a,
    q2: -3 * a**2,
    q1: -18 * a**3,
    q0: 0,
    T: 1 / (5 * a),
}
assert all(sp.cancel(row.subs(solution)) == 0 for row in rows + [wrapper])
q_solution = sp.factor(q.subs(solution))
R_solution = sp.factor(R.subs(solution))
assert q_solution == z * (z - 2 * a) * (z + 3 * a)**2
assert R_solution == z**25 * (z + 3 * a)**14 * (z - 2 * a)

u = x * y
G_face = y**18 * (u + 3 * a)**9
F_face = y**12 * (u + 3 * a)**6
T2_face = y**10 * (u + 3 * a)**5
T3_face = y**25 * (u + 3 * a)**14 * (u - 2 * a)


def jac(first, second):
    return sp.factor(sp.diff(first, x) * sp.diff(second, y)
                     - sp.diff(first, y) * sp.diff(second, x))


face_jacobian = jac(T3_face, G_face)
assert sp.expand(face_jacobian
                 - 45 * x * y**44 * (u + 3 * a)**22) == 0
assert jac(F_face, G_face) == 0


def inverse_omega_check(expr, degree):
    """Termwise check of the inverse-Omega degree envelope.

    Omega^-1(x^e*y^j)=X^(j-e)[X^2(Y-a0)-a1X-a2]^j.  Thus a face
    monomial is individually polynomial of old degree at most D when
    j-e>=0 and 4j-e<=D.  Cancellation is not used here.
    """
    support = [monomial for monomial, coefficient
               in sp.Poly(sp.expand(expr), x, y).terms() if coefficient]
    assert all(j - e >= 0 and 4 * j - e <= degree for e, j in support)
    return {
        "terms": len(support),
        "min_j_minus_e": min(j - e for e, j in support),
        "max_4j_minus_e": max(4 * j - e for e, j in support),
    }


output = {
    "scope": "RADIUS-TWO-LEADING-FACE-ONLY",
    "verdict": "SURVIVES[PRINTED-LEADER-ODE-FACE]",
    "ring": "Q[T,q0,q1,q2,q3,k,a]",
    "wrapper": "T*a*k-1",
    "unknowns_excluding_wrapper": 6,
    "raw_rows": [str(sp.factor(row)) for row in raw_rows],
    "independent_rows": len(rows),
    "dimension": 1,
    "free_parameter": "a != 0",
    "solution": {str(symbol): str(value) for symbol, value in solution.items()},
    "q": str(q_solution),
    "H": str(sp.factor(H)),
    "R": str(R_solution),
    "wrapped_reduced_basis": [str(poly.as_expr()) for poly in main.polys],
    "controls": {
        "main_unit": main.contains(sp.Integer(1)),
        "wrapper_only_unit": wrapper_only.contains(sp.Integer(1)),
        "unsaturated_unit": unsaturated.contains(sp.Integer(1)),
        "plus_a_unit": control_a.contains(sp.Integer(1)),
        "plus_k_unit": control_k.contains(sp.Integer(1)),
    },
    "bivariate_faces": {
        "F": str(F_face),
        "G": str(G_face),
        "T2": str(T2_face),
        "T3": str(T3_face),
        "J(T3,G)": str(face_jacobian),
        "J(F,G)": "0",
        "inverse_Omega": {
            "F_degree_66": inverse_omega_check(F_face, 66),
            "G_degree_99": inverse_omega_check(G_face, 99),
            "T2_degree_55": inverse_omega_check(T2_face, 55),
            "T3_degree_145": inverse_omega_check(T3_face, 145),
        },
    },
}
print(json.dumps(output, indent=2, sort_keys=True))
