#!/usr/bin/env python3
"""Sparse support audit for the attained T2 + defect-R T3 charts.

This is deliberately a construction audit, not a Groebner decision.  It
enumerates the Proposition-3.1 target terms, checks the exact top cancellations
and localized unit determinants, then measures the occurring-variable
projection of the frozen stage-8 source maps without expanding coefficients.
"""
from __future__ import annotations
import argparse,hashlib,json,re,time
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
CASES={
 "99-delta2":ROOT/"box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json",
 "99-delta52":ROOT/"box/char-degree-20260905/active-gauge/inputs/delta52_stage8.strongest.json",
 "108-free-mean":ROOT/"box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json",
}
ID=re.compile(r"\b[A-Za-z_]\w*\b")
TERM=re.compile(r"^\((.*)\)\*tt\^(\d+)\*zz\^(\d+)$")

def ids(s): return {x for x in ID.findall(s) if x not in {"tt","zz"}}
def add(*tabs):
 out={}
 for tab in tabs:
  for pos,v in tab.items(): out.setdefault(pos,set()).update(v)
 return out
def shift(tab,r=0,z=0,extra=()):
 e=set(extra);return {(a+r,b+z):set(v)|e for (a,b),v in tab.items()}
def mul(a,b,cap):
 out={}
 for (r,z),u in a.items():
  for (s,w),v in b.items():
   if r+s<=cap: out.setdefault((r+s,z+w),set()).update(u|v)
 return out
def power(a,n,cap):
 out={(0,0):set()}
 for _ in range(n): out=mul(out,a,cap)
 return out
def rawtab(tab): return {(int(r),int(z)):ids(e) for r,z,e in tab}
def split_top(s):
 out=[];start=depth=0
 for i,c in enumerate(s):
  if c=="(": depth+=1
  elif c==")": depth-=1
  elif c=="+" and depth==0: out.append(s[start:i]);start=i+1
 out.append(s[start:]);return [x for x in out if x]
def strtab(s):
 out={}
 for term in split_top(s):
  m=TERM.match(term)
  if not m: raise ValueError(term[:160])
  e,r,z=m.groups();out.setdefault((int(r),int(z)),set()).update(ids(e))
 return out

def hopcroft_karp(rows,variables):
 from collections import deque
 adj=[list(vs&variables) for _,vs in rows];pairu={};pairv={};dist={}
 def bfs():
  q=deque();found=False
  for u in range(len(adj)):
   if u not in pairu: dist[u]=0;q.append(u)
   else: dist[u]=-1
  while q:
   u=q.popleft()
   for v in adj[u]:
    w=pairv.get(v)
    if w is None: found=True
    elif dist[w]<0: dist[w]=dist[u]+1;q.append(w)
  return found
 def dfs(u):
  for v in adj[u]:
   w=pairv.get(v)
   if w is None or (dist.get(w)==dist[u]+1 and dfs(w)):
    pairu[u]=v;pairv[v]=u;return True
  dist[u]=-1;return False
 while bfs():
  for u in range(len(adj)):
   if u not in pairu: dfs(u)
 return pairv

