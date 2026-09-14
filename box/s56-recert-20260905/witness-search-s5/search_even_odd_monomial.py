#!/usr/bin/env python3
"""Monomial-path search in the centered even-Q/odd-P S5 subchart."""
from itertools import product
import json
import sympy as s

MOD=32003
# unknown theta k3,k2,k1,k0,c
def at(x,A,B,C,dA,dB,dC,p=MOD):
    rows=[]
    def add(cols,base): rows.append(([z%p for z in cols],(-base)%p))
    base2=(-3645*A**4*dA+5832*A**3*dB+17496*A**2*B*dA-11664*A**2*dC
           -23328*A*B*dB-23328*A*C*dA-11664*B**2*dA+46656*B*dC+46656*C*dB)
    ck3=(3080*A**3*dA-5040*A**2*dB-10080*A*B*dA+12096*A*dC+12096*B*dB+12096*C*dA)
    ck2=(5040*A**2*dA-8640*A*dB-8640*B*dA+51840*dC)
    ck1=(-15552*A*dA+31104*dB)
    ck0=10368*dA
    add([ck3,ck2,ck1,ck0,0],base2)
    base1=(243*A**4*dB-1944*A**3*B*dA-1944*A**3*dC+1944*A**2*B*dB
           +7776*A*B**2*dA+7776*A*B*dC+7776*A*C*dB-11664*B**2*dB
           -15552*B*C*dA+46656*C*dC)
    ck3=(-280*A**3*dB+1680*A**2*B*dA+3024*A**2*dC-2016*A*B*dB
         -4032*B**2*dA+12096*B*dC+12096*C*dB)
    ck2=(-720*A**2*dB+2880*A*B*dA+25920*A*dC-8640*B*dB)
    ck1=(5184*A*dB-10368*B*dA+31104*dC)
    ck0=10368*dB
    add([ck3,ck2,ck1,ck0,0],base1)
    base0=dC*(243*A**4-1944*A**2*B+7776*A*C+3888*B**2)
    ck3=dC*(-280*A**3+2016*A*B+12096*C)
    ck2=dC*(-720*A**2+8640*B)
    ck1=dC*(5184*A)
    ck0=dC*10368
    add([ck3,ck2,ck1,ck0,-10368*pow(x,8,p)],base0)
    return rows

def solve(rows,p=MOD):
    n=5; A=[r[0]+[r[1]] for r in rows]; rr=0;piv=[]
    for j in range(n):
      q=next((i for i in range(rr,len(A)) if A[i][j]%p),None)
      if q is None: continue
      A[rr],A[q]=A[q],A[rr]; inv=pow(A[rr][j]%p,-1,p);A[rr]=[z*inv%p for z in A[rr]]
      for i in range(len(A)):
       if i!=rr and A[i][j]%p:
        u=A[i][j]%p;A[i]=[(v-u*w)%p for v,w in zip(A[i],A[rr])]
      piv.append(j);rr+=1
    if any(all(z%p==0 for z in r[:n]) and r[n]%p for r in A):return None
    z=[0]*n
    for i,j in enumerate(piv):z[j]=A[i][n]%p
    if 4 in piv:
      if z[4]==0:return None
    else:
      z[4]=1
      for i,j in enumerate(piv):z[j]=(A[i][n]-A[i][4])%p
    return z

def exact(data):
    x=s.symbols('x'); k3,k2,k1,k0,c=s.symbols('k3 k2 k1 k0 c');th=(k3,k2,k1,k0,c)
    aa,bb,cc=data['coeffs']; ea,eb,ec=data['exponents']
    A=s.Integer(aa)*x**ea;B=s.Integer(bb)*x**eb;C=s.Integer(cc)*x**ec
    # Reuse the module's exact residual forms.
    import importlib.util,contextlib
    with open('/dev/null','w') as f,contextlib.redirect_stdout(f):
      spec=importlib.util.spec_from_file_location('eo','box/s56-recert-20260905/witness-search-s5/even_odd_distribution.py');eo=importlib.util.module_from_spec(spec);spec.loader.exec_module(eo)
    sub0={eo.A:A,eo.B:B,eo.C:C,eo.dA:s.diff(A,x),eo.dB:s.diff(B,x),eo.dC:s.diff(C,x),eo.k3:k3,eo.k2:k2,eo.k1:k1,eo.k0:k0}
    expr=[s.together(eo.forms[0].subs(sub0)),s.together(eo.forms[1].subs(sub0)),s.together(eo.forms[2].subs(sub0)-c*x**8)]
    eq=[]
    for z in expr: eq += s.Poly(z,x).all_coeffs()
    sol=s.linsolve(eq,th)
    for tup in sol:
      # Pick 1 for free original unknowns, 0 for other generated parameters.
      sy=set().union(*(u.free_symbols for u in tup)); sub={u:(1 if u in th else 0) for u in sy}
      tup=tuple(s.factor(u.subs(sub)) for u in tup)
      if tup[-1]!=0 and all(s.expand(z.subs(dict(zip(th,tup))))==0 for z in expr):return [str(u) for u in tup]
    return None

def main():
  vals=(-4,-3,-2,-1,1,2,3,4);hits=[];tested=0
  for ea,eb,ec in product(range(0,4),range(0,7),range(1,10)):
    # r0 possible exponents, including constant-parameter terms.
    poss={ec-1,ea+ec-1,eb+ec-1,2*ea+ec-1,ea+eb+ec-1,2*eb+ec-1,4*ea+ec-1}
    if 8 not in poss:continue
    for aa,bb,cc in product(vals,repeat=3):
      tested+=1;rr=[]
      for xx in (1,2,3,4,5,6,7):
        vv=[q*pow(xx,e,MOD)%MOD for q,e in ((aa,ea),(bb,eb),(cc,ec))]
        dd=[0 if e==0 else q*e*pow(xx,e-1,MOD)%MOD for q,e in ((aa,ea),(bb,eb),(cc,ec))]
        rr+=at(xx,*vv,*dd)
      z=solve(rr)
      if z is None:continue
      d={'exponents':[ea,eb,ec],'coeffs':[aa,bb,cc],'mod_solution':z}
      q=exact(d)
      if q:d['rational_solution']=q;hits.append(d);print(json.dumps(d),flush=True)
  print(json.dumps({'tested':tested,'hits':hits},indent=2))
if __name__=='__main__':main()
