#!/usr/bin/env python3
"""Exact filtered C-space basis and universal constant-pivot witness; no solve."""
import ast
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import socket
import time

def require(ok, why):
    if not ok: raise ValueError(why)
require(socket.gethostname() == "ip-172-30-0-56", "Allocated worker only")
require(Path("/sys/class/dmi/id/sys_vendor").read_text().strip()=="Amazon EC2","EC2 only")
require(os.environ.get("JC2_REGISTERED_JOB")=="linear-c-filtered-pilot-astra-20260906","Registered tag")
started=time.monotonic()
root=Path.cwd()
require(root==Path("/home/ubuntu/linear-c-root-replay-20260906"),"Fresh owned root replay scratch required")
raw=Path("delta2_stage8.strongest.json").read_bytes()
SOURCE_SHA="778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea"
require(hashlib.sha256(raw).hexdigest()==SOURCE_SHA,"Source drift")
data=json.loads(raw)
require(data["residual_rows"]==[],"Source residual rows")

def add(a,b,scale=Q(1)):
    out=dict(a)
    for p,v in b.items():
        out[p]=out.get(p,Q(0))+scale*v
        if not out[p]:del out[p]
    return out
def scal(a,c):return {p:v*c for p,v in a.items() if v*c}
def mul(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            p=i+k,j+l;out[p]=out.get(p,Q(0))+v*w
    return {p:v for p,v in out.items() if v}
def power(a,n):
    out={(0,0):Q(1)}
    for _ in range(n):out=mul(out,a)
    return out
def jac(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            c=i*l-j*k
            if c:
                p=i+k-1,j+l-1
                require(min(p)>=0,"Jacobian negative degree")
                out[p]=out.get(p,Q(0))+v*w*c
    return {p:v for p,v in out.items() if v}
def degree(a):return max(map(sum,a),default=-1)
def lead(a):return min(a,key=lambda p:(-sum(p),p))
def top(a):
    d=degree(a);return {p:v for p,v in a.items() if sum(p)==d}

# Linear-expression parser, rejecting affine constants and nonlinear products.
def ev(n):
    if isinstance(n,ast.Constant) and type(n.value)is int:return {None:Q(n.value)} if n.value else {}
    if isinstance(n,ast.Name):return {n.id:Q(1)}
    if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return scal(ev(n.operand),-1)
    if isinstance(n,ast.BinOp):
        a,b=ev(n.left),ev(n.right)
        if isinstance(n.op,ast.Add):return add(a,b)
        if isinstance(n.op,ast.Sub):return add(a,b,-1)
        if isinstance(n.op,ast.Mult):
            require(set(a)<={None} or set(b)<={None},"Nonlinear source C")
            return scal(b,a.get(None,0)) if set(a)<={None} else scal(a,b.get(None,0))
        if isinstance(n.op,ast.Div):
            require(set(b)=={None},"Nonconstant denominator")
            return scal(a,1/b[None])
    raise ValueError(ast.dump(n))
source={}
C_support=set()
for r,z,e in data["maps"]["A3"]:
    p=(98-int(r)-int(z),int(z))
    require(min(p)>=0 and p not in C_support,"Physical C support")
    C_support.add(p)
    row=ev(ast.parse(str(e).replace("^","**"),mode="eval").body)
    require(None not in row,"C affine offset")
    for n,c in row.items():
        source.setdefault(n,{})[p]=c
names=sorted(source)
require(len(names)==192,"192 C parameters")
others=set()
for key in ("h3","C2","C3","B2"):
    for r,z,e in data["maps"][key]:
        others.update(n.id for n in ast.walk(ast.parse(str(e).replace("^","**"),mode="eval")) if isinstance(n,ast.Name))
require(not set(names)&others,"C/base independence")
identity={}
for n,p in source.items():
    slots=[q for q,c in p.items() if c==1 and all(q not in source[m] for m in names if m!=n)]
    require(bool(slots),"Missing identity slot")
    identity[n]=sorted(slots)[0]

# Sparse column echelonization in descending physical degree: filtration-adapted.
echelon={}
for n in names:
    poly=dict(source[n]);comb={n:Q(1)}
    while poly:
        p=lead(poly)
        if p not in echelon:
            c=poly[p]
            echelon[p]=(scal(poly,1/c),scal(comb,1/c))
            break
        old,oldcomb=echelon[p]
        c=poly[p];poly=add(poly,old,-c);comb=add(comb,oldcomb,-c)
    else:raise ValueError("Source columns not injective")
adapted=[echelon[p] for p in sorted(echelon,key=lambda p:(-sum(p),p))]
require(len(adapted)==192,"Adapted census")
H={(3-j,8+j):Q(math.comb(3,j)) for j in range(4)}
Gtop=power(H,6)
require(degree(H)==11 and degree(Gtop)==66,"Leading degrees")
groups=defaultdict(list)
for poly,comb in adapted:groups[degree(poly)].append((poly,comb))

# Column operations confined to one homogeneous filtration quotient.
active=[];free=[];profile=[]
for d in sorted(groups,reverse=True):
    image_pivots={}
    for poly0,comb0 in groups[d]:
        poly,comb=dict(poly0),dict(comb0)
        image=jac(top(poly),Gtop)
        while image:
            pos=lead(image)
            if pos not in image_pivots:
                c=image[pos]
                poly,comb,image=scal(poly,1/c),scal(comb,1/c),scal(image,1/c)
                item={"degree":d,"poly":poly,"comb":comb,"pivot":pos,"top_image":image}
                image_pivots[pos]=item;active.append(item)
                break
            old=image_pivots[pos];c=image[pos]
            poly=add(poly,old["poly"],-c);comb=add(comb,old["comb"],-c)
            image=add(image,old["top_image"],-c)
        else:
            require(degree(poly)==d,"Filtration lost under within-degree operations")
            require(not jac(top(poly),Gtop),"Leading kernel not zero")
            free.append({"degree":d,"poly":poly,"comb":comb})
    rank=len(image_pivots);dim=len(groups[d])
    require(dim-rank <= (1 if d%11==0 else 0),"Homogeneous kernel bound")
    profile.append({"degree":d,"dimension":dim,"rank":rank,"kernel_slots":dim-rank})
require(len(active)>=188 and len(active)+len(free)==192,"Filtered rank bound")
basis=active+free

# Every basis vector is exactly its displayed rational source combination.
for item in basis:
    recovered={}
    for n,c in item["comb"].items():recovered=add(recovered,source[n],c)
    require(recovered==item["poly"],"Source change-of-basis equality")
check_echelon={}
for item in basis:
    p=dict(item["comb"])
    while p:
        n=min(p)
        if n not in check_echelon:
            check_echelon[n]=scal(p,1/p[n]);break
        p=add(p,check_echelon[n],-p[n])
    else:raise ValueError("Final source transform singular")
require(len(check_echelon)==192,"Invertible source transform")

# A selected matrix entry is a Q-linear polynomial in arbitrary lower G_uv.
# key=(-1,-1) means constant, already evaluated against fixed Gtop.
def entry(poly,row):
    result={}
    for (i,j),c in poly.items():
        u,v=row[0]+1-i,row[1]+1-j
        if min(u,v)<0 or u+v>66:continue
        c*=i*v-j*u
        if not c:continue
        if u+v==66:
            c*=Gtop.get((u,v),0);key=(-1,-1)
        else:key=(u,v)
        if c:
            result[key]=result.get(key,Q(0))+c
            if not result[key]:del result[key]
    return result

entries=[]
nnz=terms=0
for i,left in enumerate(active):
    row=left["pivot"]
    for j,right in enumerate(basis):
        value=entry(right["poly"],row)
        if j<len(active):
            if j>i:require(not value,"Universal upper-triangular entry not zero")
            if j==i:require(value=={(-1,-1):Q(1)},"Universal diagonal not exactly one")
        if value:
            entries.append({"row":i,"column":j,"terms":[[u,v,str(c)] for (u,v),c in sorted(value.items())]})
            nnz+=1;terms+=len(value)
# This checks ALL arbitrary lower-G coefficients, not a numerical specialization.
require(len({x["pivot"] for x in active})==len(active),"Distinct row minor")

# Positive and negative exact controls of the leading kernel.
full_rank=[]
for d in range(36):
    piv={}
    for j in range(d+1):
        p=jac({(d-j,j):Q(1)},Gtop)
        while p:
            q=lead(p)
            if q not in piv:piv[q]=scal(p,1/p[q]);break
            p=add(p,piv[q],-p[q])
    nullity=d+1-len(piv)
    require(nullity==(1 if d%11==0 else 0),"Full homogeneous kernel dimension")
    if d%11==0:require(not jac(power(H,d//11),Gtop),"H-power kernel")
    full_rank.append([d,len(piv),nullity])
require(jac({(11,0):Q(1)},Gtop),"Nonkernel negative control")
Gsample=add(Gtop,{(65,0):Q(2),(1,0):Q(1),(0,2):Q(3)})
for j,right in enumerate(active):
    image=jac(right["poly"],Gsample)
    for i,left in enumerate(active):
        value=image.get(left["pivot"],Q(0))
        if j>i:require(value==0,"Sample upper triangle")
        if j==i:require(value==1,"Sample diagonal")

def encode_poly(poly):return [[i,j,str(c)] for (i,j),c in sorted(poly.items())]
packet={"schema":"JC2_C_FILTERED_PIVOT/v1","field":"Q","source_sha256":SOURCE_SHA,
        "source_variables":names,"source_columns":[encode_poly(source[n]) for n in names],
        "source_identity_slots":identity,"G_top":encode_poly(Gtop),
        "G_lower":"arbitrary coefficients g_u_v with u+v<66; no parameter localization",
        "source_basis_transform_orientation":"C=sum(new_coordinate_j * basis_polynomial_j); old_c_n=sum_j comb_j[n]*new_coordinate_j",
        "basis":[{"index":i,"kind":"active" if i<len(active) else "free","degree":x["degree"],
                  "polynomial":encode_poly(x["poly"]),"source_combination":{n:str(c) for n,c in sorted(x["comb"].items())},
                  "selected_J_row":list(x["pivot"]) if i<len(active) else None} for i,x in enumerate(basis)],
        "profile":profile,"selected_matrix_entries":entries,
        "entry_encoding":"[u,v,coefficient] multiplies g_u_v; [-1,-1,coefficient] is constant",
        "minor":{"size":len(active),"determinant":"1","proof":"All entries above diagonal are identically zero in arbitrary lower G coordinates; all diagonal entries exactly 1."},
        "full_homogeneous_kernel_controls":full_rank}
target=Path("filtered_basis_certificate.json")
require(not target.exists(),"No overwrite")
target.write_text(json.dumps(packet,sort_keys=True,separators=(",",":"))+"\n")
summary={"status":"EXACT_UNIVERSAL_CONSTANT_PIVOTS_PASS","source_dimension":192,
         "active_constant_pivots":len(active),"remaining_C_coordinates":len(free),
         "free_degrees":[x["degree"] for x in free],"minor_determinant":"1",
         "universality":"every G with fixed G_top=H^6 and degree(G-G_top)<66",
         "source_C_support":len(C_support),"profile":profile,
         "basis_physical_terms":sum(len(x["poly"]) for x in basis),
         "source_change_of_basis_terms":sum(len(x["comb"]) for x in basis),
         "selected_matrix_nonzero_entries":nnz,"selected_matrix_literal_G_linear_terms":terms,
         "certificate_bytes":target.stat().st_size,"certificate_sha256":hashlib.sha256(target.read_bytes()).hexdigest(),
         "dense_reconstruction_expanded":False,"semantic_source_substitution_expanded":False,
         "all_remaining_J_rows_dropped":False,"solver_launched":False,
         "negative_nonkernel_control":True,"universal_symbolic_triangle_check":True,
         "arbitrary_lower_G_exact_sample_check":True,"full_homogeneous_kernel_controls":True,
         "wall_seconds":time.monotonic()-started,"peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path("filtered_basis_summary.json").write_text(json.dumps(summary,sort_keys=True,indent=2)+"\n")
print(json.dumps(summary,sort_keys=True),flush=True)
