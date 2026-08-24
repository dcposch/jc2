#!/usr/bin/env python3
"""Exact B=1 probe over the six-point t0 survivor residue field."""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, path, expected):
    assert sha256(path.read_bytes()).hexdigest() == expected
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


base = load(
    "q2_base",
    HERE / "replay.py",
    "0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357",
)
uniform = load(
    "uniform_third",
    HERE.parent / "td6_moduli_uniform_third_band_20260824" / "replay.py",
    "7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8",
)
nr, fb, E = base.nr, base.fb, uniform.E
S, D, L, A = (
    E(uniform.S_FIELD),
    E(uniform.D_FIELD),
    E(uniform.L_FIELD),
    uniform.A_FIELD,
)


def multiply(left, right):
    out = [E(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def power(poly, exponent):
    out = [E(1)]
    for _ in range(exponent):
        out = multiply(out, poly)
    return out


R = multiply([E(-1), E(1)], [E(-1), E(1)])
R = multiply(R, [D, -S, E(1)])
R3, R5 = power(R, 3), power(R, 5)
POLE_F = {1: -(L**3) * A, 6: L**3}
POLE_G = {
    0: Q(5, 9) * L**5 * A**2,
    5: -Q(5, 3) * L**5 * A,
    10: L**5,
}


def rhs(key):
    if key[0] == "JX-FIRST":
        return E(0)
    owner, chart, exponent, degree = key
    if chart == "X" and exponent == 0:
        return E(
            1
            if (owner, degree) in (
                ("f", 15), ("g", 1), ("g", 2), ("g", 25)
            )
            else 0
        )
    if chart == "F1" and exponent == (-15 if owner == "f" else -25):
        pattern = R3 if owner == "f" else R5
        return pattern[degree // 5] if degree % 5 == 0 and degree // 5 < len(pattern) else E(0)
    if chart == "F0" and exponent == (-3 if owner == "f" else -5):
        return (POLE_F if owner == "f" else POLE_G).get(degree, E(0))
    return E(0)


def propagate(records):
    pivot_rhs = {}
    compatibility = []
    for key, kind, pivot, lead, factors in records:
        value = rhs(key)
        for old_pivot, factor in factors:
            value -= factor * pivot_rhs[old_pivot]
        if kind == "pivot":
            pivot_rhs[pivot] = value / lead
        elif value:
            compatibility.append((key, value))
    return pivot_rhs, compatibility


def parameterization(nvariables, pivots, pivot_rhs):
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            # The base matrix is rational.  Keep its 94 homogeneous
            # directions over Q; only the particular constants live in E.
            forms[variable] = (E(0), {parameter_of[variable]: Q(1)})
            continue
        form = (pivot_rhs[variable], {})
        for other, coefficient in pivots[variable].items():
            if other != variable:
                form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    return forms, free


def rows(family, polynomials):
    out = []
    for degree, polynomial in enumerate(polynomials):
        row = {}
        constant = polynomial.get((), E(0))
        for monomial, coefficient in polynomial.items():
            if monomial:
                assert len(monomial) == 1
                row[monomial[0]] = coefficient
        if row or constant:
            out.append(((family, degree), row, -constant))
    return out


def affine_from_rows(nvariables, equations):
    solution, pivots, error = fb.exact_solve(
        nvariables, equations, allow_inconsistent=True
    )
    if error:
        return None, None, pivots, error
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (E(0), {parameter_of[variable]: E(1)})
            continue
        row, value = pivots[variable]
        form = (value, {})
        for other, coefficient in row.items():
            if other != variable:
                form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    return forms, free, pivots, None


def compose(forms, parameter_forms):
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
    nf, ng, rational_rows = base.build_first_band_system()
    pivots, records = uniform.mu.factor_matrix(rational_rows)
    pivot_rhs, compatibility = propagate(records)
    assert not compatibility
    forms94, free94 = parameterization(nf + ng, pivots, pivot_rhs)
    assert (len(pivots),len(free94))==(3508,94)

    f1 = nr.x_band_forms(15,60,1,forms94,0)
    f2 = nr.x_band_forms(15,60,2,forms94,0)
    g1 = nr.x_band_forms(25,100,1,forms94,nf)
    g2 = nr.x_band_forms(25,100,2,forms94,nf)
    previous = base.compile_x_previous(f1,f2,g1,g2)
    parameter_forms, free58, previous_pivots, previous_error = affine_from_rows(
        94, rows("X-1", previous)
    )
    assert previous_error is None and (len(previous_pivots),len(free58))==(36,58)
    global58=compose(forms94,parameter_forms)
    f1=nr.x_band_forms(15,60,1,global58,0)
    f2=nr.x_band_forms(15,60,2,global58,0)
    f3=nr.x_band_forms(15,60,3,global58,0)
    g1=nr.x_band_forms(25,100,1,global58,nf)
    g2=nr.x_band_forms(25,100,2,global58,nf)
    g3=nr.x_band_forms(25,100,3,global58,nf)
    current=base.compile_x_current(f1,f2,f3,g1,g2,g3)
    solution,current_pivots,current_error=fb.exact_solve(
        58,rows("X0",current),allow_inconsistent=True
    )
    tangent=nr.exact_rank(nr.tangent_rows(current),58)
    assert solution is None and current_error is not None
    assert current_error[0]==("X0",4) and tangent==25
    residual=current_error[1]
    expected=E([
        uniform.K([
            Q(2145334,3625),Q(-4154976,3625),Q(4405068,3625),
            Q(-2488119,3625),Q(761922,3625),Q(-105084,3625),
        ]),
        uniform.K(Q(136875,29)),
    ])
    assert residual==expected
    print("TD6-BOUNDARY-Q2-B1: PASS")
    print("verdict = B2-EQUALS-ONE-EMPTY")
    print("base = rank 3508 / 3602; dimension 94")
    print("previous_x = rank 36 / 94; dimension 58")
    print("current_centered_band = tangent_rank 25 / 58; EMPTY at t^4")
    print(f"residual.sha256 = {sha256(repr(residual).encode()).hexdigest()}")
    print("full_b2_family_killed = false")


if __name__ == "__main__":
    main()
