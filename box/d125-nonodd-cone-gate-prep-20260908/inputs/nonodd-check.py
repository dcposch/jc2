"""Free-symbol degree3/5 controls; no actual source or H powers."""
import ast,json,resource,signal,sys
from fractions import Fraction as F
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
signal.alarm(30)
N=10
def need(ok,msg):
    if not ok: raise ValueError(msg)
def c(x): return {(0,)*N:F(x)} if x else {}
def v(i): return {tuple(int(i==j) for j in range(N)):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for e,a in p.items(): out[e]=out.get(e,F(0))+a
    return {e:a for e,a in out.items() if a}
def sc(p,a): return {e:q*F(a) for e,q in p.items() if q*F(a)}
def mul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            k=tuple(x+y for x,y in zip(e,f));out[k]=out.get(k,F(0))+a*b
    return {e:a for e,a in out.items() if a}
def pw(p,n):
    need(0<=n<=5,"tiny power cap")
    out=c(1)
    for _ in range(n): out=mul(out,p)
    return out
def der(p,i):
    out={}
    for e,a in p.items():
        if e[i]:
            k=list(e);k[i]-=1;out[tuple(k)]=a*e[i]
    return out
def wedge(p,q,i,j):
    return add(mul(der(p,i),der(q,j)),sc(mul(der(p,j),der(q,i)),-1))
mode=sys.argv[1] if len(sys.argv)>1 else "positive"
need(mode in ("positive","--omit-b4","--omit-b2","--partial-constant-shear","--wrong-f"),"mode")
r,f,z,a,a0,b4,b3,b2,b1,b0=[v(i) for i in range(N)]
fa=add(pw(r,3),mul(a,r),a0)
fb=add(pw(r,5),mul(b4,pw(r,4)),mul(b3,pw(r,3)),mul(b2,pw(r,2)),mul(b1,r),b0)
q=add(sc(pw(r,2),F(5,3)),{} if mode=="--omit-b4" else sc(mul(b4,r),F(4,3)),b3,sc(a,F(-5,9)))
tau=add({} if mode=="--omit-b2" else sc(b2,2),sc(mul(b4,a),F(-4,3)))
delta=add(b1,sc(mul(b3,a),-1),sc(pw(a,2),F(5,9)))
need(der(fb,0)==add(mul(der(fa,0),q),mul(tau,r),delta),"full polynomial derivative division")
A=add(fa,f);B=add(fb,mul(q,f),z)
T=add(mul(der(fa,0),z),sc(mul(add(mul(tau,r),delta),f),-1),
      sc(mul(add(sc(r,F(5,3)),sc(b4,F(2,3))),pw(f,2)),-1))
for i,j in ((0,1),(0,2),(1,2)):
    need(wedge(A,B,i,j)==add(wedge(r,T,i,j),wedge(f,z,i,j)),"nonodd bracket identity")
actual=add(B,sc(mul(b3,add(A,sc(a0,-1)) if mode=="--partial-constant-shear" else A),-1))
expected=add(pw(r,5),mul(b4,pw(r,4)),mul(b2,pw(r,2)),mul(add(b1,sc(mul(b3,a),-1)),r),
             b0,sc(mul(b3,a0),-1),mul(add(q,sc(b3,-1)),f),z)
need(actual==expected,"full constant-sensitive beta3 shear")
kernels=[ell for ell in range(1,29) if 25-ell>=0 and (25-ell)%5==0]
need(kernels==[5,10,15,20,25],"all nonodd polynomial kernels")
need([j for j in range(1,15) if (35-2*j)%5==0]==[5,10],"second-order scalar exceptions")
need(all(2*j<36 and 15+j>2*j for j in range(1,15)),"all tentative contact orders")
need(7*F(9,2)<36 and 5-F(9,2)>0,"uniform strict weight margin")
# Independent formal degree3/5 commutation residual after positive homogeneity kills constants.
Z,u,vv,up,vp,h=[v(i) for i in range(6)]
P=add(pw(Z,3),mul(u,Z),vv)
Q=add(pw(Z,5),sc(mul(u,pw(Z,3)),F(5,3)),sc(mul(vv,pw(Z,2)),F(5,3)),
      sc(mul(pw(u,2),Z),F(5,9)),sc(mul(u,vv),F(8,9) if mode=="--wrong-f" else F(10,9)))
def D(poly):
    return add(mul(der(poly,1),up),mul(der(poly,2),vp))
br=add(mul(der(P,0),D(Q)),sc(mul(D(P),der(Q,0)),-1))
left=add(mul(pw(u,2),up),sc(mul(vv,vp),-6))
right=add(sc(mul(mul(u,vv),up),2),mul(pw(u,2),vp))
need(br==sc(add(mul(left,Z),right),F(5,9)),"formal cubic quintic final rows")
euler_left=add(mul(pw(u,2),sc(mul(h,u),2)),sc(mul(vv,sc(mul(h,vv),3)),-6))
euler_right=add(sc(mul(mul(u,vv),sc(mul(h,u),2)),2),mul(pw(u,2),sc(mul(h,vv),3)))
need(euler_left==sc(mul(h,add(pw(u,3),sc(pw(vv,2),-9))),2),"Euler first equation")
need(euler_right==sc(mul(h,mul(pw(u,2),vv)),7),"Euler second equation")
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),"assert gate")
print(json.dumps({"status":"PASS","kernels":kernels,"formal_quintic_only":True,"full_source":False},sort_keys=True))
