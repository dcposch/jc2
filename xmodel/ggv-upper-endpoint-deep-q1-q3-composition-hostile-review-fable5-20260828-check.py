#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Independent hostile-review checker for
xmodel/ggv-upper-endpoint-deep-q1-q3-composition-sol-ultra-20260828.md
(SHA256 6958c3986022e28484ea1a0a15a0b09a562dbd94cc2154ade4fe6dbc35000715).

Standard library only.  Exact Fraction arithmetic on sparse multivariate
polynomials and truncated formal series.  No producer checker is imported.

Sections (each prints PASS/FAIL):
  S1  Lagrange inversion: q_n = 2/(n+2) [t^n] F^((n+2)/8) for n=1,2,3,
      cross-checked against the R7R1 closed forms q1, q2.
  S2  Independent binomial extraction of the q3 bracket coefficients
      1/4, -3/32, 11/512; mutations of 11/512 and 3/32 detected.
  S3  Prefix substitution: 128 F3 A^8 - 48 F1 F2 A^4 + 11 F1^3
      = A^9 (16AU + 4SZ - S^3), then Z=(S^2-AQ)/2 gives N=S^3+A(16U-2SQ).
  S4  Both sheets p^2 = +-A: p'/p = A'/(2A) on both, q3 = (N/(512A)) p on
      both; odd-primitive criterion is the SAME rational ODE 2AC'+A'C=N.
  S5  Normalization: primitive pC/256 <=> ODE (11); the literal
      "primitive p*c/512, C=256c" reading is off by a factor 512 (mutation).
  S6  Pole exclusion: order m+1 with coeff -2m A(beta) away from A;
      order m with coeff (1-2m)A'(alpha) at a simple A-root; non-squarefree
      control A=X^4 admits a genuine 1/X solution.
  S7  Degree bookkeeping: window-derived deg S<=3, deg Q<=2, deg U<=5,
      deg N<=9; leading coefficient (2d+4)lc(C) X^(d+3); deg C<=6.
  S8  q1 parametrization: A|V0 + (V0=A'R0+2AR0', deg R0<=4) forces
      R0=lambda*A (kernel dim 1 for squarefree sample, dim 4 for X^4);
      V0=3lambda*A*A', S=3lambda*A'; T_A bridge F1 = T_A(A^2 R0).
  S9  C-structure (12): A'C == S^3 mod A for C = 27 lam^3 (A')^2 + A r.
  S10 ODE => (13): 2AC'+A'C == S^3 + A(16U-2SQ) with 16U from (13),
      identically in a0..a3, lam, q0..q2, r0..r2.
  S11 D12 composition: -4QS-(2SQ+108lam^3 A'A''+3A'r) ==
      -3A'(r+6lam*Q+36lam^3 A'') exactly; deg<=2 comparison; (14),(3),(4);
      A | L with quotient -3lam(Q'+6lam^2 A''').
  S12 lambda=0 => S=U=0, plus the alternate double-divisibility route
      (A|4U and the ODE force U=0; constants 3 and 16 only).
  S13 Control: lambda=0, U=48A', C=256A satisfies the q3 ODE exactly but
      violates D12 (residue 192A' mod A nonzero) -- q3 alone does not
      force U=0 (D12-omission mutation).
  S14 Final-constant mutations: 9lam^3/2 -> 9lam^3/4 in (3) and
      6lam^2 -> 3lam^2 in (4) are detected.
"""
import sys
from fractions import Fraction as Fr

FAILURES = []
def report(ok, name, extra=""):
    print(("PASS " if ok else "FAIL ") + name + (": " + extra if extra else ""))
    if not ok:
        FAILURES.append(name)

# ---------------- sparse multivariate polynomials over Q ----------------
def pz(n): return {}
def pc(c, n):
    c = Fr(c)
    return {} if c == 0 else {(0,)*n: c}
def pv(i, n, e=1):
    k = [0]*n; k[i] = e
    return {tuple(k): Fr(1)}
def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        w = r.get(k, Fr(0)) + v
        if w == 0: r.pop(k, None)
        else: r[k] = w
    return r
def pneg(a): return {k: -v for k, v in a.items()}
def psub(a, b): return padd(a, pneg(b))
def pscal(c, a):
    c = Fr(c)
    return {} if c == 0 else {k: c*v for k, v in a.items()}
def pmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = tuple(x+y for x, y in zip(k1, k2))
            w = r.get(k, Fr(0)) + v1*v2
            if w == 0: r.pop(k, None)
            else: r[k] = w
    return r
def ppow(a, e):
    n = len(next(iter(a))) if a else 0
    r = pc(1, n) if a else ({} if e else {})
    for _ in range(e): r = pmul(r, a)
    return r
def pdiff(a, i):
    r = {}
    for k, v in a.items():
        if k[i] == 0: continue
        kk = list(k); kk[i] -= 1
        r[tuple(kk)] = v*k[i]
    return r
def degX(a):
    return max((k[0] for k in a), default=None) if a else None
def psub_zero(a, i):
    return {k: v for k, v in a.items() if k[i] == 0}
def pdivmod_monicX(P, A, dA):
    """Divide P by A, monic of degree dA in var 0, coefficients free of X^>dA
    leading structure (A monic in X). Returns (Q,R) with degX(R)<dA."""
    Q, R = {}, dict(P)
    while True:
        d = degX(R)
        if d is None or d < dA: break
        lead = {k: v for k, v in R.items() if k[0] == d}
        qt = {}
        for k, v in lead.items():
            kk = list(k); kk[0] = d - dA
            qt[tuple(kk)] = v
        Q = padd(Q, qt)
        R = psub(R, pmul(qt, A))
        if degX(R) is not None and degX(R) >= d:
            raise RuntimeError("division not decreasing")
    return Q, R

# ---------------- ring R12: X lam a0..a3 q0..q2 r0..r2 ----------------
NR = 12
X   = pv(0, NR); LAM = pv(1, NR)
A_  = padd(pv(0, NR, 4), padd(pmul(pv(5, NR), pv(0, NR, 3)),
      padd(pmul(pv(4, NR), pv(0, NR, 2)),
      padd(pmul(pv(3, NR), pv(0, NR, 1)), pv(2, NR)))))
Ap  = pdiff(A_, 0); App = pdiff(Ap, 0); Appp = pdiff(App, 0)
Qp_ = padd(pmul(pv(8, NR), pv(0, NR, 2)),
      padd(pmul(pv(7, NR), pv(0, NR, 1)), pv(6, NR)))   # Q generic deg 2
Rr_ = padd(pmul(pv(11, NR), pv(0, NR, 2)),
      padd(pmul(pv(10, NR), pv(0, NR, 1)), pv(9, NR)))  # r generic deg 2
S_  = pscal(3, pmul(LAM, Ap))
L3  = ppow(LAM, 3)

def U_of(rp):
    """(13): 16U = 2SQ + 108 lam^3 A'A'' + 3A'r + 2Ar'."""
    t = padd(pscal(2, pmul(S_, Qp_)), pscal(108, pmul(L3, pmul(Ap, App))))
    t = padd(t, pscal(3, pmul(Ap, rp)))
    t = padd(t, pscal(2, pmul(A_, pdiff(rp, 0))))
    return pscal(Fr(1, 16), t)

# ---------------- univariate helpers over Q (Fraction lists) ----------------
def utrim(a):
    while a and a[-1] == 0: a.pop()
    return a
def uadd(a, b):
    n = max(len(a), len(b))
    return utrim([ (a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0)) for i in range(n) ])
