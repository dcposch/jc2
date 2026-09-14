#!/usr/bin/env python3
"""Desk-sized literal source and exact negative controls; no CAS dependency."""
import ast
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
source_path=ROOT/"box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json"
raw=source_path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea"
data=json.loads(raw)
expected={
 "h3":[[11,0,"Hc_11_0"]],
 "C2":[[22,0,"C2c_22_0"]],
 "C3":[[32,0,"1"],[33,0,"C3c_33_0"]],
 "B2":[[64,0,"B2c_64_0"],[65,0,"B2c_65_0"]],
 "A3":[[97,0,"A3c_97_0"],[98,0,"A3c_98_0"]]}
line={key:[row for row in data["maps"][key] if int(row[1])==0] for key in expected}
assert line==expected and data["residual_rows"]==[]
assert max(int(z) for r,z,e in data["maps"]["A3"])==32
assert max(98-int(r) for r,z,e in data["maps"]["A3"])==35
C33=[row for row in data["maps"]["A3"] if int(row[0])==65]
assert [int(row[1]) for row in C33]==list(range(24,33))
old=json.loads((ROOT/"box/factored-jacobian-pilot-20260906/complete_export.json").read_text())
aux=[n for n in old["coordinate_order"] if n.startswith("Hfact_")]
assert len(aux)==160
assert [n for n in aux if int(n.split("_")[2])==0]==["Hfact_0_0"]
assert max(sum(map(int,n.split("_")[1:])) for n in aux)==31

def add(a,b):
    out=dict(a)
    for p,v in b.items():out[p]=out.get(p,Q(0))+v
    return {p:v for p,v in out.items() if v}
def mul(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            p=i+k,j+l;out[p]=out.get(p,Q(0))+v*w
    return {p:v for p,v in out.items() if v}
def diff(a,k):
    out={}
    for p,v in a.items():
        if p[k]:
            q=list(p);q[k]-=1;out[tuple(q)]=v*p[k]
    return out
def jac(a,b):
    m=mul(diff(a,1),diff(b,0))
    return add(mul(diff(a,0),diff(b,1)),{p:-v for p,v in m.items()})
H={(3-i,8+i):Q(comb(3,i)) for i in range(4)}
H3={(9-i,24+i):Q(comb(9,i)) for i in range(10)}
H6={(18-i,48+i):Q(comb(18,i)) for i in range(19)}
# H is in the ACTUAL source C space, not only in an enlarged support rectangle.
assignment={"A3c_87_8":Q(1),"A3c_87_9":Q(3),"A3c_87_10":Q(3),"A3c_87_11":Q(1)}
def ev(n):
    if isinstance(n,ast.Constant):return Q(n.value)
    if isinstance(n,ast.Name):return assignment.get(n.id,Q(0))
    if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -ev(n.operand)
    if isinstance(n,ast.BinOp):
        a,b=ev(n.left),ev(n.right)
        if isinstance(n.op,ast.Add):return a+b
        if isinstance(n.op,ast.Sub):return a-b
        if isinstance(n.op,ast.Mult):return a*b
        if isinstance(n.op,ast.Div):return a/b
        if isinstance(n.op,ast.Pow):return a**int(b)
    raise ValueError(ast.dump(n))
P={}
for r,z,e in data["maps"]["A3"]:
    c=ev(ast.parse(str(e).replace("^","**"),mode="eval").body)
    if c:P[98-int(r)-int(z),int(z)]=c
assert P==H and not jac(H,H6)
assert not any(j==0 for i,j in H6) # Dropped transverse-line condition.
R=add(H3,{(1,0):Q(1)});G=mul(R,R)
assert not jac(R,G)
assert {p:v for p,v in G.items() if p[1]==0}=={(2,0):Q(1)}
assert R.get((0,33))==1 # Dropped C-support condition.
X={(1,0):Q(1)};smallG={(2,0):Q(1),(0,1):Q(1)}
assert jac(X,smallG)=={(0,0):Q(1)} # Positive-only is not zero-J.
result={"status":"DESK_LITERAL_AND_NEGATIVE_CONTROLS_PASS","source_sha256":hashlib.sha256(raw).hexdigest(),
 "literal_W_zero_rows":line,"C_degree33_W_exponents":list(range(24,33)),
 "C_maximum_W_exponent":32,"C_maximum_total_degree":35,
 "h_lift_W_zero_auxiliary":["Hfact_0_0"],"h_lift_maximum_auxiliary_physical_degree":31,
 "drop_transverse_line":{"G":"H^6","P":"H","P_in_actual_C_source":True,"Jacobian":0,"G_on_W_zero":0},
 "drop_C_support":{"G":"(H^3+X)^2","P":"H^3+X","Jacobian":0,"G_on_W_zero":"X^2","P_W33_coefficient":1},
 "positive_only_not_zero_J":{"G":"X^2+W","P":"X","Jacobian":1},
 "no_performance_or_solver_claim":True}
print(json.dumps(result,sort_keys=True,indent=2))
