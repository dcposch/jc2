#!/usr/bin/env python3
"""C3: the t=2 base case, in the cone formulation.

On the fibre d=-1 (y=1/5) of A_2 = Q x Q the positive-band cone V(I_{2,+}) is
the whole b3-axis (dim 1, confirmed by dimtest_t2_branch0), because alpha_2 is
a zero divisor vanishing exactly there and phi_2 = 0.  So W != empty at t=2 and
the producer's RESIDUAL-ZERO/TOP-TAIL-UNIT split cannot apply.  Lemma CONE says
(8.1) still holds iff tau_2 (the weight-9 part of T_{2,0}) lies in sqrt(I_{2,+}).
This script emits the two Singular checks:
   (a) Rabinowitsch: 1 in <I_+, 1 - z*tau> ?      <=> tau in sqrt(I_+)
   (b) the direct unit test 1 in <T_{2,0},...,T_{2,3}> on both fibres.
"""
import pathlib, sys, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16terminal-opus-20260903")
from tf_load import load
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16terminal-opus-20260903")

t = 2
D = load(t); y, H, b3, b4 = D["y"], D["H"], D["b3"], D["b4"]
roots = sorted(sp.Poly(H, y).all_roots())
tau = sp.expand(D["rows"][0] - sp.expand(D["rows"][0]).subs({b3: 0, b4: 0}))
print("tau_2 =", sp.factor(tau))
print("tau_2 | b4=0 :", sp.expand(tau.subs(b4, 0)))
print("c     =", sp.factor(sp.expand(D["rows"][0]).subs({b3: 0, b4: 0})))

def clear(e, vs):
    e = sp.expand(e)
    if e == 0:
        return None
    p = sp.Poly(e, *vs, domain="QQ")
    den = 1
    for co in p.coeffs():
        den = sp.ilcm(den, sp.Rational(co).q)
    p = sp.Poly(sp.expand(e*den), *vs, domain="QQ")
    return sp.expand(p.as_expr()/sp.gcd(list(p.coeffs())))

for i, r in enumerate(roots):
    sub = {y: sp.nsimplify(r)}
    pos = [clear(D["rows"][k].subs(sub), [b4, b3]) for k in range(1, 2*t)]
    pos = [g for g in pos if g is not None]
    tv = clear(tau.subs(sub), [b4, b3])
    full = [clear(D["rows"][k].subs(sub), [b4, b3]) for k in range(0, 2*t)]
    full = [g for g in full if g is not None]
    src = ["ring R=0,(z,b4,b3),dp;"]
    src.append("ideal Ipos=" + ",".join(str(g).replace("**", "^") for g in pos) + ";")
    src.append("ideal Rab=Ipos, 1-z*(%s);" % str(tv).replace("**", "^"))
    src.append("ideal GR=std(Rab);")
    src.append('printf("t=2 branch%d RABINOWITSCH_tau_in_radical=%%s", (size(GR)==1 && GR[1]==1));' % i)
    src.append("ideal Ifull=" + ",".join(str(g).replace("**", "^") for g in full) + ";")
    src.append("ideal GF=std(Ifull);")
    src.append('printf("t=2 branch%d y=%s UNIT_IDEAL_8.1=%%s", (size(GF)==1 && GF[1]==1));' % (i, r))
    src.append("quit;")
    p = HERE/("t2_cone_branch%d.sing" % i)
    p.write_text("\n".join(src) + "\n")
    print("wrote", p)
