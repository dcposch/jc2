#!/usr/bin/env python3
"""Exact leading-face check for Xu's delta=5/2 exceptional split.

This is only a face calculation in Moh's Omega chart.  It does not construct
an original-coordinate Keller pair.
"""

from __future__ import annotations

import json

import sympy as sp


z, x, y, s = sp.symbols("z x y s")
A, B, C = sp.symbols("A B C")
rho, k, T, U = sp.symbols("rho k T U")
b = sp.symbols("b0:10")  # b[i] is the coefficient of z**i in q1.


# Half-integral radius in an integer-exponent Omega chart.  The f-face is
# x^-3*p(sqrt(x)*y)^6, so p^6 must be even.  These two triangular pivots
# force a monic cubic p to be odd; all remaining parity rows then vanish.
p_general = z**3 + A * z**2 + B * z + C
p6 = sp.Poly(sp.expand(p_general**6), z)
parity_rows = [p6.coeff_monomial(z**j) for j in range(1, 19, 2)]
parity_pivots = [sp.expand(p6.coeff_monomial(z**17)),
                 sp.expand(p6.coeff_monomial(z**15).subs(A, 0))]
assert parity_pivots == [6 * A, 6 * C]
assert all(sp.expand(row.subs({A: 0, C: 0})) == 0 for row in parity_rows)
parity_variables = (U, A, C, B)
parity_wrapper = U * B - 1
parity_gb = sp.groebner(parity_rows + [parity_wrapper], *parity_variables,
                        order="lex")
parity_negative = sp.groebner(parity_rows + [parity_wrapper, B],
                              *parity_variables, order="lex")
parity_wrapper_only = sp.groebner([parity_wrapper], *parity_variables,
                                  order="lex")
parity_unsaturated = sp.groebner(parity_rows, *parity_variables, order="lex")
assert not parity_gb.contains(sp.Integer(1))
assert parity_negative.contains(sp.Integer(1))
assert not parity_wrapper_only.contains(sp.Integer(1))
assert not parity_unsaturated.contains(sp.Integer(1))
assert all(sp.expand(row.subs({A: 0, B: -1, C: 0, U: -1})) == 0
           for row in parity_rows + [parity_wrapper])

# Write B=-rho.  On rho != 0 this has the three distinct roots
# 0,+/-sqrt(rho).  (Xu calls this splitting parameter c; it is not the
# constant Jacobian scalar.)
p = z * (z**2 - rho)
assert sp.discriminant(p, z) == 4 * rho**3

# Xu first obtains q=p^10*q1, deg(q1)=10.  Fix the torus gauge by making q1
# monic.  The reduced face equation is q1'=k*p^3.
q1 = z**10 + sum(b[i] * z**i for i in range(10))
reduced = sp.Poly(sp.expand(sp.diff(q1, z) - k * p**3), z)
ode_rows = [reduced.coeff_monomial(z**j) for j in range(9, -1, -1)]

solution = {
    k: sp.Integer(10),
    b[9]: sp.Integer(0),
    b[8]: -sp.Rational(15, 4) * rho,
    b[7]: sp.Integer(0),
    b[6]: 5 * rho**2,
    b[5]: sp.Integer(0),
    b[4]: -sp.Rational(5, 2) * rho**3,
    b[3]: sp.Integer(0),
    b[2]: sp.Integer(0),
    b[1]: sp.Integer(0),
}
assert all(sp.expand(row.subs(solution)) == 0 for row in ode_rows)

q1_solution = sp.expand(q1.subs(solution))
quotient_resultant = sp.factor(sp.resultant(p, q1_solution, z))
assert quotient_resultant == b[0] * (4 * b[0] - rho**5)**2 / 16
q = sp.expand(p**10 * q1)
raw_face_ode = sp.expand(p * sp.diff(q, z) - 10 * sp.diff(p, z) * q - k * p**14)
assert sp.expand(raw_face_ode - p**11 * (sp.diff(q1, z) - k * p**3)) == 0
assert sp.expand(raw_face_ode.subs(solution)) == 0

# Saturation wrapper.  This selects a genuine split (rho != 0) and a nonzero
# ODE scalar induced by the nonzero Jacobian (k != 0).  The main ideal is
# nonunit, while adjoining rho=0
# or k=0 to that wrapped ideal is a negative control and gives [1].
variables = (T, b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], k,
             b[0], rho)
wrapper = T * rho * k - 1
main_gb = sp.groebner(ode_rows + [wrapper], *variables, order="lex")
control_rho = sp.groebner(ode_rows + [wrapper, rho], *variables, order="lex")
control_k = sp.groebner(ode_rows + [wrapper, k], *variables, order="lex")
wrapper_only = sp.groebner([wrapper], *variables, order="lex")
unsaturated = sp.groebner(ode_rows, *variables, order="lex")
assert not main_gb.contains(sp.Integer(1))
assert control_rho.contains(sp.Integer(1))
assert control_k.contains(sp.Integer(1))
assert not wrapper_only.contains(sp.Integer(1))
assert not unsaturated.contains(sp.Integer(1))

witness = {rho: 1, b[0]: 1, T: sp.Rational(1, 10), **solution}
assert all(sp.expand(row.subs(witness)) == 0 for row in ode_rows + [wrapper])

# Integer-exponent bivariate faces in the ramified evaluation
# (x,y)=(s^2,z/s).  H has order -1/2, and R has order -5.
u = x * y**2
H = y * (u - rho)
Q = u**5 - sp.Rational(15, 4) * rho * u**4 + 5 * rho**2 * u**3 \
    - sp.Rational(5, 2) * rho**3 * u**2 + b[0]
