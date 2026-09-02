#!/usr/bin/env python3
"""Alexander data of H in the MERIDIAN basis (Lemma F1), for every N=8 survivor."""
import sys, itertools, pickle
sys.path.insert(0,'/tmp/cuspa')
import sympy as sp
from cover_h1 import perm_inv, perm_mul, to_transport_convention
from rs_fox import rs_presentation, fox_alexander
from snf import snf, inv_unimodular

def h_ab(gens, rels):
    n=len(gens)
    M=[[0]*n for _ in rels]
    for r,rel in enumerate(rels):
        for L in rel: M[r][abs(L)-1] += (1 if L>0 else -1)
    D,U,V,rk = snf(M)
    tors=[abs(D[i][i]) for i in range(rk) if abs(D[i][i])!=1]
    j = n-rk
    # rows of M generate L;  U M V = D  =>  x |-> x*V  sends L to rowspace(D).
    ab = [[V[k][rk+t] for t in range(j)] for k in range(n)]
    return ab, j, tors

def winv(w): return [-x for x in reversed(w)]

def run(A,B,p,q):
    N=len(A); P=to_transport_convention([A,B]); Pi=[perm_inv(x) for x in P]
    relator=[1]*p+[-2]*q
    gens, rels, gidx, tr, rewrite = rs_presentation(P,N,relator)
    ab, j, tors = h_ab(gens,rels)
    # meridian word in G
    def ext(a,b):
        if b==0: return a,1,0
        g,x,y=ext(b,a%b); return g,y,x-(a//b)*y
    g,e,f = ext(q,p); assert g==1
    mw = ([1]*e if e>=0 else [-1]*(-e)) + ([2]*f if f>=0 else [-2]*(-f))
    # fixed sheets of the coset action
    def actw(i,w):
        for L in w: i = P[abs(L)-1][i] if L>0 else Pi[abs(L)-1][i]
        return i
    fixed=[i for i in range(N) if actw(i,mw)==i]
    mer_vec={}
    for i in fixed:
        w = tr[i] + mw + winv(tr[i])
        r = rewrite(w, 0)
        v=[0]*j
        for L in r:
            s = 1 if L>0 else -1
            for c in range(j): v[c]+= s*ab[abs(L)-1][c]
        mer_vec[i]=tuple(v)
    distinct = sorted(set(mer_vec.values()))
    return dict(j=j,tors=tors,a=len(fixed),fixed=fixed,mer_vec=mer_vec,
                distinct=distinct,gens=gens,rels=rels,ab=ab)

def change_basis(ab, j, distinct):
    """Return new ab-map in which the meridian classes are the standard basis."""
    Bm = sp.Matrix([list(v) for v in distinct])   # j x j (rows = meridians)
    d = Bm.det()
    if abs(d)!=1: return None, d
    T = Bm.inv()      # sends meridian vectors to standard basis (row vector * T)
    newab=[[int(sum(sp.Rational(ab[k][c])*T[c,t] for c in range(j))) for t in range(j)]
           for k in range(len(ab))]
    return newab, d

def alexander_from(gens,rels,ab,j):
    tv=sp.symbols('t1:%d'%(j+1))
    Amat=fox_alexander(gens,rels,ab,j,tv)
    m,n=Amat.shape
    minors=[sp.expand(Amat[:,[c for c in range(n) if c!=k]].det(method='berkowitz'))
            for k in range(n)]
    def clear(x):
        num,den=sp.fraction(sp.cancel(sp.together(x)))
        return sp.expand(num)
    nz=[clear(x) for x in minors if sp.simplify(x)!=0]
    if not nz: return sp.Integer(0), tv, minors
    g=nz[0]
    for x in nz[1:]: g=sp.gcd(g,x)
    return sp.factor(g), tv, minors

if __name__=="__main__":
    S=pickle.load(open('/tmp/cuspa/surv.pkl','rb'))
    from collections import Counter
    for key in [(2,3),(3,2),(3,4),(4,3)]:
        print("=== cell", key, " survivors:", len(S[key]))
        tally=Counter(); dtally=Counter()
        for idx,r in enumerate(S[key]):
            A,B,p,q=r['A'],r['B'],r['p'],r['q']
            info=run(A,B,p,q)
            nb, det = change_basis(info['ab'], info['j'], info['distinct'])
            partition = tuple(sorted(Counter(info['mer_vec'].values()).values(),reverse=True))
            if nb is None:
                tally[('MERIDIAN-BASIS-FAIL', det, partition)]+=1
                continue
            D,tv,mins = alexander_from(info['gens'],info['rels'],nb,info['j'])
            tally[(str(sp.factor(D)), partition, len(info['distinct']))]+=1
        for k,v in tally.items(): print("    ", v, "x ", k)
