#!/usr/bin/env python3
"""Exact fixed-Q reduction for centered degree-(6,9) Jacobian equations.

This module is a faster equivalent of ``search_linear_q.py``.  For

  Q=z^6+sum(r=0..4) q_r(x)z^r,
  P=z^9+sum(s=0..8) p_s(x)z^s,

the coefficients z^13 down through z^5 recursively determine p_8,...,p_0
up to their nine x-constant integration constants.  It then checks the five
remaining z bands and the completed-chart x-degree bounds exactly over GF(p).
"""

from __future__ import annotations

NV=9
P_BOUND={s:27-3*s for s in range(9)}


def zero():return [0]*(NV+1)
def scalar(c,p):v=zero();v[NV]=c%p;return v
def unit(i):v=zero();v[i]=1;return v
def va(a,b,p):return [(x+y)%p for x,y in zip(a,b)]
def vs(a,c,p):return [x*c%p for x in a]


def pa(*fs,p):
 out={}
 for f in fs:
  for e,v in f.items():
   out[e]=va(out.get(e,zero()),v,p)
   if not any(out[e]):del out[e]
 return out


def ps(f,c,p):return {e:vs(v,c,p) for e,v in f.items() if any(vs(v,c,p))}
def pd(f,p):return {e-1:vs(v,e,p) for e,v in f.items() if e and any(vs(v,e,p))}
def pi(f,p,slot):
 out={e+1:vs(v,pow(e+1,-1,p),p) for e,v in f.items()}
 out[0]=unit(slot);return out
def fd(f,p):return {e-1:e*c%p for e,c in f.items() if e and e*c%p}


def fm(f,a,p):
 out={}
 for i,c in f.items():
  for j,v in a.items():
   e=i+j;out[e]=va(out.get(e,zero()),vs(v,c,p),p)
   if not any(out[e]):del out[e]
 return out


def fixed_affine(f,p):return {e:scalar(c,p) for e,c in f.items()}


def bracket_band(q,pset,k,p):
 """Coefficient of z^k in {Q,P}; q is fixed, pset affine."""
 out={}
 for r,qr in q.items():
  dqr=fd(qr,p)
  for s,pp in pset.items():
   if r+s-1!=k:continue
   if s and dqr:out=pa(out,ps(fm(dqr,pp,p),s,p),p=p)
   if r:
    dpp=pd(pp,p)
    if dpp:out=pa(out,ps(fm(qr,dpp,p),-r,p),p=p)
 return out


def reduce_q(qfixed,p):
 """Return (linear rows, target, reconstructed affine p_s)."""
 q={r:dict(f) for r,f in qfixed.items()}
 q[6]={0:1}
 pset={9:{0:scalar(1,p)}}
 inv6=pow(6,-1,p)
 for s in range(8,-1,-1):
  k=s+5
  # The omitted leading-Q contribution is -6*p_s'.
  other=bracket_band({r:f for r,f in q.items() if r!=6},pset,k,p)
  pset[s]=pi(ps(other,inv6,p),p,s)
 rows=[]
 for s in range(9):
  rows.extend(v for e,v in pset[s].items() if e>P_BOUND[s] and any(v))
 target=zero()
 for k in range(5):
  band=bracket_band(q,pset,k,p)
  for e,v in band.items():
   if k==0 and e==8:target=v
   elif any(v):rows.append(v)
 return rows,target,pset


def solve(rows,target,p,want_assignment=False):
 piv={}
 for orig in rows:
  row=orig[:]
  while True:
   cols=[i for i in range(NV) if row[i]]
   if not cols:
    if row[NV]:return False,None,None
    break
   q=min(cols)
   if q not in piv:
    inv=pow(row[q],-1,p);row=[x*inv%p for x in row]
    for old in piv.values():
     fac=old[q]
     if fac:old[:]=[(x-fac*y)%p for x,y in zip(old,row)]
    piv[q]=row;break
   fac=row[q];row=[(x-fac*y)%p for x,y in zip(row,piv[q])]
 tr=target[:]
 for q in sorted(piv):
  fac=tr[q]
  if fac:
   tr[q]=0
   for i in range(q+1,NV):tr[i]=(tr[i]-fac*piv[q][i])%p
   tr[NV]=(tr[NV]-fac*piv[q][NV])%p
 assignment=None
 if want_assignment and any(tr):
  assignment=[0]*NV
  free=[i for i in range(NV) if i not in piv]
  # Pick a free coordinate if needed to make target nonzero.
  if not tr[NV]:
   j=next(i for i in free if tr[i]);assignment[j]=1
  for q in sorted(piv,reverse=True):
   assignment[q]=(-piv[q][NV]-sum(piv[q][i]*assignment[i] for i in range(q+1,NV)))%p
 return True,tr,assignment

