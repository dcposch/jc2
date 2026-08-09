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

def layer2():
    """Layer 2: m=2 pattern forms (Prop 8.1(ii)/4.2) + printed transport laws.

    Laws used (all printed-tier, page refs sigray_full.pdf):
      L2 (p.41, St 3.9+3.16):  mult(p_G, c) = deg(p_F) EXACT for vertex
          patterns on every edge (F = G*c deeper).
      L1 (St 8.3(ii), p.41):   equality of counts for members j <= m_F.
      L3 (St 3.11(i)):         deg(p_{h,F*c}) <= mult(p_{h,F}, c), all h.
      L4 (p.40, Prop 8.1 proof via Prop 6.3): dead member h_m at F: for ANY
          root c of p_F: mult(p_{h_m,F}, c) = (mu_F - 1)mult(p_F, c) + 1.
      L5 (Prop 4.2(iii)/8.1):  alive h_j: p_{h_j,F} = (-)p_red^{i l_j/k_j},
          i l_j/k_j in N; full pattern p_F = p_red^i (Prop 8.1(i)).
      Orbit frame (Not/Prop 9.3, 2POLE 2b): G_m patterns in eta^s*C[eta^3];
          each pole direction = full eta^3-orbit factor (eta^3-c_i^3)^{mu_i},
          mult(p_F, c_i) = i*mu_i; St 3.16: >1 root at non-pole chain vertices.
    Level-0 cross-checks of L4 (both EXACT in the banked template):
      G_m: (3/2-1)*2+1 = 2 = mult(P*q, c_i) (E5 'pq: 1+1', q = H*eta*P*(t-b));
      F_s: (25/6-1)*12+1 = 39 = mult(p_{h2,Fs}, c_m) (E4/E7)."""
    print("\nR6 LAYER-2 ledger (m_Gm = 2; suffix + merge transports)")
    assert (Fr(3,2)-1)*2 + 1 == 2 and (Fr(25,6)-1)*12 + 1 == 39  # L4 checks
    for k1, l1 in WINDOW:
        r = Fr(l1, k1)
        mu2 = Fr(3, 2) + (k1 - 1) * r          # mu_Gm, m=2 (Prop 4.2(iv))
        degp_h1_gm = 12 * r
        Mst_gm = gcd(gcd(12, 18), int(degp_h1_gm))
        i_gm = 12 // Mst_gm
        print(f"\n  ({k1},{l1}) r={r}: mu2={mu2}, M*_Gm={Mst_gm}, i_Gm={i_gm}")
        # (A) merge-edge vertex transport (L2): mult(p_f@Gm,c_i) = i_Gm*mu_i
        #     must EQUAL deg p_f@P = 2, mu_i in N>=1; orbit fit: pole orbit
        #     (eta^3-c_i^3)^{mu_i} needs 3*mu_i <= deg p_red = M*_Gm.
        A_ok = (2 % i_gm == 0) and (3 * (2 // i_gm) <= Mst_gm)
        print(f"    (A) merge transport: i_Gm*mu_i = 2 with mu_i in N: "
              f"{'PASS (mu_i=%d)' % (2//i_gm) if 2 % i_gm == 0 else 'FAIL (mu_i=2/%d not in N)' % i_gm}"
              + ("" if 2 % i_gm else f"; orbit fit 3*mu_i <= {Mst_gm}: "
                 + ("PASS" if A_ok else "FAIL")))
        if not A_ok:
            print(f"    -> DEAD (A): mult(p_f@Gm,c_i) = {i_gm}*mu_i >= {i_gm}"
                  f" != 2 = deg p_f@P (L2 exact); equivalently deg-2 reduced"
                  f" pattern cannot contain an eta^3 pole orbit (St 3.16).")
            print(f"        corroboration: L4 RHS (mu2-1)*2+1 = {2*mu2-1}"
                  f" not in N -> merge data cannot exist.")
            continue
        # (B) suffix-edge St 8.3(ii) EQUALITY for h1 (member both sides):
        #     mult(p_h1@Fs,c_m) = i_Fs*r*m1, and L2 forces i_Fs*m1 = 12
        #     -> mult = 12r = deg p_h1@Gm identically; content = m1 = 12/i_Fs
        #     in N, i_Fs from M*_Fs | gcd(126,189,126r).
        Mst_fs_h01 = gcd(63, int(126 * r))
        i_menu = [126 // d for d in range(1, Mst_fs_h01 + 1)
                  if Mst_fs_h01 % d == 0 and d in (1, 3, 7, 9, 21, 63)]
        i_ok = sorted(i for i in i_menu if 12 % i == 0)
        print(f"    (B) h1 suffix equality: i_Fs menu (m1=12/i in N): {i_ok};"
              f" mult(p_h1@Fs,c_m) = i*r*(12/i) = {12*r} == deg p_h1@Gm ="
              f" {degp_h1_gm}: PASS (identity via L2+L5)")
        # (C) E5-analogue, h1 at pole edges: mult(p_h1@Gm,c_i) = i_Gm*r*mu_i
        #     = 2r; h0 ALIVE at Gm (m=2) -> (g+)^2 = s0(f+)^3 transports ->
        #     eta^6-coeff m_i^2 - s0*lam_i^3 = 0 AUTOMATIC; pole-ODE identity
        #     z(z-(3/2)w^2)^2 - (z-w^2)^3 = -(3/4)w^4 z + w^6 (z^2 cancels):
        #     deg p_h1@P = 2 EXACT (w != 0), d_h1@P = 3/21 - 4/42 = 1/21.
        c_ok = 2 <= 2 * r
        print(f"    (C) E5-analogue h1@P: deg 2 <= mult(p_h1@Gm,c_i) = {2*r}:"
              f" {'PASS' if c_ok else 'FAIL'} (drop forced, w_i^4 pinned as"
              f" level-0 E5; d_h1@P = 1/21)")
        # (D) h2 at pole edges (the binding kill): levels k1*(1/21) vs
        #     l1*(1/21): l1 > k1 -> f-side wins: p_h2@P = (-)s1*lam^l1*
        #     (eta^2-w^2)^l1, deg 2*l1 EXACT (pure power, no drop possible).
        #     L3 + L4: 2*l1 <= mult(p_h2@Gm,c_i) = (mu2-1)*2 + 1 = 2*mu2-1
        #     <=> l1 <= k1  (TEMPLATE sec 3 R6's own inequality, now with
        #     d_h1@P pinned so it binds for ALL l1 > k1, not just l1 > 3k1).
        lhs, rhs = 2 * l1, 2 * mu2 - 1
        print(f"    (D) h2 pole-edge count: deg p_h2@P = 2*l1 = {lhs} <= "
              f"mult(p_h2@Gm,c_i) = 2*mu2-1 = {rhs}: "
              f"{'PASS' if lhs <= rhs else 'FAIL -> DEAD'}")
        if lhs > rhs:
            print(f"    -> DEAD (D): {lhs} > {rhs}; general form 2l1 <= "
                  f"2+2l1-2l1/k1 <=> l1 <= k1, false on the whole window.")
            # (E) E4-analogue (h3 top at Gm) is MOOT; record the constraint it
            #     would have imposed on (k2,l2): deg q = 12(r2-mu2+1) with
            #     q >= H*eta*P*(t-b)^{m_b} (b-orbit relocated into h2, m_b>=1)
            #     -> minimal shape forces r2 = mu2 - 1/6 (self-similar echo).
            print(f"        (E, moot) suffix h2 equality would pin deg q ="
                  f" 12(r2-{mu2-1}); minimal q-shape -> r2 = {mu2-Fr(1,6)}.")
    print("\nlayer-2 verdicts: ALL 8 DEAD (A: six k1 in {3,6}; D: (2,3),(2,5)).")
    print("R6 CLOSED: m_Gm = 1 minimal assignment forced; no isomorphic-genome"
          " survivor (the (2,3) self-similar echo dies at (D)).")

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
    layer2()
