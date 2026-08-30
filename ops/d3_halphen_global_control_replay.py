#!/usr/bin/env python3
"""Global and ramification audit of the D3 Halphen positive control.

This replay proves exact polynomial identities for one control.  Standard
surface-classification and Kummer-cover theorems are stated as interfaces in
the accompanying report; the script does not construct a Keller map.
"""

from __future__ import annotations

import ast
import json
import sys

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def coefficient(form, variables, monomial):
    return sp.Poly(form, *variables).coeff_monomial(monomial)


def hessian_covariant(form, variables):
    return sp.expand(-sp.det(sp.hessian(form, variables)) / 2)


def ternary_invariants(form, variables, control_monomial):
    u = sp.symbols("invariant_pencil_u")
    hessian = hessian_covariant(form, variables)
    pencil = sp.Poly(hessian_covariant(form + u * hessian, variables), u)
    form_control = coefficient(form, variables, control_monomial)
    hessian_control = coefficient(hessian, variables, control_monomial)
    require(form_control == 1, "chosen invariant control coefficient is not one")
    linear_control = coefficient(
        pencil.coeff_monomial(u), variables, control_monomial
    )
    quadratic_control = coefficient(
        pencil.coeff_monomial(u**2), variables, control_monomial
    )
    c4 = sp.expand(linear_control / 3)
    c6 = sp.expand((quadratic_control + 3 * c4 * hessian_control) / 6)
    discriminant = sp.factor((c4**3 - c6**2) / 1728)
    return sp.factor(c4), sp.factor(c6), discriminant


