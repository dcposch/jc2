#!/usr/bin/env python3
"""Opus review Part C: F/G/K identity, h_top=H^3, denominators & base specialization."""
import ast,json,math
from fractions import Fraction as F
from collections import defaultdict
import sympy as S
R=[];P=lambda *a:(R.append(" ".join(map(str,a))),print(*a))
d=json.load(open("/tmp/jc2-lane.1CmqE8/inputs/delta2_stage8.strongest.json"))
cert=json.load(open("/tmp/jc2-lane.1CmqE8/inputs/filtered_basis_certificate.json"))

# --- 1. J(F,G) = K + J(C,G) as a formal identity ---
x,w=S.symbols("x w"); h,D,Cc,a,b=S.symbols("h D C a b")
hf,Df,Cf=S.Function("h")(x,w),S.Function("D")(x,w),S.Function("C")(x,w)
Ff=hf**3+(3*Df+a)*hf/2+Cf; Gf=hf**2-b*hf/3+Df
jac=lambda f,g:S.diff(f,x)*S.diff(g,w)-S.diff(f,w)*S.diff(g,x)
K=((3*Df+a+b*hf)/2)*jac(hf,Df)
P("J(F,G) - K - J(C,G) == 0 :",S.simplify(S.expand(jac(Ff,Gf)-K-jac(Cf,Gf)))==0)

# --- 2. h_top = H^3 from the frozen h3 map (degree-11 part must be literally H) ---
def lin(e):
    n0=ast.parse(str(e).replace("^","**"),mode="eval").body
    def go(n):
        if isinstance(n,ast.Constant): return {"":F(n.value)}
        if isinstance(n,ast.Name): return {n.id:F(1)}
        if isinstance(n,ast.UnaryOp): return {k:(-v if isinstance(n.op,ast.USub) else v) for k,v in go(n.operand).items()}
        if isinstance(n,ast.BinOp):
            A,B=go(n.left),go(n.right)
            if isinstance(n.op,ast.Add): o=dict(A); [o.__setitem__(k,o.get(k,F(0))+v) for k,v in B.items()]; return o
            if isinstance(n.op,ast.Sub): o=dict(A); [o.__setitem__(k,o.get(k,F(0))-v) for k,v in B.items()]; return o
            if isinstance(n.op,ast.Mult):
                s=A[""] if set(A)<={""} else B[""]; t=B if set(A)<={""} else A; return {k:v*s for k,v in t.items()}
            if isinstance(n.op,ast.Div): return {k:v/B[""] for k,v in A.items()}
        raise ValueError("nonlinear h3 row")
    return go(n0)
h3top={}
mixed=[]
for r,z,e in d["maps"]["h3"]:
    p=(11-int(r)-int(z),int(z))
    if sum(p)==11:
        try: row=lin(e)
        except Exception as ex: mixed.append((p,str(e)[:60],str(ex))); continue
        h3top[p]=row
P("h3 degree-11 rows:",len(h3top),"| nonlinear rows:",len(mixed))
Hcoef={(3-j,8+j):F(math.comb(3,j)) for j in range(4)}
ok=all(set(v)=={""} and v[""]==Hcoef.get(p) for p,v in h3top.items()) and set(h3top)==set(Hcoef)
P("h3 top part is EXACTLY H=(X+W)^3W^8 with constant coefficients:",ok,"| values",{p:str(v) for p,v in h3top.items()})
P("=> h_top = h3_top^3 = H^3, G_top = h_top^2 = H^6")
degs={k:(max(int(d['normalization'][k])-int(r) for r,z,e in d['maps'][k])) for k in ('h3','C2','C3','B2','A3')}
P("exact top degrees:",degs,"| deg h = max(33,11+14,14) = 33 ; deg G = 66 ; deg(G-Gtop) <=",max(33,degs['B2']))

# --- 3. denominators: over which base rings does the reduction survive? ---
den=set()
for bs in cert["basis"]:
    for n,c in bs["source_combination"].items(): den.add(F(c).denominator)
    for i,j,c in bs["polynomial"]: den.add(F(c).denominator)
pr=set()
for q in den:
    m=q
    for p in range(2,200):
        while m%p==0: pr.add(p); m//=p
    if m>1: pr.add(m)
P("distinct denominators in the change of basis:",sorted(den)[:12],"...","count",len(den))
P("primes inverted by the basis change:",sorted(pr))
ent=set()
for e in cert["selected_matrix_entries"]:
    for u,v,c in e["terms"]: ent.add(F(c).denominator)
P("denominators in the 42131 matrix entries:",sorted(ent)[:12],"count",len(ent))
open("rev_c.out","w").write("\n".join(R)+"\n")
