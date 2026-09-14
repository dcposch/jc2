#!/usr/bin/env python3
"""Fixed place alpha=-3/4 with D=-2 constant: solve WJ=R for the W germ over Q(sqrt(10)).
Pivot at order k>=2 must be 2(k+1)w-8/3 (report §3).  Exact, no CAS."""
import resource
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2)); resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
from fractions import Fraction as Fr
class T:  # a + b*sqrt(10)
    __slots__=('a','b')
    def __init__(s,a,b=0): s.a=Fr(a); s.b=Fr(b)
    def __add__(s,o): o=L(o); return T(s.a+o.a,s.b+o.b)
    __radd__=__add__
    def __neg__(s): return T(-s.a,-s.b)
    def __sub__(s,o): return s+(-L(o))
    def __rsub__(s,o): return L(o)+(-s)
    def __mul__(s,o): o=L(o); return T(s.a*o.a+10*s.b*o.b, s.a*o.b+s.b*o.a)
    __rmul__=__mul__
    def inv(s): n=s.a*s.a-10*s.b*s.b; return T(s.a/n,-s.b/n)
    def __truediv__(s,o): return s*L(o).inv()
    def __rtruediv__(s,o): return L(o)*s.inv()
    def __eq__(s,o): o=L(o); return s.a==o.a and s.b==o.b
    def __bool__(s): return s.a!=0 or s.b!=0
    def __repr__(s): return f"({s.a}+{s.b}*sqrt10)"
def L(o): return o if isinstance(o,T) else T(o)
M=7
def mul(p,q): return [sum((p[j]*q[i-j] for j in range(i+1)),T(0)) for i in range(M+1)]
def add(*ps): return [sum((p[i] for p in ps),T(0)) for i in range(M+1)]
def sc(c,p): return [L(c)*a for a in p]
def der(p): return [(i+1)*p[i+1] for i in range(M)]+[T(0)]
def inv(p):
    q=[T(0)]*(M+1); q[0]=1/p[0]
    for i in range(1,M+1): q[i]=-sum((p[j]*q[i-j] for j in range(1,i+1)),T(0))/p[0]
    return q
alpha=T(Fr(-3,4)); xs=[alpha,T(1)]+[T(0)]*(M-1); xi=inv(xs)
Ds=[T(-2)]+[T(0)]*M
Rs=add(sc(Fr(1,3),mul(xs,mul(Ds,Ds))),sc(-1,Ds),[T(-1)]+[T(0)]*M)
assert_ok=True
def chk(c,l):
    global assert_ok
    print(("PASS " if c else "FAIL ")+l); assert_ok = assert_ok and c
chk(Rs[0]==0 and Rs[1]==T(Fr(4,3)) and all(not c for c in Rs[2:]), "R=(4/3)(x+3/4) exactly when D=-2")
def resid(Ws):
    Js=add(sc(2,der(Ws)),sc(-1,mul(add(Ws,[T(1)]+[T(0)]*M),xi)),sc(2,Ds))
    return add(mul(Ws,Js),sc(-1,Rs)), Js
for sgn in (1,-1):
    w=T(Fr(2,3),Fr(sgn,3))          # (2 +/- sqrt10)/3
    chk(3*w*w-4*w-2==0, f"slope root 3w^2-4w-2=0, w=(2{'+' if sgn>0 else '-'}sqrt10)/3")
    Ws=[T(0),w]+[T(0)]*(M-1)
    res,Js=resid(Ws)
    chk(res[1]==0 and Js[0]==2*w-T(Fr(8,3)) and Ws[1]*Js[0]==T(Fr(4,3)), "order-1: wJ(alpha)=4/3, J(alpha)=2w-8/3 !=0")
    for k in range(2,M+1):
        r0=resid(Ws)[0][k]; Ws[k]=T(1); r1=resid(Ws)[0][k]; piv=r1-r0
        chk(piv==2*(k+1)*w-T(Fr(8,3)) and bool(piv), f"order {k}: pivot = 2(k+1)w-8/3 = {piv}, nonzero")
        Ws[k]=-r0/piv
    res,_=resid(Ws)
    chk(all(not c for c in res), f"WJ=R holds to order {M} with D=-2, w sign {sgn}")
print("ALL_FIXED_PLACE_PASS" if assert_ok else "FIXED_PLACE_FAILED")
