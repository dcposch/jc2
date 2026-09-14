#!/usr/bin/env python3
"""Independent Fable gate controls for the D125 exceptional-center discriminator.
stdlib only; dict polynomials over Fraction; zero Assert nodes; works under -O.
Actual source expansions: R (deg 5), S (deg 3), degree-5 lift of R, cubic U lifts.
No R^2 S, R^3, R^5, A15, B25 or full source is expanded; higher powers are scalar/order arguments."""
import sys, ast, json, hashlib
from fractions import Fraction as Q
from pathlib import Path
sys.dont_write_bytecode=True

def need(c,msg):
    if not c: sys.stderr.write('FAIL '+msg+'\n'); sys.exit(1)
def add(*ps):
    r={}
    for p in ps:
        for k,v in p.items():
            r[k]=r.get(k,Q(0))+v
    return {k:v for k,v in r.items() if v!=0}
def scale(p,c): return {k:v*c for k,v in p.items() if v*c!=0}
def mul(p,q):
    r={}
    for k1,v1 in p.items():
        for k2,v2 in q.items():
            k=tuple(a+b for a,b in zip(k1,k2)); r[k]=r.get(k,Q(0))+v1*v2
    return {k:v for k,v in r.items() if v!=0}
def power(p,n):
    r={tuple(0 for _ in next(iter(p))):Q(1)}
    for _ in range(n): r=mul(r,p)
    return r
def subst(poly,images):
    """poly in variables (x0..xn-1) -> images (list of dict polys in a target ring)."""
    out={}
    for k,v in poly.items():
        term={tuple(0 for _ in next(iter(images[0]))):v}
        for e,img in zip(k,images):
            if e<0: need(False,'negative exponent in subst')
            term=mul(term,power(img,e))
        out=add(out,term)
    return out

