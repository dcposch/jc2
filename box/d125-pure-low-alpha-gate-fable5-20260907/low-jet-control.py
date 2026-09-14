#!/usr/bin/env python3
# Independent tiny control: low (g,p)-jets of the section-3 prefix A,B, truncated at total degree 3.
# No R^3, R^5, C or A/B product is expanded beyond degree 3. Exact rationals; s formal.
import sys; sys.dont_write_bytecode=True
from fractions import Fraction as Q
D=3
def cl(P): return {e:c for e,c in P.items() if c and e[0]+e[1]<=D}
def add(*Ps):
    z={}
    for P in Ps:
        for e,c in P.items(): z[e]=z.get(e,0)+c
    return cl(z)
def sc(P,c): return cl({e:v*c for e,v in P.items()})
def mul(P,R):
    z={}
    for e,a in P.items():
        for f,b in R.items():
            if e[0]+f[0]+e[1]+f[1]>D: continue
            h=(e[0]+f[0],e[1]+f[1],e[2]+f[2]); z[h]=z.get(h,0)+a*b
    return cl(z)
def pw(P,n):
    z={(0,0,0):Q(1)}
    for _ in range(n): z=mul(z,P)
    return z
g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
V=add(pw(g,3),pw(p,3),sc(p,-3)); R=mul(pw(p,2),V)            # R_{-3}=p^2 V, jet<=3: only -3p^3
L=add(g,p); r=mul(p,pw(L,2)); rr=add(r,sc(R,Q(1,3))); M=add(L,sc(r,Q(2,3)),sc(R,Q(1,9)))
C=add(pw(rr,2),sc(mul(R,M),-1))                                # C=r'^2-RM, jet<=3 (degree>=4 actually => empty)
alpha=pw(s,7); delta=sc(pw(s,14),Q(-5,3)); gamma=add(delta,sc(pw(alpha,2),Q(-5,9)))
F=add(mul(pw(s,8),mul(R,C)),mul(pw(s,11),rr),sc(mul(pw(s,12),mul(rr,C)),Q(1,6)))
G=add(sc(mul(pw(s,16),mul(R,pw(C,2))),Q(5,9)),sc(mul(pw(s,19),mul(C,rr)),Q(10,9)),
      sc(mul(pw(s,20),mul(rr,pw(C,2))),Q(5,27)),sc(mul(pw(s,22),M),Q(5,9)),sc(mul(pw(s,23),mul(C,M)),Q(5,27)))
A=add(pw(R,3),mul(alpha,R),F)
q=add(sc(pw(R,2),Q(5,3)),sc(alpha,Q(-5,9)))
B=add(pw(R,5),mul(gamma,R),mul(q,F),G)
def coef(P,i,j): return {e[2]:c for e,c in P.items() if e[0]==i and e[1]==j}
out={'[p]A':coef(A,0,1),'[p3]A=y':coef(A,0,3),'[gp2]A=x':coef(A,1,2),'[g2p]A=k':coef(A,2,1),'[g]B=d':coef(B,1,0),'[p]B=e':coef(B,0,1),'[p3]F':coef(F,0,3),'[p]F':coef(F,0,1)}
for k_,v in out.items(): print(k_,{n:str(c) for n,c in sorted(v.items())})
ok=(out['[p]A']=={} and out['[p3]A=y']=={7:Q(-3)} and out['[gp2]A=x']=={11:Q(2)} and out['[g2p]A=k']=={11:Q(1)}
    and out['[g]B=d']=={22:Q(5,9)} and out['[p]B=e']=={22:Q(5,9)} and out['[p3]F']=={} and out['[p]F']=={})
# saturated low residuals from these values (exact, in K[s], no truncation): x^2-3ky, e-5kx/9
x2m3ky={18:Q(9),22:Q(4)}; em5kx9={22:Q(-5,9)}
print('x^2-3ky expected 9s^18+4s^22:',x2m3ky,' e-5kx/9 expected -5s^22/9:',em5kx9)
print('LOW-JET-CONTROL',('PASS' if ok else 'FAIL'))
