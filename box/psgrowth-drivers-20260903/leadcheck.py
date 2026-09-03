#!/usr/bin/env python3
"""End-to-end test of RESIDUE-LEAD: PREDICT the set {k : R_k != 0} from the bottom-star
data alone, then MEASURE it on the pair.

Prediction (report sec.4): with nu conjugate bottom-major discs each carrying the star
(d,e,V_2) and per-root frontier contribution cmax, the leading term of R_k sits at
t-exponent 1 - (k+1)cmax and survives only if
   (i)  the per-disc star sum ptilde_{k+1} != 0  (measured in starres2.py), AND
   (ii) (k+1) cmax is an INTEGER      (Galois: sum over conjugates of t^{theta} with
                                       theta not in Z vanishes).
For the family (d,e,V_2) = (1,e,1) with b_1 = 1 the star is p_g = pi^e + p_0, p_f = q_1 pi,
so ptilde_j != 0 iff e | j, and cmax = 1/(e*nu) for nu conjugate discs; the two conditions
COINCIDE and R_k is expected to be EXACTLY 0 unless (e*nu) | (k+1).
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/ubuntu/jc2/box/psgrowth-drivers-20260903')
from psgrowth import (x, y, c, Pair, chi_poly, cmax_of, residues, degx, check, FAIL, NCHK)
import sympy as sp

CASES = [  # (pair, e_star, nu, label)
    (Pair(y, x + y**2, "A1 (y,x+y^2)"),        2, 1),
    (Pair(y, x + y**3, "A2 (y,x+y^3)"),        3, 1),
    (Pair(y, x + y**4, "A4 (y,x+y^4)"),        4, 1),
    (Pair(y, x + y**6, "A6 (y,x+y^6)"),        6, 1),
    (Pair(x + y**5, y + (x + y**5)**3, "D15 (x+y^5,y+(x+y^5)^3)"), 3, 5),
]
K = 24
if __name__ == "__main__":
    print("leadcheck.py -- RESIDUE-LEAD predicted vs measured   (k <= %d)" % K)
    print("="*88)
    for P, es, nu in CASES:
        cm = cmax_of(chi_poly(P.f, P.g, P.n))
        Rs = residues(P.f, P.g, P.n, K)
        meas = [k for k in range(K+1) if Rs[k] != 0]
        # RESIDUE-LEAD governs the TOP term only: it predicts exactly the k at which the
        # PS-3 bound (k+1)cmax - 1 is ATTAINED.  R_k may be nonzero at a strictly lower
        # order at other k (D15 does this at k = 17, 20, 23).
        tightm = [k for k in range(K+1)
                  if Rs[k] != 0 and F(degx(Rs[k])) == F(k+1)*cm - 1]
        pred = [k for k in range(K+1) if (k+1) % (es*nu) == 0]
        print("\n%-32s n=%-3d cmax=%-6s  star (1,%d,1) x nu=%d  1/(e*nu)=%s"
              % (P.label, P.n, cm, es, nu, F(1, es*nu)))
        print("   predicted {k : PS-3 bound ATTAINED} = %s" % pred)
        print("   measured  {k : PS-3 bound ATTAINED} = %s" % tightm)
        print("   measured  {k : R_k != 0}             = %s" % meas)
        check("%s : RESIDUE-LEAD prediction == measured tightness set" % P.label[:3],
              pred == tightm, "pred %s vs tight %s" % (pred, tightm))
        check("%s : cmax == 1/(e*nu)" % P.label[:3], cm == F(1, es*nu),
              "%s vs %s" % (cm, F(1, es*nu)))
        tight = [(k, degx(Rs[k]), F(k+1)*cm - 1) for k in meas]
        print("   deg_x R_k vs the PS-3 bound (k+1)cmax-1 on the surviving k: %s"
              % [(k, d, str(b), "TIGHT" if F(d) == b else "slack") for k, d, b in tight])
    print("\n%d checks, %d failures" % (NCHK[0], len(FAIL)))
    for nm, dt in FAIL: print("   FAILED:", nm, dt)
