#!/usr/bin/env python3
"""Exact replay for the bounded GCD3-(6,9) cube-core mismatch gate.

This derives the complete Faber high-row form, integrates the five remaining
rows into Laurent coefficients, checks the target-translation quotient, and
freezes controls.  It does not enumerate polynomial trajectories or claim
that the cube core, (6,9), or JC2 is closed.
"""

from __future__ import annotations

import sympy as sp


def coeff(expr: sp.Expr, var: sp.Symbol, power: int) -> sp.Expr:
    return sp.Poly(sp.expand(expr), var).coeff_monomial(var**power)


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


def polynomial_part_at_infinity(expr: sp.Expr, u: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    """Return the nonnegative-z part of a Laurent series written in u=1/z."""
    truncated = sp.series(expr, u, 0, 1).removeO()
    kept = sum(
        term
        for term in sp.Add.make_args(sp.expand(truncated))
        if term.as_powers_dict().get(u, 0) <= 0
    )
    return sp.expand(kept.subs(u, 1 / z))


def main() -> None:
    z, u = sp.symbols("z u")
    d, q = sp.symbols("d q")
    avec = sp.symbols("a0:5")
    bvec = sp.symbols("b0:8")
    cvec = sp.symbols("c0:8")
    vavec = sp.symbols("va0:5")
    vbvec = sp.symbols("vb0:8")
    a0, a1, a2, a3, a4 = avec

    f = z**6 + a4 * z**4 + a3 * z**3 + a2 * z**2 + a1 * z + a0
    f_velocity = sum(vavec[i] * z**i for i in range(5))

    # w=f^(1/6)=z+O(z^-1). F_j is the polynomial part of w^j.
    U = a4 * u**2 + a3 * u**3 + a2 * u**4 + a1 * u**5 + a0 * u**6
    w_series = u**-1 * sp.series((1 + U) ** sp.Rational(1, 6), u, 0, 18).removeO()
    F = [polynomial_part_at_infinity(w_series**j, u, z) for j in range(10)]
    assert F[0] == 1 and F[1] == z and F[6] == f

    H_coefficients = {9: sp.Integer(1), 8: d, **{j: cvec[j] for j in range(8)}}
    g_faber = sp.expand(F[9] + d * F[8] + sum(cvec[j] * F[j] for j in range(8)))
    assert coeff(g_faber, z, 9) == 1
    assert coeff(g_faber, z, 8) == d

    # Independently integrate the triangular high source rows.
    g_template = z**9 + d * z**8 + sum(bvec[i] * z**i for i in range(8))
    independent_g_velocity = sum(vbvec[i] * z**i for i in range(8))
    source_template = sp.Poly(
        sp.expand(
            f_velocity * sp.diff(g_template, z)
            - sp.diff(f, z) * independent_g_velocity
        ),
        z,
    )
    solved_b: dict[sp.Symbol, sp.Expr] = {}
    solved_vb: dict[sp.Symbol, sp.Expr] = {}
    variable_order = [a4, a3, a2, a1, a0]
    velocity_for = {avec[i]: vavec[i] for i in range(5)}
    for bj, power in zip(range(7, -1, -1), range(12, 4, -1)):
        row = sp.expand(
            source_template.coeff_monomial(z**power).subs(solved_b).subs(solved_vb)
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

    g_integrated = sp.expand(g_template.subs(solved_b))
    assert sp.expand(g_integrated - g_faber) == 0
    assert coeff(g_faber, z, 7) == sp.Rational(3, 2) * a4 + cvec[7]
    assert coeff(g_faber, z, 6) == (
        sp.Rational(3, 2) * a3 + sp.Rational(4, 3) * d * a4 + cvec[6]
    )
    assert coeff(g_faber, z, 5) == (
        sp.Rational(3, 2) * a2
        + sp.Rational(4, 3) * d * a3
        + sp.Rational(3, 8) * a4**2
        + sp.Rational(7, 6) * cvec[7] * a4
        + cvec[5]
    )

    g_velocity = sum(sp.diff(g_faber, avec[i]) * vavec[i] for i in range(5))
    source_j = sp.Poly(
        sp.expand(f_velocity * sp.diff(g_faber, z) - sp.diff(f, z) * g_velocity),
        z,
    )
    assert all(source_j.coeff_monomial(z**power) == 0 for power in range(12, 4, -1))

    # Legal target gauges. Q-c6 P and Q-c0 remove c6,c0. P+q acts as below.
    translation = {
        a0: a0 + q,
        cvec[3]: cvec[3] - sp.Rational(3, 2) * q,
        cvec[2]: cvec[2] - sp.Rational(4, 3) * d * q,
        cvec[1]: cvec[1] - sp.Rational(7, 6) * cvec[7] * q,
        cvec[0]: cvec[0] - cvec[6] * q,
    }
    assert sp.expand(g_faber.subs(translation, simultaneous=True) - g_faber) == 0
    mu = sp.expand(8 * d * cvec[3] - 9 * cvec[2])
    nu = sp.expand(8 * d * cvec[1] - 7 * cvec[7] * cvec[2])
    assert sp.expand(mu.subs(translation, simultaneous=True) - mu) == 0
    assert sp.expand(nu.subs(translation, simultaneous=True) - nu) == 0
    barred_a0 = a0 + 3 * cvec[2] / (4 * d)
    barred_c3 = cvec[3] - 9 * cvec[2] / (8 * d)
    barred_c1 = cvec[1] - 7 * cvec[7] * cvec[2] / (8 * d)
    assert all(
        sp.expand(expr.subs(translation, simultaneous=True) - expr) == 0
        for expr in (barred_a0, barred_c3, barred_c1)
    )
    # The d=0 quotient is a separate stratum and uses no division by d.
    nu0 = sp.expand(9 * cvec[1] - 7 * cvec[7] * cvec[3])
    assert sp.expand(nu0.subs(translation, simultaneous=True).subs(d, 0) - nu0.subs(d, 0)) == 0

    # Remove the two Q gauges for the lower-row calculation.
    lower_g = sp.expand(g_faber.subs({cvec[6]: 0, cvec[0]: 0}))
    lower_g_velocity = sum(sp.diff(lower_g, avec[i]) * vavec[i] for i in range(5))
    lower_j = sp.Poly(
        sp.expand(f_velocity * sp.diff(lower_g, z) - sp.diff(f, z) * lower_g_velocity),
        z,
    )
    lower_rows = sp.Matrix(
        [sp.expand(lower_j.coeff_monomial(z**power)) for power in range(4, -1, -1)]
    )

    # If H(w)-g=sum r_n w^-n, the polynomial parts A_n=[f_z w^-n]_+
    # give J=sum r_n' A_n.  Compute A_1,...,A_5 independently.
    fz_u = sp.diff(f, z).subs(z, 1 / u)
    A: list[sp.Expr] = []
    for n in range(1, 6):
        wn = u**n * sp.series((1 + U) ** (-sp.Rational(n, 6)), u, 0, 7).removeO()
        A.append(polynomial_part_at_infinity(sp.expand(fz_u * wn), u, z))
    assert A == [
        6 * z**4 + 3 * a4 * z**2 + 2 * a3 * z + a2 - a4**2 / 12,
        6 * z**3 + 2 * a4 * z + a3,
        6 * z**2 + a4,
        6 * z,
        6,
    ]
    coefficient_matrix = sp.Matrix(
        [[coeff(A[n], z, power) for n in range(5)] for power in range(4, -1, -1)]
    )
    assert coefficient_matrix.det() == 6**5

    r_velocity = coefficient_matrix.inv() * lower_rows
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
    active_parameters = [d, cvec[7], cvec[5], cvec[4], cvec[3], cvec[2], cvec[1]]
    term_counts = [
        len(sp.Poly(sp.expand(item), *avec, *active_parameters).terms()) for item in r
    ]
    assert term_counts == [31, 36, 48, 55, 69]

    # Exact regular local survivor: d=1, other constants zero, a=(0,0,0,0,1).
    zero_constants = {cvec[i]: 0 for i in range(8)}
    point = {a0: 0, a1: 0, a2: 0, a3: 0, a4: 1, d: 1, **zero_constants}
    r_values = [sp.factor(item.subs(point)) for item in r]
    assert r_values == [
        -sp.Rational(3, 256),
        -sp.Rational(8, 729),
        sp.Rational(5, 1024),
        sp.Rational(20, 6561),
        -sp.Rational(5, 6144),
    ]
    pfaffian_matrix = sp.Matrix(
        [[lower_rows[row].coeff(vavec[col]).subs(point) for col in range(5)] for row in range(5)]
    )
    assert pfaffian_matrix.det() == sp.Rational(92286875, 25048249270272)
    tangent = pfaffian_matrix.inv() * sp.Matrix([0, 0, 0, 0, 1])
    assert list(tangent) == [
        sp.Rational(128, 3),
        sp.Rational(131072, 729),
        sp.Rational(194683904, 177147),
        sp.Rational(1221232033792, 4485142125),
        sp.Rational(1689034934081536, 1089889536375),
    ]

    # Primitive polynomial cube-core rejection control: high rows and
    # polynomial boundaries survive, but both coordinates depend on z=xy.
    x, y = sp.symbols("x y")
    primitive_P = (x * y) ** 6
    primitive_Q = (x * y) ** 9 + d * (x * y) ** 8
    primitive_J = sp.expand(
        sp.diff(primitive_P, x) * sp.diff(primitive_Q, y)
        - sp.diff(primitive_P, y) * sp.diff(primitive_Q, x)
    )
    assert primitive_J == 0

    # Monomial-core terminal control: 6 r5'=j/s integrates rationally for
    # s=C t^m, m>=2. The divisor argument excluding multiple distinct roots
    # is in the producer report.
    t, Ccore, jconst, m = sp.symbols("t Ccore jconst m", nonzero=True)
    monomial_r5 = jconst * t ** (1 - m) / (6 * Ccore * (1 - m))
    assert sp.simplify(6 * sp.diff(monomial_r5, t) - jconst / (Ccore * t**m)) == 0

    # First weighted d-deformation controls. Ordinary first-order motion is
    # obstructed on squarefree/double common points but ramified motion is
    # not tested; DS survives and triple is exceptional.
    r_zero_c = [sp.expand(item.subs(zero_constants)) for item in r[:4]]
    controls = {
        "DS": {a0: 6, a1: 0, a2: 10, a3: 0, a4: 4, d: 0},
        "COMMON_SQUAREFREE": {a0: 0, a1: 0, a2: 1, a3: 0, a4: 2, d: 0},
        "COMMON_DOUBLE": {a0: 4, a1: -12, a2: 9, a3: 4, a4: -6, d: 0},
        "TRIPLE": {a0: 0, a1: 0, a2: 0, a3: 0, a4: 0, d: 0},
    }
    expected_ranks = {
        "DS": (4, 4),
        "COMMON_SQUAREFREE": (0, 1),
        "COMMON_DOUBLE": (0, 1),
        "TRIPLE": (0, 0),
    }
    for name, control in controls.items():
        linear = sp.Matrix(
            [[sp.diff(r_zero_c[i], avec[j]).subs(control) for j in range(5)] for i in range(4)]
        )
        d_load = sp.Matrix([-sp.diff(r_zero_c[i], d).subs(control) for i in range(4)])
        assert (linear.rank(), linear.row_join(d_load).rank()) == expected_ranks[name]
    ds_control = controls["DS"]
    ds_linear = sp.Matrix(
        [[sp.diff(r_zero_c[i], avec[j]).subs(ds_control) for j in range(5)] for i in range(4)]
    )
    ds_load = sp.Matrix([-sp.diff(r_zero_c[i], d).subs(ds_control) for i in range(4)])
    ds_v = sp.Matrix(
        [0, -sp.Rational(660128, 531441), 0, -sp.Rational(50176, 531441), 0]
    )
    assert ds_linear * ds_v == ds_load

    print("PASS-GCD3-69-CUBE-MISMATCH-GATE")
    print("high_row_normal_form=g=[H(f^(1/6))]_+")
    print("pinned_constants=d,c7,c6,c5,c4,c3,c2,c1,c0")
    print("global_target_gauges=REMOVE-c6,c0-AND-QUOTIENT-P-TRANSLATION")
    print("d_nonzero_invariants=8d*c3-9c2,8d*c1-7c7*c2")
    print("d_zero_cube_core=OPEN-SEPARATE-STRATUM")
    print("lower_rows=r1'=r2'=r3'=r4'=0,6r5'=j/s")
    print("cube_core_terminal=s-CONSTANT-OR-SINGLE-ROOT-POWER")
    print("regular_local_formal_survivor=true")
    print("common_ramified_puiseux_strata=OPEN")
    print("cube_mismatch_closed=false")
    print("degree_69_closed=false")
    print("keller_pair_found=false")
    print("jc2_inference=false")


if __name__ == "__main__":
    main()
