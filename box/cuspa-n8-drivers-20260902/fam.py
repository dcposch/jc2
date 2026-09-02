import sys, itertools, math; sys.path.insert(0,'/tmp/cuspa')
from ledger import *
from sweep import light, rep_of
N=8
A=rep_of((6,2),N)
for D in (1,5,7,11,13):
    q=4*D; p=3
    tA=ppow(A,p); n=0; prof={}
    for B in itertools.permutations(range(N)):
        if ppow(B,q)!=tA: continue
        r=light(A,B,p,q,N)
        if r is None: continue
        n+=1
        k=(r['kappa'],r['j'],r['a'],r['t'],r['per'],r['msp'])
        prof[k]=prof.get(k,0)+1
    print("  (p,q)=(3,%d)  D=%2d  survivors=%d  %s" % (q,D,n,prof))
