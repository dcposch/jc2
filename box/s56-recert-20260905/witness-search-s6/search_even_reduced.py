#!/usr/bin/env python3
"""Reduced finite-field scan for even Q and odd P.

Q=z^6+a(x)z^4+b(x)z^2+c(x),
P=z^9+u7(x)z^7+u5(x)z^5+u3(x)z^3+u1(x)z.

The upper four coefficient equations recursively integrate u7,u5,u3,u1;
only four integration constants remain.  This makes exhaustive coefficient
screens for sparse a,b,c inexpensive.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

NV = 4  # k7,k5,k3,k1; affine constant is slot NV


def sc(c, p):
    c %= p
    return [0]*NV+[c]


def unit(i):
    v=[0]*(NV+1);v[i]=1;return v


def vadd(a,b,p): return [(x+y)%p for x,y in zip(a,b)]
def vscale(a,c,p): return [x*c%p for x in a]


def padd(*fs,p):
    out={}
    for f in fs:
        for e,v in f.items():
            out[e]=vadd(out.get(e,[0]*(NV+1)),v,p)
            if not any(out[e]):del out[e]
    return out


def pscale(f,c,p): return {e:vscale(v,c,p) for e,v in f.items() if any(vscale(v,c,p))}


def deriv(f,p):
    return {e-1:vscale(v,e,p) for e,v in f.items() if e and any(vscale(v,e,p))}


def integ(f,p,const_slot):
    out={e+1:vscale(v,pow(e+1,-1,p),p) for e,v in f.items()}
    out[0]=unit(const_slot)
    return out


def fixed_mul(a,f,p):
    out={}
    for i,c in a.items():
        for j,v in f.items():
            e=i+j;out[e]=vadd(out.get(e,[0]*(NV+1)),vscale(v,c,p),p)
            if not any(out[e]):del out[e]
    return out


def fixed_deriv(a,p): return {e-1:e*c%p for e,c in a.items() if e and e*c%p}


def fixed(exp,coeff,p): return {} if not coeff%p else {exp:coeff%p}


def affine_fixed(a): return {e:sc(c,10**18+3) for e,c in a.items()}  # unused


def equations(ea,eb,ec,A,B,C,p):
    a,b,c=fixed(ea,A,p),fixed(eb,B,p),fixed(ec,C,p)
    da,db,dc=fixed_deriv(a,p),fixed_deriv(b,p),fixed_deriv(c,p)
    daA={e:sc(v,p) for e,v in da.items()};dbA={e:sc(v,p) for e,v in db.items()};dcA={e:sc(v,p) for e,v in dc.items()}
    inv2=pow(2,-1,p);inv6=pow(6,-1,p)
    u7=integ(pscale(daA,3*inv2,p),p,0)
    du7=deriv(u7,p)
    rhs=padd(pscale(fixed_mul(a,du7,p),-4,p),pscale(fixed_mul(da,u7,p),7,p),pscale(dbA,9,p),p=p)
    u5=integ(pscale(rhs,inv6,p),p,1);du5=deriv(u5,p)
    rhs=padd(pscale(fixed_mul(a,du5,p),-4,p),pscale(fixed_mul(b,du7,p),-2,p),
              pscale(fixed_mul(da,u5,p),5,p),pscale(fixed_mul(db,u7,p),7,p),pscale(dcA,9,p),p=p)
    u3=integ(pscale(rhs,inv6,p),p,2);du3=deriv(u3,p)
    rhs=padd(pscale(fixed_mul(a,du3,p),-4,p),pscale(fixed_mul(b,du5,p),-2,p),
              pscale(fixed_mul(da,u3,p),3,p),pscale(fixed_mul(db,u5,p),5,p),pscale(fixed_mul(dc,u7,p),7,p),p=p)
    u1=integ(pscale(rhs,inv6,p),p,3);du1=deriv(u1,p)
    E4=padd(pscale(fixed_mul(a,du1,p),-4,p),pscale(fixed_mul(b,du3,p),-2,p),
             fixed_mul(da,u1,p),pscale(fixed_mul(db,u3,p),3,p),pscale(fixed_mul(dc,u5,p),5,p),p=p)
    E2=padd(pscale(fixed_mul(b,du1,p),-2,p),fixed_mul(db,u1,p),pscale(fixed_mul(dc,u3,p),3,p),p=p)
    E0=fixed_mul(dc,u1,p)
    rows=[];target=[0]*(NV+1)
    for E in (E4,E2):rows.extend(v for v in E.values() if any(v))
    for zd,u,bound in ((7,u7,6),(5,u5,12),(3,u3,18),(1,u1,24)):
        rows.extend(v for e,v in u.items() if e>bound and any(v))
    for e,v in E0.items():
        if e==8:target=v
        elif any(v):rows.append(v)
    return rows,target


def solve(rows,target,p):
    piv={}
    for orig in rows:
        row=orig[:]
        while True:
            cols=[i for i in range(NV) if row[i]]
            if not cols:
                if row[NV]:return False,None
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
            # p_q = -free - const
            tr[NV]=(tr[NV]-fac*piv[q][NV])%p
    return True,tr


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=32003)
    ap.add_argument('--all-field',action='store_true');ap.add_argument('--out',type=Path)
    ap.add_argument('--coeff-min',type=int,default=-20);ap.add_argument('--coeff-max',type=int,default=20)
    args=ap.parse_args();p=args.prime
    Cs=range(1,p) if args.all_field else [i%p for i in range(args.coeff_min,args.coeff_max+1) if i]
    hits=[];seen=0
    for ea in range(7):
      for eb in range(13):
       for C in Cs:
        seen+=1;rows,target=equations(ea,eb,9,1,1,C,p);ok,tr=solve(rows,target,p)
        if ok and any(tr):
            hit={'exponents':[ea,eb,9],'coefficients':[1,1,C],'target':tr}
            hits.append(hit);print(json.dumps(hit),flush=True)
    payload={'prime':p,'seen':seen,'hit_count':len(hits),'hits':hits}
    if args.out:args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:payload[k] for k in ('prime','seen','hit_count')}))


if __name__=='__main__':main()
