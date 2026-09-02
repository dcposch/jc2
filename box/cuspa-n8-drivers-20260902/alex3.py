import sys, pickle; sys.path.insert(0,'/tmp/cuspa')
import sympy as sp
from ledger import *
from rs_fox import fox_alexander
from collections import Counter

def alex(r):
    j=r['rs_j']; tv=sp.symbols('t1:%d'%(j+1))
    A=fox_alexander(r['gens'],r['rels'],r['ab'],j,tv)
    m,n=A.shape
    mins=[sp.expand(A[:,[c for c in range(n) if c!=k]].det(method='berkowitz')) for k in range(n)]
    def clr(x):
        nu,de=sp.fraction(sp.cancel(sp.together(x))); return sp.expand(nu)
    nz=[clr(x) for x in mins if sp.simplify(x)!=0]
    if not nz: return sp.Integer(0),tv
    g=nz[0]
    for x in nz[1:]: g=sp.gcd(g,x)
    return sp.factor(g),tv

S=pickle.load(open('/tmp/cuspa/surv.pkl','rb'))
for key in [(2,3),(3,2),(3,4),(4,3)]:
    tal=Counter()
    for r0 in S[key]:
        r=full_record(r0['A'],r0['B'],r0['p'],r0['q'])
        D,tv=alex(r)
        tal[str(D)]+=1
    print("=== cell",key," Delta_1 (SNF basis of H^ab, up to units):")
    for k,v in tal.items(): print("      %2d x  %s" % (v,k))
