#!/usr/bin/env python3
"""Independent Newton-Puiseux radius measurement for constructed J=c gamma^k pairs.
Does not import control_pairs.py. Uses etaexp.char_data only for (M,d), not for radii.
"""
from fractions import Fraction as F
from math import gcd
import os, sys
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from etaexp import char_data
from gate_replay import closed, galois_test

mp.mp.dps = 80

def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        w = r.get(k, F(0)) + v
        if w:
            r[k] = w
        else:
            r.pop(k, None)
    return r

def pmul(a, b):
    r = {}
    for (i, j), u in a.items():
        for (p, q), v in b.items():
            k = (i + p, j + q)
            w = r.get(k, F(0)) + u * v
            if w:
                r[k] = w
            else:
                r.pop(k, None)
    return r

def pscal(a, c):
    c = F(c)
    return {} if c == 0 else {k: v * c for k, v in a.items()}

def deg(a):
    return max((i + j for (i, j) in a), default=-1)

def degpi(a):
    return max((j for (i, j) in a), default=-1)

def d_g(a):
    return {(i - 1, j): v * i for (i, j), v in a.items() if i}

def d_p(a):
    return {(i, j - 1): v * j for (i, j), v in a.items() if j}

def jac(a, b):
    return padd(pmul(d_g(a), d_p(b)), pscal(pmul(d_p(a), d_g(b)), -1))

def compose(cs, P):
    out = {}
    cur = {(0, 0): F(1)}
    for c in cs:
        if c:
            out = padd(out, pscal(cur, c))
        cur = pmul(cur, P)
    return out

def roots_at(a, X):
    d = degpi(a)
    co = [mp.mpf(0)] * (d + 1)
    for (i, j), v in a.items():
        co[d - j] += mp.mpf(v.numerator) / v.denominator * X ** i
    return mp.polyroots(co, maxsteps=200, extraprec=200)

def cluster(rs, cut):
    n = len(rs)
    par = list(range(n))
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for i in range(n):
        for j in range(i + 1, n):
            if abs(rs[i] - rs[j]) <= cut:
                a, b = find(i), find(j)
                if a != b:
                    par[a] = b
    g = {}
    for i in range(n):
        g.setdefault(find(i), []).append(i)
    return list(g.values())

def pairmin(idx, rs):
    return min(abs(rs[i] - rs[j]) for a, i in enumerate(idx) for j in idx[a + 1:]) if len(idx) > 1 else None

def pairmax(rs):
    return max(abs(rs[i] - rs[j]) for i in range(len(rs)) for j in range(i + 1, len(rs)))

def measure(Q, X1=mp.mpf("30"), X2=mp.mpf("10000")):
    R1, R2 = roots_at(Q, X1), roots_at(Q, X2)
    top1, top2 = pairmax(R1), pairmax(R2)
    d_top = -(mp.log(top2) - mp.log(top1)) / (mp.log(X2) - mp.log(X1))
    def sub(R):
        mn = min(abs(R[i] - R[j]) for i in range(len(R)) for j in range(i + 1, len(R)))
        cut = mp.sqrt(mn * pairmax(R))
        return cluster(R, cut)
    c1, c2 = sub(R1), sub(R2)
    b1, b2 = max(c1, key=len), max(c2, key=len)
    m1, m2 = pairmin(b1, R1), pairmin(b2, R2)
    d_in = None
    if m1 and m2:
        d_in = -(mp.log(m2) - mp.log(m1)) / (mp.log(X2) - mp.log(X1))
    return d_top, d_in, sorted(len(c) for c in c2)

def make_pair(phi_c, e, kk, psi_c, a):
    P = {(0, j): F(c) for j, c in enumerate(phi_c) if c}
    P = padd(P, {(kk + 1, 0): F(e)})
    Q = padd(compose([F(c) for c in psi_c], P), {(0, 1): F(a)})
    return P, Q

