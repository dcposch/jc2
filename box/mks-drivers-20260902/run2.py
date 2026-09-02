import sympy as sp
from tree import analyse, Skip, x, y

def dump(nm,P,Q,short=False):
    r = analyse(P,Q)
    print("===",nm,"D=%d N=%d kappa=%d Sn=%d ell=%d xi=%d T=%d Tclass=%d Lam=%d Psi=%d Z.K=%d valE0=%d leaves=%d fork=%d numax=%d mmax=%d"%(
        r['D'],r['N'],r['kappa'],r['Sn'],r['ell'],r['xi'],r['T'],r['Tclass'],r['Lam'],r['Psi'],r['ZK1'],r['valE0'],r['leaves'],r['fork'],r['numax'],r['mmax']))
    print("   checks: Z2=N",r['Zsq']==r['N']," ZK",r['ZK1']==r['ZK2']," c",r['okc'],
          " FG",r['ZK1']==r['Psi']-r['Lam']-r['kappa']," TH",r['ZK1']==r['Theta']-r['kappa']-r['Sn'])
    lev1=[cl for cl in r['cluster'] if cl['prox']==['E0']]
    print("   level-1 a's:",[cl['a'] for cl in lev1], " sum=",sum(cl['a'] for cl in lev1), " (D=%d)"%r['D'])
    if short: return r
    Tp={l for l,d in r['divs'].items() if d['m']>0}
    for l in sorted(r['divs'], key=lambda s:(len(s),s)):
        d=r['divs'][l]
        degT = sum(1 for o in d['adj'] if o in Tp)
        typ = 'contract' if d['c']==0 else ('DICRIT' if d['m']==0 else 'overL k=%d'%d['c'])
        print("  %-4s nu=%-3d m=%-4d c=%-3d self=%-3d deg=%d degT=%d adj=%s  %s"%(l,d['nu'],d['m'],d['c'],d['self'],d['deg'],degT,sorted(d['adj']),typ))
    return r

# MOCK subrectangular pair: l(P)=(x y^2)^2, l(Q)=(x y^2)^3, u1=1,v1=2,m=2,n=3 -> D=9,e=3
dump("MOCK u1=1,v1=2,m=2,n=3", x**2*y**4 + x + y, x**3*y**6 + x**2*y + 1, short=True)
# MOCK with u1=2,v1=3,m=2,n=3 -> K=5, D=15
dump("MOCK u1=2,v1=3,m=2,n=3", x**4*y**6 + x + y, x**6*y**9 + x**2*y + 1, short=True)
dump("(x,x^2y^2)", x, x**2*y**2)
