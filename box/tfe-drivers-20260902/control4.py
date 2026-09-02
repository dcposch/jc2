#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- CONTROL 4 (NEGATIVE): a non-Keller two-tower row must FAIL.

The rows are NOTT's explicit two-tower pairs: f, g are products of factors
(y - a x)^p - b x^q, so every root is explicit and the whole tree is exact.
For each row we compute, at the DEEPEST disc D_1 of the g-tree:
   delta_1, lam_g(delta_1), lam_f(delta_1),  p_g(pi), p_f(pi)
and test the two things LOCAL-KELLER forces on a Keller pair:
   (ORD)  lam_f(delta_1) + lam_g(delta_1) = delta_1 - 1
   (ODE)  lam_f p_f p_g' - lam_g p_g p_f'  is a NONZERO CONSTANT in pi.
Both must fail off the Keller locus.
"""
import sys, itertools
from fractions import Fraction as F
import sympy as sp
sys.path.insert(0,'/Users/dc/code/math/jc2/box')

x, y = sp.symbols('x y')
pi_ = sp.Symbol('pi')
INF = F(10**9)

def factor_poly(a,p,b,q): return sp.expand((y-a*x)**p - b*x**q)
def factor_roots(a,p,b,q):
    return [{F(1,1): sp.Integer(a),
             F(q,p): sp.root(sp.Integer(b), p)*sp.exp(2*sp.pi*sp.I*sp.Rational(k,p))}
            for k in range(p)]
def build(spec):
    poly = sp.Integer(1); rts=[]
    for tpl in spec:
        poly = sp.expand(poly*factor_poly(*tpl)); rts += factor_roots(*tpl)
    return poly, rts
def ord_diff(r1, r2):
    for e_ in sorted(set(r1)|set(r2), reverse=True):
        if sp.simplify(r1.get(e_,0)-r2.get(e_,0)) != 0: return -e_
    return INF
def lam(delta, ords): return sum(min(delta,o) for o in ords)

TWO_TOWER = [
    ([(1,1,3,0),(2,1,5,0)],  [(1,2,7,1),(2,1,11,0)]),
    ([(1,2,3,1),(2,1,5,0)],  [(1,2,7,1),(2,2,11,1)]),
    ([(1,2,3,1),(2,2,5,1)],  [(1,3,7,2),(2,1,11,0)]),
    ([(1,1,3,0),(2,2,5,1)],  [(1,2,7,1),(2,2,11,1)]),
    ([(1,3,3,2),(2,1,5,0)],  [(1,3,7,1),(2,1,11,0)]),
    ([(1,2,3,1),(2,2,5,1)],  [(1,4,7,2),(2,2,11,1)]),
    ([(1,2,3,1),(2,2,3,1)],  [(1,3,3,1),(2,3,3,1)]),
]
FAIL=[]; NCHK=[0]
def check(name, cond, detail=""):
    NCHK[0]+=1
    if not cond: FAIL.append((name,detail)); print("  FAIL  %-56s %s"%(name,detail))
    return cond

def coeff_at(root, ex):
    for e_, c in root.items():
        if e_ == ex: return c
    return sp.Integer(0)

def analyse(fs, gs, label):
    f, phis = build(fs); g, taus = build(gs)
    m, n = len(phis), len(taus)
    J = sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))
    keller = (J.free_symbols == set())
    # deepest disc of the g-tree: pick the root rho with the LARGEST pairwise contact
    best = None
    for i in range(n):
        oth = [ord_diff(taus[i], taus[j]) for j in range(n) if j != i]
        d1 = max(o for o in oth if o < INF)
        if best is None or d1 > best[0]: best = (d1, i)
    delta1, i0 = best
    rho = taus[i0]
    og = [ord_diff(rho, t) for t in taus if t is not rho]
    of = [ord_diff(rho, p) for p in phis]
    lg = lam(delta1, og); lf = lam(delta1, of)
    inD = [t for t in taus if ord_diff(rho,t) >= delta1]
    inF = [p for p in phis if ord_diff(rho,p) >= delta1]
    a1, b1 = len(inD), len(inF)
    Cg = sp.Integer(1)
    for t in taus:
        if t not in inD: Cg *= coeff_at(t, -ord_diff(rho,t))*(-1) if False else 1
    # p_g(pi) = prod_{roots in D_1} (pi - c) up to a nonzero constant; p_f likewise
    pg = sp.expand(sp.prod([pi_ - coeff_at(t, -delta1) for t in inD])) if a1 else sp.Integer(1)
    pf = sp.expand(sp.prod([pi_ - coeff_at(p, -delta1) for p in inF])) if b1 else sp.Integer(1)
    W  = sp.expand(sp.simplify(lf*pf*sp.diff(pg,pi_) - lg*pg*sp.diff(pf,pi_)))
    degW = sp.degree(sp.Poly(W, pi_), pi_) if W != 0 else -1
    ordok = (lf + lg == F(delta1) - 1)
    print("   %-26s m=%-2d n=%-2d J const=%-5s delta_1=%-7s lam_f+lam_g=%-8s delta_1-1=%-8s (ORD) %-5s a_1=%d b_1=%d deg W=%s"
          % (label, m, n, keller, delta1, lf+lg, F(delta1)-1, ordok, a1, b1, degW))
    check("%s is non-Keller"%label, not keller, str(J)[:40])
    check("%s (ORD) lam_f+lam_g = delta_1-1 FAILS"%label, not ordok, "%s vs %s"%(lf+lg, F(delta1)-1))
    check("%s (ODE) bracket is NOT a nonzero constant"%label, degW != 0, "deg W = %s"%degW)
    return ordok, degW

if __name__ == "__main__":
    print("== CONTROL 4 (NEGATIVE): NOTT's seven two-tower rows, all non-Keller ==")
    print("   A Keller pair must satisfy (ORD) lam_f+lam_g = delta_1 - 1 [D1-PIN] and (ODE)")
    print("   the bottom bracket must be a nonzero CONSTANT.  Both must fail here.")
    for k,(fs,gs) in enumerate(TWO_TOWER):
        analyse(fs, gs, "row %d"%k)
    print("\n%d checks, %d failures"%(NCHK[0], len(FAIL)))
    for nm,dt in FAIL: print("   FAILED:", nm, dt)
