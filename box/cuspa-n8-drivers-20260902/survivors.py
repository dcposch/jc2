#!/usr/bin/env python3
"""CUSP-A-N8-GATE: enumerate the N=8 case-(A) survivors and evaluate gates.

Consumes /tmp/cuspa/cover_h1.py (byte-identical copy of box/cover_h1.py).
Left-action homomorphisms throughout; converted for cover_h1.
"""
import sys, itertools, math
sys.path.insert(0, '/tmp/cuspa')
from cover_h1 import (cover_h1, to_transport_convention, perm_mul, perm_inv,
                      is_transitive, fmt)

N = 8

def pid(k=N): return tuple(range(k))
def ppow(p, e):
    k = len(p)
    if e < 0: p, e = perm_inv(p), -e
    r = pid(k)
    for _ in range(e): r = perm_mul(p, r)
    return r
def cycles(p):
    k = len(p); seen=[False]*k; out=[]
    for i in range(k):
        if not seen[i]:
            c=[i]; seen[i]=True; j=p[i]
            while j!=i: seen[j]=True; c.append(j); j=p[j]
            out.append(tuple(c))
    return out
def ctype(p): return tuple(sorted((len(c) for c in cycles(p)), reverse=True))
def nfix(p): return sum(1 for i,v in enumerate(p) if v==i)
def sign(p):
    return (-1)**(len(p)-len(cycles(p)))
def group_order(gens, k=N):
    seen={pid(k)}; stack=[pid(k)]
    while stack:
        g=stack.pop()
        for h in gens:
            x=perm_mul(h,g)
            if x not in seen: seen.add(x); stack.append(x)
    return len(seen), seen
def orbits(gens, k=N):
    seen=[False]*k; out=[]
    for i in range(k):
        if seen[i]: continue
        comp={i}; stack=[i]; seen[i]=True
        while stack:
            c=stack.pop()
            for g in gens:
                t=g[c]
                if not seen[t]: seen[t]=True; comp.add(t); stack.append(t)
        out.append(frozenset(comp))
    return out

def bezout_ef(p,q):
    """e*q + f*p = 1"""
    g,e,f = ext(q,p)
    assert g==1
    return e,f
def ext(a,b):
    if b==0: return a,1,0
    g,x,y = ext(b, a%b)
    return g, y, x-(a//b)*y

def analyse(A,B,p,q):
    """A,B left-action perms with A^p = B^q.  Return the full gate record."""
    z = ppow(A,p)
    assert z == ppow(B,q)
    kappa = 1
    t = z
    while t != pid(): t = perm_mul(z,t); kappa += 1
    M = N//kappa
    e,f = bezout_ef(p,q)
    m = perm_mul(ppow(A,e), ppow(B,f))
    a = nfix(m)
    # blocks = <z>-orbits
    blocks = orbits([z])
    assert all(len(b)==kappa for b in blocks) and len(blocks)==M
    bidx = {}
    for i,b in enumerate(blocks):
        for x in b: bidx[x]=i
    def induced(g):
        out=[None]*M
        for i,b in enumerate(blocks):
            x = next(iter(b)); out[i]=bidx[g[x]]
        return tuple(out)
    bA, bB, bm = induced(A), induced(B), induced(m)
    s  = len(cycles(A));  s2 = len(cycles(B))
    assert s == len(cycles(bA)) and s2 == len(cycles(bB))
    c = len(cycles(bm))
    t_periph = len(orbits([m,z]))
    ordG,_ = group_order([A,B])
    res = cover_h1(2, [[1]*p + [-2]*q], to_transport_convention([A,B]), N)
    j = res["free_rank"]; tors = res["torsion"]
    return dict(p=p,q=q,A=A,B=B,z=z,kappa=kappa,M=M,e=e,f=f,m=m,a=a,
                mer=ctype(m),alpha_t=ctype(A),beta_t=ctype(B),
                s=s,s2=s2,j=j,tors=tuple(tors),c=c,t=t_periph,
                bA=bA,bB=bB,bm=bm,bm_t=ctype(bm),ordG=ordG,
                h1=fmt(res))

def rep_of_type(ct, k=N):
    """canonical perm of the given cycle type"""
    p=[0]*k; base=0
    for L in ct:
        for i in range(L): p[base+i] = base+((i+1)%L)
        base+=L
    return tuple(p)

def cell(p,q,alpha_type):
    """fix alpha of the given cycle type; enumerate all beta in S_8 with A^p=B^q."""
    A = rep_of_type(alpha_type)
    tgt = ppow(A,p)
    rel=[];  surv=[]
    for B in itertools.permutations(range(N)):
        if ppow(B,q)!=tgt: continue
        rel.append(B)
        if not is_transitive([A,B],N): continue
        r = analyse(A,B,p,q)
        surv.append(r)
    return A, rel, surv

if __name__ == "__main__":
    CELLS = [((2,3),(4,4)), ((3,2),(6,2)), ((3,4),(6,2)), ((4,3),(8,))]
    allsurv={}
    for (p,q),at in CELLS:
        A,rel,surv = cell(p,q,at)
        print("### cell (p,q)=(%d,%d)  alpha fixed type %s  A=%s" % (p,q,at,A))
        print("    relation-satisfying beta: %d   transitive: %d" % (len(rel), len(surv)))
        # cheap gates + homology gate
        keep=[]
        for r in surv:
            ok_a = (2 <= r['a'] <= N-2)
            ok_h = (not r['tors']) and r['j']>=2 and r['j']<=r['a']
            ok_reg = (r['ordG'] > N)
            if ok_a and ok_h and ok_reg: keep.append(r)
        print("    after a-window + torsion-free + j<=a + nonregular: %d" % len(keep))
        from collections import Counter
        print("    profiles:", Counter((r['j'],r['a'],r['M'],r['kappa'],r['mer'],r['ordG'],
                                        r['s'],r['s2'],r['c'],r['t']) for r in keep))
        allsurv[(p,q)]=keep
    import pickle
    pickle.dump({k:[{kk:vv for kk,vv in r.items()} for r in v] for k,v in allsurv.items()},
                open('/tmp/cuspa/surv.pkl','wb'))
