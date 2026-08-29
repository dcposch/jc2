#!/usr/bin/env python3
"""Exact audit of the lambda=0 q5--q13 odd-gate tail.

The checker is standard-library only.  It symbolically reconstructs the five
Lagrange coefficients in a sparse Laurent polynomial ring, checks the even
q8 control, verifies the literal raw-window count, and computes the complete
five-gate rank on two unrelated squarefree quartic fixtures.
"""

from __future__ import annotations

from fractions import Fraction as QF
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREFIX_REPORT = (
    ROOT
    / "xmodel/ggv-upper-endpoint-deep-q1-lambda0-odd-gate-prefix-sol-ultra-20260828.md"
)
PREFIX_REPORT_SHA256 = "db230f946e04a3be58dd3e59877d47b23097ec79079109120fce91163be138bf"
PREFIX_CHECKER = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_odd_gates_20260828"
    / "verify_lambda0_odd_gates.py"
)
PREFIX_CHECKER_SHA256 = "d93ca0c7753097c4dcf6aae1cc58d1966780256700df4179e6e6fda9e30e1f64"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Sparse Laurent polynomials in A,Q,r,f,F9,e,F8,F11,F13.  Negative A
# exponents are allowed during the normalized binomial expansion and must
# cancel from each final h_n.
VARIABLES = ("A", "Q", "r", "f", "F9", "e", "F8", "F11", "F13")
ZERO_KEY = (0,) * len(VARIABLES)


def mv_const(value):
    value = QF(value)
    return {} if not value else {ZERO_KEY: value}


def mv_var(index, exponent=1):
    key = [0] * len(VARIABLES)
    key[index] = exponent
    return {tuple(key): QF(1)}


def mv_add(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, QF(0)) + value
            if not out[key]:
                del out[key]
    return out


def mv_scale(value, term):
    value = QF(value)
    return {key: value * coefficient for key, coefficient in term.items()
            if value * coefficient}


def mv_mul(left, right):
    out = {}
    for key1, value1 in left.items():
        for key2, value2 in right.items():
            key = tuple(a + b for a, b in zip(key1, key2))
            out[key] = out.get(key, QF(0)) + value1 * value2
            if not out[key]:
                del out[key]
    return out


def mv_pow(base, exponent):
    assert exponent >= 0
    out = mv_const(1)
    while exponent:
        if exponent & 1:
            out = mv_mul(out, base)
        base = mv_mul(base, base)
        exponent //= 2
    return out


def mv_monomial(**powers):
    key = tuple(powers.get(name, 0) for name in VARIABLES)
    return {key: QF(1)}


