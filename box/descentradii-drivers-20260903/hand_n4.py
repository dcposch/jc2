#!/usr/bin/env python3
"""DESCENT-RADII (A): independent sympy check of the printed n=4, m=2 witness.

Recomputes J, deg=deg_y, the eta-expansion coefficients f_{-2..3} and M=[-2,1]
from the printed f, g, without importing etaexp.py.  Then cross-checks etaexp.
"""
import sys, os
from fractions import Fraction as F
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

x, y = sp.symbols('x y')

g = (y**4 - 3*x*y**3 + sp.Rational(27, 8)*x**2*y**2
     - sp.Rational(27, 16)*x**3*y + sp.Rational(81, 256)*x**4
     + 2*y**3 - sp.Rational(35, 8)*x*y**2 + sp.Rational(51, 16)*x**2*y
     - sp.Rational(99, 128)*x**3
     + sp.Rational(9, 8)*y**2 - sp.Rational(25, 16)*x*y + sp.Rational(139, 256)*x**2
     + sp.Rational(9, 64)*y - sp.Rational(25, 256)*x + sp.Rational(1, 256))
f = (y**2 - sp.Rational(3, 2)*x*y + sp.Rational(9, 16)*x**2
     + y - sp.Rational(11, 16)*x)

print("== independent sympy check of the printed n=4 witness ==")
print("  g monic in y, deg_y g =", sp.degree(g, y), " total deg =", sp.total_degree(g))
print("  f monic in y, deg_y f =", sp.degree(f, y), " total deg =", sp.total_degree(f))
J = sp.expand(sp.diff(f, x)*sp.diff(g, y) - sp.diff(f, y)*sp.diff(g, x))
print("  J(f,g) =", J, "   constant nonzero:", J.free_symbols == set() and J != 0)

# Hand-readable rewrite: complete the square in f
# f = (y - 3/4 x)^2 + (y - 11/16 x)
print("  f = (y - 3/4 x)^2 + y - 11/16 x   identity:",
      sp.expand(f - ((y - sp.Rational(3, 4)*x)**2 + y - sp.Rational(11, 16)*x)) == 0)

# ---- eta-expansion, independent of etaexp.py ----
# g = y^4 * (1 + u * (...)) with u = 1/y.  eta = g^{-1/4} = u * (unit)^{-1/4}
u = sp.symbols('u')
# g as series in u: g = u^{-4} * G(u), G(0)=1
Gpoly = sp.Poly(sp.expand(g.subs(y, 1/u) * u**4), u)
# coefficients of G in u, with coeffs in Q[x]
Nprec = 12
Gcoeffs = [sp.expand(Gpoly.coeff_monomial(u**k)) for k in range(Nprec)]
print("  G(0) =", Gcoeffs[0], "  (need 1)")

# unit_pow: G^alpha, recursion N e_N = alpha * sum j g_j e_{N-j} - sum k e_k g_{N-k}
def unit_pow(gco, alpha, N):
    e = [sp.Integer(0)] * N
    e[0] = sp.Integer(1)
    for M in range(1, N):
        acc = 0
        for j in range(1, M+1):
            acc += j * alpha * gco[j] * e[M-j]
        for k in range(1, M):
            acc -= k * e[k] * gco[M-k]
        e[M] = sp.together(acc / M)
    return e

E = unit_pow(Gcoeffs, sp.Rational(-1, 4), Nprec)   # (unit)^{-1/4}; eta = u * E(u)
Einv = unit_pow(Gcoeffs, sp.Rational(1, 4), Nprec)  # (unit)^{+1/4}

# f = u^{-2} * F(u).  We want f = eta^{-2} + sum_{j>-2} f_j(x) eta^j
# eta = u * E, so eta^j = u^j E^j.  Work in powers of u.
Fpoly = sp.Poly(sp.expand(f.subs(y, 1/u) * u**2), u)
# remainder R starts as f, as a series in u of order -2
# Peel: for j = -2, -1, 0, ...  the u^j coefficient of remainder, divided by E^j's constant 1,
# is f_j (a polynomial in x).

