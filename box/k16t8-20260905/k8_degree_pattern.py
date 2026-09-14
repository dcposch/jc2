#!/usr/bin/env python3
"""Cor. 3.6 degree-pattern instrument at t=8: the Frobenius cycle type on the
n = 52138 geometric points of the mod-p chart, read off the eliminating
polynomial w = minpoly(b3) produced by msolve's FGLM.

Prints, in order:
  DEG        deg w                      (must equal n = 52138 for Lemma 3.5)
  SQFREE     gcd(w, w') == 1            (Cor. 3.6 hypothesis: m-bar squarefree)
  NROOTS     #F_p-roots of w            (= #F_p-points of the chart)
  DDF k ...  deg gcd(x^(p^k) - x, w)    (distinct-degree factorisation, cumulative)
  RABIN      x^(p^n) == x and gcd(x^(p^(n/l)) - x, w) == 1 for every prime l | n
             <=> w irreducible <=> ONE Frobenius orbit on the n points.
"""
import sys, time
from flint import nmod_poly
p = 32003
co = [int(c) for c in open(sys.argv[1]).read().split()]
w = nmod_poly(co, p)
n = w.degree()
print("DEG", n, flush=True)
x = nmod_poly([0, 1], p)
t0 = time.time()
g = w.gcd(w.derivative())
print("SQFREE", g.degree() == 0, "gcd_deg", g.degree(), "t=%.1fs" % (time.time()-t0), flush=True)
t0 = time.time()
h1 = x.pow_mod(p, w)               # x^p mod w
print("FROB1 built t=%.1fs" % (time.time()-t0), flush=True)
t0 = time.time()
d1 = (h1 - x).gcd(w)
print("DDF 1 deg", d1.degree(), "(#linear factors) t=%.1fs" % (time.time()-t0), flush=True)
# cheap low-degree sweep
h = h1
for k in range(2, 9):
    t0 = time.time()
    h = h.compose_mod(h1, w)       # x^(p^k) mod w
    dk = (h - x).gcd(w)
    print("DDF", k, "deg", dk.degree(), "t=%.1fs" % (time.time()-t0), flush=True)
# Rabin irreducibility test
def frob_pow(e):
    """x^(p^e) mod w, by binary powering of the Frobenius composition."""
    res = x; base = h1; ee = e
    while ee:
        if ee & 1: res = res.compose_mod(base, w)
        base = base.compose_mod(base, w)
        ee >>= 1
    return res
for l in (2, 131, 199):
    assert n % l == 0
    t0 = time.time()
    hl = frob_pow(n // l)
    dl = (hl - x).gcd(w)
    print("RABIN_PROPER l=%d n/l=%d gcd_deg=%d" % (l, n // l, dl.degree()),
          "t=%.1fs" % (time.time()-t0), flush=True)
t0 = time.time()
hn = frob_pow(n)
print("RABIN_FULL x^(p^n)==x :", hn == x, "t=%.1fs" % (time.time()-t0), flush=True)
print("K8_INSTRUMENT_DONE", flush=True)
