#!/usr/bin/env python3
"""Independent certificate checks and manual R028 recomputation, no producer imports."""
import json
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
BASE=Path(__file__).resolve().parent
DATA=json.loads((BASE/'closure-fixed-results.json').read_text())
checks=0

def eq(a,b):
 global checks
 checks+=1
 assert a==b,(a,b)

def statekey(node):
 return (node['i'],int(node['rho_f']),F(node['kappa']),int(node['L']),bool(node.get('selected_path',False)))

def fv(vs):return {(F(x),F(y)) for x,y in vs}

for rid,cert in DATA.items():
 src=cert['source'];n,m=src['n'],src['m'];lookup={statekey(v):v for v in cert['nodes']}
 def getnode(i,rho,kappa,L,selected):
  if i==1:
   found=[v for k,v in lookup.items() if k[:4]==(i,rho,kappa,L)]
   assert found
   return found[0]
  return lookup[(i,rho,kappa,L,selected)]
 def values(node):
  if node['i']==1:return {(F(node['final_J']),F(0))} if node['galois_ok'] else set()
  return fv(node.get('values',[]))
 for node in cert['nodes']:
  i,rho,k,L,_=statekey(node);W=n-src['M'][i-1]
  lam=F(m)*k/(W*rho-m);delta=1-F(W)*k/(W*rho-m)
  eq(F(node['delta']),delta)
  if 'A' in node:eq(node['A'],(L*delta).denominator)
  if i==1:
   rg=F(n*rho,m);A=(L*delta).denominator
   eq(F(node['rho_g']),rg)
   eq(F(node['final_J']),F(n,n+m)*rho*(1-delta))
   eq(node['galois_ok'],rg.denominator==1 and rho%A in (0,1) and rg%A in (0,1) and (rho%A,rg%A)!=(1,1))
   continue
  P=F(rho*src['d'][i-1],m);Q=F(rho*W,m)
  eq(F(node['P']),P);eq(F(node['Q']),Q)
  if 'failure' in node:
   eq(P.denominator>1 or Q.denominator>1,True);continue
  A=node['A'];threshold=F(src['d'][i-1],W)
  nodevalues=set()
  for p in node['patterns']:
   z=p['z'];rs=p['orbit_multiplicities']
   eq(z+A*sum(rs),P)
   assert (z>0)+A*len(rs)<=Q
   assert all(r!=threshold for r in ([z] if z else [])+rs)
   assert any(r>threshold for r in ([z] if z else [])+rs)
   # Actual selected route must never be silently resolved between zero and nonzero.
   selected=node.get('selected_path',False);want=src['V'][i-2]
   if selected:
    assert want in ([z] if z else [])+rs
    assert not(z==want and want in rs),('ambiguous selected route',rid,i,p)
   vals={(F(0),F(0))};used=False
   for f in p['factors']:
    r,cnt=f['r'],f['count'];cr=F(m*r,src['d'][i-1]);ck=cr*(1-delta)-lam
    eq(F(f['rho']),cr);eq(F(f['kappa']),ck)
    eq(cnt,1 if f['kind']=='zero' else A)
    if ck<0:
     eq(f['type'],'minor');eq(F(f['delta']),1-ck/cr)
     childvals={(F(0),-ck/cr)}
    else:
     assert ck>0
     childsel=selected and r==want and not used
     if childsel:used=True
     childL=L if f['kind']=='zero' else lcm(L,delta.denominator)
     eq(f['L'],childL);eq(f['selected'],childsel)
     child=getnode(i-1,int(cr),ck,childL,childsel)
     childvals=values(child)
    vals={(a+cnt*x,b+cnt*y) for a,b in vals for x,y in childvals}
   eq(vals,fv(p['values']));nodevalues|=vals
  eq(nodevalues,fv(node['values']))
 rho=F(m*src['v_s'],src['d'][src['s']-1]);kappa=2*rho-m
 root=getnode(src['s']-1,int(rho),kappa,1,True)
 eq(F(cert['minor_base']),F(src['v_s'],src['u_s']))
 full={(a,b+F(cert['minor_base'])) for a,b in values(root)}
 eq(full,fv(cert['full_outcomes']))
 eq({v for v in full if v[0].denominator==1 and v[0]>=v[1]},fv(cert['survivors']))

# Manual R028: use the formulas directly, independently of certificate node values.
def disc(n,m,rho,k,W):return 1-F(W)*k/(W*rho-m),F(m)*k/(W*rho-m)
def major(n,m,rho,k):return F(n)*rho*k/((n+m)*rho-m)
n,m=180,120
bigdelta,biglam=disc(n,m,40,F(30),48)
smalldelta,smalllam=disc(n,m,10,F(5),48)
eq((bigdelta,biglam),(F(1,5),F(2)))
eq((smalldelta,smalllam),(F(1,3),F(5,3)))
bigk=6*(1-bigdelta)-biglam
minororder=bigdelta+biglam/2
smallk2=4*(1-smalldelta)-smalllam
smallk3=6*(1-smalldelta)-smalllam
IM=5*major(n,m,6,bigk)+6*(major(n,m,4,smallk2)+major(n,m,6,smallk3))
Im=F(5)+5*(minororder-1)
eq((IM,Im),(F(22),F(6)))
flat=5*major(n,m,6,bigk)+6*major(n,m,10,F(5))
eq(flat,F(111,4))
# Every split is primitive even under report Lemma A; every deeper M respects genuine ancestor divisors.
assert all(gcd(*x)==1 for x in [(4,1),(1,3),(2,3)])
assert all(132%d==0 for d in [12,6])
assert all(-120%d==0 for d in [60,12,6])
print(json.dumps({'checked_rows':list(DATA),'certificate_equalities':checks,'selected_route_ambiguities':0,'R028_IM':str(IM),'R028_Im_unsplit':str(Im),'R028_flat_IM_same_configuration':str(flat),'R028_passes_A_and_correctly_scoped_B':True},indent=2))
