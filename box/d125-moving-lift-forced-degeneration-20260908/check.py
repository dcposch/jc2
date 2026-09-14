"""Tiny Laurent/source-scalar controls only; no actual A15/B25 expansion."""
import ast
import json
from fractions import Fraction as F
from pathlib import Path
import resource
import signal
import sys
resource.setrlimit(resource.RLIMIT_CPU, (25,25))
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,512*1024**2))
signal.alarm(30)
def need(ok, label):
    if not ok:
        raise ValueError(label)
def term(a,b,c,k=1):
    return {(a,b,c):F(k)} if k else {}
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():
            out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def scale(p,k):
    return {e:c*F(k) for e,c in p.items() if c*F(k)}
def mul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            key=tuple(a+b for a,b in zip(e,f))
            out[key]=out.get(key,F(0))+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    need(0<=n<=5,"tiny degree cap")
    out=term(0,0,0)
    for _ in range(n):
        out=mul(out,p)
    return out
def deriv(p,i):
    out={}
    for e,c in p.items():
        if e[i]:
            key=list(e); key[i]-=1
            out[tuple(key)]=c*e[i]
    return out
def bracket(p,q):
    return add(mul(deriv(p,1),deriv(q,2)),
               scale(mul(deriv(p,2),deriv(q,1)),-1))
mode=sys.argv[1] if len(sys.argv)>1 else "positive"
need(mode in ("positive","--omit-inverse-v","--wrong-ell","--wrong-k"),"mode")
# Laurent variables here are (s,u,v).
ell_power=1 if mode=="--wrong-ell" else 2
p_move=add(term(0,1,4),term(ell_power,0,1,-1),
           {} if mode=="--omit-inverse-v" else term(0,0,-1,-1))
g_move=term(0,0,-1)
p_old_scaled=add(term(-1,1,4),term(1,0,1,-1),term(-1,0,-1,-1))
g_old_scaled=term(-1,0,-1)
need(mul(term(-1,0,0),p_move)==p_old_scaled,"literal corrected lift")
fixtures=0
for i,j in ((0,1),(1,0),(2,1),(0,3),(1,2),(2,2),(0,5)):
    D=5
    lhs=mul(term(D-i-j,0,0),mul(power(g_move,i),power(p_move,j)))
    rhs=mul(term(D,0,0),mul(power(g_old_scaled,i),power(p_old_scaled,j)))
    need(lhs==rhs,"whole tiny monomial pullback")
    for t in range(j+1):
        for d in range(j-t+1):
            e=5*t+2*d-i-j
            need(D-5*t+e==D-i-j+2*d>=0,"row exponent and regularity")
    fixtures+=1
# Actual fixed-face scalar exponents, no high monomial expansion.
k_weight=10 if mode=="--wrong-k" else 12
for D,i,j,power_k in ((15,2,1,1),(25,8,5,1),(25,1,0,2)):
    need(D-i-j==power_k*k_weight,"fixed second-face transport")
need(15+25-2-2==3*k_weight==15+25-5+1,"exact target exponent")
need(k_weight-6*ell_power==0,"punctured normalized k constant")
# Same tiny algebra, variables now (s,g,p); k=2 scalar control.
A=term(12,2,1,2); B=term(24,1,0,F(20,9))
need(bracket(A,B)==term(36,2,0,F(-40,9)),"actual degree3/1 bracket sign")
# Ell=0 quintic only, never H^3 or H^5.
p0=add(term(0,1,4),term(0,0,-1,-1))
H=mul(power(p0,2),add(power(g_move,3),power(p0,3)))
w=term(0,1,5)
C=mul(term(0,1,0),mul(power(add(w,term(0,0,0,-1)),2),
                   add(power(w,2),scale(w,-3),term(0,0,0,3))))
need(H==C,"ell-zero quintic ordinary lift")
need(all(e[2]>=0 for e in H),"quintic no negative v")
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),"assert gate")
print(json.dumps({"status":"PASS","tiny_monomial_fixtures":fixtures,
                  "quintic_only":True,"full_source":False},sort_keys=True))
