#!/usr/bin/env python3
"""Opus independent review, Part A: actual C source map facts. No producer code reused."""
import ast, json, math
from fractions import Fraction as F
from collections import defaultdict
SRC="/tmp/jc2-lane.1CmqE8/inputs/delta2_stage8.strongest.json"
d=json.load(open(SRC))
R=[]
def P(*a): R.append(" ".join(map(str,a))); print(*a)

# --- independent linear parser (sympy-free, my own): returns dict name->Fraction plus 'const'
def lin(e):
    node=ast.parse(str(e).replace("^","**"),mode="eval").body
    def go(n):
        if isinstance(n,ast.Constant): return {"":F(n.value)}
        if isinstance(n,ast.Name): return {n.id:F(1)}
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub): return {k:-v for k,v in go(n.operand).items()}
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.UAdd): return go(n.operand)
        if isinstance(n,ast.BinOp):
            a,b=go(n.left),go(n.right)
            if isinstance(n.op,ast.Add):
                o=dict(a)
                for k,v in b.items(): o[k]=o.get(k,F(0))+v
                return {k:v for k,v in o.items() if v}
            if isinstance(n.op,ast.Sub):
                o=dict(a)
                for k,v in b.items(): o[k]=o.get(k,F(0))-v
                return {k:v for k,v in o.items() if v}
            if isinstance(n.op,ast.Mult):
                if set(a)<={""}: return {k:v*a.get("",F(0)) for k,v in b.items() if v*a.get("",F(0))}
                if set(b)<={""}: return {k:v*b.get("",F(0)) for k,v in a.items() if v*b.get("",F(0))}
                raise ValueError("NONLINEAR")
            if isinstance(n.op,ast.Div):
                if set(b)!={""}: raise ValueError("NONCONST DENOM")
                return {k:v/b[""] for k,v in a.items()}
            if isinstance(n.op,ast.Pow): raise ValueError("POWER")
        raise ValueError(ast.dump(n))
    return go(node)

# --- A3 -> C map
C=defaultdict(dict); support=set(); nonlin=0; affine=0
for r,z,e in d["maps"]["A3"]:
    r,z=int(r),int(z); p=(98-r-z,z)
    assert min(p)>=0 and p not in support, ("bad pos",p)
    support.add(p)
    row=lin(e)
    if "" in row and row[""]!=0: affine+=1
    for n,c in row.items():
        if n=="": continue
        C[n][p]=c
names=sorted(C)
P("A3 rows",len(d["maps"]["A3"]),"| physical support positions",len(support),"| C params",len(names),"| affine offsets",affine)
degs={sum(p) for p in support}
P("physical C degrees present: min",min(degs),"max",max(degs),"| all deg<=35:",max(degs)<=35)
P("W^33 slot (0,33) in support:", (0,33) in support, "| deg-33 slots:", sorted(p for p in support if sum(p)==33))

# --- identity slots / injectivity, computed independently by rank
occ=defaultdict(list)
for n in names:
    for p in C[n]: occ[p].append(n)
solo={p:v[0] for p,v in occ.items() if len(v)==1}
idslots={}
for n in names:
    s=[p for p,m in solo.items() if m==n and C[n][p]==1]
    if s: idslots[n]=sorted(s)[0]
P("params with a coefficient-1 exclusive identity slot:",len(idslots),"of",len(names))
# independent exact rank of the 201 x 192 matrix
pos=sorted(support); pidx={p:i for i,p in enumerate(pos)}
cols=[[C[n].get(p,F(0)) for p in pos] for n in names]
piv={}; rank=0
for col in cols:
    v=list(col)
    for r0,pv in piv.items():
        if v[r0]:
            c=v[r0]
            v=[a-c*b for a,b in zip(v,pv)]
    nz=[i for i,a in enumerate(v) if a]
    if nz:
        r0=nz[0]; c=v[r0]; piv[r0]=[a/c for a in v]; rank+=1
P("exact Q rank of source C matrix =",rank,"| injective:",rank==len(names))

# --- disjointness / count of other physical coordinates
others=set()
for key in ("h3","C2","C3","B2"):
    for r,z,e in d["maps"][key]:
        for n in ast.walk(ast.parse(str(e).replace("^","**"),mode="eval")):
            if isinstance(n,ast.Name): others.add(n.id)
P("other syntactically occurring names in h3,C2,C3,B2 =",len(others))
P("intersection with C params =",sorted(set(names)&others))
P("sample others:",sorted(others)[:6],"...",sorted(others)[-4:])

# --- normalizer / degree bounds for h,D,C
for key,N,lab in (("h3",11,"h3"),("C2",22,"C2"),("C3",33,"C3"),("B2",65,"D"),("A3",98,"C")):
    ds={N-int(r) for r,z,e in d["maps"][key]}
    bad=[(r,z) for r,z,e in d["maps"][key] if N-int(r)-int(z)<0]
    P(f"  {lab}: normalizer {N}, total degrees {min(ds)}..{max(ds)}, negative-X rows {len(bad)}")
open("/home/ubuntu/jc2/box/linear-c-filtered-gate-opus5-20260906/rev_a.out","w").write("\n".join(R)+"\n")
