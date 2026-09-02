import sympy as sp
from engine import Resolution, x, y

def info(nm,P,Q):
    r=Resolution(sp.expand(P),sp.expand(Q),nm)
    assert all(r.checks.values()), (nm,[k for k,v in r.checks.items() if not v])
    pa=(r.D-1)*(r.D-2)//2; delta=sum(a*(a-1)//2 for a in r.a.values())
    g=pa-delta
    dic=sorted([r.rho[i] for i in r.rho if r.kind.get(i)=='dicritical'])
    ont=sorted([(r.m[i],r.rho[i]) for i in r.rho if r.kind.get(i)=='onto-Linf'])
    return dict(nm=nm,D=r.D,N=r.N,kap=r.kappa,Lam=r.Lam,T=r.T,ZK=r.ZK,g=g,
                dic=dic,onto=ont,r=r.r)

# right composition:  F o chi   with chi an automorphism of the SOURCE
chis=[("id",x,y),("(x,y+x^2)",x,y+x**2),("(x,y+x^3)",x,y+x**3),
      ("(x+y^2,y)",x+y**2,y),("(x,y+x^2)o(x+y^2,y)",x+y**2,y+(x+y**2)**2)]
bases=[("(x, x y^2)",x,x*y**2),("(x, x^2 y^3)",x,x**2*y**3),("(x, y^3)",x,y**3),
       ("(x, x y^3)",x,x*y**3),("auto (x,y+x^2)",x,y+x**2)]
for bn,BP,BQ in bases:
    print("="*100); print("base:",bn)
    for cn,c1,c2 in chis:
        P=sp.expand(BP.subs({x:c1,y:c2},simultaneous=True))
        Q=sp.expand(BQ.subs({x:c1,y:c2},simultaneous=True))
        try:
            d=info(f"o {cn}",P,Q)
        except AssertionError as e:
            print("   ",cn,"SKIP",e); continue
        print(f"   chi={cn:22s} D={d['D']:3d} N={d['N']:3d} kap={d['kap']:2d} Lam={d['Lam']:3d} "
              f"T={d['T']:3d} ZK={d['ZK']:3d} g_net={d['g']:2d} dicr_rho={d['dic']} onto(m,k)={d['onto']}")
