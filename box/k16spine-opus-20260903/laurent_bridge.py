#!/usr/bin/env python3
"""Exact tuple-level Laurent bridge for the K=16 ray, from the order chart.

Chart (charged, k16-uniform-structure-sol56 lines 40-80):
  z=pi-gamma, B=pi*z+b1*pi+b2, A=pi*B+b3, h=pi*A+b4
  P=h^e+sum_{i=1..e} alpha_i h^{e-i},  Q=h^q+sum_{j=2..q} beta_j h^{q-j}
  S_i=<1> (i<=t), <1,A> (t<i<=2t), <1,A,B> (2t<i<=3t), S_e=<1,gamma,A,B,z>.
Method: xi=h^{-1/4} (so h=xi^-4), solve h(gamma,Y(xi))=xi^-4 for pi=Y(xi) by
Newton iteration in k[gamma,params]((xi)); then
  G_P = P*xi^{n} = 1+sum alpha_i xi^{4i},  G_Q = Q*xi^{m} = 1+sum beta_j xi^{4j}
  eta = P^{-1/n} = xi * G_P^{-1/n};  revert to get xi(eta);
  Phi = Q*eta^m = G_Q * G_P^{-q/e}  re-expanded in eta;  q_i = [eta^{i+m}] Phi.
4-tuple condition: q_i=0 for 4 not| i, i<M2=12t+1; q_{M2}!=0.  M2+m=20t+5.
"""
import sys, sympy as sp
from sympy import Rational as R

T = int(sys.argv[1]) if len(sys.argv) > 1 else 1
PREC = int(sys.argv[2]) if len(sys.argv) > 2 else 20*T + 8   # rel. order in xi/eta

e, q = 3*T+1, 2*T+1
n, m, M2 = 12*T+4, 8*T+4, 12*T+1
g = sp.Symbol('g')                                   # gamma
b1, b2, b3, b4 = sp.symbols('b1 b2 b3 b4')

# ---------- truncated Laurent series: dict {exponent: coeff}, exps >= lo ----------
class S:
    __slots__ = ('c', 'lo')
    def __init__(self, c, lo=0):
        self.c = dict(c); self.lo = lo
    def trunc(self, top):
        return S({k: v for k, v in self.c.items() if k < top and v != 0}, self.lo)

def smul(a, b, lo, top):
    out = {}
    for i, u in a.items():
        if u == 0: continue
        for j, v in b.items():
            if v == 0: continue
            k = i + j
            if k < top:
                out[k] = out.get(k, 0) + u*v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}

def sadd(a, b, top):
    out = dict(a)
    for j, v in b.items():
        if j < top:
            out[j] = sp.expand(out.get(j, 0) + v)
    return {k: v for k, v in out.items() if v != 0}

def sscal(a, s):
    return {k: sp.expand(s*v) for k, v in a.items() if sp.expand(s*v) != 0}

def spow_unit(a, s, top):
    """a^s for a = {0:1, ...}; recurrence k c_k = sum_{j=1..k}(s j-(k-j)) a_j c_{k-j}."""
    assert a.get(0, 0) == 1
    c = {0: sp.Integer(1)}
    for k in range(1, top):
        acc = 0
        for j in range(1, k+1):
            aj = a.get(j, 0)
            if aj == 0: continue
            ck = c.get(k-j, 0)
            if ck == 0: continue
            acc += (s*j - (k-j))*aj*ck
        acc = sp.expand(sp.together(acc/k))
        if acc != 0: c[k] = sp.cancel(acc)
    return c

# ---------- chart parameters ----------
alpha = {}; beta = {}; params = [b1, b2, b3, b4]
def basis(i):
    if i <= T:            return ['1']
    if i <= 2*T:          return ['1', 'A']
    if i <= 3*T:          return ['1', 'A', 'B']
    return ['1', 'g', 'A', 'B', 'z']            # i == e
for i in range(1, e+1):
    for f in basis(i):
        s = sp.Symbol(f'a{i}_{f}'); alpha[(i, f)] = s; params.append(s)
for j in range(2, q+1):
    for f in basis(j):
        s = sp.Symbol(f'q{j}_{f}'); beta[(j, f)] = s; params.append(s)
cc = sp.Symbol('c'); params.append(cc)
print(f"t={T}: e={e} q={q} n={n} m={m} M2={M2}; chart unknowns (ungauged, incl c) = {len(params)}")

# ---------- pi = Y(xi) with h(g,Y)=xi^{-4}  ----------
# h = pi^4 + (b1-g) pi^3 + b2 pi^2 + b3 pi + b4.
top = PREC + 6
# Y = xi^{-1} * u, u = 1 + O(xi).  h = Y^4(1+(b1-g)/Y+b2/Y^2+b3/Y^3+b4/Y^4) = xi^{-4}
# => Y = xi^{-1} * (1+(b1-g)/Y+b2/Y^2+b3/Y^3+b4/Y^4)^{-1/4}. Iterate on u.
u = {0: sp.Integer(1)}
for _ in range(top.bit_length()+3):
    # 1/Y = xi * u^{-1}
    uinv = spow_unit(u, -1, top)
    invY = {k+1: v for k, v in uinv.items() if k+1 < top}
    p2 = smul(invY, invY, 0, top); p3 = smul(p2, invY, 0, top); p4 = smul(p3, invY, 0, top)
    W = {0: sp.Integer(1)}
    W = sadd(W, sscal(invY, b1-g), top)
    W = sadd(W, sscal(p2, b2), top); W = sadd(W, sscal(p3, b3), top); W = sadd(W, sscal(p4, b4), top)
    unew = spow_unit(W, R(-1, 4), top)
    if unew == u: break
    u = unew
Y = {k-1: v for k, v in u.items()}                       # pi as series in xi, ord -1
def ck(sr):                                              # check
    return sr
# verify h(Y) = xi^{-4}
Y2 = smul(Y, Y, -2, top); Y3 = smul(Y2, Y, -3, top); Y4 = smul(Y3, Y, -4, top)
hh = sadd(sadd(sadd(sadd(Y4, sscal(Y3, b1-g), top), sscal(Y2, b2), top), sscal(Y, b3), top), {0: b4}, top)
hh = {k: sp.expand(v) for k, v in hh.items() if sp.expand(v) != 0}
assert hh == {-4: sp.Integer(1)}, ("h(Y) != xi^-4", sorted(hh)[:6])
print("  [control] h(gamma,Y(xi)) == xi^-4 exactly, to relative order", top)
