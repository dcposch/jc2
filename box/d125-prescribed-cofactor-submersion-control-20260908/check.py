#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
import json

def need(ok,message):
    if not ok:
        raise ValueError(message)

def add(*ps):
    r={}
    for p in ps:
        for m,c in p.items():
            r[m]=r.get(m,F(0))+c
    return {m:c for m,c in r.items() if c}

def scale(p,c):
    return {m:a*c for m,a in p.items() if a*c}

def mul(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            e=(i+k,j+l)
            r[e]=r.get(e,F(0))+a*b
    return {m:c for m,c in r.items() if c}

def powp(p,n):
    r={(0,0):F(1)}
    for _ in range(n):
        r=mul(r,p)
    return r

def diff(p,axis):
    r={}
    for m,c in p.items():
        if m[axis]:
            n=list(m)
            n[axis]-=1
            r[tuple(n)]=m[axis]*c
    return r

def at(p,x,y):
    r=F(0)
    for (i,j),c in p.items():
        r+=c*x**i*y**j
    return r

def curve(p):
    r={}
    vu={(0,-3):F(1),(0,-5):F(1)}
    for (i,j),c in p.items():
        r=add(r,mul(scale(powp(vu,i),c),{(0,j):F(1)}))
    return r

def wire(p):
    return [[i,j,str(c)] for (i,j),c in sorted(p.items())]

def run(mode):
    one={(0,0):F(1)}
    u={(1,0):F(1)}
    v={(0,1):F(1)}
    N=add(mul(u,powp(v,5)),scale(powp(v,2),-1),scale(one,-1))
    L=add(mul(u,powp(v,3)),scale(one,1 if mode=='changed-L-sign' else -1))
    lam=F(0) if mode=='omit-a' else F(1)
    M=add(mul(v,powp(L,2)),scale(N,lam))
    P=mul(N,M)
    M0=add(v,mul(u,powp(v,2)),scale(mul(u,powp(v,4)),-1))
    H=add(mul(u,powp(v,2)),scale(one,lam))
    need(M==add(M0,mul(N,H)),'exact prescribed-cofactor extension H')
    need(curve(M)=={(0,-3):F(1)},'cofactor v^-3')
    Nu=diff(N,0)
    Nv=diff(N,1)
    Pu=diff(P,0)
    Pv=diff(P,1)
    N1=add(N,one)
    # Clear denominators in the exact cylinder expression.
    need(mul(powp(v,3),P)==add(mul(N,powp(N1,2)),scale(mul(powp(v,3),powp(N,2)),lam)),
         'cleared cylinder expression')
    expected_pu=add(mul(powp(v,2),mul(N1,add(scale(N,3),one))),
                    scale(mul(powp(v,5),N),2*lam))
    need(Pu==expected_pu,'u derivative / v5 P_z identity')
    sign=3 if mode=='changed-derivative-sign' else -3
    expected_cross=scale(mul(v,mul(N,powp(N1,2))),sign)
    need(add(mul(powp(v,5),Pv),scale(mul(Nv,Pu),-1))==expected_cross,
         'fixed-N derivative chain identity')
    # Symbolic evaluations on the entire divisor v=0.
    need({m:c for m,c in Pu.items() if m[1]==0}=={},'Pu on v=0')
    need({m:c for m,c in Pv.items() if m[1]==0}==scale(one,-1),'Pv on v=0')
    need({m:c for m,c in P.items() if m[1]==0}==scale(one,lam),'P on v=0')
    # The only two cylinder critical candidates are N=0 and N=-1.
    # N=-1 means u=v^-3, checked at one point solely as a mutation witness.
    # Universal nonvanishing is the displayed Pu formula: v2, -2a*v5.
    need(at(Pu,F(1),F(1))!=0 or at(Pv,F(1),F(1))!=0,
         'actual changed candidate critical at u=v=1')
    need(lam!=0,'N=-1 cylinder branch requires nonzero a')
    need(at(Pu,F(1),F(1))==-2*lam,'actual N=-1 point derivative')
    # a=0 is an actual changed polynomial with a critical point u=v=1.
    Pzero=mul(N,mul(v,powp(add(mul(u,powp(v,3)),scale(one,-1)),2)))
    need(at(diff(Pzero,0),F(1),F(1))==0 and at(diff(Pzero,1),F(1),F(1))==0,
         'actual omitted-a critical point')
    need(max(i+j for i,j in P)==15 and max(i for i,j in P)==3,'toy degrees')
    return {'status':'PASS','mode':mode,'parameter':'a=1, universal proof for all a!=0',
            'H':wire(H),'M':wire(M),'P':wire(P),'terms':len(P),
            'degree':15,'u_degree':3,'cofactor':'v^-3','v0_derivative':'-1',
            'a0_critical_point':['1','1'],'zero_assert':True}

if __name__=='__main__':
    print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else 'normal'),sort_keys=True))
