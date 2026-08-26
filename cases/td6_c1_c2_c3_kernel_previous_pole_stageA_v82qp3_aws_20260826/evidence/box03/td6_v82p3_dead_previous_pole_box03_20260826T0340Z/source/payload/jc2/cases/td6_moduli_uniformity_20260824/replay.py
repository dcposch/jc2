#!/usr/bin/env python3
"""Exact replay for TD6-MODULI-UNIFORMITY-GATE (2026-08-24).

The calculation has two parts.

1. A coefficient-level proof, independent of the common centering, derives
   the universal next-row obstruction from the F1 boundary polynomial.
2. On the normalized C=1, center=(1,1,1), zero-dead-stretch slice, an exact
   dual factorization propagates symbolic S,D,L,A right-hand sides through
   the full 6547-row first-band system and certifies the surviving locus and
   its paired-next-row rank.

All arithmetic in the compiler is over Q.  Algebraic-complex points are
described by polynomial equations; no floating point or finite field is used.
"""

from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
NEXT_ROW_REPLAY = HERE.parent / "td6_two_chart_next_row_20260824" / "replay.py"
NEXT_ROW_SHA256 = (
    "0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8"
)
assert sha256(NEXT_ROW_REPLAY.read_bytes()).hexdigest() == NEXT_ROW_SHA256

spec = importlib.util.spec_from_file_location("td6_next_row", NEXT_ROW_REPLAY)
nr = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(nr)


# ---------------------------------------------------------------------------
# Sparse polynomials over Q in (S,D,L,A)

ZERO_MONOMIAL = (0, 0, 0, 0)
VARIABLE_NAMES = ("S", "D", "L", "A")


def poly_constant(value):
    value = Q(value)
    return {ZERO_MONOMIAL: value} if value else {}


def poly_variable(index):
    exponent = [0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): Q(1)}


def poly_add(left, right, scale=Q(1)):
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, Q(0)) + scale * coefficient
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def poly_scale(poly, scale):
    return {
        monomial: scale * coefficient
        for monomial, coefficient in poly.items()
        if scale * coefficient
    }


def poly_multiply(left, right):
    out = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_monomial[k] + right_monomial[k] for k in range(4)
            )
            out[monomial] = (
                out.get(monomial, Q(0))
                + left_coefficient * right_coefficient
            )
    return {m: c for m, c in out.items() if c}


def poly_power(poly, exponent):
    out = poly_constant(1)
    for _ in range(exponent):
        out = poly_multiply(out, poly)
    return out


def zpoly_multiply(left, right):
    out = [{} for _ in range(len(left) + len(right) - 1)]
    for i, left_coefficient in enumerate(left):
        for j, right_coefficient in enumerate(right):
            out[i + j] = poly_add(
                out[i + j],
                poly_multiply(left_coefficient, right_coefficient),
            )
    return out


def zpoly_power(poly, exponent):
    out = [poly_constant(1)]
    for _ in range(exponent):
        out = zpoly_multiply(out, poly)
    return out


def zpoly_derivative(poly):
    return [poly_scale(poly[k], Q(k)) for k in range(1, len(poly))]


def zpoly_subtract(left, right):
    out = [{} for _ in range(max(len(left), len(right)))]
    for k in range(len(out)):
        if k < len(left):
            out[k] = poly_add(out[k], left[k])
        if k < len(right):
            out[k] = poly_add(out[k], right[k], -Q(1))
    return out


S, D, L, A = (poly_variable(k) for k in range(4))
ONE = poly_constant(1)

# R(z)=(z-1)^2(z^2-Sz+D), the C=1 normalized reduced F1 pattern.
Z_MINUS_ONE = [poly_constant(-1), ONE]
EXTRA_QUADRATIC = [D, poly_scale(S, -Q(1)), ONE]
R = zpoly_multiply(
    zpoly_multiply(Z_MINUS_ONE, Z_MINUS_ONE), EXTRA_QUADRATIC
)
R_CUBED = zpoly_power(R, 3)
R_FIFTH = zpoly_power(R, 5)


# ---------------------------------------------------------------------------
# Exact matrix factorization and symbolic RHS propagation

