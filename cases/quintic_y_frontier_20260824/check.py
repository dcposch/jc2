#!/usr/bin/env python3
"""Exact replay for the independent quintic-y frontier preflight.

Run with:
  uv run --no-project --with sympy==1.14.0 python3 \
    cases/quintic_y_frontier_20260824/check.py
"""

import sympy as s


passed = 0


def check(label, condition):
    global passed
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'}  {label}")
    if not ok:
        raise AssertionError(label)
    passed += 1


x, y, t = s.symbols("x y t")

# ---------------------------------------------------------------------------
# (2,5): exact differential normal form and the first pole coefficient.
# ---------------------------------------------------------------------------
p = s.Function("p")(x)
lam, mu = s.symbols("lambda mu")
P25 = t**2 + p
q1 = s.Rational(15, 8) * p**2 + s.Rational(3, 2) * lam * p + mu
Q25 = t**5 + (s.Rational(5, 2) * p + lam) * t**3 + q1 * t
J25 = s.Poly(s.expand(s.diff(P25, x) * s.diff(Q25, t)
                      - s.diff(P25, t) * s.diff(Q25, x)), t)
check("(2,5) normalized bracket is p' q1", s.simplify(J25.as_expr() - s.diff(p, x) * q1) == 0)

rho, C0 = s.symbols("rho C0")
p0 = C0 - rho**2
Q25_y0 = s.expand(
    rho**5 + (s.Rational(5, 2) * p0 + lam) * rho**3
    + (s.Rational(15, 8) * p0**2 + s.Rational(3, 2) * lam * p0 + mu) * rho
)
want25 = (s.Rational(3, 8) * rho**5
          + (-s.Rational(5, 4) * C0 - lam / 2) * rho**3
          + (s.Rational(15, 8) * C0**2 + s.Rational(3, 2) * C0 * lam + mu) * rho)
check("(2,5) y=0 pole coefficient is 3/8", s.expand(Q25_y0 - want25) == 0)

# Exact Laurent near-control: P polynomial and J constant, Q misses only at y=0.
h25 = x**7
r25 = x**-1
t25 = h25 * y + r25
pp25 = -r25**2
Pc25 = s.expand(t25**2 + pp25)
Qc25 = s.expand(t25**5 + s.Rational(5, 2) * pp25 * t25**3
                 + s.Rational(15, 8) * pp25**2 * t25)
Jc25 = s.factor(s.diff(Pc25, x) * s.diff(Qc25, y)
                - s.diff(Pc25, y) * s.diff(Qc25, x))
check("(2,5) Laurent control P is polynomial", Pc25.is_polynomial(x, y))
check("(2,5) Laurent control has J=15/4", Jc25 == s.Rational(15, 4))
check("(2,5) Laurent control residual is 3/(8x^5)", s.factor(Qc25.subs(y, 0)) == s.Rational(3, 8) / x**5)

# ---------------------------------------------------------------------------
# (3,5): cubic first integral, pole resultant, and singular-curve pullback.
# ---------------------------------------------------------------------------
A = s.Function("A")(x)
B = s.Function("B")(x)
gam, mconst, nconst = s.symbols("gamma m n")
P35 = t**3 + A * t + B
Q35 = (t**5 + gam * t**4 + s.Rational(5, 3) * A * t**3
       + (s.Rational(4, 3) * gam * A + s.Rational(5, 3) * B + mconst) * t**2
       + (s.Rational(5, 9) * A**2 + s.Rational(4, 3) * gam * B + nconst) * t
       + s.Rational(2, 9) * gam * A**2 + s.Rational(10, 9) * A * B
       + s.Rational(2, 3) * mconst * A)
J35 = s.Poly(s.expand(s.diff(P35, x) * s.diff(Q35, t)
                      - s.diff(P35, t) * s.diff(Q35, x)), t)
H35 = 36 * gam * A * B + 54 * mconst * B + 27 * nconst * A - 5 * A**3 + 45 * B**2
check("(3,5) only t^1 and t^0 bracket rows remain",
      all(J35.coeff_monomial(t**i) == 0 for i in range(6, 1, -1)))
check("(3,5) t-row is H'/27", s.simplify(J35.coeff_monomial(t) - s.diff(H35, x) / 27) == 0)

a = s.symbols("a")
f35 = 5 * a**2 + 10 * a + 6
g35 = a**3 - 9 * a**2 - 18 * a - 9
subs35 = s.subresultants(g35, f35, a)
check("(3,5) depression-pole subresultant ends at 441", subs35[-1] == 441)

# Completing the square gives 225 Z^2 = Phi(A).
AA, ZZ, kk = s.symbols("AA ZZ kappa")
BB = ZZ - s.Rational(2, 5) * gam * AA - s.Rational(3, 5) * mconst
completed = s.expand(36 * gam * AA * BB + 54 * mconst * BB + 27 * nconst * AA
                     - 5 * AA**3 + 45 * BB**2 - kk)
Phi = (25 * AA**3 + 36 * gam**2 * AA**2
       + (108 * gam * mconst - 135 * nconst) * AA + 5 * kk + 81 * mconst**2)
check("(3,5) Weierstrass completion", s.expand(5 * completed - (225 * ZZ**2 - Phi)) == 0)

