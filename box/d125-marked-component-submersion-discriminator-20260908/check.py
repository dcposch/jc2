#!/usr/bin/python3
import sys
sys.dont_write_bytecode = True
from fractions import Fraction as F
import json

def need(ok, message):
    if not ok:
        raise ValueError(message)

def add(*ps):
    r = {}
    for p in ps:
        for m, c in p.items():
            r[m] = r.get(m, F(0)) + c
    return {m: c for m, c in r.items() if c}

def scale(p, c):
    return {m: v*c for m, v in p.items() if v*c}

def mul(p, q):
    r = {}
    for (i,j), a in p.items():
        for (k,l), b in q.items():
            m = (i+k,j+l)
            r[m] = r.get(m,F(0)) + a*b
    return {m:c for m,c in r.items() if c}

def power(p, n):
    r = {(0,0):F(1)}
    for _ in range(n):
        r = mul(r,p)
    return r

def diff(p, axis):
    r = {}
    for m,c in p.items():
        if m[axis]:
            e = list(m)
            e[axis] -= 1
            r[tuple(e)] = c*m[axis]
    return r

def bracket(p,q):
    return add(mul(diff(p,0),diff(q,1)),scale(mul(diff(p,1),diff(q,0)),-1))

def curve(p):
    # u=v^-3+v^-5, using the same two-variable representation.
    r = {}
    u = {(0,-3):F(1),(0,-5):F(1)}
    for (i,j),c in p.items():
        r = add(r,mul(scale(power(u,i),c),{(0,j):F(1)}))
    return r

def wire(p):
    return [[i,j,str(c)] for (i,j),c in sorted(p.items())]

def run(mode):
    one={(0,0):F(1)}
    u={(1,0):F(1)}
    v={(0,1):F(1)}
    q=add(one,power(v,2))
    N=add(mul(u,power(v,5)),scale(q,-1))
    need(not curve(N),'curve equation')
    Pplus=mul(v,N)
    need(diff(Pplus,0)==power(v,6),'exact embedding submersion u derivative')
    need({m:c for m,c in diff(Pplus,1).items() if m[1]==0}==scale(one,-1),
         'exact embedding submersion on v=0')
    standard=add(mul(power(u,2),v),scale(u,-1))
    need(diff(standard,1)==power(u,2),'standard control derivative')
    need({m:c for m,c in diff(standard,0).items() if m[0]==0}==scale(one,-1),
         'standard control at u=0')
    M=add(v,mul(u,power(v,2)),scale(mul(u,power(v,4)),1 if mode=='bad-M' else -1))
    need(curve(M)=={(0,-3):F(1)},'prescribed cofactor restriction')
    w=add(mul(u,power(v,4)),scale(v,-1))
    need(curve(w)=={(0,-1):F(1)},'polynomial inverse v')
    P=mul(N,M)
    need(curve(diff(P,0))==power(v,2),'normal derivative')
    Q=scale(w,F(-5,9) if mode=='bad-Q-sign' else F(5,9))
    need(curve(bracket(P,Q))==scale(one,F(-5,9)),'marked Jacobian compatibility sign')
    # Check the discriminant uniformly for arbitrary h via coefficient identities.
    # h=0 and a nonconstant h are independent exact controls, not a universal proof.
    for h in ({},add(one,power(v,3))):
        a=add(power(v,2),scale(power(v,4),-1),mul(power(v,5),h))
        b=add(v,scale(mul(q,h),-1))
        need(add(mul(a,q),mul(b,power(v,5)))==power(v,2),'restriction syzygy')
        A=mul(power(v,5),a)
        B=add(mul(power(v,5),b),scale(mul(q,a),-1))
        cc=scale(mul(q,b),-1)
        disc=add(power(B,2),scale(mul(A,cc),-4))
        need(disc==power(v,4),'quadratic discriminant')
    # Minimal cofactor critical point in Q[v]/(v^2-3/5), v a unit.
    z=F(3,5)
    def eval_even(poly, uc):
        total=F(0)
        # u_c is an odd Laurent scalar: u_c=uc*v^-1.
        for (i,j),c in poly.items():
            exponent=j-i
            need(exponent%2==0,'even quotient evaluation')
            total += c*uc**i*z**(exponent//2)
        return total
    uc=F(35,36) # (1-2v^4)/(2v^4(1-v^2))
    if mode=='bad-critical':
        uc=-uc
    # Both derivatives become even Laurent powers after u=uc/v.
    need(eval_even(diff(P,0),uc)==0,'actual P_u critical control')
    need(eval_even(diff(P,1),uc)==0,'actual P_v critical control')
    # Rational symplectic chart x=N/v^3, y=1/v; not global affine coordinates.
    x=mul(N,{(0,-3):F(1)})
    y={(0,-1):F(1)}
    need(bracket(x,y)==scale(one,-1),'rational chart determinant')
    # A polynomial in original coordinates can have a pole on the added y=0 line.
    need(y!={},'nonzero punctured coordinate')
    return {'status':'PASS','mode':mode,'zero_assert':True,
            'P_minimal':wire(P),'minimal_critical_v_squared':'3/5',
            'minimal_critical_u_times_v':str(uc),'curve_J':'-5/9',
            'restriction':'v^-3','rational_chart_J':'-1'}

if __name__=='__main__':
    print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else 'normal'),sort_keys=True))
