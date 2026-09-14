#!/usr/bin/env python3
"""Search monomial b0,b1,b2 paths in the h=y^3 residual distribution.

For a fixed path the remaining constants in P enter linearly.  Screen over a
prime at many x values, then verify any hit as an exact SymPy identity.
"""
from itertools import product
from fractions import Fraction
import json
import sympy as s

PRIME=32003
# theta order: a7,a8,k5,k4,k3,k2,k1,c

def rows_at(x,b0,b1,b2,d0,d1,d2,p=PRIME):
    rows=[]
    def add(co,base): rows.append(([z%p for z in co],(-base)%p))
    add([7*b2*d2,16*(b1*d2+b2*d1),30*d0,24*d1,18*d2,0,0,0],
        27*(b0*d2+b1*d1+b2*d0))
    add([7*(b1*d2+b2*d1),16*(b0*d2+b1*d1+b2*d0),0,24*d0,18*d1,12*d2,0,0],
        27*(b0*d1+b1*d0))
    add([28*(b0*d2+b1*d1+b2*d0),64*(b0*d1+b1*d0),-20*b2*d2,0,0+72*d0,48*d1,24*d2,0],
        108*b0*d0-27*b2*b2*d2)
    add([84*(b0*d1+b1*d0),192*b0*d0-64*b2*b2*d2,-60*(b1*d2+b2*d1),-96*b2*d2,0,144*d0,72*d1,0],
        -162*b1*b2*d2-81*b2*b2*d1)
    add([84*b0*d0,-32*b1*b2*d2,-60*b1*d1+60*b2*d0,-48*b1*d2,0,0,72*d0,-72*pow(x,8,p)],
        -54*b1*b1*d2-54*b1*b2*d1+27*b2*b2*d0)
    return rows

def rref_solve(rows,p=PRIME):
    A=[r[0][:]+[r[1]%p] for r in rows]
    m=len(A); n=8; piv=[]; rr=0
    for cc in range(n):
        ii=next((i for i in range(rr,m) if A[i][cc]%p),None)
        if ii is None: continue
        A[rr],A[ii]=A[ii],A[rr]
        inv=pow(A[rr][cc]%p,-1,p)
        A[rr]=[(z*inv)%p for z in A[rr]]
        for i in range(m):
            if i!=rr and A[i][cc]%p:
                q=A[i][cc]%p
                A[i]=[(u-q*v)%p for u,v in zip(A[i],A[rr])]
        piv.append(cc); rr+=1
    if any(all(z%p==0 for z in row[:n]) and row[n]%p for row in A): return None
    # Particular solution; free variables zero.
    sol=[0]*n
    for i,cc in enumerate(piv): sol[cc]=A[i][n]%p
    # Is there a possible nonzero c?
    if 7 in piv:
        c_forced=sol[7]
        c_possible=c_forced!=0
    else:
        c_possible=True
        sol[7]=1
        # back-substitute impact of free c from RREF.
        for i,cc in enumerate(piv): sol[cc]=(A[i][n]-A[i][7])%p
    return sol if c_possible else None

def val(A,e,x,p): return A*pow(x,e,p)%p
def der(A,e,x,p): return 0 if e==0 else A*e*pow(x,e-1,p)%p

def exact_check(data):
    x=s.symbols('x')
    A0,A1,A2=data['coeffs']; e0,e1,e2=data['exponents']
    b0=s.Integer(A0)*x**e0; b1=s.Integer(A1)*x**e1; b2=s.Integer(A2)*x**e2
    d0=s.diff(b0,x);d1=s.diff(b1,x);d2=s.diff(b2,x)
    a7,a8,k5,k4,k3,k2,k1,c=s.symbols('a7 a8 k5 k4 k3 k2 k1 c')
    theta=(a7,a8,k5,k4,k3,k2,k1,c)
    eq=[]
    for xx in range(1,20):
        vals={x:s.Integer(xx)}
        rr=rows_symbolic(x,b0,b1,b2,d0,d1,d2,theta)
        eq.extend([z.subs(vals) for z in rr])
    sol=s.linsolve(eq,theta)
    for tup in sol:
        free=set().union(*(z.free_symbols for z in tup)) - set(theta)
        # linsolve usually reuses theta symbols as free parameters.
        sub={z:s.Integer(1) for z in set().union(*(z.free_symbols for z in tup)) if z in theta}
        cand=tuple(s.factor(z.subs(sub)) for z in tup)
        if cand[-1]==0: continue
        rr=rows_symbolic(x,b0,b1,b2,d0,d1,d2,theta)
        if all(s.expand(z.subs(dict(zip(theta,cand))))==0 for z in rr):
            return [str(z) for z in cand]
    return None

def rows_symbolic(x,b0,b1,b2,d0,d1,d2,th):
    a7,a8,k5,k4,k3,k2,k1,c=th
    return [
      7*a7*b2*d2+16*a8*(b1*d2+b2*d1)+30*k5*d0+24*k4*d1+18*k3*d2+27*(b0*d2+b1*d1+b2*d0),
      7*a7*(b1*d2+b2*d1)+16*a8*(b0*d2+b1*d1+b2*d0)+24*k4*d0+18*k3*d1+12*k2*d2+27*(b0*d1+b1*d0),
      28*a7*(b0*d2+b1*d1+b2*d0)+64*a8*(b0*d1+b1*d0)-20*k5*b2*d2+72*k3*d0+48*k2*d1+24*k1*d2+108*b0*d0-27*b2**2*d2,
      84*a7*(b0*d1+b1*d0)+a8*(192*b0*d0-64*b2**2*d2)-60*k5*(b1*d2+b2*d1)-96*k4*b2*d2+144*k2*d0+72*k1*d1-162*b1*b2*d2-81*b2**2*d1,
      84*a7*b0*d0-32*a8*b1*b2*d2+k5*(-60*b1*d1+60*b2*d0)-48*k4*b1*d2+72*k1*d0-54*b1**2*d2-54*b1*b2*d1+27*b2**2*d0-72*c*x**8,
    ]

def main():
    coeff_choices=(-3,-2,-1,1,2,3)
    hits=[]; tested=0
    # b0 has no constant term.  Chart degree caps: 9,7,6 respectively.
    # Search enough exponents to permit degree-eight r0.
    for e0,e1,e2 in product(range(1,10),range(0,8),range(0,7)):
      possible={2*e0-1,e1+2*e2-1,2*e1+e2-1,2*e1-1,e1+e2-1,2*e2+e0-1,e2+e0-1,e0-1}
      if 8 not in possible: continue
      for A0,A1,A2 in product(coeff_choices,repeat=3):
        tested+=1; rows=[]
        for xx in (1,2,3,4,5,6):
          z=[val(A,e,xx,PRIME) for A,e in ((A0,e0),(A1,e1),(A2,e2))]
          dz=[der(A,e,xx,PRIME) for A,e in ((A0,e0),(A1,e1),(A2,e2))]
          rows += rows_at(xx,*z,*dz)
        sol=rref_solve(rows)
        if sol is None: continue
        data={'exponents':[e0,e1,e2],'coeffs':[A0,A1,A2],'mod_solution':sol}
        qsol=exact_check(data)
        if qsol:
          data['rational_solution']=qsol;hits.append(data);print(json.dumps(data),flush=True)
    print(json.dumps({'tested':tested,'hits':hits},indent=2))

if __name__=='__main__': main()
