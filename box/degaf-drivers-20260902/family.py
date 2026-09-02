"""Witness family: polynomial curves (one place at infinity, rational) with
exactly ONE ordinary (2,3) cusp and exactly k nodes, for k = 1,2,3,...
a(t)=t^3, b(t)=t^q + beta t^2 (+ tweak).  Checks: birational, cusp type,
node count, delta_aff via the semigroup, and the genus budget."""
import sympy as sp
import sys; sys.path.insert(0,'/tmp/degaf')
from sg3 import gamma, deg as pdeg
t,s = sp.symbols('t s')

def analyse(aexpr,bexpr,label):
    a=sp.Poly(aexpr,t); b=sp.Poly(bexpr,t)
    p,q=a.degree(),b.degree(); n=max(p,q)
    # birationality: C(a,b)=C(t) <=> the generic fibre of (a,b) is one point
    A=sp.Poly(sp.expand((a.as_expr()-a.as_expr().subs(t,s))/(t-s)),t,s)
    B=sp.Poly(sp.expand((b.as_expr()-b.as_expr().subs(t,s))/(t-s)),t,s)
    R=sp.Poly(sp.resultant(A.as_expr(),B.as_expr(),s),t)
    # roots of R = t-values that share their image with some other parameter
    rts=sp.roots(R)
    # ordered pairs (t1,t2), t1!=t2 with same image: solve system
    sols=sp.solve([A.as_expr(),B.as_expr()],[t,s],dict=True)
    pairs=set()
    for so in sols:
        if t in so and s in so:
            pairs.add(frozenset([sp.nsimplify(so[t]),sp.nsimplify(so[s])]))
    nodes=len([P for P in pairs if len(P)==2])
    # cusp: critical points of the parametrisation
    crit=sp.solve([sp.diff(a.as_expr(),t),sp.diff(b.as_expr(),t)],t)
    # semigroup
    ac=[int(c) for c in reversed(a.all_coeffs())]; bc=[int(c) for c in reversed(b.all_coeffs())]
    M=max(60,3*p*q)
    G=gamma(ac,bc,M); win=min(3*n+10, M//3)
    gaps=[m for m in range(win+1) if m not in G]
    pa=(n-1)*(n-2)//2
    print(f"{label:26s} (p,q)=({p},{q}) n={n:2d} crit={crit} #node-pairs={nodes:2d} "
          f"delta_aff={len(gaps):2d}  p_a={pa:3d} delta_inf={pa-len(gaps):3d}  gaps={gaps}")
    return len(gaps),nodes,crit

for q in [4,5,7,8,10,11]:
    analyse(t**3, t**q + t**2, f"cusp+nodes q={q}")
print()
print("control: no cusp (generic) ---")
for q in [4,5,7]:
    analyse(t**3+t, t**q + t**2 + t, f"generic (3,{q})")
