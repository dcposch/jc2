#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- part C', numerical: does the bottom star EXIST for a given
(d,e,V)?  Solves the square system

    Q monic of degree b = dV, q_{b-1} = 0 (translation), L(q) = 1 (a generic slice of the
    pi -> alpha pi scaling orbit);  the coefficients of pi^{-1},...,pi^{-(b-2)} of
    Q^{e/d} vanish   [b-2 equations]

by Newton from random complex starts at 60 digits, then VERIFIES the witness against the
defining conditions:  d Q P' - e P Q' constant and nonzero;  deg(Q^e - P^d) = V(de-d-e)+1;
Q, P, Q^e - P^d all squarefree (separated roots).   P := [Q^{e/d}]_{>=0}.
"""
import sys, random
from mpmath import mp, mpc, mpf, binomial, polyroots, fabs

mp.dps = 60

def series_pow(u, alpha, K):
    """(1+u)^alpha as a list of coefficients c[0..K] in s, u a list c[0..K] with u[0]=0."""
    out = [mpc(0)]*(K+1); out[0] = mpc(1)
    term = [mpc(0)]*(K+1); term[0] = mpc(1)          # u^k / running
    for k in range(1, K+1):
        # term <- term * u  (truncated)
        new = [mpc(0)]*(K+1)
        for i in range(K+1):
            if term[i] == 0: continue
            for j in range(1, K+1-i):
                if u[j] != 0: new[i+j] += term[i]*u[j]
        term = new
        if all(t == 0 for t in term): break
        cb = binomial(alpha, k)
        for i in range(K+1): out[i] += cb*term[i]
    return out

def build(q, d, e, V):
    """q = [q_0..q_{b-2}] (q_{b-1}=0).  Return (Pcoeffs desc, Qcoeffs desc, eqs)."""
    b, a = d*V, e*V
    Qc = [mpc(1)] + [mpc(0)] + [q[b-2-i] for i in range(b-1)]   # desc: pi^b ... pi^0
    K = a + b
    u = [mpc(0)]*(K+1)
    for j in range(1, b+1): u[j] = Qc[j]
    S = series_pow(u, mpf(e)/mpf(d), K)           # Q^{e/d} = pi^a * sum S[j] s^j
    Pc = [S[j] for j in range(0, a+1)]            # desc coefficients of P, degree a
    eqs = [S[a+j] for j in range(1, b-1)]         # coefficients of pi^{-1}..pi^{-(b-2)}
    return Pc, Qc, eqs

def polymul(A, B):
    C = [mpc(0)]*(len(A)+len(B)-1)
    for i,ai in enumerate(A):
        if ai == 0: continue
        for j,bj in enumerate(B): C[i+j] += ai*bj
    return C
def polyder(A):
    n = len(A)-1
    return [A[i]*(n-i) for i in range(n)] if n > 0 else [mpc(0)]
def polypow(A, k):
    R = [mpc(1)]
    for _ in range(k): R = polymul(R, A)
    return R
def polysub(A, B):
    n = max(len(A), len(B)); A = [mpc(0)]*(n-len(A))+list(A); B = [mpc(0)]*(n-len(B))+list(B)
    return [A[i]-B[i] for i in range(n)]
def trim(A, tol):
    i = 0
    while i < len(A)-1 and fabs(A[i]) < tol: i += 1
    return A[i:]

def kappa_of(Pc, Qc, d, e):
    W = polysub(polymul([mpc(d)], polymul(Qc, polyder(Pc))),
                polymul([mpc(e)], polymul(Pc, polyder(Qc))))
    return W[-1]

def solve_star(d, e, V, tries=80, seed=1):
    """Newton on the SQUARE system: the b-2 truncation equations plus kappa(q) = 1.
    Normalising kappa (which scales by alpha^{1-a-b} under pi -> alpha pi) both fixes the
    scaling orbit AND excludes the spurious component Q = R^d, P = R^e, on which kappa
    vanishes identically."""
    b = d*V
    rnd = random.Random(seed)
    def Fsys(q):
        b_, a_ = d*V, e*V
        Qc = [mpc(1)] + [mpc(0)] + [q[b_-2-i] for i in range(b_-1)]
        K = a_ + b_
        u = [mpc(0)]*(K+1)
        for j in range(1, b_+1): u[j] = Qc[j]
        S = series_pow(u, mpf(e)/mpf(d), K)
        # coefficients of pi^{-1}..pi^{-(b-2)} vanish, and the FIRST allowed one is 1
        return [S[a_+j] for j in range(1, b_-1)] + [S[a_+b_-1] - 1]
    for _ in range(tries):
        q = [mpc(rnd.uniform(-2,2), rnd.uniform(-2,2)) for _ in range(b-1)]
        ok = False
        for it in range(300):
            Fv = Fsys(q)
            nrm = max(fabs(zz) for zz in Fv)
            if nrm < mpf(10)**(-mp.dps+15): ok = True; break
            if nrm > mpf(10)**30: break
            h = mpf(10)**(-mp.dps//2)
            Jm = []
            for i in range(len(q)):
                q2 = list(q); q2[i] = q2[i] + h
                F2 = Fsys(q2)
                Jm.append([(F2[r]-Fv[r])/h for r in range(len(Fv))])
            nn = len(q)
            M = [[Jm[c][r] for c in range(nn)] + [-Fv[r]] for r in range(nn)]
            sing = False
            for c in range(nn):
                pv = max(range(c, nn), key=lambda r: fabs(M[r][c]))
                if fabs(M[pv][c]) < mpf(10)**(-mp.dps+5): sing = True; break
                M[c], M[pv] = M[pv], M[c]
                for r in range(nn):
                    if r == c: continue
                    fct = M[r][c]/M[c][c]
                    for k in range(c, nn+1): M[r][k] -= fct*M[c][k]
            if sing: break
            dq = [M[i][nn]/M[i][i] for i in range(nn)]
            q = [q[i]+dq[i] for i in range(nn)]
        if ok:
            Pc, Qc, eqs = build(q, d, e, V)
            if fabs(kappa_of(Pc, Qc, d, e)) > mpf(10)**(-15):
                return Pc, Qc, q
    return None, None, None

def verify(Pc, Qc, d, e, V, tol=None):
    if tol is None: tol = mpf(10)**(-mp.dps+20)
    a, b = e*V, d*V
    W = polysub(polymul([mpc(d)]+[mpc(0)]*0, polymul(Qc, polyder(Pc))),
                polymul([mpc(e)], polymul(Pc, polyder(Qc))))
    W = [mpc(d)*w for w in [mpc(0)]] if False else W
    scale = max(fabs(c) for c in W) if W else mpf(0)
    kap = W[-1]
    const = all(fabs(W[i]) < tol*max(mpf(1),scale) for i in range(len(W)-1))
    C = polysub(polypow(Qc, e), polypow(Pc, d))
    Ct = trim(C, tol*max(mpf(1), max(fabs(c) for c in C)))
    degC = len(Ct)-1
    def sep(A):
        if len(A) <= 2: return mpf(1)
        r = polyroots([complex(c) for c in A], maxsteps=200, extraprec=200)
        return min(abs(r[i]-r[j]) for i in range(len(r)) for j in range(i+1,len(r)))
    return const, kap, degC, V*(d*e-d-e)+1, sep(Pc), sep(Qc), sep(Ct)
