#!/usr/bin/env python3
"""Exact face resultants (Sylvester determinants over A_t=Q[y]/(H_t)) of the 2-dimensional facial factors:
 t=4, face {q2,q3} (the b4=0 boundary of (R_1,R_2)):  R_1|_0 = q2^2 P(q2^3,q3^2), R_2|_0 = Q(q2^3,q3^2); sigma4d = Res_{3,4}(P,Q).
 t=5, face {q2,q4}: R_2| = P2(q2^2,q4) deg 7, R_4| = P4(q2^2,q4) deg 8; Res_{7,8}(P2,P4).
 Also modular fingerprints at the certified primes."""
import sys, re
from fractions import Fraction
sys.path.insert(0,'.')
import norms
from macaulay_window import parse_ideal, terms
def parse_exact(poly, vars_):
    res={}
    for tm in terms(poly):
        m=re.match(r"([+-]?)\s*(\([^)]*\)|[0-9/]+)?\*?(.*)$", tm)
        sign, co, mon = m.group(1), m.group(2), m.group(3)
        a,b=norms.parse(co if co else "1")
        if sign=="-": a,b=-a,-b
        e=[0]*len(vars_)
        if mon:
            for f in mon.split("*"):
                if "^" in f: v,k=f.split("^"); k=int(k)
                else: v,k=f,1
                e[vars_.index(v)]+=k
        res[tuple(e)]=(a,b)
    return res
class A:
    def __init__(self,t,a,b): self.t=t; q=2*t+1; self.s=Fraction(t+1,q); self.p=Fraction((t+1)*(3*t+2),12*q*q); self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o): return A(self.t,self.a+o.a,self.b+o.b)
    def __sub__(self,o): return A(self.t,self.a-o.a,self.b-o.b)
    def __neg__(self): return A(self.t,-self.a,-self.b)
    def __mul__(self,o):
        ac=self.a*o.a; return A(self.t, ac*self.s+self.a*o.b+self.b*o.a, self.b*o.b-ac*self.p)
    def iszero(self): return self.a==0 and self.b==0
    def inv(self):
        n=norms.norm(self.t,self.a,self.b); conj=A(self.t,-self.a,self.b+self.a*self.s)  # conj(a y+b)=a y'+b, y'=s-y
        return A(self.t,conj.a/n,conj.b/n)
    def __truediv__(self,o): return self*o.inv()
    def norm(self): return norms.norm(self.t,self.a,self.b)
    def __repr__(self): return f"({self.a})*yy+({self.b})"
def det(M,t):
    # Bareiss-free: plain Gaussian elimination in the field A_t
    n=len(M); M=[row[:] for row in M]; d=A(t,0,1)
    for c in range(n):
        piv=None
        for i in range(c,n):
            if not M[i][c].iszero(): piv=i; break
        if piv is None: return A(t,0,0)
        if piv!=c: M[c],M[piv]=M[piv],M[c]; d=-d
        d=d*M[c][c]; inv=M[c][c].inv()
        for i in range(c+1,n):
            if M[i][c].iszero(): continue
            f=M[i][c]*inv
            for j in range(c,n): M[i][j]=M[i][j]-f*M[c][j]
    return d
def sylvester(P,Q,t):
    m=len(P)-1; n=len(Q)-1; N=m+n
    M=[[A(t,0,0) for _ in range(N)] for _ in range(N)]
    for i in range(n):
        for k,c in enumerate(P): M[i][i+k]=c
    for i in range(m):
        for k,c in enumerate(Q): M[n+i][i+k]=c
    return det(M,t)
def coef(P,e,t):
    a,b=P.get(tuple(e),(Fraction(0),Fraction(0))); return A(t,a,b)
# ---- t=4
t=4; vars4=["b4","q2_0","q3_0"]
polys=parse_ideal("/home/ubuntu/jc2/box/k16toptail-20260903/restop_t4_exact.sing")  # RStop[m]=R_{t-m}
R={4-m:parse_exact(pl,vars4) for m,pl in enumerate(polys,start=1)}
P=[coef(R[1],(0,11-3*k,2*k),t) for k in range(4)]   # u^{3-k} v^k, u=q2^3, v=q3^2 (times q2^2)
Q=[coef(R[2],(0,12-3*k,2*k),t) for k in range(5)]
print("t=4 P coefficients (u^3..v^3):",P); print("t=4 Q coefficients (u^4..v^4):",Q)
s4=sylvester(P,Q,t); print("t=4 sigma4d = Res_{3,4}(P,Q) =",s4); norms.describe(4,f"({s4.a}*yy+{s4.b})","N(sigma4d)")
c8=Q[4]; print("t=4 c8 = Q(0,1) =",c8)
# control: the q2-dehomogenised bivariate resultant in q3 should equal sigma4d^2 * c8^? -- skip; instead control with a modular Singular value below
# ---- t=5
t=5; vars5=["b4","q2_0","q3_0","q4_0"]
polys=parse_ideal("/home/ubuntu/jc2/box/k16toptail-20260903/restop_t5_exact.sing")
R={5-m:parse_exact(pl,vars5) for m,pl in enumerate(polys,start=1)}
P2=[coef(R[2],(0,14-2*b,0,b),t) for b in range(8)]   # u^{7-b} v^b, u=q2^2, v=q4
P4=[coef(R[4],(0,16-2*b,0,b),t) for b in range(9)]
print("t=5 P2 (deg 7):",[str(x)[:40] for x in P2]); print("t=5 P4 (deg 8):",[str(x)[:40] for x in P4])
assert not any(x.iszero() for x in P2+P4), "unexpected zero coefficient"
s5=sylvester(P2,P4,t); print("t=5 face(2,4) resultant Res_{7,8}(P2,P4) =",str(s5)[:200],"..."); norms.describe(5,f"({s5.a}*yy+{s5.b})","N(face24_t5)")
# modular fingerprints
def md(x,p,y0):
    v=(x.a.numerator*pow(x.a.denominator,-1,p)*y0 + x.b.numerator*pow(x.b.denominator,-1,p))%p
    return v if v<=p//2 else v-p
print("MOD fingerprints: t=4 sigma4d mod (32029,25378) =",md(s4,32029,25378),"; c8 =",md(c8,32029,25378))
print("MOD fingerprints: t=5 face24 mod (32009,1821) =",md(s5,32009,1821))
