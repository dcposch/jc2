"""Graded (top-band) presentation of the CQ-ELIM chart for (99,66).

Binary forms in (x,y) are dehomogenised at x=1: a form of homogeneous degree D
is a univariate poly in y of degree <= D.  Euler gives, for homogeneous A (deg a),
B (deg b):      J(A,B)|_{x=1} = a*A*B' - b*A'*B          (degree <= a+b-2).
"""
from fractions import Fraction as Fr

def pmul(A,B):
    if not A or not B: return []
    C=[Fr(0)]*(len(A)+len(B)-1)
    for i,ai in enumerate(A):
        if ai:
            for j,bj in enumerate(B):
                if bj: C[i+j]+=ai*bj
    return trim(C)
def padd(A,B):
    n=max(len(A),len(B)); C=[Fr(0)]*n
    for i,a in enumerate(A): C[i]+=a
    for i,b in enumerate(B): C[i]+=b
    return trim(C)
def pscal(c,A): return trim([Fr(c)*a for a in A])
def pder(A): return trim([A[i]*i for i in range(1,len(A))])
def trim(A):
    while A and A[-1]==0: A.pop()
    return A
def ppow(A,n):
    R=[Fr(1)]
    for _ in range(n): R=pmul(R,A)
    return R
def Jd(A,a,B,b):
    """dehomogenised Jacobian of homogeneous A (deg a) and B (deg b)"""
    return padd(pscal(a,pmul(A,pder(B))), pscal(-b,pmul(pder(A),B)))

# P0 = y^3 (y-x)^8  ->  p(y) = y^3 (y-1)^8
p = pmul(ppow([Fr(0),Fr(1)],3), ppow([Fr(-1),Fr(1)],8))
assert len(p)-1==11
P5, P6, P9 = ppow(p,5), ppow(p,6), ppow(p,9)

if __name__=="__main__":
    print("deg p =",len(p)-1, " deg P5,P6,P9 =",len(P5)-1,len(P6)-1,len(P9)-1)
    # consistency: J(Q_55,G_66) = J(lam P5, P6) must vanish identically
    print("J(P5,P6) =", Jd(P5,55,P6,66), "  (empty list = 0, band nu=0 is automatic)")
    # and the F-top consistency  G_66^3 - F_99^2 = 0
    print("G66^3 - F99^2 =", padd(ppow(P6,3), pscal(-1,ppow(P9,2))))
