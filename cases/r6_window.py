#!/usr/bin/env python3
"""R6 window, layer-1 arithmetic (SHEET6-R6.md; parent-session inline build).

Deeper-tower variants of the two-pole template: m_{G_m} = 2, tower level-1
exponents (k1,l1) in the surviving window 4/3 < r=l1/k1 < 3, 6r in N
(SHEET6-LT-REVIEW.md 7c; SHEET6-TEMPLATE.md sec 3 R6).

Layer 1 = everything decidable from the ladder + gcd + count-law skeleton
already fixed by SHEET6-TEMPLATE.md sec 2c (E2/E3 printed logic), WITHOUT
the m=2 pattern forms of Prop 8.1(ii) (layer 2, pending):
  (a) integrality of every ladder entry (deg p_h at each vertex);
  (b) M*_{F_s} = gcd(deg p_f, deg p_g, deg p_h1)|_{F_s} and i = deg p/M*;
  (c) E3-analogue top-cancellation at G_m one level up: with m_{G_m}=2, h2
      is a TOWER MEMBER at G_m, so its tops must cancel STRICTLY:
      k1*d_h1 = l1*d at G_m with d_h1 = r*d  =>  k1*r = l1 holds
      identically -- the R6 constraint moves to level 2: h3 = h2^{k2}-s2 f^{l2}
      dead at G_m => p_{h3,G_m} = top; the E3 count argument then runs on
      (k2,l2) at the NEXT level (recursion), but the LEVEL-1 h2 ladder value
      is pinned: d_h2 = ? by the delta-recursion (Prop 4.2): tower-member
      cancellation depth d_{h2} < r2 := l1*d... layer 2. What IS decidable
      here: the h2 ladder integrality under d_{h2,Gm} = (l1/k1-tower alive)
      unknown => we record only deg-p integrality for h1.
  (d) E2-analogue suffix-edge count for h1 with St 8.3(ii) EQUALITY (h1 is
      a tower member at BOTH F_s (m>=3) and G_m (m=2)):
      deg p_{h1,G_m} must EQUAL mult(p_{h1,F_s}, c_m).
      Layer-1 lower/upper bounds on that mult from the i/M* skeleton alone:
      mult >= (deg p_{h1,F_s}/deg p_{F_s}) * mult(p_{F_s},c_m) is NOT a
      printed law; the only printed-safe layer-1 relation is the MONOTONE
      count law St 3.11(i): deg p_{h1,G_m} <= mult(p_{h1,F_s}, c_m)
      <= deg p_{h1,F_s} / (number of eta-orbits >= 1)  -- too weak to kill
      alone; we bank the numbers for layer 2.
Honest output: per case, PASS/FAIL per sub-test + DECIDED/UNDECIDED-AT-L1.
"""
from fractions import Fraction as Fr
from math import gcd

# Level-0 genome frame (SHEET6-TEMPLATE.md 1a): kappa scaling column
# d-values at vertices (units of 1: d_F = D/kappa with kappa_R=1 scale)
D_F = {"R": 42, "Fs": 42, "Gm": 6, "P": 2}            # D_f (f-a level D)
KAP = {"R": 1, "Fs": 7, "Gm": 21, "P": 42}
DEGP_F = {"R": 126, "Fs": 126, "Gm": 12, "P": 2}      # deg p_f at vertex
DEGP_G = {"R": 189, "Fs": 189, "Gm": 18, "P": 3}      # deg p_g
# d (level) per vertex = D/kappa
d_f = {v: Fr(D_F[v], KAP[v]) for v in D_F}
d_g = {"R": Fr(63, 1), "Fs": Fr(9, 1), "Gm": Fr(9, 21), "P": Fr(3, 42)}
# NB table 1a lists d_g slightly differently normalized; ratios are what matter.

WINDOW = [(2, 3), (2, 5), (3, 5), (3, 7), (3, 8), (6, 11), (6, 13), (6, 17)]

def case_report(k1, l1):
    r = Fr(l1, k1)
    rep = {"k1": k1, "l1": l1, "r": r, "tests": {}}
    # window sanity
    rep["tests"]["window"] = (Fr(4, 3) < r < 3) and (6 * r).denominator == 1
    # (a) h1 ladder: tower member at R, Fs, Gm  => d_h1 = r * d_f there;
    # deg p_h1 at vertex = r * deg p_f (h1 "is" f^r on the tower locus)
    degp_h1 = {v: r * DEGP_F[v] for v in ("R", "Fs", "Gm")}
    rep["degp_h1"] = degp_h1
    rep["tests"]["h1_integrality"] = all(x.denominator == 1 for x in degp_h1.values())
    # (b) M* and i at F_s over the family {f,g,h1}
    if rep["tests"]["h1_integrality"]:
        Mstar = gcd(gcd(126, 189), int(degp_h1["Fs"]))
        i_Fs = 126 // Mstar
        rep["Mstar_Fs"], rep["i_Fs"] = Mstar, i_Fs
        # Level-0 suffix-edge geometry required i quantized to the eta^7-orbit
        # structure: mult(p_{F_s}, c_m) = 6 needs i | 6*? -- printed-safe form:
        # the merge ratio 9.3(b) fixed deg q = 10 and i_Gm = 2 at level 0;
        # the F_s reduced pattern lives in t = eta^7 => i_Fs must divide
        # deg p_{Fs}/deg_t(pattern) = 126/3 = 42 and match M* | multiples of 21
        # exactly when 3 | 6r fails/holds; we bank i for layer 2 and flag the
        # E2-shape smell: i_Fs = 2 reproduces the KILLED m=1 geometry.
        rep["tests"]["i_not_2_smell"] = (i_Fs != 2)
    else:
        rep["Mstar_Fs"] = rep["i_Fs"] = None
        rep["tests"]["i_not_2_smell"] = None
    # (d) suffix-edge equality target for layer 2
    rep["suffix_equality_target"] = (degp_h1["Gm"],
                                     f"mult(p_h1@Fs,c_m) must EQUAL {degp_h1['Gm']}")
    # h2 at G_m alive (m=2): strict top-cancellation is identically satisfiable
    # (k1*r == l1); the binding level-2 data (d_h2, deg p_h2) needs Prop 4.2
    # delta-recursion values => layer 2.
    return rep

def main():
    print("R6 layer-1 ledger (see SHEET6-R6.md; layer 2 = m=2 pattern forms)")
    for k1, l1 in WINDOW:
        rep = case_report(k1, l1)
        t = rep["tests"]
        verdict = "UNDECIDED-AT-L1"
        why = []
        if not t["window"]:
            verdict, why = "EXCLUDED-L1", ["window arithmetic fails"]
        elif not t["h1_integrality"]:
            verdict, why = "DEAD-L1", ["h1 ladder non-integral"]
        else:
            why.append(f"M*_Fs={rep['Mstar_Fs']}, i_Fs={rep['i_Fs']}")
            if not t["i_not_2_smell"]:
                why.append("i_Fs=2 reproduces the E2-killed m=1 geometry "
                           "(layer-2 check expected fatal)")
            why.append(f"suffix equality target: deg p_h1@Gm = {rep['suffix_equality_target'][0]}")
        print(f"  ({k1},{l1}) r={rep['r']}: {verdict} | " + "; ".join(why))
    print("layer-1 complete; no case fully closes at layer 1 except by "
          "non-integrality (none); kills require layer-2 pattern counts.")

if __name__ == "__main__":
    main()
