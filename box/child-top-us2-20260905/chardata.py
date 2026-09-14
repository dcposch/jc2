"""p.150 characteristic-data engine for a pair (f,g).

Moh 1983 p.150 (image pg11-11.png):
   g = eta^{-n},  eta = g^{-1/n} = y^{-1}+alpha_2(x)y^{-2}+... in k[x]((eta))
   f = eta^{-m} + sum_{j>-m} f_j(x) eta^j
   d_1 = n, d_{j+1} = gcd(n,M_1,..,M_j), M_j = min{i : f_i(x)!=0, d_j /| i}, M_{h+1}=inf

Here `param` plays y and `base` plays x.  Setting param=x, base=y gives the
"x-side" datum.  Normalisation: g need not be monic in param; we use
eta = (g/lc)^{-1/n}, which rescales each f_j by a nonzero element of k(base)
and therefore leaves the support {j : f_j != 0} -- hence every M_j -- unchanged.
"""
import sympy as sp
from math import gcd

def _mul(A, B, N):
    C = [sp.S(0)]*(N+1)
    for i, a in enumerate(A):
        if a == 0: continue
        for j, b in enumerate(B):
            if i+j > N: break
            if b == 0: continue
            C[i+j] += a*b
    return [sp.cancel(c) for c in C]

def _pow_alpha(P, alpha, N):
    """P = 1 + p1 T + ... ; return P^alpha truncated at T^N."""
    q = [sp.S(0)]*(N+1); q[0] = sp.S(1)
    for j in range(1, N+1):
        acc = sp.S(0)
        for k in range(1, j+1):
            if k < len(P) and P[k] != 0:
                acc += (k*alpha - (j-k))*P[k]*q[j-k]
        q[j] = sp.cancel(acc/j)
    return q

def _revert(A, N):
    """eta = T*A(T), A(0)=1.  Return C with T = eta*C(eta), C(0)=1."""
    C = [sp.S(0)]*(N+1); C[0] = sp.S(1)
    for _ in range(N+1):
        # T = eta / A(T)  with T = eta*C(eta)
        # compose A at T = eta*C(eta):  A(T) = sum A_k T^k
        Tser = [sp.S(0)]*(N+2)          # coefficients of T in powers of eta, T = eta*C
        for i, c in enumerate(C):
            if i+1 <= N+1: Tser[i+1] = c
        acc = [sp.S(0)]*(N+1); acc[0] = sp.S(1)   # A(T) as series in eta
        pw = [sp.S(0)]*(N+1); pw[0] = sp.S(1)
        for k in range(1, N+1):
            pw = _mul(pw, Tser[:N+1], N)
            if k < len(A) and A[k] != 0:
                acc = [sp.cancel(x + A[k]*y) for x, y in zip(acc, pw)]
            if all(v == 0 for v in pw): break
        inv = _pow_alpha(acc, -1, N)
        newC = inv
        if newC == C: break
        C = newC
    return C

def series_of_pair(f, g, param, base, N):
    """Return (n, m, support-set S, list D) with f = eta^{-m} * sum_i D_i eta^i."""
    fp = sp.Poly(f, param); gp = sp.Poly(g, param)
    n = gp.degree(); m = fp.degree()
    assert n >= 1
    lc = gp.LC()
    # G/lc = 1 + sum_{i<n} (c_i/lc) T^{n-i}
    P = [sp.S(0)]*(N+1); P[0] = sp.S(1)
    for i in range(0, n):
        c = gp.coeff_monomial(param**i) if i > 0 else gp.coeff_monomial(1)
        if c != 0 and n-i <= N:
            P[n-i] = sp.cancel(sp.together(c/lc))
    A = _pow_alpha(P, sp.Rational(-1, n), N)          # eta = T*A(T)
    C = _revert(A, N)                                  # T = eta*C(eta)
    # F(T) = f * T^m = sum_j b_j T^{m-j}
    F = [sp.S(0)]*(N+1)
    for j in range(0, m+1):
        b = fp.coeff_monomial(param**j) if j > 0 else fp.coeff_monomial(1)
        if b != 0 and m-j <= N:
            F[m-j] = sp.cancel(b)
    # f = (eta*C)^{-m} * F(eta*C)  = eta^{-m} * [ C^{-m} * F(eta*C) ]
    Tser = [sp.S(0)]*(N+1)
    for i, c in enumerate(C):
        if i+1 <= N: Tser[i+1] = c
    Fc = [sp.S(0)]*(N+1); Fc[0] = F[0]
    pw = [sp.S(0)]*(N+1); pw[0] = sp.S(1)
    for k in range(1, N+1):
        pw = _mul(pw, Tser, N)
        if F[k] != 0:
            Fc = [sp.cancel(x + F[k]*y) for x, y in zip(Fc, pw)]
        if all(v == 0 for v in pw): break
    Cm = _pow_alpha(C, -m, N)
    D = _mul(Cm, Fc, N)
    D = [sp.cancel(sp.simplify(d)) for d in D]
    S = sorted(-m+i for i, d in enumerate(D) if d != 0)
    return n, m, S, D

def chardata(f, g, param, base, N=None):
    gp = sp.Poly(g, param); n = gp.degree()
    if N is None: N = 3*n + 8
    n, m, S, D = series_of_pair(f, g, param, base, N)
    Ms, ds = [], [n]
    d = n
    horizon = -m + N
    while d != 1:
        cand = [i for i in S if i % d != 0]
        if not cand:
            Ms.append(None); break                      # chain closed: M = infinity
        M = min(cand)
        Ms.append(M); d = gcd(d, abs(M)); ds.append(d)
        if M > horizon - 2:
            Ms.append('TRUNCATION-RISK'); break
    return dict(n=n, m=m, M=Ms, d=ds, support=S[:40], horizon=horizon)
