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

WINDOW = [(1, 2),   # review 5(iv): missing from all prior banks; passes all window tests
          (2, 3), (2, 5), (3, 5), (3, 7), (3, 8), (6, 11), (6, 13), (6, 17)]

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
              f" level-0 E5; d_h1@P = 1/7 -- REVIEW front 4: nonzero deg-2"
              f" pattern means NO level drop; St 3.9(iii) drops d only via"
              f" mult along steps, never via in-vertex cancellation)")
        # (D) h2 at pole edges — REVIEW-CORRECTED (SHEET6-R6-REVIEW front 4):
        #     d_h1@P = 1/7 (= 3/21), so h2 = h1^k1 - s1 f^l1 at P compares
        #     levels k1*(3/21) vs l1*(1/21): h1-side wins iff l1 < 3k1 --
        #     TRUE on the whole window (r < 3). p_h2@P = (p_h1@P)^{k1},
        #     deg 2*k1, pure power, strict level gap (no cancellation).
        #     L3 + L4: 2*k1 <= mult(p_h2@Gm,c_i) = 2*mu2-1 = 2+2(k1-1)*r
        #     <=> k1 <= l1: PASSES the whole window with slack
        #     2(k1-1)(r-1) > 0 (= 0 only at k1 = 1: equality).
        lhs, rhs = 2 * k1, 2 * mu2 - 1
        print(f"    (D, corrected) h2 pole-edge count: deg p_h2@P = 2*k1 ="
              f" {lhs} <= mult(p_h2@Gm,c_i) = 2*mu2-1 = {rhs}: "
              f"{'PASS' if lhs <= rhs else 'FAIL -> DEAD'}")
        # (E) suffix h2 St 8.3(ii) equality (h2 member at F_s m>=3, dead at
        #     G_m... member at G_m m=2): forces the next-level tower datum:
        #     minimal q-shape (b-orbit relocated) pins r2 = mu2 - 1/6 --
        #     the FORCED self-similar echo (review 5(iii): real and OPEN).
        r2 = mu2 - Fr(1, 6)
        k2l2 = (6, int(6 * r2)) if (6 * r2).denominator == 1 else None
        print(f"    (E) forced echo: r2 = mu2 - 1/6 = {r2} -> (k2,l2) ="
              f" {k2l2}: next recursion rung NOT RUN -> case OPEN"
              f" (echo chain), unless k1 == 1 (see (1,2) note).")
        if k1 == 1:
            print("        (1,2) note: (D) passes AT EQUALITY; suffix"
                  " equality forces r2 = 4/3 i.e. (k2,l2) = (3,4): the"
                  " MINIMAL genome with re-indexed tower (2,3),(1,2),(3,4)"
                  " -- a DISJOINT R1 branch (d_h1@Gm = 12/21, quotient"
                  " ~P^4 vs minimal 8/21, quotient pq). Needs k1=1"
                  " exclusion or R1 enumeration (review 5(iv)).")
    print("\nlayer-2 verdicts (REVIEW-CORRECTED): 6 DEAD at (A)"
          " (k1 in {3,6}: merge transport, doubly printed-tier);"
          " OPEN: (2,3)->echo(6,17), (2,5)->echo(6,23), (1,2)->minimal-"
          "reindexed disjoint branch.")
    print("R6 status: PARTIALLY CLOSED. m_Gm >= 3 closed by review scope"
          " patch (5(i)); R1 must enumerate minimal (3,4) + (1,2) branch;"
          " echo chains need one more recursion rung.")

def _pmul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out

def _ppow(a, n):
    out = [Fr(1)]
    for _ in range(n):
        out = _pmul(out, a)
    return out

def _psub(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else Fr(0)) - (b[i] if i < len(b) else Fr(0))
            for i in range(n)]

def _pdiff(a):
    return [i * a[i] for i in range(1, len(a))]

def _pdeg(a):
    for i in range(len(a) - 1, -1, -1):
        if a[i]:
            return i
    return -1