def conv(a, b, N):
    out = [0]*N
    for i, ai in enumerate(a):
        if ai == 0: continue
        for j, bj in enumerate(b):
            if i+j < N:
                out[i+j] += ai*bj
    return [sp.expand(t) for t in out]

# E^j as series in u, j running
Ej = [sp.Integer(0)]*Nprec; Ej[0] = 1  # E^0
# start at j=-2: need E^{-2} = (Einv)^2
Einv2 = conv(Einv, Einv, Nprec)
# remainder of f as series in u, lo=-2: coeffs of u^{-2}, u^{-1}, ...
R = [sp.expand(Fpoly.coeff_monomial(u**k)) for k in range(Nprec)]  # R[k] = coeff of u^{k-2}? 
# f.subs(y,1/u)*u^2 = F, so f = u^{-2} * F; coeff of u^j in f is coeff of u^{j+2} in F
# Let's store f as dict j -> coeff, j = exponent of u.

f_u = {j: sp.expand(Fpoly.coeff_monomial(u**(j+2))) for j in range(-2, Nprec-2)}

# Peel against eta^j = u^j * E^j
# E^{j} for j starting at -2
powE = Einv2[:]  # E^{-2}
fj = {}
for j in range(-2, 4):
    # coeff of u^j in remainder is f_u[j] currently, and E^j has constant term 1,
    # so f_j(x) = remainder's u^j coefficient (the E^j constant is 1)
    cj = f_u.get(j, 0)
    fj[j] = sp.expand(cj)
    # subtract f_j * eta^j = f_j * u^j * E^j  from remainder
    for k in range(Nprec):
        uk = j + k  # power of u
        if uk in f_u:
            f_u[uk] = sp.expand(f_u[uk] - cj * powE[k])
        elif cj != 0 and powE[k] != 0:
            f_u[uk] = sp.expand(-cj * powE[k])
    # next: E^{j+1} = E^j * E
    powE = conv(powE, E, Nprec)

print("  eta-expansion coefficients (independent):")
for j in sorted(fj):
    print("     f_%d = %s" % (j, fj[j]))

print("  f_{-2} == 1:", fj[-2] == 1)
print("  f_{-1} == 0:", fj.get(-1, 0) == 0)
print("  f_0 == -1/16:", fj[0] == -sp.Rational(1, 16))
print("  f_1 == -1/128:", fj[1] == -sp.Rational(1, 128))
print("  f_2 == 1/256:", fj[2] == sp.Rational(1, 256))
print("  f_3 == -3/4096 + x/4096:", fj[3] == -sp.Rational(3, 4096) + x/4096)
print("  deg_x f_3 =", sp.degree(sp.Poly(fj[3], x), x), "  (Lemma 2.1 wants 1)")
print("  f_i constant for i < 3:", all(sp.degree(sp.Poly(fj[j], x), x) <= 0 for j in range(-2, 3)))

# characteristic data: M_j = min{i : f_i != 0, d_j doesn't divide i}
from math import gcd
Ms, ds = [], [4]
cur = 4
for j in sorted(fj):
    if fj[j] == 0:
        continue
    if cur and (j % cur != 0):
        Ms.append(j)
        cur = gcd(cur, abs(j))
        ds.append(cur)
print("  M =", Ms, "  d =", ds)
print("  M_2 =", Ms[1], " <= m = 2  -> M_2 > m is", Ms[1] > 2)

# cross-check etaexp
from etaexp import char_data
fP = {(0, 2): F(1), (1, 1): F(-3, 2), (2, 0): F(9, 16), (0, 1): F(1), (1, 0): F(-11, 16)}
gP = {}
# parse g monomials from sympy
gp = sp.Poly(g, x, y)
for (i, j), c in zip(gp.monoms(), gp.coeffs()):
    gP[(i, j)] = F(c.p, c.q) if hasattr(c, 'p') else F(int(c))
Ms2, ds2, fj2 = char_data(fP, 2, gP, 4, extra=8)
print("  etaexp.py cross-check M,d =", Ms2, ds2)
print("  match:", Ms2 == Ms and ds2 == ds)
