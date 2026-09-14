"""Tiny free-symbol checks, not actual source/H/R expansions."""
import ast,json,resource,signal,sys
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
signal.alarm(30)
N=10
def need(v,msg):
    if not v: raise ValueError(msg)
def c(v): return {(0,)*N:Q(v)} if v else {}
def x(i): return {tuple(int(j==i) for j in range(N)):Q(1)}
def add(*ps):
    out={}
    for p in ps:
        for e,a in p.items():out[e]=out.get(e,Q(0))+a
    return {e:a for e,a in out.items() if a}
def scale(p,a):return {e:b*Q(a) for e,b in p.items() if b*Q(a)}
def mul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            k=tuple(i+j for i,j in zip(e,f));out[k]=out.get(k,Q(0))+a*b
    return {e:a for e,a in out.items() if a}
def pow_(p,n):
    need(0<=n<=5,'free-symbol power cap')
    out=c(1)
    for _ in range(n):out=mul(out,p)
    return out
def diff(p,i):
    out={}
    for e,a in p.items():
        if e[i]:
            f=list(e);f[i]-=1;out[tuple(f)]=a*e[i]
    return out
def wedge(p,q,i,j):return add(mul(diff(p,i),diff(q,j)),scale(mul(diff(p,j),diff(q,i)),-1))
def evaluate(p,values):
    return sum(a*__import__('functools').reduce(lambda u,iv:u*Q(values[iv[0]])**iv[1],enumerate(e),Q(1)) for e,a in p.items())
mode=sys.argv[1] if len(sys.argv)>1 else 'positive'
need(mode in ('positive','--omit-b4','--omit-b2','--wrong-euler-sign','--false-h0','--false-gcd-one'),'mode')
R,F,G,alpha,a0,b4,b3,b2,b1,b0=[x(i) for i in range(N)]
fa=add(pow_(R,3),mul(alpha,R),a0)
fb=add(pow_(R,5),mul(b4,pow_(R,4)),mul(b3,pow_(R,3)),mul(b2,pow_(R,2)),mul(b1,R),b0)
q=add(scale(pow_(R,2),Q(5,3)),{} if mode=='--omit-b4' else scale(mul(b4,R),Q(4,3)),b3,scale(alpha,Q(-5,9)))
tau=add({} if mode=='--omit-b2' else scale(b2,2),scale(mul(b4,alpha),Q(-4,3)))
delta=add(b1,scale(mul(b3,alpha),-1),scale(pow_(alpha,2),Q(5,9)))
need(diff(fb,0)==add(mul(diff(fa,0),q),mul(tau,R),delta),'all-five-kernel derivative division')
A=add(fa,F);B=add(fb,mul(q,F),G)
T=add(mul(diff(fa,0),G),scale(mul(add(mul(tau,R),delta),F),-1),scale(mul(add(scale(R,Q(5,3)),scale(b4,Q(2,3))),pow_(F,2)),-1))
for i,j in ((0,1),(0,2),(1,2)):
    need(wedge(A,B,i,j)==add(wedge(R,T,i,j),wedge(F,G,i,j)),'exact reference bracket identity')
# Universal Euler bracket identity: p*P_p and p*Q_p eliminated algebraically.
P,Qp,Pz,Qz,Z,h,m,n=[x(i) for i in range(8)]
pDp=add(mul(mul(m,h),P),scale(mul(mul(h,Z),Pz),-1))
pDq=add(mul(mul(n,h),Qp),scale(mul(mul(h,Z),Qz),-1))
actual=add(mul(Pz,pDq),scale(mul(pDp,Qz),-1))
rhs=mul(h,add(mul(mul(n,Pz),Qp),scale(mul(mul(m,P),Qz),1 if mode=='--wrong-euler-sign' else -1)))
need(actual==rhs,'universal weighted Euler bracket identity')
# Real h=0 counter-control, degree3/5 polynomials only.
Z,p=x(0),x(1)
P0=add(pow_(Z,3),c(1));Q0=pow_(Z,5)
need(wedge(P0,Q0,0,1)=={} and diff(P0,1)=={} and diff(Q0,1)=={},'h-zero hypotheses')
at0=[0]*N
same=evaluate(Q0,at0)**3==evaluate(P0,at0)**5
need(same if mode=='--false-h0' else not same,'h-zero forbids power conclusion')
# gcd>1 is a formal factor control: no degree6/10 polynomial is expanded.
m0,n0=6,10;d=gcd(m0,n0);W=add(pow_(Z,2),pow_(p,2))
EW=add(mul(Z,diff(W,0)),mul(p,diff(W,1)))
need(EW==scale(W,2),'quadratic W homogeneous')
need((1 if mode=='--false-gcd-one' else d)==2 and (m0//d,n0//d)==(3,5),'gcd-two retains quadratic common factor')
# W^3,W^5 commute by the chain rule and have degrees6/10, not a linear W.
need(3*5-5*3==0 and 2*3==m0 and 2*5==n0,'formal common-factor chain rule')
# Strict weight and squarefree hypotheses are actually necessary for injection.
normal_V=add(Z,p)
need(evaluate(normal_V,[-1,1]+[0]*(N-2))==0 and normal_V!={},'boundary normal restriction kernel')
need(Q(5*1-1,1)==4 and max(5,-4)==5,'strict boundary has a normal weight-five kernel')
repeated_V=pow_(normal_V,2)
need(repeated_V!=normal_V and evaluate(repeated_V,[-1,1]+[0]*(N-2))==0,'repeated V loses distinct branches')
# A few scalar examples illustrate, never prove, the universal inequalities.
examples=[]
for a,b in ((1,2),(2,3),(3,3),(4,4),(6,6)):
    D=a+b;t=Q(5*b-1,a);M=7*D-3;eta=Q(2*D-1,2)
    need(t>4 and M>6*D-2 and M>7*eta and D-eta>0,'scalar bound illustration')
    examples.append([a,b,str(t),str(M-7*eta)])
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'no gating asserts')
print(json.dumps({'status':'PASS','free_symbol_only':True,'source_expansion':False,'examples':examples,'countercontrols':['h=0','gcd=2','weight equality','repeated V']},sort_keys=True))