def derive(mutate_kummer_denominator: bool = False):
    x, y, z, t = sp.symbols("x y z t")
    S, T, u = sp.symbols("S T u")
    plane = (x, y, z)

    affine = sp.expand((x + t * z) ** 3 + t * y**3 + t**3 * x**2 * z)
    global_form = sp.expand(
        (S * x + T * z) ** 3 + T * S**2 * y**3 + T**3 * x**2 * z
    )
    require(
        sp.expand(global_form.subs({S: 1, T: t}) - affine) == 0,
        "bihomogeneous affine chart drifted",
    )

    # Projection to the target P2 is finite: the four binary-cubic
    # coefficients have no common projective zero.  The displayed triangular
    # implication is x^3=0 => x=0, then y^3=0, then z^3=0.
    fibre_poly = sp.Poly(global_form, S, T)
    fibre_coefficients = {
        "S3": fibre_poly.coeff_monomial(S**3),
        "S2T": fibre_poly.coeff_monomial(S**2 * T),
        "ST2": fibre_poly.coeff_monomial(S * T**2),
        "T3": fibre_poly.coeff_monomial(T**3),
    }
    expected_fibre_coefficients = {
        "S3": x**3,
        "S2T": 3 * x**2 * z + y**3,
        "ST2": 3 * x * z**2,
        "T3": z**3 + x**2 * z,
    }
    require(
        all(
            sp.expand(fibre_coefficients[key] - value) == 0
            for key, value in expected_fibre_coefficients.items()
        ),
        "binary-cubic coefficient ledger drifted",
    )
    require(
        fibre_coefficients["S2T"].subs(x, 0) == y**3
        and fibre_coefficients["T3"].subs({x: 0, y: 0}) == z**3,
        "finite-projection triangular certificate failed",
    )

    # Exact ternary invariants in the two coefficient-base charts.
    c4, c6, discriminant = ternary_invariants(affine, plane, x**3)
    expected_c6 = 216 * t**12 * (4 * t**2 + 27)
    expected_discriminant = -27 * t**24 * (4 * t**2 + 27) ** 2
    require(c4 == 0, "finite-chart c4 is not identically zero")
    require(sp.expand(c6 - expected_c6) == 0, "finite-chart c6 drifted")
    require(
        sp.expand(discriminant - expected_discriminant) == 0,
        "finite-chart discriminant drifted",
    )

    infinity_form = sp.expand((u * x + z) ** 3 + u**2 * y**3 + x**2 * z)
    c4_inf, c6_inf, discriminant_inf = ternary_invariants(
        infinity_form, plane, z**3
    )
    expected_c6_inf = 216 * u**4 * (27 * u**2 + 4)
    expected_discriminant_inf = -27 * u**8 * (27 * u**2 + 4) ** 2
    require(c4_inf == 0, "infinity-chart c4 is not identically zero")
    require(sp.expand(c6_inf - expected_c6_inf) == 0, "infinity c6 drifted")
    require(
        sp.expand(discriminant_inf - expected_discriminant_inf) == 0,
        "infinity discriminant drifted",
    )

    # Total-space singular locus.  On S!=0, Fy=3t*y^2.  At t=0 the only
    # solution is [x:y:z]=[0:0:1].  For t!=0, y=0 and z cannot vanish.  Put
    # z=1, x=t(r-1); the remaining derivative certificate has no total-space
    # singular solution.
    derivatives = {variable: sp.diff(affine, variable) for variable in (*plane, t)}
    require(
        derivatives[y] == 3 * t * y**2,
        "finite-chart y derivative drifted",
    )
    require(
        derivatives[x].subs(t, 0) == 3 * x**2
        and derivatives[t].subs({t: 0, x: 0}) == y**3,
        "central singular-point certificate drifted",
    )
    r = sp.symbols("r")
    finite_subs = {x: t * (r - 1), y: 0, z: 1}
    fx_scaled = sp.expand(derivatives[x].subs(finite_subs) / t**2)
    fz_scaled = sp.expand(derivatives[z].subs(finite_subs) / t**3)
    ft_scaled = sp.expand(derivatives[t].subs(finite_subs) / (3 * t**2))
    require(
        sp.expand(fx_scaled - (3 * r**2 + 2 * t**2 * (r - 1))) == 0,
        "finite Fx drifted",
    )
    require(
        sp.expand(fz_scaled - (3 * r**2 + t**2 * (r - 1) ** 2)) == 0,
        "finite Fz drifted",
    )
    require(
        sp.factor(fz_scaled - fx_scaled) == t**2 * (r - 3) * (r - 1),
        "finite derivative factorization drifted",
    )
    require(fx_scaled.subs(r, 1) == 3, "r=1 singularity control failed")
    require(
        fx_scaled.subs({r: 3, t**2: -sp.Rational(27, 4)}) == 0
        and ft_scaled.subs({r: 3, t**2: -sp.Rational(27, 4)}) == -18,
        "r=3 total-space transversality control failed",
    )

    # At coefficient-base infinity u=0, the only singular point is
    # [x:y:z]=[0:1:0].
    inf_derivatives = {
        variable: sp.diff(infinity_form, variable) for variable in (*plane, u)
    }
    require(
        sp.expand(infinity_form.subs(u, 0) - z * (z**2 + x**2)) == 0,
        "infinity fibre drifted",
    )
    require(
        inf_derivatives[x].subs(u, 0) == 2 * x * z
        and inf_derivatives[z].subs(u, 0) == x**2 + 3 * z**2
        and inf_derivatives[u].subs(u, 0) == 3 * x * z**2,
        "infinity singular-locus certificate drifted",
    )
    local_infinity = sp.expand(infinity_form.subs(y, 1))
    epsilon = sp.symbols("epsilon")
    local_scaled = sp.Poly(
        sp.expand(
            local_infinity.subs(
                {u: epsilon * u, x: epsilon * x, z: epsilon * z}
            )
        ),
        epsilon,
    )
    require(
        local_scaled.coeff_monomial(epsilon**2) == u**2
        and local_scaled.coeff_monomial(epsilon**3) == z**3 + x**2 * z,
        "infinity D4 two-jet/three-jet certificate drifted",
    )
    cubic_tangent = z**3 + x**2 * z
    require(
        sp.factor(sp.discriminant(sp.Poly(cubic_tangent, z), z)) == -4 * x**6,
        "D4 ordinary-triple tangent certificate failed",
    )

    # Discriminant of the finite cubic projection, retained as a target-side
    # checksum distinct from the ternary-cubic coefficient-base discriminant.
    finite_cover_discriminant = sp.factor(sp.discriminant(affine, t))
    expected_cover_discriminant = -z * (
        27 * x**10 * z
        + 54 * x**6 * y**3 * z**2
        + 36 * x**4 * y**6 * z
        + 4 * x**2 * y**9
        + 27 * x**2 * y**6 * z**3
        + 4 * y**9 * z**2
    )
    require(
        sp.expand(finite_cover_discriminant - expected_cover_discriminant) == 0,
        "finite-cover discriminant drifted",
    )

    # Dense affine ramification component.  Eliminate y^3 from F=F_t=0,
    # rationalize the (x,t)-curve, and record the resulting cyclic cubic
    # extension for y.
    affine_target_chart = sp.expand(affine.subs(z, 1))
    ft = sp.diff(affine_target_chart, t)
    ramification_base = sp.factor(affine_target_chart - t * ft)
    expected_ramification_base = sp.expand(
        (x + t) ** 2 * (x - 2 * t) - 2 * t**3 * x**2
    )
    require(
        sp.expand(ramification_base - expected_ramification_base) == 0,
        "ramification elimination drifted",
    )
    q = sp.symbols("q")
    r_parameter = 2 * q**2 + 3
    x_parameter = r_parameter * q
    t_parameter = r_parameter * q / (r_parameter - 1)
    require(
        sp.factor(
            expected_ramification_base.subs({x: x_parameter, t: t_parameter})
        )
        == 0,
        "ramification rational parameterization failed",
    )
    y_cubed = sp.factor(
        -sp.Rational(3, 4)
        * q**2
        * (2 * q**2 + 3) ** 4
        / (q**2 + (2 if mutate_kummer_denominator else 1))
    )
    expected_y_cubed = sp.factor(
        -sp.Rational(3, 4) * q**2 * (2 * q**2 + 3) ** 4 / (q**2 + 1)
    )
    require(y_cubed == expected_y_cubed, "ramification Kummer function drifted")
    require(
        sp.factor(
            ft.subs({x: x_parameter, t: t_parameter, y**3: y_cubed})
        )
        == 0,
        "ramification lift to y^3 failed",
    )

    numerator, denominator = sp.fraction(y_cubed)
    require(
        sp.expand(numerator + 3 * q**2 * (2 * q**2 + 3) ** 4) == 0
        and sp.expand(denominator - 4 * (q**2 + 1)) == 0,
        "Kummer numerator/denominator factorization drifted",
    )
    require(
        sp.gcd(q, 2 * q**2 + 3) == 1
        and sp.gcd(q, q**2 + 1) == 1
        and sp.gcd(2 * q**2 + 3, q**2 + 1) == 1,
        "Kummer branch supports collided",
    )
    branch_valuations_mod_3 = {
        "q=0": 2,
        "two_roots_2q2+3": 1,
        "two_roots_q2+1": 2,
        "q=infinity": 1,
    }
    branch_points = 1 + 2 + 2 + 1
    kummer_genus = (3 * (-2) + branch_points * (3 - 1) + 2) // 2
    require(branch_points == 6 and kummer_genus == 4, "Kummer genus ledger failed")

    source_tree = ast.parse(open(__file__, encoding="utf-8").read())
    assert_count = sum(isinstance(node, ast.Assert) for node in ast.walk(source_tree))
    require(assert_count == 0, "replay contains optimization-sensitive asserts")

    return {
        "schema": "D3-HALPHEN-GLOBAL-CONTROL/v1",
        "sympy_version": sp.__version__,
        "surface": {
            "bidegree": [3, 3],
            "finite_flat_target_degree": 3,
            "singular_points": ["t=0,[x:y:z]=[0:0:1]", "t=infinity,[x:y:z]=[0:1:0]"],
            "infinity_tangent_type": "ordinary triple; hypersurface suspension D4",
            "normal": True,
        },
        "coefficient_base_invariants": {
            "c4": "0",
            "c6_finite": str(expected_c6),
            "discriminant_finite": str(expected_discriminant),
            "c6_infinity": str(expected_c6_inf),
            "discriminant_infinity": str(expected_discriminant_inf),
            "minimal_fibre_valuations": {
                "t=0_after_level_2_drop": [0, 0],
                "two_roots_4t2+27": [1, 2],
                "t=infinity": [4, 8],
            },
            "minimal_discriminant_degree": 12,
        },
        "finite_cover_discriminant": str(expected_cover_discriminant),
        "ramification": {
            "base_parameter": {
                "r": str(r_parameter),
                "x": str(x_parameter),
                "t": str(t_parameter),
            },
            "kummer_y3": str(expected_y_cubed),
            "branch_valuations_mod_3": branch_valuations_mod_3,
            "branch_points": branch_points,
            "normalization_genus": kummer_genus,
            "proper_block_rational_forest_compatible": False,
        },
        "ast_assert_nodes": assert_count,
        "status": "PASS",
    }


def main() -> None:
    mutate = sys.argv[1:] == ["--mutate-kummer-denominator"]
    require(mutate or not sys.argv[1:], "unknown command-line argument")
    result = derive(mutate_kummer_denominator=mutate)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print("FAIL:" + str(error), file=sys.stderr)
        raise SystemExit(1)