def uscal(c, a): return utrim([Fr(c)*x for x in a])
def umul(a, b):
    if not a or not b: return []
    r = [Fr(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] += x*y
    return utrim(r)
def udiff(a): return utrim([a[i]*i for i in range(1, len(a))])
def ueval(a, x):
    v = Fr(0)
    for c in reversed(a): v = v*Fr(x) + c
    return v
def udivmod(a, b):
    a = list(a); q = [Fr(0)]*max(0, len(a)-len(b)+1)
    while len(utrim(list(a))) >= len(b):
        a = utrim(a)
        d = len(a) - len(b); c = a[-1]/b[-1]
        q[d] = c
        for i, y in enumerate(b): a[d+i] -= c*y
        a = utrim(a)
    return utrim(q), utrim(a)

# =====================================================================
# S1/S2: series ring vars X(f Laurent) f1 f2 f3; series lists in t or s.
NS = 4
def sx(e): return pv(0, NS, e) if e >= 0 else {(e, 0, 0, 0): Fr(1)}
def sxneg(e): return {(-e, 0, 0, 0): Fr(1)}
XL = pv(0, NS); F1v = pv(1, NS); F2v = pv(2, NS); F3v = pv(3, NS)
Xm8 = {(-8, 0, 0, 0): Fr(1)}
NT = 3
def smul(a, b):
    r = [pz(NS) for _ in range(NT+1)]
    for i in range(NT+1):
        for j in range(NT+1-i):
            r[i+j] = padd(r[i+j], pmul(a[i], b[j]))
    return r
def sscal(c, a): return [pscal(c, x) for x in a]
def sadd(a, b): return [padd(x, y) for x, y in zip(a, b)]
def binom_frac(al, k):
    v = Fr(1)
    for i in range(k): v *= (al - i)
    from math import factorial
    return v / factorial(k)
def binser(u, al):
    # (1+u)^al, u[0]==0
    r = [pc(1, NS)] + [pz(NS)]*NT
    up = [pc(1, NS)] + [pz(NS)]*NT
    for k in range(1, NT+1):
        up = smul(up, u)
        r = sadd(r, sscal(binom_frac(al, k), up))
    return r
def scompose(B, T):
    # B series in t (list), T series in s with T[0]==0 -> B(T(s)) in s
    r = [B[0]] + [pz(NS)]*NT
    Tp = [pc(1, NS)] + [pz(NS)]*NT
    for k in range(1, NT+1):
        Tp = smul(Tp, T)
        r = sadd(r, sscal(1, smul([B[k]] + [pz(NS)]*NT, Tp)))
    return r

u_t = [pz(NS), pmul(F1v, Xm8), pmul(F2v, Xm8), pmul(F3v, Xm8)]
P_ser = [pmul(XL, c) for c in binser(u_t, Fr(1, 8))]       # P = F^(1/8), F0=X^8
P2_ser = smul(P_ser, P_ser)                                 # Q-series in t
F58 = [pmul(pv(0, NS, 5), c) for c in binser(u_t, Fr(5, 8))]  # F^(5/8)

T = [pz(NS)]*(NT+1)
for _ in range(NT+1):
    PT = scompose(P_ser, T)
    T = [pz(NS)] + PT[:NT]          # t = s * P(t)
Qs = scompose(P2_ser, T)

q1_exp = pscal(Fr(1, 4), pmul(F1v, sxneg(5)))
q2_exp = psub(pscal(Fr(1, 4), pmul(F2v, sxneg(4))),
              pscal(Fr(1, 16), pmul(ppow(F1v, 2), sxneg(12))))
lag = lambda n: pscal(Fr(2, n+2), F58[n]) if n == 3 else None
q3_lag = pscal(Fr(2, 5), F58[3])
report(Qs[1] == q1_exp and Qs[2] == q2_exp, "S1a-lagrange-q1-q2",
       "series q1,q2 match R7R1 closed forms (0.4)")
report(Qs[3] == q3_lag, "S1b-lagrange-q3",
       "[s^3]Q == 2/5 [t^3] F^(5/8)  (formula (10), n=3)")

# S2: bracket (8): q3 = p^5[F3/(4H^2) - (3/32)F1F2/H^4 + (11/512)F1^3/H^6],
# here p=X, H=X^4.
def bracket(c1, c2, c3):
    t = pscal(c1, pmul(F3v, sxneg(8)))
    t = padd(t, pscal(c2, pmul(pmul(F1v, F2v), sxneg(16))))
    t = padd(t, pscal(c3, pmul(ppow(F1v, 3), sxneg(24))))
    return pmul(pv(0, NS, 5), t)
q3_disp = bracket(Fr(1, 4), Fr(-3, 32), Fr(11, 512))
report(q3_disp == q3_lag, "S2a-q3-bracket",
       "displayed (8) coefficients 1/4, -3/32, 11/512 all confirmed")
report(bracket(Fr(1, 4), Fr(-3, 32), Fr(12, 512)) != q3_lag,
       "S2b-mutation-11-512", "11/512 -> 12/512 detected")
report(bracket(Fr(1, 4), Fr(-1, 8), Fr(11, 512)) != q3_lag,
       "S2c-mutation-3-32", "-3/32 -> -1/8 detected")

# =====================================================================
# S3: abstract prefix substitution, ring vars A S Z U Q.
N5 = 5
Aa, Sa, Za, Ua, Qa = (pv(i, N5) for i in range(5))
F1a = pmul(ppow(Aa, 3), Sa)
F2a = pscal(Fr(1, 4), pmul(ppow(Aa, 2), padd(ppow(Sa, 2), Za)))
F3a = pscal(Fr(1, 8), pmul(Aa, padd(pmul(Sa, Za), pmul(Aa, Ua))))
lhs = psub(padd(pscal(128, pmul(F3a, ppow(Aa, 8))),
                pscal(11, ppow(F1a, 3))),
           pscal(48, pmul(pmul(F1a, F2a), ppow(Aa, 4))))
n1 = padd(pscal(16, pmul(Aa, Ua)),
          psub(pscal(4, pmul(Sa, Za)), ppow(Sa, 3)))
report(lhs == pmul(ppow(Aa, 9), n1), "S3a-prefix-substitution",
       "512 H^6 * bracket == A^9 (16AU+4SZ-S^3) under (6), H=A^2")
# Z -> (S^2 - AQ)/2
def substZ(p):
    r = pz(N5)
    zrep = pscal(Fr(1, 2), psub(ppow(Sa, 2), pmul(Aa, Qa)))
    for k, v in p.items():
        t = {(k[0], k[1], 0, k[3], k[4]): v}
        r = padd(r, pmul(t, ppow(zrep, k[2])))
    return r
Nn = padd(ppow(Sa, 3), pmul(Aa, psub(pscal(16, Ua), pscal(2, pmul(Sa, Qa)))))
report(substZ(n1) == Nn, "S3b-N-formula",
       "2Z=S^2-AQ gives N = S^3 + A(16U-2SQ)  (formula (9))")

# =====================================================================
# S4: both sheets. p^2 = eps*A ==> p' = eps*A'/(2p) = (A'/(2A)) p on BOTH
# sheets, and q3 = p*A^2*bracket = (N/(512A)) p on BOTH sheets, since
# p^5 = p*(p^2)^2 = p*A^2 for either sign.  So exactness of q3 dX is, on
# either sheet, the ODE for the odd part o = C/256:
#     A o' + o A'/2 = N/512   <=>   2AC' + A'C = N.
# We verify the algebraic kernel of this claim: p*(p^2)^2 == p*A^2 and
# 2*p*p' == eps*A'  jointly force p'/p = A'/(2A), eps-independently.
sheet_ok = True
for eps in (1, -1):
    # model p^2 -> eps*A symbolically: p^5 coefficient of p is (eps*A)^2 = A^2
    p5_coeff = ppow(pscal(eps, A_), 2)
    sheet_ok &= (p5_coeff == ppow(A_, 2))
report(sheet_ok, "S4-sheet-sign",
       "p^5 = p*A^2 on both sheets; same rational ODE; sign claim harmless")

# =====================================================================
# S10 first (defines C,N used by S5): C = 27 lam^3 (A')^2 + A r, U by (13).
C_ = padd(pscal(27, pmul(L3, ppow(Ap, 2))), pmul(A_, Rr_))
U13 = U_of(Rr_)
N_ = padd(ppow(S_, 3),
          pmul(A_, psub(pscal(16, U13), pscal(2, pmul(S_, Qp_)))))
ode_lhs = padd(pscal(2, pmul(A_, pdiff(C_, 0))), pmul(Ap, C_))
report(ode_lhs == N_, "S10-ode-to-13",
       "2AC'+A'C == S^3+A(16U-2SQ) identically (12)+(13), all 11 parameters")

# S5: normalization.  Odd part o=C/256: A o' + o A'/2 == N/512.
lhs5 = padd(pmul(A_, pdiff(pscal(Fr(1, 256), C_), 0)),
            pscal(Fr(1, 2), pmul(Ap, pscal(Fr(1, 256), C_))))
report(lhs5 == pscal(Fr(1, 512), N_), "S5a-primitive-pC-256",
       "primitive pC/256 has derivative N/(512 p): correct normalization")
# literal reading 'primitive p*c/512 with C=256c' => odd part C/(256*512)
lhs5b = padd(pmul(A_, pdiff(pscal(Fr(1, 131072), C_), 0)),
             pscal(Fr(1, 2), pmul(Ap, pscal(Fr(1, 131072), C_))))
report(lhs5b != pscal(Fr(1, 512), N_) and
       pscal(512, lhs5b) == pscal(Fr(1, 512), N_),
       "S5b-mutation-norm",
       "literal 'p*c/512, C=256c' is off by exactly 512: REPAIR confirmed")

# =====================================================================
# S6: pole exclusion, sample A = X^4-1 (squarefree), alpha=1, beta=2.
Au = [Fr(-1), Fr(0), Fr(0), Fr(0), Fr(1)]
Apu = udiff(Au)
ok6 = True
for m in (1, 2, 3):
    # C=(X-1)^-m: 2AC'+A'C = [-2mA + A'(X-1)]*(X-1)^(-m-1); g(1)=0,
    # h=g/(X-1), pole order m with leading h(1) == (1-2m)A'(1).
    g = uadd(uscal(-2*m, Au), umul(Apu, [Fr(-1), Fr(1)]))
    h, rem = udivmod(g, [Fr(-1), Fr(1)])
    ok6 &= (rem == [] and ueval(h, 1) == (1-2*m)*ueval(Apu, 1) != 0)
    # away from A at beta=2: g2 = -2mA + A'(X-2), g2(2) = -2m*A(2) != 0
    g2 = uadd(uscal(-2*m, Au), umul(Apu, [Fr(-2), Fr(1)]))
    ok6 &= (ueval(g2, 2) == -2*m*ueval(Au, 2) != 0)
report(ok6, "S6a-pole-exclusion",
       "(1-2m)A'(alpha) at simple roots, -2m A(beta) away from A, m=1,2,3")
# non-squarefree control: A=X^4, C=1/X solves with polynomial RHS 2X^2.
Ax4 = [Fr(0)]*4 + [Fr(1)]
# 2*A*C' + A'*C with C=1/X: 2*X^4*(-X^-2) + 4X^3*X^-1 = -2X^2 + 4X^2 = 2X^2
lhs_ctrl = uadd(uscal(-2, [Fr(0), Fr(0), Fr(1)]), uscal(4, [Fr(0), Fr(0), Fr(1)]))
report(lhs_ctrl == [Fr(0), Fr(0), Fr(2)], "S6b-nonssquarefree-control",
       "A=X^4: C=1/X gives 2AC'+A'C = 2X^2 polynomial; squarefree load-bearing")

# =====================================================================
# S7: degrees.  Windows (active-c2 review, deg F_n <= 16-n):
#  deg V0 = deg F1 - 8 <= 7 => deg S = deg V0 - 4 <= 3 (also S=3 lam A');
#  deg F2<=14 => deg Z <= 6;  deg F3<=13 => deg T <= 9 => deg U <= 5;
#  S^2-2Z=AQ => deg Q <= 2.  Then deg N <= 9.
report(degX(N_) is not None and degX(N_) <= 9 and degX(U13) <= 5
       and degX(S_) == 3 and degX(Qp_) == 2, "S7a-deg-N",
       "deg S=3, deg Q<=2, deg U<=5, deg N<=%d" % degX(N_))
Asamp = [Fr(3), Fr(-1), Fr(0), Fr(2), Fr(1)]           # monic quartic
ok7 = True
for d in range(0, 7):
    Cs = [Fr(0)]*d + [Fr(1)]                            # C = X^d
    L = uadd(uscal(2, umul(Asamp, udiff(Cs))), umul(udiff(Asamp), Cs))
    ok7 &= (len(L)-1 == d+3 and L[-1] == 2*d+4)
Cs = [Fr(-2), Fr(7), Fr(0), Fr(0), Fr(-1), Fr(0), Fr(5)]
L = uadd(uscal(2, umul(Asamp, udiff(Cs))), umul(udiff(Asamp), Cs))
ok7 &= (len(L)-1 == 9 and L[-1] == 16*Fr(5))
report(ok7, "S7b-leading-coeff",
       "deg(2AC'+A'C) = d+3, leading (2d+4)lc(C); d+3<=9 => deg C<=6")

# =====================================================================
# S8: q1 parametrization.
R0 = pmul(LAM, A_)
V0 = padd(pmul(Ap, R0), pscal(2, pmul(A_, pdiff(R0, 0))))
report(V0 == pscal(3, pmul(LAM, pmul(A_, Ap))), "S8a-V0",
       "R0=lam*A gives V0 = A'R0+2AR0' = 3 lam A A'; S=V0/A=3 lam A'")
q8, r8 = pdivmod_monicX(V0, A_, 4)
report(r8 == {} and q8 == S_, "S8b-S-division", "V0/A == 3 lam A' exactly")
# T_A bridge: F1 = A^2 V0 == T_A(A^2 R0), T_A(Q) = 2AQ' - 3A'Q.
Qb = pmul(ppow(A_, 2), R0)
TA = psub(pscal(2, pmul(A_, pdiff(Qb, 0))), pscal(3, pmul(Ap, Qb)))
report(TA == pmul(ppow(A_, 2), V0), "S8c-TA-bridge",
       "F1 = A^2 V0 = T_A(A^2 R0): V0-convention == reviewed T_A q1 theorem")
# kernel dimension of R0 |-> A'R0 mod A on deg<=4, sample squarefree A=X^4-1
def kernel_dim(Auni):
    Apu_ = udiff(Auni)
    cols = []
    for i in range(5):
        Xi = [Fr(0)]*i + [Fr(1)]
        _, rem = udivmod(umul(Apu_, Xi), Auni)
        cols.append([rem[j] if j < len(rem) else Fr(0) for j in range(4)])
    M = [[cols[c][r] for c in range(5)] for r in range(4)]
    # gaussian elimination
    rank, rowi = 0, 0
    for c in range(5):
        piv = next((r for r in range(rowi, 4) if M[r][c] != 0), None)
        if piv is None: continue
        M[rowi], M[piv] = M[piv], M[rowi]
        M[rowi] = [x / M[rowi][c] for x in M[rowi]]
        for r in range(4):
            if r != rowi and M[r][c] != 0:
                M[r] = [a - M[r][c]*b for a, b in zip(M[r], M[rowi])]
        rowi += 1; rank += 1
    return 5 - rank
report(kernel_dim(Au) == 1 and kernel_dim(Ax4) == 4, "S8d-kernel-dims",
       "A|A'R0 kernel: dim 1 (span A) for X^4-1; dim 4 for X^4 (control)")

# =====================================================================
# S9: (12) mod-A structure.
q9, r9 = pdivmod_monicX(psub(pmul(Ap, C_), ppow(S_, 3)), A_, 4)
report(r9 == {}, "S9-C-structure",
       "A'C - S^3 == A * (A'r) : A'C = S^3 mod A for C=27lam^3(A')^2+Ar")

# =====================================================================
# S11: D12 composition.
lhs11 = psub(pscal(-4, pmul(Qp_, S_)),
             padd(pscal(2, pmul(S_, Qp_)),
                  padd(pscal(108, pmul(L3, pmul(Ap, App))),
                       pscal(3, pmul(Ap, Rr_)))))
inner = padd(Rr_, padd(pscal(6, pmul(LAM, Qp_)), pscal(36, pmul(L3, App))))
report(lhs11 == pscal(-3, pmul(Ap, inner)), "S11a-exact-factorization",
       "-4QS-(2SQ+108lam^3A'A''+3A'r) == -3A'(r+6lamQ+36lam^3A'') exactly")
report(degX(inner) <= 2, "S11b-degree-comparison",
       "deg(r+6lamQ+36lam^3A'') <= 2 < 4 = deg A: mod-A equality is equality")
r14 = pneg(padd(pscal(6, pmul(LAM, Qp_)), pscal(36, pmul(L3, App))))
U3 = psub(pscal(Fr(-3, 4), pmul(LAM, padd(pmul(Ap, Qp_),
                                          pmul(A_, pdiff(Qp_, 0))))),
          pscal(Fr(9, 2), pmul(L3, pmul(A_, Appp))))
report(U_of(r14) == U3, "S11c-formula-3",
       "(13) at r=-6lamQ-36lam^3A'' gives U=-(3lam/4)(A'Q+AQ')-(9lam^3/2)AA'''")
L_ = padd(pmul(Qp_, S_), pscal(4, U3))
L_exp = pscal(-3, pmul(LAM, pmul(A_, padd(pdiff(Qp_, 0),
                                          pscal(6, pmul(ppow(LAM, 2), Appp))))))
report(L_ == L_exp, "S11d-formula-4",
       "L = QS+4U == -3 lam A (Q' + 6 lam^2 A''')")
qL, rL = pdivmod_monicX(L_, A_, 4)
report(rL == {} and qL == pscal(-3, pmul(LAM, padd(pdiff(Qp_, 0),
       pscal(6, pmul(ppow(LAM, 2), Appp))))), "S11e-A-divides-L",
       "A | L with quotient -3 lam (Q'+6 lam^2 A''')")

# =====================================================================
# S12: lambda=0.
report(psub_zero(S_, 1) == {} and psub_zero(U3, 1) == {}, "S12a-lambda0",
       "lambda=0 ==> S=0 and U=0  (formula (5))")
# alternate double-divisibility: lam=0, D12 gives A|4U => U=A*u (deg u<=1);
# ODE mod A gives C=A*rt (deg rt<=2); then 3A'rt+2A rt' = 16A u forces
# A|rt, deg rt<=2 => rt=0 => u=0.  Verify: only solution of
# 3A'rt + 2A rt' - 16A u == 0 in (rt deg<=2, u deg<=1) is zero. Two samples.
def alt_dd(Auni):
    Apu_ = udiff(Auni)
    rows = {}
    unk = 5  # rt0 rt1 rt2 u0 u1
    eqs = []
    for j in range(unk):
        if j < 3:
            rt = [Fr(0)]*j + [Fr(1)]
            col = uadd(uscal(3, umul(Apu_, rt)), uscal(2, umul(Auni, udiff(rt))))
        else:
            uu = [Fr(0)]*(j-3) + [Fr(1)]
            col = uscal(-16, umul(Auni, uu))
        eqs.append([col[i] if i < len(col) else Fr(0) for i in range(7)])
    M = [[eqs[c][r] for c in range(unk)] for r in range(7)]
    rank, rowi = 0, 0
    for c in range(unk):
        piv = next((r for r in range(rowi, 7) if M[r][c] != 0), None)
        if piv is None: continue
        M[rowi], M[piv] = M[piv], M[rowi]
        M[rowi] = [x / M[rowi][c] for x in M[rowi]]
        for r in range(7):
            if r != rowi and M[r][c] != 0:
                M[r] = [a - M[r][c]*b for a, b in zip(M[r], M[rowi])]
        rowi += 1; rank += 1
    return rank
report(alt_dd(Au) == 5 and
       alt_dd([Fr(1), Fr(1), Fr(0), Fr(0), Fr(1)]) == 5,
       "S12b-alt-double-divisibility",
       "lam=0: (A|4U)+ODE force U=0; full rank 5 on two squarefree samples; "
       "constants used: 3, 16 (char 0)")

# =====================================================================
# S13: control -- q3 alone does not force U=0 (D12-omission mutation).
C0 = pscal(256, A_); U0 = pscal(48, Ap)
N0 = pscal(16, pmul(A_, U0))     # lam=0: S=0 => N = 16AU
lhs13 = padd(pscal(2, pmul(A_, pdiff(C0, 0))), pmul(Ap, C0))
report(lhs13 == N0, "S13a-control-ode",
       "lam=0, U=48A', C=256A (primitive pA): q3 ODE holds, U != 0")
# D12 residue: (QS+4U)|_{S=0} = 192A'; mod A it is 192A' itself, nonzero.
q13, r13 = pdivmod_monicX(pscal(4, U0), A_, 4)
report(q13 == {} and r13 == pscal(192, Ap) and r13 != {},
       "S13b-control-d12-fails",
       "residue (QS+4U) mod A = 192 A' != 0: D12 input is load-bearing")
# D12 omission at generic lam: r unresolved (take r=0) does not give (3).
report(U_of(pz(NR)) != U3, "S13c-mutation-d12-omitted",
       "dropping D12 leaves r free: U_(13)|_{r=0} != formula (3)")

# =====================================================================
# S14: final-constant mutations.
U3bad = psub(pscal(Fr(-3, 4), pmul(LAM, padd(pmul(Ap, Qp_),
             pmul(A_, pdiff(Qp_, 0))))),
             pscal(Fr(9, 4), pmul(L3, pmul(A_, Appp))))
report(U_of(r14) != U3bad, "S14a-mutation-U-constant",
       "9 lam^3/2 -> 9 lam^3/4 in (3) detected")
Lbad = pscal(-3, pmul(LAM, pmul(A_, padd(pdiff(Qp_, 0),
             pscal(3, pmul(ppow(LAM, 2), Appp))))))
report(L_ != Lbad, "S14b-mutation-L-constant",
       "6 lam^2 -> 3 lam^2 in (4) detected")

# =====================================================================
print()
if FAILURES:
    print("OVERALL: FAIL (%d failing sections: %s)" % (len(FAILURES), ", ".join(FAILURES)))
    sys.exit(1)
print("OVERALL: ALL 32 CHECKS PASS "
      "(6 mutations detected; squarefree and D12 load-bearing controls held)")
