"""Minimal exact sparse polynomial ring over Q, written for this lane."""
from fractions import Fraction as Fr

def zero(): return {}
def const(c):
    c = Fr(c)
    return {(): c} if c else {}
def var(name, e=1): return {((name, e),): Fr(1)}

def add(a, b):
    r = dict(a)
    for m, c in b.items():
        n = r.get(m, 0) + c
        if n: r[m] = n
        elif m in r: del r[m]
    return r

def neg(a): return {m: -c for m, c in a.items()}
def sub(a, b): return add(a, neg(b))

def smul(a, s):
    s = Fr(s)
    if not s: return {}
    return {m: c * s for m, c in a.items()}

def _mmul(m1, m2):
    d = dict(m1)
    for v, e in m2:
        d[v] = d.get(v, 0) + e
    return tuple(sorted(d.items()))

def mul(a, b):
    if not a or not b: return {}
    if len(a) == 1 and () in a: return smul(b, a[()])
    if len(b) == 1 and () in b: return smul(a, b[()])
    r = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            m = _mmul(m1, m2); n = r.get(m, 0) + c1 * c2
            if n: r[m] = n
            elif m in r: del r[m]
    return r

def is_zero(a): return not a
def vars_of(a):
    s = set()
    for m in a:
        for v, e in m: s.add(v)
    return s
def as_const(a):
    """return Fraction if a is a constant, else None"""
    if not a: return Fr(0)
    if len(a) == 1 and () in a: return a[()]
    return None
def lin_coeff(a, name):
    """coefficient of the degree-1 monomial `name` (must be pure linear term)."""
    return a.get(((name, 1),), Fr(0))
def subst(a, name, val):
    """substitute variable `name` -> polynomial val."""
    out = {}
    for m, c in a.items():
        e = 0; rest = []
        for v, ex in m:
            if v == name: e = ex
            else: rest.append((v, ex))
        term = {tuple(sorted(rest)): c}
        for _ in range(e): term = mul(term, val)
        out = add(out, term)
    return out

# ---- polynomials in one auxiliary variable V, coefficients in the ring ----
def pzero(): return {}
def padd(A, B):
    r = dict(A)
    for k, v in B.items():
        n = add(r.get(k, {}), v)
        if n: r[k] = n
        elif k in r: del r[k]
    return r
def pmul(A, B):
    r = {}
    for k1, v1 in A.items():
        for k2, v2 in B.items():
            k = k1 + k2; n = add(r.get(k, {}), mul(v1, v2))
            if n: r[k] = n
            elif k in r: del r[k]
    return r
def psmul(A, s):
    r = {}
    for k, v in A.items():
        n = smul(v, s)
        if n: r[k] = n
    return r
def pscale(A, poly):
    r = {}
    for k, v in A.items():
        n = mul(v, poly)
        if n: r[k] = n
    return r
def pdiff(A):
    r = {}
    for k, v in A.items():
        if k:
            n = smul(v, k)
            if n: r[k - 1] = n
    return r
def ppow(A, n):
    r = {0: const(1)}
    for _ in range(n): r = pmul(r, A)
    return r
