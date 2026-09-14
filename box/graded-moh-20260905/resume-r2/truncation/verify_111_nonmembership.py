#!/usr/bin/env python3
"""Independent exact-Q truncated Buchberger nonmembership verifier.
Only algebraic positive assertions are promoted; every check is asserted.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,re,hashlib,time
BASE=Path('/home/ubuntu/jc2/box/graded-moh-20260905')
out=BASE/'resume-r2/truncation/C_n18m12_M2_9_ell2_s3_V3_8_N1/x-specialization'
cust=json.loads((out/'custody.json').read_text());src=Path(cust['original_source_input']);meta=json.loads((src.parent/'manifest.json').read_text());vs=cust['variables'];vi={v:i for i,v in enumerate(vs)};W=cust['weights'];X=cust['target_Bdegree'];nv=len(vs);zero={v for v,n in cust['assignments'][0].items() if n==0}
assert zero=={v for v,w in meta['weights'].items() if w[0]==0}
assert vs==[v for v in meta['variables'] if meta['weights'][v][0]>0]
assert W==[meta['weights'][v][0] for v in vs]
assert X==meta['target_bidegree'][0]
assert hashlib.sha256(Path(meta['source_rows']).read_bytes()).hexdigest()==meta['source_sha256']
assert zero==set(cust['assignments'][0]);assert hashlib.sha256(src.read_bytes()).hexdigest()==cust['original_source_input_sha256']
def parse(s, specialize=False):
 p={}
 for t in re.findall(r'[+-]?[^+-]+',s.replace(' ','').replace('\n','').strip('()')):
  m=[0]*nv;c=F(1)
  for f in t.split('*'):
   if f.startswith('-') and not f[1:].replace('/','').isdigit():c=-c;f=f[1:]
   if f.startswith('+'):f=f[1:]
   a=f.split('^');v=a[0];e=int(a[1]) if len(a)>1 else 1
   if v in zero and specialize:c=F(0);break
   if v in vi:m[vi[v]]+=e
   else:c*=F(f)
  if c:
   k=tuple(m);p[k]=p.get(k,F(0))+c
 return {k:c for k,c in p.items() if c}
def deg(m):return sum(a*b for a,b in zip(m,W))
def key(m):return (deg(m),tuple(-e for e in reversed(m)))
def lm(p):return max(p,key=key)
def divisible(m,n):return all(a>=b for a,b in zip(m,n))
def submul(p,q,m,c):
 for n,a in q.items():
  k=tuple(x+y for x,y in zip(n,m));p[k]=p.get(k,F(0))-c*a
  if not p[k]:del p[k]
def reduce(p,G):
 p=dict(p);rem={}
 while p:
  n=lm(p);c=p[n]
  for g,l,d in G:
   if divisible(n,l):submul(p,g,tuple(a-b for a,b in zip(n,l)),c/d);break
  else:rem[n]=c;del p[n]
 return rem
G0=[parse(s) for s in (out/'basis-0.txt').read_text().strip().split(',')];assert all(g for g in G0)
G=[(g,lm(g),g[lm(g)]) for g in G0];assert all(len({deg(m) for m in g})==1 and deg(lm(g))<=X for g in G0)
rows=[]
for line in Path(meta['source_rows']).read_text().splitlines()[1:]:
 idx,j,b,a,expr=line.split('|',4)
 if int(idx) in {r['source'] for r in meta['selected_rows']}:rows.append(parse(expr,True))
assert len(rows)==meta['selected_row_count']
start=time.monotonic();assert all(not reduce(f,G) for f in rows)
count=0
for (g,l,c),(h,m,d) in combinations(G,2):
 n=tuple(max(a,b) for a,b in zip(l,m))
 if deg(n)>X:continue
 sp={};submul(sp,g,tuple(a-b for a,b in zip(n,l)),-1/c);submul(sp,h,tuple(a-b for a,b in zip(n,m)),1/d)
 assert not reduce(sp,G);count+=1
c=parse('c');nf=reduce(c,G);assert nf==c
perturb=dict(rows[0]);perturb[next(iter(c))]=perturb.get(next(iter(c)),F(0))+1
assert reduce(perturb,G)  # Deliberate row+c corruption is detected.
assert not reduce(G0[0],G) # positive control
result=dict(coefficient_field='Q',source_rows_checked=len(rows),basis_elements=len(G),basis_homogeneous_in_B=True,truncated_degree=X,spairs_checked=count,input_images_reduce_zero=True,all_required_spairs_reduce_zero=True,c_normalform='c',c_nonmembership=True,negative_corrupted_row_detected=True,positive_basis_row_reduces_zero=True,elapsed_seconds=time.monotonic()-start,proof_scope='c is not in the full original ideal by exact bidegree restriction and a rational specialization preserving B; no claim about c powers or saturation.',files={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [src,Path(meta['source_rows']),out/'basis-0.txt',Path(__file__)]})
(out/'independent-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
