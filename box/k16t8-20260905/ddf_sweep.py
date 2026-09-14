#!/usr/bin/env python3
"""Low-degree part of the Frobenius cycle type on Y_8 (x) F_32003, from w = minpoly(b3).
For k = 1..K prints deg gcd(x^(p^k) - x, w) = sum of degrees of the irreducible
factors of w of degree dividing k.  Saves every factor of positive degree."""
import sys, time
from flint import nmod_poly
p = 32003
co = [int(c) for c in open(sys.argv[1]).read().split()]
w = nmod_poly(co, p); n = w.degree()
K = int(sys.argv[2]) if len(sys.argv) > 2 else 40
x = nmod_poly([0,1], p)
h1 = x.pow_mod(p, w)
print("DDFSWEEP deg_w", n, flush=True)
h = x; tot = 0
for k in range(1, K+1):
    t0 = time.time()
    h = h1 if k == 1 else h.compose_mod(h1, w)
    d = (h - x).gcd(w)
    print("DDFSWEEP k=%d cumdeg=%d t=%.1fs" % (k, d.degree(), time.time()-t0), flush=True)
    if d.degree() > 0:
        with open("ddf_factor_k%d.txt" % k, "w") as f:
            f.write(" ".join(str(int(c)) for c in d.coeffs()) + "\n")
        print("DDFSWEEP saved ddf_factor_k%d.txt deg=%d" % (k, d.degree()), flush=True)
        tot = d.degree()
print("DDFSWEEP_DONE cum_low_degree_part=%d of %d" % (tot, n), flush=True)
