#!/usr/bin/env python3
"""Exact replay for TD6-TWO-CHART-FIRST-BAND (2026-08-24).

The calculation is deliberately finite.  One coefficient vector for each of
f and g in the fixed SP-2 rectangles is transported into both infinity
charts.  The first possible Jacobian coefficient at each end is imposed, but
no later Jacobian row is used.

Everything is over Q via fractions.Fraction.  The sparse row reducer uses the
least numbered variable as pivot and sets every free variable to zero, so the
reported witness is deterministic.
"""

from fractions import Fraction as Q
from hashlib import sha256
from math import comb, factorial


# ---------------------------------------------------------------------------
# Frozen pairing and chart choices

CENTER = (Q(1), Q(1), Q(1))
F1_CHAIN = Q(1)
F1_ORBIT_A = Q(2)
F1_ORBIT_B = Q(28, 25)
POLE_A = Q(1, 9)


def univar_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def univar_pow(a, n):
    out = [Q(1)]
    for _ in range(n):
        out = univar_mul(out, a)
    return out


def univar_deriv(a):
    return [Q(i + 1) * a[i + 1] for i in range(len(a) - 1)]


def univar_sub(a, b):
    n = max(len(a), len(b))
    return [
        (a[i] if i < len(a) else Q(0))
        - (b[i] if i < len(b) else Q(0))
        for i in range(n)
    ]


def fifth_factor(a):
    return [-a] + [Q(0)] * 4 + [Q(1)]


# The SP-2 II(a), k=2, nu=5 reduced pattern.  The chain orbit is squared.
P_REDUCED = univar_mul(
    univar_mul(fifth_factor(F1_CHAIN), fifth_factor(F1_CHAIN)),
    univar_mul(fifth_factor(F1_ORBIT_A), fifth_factor(F1_ORBIT_B)),
)
F1_F_PATTERN = univar_pow(P_REDUCED, 3)
F1_G_PATTERN = univar_pow(P_REDUCED, 5)

# Taylor transport at eta=1.  With eta=1+zeta*r^12, the reduced pattern
# starts L*zeta^2*r^24.  Thus the transported f/g top scales are L^3,L^5.
TAYLOR_L = (
    Q(25)
    * (F1_CHAIN - F1_ORBIT_A)
    * (F1_CHAIN - F1_ORBIT_B)
)
POLE_F_SCALE = TAYLOR_L**3
POLE_G_SCALE = TAYLOR_L**5

# The r9/M2 pole patterns, normalized so 3*p*q' - 5*p'*q = 25.  This
# matches det d(x,y)/d(r,zeta) = -25*r^-9 in the chosen pole chart.
POLE_F_PATTERN = [Q(0)] * 7
POLE_F_PATTERN[1] = -POLE_F_SCALE * POLE_A
POLE_F_PATTERN[6] = POLE_F_SCALE
POLE_G_PATTERN = [Q(0)] * 11
POLE_G_PATTERN[0] = POLE_G_SCALE * Q(5, 9) * POLE_A**2
POLE_G_PATTERN[5] = -POLE_G_SCALE * Q(5, 3) * POLE_A
POLE_G_PATTERN[10] = POLE_G_SCALE


# ---------------------------------------------------------------------------
# Source maps from fixed Q[x,y] rectangles

_X_POWER_CACHE = {}


def x_power_expansion(i):
    """Expansion of (c1*s+c2*s^2+c3*s^3+t*s^4)^i.

    Return {(s_degree, t_degree): coefficient}.  The three centering
    coefficients are the same for every f/g term and every x-side branch.
    """
    if i in _X_POWER_CACHE:
        return _X_POWER_CACHE[i]
    c1, c2, c3 = CENTER
    out = {}
    for kt in range(i + 1):
        for a2 in range(i - kt + 1):
            for a3 in range(i - kt - a2 + 1):
                a1 = i - kt - a2 - a3
                coeff = Q(
                    factorial(i),
                    factorial(kt)
                    * factorial(a1)
                    * factorial(a2)
                    * factorial(a3),
                )
                coeff *= c1**a1 * c2**a2 * c3**a3
                if not coeff:
                    continue
                sdeg = i + a2 + 2 * a3 + 3 * kt
                key = (sdeg, kt)
                out[key] = out.get(key, Q(0)) + coeff
    _X_POWER_CACHE[i] = out
    return out


def add_to_row(rows, key, variable, coefficient):
    if not coefficient:
        return
    row, _ = rows.setdefault(key, ({}, Q(0)))
    row[variable] = row.get(variable, Q(0)) + coefficient


