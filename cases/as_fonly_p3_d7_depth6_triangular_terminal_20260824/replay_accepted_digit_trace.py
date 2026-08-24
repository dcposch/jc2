#!/usr/bin/env python3
"""Exact accepted-digit trace for the triangular survivor, without SMT."""
from __future__ import annotations


def add(left, right):
    size = max(len(left), len(right))
    return [(left[i] if i < len(left) else 0) +
            (right[i] if i < len(right) else 0) for i in range(size)]


def scale(scalar, polynomial):
    return [scalar*coefficient for coefficient in polynomial]


def multiply(left, right):
    out = [0]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i+j] += a*b
    return out


def pad(polynomial, size=31):
    return polynomial+[0]*(size-len(polynomial))


def H(a):
    a2 = multiply(a, a)
    a3 = multiply(a2, a)
    a4 = multiply(a3, a)
    a5 = multiply(a4, a)
    return pad(add(add(a2, scale(-3, a3)),
                   add(scale(9, a4), scale(-27, a5))))


def inverse_1_plus_3a(a):
    answer = [1]
    power = [1]
    for exponent in range(1, 6):
        power = multiply(power, a)
        answer = add(answer, scale((-3)**exponent, power))
    return pad(answer)


partials = [
    [0, 0, 2, 0, 0, 0, 0],
    [0, 0, 2, 0, 6, 0, 0],
    [0, 0, 2, 0, 6, 0, 9],
    [0, 0, 2, 0, 6, 0, 9],
]

for depth, a in enumerate(partials, start=1):
    modulus = 3**depth
    high = H(a)[7:]
    assert all(coefficient % modulus == 0 for coefficient in high)
    print("accepted_H_mod", modulus, "high_nonzero", [])

a = partials[-1]
assert a[2] % 3 == 2
assert a[5] % 3 == 0
inverse = [coefficient % 729 for coefficient in inverse_1_plus_3a(a)]
assert not any(inverse[7:])
assert inverse[:7] == [1, 0, 723, 0, 18, 0, 702]

# P_x=1+3a mod729.  Integrate the three nonconstant terms explicitly.
p_x = [1, 0, 6, 0, 18, 0, 27]
p = [0, 1, 0, 2, 0, 441, 0, 108]
for exponent, coefficient in enumerate(p_x):
    if exponent == 0:
        assert p[1] % 729 == coefficient
    else:
        assert ((exponent+1)*p[exponent+1]-coefficient) % 729 == 0

print("a_mod81", a)
print("inverse_mod729", inverse[:7])
print("P_coefficients_mod729", p)
print("PASS-ACCEPTED-DIGIT-TRACE")

