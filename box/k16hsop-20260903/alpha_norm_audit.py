#!/usr/bin/env python3
"""Independent symbolic audit of the b3-axis leading scalar alpha_t and its norm.

Charged closed form (sol56 (6.2) = fable (3.3)):
   alpha_t = t(3t+1)(A_b d + B_b) / (12 q^2 (3t-1)^2 (3t+2)),
   A_b = 27t^3-30t^2+t-2,  B_b = 6t^3+13t^2-3t+2,  q=2t+1,  A_t=Q[d]/(3d^2-(t+1)).
Norm of a linear class a d + b in A_t:   Res_y(H_t, a d + b) = 4 q^2 (3 b^2 - a^2 (t+1)).
Claimed factorisation (sol56 (3.6)):
   3 B_b^2 - A_b^2 (t+1) = -(t-2)(3t-1)^2(3t+2)(27t^3+17t^2+t+2).
This script re-derives that factorisation from scratch and locates every integer root.
"""
import sympy as sp

t, d, y = sp.symbols('t d y')
q = 2 * t + 1
Ab = 27 * t**3 - 30 * t**2 + t - 2
Bb = 6 * t**3 + 13 * t**2 - 3 * t + 2

lhs = sp.expand(3 * Bb**2 - Ab**2 * (t + 1))
claim = sp.expand(-(t - 2) * (3 * t - 1)**2 * (3 * t + 2) * (27 * t**3 + 17 * t**2 + t + 2))
print("3B^2-(t+1)A^2 - claimed =", sp.simplify(lhs - claim))
print("factor(3B^2-(t+1)A^2)   =", sp.factor(lhs))
print()
# integer roots of each factor
print("integer roots of (t-2):            [2]")
print("rational roots of 27t^3+17t^2+t+2: ", sp.solve(sp.Eq(27*t**3+17*t**2+t+2, 0), t, rational=True))
cub = sp.Poly(27*t**3+17*t**2+t+2, t)
print("real roots of 27t^3+17t^2+t+2:     ", [sp.nsimplify(r, rational=False) for r in sp.real_roots(cub)])
print("  numeric:", [sp.N(r, 12) for r in sp.real_roots(cub)])
print("integer roots of (3t-1)^2,(3t+2):  none (t=1/3, t=-2/3)")
print()
# Full norm including the 4q^2 prefactor
norm = sp.factor(4 * q**2 * lhs)
print("Res_y(H_t, A_b d + B_b) =", norm)
print()
print("Sign/vanishing table for integer t:")
for tv in range(1, 13):
    v = norm.subs(t, tv)
    print(f"   t={tv:3d}:  Res = {sp.nsimplify(v)}   ->  alpha_t {'ZERO-DIVISOR/NON-UNIT' if v == 0 else 'UNIT'}")
print()
# Also: alpha_t itself is nonzero as an element only if (A_b,B_b) != (0,0)
print("A_b, B_b common integer roots:", sp.solve([sp.Eq(Ab,0), sp.Eq(Bb,0)], t))
print()
# the t=2 split: which factor of A_2 = Q x Q kills alpha_2 ?
t2 = 2
Ab2, Bb2 = int(Ab.subs(t, t2)), int(Bb.subs(t, t2))
dd = 2 * (2 * t2 + 1) * y - (t2 + 1)                       # d = 2qy-(t+1)
lin = sp.expand(Ab2 * dd + Bb2)
print(f"t=2: A_b={Ab2} B_b={Bb2};  A_b*d+B_b = {sp.factor(lin)}")
alpha2 = sp.simplify(t2*(3*t2+1)*lin / (12*(2*t2+1)**2*(3*t2-1)**2*(3*t2+2)))
print("     alpha_2 =", sp.factor(alpha2), "   (H_2 roots y=1/5, 2/5)")
print("     alpha_2 at y=1/5:", sp.simplify(alpha2.subs(y, sp.Rational(1,5))))
print("     alpha_2 at y=2/5:", sp.simplify(alpha2.subs(y, sp.Rational(2,5))))
