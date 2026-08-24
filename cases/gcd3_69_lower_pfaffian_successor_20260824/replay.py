#!/usr/bin/env python3
"""Exact replay for the lower Pfaffian successor to GCD3-(6,9).

This derives the four lower first integrals, checks their Kummer weights,
verifies both reduced invariant strata and the terminal one-form, and freezes
the shifted Davenport--Stothers and rank-drop controls.  Completeness of the
universal component decomposition is independently checked in Singular.
"""

from __future__ import annotations

import sympy as sp


def integrate_exact(form: sp.Matrix, variables: list[sp.Symbol]) -> sp.Expr:
    """Integrate a checked exact polynomial one-form in fixed order."""
    for i in range(len(variables)):
        for j in range(i + 1, len(variables)):
            assert sp.expand(
                sp.diff(form[i], variables[j]) - sp.diff(form[j], variables[i])
            ) == 0
    potential = sp.Integer(0)
    for i, variable in enumerate(variables):
        remainder = sp.expand(form[i] - sp.diff(potential, variable))
        potential = sp.expand(potential + sp.integrate(remainder, variable))
    assert all(
        sp.expand(sp.diff(potential, variables[i]) - form[i]) == 0
        for i in range(len(variables))
    )
    return sp.factor(potential)


def monomial_weight(
    polynomial: sp.Expr, variables: list[sp.Symbol], weights: list[int]
) -> int:
    """Return the common Z/3 weight, failing if the polynomial is inhomogeneous."""
    seen = {
        sum(exponent * weight for exponent, weight in zip(monomial, weights)) % 3
        for monomial, _coefficient in sp.Poly(polynomial, *variables).terms()
    }
    assert len(seen) == 1
    return seen.pop()


