import sympy as sp
from engine import Resolution, x, y

def detail(nm,P,Q):
    r = Resolution(P,Q,nm); s=r.summary()
    ids=[0]+sorted(r.a.keys())
    nc=[i for i in ids if r.rho[i]>0]
    kap_nu=sum(r.nu[i]*r.rho[i] for i in nc if r.kind[i]=='onto-Linf')
    S_nu  =sum(r.nu[i]*r.rho[i] for i in nc if r.kind[i]=='dicritical')
    numax_nc=max([r.nu[i] for i in nc], default=0)
    pa=(r.D-1)*(r.D-2)//2
    delta=sum(a*(a-1)//2 for a in r.a.values())
    g_plus=pa-delta                      # = g_net + delta_aff(C_gen)
    assert r.ZK==2*g_plus-r.N-2, (nm,r.ZK,g_plus)
    nsat=len([i for i in r.a if len(r.prox[i])==2])
    return dict(nm=nm,D=r.D,N=r.N,kap=r.kappa,Lam=r.Lam,T=r.T,rho0=r.rho[0],
                E0=r.kind[0],kap_nu=kap_nu,S_nu=S_nu,numax_nc=numax_nc,
                gplus=g_plus,nsat=nsat,nnc=len(nc))

tests=[("auto (x,y+x^2)",x,y+x**2),("auto (x,y+x^4)",x,y+x**4),
       ("auto (x,y+x^6)",x,y+x**6),("auto nested",x+(y+x**2)**3,y+x**2),
       ("(x,xy)",x,x*y),("(x,xy^2)",x,x*y**2),("(x,x^2y)",x,x**2*y),
       ("(x,x^3y^2)",x,x**3*y**2),("(x,y^4)",x,y**4),("(x^2,y^4)",x**2,y**4),
       ("(x^3,y^2)",x**3,y**2),("psi2o(x,xy^2)",x+(x*y**2)**2,x*y**2),
       ("psi4o(x,xy^2)",x+(x*y**2)**4,x*y**2),("psi2o(x,xy^3)",x+(x*y**3)**2,x*y**3),
       ("psi3o(x,xy^3)",x+(x*y**3)**3,x*y**3),("(x+y^2,y+x^2)",x+y**2,y+x**2),
       ("(x,x^2y^3)",x,x**2*y**3),("(x,x^2y^4)",x,x**2*y**4)]
hdr=f"{'map':18s}{'D':>3}{'N':>4}{'rho0':>5} {'E0kind':10s}{'kap':>4}{'Lam':>4}{'T':>4}{'kapnu':>6}{'Snu':>5}{'nu*':>4}{'g+':>4}{'#sat':>5}{'#nc':>4}"
print(hdr)
for t in tests:
    d=detail(*t)
    print(f"{d['nm']:18s}{d['D']:3d}{d['N']:4d}{d['rho0']:5d} {d['E0']:10s}{d['kap']:4d}{d['Lam']:4d}{d['T']:4d}{d['kap_nu']:6d}{d['S_nu']:5d}{d['numax_nc']:4d}{d['gplus']:4d}{d['nsat']:5d}{d['nnc']:4d}")
    assert d['D']==d['kap_nu']+d['S_nu'], d
    assert d['T']==(d['kap_nu']-d['kap'])+(d['S_nu']-d['Lam']), d
    assert (d['T']==0)==(d['numax_nc']<=1), d
    assert (d['T']==0)==(d['nsat']==0), d
print("\nD = kappa_nu + S_nu ; T = (kappa_nu-kappa)+(S_nu-Lam) ; T=0 <=> nu|nc == 1 <=> no satellite : ALL OK")
