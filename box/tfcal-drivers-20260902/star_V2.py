#!/usr/bin/env python3
"""(BOTTOM) at (d,e)=(2,3), V=2 and V=3: solve d Q P' - e Q' P = gamma != 0 exactly.
   Normalisation: P monic of degree 3V with no pi^{3V-1} term (translation), Q monic
   of degree 2V; the residual pi -> alpha pi scaling is fixed by an extra equation."""
import sys, time
import sympy as sp
pi = sp.symbols('pi')

def run(V, d=2, e=3, fix=None):
    dP,dQ = e*V, d*V
    a = sp.symbols('a0:%d'%(dP-1)); b = sp.symbols('b0:%d'%dQ)
    P = pi**dP + sum(a[i]*pi**i for i in range(dP-1))
    Q = pi**dQ + sum(b[i]*pi**i for i in range(dQ))
    W = sp.Poly(sp.expand(d*Q*sp.diff(P,pi)-e*sp.diff(Q,pi)*P), pi)
    eqs = [sp.expand(W.nth(j)) for j in range(1,(d+e)*V-1)]
    unk = list(a)+list(b)
    if fix is not None: eqs = eqs + [fix[0]-fix[1]]
    t0=time.time()
    G = sp.groebner(eqs, *unk, order='lex')
    print("  V=%d: %d eqs, %d unknowns; Groebner in %.1fs; is_zero_dimensional=%s"
          % (V,len(eqs),len(unk),time.time()-t0, G.is_zero_dimensional if hasattr(G,'is_zero_dimensional') else '?'))
    sols = sp.solve(eqs, unk, dict=True)
    good=[]
    for s in sols:
        Ps=sp.expand(P.subs(s)); Qs=sp.expand(Q.subs(s))
        gam=sp.simplify(sp.expand(d*Qs*sp.diff(Ps,pi)-e*sp.diff(Qs,pi)*Ps))
        free=sorted((Ps.free_symbols|Qs.free_symbols)-{pi},key=str)
        if free:
            sub={f:1 for f in free}
            Ps=sp.expand(Ps.subs(sub)); Qs=sp.expand(Qs.subs(sub)); gam=sp.simplify(gam.subs(sub))
        if gam==0: continue
        dp=sp.simplify(sp.discriminant(sp.Poly(Ps,pi),pi)); dq=sp.simplify(sp.discriminant(sp.Poly(Qs,pi),pi))
        res=sp.simplify(sp.resultant(Ps,Qs,pi))
        good.append((Ps,Qs,gam,dp!=0,dq!=0,res!=0))
    for (Ps,Qs,gam,sp1,sq,co) in good:
        print("     ADMISSIBLE gamma=%s  P=%s  Q=%s  simple(P)=%s simple(Q)=%s coprime=%s"
              % (gam, sp.factor(Ps), sp.factor(Qs), sp1, sq, co))
    print("     -> %d admissible solution branch(es)" % len(good))
    return good

if __name__=="__main__":
    for V in [2,3]:
        run(V)
