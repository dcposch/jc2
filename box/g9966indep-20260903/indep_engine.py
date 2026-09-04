#!/usr/bin/env python3
"""Independent (99,66) joint-chart band engine, built from the design reports only.

Conventions are listed in CONVENTIONS below and in the lane report.
Never read: box/g9966band-20260903/band_engine.py (deliberately uncharged).
"""
import sys, json, argparse
from math import comb
from fractions import Fraction as Fr
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ring import *

NT = 9           # t-truncation (t-powers 0..NT-1 kept)

# ---------------- block supports ----------------
def slots(D, r0):  return [(r, q) for q in range(r0) for r in range(0, D - q + 1)]
H_SLOTS  = [(r + 1, q) for (r, q) in slots(10, 11)]        # K3 uses t^{r+1}
H_FREE   = [s for s in H_SLOTS if 3 * s[0] + 4 * s[1] >= 33]
K2_SLOTS = [(r, q) for q in range(33) for r in range(1, 34 - q)]
B1_SLOTS = [(r, q) for (r, q) in slots(32, 33) if 3 * r + 4 * q >= 93]

def hname(r, q): return 'Hc_%d_%d' % (r, q)
def kname(r, q): return 'K2c_%d_%d' % (r, q)
def bname(r, q): return 'B1c_%d_%d' % (r, q)

# ---------------- K3, K2 towers ----------------
def build_K3(NT=None):
    NT = globals()['NT'] if NT is None else NT
    S = [pzero() for _ in range(NT)]
    top = pmul(ppow({0: const(1), 1: const(1)}, 3), {8: const(1)})   # (1+V)^3 V^8
    S[0] = top
    for (r, q) in H_FREE:
        if r < NT: S[r] = padd(S[r], {q: var(hname(r, q))})
    return S

def tmul(A, B, N=None):
    N = len(A) if N is None else N
    C = [pzero() for _ in range(N)]
    for i, a in enumerate(A):
        if not a: continue
        for j in range(0, N - i):
            if B[j]: C[i + j] = padd(C[i + j], pmul(a, B[j]))
    return C

def build_K2(K3):
    NT = len(K3)
    """K2 = (K3^3)|_{q>=22} + sum_{q<=21} K2c_{a,q} V^q, with the D2 rule."""
    C3 = tmul(tmul(K3, K3), K3)
    S = [pzero() for _ in range(NT)]
    S[0] = C3[0]                                   # (1+V)^9 V^24, fixed top
    low_free, low_const, viol = [], [], []
    for a in range(1, NT):
        p = {q: c for q, c in C3[a].items() if q >= 22}
        for q, c in C3[a].items():
            if 3 * a + 4 * q < 96 and c: viol.append((a, q))  # must be empty
        for q in range(0, 22):
            if (a, q) not in K2_SLOTS: continue
            W = 3 * a + 4 * q
            if W < 96: continue
            if W == 96:
                k = a // 4
                assert a == 4 * k and q == 24 - 3 * k, (a, q)
                p[q] = const((-1) ** k * comb(8, k)); low_const.append((a, q))
            else:
                p[q] = var(kname(a, q)); low_free.append((a, q))
        S[a] = p
    return S, low_free, low_const, viol

def build_B1(NT=None):
    NT = globals()['NT'] if NT is None else NT
    S = [pzero() for _ in range(NT)]
    used = []
    for (r, q) in B1_SLOTS:
        if r < NT: S[r] = padd(S[r], {q: var(bname(r, q))}); used.append((r, q))
    return S, used

