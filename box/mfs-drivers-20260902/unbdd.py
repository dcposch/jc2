# Control: does LOC-MULT (new) bound delta_aff in any cell?  Add k nodes with K=0.
import sys; sys.path.insert(0,'/tmp/mfs')
from lib import n_from_delta
rows=[]
for (N,a,W,S) in [(4,2,2,1),(5,3,2,1),(8,6,2,1),(10,5,5,1),(12,10,2,1),(16,8,8,1),(20,18,2,1)]:
    d=W-S; Kt=a-1
    for k in [1,10,10**3,10**6]:
        # cusp carries all of K ; k nodes carry K=0
        mult_c=max(2,1+-(-Kt//d)); mults=[mult_c]+[2]*k
        deltas=[mult_c*(mult_c-1)//2]+[1]*k
        # ledger checks (DG 5.1) : (K) sum=a-1 ; (L) a_p>=0 ; (C1) r*W<=N ; (C3) #{K>0}=1<=R+beta=0+1
        okK = Kt == Kt
        okL = (a-Kt>=0) and (a-(2-1)*W-0>=0)
        okC1 = 2*W<=N
        D=sum(deltas)
        rows.append((N,a,W,k,mult_c,D,n_from_delta(D),okK and okL and okC1))
print("N   a  W      k  mult_c   delta_aff  n_floor(delta)  ledger-OK")
for r in rows: print("%2d %3d %2d %7d %5d %11d %10d      %s"%r)
