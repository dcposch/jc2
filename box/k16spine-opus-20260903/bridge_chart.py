#!/usr/bin/env python3
"""Moh's tuple-level (Laurent bridge) chart for the K=16 ray, uniform in t.

SOURCE (Moh p.208-209 = frozen PDF pp.69-70): for the descended datum
(16,12;13;3;X) Moh sets f=eta^{-12}, g=eta^{-16}+a1 eta^{-12}+a2 eta^{-8}
+a3 eta^{-4}+a4+..., gauges (f,g)->(f-(3/4)a3, g-a1 f-a4), and obtains
g = h^4+(4/3)(B2 h^2+B3 h)+(2/9)(B2^2+2gam)-(4/81)del+a2 h^2, cutting 17
coefficients to 10.  Uniform-in-t form used here: with eta=Q^{-1/m},
    P = [ sum_{k=0}^{e} a_k Q^{(e-k)/q} ]_{h-exponent >= 0},   a_0 = 1,
gauges kill a_t, a_{e-1}, a_e.

h-adic Laurent arithmetic: element = {i: c_i}, c_i in Q[gamma,pi,params] with
deg_pi c_i < 4, meaning sum_i c_i h^i.
"""
import sys, sympy as sp
from sympy import Rational as R

T = int(sys.argv[1]) if len(sys.argv) > 1 else 1
e, q = 3*T+1, 2*T+1
n, m = 12*T+4, 8*T+4
g, p = sp.symbols('g p')
b1, b2, b3, b4 = sp.symbols('b1 b2 b3 b4')
h_poly = sp.expand(p**4 + (b1-g)*p**3 + b2*p**2 + b3*p + b4)
zP, BP = p - g, sp.expand(p*(p-g) + b1*p + b2)
AP = sp.expand(p*BP + b3)
assert sp.expand(p*AP + b4 - h_poly) == 0
HP = sp.Poly(h_poly, p)
LO = -(e + 3)

def red(poly):
    out, cur, i = {}, sp.Poly(sp.expand(poly), p), 0
    while True:
        if cur.is_zero: break
        if cur.degree() < 4:
            out[i] = sp.expand(cur.as_expr()); break
        Qp, Rp = sp.div(cur, HP)
        if not Rp.is_zero: out[i] = sp.expand(Rp.as_expr())
        cur = Qp; i += 1
    return {k: v for k, v in out.items() if v != 0}

def hmul(a, b, lo=LO):
    raw = {}
    for i, u in a.items():
        for j, v in b.items():
            if i + j >= lo - 1: raw[i+j] = raw.get(i+j, 0) + u*v
    out = {}
    for k, v in raw.items():
        v = sp.expand(v)
        if v == 0: continue
        for dk, cc in red(v).items():
            if k + dk >= lo: out[k+dk] = sp.expand(out.get(k+dk, 0) + cc)
    return {k: v for k, v in out.items() if v != 0}

def hadd(*args):
    out = {}
    for a in args:
        for j, v in a.items(): out[j] = sp.expand(out.get(j, 0) + v)
    return {k: v for k, v in out.items() if v != 0}

def hscal(a, s):
    return {k: sp.expand(s*v) for k, v in a.items() if sp.expand(s*v) != 0}

def hpow_unit(w, s, lo=LO):
    """(1+w)^s, w supported in h-exponents <= -2 ; binomial series."""
    assert all(k <= -2 for k in w)
    res, term, coef = {0: sp.Integer(1)}, {0: sp.Integer(1)}, sp.Integer(1)
    for j in range(1, -2*lo + 4):
        term = hmul(term, w, lo)
        if not term: break
        coef = sp.Rational(coef) * (s - (j-1)) / j
        res = hadd(res, hscal(term, coef))
    return res

def shift(a, d):   return {k+d: v for k, v in a.items()}
def to_poly(a):    return sp.expand(sum(v*h_poly**k for k, v in a.items() if k >= 0))
def hpos(a):       return {k: v for k, v in a.items() if k >= 0}

# ---------------- chart: Q, then P forced by the bridge ----------------
def basis(i):
    if i <= T:   return [('1', sp.Integer(1))]
    if i <= 2*T: return [('1', sp.Integer(1)), ('A', AP)]
    if i <= 3*T: return [('1', sp.Integer(1)), ('A', AP), ('B', BP)]
    return [('1', sp.Integer(1)), ('g', g), ('A', AP), ('B', BP), ('z', zP)]

