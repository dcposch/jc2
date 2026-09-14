#!/usr/bin/env python3
"""Exact bare-tower ramification identity, over Q(t)[d]/(3d^2-t-1).

Run in the foreground:
  timeout 1800 stdbuf -oL python3 box/k16astra-20260905/belyi_identity.py
This certifies only the bare-tower Belyi map, not the K16 residual atom.
"""
import sympy as s

t, d, v = s.symbols("t d v")
q, e = 2*t+1, 3*t+1
y = (d+t+1)/(2*q)
g1 = e/q
g2 = e*(d+q)/(2*q**2)
g = e*t*(3*d+2*t+2)/(6*q**3)
f = v**2+v+y
G = v**3+g1*v**2+g2*v+g


def red(expr):
    num, den = s.together(expr).as_numer_denom()
    assert not den.has(d), "This audit uses denominators in Q[t] only"
    return s.factor(s.rem(num, 3*d**2-t-1, d)/den)


identity = v*(q*f*s.diff(G,v)-e*s.diff(f,v)*G)-f*G
assert red(identity+y*g) == 0
print("UNIFORM_WRONSKIAN_IDENTITY_PASS", flush=True)
print("q=2t+1; e=3t+1; 3q-2e=1", flush=True)
print("R(v)=G(v)^q/(v*f(v)^e)", flush=True)
print("R'(v)=-y*g*G(v)^(q-1)/(v^2*f(v)^(e+1))", flush=True)
print("degree=6t+3; passport=(q,q,q),(e,e,1),(5,1^(6t-2))", flush=True)

norm = lambda expr: red(expr*expr.xreplace({d:-d}))
print("N(y)=", s.factor(norm(y)), flush=True)
print("N(g)=", s.factor(norm(g)), flush=True)
print("Res_v(f,G)=", red(s.resultant(f,G,v)), flush=True)

for tt in [2,3,4]:
    # Exact number fields; both rational t=2 fibres are checked separately.
    roots = [-s.sqrt(s.Rational(tt+1,3)), s.sqrt(s.Rational(tt+1,3))]
    for dd in roots:
        smap = {t:tt,d:dd}
        ff, GG = s.expand(f.subs(smap)), s.expand(G.subs(smap))
        qq, ee = 2*tt+1, 3*tt+1
        HH = s.Poly(s.expand(GG**qq-v*ff**ee),v,extension=True)
        assert HH.degree() == 6*tt-2
        assert s.gcd(HH, HH.diff()).degree() == 0
        assert s.simplify(HH.LC()-(y*g/5).subs(smap)) == 0
        assert s.gcd(s.Poly(ff,v,extension=True), s.Poly(GG,v,extension=True)).degree() == 0
        print(f"EXACT_CONTROL t={tt} d={dd} y={s.simplify(y.subs(smap))} PASS; "
              f"finite_Rminus1_degree={HH.degree()}", flush=True)

print("BARE_BELYI_AUDIT_DONE; NO_UNIFORM_ATOM_PROMOTION", flush=True)
