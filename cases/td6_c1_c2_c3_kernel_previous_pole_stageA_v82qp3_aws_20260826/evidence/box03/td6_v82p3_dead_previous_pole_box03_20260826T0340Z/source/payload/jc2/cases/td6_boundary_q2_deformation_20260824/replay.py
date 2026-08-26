#!/usr/bin/env python3
"""Exact preflight for the smallest q-boundary deformation in SP-2.

The retained specialization is changed only from q=t+t^25 to
q=t+B*t^2+t^25, first at B=1.  All arithmetic is over Q and all shared
global polynomial coefficients remain inside the fixed rectangles.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
NEXT_REPLAY = HERE.parent / "td6_two_chart_next_row_20260824" / "replay.py"
NEXT_REPLAY_SHA256 = (
    "0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8"
)
assert sha256(NEXT_REPLAY.read_bytes()).hexdigest() == NEXT_REPLAY_SHA256
spec = importlib.util.spec_from_file_location("td6_next", NEXT_REPLAY)
nr = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(nr)
fb = nr.fb


B = Q(1)
Q_PRIME = {0: Q(1), 1: 2 * B, 24: Q(25)}
P_PRIME = {14: Q(15)}


def build_first_band_system():
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25,
        100,
        5,
        {1: Q(1), 2: B, 25: Q(1)},
        fb.F1_G_PATTERN,
        fb.POLE_G_PATTERN,
    )
    rows = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (('g',) + key, {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]

    for degree in range(40):
        row = {}
        # f1*q'
        for q_degree, multiplier in Q_PRIME.items():
            f_degree = degree - q_degree
            if 0 <= f_degree <= 15:
                for variable, coefficient in fb.x_chart_coefficient(
                    15, 60, 1, f_degree
                ).items():
                    nr.add_linear(row, variable, multiplier * coefficient)
        # -p'*g1
        g_degree = degree - 14
        if 0 <= g_degree <= 25:
            for variable, coefficient in fb.x_chart_coefficient(
                25, 100, 1, g_degree
            ).items():
                nr.add_linear(row, nf + variable, -Q(15) * coefficient)
        rows.append((("JX-FIRST", degree), row, Q(0)))
    return nf, ng, rows


def compile_x_previous(f1, f2, g1, g2):
    rows = []
    for degree in range(40):
        equation = {}
        # f1*g1' - f1'*g1
        for i, left in enumerate(f1):
            j = degree - i + 1
            if 1 <= j < len(g1):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(g1[j], Q(j))),
                )
        for i in range(1, len(f1)):
            j = degree - (i - 1)
            if 0 <= j < len(g1):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(nr.scale_affine(f1[i], Q(i)), g1[j]),
                    -Q(1),
                )
        # +2*f2*q' -2*p'*g2
        for i, form in enumerate(f2):
            multiplier = Q_PRIME.get(degree - i, Q(0))
            if multiplier:
                equation = nr.add_polynomial(
                    equation, nr.affine_polynomial(form), 2 * multiplier
                )
        g_degree = degree - 14
        if 0 <= g_degree < len(g2):
            equation = nr.add_polynomial(
                equation, nr.affine_polynomial(g2[g_degree]), -Q(30)
            )
        rows.append(equation)
    return rows


def compile_x_current(f1, f2, f3, g1, g2, g3):
    rows = []
    for degree in range(40):
        equation = {}
        # f1*g2' + 2*f2*g1'
        for i, left in enumerate(f1):
            j = degree - i + 1
            if 1 <= j < len(g2):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(g2[j], Q(j))),
                )
        for i, left in enumerate(f2):
            j = degree - i + 1
            if 1 <= j < len(g1):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(g1[j], Q(j))),
                    Q(2),
                )
        # +3*f3*q' -3*p'*g3
        for i, form in enumerate(f3):
            multiplier = Q_PRIME.get(degree - i, Q(0))
            if multiplier:
                equation = nr.add_polynomial(
                    equation, nr.affine_polynomial(form), 3 * multiplier
                )
        g_degree = degree - 14
        if 0 <= g_degree < len(g3):
            equation = nr.add_polynomial(
                equation, nr.affine_polynomial(g3[g_degree]), -Q(45)
            )
        # -2*f1'*g2 -f2'*g1
        for i in range(1, len(f1)):
            j = degree - (i - 1)
            if 0 <= j < len(g2):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(nr.scale_affine(f1[i], Q(i)), g2[j]),
                    -Q(2),
                )
        for i in range(1, len(f2)):
            j = degree - (i - 1)
            if 0 <= j < len(g1):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(nr.scale_affine(f2[i], Q(i)), g1[j]),
                    -Q(1),
                )
        if degree == 0:
            equation = nr.add_polynomial(equation, {(): Q(-1)})
        rows.append(equation)
    return rows


def linear_rows(family, polynomials):
    packed = []
    for degree, polynomial in enumerate(polynomials):
        row = {}
        constant = polynomial.get((), Q(0))
        for monomial, coefficient in polynomial.items():
            if not monomial:
                continue
            assert len(monomial) == 1
            nr.add_linear(row, monomial[0], coefficient)
        if row or constant:
            packed.append(((family, degree), row, -constant))
    return packed


def parameterize(nvariables, rows):
    solution, pivots, error = fb.exact_solve(
        nvariables, rows, allow_inconsistent=True
    )
    if error:
        return None, None, pivots, error
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (Q(0), {parameter_of[variable]: Q(1)})
            continue
        row, rhs = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other != variable:
                form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    for key, row, rhs in rows:
        got = (Q(0), {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (rhs, {}), (key, got, rhs)
    return forms, free, pivots, None


def compose_forms(forms, parameter_forms):
    out = []
    for constant, coefficients in forms:
        value = (constant, {})
        for parameter, coefficient in coefficients.items():
            value = nr.add_affine(value, parameter_forms[parameter], coefficient)
        out.append(value)
    return out


def main():
    fb.CENTER = (Q(1), Q(1), Q(1))
    fb._X_POWER_CACHE.clear()
    nf, ng, base_rows = build_first_band_system()
    global_94, free_94, base_pivots, base_error = parameterize(
        nf + ng, base_rows
    )
    assert base_error is None

    f1 = nr.x_band_forms(15, 60, 1, global_94, 0)
    f2 = nr.x_band_forms(15, 60, 2, global_94, 0)
    g1 = nr.x_band_forms(25, 100, 1, global_94, nf)
    g2 = nr.x_band_forms(25, 100, 2, global_94, nf)
    x_previous = compile_x_previous(f1, f2, g1, g2)

    p1 = [
        nr.combine_global_linear(
            nr.pole_coefficient(15, 60, -2, degree), global_94, 0
        )
        for degree in range(61)
    ]
    q1 = [
        nr.combine_global_linear(
            nr.pole_coefficient(25, 100, -4, degree), global_94, nf
        )
        for degree in range(101)
    ]
    pole_previous = nr.compile_pole_next_rows(p1, q1)
    previous_rows = linear_rows("X-1", x_previous)
    x_only_rows = list(previous_rows)
    previous_rows += linear_rows("P1", pole_previous)
    parameter_forms, free_after, previous_pivots, previous_error = parameterize(
        len(free_94), previous_rows
    )

    x_only_solution, x_only_pivots, x_only_error = fb.exact_solve(
        len(free_94), x_only_rows, allow_inconsistent=True
    )
    print(
        f"base = rank {len(base_pivots)} / {nf+ng}; "
        f"dimension {len(free_94)}; error {base_error}"
    )
    print(
        f"previous_x = rank {len(x_only_pivots)} / {len(free_94)}; "
        f"error {x_only_error}"
    )
    print(
        f"previous_pair = rank {len(previous_pivots)} / {len(free_94)}; "
        f"error {previous_error}"
    )
    if previous_error:
        print("verdict = PREVIOUS-BAND-EMPTY")
        return

    global_after = compose_forms(global_94, parameter_forms)
    f1 = nr.x_band_forms(15, 60, 1, global_after, 0)
    f2 = nr.x_band_forms(15, 60, 2, global_after, 0)
    f3 = nr.x_band_forms(15, 60, 3, global_after, 0)
    g1 = nr.x_band_forms(25, 100, 1, global_after, nf)
    g2 = nr.x_band_forms(25, 100, 2, global_after, nf)
    g3 = nr.x_band_forms(25, 100, 3, global_after, nf)
    current = compile_x_current(f1, f2, f3, g1, g2, g3)
    assert nr.parameter_degree(current) <= 1
    current_rows = linear_rows("X0", current)
    current_solution, current_pivots, current_error = fb.exact_solve(
        len(free_after), current_rows, allow_inconsistent=True
    )
    tangent_rank = nr.exact_rank(nr.tangent_rows(current), len(free_after))
    print(
        f"current_x = rows {sum(bool(row) for row in current)}; "
        f"tangent_rank {tangent_rank} / {len(free_after)}; "
        f"affine_rank_before_stop {len(current_pivots)}; error {current_error}"
    )
    if current_error:
        print("verdict = CURRENT-CENTERED-BAND-EMPTY")
    else:
        print(
            f"verdict = NONEMPTY-THROUGH-CENTERED-BAND; "
            f"dimension {len(free_after)-len(current_pivots)}"
        )


if __name__ == "__main__":
    main()