# On a double-root component A=s+R^2, 3Z=eps(A-r)R.  The bracket
# pullback has degree 6 in R with leading coefficient -eps*35/27.
R, rr, eps = s.symbols("R r eps")
ss = -s.Rational(36, 25) * gam**2 - 2 * rr
Ap = ss + R**2
Zp = eps * (Ap - rr) * R / 3
Bp = Zp - s.Rational(2, 5) * gam * Ap - s.Rational(3, 5) * mconst
np = (108 * gam * mconst - 25 * (rr**2 + 2 * rr * ss)) / 135
j35_R = -(4 * gam * Ap**2 * s.diff(Ap, R) - 12 * gam * Bp * s.diff(Bp, R)
          + 6 * mconst * Ap * s.diff(Ap, R) - 9 * np * s.diff(Bp, R)
          + 5 * Ap**2 * s.diff(Bp, R) + 10 * Ap * Bp * s.diff(Ap, R)) / 9
for sign in (1, -1):
    poly = s.Poly(s.factor(j35_R.subs(eps, sign)), R)
    check(f"(3,5) singular pullback degree 6, eps={sign}", poly.degree() == 6)
    check(f"(3,5) singular pullback leading coefficient, eps={sign}",
          poly.LC() == -sign * s.Rational(35, 27))

# ---------------------------------------------------------------------------
# (4,5): two first integrals and weighted-infinity discriminator.
# ---------------------------------------------------------------------------
C = s.Function("C")(x)
L, M, N = s.symbols("L M N")
P45 = t**4 + A * t**2 + B * t + C
E = s.Rational(5, 4) * A + L
F = s.Rational(5, 4) * B + M
G = s.Rational(5, 32) * A**2 + s.Rational(3, 4) * L * A + s.Rational(5, 4) * C + N
H = s.Rational(5, 16) * A * B + s.Rational(1, 2) * M * A + s.Rational(3, 4) * L * B
Q45 = t**5 + E * t**3 + F * t**2 + G * t + H
J45 = s.Poly(s.expand(s.diff(P45, x) * s.diff(Q45, t)
                      - s.diff(P45, t) * s.diff(Q45, x)), t)
I2 = (5 * A**3 + 12 * L * A**2 - 32 * N * A - 40 * A * C - 20 * B**2
      - 64 * M * B - 96 * L * C)
I1 = (24 * L * A * B + 16 * M * A**2 - 64 * M * C - 32 * N * B
      + 15 * A**2 * B - 40 * B * C)
check("(4,5) high bracket rows vanish",
      all(J45.coeff_monomial(t**i) == 0 for i in range(7, 2, -1)))
check("(4,5) t^2 row is -I2'/32",
      s.simplify(J45.coeff_monomial(t**2) + s.diff(I2, x) / 32) == 0)
check("(4,5) t row is -I1'/32",
      s.simplify(J45.coeff_monomial(t) + s.diff(I1, x) / 32) == 0)

# Leading pole equations for a=A/rho^2, b=B/rho^3, c=C/rho^4.
b, c = s.symbols("b c")
leadP = 1 + a + b + c
leadI2 = a**3 - 8 * a * c - 4 * b**2
leadI1 = b * (3 * a**2 - 8 * c)
leadQ = -s.Rational(1, 4) + s.Rational(5, 32) * a**2 + s.Rational(5, 16) * a * b
GB = s.groebner([leadP, leadI2, leadI1, leadQ], c, b, a, order="lex")
check("(4,5) no common depression-pole leading point", len(GB.polys) == 1 and GB.polys[0].as_expr() == 1)

f45 = 9 * a**4 + 80 * a**3 + 112 * a**2 + 128 * a + 64
g45 = 15 * a**3 + 20 * a**2 + 40 * a + 32
check("(4,5) b!=0 branch resultant",
      s.resultant(f45, g45, a) == -12180258816)

# Top bracket coefficients on the three weighted-infinity branches.
q, aa, bb, cc = s.symbols("q aa bb cc", nonzero=True)
topj_num = q * (20 * aa**2 * cc - 50 * aa * bb**2 + 160 * cc**2)
check("(4,5) C-only infinity branch bracket nonzero", 5 * q * cc**2 != 0)
check("(4,5) B=0 infinity branch bracket coefficient",
      s.simplify((topj_num / 32).subs({bb: 0, cc: aa**2 / 8}) - 5 * q * aa**4 / 32) == 0)
check("(4,5) cusp infinity branch bracket coefficient",
      s.simplify((topj_num / 32).subs({cc: 3 * aa**2 / 8, bb**2: -aa**3 / 2})
                 - 55 * q * aa**4 / 32) == 0)

# Exact Laurent near-control on the C-only branch.
h45 = x**9
r45 = x**-1
t45 = h45 * y + r45
Cc45 = -r45**4
Pc45 = s.expand(t45**4 + Cc45)
Qc45 = s.expand(t45**5 + s.Rational(5, 4) * Cc45 * t45)
Jc45 = s.factor(s.diff(Pc45, x) * s.diff(Qc45, y)
                - s.diff(Pc45, y) * s.diff(Qc45, x))
check("(4,5) Laurent control P is polynomial", Pc45.is_polynomial(x, y))
check("(4,5) Laurent control has J=-5", Jc45 == -5)
check("(4,5) Laurent control residual is -1/(4x^5)",
      s.factor(Qc45.subs(y, 0)) == -s.Rational(1, 4) / x**5)

print(f"\n{passed}/{passed} exact checks passed")