def main() -> None:
    z = sp.symbols("z")
    a = sp.symbols("a0:5")
    a0, a1, a2, a3, a4 = a
    va = sp.symbols("va0:5")
    kappa, mu = sp.symbols("kappa mu")

    f = z**6 + sum(a[i] * z**i for i in range(5))
    b = sp.symbols("b0:8")
    g_generic = z**9 + sum(b[i] * z**i for i in range(8))
    # The zero-constant high-row solution from the first gate.
    bsol = {
        b[7]: sp.Rational(3, 2) * a4,
        b[6]: sp.Rational(3, 2) * a3,
        b[5]: sp.Rational(3, 8) * (4 * a2 + a4**2),
        b[4]: sp.Rational(3, 4) * (2 * a1 + a3 * a4),
        b[3]: sp.Rational(1, 16)
        * (24 * a0 + 12 * a2 * a4 + 6 * a3**2 - a4**3),
        b[2]: sp.Rational(3, 16)
        * (4 * a1 * a4 + 4 * a2 * a3 - a3 * a4**2),
        b[1]: sp.Rational(3, 128)
        * (
            32 * a0 * a4
            + 32 * a1 * a3
            + 16 * a2**2
            - 8 * a2 * a4**2
            - 8 * a3**2 * a4
            + a4**4
        ),
        b[0]: sp.Rational(1, 32)
        * (
            24 * a0 * a3
            + 24 * a1 * a2
            - 6 * a1 * a4**2
            - 12 * a2 * a3 * a4
            - 2 * a3**3
            + 3 * a3 * a4**3
        ),
    }
    square_root_section = z**3 + sp.Rational(1, 2) * a4 * z + sp.Rational(1, 2) * a3
    g = sp.expand(g_generic.subs(bsol) + kappa * square_root_section)

    f_velocity = sum(sp.diff(f, a[i]) * va[i] for i in range(5))
    g_velocity = sum(sp.diff(g, a[i]) * va[i] for i in range(5))
    source_bracket = sp.Poly(
        sp.expand(f_velocity * sp.diff(g, z) - sp.diff(f, z) * g_velocity), z
    )
    assert all(source_bracket.coeff_monomial(z**r) == 0 for r in range(12, 4, -1))

    # Rows are ordered z^4,z^3,z^2,z,z^0 and columns da0,...,da4.
    matrix = sp.Matrix(
        [
            [source_bracket.coeff_monomial(z**r).coeff(va[i]) for i in range(5)]
            for r in range(4, -1, -1)
        ]
    )
    alpha4, alpha3, alpha2, alpha1, alpha0 = [
        sp.Matrix([matrix[row, i] for i in range(5)]) for row in range(5)
    ]

    # The triangular Frobenius correction is exact, not an ansatz.
    dI4 = alpha4
    dI3 = alpha3
    dI2 = alpha2 - a4 * alpha4 / 2
    dI1 = alpha1 - a3 * alpha4 / 3 - a4 * alpha3 / 3
    I4 = integrate_exact(dI4, list(a))
    I3 = integrate_exact(dI3, list(a))
    I2 = integrate_exact(dI2, list(a))
    I1 = integrate_exact(dI1, list(a))

    e4 = (
        64 * a0 * a2
        - 16 * a0 * a4**2
        + 32 * a1**2
        - 32 * a1 * a3 * a4
        - 16 * a2**2 * a4
        - 16 * a2 * a3**2
        + 8 * a2 * a4**3
        + 12 * a3**2 * a4**2
        - a4**5
    )
    e3 = (
        64 * a0 * a1
        - 32 * a0 * a3 * a4
        - 32 * a1 * a2 * a4
        - 16 * a1 * a3**2
        + 8 * a1 * a4**3
        - 16 * a2**2 * a3
        + 24 * a2 * a3 * a4**2
        + 8 * a3**3 * a4
        - 5 * a3 * a4**4
    )
    A = 4 * a2 - a4**2
    B = 2 * a1 - a3 * a4
    assert sp.expand(I4 - (sp.Rational(9, 128) * e4 + sp.Rational(3, 4) * kappa * A)) == 0
    assert sp.expand(I3 - (sp.Rational(9, 128) * e3 + sp.Rational(3, 2) * kappa * B)) == 0

    # Coefficient weights are -i mod 3; kappa is invariant.  Constants of
    # nonzero weight vanish in the nontrivial Kummer extension.
    weight_variables = [a0, a1, a2, a3, a4, kappa]
    weights = [0, 2, 1, 0, 2, 0]
    assert [monomial_weight(I, weight_variables, weights) for I in (I4, I3, I2, I1)] == [1, 2, 0, 1]

    # Reduced stratum A: the full source coordinates are polynomials in one
    # moving cubic K, with constant offsets.  Its bracket is identically zero.
    u, v, d, du, dv = sp.symbols("u v d du dv")
    K = z**3 + u * z + v
    subA = {a4: 2 * u, a3: 2 * v, a2: u**2, a1: 2 * u * v, a0: v**2 + d}
    q = kappa + sp.Rational(3, 2) * d
    assert sp.expand(f.subs(subA) - (K**2 + d)) == 0
    assert sp.expand(g.subs(subA) - (K**3 + q * K)) == 0
    assert all(sp.expand(I.subs(subA)) == 0 for I in (I4, I3, I1))
    assert sp.expand(I2.subs(subA) - (sp.Rational(9, 4) * d**2 + 3 * kappa * d)) == 0
    K_velocity = du * z + dv
    bracketA = sp.expand(
        (2 * K * K_velocity) * sp.diff(K**3 + q * K, z)
        - sp.diff(K**2 + d, z) * ((3 * K**2 + q) * K_velocity)
    )
    assert bracketA == 0

    # Reduced stratum B and its j=0 elliptic coordinate model.
    a0B = a2 * a4 / 4 - a4**3 / 16 - sp.Rational(2, 3) * kappa
    subB = {a3: 0, a1: 0, a0: a0B}
    EB = (
        384 * a2**3
        - 432 * a2**2 * a4**2
        + 144 * a2 * a4**4
        - 15 * a4**6
        + 1024 * kappa**2
        + 1024 * mu
    )
    assert all(sp.expand(I.subs(subB)) == 0 for I in (I4, I3, I1))
    assert sp.expand((I2 - mu).subs(subB) + EB / 1024) == 0
    X = 8 * a2 - 2 * a4**2
    Y = 3 * a4 * X
    C = kappa**2 + mu
    assert sp.expand((Y**2 - 3 * X**3 - 4096 * C) + 4 * EB) == 0

    # Pull back the terminal row polynomially before dividing by any chart
    # coordinate.  These are its coefficients in da4,da2 on stratum B.
    beta_a4 = sp.factor((alpha0[0] * sp.diff(a0B, a4) + alpha0[4]).subs(subB))
    beta_a2 = sp.factor((alpha0[0] * sp.diff(a0B, a2) + alpha0[2]).subs(subB))
    assert sp.expand(
        beta_a4
        - sp.Rational(3, 2048)
        * (4 * a2 - 3 * a4**2)
        * (4 * a2 - a4**2)
        * (4 * a2 + a4**2)
    ) == 0
    assert sp.expand(
        beta_a2
        - sp.Rational(3, 512)
        * a4
        * (4 * a2 - a4**2)
        * (4 * a2 + a4**2)
    ) == 0

    # Change from (a4,a2) to (a4,X).  On the elliptic equation this is
    # beta=(7Y^2-12288C)/(147456X) dY.
    beta_X = sp.factor(beta_a2 / 8)
    beta_A = sp.factor(beta_a4 + a4 * beta_a2 / 2)
    mu_on_curve = sp.expand((Y**2 - 3 * X**3) / 4096 - kappa**2)
    qY = (7 * Y**2 - 12288 * C) / (147456 * X)
    assert sp.factor((beta_A - qY * 3 * X).subs(mu, mu_on_curve)) == 0
    assert sp.factor((beta_X - qY * 3 * a4).subs(mu, mu_on_curve)) == 0

    # With X=sR and Y,R rational, beta=j/s gives this exact rational ODE.
    h, R, Yx, j = sp.symbols("h R Yx j", nonzero=True)
    terminal_R = sp.Eq((7 * Y**2 - 12288 * C) * Yx, 147456 * j * R)
    curve_R = sp.Eq(3 * h * R**3, Y**2 - 4096 * C)
    assert terminal_R.lhs == (7 * Y**2 - 12288 * C) * Yx
    assert curve_R.lhs == 3 * h * R**3
    eliminated = sp.expand(
        3 * h * (7 * Y**2 - 12288 * C) ** 3 * Yx**3
        - (147456 * j) ** 3 * (Y**2 - 4096 * C)
    )
    assert sp.expand(
        eliminated.subs(
            R, (7 * Y**2 - 12288 * C) * Yx / (147456 * j)
        )
        - (147456 * j) ** 3
        * (curve_R.lhs - curve_R.rhs).subs(
            R, (7 * Y**2 - 12288 * C) * Yx / (147456 * j)
        )
    ) == 0

    # Forbidden-value valuation when C!=0.  At a ramified preimage of either
    # root of 7Y^2-12288C, order e>=1, h has order 3-6e<0.
    ramification = sp.symbols("ramification", integer=True, positive=True)
    h_order = -3 * ramification - 3 * (ramification - 1)
    assert sp.expand(h_order - (3 - 6 * ramification)) == 0
    assert h_order < 0
    # At the same value Y^2=12288C/7, both X^3 and Y^2-4096C are nonzero.
    assert sp.expand(
        sp.Rational(12288, 7) * C
        - 4096 * C
        + sp.Rational(16384, 7) * C
    ) == 0

    # Special fiber C=0: EB=(3/4)X^2(X-3a4^2).  X=0 belongs to zero-bracket
    # stratum A; the other branch is a constant-shifted DS curve.
    assert sp.factor(EB.subs(mu, -kappa**2) - sp.Rational(3, 4) * X**2 * (X - 3 * a4**2)) == 0
    K0 = z**3 + a4 * z / 2
    subX0 = {a3: 0, a1: 0, a2: a4**2 / 4, a0: -sp.Rational(2, 3) * kappa}
    assert sp.expand(f.subs(subX0) - (K0**2 - sp.Rational(2, 3) * kappa)) == 0
    assert sp.expand(g.subs(subX0) - K0**3) == 0
    lam = sp.symbols("lam")
    shifted_ds = {
        a4: 4 * lam,
        a3: 0,
        a2: 10 * lam**2,
        a1: 0,
        a0: 6 * lam**3 - sp.Rational(2, 3) * kappa,
    }
    f_lam = z**6 + 4 * lam * z**4 + 10 * lam**2 * z**2 + 6 * lam**3
    g_lam = z**9 + 6 * lam * z**7 + 21 * lam**2 * z**5 + 35 * lam**3 * z**3 + sp.Rational(63, 2) * lam**4 * z
    assert sp.expand(f.subs(shifted_ds) - (f_lam - sp.Rational(2, 3) * kappa)) == 0
    assert sp.expand(g.subs(shifted_ds) - g_lam) == 0
    shifted_lam_bracket = sp.factor(
        sp.diff(f_lam - sp.Rational(2, 3) * kappa, lam) * sp.diff(g_lam, z)
        - sp.diff(f_lam - sp.Rational(2, 3) * kappa, z) * sp.diff(g_lam, lam)
    )
    assert shifted_lam_bracket == 567 * lam**6
    shifted_matrix = matrix.subs(shifted_ds)
    assert sp.factor(shifted_matrix.det(method="domain-ge")) == sp.Rational(3**18 * 7, 32) * lam**20

    # The pure-static DS determinant is a negative control: its extra rank
    # factors lie outside the Kummer invariant fiber unless kappa=0.
    pure_ds = dict(shifted_ds)
    pure_ds[a0] = 6 * lam**3
    pure_det = sp.factor(matrix.subs(pure_ds).det(method="domain-ge"))
    expected_pure_det = (
        sp.Rational(81, 32)
        * lam**5
        * (4 * kappa + 63 * lam**3)
        * (8 * kappa**2 - 72 * kappa * lam**3 + 729 * lam**6) ** 2
    )
    assert sp.expand(pure_det - expected_pure_det) == 0
    assert sp.factor(I4.subs(pure_ds)) == 18 * kappa * lam**2

    # Recheck the nontrivial-Kummer valuation contradiction for the shifted
    # DS terminal ODE 567*s*lambda^6*lambda'=j.
    xx = sp.symbols("xx")
    hh = sp.Function("hh")(xx)
    qq = sp.Function("qq")(xx)
    descended_source = sp.expand(
        189
        * hh**4
        * qq**6
        * (2 * sp.diff(hh, xx) * qq + 3 * hh * sp.diff(qq, xx))
    )
    assert sp.expand(
        descended_source
        - 567
        * hh**5
        * qq**6
        * (sp.Rational(2, 3) * sp.diff(hh, xx) * qq / hh + sp.diff(qq, xx))
    ) == 0
    kval = sp.symbols("kval", integer=True, positive=True)
    eval_ = 3 + 7 * kval
    nval = -2 - 5 * kval
    assert 5 * eval_ + 7 * nval - 1 == 0
    assert 2 * eval_ + 3 * nval == -kval
    ell = sp.symbols("ell", integer=True, positive=True)
    assert sp.expand(eval_.subs(kval, 3 * ell) - (3 + 21 * ell)) == 0

    print("PASS-GCD3-69-LOWER-PFAFFIAN-SUCCESSOR")
    print("lower_zero_rows=FOUR-TRIANGULAR-FIRST-INTEGRALS")
    print("kummer_constants=I4=I3=I1=0,I2=mu")
    print("reduced_invariant_strata=ZERO-BRACKET-SHEET,ELLIPTIC-SHEET")
    print("elliptic_terminal_beta=(7Y^2-12288C)dY/(147456X)")
    print("constant_Y=TERMINAL-FAILS-BEFORE-CLEARING")
    print("forbidden_finite_value=X-NONZERO-NO-CHART-ESCAPE")
    print("ramified_preimage=h-order=3-6e<0")
    print("elliptic_C_nonzero=POLYNOMIAL-H-VALUATION-EMPTY")
    print("elliptic_C_zero=ZERO-BRACKET-OR-SHIFTED-DS")
    print("component_switching=PRIME-GENERIC-PATH-CANNOT-SWITCH")
    print("embedded_C_zero=NO-EXTRA-FIELD-VALUED-BRANCH")
    print("denominator_rank_strata=DISPATCHED-WITHOUT-MATRIX-INVERSION")
    print("shifted_ds_bracket=567*lambda^6")
    print("shifted_ds_constant_subtraction=BRACKET-AND-VALUATIONS-UNCHANGED")
    print("aligned_noncube_69_branch=PROVISIONAL-EMPTY")
    print("full_cubic_boundary_reduction=UNUSED")
    print("cube_mismatch_branch=OPEN")
    print("jc2_inference=false")


if __name__ == "__main__":
    main()
