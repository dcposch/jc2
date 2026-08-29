#!/usr/bin/env python3
"""Exact checks for the lambda=0 q3/q5/q7/q9 odd-gate prefix.

The universal statements are hand algebra in the accompanying producer
report.  This checker independently expands the Lagrange coefficient formula
over exact rationals, guards the q5/q7/q9 constants, and checks the relevant
degree-bounded connection ranks on two squarefree quartics.
"""

from __future__ import annotations

from fractions import Fraction as Q


def trim(poly):
    out = list(poly)
    while out and not out[-1]:
        out.pop()
    return out


def add(left, right):
    out = [Q(0)] * max(len(left), len(right))
    for i in range(len(out)):
        out[i] = (left[i] if i < len(left) else 0) + (
            right[i] if i < len(right) else 0
        )
    return trim(out)


def scale(value, poly):
    return trim([Q(value) * coefficient for coefficient in poly])


def mul(left, right):
    if not left or not right:
        return []
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def derivative(poly):
    return trim([Q(i) * poly[i] for i in range(1, len(poly))])


def power(poly, exponent):
    out = [Q(1)]
    base = list(poly)
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent //= 2
    return out


def series_mul(left, right, maximum):
    out = [Q(0)] * (maximum + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= maximum:
                out[i + j] += a * b
    return out


def series_power_one(base, exponent, maximum):
    assert base[0] == 1
    u = list(base[: maximum + 1]) + [Q(0)] * max(0, maximum + 1 - len(base))
    u[0] = 0
    out = [Q(0)] * (maximum + 1)
    term = [Q(0)] * (maximum + 1)
    term[0] = 1
    choose = Q(1)
    for k in range(maximum + 1):
        if k:
            term = series_mul(term, u, maximum)
            choose *= (exponent - (k - 1)) / k
        for degree, coefficient in enumerate(term):
            out[degree] += choose * coefficient
    return out


def q_coefficient(p, rows, n):
    """q_n=2/(n+2)[t^n]F^((n+2)/8), with F0=p^8."""
    f0 = Q(p) ** 8
    normalized = [Q(0)] * (n + 1)
    normalized[0] = 1
    for degree, value in rows.items():
        if 0 < degree <= n:
            normalized[degree] = Q(value) / f0
    coefficient = series_power_one(normalized, Q(n + 2, 8), n)[n]
    return Q(2, n + 2) * Q(p) ** (n + 2) * coefficient


def matrix_rank(matrix):
    rows = [list(map(Q, row)) for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        divisor = rows[rank][column]
        rows[rank] = [value / divisor for value in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][column]:
                factor = rows[r][column]
                rows[r] = [a - factor * b for a, b in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def coefficient_matrix(columns):
    maximum = max((len(poly) for poly in columns), default=0)
    return [
        [poly[degree] if degree < len(poly) else Q(0) for poly in columns]
        for degree in range(maximum)
    ]


def q3_d12_rank(A):
    """Kernel of 2AC'+A'C=16A*(A*u), deg C<=6, deg u<=1."""
    Ap = derivative(A)
    columns = []
    for degree in range(7):
        monomial = [Q(0)] * degree + [Q(1)]
        columns.append(add(scale(2, mul(A, derivative(monomial))), mul(Ap, monomial)))
    for degree in range(2):
        monomial = [Q(0)] * degree + [Q(1)]
        columns.append(scale(-16, mul(power(A, 2), monomial)))
    return matrix_rank(coefficient_matrix(columns)), len(columns)


def q5_rank(A):
    """Kernel of 2AC'+3A'C=A*r, deg C<=4, deg r<=3."""
    Ap = derivative(A)
    columns = []
    for degree in range(5):
        monomial = [Q(0)] * degree + [Q(1)]
        columns.append(add(scale(2, mul(A, derivative(monomial))), scale(3, mul(Ap, monomial))))
    for degree in range(4):
        monomial = [Q(0)] * degree + [Q(1)]
        columns.append(scale(-1, mul(A, monomial)))
    return matrix_rank(coefficient_matrix(columns)), len(columns)


def q7_image_rank(A):
    Ap = derivative(A)
    columns = []
    for degree in range(3):
        monomial = [Q(0)] * degree + [Q(1)]
        columns.append(add(scale(5, mul(Ap, monomial)), scale(2, mul(A, derivative(monomial)))))
    return matrix_rank(coefficient_matrix(columns))


def main():
    fixtures = [
        (Q(2), Q(3, 5), Q(-7, 3), Q(11, 4), Q(-5, 6)),
        (Q(3), Q(-2, 7), Q(5, 9), Q(-13, 8), Q(17, 10)),
        (Q(5), Q(7, 11), Q(19, 13), Q(23, 17), Q(-29, 19)),
    ]
    for p, q, r, f, f9 in fixtures:
        A = p * p
        rows = {
            2: -A ** 3 * q / 8,
            4: A ** 2 * q * q / 256,
            5: A ** 2 * r / 256,
            6: Q(31, 37),
            7: A * f,
            8: Q(-41, 43),
            9: f9,
        }
        q5 = q_coefficient(p, rows, 5)
        q7 = q_coefficient(p, rows, 7)
        q9 = q_coefficient(p, rows, 9)
        assert q5 == p ** 3 * r / 1024
        assert q7 == p ** 3 * (f / 4 - q * r / 65536)
        expected9 = p ** 3 * (
            f9 / 4 - 3 * q * f / 256 - 3 * q * q * r / 8388608
        )
        assert q9 == expected9
        mutated9 = p ** 3 * (
            f9 / 4 - 3 * q * f / 256 - 3 * q * q * r / 4194304
        )
        assert q9 != mutated9

    quartics = [
        [Q(-1), Q(0), Q(0), Q(0), Q(1)],
        [Q(1), Q(1), Q(0), Q(0), Q(1)],
    ]
    for A in quartics:
        rank3, columns3 = q3_d12_rank(A)
        rank5, columns5 = q5_rank(A)
        assert rank3 == columns3 == 9
        assert columns5 - rank5 == 1
        assert q7_image_rank(A) == 3

    print("q5=p^3*r/1024")
    print("q7=p^3*(f/4-Q*r/65536)")
    print("q9=p^3*(F9/4-3*Q*f/256-3*Q^2*r/2^23)")
    print("q3_plus_D12_nullity=0;q5_connection_nullity=1;q7_image_rank=3")
    print("PASS_EXACT_LAMBDA0_ODD_GATE_PREFIX")


if __name__ == "__main__":
    main()
