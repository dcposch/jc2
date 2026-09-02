import sympy as sp
from tree import analyse, Skip, x, y

def nu_topform(P,Q):
    dP,dQ = sp.Poly(P,x,y).total_degree(), sp.Poly(Q,x,y).total_degree(); D=max(dP,dQ)
    def lf(R,d):
        R=sp.Poly(R,x,y); return sum(c*x**i*y**j for (i,j),c in R.terms() if i+j==d)
    fs=[sp.Poly(lf(R,d),x,y) for R,d in ((P,dP),(Q,dQ)) if d==D]
    G=fs[0]
    for f in fs[1:]: G=G.gcd(f)
    Tv=sp.Symbol('T'); e=G.as_expr()
    if e.is_number: return 0
    g=sp.Poly(sp.expand(e.subs({x:1,y:Tv})),Tv)
    n=len([f for f,_ in sp.factor_list(g.as_expr(),Tv)[1]]) if g.degree()>0 else 0
    if g.degree()<sp.Poly(e,x,y).total_degree(): n+=1
    return n

def go(nm,P,Q):
    try: r=analyse(P,Q)
    except Skip as ex:
        print("%-32s SKIP %s"%(nm,ex)); return
    Tp={l for l,d in r['divs'].items() if d['m']>0}
    dg0=sum(1 for o in r['divs']['E0']['adj'] if o in Tp)
    print("%-32s D=%-3d N=%-2d nu=%d vE0=%d degT(E0)=%d Sn=%-2d ell=%d T=%-3d Lam=%-4d Psi=%-4d ZK=%-4d [E0 leaf of T+? %s]"%(
      nm,r['D'],r['N'],nu_topform(P,Q),r['valE0'],dg0,r['Sn'],r['ell'],r['T'],r['Lam'],r['Psi'],r['ZK1'], "YES" if dg0<=1 else "no"))

print("### right-composing a NON-PROPER map with a source automorphism  chi=(x,y+x^2)")
chi = (x, y+x**2)
for nm,P,Q in [("(x,xy)",x,x*y),("(x,x^2y^2)",x,x**2*y**2),("(x,x^2y^3)",x,x**2*y**3)]:
    go(nm,P,Q)
    Pc = sp.expand(P.subs({x:chi[0],y:chi[1]},simultaneous=True))
    Qc = sp.expand(Q.subs({x:chi[0],y:chi[1]},simultaneous=True))
    go(nm+" o chi", Pc, Qc)
print("### CH2 hypothesis test: any map with E0 a LEAF of T+ and a dicritical?")
for nm,P,Q in [("(x,y^2)",x,y**2),("(x^3,y^2)",x**3,y**2),("(x,y+x^3)",x,y+x**3)]:
    go(nm,P,Q)
