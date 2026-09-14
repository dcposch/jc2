#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,random

def add(A,B,scale=F(1),shift=0):
 C=dict(A)
 for (r,z),v in B.items():
  key=(r+shift,z);C[key]=C.get(key,F(0))+scale*v
 return {m:c for m,c in C.items() if c}
def mul(A,B,cap=None):
 C={}
 for (r,z),a in A.items():
  for (s,w),b in B.items():
   if cap is None or r+s<=cap:
    key=(r+s,z+w);C[key]=C.get(key,F(0))+a*b
 return {m:c for m,c in C.items() if c}
def trunc(A,cap):return {m:c for m,c in A.items() if m[0]<=cap}
def complete(H,v,U,R,p,q,k):
 HH=mul(H,H);Q=mul(R,HH)
 Q={m:F(3,4)*c for m,c in Q.items()}
 for A,co,sh in [(mul(mul(v,U),H),F(-1,8),1),(mul(v,R),F(1),1),
  (mul(U,U),F(-9,64),2),(mul(p,HH),F(1),4*k-2),(mul(p,v),F(1),4*k-1),(q,F(1),6*k-2)]:Q=add(Q,A,co,sh)
 return Q
def circuit(H,v,U,R,p,q,k,depth):
 minR=min((r for r,z in R),default=depth+1)
 HH=mul(H,H,max(depth-minR,depth-(4*k-2)))
 vU=mul(v,U,depth-1)
 Q={m:F(3,4)*c for m,c in mul(R,HH,depth).items()}
 for A,co,sh in [(mul(vU,H,depth-1),F(-1,8),1),(mul(v,R,depth-1),F(1),1),
  (mul(U,U,depth-2),F(-9,64),2),(mul(p,HH,depth-(4*k-2)),F(1),4*k-2),
  (mul(p,v,depth-(4*k-1)),F(1),4*k-1),(q,F(1),6*k-2)]:Q=add(Q,A,co,sh)
 return trunc(Q,depth)
rng=random.Random(990108);tests=[]
for k in (2,3,33,36):
 for depth in (0,1,4*k-3,4*k-2,4*k-1,6*k-3,6*k,6*k+2):
  for emptyR in (False,True):
   def sample(zcap):
    A={}
    for _ in range(12):
     m=(rng.choice((0,1,2,depth//2,depth,max(0,depth+1))),rng.randrange(zcap+1))
     A[m]=F(rng.randrange(-5,6),rng.randrange(1,5))
    return {m:c for m,c in A.items() if c}
   H=sample(k);v=sample(k-1);U=sample(k-1);R={} if emptyR else sample(k-1)
   p={(0,0):F(7,3)};q={(0,0):F(-11,4)}
   exact=trunc(complete(H,v,U,R,p,q,k),depth)
   emitted=circuit(H,v,U,R,p,q,k,depth)
   assert exact==emitted,(k,depth,emptyR)
   tests.append({'k':k,'depth':depth,'empty_R':emptyR,'retained_coefficients':len(exact)})
path=Path(__file__).parent/'d108/coefficient_circuit_backend_v2.py'
out={'field':'Q','result':'PASS','driver_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'seed':990108,'test_count':len(tests),'all_full_Q_coefficients_through_depth_match':True,
 'empty_R_and_pH2_boundary_included':True,'cases':tests}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