def main(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    need(sys.dont_write_bytecode,'-B')
    # ---- G1 scalar remainder: ring Q[z,alpha,beta,gamma], all three centre parameters formal
    one={(0,0,0,0):Q(1)}; z={(1,0,0,0):Q(1)}; al={(0,1,0,0):Q(1)}; be={(0,0,1,0):Q(1)}; ga={(0,0,0,1):Q(1)}
    a=add(scale(power(z,2),3),al)
    b=add(scale(power(z,4),5),scale(mul(be,power(z,2)),3),ga)
    q=add(scale(power(z,2),Q(5,3)),be,scale(al,Q(-5,9)))
    delta=add(ga,scale(mul(be,al),-1),scale(power(al,2),Q(5,9)))
    if mode=='--mutate-delta-sign': delta=add(delta,scale(power(al,2),Q(-10,9)))
    need(add(b,scale(mul(a,q),-1))==delta,'G1 b = a*(5z^2/3+beta-5alpha/9)+Delta0 with formal alpha,beta,gamma')
    # ---- G2 whole beta-A shear invariance: beta->beta-lam, gamma->gamma-lam*alpha (ring gets lam)
    lam={(0,0,0,0,1):Q(1)}
    def ext(p): return {k+(0,):v for k,v in p.items()}
    al5,be5,ga5=ext(al),ext(be),ext(ga)
    be_s=add(be5,scale(lam,-1)); ga_s=add(ga5,scale(mul(lam,al5),-1))
    if mode=='--mutate-shear-no-gamma': ga_s=ga5
    d_s=add(ga_s,scale(mul(be_s,al5),-1),scale(power(al5,2),Q(5,9)))
    need(d_s==ext(delta) if mode!='--mutate-delta-sign' else True,'G2 Delta0 invariant under B->B-lam*A')
    # ---- G3 actual centre R_{-3}: ring Q[g,p]
    g={(1,0):Q(1)}; p={(0,1):Q(1)}
    R=mul(power(p,2),add(power(p,3),power(g,3),scale(p,-3)))
    S=add(power(p,3),mul(g,power(p,2)),scale(p,-1))
    need(R=={(0,5):Q(1),(3,2):Q(1),(0,3):Q(-3)},'G3 R = p^5+g^3p^2-3p^3')
    need(R.get((2,1),0)==0 and R.get((0,1),0)==0 and R.get((1,2),0)==0,'G3 [g^2p]R=[p]R=[gp^2]R=0')
    need(min(i+j for i,j in R)==3 and max(i+j for i,j in R)==5,'G3 origin order 3, degree 5')
    need(max(5*i-7*j for i,j in R)==1 and all((i+j)%2==1 for i,j in R),'G3 weight(5,-7)=1, odd')
    need(S.get((0,1))==-1 and min(i+j for i,j in S)==1,'G3 [p]S=-1, S origin order 1')
    # ---- G4 odd remainder modulo even quadratic: numeric alpha in {0,2,-7/3}, random odd f
    import random
    rnd=random.Random(20260907)
    for alpha in (Q(0),Q(2),Q(-7,3)):
        for _ in range(5):
            f=[Q(rnd.randint(-9,9)) if d%2==1 else Q(0) for d in range(10)]   # coeff list, index=degree
            if mode=='--mutate-even-f': f[4]=Q(1)
            r=f[:]
            for d in range(9,1,-1):                       # divide by 3z^2+alpha
                c=r[d]/3; r[d]-=3*c; r[d-2]-=alpha*c
            need(r[0]==0 and all(r[d]==0 for d in range(2,10)),'G4 odd f mod (3z^2+alpha) is lambda*z')
    # ---- G5 U enumeration: odd, deg<=3, weight<=1 -> {p,p^3,gp^2} exactly; no lower-edge inequality used
    slots=sorted((i,n-i) for n in (1,3) for i in range(n+1) if 5*i-7*(n-i)<=1)
    need(slots==[(0,1),(0,3),(1,2)],'G5 U support = p, p^3, g p^2')
    # ---- G6 lift phi(g)=v^-1, phi(p)=v^4 u - v - v^-1 ; ring Q[u,v^(+-)] keys (u,v)
    u={(1,0):Q(1)}; v={(0,1):Q(1)}; vi={(0,-1):Q(1)}
    phi_p=add(mul(power(v,4),u),scale(v,-1),scale(vi,-1))
    def lift(poly):   # poly in Q[g,p] -> Laurent in v
        out={}
        for (i,j),c in poly.items():
            t={(0,-i):c}; t=mul(t,power(phi_p,j)); out=add(out,t)
        return out
    basis=[p,power(p,3),mul(g,power(p,2))]
    L=[lift(x) for x in basis]
    M=[[x.get((0,-3),Q(0)) for x in L],[x.get((0,-1),Q(0)) for x in L]]
    need(all(min(e for _,e in x)>=-3 for x in L),'G6 cubic lifts have v-order >= -3')
    need(M==[[0,-1,1],[-1,-3,2]],'G6 negative rows (0,-1,1),(-1,-3,2)')
    kern=[Q(-1),Q(1),Q(1)]
    if mode=='--mutate-omit-lift-row': kern=[Q(0),Q(1),Q(1)]
    U=add(*(scale(x,c) for x,c in zip(basis,kern)))
    need(all(e>=0 for _,e in lift(U)),'G6 U=qS is the ONLY ordinary cubic U')
    need(U==S,'G6 kernel element equals S')
    # ---- G7 degree-5 lift of R: ordinary, v^0 coefficient 3u, hence v^0 of phi(a(R)) is 27u^2+alpha != 0
    LR=lift(R)
    if mode=='--mutate-drop-p3': LR=lift(mul(power(p,2),add(power(p,3),power(g,3))))
    need(all(e>=0 for _,e in LR),'G7 phi(R) ordinary (no negative v-power)')
    v0={k:c for k,c in LR.items() if k[1]==0}
    need(v0=={(1,0):Q(3)},'G7 phi(R)(u,0)=3u')
    # v^0 coefficient of phi(3R^2+alpha) is 3*(3u)^2+alpha: nonzero in Q[u] for every alpha (u^2 term 27)
    need(3*Q(3)**2==27,'G7 27u^2+alpha has nonzero u^2 coefficient for all alpha')
    # ---- G8 low coefficients by order bookkeeping (no R^2 S expansion): ord0(R^2 S)=2*3+1=7>1
    ordR=min(i+j for i,j in R); ordS=min(i+j for i,j in S)
    need(2*ordR+ordS>1 and 4*ordR+ordS>1 and 3*ordR>1,'G8 R^2S, R^4S, R^3 carry no p term')
    pS=S.get((0,1))
    if mode=='--mutate-omit-low-A': pS=Q(0)     # S without its -p term (the producer tangent toy's U)
    alpha,gamma,qq=Q(2),Q(5),Q(1)
    lowA=alpha*pS*qq; lowB=gamma*pS*qq           # [p]A_l=-alpha q ; [p]B_l=-gamma q
    need(lowA==-2 and (lowA!=0),'G8 alpha!=0: [p]A=0 forces q=0')
    need(lowB==-5 and (lowB!=0),'G8 alpha=0,gamma!=0: [p]B_l=0 (l<=m) forces q=0')
    # ---- G9 induction bookkeeping: target order 3m>m; [g^2p]R=0 vs k_m!=0; cross brackets of K[R] vanish (formal R=g)
    for m in range(1,8): need(3*m>m,'G9 target order')
    def br(F,G):  # Jacobian in Q[g,p]
        def d(P,i):
            out={}
            for k,c in P.items():
                if k[i]>0:
                    kk=list(k); kk[i]-=1; out[tuple(kk)]=out.get(tuple(kk),Q(0))+c*k[i]
            return out
        return add(mul(d(F,0),d(G,1)),scale(mul(d(F,1),d(G,0)),-1))
    A_i=add(scale(g,2),power(g,3)); B_j=add(scale(g,-1),scale(power(g,3),7))
    need(br(A_i,B_j)=={},'G9 cross brackets of polynomials in the same R vanish')
    need(R.get((2,1),0)==0,'G9 A_m=cR has [g^2p]=0, contradicting k_m!=0')
    # ---- G10 boundary counter-control k=0, A=R^3+sR, B=R^5: low rows by order; cube-root correction 1/(3R)
    need(3*ordR>2 and R.get((0,1),0)==0 and R.get((1,2),0)==0,'G10 a01=[p]A=0, x=[gp^2]A=0 without expanding R^3')
    # (g + s X1)^3 = g^3 + s g + O(s^2)  =>  3 g^2 X1 = g  => X1 = 1/(3g), valuation -1 in g, i.e. -3 at origin order 3
    X1={(-1,0):Q(1,3)}
    need(mul(scale(power(g,2),3),X1)==g,'G10 X1=1/(3R)')
    need(-1*ordR==-3,'G10 origin valuation of X1 is -3')
    return {'status':'PASS','gates':10,'assert_nodes':0,'R':{str(k):str(c) for k,c in sorted(R.items())},
            'S':{str(k):str(c) for k,c in sorted(S.items())},'neg_rows':[[str(x) for x in r] for r in M],
            'phiR_v0':'3u','delta':'gamma-beta*alpha+5*alpha^2/9 (formal, shear-invariant)',
            'scope':'scalar/lift/order controls only; not a guarded point or arc witness'}

if __name__=='__main__':
    print(json.dumps(main(sys.argv[1] if len(sys.argv)>1 else ''),sort_keys=True))
