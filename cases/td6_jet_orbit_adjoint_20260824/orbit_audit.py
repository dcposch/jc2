#!/usr/bin/env python3
"""Exact finite audit of the TD6 boundary-jet orbit and source tangents."""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PARENT = REPO / "cases/td6_moduli_uniform_third_band_20260824/replay.py"
PARENT_SHA = "7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8"
assert sha256(PARENT.read_bytes()).hexdigest() == PARENT_SHA
spec = importlib.util.spec_from_file_location("uniform", PARENT)
uniform = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(uniform)


def add(poly, degree, coefficient):
    if coefficient:
        poly[degree] = poly.get(degree, Q(0)) + coefficient
        if not poly[degree]:
            poly.pop(degree)


def derivative(poly):
    return {degree - 1: degree * coefficient for degree, coefficient in poly.items() if degree}


def multiply(left, right):
    out = {}
    for i, a in left.items():
        for j, b in right.items():
            add(out, i + j, a * b)
    return out


def scale(poly, scalar):
    return {degree: scalar * coefficient for degree, coefficient in poly.items() if scalar * coefficient}


def compose_tangent(poly, h):
    """d/d eps poly(t+eps*h(t)) at eps=0."""
    return multiply(derivative(poly), h)


def vector(*blocks):
    out = {}
    for family, poly in blocks:
        for degree, coefficient in poly.items():
            out[(family, degree)] = coefficient
    return out


def vadd(left, right, scale_right=Q(1)):
    out = dict(left)
    for key, coefficient in right.items():
        value = out.get(key, Q(0)) + scale_right * coefficient
        if value:
            out[key] = value
        else:
            out.pop(key, None)
    return out


def rank(rows):
    pivots = {}
    for original in rows:
        row = dict(original)
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            for key, coefficient in pivots[pivot].items():
                value = row.get(key, Q(0)) - factor * coefficient
                if value:
                    row[key] = value
                else:
                    row.pop(key, None)
        if row:
            pivot = min(row)
            lead = row[pivot]
            pivots[pivot] = {key: coefficient / lead for key, coefficient in row.items()}
    return len(pivots), tuple(pivots)


def main():
    p = {15: Q(1)}
    q = {1: Q(1), 25: Q(1)}
    h2 = {2: Q(1)}

    # Full formal source-coordinate orbit: chart and both boundary members.
    orbit_h2 = vector(
        ("chart", h2),
        ("p", compose_tangent(p, h2)),
        ("q", compose_tangent(q, h2)),
    )
    assert orbit_h2 == {
        ("chart", 2): Q(1),
        ("p", 16): Q(15),
        ("q", 2): Q(1),
        ("q", 26): Q(25),
    }
    q2_only = {("q", 2): Q(1)}
    transverse_representative = vadd(q2_only, orbit_h2, Q(-1))
    assert transverse_representative == {
        ("chart", 2): Q(-1),
        ("p", 16): Q(-15),
        ("q", 26): Q(-25),
    }

    # The fixed-linear-chart section is transverse to every nonzero formal
    # t-reparametrization because the chart component is literally h.
    orbit_rows = []
    for degree in range(0, 7):
        h = {degree: Q(1)}
        orbit_rows.append(
            vector(
                ("chart", h),
                ("p", compose_tangent(p, h)),
                ("q", compose_tangent(q, h)),
            )
        )
    assert rank(orbit_rows)[0] == len(orbit_rows)
    assert rank(orbit_rows + [q2_only])[0] == len(orbit_rows) + 1

    # Target determinant-one gauge tangents on the boundary pair.
    target_f_translation = {("p", 0): Q(1)}
    target_g_translation = {("q", 0): Q(1)}
    target_scaling = vadd(vector(("p", p)), vector(("q", q)), Q(-1))
    target_lower_shear = vector(("q", p))  # g -> g + eps*f
    target_gauges = [
        target_f_translation,
        target_g_translation,
        target_scaling,
        target_lower_shear,
    ]
    assert rank(target_gauges)[0] == 4
    assert rank(orbit_rows + target_gauges)[0] == len(orbit_rows) + 4

    # Frozen source equations in S,D,L,A.  Q=0 and 3H^3=1 make S,D
    # infinitesimally rigid; L=25H and L^8*A^3=9 then fix L,A.
    S = uniform.S_FIELD
    H = uniform.H_FIELD
    L = uniform.L_FIELD
    A = uniform.A_FIELD
    zero = uniform.E(0)
    one = uniform.E(1)
    source_tangent = [
        [uniform.E(-4 * S + 2), uniform.E(5), zero, zero],
        [uniform.E(-9 * H**2), uniform.E(9 * H**2), zero, zero],
        [uniform.E(25), uniform.E(-25), one, zero],
        [zero, zero, uniform.E(8) / uniform.E(L), uniform.E(3) / uniform.E(A)],
    ]

    def field_rank(matrix):
        matrix = [list(row) for row in matrix]
        found = 0
        for column in range(len(matrix[0])):
            pivot = next((row for row in range(found, len(matrix)) if matrix[row][column]), None)
            if pivot is None:
                continue
            matrix[found], matrix[pivot] = matrix[pivot], matrix[found]
            lead = matrix[found][column]
            matrix[found] = [value / lead for value in matrix[found]]
            for row in range(len(matrix)):
                if row == found:
                    continue
                factor = matrix[row][column]
                if factor:
                    matrix[row] = [
                        left - factor * right
                        for left, right in zip(matrix[row], matrix[found])
                    ]
            found += 1
        return found

    assert field_rank(source_tangent) == 4
    # Equivalently, the first two rows have determinant
    # 9*H^2*(7-4*S), nonzero because F(7/4) != 0.
    determinant_sd = uniform.E(9 * H**2 * (7 - 4 * S))
    assert determinant_sd
    f_at_7_over_4 = sum(
        Q(coefficient) * Q(7, 4) ** degree
        for degree, coefficient in enumerate(uniform.F_INTEGER)
    )
    assert f_at_7_over_4

    # A t^2 reparametrization cannot change the first nonzero t^4
    # compatibility coefficient: if R=rho*t^4+..., R(t+eps*t^2) has the
    # same t^4 coefficient.  Lower compatibility coefficients are zero.
    rho = {4: Q(1)}
    assert compose_tangent(rho, h2).get(4, Q(0)) == 0

    payload = (
        "orbit_h2=chart:t2+p:15t16+q:t2+25t26\n"
        "q2_class=fixed-chart-transverse\n"
        "target_gauge_rank=4\n"
        "source_SDLA_tangent_rank=4\n"
        f"F(7/4)={f_at_7_over_4.numerator}/{f_at_7_over_4.denominator}\n"
        "orbit_t4_adjoint_derivative=0\n"
    )
    print("TD6-JET-ORBIT-AUDIT: PASS")
    print("full_t2_orbit = chart:t^2; p:15*t^16; q:t^2+25*t^26")
    print("q2_only_mod_orbit = -chart:t^2-15*p:t^16-25*q:t^26")
    print("fixed_linear_chart_q2_transverse = true")
    print("target_gauge_rank = 4 (two translations, reciprocal scaling, g+=eps*f)")
    print("source_tangent_rank_SDLA = 4/4")
    print(f"F(7/4) = {f_at_7_over_4}")
    print("full_t2_orbit_t4_adjoint_derivative = 0")
    print(f"audit.sha256 = {sha256(payload.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
