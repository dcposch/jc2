#!/usr/bin/env python3
"""Fixed coefficient-field blocks only; never expands A-dependent forcing."""
from fractions import Fraction as F
import json
import sys

def req(ok,msg):
    if not ok: raise ValueError(msg)
Z=(F(0),F(0)); O=(F(1),F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sc(x,a): return (x[0]*a,x[1]*a)
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d,a*d+b*c+3*b*d)
def inv(x):
    a,b=x; n=a*a+3*a*b+b*b
    req(n!=0,"coefficient-field unit")
    return ((a+3*b)/n,-b/n)
def power(x,n):
    z=O
    for _ in range(n): z=mul(z,x)
    return z
def enc(x): return [[x[0].numerator,x[0].denominator],[x[1].numerator,x[1].denominator]]
def conv(p,q):
    out=[Z]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]=add(out[i+j],mul(a,b))
    return out
def ppow(p,n):
    out=[O]
    for _ in range(n): out=conv(out,p)
    return out
def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def pts(poly):
    es=list(zip(poly,poly[1:]+poly[:1]))
    out=[]
    for i in range(max(x for x,y in poly)+1):
        for j in range(max(y for x,y in poly)+1):
            cs=[cross(a,b,(i,j)) for a,b in es]
            if all(c>=0 for c in cs) or all(c<=0 for c in cs): out.append((i,j))
    return out
