#!/usr/bin/env python3
"""Exact q15 and combined q5--q15 audit on the lambda-zero branch."""

from __future__ import annotations

from fractions import Fraction as QF
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAIL_REPORT = ROOT / "xmodel/ggv-upper-endpoint-deep-q1-lambda0-odd-gate-tail-independent-sol-ultra-20260828.md"
TAIL_REPORT_SHA256 = "b649e0821a07fa8d3ed861169b608a5b4dcd8356452f875b8b218693d3cb69a0"
TAIL_CHECKER = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_odd_gate_tail_20260828"
    / "verify_lambda0_odd_gate_tail.py"
)
TAIL_CHECKER_SHA256 = "c063ccc20c12785d092f56c65e2def86215ae1cc49fb6c3cf8ab4754e1c782ca"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Sparse Laurent ring used to derive q15 directly from F^(17/8).
NAMES = ("A", "Q", "r", "f", "F9", "e", "F8", "F10", "F11", "F13")
ZERO = (0,) * len(NAMES)


def s_const(value):
    value = QF(value)
    return {} if not value else {ZERO: value}


def s_monomial(**powers):
    return {tuple(powers.get(name, 0) for name in NAMES): QF(1)}


def s_add(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, QF(0)) + value
            if not out[key]:
                del out[key]
    return out


def s_scale(value, term):
    value = QF(value)
    return {key: value * coefficient for key, coefficient in term.items()
            if value * coefficient}


def s_mul(left, right):
    out = {}
    for key1, value1 in left.items():
        for key2, value2 in right.items():
            key = tuple(a + b for a, b in zip(key1, key2))
            out[key] = out.get(key, QF(0)) + value1 * value2
            if not out[key]:
                del out[key]
    return out


