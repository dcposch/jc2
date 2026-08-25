#!/usr/bin/env python3
"""Exact symbolic replay of the pure-N degree 12/11/10 radial identities."""
from __future__ import annotations

import contextlib
import io
import os
import runpy
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
BASE = (ROOT / "cases/as_fonly_binary_wronskian_char3_20260824"
        / "replay.py")
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(BASE))

padd = ns["padd"]
pmul = ns["pmul"]
pscale = ns["pscale"]
derivative = ns["derivative"]
bracket = ns["bracket"]
generic_form = ns["generic_form"]
eadd = ns["eadd"]
escale = ns["escale"]
emul = ns["emul"]


def total_part(polynomial, total):
    return {xy: expression for xy, expression in polynomial.items()
            if sum(xy) == total and expression}


def dehomogeneous(form):
    return {i: expression for (i, _), expression in form.items()}


def uadd(*terms):
    out = {}
    for scalar, polynomial in terms:
        for exponent, expression in polynomial.items():
            value = eadd(out.get(exponent, {}), escale(scalar, expression))
            if value:
                out[exponent] = value
            else:
                out.pop(exponent, None)
    return out


def umul(left, right):
    out = {}
    for i, eleft in left.items():
        for j, eright in right.items():
            value = eadd(out.get(i + j, {}), emul(eleft, eright))
            if value:
                out[i + j] = value
            else:
                out.pop(i + j, None)
    return out


def uderivative(polynomial):
    return {i - 1: escale(i, expression)
            for i, expression in polynomial.items() if i % 3}


def homogenize_coefficient(polynomial, total):
    return {(i, total - i): expression for i, expression in polynomial.items()
            if expression}


C7 = generic_form("c7_", 7)
C6 = generic_form("c6_", 6)
C5 = generic_form("c5_", 5)
D7 = generic_form("d7_", 7)
D6 = generic_form("d6_", 6)
D5 = generic_form("d5_", 5)
C = padd(C7, C6, C5)
D = padd(D7, D6, D5)
N = bracket(C, D)

c0, c1, c2 = map(dehomogeneous, (C7, C6, C5))
d0, d1, d2 = map(dehomogeneous, (D7, D6, D5))

N12 = uadd((1, umul(uderivative(c0), d0)),
           (-1, umul(c0, uderivative(d0))))
N11 = uadd((1, umul(uderivative(c1), d0)),
           (-1, umul(c0, uderivative(d1))))
cross10 = uadd((1, umul(c2, d0)), (-1, umul(c0, d2)))
N10 = uderivative(cross10)

assert total_part(N, 12) == homogenize_coefficient(N12, 12)
assert total_part(N, 11) == homogenize_coefficient(N11, 11)
assert total_part(N, 10) == homogenize_coefficient(N10, 10)

# Equal-degree forms of degree divisible by three have identically zero
# binary bracket.  This is stronger than spectator-independence.
assert not bracket(C6, D6)

# The explicit free degree-six directions are all Frobenius forms.
frobenius6 = {(0, 6): {(): 1}, (3, 3): {(): 1}, (6, 0): {(): 1}}
assert not derivative(frobenius6, 0)
assert not derivative(frobenius6, 1)

# A nearby degree-five/six pair is not spuriously killed.
control = bracket({(5, 0): {(): 1}}, {(0, 6): {(): 1}})
assert control == {}  # D6 itself is Frobenius.
control = bracket({(5, 0): {(): 1}}, {(1, 5): {(): 1}})
assert control == {(5, 4): {(): 1}}

print("pure_N12_identity", "c0'd0-c0d0'")
print("pure_N11_identity", "c1'd0-c0d1'")
print("pure_N10_identity", "(c2*d0-c0*d2)'")
print("all_degree6_self_brackets", "ZERO")
print("degree6_frobenius_spectator_gradient", "ZERO")
print("PASS-BINARY-TOP3-RADIAL-CHAR3")
