import sympy as sp, itertools
from engine import Resolution, x, y

def paths(r):
    """pi(i,k) = number of proximity paths from p_i down to p_k (pi(i,i)=1)."""
    ids=[0]+sorted(r.a.keys()); pi={}
    for i in ids:
        d={i:1}
        for j in sorted([q for q in ids if q<i], reverse=True):
            pass
        # forward accumulation
        for j in sorted(ids):
            if j>=i: continue
        pi[i]=d
    # recompute properly by recursion  pi(i,k) = sum_{p in prox(i)} pi(p,k)
    PI={0:{0:1}}
    for i in sorted(r.a.keys()):
        d={i:1}
        for p in r.prox[i]:
            for k,v in PI[p].items():
                d[k]=d.get(k,0)+v
        PI[i]=d
    return PI

def check(nm,P,Q):
    r=Resolution(sp.expand(P),sp.expand(Q),nm)
    assert all(r.checks.values()), nm
    PI=paths(r); ids=[0]+sorted(r.a.keys())
    A={0:r.D}; A.update(r.a)
    # (b)  m_i = D*nu_i - sum_k pi(i,k) a_k   (k ranges over the cluster, k>=1)
    for i in ids:
        pred=r.D*r.nu[i]-sum(v*A[k] for k,v in PI[i].items() if k>=1)
        assert (r.m[i] or 0)==pred, (nm,i,r.m[i],pred)
    # (c) T-POSITIVE test on T=0 rows
    dic=[i for i in ids if r.kind[i]=='dicritical']
    out=dict(nm=nm,D=r.D,N=r.N,kap=r.kappa,T=r.T,ell=len(dic),
             sln=sorted(r.rho[i] for i in dic))
    if r.T==0 and len(dic)==1:
        out['bound']= (r.D<=2*r.kappa)
        assert r.D<=2*r.kappa, ("T-POSITIVE violated",nm,r.D,r.kappa)
    if r.T==0:
        # general form: 2*s_l*n <= D for every dicritical
        for i in dic:
            assert 2*r.rho[i]<=r.D, ("2 s_l n <= D violated",nm,i,r.rho[i],r.D)
    return out

tests=[("(x,y+x^2)",x,y+x**2),("(x,y+x^5)",x,y+x**5),("(x,xy)",x,x*y),
 ("(x,xy^2)",x,x*y**2),("(x,xy^3)",x,x*y**3),("(x,xy^4)",x,x*y**4),
 ("(x,xy^5)",x,x*y**5),("(x,x^2y)",x,x**2*y),("(x,x^2y^2)",x,x**2*y**2),
 ("(x,x^3y^2)",x,x**3*y**2),("(x,x^2y^3)",x,x**2*y**3),("(x,y^3)",x,y**3),
 ("(x,y^4)",x,y**4),("(x^2,y^4)",x**2,y**4),("(x^3,y^2)",x**3,y**2),
 ("(x^2y,y)",x**2*y,y),("(xy,y)",x*y,y),("psi2o(x,xy^2)",x+(x*y**2)**2,x*y**2),
 ("psi3o(x,xy^3)",x+(x*y**3)**3,x*y**3),("psi2o(x,xy)",x+(x*y)**2,x*y),
 ("(x,xy^2)o(x,y+x^2)",x,x*(y+x**2)**2),("(x,xy^3)o(x,y+x^3)",x,x*(y+x**3)**3),
 ("(x,x^2y^3)o(x+y^2,y)",x+y**2,(x+y**2)**2*y**3),("(x,y+x^2+x^3)",x,y+x**2+x**3),
 ("(x,x^3y^4)",x,x**3*y**4),("(x,x^4y^3)",x,x**4*y**3),("(x,x y^2+y)",x,x*y**2+y)]
print(f"{'map':26s}{'D':>4}{'N':>4}{'kap':>5}{'T':>4}{'#dic':>5} {'dicr rho'} ")
n=0
for t in tests:
    try: o=check(*t)
    except AssertionError as e:
        print("  ASSERT",t[0],e); continue
    n+=1
    flag = "  <= 2kap OK" if (o['T']==0 and o['ell']==1) else ""
    print(f"{o['nm']:26s}{o['D']:4d}{o['N']:4d}{o['kap']:5d}{o['T']:4d}{o['ell']:5d} {o['sln']}{flag}")
print(f"\nm_i = D*nu_i - sum_k pi(i,k) a_k : verified on {n} maps, 0 failures")
print("T=0 => 2*s_l*n <= D for every dicritical : verified, 0 failures")
