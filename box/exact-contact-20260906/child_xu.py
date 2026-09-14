"""ell-shifted exact contact for the OWN CHILD (Moh Prop 6.3: J = c*gamma^ell).

With J = x^ell, Xu Lemma 4.1 gives  d/dt terms = -t^{-ell-2}, so
  Lemma 4.4(i)  final major  <=>  delta = lam^f + lam^g + 1 + ell   (and delta < 1+ell)
  Lemma 4.4(ii) final minor  <=>  lam^f = lam^g = 0 and delta > 1+ell
  Moh Prop 4.6(3)* (p.171 Remark)  lam = (-1-ell+delta)/(n-M_r)
  Theorem 5.1     I_M = (n/(n+m)) sum_{PM} |D^f| (1+ell-delta)  = deg_x Res_y(f_xi,g) in Z
The packet formulas are unchanged with kappa := rho*((1+ell) - delta_zero):
  J_final = n*rho*kappa/((n+m)*rho - m),  minor leaf order - (1+ell) = -kappa/rho.
"""
from fractions import Fraction as Q
from math import gcd
import json, itertools, sys
sys.path.insert(0, 'box/exact-contact-20260906')
from exact_contact import patterns

def child_tower(oc, ell):
    n, m = oc['n_prime'], oc['m_prime']
    s = oc['s_prime']
    M = {i+1: oc['M_prime'][i] for i in range(s)}
    d = {i+1: oc['d_prime'][i] for i in range(len(oc['d_prime']))}
    V = {i+2: oc['V_prime'][i] for i in range(len(oc['V_prime']))}
    V[s+1] = d[s+1]
    delta = {}
    for i in range(1, s+1):
        r = Q(n-M[i], n-M[s]-1)
        for j in range(i+1, s+1):
            r *= Q(V[j]*(n-M[j])-d[j], V[j]*(n-M[j-1])-d[j])
        delta[i] = (ell+1)*(1-r)
    P = {i: Q(V[i+1]*d[i], d[i+1]) for i in range(1, s+1)}
    Qd = {i: Q(V[i+1]*(n-M[i]), d[i+1]) for i in range(1, s+1)}
    lo = {i: Q(d[i], n-M[i]) for i in range(1, s+1)}
    A = {}
    for i in range(1, s+1):
        L = 1
        for j in range(i+1, s+1):
            L = L*delta[j].denominator//gcd(L, delta[j].denominator)
        A[i] = (L*delta[i]).denominator
    lam = {i: Q(m*(delta[i]-1-ell), n-M[i]) for i in range(1, s+1)}
    return dict(n=n, m=m, s=s, M=M, d=d, V=V, delta=delta, P=P, Qd=Qd,
                lo=lo, A=A, lam=lam, ell=ell)

def evaluate(T, chosen, selection):
    n, m, s, ell = T['n'], T['m'], T['s'], T['ell']
    IM = Q(0); Imin = []; leaves = []; N = 1
    for i in range(s, 1, -1):
        di, deli, lami = T['d'][i], T['delta'][i], T['lam'][i]
        unit = Q(m, di)
        pat = chosen[i]; Ai = T['A'][i]
        classes = ([('zero', pat['z'], 1)] if pat['z'] > 0 else []) + \
                  [('orbit', r, Ai) for r in pat['orbits']]
        ix0 = selection[i]
        if classes[ix0][1] != T['V'][i]: return None
        for ix, (kind, r, copies) in enumerate(classes):
            rho = unit*r
            kappa = rho*(1+ell-deli) + lami
            if ix == ix0: sel = (rho, kappa, copies); continue
            if kappa < 0:
                Imin.append((N*copies, -kappa/rho))
                leaves.append(f"L{i} minor rho={rho} x{N*copies} delta={1+ell-kappa/rho}")
            elif kappa > 0:
                j = Q(n*rho*kappa, (n+m)*rho-m); IM += N*copies*j
                leaves.append(f"L{i} MAJOR-SIB rho={rho} x{N*copies} IMeach={j}")
            else: return None
        rho, kappa, copies = sel
        if kappa <= 0: return None
        N *= copies
        if i == 2:
            j = Q(n*rho*kappa, (n+m)*rho-m); IM += N*j
            leaves.append(f"L1 major-final rho={rho} x{N} IMeach={j} "
                          f"delta={1+ell-Q((n+m)*kappa,(n+m)*rho-m)}")
    return dict(IM=IM, minor=Imin, leaves=leaves)

if __name__ == '__main__':
    rows = {json.loads(l)['row_id']: json.loads(l)
            for l in open('/tmp/jc2-lane.69C0ak/inputs/roster.jsonl')}
    for rid in sys.argv[1:]:
        oc = rows[rid]['own_child']; ell = oc['ell']
        T = child_tower(oc, ell)
        print(f"\n=== {rid} own child  (n',m')=({T['n']},{T['m']}) s'={T['s']} ell={ell} "
              f"M'={list(T['M'].values())} d'={list(T['d'].values())} V'={T['V']}")
        print(f"    delta'={[str(v) for v in T['delta'].values()]}  (roster: "
              f"{oc['delta_prime']})  A'={T['A']} lo'={[str(v) for v in T['lo'].values()]} "
              f"P'={[str(v) for v in T['P'].values()]} Q'={[str(v) for v in T['Qd'].values()]}")
        levels = list(range(T['s'], 1, -1))
        opts = []
        for i in levels:
            cand = []
            for p in patterns(T['P'][i], T['Qd'][i], T['A'][i], T['V'][i], T['lo'][i]):
                cl = ([p['z']] if p['z'] > 0 else []) + list(p['orbits'])
                for ix, c in enumerate(cl):
                    if c == T['V'][i]: cand.append((p, ix))
            opts.append(cand)
        seen = set()
        for combo in itertools.product(*opts) if opts else [()]:
            ch = {i: c[0] for i, c in zip(levels, combo)}
            sl = {i: c[1] for i, c in zip(levels, combo)}
            r = evaluate(T, ch, sl)
            if r is None: continue
            key = (r['IM'], tuple(r['leaves']))
            if key in seen: continue
            seen.add(key)
            pat = {i: (c[0]['z'], c[0]['orbits'], c[1]) for i, c in zip(levels, combo)}
            print(f"  pat={pat}  I_M'={r['IM']}  integral={r['IM'].denominator==1}")
            for L in r['leaves']: print("      ", L)
            print("       minor packets (count, delta-(1+ell)):", r['minor'])
