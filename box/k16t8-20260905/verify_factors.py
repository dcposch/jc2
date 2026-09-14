#!/usr/bin/env python3
"""Verify the low-degree factors found by the DDF sweep: each divides w exactly and
is irreducible over F_32003; the three are pairwise coprime."""
from flint import nmod_poly
p = 32003
w = nmod_poly([int(c) for c in open("w_t8_b3_p32003.txt").read().split()], p)
fs = {}
for k in (7, 17, 20):
    f = nmod_poly([int(c) for c in open("ddf_factor_k%d.txt" % k).read().split()], p)
    fs[k] = f
    q, r = divmod(w, f)
    fac = f.factor()
    irr = (len(fac[1]) == 1 and fac[1][0][1] == 1 and fac[1][0][0].degree() == f.degree())
    print("FACTOR k=%d deg=%d DIVIDES_W=%s IRREDUCIBLE=%s" % (k, f.degree(), r.is_zero(), irr), flush=True)
prod = fs[7] * fs[17] * fs[20]
q, r = divmod(w, prod)
print("PRODUCT deg=%d DIVIDES_W=%s cofactor_deg=%d" % (prod.degree(), r.is_zero(), q.degree()), flush=True)
print("PAIRWISE_COPRIME", all(fs[a].gcd(fs[b]).degree() == 0 for a, b in ((7,17),(7,20),(17,20))), flush=True)
print("VERIFY_FACTORS_DONE", flush=True)
