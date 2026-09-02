import sympy as sp, sys; sys.path.insert(0,'/tmp/degaf')
from sg3 import gamma
t,s=sp.symbols('t s')
def divdiff(f): return sp.expand(sp.cancel((f-f.subs(t,s))/(t-s)))
def full(ae,be,label):
    a=sp.Poly(ae,t); b=sp.Poly(be,t); p,q=a.degree(),b.degree(); n=max(p,q)
    R=sp.Poly(sp.resultant(divdiff(ae),divdiff(be),s),t)
    rts=sp.roots(R); crit=sp.solve([sp.diff(ae,t),sp.diff(be,t)],t)
    ac=[int(c) for c in reversed(a.all_coeffs())]; bc=[int(c) for c in reversed(b.all_coeffs())]
    G=gamma(ac,bc,max(80,3*p*q)); win=3*n+6
    gaps=[m for m in range(win+1) if m not in G]
    # local type at the critical point t=0
    print(f"{label}: (p,q)=({p},{q}) n={n} crit={crit} roots(R)={sorted(rts.keys(), key=str)}")
    print(f"   Gamma gaps={gaps}  delta_aff={len(gaps)}  p_a={(n-1)*(n-2)//2}  delta_inf={(n-1)*(n-2)//2-len(gaps)}")
    # germ at t=0 after removing the a-multiple: b - b2*a  (a=t^2 exactly here)
    return len(gaps)
full(t**2, t**5+t**3+t**2, "cusp+1 node, degree 5")
full(t**2, t**5+t**2,      "cusp only,   degree 5")
full(t**3, t**4+t**2,      "cusp+2 nodes, degree 4")
# germ check for the first: b - a  = t^5+t^3 ; germ (t^2, t^3(1+t^2)) -> semigroup <2,3>
print()
print("germ at t=0 of (t^2, t^5+t^3+t^2) after v -> v-u :  (t^2, t^3+t^5)  => semigroup <2,3>, an ordinary cusp")
print("node pairs: a(t1)=a(t2) => t2=-t1 ; b odd part t^5+t^3=0 => t^2=-1 => ONE pair {i,-i}")
