#!/usr/bin/env python3
"""Individual lift projections and universal axis jets, never full source."""
import ast
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json
import resource
import sys

resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024, 512*1024*1024))
NAMES = ('a','b','c','E0','E2','D0','D2','D4','k','alpha','beta','gamma','t')
ZERO = (0,)*len(NAMES)
def need(ok, why):
    if not ok: raise ValueError(why)
def const(c): return {ZERO: Q(c)} if c else {}
def var(n):
    e=list(ZERO); e[NAMES.index(n)]=1
    return {tuple(e):Q(1)}
def add(*polys):
    out={}
    for p in polys:
        for e,c in p.items(): out[e]=out.get(e,Q(0))+c
    return {e:c for e,c in out.items() if c}
def scale(p,c): return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            h=tuple(x+y for x,y in zip(e,f)); out[h]=out.get(h,Q(0))+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out=const(1)
    for _ in range(n): out=mul(out,p)
    return out
def subst(p,values):
    out={}
    for e,c in p.items():
        term=const(c)
        for n,j in zip(NAMES,e): term=mul(term,power(values.get(n,var(n)),j))
        out=add(out,term)
    return out
def upmul(p,q):
    out={}
    for i,c in p.items():
        for j,d in q.items(): out[i+j]=add(out.get(i+j,{}),mul(c,d))
    return {i:c for i,c in out.items() if c}
def project(i,j,t,e):
    num=e+i+j-5*t
    if num%2: return 0
    d=num//2
    if not (0<=t<=j and 0<=d<=j-t): return 0
    return (-1)**(j-t)*comb(j,t)*comb(j-t,d)
def top_projection(m, changed=False):
    # H^m has these m+1 fixed monomials; no polynomial power is expanded.
    terms=[]
    for r in range(m+1):
        i,j=3*(m-r),2*m+3*r
        coefficient=comb(m,r)+(1 if changed and r==0 else 0)
        terms.append(coefficient*project(i,j,m,0))
    return terms

def main(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert gate')
    atop=top_projection(3,mode=='face-a')
    btop=top_projection(5,mode=='face-b')
    need(sum(atop)==27,'actual A top projection')
    need(sum(btop)==243,'actual B top projection')
    # Independent degree-three Laurent expansion of (v^4u-v-v^-1)^3.
    terms={(0,0):1}; images={(1,4):1,(0,1):-1,(0,-1):-1}
    for _ in range(3):
        out={}
        for (t,e),c in terms.items():
            for (tt,ee),d in images.items(): out[t+tt,e+ee]=out.get((t+tt,e+ee),0)+c*d
        terms=out
    need(all(project(0,3,t,e)==c for (t,e),c in terms.items()),'independent cubic projection')
    a,b,c,E0,E2,D0,D2,D4,k,al,be,ga,t=map(var,NAMES)
    Pu={2:const(81),0:a}; Qu={4:const(1215),2:scale(b,3),0:c}
    Pv={2:E2,0:E0}; Qv={4:D4,2:D2,0:D0}
    pos,neg=upmul(Pu,Qv),upmul(Pv,Qu)
    J={i:add(pos.get(i,{}),scale(neg.get(i,{}),-1)) for i in (0,2,4,6)}
    target=scale(power(k,3),Q(5,9))
    rows=dict(J); rows[0]=add(rows[0],target)
    delta=add(c,scale(mul(a,b),Q(-1,27)),scale(power(a,2),Q(5,9) if mode=='delta-factor' else Q(5,27)))
    E=E0 if mode=='omit-E2' else add(E0,scale(mul(a,E2),Q(-1,81)))
    certificate=add(scale(rows[0],-1),scale(mul(a,rows[2]),Q(1,81)),scale(mul(power(a,2),rows[4]),Q(-1,81**2)))
    if mode!='omit-row6': certificate=add(certificate,scale(mul(power(a,3),rows[6]),Q(1,81**3)))
    lhs=add(mul(E,delta),target if mode=='target-sign' else scale(target,-1))
    need(lhs==certificate,'universal four-row Bezout identity')
    # Actual degree-five R_t projections (linear in t, no R^3/R^5).
    R={(3,2):const(1),(0,5):const(1),(1,2):add(t,const(3)),(0,3):t,(0,1):scale(add(t,const(3)),-1)}
    raxis=add(*(scale(co,project(i,j,1,0)) for (i,j),co in R.items()))
    rv=add(*(scale(co,project(i,j,0,1)) for (i,j),co in R.items()))
    need(raxis==const(3) and rv==scale(add(t,const(4)),-1),'actual R axis and normal projection')
    boundary={'a':scale(al,3),'b':scale(be,27),'c':scale(ga,3),'E2':scale(rv,27),'E0':mul(al,rv)}
    Delta=add(ga,scale(mul(be,al),-1),scale(power(al,2),Q(5,9)))
    need(subst(delta,boundary)==scale(Delta,3),'boundary coefficient normalization')
    need(subst(E,boundary)=={},'boundary E vanishes')
    # Axis-only model over Q[epsilon]/epsilon^2: a=epsilon is not inverted.
    dual={'a':(Q(0),Q(1)),'b':(Q(0),Q(0)),'c':(Q(5,9),Q(0)),
          'E0':(Q(1),Q(0)),'E2':(Q(0),Q(0)),'D0':(Q(0),Q(-5,27)),
          'D2':(Q(15),Q(0)),'D4':(Q(0),Q(0)),'k':(Q(1),Q(0))}
    def dm(x,y): return x[0]*y[0],x[0]*y[1]+x[1]*y[0]
    def ev(p):
        out=(Q(0),Q(0))
        for ex,co in p.items():
            term=(co,Q(0))
            for n,j in zip(NAMES,ex):
                for _ in range(j): term=dm(term,dual.get(n,(Q(0),Q(0))))
            out=(out[0]+term[0],out[1]+term[1])
        return out
    need(all(ev(row)==(0,0) for row in rows.values()),'nonreduced axis control')
    return {'status':'PASS','A_leading_terms':atop,'B_leading_terms':btop,
            'delta':'c-a*b/27+5*a^2/27','E':'E0-a*E2/81',
            'certificate_rows':[0,2,4,6],'boundary_delta_factor':3,
            'boundary_E':0,'nonreduced_axis_control':True,
            'scope':'individual projections/universal univariate jets only; no full source point or expansion'}

if __name__=='__main__': print(json.dumps(main(sys.argv[1] if len(sys.argv)>1 else ''),sort_keys=True))
