#!/usr/bin/env python3
"""Symbolic weight-balance audit for the Sol Section 2 coefficient recurrence.

This does not expand fixed-t terminal rows.  It verifies the weight identities
that make the indexed recurrence homogeneous for arbitrary t.
"""
import sympy as sp

t, m, a, b, k = sp.symbols("t m a b k", integer=True)
q = 2*t + 1

checks = []

# Coefficients after X=L+b4.
checks.append(("U_m top", q - m, q - m))
checks.append(("U_m summand", sp.symbols("i") + (q - sp.symbols("i") - m), q - m))
checks.append(("C_m top", t - 1 - m, t - 1 - m))
checks.append(("C_m summand", sp.symbols("j") + (t - 1 - sp.symbols("j") - m), t - 1 - m))

# B_{m+1}, S_m.
checks.append(("B_{m+1}", t - 1 - m, t - (m + 1)))
checks.append(("S_m from U_{m+1}", q - (m + 1), 2*t - m))
checks.append(("S_m from C_a B_b", ((t - 1 - a) + (t - b)).subs(b, m - 1 - a), 2*t - m))
checks.append(("S_m from b3 C_m", (t + 1) + (t - 1 - m), 2*t - m))

# V,Y,Z coefficient arrays.
checks.append(("V_m from C_{m-2}", t - 1 - (m - 2), t + 1 - m))
checks.append(("V_0 from b3", t + 1, t + 1))
checks.append(("Y_m from S_{m-1}", 2*t - (m - 1), 2*t + 1 - m))
checks.append(("Y_m from b3 B_m", (t + 1) + (t - m), 2*t + 1 - m))
checks.append(("Y_0 from b2", 2*t + 1, 2*t + 1))
checks.append(("Z_m from B_{m-1}", t - (m - 1), t + 1 - m))
checks.append(("Z_0 from b3", t + 1, t + 1))

# N, P0', R=-E.
checks.append(("N_m from V_a Y'_{b}", ((t + 1 - a) + (2*t + 1 - (b + 1))).subs(b, m - a), 3*t + 1 - m))
checks.append(("N_m from V'_{a} Y_b", ((t + 1 - (a + 1)) + (2*t + 1 - b)).subs(b, m - a), 3*t + 1 - m))
checks.append(("N_m from U'_{a} Z_b", ((q - (a + 1)) + (t + 1 - b)).subs(b, m - a), 3*t + 1 - m))
checks.append(("P0'_r", (3*t + 1 - (m + 1)), 3*t - m))
checks.append(("R_m from V_a P_b", ((t + 1 - a) + (3*t - b)).subs(b, m - a), 4*t + 1 - m))
checks.append(("R_m from U'_{a} Y_b", ((q - (a + 1)) + (2*t + 1 - b)).subs(b, m - a), 4*t + 1 - m))

# Change back from L to X: b4^(m-k) R_m.
checks.append(("T_k from R_m and b4", (4*t + 1 - m) + (m - k), 4*t + 1 - k))

failures = []
for name, lhs, rhs in checks:
    delta = sp.simplify(lhs - rhs)
    print(f"{name}: lhs={sp.simplify(lhs)} rhs={sp.simplify(rhs)} delta={delta}")
    if delta != 0:
        failures.append(name)

print("R_0 also has the scalar -y*g of weight 0; this is the sole inhomogeneous part.")
print("SYMBOLIC_WEIGHT_AUDIT =", "PASS" if not failures else "FAIL")
if failures:
    raise SystemExit(1)
