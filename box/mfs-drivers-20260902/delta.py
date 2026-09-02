import sys; sys.path.insert(0,'/tmp/mfs')
from lib import *
from price import beta_min_B2

def min_delta(N,W,case):
    """min over admissible configs of sum_P delta_P^min  -> guaranteed lower bd on delta_aff"""
    a=N-W; Dgap=N-2*W
    if W<2 or Dgap<0 or a<1: return None
    best=None; cfg=None
    for dic in dicritical_sets(W):
        S=sum(s for s,mu in dic); L=len(dic); R=S-L
        has_s1=any(s==1 for s,mu in dic); d=W-S
        if d<1: continue
        Kt=a-1
        for m in (range(1,Kt+1) if Kt>0 else [0]):
            maxK = Dgap if case in ('B1','B2') else a
            if Kt>0 and maxK<1: continue
            for K in (partitions_into(Kt,m,maxK) if Kt>0 else [()]):
                cand=[]
                if case=='B1':
                    if m>R: continue
                    de=[]
                    for k in K:
                        mu=max(2,2+-(-k//d)); de.append(mu*(mu-1)//2)
                    while len(de)<2: de.append(1)
                    cand.append(de)
                elif case=='B2':
                    bmin=beta_min_B2(N)
                    if bmin is None: continue
                    if has_s1:
                        if m<bmin: continue
                        extra=0
                    else:
                        beta=max(bmin,m-R); extra=max(0,beta-m)
                    de=[]
                    for k in K:
                        mu=max(2,2+-(-k//d)); de.append(max(mu*(mu-1)//2,2))
                    de += [2]*extra
                    while len(de)<2: de.append(1)
                    cand.append(de)
                else:
                    de=[]
                    for k in K:
                        mu=max(2,1+-(-k//d)); de.append(mu*(mu-1)//2)
                    de=de+[1] if de else [1,1]
                    cand.append(de)
                for de in cand:
                    v=sum(de)
                    if best is None or v<best: best=v; cfg=(dic,d,tuple(K))
    return best,cfg

print("(B2)/(B3) forced lower bound on delta_aff   [death thresholds: <=3 for N<=10, <=1 for 11..16]")
print("N   W | B2 min-delta   B3 min-delta | B2 death thr | B2 route open?")
for N in range(5,17):
    for W in range(2,N//2+1):
        r2=min_delta(N,W,'B2'); r3=min_delta(N,W,'B3')
        thr = 3 if N<=10 else 1
        v2 = None if r2 is None else r2[0]
        v3 = None if r3 is None else r3[0]
        ok = '-' if v2 is None else ('KILL-ROUTE-DEAD' if v2>thr else 'open')
        print("%2d %3d | %s %s | %6d | %s"%(N,W,
             ('   -  ' if v2 is None else '%6d'%v2),('   -  ' if v3 is None else '%6d'%v3),thr,ok))
    print()
