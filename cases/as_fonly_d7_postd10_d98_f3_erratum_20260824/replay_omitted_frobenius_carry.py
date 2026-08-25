#!/usr/bin/env python3
"""Exact integer witnesses for the omitted divided Frobenius cross-carry."""
from __future__ import annotations

from collections import defaultdict


def add(*polys):
    out = defaultdict(int)
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] += coefficient
    return {m: c for m, c in out.items() if c}


def scale(scalar, poly):
    return {m: scalar*c for m, c in poly.items() if scalar*c}


def mul(left, right):
    out = defaultdict(int)
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            out[(i+k, j+ell)] += a*b
    return {m: c for m, c in out.items() if c}


def derivative(poly, axis):
    out = {}
    for (i, j), coefficient in poly.items():
        exponent = (i, j)[axis]
        if exponent:
            key = (i-1, j) if axis == 0 else (i, j-1)
            out[key] = coefficient*exponent
    return out


def bracket(left, right):
    return add(mul(derivative(left, 0), derivative(right, 1)),
               scale(-1, mul(derivative(left, 1), derivative(right, 0))))


def divided_mod3(poly, divisor):
    assert all(c % divisor == 0 for c in poly.values())
    return {m: (c//divisor) % 3 for m, c in poly.items()
            if (c//divisor) % 3}


# Frozen vertical fibre-count-one representative:
# (P,Q,R,T,s,w,h)=(0,0,0,1,0,0,0), f_b=u6_6=1.
# The triangular inverse gives t=1 and all other degree-four parameters zero.
U0 = {(4, 0): 2}
V0 = {(2, 1): 1, (3, 1): 1}
UF = {(6, 0): 1}
VF = {}
K0 = bracket(add({(3, 0): -1}, U0), V0)
Kfull = bracket(add({(3, 0): -1}, U0, UF), add(V0, VF))
vertical = divided_mod3(add(Kfull, scale(-1, K0)), 3)
assert vertical == {(7, 0): 2, (8, 0): 2}, vertical
assert vertical[(8, 0)] == 2

# On g!=0, the omitted pure Frobenius u6_0=y^6 couples to V5=g*x^5.
# At g=1 this already creates a degree-nine row.
U0g = {}
V0g = {(2, 1): 1, (5, 0): 1}
UFg = {(0, 6): 1}
K0g = bracket({(3, 0): -1}, V0g)
Kfullg = bracket(add({(3, 0): -1}, UFg), V0g)
gendpoint = divided_mod3(add(Kfullg, scale(-1, K0g)), 3)
assert gendpoint == {(1, 6): 2, (4, 5): 2}, gendpoint
assert gendpoint[(4, 5)] == 2

# Two Frobenius derivatives each carry a factor 3, so their product divided
# by 3 is still zero mod 3.  The missing term is exactly the single-cross
# class, not a double-Frobenius term.
double = divided_mod3(bracket({(6, 0): 1}, {(0, 6): 1}), 3)
assert double == {}, double

print("vertical_[Kfrob/3]_mod3", sorted(vertical.items()))
print("g_endpoint_[Kfrob/3]_mod3", sorted(gendpoint.items()))
print("double_frobenius_after_division_mod3", sorted(double.items()))
print("PASS-OMITTED-FROBENIUS-CROSS-CARRY-WITNESSES")