# ---------------- minor substitutions ----------------
class Branch:
    def __init__(self, name):
        self.name = name
        if name == 'delta2':
            self.tw = 1            # local variable = t
            self.X = {2: var('u'), 3: var('zeta')}     # w as series in t
            self.zvar, self.leadvar = 'zeta', 'rho'
            self.leadpow, self.leaddeg = 9, 3          # [t^9] K3 = zeta^2(zeta+3 rho)
        else:
            self.tw = 2            # t = s^2
            self.X = {4: var('u'), 6: var('vv'), 7: var('pi')}
            self.zvar, self.leadvar = 'pi', 'c'
            self.leadpow, self.leaddeg = 21, 3         # [s^21] K3 = pi(pi^2-c)

    def Xpow(self, i, M):
        """X^i truncated at local power M ; dict {power: ringelt}"""
        r = {0: const(1)}
        for _ in range(i):
            n = {}
            for p1, c1 in r.items():
                for p2, c2 in self.X.items():
                    if p1 + p2 <= M:
                        n[p1 + p2] = add(n.get(p1 + p2, {}), mul(c1, c2))
            r = {k: v for k, v in n.items() if v}
        return r

    def sub_series(self, S, M):
        """substitute w=1+V, V=X-1 into a t-series S ; return dict {localpow: ringelt}"""
        out = {}
        maxi = M // min(self.X)
        Xp = [self.Xpow(i, M) for i in range(maxi + 1)]
        for a, P in enumerate(S):
            base = a * self.tw
            if base > M or not P: continue
            for q, c in P.items():
                for i in range(0, min(q, maxi) + 1):
                    co = Fr((-1) ** (q - i) * comb(q, i))
                    if not co: continue
                    for p, cc in Xp[i].items():
                        m = base + p
                        if m > M: continue
                        t = smul(mul(c, cc), co)
                        if t: out[m] = add(out.get(m, {}), t)
        return {k: v for k, v in out.items() if v}

def split_z(poly, zvar):
    """split a ring element into coefficients of powers of the branch coordinate."""
    d = {}
    for m, c in poly.items():
        e = 0; rest = []
        for v, ex in m:
            if v == zvar: e = ex
            else: rest.append((v, ex))
        d.setdefault(e, {})
        mm = tuple(sorted(rest)); d[e][mm] = d[e].get(mm, Fr(0)) + c
    return {k: {m: c for m, c in v.items() if c} for k, v in d.items()}

# ---------------- Q* elimination ----------------
class Elim:
    """Exact eliminator: pivots only on variables with a nonzero RATIONAL coefficient.
       Never pivots on the localized branch parameters (rho / c) nor on nonlinear rows."""
    def __init__(self, forbidden):
        self.sub = {}          # var -> ring element
        self.forbidden = set(forbidden)
        self.pivots = []       # (label, var, coeff)
        self.residues = []     # (label, ring element)
        self.zero = 0
        self.rank_key = lambda v: v

    def reduce(self, p):
        changed = True
        while changed:
            changed = False
            for v in list(vars_of(p)):
                if v in self.sub:
                    p = subst(p, v, self.sub[v]); changed = True
        return p

    def feed(self, label, p):
        p = self.reduce(p)
        if is_zero(p): self.zero += 1; return 'zero'
        # look for a variable occurring linearly with rational (constant) coefficient
        cand = None
        for v in sorted(vars_of(p), key=self.rank_key):
            if v in self.forbidden: continue
            c = lin_coeff(p, v)
            if c:
                # confirm v occurs ONLY in that pure-linear monomial
                if all((v not in dict(m)) or m == ((v, 1),) for m in p):
                    cand = (v, c); break
        if cand is None:
            self.residues.append((label, p)); return 'residue'
        v, c = cand
        rest = {m: co for m, co in p.items() if m != ((v, 1),)}
        val = smul(rest, Fr(-1) / c)
        for k in list(self.sub):
            self.sub[k] = subst(self.sub[k], v, val)
        self.sub[v] = val
        self.pivots.append((label, v, str(c)))
        return 'pivot'

# ---------------- branch h3-leader reduction ----------------
def leader_rows(br, K3):
    """rows [t^m] K3(t,w(t)) = 0 for m < leadpow, and the leader normalisation."""
    M = br.leadpow
    ser = br.sub_series(K3, M)
    rows = []
    for m in range(0, M):
        for e, c in sorted(split_z(ser.get(m, {}), br.zvar).items()):
            rows.append(('h3_%s%d_%s^%d' % ('s' if br.tw == 2 else 't', m, br.zvar, e), c))
    lead = split_z(ser.get(M, {}), br.zvar)
    if br.name == 'delta2':      # target zeta^3 + 3*rho*zeta^2
        tgt = {3: const(1), 2: smul(var('rho'), 3), 1: {}, 0: {}}
    else:                        # target pi^3 - c*pi
        tgt = {3: const(1), 2: {}, 1: neg(var('c')), 0: {}}
    for e in sorted(set(lead) | set(tgt)):
        rows.append(('h3_lead_%s^%d' % (br.zvar, e),
                     sub(lead.get(e, {}), tgt.get(e, {}))))
    return rows

