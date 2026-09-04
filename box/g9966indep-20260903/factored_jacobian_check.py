import sys,time; sys.path.insert(0,'box/g9966indep-20260903')
import indep_engine as E
from ring import *
N=5
K3=E.build_K3(N); K2,_,_,_=E.build_K2(K3); B1,_=E.build_B1(N)
KF,KG=E.build_KFKG(K2,B1)
KJa=E.build_KJ(KF,KG); KJb=E.build_KJ_factored(KF,B1,K2)
ok=True
for a in range(N):
    d=padd(KJa[a],psmul(KJb[a],-1))
    if d: ok=False; print('MISMATCH t^%d'%a, {k:len(v) for k,v in d.items()})
print('factored KJ identity holds:',ok)
