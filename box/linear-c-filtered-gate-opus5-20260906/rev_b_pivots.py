#!/usr/bin/env python3
"""Opus review Part B: independent rebuild of graded source, kernel lemma controls,
and full recomputation of the 189x192 universal matrix over Q[g_uv]. Own code."""
import ast,json,math
from fractions import Fraction as F
from collections import defaultdict
R=[]
def P(*a): R.append(" ".join(map(str,a))); print(*a)
d=json.load(open("/tmp/jc2-lane.1CmqE8/inputs/delta2_stage8.strongest.json"))
cert=json.load(open("/tmp/jc2-lane.1CmqE8/inputs/filtered_basis_certificate.json"))

def lin(e):
    n0=ast.parse(str(e).replace("^","**"),mode="eval").body
    def go(n):
        if isinstance(n,ast.Constant): return {"":F(n.value)}
        if isinstance(n,ast.Name): return {n.id:F(1)}
        if isinstance(n,ast.UnaryOp): return {k:(-v if isinstance(n.op,ast.USub) else v) for k,v in go(n.operand).items()}
        a,b=go(n.left),go(n.right)
        if isinstance(n.op,ast.Add): o=dict(a); [o.__setitem__(k,o.get(k,F(0))+v) for k,v in b.items()]; return {k:v for k,v in o.items() if v}
        if isinstance(n.op,ast.Sub): o=dict(a); [o.__setitem__(k,o.get(k,F(0))-v) for k,v in b.items()]; return {k:v for k,v in o.items() if v}
        if isinstance(n.op,ast.Mult):
            s=a[""] if set(a)<={""} else b[""]; t=b if set(a)<={""} else a
            return {k:v*s for k,v in t.items() if v*s}
        if isinstance(n.op,ast.Div): return {k:v/b[""] for k,v in a.items()}
        raise ValueError
    return go(n0)
SRC=defaultdict(dict)
for r,z,e in d["maps"]["A3"]:
    for n,c in lin(e).items(): SRC[n][(98-int(r)-int(z),int(z))]=c
names=sorted(SRC)

# ---- polynomial helpers (mine) ----
def padd(a,b,s=F(1)):
    o=dict(a)
    for p,v in b.items():
        o[p]=o.get(p,F(0))+s*v
        if not o[p]: del o[p]
    return o
def psc(a,c): return {p:v*c for p,v in a.items() if v*c}
def pmul(a,b):
    o={}
    for p,v in a.items():
        for q,w in b.items():
            k=(p[0]+q[0],p[1]+q[1]); o[k]=o.get(k,F(0))+v*w
    return {p:v for p,v in o.items() if v}