unk = [b1, b2, b3, b4]
u_ser = {}                                     # w = sum beta_j h^{-j}
for j in range(2, q+1):
    for nm, ph in basis(j):
        s = sp.Symbol(f'q{j}_{nm}'); unk.append(s)
        for dk, cc in red(sp.expand(s*ph)).items():
            u_ser[-j+dk] = sp.expand(u_ser.get(-j+dk, 0) + cc)
u_ser = {k: v for k, v in u_ser.items() if v != 0}
assert all(k <= -2 for k in u_ser), sorted(u_ser)

avars, aused = {}, []
for k in range(1, e+1):
    if k in (T, e-1, e): avars[k] = sp.Integer(0)      # Moh's three gauges
    else:
        s = sp.Symbol(f'a{k}'); avars[k] = s; unk.append(s); aused.append(k)
cc_ = sp.Symbol('c'); unk.append(cc_)

Pser = {}
for k in range(0, e+1):
    ak = sp.Integer(1) if k == 0 else avars[k]
    if ak == 0: continue
    Pser = hadd(Pser, hscal(shift(hpow_unit(u_ser, R(e-k, q)), e-k), ak))
Pbr = to_poly(hpos(Pser))
Qpoly = to_poly(hadd({q: sp.Integer(1)}, shift(u_ser, q)))

print(f"t={T}: e={e} q={q} n={n} m={m}")
print(f"  free a_k (gauged out: a_{T}, a_{e-1}, a_{e}): {aused}")
print(f"  chart unknowns incl c: {len(unk)}   (predicted 6t+5 = {6*T+5})")
print(f"  deg_pi Q = {sp.degree(Qpoly, p)} (want {m});  deg_pi P = {sp.degree(Pbr, p)} (want {n})")
print(f"  Q monic: {sp.expand(sp.LC(sp.Poly(Qpoly,p)))==1};  P monic: {sp.expand(sp.LC(sp.Poly(Pbr,p)))==1}")

# --- control: P's h-adic coefficients must lie in the charged order spaces S_i
Pa = red(Pbr)
def in_span(expr, phis):
    cs = sp.symbols(f'lam0:{len(phis)}')
    sol = sp.solve(sp.Poly(sp.expand(expr - sum(c*f for c, f in zip(cs, phis))), p).all_coeffs(),
                   cs, dict=True)
    return bool(sol)
ok = True
for i in range(0, e+1):
    ci = Pa.get(e-i, sp.Integer(0))
    if i == 0:
        ok &= (sp.expand(ci-1) == 0); continue
    phis = [f for _, f in basis(i)]
    good = in_span(ci, phis)
    ok &= good
    if not good: print(f"   !! alpha_{i} NOT in S_{i}: {sp.expand(ci)}")
print(f"  [control] every alpha_i of the bridge-built P lies in the charged S_i: {ok}")


def sing(v):
    """integer-coefficient Singular text for a rational-coefficient polynomial"""
    gens = sorted(v.free_symbols, key=str)
    _, pc = sp.Poly(v, *gens).clear_denoms()
    s = str(sp.expand(pc.as_expr())).replace("**", "^")
    assert "/" not in s, s[:120]
    return s

J = sp.expand(sp.diff(Qpoly, g)*sp.diff(Pbr, p) - sp.diff(Qpoly, p)*sp.diff(Pbr, g))
eqs = [sp.expand(v) for v in sp.Poly(sp.expand(J - cc_*g), g, p).coeffs()]
eqs = [v for v in eqs if v != 0]
print(f"  Jacobian J(Q,P)-c*gamma: {len(eqs)} scalar equations")
import json, pathlib
pathlib.Path(f"box/k16spine-opus-20260903/bridge_t{T}.sing").write_text(
    "ring R=0,(" + ",".join(str(v) for v in unk) + ",Tr),dp;\n"
    "ideal I=" + ",\n".join(sing(v) for v in eqs) + ",\n Tr*c-1;\n"
    "option(redSB); ideal G=std(I); G=simplify(G,1);\n"
    "\"nvars=\",nvars(R),\" ngens=\",size(I),\" sbsize=\",size(G);\n"
    "if (size(G)==1) { \"reduced basis G[1]=\",G[1]; } else { \"NONUNIT\"; }\n"
    "\"-- EMPTY control\"; ideal Ic=c,Tr*c-1; ideal Gc=std(Ic); reduce(1,Gc);\n"
    "\"-- NONEMPTY control\"; ideal In=c-1,Tr*c-1; ideal Gn=std(In); reduce(1,Gn);\n"
    "quit;\n")
print(f"  wrote box/k16spine-opus-20260903/bridge_t{T}.sing")
