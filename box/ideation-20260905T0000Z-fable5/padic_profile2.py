#!/usr/bin/env python3
"""As padic_profile.py, but reports per (p, fibre) whether EVERY tail row has a
UNIQUE minimal-valuation term, and prints those terms (the p-adic initial
monomials).  Also reports the mod-p value of the normalizer scalar proxy: the
constant c = -yy*g is not in the file, so we report yy mod p only."""
import re, sys
from fractions import Fraction as Fr
import sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/ideation-20260905T0000Z-fable5")
from padic_profile import vp, roots_mod, hensel

def main(t, pmax, N=24, verbose=False):
    q = 2*t+1
    H = lambda y: 12*q*q*y*y - 12*q*(t+1)*y + (t+1)*(3*t+2)
    dH = lambda y: 24*q*q*y - 12*q*(t+1)
    path = f"/home/ubuntu/jc2/box/k16brcr-20260903/explicit_tail_t{t}_exact.txt"
    txt = open(path).read()
    names = ["b4"] + [f"q{j}_0" for j in range(2, t)] + ["b3"]
    syms = sp.symbols(names + ["yy"]); S = dict(zip(names + ["yy"], syms)); yy = S["yy"]
    rows = {}
    for m in re.finditer(r"^(T_\d+) = (.*?);\s*$", txt, re.M):
        P = sp.Poly(sp.expand(sp.sympify(m.group(2).replace("^", "**"), locals=S)), *[S[n] for n in names])
        rows[m.group(1)] = [(mon, sp.expand(c)) for mon, c in P.terms()]
    primes = [p for p in range(5, pmax) if all(p % d for d in range(2, int(p**0.5)+1))]
    print(f"t={t}: special numbers t+1={t+1} 2t+1={q} 3t+1={3*t+1} 3t+2={3*t+2} 4t+1={4*t+1} 3(t+1)={3*(t+1)}")
    for p in primes:
        rs = roots_mod(H, p)
        if len(rs) != 2: continue
        for r0 in rs:
            r = hensel(H, dH, r0, p, N)
            if r is None: continue
            uniq = True; report = []
            for k in sorted(rows, key=lambda s: -int(s[2:])):
                vals = []
                for mon, c in rows[k]:
                    a = c.coeff(yy, 1); b = c.coeff(yy, 0)
                    vals.append((vp(Fr(str(a))*r + Fr(str(b)), p, cap=N-2), mon))
                vmin = min(v for v, _ in vals); at = [mon for v, mon in vals if v == vmin]
                if len(at) != 1: uniq = False
                mons = ["*".join(f"{n}^{e}" for n, e in zip(names, mon) if e) for mon in at]
                report.append(f"{k}:vmin={vmin}:{'|'.join(mons) if len(at)<=3 else str(len(at))+'terms'}")
            if uniq or verbose:
                print(f"p={p} yy={r0} ALL-UNIQUE={uniq} :: " + "  ".join(report), flush=True)

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), verbose=(len(sys.argv) > 3))
