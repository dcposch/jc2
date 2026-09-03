#!/usr/bin/env python3
"""C1: closed form of the terminal family on the b3-axis, uniformly in t.

Sub-chart  S = { b4 = 0, q_{2,0} = ... = q_{t-1,0} = 0 }, residual variable b3.

Weight argument (A4 grading, wt(b3)=t+1): every eliminated variable has weight
in {1,...,2t+1} (C_j and q_{t..2t}, b2) or 3t+1 (b1) or t (B0); a weighted-
homogeneous rhs in the single variable b3 of weight t+1 is zero unless the
weight is a multiple of t+1.  In 1..2t+1 the only multiple is t+1 itself, and
3t+1, t are not multiples for t>=2.  Hence on S:

    C_j = 0 (all j),  b2 = b1 = B0 = 0,  q_{j,0} = 0 for j != t+1,
    q_{t+1,0} = lam * b3   for a scalar lam in A_t.

Everything is then explicit and this script solves for lam and evaluates the
two surviving terminal bands  2t-1  and  t-2  in Q(t)[d]/(3d^2-(t+1)).
"""
import sympy as sp

t, b3, lam = sp.symbols("t b3 lam")
d = sp.Symbol("d")
q = 2*t+1
e = 3*t+1
MIN = 3*d**2 - (t+1)                      # 3 d^2 = t+1 in A_t

def red(x):
    """Normal form in Q(t)[d]/(3d^2-(t+1)) with polynomial coefficients in b3, lam."""
    x = sp.together(sp.expand(x))
    n, den = sp.fraction(x)
    n = sp.rem(sp.Poly(sp.expand(n), d), sp.Poly(MIN, d)).as_expr()
    den = sp.rem(sp.Poly(sp.expand(den), d), sp.Poly(MIN, d)).as_expr()
    if sp.Poly(den, d).degree() > 0:                    # rationalise: N(a+bd)=a^2-b^2(t+1)/3
        a = sp.Poly(den, d).nth(0); b = sp.Poly(den, d).nth(1)
        conj = a - b*d
        n = sp.expand(n*conj)
        n = sp.rem(sp.Poly(n, d), sp.Poly(MIN, d)).as_expr()
        den = sp.expand(a**2 - b**2*(t+1)/3)
    return sp.expand(sp.cancel(sp.expand(n)/sp.expand(den)))

y  = red((d+t+1)/(2*q))
g  = red(e*t*(3*d+2*(t+1))/(6*q**3))
g1 = sp.Rational(1, 1)*e/q
g2 = red(g*(3*t+2)/(2*t*y))
c  = red(-y*g)

# --- consistency with the charged normalizer (5.7a) -------------------------
checks = {
    "H_t (3d^2=t+1) <-> 12q^2y^2-12q(t+1)y+(t+1)(3t+2)":
        red(12*q**2*y**2 - 12*q*(t+1)*y + (t+1)*(3*t+2)),
    "(3t+2)g - 2t y g2":            red((3*t+2)*g - 2*t*y*g2),
    "3q g + (t+1) g2 - (4t+1) y g1": red(3*q*g + (t+1)*g2 - (4*t+1)*y*g1),
    "2q g2 - t g1 - 2 e y":         red(2*q*g2 - t*g1 - 2*e*y),
}
for k, v in checks.items():
    print("  check %-46s = %s" % (k, sp.simplify(v)))

# --- the collapsed chart ----------------------------------------------------
w = lam*b3                                   # q_{t+1,0}
B_lead = red(g*(3*t+2)/(2*t*y))              # B = B_lead * h^t ; equals g2
delta  = red(g*(6*t*w + (5*t+2)*b3)/(2*y*(2*t-1)))
eta    = red(delta - g2*b3)
Bc     = red((eta + q*y*g1*b3 - 2*q*g*b3 + 2*t*g2*w)/(2*y))     # [h^{2t-1}] X'
Cc     = red(t*b3*(y*eta - 2*w*g)/(2*y))                        # [h^{t-2}]  X'

band_3t   = red(Bc - y*b3*e - q*eta - t*w*g1)      # eliminated: solves lam
band_2tm1 = red(Cc - y*b3*Bc - t*w*eta)            # terminal, weight 2t+2
band_tm2  = red(-y*b3*Cc)                          # terminal, weight 3t+3

sol = sp.solve(sp.Eq(sp.expand(band_3t/b3), 0), lam)
print("\n  lam solutions:", len(sol))
LAM = red(sol[0])
print("  lam =", sp.simplify(LAM))
print("  band_3t at lam :", sp.simplify(red(band_3t.subs(lam, LAM))))

alpha = sp.factor(sp.simplify(red(band_2tm1.subs(lam, LAM))/b3**2))
phi   = sp.factor(sp.simplify(red(band_tm2.subs(lam, LAM))/b3**3))
print("\n  alpha_t = [b3^2] T_{t,2t-1}|_S =", alpha)
print("\n  phi_t   = [b3^3] T_{t,t-2}|_S  =", phi)

# --- norms (1.1): for u = A*d + B, Res_y(H_t,u) ~ N(u) = B^2 - A^2 (t+1)/3 ----
print("\n  --- unit norms ---")
for name, expr in (("phi_t linear part 6*t*d-(t+1)", 6*t*d-(t+1)),
                   ("alpha_t linear part", (27*t**3-30*t**2+t-2)*d + (6*t**3+13*t**2-3*t+2))):
    P = sp.Poly(expr, d)
    A, B = P.nth(1), P.nth(0)
    N = sp.factor(sp.expand(B**2 - A**2*(t+1)/3))
    print("  N(%s)\n     = %s" % (name, N))
    print("     integer roots t>=1:",
          [r for r in sp.solve(sp.Eq(sp.expand(N*3), 0), t) if r.is_integer and r >= 1])
print("\n  rational prefactor of phi_t vanishes at t =",
      [r for r in sp.solve(sp.Eq(t*(t-2)*(3*t+1), 0), t) if r.is_integer])
print("  rational prefactor of alpha_t vanishes at t =",
      [r for r in sp.solve(sp.Eq(t*(3*t+1), 0), t) if r.is_integer])
print("  denominators: phi_t 72*(2t+1)^3*(3t-1) ; alpha_t 12*(2t+1)^2*(3t-1)^2*(3t+2)")
print("  denominator integer roots t>=1:",
      sorted({r for r in sp.solve(sp.Eq((2*t+1)*(3*t-1)*(3*t+2), 0), t) if r.is_integer and r >= 1}))
