#!/usr/bin/env python3
"""Exact mixed-modulus lift in the fixed a=0,b=x^5,D=7 slice.

Set FULL_N6=1 to add the depth-six P,Q cap-seven support rows to the
depth-five equations and the depth-six determinant/Cartier rows.
"""
import os
from z3 import BitVec, Solver, Sum, ULT, URem, sat

D=7
X={(1,0):1};Y={(0,1):1}
def mons(D):return [(i,t-i) for t in range(D+1) for i in range(t+1)]
def add(*ps):
 o={}
 for p in ps:
  for m,v in p.items():o[m]=o.get(m,0)+v
 return {m:v for m,v in o.items() if v}
def sc(k,p):return {m:k*v for m,v in p.items() if k*v}
def mul(p,q):
 o={}
 for (i,j),u in p.items():
  for (k,l),v in q.items():o[(i+k,j+l)]=o.get((i+k,j+l),0)+u*v
 return {m:v for m,v in o.items() if v}
def pw(p,n):
 o={(0,0):1}
 for _ in range(n):o=mul(o,p)
 return o
def der(p,v):
 return {((i-1,j) if v==0 else (i,j-1)):u*(i if v==0 else j) for (i,j),u in p.items() if (i if v==0 else j)}
def jac(A,B):return add(mul(der(A,0),der(B,1)),sc(-1,mul(der(A,1),der(B,0))))
def comp(A,B):
 S={}
 for j in range(5):S=add(S,sc(3**j,pw(A,2*j)))
 return add(A,sc(-1,pw(A,3))),mul(B,S)
def put(base,p,d):return add(base,sc(p,d))

a={}
b={(5,0):1}
variables=[(z,m) for z,cap in (('c',5),('d',7),('e',7),('f',7)) for m in mons(cap)]

def residual(digits):
 A=put(put(X,3,a),9,digits.get('c',{}));A=put(A,27,digits.get('e',{}))
 B=put(put(Y,3,b),9,digits.get('d',{}));B=put(B,27,digits.get('f',{}))
 P,Q=comp(A,B);J=add(jac(A,B),{(0,0):-1})
 out={}
 for m,v in J.items():out[('J',m)]=v
 for name,H in (('P',P),('Q',Q)):
  for m,v in H.items():
   if sum(m)>D:out[(name,m)]=v
 return out

base=residual({});cols=[];keys=set(base)
for z,m in variables:
 q=residual({z:{m:1}});keys|=q.keys();cols.append(q)
rows=set()
for key in keys:
 mod=81 if key[0]=='J' else 243
 bb=base.get(key,0)%mod
 dd=tuple((cols[i].get(key,0)-base.get(key,0))%mod for i in range(len(variables)))
 if bb or any(dd):rows.add((mod,bb,dd))
active=sorted({i for _,_,r in rows for i,z in enumerate(r) if z})
print('variables',len(variables),'active',len(active),'rows',len(rows),flush=True)
WIDTH=20
s=Solver();vs=[BitVec(f'u{i}',WIDTH) for i in range(len(variables))]
for i in range(len(vs)):s.add(ULT(vs[i],3))
for mod,bb,row in rows:s.add(URem(bb+Sum([row[i]*vs[i] for i in active if row[i]]),mod)==0)

# Add the exact final determinant digit.  Only {c,d} is nonlinear.
digits={z:{} for z in 'cdef'}
for u,(z,mon) in zip(vs,variables):digits[z][mon]=u
gh=[(z,mon) for z in 'gh' for mon in mons(7)]
ww=[BitVec(f'w{i}',WIDTH) for i in range(len(gh))]
for u in ww:s.add(ULT(u,3))
for u,(z,mon) in zip(ww,gh):digits.setdefault(z,{})[mon]=u

def zn(v):return URem(v,729) if hasattr(v,'sort') else v%729
def zadd(*ps):
 out={}
 for p in ps:
  for mon,v in p.items():
   raw=zn(out.get(mon,0))+zn(v);out[mon]=URem(raw,729) if hasattr(raw,'sort') else raw%729
 return out
def zsc(k,p):
 return {mon:(URem((k%729)*zn(v),729) if hasattr(v,'sort') else ((k%729)*v)%729) for mon,v in p.items()}
def zmul(p,q):
 out={}
 for (i,j),u in p.items():
  for (k,l),v in q.items():
   raw=zn(out.get((i+k,j+l),0))+zn(u)*zn(v)
   out[(i+k,j+l)]=URem(raw,729) if hasattr(raw,'sort') else raw%729
 return out