# ---------------- outer D1 rows (block-local) ----------------
def d1_rows_for(block, D, r0, d2b, d1b, namer):
    W0, T = int(3 * (D + d2b)), int(9 * (D + d1b))
    keep = [(r, q) for (r, q) in slots(D, r0) if 3 * r + 4 * q >= W0]
    byW = {}
    for (r, q) in keep: byW.setdefault(3 * r + 4 * q, []).append((r, q))
    rows = []
    for W in sorted(byW):
        if 3 * W >= T: continue
        for j in range(T - 3 * W):
            p = {}
            for (r, q) in byW[W]:
                if q >= j:
                    p = add(p, smul(var(namer(r, q)), comb(q, j)))
            rows.append((W - W0, '%s_D1_W%d_j%d' % (block, W, j), p))
    return rows

def h2_d1_rows(K2):
    """the seven h2 D1 rows below e^296 (weights 97,98)."""
    byW = {}
    for a in range(0, NT):
        for q, c in K2[a].items():
            byW.setdefault(3 * a + 4 * q, []).append((a, q, c))
    rows = []
    for W in sorted(byW):
        if 3 * W >= 296 or W < 97: continue
        for j in range(296 - 3 * W):
            p = {}
            for (a, q, c) in byW[W]:
                if q >= j: p = add(p, smul(c, comb(q, j)))
            rows.append(('h2_D1_W%d_j%d' % (W, j), p))
    return rows

# ---------------- KF, KG, KJ ----------------
def build_KFKG(K2, B1):
    NT = len(K2)
    KF = tmul(tmul(K2, K2), K2)                      # A2,A3 enter only at t^>=22
    KG = tmul(K2, K2)
    BA = tmul(B1, K2)
    for a in range(NT - 1, 0, -1): KG[a] = padd(KG[a], BA[a - 1])   # + t*B1*K2
    return KF, KG

def dt(S):
    """t * d/dt of a t-series"""
    return [psmul(S[a], a) for a in range(len(S))]

def build_KJ(KF, KG):
    NT = len(KF)
    KFv = [pdiff(p) for p in KF]; KGv = [pdiff(p) for p in KG]
    KFt = dt(KF); KGt = dt(KG)
    T1 = tmul(KF, KGv); T2 = tmul(KFt, KGv)
    T3 = tmul(KFv, KG); T4 = tmul(KFv, KGt)
    KJ = []
    for a in range(NT):
        p = padd(padd(psmul(T1[a], 99), psmul(T2[a], -1)),
                 padd(psmul(T3[a], -66), T4[a]))
        KJ.append(p)
    return KJ

def to_w(P):
    """convert a V-polynomial (V=w-1) to the w-monomial basis."""
    out = {}
    for q, c in P.items():
        for j in range(q + 1):
            co = Fr((-1) ** (q - j) * comb(q, j))
            t = smul(c, co)
            if t: out[j] = add(out.get(j, {}), t)
    return {k: v for k, v in out.items() if v}


def series_subst(S, sub):
    out = []
    for P in S:
        Q = {}
        for q, c in P.items():
            for v in list(vars_of(c)):
                if v in sub: c = subst(c, v, sub[v])
            if c: Q[q] = c
        out.append(Q)
    return out

def build_KJ_factored(KF, B1, K2):
    NT = len(KF)
    """KJ = t*A^3*(99*A*B_V - 96*B*A_V) + 3*t^2*A^3*(A_V*B_t - A_t*B_V),
       valid while KF=A^3 and KG=A^2+t*B*A (i.e. below the A2/A3/B2 onset t^22)."""
    A = K2; AV = [pdiff(p) for p in A]; At = dt(A)
    BV = [pdiff(p) for p in B1]; Bt = dt(B1)
    br1 = [padd(psmul(p, 99), psmul(q, -96))
           for p, q in zip(tmul(A, BV), tmul(B1, AV))]
    br2 = [padd(p, psmul(q, -1)) for p, q in zip(tmul(AV, Bt), tmul(At, BV))]
    P1 = tmul(KF, br1); P2 = tmul(KF, br2)
    KJ = [pzero() for _ in range(NT)]
    for a in range(NT):
        if a >= 1: KJ[a] = padd(KJ[a], P1[a - 1])
        if a >= 1: KJ[a] = padd(KJ[a], psmul(P2[a - 1], 3))  # P2 already carries one t
    return KJ
