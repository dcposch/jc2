#!/usr/bin/env python3
"""Arrow 4 (Fable control): exhaustive box check of N > min(M,3m) with v at its bound (1), including
q,d = infinity and v = infinity, half-integral orders, and the equal-order case; the hand proof in the
report covers all orders, this is a consistency box only.  Mutation --allow-a-equal-j: with a=j the
strict inequality 2j+f > M fails at f=3j/2, showing a<j is load-bearing.  No Assert nodes."""
import sys, json
from fractions import Fraction as Q
mode=sys.argv[1] if len(sys.argv)>1 else ''
INF=Q(10**9)
def need(ok,msg):
    if not ok: raise ValueError(msg)
checked=0; fails=[]
for j in range(1,11):
    amax=j if mode=='--allow-a-equal-j' else j-1
    for a in range(1,amax+1):
        for m in range(j+1,2*j+6):
            for q in list(range(j+1,3*j+4))+[INF]:
                for d in list(range(j+1,3*j+4))+[INF]:
                    j_,a_,m_,q_,d_=map(Q,(j,a,m,q,d))
                    f=min(q_,j_+a_/2)
                    vmin=min(q_+min(d_,2*j_)-a_,3*m_-a_)
                    M=min(d_+f,a_/2+2*f)
                    for v in (vmin,INF):
                        N=min(j_+v,3*j_+a_/2,2*j_+f)
                        checked+=1
                        if not N>min(M,3*m_): fails.append({'j':j,'a':a,'m':m,'q':str(q),'d':str(d),'v':str(v),'f':str(f),'M':str(M),'N':str(N)})
print(json.dumps({'mode':mode or 'positive','tuples_checked':checked,'failures':len(fails),'first_failures':fails[:3]},sort_keys=True))
need(not fails,'N > min(M,3m) fails somewhere in the box')
