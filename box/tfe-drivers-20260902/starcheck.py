#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- the uniform star identities, verified EXACTLY (trace form).

For every bottom-major disc, with a_1 = eV_2, b_1 = dV_2 and
      d p_f p_g' - e p_g p_f' = kappa != 0 :
  STAR-RESIDUE  p_f(c_i) p_g'(c_i) = kappa/d, the same constant at every star point
  STAR-SUM      sum_i c_i^k / p_g'(c_i)^2 = 0   for k = 0, ..., (e-d)V_2 - 2
  STAR-EIGEN    if p_g is a pi -> zeta_A pi eigenvector then
                (a_1 = 1, b_1 = 0 mod A) or (a_1 = 0, b_1 = 1 mod A); so A | (d+e)V_2 - 1.
Symmetric sums are computed as TRACES in Q[pi]/(p_g) -- no radicals, no root isolation.
"""
import sys
import sympy as sp
pi_ = sp.Symbol('pi')

STARS = {   # exact V = 1 stars from star.py (star_run.log)
 (2,3,1): (pi_*(2*pi_**2+3)/2, pi_**2+1),
 (2,5,1): (pi_*(8*pi_**4+20*pi_**2+15)/8, pi_**2+1),
 (2,7,1): (pi_*(16*pi_**6+56*pi_**4+70*pi_**2+35)/16, pi_**2+1),
 (3,4,1): ((9*pi_**4+12*pi_**2+2)/9, pi_*(pi_**2+1)),
 (3,5,1): ((27*pi_**5+45*pi_**3-15*pi_**2+15*pi_-10)/27, (3*pi_**3+3*pi_-1)/3),
 (4,5,1): (pi_*(16*pi_**4+20*pi_**2+5)/16, (8*pi_**4+8*pi_**2+1)/8),
}
FAIL=[]; NCHK=[0]
def check(name, cond, detail=""):
    NCHK[0]+=1
    if not cond: FAIL.append((name,detail)); print("  FAIL  %-58s %s"%(name,detail))
    return cond

def trace_of(h, p):
    """Tr_{Q[pi]/(p)} h(pi) = sum over the roots of p of h(root); p squarefree, monic-ised."""
    P = sp.Poly(p, pi_).monic(); a = P.degree()
    hh = sp.rem(sp.expand(h), P.as_expr(), pi_)
    tr = 0
    for j in range(a):
        col = sp.Poly(sp.rem(sp.expand(hh*pi_**j), P.as_expr(), pi_), pi_)
        tr += col.nth(j)
    return sp.simplify(tr)

def inv_mod(h, p):
    P = sp.Poly(p, pi_).monic().as_expr()
    g, s_, t_ = sp.gcdex(sp.Poly(h, pi_), sp.Poly(P, pi_))
    # sympy gcdex(f,g) -> (s,t,h) with s f + t g = h ; adapt
    s_, t_, g_ = sp.gcdex(sp.Poly(h, pi_).as_expr(), P, pi_)
    assert sp.degree(sp.Poly(g_, pi_), pi_) == 0, "not invertible"
    return sp.expand(s_/g_)

def symmetry_order(Pol):
    P = sp.Poly(sp.expand(Pol), pi_)
    ex = [j for j in range(P.degree()+1) if sp.expand(P.nth(j)) != 0]
    if len(ex) < 2: return 0
    from math import gcd
    g = 0
    for j in ex[1:]: g = gcd(g, j-ex[0])
    return g

if __name__ == "__main__":
    print("%-10s %-4s %-4s %-8s %-16s %-6s %-24s %-24s" %
          ("(d,e,V)","a_1","b_1","kappa","kappa/d","#SUM","STAR-SUM_k values","A(p_g),A(p_f) / dichotomy"))
    for (d,e,V) in sorted(STARS):
        Pg, Pf = STARS[(d,e,V)]
        a1, b1 = e*V, d*V
        W = sp.expand(d*Pf*sp.diff(Pg,pi_) - e*Pg*sp.diff(Pf,pi_))
        check("(%d,%d,%d) BOTTOM-ODE gives a constant"%(d,e,V),
              sp.degree(sp.Poly(W,pi_),pi_)==0, str(W)); kap = sp.simplify(W)
        check("(%d,%d,%d) kappa != 0"%(d,e,V), kap != 0)
        check("(%d,%d,%d) deg p_g = a_1"%(d,e,V), sp.degree(sp.Poly(Pg,pi_),pi_)==a1)
        check("(%d,%d,%d) deg p_f = b_1"%(d,e,V), sp.degree(sp.Poly(Pf,pi_),pi_)==b1)
        check("(%d,%d,%d) p_g squarefree"%(d,e,V),
              sp.degree(sp.gcd(sp.Poly(Pg,pi_), sp.Poly(sp.diff(Pg,pi_),pi_)),pi_)==0)
        check("(%d,%d,%d) p_f squarefree"%(d,e,V),
              sp.degree(sp.gcd(sp.Poly(Pf,pi_), sp.Poly(sp.diff(Pf,pi_),pi_)),pi_)==0)
        check("(%d,%d,%d) gcd(p_f,p_g) = 1"%(d,e,V),
              sp.degree(sp.gcd(sp.Poly(Pf,pi_), sp.Poly(Pg,pi_)),pi_)==0)
        # STAR-RESIDUE, as an identity mod p_g:  p_f p_g' = kappa/d  in Q[pi]/(p_g)
        R = sp.simplify(sp.rem(sp.expand(Pf*sp.diff(Pg,pi_) - kap/d), sp.Poly(Pg,pi_).monic().as_expr(), pi_))
        check("(%d,%d,%d) STAR-RESIDUE (p_f p_g' = kappa/d mod p_g)"%(d,e,V), sp.simplify(R)==0, str(R))
        # STAR-SUM by traces
        w = inv_mod(sp.diff(Pg,pi_), Pg); w2 = sp.rem(sp.expand(w*w), sp.Poly(Pg,pi_).monic().as_expr(), pi_)
        K = (e-d)*V - 2; sums=[]
        for kk in range(0, K+1):
            S = sp.simplify(trace_of(sp.expand(pi_**kk*w2), Pg)); sums.append(S)
            check("(%d,%d,%d) STAR-SUM k=%d"%(d,e,V,kk), S==0, str(S))
        # the FIRST non-vanishing one, k = a_1-b_1-1, must be nonzero (it carries lc(p_f))
        Sfirst = sp.simplify(trace_of(sp.expand(pi_**(a1-b1-1)*w2), Pg))
        check("(%d,%d,%d) STAR-SUM at k=a_1-b_1-1 is NONzero"%(d,e,V), Sfirst != 0, str(Sfirst))
        A = symmetry_order(Pg); Af = symmetry_order(Pf)
        dich = "-"
        if A:
            c_1 = (a1 % A == 1 % A) and (b1 % A == 0)
            c_2 = (a1 % A == 0) and (b1 % A == 1 % A)
            check("(%d,%d,%d) STAR-EIGEN dichotomy at A=%d"%(d,e,V,A), c_1 or c_2, "a1=%d b1=%d"%(a1,b1))
            check("(%d,%d,%d) A | (d+e)V-1"%(d,e,V), ((d+e)*V-1) % A == 0)
            dich = "case %d" % (1 if c_1 else 2)
        print("%-10s %-4d %-4d %-8s %-16s %-6d %-24s %-24s" %
              (str((d,e,V)), a1, b1, kap, sp.nsimplify(kap/d), max(0,K+1),
               str(sums)[:24], "A=%d,%d %s (k=%d: %s)"%(A,Af,dich,a1-b1-1,sp.nsimplify(Sfirst))))
    print("\n%d checks, %d failures"%(NCHK[0], len(FAIL)))
    for nm,dt in FAIL: print("   FAILED:", nm, dt)
