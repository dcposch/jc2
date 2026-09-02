import sympy as sp
from tree import analyse, Skip, x, y
def brief(nm,P,Q):
    try: r = analyse(P,Q)
    except Skip as e:
        print("%-34s SKIP %s"%(nm,e)); return None
    lev1=[cl for cl in r['cluster'] if cl['prox']==['E0']]
    ok = (r['Zsq']==r['N']) and (r['ZK1']==r['ZK2']) and r['okc'] and r['ZK1']==r['Psi']-r['Lam']-r['kappa'] and r['ZK1']==r['Theta']-r['kappa']-r['Sn']
    print("%-34s D=%-3d N=%-3d kap=%-2d Sn=%-3d ell=%d xi=%d T=%-3d Tcl=%-3d Lam=%-4d Psi=%-4d ZK=%-4d vE0=%d lvs=%d frk=%d numax=%-2d mmax=%-3d lev1a=%s %s"%(
      nm,r['D'],r['N'],r['kappa'],r['Sn'],r['ell'],r['xi'],r['T'],r['Tclass'],r['Lam'],r['Psi'],r['ZK1'],r['valE0'],r['leaves'],r['fork'],r['numax'],r['mmax'],
      [cl['a'] for cl in lev1], "ok" if ok else "**FAIL**"))
    return r
print("--- mock subrectangular pairs: l(P)=(x^u y^v)^m, l(Q)=(x^u y^v)^n ; predict lev1 a = [e*v, e*u], sum=D=e(u+v)")
brief("u=1,v=2,m=2,n=3", x**2*y**4 + x + y, x**3*y**6 + x**2*y + 1)
brief("u=1,v=2,m=2,n=3 (b)", x**2*y**4 + x*y + 1, x**3*y**6 + x*y**2 + x)
brief("u=2,v=3,m=2,n=3", x**4*y**6 + x*y + 1, x**6*y**9 + x*y**2 + x)
brief("u=2,v=3,m=2,n=3(b)", x**4*y**6 + x**2*y**2 + x, x**6*y**9 + x**3*y**3 + y)
brief("u=1,v=3,m=2,n=3", x**2*y**6 + x*y + 1, x**3*y**9 + x*y**2 + x)
brief("u=4,v=12,m=2,n=3", x**8*y**24 + x*y + 1, x**12*y**36 + x*y**2 + x)
print("--- family (B): psi_k o (x, x y^m) ---")
for m in (2,3,4):
  for k in (1,2,3):
    Qm = x*y**m
    brief("psi_%d o (x,xy^%d)"%(k,m), x + Qm**k, Qm)
print("--- family (A): (x, x^c y^N) ---")
for N in (2,3,4):
  for c in (1,2,3):
    brief("(x, x^%d y^%d)"%(c,N), x, x**c*y**N)
print("--- PROFILE-WITNESS G_k = psi_k o (x, x y^4 - y^2) ---")
for k in (1,2,3):
    Qm = x*y**4 - y**2
    brief("psi_%d o (x,xy^4-y^2)"%k, x + Qm**k, Qm)