cases={
"unequal":{"A":[(0,0),(0,15),(9,6),(2,1)],"B":[(0,0),(0,25),(15,10),(1,0)],"normal":(5,-7),"wa":3,"wb":5},
"common3":{"A":[(0,0),(0,15),(9,6),(3,0)],"B":[(0,0),(0,25),(15,10),(5,0)],"normal":(1,-1),"wa":3,"wb":5},
"common4":{"A":[(0,0),(0,15),(9,6),(9,0)],"B":[(0,0),(0,25),(15,10),(15,0)],"normal":(1,0),"wa":9,"wb":15}}
def qformula(case,d):
    if case=="unequal": return (7*d+4)//12
    if case=="common3": return min(d,(d+4)//2)
    return min(d,14)
H={"rational":[O,Z,Z,O],"golden":[O,(F(3),F(-2)),(F(2),F(-1)),(F(0),F(1))]}
def normweight(ij,n): return ij[0]*n[0]+ij[1]*n[1]
def L(h,d,c):
    out=[Z]*(d+14)
    for i,ci in enumerate(c):
        for p,hp in enumerate(h):
            r=p+i-1
            if r>=0: out[r]=add(out[r],sc(mul(hp,ci),p*d-15*i))
    return out
def mod(x,rho=24,p=101):
    a,b=x
    return (a.numerator*pow(a.denominator,-1,p)+rho*b.numerator*pow(b.denominator,-1,p))%p
def rank_mod(h,d,q):
    m=[]
    for r in range(d+14):
        row=[]
        for i in range(q+1):
            p=r+1-i
            row.append(mod(sc(h[p],p*d-15*i)) if 0<=p<len(h) else 0)
        m.append(row)
    rank=0
    for c in range(q+1):
        ix=next((i for i in range(rank,len(m)) if m[i][c]),None)
        if ix is None: continue
        m[rank],m[ix]=m[ix],m[rank]
        u=pow(m[rank][c],-1,101); m[rank]=[(v*u)%101 for v in m[rank]]
        for i in range(rank+1,len(m)):
            f=m[i][c]
            if f: m[i]=[(a-f*b)%101 for a,b in zip(m[i],m[rank])]
        rank+=1
    return rank
data={}; tables={}
for case,info in cases.items():
    ap=pts(info["A"]); bp=pts(info["B"]); n=info["normal"]
    req(set(ap)<=set(bp),"gauge support inclusion")
    req(max(normweight(v,n) for v in ap)<info["wb"],"gauge strictly below B inner face")
    fa=[v for v in ap if v!=(0,0) and sum(v)!=15 and normweight(v,n)!=info["wa"]]
    fb=[v for v in bp if v!=(0,0) and sum(v)!=25 and normweight(v,n)!=info["wb"]]
    req(len(fa)=={"unequal":71,"common3":77,"common4":98}[case],"free A count")
    req(len(fb)=={"unequal":196,"common3":214,"common4":269}[case],"free B count")
    tabs=[]
    for d in range(1,25):
        q=qformula(case,d)
        cols=[i for i in range(d+1) if (i,d-i) in fb]
        req(cols==list(range(q+1)),"literal free homogeneous columns")
        tabs.append([d,q+1,q+1-int(d%5==0)])
    tables[case]=tabs; data[case]={}
    for branch,h0 in H.items():
        h=ppow(h0,3); witnesses=[]
        for d,q1,rank in tabs:
            q=q1-1; C=[O]
            for i in range(1,q+1):
                s=Z
                for j in range(i):
                    p=i-j
                    if p<len(h): s=add(s,sc(mul(h[p],C[j]),p*d-15*j))
                C.append(sc(s,F(1,15*i)))
            image=L(h,d,C)
            req(all(v==Z for v in image[:q]),"literal rational triangular recurrence")
            if d%5==0:
                kernel=ppow(h0,d//5)+[Z]*(q+1-len(ppow(h0,d//5)))
                req(C==kernel and all(v==Z for v in image),"restricted kernel H power")
                r=None; schur=Z
            else:
                r=next((i for i in range(q,len(image)) if image[i]!=Z),None)
                req(r is not None,"nonzero exact extra pivot")
                schur=image[r]
                req(mul(schur,inv(schur))==O,"fixed Schur inverse")
            req(rank_mod(h,d,q)==rank,"independent mod101 rank")
            det=O
            for i in range(1,q+1): det=sc(det,-15*i)
            if r is not None: det=mul(det,schur)
            witnesses.append({"d":d,"columns":q+1,"rank":rank,"triangular_rows":list(range(q)),"extra_row":r,"schur":enc(schur),"nonzero_minor":enc(det)})
        data[case][branch]=witnesses
    req(sum(r for d,n,r in tabs)==len(fb)-4,"four kernel slots only")
# Scalar physical-variable bracket control of target shear and fixed origin.
def padd(p,q):
    z=p.copy()
    for e,c in q.items(): z[e]=z.get(e,F(0))+c
    return {e:c for e,c in z.items() if c}
def pscale(p,c): return {e:a*c for e,a in p.items() if a*c}
def bracket(p,q):
    z={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            c=(i*l-j*k)*a*b
            if c: z=padd(z,{(i+k-1,j+l-1):c})
    return z
aa={(0,15):F(1),(2,1):F(2),(0,4):F(3)}
bb={(0,25):F(1),(0,15):F(7),(1,0):F(5)}
ss=bb[(0,15)]; bb1=padd(bb,pscale(aa,-ss))
req(bb1.get((0,15),0)==0 and bracket(aa,bb1)==bracket(aa,bb),"literal target gauge")
req((0,0) not in bb1 and padd(bb1,pscale(aa,ss))==bb,"gauge inverse and fixed origin")
# Negative-lift row sets: Q contains every P row needed for the row operation.
LP={(t,e) for t in range(3) for e in range(5*t-15,0)}
LQ={(t,e) for t in range(5) for e in range(5*t-25,0)}
req(LP<=LQ,"all lift rows stable under target shear")
if "--mutate" in sys.argv:
    # Actual replacement H=pi^5 violates primitivity; the same rank check fails.
    h=[O]
    req(rank_mod(h,24,14)==15,"injected nonprimitive quintic")
if "--mutate-kernel" in sys.argv:
    bad=[O]*4
    req(all(v==Z for v in L(ppow(H["golden"],3),5,bad)),"injected false homogeneous kernel")
print(json.dumps({"status":"PASS","tables":tables,"witnesses":data,"max_matrix_rows":38,"max_matrix_columns":15,"field":"Q or Q[rho]/(rho^2-3rho+1)","mod_check":{"p":101,"rho":24},"no_A_dependent_forcing_expanded":True},sort_keys=True))