R = H**10 * Q
G = H**9
F = H**6
T2 = H**5
jac_F_G = sp.factor(sp.diff(F, x) * sp.diff(G, y)
                    - sp.diff(F, y) * sp.diff(G, x))
assert jac_F_G == 0
jac = sp.factor(sp.diff(R, x) * sp.diff(G, y) - sp.diff(R, y) * sp.diff(G, x))
assert sp.expand(jac - 45 * x * H**22) == 0
assert sp.simplify(H.subs({x: s**2, y: z / s}) - p / s) == 0
assert sp.simplify(F.subs({x: s**2, y: z / s}) - p**6 / s**6) == 0
assert sp.simplify(G.subs({x: s**2, y: z / s}) - p**9 / s**9) == 0
assert sp.simplify(T2.subs({x: s**2, y: z / s}) - p**5 / s**5) == 0
assert sp.simplify(R.subs({x: s**2, y: z / s})
                   - p**10 * q1_solution / s**10) == 0

# Xu's displayed normalization is k=-2.  It differs only by scaling R.
Q_xu = -u**5 / 5 + sp.Rational(3, 4) * rho * u**4 - rho**2 * u**3 \
    + rho**3 * u**2 / 2 + sp.symbols("d")
R_xu = H**10 * Q_xu
jac_xu = sp.factor(sp.diff(R_xu, x) * sp.diff(G, y)
                   - sp.diff(R_xu, y) * sp.diff(G, x))
assert sp.expand(jac_xu + 9 * x * H**22) == 0


def inverse_omega_face_check(expr: sp.Expr, old_degree: int) -> dict[str, int]:
    """Apply (e,j) -> X^(j-e)[X^2(Y-a0)-a1X-a2]^j termwise."""
    terms = sp.Poly(sp.expand(expr), x, y).terms()
    exponents = [(monomial[0], monomial[1]) for monomial, coeff in terms
                 if coeff != 0]
    assert all(j - e >= 0 and 4 * j - e <= old_degree for e, j in exponents)
    return {
        "support_terms": len(exponents),
        "minimum_outer_X_exponent_j_minus_e": min(j - e for e, j in exponents),
        "maximum_old_total_degree_4j_minus_e": max(4 * j - e for e, j in exponents),
    }


inverse_checks = {
    "H_degree_11": inverse_omega_face_check(H, 11),
    "F_degree_66": inverse_omega_face_check(F, 66),
    "G_degree_99": inverse_omega_face_check(G, 99),
    "T2_degree_55": inverse_omega_face_check(T2, 55),
    "R_degree_145": inverse_omega_face_check(R, 145),
}

out = {
    "scope": "LEADING-FACE-ONLY",
    "verdict": "SURVIVES[DELTA-5/2-LEADING-FACE]",
    "parity_band": {
        "unknowns": 3,
        "raw_equations": len(parity_rows),
        "independent_pivots": [str(v) for v in parity_pivots],
        "dimension": 1,
        "solution": "A=C=0, B=-rho; saturate rho",
        "generator_order": [str(v) for v in parity_variables],
        "wrapped_reduced_basis": [str(v.as_expr()) for v in parity_gb.polys],
        "extracted_component_Q[A,B,C]": ["A", "C"],
        "main_wrapped_unit": parity_gb.contains(sp.Integer(1)),
        "wrapper_only_unit": parity_wrapper_only.contains(sp.Integer(1)),
        "unsaturated_unit": parity_unsaturated.contains(sp.Integer(1)),
        "negative_control_B_unit": parity_negative.contains(sp.Integer(1)),
        "positive_witness": "A=C=0, B=-1, U=-1",
    },
    "ode_band_monic_gauge": {
        "unknowns_excluding_wrapper": 12,
        "raw_equations_after_q=p^10*q1": len(ode_rows),
        "raw_equations_before_cancelling_p^11": 43,
        "dimension": 2,
        "free_parameters": ["rho (nonzero)", "b0"],
        "generator_order": [str(v) for v in variables],
        "coefficient_rows_descending_z_degree": [str(v) for v in ode_rows],
        "wrapped_reduced_basis": [str(v.as_expr()) for v in main_gb.polys],
        "extracted_component_Q[b1,...,b9,k,b0,rho]": [
            str(v.as_expr()) for v in main_gb.polys
            if not v.as_expr().has(T)
        ],
        "solution": str(q1_solution),
        "resultant_p_q1": str(quotient_resultant),
        "generic_coprime_open": "b0*(4*b0-rho^5) != 0 (optional; not needed for face survival)",
        "main_wrapped_unit": main_gb.contains(sp.Integer(1)),
        "wrapper_only_unit": wrapper_only.contains(sp.Integer(1)),
        "unsaturated_unit": unsaturated.contains(sp.Integer(1)),
        "negative_control_rho_unit": control_rho.contains(sp.Integer(1)),
        "negative_control_k_unit": control_k.contains(sp.Integer(1)),
        "positive_witness": "rho=1, b0=1, k=10, T=1/10 and displayed pivots",
    },
    "faces": {
        "H": str(H),
        "F": str(F),
        "G": str(G),
        "T2": str(T2),
        "R": str(R),
        "jacobian_F_G": str(jac_F_G),
        "jacobian_R_G": str(jac),
        "xu_normalization_jacobian_R_G": str(jac_xu),
        "inverse_omega_termwise_checks": inverse_checks,
    },
}
print(json.dumps(out, indent=2, sort_keys=True))
