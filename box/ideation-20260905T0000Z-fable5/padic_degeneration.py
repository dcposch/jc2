#!/usr/bin/env python3
"""p-adic valuative degeneration test at p = 4t+1 (fibre where b_r,c_r are p-divisible).
With b3-weight lambda=1/2 the initial forms of the tail rows are
   u_r * b4^r * b3^2 + cbar_r(b4,q),   cbar_r = (c_r/p) mod p,  u_r = [b4^r]a_r mod p.
Eliminating Z=b3^2 gives D_r = u_0*cbar_r - u_r*b4^r*cbar_0 (r=1..t-1).
If V(D_1..D_{t-1}) = {0} over F_p-bar then V(initial forms)={0}, hence dim J_tail = 0
over the fibre (flat valuative degeneration; homogeneous ideal, Hilbert function preserved).
Emits a Singular script and runs it (dim, vdim)."""
import re, sys, subprocess
from fractions import Fraction as Fr
import sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/ideation-20260905T0000Z-fable5")
from padic_profile import vp, roots_mod, hensel

def modp(x, p):
    x = Fr(x); return (x.numerator % p) * pow(x.denominator % p, -1, p) % p

def main(t, p, N=30):
    q = 2*t+1
    H = lambda y: 12*q*q*y*y - 12*q*(t+1)*y + (t+1)*(3*t+2)
    dH = lambda y: 24*q*q*y - 12*q*(t+1)
    txt = open(f"/home/ubuntu/jc2/box/k16brcr-20260903/explicit_tail_t{t}_exact.txt").read()
    names = ["b4"] + [f"q{j}_0" for j in range(2, t)]
    syms = sp.symbols(names + ["yy"]); S = dict(zip(names + ["yy"], syms)); yy = S["yy"]
    parts = {}
    for m in re.finditer(r"^([abc]_\d+) = (.*?);\s*$", txt, re.M):
        e = sp.expand(sp.sympify(m.group(2).replace("^", "**"), locals=S))
        parts[m.group(1)] = [(mon, sp.expand(c)) for mon, c in sp.Poly(e, *[S[n] for n in names]).terms()] if e != 0 else []
    for r0 in roots_mod(H, p):
        r = hensel(H, dH, r0, p, N)
        # check the fibre: all b_r, c_r valuations >= 1 and a_r units with b4^r initial
        ok = True; cbar = {}; u = {}
        for rr in range(t):
            for part in "abc":
                vals = []
                for mon, c in parts[f"{part}_{rr}"]:
                    a = c.coeff(yy, 1); b = c.coeff(yy, 0); val = Fr(str(a))*r + Fr(str(b))
                    vals.append((vp(val, p, cap=N-2), mon, val))
                vmin = min(v for v, _, _ in vals)
                if part == "a":
                    if vmin != 0: ok = False
                    lead = [(mon, val) for v, mon, val in vals if v == 0]
                    if len(lead) != 1 or lead[0][0] != tuple([rr] + [0]*(t-2)): ok = False
                    else: u[rr] = modp(lead[0][1], p)
                else:
                    if vmin < 1: ok = False
                    if part == "c":
                        cbar[rr] = [(mon, modp(val / p, p)) for v, mon, val in vals if v == 1]
        if not ok:
            print(f"t={t} p={p} yy={r0}: fibre does NOT have the (a unit b4^r, b,c divisible) shape -> skip"); continue
        def poly(terms):
            return "+".join(f"{c}*" + "*".join(f"{n}^{e}" for n, e in zip(names, mon) if e) if any(mon) else f"{c}" for mon, c in terms) or "0"
        D = []
        for rr in range(1, t):
            D.append(f"{u[0]}*({poly(cbar[rr])}) - {u[rr]}*b4^{rr}*({poly(cbar[0])})")
        wts = ",".join(str(w) for w in [1] + list(range(2, t)))
        sing = f"ring R=({p}),({','.join(names)}),wp({wts});\n"
        sing += "".join(f"poly D{i+1}={d};\n" for i, d in enumerate(D))
        sing += f"ideal I={','.join('D'+str(i+1) for i in range(t-1))};\n"
        sing += "".join(f'print("size D{i+1}="+string(size(D{i+1}))+" deg="+string(deg(D{i+1})));\n' for i in range(t-1))
        sing += 'ideal G=std(I); print("dim="+string(dim(G))); if(dim(G)==0){print("vdim="+string(vdim(G)));}\n'
        sing += 'ideal C0=' + poly(cbar[0]) + '; print("cbar0 terms="+string(size(C0)));\nquit;\n'
        path = f"/home/ubuntu/jc2/box/ideation-20260905T0000Z-fable5/degen_t{t}_p{p}_y{r0}.sing"
        open(path, "w").write(sing)
        out = subprocess.run(["timeout", "120", "Singular", "-q", path], capture_output=True, text=True).stdout
        print(f"t={t} p={p} yy={r0} fibre OK; u={u}\n" + out.strip())

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
