#!/usr/bin/env python3
"""Tiny exact controls for a theorem-based interface; no solver or CAS."""
from fractions import Fraction as Q
from math import comb
import resource

resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))

def need(c, name):
    if not c:
        raise RuntimeError("CHECK_FAILED: " + name)
    print("PASS " + name)

def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(p,q):
    return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
                 for i in range(max(len(p),len(q)))])

def scale(c,p):
    return trim([c*v for v in p])

def mul(p,q):
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,u in enumerate(p):
        for j,v in enumerate(q):
            r[i+j]+=u*v
    return trim(r)

def der(p):
    return trim([i*p[i] for i in range(1,len(p))] or [Q(0)])

def power(a,s):
    return [Q(comb(a,i))*s**(a-i) for i in range(a+1)]

def shift(p,s):
    r=[Q(0)]
    for i,v in enumerate(p):
        r=add(r,scale(v,power(i,s)))
    return r

a,b=24,84
s=Q(7,5)
p=power(a,s)
q=power(16,s)
e=[s/Q(b-a),Q(1,b-a)]
need(add(scale(b,mul(der(e),p)),scale(-1,mul(e,der(p))))==p,
     "vertical-Euler-sign-and-constant")
need(add(scale(56,mul(der(p),q)),scale(-84,mul(p,der(q))))==[0],
     "common-root-bracket")
badq=power(16,s+1)
need(add(scale(56,mul(der(p),badq)),scale(-84,mul(p,der(badq))))!=[0],
     "different-root-mutation-rejected")
need(shift(p,-s)==[Q(0)]*24+[Q(1)] and shift(q,-s)==[Q(0)]*16+[Q(1)],
     "simultaneous-translation-sign")
need(Q(85-84,24-22)==Q(1,2) and 24+2*84==22+2*85
     and 22+85<24+84, "exposed-upper-edge-control")
need([(i,j) for i in range(6) for j in range(6) if i+2*j==3]
     ==[(1,1),(3,0)], "positive-weight-E-support")
need([(i,j) for i in range(6) for j in range(6) if 2*i+3*j==5]
     ==[(1,1)], "nonintegral-pure-power-case")
need(24*0-84*3!=0, "start-endpoint-nonalignment")

for r in [2,3]:
    face={(r+k,4*k):Q(comb(7*r,k))*(-1)**(7*r-k)
          for k in range(7*r+1)}
    translated={}
    for (i,j),c in face.items():
        for z in range(i+1):
            key=(z,j)
            translated[key]=translated.get(key,Q(0))+c*comb(i,z)*(-s)**(i-z)
    translated={key:c for key,c in translated.items() if c}
    need({key:c for key,c in translated.items() if 4*key[0]-key[1]==4*r}==face,
         "fixed-4-minus1-face-power-"+str(r))
    need({key:c for key,c in translated.items() if sum(key)==36*r}
         =={(8*r,28*r):Q(1)}, "unique-total-leader-power-"+str(r))

print("ALL_EXACT_CONTROLS_PASS")
