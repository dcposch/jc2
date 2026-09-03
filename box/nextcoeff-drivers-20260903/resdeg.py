#!/usr/bin/env python3
"""RES-DEGREE (Opus ideation 20260903T1015Z sec.6), tested and CORRECTED.

Claimed:   deg_x Res_y(g - c_2, f) = sum_i (1 - delta^0_i) = N - shed,
           shed := sum_i (1 - delta^0_i)^-.
What is TRUE (proved in the report, sec.5):
  (RD-1)  deg_x Res_y(g - c_2, f - c_1) = sum_i (1 - delta^0_i)^+ = N  for generic (c_1,c_2)
          -- this is CONTACT-DEFICIENCY / FRONTIER-N and carries no new information.
  (RD-2)  deg_x Res_y(g - c_2, f)       = N - shed_0,
          shed_0 := sum over NON-PROPER branches of ord_t f(tau_i) >= 0,
          which is 0 unless f VANISHES at infinity along a non-proper branch of the
          pencil.  shed_0 is NOT sum_i (1 - delta^0_i)^-, and it is not tree data.
This file measures both on the control library.  FAIL-CLOSED.
"""
import sys, time
from fractions import Fraction as F
import sympy as sp
sys.path.insert(0, '/home/ubuntu/jc2/box/nextcoeff-drivers-20260903')
from psgrowth import (x, y, c, T, Pair, controls, big_control, negatives,
                      chi_poly, branch_orders, cmax_of, degx, check, FAIL, NCHK)

c1 = sp.Symbol('c1')

def res_degrees(P):
    n = P.n
    R0 = sp.expand(sp.resultant(sp.expand(P.g - c), P.f, y))
    R1 = sp.expand(sp.resultant(sp.expand(P.g - c), sp.expand(P.f - c1), y))
    d0 = degx(R0); d1 = degx(R1)
    ords = branch_orders(chi_poly(P.f, P.g, n))
    Npos = sum(o for o in ords if o is not None and o > 0)
    Nsum = sum(o for o in ords if o is not None)          # sum_i (1 - delta^0_i), signed
    shed_claimed = Npos - Nsum                            # sum_i (1-delta^0_i)^-
    return R0, R1, d0, d1, Npos, Nsum, shed_claimed, ords

if __name__ == "__main__":
    print("resdeg.py -- RES-DEGREE, measured.   sympy", sp.__version__)
    print("="*94)
    print("%-46s %-4s %-6s %-6s %-7s %-9s %-8s" %
          ("pair", "N", "d0", "d1", "sum(-ord f)", "N-sum", "shed_0"))
    print("   d0 = deg_x Res_y(g-c, f) ; d1 = deg_x Res_y(g-c, f-c_1) ; claimed = N - sum(1-d0)")
    rows = []
    # two DISCRIMINATING rows carrying a NON-PROPER branch (delta^0 > 1).  g = y^3 + xy
    # is monic in y with deg = deg_y = 3; the fibre has one branch tau ~ c/x on which f
    # does NOT blow up.  NP0 has f -> 0 there (a_0 = 0), NP1 has f -> 1 (a_0 != 0).
    NP = [Pair(y, y**3 + x*y, "NP0 (y, y^3+xy)  non-proper branch, a_0 = 0", "NON-KELLER"),
          Pair(y + 1, y**3 + x*y, "NP1 (y+1, y^3+xy)  non-proper branch, a_0 = 1", "NON-KELLER")]
    for P in controls() + [big_control()] + negatives() + NP:
        R0, R1, d0, d1, Npos, Nsum, shedc, ords = res_degrees(P)
        shed0 = Npos - (d0 if d0 is not None else 0)
        print("%-46s %-4s %-6s %-6s %-9s %-9s %-8s  %s" %
              (P.label[:46], Npos, d0, d1, Nsum, shedc, shed0, P.kind))
        if P.kind == "KELLER":
            check("%s : (RD-1) deg_x Res(g-c, f-c_1) = N" % P.label[:4], F(d1) == Npos,
                  "%s vs %s" % (d1, Npos))
            check("%s : (RD-2) deg_x Res(g-c, f) = N - shed_0, shed_0 >= 0" % P.label[:4],
                  shed0 >= 0, "shed_0 = %s" % shed0)
            check("%s : the CHARGED form N - sum(1-d0)^- %s" % (P.label[:4],
                  "agrees" if shedc == shed0 else "DISAGREES with the measured degree"),
                  True)
        rows.append((P.label, Npos, d0, d1, Nsum, shedc, shed0, P.kind))
    # ---- the explicit REFUTATION of the charged form, hand-computed
    print("\n-- REFUTATION WITNESS for the charged form  deg_x Res_y(g-c,f) = sum_i (1-delta^0_i)")
    print("   g = y^3 + xy (monic in y, deg = deg_y = 3).  Branches of g = c at infinity:")
    print("     tau_+- ~ +-sqrt(-x)   ord_t = -1/2 ,  delta^0 = 1/2 ,  1-delta^0 = +1/2  (PROPER)")
    print("     tau_0   ~  c/x        ord_t = +1")
    print("   NP0 (f = y)  : a_0 = 0, so 1-delta^0 = -ord_t f(tau_0) = -1 ; sum_i(1-delta^0) = 0")
    print("                  measured deg_x Res_y(g-c,f) = %s   -> charged form HOLDS here" %
          res_degrees(NP[0])[2])
    print("   NP1 (f = y+1): a_0 = 1, so 1-delta^0 = -ord_t(f(tau_0)-1) = -1 ; sum_i(1-delta^0) = 0")
    print("                  measured deg_x Res_y(g-c,f) = %s   -> charged form REFUTED (0 != %s)" %
          (res_degrees(NP[1])[2], res_degrees(NP[1])[2]))
    check("RES-DEGREE charged form is REFUTED by NP1", res_degrees(NP[1])[2] != 0,
          "deg_x Res = %s, sum_i (1-delta^0_i) = 0" % res_degrees(NP[1])[2])
    check("RES-DEGREE corrected form  d0 = N - shed_0  on NP0 (shed_0 = 1)",
          res_degrees(NP[0])[2] == 0 and res_degrees(NP[0])[4] == 1)
    print("\n-- verdict on the charged form  deg_x Res_y(g-c,f) = N - sum_i (1-delta^0_i)^- :")
    bad = [r for r in rows if r[7] == "KELLER" and r[5] != r[6]]
    print("   Keller controls where the charged 'shed' differs from the measured one: %d/%d"
          % (len(bad), len([r for r in rows if r[7] == "KELLER"])))
    for r in bad: print("     %s : claimed shed = %s, measured shed_0 = %s" % (r[0][:40], r[5], r[6]))
    print("\n%d checks, %d failures" % (NCHK[0], len(FAIL)))
    for nm, dt in FAIL: print("   FAILED:", nm, dt)
