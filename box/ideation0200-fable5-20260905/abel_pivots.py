#!/usr/bin/env python3
"""Desk check (Fable): top-down pivots of Astra's (F3) Abel equation in the Z = xW - r form.
x (Z^2)' - 3 Z^2 = (B - 2A + D) x Z + R(x); Z = sum Z_k x^k, Z_{2t+2} = omega, A = alpha x^3 C^2 (alpha = 3/(4y^2)).
Coefficient of Z_{2t+2-j} in the x^{4t+4-j} equation: pivot_j = 2 omega (4t+1-j) + 2 alpha.
With omega = alpha (2d-1)/(4t+1) [Astra (F1)] and 4t+1 = 3(2d-1)(2d+1) [3d^2 = t+1]:
pivot_j = 0  <=>  j = 6 d (2d+1).  For d>0 this exceeds 2t+2; for d = -delta it is 4t+4-6 delta,
inside [0, 2t+2] iff delta = 1 iff t = 2 (then j = 2t+2 = 6: the Z_0 = -r closing pivot).
Also: y = (d+t+1)/(2q) (Astra section 1) gives y = 1/5 at (t,d) = (2,-1), the banked failure fibre.
"""
import sympy as sp
t, d, j, alpha = sp.symbols('t d j alpha')
omega = alpha*(2*d-1)/(4*t+1)
pivot = 2*omega*(4*t+1-j) + 2*alpha
sol = sp.solve(sp.Eq(pivot, 0), j)[0]
print("j_res (general) =", sp.simplify(sol))
jres = sp.simplify(sol.subs(t, 3*d**2 - 1))
print("j_res with t = 3d^2-1 =", sp.factor(jres))
for (tt, dd) in [(2, 1), (2, -1), (3, sp.Rational(2, 3)*sp.sqrt(3)), (3, -sp.Rational(2, 3)*sp.sqrt(3)), (11, 2), (11, -2), (26, 3), (26, -3)]:
    q = 2*tt + 1
    y = sp.nsimplify((dd + tt + 1)/(2*q))
    jr = sp.simplify(sol.subs({t: tt, d: dd}))
    print(f"t={tt:2d} d={sp.nsimplify(dd)!s:12s} y={y!s:22s} j_res={sp.nsimplify(jr)!s:14s} 2t+2={2*tt+2:3d} resonant_in_range={bool(sp.simplify(jr).is_integer and 0 <= jr <= 2*tt+2)}")
# leading balance check: (4t+1) omega^2 + 2 alpha omega - alpha^2/3 = 0 with 3d^2 = t+1
lb = sp.simplify(((4*t+1)*omega**2 + 2*alpha*omega - alpha**2/3).subs(t, 3*d**2-1))
print("leading balance residual with t=3d^2-1:", sp.factor(lb))
