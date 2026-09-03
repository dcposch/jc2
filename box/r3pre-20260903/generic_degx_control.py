#!/usr/bin/env python3
"""Mechanical deg_x(J)=4 control for the delta_1'=0 R3 ansatz.

In the descended d'=2,e'=3 chart write

    f = f_2(y) x^2 + lower x terms,
    g = g_3(y) x^3 + lower x terms.

Then coeff_x^4 J(f,g) is 2*f_2*g_3' - 3*f_2'*g_3.  The specialization
f_2=y^(2s)+1, g_3=-y^(3s) proves this coefficient is generically nonzero.
"""

import sympy as sp

y = sp.Symbol("y")
ROWS = ((21, 14, 15, 6, 4), (24, 16, 18, 7, 4), (27, 18, 21, 8, 4))

for n, m, m2, s, k in ROWS:
    f2 = y ** (2 * s) + 1
    g3 = -(y ** (3 * s))
    x4 = sp.expand(2 * f2 * sp.diff(g3, y) - 3 * sp.diff(f2, y) * g3)
    print(f"ROW {n}_{m}_{m2}_{s}_k{k} coeff_x4_specialization={x4}")
    if x4 == 0:
        raise SystemExit("deg_x control failed")
print("GENERIC_DEGX_J_EQ_4_PASS")
