#!/usr/bin/env python3
"""One bounded prefix-block elimination experiment; exact Q, no solve."""
import ast
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import resource
import socket
import time

def require(ok,why):
    if not ok:raise ValueError(why)
require(platform.system()=="Linux" and socket.gethostname()=="ip-172-30-0-56","Allocated Linux worker")
require(Path("/sys/class/dmi/id/sys_vendor").read_text().strip()=="Amazon EC2","EC2")
require(os.environ.get("JC2_REGISTERED_JOB")=="linear-c-structured-pilot-astra-20260906","Registration")
require(Path.cwd()==Path("/home/ubuntu/linear-c-structured-pilot-20260906"),"New scratch only")
from flint import fmpq_mpoly_ctx, fmpq_mpoly
started=time.monotonic()
SOURCE_SHA="778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea"
CERT_SHA="c2b5965278e0fa30f0490b7f5a019434abe5291e50b748d3a3c0795c8175f906"
raw=Path("delta2_stage8.strongest.json").read_bytes();require(hashlib.sha256(raw).hexdigest()==SOURCE_SHA,"Source pin")
source=json.loads(raw);require(source["residual_rows"]==[],"Residual rows")
rawc=Path("filtered_basis_certificate.json").read_bytes();require(hashlib.sha256(rawc).hexdigest()==CERT_SHA,"Pivot pin")
cert=json.loads(rawc)
cvars=set(cert["source_variables"])
exprs=[str(e) for key in ("h3","C2","C3","B2") for r,z,e in source["maps"][key]]
base=sorted(set(re.findall(r"\b[A-Za-z_][A-Za-z_0-9]*\b"," ".join(exprs)))|{"target_a","target_b"})
require(len(base)==247 and not set(base)&cvars,"Base source ring")
ctx=fmpq_mpoly_ctx.get(tuple(base),ordering="degrevlex")
vals=dict(zip(base,ctx.gens()));cache={}
def parse(text):
    s=str(text)
    if s not in cache:cache[s]=fmpq_mpoly(s,ctx=ctx)
    return cache[s]
def add(a,b,c=1):
    out=dict(a)
    for p,v in b.items():
        out[p]=out.get(p,ctx.constant(0))+c*v
        if not out[p]:del out[p]
    return out
def mul(a,b):
    out={}
    for p,v in a.items():
        for q,w in b.items():
            t=p[0]+q[0],p[1]+q[1]
            out[t]=out.get(t,ctx.constant(0))+v*w
    return {p:v for p,v in out.items() if v}
def diff(a,k):
    out={}
    for p,v in a.items():
        if p[k]:
            q=list(p);q[k]-=1;out[tuple(q)]=v*p[k]
    return out
def jac(a,b):return add(mul(diff(a,0),diff(b,1)),mul(diff(a,1),diff(b,0)),-1)
def load(key,N):
    out={}
    for r,z,e in source["maps"][key]:
        p=N-int(r)-int(z),int(z);require(min(p)>=0,"Physical exponents")
        v=parse(e)
        if v:out[p]=v
    return out
def stats(a):
    return {"rows":len(a),"terms":sum(len(v) for v in a.values()),"degree":max((int(v.total_degree()) for v in a.values()),default=-1)}
