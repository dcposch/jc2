import sys, itertools, math; sys.path.insert(0,'/tmp/cuspa')
from ledger import (pid, ppow, cycles, ctype, nfix, orbits, grp_order, ext)
from cover_h1 import cover_h1, to_transport_convention, perm_mul, perm_inv, is_transitive

def light(A,B,p,q,N):
    z=ppow(A,p)
    if z!=ppow(B,q): return None
    if not is_transitive([A,B],N): return None
    k=1; t=z
    while t!=pid(N): t=perm_mul(z,t); k+=1
    g,e,f=ext(q,p); m=perm_mul(ppow(A,e),ppow(B,f)); a=nfix(m)
    if not (2<=a<=N-2): return None
    tper=len(orbits([m,z],N))
    res=cover_h1(2,[[1]*p+[-2]*q], to_transport_convention([A,B]), N)
    if res['torsion']: return None
    j=res['free_rank']
    if not (2<=j<=a): return None
    if grp_order([A,B],N)<=N: return None      # COR 7.2 nonregular
    return dict(N=N,p=p,q=q,kappa=k,j=j,a=a,t=tper,
                per=(tper==j), msp=(j*k<=a))

def types(N):
    out=[]
    def part(n, mx, cur):
        if n==0: out.append(tuple(cur)); return
        for x in range(min(n,mx),0,-1): part(n-x,x,cur+[x])
    part(N,N,[]); return out
def rep_of(ct,N):
    p=[0]*N; b=0
    for L in ct:
        for i in range(L): p[b+i]=b+((i+1)%L)
        b+=L
    return tuple(p)

tot=0; per=0; msp=0; both=0; recs=[]
for N in (2,3,4,5,6,7):
    perms=list(itertools.permutations(range(N)))
    for p in range(2,8):
        for q in range(2,8):
            if math.gcd(p,q)!=1: continue
            for ct in types(N):
                A=rep_of(ct,N); tA=ppow(A,p)
                for B in perms:
                    if ppow(B,q)!=tA: continue
                    r=light(A,B,p,q,N)
                    if r is None: continue
                    tot+=1; per+=r['per']; msp+=r['msp']
                    if r['per'] and r['msp']: both+=1; recs.append(r)
    print("  N=%d cumulative: candidates %d ; PERIPHERAL-RANK %d ; MERIDIAN-SPAN %d ; BOTH %d"
          % (N,tot,per,msp,both))
print("FINAL: candidates %d ; both gates %d (theorem CUSP-A-VOID-II predicts 0)" % (tot,both))
