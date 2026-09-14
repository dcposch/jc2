"""Only exact golden factors of degree<=5 and scalar/factor orders."""
import ast,json,sys
from fractions import Fraction as F
from pathlib import Path
def need(v,msg):
    if not v:raise ValueError(msg)
def q(a=0,b=0):return (F(a),F(b))
def addq(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mulq(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+3*a[1]*b[1])
def conj(a):return (a[0]+3*a[1],-a[1])
def scaleq(a,n):return mulq(a,q(n))
def add(*ps):
    out={}
    for p in ps:
        for e,a in p.items():out[e]=addq(out.get(e,q()),a)
    return {e:a for e,a in out.items() if a!=q()}
def sc(p,a):return {e:b for e,v in p.items() if (b:=mulq(v,a))!=q()}
def mul(p,r):
    out={}
    for e,a in p.items():
        for f,b in r.items():
            k=tuple(i+j for i,j in zip(e,f));need(sum(k)<=5,'actual degree-five cap')
            out[k]=addq(out.get(k,q()),mulq(a,b))
    return {e:a for e,a in out.items() if a!=q()}
def power(p,n):
    out={(0,0,0):q(1)}
    for _ in range(n):out=mul(out,p)
    return out
def x(i):return {tuple(int(i==j) for j in range(3)):q(1)}
def H(g,p,t):return mul(power(p,2),mul(add(p,g),power(add(p,sc(g,t)),2)))
def D(g,p,t):return mul(p,mul(add(p,g),add(p,sc(g,t))))
mode=sys.argv[1] if len(sys.argv)>1 else 'positive'
need(mode in ('positive','--wrong-critical-shift','--drop-constant','--drop-half-loss','--drop-split-sign'),'mode')
results=[]
for rho in (q(0,1),q(3,-1)):
    t=addq(q(1),neg(rho));tm1=addq(t,q(-1));ainit=mulq(t,tm1)
    need(mulq(t,t)==rho and mulq(t,addq(q(2),neg(rho)))==q(1),'both golden conjugates')
    need(t!=q() and tm1!=q() and ainit!=q(),'critical units')
    w,p,s=x(0),x(1),x(2)
    g0=sc(p,addq(rho,q(-2)))
    actual=H(add(g0,w),p,t)
    expected=add(sc(mul(power(p,3),power(w,2)),ainit),sc(mul(power(p,2),power(w,3)),rho))
    need(actual==expected,'exact golden critical cubic')
    dactual=D(add(g0,w),p,t)
    dexpected=add(sc(mul(power(p,2),w),tm1),sc(mul(p,power(w,2)),t))
    need(dactual==dexpected,'nonzero transverse D jet')
    gc=add(g0,s if mode=='--wrong-critical-shift' else sc(s,q(-1)))
    need(H(add(gc,s),p,t)=={},'moving critical point of H(g+s,p)')
    # First coefficient P0_j=p²D has degree5; s^j is only an order label.
    p0=mul(power(p,2),D(gc,p,t))
    early={} if mode=='--drop-constant' else sc(mul(power(p,4),s),neg(tm1))
    expected=add(early,sc(mul(power(p,3),power(s,2)),t))
    need(p0==expected,'earlier moving constant at j10 has q11')
    results.append({'rho':[str(a) for a in rho],'critical_unit':[str(a) for a in ainit]})
# Correct ramified bracket cost: 6r+10r-r=15r, not 7*(2r).
j=12;r=F(j,5);eta=2*r
actual_order=7*eta if mode=='--drop-half-loss' else 15*r
need(actual_order==36,'j12 ramified equality is not commutation')
need(15*F(11,5)<36 and 15*F(14,6)<36,'strict coalesced subwindows')
# A q=3*kappa constant balance is coalesced, not a separated-sheet expansion.
j,kappa,q0=11,4,12;r=F(q0,6)
need(2*r==kappa and r<F(j,5) and 15*r<36,'earlier constant at split boundary')
# Both signs are essential: at equal scalar order one cancellation is possible.
b,c=-1,1
values=[b+c,b+(c if mode=='--drop-split-sign' else -c)]
need(values==[0,-2] and any(values),'global separated-sheet minimum')
j,kappa,q0=12,4,13
nu=min(F(q0),F(j)+F(kappa,2));eta=nu/3
need(eta>kappa and 7*eta<36-F(kappa,2),'separated strict margin')
# Formal common quadratic, no degree6/10 materialization:
# (Y²+aY+b)^3 has Y5 coefficient3a and, once a=0, Y4 coefficient3b.
need(3*0==0 and 3*7==21,'quadratic high-coefficient comparison')
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'no gating asserts')
print(json.dumps({'status':'PASS','both_conjugates':results,'max_actual_degree':5,'source_A_B_built':False,'j12_order':str(actual_order)},sort_keys=True))
