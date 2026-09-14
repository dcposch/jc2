"""Exact-contact Xu calculus for the residual-66 roster.

Everything is exact rational arithmetic.  A "packet" is a set of roots of the
smaller polynomial (Xu's f, degree m) that still share a disc.  A packet is
described by (rho, kappa) where rho = #roots of f in it and
kappa = rho*(1 - delta_zero), delta_zero being the radius at which
ord f = ord g = 0 for that packet.

Printed sources (frozen charged copies):
  Xu Thm 5.1  I(f_xi,g) = I_M = (n/(n+m)) sum_{PM} |D^f_sigma| (1-delta_sigma)
  Xu Cor 5.3  I_M >= I_m = 1 + sum_{Pm}(delta_sigma - 1)
  Xu Lem 4.4  major => delta = lam^f+lam^g+1 < 1 ; minor => lam^f=lam^g=0, delta>1
  Xu sec.2    I(f,g) = deg_x Res_y(f,g)  ==> I_M is a NON-NEGATIVE INTEGER
  Moh Def 5.1 (1)(2)(3)(4) p.179 ; Prop 4.6 (1)-(5) p.170
"""
from fractions import Fraction as Q
from math import gcd
import json, itertools, sys

# ---------- tower arithmetic (Moh Def 5.1) ----------

def tower(src):
    n, m, s = src['n'], src['m'], src['s']
    M = {i+1: src['M'][i] for i in range(s)}
    d = {i+1: src['d'][i] for i in range(len(src['d']))}
    V = {i+2: src['V'][i] for i in range(len(src['V']))}
    V[s+1] = d[s+1]
    # Def 5.1(3)
    delta = {}
    for i in range(1, s+1):
        r = Q(n-M[i], n-M[s]-1)
        for j in range(i+1, s+1):
            r *= Q(V[j]*(n-M[j])-d[j], V[j]*(n-M[j-1])-d[j])
        delta[i] = 1 - r
    P = {i: Q(V[i+1]*d[i], d[i+1]) for i in range(1, s+1)}      # deg p  (Prop 4.6 v)
    Qd = {i: Q(V[i+1]*(n-M[i]), d[i+1]) for i in range(1, s+1)}  # deg q
    lo = {i: Q(d[i], n-M[i]) for i in range(1, s+1)}             # P/Q threshold
    A = {}
    for i in range(1, s+1):
        L = 1
        for j in range(i+1, s+1):
            L = L*delta[j].denominator // gcd(L, delta[j].denominator)
        A[i] = (L*delta[i]).denominator
    # rho_f(D_i) = (m/d_{i+1}) V_{i+1}   (Def 5.1(1) applied to T*_1, deg m)
    rho = {i: Q(m*V[i+1], d[i+1]) for i in range(1, s+1)}
    lam = {i: Q(m*(delta[i]-1), n-M[i]) for i in range(1, s+1)}  # Prop 4.6(2)(3)
    return dict(n=n, m=m, s=s, M=M, d=d, V=V, delta=delta, P=P, Qd=Qd,
                lo=lo, A=A, rho=rho, lam=lam)

# ---------- Moh Prop 4.6 pattern enumeration at one level ----------

def partitions(total, maxpart=None):
    if maxpart is None: maxpart = total
    if total == 0:
        yield ()
        return
    for k in range(min(total, maxpart), 0, -1):
        for rest in partitions(total-k, k):
            yield (k,)+rest

