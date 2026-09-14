# Free-symbol 3/5 identities only; no source objects, no H/R powers, no CAS.
# Polynomials are dicts {(e_eps, e_p, e_Z): Fraction}; eps^2 is truncated to 0.
from fractions import Fraction as Fr
import sys
def add(a,b):
    r=dict(a)
    for k,v in b.items():
        r[k]=r.get(k,0)+v
        if r[k]==0: del r[k]
    return r
def mul(a,b,trunc_eps=True):
    r={}
    for (e1,p1,z1),c1 in a.items():
        for (e2,p2,z2),c2 in b.items():
            e=e1+e2
            if trunc_eps and e>=2: continue
            k=(e,p1+p2,z1+z2); r[k]=r.get(k,0)+c1*c2
            if r[k]==0: del r[k]
    return r
def d(a,i):
    r={}
    for k,c in a.items():
        if k[i]==0: continue
        kk=list(k); kk[i]-=1; r[tuple(kk)]=r.get(tuple(kk),0)+c*k[i]
    return r
def bracket(P,Q,trunc=True):  # P_Z Q_p - P_p Q_Z
    return add(mul(d(P,2),d(Q,1),trunc), {k:-v for k,v in mul(d(P,1),d(Q,2),trunc).items()})
def need(x,m):
    if not x: print("FAIL:",m); sys.exit(1)
# Astra dual-number control: P=Z^3+eps p^2 Z, Q=Z^5+(5/3)eps p^2 Z^3
P={(0,0,3):Fr(1),(1,2,1):Fr(1)}; Q={(0,0,5):Fr(1),(1,2,3):Fr(5,3)}
need(bracket(P,Q,True)=={}, "dual-number pair must commute mod eps^2")
full=bracket(P,Q,False)
need(full=={(2,3,3):Fr(-20,3)}, "untruncated bracket must be -20/3 eps^2 p^3 Z^3")
# UFD failure in the nonreduced ring: f^5 = g^3 mod eps^2 (degree 15 in the free symbol Z only)
def pw(a,n):
    r={(0,0,0):Fr(1)}
    for _ in range(n): r=mul(r,a,True)
    return r
need(pw(P,5)==pw(Q,3), "f^5 = g^3 mod eps^2")
# but P is not the cube of a monic linear Z+eps*a(p): (Z+eps a)^3 = Z^3+3 eps a Z^2 has a Z^2 term, never a Z term
# mutation control: wrong coefficient 4/3 must NOT commute
Qbad={(0,0,5):Fr(1),(1,2,3):Fr(4,3)}
need(bracket(P,Qbad,True)!={}, "mutated coefficient must fail to commute")
# root ramified 6/10 control: P=(Z^2+a p)^3, Q=(Z^2+a p)^5 with a=1 commute exactly (untruncated, no eps)
W={(0,0,2):Fr(1),(0,1,0):Fr(1)}
P6=pw(W,3); Q10=pw(W,5)
need(bracket(P6,Q10,False)=={}, "ramified common-quadratic 6/10 pair must commute")
need(bracket({(0,0,3):Fr(1),(0,2,1):Fr(1)},{(0,0,5):Fr(1),(0,2,3):Fr(5,3)},False)!={}, "reduced (eps->1) 3/5 pair must NOT commute")
print("PASS thickened controls: dual-number commutes mod eps^2; f^5=g^3 mod eps^2; ramified 6/10 commutes; reduced 3/5 control fails as required")
