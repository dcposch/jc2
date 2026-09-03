#!/usr/bin/env python3
"""EXISTENCE of a bottom star of type (d,e,V): is the saturated ideal proper?

  I = ( coeffs pi^1..pi^{a+b-1} of  d p_f p_g' - e p_g p_f' ,  z*kappa - 1 )
  a star with kappa != 0 exists  <=>  GB(I) != {1}.
This settles the row that sympy.solve got WRONG in starres.py (which reported no
(2,3,2) star; one exists).  Controls: an inconsistent and a consistent toy ideal.
"""
import sys, time
import sympy as sp
pi_ = sp.Symbol('pi'); z = sp.Symbol('z')
FAIL = []; N = [0]
def check(n_, c_, d_=""):
    N[0] += 1
    if not c_: FAIL.append((n_, d_)); print("    FAIL %-50s %s" % (n_, d_))
def exists(d, e, V):
    a, b = e*V, d*V
    ps = sp.symbols('p0:%d' % a); qs = sp.symbols('q0:%d' % (b+1))
    pg = pi_**a + sum(ps[i]*pi_**i for i in range(a-1))
    pf = sum(qs[i]*pi_**i for i in range(b+1))
    B = sp.Poly(sp.expand(d*pf*sp.diff(pg, pi_) - e*pg*sp.diff(pf, pi_)), pi_)
    eqs = [sp.expand(B.nth(j)) for j in range(1, a+b)]; kap = sp.expand(B.nth(0))
    unk = list(ps[:a-1]) + list(qs); t0 = time.time()
    G = sp.groebner(eqs + [sp.expand(z*kap - 1)], *(unk + [z]), order='grevlex')
    triv = (list(G.exprs) == [sp.Integer(1)])
    print("  (d,e,V)=(%d,%d,%d)  a_1=%-2d b_1=%-2d  gamma=%-2d  GB size %-3d  star EXISTS: %-5s [%.2fs]"
          % (d, e, V, a, b, V*(d*e-d-e)+1, len(G.exprs), not triv, time.time()-t0))
    return not triv
if __name__ == "__main__":
    print("existence.py -- BOTTOM-ODE star existence by saturated Groebner.  sympy", sp.__version__)
    u_, w_ = sp.symbols('u w')
    check("control: inconsistent saturation reported as NO",
          list(sp.groebner([u_**2-1, w_*(u_**2-1)-1], u_, w_, order='grevlex').exprs) == [sp.Integer(1)])
    check("control: consistent saturation reported as YES",
          list(sp.groebner([u_**2-1, w_*u_-1], u_, w_, order='grevlex').exprs) != [sp.Integer(1)])
    for t in [(1,2,1),(1,3,1),(1,4,1),(1,6,1),(2,3,1),(2,3,2),(2,3,3),
              (2,5,1),(3,5,1),(4,5,1),(2,5,2),(3,4,1)]:
        try: check("star %s existence decided" % (t,), exists(*t) is not None)
        except Exception as ex: print("  ERROR on %s: %s" % (t, ex))
    print("\n%d checks, %d failures" % (N[0], len(FAIL)))
