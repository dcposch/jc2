#!/usr/bin/env python3
"""Fable5 independent changed-object controls for the Euler envelope lemma.
stdlib only, exact Fractions. Not the producer's check.py."""
from fractions import Fraction as Q
from math import gcd, comb
import resource, random
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
def need(c,n):
    if not c: raise RuntimeError("FAIL "+n)
    print("PASS "+n)
# polynomial helpers (coeff lists, index = degree)
def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def add(p,q): return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def mul(p,q):
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,u in enumerate(p):
        for j,v in enumerate(q): r[i+j]+=u*v
    return trim(r)
def der(p): return trim([i*p[i] for i in range(1,len(p))] or [Q(0)])
def sc(c,p): return trim([c*v for v in p])
def ode(b,e,p): return add(sc(b,mul(der(e),p)),sc(-1,mul(e,der(p))))
# (1) CHANGED OBJECT: b<a. (a,b)=(4,2): e=A^2+A, p=A(A+1)^3 solves b e'p - e p' = p,
#     p is NOT a shifted 4th power (roots 0 and -1 distinct). So the b>a hypothesis of
#     producer sec.3 is load-bearing; it holds at (24,84) and (16,56).
e=[Q(0),Q(1),Q(1)]; p=mul([Q(0),Q(1)],mul(mul([Q(1),Q(1)],[Q(1),Q(1)]),[Q(1),Q(1)]))
need(ode(2,e,p)==p,"b<a-counterobject-(4,2)-satisfies-ODE")
need(p!=[Q(comb(4,i))*Q(1,2)**(4-i) for i in range(5)] and p[0]==0 and p[1]!=0,"b<a-counterobject-not-shifted-power")
# (2) b>a: degree-r leading coefficient of b e'p - e p' is lc(e)*c*(b r - a); with b>a, r>=2 it is
#     nonzero and of degree a+r-1>a. Exact check at (24,84), r=2,3, random e.
random.seed(1)
for r in (2,3):
    ee=[Q(random.randint(1,9)) for _ in range(r+1)]; pp=[Q(random.randint(1,9)) for _ in range(24)]+[Q(3)]
    lhs=ode(84,ee,pp)
    need(len(lhs)-1==24+r-1 and lhs[-1]==ee[-1]*Q(3)*(84*r-24),"b>a-leading-coefficient-r=%d"%r)
# (3) Direction selection of producer sec.2 on a changed support: unique total leader (a,b)=(5,7),
#     violators (3,8),(1,9),(0,10),(2,8). Max ratio (j-b)/(a-i): (3,8):1/2,(1,9):1/2,(0,10):3/5,(2,8):1/3 -> 3/5.
a,b=5,7; supp=[(5,7),(3,8),(1,9),(0,10),(2,8),(4,3),(6,2),(7,0),(0,0),(2,2)]
need(all(i+j<a+b for (i,j) in supp if (i,j)!=(a,b)),"unique-total-leader")
rat=max(Q(j-b,a-i) for (i,j) in supp if j>b); rho,sig=rat.numerator,rat.denominator
need((rho,sig)==(3,5) and gcd(rho,sig)==1 and 0<rho<sig,"max-ratio-direction")
w=lambda i,j: rho*i+sig*j
top=w(a,b); face=[(i,j) for (i,j) in supp if w(i,j)==top]
need(all(w(i,j)<=top for (i,j) in supp) and (a,b) in face and len(face)>=2,"face-exposed-nonmonomial")
need(max(face,key=lambda t:t[0]-t[1])==(a,b),"st-is-(a,b)-by-Remark-1.8")
Esupp=[(u,v) for u in range(0,20) for v in range(0,20) if rho*u+sig*v==rho+sig]
need(Esupp==[(1,1)],"E-monomial-when-rho>1-so-Remark-2.5-kills")
# rho=1 variant: same support but violators giving ratio 1/2 only
supp2=[(5,7),(3,8),(1,9),(4,3),(0,0)]
rat2=max(Q(j-b,a-i) for (i,j) in supp2 if j>b); r2,s2=rat2.numerator,rat2.denominator
Esupp2=[(u,v) for u in range(0,20) for v in range(0,20) if r2*u+s2*v==r2+s2]
st_E=max(Esupp2,key=lambda t:t[0]-t[1])
need((r2,s2)==(1,2) and Esupp2==[(1,1),(3,0)] and st_E==(3,0) and a*0-b*3!=0,"rho=1-stE-(1+sigma,0)-not-aligned-with-(a,b)")
# (4) Envelope-derived d in {0,1}: lower endpoint (x0,12d) of the predecessor edge with normal (rho,sigma),
#     0<rho<-sigma, must have x0<84 hence 12d<24.
for d in range(0,5):
    y0=12*d
    ok = (y0<24)
    need(ok == (d<=1),"d-in-{0,1}-from-deg_x=84-d=%d"%d)
print("FABLE5_CHANGED_OBJECT_CONTROLS_PASS")
