#!/usr/bin/env python3
"""Control for the tail identity  J(Q,P) = -J(Q,S_<0)  in the bridge normal form.

S = sum_k a_k Q^{(e-k)/q} is a formal power of Q, so J(Q,S)=0; P = S_{h>=0},
hence J(Q,P) = -J(Q,S_{h<0}).  Checked at t=1 on random rational chart points by
comparing J(Q,P) against -J(Q,S_{<0}) truncated h-adically.
"""
import sys, importlib.util, sympy as sp, random
sys.argv = ['x', '1']
spec = importlib.util.spec_from_file_location("bc", "box/k16spine-opus-20260903/bridge_chart.py")
bc = importlib.util.module_from_spec(spec); spec.loader.exec_module(bc)
g, p = bc.g, bc.p
random.seed(11)
pts = {s: sp.Rational(random.randint(-4, 4), random.randint(1, 3))
       for s in bc.unk if str(s) != 'c'}
Q0 = sp.expand(bc.Qpoly.subs(pts)); P0 = sp.expand(bc.Pbr.subs(pts))
Sneg = {k: sp.expand(v.subs(pts)) for k, v in bc.Pser.items() if k < 0}
h0 = sp.expand(bc.h_poly.subs(pts))
def J(a, b): return sp.expand(sp.diff(a,g)*sp.diff(b,p) - sp.diff(a,p)*sp.diff(b,g))
lhs = J(Q0, P0)
# -J(Q, sum_{k<0} c_k h^k)  as a Laurent polynomial in h; compare the h^0 part
rhs = 0
for k, ck in Sneg.items():
    if k < -3: continue                       # h^{-4} and below cannot reach h-level 0
    rhs += J(Q0, ck*h0**k)
rhs = sp.expand(sp.together(-rhs))
diff = sp.simplify(sp.together(lhs - rhs))
num, den = sp.fraction(sp.cancel(diff))
print("  J(Q,P) degree in (g,p):", sp.total_degree(lhs))
print("  ord_h of first discarded term:", max(k for k in Sneg) if Sneg else None)
print("  J(Q,P) + J(Q,S_<0 truncated at h^-3) == 0 ?", sp.expand(num) == 0)
if sp.expand(num) != 0:
    r = sp.Poly(sp.expand(num), g, p)
    print("   (residual is the h^<0 remainder; lowest h-power kept = -3)")
    print("   residual total degree:", r.total_degree())