def series_mul(left, right, maximum):
    out = [{} for _ in range(maximum + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= maximum:
                out[i + j] = s_add(out[i + j], s_mul(a, b))
    return out


def series_binomial_one(base, exponent, maximum):
    assert base[0] == s_const(1)
    u = list(base) + [{} for _ in range(maximum + 1 - len(base))]
    u = u[: maximum + 1]
    u[0] = {}
    out = [{} for _ in range(maximum + 1)]
    term = [{} for _ in range(maximum + 1)]
    term[0] = s_const(1)
    choose = QF(1)
    for count in range(maximum + 1):
        if count:
            term = series_mul(term, u, maximum)
            choose *= (exponent - (count - 1)) / count
        for degree in range(maximum + 1):
            out[degree] = s_add(out[degree], s_scale(choose, term[degree]))
    return out


def derive_h15():
    # F/F0, with F0=A^4.  F12/F14 cannot enter weight 15 because the first
    # nonzero odd weight is five, and F15 is absent.
    normalized = [{} for _ in range(16)]
    normalized[0] = s_const(1)
    normalized[2] = s_scale(QF(-1, 8), s_monomial(A=-1, Q=1))
    normalized[4] = s_scale(QF(1, 256), s_monomial(A=-2, Q=2))
    normalized[5] = s_scale(QF(1, 256), s_monomial(A=-2, r=1))
    normalized[6] = s_scale(QF(1, 2048), s_monomial(A=-3, e=1))
    normalized[7] = s_monomial(A=-3, f=1)
    normalized[8] = s_monomial(A=-4, F8=1)
    normalized[9] = s_monomial(A=-4, F9=1)
    normalized[10] = s_monomial(A=-4, F10=1)
    normalized[11] = s_monomial(A=-4, F11=1)
    normalized[13] = s_monomial(A=-4, F13=1)
    coefficient = series_binomial_one(normalized, QF(17, 8), 15)[15]
    # q15/p^3=(2/17)*p^14*[t15](F/F0)^(17/8)=(2/17)A^7*coefficient.
    return s_scale(QF(2, 17), s_mul(s_monomial(A=7), coefficient))


def expected_h15():
    return s_add(
        s_scale(QF(-9, 256), s_monomial(A=2, Q=1, F13=1)),
        s_scale(QF(45, 2**15), s_monomial(A=1, Q=2, F11=1)),
        s_scale(QF(-15, 2**21), s_monomial(Q=3, F9=1)),
        s_scale(QF(9, 2**16), s_monomial(e=1, F9=1)),
        s_scale(QF(9, 32), s_monomial(f=1, F8=1)),
        s_scale(QF(-9, 2**22), s_monomial(Q=1, f=1, e=1)),
        s_scale(QF(-45, 2**29), s_monomial(Q=4, f=1)),
        s_scale(QF(9, 2**13), s_monomial(A=1, r=1, F10=1)),
        s_scale(QF(-9, 2**19), s_monomial(Q=1, r=1, F8=1)),
        s_scale(QF(-27, 2**37), s_monomial(Q=2, r=1, e=1)),
        s_scale(QF(-63, 2**43), s_monomial(Q=5, r=1)),
        s_scale(QF(3, 2**33), s_monomial(A=1, r=3)),
    )


# Ordinary exact polynomial arithmetic for the r=0 combined rank.
def trim(poly):
    out = list(poly)
    while out and not out[-1]:
        out.pop()
    return out


def add(*polys):
    size = max((len(poly) for poly in polys), default=0)
    out = [QF(0)] * size
    for poly in polys:
        for index, value in enumerate(poly):
            out[index] += value
    return trim(out)


def scale(value, poly):
    return trim([QF(value) * coefficient for coefficient in poly])


def mul(left, right):
    if not left or not right:
        return []
    out = [QF(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def power(poly, exponent):
    out = [QF(1)]
    for _ in range(exponent):
        out = mul(out, poly)
    return out


def derivative(poly):
    return trim([QF(index) * poly[index] for index in range(1, len(poly))])


def monomial(degree):
    return [QF(0)] * degree + [QF(1)]


def t5(A, d):
    return scale(QF(1, 2), add(
        scale(5, mul(derivative(A), d)),
        scale(2, mul(A, derivative(d))),
    ))


def h7_to_h15(A, q, e, f8, f, f9, f11, f13):
    q2 = mul(q, q)
    q3 = mul(q2, q)
    q4 = mul(q2, q2)
    h7 = scale(QF(1, 4), f)
    h9 = add(scale(QF(1, 4), f9), scale(QF(-3, 256), mul(q, f)))
    h11 = add(
        scale(QF(1, 4), mul(A, f11)),
        scale(QF(-5, 256), mul(q, f9)),
        scale(QF(5, 2**15), mul(q2, f)),
    )
    h13 = add(
        scale(QF(1, 4), mul(power(A, 2), f13)),
        scale(QF(-7, 256), mul(mul(A, q), f11)),
        scale(QF(21, 2**15), mul(q2, f9)),
        scale(QF(7, 2**21), mul(f, add(q3, scale(32, e)))),
    )
    h15 = add(
        scale(QF(-9, 256), mul(mul(power(A, 2), q), f13)),
        scale(QF(45, 2**15), mul(mul(A, q2), f11)),
        scale(QF(-15, 2**21), mul(q3, f9)),
        scale(QF(9, 2**16), mul(e, f9)),
        scale(QF(9, 32), mul(f, f8)),
        scale(QF(-9, 2**22), mul(mul(q, f), e)),
        scale(QF(-45, 2**29), mul(q4, f)),
    )
    return h7, h9, h11, h13, h15


RAW_WINDOWS = {
    "f": tuple(range(0, 6)),
    "f9": tuple(range(1, 8)),
    "f11": tuple(range(1, 6)),
    "f13": tuple(range(2, 4)),
}
BLOCK_SIZES = (6, 8, 10, 12, 14)
PRIMITIVE_MAXIMA = (2, 4, 6, 8, 10)


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


def combined_rank(A, q, e, f8):
    columns = []
    names = tuple(RAW_WINDOWS)
    for name, degrees in RAW_WINDOWS.items():
        for degree in degrees:
            values = {key: [] for key in names}
            values[name] = monomial(degree)
            columns.append(concatenate(h7_to_h15(A, q, e, f8, **values)))
    for block, maximum in enumerate(PRIMITIVE_MAXIMA):
        for degree in range(maximum + 1):
            blocks = [[] for _ in range(5)]
            blocks[block] = scale(-1, t5(A, monomial(degree)))
            columns.append(concatenate(blocks))
    rows = [[column[index] for column in columns]
            for index in range(sum(BLOCK_SIZES))]
    return matrix_rank(rows), len(columns), len(rows)


def main():
    assert sha256(TAIL_REPORT) == TAIL_REPORT_SHA256
    assert sha256(TAIL_CHECKER) == TAIL_CHECKER_SHA256

    # Finite-support licensing.  D35 can be nonzero; D36 and D37 have no
    # raw (F_i,G_j) pair at all.
    f_weights = tuple(range(0, 15))
    g_weights = tuple(range(0, 22))
    weights = {i + j for i in f_weights for j in g_weights}
    assert max(weights) == 35 and 35 in weights
    assert 36 not in weights and 37 not in weights
    assert 15 + 22 == 37 < 38

    derived = derive_h15()
    expected = expected_h15()
    assert derived == expected
    without_cubic = dict(expected)
    cubic_key = next(key for key in expected
                     if key[NAMES.index("r")] == 3)
    del without_cubic[cubic_key]
    assert derived != without_cubic

    assert sum(len(window) for window in RAW_WINDOWS.values()) == 20
    assert sum(maximum + 1 for maximum in PRIMITIVE_MAXIMA) == 35
    assert sum(BLOCK_SIZES) == 50

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
        assert combined_rank(*fixture) == (50, 55, 50)

    # T5 has leading multiplier (2k+20)/2 on degree k, hence zero kernel.
    assert all(QF(2 * degree + 20, 2) for degree in range(11))

    print("finite_support=max_F14_plus_G21=D35;D36_D37_identically_zero")
    print("q15_license=37<38")
    print("q15_symbolic_F17over8=PASS;cubic_F5^3_load=REQUIRED")
    print("r0_raw_variables=20;primitive_variables=35;equations=50")
    print("universal_r0_raw_survivor_dimension_at_least=5")
    print("two_fixture_rank=50;two_fixture_r0_raw_survivor_dimension=5")
    print("PASS_EXACT_LAMBDA0_Q15")


if __name__ == "__main__":
    main()
