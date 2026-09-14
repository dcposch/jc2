#!/usr/bin/env python3
"""Exact stdlib controls for the producer's Lemma 3.1 algebra, Remark 4.1 and Remark 4.3.
No Assert nodes; every check prints PASS/FAIL and the exit code is the number of failures
among positive checks plus the number of negative controls that unexpectedly passed.
Input factor degrees are <= 5. Bivariate polynomials are dicts {(i_delta, j_w): Fraction}."""
from fractions import Fraction as Fr
import sys

# ---------- univariate over Fractions (or ints mod p) ----------
def padd(a, b):
    n = max(len(a), len(b)); r = [0]*n
    for i, c in enumerate(a): r[i] += c
    for i, c in enumerate(b): r[i] += c
    return trim(r)
def pneg(a): return [-c for c in a]
def psub(a, b): return padd(a, pneg(b))
def pmul(a, b):
    if not a or not b: return []
    r = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x == 0: continue
        for j, y in enumerate(b):
            r[i+j] += x*y
    return trim(r)
def pscale(a, s): return trim([c*s for c in a])
def trim(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    return a
def pcompose(a, b):           # a(b(z))
    r = []
    for c in reversed(a):
        r = padd(pmul(r, b), [c])
    return r
def pderiv(a): return trim([i*a[i] for i in range(1, len(a))])
def peval(a, x):
    r = 0
    for c in reversed(a): r = r*x + c
    return r
def ordz(a):
    for i, c in enumerate(a):
        if c != 0: return i
    return None
def pmod(a, p): return trim([c % p for c in a])
def z(): return [0, 1]

fails = 0
def report(name, ok, expect=True):
    global fails
    tag = "PASS" if ok == expect else "FAIL"
    if ok != expect: fails += 1
    print(f"[{tag}] {name}: observed={ok} expected={expect}")

# ---------- T1: identity (6) of Lemma 3.1 ----------
# f = z + c z^{k+1} + z^{k+2} r(z); g = (1+d^k) f; claim for z != 0:
# g' = 1 - k d^k + (1+d^k) z^{k+1}(r + z r') + (k+1)(g - z)/z
def identity6(k, c, r, d, k_coef=None, sign=-1):
    kc = k if k_coef is None else k_coef
    f = padd(padd(z(), [0]*(k+1) + [c]), pmul([0]*(k+2) + [1], r))
    s = 1 + d**k
    g = pscale(f, s)
    lhs = pderiv(g)
    quot = trim((psub(g, z()))[1:])                       # (g - z)/z, exact since g(0)=0
    term3 = pscale(pmul([0]*(k+1) + [1], padd(r, pmul(z(), pderiv(r)))), s)
    rhs = padd(padd([1 + sign*kc*d**k], term3), pscale(quot, k+1))
    return psub(lhs, rhs) == [], len(f) - 1

for (k, r) in [(1, [Fr(2), Fr(-3), Fr(5, 7)]), (2, [Fr(3, 2), Fr(-1)]), (3, [Fr(-4, 3)]), (1, [Fr(0)]), (2, [Fr(7)])]:
    c, d = Fr(3, 5), Fr(1, 3)
    ok, degf = identity6(k, c, r, d)
    report(f"T1 identity (6) k={k} deg f={degf}", ok)
    ok_neg, _ = identity6(k, c, r, d, k_coef=k+1)
    report(f"T1-neg identity (6) with -(k+1)d^k k={k}", ok_neg, expect=False)
    ok_sgn, _ = identity6(k, c, r, d, sign=+1)
    report(f"T1-neg identity (6) with +k d^k k={k}", ok_sgn, expect=False)

# ---------- T2: fixed-point equation (5) ----------
# g_d(d w) - d w == d^{k+1} w H(d, w), H = 1 + (1+d^k) c w^k + d (1+d^k) w^{k+1} r(d w), as bivariate polys
def badd(A, B):
    R = dict(A)
    for m, c in B.items(): R[m] = R.get(m, 0) + c
    return {m: c for m, c in R.items() if c != 0}
def bmul(A, B):
    R = {}
    for (i, j), x in A.items():
        for (k_, l), y in B.items():
            R[(i+k_, j+l)] = R.get((i+k_, j+l), 0) + x*y
    return {m: c for m, c in R.items() if c != 0}
def bscale(A, s): return {m: c*s for m, c in A.items() if c*s != 0}
def bpow(A, n):
    R = {(0, 0): Fr(1)}
    for _ in range(n): R = bmul(R, A)
    return R
D = {(1, 0): Fr(1)}; W = {(0, 1): Fr(1)}; ONE = {(0, 0): Fr(1)}
def eq5(k, c, r, mutate=False):
    zz = bmul(D, W)                                          # z = d w
    rz = {}
    for i, rc in enumerate(r): rz = badd(rz, bscale(bpow(zz, i), rc))
    f = badd(badd(zz, bscale(bpow(zz, k+1), c)), bmul(bpow(zz, k+2), rz))
    s = badd(ONE, bpow(D, k))                                # 1 + d^k
    lhs = badd(bmul(s, f), bscale(zz, Fr(-1)))               # g_d(z) - z
    rw = {}
    for i, rc in enumerate(r): rw = badd(rw, bscale(bpow(zz, i), rc))   # r(d w)
    H = badd(badd(ONE, bscale(bmul(s, bpow(W, k)), c)), bmul(bmul(bmul(D, s), bpow(W, k+1)), rw))
    if mutate: H = badd(H, bscale(bpow(W, k), c))            # wrong H: (2+d^k) c w^k
    rhs = bmul(bmul(bpow(D, k+1), W), H)
    return badd(lhs, bscale(rhs, Fr(-1))) == {}
for (k, r) in [(1, [Fr(2), Fr(-3)]), (2, [Fr(3, 2), Fr(-1)]), (3, [Fr(-4, 3)])]:
    report(f"T2 fixed-point equation (5) k={k}", eq5(k, Fr(3, 5), r))
    report(f"T2-neg (5) with mutated H k={k}", eq5(k, Fr(3, 5), r, mutate=True), expect=False)

# ---------- T3: Remark 4.1 sharpness, char 0 ----------
for dgr in range(2, 6):
    a = padd(z(), [0]*dgr + [Fr(1)]); b = padd(z(), [0]*dgr + [Fr(-1)])
    comp = psub(pcompose(a, b), z())
    o = ordz(comp)
    report(f"T3 ord_0(a∘b - z) = 2d-1 = {2*dgr-1}, leading -d, d={dgr}", o == 2*dgr-1 and comp[o] == -dgr)
    b2 = padd(z(), [0]*dgr + [Fr(1)])                        # changed object: b = z + z^d
    report(f"T3-neg with b = z + z^d gives ord {ordz(psub(pcompose(a, b2), z()))} = 2d-1, d={dgr}",
           ordz(psub(pcompose(a, b2), z())) == 2*dgr-1, expect=False)

# ---------- T4: Remark 4.3 positive characteristic ----------
for p in (2, 3, 5):
    a = padd(z(), [0]*p + [1]); b = padd(z(), [0]*p + [-1])
    comp = pmod(psub(pcompose(a, b), z()), p)
    target = pmod([0]*(p*p) + [-1], p)
    report(f"T4 char {p}: a∘b - z == -z^(p^2) mod p, ord {p*p} > 2p-1 = {2*p-1}", comp == target and ordz(comp) == p*p)
    comp0 = psub(pcompose(a, b), z())                         # same objects in char 0
    report(f"T4-ctrl char 0 same pair: ord = 2p-1 = {2*p-1} (bound attained, not exceeded)", ordz(comp0) == 2*p-1)

print("failures:", fails)
sys.exit(fails)