def event(phase,**kwargs):
    print(json.dumps({"phase":phase,"wall":time.monotonic()-started,"rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kwargs},sort_keys=True),flush=True)
h3,c2,c3=load("h3",11),load("C2",22),load("C3",33)
oldh=add(add(mul(mul(h3,h3),h3),mul(c2,h3)),c3)
sites=sorted(p for p,v in oldh.items() if v.total_degree()>0)
require(len(sites)==160,"h graph")
PREFIX=24
require([cert["basis"][i]["degree"] for i in (0,6,7,14,15,23)]==[35,35,34,34,33,33],"Frozen three-block prefix")
names=base+[f"Hfact_{i}_{j}" for i,j in sites]+[f"q{i}" for i in range(PREFIX,189)]+["v22","v11","Zj"]
require(len(names)==575,"Reduced prefix coordinate count")
ctx=fmpq_mpoly_ctx.get(tuple(names),ordering="degrevlex");vals=dict(zip(names,ctx.gens()));cache={}
zero,one=ctx.constant(0),ctx.constant(1)
h={p:vals[f"Hfact_{p[0]}_{p[1]}"] if p in sites else parse(str(v)) for p,v in oldh.items()}
D=load("B2",65);a,b=vals["target_a"],vals["target_b"]
graphdefs={p:vals[f"Hfact_{p[0]}_{p[1]}"]-parse(str(oldh[p])) for p in sites}
G=add(add(mul(h,h),h,-b/3),D)
A=add(add({p:3*v/2 for p,v in D.items()},h,b/2),{(0,0):a/2})
hd=jac(h,D)
event("lifted_base",variables=len(names),h=stats(h),G=stats(G),hd=stats(hd))
def Kcoef(pos):
    out=zero
    for (i,j),v in A.items():
        w=hd.get((pos[0]-i,pos[1]-j))
        if w is not None:out+=v*w
    return out
matrix=[[] for _ in range(189)]
for entry in cert["selected_matrix_entries"]:matrix[entry["row"]].append(entry)
def matrix_value(terms):
    p=zero
    for u,v,c in terms:
        coeff=parse(c)
        p+=coeff if u<0 else coeff*G.get((u,v),zero)
    return p
R={}
prefix_data=[]
prefix_start=time.monotonic()
with Path("prefix_reconstruction.jsonl").open("w") as out:
    out.write(json.dumps({"type":"header","source_sha256":SOURCE_SHA,"pivot_sha256":CERT_SHA,"variables":names,"prefix":PREFIX,"scope":"Only C degrees35,34,33 reconstructed; lower blocks remain q nodes."})+"\n")
    for i in range(PREFIX):
        pos=tuple(cert["basis"][i]["selected_J_row"])
        value=-Kcoef(pos)
        for e in matrix[i]:
            j=e["column"]
            if j==i:continue
            require(j<i or j in (189,190),"Universal triangular contract")
            image=R[j] if j<i else vals["v22" if j==189 else "v11"]
            value-=matrix_value(e["terms"])*image
            require(len(value)<=100000,"PREFIX_ROW_TERM_CAP")
        require(len(value)<=100000 and sum(len(x) for x in R.values())+len(value)<=500000,"PREFIX_AGGREGATE_TERM_CAP")
        R[i]=value
        rec={"type":"reconstruction","index":i,"C_degree":cert["basis"][i]["degree"],"physical_row":pos,
             "degree":int(value.total_degree()),"terms":len(value),"polynomial":str(value)}
        out.write(json.dumps(rec,sort_keys=True)+"\n")
        prefix_data.append({k:v for k,v in rec.items() if k!="polynomial"})
    out.write(json.dumps({"type":"complete","reconstructed":len(R)})+"\n")
event("prefix",rows=len(R),terms=sum(len(x) for x in R.values()),degree=max(int(x.total_degree()) for x in R.values()),seconds=time.monotonic()-prefix_start)
C={}
for item in cert["basis"]:
    i=item["index"]
    if i==191:continue
    value=R[i] if i<PREFIX else (vals[f"q{i}"] if i<189 else vals["v22" if i==189 else "v11"])
    for x,w,c in item["polynomial"]:
        C[(x,w)]=C.get((x,w),zero)+parse(c)*value
C={p:v for p,v in C.items() if v}
event("reconstructed_C",stats=stats(C))
Cx,Cw,Gx,Gw=diff(C,0),diff(C,1),diff(G,0),diff(G,1)
support=set()
for left,right in [(A,hd),(Cx,Gw),(Cw,Gx)]:
    support.update((i+k,j+l) for i,j in left for k,l in right)
require(max(map(sum,support))<=99,"Physical J cap")
def Jcoef(pos):
    out=Kcoef(pos)
    for left,right,sign in [(Cx,Gw,1),(Cw,Gx,-1)]:
        for (i,j),v in left.items():
            w=right.get((pos[0]-i,pos[1]-j))
            if w is not None:out+=sign*v*w
    return out
for i in range(PREFIX):
    require(not Jcoef(tuple(cert["basis"][i]["selected_J_row"])),"Prefix exact selected-row substitution")
event("prefix_selected_rows_exact_zero")
# Separate exact J0 extraction from physical linear jets.
h0,hx,hw=[h.get(p,zero) for p in [(0,0),(1,0),(0,1)]]
d0,dx,dw=[D.get(p,zero) for p in [(0,0),(1,0),(0,1)]]
cx,cw=[C.get(p,zero) for p in [(1,0),(0,1)]]
fx=(3*h0*h0+(3*d0+a)/2)*hx+3*h0*dx/2+cx
fw=(3*h0*h0+(3*d0+a)/2)*hw+3*h0*dw/2+cw
gx=(2*h0-b/3)*hx+dx;gw=(2*h0-b/3)*hw+dw
J0=Jcoef((0,0));require(J0==fx*gw-fw*gx and bool(J0),"Independent J0 jets")
Path("J0.json").write_text(json.dumps({"variables":names,"J0":str(J0),"terms":len(J0),"degree":int(J0.total_degree()),"linear_jet_check":"PASS"},sort_keys=True)+"\n")
# Stream every row if feasible, but stop on ACTUAL row/count growth; no solve.
MAX_ROW=100000
MAX_TOTAL=12000000
count=terms=maxdegree=0;visited=0;zero_rows=0;status="COMPLETE_EXACT_PREFIX_REDUCED_IDEAL"
maximum_row={"terms":0}
stream_path=Path("prefix_reduced_ideal.partial.jsonl")
out=stream_path.open("w")
out.write(json.dumps({"type":"ring","field":"Q","order":"global dp","variables":names,"source_sha256":SOURCE_SHA,"prefix":PREFIX,
                     "all_remaining_contract":"ALL physical positive J coefficients through99 plus Zj*J0-1 and160 monic h definitions"})+"\n")
def emit(label,p):
    global count,terms,maxdegree
    text=str(p)
    out.write(json.dumps({"type":"generator","index":count,"label":label,"polynomial":text,"terms":len(p),"degree":int(p.total_degree())},sort_keys=True)+"\n")
    count+=1;terms+=len(p);maxdegree=max(maxdegree,int(p.total_degree()))
for p,v in graphdefs.items():emit(f"define_Hfact_{p[0]}_{p[1]}",v)
emit("inverse_J",vals["Zj"]*J0-one)
for pos in sorted(support,key=lambda p:(-sum(p),p)):
    if pos==(0,0):continue
    value=Jcoef(pos);visited+=1
    if not value:zero_rows+=1;continue
    n=len(value)
    if n>maximum_row["terms"]:maximum_row={"terms":n,"physical_row":pos,"degree":int(value.total_degree())}
    if n>MAX_ROW or terms+n>MAX_TOTAL:
        status="ACTUAL_TERM_CAP";event("typed_stop",status=status,next_row=pos,next_terms=n,emitted_terms=terms);break
    emit(f"J_{pos[0]}_{pos[1]}",value)
    if visited%50==0:event("residual_rows",visited=visited,generators=count,terms=terms,last_physical_degree=sum(pos),maximum_row=maximum_row)
footer={"type":"terminal","status":status,"generators":count,"terms":terms,"visited_positive_slots":visited,"zero_rows":zero_rows}
out.write(json.dumps(footer,sort_keys=True)+"\n");out.flush();os.fsync(out.fileno());out.close()
if status.startswith("COMPLETE"):
    os.replace(stream_path,Path("prefix_reduced_ideal.jsonl"));stream_path=Path("prefix_reduced_ideal.jsonl")
summary={"status":status,"source_sha256":SOURCE_SHA,"pivot_sha256":CERT_SHA,"variables":len(names),
         "prefix_C_degrees":[35,34,33],"eliminated_C_coordinates":PREFIX,"remaining_C_graph_nodes":165,"free_nonconstant_C":2,
         "prefix_rows":prefix_data,"prefix_reconstruction_terms":sum(len(v) for v in R.values()),
         "prefix_reconstruction_maximum_degree":max(int(v.total_degree()) for v in R.values()),
         "reconstructed_C":stats(C),"selected_rows_exact_zero":True,"J0_linear_jet_check":"PASS",
         "candidate_positive_slots":len(support)-1,"visited_positive_slots":visited,
         "emitted_generators":count,"emitted_terms":terms,"maximum_ideal_degree":maxdegree,"maximum_J_row":maximum_row,
         "zero_rows":zero_rows,"actual_term_caps":{"row":MAX_ROW,"total":MAX_TOTAL},
         "stream":str(stream_path.resolve()),"stream_bytes":stream_path.stat().st_size,
         "stream_sha256":hashlib.sha256(stream_path.read_bytes()).hexdigest(),
         "complete_smaller_ideal_claim":status.startswith("COMPLETE"),"solver_launched":False,
         "wall_seconds":time.monotonic()-started,"peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path("structured_summary.json").write_text(json.dumps(summary,sort_keys=True,indent=2)+"\n")
event("terminal",summary=summary)
