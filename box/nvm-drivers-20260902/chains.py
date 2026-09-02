"""Enumerate multi-chain clusters over L_infty (all base points free) and
   evaluate the Keller boundary ledger.  Root multiplicities sum to D
   (so E_0 is contracted, which N = sum m_C k_C forces once N < D)."""
import sys, math, itertools
sys.path.insert(0,'/tmp/nvm')
from synth import analyse_cluster

def chains_of(root, maxlen, maxpts):
    """non-increasing multiplicity chains starting at `root`."""
    out = [[root]]
    frontier = [[root]]
    while frontier:
        new = []
        for ch in frontier:
            if len(ch) >= maxlen: continue
            for nxt in range(1, ch[-1]+1):
                c = ch+[nxt]
                if len(c) <= maxpts:
                    new.append(c); out.append(c)
        frontier = new
    return out

def partitions(nn, maxpart, maxlen):
    if nn == 0: yield []; return
    if maxlen == 0: return
    for k in range(min(nn, maxpart), 0, -1):
        for rest in partitions(nn-k, k, maxlen-1):
            yield [k]+rest

def build(chs):
    pts, base = [], 0
    for ch in chs:
        for i, a in enumerate(ch):
            pts.append((a, ['L'] if i == 0 else [base+i-1]))
        base += len(ch)
    return pts

def scan(D, Ntarget, maxlen=6, maxroots=4, maxpts=14):
    hits = []
    for roots in partitions(D, D, maxroots):
        pools = [chains_of(rt, maxlen, maxpts) for rt in roots]
        for combo in itertools.product(*pools):
            tot = sum(len(c) for c in combo)
            if tot > maxpts: continue
            if sum(a*a for c in combo for a in c) != D*D - Ntarget: continue
            pts = build(list(combo))
            res = analyse_cluster(D, pts)
            if not res['ok'] or res['N'] != Ntarget: continue
            if res['Lam'] == 0 or res['kappa'] == 0: continue
            hits.append((res, [list(c) for c in combo]))
    return hits

def profiles(res):
    out = []
    N, Lam, kappa, suma, D = res['N'], res['Lam'], res['kappa'], res['suma'], res['D']
    for n in range(1, Lam+1):
        if Lam % n: continue
        S = Lam//n
        for a in range(math.ceil(N/2), N-1):
            W = N-a
            if W < 2*S: continue
            if suma == 3*D - 2*N - kappa + n*(W-S):
                out.append((n, S, W, a))
    return out

if __name__ == "__main__":
    Nt = int(sys.argv[1]); Dlo, Dhi = int(sys.argv[2]), int(sys.argv[3])
    for D in range(Dlo, Dhi+1):
        for res, combo in scan(D, Nt):
            ps = profiles(res)
            if ps:
                print("N=%d D=%-3d kappa=%-2d Lam=%-3d sat=%-2d suma=%-3d r=%-2d chains=%s -> (n,S,W,a)=%s"
                      % (Nt, D, res['kappa'], res['Lam'], res['sat'], res['suma'], res['r'], combo, ps))
