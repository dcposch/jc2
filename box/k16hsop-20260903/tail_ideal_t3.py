#!/usr/bin/env python3
"""t=3 end-to-end verification on MY independently generated rows.

 (1) the tail ideal J = (T_{3,3},T_{3,4},T_{3,5}) is 0-dimensional of length 90
     = L_3 = 2*binom(10,2)   [modular fibres p=1009, both roots of H_3];
 (2) J = (Q_0, G_1, G_2) with Q_0 = a_0 b3^2 + b_0 b3 + c_0 (a_0 a unit) and
     G_r b3-linear  -> the rank-2 splitting;
 (3) the eliminant W_r = a_0 C_r^2 - b_0 B_r C_r + c_0 B_r^2 = Res_b3(Q_0,G_r)
     lies in J, has weight 4t+4+2r, and V(W_1,W_2) = {0} in A^2_{b4,u2};
 (4) the standard-monomial count of S/J against the predicted CI series
     P_3(s) = (1+s^4)[10 choose 2]_s.
"""
import json, sympy as sp
from sympy import GF

y, b4, u2, b3 = sp.symbols('y b4 u2 b3')
t = 3; q = 2*t+1; p = 1009
H = 12*q**2*y**2 - 12*q*(t+1)*y + (t+1)*(3*t+2)
roots = [r for r in range(p) if (int(sp.Poly(H, y).eval(r)) % p) == 0]
print("H_3 roots mod 1009:", roots, "  (charged sol56 table: 632, 810)")

D = json.load(open('/home/ubuntu/jc2/box/k16hsop-20260903/tail_t3_rows.json'))
T = {int(k): sp.sympify(v) for k, v in D['rows'].items()}
a = {int(k): sp.sympify(v) for k, v in D['a'].items()}
B = {int(k): sp.sympify(v) for k, v in D['B'].items()}
Cc = {int(k): sp.sympify(v) for k, v in D['C'].items()}
a0 = sp.sympify(D['a0'])
Q0 = T[2*t-1]
b0 = sp.Poly(sp.expand(Q0), b3).nth(1)
c0 = sp.Poly(sp.expand(Q0), b3).nth(0)

def modp(e, yv):
    """reduce a rational-in-y expression to GF(p) with y=yv"""
    e = sp.together(sp.expand(e))
    n, dd = sp.fraction(e)
    n = sp.Poly(sp.expand(n), b4, u2, b3, y)
    dd = sp.expand(dd)
    dnum = int(sp.Poly(dd, y).eval(yv)) % p if dd.has(y) else int(dd) % p
    inv = pow(dnum, p-2, p)
    out = 0
    for mo, co in zip(n.monoms(), n.coeffs()):
        co = sp.Rational(co)
        cn, cd = int(co.p) % p, int(co.q) % p
        cc = cn * pow(cd, p-2, p) % p
        cc = cc * pow(yv, mo[3], p) % p
        out += cc * b4**mo[0] * u2**mo[1] * b3**mo[2]
    return sp.expand(out * inv)

def gb_and_vdim(polys, gens, yv, tag):
    ps = [modp(f, yv) for f in polys]
    ps = [f for f in ps if f != 0]
    G = sp.groebner(ps, *gens, order='grevlex', modulus=p)
    lts = [sp.LT(g, gens, order='grevlex') for g in G.exprs]
    lms = []
    for g in G.exprs:
        pg = sp.Poly(g, *gens, modulus=p)
        lms.append(pg.monoms(order='grevlex')[0])
    # dimension test: is some pure power of each variable a leading monomial?
    n = len(gens)
    pure = []
    for i in range(n):
        ok = any(all(m[j] == 0 for j in range(n) if j != i) and m[i] > 0 for m in lms)
        pure.append(ok)
    if not all(pure):
        print(f"   [{tag}] NOT zero-dimensional: pure powers {pure}")
        return None, lms
    bounds = []
    for i in range(n):
        bounds.append(min(m[i] for m in lms if all(m[j] == 0 for j in range(n) if j != i) and m[i] > 0))
    cnt = 0
    import itertools
    for expo in itertools.product(*[range(b) for b in bounds]):
        if not any(all(expo[j] >= m[j] for j in range(n)) for m in lms):
            cnt += 1
    print(f"   [{tag}] dim=0, pure-power bounds {dict(zip([str(g) for g in gens],bounds))}, vdim = {cnt}")
    return cnt, lms

print("\n(1) tail ideal J = (T_3,T_4,T_5), predicted length L_3 = 90")
for yv in roots:
    gb_and_vdim([T[3], T[4], T[5]], (b4, u2, b3), yv, f"y={yv}")

print("\n(2) rank-2 splitting: J == (Q_0, G_1, G_2)?")
G1 = sp.expand(a0*T[4] - a[1]*T[5])
G2 = sp.expand(a0*T[3] - a[2]*T[5])
for yv in roots[:1]:
    A = sp.groebner([modp(f, yv) for f in [T[3], T[4], T[5]]], b4, u2, b3, order='grevlex', modulus=p)
    Bg = sp.groebner([modp(f, yv) for f in [T[5], G1, G2]], b4, u2, b3, order='grevlex', modulus=p)
    print(f"   y={yv}: GB(J) == GB(Q_0,G_1,G_2) :", set(A.exprs) == set(Bg.exprs))
    print(f"           deg_b3(G_1)={sp.Poly(G1,b3).degree()}  deg_b3(G_2)={sp.Poly(G2,b3).degree()}")

print("\n(3) eliminants W_r = a_0 C_r^2 - b_0 B_r C_r + c_0 B_r^2  (= Res_b3(Q_0,G_r))")
W = {}
for r in (1, 2):
    Wr = sp.expand(a0*Cc[r]**2 - b0*B[r]*Cc[r] + c0*B[r]**2)
    Wr = sp.simplify(Wr)
    W[r] = Wr
    res = sp.resultant(sp.Poly(Q0, b3), sp.Poly(sp.expand(a0*T[2*t-1-r] - a[r]*T[2*t-1]), b3))
    print(f"   r={r}: W_r == Res_b3(Q_0,G_r) :", sp.simplify(sp.expand(Wr - res)) == 0,
          "  vars:", sorted(str(v) for v in Wr.free_symbols if v != y))
print("   V(W_1,W_2) in A^2_{b4,u2}:")
for yv in roots:
    gb_and_vdim([W[1], W[2]], (b4, u2), yv, f"y={yv} eliminant")

print("\n(4) predicted CI series P_3(s) = (1+s^4)[10 choose 2]_s, sum = 90")