def set_rhs(rows, key, value):
    row, _ = rows.setdefault(key, ({}, Q(0)))
    rows[key] = (row, Q(value))


def build_transport(imax, jmax, d, x_boundary, f1_pattern, pole_pattern):
    """Build one polynomial's two-chart affine transport system.

    Global monomials are x^i*y^j, 0<=i<=imax, 0<=j<=jmax.

    x-side: y=s^-1, x=s+s^2+s^3+t*s^4.
    F1 side: x=q^-5, y=eta*q.
    pole side: x=r^-25, y=r^5+zeta*r^17.
    """
    nvars = (imax + 1) * (jmax + 1)

    def vid(i, j):
        return i * (jmax + 1) + j

    rows = {}

    # Holomorphy through s=0 and the exact x-side boundary pattern.
    for i in range(imax + 1):
        xp = x_power_expansion(i)
        for j in range(jmax + 1):
            for (sdeg, tdeg), coeff in xp.items():
                exponent = sdeg - j
                if exponent <= 0:
                    add_to_row(rows, ("X", exponent, tdeg), vid(i, j), coeff)
    for key in list(rows):
        if key[0] == "X" and key[1] == 0:
            set_rhs(rows, key, x_boundary.get(key[2], Q(0)))

    # First y-side terminal vertex: q^(5d) h(q^-5,eta*q).
    pole_order = 5 * d
    for i in range(imax + 1):
        for j in range(jmax + 1):
            exponent = -5 * i + j
            if exponent <= -pole_order:
                add_to_row(rows, ("F1", exponent, j), vid(i, j), Q(1))
    for eta_degree, coeff in enumerate(f1_pattern):
        set_rhs(rows, ("F1", -pole_order, eta_degree), coeff)

    # r9 pole vertex.  The eleven dead-stretch coefficients at r^6,...,r^16
    # are specialized to zero, a licensed fully specified chain choice.
    cutoff = -d
    for i in range(imax + 1):
        for j in range(jmax + 1):
            base = -25 * i + 5 * j
            for zeta_degree in range(j + 1):
                exponent = base + 12 * zeta_degree
                if exponent <= cutoff:
                    add_to_row(
                        rows,
                        ("F0", exponent, zeta_degree),
                        vid(i, j),
                        Q(comb(j, zeta_degree)),
                    )
                else:
                    break
    for zeta_degree, coeff in enumerate(pole_pattern):
        set_rhs(rows, ("F0", cutoff, zeta_degree), coeff)

    packed = []
    for key, (row, rhs) in rows.items():
        row = {v: c for v, c in row.items() if c}
        if row or rhs:
            packed.append((key, row, rhs))
    return nvars, packed


def x_chart_coefficient(imax, jmax, exponent, tdegree):
    """Linear form for [s^exponent*t^tdegree] in the x-side chart."""
    out = {}
    for i in range(imax + 1):
        for (sdeg, kt), coeff in x_power_expansion(i).items():
            if kt != tdegree:
                continue
            j = sdeg - exponent
            if 0 <= j <= jmax:
                v = i * (jmax + 1) + j
                out[v] = out.get(v, Q(0)) + coeff
    return out


def exact_solve(nvars, rows, allow_inconsistent=False):
    """Sparse exact echelon solve; free variables are deterministically 0."""
    pivots = {}
    for key, row0, rhs0 in rows:
        row = dict(row0)
        rhs = rhs0
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs = pivots[pivot]
            for v, coeff in old_row.items():
                new = row.get(v, Q(0)) - factor * coeff
                if new:
                    row[v] = new
                else:
                    row.pop(v, None)
            rhs -= factor * old_rhs
        if not row:
            if rhs:
                if allow_inconsistent:
                    return None, pivots, (key, rhs)
                raise AssertionError(("inconsistent", key, rhs, len(pivots)))
            continue
        pivot = min(row)
        lead = row[pivot]
        pivots[pivot] = (
            {v: coeff / lead for v, coeff in row.items()},
            rhs / lead,
        )

    solution = {}
    for pivot in sorted(pivots, reverse=True):
        row, rhs = pivots[pivot]
        solution[pivot] = rhs - sum(
            coeff * solution.get(v, Q(0))
            for v, coeff in row.items()
            if v != pivot
        )

    for key, row, rhs in rows:
        got = sum(coeff * solution.get(v, Q(0)) for v, coeff in row.items())
        assert got == rhs, ("row replay", key, got, rhs)
    assert all(0 <= v < nvars for v in solution)
    return solution, pivots, None