def zder(p,v):
 return {((i-1,j) if v==0 else (i,j-1)):u*(i if v==0 else j) for (i,j),u in p.items() if (i if v==0 else j)}
def zbr(p,q):return zadd(zmul(zder(p,0),zder(q,1)),zsc(-1,zmul(zder(p,1),zder(q,0))))

L1=zadd(zder(a,0),zder(b,1))
L2=zadd(zder(digits['c'],0),zder(digits['d'],1),zbr(a,b))
L3=zadd(zder(digits['e'],0),zder(digits['f'],1),zbr(a,digits['d']),zbr(digits['c'],b))
L4=zadd(zder(digits['g'],0),zder(digits['h'],1),zbr(a,digits['f']),zbr(digits['c'],digits['d']),zbr(digits['e'],b))
Jerr=zadd(zsc(3,L1),zsc(9,L2),zsc(27,L3),zsc(81,L4))
for coefficient in Jerr.values():s.add(URem(coefficient,243)==0)
L5=zadd(
 zbr(a,digits['h']),zbr(digits['c'],digits['f']),
 zbr(digits['e'],digits['d']),zbr(digits['g'],b),
)
Jerr6=zadd(Jerr,zsc(243,L5))
required=[]
for monomial,coefficient in Jerr6.items():
 if sum(monomial)>6 or (monomial[0]%3==2 and monomial[1]%3==2):
  s.add(URem(coefficient,729)==0);required.append(monomial)
print('n6_fixed_D7_required_rows',len(required),flush=True)

# At depth six the next digits 243*k,243*l cannot alter support above cap
# seven: their direct terms obey the cap, and all nonlinear cross terms vanish
# modulo 729.  Thus these are exact necessary-and-sufficient support rows on
# the depth-five residue.  The displayed p-adic Taylor expansions avoid a
# prohibitively large generic symbolic power expansion.
if os.environ.get('FULL_N6') == '1':
 x2=mul(X,X);x3=mul(x2,X)
 p6=zadd(
  X,zsc(-1,x3),zsc(9,digits['c']),zsc(27,digits['e']),zsc(81,digits['g']),
  zsc(-27,zmul(x2,digits['c'])),zsc(-81,zmul(x2,digits['e'])),
  zsc(-243,zmul(x2,digits['g'])),
  zsc(-243,zmul(X,zmul(digits['c'],digits['c']))),
 )
 sbase={}
 for jj in range(6):sbase=zadd(sbase,zsc(3**jj,pw(X,2*jj)))
 b6=zadd(Y,zsc(3,b),zsc(9,digits['d']),zsc(27,digits['f']),zsc(81,digits['h']))
 q6=zmul(b6,sbase)
 q6=zadd(
  q6,
  zsc(54,zmul(Y,zmul(X,digits['c']))),
  zsc(162,zmul(Y,zmul(X,digits['e']))),
  zsc(486,zmul(Y,zmul(X,digits['g']))),
  zsc(243,zmul(Y,zmul(digits['c'],digits['c']))),
  zsc(324,zmul(Y,zmul(x3,digits['c']))),
  zsc(243,zmul(Y,zmul(x3,digits['e']))),
  zsc(162,zmul(b,zmul(X,digits['c']))),
  zsc(486,zmul(b,zmul(X,digits['e']))),
  zsc(243,zmul(b,zmul(x3,digits['c']))),
  zsc(486,zmul(digits['d'],zmul(X,digits['c']))),
 )
 p6_high={mon:co for mon,co in p6.items() if sum(mon)>D}
 q6_high={mon:co for mon,co in q6.items() if sum(mon)>D}
 for coefficient in p6_high.values():s.add(URem(coefficient,729)==0)
 for coefficient in q6_high.values():s.add(URem(coefficient,729)==0)
 print('n6_support_rows_P_Q',len(p6_high),len(q6_high),flush=True)
 print('depth5_determinant_monomial_rows',len(Jerr),flush=True)
 print('total_solver_assertions_including_201_domains',len(s.assertions()),flush=True)
 if os.environ.get('COUNT_ONLY') == '1':raise SystemExit(0)
s.set(timeout=300000)
status=s.check();print('full_status',status,flush=True)
if status==sat:
 m=s.model()
 for z in 'cdefgh':
  vals={mon:m.eval(u).as_long() for mon,u in digits[z].items() if m.eval(u).as_long()}
  print(z,vals)
