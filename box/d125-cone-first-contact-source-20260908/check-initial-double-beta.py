"""Only free-symbol degree<=5 identities and tiny scalar/factor controls."""
import ast
import json
from fractions import Fraction as Q
from pathlib import Path
import resource
import signal
import sys
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
signal.alarm(30)
N=6
def need(ok,label):
    if not ok:
        raise ValueError(label)
def const(c):
    return {(0,)*N:Q(c)} if c else {}
def var(i):
    return {tuple(int(i==j) for j in range(N)):Q(1)}
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():
            out[e]=out.get(e,Q(0))+c
    return {e:c for e,c in out.items() if c}
def sc(p,c):
    return {e:q*Q(c) for e,q in p.items() if q*Q(c)}
def mul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            key=tuple(a+b for a,b in zip(e,f))
            out[key]=out.get(key,Q(0))+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    need(0<=n<=5,"tiny power cap")
    out=const(1)
    for _ in range(n):
        out=mul(out,p)
    return out
def diff(p,i):
    out={}
    for e,c in p.items():
        if e[i]:
            key=list(e); key[i]-=1
            out[tuple(key)]=c*e[i]
    return out
def wedge(p,q,i,j):
    return add(mul(diff(p,i),diff(q,j)),sc(mul(diff(p,j),diff(q,i)),-1))
r,f,z,a,b,c=[var(i) for i in range(N)]
mode=sys.argv[1] if len(sys.argv)>1 else "positive"
need(mode in ("positive","--omit-alpha-cross","--omit-gamma","--partial-shear"),"mode")
A=add(power(r,3),mul(a,r),f)
q=add(sc(power(r,2),Q(5,3)),b,
      {} if mode=="--omit-alpha-cross" else sc(a,Q(-5,9)))
B=add(power(r,5),mul(b,power(r,3)),mul(c,r),mul(q,f),z)
delta=add({} if mode=="--omit-gamma" else c,sc(mul(b,a),-1),sc(power(a,2),Q(5,9)))
T=add(mul(add(sc(power(r,2),3),a),z),sc(mul(delta,f),-1),
      sc(mul(r,power(f,2)),Q(-5,3)))
for i,j in ((0,1),(0,2),(1,2)):
    rhs=add(wedge(r,T,i,j),wedge(f,z,i,j))
    need(wedge(A,B,i,j)==rhs,"exact moving-reference bracket identity")
actual_shear=add(B,sc(mul(b,add(power(r,3),mul(a,r)) if mode=="--partial-shear" else mul(b,A)),-1))
expected_shear=add(power(r,5),mul(add(delta,sc(power(a,2),Q(-5,9))),r),
                   mul(add(sc(power(r,2),Q(5,3)),sc(a,Q(-5,9))),f),z)
need(actual_shear==expected_shear,"whole beta A shear")
# Fixed degree15/25 scalar bookkeeping, not polynomial source construction.
kernels=[ell for ell in range(2,29,2) if 25-ell>=0 and (25-ell)%5==0]
need(kernels==[10,20],"all polynomial G kernels")
for j in range(2,15,2):
    need(2*j<36 and 20+j>2*j,"target/delta order separation")
    degree=35-2*j
    need(degree%5!=0 or (j==10 and degree==15),"second-order centralizer")
# Genuine omitted-weight and selected-component controls; only degree<=5 factors.
P={(4,1):Q(1),(1,4):Q(1)}       # g*p*(g^3+p^3)
H={(3,2):Q(1),(0,5):Q(1)}
need(max(5*i-7*j for i,j in P)==13,"dropped-weight control")
need(min(j for i,j in P)==1 and min(j for i,j in H)==2,"H does not divide P")
C={(1,1):Q(1),(0,2):Q(1)}
need(max(5*i-7*j for i,j in C)<=2 and max(i for i,j in C)<3,"normal first-contact C")
need(sum(c*((-1)**i) for (i,j),c in C.items())==0,"C may vanish on g=-p component")
need(not any(isinstance(t,ast.Assert) for t in ast.walk(ast.parse(Path(__file__).read_text()))),"assert gate")
print(json.dumps({"status":"PASS","formal_wedge_rows":3,"kernels":kernels,
                  "actual_source_expanded":False,"component_nonvanishing_not_assumed":True},sort_keys=True))
