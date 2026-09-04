#!/usr/bin/env python3
"""Weighted CI Hilbert series of the terminal tail T_{t,t..2t-1}.

Identity verified here (exact integer coefficient-list arithmetic):

  P_t(s) := prod_{d=2t+2}^{3t+1}(1-s^d) / D_t(s),
  D_t(s)  = (1-s) prod_{j=2}^{t-1}(1-s^j) (1-s^{t+1})

  (I1) the division is exact;
  (I2) P_t(s) = (1+s^{t+1}) * [3t+1 choose t-1]_s     (Gaussian binomial);
  (I3) all coefficients of P_t are >= 0;
  (I4) deg P_t = (2t-1)(t+1);
  (I5) P_t(1) = 2*binom(3t+1,t-1) = 2*binom((2t+2)+(t-1), t-1);
  (I6) [s^n]P_t = #{(eps,m): eps in {0,1}, m in Z_{>=0}^{t-1}, |m|_1 <= 2t+2,
                             eps*(t+1) + sum_i i*m_i = n}.
"""
import sys
from math import comb

def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[i + j] += x * y
    return r

def oms(d):
    v = [0] * (d + 1); v[0] = 1; v[d] = -1; return v

def trim(v):
    v = list(v)
    while v and v[-1] == 0: v.pop()
    return v

def exact_div(a, b):
    """Exact polynomial division; returns (quotient, remainder-list)."""
    a = trim(a); b = trim(b)
    if not a: return [0], []
    if len(a) < len(b): return [0], a
    q = [0] * (len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        d = len(a) - len(b)
        if a[-1] % b[-1]: return None, a
        c = a[-1] // b[-1]
        q[d] = c
        for i, y in enumerate(b): a[d + i] -= c * y
        a = trim(a)
    return q, a

def gauss(n, k):
    num = [1]
    for i in range(1, k + 1): num = pmul(num, oms(n - k + i))
    den = [1]
    for i in range(1, k + 1): den = pmul(den, oms(i))
    q, rem = exact_div(num, den)
    assert q is not None and rem == [], (n, k)
    return q

def Pt(t):
    num = [1]
    for d in range(2 * t + 2, 3 * t + 2): num = pmul(num, oms(d))
    den = oms(1)
    for j in range(2, t): den = pmul(den, oms(j))
    den = pmul(den, oms(t + 1))
    return exact_div(num, den)

def model(t):
    D = 2 * t + 2
    top = (t - 1) * D + (t + 1)
    dp = [0] * (top + 1); dp[0] = 1                    # dp over unweighted degree budget
    # count monomials in weights 1..t-1 with total unweighted degree <= D, graded by weight
    cnt = [[0] * (top + 1) for _ in range(D + 1)]
    cnt[0][0] = 1
    for i in range(1, t):
        for k in range(1, D + 1):
            for w in range(i, top + 1):
                if cnt[k - 1][w - i]: cnt[k][w] += cnt[k - 1][w - i]
    base = [0] * (top + 1)
    for k in range(D + 1):
        for w in range(top + 1): base[w] += cnt[k][w]
    out = [0] * (top + 1)
    for w in range(top + 1):
        out[w] += base[w]
        if w + t + 1 <= top: out[w + t + 1] += base[w]
    return trim(out)

TMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24
print("  t | I1 exact | I2 gauss | I3 nonneg | I4 deg | I5 L_t | I6 model |      L_t")
allok = True
for t in range(2, TMAX + 1):
    q, rem = Pt(t)
    i1 = (q is not None and rem == [])
    q = trim(q)
    i2 = q == trim(pmul([1] + [0] * t + [1], gauss(3 * t + 1, t - 1)))
    i3 = all(c >= 0 for c in q)
    i4 = (len(q) - 1) == (2 * t - 1) * (t + 1)
    L = sum(q)
    i5 = (L == 2 * comb(3 * t + 1, t - 1) == 2 * comb(3 * t + 1, 2 * t + 2))
    i6 = (q == model(t)) if t <= 13 else None
    ok = i1 and i2 and i3 and i4 and i5 and (i6 is not False)
    allok &= bool(ok)
    print(f"{t:3d} |   {str(i1):5s}  |  {str(i2):5s}   |   {str(i3):5s}   |  {str(i4):5s} | {str(i5):5s}  |  {str(i6):5s}   | {L}")
print()
for t, m in [(3, 90), (4, 572), (5, 3640), (6, 23256), (7, 149226)]:
    v = 2 * comb(3 * t + 1, t - 1)
    print(f"  banked measured L_{t} = {m:8d}   2*C(3t+1,t-1) = {v:8d}   match={v == m}")
print()
print("P_3 =", trim(Pt(3)[0]))
print("P_4 =", trim(Pt(4)[0]))
print("L_8 =", 2 * comb(25, 7), "  L_9 =", 2 * comb(28, 8), "  L_10 =", 2 * comb(31, 9))
print()
print("ALL_IDENTITY_CHECKS_PASS =", allok)
