#!/usr/bin/env python3
"""Norm convention: Res_y(H_t, A d + B) = 12 q^2 N(Ad+B), N=B^2-A^2(t+1)/3.

Checked as a polynomial identity in (t,A,B) after substituting d=2qy-(t+1).
"""
from __future__ import annotations

import sympy as sp

t, y, A, B = sp.symbols("t y A B")
q = 2 * t + 1
H = 12 * q**2 * y**2 - 12 * q * (t + 1) * y + (t + 1) * (3 * t + 2)
d = 2 * q * y - (t + 1)
u = A * d + B
N = B**2 - A**2 * (t + 1) / 3
Res = sp.resultant(sp.Poly(H, y), sp.Poly(sp.expand(u), y))
lhs = sp.factor(sp.expand(Res))
rhs = sp.factor(sp.expand(12 * q**2 * N))
print("Res_y(H, Ad+B) =", lhs)
print("12 q^2 N       =", rhs)
print("IDENTITY", sp.expand(Res - 12 * q**2 * N) == 0)

# five claimed scalar formulas (Opus (2.2)) specialised vs charged fixed_r1.json
# is a separate driver (spec_fixed.py)
