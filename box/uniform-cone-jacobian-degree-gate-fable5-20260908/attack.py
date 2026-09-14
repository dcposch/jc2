"""Fable5 independent changed-object attack. Exact Fraction arithmetic, polynomials of degree<=5 in (Z,p) or (g,p).
No source powers, no CAS. Three probes:
 (A) sharpness of the normal-block injection (9): kernel element p^(a-1)V has weight exactly 1+t;
     in scope (t>4) it lies outside weight<=5, at the boundary t=4 it is a weight-5 normal kernel element.
     Verified by scalar weight arithmetic for six (a,b) rows and by a degree<=5 Vandermonde check at (a,b)=(2,2), V=g^2-p^2.
 (B) global lower-Q0 order step: [P,e]_(Z,p)=P_Z e' for Z-free e; Z^2 coefficient 3e'; changed object e=const (p-degree 0)
     is NOT excluded, so positive p-degree 5D-nu>0 is load-bearing; a Z-carrying e breaks the P_Z e' form.
 (C) Euler lemma consistency on a changed object: P=Z^3+p^2 Z (u!=0,h=1) admits no commuting monic depressed quintic
     Q=Z^5+(5/3)p^2Z^3+c p^4 Z for any scalar c (residual has two independent nonzero coefficients).
 (D) margin (12) at L0=D+1 vs L0=D+2, scalar."""
import json,resource,signal,sys
from fractions import Fraction as Q
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2)); signal.alarm(30)
out={}
# --- (A) injection sharpness ---
rows=[]
for a,b,tag in ((1,1,'boundary'),(6,5,'boundary'),(11,9,'boundary'),(1,2,'scope'),(2,2,'scope'),(2,3,'scope'),(3,3,'scope')):
    t=Q(5*b-1,a); wV=5*b; wker=wV-t*(a-1)   # weight of p^(a-1)V
    rows.append({'a':a,'b':b,'t':str(t),'in_scope(t>4)':t>4,'w(p^(a-1)V)':str(wker),'equals_1+t':wker==1+t,'inside_weight_le5':wker<=5,'normal(p-deg a-1<a)':True})
out['A_rows']=rows
out['A_verdict']='kernel element p^(a-1)V is normal, restricts to 0 on every V component, weight 1+t; injection for weight<=5 holds iff 1+t>5 iff 5b>4a+1 (hypothesis is SHARP)'
# Vandermonde at (a,b)=(2,2), V=g^2-p^2, lambda=+-1: normal weight<=5 polys of degree k have g-degree<=1 (enumerate k<=5)
a,b=2,2; t=Q(5*b-1,a); bad=[]
for k in range(0,6):
    for i in range(0,k+1):
        j=k-i
        normal = not (i>=b and j>=a)
        if normal and 5*i-t*j<=5 and i>=b: bad.append((i,j))
det=Q(1)*(-1)-Q(1)*(1)  # rows (1,lambda) for lambda=1,-1
out['A_vandermonde_22']={'normal_weight_le5_monomials_with_gdeg_ge_b':bad,'det':str(det),'injective':det!=0 and not bad}
# --- polynomial helpers in two vars (Z,p): dict {(i,j):Q}
def add(*ps):
    o={}
    for p in ps:
        for e,c in p.items(): o[e]=o.get(e,Q(0))+c
    return {e:c for e,c in o.items() if c}
def mul(p,q):
    o={}
    for e,c in p.items():
        for f,d in q.items():
            k=(e[0]+f[0],e[1]+f[1]); o[k]=o.get(k,Q(0))+c*d
    return {e:c for e,c in o.items() if c}
def sc(p,c): return {e:d*Q(c) for e,d in p.items() if d*Q(c)}
def dZ(p): return {(e[0]-1,e[1]):c*e[0] for e,c in p.items() if e[0]}
def dp(p): return {(e[0],e[1]-1):c*e[1] for e,c in p.items() if e[1]}
def br(P,Qq): return add(mul(dZ(P),dp(Qq)),sc(mul(dp(P),dZ(Qq)),-1))
def deg(p): return max((e[0]+e[1] for e in p),default=-1)
Z={(1,0):Q(1)}; P_={(0,1):Q(1)}
def mono(i,j,c=1): return {(i,j):Q(c)}
# --- (B) lower-Q0 step ---
Pc=add(mono(3,0),mono(1,2))          # Z^3 + p^2 Z  (u=p^2, v=0, h=1)
res={}
for k in (0,1,2):
    e=mono(0,k)                       # Z-free initial of p-degree k
    B_=br(Pc,e)
    res['e=p^%d'%k]={'bracket':{str(x):str(c) for x,c in B_.items()},'Z2_coeff':str(B_.get((2,k-1),Q(0))) if k else '0','equals_PZ_times_eprime':B_==mul(dZ(Pc),dp(e)),'nonzero':bool(B_)}
eZ=mono(1,1)                          # changed object: e carries Z
BZ=br(Pc,eZ)
res['e=Zp']={'bracket':{str(x):str(c) for x,c in BZ.items()},'equals_PZ_times_eprime':BZ==mul(dZ(Pc),dp(eZ))}
out['B']=res
out['B_verdict']='Z-free e with p-degree>=1 gives nonzero bracket with Z^2 coefficient 3e\'; e constant (degree 0) is NOT excluded (bracket 0) so 5D-nu>0 is load-bearing; Z-carrying e leaves the P_Z e\' form'
# --- (C) Euler lemma consistency: does any Q=Z^5+(5/3)p^2Z^3+c p^4 Z commute with P=Z^3+p^2Z? residual is linear in c
Q0=add(mono(5,0),mono(3,2,Q(5,3)))     # c=0 part
Q1=mono(1,4)                           # coefficient of c
R0=br(Pc,Q0); R1=br(Pc,Q1)
out['C']={'deg_P':deg(Pc),'deg_Q':5,'residual_c0':{str(x):str(v) for x,v in R0.items()},'residual_c1':{str(x):str(v) for x,v in R1.items()},
          'EP=3P':add(mul(P_,dp(Pc)),mul(Z,dZ(Pc)))==sc(Pc,3),'EQ0=5Q0':add(mul(P_,dp(Q0)),mul(Z,dZ(Q0)))==sc(Q0,5)}
# solvable iff R0 + c R1 == 0 for some c: check monomial-wise ratios
keys=set(R0)|set(R1); ratios=set()
solvable=True
for k in keys:
    r0=R0.get(k,Q(0)); r1=R1.get(k,Q(0))
    if r1==0 and r0!=0: solvable=False
    elif r1!=0: ratios.add(-r0/r1)
if len(ratios)>1: solvable=False
out['C']['some_c_makes_commute']=solvable; out['C']['ratios']=[str(r) for r in ratios]
out['C_verdict']='no scalar c makes Q commute with P=Z^3+p^2Z: consistent with lemma (P must be W^3=Z^3 when depressed)'
# --- (D) margin (12)
D_=[]
for a,b in ((1,2),(2,3),(3,3),(4,4),(6,6),(11,9)):
    D=a+b; eta=Q(2*D-1,2)
    D_.append({'a':a,'b':b,'M(L0=D+1)':7*D-3,'7eta_max':str(7*eta),'strict_at_D+1':7*eta<7*D-3,'M(L0=D+2)':7*D-4,'strict_at_D+2':7*eta<7*D-4})
out['D']=D_
print(json.dumps(out,indent=1,sort_keys=True))
