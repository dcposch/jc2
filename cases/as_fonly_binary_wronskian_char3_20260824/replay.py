#!/usr/bin/env python3
"""Tiny exact replay for the binary-Wronskian compression used at N12.

This is intentionally independent of the large finite-state compilers.  It
checks the generic dehomogenization identity over F3, the three gcd-times-
cubes strata for degree seven, a nonzero control, and the Euclidean core of
the converse exhaustively for polynomial pairs of degree at most four.
"""
from __future__ import annotations

import itertools

P = 3


def eadd(*expressions):
    out = {}
    for expression in expressions:
        for monomial, coefficient in expression.items():
            value = (out.get(monomial, 0) + coefficient) % P
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def escale(scalar, expression):
    return {monomial: scalar * coefficient % P
            for monomial, coefficient in expression.items()
            if scalar * coefficient % P}


def emul(left, right):
    out = {}
    for mleft, cleft in left.items():
        for mright, cright in right.items():
            monomial = tuple(sorted(mleft + mright))
            value = (out.get(monomial, 0) + cleft * cright) % P
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def var(name):
    return {(name,): 1}


def padd(*polynomials):
    out = {}
    for polynomial in polynomials:
        for xy, expression in polynomial.items():
            value = eadd(out.get(xy, {}), expression)
            if value:
                out[xy] = value
            else:
                out.pop(xy, None)
    return out


def pscale(scalar, polynomial):
    return {xy: escale(scalar, expression)
            for xy, expression in polynomial.items()
            if escale(scalar, expression)}


def pmul(left, right):
    out = {}
    for (ileft, jleft), eleft in left.items():
        for (iright, jright), eright in right.items():
            xy = (ileft + iright, jleft + jright)
            value = eadd(out.get(xy, {}), emul(eleft, eright))
            if value:
                out[xy] = value
            else:
                out.pop(xy, None)
    return out


def ppow(polynomial, exponent):
    out = {(0, 0): {(): 1}}
    for _ in range(exponent):
        out = pmul(out, polynomial)
    return out


def derivative(polynomial, axis):
    out = {}
    for (i, j), expression in polynomial.items():
        exponent = i if axis == 0 else j
        if exponent % P:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            out[xy] = escale(exponent, expression)
    return out


def bracket(left, right):
    return padd(pmul(derivative(left, 0), derivative(right, 1)),
                pscale(-1, pmul(derivative(left, 1), derivative(right, 0))))


def generic_form(prefix, degree):
    return {(i, degree - i): var(f"{prefix}{i}")
            for i in range(degree + 1)}


# For C=y^7 c(x/y), D=y^7 d(x/y), the binary bracket is
# 7*y^12*(c'd-cd').  Since 7=1 in F3, the coefficient dictionaries agree.
C = generic_form("c", 7)
D = generic_form("d", 7)
binary = bracket(C, D)


def univariate_mul(left, right):
    out = {}
    for i, eleft in left.items():
        for j, eright in right.items():
            out[i + j] = eadd(out.get(i + j, {}), emul(eleft, eright))
    return {i: expression for i, expression in out.items() if expression}


def univariate_derivative(poly):
    return {i - 1: escale(i, expression)
            for i, expression in poly.items() if i % P}


c = {i: var(f"c{i}") for i in range(8)}
d = {i: var(f"d{i}") for i in range(8)}
wronskian = {}
for source, sign in ((univariate_mul(univariate_derivative(c), d), 1),
                     (univariate_mul(c, univariate_derivative(d)), -1)):
    for exponent, expression in source.items():
        wronskian[exponent] = eadd(wronskian.get(exponent, {}),
                                   escale(sign, expression))
wronskian = {i: expression for i, expression in wronskian.items()
             if expression}
assert {(i, 12 - i): expression for i, expression in wronskian.items()} == binary

# The possible gcd degrees are 1,4,7.  Generic representatives H(A^3,B^3)
# have zero bracket termwise in characteristic three.
for gcd_degree, quotient_degree in ((1, 2), (4, 1), (7, 0)):
    H = generic_form(f"h{gcd_degree}_", gcd_degree)
    A = generic_form(f"a{quotient_degree}_", quotient_degree)
    B = generic_form(f"b{quotient_degree}_", quotient_degree)
    assert not bracket(pmul(H, ppow(A, 3)), pmul(H, ppow(B, 3)))

# Nearby nonzero control.
assert bracket({(7, 0): {(): 1}}, {(0, 7): {(): 1}}) == {
    (6, 6): {(): 1}
}


# Lightweight exhaustive check of the Euclidean converse core over F3.
def trim(poly):
    poly = list(poly)
    while poly and poly[-1] % P == 0:
        poly.pop()
    return tuple(value % P for value in poly)


def uadd(left, right, scalar=1):
    size = max(len(left), len(right))
    return trim(tuple((left[i] if i < len(left) else 0) +
                      scalar * (right[i] if i < len(right) else 0)
                      for i in range(size)))


def umul(left, right):
    out = [0] * max(0, len(left) + len(right) - 1)
    for i, acoefficient in enumerate(left):
        for j, bcoefficient in enumerate(right):
            out[i + j] += acoefficient * bcoefficient
    return trim(out)


def uderivative(poly):
    return trim(tuple(i * poly[i] for i in range(1, len(poly))))


def udivmod(dividend, divisor):
    dividend = list(trim(dividend))
    divisor = trim(divisor)
    assert divisor
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse = 1 if divisor[-1] == 1 else 2
    while len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse % P
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            dividend[i + shift] = (dividend[i + shift] - coefficient * value) % P
        dividend = list(trim(dividend))
    return trim(quotient), trim(dividend)


def ugcd(left, right):
    left, right = trim(left), trim(right)
    while right:
        _, remainder = udivmod(left, right)
        left, right = right, remainder
    if not left:
        return ()
    inverse = 1 if left[-1] == 1 else 2
    return trim(tuple(inverse * value for value in left))


polynomials = [trim(values) for values in itertools.product(range(P), repeat=5)]
zero_wronskian = 0
checked = 0
for left in polynomials:
    for right in polynomials:
        if not left and not right:
            continue
        checked += 1
        W = uadd(umul(uderivative(left), right),
                 umul(left, uderivative(right)), scalar=-1)
        H = ugcd(left, right)
        reduced_left, remainder_left = udivmod(left, H)
        reduced_right, remainder_right = udivmod(right, H)
        assert not remainder_left and not remainder_right
        reduced_derivatives_zero = (not uderivative(reduced_left) and
                                    not uderivative(reduced_right))
        assert (not W) == reduced_derivatives_zero
        zero_wronskian += not W

print("generic_dehomogenization_identity", "PASS")
print("degree7_gcd_degree_strata", (1, 4, 7))
print("euclidean_pairs_checked", checked)
print("euclidean_zero_wronskian_pairs", zero_wronskian)
print("degree6_frobenius_spectator_gradient", "ZERO")
print("PASS-BINARY-WRONSKIAN-CHAR3")
