"""Modular p.150 characteristic-data engine (fast).

Identical recipe to chardata.py / fastchar.py, but arithmetic is in F_p with the
base variable specialised to b0 in F_p.  Soundness of the two directions:

  coefficient != 0 in F_p  ==>  f_i(base) != 0 over Q     (PROOF of support
                                membership, hence an upper bound on every M_j)
  coefficient == 0 for several independent (p, b0)  ==>  f_i == 0 (overwhelming)

A false zero can only make a computed M_j LARGER, i.e. it can only manufacture
the "M' = n'-1" reading, never destroy it -- so every REFUTING instance reported
(M' < n'-1) is unconditional once its support entry is exhibited nonzero, and is
re-run exactly with a symbolic base in exact.py.
"""
from math import gcd

def _inv(a, p):
    return pow(a % p, p - 2, p)

def _mul(A, B, N, p):
    C = [0] * (N + 1)
    for i, a in enumerate(A):
        if a == 0:
            continue
        lim = N - i
        for j, b in enumerate(B):
            if j > lim:
                break
            if b:
                C[i + j] = (C[i + j] + a * b) % p
    return C

def _pow_alpha(P, an, ad, N, p):
    """P = 1 + p1 T + ...; return P^(an/ad) mod T^{N+1} over F_p."""
    alpha = an % p * _inv(ad, p) % p
    q = [0] * (N + 1); q[0] = 1
    for j in range(1, N + 1):
        acc = 0
        for k in range(1, j + 1):
            if k < len(P) and P[k]:
                acc = (acc + (k * alpha - (j - k)) * P[k] % p * q[j - k]) % p
        q[j] = acc * _inv(j, p) % p
    return q

def _revert(A, N, p):
    """eta = T*A(T), A(0)=1.  Return C with T = eta*C(eta), C(0)=1 (Newton-free fixpoint)."""
    C = [0] * (N + 1); C[0] = 1
    for _ in range(N + 2):
        T = [0] * (N + 1)
        for i, c in enumerate(C):
            if i + 1 <= N:
                T[i + 1] = c
        acc = [0] * (N + 1); acc[0] = 1
        pw = [0] * (N + 1); pw[0] = 1
        for k in range(1, N + 1):
            pw = _mul(pw, T, N, p)
            if k < len(A) and A[k]:
                acc = [(u + A[k] * v) % p for u, v in zip(acc, pw)]
            if not any(pw):
                break
        new = _pow_alpha(acc, -1, 1, N, p)
        if new == C:
            break
        C = new
    return C

def support(gco, fco, N, p):
    n = len(gco) - 1
    while n > 0 and gco[n] == 0:
        n -= 1
    m = len(fco) - 1
    while m > 0 and fco[m] == 0:
        m -= 1
    li = _inv(gco[n], p)
    P = [0] * (N + 1); P[0] = 1
    for i in range(0, n):
        if gco[i] and n - i <= N:
            P[n - i] = gco[i] * li % p
    A = _pow_alpha(P, -1, n, N, p)
    C = _revert(A, N, p)
    Fs = [0] * (N + 1)
    for j in range(0, m + 1):
        if fco[j] and m - j <= N:
            Fs[m - j] = fco[j] % p
    T = [0] * (N + 1)
    for i, c in enumerate(C):
        if i + 1 <= N:
            T[i + 1] = c
    Fc = [0] * (N + 1); Fc[0] = Fs[0]
    pw = [0] * (N + 1); pw[0] = 1
    for k in range(1, N + 1):
        pw = _mul(pw, T, N, p)
        if Fs[k]:
            Fc = [(u + Fs[k] * v) % p for u, v in zip(Fc, pw)]
        if not any(pw):
            break
    Cm = _pow_alpha(C, -m, 1, N, p)
    D = _mul(Cm, Fc, N, p)
    return n, m, [-m + i for i, d in enumerate(D) if d], D

def chain(n, S, horizon):
    Ms, ds, d, trunc = [], [n], n, False
    while d != 1:
        cand = [i for i in S if i % d != 0]
        if not cand:
            Ms.append(None)
            break
        M = min(cand)
        Ms.append(M); d = gcd(d, abs(M)); ds.append(d)
        if M > horizon - 2:
            trunc = True
            break
    return Ms, ds, trunc

def chardata(poly_f, poly_g, param_is_y, b0, p, N=None):
    """poly_* : dict (i,j) -> int coeff of x^i y^j."""
    def coeffs(q):
        out = {}
        for (i, j), c in q.items():
            k = j if param_is_y else i
            b = i if param_is_y else j
            out[k] = (out.get(k, 0) + c * pow(b0, b, p)) % p
        return [out.get(k, 0) for k in range(max(out) + 1)] if out else [0]
    gco, fco = coeffs(poly_g), coeffs(poly_f)
    n = len(gco) - 1
    while n > 0 and gco[n] == 0:
        n -= 1
    m = len(fco) - 1
    while m > 0 and fco[m] == 0:
        m -= 1
    if N is None:
        N = n + m + 4                     # enough: every M_j is < n (Prop 5.1 range)
    n, m, S, D = support(gco, fco, N, p)
    Ms, ds, trunc = chain(n, S, -m + N)
    return dict(n=n, m=m, M=Ms, d=ds, support=S, truncated=trunc, horizon=-m + N)
