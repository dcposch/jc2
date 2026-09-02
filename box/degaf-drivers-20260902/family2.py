import sympy as sp, sys; sys.path.insert(0,'/tmp/degaf')
from sg3 import gamma
t,s = sp.symbols('t s')
def divdiff(f):
    return sp.simplify(sp.cancel((f - f.subs(t,s))/(t-s)))
def analyse(ae,be,label):
    a=sp.Poly(ae,t); b=sp.Poly(be,t); p,q=a.degree(),b.degree(); n=max(p,q)
    A=sp.expand(divdiff(ae)); B=sp.expand(divdiff(be))
    R=sp.Poly(sp.resultant(A,B,s),t)
    Rsq=sp.Poly(sp.gcd(R.as_expr(), sp.diff(R.as_expr(),t)),t)   # repeated part
    ndistinct=R.degree()-Rsq.degree()
    crit=sp.solve([sp.diff(ae,t),sp.diff(be,t)],t)
    ac=[int(c) for c in reversed(a.all_coeffs())]; bc=[int(c) for c in reversed(b.all_coeffs())]
    M=max(80,3*p*q); G=gamma(ac,bc,M); win=min(3*n+10,M//3)
    gaps=[m for m in range(win+1) if m not in G]; d=len(gaps); pa=(n-1)*(n-2)//2
    k=(ndistinct-1)//2
    print(f"{label:22s} n={n:2d} crit(t)={crit}  #distinct roots of R = {ndistinct:2d}"
          f"  => 1 cusp + k={k:2d} nodes   delta_aff={d:2d}  (1+k={1+k})  p_a={pa:3d} delta_inf={pa-d:3d}")
    return d,k
print("FAMILY  a=t^3, b=t^q+t^2   (ordinary (2,3) cusp at t=0)")
for q in [4,5,7,8,10,11,13,14]:
    analyse(t**3, t**q+t**2, f"q={q}")
print()
print("FAMILY  a=t^3+t^2 variant to reach the skipped residues")
for q in [6,9,12]:
    analyse(t**3, t**q+t**2+t**4, f"q={q} (+t^4)")
