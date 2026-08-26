#!/usr/bin/env python3
"""Exact replay for TD6-TWO-CHART-NEXT-ROW (2026-08-24).

This script keeps the frozen first-band specialization and rectangles.  It
parameterizes the full 94-dimensional affine solution space over Q, compiles
only [s^-1]J=0 and [r^1](J-1)=0, and checks a one-coefficient Q-infeasibility
certificate.  No finite-field inference is used.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
FIRST_BAND_REPLAY = (
    HERE.parent / "td6_two_chart_first_band_20260824" / "replay.py"
)
FIRST_BAND_SHA256 = (
    "c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735"
)
assert sha256(FIRST_BAND_REPLAY.read_bytes()).hexdigest() == FIRST_BAND_SHA256

spec = importlib.util.spec_from_file_location("td6_first_band", FIRST_BAND_REPLAY)
fb = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(fb)


def add_linear(row, variable, coefficient):
    if coefficient:
        row[variable] = row.get(variable, Q(0)) + coefficient
        if not row[variable]:
            row.pop(variable)


def build_first_band_system():
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25,
        100,
        5,
        {1: Q(1), 25: Q(1)},
        fb.F1_G_PATTERN,
        fb.POLE_G_PATTERN,
    )
    offset = nf
    rows = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (('g',) + key, {offset + v: c for v, c in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]

    for degree in range(40):
        row = {}
        for f_degree, multiplier in (
            (degree, Q(1)),
            (degree - 24, Q(25)),
        ):
            if 0 <= f_degree <= 15:
                for v, coefficient in fb.x_chart_coefficient(
                    15, 60, 1, f_degree
                ).items():
                    add_linear(row, v, multiplier * coefficient)
        g_degree = degree - 14
        if 0 <= g_degree <= 25:
            for v, coefficient in fb.x_chart_coefficient(
                25, 100, 1, g_degree
            ).items():
                add_linear(row, offset + v, -Q(15) * coefficient)
        rows.append((("JX-FIRST", degree), row, Q(0)))
    return nf, ng, rows_f, rows_g, rows


def add_affine(left, right, scale=Q(1)):
    constant = left[0] + scale * right[0]
    coefficients = dict(left[1])
    for parameter, coefficient in right[1].items():
        add_linear(coefficients, parameter, scale * coefficient)
    return constant, coefficients


def scale_affine(form, scale):
    return (
        scale * form[0],
        {
            parameter: scale * coefficient
            for parameter, coefficient in form[1].items()
            if scale * coefficient
        },
    )


def affine_parameterization(nvariables, rows):
    """Return the exact affine map from ordered free variables to all vars."""
    particular, pivots, _ = fb.exact_solve(nvariables, rows)
    free_variables = [v for v in range(nvariables) if v not in pivots]
    parameter_of = {v: k for k, v in enumerate(free_variables)}
    forms = [None] * nvariables

    # Each normalized pivot row has its pivot as its least variable, so every
    # other variable in it has already been expanded in this descending pass.
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (Q(0), {parameter_of[variable]: Q(1)})
            continue
        row, rhs = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other != variable:
                form = add_affine(form, forms[other], -coefficient)
        forms[variable] = form

    # Identity replay: every base equation must vanish coefficientwise in all
    # 94 parameters, not only at the free-variables-zero point.
    for key, row, rhs in rows:
        got = (Q(0), {})
        for variable, coefficient in row.items():
            got = add_affine(got, forms[variable], coefficient)
        assert got == (rhs, {}), ("affine base replay", key, got, rhs)

    # Parameter zero is exactly the prior deterministic witness.
    for variable, (constant, _) in enumerate(forms):
        assert constant == particular.get(variable, Q(0))

    return forms, free_variables, pivots


def combine_global_linear(row, forms, offset=0):
    out = (Q(0), {})
    for variable, coefficient in row.items():
        out = add_affine(out, forms[offset + variable], coefficient)
    return out


def x_band_forms(imax, jmax, exponent, forms, offset):
    return [
        combine_global_linear(
            fb.x_chart_coefficient(imax, jmax, exponent, degree),
            forms,
            offset,
        )
        for degree in range(imax + 1)
    ]


def pole_coefficient(imax, jmax, exponent, zeta_degree):
    row = {}
    for i in range(imax + 1):
        for j in range(jmax + 1):
            if (
                zeta_degree <= j
                and -25 * i + 5 * j + 12 * zeta_degree == exponent
            ):
                row[i * (jmax + 1) + j] = Q(comb(j, zeta_degree))
    return row


# Parameter-polynomial representation: a monomial is a sorted tuple of
# parameter indices.  Only degrees zero, one, and two can arise a priori.
def clean_polynomial(poly):
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def affine_polynomial(form):
    out = {(): form[0]} if form[0] else {}
    for parameter, coefficient in form[1].items():
        if coefficient:
            out[(parameter,)] = coefficient
    return out


def add_polynomial(left, right, scale=Q(1)):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Q(0)) + scale * coefficient
    return clean_polynomial(out)


def scale_polynomial(poly, scale):
    return clean_polynomial(
        {monomial: scale * coefficient for monomial, coefficient in poly.items()}
    )


def multiply_affine(left, right):
    out = {}
    for monomial_left, coefficient_left in affine_polynomial(left).items():
        for monomial_right, coefficient_right in affine_polynomial(right).items():
            monomial = tuple(sorted(monomial_left + monomial_right))
            out[monomial] = (
                out.get(monomial, Q(0)) + coefficient_left * coefficient_right
            )
    return clean_polynomial(out)


def compile_x_next_rows(f1, f2, g1, g2):
    """Compile [s^-1]J=0 in all forty possible t degrees.

    If F=p+s*f1+s^2*f2+... and G=q+s*g1+s^2*g2+..., then the
    coefficient of s in F_s*G_t-F_t*G_s is

      f1*g1' - f1'*g1 + 2*f2*q' - 2*p'*g2,

    with p=t^15 and q=t+t^25.
    """
    rows = []
    for degree in range(40):
        equation = {}
        for i, left in enumerate(f1):
            j = degree - i + 1
            if 1 <= j < len(g1):
                equation = add_polynomial(
                    equation,
                    multiply_affine(left, scale_affine(g1[j], Q(j))),
                )
        for i in range(1, len(f1)):
            j = degree - (i - 1)
            if 0 <= j < len(g1):
                equation = add_polynomial(
                    equation,
                    multiply_affine(scale_affine(f1[i], Q(i)), g1[j]),
                    -Q(1),
                )
        for i, form in enumerate(f2):
            if degree - i == 0:
                equation = add_polynomial(
                    equation, affine_polynomial(form), Q(2)
                )
            if degree - i == 24:
                equation = add_polynomial(
                    equation, affine_polynomial(form), Q(50)
                )
        g_degree = degree - 14
        if 0 <= g_degree < len(g2):
            equation = add_polynomial(
                equation, affine_polynomial(g2[g_degree]), -Q(30)
            )
        rows.append(equation)
    return rows


def compile_pole_next_rows(p1, q1):
    """Compile [r^1](J-1)=0 in all fourteen possible zeta degrees.

    For F=r^-3*p+r^-2*p1+... and G=r^-5*q+r^-4*q1+..., the r^-8
    local-wedge coefficient is

      -3*p*q1' - 2*p1*q' + 4*p'*q1 + 5*p1'*q.

    The chart determinant is exactly -25*r^-9.  We divide by -25 below so
    the compiled row is the actual r^1 Jacobian coefficient, not merely an
    equivalent local-wedge numerator.
    """
    p = fb.POLE_F_PATTERN
    q = fb.POLE_G_PATTERN
    rows = []
    for degree in range(14):
        equation = {}
        for i, coefficient in enumerate(p):
            j = degree - i + 1
            if coefficient and 1 <= j < len(q1):
                equation = add_polynomial(
                    equation,
                    affine_polynomial(q1[j]),
                    -Q(3) * coefficient * j,
                )
        for i, form in enumerate(p1):
            j = degree - i + 1
            if 1 <= j < len(q) and q[j]:
                equation = add_polynomial(
                    equation,
                    affine_polynomial(form),
                    -Q(2) * q[j] * j,
                )
        for i in range(1, len(p)):
            j = degree - (i - 1)
            if p[i] and 0 <= j < len(q1):
                equation = add_polynomial(
                    equation,
                    affine_polynomial(q1[j]),
                    Q(4) * i * p[i],
                )
        for i in range(1, len(p1)):
            j = degree - (i - 1)
            if 0 <= j < len(q) and q[j]:
                equation = add_polynomial(
                    equation,
                    affine_polynomial(p1[i]),
                    Q(5) * i * q[j],
                )
        rows.append(scale_polynomial(equation, -Q(1, 25)))
    return rows


def parameter_degree(rows):
    return max((len(monomial) for row in rows for monomial in row), default=-1)


def tangent_rows(rows):
    return [
        {
            monomial[0]: coefficient
            for monomial, coefficient in row.items()
            if len(monomial) == 1
        }
        for row in rows
    ]


def exact_rank(linear_rows, nparameters):
    packed = [
        (("tangent", index), row, Q(0))
        for index, row in enumerate(linear_rows)
        if row
    ]
    _, pivots, _ = fb.exact_solve(nparameters, packed)
    return len(pivots)


def fraction_text(value):
    return f"{value.numerator}/{value.denominator}"


def parameterization_digest(forms, free_variables):
    digest = sha256()
    digest.update(
        ("free=" + ",".join(map(str, free_variables)) + "\n").encode()
    )
    for variable, (constant, coefficients) in enumerate(forms):
        digest.update(f"v{variable}:{fraction_text(constant)}".encode())
        for parameter, coefficient in sorted(coefficients.items()):
            digest.update(
                f";u{parameter}:{fraction_text(coefficient)}".encode()
            )
        digest.update(b"\n")
    return digest.hexdigest()


def equations_digest(x_rows, pole_rows):
    digest = sha256()
    for family, rows in (("X", x_rows), ("P", pole_rows)):
        for degree, row in enumerate(rows):
            digest.update(f"{family},{degree}".encode())
            for monomial, coefficient in sorted(row.items()):
                name = "1" if not monomial else "*".join(
                    f"u{k}" for k in monomial
                )
                digest.update(f";{name}:{fraction_text(coefficient)}".encode())
            digest.update(b"\n")
    return digest.hexdigest()


def main():
    nf, ng, rows_f, rows_g, base_rows = build_first_band_system()
    nvariables = nf + ng
    forms, free_variables, pivots = affine_parameterization(
        nvariables, base_rows
    )
    assert nf == 976 and ng == 2626 and nvariables == 3602
    assert len(pivots) == 3508 and len(free_variables) == 94

    offset = nf
    f1 = x_band_forms(15, 60, 1, forms, 0)
    f2 = x_band_forms(15, 60, 2, forms, 0)
    g1 = x_band_forms(25, 100, 1, forms, offset)
    g2 = x_band_forms(25, 100, 2, forms, offset)

    # The key structural collapse: the first transverse jets are fixed on the
    # entire affine family.  One needed second-jet coefficient is fixed too.
    assert [(i, form) for i, form in enumerate(f1) if form != (Q(0), {})] == [
        (14, (Q(-384, 25), {}))
    ]
    assert [(i, form) for i, form in enumerate(g1) if form != (Q(0), {})] == [
        (0, (Q(-128, 125), {})),
        (24, (Q(-128, 5), {})),
    ]
    assert f2[13] == (Q(66927, 625), {})

    x_rows = compile_x_next_rows(f1, f2, g1, g2)
    assert len(x_rows) == 40
    assert sum(bool(row) for row in x_rows) == 37
    assert parameter_degree(x_rows) == 1
    assert not any(
        len(monomial) == 2 for row in x_rows for monomial in row
    )

    p1 = [
        combine_global_linear(
            pole_coefficient(15, 60, -2, degree), forms, 0
        )
        for degree in range(61)
    ]
    q1 = [
        combine_global_linear(
            pole_coefficient(25, 100, -4, degree), forms, offset
        )
        for degree in range(101)
    ]
    assert [i for i, form in enumerate(p1) if form != (Q(0), {})] == [4]
    assert [i for i, form in enumerate(q1) if form != (Q(0), {})] == [3, 8]

    pole_rows = compile_pole_next_rows(p1, q1)
    assert len(pole_rows) == 14
    assert [i for i, row in enumerate(pole_rows) if row] == [3, 8]
    assert parameter_degree(pole_rows) == 1
    assert not any(
        len(monomial) == 2 for row in pole_rows for monomial in row
    )

    x_tangent = tangent_rows(x_rows)
    pole_tangent = tangent_rows(pole_rows)
    x_rank = exact_rank(x_tangent, 94)
    pole_rank = exact_rank(pole_tangent, 94)
    combined_rank = exact_rank(x_tangent + pole_tangent, 94)
    assert (x_rank, pole_rank, combined_rank) == (36, 2, 38)

    # A single coefficient is an exact infeasibility certificate: it has no
    # parameter term at all and is nonzero in Q.
    obstruction = Q(-18858, 3125)
    assert x_rows[13] == {(): obstruction}
    assert obstruction == (
        -Q(14) * Q(-384, 25) * Q(-128, 125)
        + Q(2) * Q(66927, 625)
    )

    # Independent global differentiation at parameter zero replays both next
    # bands without using the jet formulas above.
    particular = {
        variable: form[0]
        for variable, form in enumerate(forms)
        if form[0]
    }
    f = fb.polynomial_from_solution(particular, 0, 15, 60)
    g = fb.polynomial_from_solution(particular, offset, 25, 100)
    jacobian = fb.poly_sub(
        fb.poly_mul(fb.poly_deriv(f, 0), fb.poly_deriv(g, 1)),
        fb.poly_mul(fb.poly_deriv(f, 1), fb.poly_deriv(g, 0)),
    )
    direct_x = fb.band(fb.x_chart_expand(jacobian, -1), -1)
    expected_x = {
        degree: row.get((), Q(0))
        for degree, row in enumerate(x_rows)
        if row.get((), Q(0))
    }
    assert direct_x == expected_x
    assert direct_x[13] == obstruction

    direct_pole = fb.band(fb.pole_chart_expand(jacobian, 1), 1)
    expected_pole = {
        degree: row.get((), Q(0))
        for degree, row in enumerate(pole_rows)
        if row.get((), Q(0))
    }
    assert direct_pole == expected_pole

    p_sha = parameterization_digest(forms, free_variables)
    e_sha = equations_digest(x_rows, pole_rows)
    certificate_payload = (
        "[s^-1*t^13]J=-18858/3125;parameter_coefficients=0\n"
    )
    c_sha = sha256(certificate_payload.encode()).hexdigest()

    print("TD6-TWO-CHART-NEXT-ROW: PASS")
    print("verdict = Q-EMPTY")
    print(
        f"base = rank {len(pivots)} / {nvariables}; "
        f"affine_dimension={len(free_variables)}; rows={len(base_rows)}"
    )
    print(f"affine_parameterization.sha256 = {p_sha}")
    print("fixed_f1 = -384/25*t^14")
    print("fixed_g1 = -128/125 - 128/5*t^24")
    print("fixed_[t^13]f2 = 66927/625")
    print(
        "next_x = scalar_slots 40; nonzero_rows 37; parameter_degree 1; "
        f"quadratic_monomials 0; tangent_rank {x_rank}; "
        f"frozen_residual_nonzero={sum(bool(row.get((), 0)) for row in x_rows)}"
    )
    print(
        "next_pole = scalar_slots 14; nonzero_rows 2; parameter_degree 1; "
        f"quadratic_monomials 0; tangent_rank {pole_rank}; "
        f"frozen_residual_nonzero={sum(bool(row.get((), 0)) for row in pole_rows)}"
    )
    print(f"combined_tangent_rank = {combined_rank} / 94")
    print(f"next_equations.sha256 = {e_sha}")
    print("certificate = [s^-1*t^13]J = -18858/3125 != 0")
    print("certificate.parameter_coefficients = 0")
    print(f"certificate.sha256 = {c_sha}")
    print("finite_field_probes = not_run_exact_Q_certificate")
    print("terminal_class_killed = false")
    print("JC2_resolved = false")


if __name__ == "__main__":
    main()
