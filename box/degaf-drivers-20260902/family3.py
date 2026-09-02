import sympy as sp, sys; sys.path.insert(0,'/tmp/degaf')
from sg3 import gamma
t,s=sp.symbols('t s')
def divdiff(f): return sp.expand(sp.cancel((f-f.subs(t,s))/(t-s)))
def analyse(ae,be,label):
    a=sp.Poly(ae,t); b=sp.Poly(be,t); p,q=a.degree(),b.degree(); n=max(p,q)
    R=sp.Poly(sp.resultant(divdiff(ae),divdiff(be),s),t)
    nd=R.degree()-sp.Poly(sp.gcd(R.as_expr(),sp.diff(R.as_expr(),t)),t).degree()
    crit=sp.solve([sp.diff(ae,t),sp.diff(be,t)],t)
    ac=[int(c) for c in reversed(a.all_coeffs())]; bc=[int(c) for c in reversed(b.all_coeffs())]
    M=max(80,3*p*q); G=gamma(ac,bc,M); win=min(3*n+10,M//3)
    d=len([m for m in range(win+1) if m not in G]); pa=(n-1)*(n-2)//2
    k=(nd-1)//2 if crit else nd//2
    print(f"{label:34s} n={n:2d} cusp@{crit}  k(nodes)={k:2d}  delta_aff={d:2d}  "
          f"1+k={1+k:2d}  p_a={pa:3d} d_inf={pa-d:3d}")
# with a cusp at t=0 and generic tail
for q,tail in [(5, 3*t**3+7*t**4),(8, 5*t**3+2*t**4+11*t**5+3*t**6+t**7),
               (11, 3*t**3+5*t**4+2*t**5+7*t**6+t**7+4*t**8+6*t**9+2*t**10)]:
    analyse(t**3, t**q+t**2+tail, f"cusp family q={q} generic tail")
print()
print("REDUCTION DEMONSTRATION (same Aut-orbit, degree 12 -> 4):")
analyse(t**3, t**12+t**4+t**2, "D  = (t^3, t^12+t^4+t^2)")
analyse(t**3, t**4+t**2,       "psi(D), psi=(u,v-u^4)")
