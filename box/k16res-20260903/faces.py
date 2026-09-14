#!/usr/bin/env python3
"""Facial structure of the weighted resultant system R_r=Res_b3(Q_0,Q_r), r=1..t-1, in P(1,2,...,t-1).
For a coordinate face L_J (only variables q_j, j in J, nonzero) the restriction of Q_r = a_r b3^2 + b_r b3 + c_r
keeps a_r iff wt(a_r)=r lies in Sem(w_J), b_r iff t+1+r in Sem(w_J), c_r iff 2t+2+r in Sem(w_J) (weight support;
exact for |J|=1 up to accidental cancellation, a proxy for |J|>=2).  R_r|_{L_J} is the formal 2x2 resultant of the
restricted quadratics; it is identically zero iff that formal expression in generic surviving coefficients is zero.
c_J := #{r : R_r|_{L_J} not identically zero}.  c_J < |J| => rho_t identically zero (structural obstruction);
c_J = |J| => an extraneous (facial) factor of the pullback Macaulay resultant."""
import sys, itertools
import sympy as sp
def sem(ws, N):
    S={0}
    for n in range(1,N+1):
        if any((n-w) in S for w in ws if n-w>=0): S.add(n)
    return S
def restricted(t, J, r, S):
    a=sp.Symbol(f"a{r}") if r in S else 0
    b=sp.Symbol(f"b{r}") if (t+1+r) in S else 0
    c=sp.Symbol(f"c{r}") if (2*t+2+r) in S else 0
    return a,b,c
def analyse(t, maxJ=3, verbose=True):
    n=t-1; ws=list(range(1,n+1)); out=[]
    for size in range(1, min(maxJ,n)+1):
        for J in itertools.combinations(range(1,n+1), size):
            if 1 in J: continue  # b4 in J: all weights present, no restriction beyond generic
            S=sem([w for w in J], 8*t)
            a0,b0,c0=restricted(t,J,0,S)
            live=[]
            for r in range(1,n+1):
                ar,br,cr=restricted(t,J,r,S)
                R=sp.expand((a0*cr-ar*c0)**2-(a0*br-ar*b0)*(b0*cr-br*c0))
                if R!=0: live.append(r)
            cJ=len(live)
            if cJ<=size:
                out.append((J,cJ,live))
    return out
if __name__=="__main__":
    T=int(sys.argv[1]) if len(sys.argv)>1 else 20
    for t in range(3,T+1):
        res=analyse(t)
        s=[]
        for J,cJ,live in res:
            tag="ZERO!" if cJ<len(J) else "facial"
            s.append(f"J={J} c={cJ} live_r={live} {tag}")
        print(f"t={t}: "+("; ".join(s) if s else "no facial factors, no obstruction (|J|<=3)"))
