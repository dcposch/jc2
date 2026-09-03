#!/usr/bin/env python3
"""GATE 3: every pivot norm in the section-5.1 Laurent/Euler order.

For each pivot class u the norm is Res_y(H_t, u).  A pivot is legitimate iff
that resultant is a NONZERO element of Q for the integer t at hand; the class
is a zero divisor of A_t exactly when the resultant vanishes.  This driver
prints each norm as a polynomial in t (and j), factors it, lists ALL its
integer roots, and checks that none lies in the declared index range.
"""
from __future__ import annotations
import sympy as sp

t, j, n, s, y, d = sp.symbols("t j n s y d")
q, e = 2 * t + 1, 3 * t + 1
H = 12 * q**2 * y**2 - 12 * q * (t + 1) * y + (t + 1) * (3 * t + 2)
fails = []


def check(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        fails.append(name)


# ---- (1.1): Res_y(H_t, a*d+b) = 4 q^2 (3 b^2 - a^2 (t+1)),  d = 2qy-(t+1)
aa, bb = sp.symbols("aa bb")
lin = aa * (2 * q * y - (t + 1)) + bb
check("N0 H_t((d+t+1)/(2q)) = 3d^2-(t+1)",
      sp.simplify(H.subs(y, (d + t + 1) / (2 * q)) - (3 * d**2 - (t + 1))) == 0)
check("N1 (1.1) Res_y(H_t, a d + b) = 4q^2(3b^2 - a^2(t+1))",
      sp.simplify(sp.resultant(H, lin, y)
                  - 4 * q**2 * (3 * bb**2 - aa**2 * (t + 1))) == 0)


def norm(a_, b_):
    return sp.factor(sp.expand(4 * q**2 * (3 * b_**2 - a_**2 * (t + 1))))


def int_roots(poly, var):
    p = sp.Poly(sp.expand(poly), var)
    if p.is_zero:
        return "IDENTICALLY ZERO"
    return sorted(r for r in sp.solve(sp.Eq(p.as_expr(), 0), var)
                  if getattr(r, "is_Integer", False))


print("\n=== A. section 5 table (charged-coordinate order) ===")
table5 = [
    ("top endpoint", sp.Integer(0), sp.Integer(1)),          # class 1
    ("tag12 t<k<2t : d", sp.Integer(1), sp.Integer(0)),
    ("tag12 k=t : 3d+1", sp.Integer(3), sp.Integer(1)),
    ("tag00 k=t+s : d+s", sp.Integer(1), s),
    ("tag00 k=t (b2) : 2d+1", sp.Integer(2), sp.Integer(1)),
    ("tag00 0<k<t : y ~ d+(t+1)", sp.Integer(1), t + 1),
    ("tag00 k=0 (b1) : 5d+2t+3", sp.Integer(5), 2 * t + 3),
    ("tag11 k=0 : 3d+2(t+1)", sp.Integer(3), 2 * (t + 1)),
    ("g5 numerator : 5d+2t+3 (scaled)", sp.Integer(5), 2 * t + 3),
]
report5 = {
    "top endpoint": sp.Integer(1),
    "tag12 t<k<2t : d": -4 * q**2 * (t + 1),
    "tag12 k=t : 3d+1": -12 * q**2 * (3 * t + 2),
    "tag00 k=t+s : d+s": 4 * q**2 * (3 * s**2 - (t + 1)),
    "tag00 k=t (b2) : 2d+1": -4 * q**2 * (4 * t + 1),
    "tag00 0<k<t : y ~ d+(t+1)": None,
    "tag00 k=0 (b1) : 5d+2t+3": 4 * q**2 * (3 * t + 2) * (4 * t + 1),
    "tag11 k=0 : 3d+2(t+1)": 12 * q**2 * (t + 1) * (4 * t + 1),
    "g5 numerator : 5d+2t+3 (scaled)": None,
}
for name, a_, b_ in table5:
    if name.startswith("top"):
        val = sp.Integer(1)
    else:
        val = norm(a_, b_)
    exp = report5[name]
    agree = "n/a" if exp is None else (
        "MATCH" if sp.simplify(val - exp) == 0 else "DIFFERS")
    roots = int_roots(val, t) if val.has(t) else "no t"
    print("  %-34s Res = %-42s report:%s  integer t-roots: %s"
          % (name, val, agree, roots))
    if exp is not None:
        check("N2 section-5 table entry: " + name, sp.simplify(val - exp) == 0)
_resy = sp.factor(sp.resultant(H, y, y))
print("  sympy Res_y(H_t, y) = %s ; H_t(0) = %s (report's monic convention)"
      % (_resy, sp.factor(H.subs(y, 0))))
check("N3 Res_y(H_t,y) = H_t(0) = (t+1)(3t+2), no positive-integer root",
      sp.expand(_resy - (t + 1) * (3 * t + 2)) == 0
      and sp.expand(H.subs(y, 0) - (t + 1) * (3 * t + 2)) == 0
      and not [r for r in sp.solve(sp.Eq((t + 1) * (3 * t + 2), 0), t)
               if getattr(r, "is_Integer", False) and r >= 1])
gnum = t * (3 * t + 1) * (t + 1) * (5 * (2 * q * y - (t + 1)) + 2 * t + 3)
check("N4 (5.3) cleared g5 resultant = 4t^2(t+1)^2 q^2(3t+1)^2(3t+2)(4t+1)",
      sp.simplify(sp.resultant(H, gnum, y)
                  - 4 * t**2 * (t + 1)**2 * q**2 * (3 * t + 1)**2
                  * (3 * t + 2) * (4 * t + 1)) == 0)

print("\n=== B. THE OBSTRUCTION: d+s on the split ray t = 3s^2-1 ===")
res_ds = norm(sp.Integer(1), s)
print("  Res_y(H_t, d+s) = %s" % res_ds)
print("  vanishes  <=>  t+1 = 3 s^2  <=>  t = 3 s^2 - 1  ->  t = %s"
      % [3 * k**2 - 1 for k in range(1, 7)])
check("N5 Res(H_t,d+s) = 0 exactly at t = 3s^2-1",
      sp.simplify(res_ds.subs(t, 3 * s**2 - 1)) == 0)
check("N6 disc(H_t) = 48 q^2 (t+1); H_t splits over Q exactly at t=3s^2-1",
      sp.simplify(sp.discriminant(H, y) - 48 * q**2 * (t + 1)) == 0)
for sv in (1, 2, 3):
    tv = 3 * sv**2 - 1
    Hv = sp.Poly(H.subs(t, tv), y, domain=sp.QQ)
    cls = sp.Poly((2 * (2 * tv + 1) * y - (tv + 1)) + sv, y, domain=sp.QQ)
    gg = sp.gcd(Hv, cls)
    fac = sp.factor_list(Hv.as_expr())
    try:
        sp.invert(cls, Hv)
        inverted = True
    except Exception:
        inverted = False
    print("  t=%2d s=%d : H_t factors %s ; gcd(H_t, d+s) = %s ; invertible=%s"
          % (tv, sv, sp.factor(Hv.as_expr()), gg.as_expr(), inverted))
    check("N7 t=%d: d+s is a NONZERO ZERO DIVISOR of A_t (not invertible)" % tv,
          gg.degree() == 1 and not inverted and sp.rem(cls, Hv).as_expr() != 0)

print("\n  bypass witnessed at t=2 (s=1): charged deferral record")
H2 = sp.Poly(300 * y**2 - 180 * y + 24, y, domain=sp.QQ)
cand, later = sp.Poly(5 * y - 1, y, domain=sp.QQ), sp.Poly(39 * y - 10, y, domain=sp.QQ)
print("    H_2 = %s" % sp.factor(H2.as_expr()))
print("    candidate 5y-1 : Res=%s ; later pivot 39y-10 : Res=%s"
      % (sp.resultant(H2.as_expr(), cand.as_expr(), y),
         sp.resultant(H2.as_expr(), later.as_expr(), y)))
check("N8 5y-1 has zero resultant (deferred, never inverted)",
      sp.resultant(H2.as_expr(), cand.as_expr(), y) == 0)
check("N8b 39y-10 has nonzero resultant (the replacement pivot)",
      sp.resultant(H2.as_expr(), later.as_expr(), y) != 0)
check("N8c H_2 = 12(5y-1)(5y-2): the deferred class is literally a factor",
      sp.expand(H2.as_expr() - 12 * (5 * y - 1) * (5 * y - 2)) == 0)

print("\n=== C. section 5.1 proof-order pivots: norms for ALL positive t ===")
A_C = (9 * j**2 * t + 18 * j**2 - 54 * j * t**2 - 81 * j * t - 26 * j
       + 72 * t**3 + 144 * t**2 + 88 * t + 16)
B_C = (-9 * j**2 * t - 10 * j**2 + 24 * j * t**2 + 33 * j * t + 10 * j
       - 12 * t**3 - 20 * t**2 - 8 * t)
A_Q = 12 * t**2 + 16 * t + 4 - j * (3 * t + 4)
B_Q = 2 * (t + 1) * (j - t)
spine = [
    ("(5.7c) reconstruction y   (T,S diagonals 2my, (2m+1)y)", sp.Integer(1), t + 1,
     "m >= 0"),
    ("(5.7c) reconstruction 3d+2(t+1) ~ g", sp.Integer(3), 2 * (t + 1), "all t"),
    ("D1 divisibility: y*g = -c", None, None, "all t"),
    ("gauge alpha_t=0 : q/y", None, None, "all t"),
    ("(5.9)-(5.11) C_j pivot L_C", A_C, B_C, "1 <= j <= t-1"),
    ("(5.12)-(5.14) q_j pivot L_Q", A_Q, B_Q, "t <= j <= 2t"),
    ("(5.15) b2 pivot L_2 = 3q d + (t+1)", 3 * q, t + 1, "all t"),
]
for name, a_, b_, rng in spine:
    if a_ is None:
        print("  %-46s [%s]  product of the two classes above" % (name, rng))
        continue
    val = norm(a_, b_)
    print("  %-46s [%s]" % (name, rng))
    print("      Res = %s" % val)
    if val.has(j):
        # zero locus over the integers, restricted to the declared range
        sols = "see part D positivity certificate"
        bad = []
        for tv in range(1, 41):
            lo, hi = (1, tv - 1) if "t-1" in rng else (tv, 2 * tv)
            for jv in range(lo, hi + 1):
                if sp.expand(val.subs({t: tv, j: jv})) == 0:
                    bad.append((tv, jv))
        print("      parametric zero set: %s ; integer zeros in range for "
              "t<=40: %s" % (sols, bad if bad else "NONE"))
        check("N9 %s: no zero in range (t<=40 exhaustive)" % name, not bad)
    else:
        print("      integer t-roots: %s" % int_roots(val, t))
        check("N9 %s: no positive-integer t-root" % name,
              not [r for r in int_roots(val, t) if r >= 1])

print("\n=== D. positivity certificates for the two indexed families ===")
F_C = sp.cancel(sp.expand(-(3 * B_C**2 - A_C**2 * (t + 1))) / (3 * t + 2)**3)
check("P1 3B_C^2 - A_C^2(t+1) = -(3t+2)^3 F_C exactly",
      sp.simplify(sp.expand(3 * B_C**2 - A_C**2 * (t + 1)
                            + (3 * t + 2)**3 * F_C)) == 0)
F_C_pos = (3 * n**4 + 24 * n**3 * t + 42 * n**3 + 66 * n**2 * t**2
           + 146 * n**2 * t + 119 * n**2 + 72 * n * t**3 + 238 * n * t**2
           + 234 * n * t + 104 * n + 27 * t**4 + 134 * t**3 + 223 * t**2
           + 136 * t + 32)
check("P2 (5.11) F_C(t,t-n) equals the all-nonnegative form",
      sp.expand(sp.cancel(F_C.subs(j, t - n)) - F_C_pos) == 0)
check("P3 every coefficient of (5.11) is nonnegative and the constant is 32",
      all(co >= 0 for co in sp.Poly(F_C_pos, n, t).coeffs())
      and sp.Poly(F_C_pos, n, t).coeff_monomial(sp.Integer(1)) == 32)
F_Q = sp.cancel(sp.expand(-(3 * B_Q**2 - A_Q**2 * (t + 1))) / ((t + 1) * (3 * t + 2)**2))
check("P4 3B_Q^2 - A_Q^2(t+1) = -(t+1)(3t+2)^2 F_Q exactly",
      sp.simplify(sp.expand(3 * B_Q**2 - A_Q**2 * (t + 1)
                            + (t + 1) * (3 * t + 2)**2 * F_Q)) == 0)
F_Q_pos = n**2 + 4 * n * t + 6 * n + 4 * t**2 - 3
check("P5 (5.14) F_Q(t,q-n) = n^2+4nt+6n+4t^2-3",
      sp.expand(sp.cancel(F_Q.subs(j, 2 * t + 1 - n)) - F_Q_pos) == 0)
check("P6 F_Q >= 12 on 1<=n<=t+1, t>=1 (min at n=1,t=1)",
      sp.expand(F_Q_pos.subs({n: 1, t: 1})) == 12
      and all(F_Q_pos.subs({n: nv, t: tv}) >= 12
              for tv in range(1, 41) for nv in range(1, tv + 2)))
check("P7 (5.11a) Res_y(H_t,L_C) = -4q^2(3t+2)^3 F_C",
      sp.simplify(norm(A_C, B_C) + 4 * q**2 * (3 * t + 2)**3 * F_C) == 0)
check("P8 (5.14a) Res_y(H_t,L_Q) = -4q^2(t+1)(3t+2)^2 F_Q",
      sp.simplify(norm(A_Q, B_Q) + 4 * q**2 * (t + 1) * (3 * t + 2)**2 * F_Q) == 0)
check("P9 (5.15) Res_y(H_t,L_2) = -12q^2(t+1)(3t+2)(4t+1)",
      sp.simplify(norm(3 * q, t + 1) + 12 * q**2 * (t + 1) * (3 * t + 2)
                  * (4 * t + 1)) == 0)

print("\n=== E. rational denominators of (5.10),(5.13) on their ranges ===")
den_C = (t + 1) * (3 * t + 2)**3 * (4 * t - 2 * j + 1)
den_Q = (t + 1) * q * (3 * t + 2)**2 * (4 * t - 2 * j + 1)
check("E1 4t-2j+1 >= 2t+3 > 0 on 1<=j<=t-1",
      all(4 * tv - 2 * jv + 1 >= 2 * tv + 3
          for tv in range(2, 41) for jv in range(1, tv)))
check("E2 4t-2j+1 >= 1 > 0 on t<=j<=2t",
      all(4 * tv - 2 * jv + 1 >= 1
          for tv in range(2, 41) for jv in range(tv, 2 * tv + 1)))
check("E3 (5.13) numerator factor (q-j) >= 1 > 0 on t<=j<=2t",
      all(2 * tv + 1 - jv >= 1
          for tv in range(2, 41) for jv in range(tv, 2 * tv + 1)))
check("E4 D_top(t)=60(2t+1)^5 has only the root t=-1/2",
      sp.solve(sp.Eq(60 * (2 * t + 1)**5, 0), t) == [sp.Rational(-1, 2)])
check("E5 lc(H_t) = 12(2t+1)^2 nonzero for every positive integer t",
      sp.expand(sp.Poly(H, y).LC() - 12 * q**2) == 0)

print("\nGATE3_DONE fails=%d" % len(fails))
if fails:
    print("FAILED:", fails)
