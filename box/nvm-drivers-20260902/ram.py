"""For each map: full boundary data + does the KELLER ledger (RAM' + campaign
   profile: H2, mu_l>=2, ceil(N/2)<=a<=N-2, W=N-a) admit a completion?"""
import sympy as sp, math, sys
from sympy import symbols
sys.path.insert(0,'/tmp/nvm')
from blowup import resolve
from synth import analyse_cluster
x, y = symbols('x y')

def full(name, P, Q, show=True):
    D, cl = resolve(P, Q, x, y)
    lab = [c['label'] for c in cl]; idx = {l:i for i,l in enumerate(lab)}
    pts = [(c['a'], ['L' if u=='L' else idx[u] for u in c['through']]) for c in cl]
    r = analyse_cluster(D, pts)
    N, kap, Lam, sat, sa = r['N'], r['kappa'], r['Lam'], r['sat'], r['suma']
    sols = []
    for n in range(1, Lam+1):
        if Lam % n: continue
        S = Lam//n
        for a in range(math.ceil(N/2), N-1):
            W = N-a
            if W < 2*S: continue
            if sa == 3*D - 2*N - kap + n*(W-S): sols.append((n,S,W,a))
    if show:
        print("%-18s D=%-3d N=%-2d kap=%-2d Lam=%-3d sat=%-3d suma=%-4d | RAM'+profile: %s"
              % (name, D, N, kap, Lam, sat, sa, sols if sols else "none"))
    return dict(D=D,N=N,kap=kap,Lam=Lam,sat=sat,suma=sa,sols=sols)

if __name__ == "__main__":
    print("=== monomial family (x, x^c y^Nn) ===")
    for Nn in range(1,9):
        for c in range(1,6):
            try: full("(x, x^%d y^%d)"%(c,Nn), x, x**c*y**Nn)
            except Exception as e: print("  exc", c, Nn, e)