def run(label, phi_c, e, kk, psi_c, a):
    P, Q = make_pair(phi_c, e, kk, psi_c, a)
    J = jac(P, Q)
    mp_, np_ = degpi(P), degpi(Q)
    okgauge = (deg(P) == mp_ and deg(Q) == np_)
    okJ = (len(J) == 1 and (kk, 0) in J)
    Ms, ds, _ = char_data(P, mp_, Q, np_)
    d_top, d_in, sizes = measure(Q)
    d2 = gcd(np_, mp_)
    print("\n  %s" % label)
    print("    deg_pi(P,Q)=(%d,%d) gauge=%s J=%s monomial g^%d: %s"
          % (mp_, np_, okgauge, J, kk, okJ))
    print("    char M=%s d=%s s'=%d" % (Ms, ds, len(Ms)))
    print("    measured d_top=%s d_in=%s clusters=%s"
          % (mp.nstr(d_top, 8), mp.nstr(d_in, 8) if d_in is not None else "n/a", sizes))
    if not (okgauge and okJ):
        print("    *** gauge/J failure ***")
        return None
    if len(Ms) != 2:
        print("    s'!=2 skip")
        return None
    M2 = Ms[1]
    biggest = max(sizes)
    V2n = F(biggest * d2, np_)
    if V2n.denominator != 1:
        print("    non-integral V2' skip")
        return None
    V2 = int(V2n)
    cf = closed(np_, mp_, M2, V2, kk)
    ag = (abs(float(cf[0]) - float(d_top)) < 5e-3 and
          (d_in is None or abs(float(cf[1]) - float(d_in)) < 5e-3))
    r = galois_test(np_, mp_, M2, V2, kk, "delta2")
    rA = galois_test(np_, mp_, M2, V2, kk, "moh")
    print("    V2'=%d closed=%s measured-agree=%s" % (V2, cf, ag))
    print("    TEST 𝔄: %s  TEST A': %s" % (r["verdict"], rA["verdict"]))
    return dict(agree=ag, verdict=r["verdict"], verdictA=rA["verdict"],
                M2=M2, V2=V2, n=np_, m=mp_, k=kk, cf=cf)

if __name__ == "__main__":
    print("== Independent NP on constructed J=c gamma^k pairs (dps=%d) ==" % mp.mp.dps)
    cases = [
        # sharpness family A
        ("A k=1 q=2  P=pi^2-g^2 Q=P^2+pi (4,2)", [0, 0, 1], -1, 1, [0, 0, 1], 1),
        ("A k=2 q=2  P=pi^3-g^3 Q=P^2+pi (6,3)", [0, 0, 0, 1], -1, 2, [0, 0, 1], 1),
        ("A k=2 q=3  P=pi^3-g^3 Q=P^3+pi (9,3)", [0, 0, 0, 1], -1, 2, [0, 0, 0, 1], 1),
        ("A k=4 q=3  P=pi^5-g^5 Q=P^3+pi (15,5)", [0, 0, 0, 0, 0, 1], -1, 4, [0, 0, 0, 1], 1),
        # compositions B (m' > k+1)
        ("B k=1 m'=4 q=2 P=pi^4-g^2 Q=P^2+pi (8,4)", [0, 0, 0, 0, 1], -1, 1, [0, 0, 1], 1),
        ("B k=2 m'=6 q=2 P=pi^6-g^3 Q=P^2+pi (12,6)", [0, 0, 0, 0, 0, 0, 1], -1, 2, [0, 0, 1], 1),
        # lower terms
        ("C k=2 phi=pi^3+2pi psi=u^2+u a=3", [0, 2, 0, 1], -1, 2, [0, 1, 1], 3),
    ]
    res = []
    for c in cases:
        try:
            res.append((c[0], run(*c)))
        except Exception as ex:
            print("\n  %s\n    ERROR %s" % (c[0], ex))
            res.append((c[0], None))
    ok = [v for _, v in res if v is not None]
    print("\n== SUMMARY ==")
    print("  ran s'=2:", len(ok))
    print("  radii match closed form:", sum(1 for v in ok if v["agree"]), "/", len(ok))
    print("  killed by 𝔄:", sum(1 for v in ok if v["verdict"] == "KILLED"), "(must be 0)")
    print("  killed by A':", sum(1 for v in ok if v["verdictA"] == "KILLED"))
    for lab, v in res:
        if v:
            print("    %s  agree=%s  𝔄=%s  A'=%s  M2=%s V2=%s cf=%s"
                  % (lab, v["agree"], v["verdict"], v["verdictA"], v["M2"], v["V2"], v["cf"]))
