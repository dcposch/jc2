#!/usr/bin/env python3
"""p-adic valuation profile of the exact K16 split-tail rows (t=3,4) at split primes.
Reads box/k16brcr-20260903/explicit_tail_t{t}_exact.txt (sealed 17(wwwww) artifact),
Hensel-lifts each root of H_t mod p, and reports for every row T_k the p-adic
valuations of its coefficients: min valuation, #terms at the min (= size of the
mod-p initial form at trivial weight), total #terms, and the valuations of the
pure-power monomials.  Desk-scale, read-only."""
import re, sys
from fractions import Fraction as Fr
import sympy as sp

def vp(x, p, cap=60):
    x = Fr(x)
    if x == 0: return cap
    v = 0; n, d = x.numerator, x.denominator
    while n % p == 0: n //= p; v += 1
    while d % p == 0: d //= p; v -= 1
    return v

def roots_mod(H, p):
    return [r for r in range(p) if H(r) % p == 0]

def hensel(H, dH, r, p, N):
    m = p
    for _ in range(N):
        m2 = m * p
        # r <- r - H(r)/H'(r) mod m2
        h = H(r) % m2; hd = dH(r) % p
        if hd == 0: return None
        inv = pow(hd, -1, p)
        r = (r - h * inv) % m2
        m = m2
    return r

def main(t, primes, N=24):
    q = 2*t+1
    H = lambda y: 12*q*q*y*y - 12*q*(t+1)*y + (t+1)*(3*t+2)
    dH = lambda y: 24*q*q*y - 12*q*(t+1)
    path = f"/home/ubuntu/jc2/box/k16brcr-20260903/explicit_tail_t{t}_exact.txt"
    txt = open(path).read()
    names = ["b4"] + [f"q{j}_0" for j in range(2, t)] + ["b3"]
    syms = sp.symbols(names + ["yy"])
    S = dict(zip(names + ["yy"], syms)); yy = S["yy"]
    rows = {}
    for m in re.finditer(r"^(T_\d+) = (.*?);\s*$", txt, re.M):
        expr = sp.sympify(m.group(2).replace("^", "**"), locals=S)
        P = sp.Poly(sp.expand(expr), *[S[n] for n in names])
        rows[m.group(1)] = P
    wts = {"b4": 1, **{f"q{j}_0": j for j in range(2, t)}, "b3": t+1}
    print(f"t={t} rows={sorted(rows)} vars={names} weights={[wts[n] for n in names]}")
    for p in primes:
        rs = roots_mod(H, p)
        if len(rs) != 2:
            print(f"p={p}: H_t has {len(rs)} root(s) mod p -> skipped"); continue
        for r0 in rs:
            r = hensel(H, dH, r0, p, N)
            if r is None: print(f"p={p} root {r0}: Hensel failed"); continue
            for k in sorted(rows, key=lambda s: -int(s[2:])):
                P = rows[k]; vals = []
                for mon, c in P.terms():
                    c = sp.expand(c)
                    a = c.coeff(yy, 1); b = c.coeff(yy, 0)
                    val = Fr(str(a)) * r + Fr(str(b))
                    # valuation of a*yy+b at the lifted root, capped by precision
                    v = vp(val, p, cap=N-2)
                    vals.append((v, mon))
                vmin = min(v for v, _ in vals)
                nmin = sum(1 for v, _ in vals if v == vmin)
                pure = {}
                for v, mon in vals:
                    nz = [i for i, e in enumerate(mon) if e]
                    if len(nz) == 1: pure[names[nz[0]]] = v
                hist = {}
                for v, _ in vals: hist[v] = hist.get(v, 0) + 1
                print(f"p={p} yy={r0:>3} {k}: terms={len(vals)} vmin={vmin} #atmin={nmin} pure={pure} hist={dict(sorted(hist.items()))}")

if __name__ == "__main__":
    t = int(sys.argv[1]); primes = [int(x) for x in sys.argv[2:]] or [5,7,11,13,17,19,23,29,31]
    main(t, primes)