def echo_rung():
    """ECHO RUNG (level 3) for (2,3)@(6,17), (2,5)@(6,23) + ninth case (1,2).

    Session 2026-08-09.  Additive to layer2(); its output is unchanged.

    Membership at the echo level (Prop 4.2 p.19-20 + Cor 6.1 p.32):
      m_P = 0 (g first-dead at P; h1,h2,h3 non-members there: St 3.11(i) only,
      leaks allowed -- exactly the review's '3 -> 2' and '1-branch' leaks),
      m_Gm = 2 (h2 first-dead: L4 + Prop 8.1(ii) pattern P^{i(mu2-1)}q),
      m_Fs >= 3 (strict m-growth; h2 ALIVE at F_s), m_R > m_Fs.
      Prop 4.2's delta_j := kappa(d_F + d_{h_j,F} - alpha_j d_F - 1 + u) in N
      is STRICTLY decreasing (p.20) => every tower is FINITE: no infinite
      recursion is possible at any vertex.  alpha-recursion (9):
      mu_{j+1} = mu_j + (k_j - 1) l_j/k_j.

    NEW PRINTED TOOL (this session): Prop 8.1(iv) ODE  delta*p*q' - (1-u)p'q
    = (nonzero const)*p at G_m.  With the m=2 window vertex data (all three
    open cases share it: i=2, p = P = (eta^3-a1)(eta^3-a2), delta = d/i =
    3/21, 1-u = 5/21, kappa*u = 16), the polynomial solution is FORCED:
      deg q = deg p * (1-u)/delta = 10  (top-cancellation of the ODE),
      P | q, q = H*eta*P*(eta^3 - b) with
      b = (2/3)(a1+a2)  and  a1*a2 = (a1+a2)^2/6,  a1+a2 != 0.
    (Level-0 cross-check: the minimal genome's E4 collapse solves to the
    SAME b and the same pole-orbit relation -- the pin is vertex-structural.)
    """
    print("\nR6 ECHO-RUNG ledger (level 3; session 2026-08-09)")
    # --- (0) the ODE pin at G_m, exact (scale fixed p1 = 3; covariant) ---
    p1, b_pin, H = Fr(3), Fr(2), Fr(1)          # b = (2/3)p1
    p2 = p1 * p1 / 6                            # a1a2 = (a1+a2)^2/6
    P_eta = [p2, 0, 0, -p1, 0, 0, Fr(1)]        # P(eta) = eta^6 - p1 eta^3 + p2
    q_eta = _pmul([0, H], _pmul(P_eta, [-b_pin, 0, 0, Fr(1)]))   # H*eta*P*(t-b)
    # lhs = 3*P*q' - 5*P'*q  (kappa=21 units of delta=3/21, 1-u=5/21)
    lhs = _psub(_pmul(P_eta, [3 * c for c in _pdiff(q_eta)]),
                _pmul(_pdiff(P_eta), [5 * c for c in q_eta]))
    ratio = [Fr(lhs[i], P_eta[i]) for i in range(len(P_eta)) if P_eta[i]]
    assert _pdeg(lhs) == 6 and all(r == ratio[0] for r in ratio) and ratio[0]
    assert _pdeg(q_eta) == 10 == Fr(6 * 5, 3)   # deg q pinned by the ODE
    print("  (0) Prop 8.1(iv) ODE at G_m: q = H*eta*P*(t-b) FORCED with"
          " b = (2/3)(a1+a2), a1a2 = (a1+a2)^2/6, a1+a2 != 0; deg q = 10."
          "  [3Pq' - 5P'q = const*P verified exactly]")
    # --- per-case echo rung ---
    P_t = [p2, -p1, Fr(1)]                      # P in t = eta^3
    W = _pmul(P_t, [-b_pin, Fr(1)])             # (t-a1)(t-a2)(t-b)
    for (k1, l1), (k2, l2) in (((2, 3), (6, 17)), ((2, 5), (6, 23))):
        r, r2 = Fr(l1, k1), Fr(l2, k2)
        mu2 = Fr(3, 2) + (k1 - 1) * r
        mu3 = mu2 + (k2 - 1) * r2               # alpha-recursion (9), p.19
        degh2 = int(12 * r2)                    # 34 / 46 = deg p_h2@Gm
        bound = int((mu3 - 1) * 12 + 1)         # L4 at F_s, root c_m (m_Fs=3)
        e = int(12 * mu2) - 12                  # P-exp of p_h3@Gm: k2*i*(mu2-1) = 24 / 36
        print(f"\n  ({k1},{l1}) echo (k2,l2)=({k2},{l2}): mu3 = {mu3},"
              f" L4@Fs bound = {bound}, generic deg p_h3@Gm = {6 * l2 * 2}")
        # (B') r2-forcing WITHOUT St-8.3(ii)-equality-at-j=m (which fails at
        # level 0: 16 != 18).  Printed route: 12r2 >= deg p_h2@Gm (St 3.11(i))
        # + hierarchy r2 < l1 (p.20) + grid 6r2 in N (Prop 8.1: i_Fs r2 in N)
        # + winner-consistency: any NON-TIE r2 has the f-side winning at G_m
        # (6r2 > 6(mu2 - 1/6)) and dies by the L4 count at F_s.
        menu = [Fr(s, 6) for s in range(degh2 // 2, 6 * l1)]
        for rr in menu:
            kk, ll = rr.denominator, rr.numerator
            m3 = mu2 + (kk - 1) * rr
            bd = (m3 - 1) * 12 + 1
            if rr == mu2 - Fr(1, 6):
                continue                        # the tie = the echo
            assert 6 * rr > 6 * mu2 - 1        # f-side wins at G_m
            assert 12 * ll > bd                # count kill: 12*l2 > (mu3-1)12+1
        print(f"    (B') r2 menu 6r2 in [{degh2 // 2},{6 * l1 - 1}]: every"
              f" non-tie value dies (f-side wins at G_m, 12*l2 > L4@Fs);"
              f" r2 = mu2 - 1/6 = {mu2 - Fr(1, 6)} is the UNIQUE survivor.")
        # (A') enlarged-family gcds at the echo level
        Mfs = gcd(gcd(126, 189), gcd(int(126 * r), int(126 * r2)))
        assert Mfs == 21 and 126 // Mfs == 6 and 12 % (126 // Mfs) == 0
        print(f"    (A') M*_Fs = gcd(126,189,{int(126 * r)},{int(126 * r2)})"
              f" = 21, i_Fs = 6, m1 = 2 in N (supersedes the layer-1 '63/2'"
              f" smell); G_m side unchanged: M* = 6, i = 2, mu_i = 1,"
              f" two-pole orbit fit 3+3 <= 6 exact.")
        # (C'/D') pole edges, corrected d-arithmetic: d_h2@P = 2/7 = k1/7,
        # levels k2*d_h2@P = 12/7 > l2*d_f@P = l2/21: h2-side wins
        assert Fr(12, 7) > Fr(l2, 21)
        mult_h3_gm_ci = e + 6                  # P^e*(q^6 - s2'P^10): e + 6
        assert 24 <= mult_h3_gm_ci
        print(f"    (C'/D') h3@P: h2-side wins (12/7 > {l2}/21), p_h3@P ="
              f" (p_h1@P)^12, deg 24 <= mult(p_h3@Gm,c_i) = {mult_h3_gm_ci}:"
              f" PASS (leak allowed: m_P = 0, h3 a non-member at P).")
        # (RUNG) the 3-coefficient W2-collapse at G_m:
        #   p_h3@Gm = (P^e q)^6 - s2' P^{6e+10}, e = i(mu2-1)/... = {4,6}
        #           = P^{6e} (q^6 - s2' P^10);  drop needed: >= 9 eta-degrees
        F = _psub(_pmul([Fr(0), Fr(0), H ** 6], _ppow(W, 6)),  # H^6 t^2 W^6
                  _ppow(P_t, 10))                              # s2' = H^6
        assert all(F[i] == 0 for i in (20, 19, 18)) and F[17] != 0
        assert 6 * e + 3 * 17 == bound          # saturates the L4@Fs bound
        print(f"    (RUNG) W2-collapse q^6 - s2'P^10: t^20,t^19,t^18 vanish"
              f" IDENTICALLY at s2' = H^6 (t^19,t^18 are the ODE pin);"
              f" t^17 != 0 => deg p_h3@Gm = {6 * e}+51 = {bound} ="
              f" L4@Fs bound EXACTLY.  3 conditions, 2 unknowns, 0 kill:"
              f" the overdetermination is absorbed by Prop 8.1(iv).  PASS.")
        # (E) next rung: tie at G_m needs 6r3 = {bound}/2 -- half-integral =>
        # impossible; k3 >= 2 dies both winners; k3 = 1 passes at equality.
        assert Fr(bound, 2).denominator == 2    # no tie on the 6r3 in N grid
        for six_r3 in range(1, 6 * l2):         # hierarchy r3 < l2
            r3 = Fr(six_r3, 6)
            k3, l3 = r3.denominator, r3.numerator
            mu4 = mu3 + (k3 - 1) * r3
            bd4 = (mu4 - 1) * 12 + 1
            if 12 * r3 > bound:                 # f-side wins at G_m
                assert 12 * l3 > bd4            # dead, every k3
            elif k3 >= 2:                       # h3-side, k3 >= 2
                assert bound * k3 > bd4         # dead: (k3-1)(bound-12r3) > 0
            else:                               # k3 = 1, h3-side
                assert bound * 1 == bd4         # equality pass, mu frozen
        print(f"    (E) rung 4: G_m tie impossible (6r3 = {Fr(bound, 2)}"
              f" not in N); f-side and every k3 >= 2 h3-side step DIE by the"
              f" same count; ONLY k3 = 1 survives (at equality, mu4 = mu3)."
              f"  Hierarchy (p.20) l3 > l4 > ... in N => the (1,l)-tail is"
              f" FINITE; delta_j(R) strictly decreasing (p.20) => the tower"
              f" TERMINATES.  No print contradiction, no infinite echo.")
        print(f"    VERDICT ({k1},{l1}): echo chain SURVIVES the printed"
              f" tier as a FINITE forced tower (2,3),({k1},{l1}),({k2},{l2})"
              f",(1,l3),...  -> R1 branch (staged G_m depths"
              f" {int(6 * r)}/42, {degh2}/42, {bound}/42; pole moduli pinned"
              f" a1a2 = (a1+a2)^2/6, a2/a1 = 2+-sqrt(3)).")
    # --- ninth case (1,2) ---
    print("\n  (1,2): k1 = 1 disposition.  Prop 4.2(iii) with k1 = 1 reads"
          " h1+ = s1 (f+)^2 EXACTLY -- a legality condition, checked at"
          " every vertex where the level-1 tie holds (h1 alive: R, F_s,"
          " G_m); at all three the alive patterns are pure powers"
          " (p_h1 = p_red^{2i}, (p_f)^2 = p_red^{2i}): CONSISTENT -- and"
          " at P the tie fails (3/21 > 2/21), so the level-0 nonzero"
          " deg-2 pattern p_h1@P (2 roots, not a square) is NOT constrained:"
          " NO k1 = 1 exclusion exists in print.")
    mu2 = Fr(3, 2)
    for rr in (Fr(4, 3), Fr(3, 2), Fr(5, 3), Fr(11, 6)):    # 16<=12r2, r2<2
        kk, ll = rr.denominator, rr.numerator
        bd = (mu2 + (kk - 1) * rr - 1) * 12 + 1
        if rr == Fr(4, 3):
            continue                            # tie: 8*k2 = 6*l2
        assert 6 * rr > 8 and 12 * ll > bd      # f-side wins and dies
    print("    (B') same winner-consistency forcing: r2 menu {4/3,3/2,5/3,"
          "11/6}: non-tie values die (12*l2 > (mu3-1)12+1); r2 = 4/3 forced"
          " => (k2,l2) = (3,4): the MINIMAL genome re-indexed, dead-member"
          " data at G_m byte-identical (P*q, deg 16, d = 8/21, same ODE pin).")
    print("    VERDICT (1,2): NOT print-excludable; DISJOINT R1 branch."
          "  R1 delta-spec: insert ONE staged resonance level at G_m:"
          " 18/21 -> 12/21 (h1 stage, quotient prop. to P^4, legality"
          " h1+ = s1(f+)^2) -> 8/21 (h2 stage, quotient P*q) -> (3,4)"
          " continuation identical to the minimal genome's L1c layer.")
    print("\nECHO-RUNG verdicts: (2,3)-chain SURVIVES-IN-PRINT (finite"
          " forced tower, R1 branch); (2,5)-chain SURVIVES-IN-PRINT (same);"
          " (1,2) SURVIVES-IN-PRINT (minimal re-indexed, R1 branch).")
    print("R6 status: CLOSED AS A PRINT CAMPAIGN -- no further printed-tier"
          " test can kill the three survivors; R1 must run per-branch on"
          " {minimal (3,4), (1,2), (2,3)-chain, (2,5)-chain}.")

if __name__ == "__main__":
    layer2()
    echo_rung()
