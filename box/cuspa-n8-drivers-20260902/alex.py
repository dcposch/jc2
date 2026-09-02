#!/usr/bin/env python3
import sys, itertools, pickle
sys.path.insert(0,'/tmp/cuspa')
import sympy as sp
from cover_h1 import perm_inv, perm_mul, to_transport_convention
from rs_fox import schreier, rs_presentation, abelianization, fox_alexander
from snf import snf, inv_unimodular

def h_abelian_map(gens, rels):
    n=len(gens)
    M=[[0]*n for _ in rels]
    for r,rel in enumerate(rels):
        for L in rel: M[r][abs(L)-1] += (1 if L>0 else -1)
    D,U,V,rk = snf(M)
    tors=[abs(D[i][i]) for i in range(rk) if abs(D[i][i])!=1]
    Vi = inv_unimodular(V)          # y = Vi * x
    j = n - rk
    ab = [[Vi[rk+t][k] for t in range(j)] for k in range(n)]
    return ab, j, tors

def alexander(A,B,p,q,verbose=True):
    N=len(A)
    P = to_transport_convention([A,B])
    relator = [1]*p + [-2]*q
    gens, rels, gidx, tr, rewrite = rs_presentation(P, N, relator)
    ab, j, tors = h_abelian_map(gens, rels)
    tv = sp.symbols('t1:%d'%(j+1))
    Amat = fox_alexander(gens, rels, ab, j, tv)
    m,n = Amat.shape
    assert n == m+1, (m,n)
    minors=[]
    for skip in range(n):
        cols=[c for c in range(n) if c!=skip]
        minors.append(sp.factor(sp.expand(Amat[:,cols].det(method='berkowitz'))))
    # gcd of the minors as Laurent polys: clear monomials, take polynomial gcd
    def clear(e):
        e=sp.together(sp.expand(e))
        num,den = sp.fraction(sp.cancel(e))
        return sp.expand(num)
    ms=[clear(x) for x in minors if sp.simplify(x)!=0]
    g = ms[0]
    for x in ms[1:]:
        g = sp.gcd(g,x)
    return dict(j=j, tors=tors, ngen=n, nrel=m, minors=minors, delta=sp.factor(g),
                tvars=tv, Amat=Amat, ab=ab, gens=gens, rels=rels)

if __name__=="__main__":
    S=pickle.load(open('/tmp/cuspa/surv.pkl','rb'))
    for key in [(2,3),(3,4),(4,3)]:
        r=S[key][0]
        A,B,p,q = r['A'],r['B'],r['p'],r['q']
        out=alexander(A,B,p,q)
        print("=== cell (p,q)=%s  A=%s B=%s" % (key,A,B))
        print("    H^ab = Z^%d  torsion %s ; presentation %d gens / %d rels"
              % (out['j'], out['tors'], out['ngen'], out['nrel']))
        print("    Delta_1 =", out['delta'])
        for i,mn in enumerate(out['minors']):
            print("      minor omit col %d : %s" % (i, sp.factor(mn)))