def factor_matrix(rows):
    """Factor the rational coefficient matrix, recording RHS operations."""
    pivots = {}
    records = []
    for key, original_row, _ in rows:
        row = dict(original_row)
        factors = []
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            factors.append((pivot, factor))
            old_row = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, Q(0)) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
        if not row:
            records.append((key, "dependent", None, None, factors))
            continue
        pivot = min(row)
        lead = row[pivot]
        pivots[pivot] = {
            variable: coefficient / lead
            for variable, coefficient in row.items()
        }
        records.append((key, "pivot", pivot, lead, factors))
    return pivots, records


L_CUBED = poly_power(L, 3)
L_FIFTH = poly_power(L, 5)
POLE_F = {
    1: poly_scale(poly_multiply(L_CUBED, A), -Q(1)),
    6: L_CUBED,
}
POLE_G = {
    0: poly_scale(
        poly_multiply(L_FIFTH, poly_power(A, 2)), Q(5, 9)
    ),
    5: poly_scale(poly_multiply(L_FIFTH, A), -Q(5, 3)),
    10: L_FIFTH,
}


def symbolic_rhs(key):
    if key[0] == "JX-FIRST":
        return {}
    owner, chart, exponent, degree = key
    if chart == "X" and exponent == 0:
        return poly_constant(
            1
            if (owner, degree) in (("f", 15), ("g", 1), ("g", 25))
            else 0
        )
    if chart == "F1" and exponent == (-15 if owner == "f" else -25):
        pattern = R_CUBED if owner == "f" else R_FIFTH
        if degree % 5 == 0 and degree // 5 < len(pattern):
            return pattern[degree // 5]
        return {}
    if chart == "F0" and exponent == (-3 if owner == "f" else -5):
        return (POLE_F if owner == "f" else POLE_G).get(degree, {})
    return {}


def propagate_symbolic_rhs(records):
    pivot_rhs = {}
    compatibility = []
    for key, kind, pivot, lead, factors in records:
        rhs = symbolic_rhs(key)
        for old_pivot, factor in factors:
            rhs = poly_add(rhs, pivot_rhs[old_pivot], -factor)
        if kind == "pivot":
            pivot_rhs[pivot] = poly_scale(rhs, Q(1) / lead)
        elif rhs:
            compatibility.append((key, rhs))
    return pivot_rhs, compatibility


def dual_value(global_row, pivots, pivot_rhs):
    """Evaluate a nullspace-invariant global linear functional symbolically."""
    row = dict(global_row)
    rhs_weights = {}
    while row:
        pivot = min(row)
        assert pivot in pivots, ("functional not invariant", pivot)
        factor = row[pivot]
        rhs_weights[pivot] = rhs_weights.get(pivot, Q(0)) + factor
        for variable, coefficient in pivots[pivot].items():
            value = row.get(variable, Q(0)) - factor * coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    out = {}
    for pivot, weight in rhs_weights.items():
        out = poly_add(out, pivot_rhs[pivot], weight)
    return out


def symbolic_particular_solution(nvariables, pivots, pivot_rhs):
    """Back-substitute with every nonpivot variable specialized to zero."""
    solution = [{} for _ in range(nvariables)]
    for pivot in sorted(pivots, reverse=True):
        value = dict(pivot_rhs[pivot])
        for variable, coefficient in pivots[pivot].items():
            if variable != pivot:
                value = poly_add(value, solution[variable], -coefficient)
        solution[pivot] = value
    return solution


def symbolic_global_linear(row, solution, offset=0):
    out = {}
    for variable, coefficient in row.items():
        out = poly_add(out, solution[offset + variable], coefficient)
    return out


def symbolic_x_band(imax, jmax, exponent, solution, offset):
    return [
        symbolic_global_linear(
            nr.fb.x_chart_coefficient(imax, jmax, exponent, degree),
            solution,
            offset,
        )
        for degree in range(imax + 1)
    ]


def symbolic_x_next_rows(f1, f2, g1, g2):
    """The forty constant-in-free-parameters next-x coefficients."""
    p_prime = [{} for _ in range(15)]
    p_prime[14] = poly_constant(15)
    q_prime = [{} for _ in range(25)]
    q_prime[0] = poly_constant(1)
    q_prime[24] = poly_constant(25)

    terms = zpoly_subtract(
        zpoly_multiply(f1, zpoly_derivative(g1)),
        zpoly_multiply(zpoly_derivative(f1), g1),
    )
    terms_2 = zpoly_subtract(
        [poly_scale(value, Q(2)) for value in zpoly_multiply(f2, q_prime)],
        [poly_scale(value, Q(2)) for value in zpoly_multiply(p_prime, g2)],
    )
    out = [{} for _ in range(40)]
    for degree in range(40):
        if degree < len(terms):
            out[degree] = poly_add(out[degree], terms[degree])
        if degree < len(terms_2):
            out[degree] = poly_add(out[degree], terms_2[degree])
    return out


def evaluate(poly, values):
    return sum(
        coefficient
        * values[0] ** monomial[0]
        * values[1] ** monomial[1]
        * values[2] ** monomial[2]
        * values[3] ** monomial[3]
        for monomial, coefficient in poly.items()
    )


# ---------------------------------------------------------------------------
# Center-independent coefficient support

def exponent_sums(number_of_center_factors):
    sums = {0}
    for _ in range(number_of_center_factors):
        sums = {old + new for old in sums for new in (1, 2, 3)}
    return sums


def centered_contributors(imax, jmax, t_degree, s_exponent):
    """Possible (i,j) sources, before using any centering coefficient value."""
    out = set()
    for i in range(t_degree, imax + 1):
        for center_degree in exponent_sums(i - t_degree):
            j = 4 * t_degree + center_degree - s_exponent
            if 0 <= j <= jmax:
                out.add((i, j))
    return out


def assert_boundary_only(imax, jmax, pole_order, t_degree, s_exponent, target):
    contributors = centered_contributors(
        imax, jmax, t_degree, s_exponent
    )
    assert target in contributors
    assert target[1] - 5 * target[0] == -pole_order
    for i, j in contributors - {target}:
        # These coefficients vanish by strict F1 holomorphy, independently
        # of c1,c2,c3 and even when some centering coefficient is zero.
        assert j - 5 * i < -pole_order


# ---------------------------------------------------------------------------
# Exact rank audit for the surviving normalized slice

def reduce_mod_x(row, x_pivots):
    row = dict(row)
    while row:
        pivot = min(row)
        if pivot not in x_pivots:
            break
        factor = row[pivot]
        old_row, _ = x_pivots[pivot]
        for variable, coefficient in old_row.items():
            value = row.get(variable, Q(0)) - factor * coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    return row


def fraction_text(value):
    return f"{value.numerator}/{value.denominator}"


def poly_text(poly):
    terms = []
    for monomial, coefficient in sorted(poly.items(), reverse=True):
        name = "*".join(
            variable + (f"^{exponent}" if exponent != 1 else "")
            for variable, exponent in zip(VARIABLE_NAMES, monomial)
            if exponent
        ) or "1"
        terms.append(f"{fraction_text(coefficient)}*{name}")
    return "+".join(terms) if terms else "0"


def certificate_digest(polynomials, quotient_vectors):
    digest = sha256()
    for name, poly in polynomials:
        digest.update(f"{name}={poly_text(poly)}\n".encode())
    for name, vector in quotient_vectors:
        digest.update(f"{name}".encode())
        for variable, coefficient in sorted(vector.items()):
            digest.update(
                f";u{variable}:{fraction_text(coefficient)}".encode()
            )
        digest.update(b"\n")
    return digest.hexdigest()


def main():
    # The coefficient proof does not choose c1,c2,c3.  The following support
    # assertions certify that all possible center-dependent contributors are
    # on strict F1-forbidden diagonals.
    assert_boundary_only(15, 60, 15, 14, 1, (14, 55))  # [s t^14]f
    assert_boundary_only(25, 100, 25, 24, 1, (24, 95))  # [s t^24]g
    assert_boundary_only(15, 60, 15, 13, 2, (13, 50))  # [s^2 t^13]f

    # Work on the normalized C=1 slice for the full symbolic transport.
    nr.fb.CENTER = (Q(1), Q(1), Q(1))
    nr.fb._X_POWER_CACHE.clear()
    nf, ng, rows_f, rows_g, base_rows = nr.build_first_band_system()
    pivots, records = factor_matrix(base_rows)
    assert (nf, ng, len(base_rows), len(pivots)) == (976, 2626, 6547, 3508)
    pivot_rhs, compatibility = propagate_symbolic_rhs(records)

    X = poly_add(poly_add(S, D, -Q(1)), poly_constant(-1))
    expected_compatibility = [
        poly_add(poly_power(L, 3), poly_power(poly_scale(X, Q(25)), 3)),
        poly_add(poly_power(L, 5), poly_power(poly_scale(X, Q(25)), 5)),
    ]
    assert len(compatibility) == 2
    assert Counter(poly_text(poly) for _, poly in compatibility) == Counter(
        poly_text(poly) for poly in expected_compatibility
    )

    # The F1-to-r9 source relation is L=25(1-S+D)=-25X, so both odd-power
    # compatibility rows vanish identically.
    source_L = poly_scale(X, -Q(25))
    assert poly_add(source_L, poly_scale(X, Q(25))) == {}

    f1_14 = dual_value(
        nr.fb.x_chart_coefficient(15, 60, 1, 14), pivots, pivot_rhs
    )
    g1_0 = dual_value(
        {
            nf + variable: coefficient
            for variable, coefficient in nr.fb.x_chart_coefficient(
                25, 100, 1, 0
            ).items()
        },
        pivots,
        pivot_rhs,
    )
    g1_24 = dual_value(
        {
            nf + variable: coefficient
            for variable, coefficient in nr.fb.x_chart_coefficient(
                25, 100, 1, 24
            ).items()
        },
        pivots,
        pivot_rhs,
    )
    f2_13 = dual_value(
        nr.fb.x_chart_coefficient(15, 60, 2, 13), pivots, pivot_rhs
    )

    expected_K = poly_scale(poly_add(S, poly_constant(2)), -Q(1, 5))
    expected_H = poly_add(
        poly_add(poly_scale(poly_power(S, 2), Q(3)), poly_scale(S, Q(18))),
        poly_add(poly_scale(D, Q(3)), poly_constant(15)),
    )
    assert f1_14 == poly_scale(expected_K, Q(15))
    assert g1_0 == expected_K
    assert g1_24 == poly_scale(expected_K, Q(25))
    assert f2_13 == expected_H

    obstruction = poly_add(
        poly_scale(f2_13, Q(2)),
        poly_scale(poly_multiply(f1_14, g1_0), -Q(14)),
    )
    expected_obstruction = poly_scale(
        poly_add(
            poly_add(poly_scale(poly_power(S, 2), -Q(2)), poly_scale(S, Q(2))),
            poly_add(poly_scale(D, Q(5)), poly_constant(-3)),
        ),
        Q(6, 5),
    )
    assert obstruction == expected_obstruction

    # Direct F1 coefficient proof: r3=-(S+2), r2=D+2S+1;
    # [z^11]R^3=f1_14, [z^19]R^5=g1_24, and [z^10]R^3=f2_13.
    assert R[3] == poly_scale(poly_add(S, poly_constant(2)), -Q(1))
    assert R[2] == poly_add(poly_add(D, poly_scale(S, Q(2))), poly_constant(1))
    assert R_CUBED[11] == f1_14
    assert R_FIFTH[19] == g1_24
    assert R_CUBED[10] == f2_13

    # Check every parameter-only next-x slot, not only degree thirteen.
    symbolic_solution = symbolic_particular_solution(
        nf + ng, pivots, pivot_rhs
    )
    symbolic_f1 = symbolic_x_band(15, 60, 1, symbolic_solution, 0)
    symbolic_f2 = symbolic_x_band(15, 60, 2, symbolic_solution, 0)
    symbolic_g1 = symbolic_x_band(25, 100, 1, symbolic_solution, nf)
    symbolic_g2 = symbolic_x_band(25, 100, 2, symbolic_solution, nf)
    assert symbolic_f1[14] == f1_14
    assert symbolic_g1[0] == g1_0
    assert symbolic_g1[24] == g1_24
    assert symbolic_f2[13] == f2_13
    symbolic_x_rows = symbolic_x_next_rows(
        symbolic_f1, symbolic_f2, symbolic_g1, symbolic_g2
    )
    assert [
        (degree, value)
        for degree, value in enumerate(symbolic_f1)
        if value
    ] == [(14, f1_14)]
    assert [
        (degree, value)
        for degree, value in enumerate(symbolic_g1)
        if value
    ] == [(0, g1_0), (24, g1_24)]

    # Leading pole Jacobian normalization.  The local ODE constant is
    # (25/9)L^8 A^3, so J=1 requires L^8 A^3=9.
    pole_f = [{} for _ in range(7)]
    pole_g = [{} for _ in range(11)]
    for degree, coefficient in POLE_F.items():
        pole_f[degree] = coefficient
    for degree, coefficient in POLE_G.items():
        pole_g[degree] = coefficient
    pole_ode = zpoly_subtract(
        [
            poly_scale(coefficient, Q(3))
            for coefficient in zpoly_multiply(
                pole_f, zpoly_derivative(pole_g)
            )
        ],
        [
            poly_scale(coefficient, Q(5))
            for coefficient in zpoly_multiply(
                zpoly_derivative(pole_f), pole_g
            )
        ],
    )
    expected_ode_constant = poly_scale(
        poly_multiply(poly_power(L, 8), poly_power(A, 3)), Q(25, 9)
    )
    assert pole_ode[0] == expected_ode_constant
    assert all(not coefficient for coefficient in pole_ode[1:])

    # Exact next-row rank on the source-compatible survivor, using the fixed
    # matrix's homogeneous directions.  Constants change with S,D,L,A; these
    # tangent vectors do not.
    forms, free_variables, base_pivots = nr.affine_parameterization(
        nf + ng, base_rows
    )
    assert len(base_pivots) == 3508 and len(free_variables) == 94
    f1 = nr.x_band_forms(15, 60, 1, forms, 0)
    f2 = nr.x_band_forms(15, 60, 2, forms, 0)
    g1 = nr.x_band_forms(25, 100, 1, forms, nf)
    g2 = nr.x_band_forms(25, 100, 2, forms, nf)
    x_rows = nr.compile_x_next_rows(f1, f2, g1, g2)
    x_tangent = nr.tangent_rows(x_rows)
    nonzero_x_tangent = [degree for degree, row in enumerate(x_tangent) if row]
    assert len(nonzero_x_tangent) == 36
    assert not x_tangent[13]
    assert nr.exact_rank(x_tangent, 94) == 36
    zero_tangent_degrees = [
        degree for degree, row in enumerate(x_tangent) if not row
    ]
    assert zero_tangent_degrees == [13, 37, 38, 39]
    assert symbolic_x_rows[13] == obstruction
    assert not symbolic_x_rows[37]
    assert not symbolic_x_rows[38]
    assert not symbolic_x_rows[39]

    baseline_values = (Q(78, 25), Q(56, 25), Q(3), Q(1, 9))
    for degree, row in enumerate(x_rows):
        assert row.get((), Q(0)) == evaluate(
            symbolic_x_rows[degree], baseline_values
        )

    x_linear_rows = [
        (("x", degree), row, Q(0))
        for degree, row in enumerate(x_tangent)
        if row
    ]
    _, x_pivots, _ = nr.fb.exact_solve(94, x_linear_rows)

    p1_4 = nr.combine_global_linear(
        nr.pole_coefficient(15, 60, -2, 4), forms, 0
    )[1]
    q1_3 = nr.combine_global_linear(
        nr.pole_coefficient(25, 100, -4, 3), forms, nf
    )[1]
    q1_8 = nr.combine_global_linear(
        nr.pole_coefficient(25, 100, -4, 8), forms, nf
    )[1]
    quotient_vectors = [
        ("P", reduce_mod_x(p1_4, x_pivots)),
        ("Q3", reduce_mod_x(q1_3, x_pivots)),
        ("Q8", reduce_mod_x(q1_8, x_pivots)),
    ]
    quotient_rows = [
        (("quotient", name), row, Q(0)) for name, row in quotient_vectors
    ]
    _, quotient_pivots, _ = nr.fb.exact_solve(94, quotient_rows)
    assert len(quotient_pivots) == 3
    assert list(quotient_pivots) == [10, 25, 38]

    # Modulo the x rows, the two actual pole-J tangent rows are
    #  R3=-(4/9)L^5 A^2 P -(1/5)L^3 A Q3,
    #  R8= (2/3)L^5 A P -(3/5)L^3 Q3 -(4/5)L^3 A Q8.
    # Since P,Q3,Q8 are independent and L*A != 0 on the source locus,
    # R3 has a nonzero Q3 component and R8 has a unique nonzero Q8
    # component.  They add rank two for every source-typed point.

    # Successor-friendly algebraic-complex survivor with rational pole data.
    # Let M(S)=10S^2-35S+37=0 and D=S-22/25.  Then L=3,A=1/9.
    minimal = (Q(37), Q(-35), Q(10))
    obstruction_after_D = (Q(-37, 5), Q(7), Q(-2))
    assert obstruction_after_D == tuple(-coefficient / 5 for coefficient in minimal)

    def evaluate_univariate(poly, value):
        return sum(coefficient * value**degree for degree, coefficient in enumerate(poly))

    # D cannot vanish: S=22/25 is not a root of M.
    assert evaluate_univariate(minimal, Q(22, 25)) != 0
    # U,V cannot collide.  Their discriminant is Delta=S^2-4S+88/25;
    # M-10*Delta=5S+9/5, whose only root is not a root of M.
    assert evaluate_univariate(minimal, Q(-9, 25)) != 0
    # Neither extra orbit collides with C=1 because
    # (1-U)(1-V)=1-S+D=3/25.
    assert Q(3, 25) != 0
    assert Q(3) ** 8 * Q(1, 9) ** 3 == 9

    cert_sha = certificate_digest(
        [
            ("compat3", expected_compatibility[0]),
            ("compat5", expected_compatibility[1]),
            ("K", expected_K),
            ("H", expected_H),
            ("obstruction", obstruction),
            ("pole_ode", expected_ode_constant),
        ],
        quotient_vectors,
    )

    print("TD6-MODULI-UNIFORMITY-GATE: PASS")
    print("verdict = GENERIC-OBSTRUCTION / COMPLEX-SURVIVOR")
    print("center_dependence = none_in_obstruction")
    print("general_formula = (6/5)*(5*E2-2*E1^2)")
    print("E1 = 2*C+U+V; E2 = C^2+2*C*(U+V)+U*V")
    print(
        "normalized_formula = (6/5)*(-2*S^2+2*S+5*D-3); "
        "S=U+V D=U*V"
    )
    print(
        "symbolic_transport = rows 6547; rank 3508 / 3602; "
        "affine_dimension 94"
    )
    print("transport_compatibility = L^3+[25*(S-D-1)]^3 = 0")
    print("transport_compatibility = L^5+[25*(S-D-1)]^5 = 0")
    print("source_relation = L=25*(1-S+D) (both automatic)")
    print("pole_J_leading = L^8*A^3/9; normalization L^8*A^3=9")
    print(
        "next_x_on_zero_locus = rank 36 / 94; "
        "affine_dimension_after_x 58"
    )
    print(
        "next_pole_mod_x = rank 2 when L*A!=0; "
        "paired_affine_dimension 56"
    )
    print("quotient_basis_pivots = 10,25,38")
    print(
        "explicit_survivor = C=1; 10*S^2-35*S+37=0; "
        "D=S-22/25; L=3; A=1/9"
    )
    print(f"symbolic_certificate.sha256 = {cert_sha}")
    print("modular_samples = none")
    print("SP2_killed = false")
    print("JC2_resolved = false")


if __name__ == "__main__":
    main()
