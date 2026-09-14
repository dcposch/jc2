"""Fast p.150 characteristic-data engine for a pair (f,g).

Moh 1983 p.150 (page image pg11-11.png), verbatim recipe:
   g = eta^{-n},  eta = g^{-1/n} = y^{-1} + alpha_2(x) y^{-2} + ... in k[x]((eta))
   f = eta^{-m} + sum_{j>-m} f_j(x) eta^j
   d_1 = n,  d_{j+1} = gcd(n, M_1,...,M_j),  M_j = min{i : f_i(x) != 0, d_j /| i},
   M_{h+1} = infinity.

`param` plays Moh's y and `base` plays Moh's x.  Swapping them gives the
"x-side" datum of the same pair.

Normalisation: g need not be monic in param; we use eta = (g/lc)^{-1/n}, which
rescales each f_j by a nonzero element of k(base) and therefore leaves the
support {j : f_j != 0} -- hence every M_j -- unchanged.

Speed: the base variable is specialised to a rational x0, so all series
arithmetic is over Q.  Specialising can only turn a nonzero f_i into zero on a
proper closed subset, so
    f_i(x0) != 0  ==>  f_i != 0                      (proof of support membership)
    f_i(x0) == 0  at several independent random x0    (overwhelming evidence)
Every verdict quoted in the report is re-run with a symbolic base in exact.py.
"""
from fractions import Fraction as F
from math import gcd


def _mul(A, B, N):
    C = [F(0)] * (N + 1)
    for i, a in enumerate(A):
        if a == 0:
            continue
        for j, b in enumerate(B):
            if i + j > N:
                break
            if b == 0:
                continue
            C[i + j] += a * b
    return C


def _pow_alpha(P, alpha, N):
    """P = 1 + p1 T + ... ; return P^alpha truncated at T^N."""
    q = [F(0)] * (N + 1)
    q[0] = F(1)
    for j in range(1, N + 1):
        acc = F(0)
        for k in range(1, j + 1):
            if k < len(P) and P[k] != 0:
                acc += (k * alpha - (j - k)) * P[k] * q[j - k]
        q[j] = acc / j
    return q


def _revert(A, N):
    """eta = T*A(T), A(0)=1.  Return C with T = eta*C(eta), C(0)=1."""
    C = [F(0)] * (N + 1)
    C[0] = F(1)
    for _ in range(N + 2):
        T = [F(0)] * (N + 1)
        for i, c in enumerate(C):
            if i + 1 <= N:
                T[i + 1] = c
        acc = [F(0)] * (N + 1)
        acc[0] = F(1)
        pw = [F(0)] * (N + 1)
        pw[0] = F(1)
        for k in range(1, N + 1):
            pw = _mul(pw, T, N)
            if k < len(A) and A[k] != 0:
                acc = [u + A[k] * v for u, v in zip(acc, pw)]
            if all(v == 0 for v in pw):
                break
        new = _pow_alpha(acc, -1, N)
        if new == C:
            break
        C = new
    return C


def support(gco, fco, N):
    """gco[i], fco[i] = coefficient of param^i.  Return (n, m, support of f)."""
    n = len(gco) - 1
    while n > 0 and gco[n] == 0:
        n -= 1
    m = len(fco) - 1
    while m > 0 and fco[m] == 0:
        m -= 1
    lc = gco[n]
    P = [F(0)] * (N + 1)
    P[0] = F(1)
    for i in range(0, n):
        if gco[i] != 0 and n - i <= N:
            P[n - i] = F(gco[i]) / lc
    A = _pow_alpha(P, F(-1, n), N)          # eta = T*A(T)
    C = _revert(A, N)                        # T = eta*C(eta)
    Fs = [F(0)] * (N + 1)
    for j in range(0, m + 1):
        if fco[j] != 0 and m - j <= N:
            Fs[m - j] = F(fco[j])
    T = [F(0)] * (N + 1)
    for i, c in enumerate(C):
        if i + 1 <= N:
            T[i + 1] = c
    Fc = [F(0)] * (N + 1)
    Fc[0] = Fs[0]
    pw = [F(0)] * (N + 1)
    pw[0] = F(1)
    for k in range(1, N + 1):
        pw = _mul(pw, T, N)
        if Fs[k] != 0:
            Fc = [u + Fs[k] * v for u, v in zip(Fc, pw)]
        if all(v == 0 for v in pw):
            break
    Cm = _pow_alpha(C, -m, N)
    D = _mul(Cm, Fc, N)
    return n, m, [-m + i for i, d in enumerate(D) if d != 0]


def chain(n, S, horizon):
    Ms, ds, d, trunc = [], [n], n, False
    while d != 1:
        cand = [i for i in S if i % d != 0]
        if not cand:
            Ms.append(None)                  # M_{h+1} = infinity : chain closed
            break
        M = min(cand)
        Ms.append(M)
        d = gcd(d, abs(M))
        ds.append(d)
        if M > horizon - 2:
            trunc = True
            break
    return Ms, ds, trunc


def chardata_poly(poly_f, poly_g, param_is_y, x0, N=None):
    """poly_* : dict (i,j) -> coefficient of x^i y^j.  param_is_y=True is Moh's y-side."""
    def coeffs(p):
        out = {}
        for (i, j), c in p.items():
            k = j if param_is_y else i
            b = i if param_is_y else j
            out[k] = out.get(k, F(0)) + F(c) * (F(x0) ** b)
        return [out.get(k, F(0)) for k in range(max(out) + 1)] if out else [F(0)]
    gco, fco = coeffs(poly_g), coeffs(poly_f)
    n = len(gco) - 1
    while n > 0 and gco[n] == 0:
        n -= 1
    if N is None:
        N = 3 * n + 12
    n, m, S = support(gco, fco, N)
    Ms, ds, trunc = chain(n, S, -m + N)
    return dict(n=n, m=m, M=Ms, d=ds, support=S[:60], truncated=trunc, horizon=-m + N)
