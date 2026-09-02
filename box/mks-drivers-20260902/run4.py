import sympy as sp
from tree import analyse, Skip, x, y

def nu_topform(P,Q):
    dP,dQ = sp.Poly(P,x,y).total_degree(), sp.Poly(Q,x,y).total_degree()
    D=max(dP,dQ)
    def lf(R,d):
        R=sp.Poly(R,x,y); return sum(c*x**i*y**j for (i,j),c in R.terms() if i+j==d)
    fs=[]
    if dP==D: fs.append(sp.Poly(lf(P,dP),x,y))
    if dQ==D: fs.append(sp.Poly(lf(Q,dQ),x,y))
    G=fs[0]
    for f in fs[1:]: G=G.gcd(f)
    Tv=sp.Symbol('T'); e=G.as_expr()
    if e.is_number: return 0
    g=sp.Poly(sp.expand(e.subs({x:1,y:Tv})),Tv)
    n=len([f for f,_ in sp.factor_list(g.as_expr(),Tv)[1]]) if g.degree()>0 else 0
    Dy=sp.Poly(e,x,y).total_degree()
    if g.degree()<Dy: n+=1   # root at [0:1]
    return n

rows=[]
def go(nm,P,Q):
    try: r=analyse(P,Q)
    except Skip as ex:
        print("%-30s SKIP %s"%(nm,ex)); return
    Tp={l for l,d in r['divs'].items() if d['m']>0}
    degTE0 = sum(1 for o in r['divs']['E0']['adj'] if o in Tp)
    lev1=[cl for cl in r['cluster'] if cl['prox']==['E0']]
    w = sum(1 for cl in r['cluster'] if 'E0' in cl['prox'])
    nu = nu_topform(P,Q)
    ok = (r['Zsq']==r['N']) and (r['ZK1']==r['ZK2']) and r['okc'] and r['ZK1']==r['Psi']-r['Lam']-r['kappa'] and r['ZK1']==r['Theta']-r['kappa']-r['Sn'] and r['sa2']==r['D']**2-r['N']
    v1 = (r['valE0']==nu)
    v2 = (r['valE0']<2) or (degTE0==r['valE0'])
    v3 = ((r['T']==r['Tclass']) == (w==len(lev1)))
    print("%-30s D=%-3d N=%-2d nu=%d vE0=%d dgT0=%d w=%-2d k=%-2d Sn=%-2d ell=%d xi=%d T=%-3d Tcl=%-3d Lam=%-3d Psi=%-3d ZK=%-4d lv=%d frk=%d %s%s%s%s"%(
       nm,r['D'],r['N'],nu,r['valE0'],degTE0,w,r['kappa'],r['Sn'],r['ell'],r['xi'],r['T'],r['Tclass'],r['Lam'],r['Psi'],r['ZK1'],r['leaves'],r['fork'],
       "" if ok else " **ID-FAIL**", "" if v1 else " **NU-FAIL**", "" if v2 else " **DEGT0-FAIL**", "" if v3 else " **TCL-FAIL**"))

print("### AUTOMORPHISM / N=1 CONTROLS (predict nu=1, E0 a leaf, T>Tclass)")
for k in (2,3,4,5,6): go("(x, y+x^%d)"%k, x, y+x**k)
go("(x+y^2, y)", x+y**2, y)
go("(x+(y+x^2)^3, y+x^2)", x+(y+x**2)**3, y+x**2)
go("(y, -x)", y, -x)
print("### PROPER / MONOMIAL")
for nm,P,Q in [("(x,y^2)",x,y**2),("(x,y^3)",x,y**3),("(x^2,y^2)",x**2,y**2),("(x^3,y^2)",x**3,y**2),
               ("(x^2,y^3)",x**2,y**3)]: go(nm,P,Q)
print("### NON-PROPER dominant (nu=2 expected)")
for nm,P,Q in [("(x,xy)",x,x*y),("(xy,y)",x*y,y),("(x,xy^2)",x,x*y**2),("(x,x^2y)",x,x**2*y),
               ("(x,x^2y^2)",x,x**2*y**2),("(x,x^3y^2)",x,x**3*y**2),("(x^2y,y)",x**2*y,y)]: go(nm,P,Q)
print("### HALF-CAP refutation witnesses (ell>=2)")
for nm,P,Q in [("(xy^2,xy)",x*y**2,x*y),("(x^2y,xy)",x**2*y,x*y),
               ("(x,x(x-1)(x-2)y^2)",x,x*(x-1)*(x-2)*y**2)]: go(nm,P,Q)
print("### MOCK subrectangular (l(P)=(x^u y^v)^m, l(Q)=(x^u y^v)^n): predict lev1 a=[e v, e u], w=2, T=Tcl")
go("mock u1,v2,m2,n3", x**2*y**4 + x + y, x**3*y**6 + x**2*y + 1)
go("mock u2,v3,m2,n3", x**4*y**6 + x*y + 1, x**6*y**9 + x*y**2 + x)
go("mock u1,v3,m2,n3", x**2*y**6 + x*y + 1, x**3*y**9 + x*y**2 + x)
go("mock u4,v12,m2,n3", x**8*y**24 + x*y + 1, x**12*y**36 + x*y**2 + x)
go("mock u4,v12,m3,n2", x**12*y**36 + x*y**2 + x, x**8*y**24 + x*y + 1)
print("### PROFILE-WITNESS G_k and family (B)")
for k in (1,2): go("psi_%d o (x,xy^4-y^2)"%k, x+(x*y**4-y**2)**k, x*y**4-y**2)
for k in (1,2,3): go("psi_%d o (x,xy^3)"%k, x+(x*y**3)**k, x*y**3)
