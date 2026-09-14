#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
import json

def need(ok,msg):
    if not ok: raise ValueError(msg)
# Exact Q[rho]/(rho^2-3rho+1), rational-string output only.
O=(Q(0),Q(0)); I=(Q(1),Q(0)); R=(Q(0),Q(1))
def fa(x,y): return (x[0]+y[0],x[1]+y[1])
def fs(x,c): return (x[0]*c,x[1]*c)
def fm(x,y):
    a,b=x; c,d=y
    return (a*c-b*d,a*d+b*c+3*b*d)
def fi(x):
    a,b=x; norm=a*a+3*a*b+b*b
    need(norm!=0,'field denominator')
    return ((a+3*b)/norm,-b/norm)
def fp(x,n):
    v=I
    for _ in range(n): v=fm(v,x)
    return v
def add(*ps):
    r={}
    for p in ps:
        for e,c in p.items(): r[e]=fa(r.get(e,O),c)
    return {e:c for e,c in r.items() if c!=O}
def sc(p,c): return {e:fm(a,c) for e,a in p.items() if fm(a,c)!=O}
def mul(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            e=(i+k,j+l); r[e]=fa(r.get(e,O),fm(a,b))
    return {e:c for e,c in r.items() if c!=O}
def powp(p,n):
    r={(0,0):I}
    for _ in range(n): r=mul(r,p)
    return r
def dg(p): return {(i-1,j):fs(c,i) for (i,j),c in p.items() if i}
def line(poly,z):
    # g=z*p, represented by Laurent p monomials with first exponent zero.
    out={}
    for (i,j),c in poly.items(): out=add(out,{(0,i+j):fm(c,fp(z,i))})
    return out
def wire(p): return [[i,j,str(c[0]),str(c[1])] for (i,j),c in sorted(p.items())]

def run(mode):
    one={(0,0):I}; g={(1,0):I}; p={(0,1):I}
    rows=[]
    for rho in (R,fa(fs(I,3),fs(R,-1))):
        need(fa(fa(fp(rho,2),fs(rho,-3)),I)==O,'both exact golden roots')
        t=fa(I,fs(rho,-1))
        need(fp(t,2)==rho and fm(t,fa(fs(I,2),fs(rho,-1)))==I,'golden factor units')
        L=add(p,g); M=add(p,sc(g,t))
        H=mul(powp(p,2),mul(L,powp(M,2)))
        radical=mul(p,mul(L,M))
        lam=fi(t) # a=1; arbitrary a is scalar multiplication in the proof.
        used_rho=R if mode=='freeze-conjugate' else rho
        mid=fa(fs(I,2 if mode=='wrong-middle' else 3),fs(used_rho,-1))
        F=add(mul(powp(g,2),p),sc(mul(g,powp(p,2)),mid),
              sc(powp(p,3),fa(fs(I,2),fs(used_rho,-1))))
        need(F==sc(radical,lam),'normalized degree3 factor identity')
        need(max(i+j for i,j in F)==3 and max(5*i-7*j for i,j in F)==3,'actual degree and weight')
        need(all(i<3 or j<2 for i,j in F),'lex normal remainder')
        need(F[(2,1)]==I,'prescribed unequal low-face coefficient a=1')
        need(all(i<=2*j and 5*i-7*j<=3 and i+j<=15 for i,j in F),'actual unequal support')
        need(max(i+j for i,j in H)==5,'H degree, no H^2 expansion')
        # The quotient certificate uses FACTOR EXPONENTS only, not expansion of F^2.
        h_exp=(2,1,2); f_exp=(1,1,1)
        need(tuple(2*x-y for x,y in zip(f_exp,h_exp))==(0,1,0),'F^2/H factor exponents')
        need(any(x<y for x,y in zip(f_exp,h_exp)),'H does not divide F')
        simple=fs(I,-1); repeated=fs(fi(t),-1)
        need(simple!=repeated,'distinct reduced branches')
        need(not line(F,simple) and not line(F,repeated),'normal residue vanishes on BOTH reduced branches')
        Hg=dg(H)
        need(line(Hg,simple)=={(0,4):fp(rho,2)},'simple-branch derivative')
        need(not line(Hg,repeated),'repeated-branch derivative zero')
        # H+s*p=0: first simple-branch motion and resulting F pole.
        g1={(0,-3):fs(fi(fp(rho,2)),1 if mode=='wrong-motion-sign' else -1)}
        need(not add(mul(line(Hg,simple),g1),p),'actual first moving-curve equation')
        f1=mul(line(dg(F),simple),g1)
        need(f1=={(0,-1):fs(fm(lam,fi(rho)),-1)},'actual normal-remainder pole')
        need(not line(Hg,repeated) and bool(p),'no unramified repeated-line first-order solution')
        # Whole unequal inner-face SCALAR relations only, no receiver pair.
        a=I; b=fp(rho,3); f=fp(rho,5)
        e=fs(fp(rho,2),Q(5,3)); d=fs(fi(rho),Q(5,9))
        c=I if mode=='wrong-c-normalization' else fs(fi(rho),Q(-5,9))
        need(fs(fm(a,d),-1)==c,'actual c=-5/(9rho), not independent c=1')
        need(fa(fs(fm(a,e),2),fs(fm(b,d),-6))==O,'first inner compatibility')
        need(fa(fs(fm(a,f),5),fs(fm(b,e),-3))==O,'second inner compatibility')
        rows.append({'rho':[str(x) for x in rho],'t':[str(x) for x in t],
                     'H':wire(H),'F_a1':wire(F),'F_square_over_H_factor':'lambda^2*(p+g)',
                     'simple_first_F_residue':wire(f1),'c':[str(x) for x in c]})
    return {'status':'PASS','mode':mode,'roots':rows,'zero_assert':True,
            'full_source_point_claimed':False,'actual_H_squared_expanded':False}

if __name__=='__main__':
    print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else 'normal'),sort_keys=True))
