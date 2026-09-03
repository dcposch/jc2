#!/usr/bin/env python3
"""M2-DESCENT: exact eta-expansion engine (Moh 1983 pp.150-151).

Given f, g in k[x,y] monic in y with deg_y g = n, deg_y f = m, computes
    eta = g^{-1/n} in k[x]((y^{-1}))~,   f = eta^{-m} + sum_{j>-m} f_j(x) eta^j
and returns the characteristic data {M_j, d_j} of Moh p.150.

Coefficients: exact Fractions; polynomials in x are dicts {deg: Fraction}.
Stdlib only.  Controls at the bottom.
"""
from fractions import Fraction as F
from math import gcd

# ---------- tiny polynomial ring Q[x] --------------------------------------
def pzero(): return {}
def pconst(c): c = F(c); return {} if c == 0 else {0: c}
def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        w = r.get(k, F(0)) + v
        if w: r[k] = w
        else: r.pop(k, None)
    return r
def pscal(a, c):
    c = F(c)
    return {} if c == 0 else {k: v*c for k, v in a.items()}
def pmul(a, b):
    r = {}
    for i, u in a.items():
        for j, v in b.items():
            k = i+j; w = r.get(k, F(0)) + u*v
            if w: r[k] = w
            else: r.pop(k, None)
    return r
def pdeg(a): return max(a) if a else -1

# ---------- Laurent series in u = y^{-1}, coefficients in Q[x] -------------
class Ser:
    """sum_{k=lo}^{lo+len-1} c[k] u^k, truncated at u^{hi} (exclusive)."""
    __slots__ = ('lo', 'c', 'hi')
    def __init__(self, lo, c, hi):
        self.lo, self.c, self.hi = lo, c, hi          # c: list of Q[x]
    def coeff(self, k):
        i = k - self.lo
        return self.c[i] if 0 <= i < len(self.c) else pzero()
    def ordv(self):
        for i, p in enumerate(self.c):
            if p: return self.lo + i
        return None

def s_mul(A, B, hi):
    lo = A.lo + B.lo
    n = hi - lo
    if n <= 0: return Ser(lo, [], hi)
    out = [pzero()]*n
    for i, u in enumerate(A.c):
        if not u: continue
        for j, v in enumerate(B.c):
            if not v: continue
            k = A.lo+i + B.lo+j - lo
            if 0 <= k < n: out[k] = padd(out[k], pmul(u, v))
    return Ser(lo, out, hi)

def s_sub(A, B, hi):
    lo = min(A.lo, B.lo); n = hi - lo
    out = [pzero()]*max(n, 0)
    for k in range(lo, hi):
        out[k-lo] = padd(A.coeff(k), pscal(B.coeff(k), -1))
    return Ser(lo, out, hi)

def unit_pow(G, alpha, hi):
    """G = 1 + O(u); returns G^alpha as a series in u truncated at u^hi.
       Recursion N e_N = alpha*sum_{j>=1} j g_j e_{N-j} - sum_{k<N} k e_k g_{N-k}."""
    N = hi
    g = [G.coeff(k) for k in range(0, N)]
    assert g[0] == {0: F(1)}, "unit_pow needs constant term 1"
    e = [pzero()]*N; e[0] = {0: F(1)}
    for M in range(1, N):
        acc = pzero()
        for j in range(1, M+1):
            if g[j]: acc = padd(acc, pscal(pmul(g[j], e[M-j]), F(j)*alpha))
        for k in range(1, M):
            if e[k]: acc = padd(acc, pscal(pmul(e[k], g[M-k]), -F(k)))
        e[M] = pscal(acc, F(1, M))
    return Ser(0, e, hi)

def poly_to_ser(P, degy, hi):
    """P = dict {(i,j): Fraction} for x^i y^j, deg_y P = degy, monic in y.
       returns P as a series in u=y^{-1}: P = u^{-degy}*(1 + a_1 u + ...)."""
    co = {}
    for (i, j), c in P.items():
        k = degy - j
        co.setdefault(k, {})
        co[k][i] = co[k].get(i, F(0)) + F(c)
    lo = -degy
    out = [pzero()]*(hi-lo)
    for k, p in co.items():
        p = {a: b for a, b in p.items() if b}
        idx = (k-degy) - lo
        if 0 <= idx < len(out): out[idx] = p
    return Ser(lo, out, hi)

def char_data(fP, m, gP, n, extra=6):
    """returns (Ms, ds, fcoeffs) -- Moh p.150 characteristic data of (f,g)."""
    hi = n + extra                      # need eta-exponents up to n-1
    prec = n + m + extra
    G = poly_to_ser(gP, n, hi)          # g = u^{-n}(1 + ...)
    Gu = Ser(0, [G.coeff(k-n) for k in range(0, prec)], prec)   # the unit part
    E = unit_pow(Gu, F(-1, n), prec)    # E = (unit)^{-1/n};  eta = u*E
    Einv = unit_pow(Gu, F(1, n), prec)
    # eta^j = u^j E^j
    R = poly_to_ser(fP, m, hi)
    fj = {}
    Ej = Ser(0, [pzero()]*prec, prec); Ej.c[0] = {0: F(1)}
    for _ in range(m): Ej = s_mul(Ej, Einv, prec)      # E^{-m}
    for j in range(-m, n):
        c = R.coeff(j)
        if c:
            fj[j] = c
            T = Ser(j, [pmul(c, Ej.coeff(k)) for k in range(0, hi-j)], hi)
            R = s_sub(R, T, hi)
        Ej = s_mul(Ej, E, prec)
    # characteristic data
    Ms, ds = [], [n]
    cur = n
    for j in sorted(fj):
        if j == -m and fj[j] == {0: F(1)}: pass
        if cur and j % cur != 0:
            Ms.append(j); cur = gcd(cur, abs(j)) if cur else abs(j); ds.append(cur)
    return Ms, ds, fj
