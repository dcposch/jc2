import sympy as sp
from engine import Resolution, x, y
rows=[]
tests=[("(x,xy)",x,x*y),("(x,xy^2)",x,x*y**2),("(x,xy^3)",x,x*y**3),("(x,xy^4)",x,x*y**4),
 ("(x,x^2y)",x,x**2*y),("(x,x^2y^2)",x,x**2*y**2),("(x,x^3y^2)",x,x**3*y**2),
 ("(x,x^2y^3)",x,x**2*y**3),("(x,x^3y^4)",x,x**3*y**4),("(x,x^4y^3)",x,x**4*y**3),
 ("psi2o(x,xy^2)",x+(x*y**2)**2,x*y**2),("psi3o(x,xy^3)",x+(x*y**3)**3,x*y**3),
 ("psi4o(x,xy^2)",x+(x*y**2)**4,x*y**2),("psi2o(x,xy)",x+(x*y)**2,x*y),
 ("(x,xy^2)o(x,y+x^2)",x,x*(y+x**2)**2),("(x,xy^3)o(x,y+x^3)",x,x*(y+x**3)**3),
 ("(x,x^2y^3)o(x+y^2,y)",x+y**2,(x+y**2)**2*y**3),("(x^2y,y)",x**2*y,y),("(xy,y)",x*y,y),
 ("(x,xy^2+y)",x,x*y**2+y),("(x,y+x^2)",x,y+x**2),("(x,y+x^5)",x,y+x**5),
 ("(x,y^3)",x,y**3),("(x^2,y^4)",x**2,y**4),("(x^3,y^2)",x**3,y**2),
 # candidates with several dicriticals
 ("(xy,x+y)",x*y,x+y),("(x^2 y^2, y)",x**2*y**2,y),("(x*y^2,x*y)",x*y**2,x*y),
 ("(x^2-y^2, x y)",x**2-y**2,x*y),("(x(x+y), y)",x*(x+y),y),
 ("(x^2y, x y)",x**2*y,x*y),("(x, x(x+1)y^2)",x,x*(x+1)*y**2),
 ("(x, (x^2-1) y^2)",x,(x**2-1)*y**2),("(x, (x^2-1)y^3)",x,(x**2-1)*y**3),
 ("(x, x(x-1)(x-2)y^2)",x,x*(x-1)*(x-2)*y**2)]
print(f"{'map':24s}{'D':>4}{'N':>4}{'kap':>5}{'Lam':>5}{'T':>4}{'l':>3}{'2(T+k)':>8}{'D<=?':>6}{'2Lam<=D':>9}")
viol=0; nl1=0
for nm,P,Q in tests:
    try: r=Resolution(sp.expand(P),sp.expand(Q),nm)
    except AssertionError as e: print(f"{nm:24s}  SKIP {e}"); continue
    if not all(r.checks.values()): print("FAIL",nm); continue
    dic=[i for i in r.kind if r.kind[i]=='dicritical']; l=len(dic)
    ok1 = r.D<=2*(r.T+r.kappa); ok2 = 2*r.Lam<=r.D
    if l==1 and r.D>r.N:
        nl1+=1
        if not (ok1 and ok2): viol+=1
    print(f"{nm:24s}{r.D:4d}{r.N:4d}{r.kappa:5d}{r.Lam:5d}{r.T:4d}{l:3d}{2*(r.T+r.kappa):8d}"
          f"{'Y' if ok1 else 'N':>6}{'Y' if ok2 else 'N':>9}")
print(f"\nHALF-CAP (l=1, D>N):  D <= 2(T+kappa)  and  2*Lam <= D  --  {nl1} rows tested, {viol} violations")
