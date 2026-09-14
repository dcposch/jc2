"""Fable arc-closure gate: exact scalar projections and toy-variety controls (stdlib only)."""
import sys
sys.dont_write_bytecode=True
import ast,json,resource
from fractions import Fraction as Q
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*2**20,512*2**20))
def need(c,s):
    if not c:raise RuntimeError('GATE FAIL: '+s)
# polynomials: dict exponent-tuple -> Fraction; variables (p,t,al,be,ga)
NV=5
def P(**kw):
    e=[0]*NV
    for k,v in kw.items():e['p t al be ga'.split().index(k)]=v
    return {tuple(e):Q(1)}
def add(a,b):
    r=dict(a)
    for k,v in b.items():
        r[k]=r.get(k,Q(0))+v
        if r[k]==0:del r[k]
    return r
def sc(c,a):return {k:Q(c)*v for k,v in a.items()} if c!=0 else {}
def mul(a,b):
    r={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            k=tuple(x+y for x,y in zip(k1,k2));r[k]=r.get(k,Q(0))+v1*v2
    return {k:v for k,v in r.items() if v!=0}
def pw(a,n):
    r={tuple([0]*NV):Q(1)}
    for _ in range(n):r=mul(r,a)
    return r
def coef_p(a,d):return {k[1:]:v for k,v in a.items() if k[0]==d}
def subst_t(a,val):
    r={}
    for k,v in a.items():
        kk=(k[0],0)+k[2:];r[kk]=r.get(kk,Q(0))+v*Q(val)**k[1]
    return {k:v for k,v in r.items() if v!=0}
def run(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one=P()
    # pure-p part of R_t (g-monomials never reach a pure-p slot): p^5 + t p^3 - (t+3) p
    Rp=add(add(P(p=5),mul(P(t=1),P(p=3))),sc(-1,mul(add(P(t=1),sc(3,one)),P(p=1))))
    if mode=='--drop-tp3':Rp=add(add(P(p=5),{}),sc(-1,mul(add(P(t=1),sc(3,one)),P(p=1))))
    R3=pw(Rp,3);R5=pw(Rp,5)
    # H = [p^13]R^3/3 + 3 == t+3 as polynomials in t (A0=R^3+al*R and deg R=5<13)
    c13=coef_p(R3,13)
    need(c13=={(1,0,0,0):Q(3)},'[p^13]R_t^3 == 3t exactly, so H=A_p13/3+3=t+3')
    need(coef_p(pw(Rp,1),13)=={},'alpha*R has no p^13 term')
    # symbolic center coefficients at general t, then t=-3
    al=P(al=1);be=P(be=1);ga=P(ga=1)
    A0=add(R3,mul(al,Rp));B0=add(add(R5,mul(be,R3)),mul(ga,Rp))
    A0m=subst_t(A0,-3);B0m=subst_t(B0,-3)
    y=coef_p(A0m,3);w=coef_p(B0m,3);v=coef_p(B0m,15)
    need(y=={(0,1,0,0):Q(-3)},'y=A_p3=-3*alpha at t=-3')
    if mode=='--gamma-sign':w={(0,0,0,1):Q(3)}
    need(w=={(0,0,0,1):Q(-3)},'w=B_p3=-3*gamma at t=-3')
    need(v=={(0,0,0,0):Q(-243),(0,0,1,0):Q(1)},'v=B_p15=-243+beta at t=-3 ([p15]R^5=-243,[p15]R^3=1,[p15]R=0)')
    need(coef_p(subst_t(R5,-3),15)=={(0,0,0,0):Q(-243)},'[p^15]R_{-3}^5 = (-3)^5 = -243 from five -3p^3 factors')
    shift=Q(0) if mode=='--omit-243' else Q(243)
    # embed y,w,v in the 5-var ring (p-exponent 0)
    emb=lambda d:{(0,)+k:c for k,c in d.items()}
    Y,W,V=emb(y),emb(w),emb(v)
    D=add(add(sc(5,mul(Y,Y)),sc(27,mul(add(V,sc(shift,one)),Y))),sc(-27,W))
    delta=add(add(ga,sc(-1,mul(be,al))),sc(Q(5,9),mul(al,al)))
    need(D==sc(81,delta),'D = 81*(gamma - beta*alpha + 5 alpha^2/9) exactly as polynomials')
    # optional B_p15=0 gauge: v=0 -> beta=243, D specializes to 5y^2+6561y-27w
    Dg=add(add(sc(5,mul(Y,Y)),sc(6561,Y)),sc(-27,W))
    Dv0=add(add(sc(5,mul(Y,Y)),sc(27,mul(add(emb({(0,0,0,0):Q(0)}),sc(243,one)),Y))),sc(-27,W))
    need(Dv0==Dg and 27*243==6561,'v=0 gauge gives 5y^2+6561y-27w')
    # toy varieties (NOT Keller points): S=Q[k,w], I=(kw-1): 1 = k*w - (kw-1) so J+(k)=S; J=I proper (point k=2,w=1/2)
    k,wv=Q(2),Q(1,2)
    need(k*wv-1==0 and k!=0,'kw=1 has a k-nonzero point')
    need(all(Q(kk)*0-1!=0 for kk in range(-5,6)),'kw=1 has empty k=0 fibre (kw-1 -> -1 at k=0)')
    # h=k toy: boundary point (0,0) exists, h in (h-k,k) but h nonzero at (2,2) on the open
    need((Q(0)-Q(0))==0 and Q(2)-Q(2)==0 and Q(2)!=0,'h=k: boundary h=0 while h=2 on the k-nonzero open')
    if mode=='--claim-global-h':need(Q(2)==0,'boundary equation h cannot be added to the k-nonzero solver input')
    return {'status':'PASS','scope':'pure-p multinomial projections (<=5 factors), exact symbolic D=81*delta, toy varieties; no actual source powers',
            'p13_R3':str(c13),'y':str(y),'w':str(w),'v':str(v),'D_minus_81delta':str(add(D,sc(-81,delta)))}
if __name__=='__main__':print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else ''),sort_keys=True))
