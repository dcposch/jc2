#!/usr/bin/env python3
"""Exact check of the Prop 4.6 face witnesses:  D(P,Q,p,q) = P p q' - Q p' q = c*p, c!=0,
   q squarefree, roots(p) subset roots(q), p not a power of q, deg p = P, deg q = Q."""
import sympy as sp
z = sp.symbols('z'); s5 = sp.sqrt(5)

def D(P,Q,p,q): return sp.expand(P*p*sp.diff(q,z) - Q*sp.diff(p,z)*q)

def check(tag,P,Q,p,q):
    p, q = sp.expand(p), sp.expand(q)
    d = sp.simplify(D(P,Q,p,q))
    c = sp.simplify(sp.cancel(d/p))
    ok_const = c.is_constant() and sp.simplify(c) != 0
    dp, dq = sp.degree(p,z), sp.degree(q,z)
    sqfree = sp.simplify(sp.resultant(q, sp.diff(q,z), z)) != 0
    rp = sp.roots(sp.Poly(p,z)); rq = set(sp.roots(sp.Poly(q,z)).keys())
    contain = all(sp.simplify(r - rr) == 0 for r in rp for rr in [min(rq, key=lambda x: sp.Abs(sp.N(x-r)))]) \
              and all(any(sp.simplify(r-rr)==0 for rr in rq) for r in rp)
    mults = sorted(rp.values(), reverse=True)
    print(f"{tag:22s} P={P} Q={Q} degp={dp} degq={dq} mults={mults} "
          f"D/p={sp.nsimplify(c)} const={bool(ok_const)} qsqfree={bool(sqfree)} roots(p)<=roots(q)={bool(contain)}")
    return bool(ok_const and sqfree and contain and dp==P and dq==Q)

res={}
# (30,20) child, D'_3 top face: P_3=2, Q_3=5, pattern (1,1)
res['top_30_20'] = check("top 30/20 (1,1)",2,5, z**2-1, z*(z**2-1)*(2*z**2-3))
# (30,20) child, D'_2 faces: P_2=5, Q_2=4
res['A'] = check("A  (3,2)",5,4, z**2*(z-1)**3, z*(z-1)*(25*z**2-35*z+7))
res['B'] = check("B  (3,1,1)",5,4, z**3*(z**2-5*z+15), z*(z**2-5*z+15)*(z+1))
a=(1+s5)/2; c=(5-s5)/10
res['C'] = check("C  (2,2,1)",5,4, z**2*(z-1)**2*(z-a), z*(z-1)*(z-a)*(z-c))
res['D'] = check("D  (2,1,1,1)",5,4, z**2*(z**3-1), z*(z**3-1))
# (32,24) child
res['top_32_24'] = check("top 32/24 (1,1)",2,3, z**2-1, z*(z**2-1))
res['E'] = check("E  (3,1)",4,3, z**3*(z-4), z*(z-4)*(z+1))
# R063 D'_3 top face: P=7, Q=2, pattern (7)
res['top_R063'] = check("top R063 (7)",7,2, z**7, z*(z-1))
# R063 D'_2 forced pattern 5,3,3,3 : P=14, Q=7 -- does a face even exist?
print("\nR063 D'_2 pattern (5,3,3,3), P=14, Q=7: search for a face")
cc,e1,e2,e3 = sp.symbols('cc e1 e2 e3')
p = z**5*(z**3-cc)**3
q = z*(z**3-cc)*(z**3-e1)
Dv = sp.expand(D(14,7,p,q))
r = sp.simplify(sp.cancel(sp.expand(Dv)/p))
print("  D/p =", sp.factor(sp.simplify(r)))
print("\nALL WITNESSES PASS:", all(res.values()), res)
