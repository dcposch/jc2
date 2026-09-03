#!/usr/bin/env python3
"""S1: SUBCHART on R = {q_{t-r,0}, b3}: closed forms in t at a fixed offset r.

Sem = <t-r, t+1>.  Predicted eliminated survivors (Prop. SUBCHART), uniformly
in t:  C_{t-r}=c1 x, q_{t+1,0}=c2 b3, q_{2t-2r,0}=c3 x^2, q_{2t-r+1,0}=c4 x b3,
and (only when r=1, because 3t+1=a(t-r)+b(t+1) forces a=2/(1+r)) b1=c5 x b3^2.
B0 (weight t) and b2 (weight 2t+1) never survive: a(1+r)=1 has no solution.
"""
import sys, time, json, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16subchart-20260903")
import sq_engine as S
from sq_engine import (t, r, x, b3, d, c1, c2, c3, c4, c5, E, ex, hcoeff,
                       spine, red, collisions)

def _norm(u):
    """N(A d + B) = B^2 - A^2 (t+1)/3;  u is a unit of A_t iff N(u) != 0."""
    P = sp.Poly(sp.expand(sp.together(u)*sp.denom(sp.together(u))), d)
    A, B = P.nth(1), P.nth(0)
    return sp.expand(B**2 - A**2*(t+1)/sp.Integer(3))


RV = int(sys.argv[1]) if len(sys.argv) > 1 else 1
S.set_r(RV)
T0 = time.time()
O = spine(has_b1=(RV == 1))
print("# r=%d   spine built in %.1fs" % (RV, time.time()-T0), flush=True)
for nm in ("C", "A", "U", "B", "D", "V", "Y", "Z", "Xp"):
    print("  %-3s h-exponents: %s" % (nm, [str(ex(k)) for k in sorted(O[nm])]))
Phi = O["Phi"]
print("\n# Phi: band k (= h-exponent) and weight 4t+1-k")
for k in sorted(Phi, reverse=True):
    print("   k = %-10s  weight = %-10s" % (sp.expand(ex(k)), sp.expand(4*t+1-ex(k))))

# --- high bands: k >= 2t, i.e. exponent triple (a,_,c) with a>2 or (a=2,c>=0)
def is_high(k):
    return k[0] > 2 or (k[0] == 2 and k[2] >= 0)

high = {k: v for k, v in Phi.items() if is_high(k)}
print("\n# high bands (k >= 2t) and their content")
eqs = []
for k in sorted(high, reverse=True):
    v = red(high[k])
    print("   k=%-10s : %s" % (sp.expand(ex(k)), sp.factor(sp.simplify(v)) if v != 0 else 0))
    if v != 0:
        eqs.append(v)
unk = [c1, c2, c3, c4] + ([c5] if RV == 1 else [])
if RV == 1:
    print("\n   c5 (b1 divisibility) =", sp.factor(sp.simplify(O["extra"]["b1"])))
else:
    print("\n   b1 divisibility constant (must be 0):",
          sp.simplify(O["extra"]["b1_condition"]))
# The solve is triangular: band 4t+1-w is affine in the weight-w variable.
print("\n# sequential (triangular) solve of the high bands", flush=True)
# high band 4t+1-w for w = t-r, t+1, 2t-2r, 2t-r+1 respectively
order = [(E(3, 1, 1), c1), (E(3, 0, 0), c2), (E(2, 2, 1), c3), (E(2, 1, 0), c4)]
SOL = {}
for key, var in order:
    row = red(high[key].subs(SOL))
    P = sp.Poly(row, var)
    assert P.degree() == 1, (var, P.degree())
    lead, rem = red(P.nth(1)), red(P.nth(0))
    Nlead = sp.factor(sp.simplify(_norm(lead)))
    val = red(-rem/lead)
    SOL[var] = val
    print("   band k=%-9s pivot %s : N(coeff)=%s" % (sp.expand(ex(key)), var, Nlead),
          flush=True)
    print("      %s = %s" % (var, sp.factor(sp.simplify(val))), flush=True)
if RV == 1:
    C5 = red(O["extra"]["b1"].subs(SOL))
    print("   c5 = %s" % sp.factor(sp.simplify(C5)))
for k in sorted(high, reverse=True):
    chk = red(high[k].subs(SOL))
    assert chk == 0, (ex(k), chk)
print("   all high bands vanish at the solution : OK", flush=True)

# --- terminal bands
print("\n# terminal bands k < 2t  (weight, monomial, scalar)")
rows = {}
for k in sorted(Phi, reverse=True):
    if is_high(k):
        continue
    v = red(Phi[k].subs(SOL))
    kk = sp.expand(ex(k))
    if v == 0:
        print("   k=%-10s : 0" % kk); continue
    P = sp.Poly(v, x, b3)
    terms = P.terms()
    rows[str(kk)] = {}
    for mon, co in terms:
        co = sp.factor(sp.simplify(red(co)))
        rows[str(kk)]["x^%d*b3^%d" % mon] = str(co)
        NN = sp.factor(sp.simplify(_norm(co)))
        print("   k=%-10s wt=%-10s  x^%d b3^%d\n        coeff = %s\n        N     = %s"
              % (kk, sp.expand(4*t+1-ex(k)), mon[0], mon[1], co, NN), flush=True)
print("\n# exponent collisions of Phi (t at which two h-exponents coincide)")
print("  ", collisions(Phi, 2, 40))
print("\n# elapsed %.1fs" % (time.time()-T0))
json.dump({"r": RV, "rows": rows,
           "c": {str(k): str(sp.factor(sp.simplify(v))) for k, v in SOL.items()}},
          open("/home/ubuntu/jc2/box/k16subchart-20260903/subchart_r%d.json" % RV, "w"),
          indent=2, sort_keys=True)
