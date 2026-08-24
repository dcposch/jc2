#!/usr/bin/env python3
"""Exact symbolic replay for the GCD3-(6,9) cube trajectory gate.

The script independently rebuilds the five Laurent invariants from the Faber
normal form, checks their weighted principal parts, the common/DS balances,
the double-root cubic obstruction, the mixed later-target cusp, and the
source-level reconstructions used in the report.  Elimination, localization,
and saturation certificates are in the companion Singular script.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def coeff(expr: sp.Expr, var: sp.Symbol, power: int) -> sp.Expr:
    return sp.Poly(sp.expand(expr), var).coeff_monomial(var**power)


def potential_from_gradient(
    variables: list[sp.Symbol], gradients: list[sp.Expr]
) -> sp.Expr:
    potential = sp.Integer(0)
    for variable, gradient in zip(variables, gradients):
        remainder = sp.expand(gradient - sp.diff(potential, variable))
        potential = sp.expand(potential + sp.integrate(remainder, variable))
    assert all(
        sp.expand(sp.diff(potential, variable) - gradient) == 0
        for variable, gradient in zip(variables, gradients)
    )
    return sp.factor(potential)


def polynomial_part_at_infinity(
    expr: sp.Expr, u: sp.Symbol, z: sp.Symbol
) -> sp.Expr:
    truncated = sp.series(expr, u, 0, 1).removeO()
    kept = sum(
        term
        for term in sp.Add.make_args(sp.expand(truncated))
        if term.as_powers_dict().get(u, 0) <= 0
    )
    return sp.expand(kept.subs(u, 1 / z))


def build_invariants() -> tuple[
    list[sp.Expr], tuple[sp.Symbol, ...], sp.Symbol, tuple[sp.Symbol, ...], sp.Symbol
]:
    z, u = sp.symbols("z u")
    d = sp.symbols("d")
    avec = sp.symbols("a0:5")
    cvec = sp.symbols("c0:8")
    vavec = sp.symbols("va0:5")
    a0, a1, a2, a3, a4 = avec

    f = z**6 + a4 * z**4 + a3 * z**3 + a2 * z**2 + a1 * z + a0
    f_velocity = sum(vavec[i] * z**i for i in range(5))

    U = a4 * u**2 + a3 * u**3 + a2 * u**4 + a1 * u**5 + a0 * u**6
    w_series = u**-1 * sp.series(
        (1 + U) ** sp.Rational(1, 6), u, 0, 18
    ).removeO()
    F = [polynomial_part_at_infinity(w_series**j, u, z) for j in range(10)]
    assert F[6] == f

    g = sp.expand(F[9] + d * F[8] + sum(cvec[j] * F[j] for j in range(8)))
    # c6 and c0 are the already-removed target gauges.
    g = sp.expand(g.subs({cvec[6]: 0, cvec[0]: 0}))
    g_velocity = sum(sp.diff(g, avec[i]) * vavec[i] for i in range(5))
    bracket = sp.Poly(
        sp.expand(f_velocity * sp.diff(g, z) - sp.diff(f, z) * g_velocity), z
    )
    rows = sp.Matrix(
        [sp.expand(bracket.coeff_monomial(z**power)) for power in range(4, -1, -1)]
    )

    fz_u = sp.diff(f, z).subs(z, 1 / u)
    A: list[sp.Expr] = []
    for n in range(1, 6):
        wn = u**n * sp.series(
            (1 + U) ** (-sp.Rational(n, 6)), u, 0, 7
        ).removeO()
        A.append(polynomial_part_at_infinity(sp.expand(fz_u * wn), u, z))
    expected_A = [
        6 * z**4 + 3 * a4 * z**2 + 2 * a3 * z + a2 - a4**2 / 12,
        6 * z**3 + 2 * a4 * z + a3,
        6 * z**2 + a4,
        6 * z,
        6,
    ]
    assert A == expected_A
    matrix = sp.Matrix(
        [[coeff(A[n], z, power) for n in range(5)] for power in range(4, -1, -1)]
    )
    assert matrix.det() == 6**5

    r_velocity = matrix.inv() * rows
    variable_order = [a4, a3, a2, a1, a0]
    r: list[sp.Expr] = []
    for form in r_velocity:
        gradients = [sp.expand(form).coeff(vavec[i]) for i in range(5)]
        potential = potential_from_gradient(
            variable_order,
            [gradients[4], gradients[3], gradients[2], gradients[1], gradients[0]],
        )
        assert sp.expand(
            form - sum(sp.diff(potential, avec[i]) * vavec[i] for i in range(5))
        ) == 0
        r.append(potential)

    return r, avec, d, cvec, z


def main() -> None:
    r, avec, d, c, z = build_invariants()
    a0, a1, a2, a3, a4 = avec

    weights = {a0: 6, a1: 5, a2: 4, a3: 3, a4: 2, d: 1}
    weights.update({c[7]: 2, c[5]: 4, c[4]: 5, c[3]: 6, c[2]: 7, c[1]: 8})
    scale = sp.symbols("scale")
    scaling = {var: var * scale**weight for var, weight in weights.items()}
    for n, invariant in enumerate(r, 1):
        assert sp.expand(
            invariant.subs(scaling, simultaneous=True) - scale ** (9 + n) * invariant
        ) == 0

    zero_high = {d: 0, **{c[j]: 0 for j in range(8)}}
    r0 = [sp.factor(item.subs(zero_high)) for item in r]

    # The two weighted leading components.
    lam = sp.symbols("lam")
    ds = {a4: 4 * lam, a3: 0, a2: 10 * lam**2, a1: 0, a0: 6 * lam**3}
    assert [sp.factor(item.subs(ds)) for item in r0] == [
        0,
        0,
        0,
        0,
        sp.Rational(27, 2) * lam**7,
    ]

    u, v, X, Y, Z, h = sp.symbols("u v X Y Z h")
    common = {a4: 2 * u, a3: 2 * v, a2: u**2, a1: 2 * u * v, a0: v**2}
    assert [sp.factor(item.subs(common)) for item in r0] == [0, 0, 0, 0, 0]

    normal = {
        a4: 2 * u,
        a3: 2 * v,
        a2: u**2 + h * X,
        a1: 2 * u * v + h * Y,
        a0: v**2 + h * Z,
    }
    q = [sp.factor(sp.expand(item.subs(normal)).coeff(h, 2)) for item in r0]
    q_expected = [
        -(729 * u * X**2 - 1458 * X * Z - 729 * Y**2) / 1944,
        (-2187 * v * X**2 - 4374 * u * X * Y + 4374 * Y * Z) / 5832,
        (2 * u**2 * X**2 - 6 * v * X * Y - 4 * u * X * Z - 2 * u * Y**2 + 3 * Z**2) / 8,
        (
            19683 * u * v * X**2
            + 13122 * u**2 * X * Y
            - 26244 * v * X * Z
            - 13122 * v * Y**2
            - 13122 * u * Y * Z
        )
        / 52488,
        (
            -729 * u**3 * X**2
            + 2187 * v**2 * X**2
            + 4374 * u * v * X * Y
            + 1458 * u**2 * X * Z
            + 729 * u**2 * Y**2
            - 4374 * v * Y * Z
        )
        / 17496,
    ]
    assert all(sp.expand(q[i] - q_expected[i]) == 0 for i in range(5))
    assert all(sp.expand(item.subs(normal)).coeff(h, 1) == 0 for item in r0)

    # The pole-order and polynomial-degree audit is finite.  A tuple records
    # the weights of the nonzero leading coefficients on each projective
    # support orbit (u contributes a4 of degree 2p; v contributes a3 of
    # degree 3p).  The rho2 axis is the unique integral leading exception and
    # is killed by its three fractional normal-correction degrees below.
    constant_supports: dict[str, tuple[int, list[tuple[int, ...]]]] = {
        "DS": (0, [(2,)]),
        "d": (1, [(2, 3)]),
        "c7": (2, [(2,), (3,), (2, 3)]),
        "c5": (4, [(2,), (2, 3)]),
        "c4": (5, [(3,), (2, 3)]),
        "c2": (7, [(2, 3)]),
        "c1": (8, [(2,), (3,)]),
        "rho1": (10, [(2,)]),
    }
    for row_name, (row_weight, supports) in constant_supports.items():
        pole_exponent = Fraction(1, 14 - row_weight)
        assert all(
            any((coefficient_weight * pole_exponent).denominator != 1 for coefficient_weight in support)
            for support in supports
        ), row_name
    rho2_p = Fraction(1, 3)
    assert 3 * rho2_p == 1
    rho2_correction_degrees = [
        4 * rho2_p - Fraction(11, 2) * rho2_p,
        5 * rho2_p - Fraction(11, 2) * rho2_p,
        6 * rho2_p - Fraction(11, 2) * rho2_p,
    ]
    assert rho2_correction_degrees == [Fraction(-1, 2), Fraction(-1, 6), Fraction(1, 6)]
    assert all(item.denominator != 1 for item in rho2_correction_degrees)

    boundary_weights = [1, 2, 4, 5, 7, 8, 10, 11]
    assert all(Fraction(12, row_weight) > 1 for row_weight in boundary_weights)
    assert all(Fraction(18, row_weight) > Fraction(3, 2) for row_weight in boundary_weights)
    assert Fraction(12, 12) == 1 and Fraction(18, 12) == Fraction(3, 2)

    # d != 0: normal=sqrt(epsilon), d=epsilon.  These are the exact four
    # Kuranishi quadrics and terminal coefficient used by Singular.
    D = sp.symbols("D")
    d_sub = {**normal, d: h**2 * D, **{c[j]: 0 for j in range(8)}}
    d_q = [sp.factor(sp.expand(item.subs(d_sub)).coeff(h, 2)) for item in r]
    assert sp.expand(
        1944 * d_q[0]
        + 729 * u * X**2
        - 1458 * X * Z
        - 729 * Y**2
        + 320 * D * u**3 * v
        - 960 * D * v**3
    ) == 0
    assert sp.expand(
        5832 * d_q[1]
        + 2187 * v * X**2
        + 4374 * u * X * Y
        - 4374 * Y * Z
        - 64 * D * u**5
        + 1440 * D * u**2 * v**2
    ) == 0
    assert sp.expand(8 * d_q[2] - 8 * q[2]) == 0

    # Every high constant has zero r3-load on the exact common surface.  This
    # is what kills an earlier double-root cubic balance.
    common_point = {**common, d: 0, **{c[j]: 0 for j in range(8)}}
    for parameter in (d, c[7], c[5], c[4], c[2], c[1]):
        assert sp.diff(r[2], parameter).subs(common_point) == 0

    # The sole projective normal direction on the double-root cone.  The
    # order-three r3 obstruction is independent of every next coefficient.
    e = sp.symbols("e")
    p = sp.symbols("p0:5")
    double_arc = {
        a4: -6 + e**2 * p[4],
        a3: 4 + e**2 * p[3],
        a2: 9 + e + e**2 * p[2],
        a1: -12 + e + e**2 * p[1],
        a0: 4 - 2 * e + e**2 * p[0],
    }
    cubic = [sp.factor(sp.expand(item.subs(double_arc)).coeff(e, 3)) for item in r0]
    psum = sum(p)
    cubic_expected = [
        3 * psum / 4,
        3 * psum / 4,
        -sp.Rational(1, 16),
        -(4 * psum + 3) / 16,
        (4 * psum - 3) / 16,
    ]
    assert all(sp.expand(cubic[i] - cubic_expected[i]) == 0 for i in range(5))

    # Mixed later target constants cannot be dropped after a rho3-leading
    # balance.  Put I2=6*rho3 and I1=6*rho4=nu.  On nu!=0 the exact
    # localized fiber has A!=0 and is birational to the displayed cubic.
    # The substitutions below are the inverse reconstruction, not only a
    # necessary elimination map.
    A, V, nu = sp.symbols("A V nu", nonzero=True)
    nconst = -sp.Rational(256, 9) * nu
    B = nconst / A**2
    wcoord = V - 8 * B**2 / A
    qcoord = 4 * wcoord / A + 8 * B**2 / A**2
    pcoord = -8 * B * wcoord / A**2 - 32 * B**3 / A**3
    mixed_reconstruction = {
        a4: qcoord,
        a3: pcoord,
        a2: (A + qcoord**2) / 4,
        a1: (B + pcoord * qcoord) / 2,
        a0: (wcoord + pcoord**2) / 4,
    }
    mixed_values = [sp.factor(sp.cancel(item.subs(mixed_reconstruction))) for item in r0]
    assert mixed_values[:2] == [0, 0]
    assert sp.factor(mixed_values[2] - (24 * V**2 - A**3) / 1024) == 0
    assert sp.factor(mixed_values[3] - nu / 6) == 0
    assert sp.factor(
        mixed_values[4] - (27 * A**5 * V - 262144 * nu**2) / (27648 * A**3)
    ) == 0

    # On the singular mu=0 cubic, lambda=V/A is its rational normalization.
    # The exact r5 map has poles of orders six and seven at the two distinct
    # points lambda=0 and lambda=infinity.
    lambda_mixed = sp.symbols("lambda_mixed", nonzero=True)
    cusp_r5 = sp.factor(
        mixed_values[4].subs({A: 24 * lambda_mixed**2, V: 24 * lambda_mixed**3})
    )
    cusp_expected = sp.Rational(27, 2) * lambda_mixed**7 - nu**2 / (1458 * lambda_mixed**6)
    assert sp.factor(cusp_r5 - cusp_expected) == 0
    cusp_numerator, cusp_denominator = sp.fraction(sp.together(cusp_r5))
    assert sp.Poly(cusp_numerator, lambda_mixed).degree() == 13
    assert sp.Poly(cusp_denominator, lambda_mixed).degree() == 6
    assert sp.factor(cusp_numerator.subs(lambda_mixed, 0)) != 0

    # Original Faber reconstruction at a common balance.
    K = z**3 + u * z + v
    phi = X * z**2 + Y * z + Z
    first_g = K**3 + sp.Rational(3, 2) * h * K * phi
    formal_three_halves = sp.series(
        K**3 * (1 + h * phi / K**2) ** sp.Rational(3, 2), h, 0, 2
    ).removeO()
    assert sp.cancel(formal_three_halves - first_g) == 0

    # Exact zero-bracket and DS reconstructions through the original
    # coefficient equations.
    eta, du, dv = sp.symbols("eta du dv")
    f_pa = K**2 + eta
    g_pa = K**3 + sp.Rational(3, 2) * eta * K
    Kdot = du * sp.diff(K, u) + dv * sp.diff(K, v)
    f_pa_dot = 2 * K * Kdot
    g_pa_dot = (3 * K**2 + sp.Rational(3, 2) * eta) * Kdot
    assert sp.expand(f_pa_dot * sp.diff(g_pa, z) - sp.diff(f_pa, z) * g_pa_dot) == 0

    f_ds = z**6 + 4 * lam * z**4 + 10 * lam**2 * z**2 + 6 * lam**3
    g_ds = (
        z**9
        + 6 * lam * z**7
        + 21 * lam**2 * z**5
        + 35 * lam**3 * z**3
        + sp.Rational(63, 2) * lam**4 * z
    )
    ds_bracket = sp.expand(sp.diff(f_ds, lam) * sp.diff(g_ds, z) - sp.diff(f_ds, z) * sp.diff(g_ds, lam))
    assert ds_bracket == 567 * lam**6
    assert sp.resultant(f_ds.subs(lam, 1), g_ds.subs(lam, 1), z) == sp.Rational(3**9 * 7**2, 2**5)

    print("PASS-GCD3-69-CUBE-TRAJECTORY-SYMBOLICS")
    print("weights=r_n:9+n")
    print("leading_components=COMMON-CUBIC-OR-DS")
    print("double_normal_cubic_r3=-1/16")
    print("pole_balance=constant:(14-k)p=1,monomial:(14-k)p=m-1")
    print("exhaustive_load_weights=d:1,c7:2,c5:4,c4:5,c2:7,c1:8,rho1:10,rho2:11,rho3:12,rho4:13")
    print("mixed_rho3_rho4=ELLIPTIC-OR-TWO-POLE-CUSP")
    print("source_reconstruction=FABER-FIRST-SPLIT,ZERO-BRACKET,DS")
    print("aligned_kummer_assumptions_imported=false")


if __name__ == "__main__":
    main()
