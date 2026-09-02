# Refined integrality proxies for EXACT-N.  pole = d(1-delta_1)/(d+e) per bottom-major g-root.
# V1: N = k * e*V2 * pole for some k in [1, floor(u/V2)]  (A_bot a multiple of a_1 = e V2, <= u e)
# V2 (loose): N = A * pole for some integer A in [1, u e]
# Each with N in Z and N >= 6 (column '>=6') and N in Z cap [6,16] (column '6..16').
import sys
sys.path.insert(0, "box")
import moh_skeleton_N as M
from math import gcd
from fractions import Fraction as F
nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 400
T = [0,0,0,0,0]; empt = {k: [] for k in ("V1ge6","V1w","V2ge6","V2w")}; withrows = []
print(f"{'D':>5} {'groups':>7} {'V1>=6':>6} {'V1 6..16':>8} {'V2>=6':>6} {'V2 6..16':>8}")
for n in range(48, nmax+1):
    rows = []
    for (m, Ms, _) in M.census(n, with_V=False):
        full = [-m]+list(Ms); s = len(full)
        dch = [n]
        for Mi in full: dch.append(gcd(dch[-1], Mi))
        ds = dch[s-1]
        for Vs in range(ds//2 + 1, ds):
            U, Sk = M.U_robust(n, m, list(Ms), Vs)
            if U is None: continue
            d, e, u, V2 = Sk.dd, Sk.e, Sk.u, Sk.V[2]
            pole = F(d*(1-Sk.delta[1]), d+e)
            a1 = e*V2
            v1 = [k*a1*pole for k in range(1, u//V2 + 1)]
            v1i = [x for x in v1 if x.denominator == 1 and x >= 6]
            v1w = [x for x in v1i if x <= 16]
            q = pole.denominator; p = pole.numerator
            # loose: A multiple of q, A <= u e
            kmax = (u*e)//q
            v2i = [p*k for k in range(1, kmax+1) if p*k >= 6]
            v2w = [x for x in v2i if x <= 16]
            rows.append((bool(v1i), bool(v1w), bool(v2i), bool(v2w)))
    if not rows: continue
    withrows.append(n)
    c = [sum(r[i] for r in rows) for i in range(4)]
    T[0] += len(rows)
    for i in range(4): T[i+1] += c[i]
    for key, ci in zip(("V1ge6","V1w","V2ge6","V2w"), c):
        if ci == 0: empt[key].append(n)
    if n in (105,108,112,117,120) or any(c):
        print(f"{n:5} {len(rows):7} {c[0]:6} {c[1]:8} {c[2]:6} {c[3]:8}")
print(f"TOTAL D<={nmax}: groups={T[0]}  V1>=6={T[1]}  V1[6,16]={T[2]}  V2>=6={T[3]}  V2[6,16]={T[4]}")
print(f"degrees with skeletons: {len(withrows)}")
for key in empt: print(f"emptied under {key}: {len(empt[key])} of {len(withrows)}; NOT emptied: {[n for n in withrows if n not in empt[key]][:40]}")
