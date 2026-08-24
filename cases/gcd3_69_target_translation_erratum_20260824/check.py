#!/usr/bin/env python3
"""Exact target-translation covariance check for the aligned (6,9) gate."""

import sympy as sp


def integrate_exact(form, variables):
    potential = sp.Integer(0)
    for i, variable in enumerate(variables):
        for j in range(i + 1, len(variables)):
            assert sp.expand(
                sp.diff(form[i], variables[j])
                - sp.diff(form[j], variables[i])
            ) == 0
        remainder = sp.expand(form[i] - sp.diff(potential, variable))
        potential = sp.expand(potential + sp.integrate(remainder, variable))
    assert all(
        sp.expand(sp.diff(potential, variables[i]) - form[i]) == 0
        for i in range(len(variables))
    )
    return sp.factor(potential)


def main():
    z = sp.symbols("z")
    aa = sp.symbols("a0:5")
    a0, a1, a2, a3, a4 = aa
    va = sp.symbols("v0:5")
    b = sp.symbols("b0:8")
    kappa, q, mu = sp.symbols("kappa q mu")

    f = z**6 + sum(aa[i] * z**i for i in range(5))
    g_generic = z**9 + sum(b[i] * z**i for i in range(8))
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
    K = z**3 + a4 * z / 2 + a3 / 2
    g0 = sp.expand(g_generic.subs(bsol))
    g = sp.expand(g0 + kappa * K)

    # A legal target translation f -> f+q is represented in the normalized
    # coefficient chart by a0 -> a0+q and kappa -> kappa-3q/2.
    translated = {a0: a0 + q, kappa: kappa - sp.Rational(3, 2) * q}
    assert sp.expand(f.subs(a0, a0 + q) - (f + q)) == 0
    assert sp.expand(g.subs(translated, simultaneous=True) - g) == 0

    f_velocity = sum(sp.diff(f, aa[i]) * va[i] for i in range(5))
    g_velocity = sum(sp.diff(g, aa[i]) * va[i] for i in range(5))
    bracket = sp.Poly(
        sp.expand(f_velocity * sp.diff(g, z) - sp.diff(f, z) * g_velocity), z
    )
    matrix = sp.Matrix(
        [
            [bracket.coeff_monomial(z**r).coeff(va[i]) for i in range(5)]
            for r in range(4, -1, -1)
        ]
    )
    alpha4, alpha3, alpha2, alpha1, _alpha0 = [
        sp.Matrix([matrix[row, i] for i in range(5)]) for row in range(5)
    ]
    integrals = [
        integrate_exact(alpha4, list(aa)),
        integrate_exact(alpha3, list(aa)),
        integrate_exact(alpha2 - a4 * alpha4 / 2, list(aa)),
        integrate_exact(
            alpha1 - a3 * alpha4 / 3 - a4 * alpha3 / 3, list(aa)
        ),
    ]
    I4, I3, I2, I1 = integrals
    assert sp.expand(I4.subs(translated, simultaneous=True) - I4) == 0
    assert sp.expand(I3.subs(translated, simultaneous=True) - I3) == 0
    assert sp.expand(I1.subs(translated, simultaneous=True) - I1) == 0
    mu_shift = 3 * kappa * q - sp.Rational(9, 4) * q**2
    assert sp.expand(I2.subs(translated, simultaneous=True) - I2 - mu_shift) == 0
    assert sp.expand(
        (kappa - sp.Rational(3, 2) * q) ** 2
        + (mu + mu_shift)
        - (kappa**2 + mu)
    ) == 0

    # On PA, d shifts while the coefficient of K in g is invariant.
    d = sp.symbols("d")
    assert sp.expand(
        (kappa - sp.Rational(3, 2) * q)
        + sp.Rational(3, 2) * (d + q)
        - (kappa + sp.Rational(3, 2) * d)
    ) == 0

    # Choosing q=2kappa/3 gauges kappa to zero and removes the shifted-DS
    # constant without changing derivatives or the source bracket.
    qfix = sp.Rational(2, 3) * kappa
    assert sp.expand((kappa - sp.Rational(3, 2) * q).subs(q, qfix)) == 0
    assert sp.expand(-sp.Rational(2, 3) * kappa + qfix) == 0

    print("PASS-GCD3-69-TARGET-TRANSLATION-ERRATUM")
    print("kappa=PINNED-NORMALIZATION-COORDINATE-NOT-GLOBAL-MODULUS")
    print("C=kappa^2+mu=TARGET-TRANSLATION-INVARIANT")
    print("aligned_lower_exclusion=UNCHANGED")
    print("cube_mismatch=OPEN")
    print("jc2_inference=false")


if __name__ == "__main__":
    main()

