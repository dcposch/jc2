#!/usr/bin/env python3
"""Fable gate controls: tiny exact stdlib bookkeeping; no R^3/R^5/A15/B25/full-jet expansion."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
import hashlib,json,resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
MODE=sys.argv[1] if len(sys.argv)>1 else ''
def need(c,m):
    if not c: sys.stderr.write('FAIL '+m+'\n'); sys.exit(1)
# Laurent polys: dict exponent-tuple -> Fraction
def add(*zs):
    r={}
    for z in zs:
        for e,c in z.items():
            r[e]=r.get(e,0)+c
    return {e:c for e,c in r.items() if c!=0}
def mul(a,b):
    r={}
    for e,c in a.items():
        for f,d in b.items():
            k=tuple(x+y for x,y in zip(e,f)); r[k]=r.get(k,0)+c*d
    return {e:c for e,c in r.items() if c!=0}
def sc(z,c): return {e:c*v for e,v in z.items() if c*v!=0}
def pw(z,n,one):
    r=one
    for _ in range(n): r=mul(r,z)
    return r
out={}
# C1: lifts of the degree<=5 factors R0=pT, S, T in (u,v) Laurent; h,t0 sampled at three scalars.
def lift_ring(h,t0):
    one={(0,0):Q(1)}; u={(1,0):Q(1)}; v={(0,1):Q(1)}; vi={(0,-1):Q(1)}
    g=vi; p=add(mul(pw(v,4,one),u),sc(v,-1),sc(vi,-1))
    T=add(pw(p,4,one),mul(pw(g,3,one),p),sc(mul(g,p),h),sc(pw(p,2,one),t0),sc(one,-h))
    R0=mul(p,T); S=mul(p,add(pw(p,2,one),mul(g,p),sc(one,-1)))
    return one,u,v,vi,g,p,T,R0,S
for h,t0 in ((Q(3),Q(0)),(Q(1),Q(-2)),(Q(-2),Q(-5))):
    one,u,v,vi,g,p,T,R0,S=lift_ring(h,t0)
    need(min(e[1] for e in R0)==0 and {e:c for e,c in R0.items() if e[1]==0}=={(1,0):Q(3)},'phiR0 v-order 0 leading 3u')
    need(min(e[1] for e in T)==1 and {e:c for e,c in T.items() if e[1]==1}=={(1,1):Q(-3)},'phiT v-order 1 leading -3u')
    need(min(e[1] for e in S)==1,'phiS ordinary v-order 1')
    # C3: Q-slot lifts and negative rows
    basis=[pw(p,2,one),pw(p,4,one),mul(g,pw(p,3,one))]
    rows=[[z.get((0,-4),Q(0)) for z in basis],[z.get((0,-2),Q(0)) for z in basis]]
    need(rows==[[0,1,-1],[1,4,-3]],'negative lift matrix rows v^-4,v^-2')
    need(all(e[1] in (-4,-2) for z in basis for e in z if e[1]<0),'only v^-4,v^-2 negative rows in Q slots')
    if MODE=='--mutate-omit-low-lift': rows=rows[1:]
    # kernel of the row system on (a,b,c): expect exactly the line (-1,1,1)
    import itertools
    sols=[t for t in itertools.product(range(-3,4),repeat=3) if all(sum(r[i]*t[i] for i in range(3))==0 for r in rows)]
    need(sols==[(-3,3,3),(-2,2,2),(-1,1,1),(0,0,0),(1,-1,-1),(2,-2,-2),(3,-3,-3)],'lift kernel is exactly b(-1,1,1)')
out['C1_C3']='phiR0 leading 3u, phiT leading -3u, rows (0,1,-1)/(1,4,-3), kernel line (-1,1,1) at three (h,t0)'
# C2: Q slots from degree<=4, even, weight<=-8
slots=[(i,n-i) for n in (0,2,4) for i in range(n+1) if 5*i-7*(n-i)<=-8]
need(slots==[(0,2),(0,4),(1,3)],'Q slots p2,p4,gp3')
# C4: pure-p scalar: [p^3](R0^2 S)=-h^2 and [p^2](T Q)=-h a, univariate truncated (degree<=5 factors, mod p^6)
def utrunc(z,n): return {e:c for e,c in z.items() if e[0]<n}
for h,t0 in ((Q(3),Q(0)),(Q(1),Q(-2))):
    one={(0,):Q(1)}; p={(1,):Q(1)}
    R0={(1,):-h,(3,):t0,(5,):Q(1)}; S={(1,):Q(-1),(3,):Q(1)}; T={(0,):-h,(2,):t0,(4,):Q(1)}
    need(utrunc(mul(mul(R0,R0),S),4)=={(3,):-h*h},'[p^3] R0^2 S = -h^2')
    a=Q(7); Qp={(2,):a,(4,):Q(-7)}
    need(utrunc(mul(T,Qp),3)=={(2,):-h*a},'[p^2] T Q = -h a')
# C5: binomials and cutoffs
def binom(x,k):
    r=Q(1)
    for i in range(k): r*= (x-i)/(i+1)
    return r
need(binom(Q(5,3),2)==Q(5,9) and binom(Q(5,3),3)==Q(-5,81),'C(5/3,2)=5/9, C(5/3,3)=-5/81')
cub=binom(Q(5,3),3)*(1 if MODE=='--mutate-double-factor' else 3)
need(cub==Q(-5,27),'mixed C^2D coefficient 3*C(5/3,3)=-5/27')
for n in range(1,41):
    for j in range(1,n+1):
        need(2*j<=3*j<=Q(7*j,2)<min(6*n,3*n+j) and 4*j>Q(7*j,2),'cutoffs 2j<=3j<=7j/2<min(6n,3n+j)<... and 4j>7j/2')
        for q in range(j+1,4*j+2):
            need(2*j+q>min(2*q,3*j) and j+2*q>2*q and 3*q>2*q,'other cubic terms after first pole')
# C6: kernel exponents from origin>=1, degree 5r<=23, odd
allowed=[r for r in range(-9,10) if (r>=1 or MODE=='--mutate-origin-bound') and 5*r<=23 and r%2==1]
need(allowed==[1,3],'localized kernel exponents exactly 1,3')
# C7: formal R=g toy of (E): variables (R,S,c,d,s); R_s=R+sS; F=s^j R_s c + s^q d, j=2,q=3,L=7,a=1.
one={(0,0,0,0,0):Q(1)}; R={(1,0,0,0,0):Q(1)}; Sv={(0,1,0,0,0):Q(1)}; c={(0,0,1,0,0):Q(1)}; d={(0,0,0,1,0):Q(1)}; s={(0,0,0,0,1):Q(1)}
Ri={(-1,0,0,0,0):Q(1)}
def st(z,n): return {e:v for e,v in z.items() if e[4]<=n}
N=7
Rs=add(R,mul(s,Sv))
def Rs_inv_pow(a):  # R_s^-a truncated at s^N, moving denominator
    z=mul(s,mul(Sv,Ri))  # tau S / R with tau=s
    r={}
    for k in range(N+1): r=add(r,sc(st(pw(z,k,one),N),binom(Q(-a),k)))
    return mul(pw(Ri,a,one),r)
if MODE=='--mutate-moving-denominator':
    Rs_inv_pow=lambda a: pw(Ri,a,one)  # frozen denominator R instead of R_s
j,q=2,3
F=add(mul(pw(s,j,one),mul(Rs,c)),mul(pw(s,q,one),d))
X5={}
for l in range(4):
    Fl=st(pw(F,l,one),N)
    P=st(pw(Rs,5-3*l,one),N) if 5-3*l>=0 else Rs_inv_pow(3*l-5)
    X5=add(X5,sc(st(mul(Fl,P),N),binom(Q(5,3),l)))
neg={e:v for e,v in X5.items() if e[0]<0}
M=add(sc(mul(d,d),Q(5,9)),sc(pw(c,3,one),Q(-5,81)))
E=add(st(mul(pw(s,3*j,one),mul(M,Rs_inv_pow(1))),N),sc(st(mul(pw(s,7,one),mul(mul(c,c),mul(d,Rs_inv_pow(2)))),N),Q(-5,27)))
negE={e:v for e,v in E.items() if e[0]<0}
need(neg==negE,'negative-R part of X^5 through s^7 equals (E) exactly, moving denominators included')
need(min(e[4] for e in neg)==6,'first pole at 3j=2q=6')
need(all(e[0]>=-1 for e in neg if e[4]==6),'order 6 pole simple: M0/R0')
need(min(e[0] for e in neg if e[4]==7)==-2,'order 7 has the double pole')
c7={e:v for e,v in neg.items() if e[4]==7 and e[0]==-2}
need(c7=={(-2,0,2,1,7):Q(-5,27),(-2,1,0,2,7):Q(-5,9),(-2,1,3,0,7):Q(5,81)},'order-7 R^-2 part is -5/27 c^2 d - M0*S (moving-denominator term folded into N0)')
c6={e:v for e,v in neg.items() if e[4]==6}
need(c6=={(-1,0,0,2,6):Q(5,9),(-1,0,3,0,6):Q(-5,81)},'order-6 simple pole is M0/R0')
out['C7']='R=g toy j=2,q=3: neg part of X^5 through s^7 == (E); poles at 6 (simple, M0/R0) and 7 (double, -5/27 c^2 d/R^2)'
out['status']='PASS'; out['mode']=MODE or 'normal'; out['assert_nodes']=0
print(json.dumps(out,sort_keys=True))