def prop31(n,m,D,n2):
 cap=n2*D;out=[]
 for j in range(cap//n+1):
  for a in range(3):
   for b in range(n2):
    weight=j*n+a*m+b*D
    if weight<=cap: out.append({"shift":cap-weight,"F":j,"G":a,"T2":b})
 return sorted(out,key=lambda x:(x["shift"],x["F"],x["G"],x["T2"]))

def exact_controls(n2):
 F,G,L=sp.symbols("F G lambda2",nonzero=True)
 if n2==3:
  mat=sp.Matrix([[2*F,-3*G**2],[-L**3*G,-L**3*F]])
  det=sp.factor(mat.det());expected=-5*L**3*G**3
  # At the common top F=h^3,G=h^2, F^2=G^3.
  reduced=sp.factor(det.subs(F**2,G**3))
  top=("lambda2^3*z^120*(1+z)^45", "lambda2^3*z^120*(1+z)^45")
 else:
  mat=sp.Matrix([[2*F,-3*G**2],[-L**4*G**2,-2*L**4*F*G]])
  det=sp.factor(mat.det());expected=-7*L**4*G**4
  reduced=sp.factor(det.subs(F**2,G**3))
  top=("lambda2^4*z^196*(1+z)^56", "lambda2^4*z^196*(1+z)^56")
 assert sp.expand(reduced-expected)==0
 return {"matrix":str(mat.tolist()),"determinant":str(det),
  "unit_reason":"leading z coefficient is -5*lambda2^3 or -7*lambda2^4; lambda2 is localized",
  "equality_top_lhs":top[0],"equality_top_rhs":top[1]}

def load_case(tag,path):
 data=json.loads(path.read_text())
 if tag.startswith("99"):
  cap0=163;m=data["maps"];base=rawtab(m["h3"])
  h=add(power(base,3,cap0),mul(rawtab(m["C2"]),base,cap0),rawtab(m["C3"]))
  D,C=rawtab(m["B2"]),rawtab(m["A3"]);allvars=set(data["full_free_coordinates"])
  pars=(33,99,66,55,3,145);res=[]
 else:
  h,D,C=strtab(data["h_expr"]),strtab(data["D_expr"]),strtab(data["C_expr"])
  allvars=set(data["names"]);pars=(36,108,72,63,4,227)
  res=[(f"source_{i}",ids(e)) for i,e in enumerate(data.get("residual_strings",[]))]
 return data,h,D,C,allvars,pars,res

def audit(tag,path):
 started=time.monotonic();data,h,D,C,allvars,(k,n,m,D2,n2,D3),rows=load_case(tag,path)
 defect=n2*D2-D3;lead=2*n-D2;qcap=lead+defect
 F=add(power(h,3,qcap),shift(C,1));G=add(power(h,2,qcap),shift(D,1))
 KQ=add(power(G,3,qcap),power(F,2,qcap),
  shift(mul(F,G,qcap),n//3,extra={"target_b"}),
  shift(power(G,2,qcap),2*n//3,extra={"target_a"}),
  shift(F,n,extra={"target_c"}),shift(G,4*n//3,extra={"target_d"}))
 for (r,z),vs in KQ.items():
  if r<lead: rows.append((f"T2_{r}_{z}",vs))
  elif r==lead: rows.append((f"T2top_{r}_{z}",vs|{"lambda2"}))
 Q={(r-lead,z):v for (r,z),v in KQ.items() if lead<=r<=qcap}
 Ft={p:v for p,v in F.items() if p[0]<=defect};Gt={p:v for p,v in G.items() if p[0]<=defect}
 if n2==3:
  R=add(power(Q,3,defect),mul(Ft,Gt,defect),shift(mul(Ft,Q,defect),11,extra={"s11"}))
 else:
  R=add(power(Q,4,defect),mul(Ft,power(Gt,2,defect),defect),
   shift(mul(mul(Ft,Gt,defect),Q,defect),9,extra={"s9"}),
   shift(mul(Ft,power(Q,2,defect),defect),18,extra={"s18"}))
 for (r,z),vs in R.items():
  if r<defect: rows.append((f"T3_{r}_{z}",vs|{"lambda2"}))
  elif r==defect: rows.append((f"T3top_{r}_{z}",vs|{"lambda2","lambda3"}))
 active=set().union(*(v for _,v in rows))|{"lambda2","lambda3","Z2","Z3","Zsep"}
 coeff={v for v in active if v.startswith(("A3c_","B2c_","C2c_","C3c_","K2c_"))}
 outer={v for v in coeff if v.startswith(("A3c_","B2c_"))}
 match_outer=hopcroft_karp(rows,outer);match_coeff=hopcroft_karp(rows,coeff)
 p31=prop31(n,m,D2,n2)
 return {"case":tag,"input":str(path.relative_to(ROOT)),"input_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
  "arithmetic":{"T2_leader_depth":lead,"T3_defect":defect,"Prop31_terms":p31,
   "active_Prop31_shifts":[x for x in p31 if x["shift"]<=defect]},
  "exact_unit_control":exact_controls(n2),
  "support_counts":{"h":len(h),"D":len(D),"C":len(C),"F":len(F),"G":len(G),"KQ":len(KQ),"T2jet":len(Q),
   "T2_rows":sum(name.startswith("T2") for name,_ in rows),"T3_rows":sum(name.startswith("T3") for name,_ in rows),"all_rows":len(rows),
   "input_generators":len(allvars),"active_generators":len(active),"outer_coefficient_generators":len(outer),
   "all_coefficient_generators":len(coeff),"noncoefficient_core":len(active-coeff),"omitted_free_input_generators":len(allvars-active)},
  "incidence_only":{"outer_matching":len(match_outer),"outer_candidate_core":len(active)-len(match_outer),
   "all_coefficient_matching":len(match_coeff),"coefficient_candidate_core":len(active)-len(match_coeff),
   "warning":"Matching certifies occurrence only, not a triangular quotient map; do not classify UNIT/PROPER from it."},
  "elapsed_seconds":round(time.monotonic()-started,3)}

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--case",choices=["all",*CASES],default="all");a=ap.parse_args()
 tags=list(CASES) if a.case=="all" else [a.case]
 print(json.dumps({"status":"PROTOTYPE_NOT_A_DECISION","cases":[audit(t,CASES[t]) for t in tags]},indent=2,sort_keys=True))
if __name__=="__main__": main()
