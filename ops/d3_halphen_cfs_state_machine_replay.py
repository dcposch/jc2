#!/usr/bin/env python3
"""Exact CFS state-machine replay for the D3 Halphen level-two row.

The replay keeps the raw coefficient-base degree-three model.  It certifies
necessary local conditions and a local positive control; it does not construct
a global (3,3) surface or a polynomial map.
"""

from __future__ import annotations

import ast
import json
import sys

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def t_coefficient(form, t, degree: int):
    return sp.expand(form).coeff(t, degree)


def line_move(form, t, variable):
    """CFS line move for the singular line variable=0."""
    return sp.expand(form.subs(variable, t * variable) / t)


def valuation(poly, t) -> int | None:
    expanded = sp.Poly(sp.expand(poly), t)
    if expanded.is_zero:
        return None
    return min(monomial[0] for monomial, _ in expanded.terms())


def derive(mutate_cycle_scale: bool = False):
    x, y, z, t = sp.symbols("x y z t")
    X, Y = sp.symbols("X Y")
    a, ell, m = sp.symbols("a ell m")
    q0, q1, q2 = sp.symbols("q0 q1 q2")
    A, B, C2, P, T = sp.symbols("A B C2 P T")
    V, M111, R, Q021, U = sp.symbols("V M111 R Q021 U")
    A3, B3, C3, P3, T3 = sp.symbols("A3 B3 C3 P3 T3")
    V3, M3, R3, Q3, U3 = sp.symbols("V3 M3 R3 Q3 U3")
    s, lam = sp.symbols("s lam")

    f2 = (
        A * x**3
        + B * y**3
        + C2 * z**3
        + P * x**2 * y
        + T * x * y**2
        + V * x**2 * z
        + M111 * x * y * z
        + R * x * z**2
        + Q021 * y**2 * z
        + U * y * z**2
    )
    f3 = (
        A3 * x**3
        + B3 * y**3
        + C3 * z**3
        + P3 * x**2 * y
        + T3 * x * y**2
        + V3 * x**2 * z
        + M3 * x * y * z
        + R3 * x * z**2
        + Q3 * y**2 * z
        + U3 * y * z**2
    )

    def raw_model(transverse_cubic):
        f1 = (
            a * x**3
            + ell * x**2 * y
            + m * x**2 * z
            + x * (q0 * y**2 + q1 * y * z + q2 * z**2)
            + transverse_cubic
        )
        return sp.expand(x**3 + t * f1 + t**2 * f2 + t**3 * f3)

    triple = raw_model(y**3)
    double = raw_model(y**2 * z)

    # The first two singular lines are x=0 and y=0.  Their composite is the
    # raw diagonal transform t^-2 F(tx,ty,z).
    e1_triple = line_move(triple, t, x)
    e1_double = line_move(double, t, x)
    require(t_coefficient(e1_triple, t, 0) == y**3, "first triple-root line move drifted")
    require(t_coefficient(e1_double, t, 0) == y**2 * z, "first double-root line move drifted")
    e2_triple = line_move(e1_triple, t, y)
    e2_double = line_move(e1_double, t, y)
    expected_e2_central = z**2 * (q2 * x + C2 * z)
    require(
        sp.expand(t_coefficient(e2_triple, t, 0) - expected_e2_central) == 0,
        "triple-root second central form drifted",
    )
    require(
        sp.expand(t_coefficient(e2_double, t, 0) - expected_e2_central) == 0,
        "double-root second central form drifted",
    )

    # If this central form is nonzero, its singular line is z=0 and the third
    # line move returns the original homogeneous cubic exactly.
    cycle_scale = t**2 if mutate_cycle_scale else t
    cycled = sp.expand(e2_triple.subs(z, t * z) / cycle_scale)
    require(sp.expand(cycled - triple) == 0, "three-line CFS cycle identity failed")

    # On the double-root first-jet branch q2=0.  Avoiding the cycle forces
    # C2=0, after which division by t is the drop on this fixed forced path.
    md = sp.expand((e2_double / t).subs({q2: 0, C2: 0}))
    md0 = t_coefficient(md, t, 0)
    expected_md0 = (
        x**3
        + m * x**2 * z
        + q1 * x * y * z
        + y**2 * z
        + R * x * z**2
        + U * y * z**2
        + C3 * z**3
    )
    require(sp.expand(md0 - expected_md0) == 0, "double-root lowered reduction drifted")
    alpha, beta = sp.symbols("alpha beta")
    normalized_cube = sp.expand((x + alpha * y + beta * z) ** 3)
    cube_x2y = sp.Poly(normalized_cube, x, y, z).coeff_monomial(x**2 * y)
    cube_y2z_after_x2y_zero = sp.Poly(
        normalized_cube.subs(alpha, 0), x, y, z
    ).coeff_monomial(y**2 * z)
    require(cube_x2y == 3 * alpha, "normalized cube x2y coefficient drifted")
    require(
        cube_y2z_after_x2y_zero == 0,
        "double-root cube obstruction disappeared",
    )

    # On the triple-root branch, avoiding the cycle forces q2=C2=0.  A
    # minimal strictly-henselian-insoluble lowered model must reduce to a cube.
    mt = sp.expand((e2_triple / t).subs({q2: 0, C2: 0, m: 3 * s}))
    mt0 = t_coefficient(mt, t, 0)
    expected_mt0 = x**3 + 3 * s * x**2 * z + q1 * x * y * z + R * x * z**2 + U * y * z**2 + C3 * z**3
    require(sp.expand(mt0 - expected_mt0) == 0, "triple-root lowered reduction drifted")
    cube_conditions = {q1: 0, U: 0, R: 3 * s**2, C3: s**3}
    require(
        sp.expand(mt0.subs(cube_conditions) - (x + s * z) ** 3) == 0,
        "first lowered cube equations failed",
    )

    # Follow the two critical flags from M0=(x+s z)^3.  Work in raw degree
    # three coefficients; parameter-dependent first-jet gauges would otherwise
    # manufacture misleading higher t-coefficients.
    mt = sp.expand(mt.subs(cube_conditions))
    n1 = line_move(sp.expand(mt.subs(x, X - s * z)), t, X)
    n10 = t_coefficient(n1, t, 0)
    b = Q021 - s * q0
    c = U3 + s**2 * ell - s * M111
    d = -s**3 * a + s**2 * V - s * R3
    expected_n10 = y**3 + b * y**2 * z + c * y * z**2 + d * z**3
    require(sp.expand(n10 - expected_n10) == 0, "first transverse cubic drifted")

    e_cube_1 = sp.expand(3 * c - b**2)
    e_cube_2 = sp.expand(27 * d - b**3)
    lam_value = b / 3
    shifted_n10 = sp.expand(n10.subs(y, Y - lam_value * z))
    expected_shifted = sp.expand(
        Y**3
        + (e_cube_1 / 3) * Y * z**2
        + (e_cube_2 / 27 - b * e_cube_1 / 9) * z**3
    )
    require(
        sp.expand(shifted_n10 - expected_shifted) == 0,
        "first transverse cube equations failed",
    )

    # Impose the first transverse cube equations without dividing by s.
    u3_solution = sp.expand(b**2 / 3 - s**2 * ell + s * M111)
    # e_cube_2 is linear in a.  Solving for a is valid on the s!=0 chart;
    # s=0 is separately ruled out below by the final nonzero condition.
    a_solution = sp.expand((s**2 * V - s * R3 - b**3 / 27) / s**3)
    critical_subs = {lam: lam_value, U3: u3_solution, a: a_solution}
    n1_shifted = sp.expand(n1.subs(y, Y - lam * z).subs(critical_subs))
    n2 = line_move(n1_shifted, t, Y)
    n20 = t_coefficient(n2, t, 0)
    kappa = sp.expand(
        3 * a * s**2
        + 2 * ell * s * lam_value
        + q0 * lam_value**2
        - 2 * V * s
        - M111 * lam_value
        + R3
    )
    eta = sp.expand(
        -A * s**3
        - P * s**2 * lam_value
        - T * s * lam_value**2
        - B * lam_value**3
        + V3 * s**2
        + M3 * s * lam_value
        + Q3 * lam_value**2
    )
    expected_n20 = sp.expand(
        (kappa * X + eta * z).subs({a: a_solution}) * z**2
    )
    require(sp.expand(n20 - expected_n20) == 0, "second critical-flag form drifted")

    # If s=0, the first cube equations give b=lam=0, and the final cube
    # conditions kappa=0, eta!=0 are inconsistent: eta specializes to zero.
    require(
        sp.expand(eta.subs({s: 0, Q021: 0})) == 0,
        "s=0 obstruction drifted",
    )

    # Exact positive control.  It is local only.
    positive = sp.expand((x + t * z) ** 3 + t * y**3 + t**3 * x**2 * z)
    positive_m = sp.expand(positive.subs({x: t * x, y: t * y}) / t**3)
    expected_positive_m = (x + z) ** 3 + t * y**3 + t**2 * x**2 * z
    require(sp.expand(positive_m - expected_positive_m) == 0, "positive-control drop drifted")
    positive_critical = sp.expand(positive_m.subs(x, X - z))
    expected_positive_critical = X**3 + t * y**3 + t**2 * (X - z) ** 2 * z
    require(
        sp.expand(positive_critical - expected_positive_critical) == 0,
        "positive-control critical coordinates drifted",
    )
    monomials = {
        "X3": X**3,
        "X2Y": X**2 * y,
        "XY2": X * y**2,
        "Y3": y**3,
        "X2Z": X**2 * z,
        "XYZ": X * y * z,
        "Y2Z": y**2 * z,
        "XZ2": X * z**2,
        "YZ2": y * z**2,
        "Z3": z**3,
    }
    critical_poly = sp.Poly(positive_critical, X, y, z)
    critical_vals = {
        name: valuation(critical_poly.coeff_monomial(monomial), t)
        for name, monomial in monomials.items()
    }
    expected_vals = {
        "X3": 0,
        "X2Y": None,
        "XY2": None,
        "Y3": 1,
        "X2Z": 2,
        "XYZ": None,
        "Y2Z": None,
        "XZ2": 2,
        "YZ2": None,
        "Z3": 2,
    }
    require(critical_vals == expected_vals, "positive control is not CFS-critical")
    ft_central_line = sp.diff(positive, t).subs({t: 0, x: 0})
    require(ft_central_line == y**3, "positive-control generic central regularity failed")

    # Generic smoothness: Fy forces y=0.  At z=0, Fx is nonzero at every
    # projective point.  At z=1 put x=t(r-1); the two remaining derivatives
    # can vanish only for r=1 or r=3, and neither candidate works.
    r = sp.symbols("r")
    fx = sp.diff(positive, x).subs({x: t * (r - 1), y: 0, z: 1}) / t**2
    fz = sp.diff(positive, z).subs({x: t * (r - 1), y: 0, z: 1}) / t**3
    require(sp.expand(fx - (3 * r**2 + 2 * t**2 * (r - 1))) == 0, "positive Fx certificate drifted")
    require(sp.expand(fz - (3 * r**2 + t**2 * (r - 1) ** 2)) == 0, "positive Fz certificate drifted")
    require(
        sp.factor(fz - fx) == t**2 * (r - 3) * (r - 1),
        "positive derivative candidate factorization drifted",
    )
    require(fx.subs(r, 1) != 0 and fx.subs(r, 3) != 0, "positive control became singular")

    source_tree = ast.parse(open(__file__, encoding="utf-8").read())
    assert_count = sum(isinstance(node, ast.Assert) for node in ast.walk(source_tree))
    require(assert_count == 0, "replay contains optimization-sensitive asserts")

    return {
        "schema": "D3-HALPHEN-CFS-STATE/v1",
        "sympy_version": sp.__version__,
        "raw_base_degree": 3,
        "forced_moves": ["L_x", "L_y"],
        "second_central_form": str(expected_e2_central),
        "nonzero_second_form_transition": "L_z exact three-cycle",
        "double_root": {
            "conditions_before_drop": ["q2=0", "C2=0"],
            "lowered_reduction": str(expected_md0),
            "status": "ELIMINATED_NOT_A_CUBE",
        },
        "triple_root": {
            "conditions_before_drop": ["q2=0", "C2=0"],
            "first_cube": ["q1=0", "U=0", "R=3*s^2", "C3=s^3"],
            "first_transverse": str(expected_n10),
            "first_transverse_cube": ["3*c=b^2", "27*d=b^3"],
            "final_reduction": "(kappa*X+eta*z)*z^2",
            "critical_open": ["kappa=0", "eta!=0"],
            "s_nonzero": True,
            "normalized_first_jet_shards": ["Q=0", "Q=y^2"],
        },
        "positive_control": {
            "raw": "(x+t*z)^3+t*y^3+t^3*x^2*z",
            "lowered": "(x+z)^3+t*y^3+t^2*x^2*z",
            "critical_valuations": critical_vals,
            "normal_at_generic_central_line": True,
            "generic_cubic_smooth": True,
            "scope": "local_only",
        },
        "ast_assert_nodes": assert_count,
        "status": "PASS",
    }


def main() -> None:
    mutate = sys.argv[1:] == ["--mutate-cycle-scale"]
    require(mutate or not sys.argv[1:], "unknown command-line argument")
    result = derive(mutate_cycle_scale=mutate)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print("FAIL:" + str(error), file=sys.stderr)
        raise SystemExit(1)
