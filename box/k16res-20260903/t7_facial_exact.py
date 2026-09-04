#!/usr/bin/env python3
"""Exact facial factors at t=7 from the exact rows (terminal box t7_rows.txt, variables b3,b4,q(2)..q(6), parameter y).
q5-axis: Q_0|=alpha_7 b3^2, Q_4|=[q5^4]c_4 * q5^4  =>  [q5^8]R_4 = alpha_7^2 * ([q5^4]T_{7,9})^2.
q6-axis: Q_0|=alpha_7 b3^2, Q_2|=[q6^3]c_2 q6^3  =>  [q6^6]R_2 = alpha_7^2 * ([q6^3]T_{7,11})^2.
q4-axis: Q_0| = alpha_7 b3^2 + [b3 q4^2]T13 b3 + [q4^4]T13 ; Q_4| = [b3^2 q4]T9 b3^2 + [b3 q4^3]T9 b3 + [q4^5]T9
         => [q4^10]R_4 = formal 2x2 resultant of these."""
import re, sys
from fractions import Fraction
sys.path.insert(0,'.')
import norms
rows={}
for line in open("/home/ubuntu/jc2/box/k16terminal-fable5-20260903/t7_rows.txt"):
    m=re.match(r"T(\d+) = (.*);$", line.strip())
    if m: rows[int(m.group(1))]=m.group(2)
def terms(poly):
    out=[]; depth=0; cur=""
    for ch in poly:
        if ch=="(": depth+=1
        if ch==")": depth-=1
        if ch in "+-" and depth==0 and cur.strip(): out.append(cur); cur=ch
        else: cur+=ch
    out.append(cur); return [x.strip() for x in out if x.strip()]
def coeff(poly, mon):
    """coefficient (a,b) with value a*y+b of the exact monomial string mon (Singular order) in poly."""
    for tm in terms(poly):
        m=re.match(r"([+-]?)\s*(\([^)]*\))?\*?(.*)$", tm)
        sign, co, mm = m.group(1), m.group(2), m.group(3)
        if mm==mon:
            a,b=norms.parse((co or "1").replace("y","yy"))
            if sign=="-": a,b=-a,-b
            return a,b
    return Fraction(0),Fraction(0)
t=7; q=15
class A:  # arithmetic in Q[y]/(H_7): y^2 = s*y - p with s=(t+1)/q, p=(t+1)(3t+2)/(12q^2)
    s=Fraction(t+1,q); p=Fraction((t+1)*(3*t+2),12*q*q)
    def __init__(self,a,b): self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o): return A(self.a+o.a,self.b+o.b)
    def __sub__(self,o): return A(self.a-o.a,self.b-o.b)
    def __mul__(self,o):
        # (a y + b)(c y + d) = ac y^2 + (ad+bc) y + bd = ac (s y - p) + ...
        ac=self.a*o.a
        return A(ac*A.s+self.a*o.b+self.b*o.a, self.b*o.b-ac*A.p)
    def norm(self): return norms.norm(t,self.a,self.b)
    def __repr__(self): return f"({self.a})*y+({self.b})"
alpha=A(*coeff(rows[13],"b3^2"))
print("alpha_7 =",alpha, " N =",alpha.norm())
c5=A(*coeff(rows[9],"q(5)^4")); print("[q5^4]T_{7,9} =",c5," N =",c5.norm())
f5=alpha*alpha*c5*c5; print("FACIAL [q5^8]R_4 = alpha^2*c^2 =",f5); norms.describe(7,f"({f5.a}*yy+{f5.b})","N([q5^8]R_4)")
c6=A(*coeff(rows[11],"q(6)^3")); print("[q6^3]T_{7,11} =",c6," N =",c6.norm())
f6=alpha*alpha*c6*c6; print("FACIAL [q6^6]R_2 = alpha^2*c^2 =",f6); norms.describe(7,f"({f6.a}*yy+{f6.b})","N([q6^6]R_2)")
# q4-axis
a0=alpha; b0=A(*coeff(rows[13],"b3*q(4)^2")); c0=A(*coeff(rows[13],"q(4)^4"))
a4=A(*coeff(rows[9],"b3^2*q(4)")); b4=A(*coeff(rows[9],"b3*q(4)^3")); c4=A(*coeff(rows[9],"q(4)^5"))
print("q4-axis Q_0|: a0,b0,c0 =",a0,b0,c0); print("q4-axis Q_4|: a4,b4,c4 =",a4,b4,c4)
R=(a0*c4-a4*c0)*(a0*c4-a4*c0)-(a0*b4-a4*b0)*(b0*c4-b4*c0)
print("FACIAL [q4^10]R_4 =",R); norms.describe(7,f"({R.a}*yy+{R.b})","N([q4^10]R_4)")
# modular fingerprints at p=32059, y=4425 for comparison with t7_pieces output
p=32059; y0=4425
def md(x): 
    v=(x.a.numerator*pow(x.a.denominator,-1,p)*y0 + x.b.numerator*pow(x.b.denominator,-1,p))%p
    return v if v<=p//2 else v-p
print("MOD p=32059 y=4425: [q5^8]R_4 =",md(f5)," [q6^6]R_2 =",md(f6)," [q4^10]R_4 =",md(R), " alpha_7 =",md(alpha))
