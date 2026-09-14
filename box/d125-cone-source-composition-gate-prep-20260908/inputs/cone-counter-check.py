#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
import json

def need(ok,msg):
    if not ok:
        raise ValueError(msg)

# Exact Q[zeta]/(zeta^2-zeta+1); no numerical roots or floats.
O=(F(0),F(0))
I=(F(1),F(0))
def qa(x,y): return (x[0]+y[0],x[1]+y[1])
def qs(x,c): return (x[0]*c,x[1]*c)
def qm(x,y):
    a,b=x
    c,d=y
    return (a*c-b*d,a*d+b*c+b*d)
def qi(x):
    a,b=x
    n=a*a+a*b+b*b
    need(n!=0,'field inversion')
    return ((a+b)/n,-b/n)
def qp(x,n):
    y=I
    for _ in range(n): y=qm(y,x)
    return y
def la(*ps):
    r={}
    for p in ps:
        for e,c in p.items(): r[e]=qa(r.get(e,O),c)
    return {e:c for e,c in r.items() if c!=O}
def lm(p,q):
    r={}
    for i,a in p.items():
        for j,b in q.items(): r[i+j]=qa(r.get(i+j,O),qm(a,b))
    return {e:c for e,c in r.items() if c!=O}
def ls(p,c): return {e:qs(a,c) for e,a in p.items() if qs(a,c)!=O}
def restrict(poly,z):
    r={}
    for (i,j),c in poly.items():
        r=la(r,{i+j:qs(qp(z,i),c)})
    return r
def dg(poly): return {(i-1,j):c*i for (i,j),c in poly.items() if i}
def wire(poly): return [[e,str(c[0]),str(c[1])] for e,c in sorted(poly.items())]
def regular(poly): return all(e>=0 for e in poly)
def first(poly,z,g1):
    p0=restrict(poly,z)
    p1=lm(restrict(dg(poly),z),g1)
    need(bool(p0 or p1),'control needs first coefficient within order1')
    return (0,p0) if p0 else (1,p1)

def run(mode):
    # Actual odd normal remainders of degree3, not actual source pairs.
    A={(1,2):F(1),(0,3):F(1)}
    B={(2,1):F(1),(1,2):F(-1),(0,3):F(1)}
    if mode=='replace-F': A={(0,3):F(1)}
    for poly,bound,degree in ((A,3,13),(B,5,23)):
        need(max(5*i-7*j for i,j in poly)<=bound,'weight bound')
        need(max(i+j for i,j in poly)<=degree,'degree bound')
        need(all((i+j)%2==1 for i,j in poly),'odd parity')
        need(all(i<3 or j<2 for i,j in poly),'monomial normality')
    roots=[(F(-1),F(0)),(F(0),F(1)),(F(1),F(-1))]
    rows=[]
    globalA=[]
    globalB=[]
    for z in roots:
        need(qp(z,3)==qs(I,-1),'actual cone root')
        g0={1:z}
        g1={-3:qs(qi(qp(z,2)),F(-1,3))}
        if mode=='freeze-moving-root': g1={}
        # R_s=p2(g3+p3)+s*p, only its exact order0/order1 are used.
        r0=la(lm({2:I},la(lm(lm(g0,g0),g0),{3:I})))
        if mode=='change-central-curve': r0=la(r0,{3:qs(I,-3)})
        need(not r0,'central curve actually contains branch')
        r1=la(ls(lm({2:I},lm(lm(g0,g0),g1)),3),{1:I})
        need(not r1,'actual moving implicit equation at order1')
        a0=restrict(A,z)
        b0=restrict(B,z)
        globalA.append(a0)
        globalB.append(b0)
        aa,af=first(A,z,g1)
        bb,bf=first(B,z,g1)
        need(regular(a0) and regular(b0),'product-global initials regular')
        need(qm(qp(z,2),qi(qs(qp(z,2),3)))==qs(I,F(1,3)),
             'target initial ratio g2/Rg=1/(3p2)')
        rows.append({'root':[str(z[0]),str(z[1])],
                     'F_initial_order':aa,'F_initial':wire(af),'F_regular':regular(af),
                     'G_initial_order':bb,'G_initial':wire(bf),'G_regular':regular(bf),
                     'F_global_initial':wire(a0),'G_global_initial':wire(b0)})
    need(any(globalA) and any(globalB),'global product injections survive')
    need(all(not (r['F_regular'] and r['G_regular']) for r in rows),
         'no common branch with both first moving residues regular')
    return {'status':'PASS','mode':mode,'field':'Q[zeta]/(zeta^2-zeta+1)',
            'branches':rows,'source_first_contact_assumed':False,
            'scalar_initial_control':{'formal_F':'s^2*R_s','eta':1,'A_initial':'Z^3+Z',
                                      'nonconstant_coefficient':False},'zero_assert':True}

if __name__=='__main__':
    print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else 'normal'),sort_keys=True))
