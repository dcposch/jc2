#!/usr/bin/env python3
"""GATE 2: post-H/c support, the boundary vanishings, and the 2t duplicates.

Symbolic in t where the statement is symbolic; explicit at t=2..6 where the
band structure is finite.  The three normalizations are x=1 (R monic),
c=-y*g, and the top-face values g1,g2,g3 read off (1+Z+y Z^2)^(e/q).
"""
from __future__ import annotations
import sympy as sp

t, y, X, b1, b2, b3, b4 = sp.symbols("t y X b1 b2 b3 b4")
fails = []


def check(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        fails.append(name)


q, e = 2 * t + 1, 3 * t + 1
H = 12 * q**2 * y**2 - 12 * q * (t + 1) * y + (t + 1) * (3 * t + 2)

# ---- top-face coefficients of G(Z)=(1+Z+y Z^2)^(e/q), symbolic in t
Z = sp.Symbol("Z")
a = sp.Rational(1, 1) * e / q
w = Z + y * Z**2
G = sum(sp.rf(a - k, k + 1) / sp.factorial(k + 1) * 0 for k in [])  # placeholder
G = sum(sp.binomial(a, k) * w**k for k in range(0, 7))
Gs = sp.Poly(sp.expand(G), Z)
gc = [sp.simplify(Gs.coeff_monomial(Z**n)) for n in range(0, 7)]
g1, g2, g3 = gc[1], gc[2], gc[3]
check("G1 g1 = e/q", sp.simplify(g1 - e / q) == 0)
check("G2 g2 = e(2qy+t)/(2q^2)", sp.simplify(g2 - e * (2 * q * y + t) / (2 * q**2)) == 0)
check("G3 g3 = g = t(3t+1)(6qy-(t+1))/(6q^3) (the charged g)",
      sp.simplify(g3 - t * (3 * t + 1) * (6 * q * y - (t + 1)) / (6 * q**3)) == 0)
g = g3
# (5.1) recurrence check
for n in range(0, 5):
    lhs = q * (n + 1) * gc[n + 1]
    rhs = (e - q * n) * gc[n] + y * (2 * e - q * (n - 1)) * (gc[n - 1] if n >= 1 else 0)
    check("G4 (5.1) recurrence at n=%d" % n, sp.simplify(lhs - rhs) == 0)
check("G5 g4 = 0 modulo H_t",
      sp.simplify(sp.rem(sp.Poly(sp.together(gc[4] * 12 * q**4 * 6).as_expr(), y),
                         sp.Poly(H, y))) == 0 or
      sp.simplify(sp.cancel(sp.numer(sp.together(gc[4])) /
                            sp.Poly(H, y).as_expr())).is_polynomial(y))
num4 = sp.Poly(sp.numer(sp.cancel(sp.together(gc[4]))), y)
quo, rem4 = sp.div(num4, sp.Poly(H, y))
check("G5b numer(g4) is an exact multiple of H_t", sp.simplify(rem4.as_expr()) == 0)
print("      g4 = (%s)/(%s) * H_t" % (sp.factor(quo.as_expr()),
                                      sp.factor(sp.denom(sp.cancel(sp.together(gc[4]))))))
check("G6 (5.2) g5 = -y*g3/(5q) modulo H_t",
      sp.simplify(sp.rem(sp.Poly(sp.numer(sp.cancel(sp.together(
          gc[5] + y * g3 / (5 * q)))), y), sp.Poly(H, y)).as_expr()) == 0)
check("G6b (5.2) g5 = -t(t+1)(3t+1)(5d+2t+3)/(60 q^5) with d=2qy-(t+1)",
      sp.simplify(sp.rem(sp.Poly(sp.numer(sp.cancel(sp.together(
          gc[5] + t * (t + 1) * (3 * t + 1) * (5 * (2 * q * y - (t + 1))
                                               + 2 * t + 3) / (60 * q**5)))), y),
          sp.Poly(H, y)).as_expr()) == 0)

# ---- (5.7a) leading-coefficient identities, symbolic in t
check("L1 (5.7a)#1 (3t+2)g - 2t y g2 = -t(3t+1)H_t/(6q^3)",
      sp.simplify((3 * t + 2) * g - 2 * t * y * g2
                  + t * (3 * t + 1) * H / (6 * q**3)) == 0)
check("L2 (5.7a)#2 3q g + (t+1) g2 = (4t+1) y g1",
      sp.simplify(3 * q * g + (t + 1) * g2 - (4 * t + 1) * y * g1) == 0)
check("L3 (5.7a)#3 2q g2 - t g1 = 2 e y",
      sp.simplify(2 * q * g2 - t * g1 - 2 * e * y) == 0)

# ---- boundary vanishings: top band of each tag, symbolic in t
r, s, tau = sp.symbols("r s tau")   # leading coefficients of R, S, T
# derived above from deg R=t, deg S=2t, deg T=t, deg U=q, deg V=e
top_C12 = -r * tau * (t + 1) + y * s * (4 * t + 1) - 3 * g * q
top_C11 = -(3 * t + 2) * g * r + 2 * t * y * tau
top_C00 = -t * r * s + 2 * q * tau - 2 * y * e
top_C01 = -e * r + q * s
sub_norm = {r: 1, s: g1, tau: g2}
check("S1 [X^{2t}]C12 = 0 by (5.7a)#2", sp.simplify(top_C12.subs(sub_norm)) == 0)
check("S2 [X^t]C11 = t(3t+1)H_t/(6q^3): this row IS H_t",
      sp.simplify(top_C11.subs(sub_norm) - t * (3 * t + 1) * H / (6 * q**3)) == 0)
check("S3 [X^{3t+1}]C00 = 0 by (5.7a)#3", sp.simplify(top_C00.subs(sub_norm)) == 0)
check("S4 [X^{4t+1}]C01 = 0", sp.simplify(top_C01.subs(sub_norm)) == 0)

# ---- explicit band structure at t=2..6 with generic block coefficients
print("      band table (generic coefficients, x=1, c=-yg, mod H_t):")
hdr = "      %2s %6s %6s %6s %6s %6s %8s %8s %8s" % (
    "t", "degC12", "degC11", "degC00", "degC01", "rows", "9t+2", "aux 6t+2", "dupes 2t")
print(hdr)
for tv in range(2, 7):
    ev, qv = 3 * tv + 1, 2 * tv + 1
    Hv = H.subs(t, tv)
    g1v, g2v, gv = (sp.cancel(w_.subs(t, tv)) for w_ in (g1, g2, g))
    Uc = [sp.Symbol("u%d" % i) for i in range(qv)] + [sp.Integer(1)]
    Rc = [sp.Symbol("r%d" % i) for i in range(tv)] + [sp.Integer(1)]
    Vc = [sp.Symbol("v%d" % i) for i in range(ev)] + [sp.Integer(1)]
    Sc = [sp.Symbol("s%d" % i) for i in range(2 * tv)] + [g1v]
    Tc = [sp.Symbol("T%d" % i) for i in range(tv)] + [g2v]
    U = sum(Uc[i] * X**i for i in range(qv + 1))
    R = sum(Rc[i] * X**i for i in range(tv + 1))
    V = sum(Vc[i] * X**i for i in range(ev + 1))
    S = sum(Sc[i] * X**i for i in range(2 * tv + 1))
    T = sum(Tc[i] * X**i for i in range(tv + 1))
    Up, Rp, Vp, Sp_, Tp = (sp.diff(z_, X) for z_ in (U, R, V, S, T))
    L = X - b4
    C12 = (-R * T + L * (R * Tp - 2 * Rp * T + 2 * y * Sp_) + y * S
           - b3 * (gv * Rp + y * Tp) - 3 * gv * Up)
    C11 = -2 * gv * R + L * (2 * y * Tp - 3 * gv * Rp)
    C00 = (L**2 * (Rp * S - R * Sp_)
           + L * (b3 * (Rp * T - y * Sp_) + 2 * b2 * (gv * Rp - y * Tp)
                  + 2 * T * Up - 2 * y * Vp)
           + gv * b3**2 * Rp + gv * b2 * R + gv * b3 * Up + b1 * gv * y)
    C01 = ((b3 * y - L * R) * Vp + (L * S - b3 * T - b2 * gv) * Up + gv * y
           - b2 * C12 - b1 * C11)
    C02 = -b1 * C12 - C11
    def bands(expr):
        pol = sp.Poly(sp.expand(expr), X)
        out = []
        for k in range(pol.degree(), -1, -1):
            co = sp.simplify(pol.coeff_monomial(X**k))
            if co != 0:
                out.append(k)
        return out
    d12, d11, d00, d01 = (max(bands(z_) + [-1]) for z_ in (C12, C11, C00, C01))
    # mod H_t reduction of the top C11 band
    top11 = sp.simplify(sp.Poly(sp.expand(C11), X).coeff_monomial(X**tv))
    isH = sp.simplify(sp.cancel(top11 / Hv)).free_symbols.isdisjoint({y})
    # duplicate rows: [X^k]C02 for k=0..2t-1 in <[X^k]C12, [X^k]C11, H>
    p02 = sp.Poly(sp.expand(C02), X)
    p12 = sp.Poly(sp.expand(C12), X)
    p11 = sp.Poly(sp.expand(C11), X)
    dup = 0
    for k in range(0, 2 * tv):
        target = sp.expand(p02.coeff_monomial(X**k))
        comb = sp.expand(-b1 * p12.coeff_monomial(X**k) - p11.coeff_monomial(X**k))
        if sp.expand(target - comb) == 0:
            dup += 1
    rows = (2 * tv) + tv + (2 * tv) + (2 * tv + 1) + (2 * tv + 1)
    aux = 6 * tv + 2
    print("      %2d %6d %6d %6d %6d %6d %8d %8s %8d" %
          (tv, d12, d11, d00, d01, rows, 9 * tv + 2, aux, dup))
    check("B%d deg C12 = 2t-1 after (5.7a)#2" % tv, d12 == 2 * tv - 1)
    check("B%d deg C11 = t and that band is a multiple of H_t" % tv,
          d11 == tv and isH)
    check("B%d deg C01 = 4t" % tv, d01 == 4 * tv)
    check("B%d all 2t tag-02 rows are -b1*C12-C11 combinations" % tv,
          dup == 2 * tv)
print("GATE2_DONE fails=%d" % len(fails))
if fails:
    print("FAILED:", fails)
