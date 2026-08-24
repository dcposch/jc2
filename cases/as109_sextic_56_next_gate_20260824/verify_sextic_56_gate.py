#!/usr/bin/env python3
"""Exact replay for the characteristic-zero (5,6) sextic gate.

The calculation is deliberately finite.  It reconstructs the polynomial
primitive missed by the parent preflight, derives the characteristic vector
field, searches for low-weight polynomial first integrals, and verifies the
weighted binary-form identities used in the pole and infinity arguments.
It does not enumerate supports and makes no AS109 or JC2 inference.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product


NAMES = ("A", "B", "C", "D", "alpha", "beta", "gamma", "delta")
X_NAMES = NAMES[:4]
WEIGHTS = (2, 3, 4, 5, 2, 3, 4, 5)
N = len(NAMES)
Exponent = tuple[int, ...]
Poly = dict[Exponent, Fraction]
Form = tuple[Poly, Poly, Poly, Poly]


def clean(poly: Poly) -> Poly:
    return {e: c for e, c in poly.items() if c}


def const(value: int | Fraction) -> Poly:
    value = Fraction(value)
    return {} if value == 0 else {(0,) * N: value}


def var(name: str) -> Poly:
    e = [0] * N
    e[NAMES.index(name)] = 1
    return {tuple(e): Fraction(1)}


def monomial(exponent: Exponent) -> Poly:
    return {exponent: Fraction(1)}


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for poly in polys:
        for e, c in poly.items():
            out[e] = out.get(e, Fraction(0)) + c
    return clean(out)


def scale(poly: Poly, scalar: int | Fraction) -> Poly:
    scalar = Fraction(scalar)
    return clean({e: scalar * c for e, c in poly.items()})


def mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for le, lc in left.items():
        for re, rc in right.items():
            e = tuple(a + b for a, b in zip(le, re))
            out[e] = out.get(e, Fraction(0)) + lc * rc
    return clean(out)


def power(poly: Poly, degree: int) -> Poly:
    out = const(1)
    for _ in range(degree):
        out = mul(out, poly)
    return out


def partial(poly: Poly, name: str) -> Poly:
    index = NAMES.index(name)
    out: Poly = {}
    for e, c in poly.items():
        if e[index] == 0:
            continue
        f = list(e)
        f[index] -= 1
        key = tuple(f)
        out[key] = out.get(key, Fraction(0)) + e[index] * c
    return clean(out)


def differential(poly: Poly) -> Form:
    return tuple(partial(poly, name) for name in X_NAMES)  # type: ignore[return-value]


def dot(form: Form, vector: Form) -> Poly:
    return add(*(mul(a, b) for a, b in zip(form, vector)))


def form_add(*forms: Form) -> Form:
    return tuple(add(*(form[i] for form in forms)) for i in range(4))  # type: ignore[return-value]


def form_scale(form: Form, scalar: int | Fraction) -> Form:
    return tuple(scale(entry, scalar) for entry in form)  # type: ignore[return-value]


def form_mul(poly: Poly, form: Form) -> Form:
    return tuple(mul(poly, entry) for entry in form)  # type: ignore[return-value]


def determinant(matrix: list[list[Poly]]) -> Poly:
    if len(matrix) == 1:
        return matrix[0][0]
    out: Poly = {}
    for column, entry in enumerate(matrix[0]):
        minor = [row[:column] + row[column + 1 :] for row in matrix[1:]]
        out = add(out, scale(mul(entry, determinant(minor)), -1 if column % 2 else 1))
    return out


def weighted_degree(exponent: Exponent) -> int:
    return sum(a * b for a, b in zip(exponent, WEIGHTS))


def homogeneous_monomials(weight: int, require_x: bool = True) -> list[Exponent]:
    bounds = [weight // w for w in WEIGHTS]
    out: list[Exponent] = []
    for e in product(*(range(bound + 1) for bound in bounds)):
        if weighted_degree(e) != weight:
            continue
        if require_x and sum(e[:4]) == 0:
            continue
        out.append(e)
    return sorted(out)


def rref(matrix: list[list[Fraction]], variable_count: int) -> tuple[list[list[Fraction]], list[int]]:
    rows = [row[:] for row in matrix]
    pivots: list[int] = []
    pivot_row = 0
    for column in range(variable_count):
        row = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if row is None:
            continue
        rows[pivot_row], rows[row] = rows[row], rows[pivot_row]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [entry / divisor for entry in rows[pivot_row]]
        for i in range(len(rows)):
            if i == pivot_row or rows[i][column] == 0:
                continue
            factor = rows[i][column]
            rows[i] = [a - factor * b for a, b in zip(rows[i], rows[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivots


def solve_columns(columns: list[Form], target: Form) -> tuple[list[Fraction], int]:
    keys = sorted(
        {(component, exponent) for component in range(4) for exponent in target[component]}
        | {
            (component, exponent)
            for column in columns
            for component in range(4)
            for exponent in column[component]
        }
    )
    augmented = [
        [column[component].get(exponent, Fraction(0)) for column in columns]
        + [target[component].get(exponent, Fraction(0))]
        for component, exponent in keys
    ]
    rows, pivots = rref(augmented, len(columns))
    assert all(not all(row[j] == 0 for j in range(len(columns))) or row[-1] == 0 for row in rows)
    assert len(pivots) == len(columns), "primitive ansatz was not unique modulo parameter constants"
    solution = [Fraction(0)] * len(columns)
    for row, pivot in enumerate(pivots):
        solution[pivot] = rows[row][-1]
    return solution, len(pivots)


def nullity_columns(columns: list[Poly]) -> int:
    keys = sorted({exponent for column in columns for exponent in column})
    matrix = [[column.get(exponent, Fraction(0)) for column in columns] for exponent in keys]
    _, pivots = rref(matrix, len(columns))
    return len(columns) - len(pivots)


def system() -> dict[str, object]:
    A, B, C, D, alpha, beta, gamma, delta = (var(name) for name in NAMES)

    I3 = add(
        scale(mul(power(A, 2), B), Fraction(-12, 25)),
        scale(mul(mul(alpha, A), B), Fraction(-4, 5)),
        scale(mul(beta, power(A, 2)), Fraction(-3, 5)),
        scale(mul(A, D), Fraction(6, 5)),
        mul(delta, A),
        scale(mul(B, C), Fraction(6, 5)),
        scale(mul(gamma, B), 2),
        scale(mul(beta, C), 3),
        scale(mul(alpha, D), 4),
    )
    I2 = add(
        scale(power(A, 4), Fraction(9, 125)),
        scale(mul(alpha, power(A, 3)), Fraction(4, 25)),
        scale(mul(A, power(B, 2)), Fraction(-12, 25)),
        scale(mul(power(A, 2), C), Fraction(-12, 25)),
        scale(mul(mul(alpha, A), C), Fraction(-4, 5)),
        scale(mul(mul(beta, A), B), Fraction(-6, 5)),
        scale(mul(gamma, power(A, 2)), Fraction(-3, 5)),
        scale(mul(alpha, power(B, 2)), Fraction(-2, 5)),
        scale(mul(D, B), Fraction(6, 5)),
        mul(delta, B),
        scale(power(C, 2), Fraction(3, 5)),
        scale(mul(gamma, C), 2),
        scale(mul(beta, D), 3),
    )
    I1 = add(
        scale(mul(power(A, 3), B), Fraction(24, 125)),
        scale(mul(mul(alpha, power(A, 2)), B), Fraction(8, 25)),
        scale(mul(beta, power(A, 3)), Fraction(4, 25)),
        scale(power(B, 3), Fraction(-4, 25)),
        scale(mul(mul(alpha, B), C), Fraction(-4, 5)),
        scale(mul(beta, power(B, 2)), Fraction(-3, 5)),
        scale(mul(mul(A, B), C), Fraction(-18, 25)),
        scale(mul(mul(beta, A), C), Fraction(-3, 5)),
        scale(mul(mul(gamma, A), B), Fraction(-4, 5)),
        scale(mul(power(A, 2), D), Fraction(-6, 25)),
        scale(mul(delta, power(A, 2)), Fraction(-1, 5)),
        scale(mul(C, D), Fraction(6, 5)),
        scale(mul(gamma, D), 2),
        mul(delta, C),
    )

    omega: Form = (
        add(
            scale(mul(power(A, 2), B), Fraction(24, 125)),
            scale(mul(mul(alpha, A), B), Fraction(8, 25)),
            scale(mul(B, C), Fraction(-18, 25)),
            scale(mul(beta, C), Fraction(-3, 5)),
            scale(mul(gamma, B), Fraction(-4, 5)),
        ),
        add(
            scale(power(B, 2), Fraction(-12, 25)),
            scale(mul(A, C), Fraction(-6, 25)),
            scale(mul(alpha, C), Fraction(-4, 5)),
            scale(mul(beta, B), Fraction(-6, 5)),
        ),
        add(
            scale(mul(A, B), Fraction(-6, 25)),
            scale(mul(alpha, B), Fraction(-4, 5)),
            scale(mul(beta, A), Fraction(3, 5)),
            scale(D, Fraction(6, 5)),
            delta,
        ),
        add(
            scale(power(A, 2), Fraction(6, 25)),
            scale(mul(alpha, A), Fraction(8, 5)),
            scale(C, Fraction(6, 5)),
            scale(gamma, 2),
        ),
    )
    eta: Form = (
        add(
            scale(mul(power(A, 2), C), Fraction(12, 125)),
            scale(mul(mul(alpha, A), C), Fraction(4, 25)),
            scale(power(C, 2), Fraction(-6, 25)),
            scale(mul(gamma, C), Fraction(-2, 5)),
        ),
        add(scale(mul(B, C), Fraction(-6, 25)), scale(mul(beta, C), Fraction(-3, 5))),
        add(scale(mul(A, C), Fraction(-6, 25)), scale(mul(alpha, C), Fraction(-4, 5))),
        add(
            scale(mul(A, B), Fraction(6, 25)),
            scale(mul(alpha, B), Fraction(4, 5)),
            scale(mul(beta, A), Fraction(3, 5)),
            scale(D, Fraction(6, 5)),
            delta,
        ),
    )

    # Exact bounded integrating-combination search:
    # dH - mu*dI3 = omega, wt(H)=9, wt(mu)=2.
    h_monomials = homogeneous_monomials(9)
    h_columns: list[Form] = [differential(monomial(e)) for e in h_monomials]
    # A possible alpha term in mu is the trivial freedom
    # (H,mu)->(H+c*alpha*I3,mu+c*alpha); quotient it by normalizing its
    # coefficient to zero.
    h_columns.append(form_scale(form_mul(A, differential(I3)), -1))
    solution, primitive_rank = solve_columns(h_columns, omega)
    H: Poly = {}
    for coefficient, exponent in zip(solution[: len(h_monomials)], h_monomials):
        H = add(H, scale(monomial(exponent), coefficient))
    mu = scale(A, solution[-1])
    assert H == I1
    assert mu == scale(A, Fraction(-2, 5))
    assert differential(I1) == form_add(omega, form_scale(form_mul(A, differential(I3)), Fraction(-2, 5)))

    gradients = [list(differential(integral)) for integral in (I1, I2, I3)]
    vector: list[Poly] = []
    for column in range(4):
        minor = [row[:column] + row[column + 1 :] for row in gradients]
        vector.append(scale(determinant(minor), -1 if column % 2 else 1))
    V: Form = tuple(vector)  # type: ignore[assignment]
    assert all(dot(differential(integral), V) == {} for integral in (I1, I2, I3))
    assert dot(omega, V) == {}
    eta_V = dot(eta, V)
    assert eta_V

    # Bounded zero-cofactor Darboux search for the characteristic derivation.
    # Parameter-only polynomials are omitted from the ansatz.
    darbouxs: dict[int, int] = {}
    for weight in range(1, 10):
        candidates = homogeneous_monomials(weight)
        columns = [dot(differential(monomial(e)), V) for e in candidates]
        darbouxs[weight] = nullity_columns(columns) if columns else 0
    assert darbouxs == {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 2}

    return {
        "primitive_search": {
            "ansatz": "wt(H)=9; wt(mu)=2; dH-mu*dI3=omega",
            "unknowns": len(h_columns),
            "rank": primitive_rank,
            "solution": "H=I1, mu=-2*A/5 (unique modulo alpha*I3 freedom)",
        },
        "characteristic_vector": "V_i=(-1)^i det(d(I1,I2,I3)/dX_without_i)",
        "V_annihilates": ["I1", "I2", "I3", "omega"],
        "eta_V_nonzero_polynomial": bool(eta_V),
        "bounded_zero_cofactor_darboux_nullities": darbouxs,
        "weights": dict(zip(NAMES, WEIGHTS)),
    }


def binary_top_and_boundary_control() -> dict[str, object]:
    # Sparse polynomials in (t,z,A,B,C,D) for the homogeneous binary forms.
    names = ("t", "z", "A", "B", "C", "D")
    count = len(names)
    BPoly = dict[tuple[int, ...], Fraction]

    def bc(value: int | Fraction) -> BPoly:
        value = Fraction(value)
        return {} if not value else {(0,) * count: value}

    def bv(name: str) -> BPoly:
        e = [0] * count
        e[names.index(name)] = 1
        return {tuple(e): Fraction(1)}

    def ba(*ps: BPoly) -> BPoly:
        out: BPoly = {}
        for p in ps:
            for e, c in p.items():
                out[e] = out.get(e, Fraction(0)) + c
        return {e: c for e, c in out.items() if c}

    def bs(p: BPoly, scalar: int | Fraction) -> BPoly:
        scalar = Fraction(scalar)
        return {e: scalar * c for e, c in p.items() if scalar * c}

    def bm(*polys: BPoly) -> BPoly:
        out = bc(1)
        for right in polys:
            product_out: BPoly = {}
            for le, lc in out.items():
                for re, rc in right.items():
                    e = tuple(a + b for a, b in zip(le, re))
                    product_out[e] = product_out.get(e, Fraction(0)) + lc * rc
            out = {e: c for e, c in product_out.items() if c}
        return out

    def bp(p: BPoly, n: int) -> BPoly:
        out = bc(1)
        for _ in range(n):
            out = bm(out, p)
        return out

    def bd(p: BPoly, name: str) -> BPoly:
        index = names.index(name)
        out: BPoly = {}
        for e, c in p.items():
            if e[index] == 0:
                continue
            f = list(e)
            f[index] -= 1
            out[tuple(f)] = c * e[index]
        return out

    t, z, A, B, C, D = (bv(name) for name in names)
    F = ba(bp(z, 5), bm(A, bp(t, 2), bp(z, 3)), bm(B, bp(t, 3), bp(z, 2)), bm(C, bp(t, 4), z), bm(D, bp(t, 5)))
    G = ba(
        bp(z, 6),
        bs(bm(A, bp(t, 2), bp(z, 4)), Fraction(6, 5)),
        bs(bm(B, bp(t, 3), bp(z, 3)), Fraction(6, 5)),
        bm(ba(bs(bp(A, 2), Fraction(3, 25)), bs(C, Fraction(6, 5))), bp(t, 4), bp(z, 2)),
        bm(ba(bs(bm(A, B), Fraction(6, 25)), bs(D, Fraction(6, 5))), bp(t, 5), z),
        bm(ba(bs(bp(A, 3), Fraction(-4, 125)), bs(bm(A, C), Fraction(6, 25)), bs(bp(B, 2), Fraction(3, 25))), bp(t, 6)),
    )
    J = ba(bm(bd(F, "t"), bd(G, "z")), bs(bm(bd(F, "z"), bd(G, "t")), -1))

    # Expected coefficient identities after setting I1=I2=I3=0.
    J3 = ba(bs(bm(bp(A, 2), B), -2), bs(bm(A, D), 5), bs(bm(B, C), 5))
    J2 = ba(bs(bp(A, 4), 3), bs(bm(A, bp(B, 2)), -20), bs(bm(bp(A, 2), C), -20), bs(bm(B, D), 50), bs(bp(C, 2), 25))
    J1 = ba(bs(bm(bp(A, 3), B), 12), bs(bp(B, 3), -10), bs(bm(A, B, C), -45), bs(bm(bp(A, 2), D), -15), bs(bm(C, D), 75))
    H10 = ba(bs(bm(bp(A, 3), C), 4), bs(bm(A, bp(C, 2)), -30), bs(bm(bp(B, 2), C), -15), bs(bm(A, B, D), 25), bs(bp(D, 2), 125))
    expected = ba(
        bs(bm(J3, bp(t, 6), bp(z, 3)), Fraction(42, 25)),
        bs(bm(J2, bp(t, 7), bp(z, 2)), Fraction(24, 125)),
        bs(bm(J1, bp(t, 8), z), Fraction(18, 125)),
        bs(bm(A, J3, bp(t, 8), z), Fraction(84, 125)),
        bs(bm(H10, bp(t, 9)), Fraction(6, 125)),
    )
    assert J == expected

    # Two minimal one-boundary survivors show that neither boundary may be
    # dropped.  They lie on I1=I2=I3=0 when the integration parameters are
    # zero.
    r = Fraction(-1)
    d_f = -r**5
    f_on_f_control = r**5 + d_f
    g_on_f_control = r**6 + Fraction(6, 5) * d_f * r
    assert f_on_f_control == 0 and g_on_f_control == Fraction(-1, 5)
    d_g = Fraction(-5, 6) * r**5
    f_on_g_control = r**5 + d_g
    g_on_g_control = r**6 + Fraction(6, 5) * d_g * r
    assert f_on_g_control == Fraction(-1, 6) and g_on_g_control == 0
    # With r=-x^-1, D=c*x^-5 and h=x^11, eta=(6/5)D D'
    # gives h*eta=-6*c^2.
    speed_f = -6 * d_f**2
    speed_g = -6 * d_g**2
    assert speed_f == -6 and speed_g == Fraction(-25, 6)

    return {
        "binary_forms": "deg(F,G)=(5,6), depressed F has no t*z^4 term",
        "jacobian_identity": "J_tz=(42/25)J3*t^6*z^3+(24/125)J2*t^7*z^2+((18/125)J1+(84/125)A*J3)t^8*z+(6/125)H10*t^9",
        "boundary_lemma": "a shared finite linear factor plus J1=J2=J3=0 forces H10=0, then F=z^5 and G=z^6",
        "one_boundary_controls": {
            "F_only": {"F0": str(f_on_f_control), "G0": str(g_on_f_control), "h_eta": str(speed_f)},
            "G_only": {"F0": str(f_on_g_control), "G0": str(g_on_g_control), "h_eta": str(speed_g)},
        },
        "both_boundaries_used": True,
    }


def main() -> None:
    print(
        json.dumps(
            {
                "verdict": "EXACT-(5,6)-EXCLUSION",
                "system": system(),
                "weighted_gate": binary_top_and_boundary_control(),
                "finite_pole_survivor": False,
                "actual_degree_pair_5_6_exists": False,
                "full_sextic_theorem_proved": False,
                "as109_floor_raised": False,
                "support_enumeration": False,
                "aws_used": False,
                "lift_found": False,
                "jc2_inference": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
