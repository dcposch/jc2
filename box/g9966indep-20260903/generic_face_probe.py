import sys; sys.path.insert(0,'box/g9966indep-20260903')
import indep_engine as E
from ring import *
# generic-face cross-check: restore a single A3 coordinate A3_{98,0} (D2 deletes it,
# so this probe is run BEFORE the outer preblock) and read [x^145 y^17]J.
N=3
K3=E.build_K3(N); K2,_,_,_=E.build_K2(K3); B1,_=E.build_B1(N)
KF,KG=E.build_KFKG(K2,B1)
KF[1]=padd(KF[1],{0:var('A3_98_0')})          # t*K_A3 , slot (r,q)=(0,0)
KJ=E.build_KJ(KF,KG)
w=E.to_w(KJ[1])
print('[x^145 y^17] J  =', {str(m):str(c) for m,c in w.get(17,{}).items()})
print('[x^146 y^16] J  =', {str(m):str(c) for m,c in w.get(16,{}).items()})