def patterns(Pdeg, Qdeg, A, Vsel, lo):
    """p = pi^z prod (pi^A - c_nu)^{r_nu}, deg p = Pdeg.
    Prop 4.6(3)(4): #distinct roots of p <= Qdeg (q squarefree, roots(p) in roots(q)).
    Def 5.1(2)/A.3: Vsel in {z} u {r}, no multiplicity == lo, some multiplicity > lo."""
    out = []
    Pdeg = int(Pdeg); Qdeg = int(Qdeg)
    for z in range(0, Pdeg+1):
        rest = Pdeg - z
        if rest % A: continue
        for part in partitions(rest//A) if rest else [()]:
            mults = ([z] if z > 0 else []) + list(part)
            if not mults: continue
            if Vsel not in mults: continue
            if any(Q(r) == lo for r in mults): continue
            if not any(Q(r) > lo for r in mults): continue
            ndistinct = (1 if z > 0 else 0) + A*len(part)
            if ndistinct > Qdeg: continue
            out.append(dict(z=z, orbits=tuple(part), ndistinct=ndistinct))
    return out

# ---------- packet calculus ----------

def Jfinal(n, m, rho, kappa):
    """I_M contribution of a major packet that goes final (Xu Thm 5.1 term)."""
    return Q(n*rho*kappa, (n+m)*rho - m)

def flat_config(T, chosen, selection):
    """chosen[i] = pattern at level i (i = s-1..2); level s forced by Prop 4.5.
    selection[i] = index into the level-i root-class list naming the class of
    multiplicity V_i that carries the tower (Def 5.1(4)/Prop 5.3).
    All other packets terminate immediately: no sibling sub-tower, no extra
    minor splitting.  Returns exact I_M, I_m and the leaf ledger."""
    n, m, s = T['n'], T['m'], T['s']
    d, V, delta, lam, A = T['d'], T['V'], T['delta'], T['lam'], T['A']
    IM = Q(0); Im_terms = []; leaves = []
    N = 1                              # conjugate copies of D_i on the tower
    for i in range(s, 1, -1):
        di, deli, lami = d[i], delta[i], lam[i]
        unit = Q(m, di)                # rho per unit multiplicity in p_i
        if i == s:
            classes = [('orbit', d[i]-V[i], 1), ('orbit', V[i], 1)]  # Prop 4.5
            sel_ix = 1
        else:
            pat = chosen[i]; Ai = A[i]
            classes = ([('zero', pat['z'], 1)] if pat['z'] > 0 else []) + \
                      [('orbit', r, Ai) for r in pat['orbits']]
            sel_ix = selection[i]
            if classes[sel_ix][1] != V[i]:
                return None
        for ix, (kind, r, copies) in enumerate(classes):
            rho = unit*r
            kappa = rho*(1-deli) + lami          # lam is negative
            if ix == sel_ix:
                sel = (rho, kappa, copies); continue
            if kappa < 0:
                Im_terms.append((N*copies, -kappa/rho))
                leaves.append(dict(level=i, kind='minor', mult=r, rho=rho,
                                   copies=N*copies, delta=1-kappa/rho))
            elif kappa > 0:
                j = Jfinal(n, m, rho, kappa)
                IM += N*copies*j
                leaves.append(dict(level=i, kind='major-sibling', mult=r, rho=rho,
                                   copies=N*copies, kappa=kappa, IM_each=j,
                                   delta=1-Q((n+m)*kappa, (n+m)*rho-m)))
            else:
                return None                      # multiplicity == lo: excluded
        rho, kappa, copies = sel
        if kappa <= 0:
            return None                          # tower branch must be major
        N = N*copies
        if i == 2:                               # its A_2 children ARE the D_1 discs
            j = Jfinal(n, m, rho, kappa)
            IM += N*j
            leaves.append(dict(level=1, kind='major-final', mult=V[2], rho=rho,
                               copies=N, kappa=kappa, IM_each=j,
                               delta=1-Q((n+m)*kappa, (n+m)*rho-m)))
    Im = Q(1) + sum(c*t for c, t in Im_terms)
    return dict(IM=IM, Im=Im, leaves=leaves)

def all_flat(T):
    """Every admissible (pattern, tower-selection) at levels s-1..2."""
    s = T['s']
    levels = list(range(s-1, 1, -1))
    opts = []
    for i in levels:
        p = patterns(T['P'][i], T['Qd'][i], T['A'][i], T['V'][i], T['lo'][i])
        cand = []
        for pat in p:
            nclass = (1 if pat['z'] > 0 else 0) + len(pat['orbits'])
            classes = ([pat['z']] if pat['z'] > 0 else []) + list(pat['orbits'])
            for ix in range(nclass):
                if classes[ix] == T['V'][i]:
                    cand.append((pat, ix))
        opts.append(cand)
    res = []
    for combo in itertools.product(*opts) if opts else [()]:
        chosen = {i: c[0] for i, c in zip(levels, combo)}
        selection = {i: c[1] for i, c in zip(levels, combo)}
        r = flat_config(T, chosen, selection)
        if r is None: continue
        r['pattern'] = {i: (c[0]['z'], c[0]['orbits'], c[1]) for i, c in zip(levels, combo)}
        res.append(r)
    # distinct patterns can give the same leaf ledger; keep all, dedupe by value
    seen = set(); out = []
    for r in res:
        key = (r['IM'], r['Im'], tuple(sorted((l['level'], l['kind'], l['mult'],
               l['rho'], l['copies']) for l in r['leaves'])))
        if key in seen: continue
        seen.add(key); out.append(r)
    return out

if __name__ == '__main__':
    rows = [json.loads(l) for l in open('/tmp/jc2-lane.69C0ak/inputs/roster.jsonl')]
    want = sys.argv[1:] or None
    print(f"{'row':6} {'n,m':10} {'s':2} {'pattern(level:z,orbits)':34} "
          f"{'I_M':>10} {'I_m':>10} {'margin':>10} {'IMint':5}")
    for row in rows:
        rid = row['row_id']
        if want and rid not in want: continue
        T = tower(row['source'])
        for r in all_flat(T):
            pat = ';'.join(f"{i}:z{z}/{list(o)}/s{ix}" for i, (z, o, ix) in sorted(r['pattern'].items()))
            mg = r['IM']-r['Im']
            print(f"{rid:6} {T['n']},{T['m']:<8} {T['s']:<2} {pat:34} "
                  f"{str(r['IM']):>10} {str(r['Im']):>10} {str(mg):>10} "
                  f"{'Y' if r['IM'].denominator==1 else 'N':5}")

def census(path='/tmp/jc2-lane.69C0ak/inputs/roster.jsonl'):
    out = []
    for row in (json.loads(l) for l in open(path)):
        T = tower(row['source'])
        cfgs = []
        for r in all_flat(T):
            cfgs.append(dict(pattern={str(i): [z, list(o), ix] for i, (z, o, ix)
                                      in r['pattern'].items()},
                             IM=str(r['IM']), Im=str(r['Im']),
                             margin=str(r['IM']-r['Im']),
                             IM_integral=(r['IM'].denominator == 1),
                             leaves=[{k: str(v) for k, v in L.items()} for L in r['leaves']]))
        out.append(dict(row_id=row['row_id'], n=T['n'], m=T['m'], s=T['s'],
                        d=[str(T['d'][i]) for i in sorted(T['d'])],
                        V={str(i): T['V'][i] for i in sorted(T['V'])},
                        delta=[str(T['delta'][i]) for i in sorted(T['delta'])],
                        A={str(i): T['A'][i] for i in sorted(T['A'])},
                        lo={str(i): str(T['lo'][i]) for i in sorted(T['lo'])},
                        P={str(i): str(T['P'][i]) for i in sorted(T['P'])},
                        Qd={str(i): str(T['Qd'][i]) for i in sorted(T['Qd'])},
                        configs=cfgs))
    return out