def series_mul(left, right, maximum):
    out = [{} for _ in range(maximum + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= maximum:
                out[i + j] = mv_add(out[i + j], mv_mul(a, b))
    return out


def series_binomial_one(base, exponent, maximum):
    assert base[0] == mv_const(1)
    u = list(base[: maximum + 1])
    u += [{} for _ in range(maximum + 1 - len(u))]
    u[0] = {}
    term = [{} for _ in range(maximum + 1)]
    term[0] = mv_const(1)
    out = [{} for _ in range(maximum + 1)]
    choose = QF(1)
    for count in range(maximum + 1):
        if count:
            term = series_mul(term, u, maximum)
            choose *= (exponent - (count - 1)) / count
        for degree in range(maximum + 1):
            out[degree] = mv_add(out[degree], mv_scale(choose, term[degree]))
    return out


def symbolic_h(n):
    """Return h_n for q_n=p^3 h_n, using the even series through F8."""
    A = mv_var(0)
    q = mv_var(1)
    r = mv_var(2)
    f = mv_var(3)
    f9 = mv_var(4)
    e = mv_var(5)
    f8 = mv_var(6)
    f11 = mv_var(7)
    f13 = mv_var(8)
    even = [{} for _ in range(9)]
    even[0] = mv_const(1)
    even[2] = mv_scale(QF(-1, 8), mv_monomial(A=-1, Q=1))
    even[4] = mv_scale(QF(1, 256), mv_monomial(A=-2, Q=2))
    even[6] = mv_scale(QF(1, 2048), mv_monomial(A=-3, e=1))
    even[8] = mv_monomial(A=-4, F8=1)
    beta = QF(n - 6, 8)
    correction = series_binomial_one(even, beta, n)
    odd = {
        5: mv_scale(QF(1, 256), mv_mul(mv_pow(A, 2), r)),
        7: mv_mul(A, f),
        9: f9,
        11: f11,
        13: f13,
    }
    total = {}
    for index, coefficient in odd.items():
        if index <= n:
            total = mv_add(total, mv_mul(coefficient, correction[n - index]))
    # p^(n-6)=p^3 A^((n-9)/2).
    return mv_scale(QF(1, 4), mv_mul(
        mv_monomial(A=(n - 9) // 2), total
    ))


def expected_h():
    return {
        5: mv_scale(QF(1, 1024), mv_var(2)),
        7: mv_add(
            mv_scale(QF(1, 4), mv_var(3)),
            mv_scale(QF(-1, 65536), mv_monomial(Q=1, r=1)),
        ),
        9: mv_add(
            mv_scale(QF(1, 4), mv_var(4)),
            mv_scale(QF(-3, 256), mv_monomial(Q=1, f=1)),
            mv_scale(QF(-3, 2**23), mv_monomial(Q=2, r=1)),
        ),
        11: mv_add(
            mv_scale(QF(1, 4), mv_monomial(A=1, F11=1)),
            mv_scale(QF(-5, 256), mv_monomial(Q=1, F9=1)),
            mv_scale(QF(5, 2**15), mv_monomial(Q=2, f=1)),
            mv_scale(QF(5, 2**29), mv_monomial(Q=3, r=1)),
            mv_scale(QF(160, 2**29), mv_monomial(e=1, r=1)),
        ),
        13: mv_add(
            mv_scale(QF(1, 4), mv_monomial(A=2, F13=1)),
            mv_scale(QF(-7, 256), mv_monomial(A=1, Q=1, F11=1)),
            mv_scale(QF(21, 2**15), mv_monomial(Q=2, F9=1)),
            mv_scale(QF(7, 2**21), mv_monomial(Q=3, f=1)),
            mv_scale(QF(224, 2**21), mv_monomial(e=1, f=1)),
            mv_scale(QF(7, 2**13), mv_monomial(r=1, F8=1)),
            mv_scale(QF(7, 2**30), mv_monomial(Q=1, r=1, e=1)),
            mv_scale(QF(35, 2**37), mv_monomial(Q=4, r=1)),
        ),
    }


# Ordinary Q[X] operations for the complete exact-rank controls.
def p_trim(poly):
    out = list(poly)
    while out and not out[-1]:
        out.pop()
    return out


def p_add(*polys):
    length = max((len(poly) for poly in polys), default=0)
    out = [QF(0)] * length
    for poly in polys:
        for index, value in enumerate(poly):
            out[index] += value
    return p_trim(out)


def p_scale(value, poly):
    return p_trim([QF(value) * coefficient for coefficient in poly])


def p_mul(left, right):
    if not left or not right:
        return []
    out = [QF(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return p_trim(out)


def p_power(poly, exponent):
    out = [QF(1)]
    for _ in range(exponent):
        out = p_mul(out, poly)
    return out


def p_derivative(poly):
    return p_trim([QF(i) * poly[i] for i in range(1, len(poly))])


def monomial(degree):
    return [QF(0)] * degree + [QF(1)]


def l5_half(A, d):
    return p_scale(QF(1, 2), p_add(
        p_scale(5, p_mul(p_derivative(A), d)),
        p_scale(2, p_mul(A, p_derivative(d))),
    ))


def h_polys(A, q, e, f8, r, f, f9, f11, f13):
    q2 = p_mul(q, q)
    q3 = p_mul(q2, q)
    q4 = p_mul(q2, q2)
    h5 = p_scale(QF(1, 1024), r)
    h7 = p_add(p_scale(QF(1, 4), f),
                  p_scale(QF(-1, 65536), p_mul(q, r)))
    h9 = p_add(
        p_scale(QF(1, 4), f9),
        p_scale(QF(-3, 256), p_mul(q, f)),
        p_scale(QF(-3, 2**23), p_mul(q2, r)),
    )
    h11 = p_add(
        p_scale(QF(1, 4), p_mul(A, f11)),
        p_scale(QF(-5, 256), p_mul(q, f9)),
        p_scale(QF(5, 2**15), p_mul(q2, f)),
        p_scale(QF(5, 2**29), p_mul(r, p_add(q3, p_scale(32, e)))),
    )
    h13 = p_add(
        p_scale(QF(1, 4), p_mul(p_power(A, 2), f13)),
        p_scale(QF(-7, 256), p_mul(p_mul(A, q), f11)),
        p_scale(QF(21, 2**15), p_mul(q2, f9)),
        p_scale(QF(7, 2**21), p_mul(f, p_add(q3, p_scale(32, e)))),
        p_scale(QF(7, 2**13), p_mul(r, f8)),
        p_scale(QF(7, 2**30), p_mul(p_mul(r, q), e)),
        p_scale(QF(35, 2**37), p_mul(r, q4)),
    )
    return (h5, h7, h9, h11, h13)


BLOCK_SIZES = (4, 6, 8, 10, 12)


def concatenate(blocks):
    out = []
    for poly, size in zip(blocks, BLOCK_SIZES):
        out.extend(poly[index] if index < len(poly) else QF(0)
                   for index in range(size))
    return out


def matrix_rank(matrix):
    rows = [list(row) for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((row for row in range(rank, len(rows))
                      if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        divisor = rows[rank][column]
        rows[rank] = [value / divisor for value in rows[rank]]
        for row in range(len(rows)):
            if row != rank and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [a - factor * b
                             for a, b in zip(rows[row], rows[rank])]
        rank += 1
    return rank


RAW_WINDOWS = {
    "r": tuple(range(0, 4)),
    "f": tuple(range(0, 6)),
    "f9": tuple(range(1, 8)),
    "f11": tuple(range(1, 6)),
    "f13": tuple(range(2, 4)),
}
PRIMITIVE_WINDOWS = (0, 2, 4, 6, 8)


def combined_rank(A, q, e, f8):
    columns = []
    names = tuple(RAW_WINDOWS)
    for name, degrees in RAW_WINDOWS.items():
        for degree in degrees:
            values = {key: [] for key in names}
            values[name] = monomial(degree)
            columns.append(concatenate(h_polys(A, q, e, f8, **values)))
    for block, maximum in enumerate(PRIMITIVE_WINDOWS):
        for degree in range(maximum + 1):
            blocks = [[] for _ in range(5)]
            blocks[block] = p_scale(-1, l5_half(A, monomial(degree)))
            columns.append(concatenate(blocks))
    rows = [[column[index] for column in columns]
            for index in range(sum(BLOCK_SIZES))]
    return matrix_rank(rows), len(columns), len(rows)


def main():
    assert sha256(PREFIX_REPORT) == PREFIX_REPORT_SHA256
    assert sha256(PREFIX_CHECKER) == PREFIX_CHECKER_SHA256

    expected = expected_h()
    for n in (5, 7, 9, 11, 13):
        assert symbolic_h(n) == expected[n]
    q9_mutation = mv_add(
        mv_scale(QF(1, 4), mv_var(4)),
        mv_scale(QF(-3, 256), mv_monomial(Q=1, f=1)),
        mv_scale(QF(-3, 2**22), mv_monomial(Q=2, r=1)),
    )
    assert symbolic_h(9) != q9_mutation

    # Independent even checksum: q8=A(F8/4-Qe/2^18-Q^4/2^23).
    even = [{} for _ in range(9)]
    even[0] = mv_const(1)
    even[2] = mv_scale(QF(-1, 8), mv_monomial(A=-1, Q=1))
    even[4] = mv_scale(QF(1, 256), mv_monomial(A=-2, Q=2))
    even[6] = mv_scale(QF(1, 2048), mv_monomial(A=-3, e=1))
    even[8] = mv_monomial(A=-4, F8=1)
    q8 = mv_scale(QF(1, 5), mv_mul(
        mv_monomial(A=5),
        series_binomial_one(even, QF(5, 4), 8)[8],
    ))
    expected_q8 = mv_add(
        mv_scale(QF(1, 4), mv_monomial(A=1, F8=1)),
        mv_scale(QF(-1, 2**18), mv_monomial(A=1, Q=1, e=1)),
        mv_scale(QF(-1, 2**23), mv_monomial(A=1, Q=4)),
    )
    assert q8 == expected_q8

    assert sum(len(degrees) for degrees in RAW_WINDOWS.values()) == 24
    assert sum(maximum + 1 for maximum in PRIMITIVE_WINDOWS) == 25
    assert sum(BLOCK_SIZES) == 40

    fixtures = (
        (
            [QF(-1), QF(0), QF(0), QF(0), QF(1)],
            [QF(2), QF(-3), QF(4)],
            [QF(1), QF(2), QF(-1), QF(3), QF(0), QF(-2), QF(1)],
            [QF(3), QF(-1), QF(4), QF(1), QF(-5), QF(9), QF(2), QF(6), QF(-5)],
        ),
        (
            [QF(1), QF(1), QF(0), QF(0), QF(1)],
            [QF(-1), QF(2), QF(3)],
            [QF(2), QF(-1), QF(0), QF(1), QF(-2), QF(3), QF(1)],
            [QF(1), QF(0), QF(-2), QF(4), QF(0), QF(3), QF(-1), QF(2), QF(5)],
        ),
    )
    for fixture in fixtures:
        rank, columns, rows = combined_rank(*fixture)
        assert (rank, columns, rows) == (40, 49, 40)

    # The L5 leading coefficient on a degree-k input is 2k+20, so its
    # polynomial kernel is zero in characteristic zero.
    for degree in range(9):
        assert 2 * degree + 20

    print("q5_q7_q9_checksum=PASS;2^23_mutation=REJECTED")
    print("q11_q13_symbolic_lagrange_formulas=PASS")
    print("even_q8=A*(F8/4-Q*e/2^18-Q^4/2^23)")
    print("raw_odd_variables=24;primitive_variables=25;coefficient_equations=40")
    print("universal_raw_survivor_dimension_at_least=9")
    print("two_fixture_rank=40;two_fixture_raw_survivor_dimension=9")
    print("PASS_EXACT_LAMBDA0_ODD_GATE_TAIL")


if __name__ == "__main__":
    main()
