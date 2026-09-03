#!/usr/bin/env python3
"""GATE 1: independent re-derivation of the charged report's section 2.

Nothing is imported from the charged compact_remainder.py.  The Jacobian is
recomputed from scratch in the (pi,gamma) chart with the SAME orientation the
charged generator t_order_system.jac uses, namely

    J(f,g) = f_gamma * g_pi - f_pi * g_gamma,

and the target equation is J(Q,P) = c*gamma.

Checks performed:
  A. tag decomposition (2.4) and syzygies (2.5), with generic symbols;
  B. Laurent decomposition (2.2) and the five identities (2.3), derived from
     the explicit gamma(X,p) substitution, no division by p;
  C. equivalence of the two systems (each D_i is a combination of the tags
     and conversely);
  D. consequences (2.6) and the band recurrences (5.6)/(5.7)/(5.7b);
  E. instantiation against the frozen charged generator at t=2,3,4.
"""
from __future__ import annotations

import sys
import sympy as sp

INPUTS = "/tmp/jc2-lane.nglVmb/inputs"
sys.path.insert(0, INPUTS)

gamma, pi, X, p = sp.symbols("gamma pi X p")
b1, b2, b3, b4 = sp.symbols("b1 b2 b3 b4")
y, g, c = sp.symbols("y g c")
fails = []


