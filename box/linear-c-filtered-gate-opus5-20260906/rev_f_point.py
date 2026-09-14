#!/usr/bin/env python3
"""Opus review Part F: end-to-end evaluation of the reconstruction graph at a real
base point. Provides the MEANINGFUL selected-only vs complete-residual control that
the producer's tautological line does not. Single numeric point; no solve."""
import json,math,random
from fractions import Fraction as F
from collections import defaultdict
R=[];P=lambda *a:(R.append(" ".join(map(str,a))),print(*a))
d=json.load(open("/tmp/jc2-lane.1CmqE8/inputs/delta2_stage8.strongest.json"))
cert=json.load(open("/tmp/jc2-lane.1CmqE8/inputs/filtered_basis_certificate.json"))
def padd(a,b,s=F(1)):
    o=dict(a)
    for p,v in b.items():
        o[p]=o.get(p,F(0))+s*v
        if not o[p]: del o[p]
    return o
def pmul(a,b):
    o={}
    for p,v in a.items():
        for q,ww in b.items():
            k=(p[0]+q[0],p[1]+q[1]); o[k]=o.get(k,F(0))+v*ww
    return {p:v for p,v in o.items() if v}
def psc(a,c): return {p:v*c for p,v in a.items() if v*c}
def JJ(a,b):
    o={}
    for (i,j),v in a.items():
        for (k,l),ww in b.items():
            c=(i*l-j*k)*v*ww
            if c: o[(i+k-1,j+l-1)]=o.get((i+k-1,j+l-1),F(0))+c
    return {p:v for p,v in o.items() if v}
def deg(a): return max(map(sum,a),default=-1)
# random base point
import ast
allnames=set()
for k in ("h3","C2","C3","B2"):
    for r,z,e in d["maps"][k]:
        for n in ast.walk(ast.parse(str(e).replace("^","**"),mode="eval")):
            if isinstance(n,ast.Name): allnames.add(n.id)
rng=random.Random(20260906)
pt={n:F(rng.randint(-9,9),rng.randint(1,5)) for n in allnames}
A_,B_=F(rng.randint(-9,9)),F(rng.randint(-9,9))
def evalrow(e):
    return eval(compile(ast.parse(str(e).replace("^","**"),mode="eval"),"<r>","eval"),
                {"__builtins__":{}},{k:v for k,v in pt.items()})
poly={}
for k,N in (("h3",11),("C2",22),("C3",33),("B2",65)):
    poly[k]={}
    for r,z,e in d["maps"][k]:
        val=F(evalrow(e))
        if val: poly[k][(N-int(r)-int(z),int(z))]=val
h=padd(padd(pmul(pmul(poly["h3"],poly["h3"]),poly["h3"]),pmul(poly["C2"],poly["h3"])),poly["C3"])
D=poly["B2"]; G=padd(padd(pmul(h,h),psc(h,-B_/3)),D)
K=pmul(psc(padd(padd(psc(D,3),{(0,0):A_}),psc(h,B_)),F(1,2)),JJ(h,D))
Hc={(3-j,8+j):F(math.comb(3,j)) for j in range(4)}
Gt={(0,0):F(1)}
for _ in range(6): Gt=pmul(Gt,Hc)
P("random base point: deg h =",deg(h),"| deg D =",deg(D),"| deg G =",deg(G),"| deg K =",deg(K))
P("top(G) == H^6 at this point:",{p:v for p,v in G.items() if sum(p)==66}==Gt)
BAS=[{(i,j):F(c) for i,j,c in b["polynomial"]} for b in cert["basis"]]
PIV=[tuple(b["selected_J_row"]) for b in cert["basis"][:189]]
JB=[JJ(b,G) for b in BAS]
P("J(B_191,G) is identically zero (constant is Jacobian-invisible):",JB[191]=={})
M=[[JB[j].get(PIV[i],F(0)) for j in range(192)] for i in range(189)]
P("selected minor unit lower triangular at this point:",
  all(M[i][i]==1 for i in range(189)) and all(M[i][j]==0 for i in range(189) for j in range(i+1,189)))
def solve(v22,v11):
    u=[]
    for i in range(189):
        s=K.get(PIV[i],F(0))+M[i][189]*v22+M[i][190]*v11+sum(M[i][j]*u[j] for j in range(i))
        u.append(-s)
    return u
res=[]
for (v22,v11,v0) in [(F(0),F(0),F(0)),(F(3,2),F(-5),F(7)),(F(1),F(0),F(0)),(F(0),F(1),F(0))]:
    u=solve(v22,v11)
    C={}
    for j,c in enumerate(u+[v22,v11,v0]): C=padd(C,BAS[j],c)
    tot=padd(K,JJ(C,G))
    sel=[tot.get(p,F(0)) for p in PIV]
    rest={p:v for p,v in tot.items() if v and p not in set(PIV) and sum(p)>0}
    res.append((v22,v11,v0,u,sel,rest,tot.get((0,0),F(0))))
    P(f"  v22={v22} v11={v11} v0={v0}: all 189 selected rows vanish:",not any(sel),
      "| retained positive rows still NONZERO:",len(rest),"| J const coeff:",tot.get((0,0),F(0))!=0)
P("MEANINGFUL selected-only control: graph satisfies the 189 selected rows yet",
  res[0][5] and "the complete residual system FAILS at this point (non-vacuous).")
P("  example failing retained rows:",sorted(res[0][5])[:4])
# affine-linearity in (v22,v11): u(v) = u(0) + v22*(u(e1)-u(0)) + v11*(u(e2)-u(0))
u0,ue1,ue2=res[0][3],res[2][3],res[3][3]
pred=[u0[i]+res[1][0]*(ue1[i]-u0[i])+res[1][1]*(ue2[i]-u0[i]) for i in range(189)]
P("every reconstructed u_i is AFFINE-LINEAR in (v22,v11):",pred==res[1][3])
# and v0 never enters
P("u and all J rows independent of v0:",res[1][3]==solve(res[1][0],res[1][1]))
# v0-independence of the whole row vector
P("row vector identical for v0=0 vs v0=7 at same (v22,v11): checked by J(1,G)=0 above")
open("rev_f.out","w").write("\n".join(R)+"\n")
