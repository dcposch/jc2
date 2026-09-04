#!/usr/bin/env python3
"""Field norms N_{A_t/Q}(x) for x = a*yy + b printed by Singular as (A/B*yy+C/D) (or a rational).
N(x) = x*x' with y+y' = (t+1)/q, y*y' = (t+1)(3t+2)/(12 q^2), q=2t+1.  Also Res_y(H_t,x) = 12 q^2 N(x)."""
import re, sys
from fractions import Fraction
from math import gcd
def parse(s):
    s=s.strip().strip("()").replace(" ","")
    a=Fraction(0); b=Fraction(0)
    for term in re.findall(r"[+-]?[^+-]+", s):
        if not term: continue
        if "yy" in term:
            co=term.replace("*yy","").replace("yy","")
            if co in ("","+"): co="1"
            if co=="-": co="-1"
            a+=Fraction(co)
        else:
            b+=Fraction(term)
    return a,b
def norm(t,a,b):
    q=2*t+1; s=Fraction(t+1,q); p=Fraction((t+1)*(3*t+2),12*q*q)
    return a*a*p + a*b*s + b*b
def smallfactors(n, bound=10**6):
    n=abs(n); f={}; d=2
    while d*d<=n and d<bound:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1 if d==2 else 2
    return f, n
def describe(t, s, label):
    a,b=parse(s); N=norm(t,a,b)
    num,den=N.numerator,N.denominator
    fn,cn=smallfactors(num); fd,cd=smallfactors(den)
    print(f"{label}: a={a} b={b}")
    print(f"  N = {num}/{den}  (digits {len(str(abs(num)))}/{len(str(den))}, sign {'+' if num>0 else '-'})")
    print(f"  num small factors {fn} cofactor digits {len(str(cn))}{' (=1)' if cn==1 else ''}")
    print(f"  den small factors {fd} cofactor digits {len(str(cd))}{' (=1)' if cd==1 else ''}")
    return N
if __name__=="__main__":
    t=int(sys.argv[1]); 
    for s in sys.argv[2:]:
        describe(t,s,"x")
