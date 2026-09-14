"""Scope check: do the closed forms proved at s=3 extend to the 66 roster rows?"""
import json, sys
from fractions import Fraction as Q
from math import gcd, lcm
sys.path.insert(0, '/home/ubuntu/jc2')
from box.lib.descend_own import descend_own

class Skel:
    def __init__(s_, n, m, M, V):
        s_.n, s_.m, s_.s = n, m, len(M)
        s_.M = {i+1: v for i, v in enumerate(M)}
        s_.V = {i+2: v for i, v in enumerate(V)}

tot = {k: [0, 0] for k in ('mobius', 'affine', 'f51', 'A_eq_closed', 'A_div_moh',
                           'NM', 'PQ_ratio', 'PQ_copied', 'lo', 'lpp')}
def hit(k, ok): tot[k][0 if ok else 1] += 1
detail = []
for line in open('/home/ubuntu/jc2/box/residual65-20260905/roster.frozen.jsonl'):
    r = json.loads(line); src = r['source']
    n, m = src['n'], src['m']; M = src['M']; V = src['V']
    s = len(M); d = {1: n}; Md = {i+1: v for i, v in enumerate(M)}
    Vd = {i+2: v for i, v in enumerate(V)}
    for i in range(1, s+1): d[i+1] = gcd(d[i], Md[i])
    Vd[s+1] = d[s+1]
    delta = {}
    for i in range(1, s+1):
        rr = Q(n-Md[i], n-Md[s]-1)
        for j in range(i+1, s+1):
            rr *= Q(Vd[j]*(n-Md[j])-d[j], Vd[j]*(n-Md[j-1])-d[j])
        delta[i] = 1-rr
    ds, vs = d[s], Vd[s]; us, ell = ds-vs, 2*vs-ds-1; c = Q(us, ds)
    L = 1
    for i in range(2, s+1): L = lcm(L, delta[i].denominator)
    A1m = (L*delta[1]).denominator
    N, Mm = Q(n, d[2])*Vd[2], Q(m, d[2])*Vd[2]
    out = descend_own(Skel(n, m, M, V))
    np_, mp_, Mp, dp, sp = out['n'], out['m'], out['M'], out['d'], out['s']
    for i in range(1, s):   # threshold transport at every level, no V' needed
        hit('PQ_ratio', Q(d[i], n-Md[i]) == Q(out['raw_d'][i], np_-out['raw_M'][i]))
    for rad in out['child_radii']:
        j = rad['first_nonzero']; met = rad['delta']; e = delta[j]
        Vp = {i: rad['V'][i-2] for i in range(2, sp+1)}; Vp[sp+1] = dp[sp+1]
        f51 = {}
        for i in range(1, sp+1):
            rr = Q(np_-Mp[i], np_-Mp[sp]-1)
            for jj in range(i+1, sp+1):
                rr *= Q(Vp[jj]*(np_-Mp[jj])-dp[jj], Vp[jj]*(np_-Mp[jj-1])-dp[jj])
            f51[i] = (ell+1)*(1-rr)
        hit('f51', f51 == met)
        hit('mobius', all(met[i] == vs-Q(us)/delta[i] for i in range(j, sp+1)))
        hit('affine', all(met[i] == vs-us-Q(us)/e*(1-delta[i]) for i in range(1, j+1)))
        Lp = 1
        for i in range(2, sp+1): Lp = lcm(Lp, met[i].denominator)
        A1p = (Lp*met[1]).denominator
        closed = (Q(us, gcd(e.numerator, us))*e.denominator*delta[1]).denominator
        hit('A_eq_closed', A1p == closed); hit('A_div_moh', A1m % A1p == 0)
        hit('NM', Q(np_, dp[2])*Vp[2] == N and Q(mp_, dp[2])*Vp[2] == Mm)
        hit('lo', Q(dp[sp], np_-Mp[sp]) == Q(d[s-1], n-Md[s-1]))
        hit('lpp', dp[sp]-3-ell == (Q(d[s-1], ds)-ds if us == 1 else c*d[s-1]-ds+2*us-2))
        ok = True
        for i in range(2, sp):
            if Vp[i+1] == Vd[i+1]:
                ok &= (Q(Vp[i+1]*dp[i], dp[i+1]) == Q(Vd[i+1]*d[i], d[i+1]) and
                       Q(Vp[i+1]*(np_-Mp[i]), dp[i+1]) == Q(Vd[i+1]*(n-Md[i]), d[i+1]))
        hit('PQ_copied', ok)
        if A1p != closed or A1m % A1p:
            detail.append((r['row_id'], s, us, j, str(e), A1p, closed, A1m))
print("pass/fail over the 66 roster rows (all licensed routes):")
for k, (p, f) in tot.items(): print(f"  {k:12s} {p} pass / {f} fail")
print("exceptions:", detail if detail else "none")
