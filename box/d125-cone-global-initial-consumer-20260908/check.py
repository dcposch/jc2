#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
import json

def need(ok,msg):
    if not ok: raise ValueError(msg)
def add(*ps):
    r={}
    for p in ps:
        for e,c in p.items(): r[e]=r.get(e,Q(0))+c
    return {e:c for e,c in r.items() if c}
def scale(p,c): return {e:a*c for e,a in p.items() if a*c}
def mul(p,q):
    r={}
    for e,a in p.items():
        for f,b in q.items():
            v=tuple(i+j for i,j in zip(e,f))
            r[v]=r.get(v,Q(0))+a*b
    return {e:c for e,c in r.items() if c}
def deriv(p,i):
    r={}
    for e,c in p.items():
        if e[i]:
            f=list(e); f[i]-=1
            r[tuple(f)]=c*e[i]
    return r
def power(p,n):
    dim=len(next(iter(p)))
    r={(0,)*dim:Q(1)}
    for _ in range(n): r=mul(r,p)
    return r
def wire(p): return [[list(e),str(c)] for e,c in sorted(p.items())]

def check(mode):
    # Independent formal variables, never actual H^3/H^5/source products.
    names=('Z','a','b','da','db','c0','d0','e0','f0')
    def var(i):
        e=[0]*len(names); e[i]=1
        return {tuple(e):Q(1)}
    Z,a,b,da,db,c0,d0,e0,f0=[var(i) for i in range(len(names))]
    def D(p): return add(mul(deriv(p,1),da),mul(deriv(p,2),db))
    P=add(power(Z,3),mul(a,Z),b)
    cc=add(scale(a,Q(5,3)),c0)
    dd=add(scale(b,Q(5,3)),d0)
    ee=add(scale(power(a,2),Q(5,9)),mul(c0,a),e0)
    ff=add(scale(mul(a,b),Q(5,9) if mode=='change-q0' else Q(10,9)),
           mul(c0,b),scale(mul(d0,a),Q(2,3)),f0)
    B=add(power(Z,5),mul(cc,power(Z,3)),mul(dd,power(Z,2)),mul(ee,Z),ff)
    J=add(mul(deriv(P,0),D(B)),scale(mul(D(P),deriv(B,0)),-1))
    shifted=b if mode=='drop-d0-shift' else add(b,scale(d0,Q(3,5)))
    K=scale(e0,Q(9,5))
    J1=add(mul(add(scale(power(a,2),Q(5,9)),scale(e0,-1)),da),
           scale(mul(shifted,db),Q(-10,3)))
    J0=add(mul(add(scale(power(a,2),Q(5,9)),scale(e0,-1)),db),
           scale(mul(mul(a,shifted),da),Q(10,9)))
    need(J==add(mul(J1,Z),J0),'universal 3/5 elimination with all constants')
    integral=add(scale(power(a,3),Q(1,3)),scale(mul(K,a),-1),scale(power(shifted,2),-3))
    need(D(integral)==scale(J1,Q(9,5)),'first integral including d0 shift')
    det=add(power(add(power(a,2),scale(K,-1)),2),scale(mul(a,power(shifted,2)),12))
    quartic=add(scale(power(a,4),6 if mode=='change-quartic' else 7),
                scale(mul(K,power(a,2)),-18),scale(mul(integral,a),-12),scale(power(K,2),3))
    need(scale(det,3)==quartic,'universal determinant quartic')
    # Exact product-ring examples in the independent variables (Z,p).
    z={(1,0):Q(1)}; p={(0,1):Q(1)}; one={(0,0):Q(1)}
    Ptuple=[add(power(z,3),mul(power(p,2),z)),power(z,3),power(z,3)]
    def bracket(A,B): return add(mul(deriv(A,0),deriv(B,1)),scale(mul(deriv(A,1),deriv(B,0)),-1))
    e=one if mode=='replace-odd-e' else p
    lower=[e,{},{}]
    need(any(bracket(A,B) for A,B in zip(Ptuple,lower)),
         'actual lower odd tuple has nonzero bracket')
    # A non-diagonal linear coefficient can evade the weaker argument.
    diagonal=[z,z,z]
    nondiagonal=[{},z,{}]
    need(any(bracket(A,B) for A,B in zip(Ptuple,diagonal)),'diagonal d sees nonconstant component')
    need(not any(bracket(A,B) for A,B in zip(Ptuple,nondiagonal)),
         'actual zero-divisor countercontrol retained')
    values=[]
    for j0 in (2,4,6,8):
        j=Q(j0)
        for q0 in (j0+1,2*j0,None):
            eta=j/2 if q0 is None else min(j/2,Q(q0,3))
            q=3*eta if q0 is None else Q(q0)
            need(j/3<eta<=j/2 and eta<=4,'Newton scale')
            need(10+eta>3*eta,'alpha absent from cubic initial')
            need(20+eta>5*eta and 10+3*eta>5*eta,'scalar B terms above window')
            need(j+4*eta>5*eta and j+3*eta>=5*eta and q+2*eta>=5*eta,
                 'z2 F block bounds')
            need(2*j+eta>=5*eta,'all positive-z G blocks above window')
            need(7*eta<=28 and 7*eta<36,'strict target-order separation')
            values.append({'j':str(j),'q':'infinity' if q0 is None else str(q0),
                           'eta':str(eta),'initial_bracket_bound':str(7*eta)})
    return {'status':'PASS','mode':mode,'formal_bracket':wire(J),'integral':wire(integral),
            'quartic':wire(quartic),'valuation_controls':values,'zero_assert':True,
            'product_controls':'odd e forces nonzero; diagonal d sees all components; nondiagonal countercontrol commutes',
            'source_provenance_claimed':False}

if __name__=='__main__':
    print(json.dumps(check(sys.argv[1] if len(sys.argv)>1 else 'normal'),sort_keys=True))
