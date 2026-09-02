"""Randomised search over synthetic clusters: does the KELLER boundary ledger
   (I1,I2,BND,RAM',profile) admit fixed N with deg A_F -> infinity?"""
import random, sys, math
sys.path.insert(0,'/tmp/nvm')
from synth import analyse_cluster

def profile_ok(N, Lam, kappa, suma, D):
    """try to complete (n,S,W,a) so that RAM' and the campaign profile hold."""
    out = []
    for n in range(1, Lam+1):
        if Lam % n: continue
        S = Lam//n
        for a in range(math.ceil(N/2), N-1):
            W = N - a
            if W < 2*S: continue            # 7.B': mu_l >= 2  =>  W = sum s_l mu_l >= 2S
            if suma == 3*D - 2*N - kappa + n*(W-S):
                out.append((n, S, W, a))
    return out

def random_cluster(D, r, rng):
    pts = []
    for i in range(r):
        # choose parents: 'L' or an earlier E, possibly a satellite pair
        cands = ['L'] + list(range(i))
        if i == 0:
            par = ['L']
        else:
            if rng.random() < 0.45 and i >= 1:
                p2 = rng.sample(cands, 2)      # satellite (proximity 2)
                par = p2
            else:
                par = [rng.choice(cands)]
        a = rng.randint(1, D)
        pts.append((a, par))
    return pts

def run(Ntarget, trials=200000, seed=1):
    rng = random.Random(seed)
    best = {}
    for _ in range(trials):
        D = rng.randint(3, 26)
        r = rng.randint(2, 12)
        pts = random_cluster(D, r, rng)
        if sum(a*a for a, _ in pts) != D*D - Ntarget: continue
        try:
            res = analyse_cluster(D, pts)
        except Exception:
            continue
        if not res['ok'] or res['N'] != Ntarget or res['Lam'] == 0 or res['kappa'] == 0:
            continue
        sols = profile_ok(res['N'], res['Lam'], res['kappa'], res['suma'], res['D'])
        for (n, S, W, a) in sols:
            key = (n, S, W)
            if key not in best or res['D'] < best[key][0]:
                best[key] = (res['D'], res['kappa'], res['Lam'], res['sat'], res['r'],
                             tuple(x[0] for x in pts), tuple(tuple(x[1]) for x in pts))
    return best

if __name__ == "__main__":
    Nt = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    b = run(Nt, trials=int(sys.argv[2]) if len(sys.argv) > 2 else 120000)
    print("N =", Nt, " solutions found:", len(b))
    for (n, S, W), v in sorted(b.items()):
        print("   n=%-3d S=%d W=%d | D=%-3d kappa=%-2d Lam=%-3d sat=%-3d r=%-2d  a=%s"
              % (n, S, W, v[0], v[1], v[2], v[3], v[4], v[5]))
