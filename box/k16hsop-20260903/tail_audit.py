#!/usr/bin/env python3
"""Structural audit of the terminal tail, on top of tail_structure.build().

Checks, for the index t given on the command line:
  A. a_0 = [b3^2]T_{t,2t-1} equals -alpha_t from the charged closed form (3.3);
  B. norms Res_y(H_t, .) of a_0 and of mu_t (=a_1/b4) against the charged tables;
  C. deg_b3 of the tail rows, and the variable support / weight of every a_r;
  D. LINEARISATION: G_r := a_0*T_{t,2t-1-r} - a_r*T_{t,2t-1} is b3-LINEAR, of
     weighted degree 2t+2+r, so J^tail = (Q_0, G_1..G_{t-1}) with Q_0 unit-quadratic;
  E. the wp-leader test: mu_{t,k} = [b4^{4t+1-k}]T_{t,k} (sol56 Sec.6 (6.1));
  F. the (t-1)x2 coefficient matrix N = (C_r | B_r) and its 2x2 minors.
Outputs a JSON with all rows as strings for reuse.
"""
import sys, json, time
import sympy as sp
sys.path.insert(0, '/home/ubuntu/jc2/box/k16hsop-20260903')
from tail_structure import build

t = int(sys.argv[1])
t0 = time.time()
D = build(t, verbose=False)
y, T, wt, resid, b3, b4, red = D['y'], D['T'], D['wt'], D['resid'], D['b3'], D['b4'], D['red']
u = D['u']
q = 2 * t + 1
print(f"=== t={t}  build {time.time()-t0:.1f}s ===", flush=True)

Hpoly = sp.Poly(D['H'], y)
def norm(scalar):
    """Res_y(H_t, scalar) for a scalar in A_t (deg_y<=1)."""
    s = sp.together(sp.simplify(scalar))
    return sp.simplify(sp.resultant(sp.Poly(sp.numer(s), y), Hpoly) / sp.denom(s)**2)

# ---------- A: alpha_t closed form -------------------------------------
d = D['d']
Ab = 27*t**3 - 30*t**2 + t - 2
Bb = 6*t**3 + 13*t**2 - 3*t + 2
alpha = sp.Rational(t*(3*t+1), 1) * (Ab*d + Bb) / (12*q**2*(3*t-1)**2*(3*t+2))
alpha = red(sp.expand(alpha))
Q0 = T[2*t-1]
a0 = red(sp.Poly(sp.expand(Q0), b3).nth(2))
print("A. a_0 + alpha_t  =", sp.simplify(a0 + alpha), "   (0 <=> a_0 = -alpha_t)", flush=True)
print("   a_0 =", sp.factor(sp.simplify(a0)))
print("   Res_y(H_t, a_0) =", norm(a0), "  (nonzero <=> unit)", flush=True)

# ---------- C/D: tail structure ----------------------------------------
rows = {}
avec = {}
print("\nC. tail rows T_{t,2t-1-r}:", flush=True)
for r in range(t):
    k = 2*t-1-r
    p = sp.Poly(sp.expand(T[k]), b3)
    a_r = red(p.nth(2)) if p.degree() >= 2 else sp.Integer(0)
    avec[r] = a_r
    supp = sorted({str(v) for v in a_r.free_symbols if v != y})
    # weighted degree of a_r
    if a_r != 0 and supp:
        pp = sp.Poly(sp.expand(a_r), *[v for v in resid if v != b3])
        degs = {sum(m*wt[v] for m, v in zip(mo, [v for v in resid if v != b3])) for mo in pp.monoms()}
    else:
        degs = {0}
    nterms = len(sp.Poly(sp.expand(a_r), *[v for v in resid if v != b3]).monoms()) if a_r != 0 else 0
    print(f"   r={r} k={k}: deg_b3={p.degree()}  a_r support={supp}  wdeg(a_r)={sorted(degs)} (exp {r})  #terms={nterms}", flush=True)
    rows[r] = T[k]

print("\nD. linearisation G_r = a_0*T_{2t-1-r} - a_r*T_{2t-1}:", flush=True)
Bmat, Cmat = {}, {}
for r in range(1, t):
    G = red(sp.expand(a0*rows[r] - avec[r]*rows[0]))
    pg = sp.Poly(sp.expand(G), b3)
    Br = red(pg.nth(1)); Cr = red(pg.nth(0))
    Bmat[r], Cmat[r] = Br, Cr
    others = [v for v in resid if v != b3]
    def wdeg(e):
        if e == 0: return set()
        pp = sp.Poly(sp.expand(e), *others)
        return {sum(m*wt[v] for m, v in zip(mo, others)) for mo in pp.monoms()}
    print(f"   r={r}: deg_b3(G_r)={pg.degree()} (expect <=1)  wdeg(B_r)={sorted(wdeg(Br))} (exp {t+1+r})"
          f"  wdeg(C_r)={sorted(wdeg(Cr))} (exp {2*t+2+r})", flush=True)

# ---------- E: wp leaders ------------------------------------------------
print("\nE. b4-axis coefficients mu_{t,k} = [b4^{4t+1-k}]T_{t,k}  (wp-leader test):", flush=True)
zero_resid = {v: 0 for v in resid if v != b4}
for k in range(1, 2*t):
    row = sp.expand(T[k].subs(zero_resid))
    mu = red(sp.Poly(row, b4).nth(4*t+1-k)) if row != 0 else sp.Integer(0)
    print(f"   k={k}: mu = {sp.factor(sp.simplify(mu))}   norm={norm(mu) if mu!=0 else 0}", flush=True)

# ---------- F: 2x2 minors of N = (C_r | B_r) -----------------------------
print("\nF. 2x2 minors  m_{r,r'} = B_r C_r' - B_r' C_r  (weights t+1+r, 2t+2+r):", flush=True)
others = [v for v in resid if v != b3]
minors = []
for r in range(1, t):
    for r2 in range(r+1, t):
        m = red(sp.expand(Bmat[r]*Cmat[r2] - Bmat[r2]*Cmat[r]))
        minors.append(((r, r2), m))
        pp = sp.Poly(sp.expand(m), *others) if m != 0 else None
        dg = sorted({sum(a*wt[v] for a, v in zip(mo, others)) for mo in pp.monoms()}) if pp else []
        print(f"   ({r},{r2}): nonzero={m!=0}  wdeg={dg} (exp {3*t+3+r+r2})  #terms={len(pp.monoms()) if pp else 0}", flush=True)

out = {'t': t,
       'a0': sp.srepr(a0),
       'alpha': sp.srepr(alpha),
       'rows': {str(k): sp.srepr(T[k]) for k in T},
       'a': {str(r): sp.srepr(avec[r]) for r in avec},
       'B': {str(r): sp.srepr(Bmat[r]) for r in Bmat},
       'C': {str(r): sp.srepr(Cmat[r]) for r in Cmat}}
json.dump(out, open(f'/home/ubuntu/jc2/box/k16hsop-20260903/tail_t{t}_rows.json', 'w'))
print(f"\nwrote tail_t{t}_rows.json   total {time.time()-t0:.1f}s", flush=True)