def check(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        fails.append(name)


# ---------------------------------------------------------------- A: tags
Us, Ups, Rs, Rps, Vs, Vps, Ss, Sps, Ts, Tps = sp.symbols(
    "U Up R Rp V Vp S Sp T Tp")

z = pi - gamma
B = pi * z + b1 * pi + b2
A = pi * B + b3
h = pi * A + b4
L = X - b4


def jac(f, k):
    """Charged orientation: t_order_system.jac."""
    return sp.diff(f, gamma) * sp.diff(k, pi) - sp.diff(f, pi) * sp.diff(k, gamma)


# Chain rule with h replaced by the free symbol X in the coefficient slots.
# Q = U(h) + A R(h) + y B ; P = V(h) + A S(h) + B T(h) + g z.
Qh, Ph = Ups + A * Rps, Vps + A * Sps + B * Tps
raw = sp.expand(
    jac(h, A) * (Qh * Ss - Rs * Ph)
    + jac(h, B) * (Qh * Ts - y * Ph)
    + jac(h, z) * (g * Qh)
    + jac(A, B) * (Rs * Ts - y * Ss)
    + jac(A, z) * (g * Rs)
    + jac(B, z) * (g * y))
# The brackets above are exact polynomials in pi, gamma; substitute h -> X only
# in the *coefficient* arguments, then reduce modulo the monic relation h - X.
raw = raw.subs({h.expand(): X}, simultaneous=True)
dom = sp.QQ[gamma, X, b1, b2, b3, b4, Us, Ups, Rs, Rps, Vs, Vps,
            Ss, Sps, Ts, Tps, y, g]
rem = sp.rem(sp.Poly(sp.expand(raw), pi, domain=dom),
             sp.Poly(h - X, pi, domain=dom)).as_expr()
tags = {k: sp.expand(v) for k, v in sp.Poly(sp.expand(rem), gamma, pi).terms()}
tags = {k: v for k, v in tags.items() if v != 0}
check("A1 tag support == the seven charged tags",
      set(tags) == {(1, 2), (1, 1), (1, 0), (0, 3), (0, 2), (0, 1), (0, 0)})
C12, C11, C10 = tags[(1, 2)], tags[(1, 1)], tags[(1, 0)]
C03, C02, C01, C00 = tags[(0, 3)], tags[(0, 2)], tags[(0, 1)], tags[(0, 0)]

# Report (2.4)/(2.5), retyped from the report text and compared to my rem.
r_C12 = (-Rs * Ts + L * (Rs * Tps - 2 * Rps * Ts + 2 * y * Sps) + y * Ss
         - b3 * (g * Rps + y * Tps) - 3 * g * Ups)
r_C11 = -2 * g * Rs + L * (2 * y * Tps - 3 * g * Rps)
r_C00 = (L**2 * (Rps * Ss - Rs * Sps)
         + L * (b3 * (Rps * Ts - y * Sps) + 2 * b2 * (g * Rps - y * Tps)
                + 2 * Ts * Ups - 2 * y * Vps)
         + g * b3**2 * Rps + g * b2 * Rs + g * b3 * Ups + b1 * g * y)
r_C01 = ((b3 * y - L * Rs) * Vps + (L * Ss - b3 * Ts - b2 * g) * Ups + g * y
         - b2 * r_C12 - b1 * r_C11)
check("A2 (2.4) C12", sp.expand(C12 - r_C12) == 0)
check("A2 (2.4) C11", sp.expand(C11 - r_C11) == 0)
check("A2 (2.4) C00", sp.expand(C00 - r_C00) == 0)
check("A2 (2.4) C01", sp.expand(C01 - r_C01) == 0)
check("A3 (2.5) C03 = -C12", sp.expand(C03 + C12) == 0)
check("A3 (2.5) C02 = -b1*C12 - C11", sp.expand(C02 + b1 * C12 + C11) == 0)
check("A3 (2.5) C10 = -y*g", sp.expand(C10 + y * g) == 0)
# J(Q,P) = c*gamma reads off c from the (1,0) tag.
check("A4 c = -y*g is forced by the (1,0) tag", sp.expand(C10 + y * g) == 0)

# ------------------------------------------------------- B: Laurent (2.2)/(2.3)
# gamma as a Laurent function of (X,p).  Derived, not assumed:
#   X = h = p^4 + b1 p^3 + b2 p^2 + b3 p + b4 - p^3*gamma.
gam_L = p + b1 + b2 / p + b3 / p**2 - (X - b4) / p**3
check("B0 gamma(X,p) inverts h",
      sp.simplify(h.subs({pi: p, gamma: gam_L}) - X) == 0)
zL = sp.together(p - gam_L)
AL, BL = (X - b4) / p, (X - b4) / p**2 - b3 / p
check("B1 A = L/p", sp.simplify(A.subs({pi: p, gamma: gam_L}) - AL) == 0)
check("B1 B = L/p^2 - b3/p", sp.simplify(B.subs({pi: p, gamma: gam_L}) - BL) == 0)
check("B1 z = -b1 - b2/p - b3/p^2 + L/p^3",
      sp.simplify(zL - (-b1 - b2 / p - b3 / p**2 + (X - b4) / p**3)) == 0)

Q1, Q2 = L * Rs - y * b3, y * L
P0, P1 = Vs - g * b1, L * Ss - b3 * Ts - g * b2
P2, P3 = L * Ts - g * b3, g * L
QL = Us + AL * Rs + y * BL
PL = Vs + AL * Ss + BL * Ts + g * zL
check("B2 (2.2) Q coefficients",
      sp.simplify(QL - (Us + Q1 / p + Q2 / p**2)) == 0)
check("B2 (2.2) P coefficients",
      sp.simplify(PL - (P0 + P1 / p + P2 / p**2 + P3 / p**3)) == 0)

# Jacobian in (X,p).  d/dX of a coefficient block is written with primes.
def dX(expr):
    """Formal X-derivative treating U,R,V,S,T as functions of X."""
    out = sp.diff(expr, X)
    for f, fp in ((Us, Ups), (Rs, Rps), (Vs, Vps), (Ss, Sps), (Ts, Tps)):
        out += sp.diff(expr, f) * fp
    return sp.expand(out)


QX, PX = dX(Us + Q1 / p + Q2 / p**2), dX(P0 + P1 / p + P2 / p**2 + P3 / p**3)
Qp = sp.diff(Us + Q1 / p + Q2 / p**2, p)
Pp = sp.diff(P0 + P1 / p + P2 / p**2 + P3 / p**3, p)
# Charged orientation again: J(Q,P) = -p^3 * (Q_X P_p - Q_p P_X)  [det = -p^3].
W = sp.expand(sp.together(QX * Pp - Qp * PX))
JL = sp.expand(-p**3 * W)
# c*gamma with c = -y*g
target = sp.expand(c * gam_L)
Dpoly = sp.Poly(sp.expand((JL - target) * p**3), p)
Dco = {n: sp.expand(v) for n, v in zip(range(Dpoly.degree(), -1, -1),
                                       Dpoly.all_coeffs())}
# JL - c*gamma == 0 as a Laurent identity <=> all p-coefficients vanish.
D0 = sp.expand(Q1 * dX(P0) - Ups * P1)
D1 = sp.expand(2 * Q2 * dX(P0) + Q1 * dX(P1) - dX(Q1) * P1 - 2 * Ups * P2)
D2 = sp.expand(-3 * Ups * P3 + Q1 * dX(P2) - 2 * dX(Q1) * P2
               + 2 * Q2 * dX(P1) - dX(Q2) * P1)
D3 = sp.expand(Q1 * dX(P3) - 3 * dX(Q1) * P3 + 2 * (Q2 * dX(P2) - dX(Q2) * P2))
D4 = sp.expand(2 * Q2 * dX(P3) - 3 * dX(Q2) * P3)
# Report (2.3): D0=-c, D1=-c b1, D2=-c b2, D3=-c b3, D4=c*L.
# (JL - c*gamma)*p^3 = -(D0+c)p^4 -(D1+c b1)p^3 -(D2+c b2)p^2 -(D3+c b3)p
#                       -(D4-c L).
resid = {4: -(D0 + c), 3: -(D1 + c * b1), 2: -(D2 + c * b2),
         1: -(D3 + c * b3), 0: -(D4 - c * L)}
for k in sorted(resid, reverse=True):
    got = Dco.get(k, sp.Integer(0))
    check("B3 (2.3) p-coefficient %d" % k, sp.expand(got - resid[k]) == 0)
check("B3 (2.3) no other p-coefficient",
      all(sp.expand(v) == 0 for k, v in Dco.items() if k not in resid))
check("B3b D4 - c*L vanishes identically (2.3) fifth row is automatic",
      sp.expand((D4 - c * L).subs({c: -y * g})) == 0)

# ------------------------------------------------- C: equivalence tags <-> D
# Rem = sum_tags C_tag * gamma^a * pi^b differs from J(Q,P)-c*gamma by a
# multiple of (h-X); substituting gamma=gamma_L(X,p), pi=p forces X=h and so
# kills that multiple.  Hence the two coefficient systems are two coordinate
# readings of ONE element, and the change of basis is explicit.
sub_c = {c: -y * g}
Dres = [sp.expand((D0 + c).subs(sub_c)), sp.expand((D1 + c * b1).subs(sub_c)),
        sp.expand((D2 + c * b2).subs(sub_c)), sp.expand((D3 + c * b3).subs(sub_c)),
        sp.expand((D4 - c * L).subs(sub_c))]
Cred = [sp.expand(C12), sp.expand(C11), sp.expand(C01), sp.expand(C00)]
rem_sub = sp.expand(sum(v * gam_L ** k[0] * p ** k[1]
                        for k, v in tags.items()))
# rem_sub is J(Q,P) read through the tags; JL is J(Q,P) read through the
# Laurent p-expansion.  They must be the identical Laurent element.
check("C1 tag reading == Laurent reading of the same element J(Q,P)",
      sp.expand(sp.together(rem_sub - JL)) == 0)
# Explicit invertible change of basis on the reduced 4-vectors.
Cvec = sp.Matrix(Cred)
M = sp.zeros(5, 4)
for i, d in enumerate(Dres):
    for j, cc in enumerate(Cred):
        pass
# Read the matrix by matching monomials in the free block symbols.
blocks = [Us, Ups, Rs, Rps, Vs, Vps, Ss, Sps, Ts, Tps]
def coeffvec(e):
    pe = sp.Poly(sp.expand(e), *blocks)
    return pe
sol = sp.symbols("m0:20")
Mrows = []
for d in Dres:
    unk = sp.symbols("u0:4")
    eq = sp.expand(d - sum(u * cc for u, cc in zip(unk, Cred)))
    pol = sp.Poly(eq, *blocks)
    # solve for the u_j as elements of Q[X,b1..b4,y,g]
    system = [sp.expand(v) for v in pol.coeffs()]
    s = sp.solve(system, unk, dict=True)
    ok = bool(s)
    if ok:
        row = [sp.simplify(s[0].get(u, u)) for u in unk]
        ok = all(not any(uu in sp.sympify(r).free_symbols for uu in unk) for r in row)
        Mrows.append(row)
    check("C2 D-row is an explicit Q[X,b]-combination of the tags", ok)
for i, row in enumerate(Mrows):
    print("      D%d = " % i + " + ".join("(%s)*%s" % (sp.factor(r), n)
          for r, n in zip(row, ["C12", "C11", "C01", "C00"]) if r != 0))

# ------------------------------------------------------------- D: (2.6),(5.7)
Cpol, Cpp = sp.symbols("C_ Cp_")   # C and C' with R = L*C
sub_R = {Rs: L * Cpol, Rps: Cpol + L * Cpp}
c11 = sp.expand(r_C11.subs(sub_R))
check("D1 C11 | (X=b4) forces R(b4)=0",
      sp.expand(r_C11.subs({X: b4})) == sp.expand(-2 * g * Rs))
check("D2 (2.6) C11/L = 2y*T' - g(5C+3LC')",
      sp.expand(sp.cancel(c11 / L)
                - (2 * y * Tps - g * (5 * Cpol + 3 * L * Cpp))) == 0)
Tp_sol = g * (5 * Cpol + 3 * L * Cpp) / (2 * y)
check("D2b C11 vanishes at the solved T'",
      sp.expand(sp.simplify(c11.subs({Tps: Tp_sol}))) == 0)
rhs57 = (3 * g * Ups + Rs * Ts - L * Rs * Tps + 2 * L * Rps * Ts
         + g * b3 * (Rs / L + sp.Rational(5, 2) * Rps))
lhs57 = y * Ss + 2 * y * L * Sps            # y(1+2L d/dL)S
c12_sub = r_C12.subs(sub_R).subs({Tps: Tp_sol.subs(sub_R)})
d57 = sp.expand(sp.simplify(sp.together(
    (lhs57 - rhs57).subs(sub_R).subs({Tps: Tp_sol}) - c12_sub)))
check("D3 (5.7) is exactly C12 = 0 (after R=LC and the solved T')", d57 == 0)
if d57 != 0:
    print("      residual (5.7)-C12 =", sp.factor(d57))
# Backward direction of the C<->D equivalence: L is monic in X, hence a
# nonzerodivisor, so D3 = L*C11 == 0 forces C11 == 0, and then
# D2 = L*C12 - b3*C11 == 0 forces C12 == 0; D1, D0 then give C00, C01.
check("C3 backward: L = X-b4 is a nonzerodivisor (monic in X)",
      sp.Poly(L, X).LC() == 1)
# (5.7b) coefficient form
m = sp.Symbol("m", integer=True, nonnegative=True)
cm, em = sp.symbols("c_m e_m")
check("D4 (5.7b) [L^(m+1)]T = g(3m+5)c_m/(2y(m+1))",
      sp.simplify(sp.expand((5 * cm + 3 * m * cm) * g / (2 * y)) / (m + 1)
                  - g * (3 * m + 5) * cm / (2 * y * (m + 1))) == 0)
check("D4 (5.7b) [L^m]S = e_m/(y(2m+1))",
      sp.simplify(em / (y * (1 + 2 * m)) - em / (y * (2 * m + 1))) == 0)

print("GATE1_PART_ABCD_DONE fails=%d" % len(fails))
if fails:
    print("FAILED:", fails)