def J(a,b):   # dA/dX dB/dW - dA/dW dB/dX, monomialwise
    o={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            c=(i*l-j*k)*v*w
            if c: 
                key=(i+k-1,j+l-1); assert min(key)>=0
                o[key]=o.get(key,F(0))+c
    return {p:v for p,v in o.items() if v}
def deg(a): return max(map(sum,a),default=-1)
def top(a):
    D=deg(a); return {p:v for p,v in a.items() if sum(p)==D}
H={(3-j,8+j):F(math.comb(3,j)) for j in range(4)}
Gtop={(0,0):F(1)}
for _ in range(6): Gtop=pmul(Gtop,H)
P("H deg",deg(H),"Gtop deg",deg(Gtop),"Gtop terms",len(Gtop))

# ---- KERNEL LEMMA computational control: kernel of S_l -> J(S_l,Gtop), l=0..40 ----
def hom_nullity(l):
    piv={}
    for j in range(l+1):
        v=J({(l-j,j):F(1)},Gtop)
        while v:
            q=min(v,key=lambda p:(-sum(p),p))
            if q not in piv: piv[q]=psc(v,1/v[q]); break
            v=padd(v,piv[q],-v[q])
    return l+1-len(piv)
ker=[(l,hom_nullity(l)) for l in range(41)]
bad=[(l,k) for l,k in ker if k!=(1 if l%11==0 else 0)]
P("homogeneous nullity l=0..40 matches (1 iff 11|l):",not bad,"| exceptions",bad)
Hp={(0,0):F(1)}
for k in range(4):
    P(f"  J(H^{k},Gtop)==0:",not J(Hp,Gtop),"deg",deg(Hp)); Hp=pmul(Hp,H)
P("  negative control J(X^11,Gtop)!=0:",bool(J({(11,0):F(1)},Gtop)))

# ---- rebuild filtration-adapted basis, my own echelonization ----
ech={}
for n in names:
    poly=dict(SRC[n]); comb={n:F(1)}
    while poly:
        p=min(poly,key=lambda q:(-sum(q),q))
        if p not in ech:
            c=poly[p]; ech[p]=(psc(poly,1/c),psc(comb,1/c)); break
        o,oc=ech[p]; c=poly[p]; poly=padd(poly,o,-c); comb=padd(comb,oc,-c)
    else: raise SystemExit("source columns dependent")
adapted=[ech[p] for p in sorted(ech,key=lambda p:(-sum(p),p))]
P("adapted source basis size",len(adapted))
groups=defaultdict(list)
for poly,comb in adapted: groups[deg(poly)].append((poly,comb))
myprofile=[];active=[];free=[]
for D in sorted(groups,reverse=True):
    ip={}
    for p0,c0 in groups[D]:
        poly,comb=dict(p0),dict(c0); img=J(top(poly),Gtop)
        while img:
            pos=min(img,key=lambda q:(-sum(q),q))
            if pos not in ip:
                c=img[pos]; poly,comb,img=psc(poly,1/c),psc(comb,1/c),psc(img,1/c)
                it={"degree":D,"poly":poly,"comb":comb,"pivot":pos,"ti":img}; ip[pos]=it; active.append(it); break
            o=ip[pos]; c=img[pos]
            poly=padd(poly,o["poly"],-c); comb=padd(comb,o["comb"],-c); img=padd(img,o["ti"],-c)
        else:
            assert deg(poly)==D and not J(top(poly),Gtop)
            free.append({"degree":D,"poly":poly,"comb":comb})
    myprofile.append({"degree":D,"dimension":len(groups[D]),"rank":len(ip),"kernel_slots":len(groups[D])-len(ip)})
P("MY active pivots =",len(active),"| free =",len(free),"| free degrees",[x["degree"] for x in free])
P("profile identical to certificate:",myprofile==cert["profile"])
P("kernel-deficient degrees:",[p["degree"] for p in myprofile if p["kernel_slots"]],
  "| degree33 (dim,rank)=",[(p["dimension"],p["rank"]) for p in myprofile if p["degree"]==33])
basis=active+free
# certificate agreement on basis polynomials & combinations
def dec(a): return {(i,j):F(c) for i,j,c in a}
okp=okc=0
for i,b in enumerate(cert["basis"]):
    if dec(b["polynomial"])==basis[i]["poly"]: okp+=1
    if {n:F(c) for n,c in b["source_combination"].items()}==basis[i]["comb"]: okc+=1
P("certificate basis polynomials reproduced:",okp,"/192 ; source combinations reproduced:",okc,"/192")
# every basis vector equals its declared source combination applied to the RAW source
bad=0
for b in basis:
    rec={}
    for n,c in b["comb"].items(): rec=padd(rec,SRC[n],c)
    if rec!=b["poly"]: bad+=1
P("basis = exact raw-source combination for all 192:",bad==0)
# invertibility of the 192x192 source transform: exact determinant by fraction-free-ish elimination
idx={n:i for i,n in enumerate(names)}
M=[[F(0)]*192 for _ in range(192)]
for j,b in enumerate(basis):
    for n,c in b["comb"].items(): M[idx[n]][j]=c
det=F(1); A=[row[:] for row in M]
for col in range(192):
    piv=None
    for r0 in range(col,192):
        if A[r0][col]: piv=r0;break
    if piv is None: det=F(0);break
    if piv!=col: A[col],A[piv]=A[piv],A[col]; det=-det
    det*=A[col][col]; inv=1/A[col][col]
    A[col]=[x*inv for x in A[col]]
    for r0 in range(col+1,192):
        if A[r0][col]:
            f=A[r0][col]; A[r0]=[x-f*y for x,y in zip(A[r0],A[col])]
P("source transform determinant =",det,"| invertible:",det!=0)
import json as _j
_j.dump({"det":str(det)},open("/home/ubuntu/jc2/box/linear-c-filtered-gate-opus5-20260906/det.json","w"))

# ---- FULL universal matrix over Q[g_uv]: my own coefficient derivation ----
# J(C,G) coeff at (p,q) = sum_{(a,b) in C} c_ab * [ (a)*(q-b+1)... ] done from scratch:
# J = C_X G_W - C_W G_X ; C_X: a*X^{a-1}W^b ; G_W: v*X^u W^{v-1}
def entry(poly,pos):
    p,q=pos; res={}
    for (a,b),c in poly.items():
        # term1: a * c * X^{a-1}W^b * v g_uv X^u W^{v-1} -> (a-1+u, b+v-1)=(p,q)
        if a:
            u,v=p-a+1,q-b+1
            if u>=0 and v>=0 and u+v<=66 and v:
                cc=F(a)*c*v; key=(-1,-1) if u+v==66 else (u,v)
                if u+v==66: cc*=Gtop.get((u,v),F(0))
                if cc: res[key]=res.get(key,F(0))+cc
        # term2: -b * c * X^a W^{b-1} * u g_uv X^{u-1} W^v -> (a+u-1, b-1+v)=(p,q)
        if b:
            u,v=p-a+1,q-b+1
            if u>=0 and v>=0 and u+v<=66 and u:
                cc=-F(b)*c*u; key=(-1,-1) if u+v==66 else (u,v)
                if u+v==66: cc*=Gtop.get((u,v),F(0))
                if cc: res[key]=res.get(key,F(0))+cc
    return {k:v for k,v in res.items() if v}
declared={(e["row"],e["column"]):{(u,v):F(c) for u,v,c in e["terms"]} for e in cert["selected_matrix_entries"]}
mine={};nnz=terms=0;upfail=diagfail=0
for i,left in enumerate(active):
    pos=left["pivot"]
    for j,b in enumerate(basis):
        val=entry(b["poly"],pos)
        if j<len(active):
            if j>i and val: upfail+=1
            if j==i and val!={(-1,-1):F(1)}: diagfail+=1
        if val: mine[(i,j)]=val; nnz+=1; terms+=len(val)
P("MY selected matrix: nonzero entries",nnz,"literal g-linear terms",terms)
P("universal upper-triangle violations:",upfail,"| diagonal!=1 violations:",diagfail)
P("entry-by-entry identical to certificate:",mine==declared)
P("distinct selected rows:",len({x['pivot'] for x in active})==len(active))
P("selected row degrees:",sorted({sum(x['pivot']) for x in active})[:3],"...",sorted({sum(x['pivot']) for x in active})[-3:])
gc={k for v in mine.values() for k in v if k!=(-1,-1)}
P("distinct lower-G coordinates used:",len(gc),"physical degree range",min(map(sum,gc)),"..",max(map(sum,gc)))
P("column 191 (constant) appears in any selected row:",any(j==191 for (i,j) in mine))
P("off-diagonal columns outside {<i,189,190}:",sorted({j for (i,j) in mine if j!=i and not(j<i or j in(189,190))}))
open("/home/ubuntu/jc2/box/linear-c-filtered-gate-opus5-20260906/rev_b.out","w").write("\n".join(R)+"\n")
