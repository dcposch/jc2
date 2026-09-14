#!/usr/bin/env python3
"""Valuation profile of the split coefficients a_r, b_r, c_r (b3^2, b3^1, b3^0 parts
of T_{2t-1-r}) at a prime p and each Hensel-lifted fibre.  Reports min valuation and
the initial monomials of each part.  Reads the sealed explicit_tail files."""
import re, sys
from fractions import Fraction as Fr
import sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/ideation-20260905T0000Z-fable5")
from padic_profile import vp, roots_mod, hensel

def main(t, primes, N=24):
    q = 2*t+1
    H = lambda y: 12*q*q*y*y - 12*q*(t+1)*y + (t+1)*(3*t+2)
    dH = lambda y: 24*q*q*y - 12*q*(t+1)
    txt = open(f"/home/ubuntu/jc2/box/k16brcr-20260903/explicit_tail_t{t}_exact.txt").read()
    names = ["b4"] + [f"q{j}_0" for j in range(2, t)]
    syms = sp.symbols(names + ["yy"]); S = dict(zip(names + ["yy"], syms)); yy = S["yy"]
    parts = {}
    for m in re.finditer(r"^([abc]_\d+) = (.*?);\s*$", txt, re.M):
        e = sp.expand(sp.sympify(m.group(2).replace("^", "**"), locals=S))
        P = sp.Poly(e, *[S[n] for n in names]) if e != 0 else None
        parts[m.group(1)] = [(mon, sp.expand(c)) for mon, c in P.terms()] if P is not None else []
    for p in primes:
        rs = roots_mod(H, p)
        if len(rs) != 2: print(f"t={t} p={p}: {len(rs)} roots -> skip"); continue
        for r0 in rs:
            r = hensel(H, dH, r0, p, N)
            if r is None: continue
            out = []
            for k in sorted(parts, key=lambda s: (int(s[2:]), s[0])):
                vals = []
                for mon, c in parts[k]:
                    a = c.coeff(yy, 1); b = c.coeff(yy, 0)
                    vals.append((vp(Fr(str(a))*r + Fr(str(b)), p, cap=N-2), mon))
                if not vals: out.append(f"{k}:0"); continue
                vmin = min(v for v, _ in vals); at = [mon for v, mon in vals if v == vmin]
                mons = ["*".join(f"{n}^{e}" for n, e in zip(names, mon) if e) or "1" for mon in at]
                out.append(f"{k}:v{vmin}:{'|'.join(mons) if len(at) <= 2 else str(len(at)) + 'terms'}")
            print(f"t={t} p={p} yy={r0} :: " + " ".join(out), flush=True)

if __name__ == "__main__":
    main(int(sys.argv[1]), [int(x) for x in sys.argv[2:]])