def polynomial_from_solution(solution, offset, imax, jmax):
    out = {}
    for i in range(imax + 1):
        for j in range(jmax + 1):
            coeff = solution.get(offset + i * (jmax + 1) + j, Q(0))
            if coeff:
                out[(i, j)] = coeff
    return out


# ---------------------------------------------------------------------------
# Independent sparse expansion and Jacobian verification


def poly_deriv(poly, axis):
    out = {}
    for (i, j), coeff in poly.items():
        degree = i if axis == 0 else j
        if not degree:
            continue
        key = (i - 1, j) if axis == 0 else (i, j - 1)
        out[key] = out.get(key, Q(0)) + degree * coeff
    return out


def poly_mul(a, b):
    out = {}
    for (i, j), ca in a.items():
        for (k, ell), cb in b.items():
            key = (i + k, j + ell)
            out[key] = out.get(key, Q(0)) + ca * cb
    return {key: value for key, value in out.items() if value}


def poly_sub(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Q(0)) - value
    return {key: value for key, value in out.items() if value}


def x_chart_expand(poly, max_exponent):
    out = {}
    for (i, j), coeff in poly.items():
        for (sdeg, tdeg), chart_coeff in x_power_expansion(i).items():
            exponent = sdeg - j
            if exponent <= max_exponent:
                key = (exponent, tdeg)
                out[key] = out.get(key, Q(0)) + coeff * chart_coeff
    return {key: value for key, value in out.items() if value}


def f1_chart_expand(poly, max_exponent):
    out = {}
    for (i, j), coeff in poly.items():
        exponent = -5 * i + j
        if exponent <= max_exponent:
            key = (exponent, j)
            out[key] = out.get(key, Q(0)) + coeff
    return {key: value for key, value in out.items() if value}


def pole_chart_expand(poly, max_exponent):
    out = {}
    for (i, j), coeff in poly.items():
        base = -25 * i + 5 * j
        for zeta_degree in range(j + 1):
            exponent = base + 12 * zeta_degree
            if exponent <= max_exponent:
                key = (exponent, zeta_degree)
                out[key] = out.get(key, Q(0)) + coeff * comb(j, zeta_degree)
            else:
                break
    return {key: value for key, value in out.items() if value}


def band(expansion, exponent):
    return {
        degree: coeff
        for (found_exponent, degree), coeff in expansion.items()
        if found_exponent == exponent
    }


def digest_band(row):
    payload = "".join(
        f"{degree}:{coeff.numerator}/{coeff.denominator}\n"
        for degree, coeff in sorted(row.items())
    )
    return sha256(payload.encode()).hexdigest()


def witness_digest(f, g):
    payload = "f\n" + "".join(
        f"{i},{j}:{c.numerator}/{c.denominator}\n"
        for (i, j), c in sorted(f.items())
    )
    payload += "g\n" + "".join(
        f"{i},{j}:{c.numerator}/{c.denominator}\n"
        for (i, j), c in sorted(g.items())
    )
    return sha256(payload.encode()).hexdigest(), len(payload)


