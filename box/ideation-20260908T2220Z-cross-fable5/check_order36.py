# Cross-lane tiny control: reproduces Fable blind §3 identity 10*P_Y*Q - 6*P*Q_Y for
# P=S^3+uY+v, Q=S^5+(5/3)S^2(uY+v)+e, S=Y^2+b over Q, free symbols (Y,u,v,e,b),
# and checks (t-1)^2+1 = 3*rho, t^2 = rho in Q(rho), rho^2=3rho-1, t=1-rho.
# stdlib only; run: python3 -I -B check_order36.py  (cap: 30 s wall, 25 s CPU, 512 MiB)
from fractions import Fraction as Fr
def add(a,b):
    r=dict(a)
    for k,c in b.items():
        r[k]=r.get(k,0)+c
        if r[k]==0: del r[k]
    return r
def mul(a,b):
    r={}
    for k1,c1 in a.items():
        for k2,c2 in b.items():
            k=tuple(x+y for x,y in zip(k1,k2)); r[k]=r.get(k,0)+c1*c2
            if r[k]==0: del r[k]
    return r
def sc(a,s): return {k:c*s for k,c in a.items()}
def dY(a):
    r={}
    for k,c in a.items():
        if k[0]>0: r[(k[0]-1,)+k[1:]]=c*k[0]
    return r
def var(i):
    k=[0]*5;k[i]=1;return {tuple(k):Fr(1)}
Y,u,v,e,b=[var(i) for i in range(5)]
one={(0,0,0,0,0):Fr(1)}
S=add(mul(Y,Y),b)
def pw(a,n):
    r=one
    for _ in range(n): r=mul(r,a)
    return r
lin=add(mul(u,Y),v)
P=add(pw(S,3),lin)
Q=add(add(pw(S,5),sc(mul(pw(S,2),lin),Fr(5,3))),e)
Br=add(sc(mul(dY(P),Q),10),sc(mul(P,dY(Q)),-6))
byY={}
for k,c in Br.items(): byY.setdefault(k[0],{})[k[1:]]=c
for d in sorted(byY,reverse=True):
    print('Y^%d:'%d, {k:str(c) for k,c in byY[d].items()})
# expected (Fable blind display): Y^5: 60e-(100/3)u^2 ; Y^4: -(220/3)uv ; Y^3: 120eb-(80/3)bu^2-40v^2 ;
# Y^2: -(200/3)buv ; Y^1: 60eb^2+(20/3)b^2u^2-40bv^2 ; Y^0: (20/3)b^2uv+10ue
exp={5:{(0,0,1,0):Fr(60),(2,0,0,0):Fr(-100,3)},4:{(1,1,0,0):Fr(-220,3)},
     3:{(0,0,1,1):Fr(120),(2,0,0,1):Fr(-80,3),(0,2,0,0):Fr(-40)},2:{(1,1,0,1):Fr(-200,3)},
     1:{(0,0,1,2):Fr(60),(2,0,0,2):Fr(20,3),(0,2,0,1):Fr(-40)},0:{(1,1,0,2):Fr(20,3),(1,0,1,0):Fr(10)}}
assert byY==exp, 'MISMATCH with Fable display'
def qm(x,y):
    a,b=x;c,d=y
    return (a*c - b*d, a*d+b*c+3*b*d)
t=(1,-1); tm1=(0,-1)
sq=qm(tm1,tm1); val=(sq[0]+1,sq[1])
assert val==(0,3) and qm(t,t)==(0,1)
print('(t-1)^2+1 =',val,'= 3rho ;  t^2 =',qm(t,t),'= rho ; ALL CHECKS PASS')
# negative control: a wrong bracket normalization (6 P_Y Q - 10 P Q_Y) must NOT match
Bw=add(sc(mul(dY(P),Q),6),sc(mul(P,dY(Q)),-10))
byW={}
for k,c in Bw.items(): byW.setdefault(k[0],{})[k[1:]]=c
assert byW!=exp; print('negative control (swapped 10/6 normalization) differs: OK')
