#!/usr/bin/env python3
"""Tiny desk controls for the B+A-Hermite composition gate (stdlib only, exceptions not asserts)."""
import sys
from fractions import Fraction as Fr
from itertools import product

def require(cond, msg):
    if not cond:
        raise RuntimeError(msg)

MUT = sys.argv[1] if len(sys.argv) > 1 else None

# ---- 1. polygons (own half-planes), gamma-degree bound, envelope recount ----
def poly_pts(case, which):
    D, W = (15, 3) if which == 'A' else (25, 5)
    if case == 'common4':
        W = 9 if which == 'A' else 15
    pts = []
    for i in range(D + 1):
        for j in range(D + 1 - i):
            if case == 'unequal':
                ok = 5 * i - 7 * j <= W and (which != 'A' or 2 * j >= i)
            elif case == 'common3':
                ok = i - j <= W
            else:
                ok = i <= W
            if ok:
                pts.append((i, j))
    return pts

pivots = {'unequal': 192, 'common3': 210, 'common4': 265}
producer_high = {'unequal': 444, 'common3': 426, 'common4': 371}
tri = [(I, e - I) for e in range(39) for I in range(e + 1)]
require(len(tri) == 780, "triangle != 780")
for case in ('unequal', 'common3', 'common4'):
    A, B = poly_pts(case, 'A'), poly_pts(case, 'B')
    gA, gB = max(i for i, _ in A), max(i for i, _ in B)
    if MUT == 'gdeg':
        gA = 10
    require((gA, gB) == (9, 15), f"{case}: gamma degrees {gA},{gB} != 9,15")
    cut = gA + gB - 1  # Jacobian gamma-degree bound = 23
    env = [(I, J) for I, J in tri if I <= cut]
    low = sum(1 for I, J in env if I + J <= 13)
    mid = sum(1 for I, J in env if 14 <= I + J <= 37)
    top = sum(1 for I, J in env if I + J == 38)
    require((len(env), low, mid, top) == (660, 105, 531, 24), f"{case}: envelope {len(env)},{low},{mid},{top}")
    corrected = mid - pivots[case]
    require(producer_high[case] - corrected == 105, f"{case}: producer overcount != 105")
    # actual Minkowski support (pairs with ad != bc), unique slots, by degree band
    supp = set()
    for (a, b), (c, d) in product(A, B):
        if a * d != b * c:
            supp.add((a + c - 1, b + d - 1))
    require(all(I <= cut for I, J in supp), f"{case}: support exceeds gamma cut")
    require(max(I for I, J in supp) <= 22 or case == 'common4', f"{case}: I=23 slot present")
    m_low = sum(1 for I, J in supp if I + J <= 13)
    m_mid = sum(1 for I, J in supp if 14 <= I + J <= 37)
    m_top = sum(1 for I, J in supp if I + J == 38)
    print(f"{case}: gammaA={gA} gammaB={gB} cut={cut} env=660 (105/531/24) corrected_unselected={corrected} "
          f"producer={producer_high[case]} minkowski_support low/mid/top={m_low}/{m_mid}/{m_top}")

# ---- 2. beta shear: a_5,a_10 are A-Hermite pivots (graph values in R); inverse restores ----
apiv = {(i, s - i) for s in range(1, 15) for i in range(-(-s // 5))}
require(len(apiv) == 27, "A pivots != 27")
require((0, 5) in apiv and (0, 10) in apiv, "a5/a10 not A pivots")
require((0, 15) not in apiv, "(0,15) must be fixed A15 top, not a pivot")
# multivariate polys as dict {exponent tuple: Fr}; vars: b1 b2 b3 b4 g5 g10
V = ['b1', 'b2', 'b3', 'b4', 'g5', 'g10']
def var(n):
    e = [0] * 6; e[V.index(n)] = 1; return {tuple(e): Fr(1)}
def add(p, q, c=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + c * v
        if r[k] == 0: del r[k]
    return r
def mul(p, q):
    r = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(x + y for x, y in zip(k1, k2)); r[k] = r.get(k, 0) + v1 * v2
    return {k: v for k, v in r.items() if v != 0}
b = [var(n) for n in ('b1', 'b2', 'b3', 'b4')]
a = [var('g5'), var('g10'), {tuple([0] * 6): Fr(1)}, {}]  # a5,a10,a15=1,a20=0 (deg A = 15)
s = b[2]
shear = [add(b[r], mul(s, a[r]), -1) for r in range(4)]           # beta' = beta - s*a
require(shear[2] == {} and shear[3] == b[3], "beta3'!=0 or beta4' changed")
require(shear[0] == add(b[0], mul(s, var('g5')), -1), "beta1' wrong")
require(shear[1] == add(b[1], mul(s, var('g10')), -1), "beta2' wrong")
if MUT == 'inverse':
    s = {}
back = [add(shear[r], mul(s, a[r]), 1) for r in range(4)]         # inverse adds s*a with s = beta3 kept
require(back == b, "inverse does not restore beta")
print("beta shear: beta1'=b1-s*g5, beta2'=b2-s*g10, beta3'=0, beta4'=b4; inverse restores; a5,a10 in the 27 A pivots")

# ---- 3. lift control: P = t v^-1, Q = 0, s = 1 -> B-negative ideal (0) vs (t) unless t=0 imposed ----
# Laurent polys in v with coefficients polynomials in t: {(vexp, tpow): Fr}
P = {(-1, 1): Fr(1)}; Q = {}
Qp = add(Q, P, -1)  # Q' = Q - s*P, s=1
neg = lambda L: {k: v for k, v in L.items() if k[0] < 0}
rowsQ, rowsQp = neg(Q), neg(Qp)
require(rowsQ == {} and rowsQp == {(-1, 1): Fr(-1)}, "Q rows should be 0 and Q' rows should be -t")
require(rowsQ != rowsQp, "B-only lift invariance must FAIL before t=0")
modt = lambda L: {k: v for k, v in L.items() if k[1] == 0}
if MUT == 'lift':
    rowsQp = {}
require(modt(rowsQ) == modt(rowsQp) == {}, "mod (t) both must vanish")
require(rowsQp != {} , "mutation check")
print("lift control: negative ideal of Q is (0), of Q'=Q-P is (t); equal only modulo the A-negative row t=0")
print("ALL CONTROLS PASS")
