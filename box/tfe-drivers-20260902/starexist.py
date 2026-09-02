#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- DECISION PROCEDURE for the bottom star.

For fixed (d,e,V) put b = dV, a = eV.  A bottom star exists <=> there is a monic
Q of degree b (translation-normalised, q_{b-1} = 0) with

    the coefficients of pi^{-1},...,pi^{-(b-2)} in Q^{e/d} all zero,     (TRUNC)
    kappa := d Q P' - e P Q' (a constant, given TRUNC) nonzero,          (NONDEG)
    P := [Q^{e/d}]_{>=0}.

Decide by the Nullstellensatz: build the ideal I = (TRUNC) + (w*kappa - 1) over QQ and
compute a Groebner basis.  1 in I  <=>  the variety is EMPTY over C  <=>  the star
does NOT exist and every skeleton with that (d,e,V_2) DIES.
"""
import sys, time
import sympy as sp
sys.path.insert(0,'/Users/dc/code/math/jc2/box/tfe-drivers-20260902')
from star import star_system, pi_

def decide(d, e, V, timeout_note=""):
    Q, Pg, eqs, unk, a, b = star_system(d, e, V)
    eqs = [sp.expand(q) for q in eqs if sp.expand(q) != 0]
    W = sp.expand(d*Q*sp.diff(Pg,pi_) - e*Pg*sp.diff(Q,pi_))
    kap = sp.expand(sp.Poly(W, pi_).nth(0))
    w = sp.Symbol('w')
    gens = list(unk) + [w]
    G = sp.groebner(eqs + [sp.expand(w*kap - 1)], *gens, order='grevlex')
    empty = (list(G.exprs) == [sp.Integer(1)]) or (G.exprs and all(g == 1 for g in G.exprs))
    return (not empty), a, b, len(eqs), len(G.exprs)

if __name__ == "__main__":
    TRIP = []
    for (d,e) in [(2,3),(2,5),(2,7),(3,4),(3,5),(3,7),(4,5),(4,7),(5,6),(5,7),(6,7)]:
        for V in range(1, 6): TRIP.append((d,e,V))
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    print("STAR EXISTENCE by Nullstellensatz (Groebner over QQ, saturated at kappa != 0)")
    print("%-11s %-5s %-5s %-7s %-9s %-12s %-8s" % ("(d,e,V)","a_1","b_1","#TRUNC","#GB","verdict","secs"))
    for (d,e,V) in sorted(TRIP, key=lambda z:(z[0]*z[2], z)):
        if d*V > lim: continue
        t0=time.time()
        try:
            ok, a, b, ne, ng = decide(d,e,V)
            print("%-11s %-5d %-5d %-7d %-9d %-12s %-8.1f" %
                  (str((d,e,V)), a, b, ne, ng, "REALISABLE" if ok else "EMPTY -> KILL", time.time()-t0))
        except Exception as ex:
            print("%-11s %-5d %-5d %-7s %-9s %-12s %-8.1f" %
                  (str((d,e,V)), e*V, d*V, "-", "-", "ERROR "+str(ex)[:24], time.time()-t0))
        sys.stdout.flush()
