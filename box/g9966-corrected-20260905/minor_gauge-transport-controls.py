#!/usr/bin/env python3
"""Independent polynomial covariance controls for the final translation gauge."""
from pathlib import Path
from collections import defaultdict
from math import comb
import json,sys,hashlib
import sympy as sp
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
from source_data import SOURCE as D
from translation_controls import translate
q=sp.Rational(2,3)  # exact full-tower control; the group-law proof is symbolic
def add(*ps):
 out=defaultdict(lambda:sp.Integer(0))
 for p in ps:
  for key,v in p.items():out[key]+=v
 return {key:v for key,value in out.items() if (v:=sp.expand(value))!=0}
def mul(p,r):
 out=defaultdict(lambda:sp.Integer(0))
 for (i,j),a in p.items():
  for (k,l),b in r.items():out[i+k,j+l]+=a*b
 return {key:v for key,value in out.items() if (v:=sp.expand(value))!=0}
def power(p,n):
 out={(0,0):sp.Integer(1)}
 for _ in range(n):out=mul(out,p)
 return out
def eq(p,r):
 assert all(sp.expand(p.get(key,0)-r.get(key,0))==0 for key in set(p)|set(r))
def shift(p):return {(r+1,k):v for (r,k),v in p.items()}
H=dict(D['h3_top'])
for pos,value in D['h3_equality'].items():H[pos]=value.subs({sp.Symbol('beta'):1,sp.Symbol('ell'):sp.Rational(7,5)})
H[D['h3_degree'],0]=sp.Integer(2)
U={(8,10):sp.Integer(3),(12,7):sp.Integer(-2),(22,0):sp.Integer(5)}
V={(20,9):sp.Integer(7),(32,0):sp.Integer(-3)}
K=add(power(H,3),mul(U,H),V)
TH=translate(H,11,q);TU=translate(U,22,q);TV=translate(V,33,q)
eq(translate(K,33,q),add(power(TH,3),mul(TU,TH),TV))
outer={}
for i,(name,(degree,floor,threshold)) in enumerate(D['outer_specs'].items()):
 qdegree=min(D['outer_qcap'],degree-1)
 outer[name]={(degree-qdegree-1,qdegree):sp.Integer(i+2),(degree,0):sp.Integer(3-i)}
 for key in outer[name]:assert key[0]+key[1]<=degree
 eq(translate(shift(outer[name]),degree+1,q),shift(translate(outer[name],degree,q)))
A,B,C,E=(shift(outer[name]) for name in ['A2','A3','B1','B2'])
F=add(power(K,3),mul(A,K),B);G=add(power(K,2),mul(C,K),E)
TK=translate(K,33,q)
TA,TB,TC,TE=(shift(translate(outer[name],D['outer_specs'][name][0],q)) for name in ['A2','A3','B1','B2'])
eq(translate(F,99,q),add(power(TK,3),mul(TA,TK),TB))
eq(translate(G,66,q),add(power(TK,2),mul(TC,TK),TE))
# Verify the explicit source-coordinate pullback, independently of normalized
# coefficient composition, on a mixed polynomial containing low/high supports.
q=sp.Symbol('translation_q')
x,y=sp.symbols('x y');poly={(1,2):sp.Integer(3),(3,1):sp.Integer(-2),(5,0):sp.Integer(7)};degree=7
physical=sum(c*x**(degree-r-k)*(y-x)**k for (r,k),c in poly.items())
image=sum(c*x**(degree-r-k)*(y-x)**k for (r,k),c in translate(poly,degree,q).items())
assert sp.expand(image-physical.subs({x:x+q,y:y+q},simultaneous=True))==0
f=x**3*y**2+2*x-y+3;g=x*y**3+x**2+2*y
J=sp.diff(f,x)*sp.diff(g,y)-sp.diff(f,y)*sp.diff(g,x)
fq=f.subs({x:x+q,y:y+q},simultaneous=True);gq=g.subs({x:x+q,y:y+q},simultaneous=True)
Jq=sp.diff(fq,x)*sp.diff(gq,y)-sp.diff(fq,y)*sp.diff(gq,x)
assert sp.expand(Jq-J.subs({x:x+q,y:y+q},simultaneous=True))==0
out={'status':'PASS','full_tower_exact_translation_parameter':'2/3','inner_canonical_identity_covariance':True,
 'outer_one_t_shift_covariance_all_four_blocks':True,'F_and_G_full_normalization_covariance':True,
 'direct_physical_source_pullback_matches_normalized_map':True,'Jacobian_chain_rule_under_diagonal_translation':True,
 'translated_H_constant':str(TH[D['h3_degree'],0]),'Hc_constant_invariant':TH[D['h3_degree'],0]==2,
 'term_counts':{'H':len(H),'K2':len(K),'F':len(F),'G':len(G)},
 'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'minor_gauge-transport-controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
