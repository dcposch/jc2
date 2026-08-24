#!/usr/bin/env python3
"""Exact replay for the first source-honest GCD3-(6,9) common-cubic gate.

This is a bounded symbolic calculation.  It checks the Kummer depression
bookkeeping, the binary common-cubic/discriminant split, the precise
one-root boundary counterexample, and the infinitesimal bracket/residue
claims.  It does not search for a Keller pair or claim nonlinear closure.
"""

from __future__ import annotations

import sympy as sp


def jac(f: sp.Expr, g: sp.Expr, t: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    """Binary/source orientation J(f,g)=f_t g_z-f_z g_t."""
    return sp.expand(sp.diff(f, t) * sp.diff(g, z) - sp.diff(f, z) * sp.diff(g, t))


def coeff(expr: sp.Expr, var: sp.Symbol, power: int) -> sp.Expr:
    return sp.Poly(sp.expand(expr), var).coeff_monomial(var**power)


def homogeneous_matrix_rank(columns: list[sp.Expr], t: sp.Symbol, z: sp.Symbol, degree: int) -> int:
    mons = [z**i * t ** (degree - i) for i in range(degree + 1)]
    matrix = sp.Matrix(
        [[sp.Poly(col, t, z).coeff_monomial(mon) for col in columns] for mon in mons]
    )
    return matrix.rank()


def potential_from_gradient(
    variables: list[sp.Symbol], gradients: list[sp.Expr]
) -> sp.Expr:
    """Integrate a checked exact polynomial one-form in a fixed order."""
    potential = sp.Integer(0)
    for variable, gradient in zip(variables, gradients):
        remainder = sp.expand(gradient - sp.diff(potential, variable))
        potential = sp.expand(potential + sp.integrate(remainder, variable))
    assert all(
        sp.expand(sp.diff(potential, variable) - gradient) == 0
        for variable, gradient in zip(variables, gradients)
    )
    return sp.factor(potential)


def main() -> None:
    x = sp.symbols("x")
    s = sp.Function("s")(x)
    A = sp.Function("A")(x)
    B = sp.Function("B")(x)

    # Actual-y rows after a6=s^6, b9=s^9, a5=s^5 A, b8=s^8 B.
    a6, b9, a5, b8 = s**6, s**9, s**5 * A, s**8 * B
    row14 = sp.expand(9 * sp.diff(a6, x) * b9 - 6 * a6 * sp.diff(b9, x))
    row13 = sp.expand(
        8 * sp.diff(a6, x) * b8
        + 9 * sp.diff(a5, x) * b9
        - 6 * a6 * sp.diff(b8, x)
        - 5 * a5 * sp.diff(b9, x)
    )
    assert sp.simplify(row14) == 0
    assert sp.simplify(row13 / s**14 - (9 * sp.diff(A, x) - 6 * sp.diff(B, x))) == 0

    # Translation z0=z-r depresses P.  Q aligns iff delta=3A-2B=0.
    z0, z, r, aa, bb = sp.symbols("z0 z r aa bb")
    p_top = sp.expand((z - r) ** 6 + aa * (z - r) ** 5)
    q_top = sp.expand((z - r) ** 9 + bb * (z - r) ** 8)
    assert coeff(p_top, z, 5) == aa - 6 * r
    assert coeff(q_top, z, 8) == bb - 9 * r
    assert sp.simplify(coeff(q_top, z, 8).subs(r, aa / 6) + (3 * aa - 2 * bb) / 2) == 0
    # Kummer weights: s,z,r,A,B have weights 1,1,1,1,1 modulo three.
    assert (-5) % 3 == 1 and (-8) % 3 == 1

    t, u, v, eps, c = sp.symbols("t u v eps c")
    K = z**3 + u * t**2 * z + v * t**3
    F0, G0 = sp.expand(K**2), sp.expand(K**3)
    assert coeff(F0, z, 5) == 0
    assert coeff(G0, z, 8) == 0
    assert jac(F0, G0, t, z) == 0
    disc = sp.discriminant(K.subs(t, 1), z)
    assert sp.expand(disc - (-4 * u**3 - 27 * v**2)) == 0

    # Exact double/triple strata.
    a = sp.symbols("a")
    Kdouble_param = sp.expand((z - a * t) ** 2 * (z + 2 * a * t))
    assert Kdouble_param == z**3 - 3 * a**2 * t**2 * z + 2 * a**3 * t**3
    assert sp.expand(disc.subs({u: -3 * a**2, v: 2 * a**3})) == 0
    assert K.subs({u: 0, v: 0}) == z**3

    # Generic normalized perturbations: no z^6,z^5 in phi and no z^9,z^8 in psi.
    ps = sp.symbols("p0:5")
    qs = sp.symbols("q0:8")
    phi = sum(ps[i] * z**i * t ** (6 - i) for i in range(5))
    psi = sum(qs[i] * z**i * t ** (9 - i) for i in range(8))
    linear = sp.expand(jac(phi, G0, t, z) + jac(F0, psi, t, z))
    factored_linear = sp.expand(K * jac(K, 2 * psi - 3 * K * phi, t, z))
    assert sp.expand(linear - factored_linear) == 0
    assert sp.rem(linear.subs(t, 1), K.subs(t, 1), z) == 0
    assert sp.resultant(K.subs(t, 1), c, z) == c**3

    # On K=z^3-t^2 z the normalized tangent map has nullity five; imposing
    # the chosen root r=0 leaves nullity four.  Full K-divisibility leaves
    # only the two depressed common-cubic moduli directions.
    Ksf = z**3 - t**2 * z
    phi_basis = [z**i * t ** (6 - i) for i in range(5)]
    psi_basis = [z**i * t ** (9 - i) for i in range(8)]
    columns = [jac(ph, Ksf**3, t, z) for ph in phi_basis]
    columns += [jac(Ksf**2, psii, t, z) for psii in psi_basis]
    rank = homogeneous_matrix_rank(columns, t, z, 13)
    assert rank == 8 and len(columns) - rank == 5
    # phi(r=0)=0 removes the t^6 basis vector and no image rank.
    one_root_columns = columns[1:]
    one_root_rank = homogeneous_matrix_rank(one_root_columns, t, z, 13)
    assert one_root_rank == 8 and len(one_root_columns) - one_root_rank == 4

    # Source-honest split-root control: both selected-root boundaries hold,
    # but phi is not zero at the other two roots and is not divisible by K.
    phi_sf = z * t**5
    psi_sf = sp.Rational(3, 2) * Ksf * phi_sf
    Lsf = sp.expand(jac(phi_sf, Ksf**3, t, z) + jac(Ksf**2, psi_sf, t, z))
    assert Lsf == 0
    assert phi_sf.subs({t: 1, z: 0}) == 0
    assert psi_sf.subs({t: 1, z: 0}) == 0
    assert [phi_sf.subs({t: 1, z: rr}) for rr in (0, 1, -1)] == [0, 1, -1]
    assert sp.rem(phi_sf.subs(t, 1), Ksf.subs(t, 1), z) == z

    # The quadratic component residue.  For a first-order kernel with
    # psi=(3/2)K phi, q2=(3/2)phi J(phi,K), and modulo K it is
    # 9 phi^2 K_z (Euler, degrees 6 and 3).
    q2_generic = sp.Rational(3, 2) * phi * jac(phi, K, t, z)
    q2_affine = sp.expand(q2_generic.subs(t, 1))
    expected_affine = sp.expand(9 * phi.subs(t, 1) ** 2 * sp.diff(K.subs(t, 1), z))
    assert sp.rem(q2_affine - expected_affine, K.subs(t, 1), z) == 0

    q2_sf = sp.factor(jac(phi_sf, psi_sf, t, z))
    assert q2_sf == sp.Rational(9, 2) * t**9 * z**2 * (-t**2 + 5 * z**2)
    sf_residues = [sp.expand(q2_sf.subs({t: 1, z: rr})) for rr in (0, 1, -1)]
    assert sf_residues == [0, 18, 18]
    assert sp.rem(q2_sf.subs(t, 1), Ksf.subs(t, 1), z) == 18 * z**2

    # The nonlinear extremal Davenport--Stothers bypass.  Shioda's unique
    # order-three representative (Birch) has a nonzero constant Wronskian.
    zz, lam = sp.symbols("zz lam")
    f_birch = zz**6 + 4 * zz**4 + 10 * zz**2 + 6
    g_birch = (
        zz**9
        + 6 * zz**7
        + 21 * zz**5
        + 35 * zz**3
        + sp.Rational(63, 2) * zz
    )
    h_birch = sp.factor(f_birch**3 - g_birch**2)
    w_birch = sp.factor(
        2 * f_birch * sp.diff(g_birch, zz)
        - 3 * sp.diff(f_birch, zz) * g_birch
    )
    assert sp.expand(
        h_birch - sp.Rational(27, 4) * (4 * zz**4 + 13 * zz**2 + 32)
    ) == 0
    assert w_birch == 378
    assert sp.gcd(f_birch, g_birch) == 1

    # Independently derive the normalized constant-W coefficient scheme
    # whose primary decomposition is checked by the Singular replay.
    avec = sp.symbols("aa0:5")
    bvec = sp.symbols("bb0:8")
    aa0, aa1, aa2, aa3, aa4 = avec
    f_gen = zz**6 + aa4 * zz**4 + aa3 * zz**3 + aa2 * zz**2 + aa1 * zz + aa0
    g_gen = zz**9 + sum(bvec[i] * zz**i for i in range(8))
    w_gen = sp.Poly(
        sp.expand(2 * f_gen * sp.diff(g_gen, zz) - 3 * sp.diff(f_gen, zz) * g_gen),
        zz,
    )
    bsol = {
        bvec[7]: sp.Rational(3, 2) * aa4,
        bvec[6]: sp.Rational(3, 2) * aa3,
        bvec[5]: sp.Rational(3, 8) * (4 * aa2 + aa4**2),
        bvec[4]: sp.Rational(3, 4) * (2 * aa1 + aa3 * aa4),
        bvec[3]: sp.Rational(1, 16)
        * (24 * aa0 + 12 * aa2 * aa4 + 6 * aa3**2 - aa4**3),
        bvec[2]: sp.Rational(3, 16)
        * (4 * aa1 * aa4 + 4 * aa2 * aa3 - aa3 * aa4**2),
        bvec[1]: sp.Rational(3, 128)
        * (
            32 * aa0 * aa4
            + 32 * aa1 * aa3
            + 16 * aa2**2
            - 8 * aa2 * aa4**2
            - 8 * aa3**2 * aa4
            + aa4**4
        ),
        bvec[0]: sp.Rational(1, 32)
        * (
            24 * aa0 * aa3
            + 24 * aa1 * aa2
            - 6 * aa1 * aa4**2
            - 12 * aa2 * aa3 * aa4
            - 2 * aa3**3
            + 3 * aa3 * aa4**3
        ),
    }
    for power in range(12, 4, -1):
        assert sp.expand(w_gen.coeff_monomial(zz**power).subs(bsol)) == 0
    residual_rows = [
        sp.factor(w_gen.coeff_monomial(zz**power).subs(bsol))
        for power in range(4, 0, -1)
    ]
    assert all(row != 0 for row in residual_rows)
    e4 = (
        64 * aa0 * aa2
        - 16 * aa0 * aa4**2
        + 32 * aa1**2
        - 32 * aa1 * aa3 * aa4
        - 16 * aa2**2 * aa4
        - 16 * aa2 * aa3**2
        + 8 * aa2 * aa4**3
        + 12 * aa3**2 * aa4**2
        - aa4**5
    )
    e3 = (
        64 * aa0 * aa1
        - 32 * aa0 * aa3 * aa4
        - 32 * aa1 * aa2 * aa4
        - 16 * aa1 * aa3**2
        + 8 * aa1 * aa4**3
        - 16 * aa2**2 * aa3
        + 24 * aa2 * aa3 * aa4**2
        + 8 * aa3**3 * aa4
        - 5 * aa3 * aa4**4
    )
    e2 = (
        96 * aa0**2
        + 16 * aa0 * aa2 * aa4
        - 48 * aa0 * aa3**2
        - 4 * aa0 * aa4**3
        + 8 * aa1**2 * aa4
        - 96 * aa1 * aa2 * aa3
        + 16 * aa1 * aa3 * aa4**2
        - 16 * aa2**3
        + 8 * aa2**2 * aa4**2
        + 44 * aa2 * aa3**2 * aa4
        - aa2 * aa4**4
        + 6 * aa3**4
        - 9 * aa3**2 * aa4**3
    )
    e1 = (
        96 * aa0 * aa1 * aa4
        - 64 * aa0 * aa2 * aa3
        - 32 * aa0 * aa3 * aa4**2
        - 32 * aa1**2 * aa3
        - 208 * aa1 * aa2**2
        + 56 * aa1 * aa2 * aa4**2
        + 8 * aa1 * aa3**2 * aa4
        - aa1 * aa4**4
        + 96 * aa2**2 * aa3 * aa4
        + 16 * aa2 * aa3**3
        - 24 * aa2 * aa3 * aa4**3
    )
    expected_residuals = [
        sp.Rational(15, 64) * e4,
        sp.Rational(33, 128) * e3,
        sp.Rational(3, 32) * e2,
        sp.Rational(3, 128) * e1,
    ]
    assert all(
        sp.expand(actual - expected) == 0
        for actual, expected in zip(residual_rows, expected_residuals)
    )

    # Both advertised radicals annihilate all four residual rows.
    common_sub = {
        aa4: 2 * u,
        aa3: 2 * v,
        aa2: u**2,
        aa1: 2 * u * v,
        aa0: v**2,
    }
    ds_a = sp.symbols("ds_a")
    ds_sub = {
        aa4: ds_a,
        aa3: 0,
        aa2: sp.Rational(5, 8) * ds_a**2,
        aa1: 0,
        aa0: sp.Rational(3, 32) * ds_a**3,
    }
    assert all(sp.expand(row.subs(common_sub)) == 0 for row in residual_rows)
    assert all(sp.expand(row.subs(ds_sub)) == 0 for row in residual_rows)

    # Derive and integrate the eight triangular source-high rows, with one
    # independent integration constant c_j in each b_j.  This proves
    # generality of the high-row normal form rather than merely checking one
    # displayed solution.
    kappa = sp.symbols("kappa")
    cvec = sp.symbols("cc0:8")
    vbvec = sp.symbols("vbb0:8")
    vavec = sp.symbols("vaa0:5")
    f_velocity = sum(sp.diff(f_gen, avec[i]) * vavec[i] for i in range(5))
    independent_g_velocity = sum(vbvec[i] * zz**i for i in range(8))
    source_general = sp.Poly(
        sp.expand(
            f_velocity * sp.diff(g_gen, zz)
            - sp.diff(f_gen, zz) * independent_g_velocity
        ),
        zz,
    )
    solved_b: dict[sp.Symbol, sp.Expr] = {}
    solved_vb: dict[sp.Symbol, sp.Expr] = {}
    variable_order = [aa4, aa3, aa2, aa1, aa0]
    velocity_for = {avec[i]: vavec[i] for i in range(5)}
    for bj, power in zip(range(7, -1, -1), range(12, 4, -1)):
        row = sp.expand(
            source_general.coeff_monomial(zz**power).subs(solved_b).subs(solved_vb)
        )
        target = sp.solve(sp.Eq(row, 0), vbvec[bj], dict=False)[0]
        gradients = [
            sp.expand(target).coeff(velocity_for[variable])
            for variable in variable_order
        ]
        assert sp.expand(
            target
            - sum(
                gradients[i] * velocity_for[variable_order[i]]
                for i in range(len(variable_order))
            )
        ) == 0
        potential = potential_from_gradient(variable_order, gradients)
        solved_b[bvec[bj]] = potential + cvec[bj]
        solved_vb[vbvec[bj]] = sum(
            sp.diff(potential, avec[i]) * vavec[i] for i in range(5)
        )

    integrated_g = sp.expand(g_gen.subs(solved_b))
    # A coefficient/integration constant of z^j has Kummer weight -j mod 3.
    assert [j for j in range(8) if (-j) % 3 == 0] == [0, 3, 6]
    nonzero_weight_constants = {cvec[j]: 0 for j in (7, 5, 4, 2, 1)}
    cubic_section = zz**3 + sp.Rational(1, 2) * aa4 * zz + sp.Rational(1, 2) * aa3
    descended_g = sp.expand(integrated_g.subs(nonzero_weight_constants))
    assert sp.expand(
        descended_g
        - (g_gen.subs(bsol) + cvec[6] * f_gen + cvec[3] * cubic_section + cvec[0])
    ) == 0
    # The constant target shear removes c_6*f and target translation removes
    # c_0.  Kappa=c_3 is the only essential high-row integration constant.
    g_reduced = sp.expand(g_gen.subs(bsol) + kappa * cubic_section)
    g_velocity = sum(sp.diff(g_reduced, avec[i]) * vavec[i] for i in range(5))
    source_j = sp.Poly(
        sp.expand(f_velocity * sp.diff(g_reduced, zz) - sp.diff(f_gen, zz) * g_velocity),
        zz,
    )
    assert all(source_j.coeff_monomial(zz**power) == 0 for power in range(12, 4, -1))
    K_affine = zz**3 + u * zz + v
    assert sp.expand(f_gen.subs(common_sub) - K_affine**2) == 0
    assert sp.expand(g_reduced.subs(common_sub) - (K_affine**3 + kappa * K_affine)) == 0
    du, dv = sp.symbols("du dv")
    K_velocity = du * zz + dv
    common_source_j = sp.expand(
        (2 * K_affine * K_velocity)
        * sp.diff(K_affine**3 + kappa * K_affine, zz)
        - sp.diff(K_affine**2, zz)
        * ((3 * K_affine**2 + kappa) * K_velocity)
    )
    assert common_source_j == 0

    # Weighted closure of the DS curve at the triple common cubic.
    f_lam = zz**6 + 4 * lam * zz**4 + 10 * lam**2 * zz**2 + 6 * lam**3
    g_lam = (
        zz**9
        + 6 * lam * zz**7
        + 21 * lam**2 * zz**5
        + 35 * lam**3 * zz**3
        + sp.Rational(63, 2) * lam**4 * zz
    )
    h_lam = sp.factor(f_lam**3 - g_lam**2)
    w_lam = sp.factor(2 * f_lam * sp.diff(g_lam, zz) - 3 * sp.diff(f_lam, zz) * g_lam)
    assert sp.expand(
        h_lam
        - sp.Rational(27, 4)
        * lam**7
        * (4 * zz**4 + 13 * lam * zz**2 + 32 * lam**2)
    ) == 0
    assert w_lam == 378 * lam**7
    assert f_lam.subs(zz, 0) == 6 * lam**3
    assert g_lam.subs(zz, 0) == 0
    assert sp.factor(sp.resultant(f_lam, g_lam, zz)) == (
        sp.Rational(3**9 * 7**2, 2**5) * lam**27
    )

    # Weighted Euler and the pure-DS source ODE.
    assert sp.expand(
        zz * sp.diff(f_lam, zz) + 2 * lam * sp.diff(f_lam, lam) - 6 * f_lam
    ) == 0
    assert sp.expand(
        zz * sp.diff(g_lam, zz) + 2 * lam * sp.diff(g_lam, lam) - 9 * g_lam
    ) == 0
    j_lam_z = sp.factor(
        sp.diff(f_lam, lam) * sp.diff(g_lam, zz)
        - sp.diff(f_lam, zz) * sp.diff(g_lam, lam)
    )
    assert j_lam_z == 567 * lam**6

    # Kummer descent lambda=s^2 q turns 567*s*lambda^6*lambda'=j
    # into 189*h^4*q^6*(2h'q+3hq')=j.
    hh0 = sp.Function("hh0")(x)
    qq0 = sp.Function("qq0")(x)
    source_factor = sp.expand(
        189
        * hh0**4
        * qq0**6
        * (2 * sp.diff(hh0, x) * qq0 + 3 * hh0 * sp.diff(qq0, x))
    )
    # Direct differentiation of lambda^7=s^14 q^7=h^4 s^2 q^7,
    # after multiplying (lambda^7)'=j/(81s) by 81s.
    descended_factor = sp.expand(
        81
        * 7
        * hh0**4
        * qq0**6
        * (sp.Rational(2, 3) * sp.diff(hh0, x) * qq0 + hh0 * sp.diff(qq0, x))
    )
    assert sp.expand(source_factor - descended_factor) == 0

    # Local valuation arithmetic used in the pure-DS exclusion.
    kval = sp.symbols("kval", integer=True, positive=True)
    eval_ = 3 + 7 * kval
    nval = -2 - 5 * kval
    assert sp.expand(5 * eval_ + 7 * nval - 1) == 0
    assert sp.expand(2 * eval_ + 3 * nval) == -kval
    rcount, ksum = sp.symbols("rcount ksum", integer=True, positive=True)
    total_e = 3 * rcount + 7 * ksum
    total_n = -2 * rcount - 5 * ksum
    assert sp.expand(5 * total_e + 7 * total_n - 1) == rcount - 1
    # Smallest history-compatible cube case: k=3, h=x^24, q=x^-17,
    # s=x^8, lambda=x^-1 gives a constant source Jacobian factor.
    xx = sp.symbols("xx", nonzero=True)
    h_ctrl, q_ctrl, s_ctrl, lam_ctrl = xx**24, xx**-17, xx**8, xx**-1
    pure_ds_source = sp.factor(
        567 * s_ctrl * lam_ctrl**6 * sp.diff(lam_ctrl, xx)
    )
    descended_ctrl = sp.factor(
        189
        * h_ctrl**4
        * q_ctrl**6
        * (2 * sp.diff(h_ctrl, xx) * q_ctrl + 3 * h_ctrl * sp.diff(q_ctrl, xx))
    )
    assert pure_ds_source == -567 and descended_ctrl == -567

    # At the remaining cube controls, the four boundary valuations are
    # ordered solely by w=2*nu+ell.  Unless w=0 their minimum is unique;
    # when w=0, regularity of both boundaries would require a common root
    # of f_1,g_1, already excluded by their nonzero resultant.
    nu, ell = sp.symbols("nu ell", integer=True, positive=True)
    boundary_vals = sp.Matrix(
        [6 * nu, -ell + 4 * nu, -2 * ell + 2 * nu, -3 * ell]
    )
    wval = 2 * nu + ell
    assert boundary_vals + sp.ones(4, 1) * 3 * ell == sp.Matrix(
        [3 * wval, 2 * wval, wval, 0]
    )

    # The Wronskian/DS differential identity, with the exact sign used here.
    ff = sp.Function("ff")(x)
    gg = sp.Function("gg")(x)
    hh = ff**3 - gg**2
    ww = 2 * ff * sp.diff(gg, x) - 3 * sp.diff(ff, x) * gg
    assert sp.simplify(ff * sp.diff(hh, x) - 3 * sp.diff(ff, x) * hh + ww * gg) == 0

    # Squarefree factorization/orbit degree is independent of discriminant.
    k_irred = z**3 - 2
    k_mixed = z * (z**2 - 2)
    k_split = z * (z - 1) * (z + 1)
    assert sp.discriminant(k_irred, z) != 0
    assert sp.discriminant(k_mixed, z) != 0
    assert sp.discriminant(k_split, z) != 0
    assert [sp.degree(f, z) for f, _ in sp.factor_list(k_irred, z)[1]] == [3]
    assert sorted(sp.degree(f, z) for f, _ in sp.factor_list(k_mixed, z)[1]) == [1, 2]
    assert sorted(sp.degree(f, z) for f, _ in sp.factor_list(k_split, z)[1]) == [1, 1, 1]

    # Singular strata: exact non-common-cubic two-jets surviving J=0 mod eps^3.
    # Double root, with the boundary root chosen to be the simple root z=-2t.
    Kd = sp.expand((z - t) ** 2 * (z + 2 * t))
    rad_d = sp.expand((z - t) * (z + 2 * t))
    phi_d = sp.expand(rad_d * t**4)
    psi1_d = sp.Rational(3, 2) * Kd * phi_d
    psi2_d = sp.Rational(3, 8) * t**8 * (z + 2 * t)
    Fd = sp.expand(Kd**2 + eps * phi_d)
    Gd = sp.expand(Kd**3 + eps * psi1_d + eps**2 * psi2_d)
    Jd = sp.factor(jac(Fd, Gd, t, z))
    assert Jd == -sp.Rational(9, 8) * eps**3 * t**11 * (z + 2 * t) * (5 * t + 4 * z)
    assert Fd.subs(z, -2 * t) == 0 and Gd.subs(z, -2 * t) == 0
    assert sp.rem(phi_d.subs(t, 1), Kd.subs(t, 1), z) != 0

    # Triple root, boundary z=0.
    Kt = z**3
    phi_t = z**2 * t**4
    psi1_t = sp.Rational(3, 2) * Kt * phi_t
    psi2_t = sp.Rational(3, 8) * z * t**8
    Ft = sp.expand(Kt**2 + eps * phi_t)
    Gt = sp.expand(Kt**3 + eps * psi1_t + eps**2 * psi2_t)
    Jt = sp.factor(jac(Ft, Gt, t, z))
    assert Jt == -sp.Rational(9, 2) * eps**3 * t**11 * z**2
    assert Ft.subs(z, 0) == 0 and Gt.subs(z, 0) == 0
    assert sp.rem(phi_t.subs(t, 1), Kt.subs(t, 1), z) != 0

    print("PASS-GCD3-69-FIRST-COMMON-CUBIC-GATE")
    print("normalization=KUMMER-ALIGNED-OR-CUBE-MISMATCH")
    print("binary_leading_structure=H^2,H^3")
    print("high_row_reduction=FIVE-COEFFICIENTS-PLUS-KAPPA")
    print("discriminant_strata=SQUAREFREE,DOUBLE,TRIPLE")
    print("full_cubic_boundary_reduction=TYPE-FAIL-WITHOUT-ORBIT-DEGREE-3")
    print("linear_constant_row=TANGENT-ONLY-NONZERO-COKERNEL-CLASS")
    print("squarefree_quadratic_residue=RHS-FILTRATION-CONDITIONAL")
    print("double_and_triple_component_residue=TWO-JET-SURVIVORS")
    print("nonlinear_constant_w_bypass=UNIQUE-ORDER3-DS-CURVE")
    print("ds_first_constant_order=lambda^7=epsilon^14")
    print("ds_persistent_common_boundary_root=false")
    print("pure_ds_source_ode=(lambda^7)'=j/(81s)")
    print("pure_ds_noncube_branch=VALUATION-EMPTY")
    print("pure_ds_cube_branch=POLYNOMIAL-BOUNDARY-EMPTY")
    print("nonlinear_69_closure=false")
    print("keller_pair_found=false")
    print("jc2_inference=false")


if __name__ == "__main__":
    main()
