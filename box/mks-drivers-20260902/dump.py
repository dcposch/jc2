import sympy as sp
from tree import analyse, x, y
import sys
def dump(nm,P,Q):
    r = analyse(P,Q)
    print("===",nm,"D=%d N=%d kappa=%d Sn=%d T=%d Lam=%d Psi=%d Z.K=%d"%(r['D'],r['N'],r['kappa'],r['Sn'],r['T'],r['Lam'],r['Psi'],r['ZK1']))
    Tp={l for l,d in r['divs'].items() if d['m']>0}
    for l in sorted(r['divs'], key=lambda s:(len(s),s)):
        d=r['divs'][l]
        degT = sum(1 for o in d['adj'] if o in Tp)
        typ = 'contract' if d['c']==0 else ('DICRIT' if d['m']==0 else 'overLinf k=%d'%d['c'])
        print("  %-4s nu=%-3d m=%-4d c=%-3d self=%-3d deg=%d degT=%d adj=%s  %s"%(l,d['nu'],d['m'],d['c'],d['self'],d['deg'],degT,sorted(d['adj']),typ))
    for cl in r['cluster']:
        print("    pt %-4s a=%-3d prox=%s"%(cl['label'],cl['a'],cl['prox']))
dump("(x,y+x^2)", x, y+x**2)
dump("(x,y+x^3)", x, y+x**3)
dump("(x,xy)", x, x*y)