def main():
    assert CENTER == (Q(1), Q(1), Q(1))
    assert TAYLOR_L == 3
    assert POLE_F_SCALE == 27 and POLE_G_SCALE == 243
    assert len(F1_F_PATTERN) == 61 and len(F1_G_PATTERN) == 101
    assert F1_F_PATTERN[-1] == F1_G_PATTERN[-1] == 1

    # Exact r9 pole ODE and chart normalization.
    pole_ode = univar_sub(
        [3 * c for c in univar_mul(POLE_F_PATTERN, univar_deriv(POLE_G_PATTERN))],
        [5 * c for c in univar_mul(univar_deriv(POLE_F_PATTERN), POLE_G_PATTERN)],
    )
    assert pole_ode[0] == 25 and all(c == 0 for c in pole_ode[1:])

    nf, rows_f = build_transport(
        15, 60, 3, {15: Q(1)}, F1_F_PATTERN, POLE_F_PATTERN
    )
    ng, rows_g = build_transport(
        25, 100, 5, {1: Q(1), 25: Q(1)}, F1_G_PATTERN, POLE_G_PATTERN
    )
    sol_f, piv_f, _ = exact_solve(nf, rows_f)
    sol_g, piv_g, _ = exact_solve(ng, rows_g)
    assert len(piv_f) == 946 and len(piv_g) == 2524

    offset = nf
    rows = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (('g',) + key, {offset + v: c for v, c in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]

    # First possible x-chart Jacobian band.  Since
    #   dx wedge dy = s^2 ds wedge dt,
    # exact J=1 first requires [s^0](F_s G_t-F_t G_s)=0, equivalently
    # [s^-2]J=0.  With p=t^15 and q=t+t^25 this is
    #   f_1(t)*(1+25t^24) - 15t^14*g_1(t) = 0.
    first_j_rows = []
    for degree in range(40):
        row = {}

        def add(variable, coefficient):
            if coefficient:
                row[variable] = row.get(variable, Q(0)) + coefficient

        for f_degree, multiplier in ((degree, Q(1)), (degree - 24, Q(25))):
            if 0 <= f_degree <= 15:
                for v, coeff in x_chart_coefficient(15, 60, 1, f_degree).items():
                    add(v, multiplier * coeff)
        g_degree = degree - 14
        if 0 <= g_degree <= 25:
            for v, coeff in x_chart_coefficient(25, 100, 1, g_degree).items():
                add(offset + v, -Q(15) * coeff)
        first_j_rows.append((("JX-FIRST", degree), row, Q(0)))
    rows.extend(first_j_rows)

    solution, pivots, _ = exact_solve(nf + ng, rows)
    assert len(pivots) == 3508
    assert nf + ng - len(pivots) == 94

    f = polynomial_from_solution(solution, 0, 15, 60)
    g = polynomial_from_solution(solution, offset, 25, 100)
    assert f[(15, 60)] == 1 and g[(25, 100)] == 1

    # Replay every local target directly from the resulting global polynomials.
    xf = x_chart_expand(f, 1)
    xg = x_chart_expand(g, 1)
    assert not [key for key in xf if key[0] < 0]
    assert not [key for key in xg if key[0] < 0]
    assert band(xf, 0) == {15: Q(1)}
    assert band(xg, 0) == {1: Q(1), 25: Q(1)}

    y1f = f1_chart_expand(f, -15)
    y1g = f1_chart_expand(g, -25)
    assert not [key for key in y1f if key[0] < -15]
    assert not [key for key in y1g if key[0] < -25]
    assert band(y1f, -15) == {
        i: c for i, c in enumerate(F1_F_PATTERN) if c
    }
    assert band(y1g, -25) == {
        i: c for i, c in enumerate(F1_G_PATTERN) if c
    }

    y0f = pole_chart_expand(f, -3)
    y0g = pole_chart_expand(g, -5)
    assert not [key for key in y0f if key[0] < -3]
    assert not [key for key in y0g if key[0] < -5]
    assert band(y0f, -3) == {
        i: c for i, c in enumerate(POLE_F_PATTERN) if c
    }
    assert band(y0g, -5) == {
        i: c for i, c in enumerate(POLE_G_PATTERN) if c
    }

    # Independent global differentiation.  At the pole end J starts with 1;
    # at the centered end the first possible pole s^-2 is absent.
    jacobian = poly_sub(
        poly_mul(poly_deriv(f, 0), poly_deriv(g, 1)),
        poly_mul(poly_deriv(f, 1), poly_deriv(g, 0)),
    )
    xj = x_chart_expand(jacobian, 0)
    assert not band(xj, -2)
    assert not [key for key in xj if key[0] < -2]
    pole_j = pole_chart_expand(jacobian, 1)
    assert not [key for key in pole_j if key[0] < 0]
    assert band(pole_j, 0) == {0: Q(1)}

    # Explicit fail-closed stop: these are the next un-imposed rows, and the
    # selected witness violates both.  In particular it is not a Keller pair.
    x_next = band(x_chart_expand(jacobian, 1), -1)
    pole_next = band(pole_j, 1)
    assert x_next and pole_next

    witness_sha, witness_bytes = witness_digest(f, g)
    print("TD6-TWO-CHART-FIRST-BAND: PASS")
    print("verdict = NONEMPTY-WITNESS")
    print(f"transport.f = rank {len(piv_f)} / {nf}; nullity {nf-len(piv_f)}")
    print(f"transport.g = rank {len(piv_g)} / {ng}; nullity {ng-len(piv_g)}")
    print(
        "shared_first_J = rank 3508 / 3602; nullity 94; "
        f"independent_J_rows={len(pivots)-len(piv_f)-len(piv_g)}"
    )
    print(f"witness.terms = f:{len(f)} g:{len(g)}")
    print(f"witness.sha256 = {witness_sha}")
    print(f"witness.serialized_bytes = {witness_bytes}")
    print(f"next_x_row = s^-1 NONZERO terms={len(x_next)} sha256={digest_band(x_next)}")
    print(
        f"next_pole_row = r^1 NONZERO terms={len(pole_next)} "
        f"sha256={digest_band(pole_next)}"
    )
    print("global_J_exact = false")
    print("terminal_class_realized = false")


if __name__ == "__main__":
    main()
