#!/usr/bin/env python3
"""Exact integer source audit for the next top-carry Frobenius terms.

All differentiation and division occur over Z.  Reduction modulo three is
performed only after formal divisibility by 3 or 9 has been asserted.
"""
from __future__ import annotations

import hashlib
import json


def eadd(*expressions):
    out = {}
    for expression in expressions:
        for monomial, coefficient in expression.items():
            value = out.get(monomial, 0) + coefficient
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def escale(scalar, expression):
    return {monomial: scalar * coefficient
            for monomial, coefficient in expression.items()
            if scalar * coefficient}


def emul(left, right):
    out = {}
    for mleft, cleft in left.items():
        for mright, cright in right.items():
            monomial = tuple(sorted(mleft + mright))
            out[monomial] = out.get(monomial, 0) + cleft * cright
    return {monomial: coefficient for monomial, coefficient in out.items()
            if coefficient}


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


def derivative(polynomial, axis):
    out = {}
    for (i, j), expression in polynomial.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            out[xy] = escale(exponent, expression)
    return out


def bracket(left, right):
    return padd(pmul(derivative(left, 0), derivative(right, 1)),
                pscale(-1, pmul(derivative(left, 1), derivative(right, 0))))


def homogeneous(prefix, degree):
    return {(i, degree - i): var(f"{prefix}_{i}")
            for i in range(degree + 1)}


def degree_part(polynomial, total):
    return {xy: expression for xy, expression in polynomial.items()
            if sum(xy) == total and expression}


def divide_mod3(polynomial, divisor):
    assert all(coefficient % divisor == 0
               for expression in polynomial.values()
               for coefficient in expression.values())
    return {
        xy: {monomial: (coefficient // divisor) % 3
             for monomial, coefficient in expression.items()
             if (coefficient // divisor) % 3}
        for xy, expression in polynomial.items()
        if any((coefficient // divisor) % 3
               for coefficient in expression.values())
    }


def mod3(polynomial):
    return {
        xy: {monomial: coefficient % 3
             for monomial, coefficient in expression.items()
             if coefficient % 3}
        for xy, expression in polynomial.items()
        if any(coefficient % 3 for coefficient in expression.values())
    }


def canonical_hash(polynomial):
    payload = [
        [[i, j], [[list(monomial), coefficient]
                  for monomial, coefficient in sorted(expression.items())]]
        for (i, j), expression in sorted(polynomial.items())
    ]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode()
    ).hexdigest()


def evaluate(polynomial, assignment):
    out = {}
    for xy, expression in polynomial.items():
        value = 0
        for monomial, coefficient in expression.items():
            term = coefficient
            for name in monomial:
                term *= assignment.get(name, 0)
            value += term
        if value % 3:
            out[xy] = value % 3
    return out


UF = {
    (0, 6): var("fua"), (3, 3): var("fa"), (6, 0): var("fb"),
}
VF = {
    (0, 6): var("fc"), (3, 3): var("fd"), (6, 0): var("fvb"),
}
C7, D7 = homogeneous("c7", 7), homogeneous("d7", 7)
C6, D6 = homogeneous("c6", 6), homogeneous("d6", 6)
C5, D5 = homogeneous("c5", 5), homogeneous("d5", 5)

# The part of M containing exactly one degree-six Frobenius first digit.
MF7 = padd(bracket(UF, D7), bracket(C7, VF))
MF6 = padd(bracket(UF, D6), bracket(C6, VF))
assert MF7 == degree_part(MF7, 11)
assert MF6 == degree_part(MF6, 10)
MF7q = divide_mod3(MF7, 3)
MF6q = divide_mod3(MF6, 3)

# The double-Frobenius part of K enters E1 divided by 3, then the following
# quotient divides once more: its correct coefficient is Kdouble/9.
Kdouble = bracket(UF, VF)
assert Kdouble == degree_part(Kdouble, 10)
Kdoubleq = divide_mod3(Kdouble, 9)

N11old = mod3(padd(bracket(C7, D6), bracket(C6, D7)))
N10old = mod3(padd(bracket(C7, D5), bracket(C6, D6), bracket(C5, D7)))
Q11 = mod3(padd(N11old, MF7q))
Q10 = mod3(padd(N10old, MF6q, Kdoubleq))
assert Q11 != N11old
assert Q10 != N10old

expected_kdouble = {
    (2, 8): eadd(escale(2, emul(var("fa"), var("fc"))),
                    escale(1, emul(var("fua"), var("fd")))),
    (5, 5): eadd(emul(var("fb"), var("fc")),
                    escale(2, emul(var("fua"), var("fvb")))),
    (8, 2): eadd(escale(2, emul(var("fb"), var("fd"))),
                    emul(var("fa"), var("fvb"))),
}
assert Kdoubleq == expected_kdouble

# Two minimal negative controls.  They need not lie on the predecessor gate;
# they prove that the omitted universal source summands are nonzero.
witness11 = evaluate(MF7q, {"fb": 1, "d7_0": 1})  # UF=x^6,D7=y^7
witness10 = evaluate(Kdoubleq, {"fb": 1, "fc": 1})  # UF=x^6,VF=y^6
assert witness11 == {(5, 6): 2}
assert witness10 == {(5, 5): 1}

print("MF7_div3_shape", len(MF7q))
print("MF6_div3_shape", len(MF6q))
print("Kdouble_div9", expected_kdouble)
print("corrected_Q11_sha256", canonical_hash(Q11))
print("corrected_Q10_sha256", canonical_hash(Q10))
print("negative_witness_degree11", witness11)
print("negative_witness_degree10", witness10)
print("PASS-NEXT-TOP-CARRY-FROBENIUS-ERRATUM-SOURCE")
