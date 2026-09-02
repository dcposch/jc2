import sys; sys.path.insert(0,'/tmp/mfs')
from lib import *
from math import ceil

def beta_min_B2(N):
    if N <= 4: return None            # (B2) EMPTY for N<=4
    if N <= 10: return 2
    return 1                          # >=11 : beta>=1 (definition of B2)

def bounds(mults, deltas, MF):
    """mults: list of mult^min over singular points ; deltas: list of delta^min"""
    ms = sorted(mults, reverse=True)
    b1 = 1 + ms[0]
    b2 = ms[0] + ms[1] if len(ms) >= 2 else 0
    b3 = n_from_delta(sum(deltas))
    return max(MF, b1, b2, b3)

def cell(N, W, case):
    a = N - W
    Dgap = N - 2*W
    if W < 2 or Dgap < 0 or a < 1: return None
    best = None; bestcfg = None
    for dic in dicritical_sets(W):
        S = sum(s for s,mu in dic); L = len(dic); R = S - L
        has_s1 = any(s == 1 for s,mu in dic)
        d = W - S
        if d < 1: continue
        MF = -(-(N-1)//d)
        Kt = a - 1                                  # (K) sum K_p = a-1
        mlist = range(1, max(Kt,0)+1) if Kt > 0 else [0]
        for m in mlist:
            if Kt == 0 and m != 0: continue
            # per-case K ceiling
            if case in ('B1','B2'): maxK = Dgap
            else: maxK = a                          # B3: charge may sit on unibranch pts
            if maxK < 1 and Kt > 0: continue
            parts_iter = partitions_into(Kt, m, maxK) if Kt > 0 else [()]
            for K in parts_iter:
                mults = []; deltas = []
                if case == 'B1':
                    if m > R: continue
                    for k in K:
                        mu = max(2, 2 + -(-k//d)); mults.append(mu); deltas.append(mu*(mu-1)//2)
                    if len(mults) < 2: mults.append(2); deltas.append(1)   # s>=2 in case (B)
                    cfgs = [(mults, deltas)]
                elif case == 'B2':
                    bmin = beta_min_B2(N)
                    if bmin is None: continue
                    if has_s1:
                        if m < bmin: continue
                        beta = m; extra_sb = 0
                    else:
                        beta = max(bmin, m - R); extra_sb = max(0, beta - m)
                    for k in K:
                        mu = max(2, 2 + -(-k//d)); mults.append(mu)
                        deltas.append(max(mu*(mu-1)//2, 2))     # multibranch + singular branch
                    for _ in range(extra_sb):
                        mults.append(2); deltas.append(2)
                    while len(mults) < 2: mults.append(2); deltas.append(1)
                    cfgs = [(mults, deltas)]
                else:  # B3
                    if m > R + max(1, m): pass
                    cfgs = []
                    # (i) all charged points unibranch cusps + one extra node
                    A = []; DA = []
                    ok = True
                    for k in K:
                        if a - k < 0: ok = False
                        mu = max(2, 1 + -(-k//d)); A.append(mu); DA.append(mu*(mu-1)//2)
                    if ok:
                        A2 = A + [2]; D2 = DA + [1]                # the mandatory multibranch pt
                        if len(A) == 0: A2 = [2,2]; D2 = [1,1]
                        cfgs.append((A2, D2))
                    # (ii) smallest-charge point made multibranch (needs K<=Dgap, a-W-K>=0)
                    if K and K[-1] <= Dgap and a - W - K[-1] >= 0:
                        B = []; DB = []
                        for i,k in enumerate(K):
                            r = 2 if i == len(K)-1 else 1
                            mu = max(2, r + -(-k//d)); B.append(mu); DB.append(mu*(mu-1)//2)
                        if len(K) == 1:                            # still need a cusp
                            B.append(2); DB.append(1)
                        cfgs.append((B, DB))
                    if not cfgs: continue
                for (mu_l, de_l) in cfgs:
                    v = bounds(mu_l, de_l, MF)
                    if best is None or v < best:
                        best = v; bestcfg = (dic, S, d, MF, tuple(K), tuple(mu_l), sum(de_l))
    return best, bestcfg

if __name__ == '__main__':
    print("N   W  a  Dgap | banked  B1     B2     B3    | Phi  C=Phi-1")
    for N in range(4,21):
        for W in range(2, N//2 + 1):
            a = N-W; Dg = N-2*W
            banked = -(-(N-1)//(W-1))
            row = {}
            for case in ('B1','B2','B3'):
                if case=='B1' and N <= 16: row[case]=None; continue
                r = cell(N,W,case)
                row[case] = None if r is None else r[0]
            live = [v for v in row.values() if v is not None]
            Phi = min(live) if live else None
            f = lambda v: ('  -  ' if v is None else '%4d '%v)
            print("%2d %3d %2d %4d  | %5d  %s %s %s | %s %s" % (N,W,a,Dg,banked,
                  f(row['B1']),f(row['B2']),f(row['B3']),
                  ('  - ' if Phi is None else '%3d'%Phi),
                  ('  - ' if Phi is None else '%3d'%(Phi-1))))
        print()
