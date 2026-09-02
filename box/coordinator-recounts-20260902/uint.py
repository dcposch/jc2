# Integrality PROXY for EXACT-N: assume A_bot = ue (N = U). Count per degree the
# branch-robust groups with U an integer in [6,16]; list degrees emptied.
import sys, time
sys.path.insert(0, "box")
import moh_skeleton_N as M
from math import gcd
from fractions import Fraction as F
nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 400
tot = surv = 0; empty = []; adm = {}
print(f"{'D':>5} {'groups':>8} {'U int':>6} {'U in[6,16]':>10} {'intU list'}")
for n in range(48, nmax+1):
    rows = []
    for (m, Ms, _) in M.census(n, with_V=False):
        full = [-m]+list(Ms); s = len(full)
        dch = [n]
        for Mi in full: dch.append(gcd(dch[-1], Mi))
        ds = dch[s-1]
        for Vs in range(ds//2 + 1, ds):
            U, S = M.U_robust(n, m, list(Ms), Vs)
            if U is None: continue
            rows.append((U, m, tuple(Ms), Vs))
    if not rows: continue
    ints = [r for r in rows if F(r[0]).denominator == 1]
    ok = [r for r in ints if 6 <= r[0] <= 16]
    tot += len(rows); surv += len(ok)
    if not ok: empty.append(n)
    if n in (105,108,112,117,120) or ok:
        print(f"{n:5} {len(rows):8} {len(ints):6} {len(ok):10} {sorted(set(int(r[0]) for r in ok))}")
print(f"TOTAL D<={nmax}: groups={tot} surviving(U int in [6,16])={surv}")
print(f"degrees D<={nmax} EMPTIED by the proxy: {len(empty)} of {nmax-47}; NOT emptied: {[n for n in range(48,nmax+1) if n not in empty and any(True for _ in [0])][:0]}")
ne = [n for n in range(48, nmax+1) if n not in empty]
print(f"degrees NOT emptied (first 60): {ne[:60]}")
print(f"admissible {[(d, d not in empty) for d in (105,108,112,117,120)]}")
