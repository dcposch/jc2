#!/usr/bin/env python3
"""Full gate ledger for the case-(A) survivors + controls."""
import sys, itertools, pickle
from collections import Counter
sys.path.insert(0,'/tmp/cuspa')
from cover_h1 import (cover_h1, to_transport_convention, perm_mul, perm_inv,
                      is_transitive, fmt)
from rs_fox import rs_presentation
from snf import snf

def pid(k): return tuple(range(k))
def ppow(p,e):
    k=len(p)
    if e<0: p,e=perm_inv(p),-e
    r=pid(k)
    for _ in range(e): r=perm_mul(p,r)
    return r
def cycles(p):
    k=len(p); seen=[False]*k; out=[]
    for i in range(k):
        if not seen[i]:
            c=[i]; seen[i]=True; j=p[i]
            while j!=i: seen[j]=True; c.append(j); j=p[j]
            out.append(tuple(c))
    return out
def ctype(p): return tuple(sorted((len(c) for c in cycles(p)),reverse=True))
def nfix(p): return sum(1 for i,v in enumerate(p) if v==i)
def orbits(gens,k):
    seen=[False]*k; out=[]
    for i in range(k):
        if seen[i]: continue
        comp={i}; st=[i]; seen[i]=True
        while st:
            c=st.pop()
            for g in gens:
                t=g[c]
                if not seen[t]: seen[t]=True; comp.add(t); st.append(t)
        out.append(frozenset(comp))
    return out
def grp_order(gens,k):
    seen={pid(k)}; st=[pid(k)]
    while st:
        g=st.pop()
        for h in gens:
            x=perm_mul(h,g)
            if x not in seen: seen.add(x); st.append(x)
    return len(seen)
def ext(a,b):
    if b==0: return a,1,0
    g,x,y=ext(b,a%b); return g,y,x-(a//b)*y
def winv(w): return [-x for x in reversed(w)]

def h_ab(gens,rels):
    n=len(gens)
    M=[[0]*n for _ in rels]
    for r,rel in enumerate(rels):
        for L in rel: M[r][abs(L)-1]+= (1 if L>0 else -1)
    D,U,V,rk=snf(M)
    tors=[abs(D[i][i]) for i in range(rk) if abs(D[i][i])!=1]
    j=n-rk
    ab=[[V[k][rk+t] for t in range(j)] for k in range(n)]
    return ab,j,tors

def det_int(rows):
    import fractions
    n=len(rows); m=[[fractions.Fraction(x) for x in r] for r in rows]
    d=fractions.Fraction(1)
    for c in range(n):
        piv=None
        for i in range(c,n):
            if m[i][c]!=0: piv=i;break
        if piv is None: return 0
        if piv!=c: m[c],m[piv]=m[piv],m[c]; d=-d
        d*=m[c][c]
        inv=m[c][c]
        for i in range(c+1,n):
            f=m[i][c]/inv
            if f: m[i]=[a-f*b for a,b in zip(m[i],m[c])]
    assert d.denominator==1
    return int(d)

def full_record(A,B,p,q):
    N=len(A); z=ppow(A,p); assert z==ppow(B,q)
    kappa=1; t=z
    while t!=pid(N): t=perm_mul(z,t); kappa+=1
    M=N//kappa
    g,e,f=ext(q,p); assert g==1
    m=perm_mul(ppow(A,e),ppow(B,f)); a=nfix(m)
    blocks=orbits([z],N); bidx={}
    for i,b in enumerate(blocks):
        for x in b: bidx[x]=i
    def induced(gp):
        return tuple(bidx[gp[next(iter(b))]] for b in blocks)
    bm=induced(m); c=len(cycles(bm))
    tper=len(orbits([m,z],N))
    s=len(cycles(A)); s2=len(cycles(B))
    res=cover_h1(2,[[1]*p+[-2]*q], to_transport_convention([A,B]), N)
    j=res['free_rank']; tors=tuple(res['torsion'])
    # --- Reidemeister-Schreier + meridian classes
    P=to_transport_convention([A,B]); Pi=[perm_inv(x) for x in P]
    gens,rels,gidx,tr,rewrite = rs_presentation(P,N,[1]*p+[-2]*q)
    ab,j2,tors2 = h_ab(gens,rels)
    mw=([1]*e if e>=0 else [-1]*(-e))+([2]*f if f>=0 else [-2]*(-f))
    def actw(i,w):
        for L in w: i = P[abs(L)-1][i] if L>0 else Pi[abs(L)-1][i]
        return i
    fixed=[i for i in range(N) if actw(i,mw)==i]
    mer={}
    for i in fixed:
        r=rewrite(tr[i]+mw+winv(tr[i]),0)
        v=[0]*j2
        for L in r:
            sg=1 if L>0 else -1
            for cc in range(j2): v[cc]+=sg*ab[abs(L)-1][cc]
        mer[i]=tuple(v)
    dist=sorted(set(mer.values()))
    basis_det = det_int([list(x) for x in dist]) if len(dist)==j2 else None
    # --- control: G^ab functional consistency
    def gab(w):  # exponent sum in G^ab = Z<m>, alpha->q, beta->p
        tot=0
        for L in w: tot += (q if abs(L)==1 else p)*(1 if L>0 else -1)
        return tot
    phi_gen=[]
    for (i,gg) in gens:
        j_=P[gg][i]
        phi_gen.append(gab(tr[i])+ (q if gg==0 else p) - gab(tr[j_]))
    return dict(p=p,q=q,N=N,A=A,B=B,kappa=kappa,M=M,e=e,f=f,a=a,mer_type=ctype(m),
                alpha_t=ctype(A),beta_t=ctype(B),s=s,s2=s2,j=j,tors=tors,
                c=c,t=tper,rs_j=j2,rs_tors=tuple(tors2),ordG=grp_order([A,B],N),
                fixed=fixed,mer=mer,ndist=len(dist),dist=dist,basis_det=basis_det,
                ab=ab,phi_gen=phi_gen,gens=gens,rels=rels)

def gates(r):
    N=r['N']
    out={}
    out['kappa|a']       = (r['a'] % r['kappa'] == 0)
    out['genus0 (t=j)']  = (r['t'] == r['j'])
    out['c=j']           = (r['c'] == r['j'])
    out['a<=kappa*j']    = (r['a'] <= r['kappa']*r['j'])
    out['MERIDIAN-COUNT']= (r['ndist'] == r['j'])
    out['MERIDIAN-BASIS']= (r['ndist']==r['j'] and abs(r['basis_det'] or 0)==1)
    out['RS==cover_h1']  = (r['rs_j']==r['j'] and r['rs_tors']==r['tors'])
    return out
