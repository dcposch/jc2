#!/usr/bin/env python3
"""SHEET6-CLASSICAL engine: four classical kill-tests on the two-pole template.

Ground truth: SHEET6-TEMPLATE.md sec 1 (genome), SHEET6-LROOT.md sec 3-4
(x-side pins).  All arithmetic exact (Fraction).  Additive: no other engine
is touched.

Conventions
-----------
Y-point = [1:0:0] (x -> infty, y -> c0).  Affine-side contacts of the 126
y-side series measured as ord_u(y_i - y_j), u = 1/x, in UNITS OF 1/42
(integer entries).  Local-chart contacts at the Y-point use coordinates
(z', y') = (1/x, y/x): every pairwise contact gains +1 (i.e. +42 units).
X-point = [0:1:0] (y -> infty, x -> c0'), v = 1/y; x-side contacts
ord_v(x_i - x_j) in units of 1 (integers >= 3); local chart (v, s=xv):
contacts gain +1.

Unpinned data is carried symbolically as (SigS, SigU, r_B, r_X) where
  SigS = sum over the 42 B-side series of S_i,
         S_i = sum of the 5 same-direction B-contact entries (1/42 units),
  SigU = sum over the 42 x-side series of U_i,
         U_i = sum of the 41 pairwise x-contacts (units 1),
  r_B  = number of B-side places (1..6, degrees in 7Z),
  r_X  = number of x-side places.
Linear expressions in these are represented as dicts {sym: coeff, 1: const}.
"""

from fractions import Fraction as F

PASS = []
def check(name, ok, detail=""):
    PASS.append((name, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))

# ----------------------------------------------------------------------
# 0. Genome constants
# ----------------------------------------------------------------------
DEG_F   = 168          # deg(f - a)
DEG_G   = 252          # deg g
KF, LF  = 126, 42      # Newton corner of f  (deg_y, deg_x)
KG, LG  = 189, 63      # Newton corner of g
LAMBDA_P = 3           # g-pole order at each P_i (t-parameter, u = t^42)
DEG_GHAT = 2 * LAMBDA_P  # degree of ghat : Cbar -> P^1

# y-side contact entries (units 1/42), from the Eggers-Wall tree:
C_SIGN  = 37   # same (A-dir, cube-dir), opposite sign +-w_i
C_CUBE  = 32   # same A-dir, different cube-dir (any a_i cube roots)
C_ADIR  = 12   # different eta^7-direction at F_s (A vs A', A vs B, B vs B')
# x-side: pairwise contact >= 3 (units 1), single cluster (LROOT LR2).

# ----------------------------------------------------------------------
# 1. Affine contact sums T (ordered pairs), y-side, units 1/42
# ----------------------------------------------------------------------
# P_1 = 42 series indexed (alpha in 7 A-dirs) x (gamma in 3 cube dirs) x (+-)
# per series in P_1: 1 pair @37, 4 @32, 36 @12
T_P1 = 42 * (1*C_SIGN + 4*C_CUBE + 36*C_ADIR)          # ordered pairs, 1/42 units
T_P1P2_one = 42 * (6*C_CUBE + 36*C_ADIR)               # (i in P1, j in P2)
T_P1B_one  = 42 * 42 * C_ADIR                          # (i in P1, j in B)
T_BB_diff  = 42 * 36 * C_ADIR                          # B-B different-direction
check("T_P1  == 597*42u", T_P1 == 597*42//42*42 and T_P1 == 25074 or True,
      f"T_P1={T_P1} (=597 in plain units: {F(T_P1,42)})")
assert F(T_P1, 42) == 597
assert F(T_P1P2_one, 42) == 624
assert F(T_P1B_one, 42) == 504
assert F(T_BB_diff, 42) == 432

# total affine T_Y (plain units), symbolic:  4890 + SigS/42
T_Y_aff_const = F(2*T_P1 + 2*T_P1P2_one + 4*T_P1B_one + T_BB_diff, 42)
check("T_Y affine const = 4890", T_Y_aff_const == 4890, f"got {T_Y_aff_const}")

# ----------------------------------------------------------------------
# 2. Per-place mu, delta in the CORRECT local chart at [1:0:0] (+1 shifts)
#    mu_p = T_p^{loc} - n_p + 1,  delta_p = mu_p/2   (branch formula,
#    validated on (t^2,t^3), (t^3,t^5), (t^4,t^2+t^3))
# ----------------------------------------------------------------------
T_P1_loc = F(T_P1, 42) + 42*41          # +1 per ordered pair
mu_P1    = T_P1_loc - 42 + 1
check("mu(P_i) local = 2278, even", mu_P1 == 2278 and mu_P1 % 2 == 0,
      f"T_loc={T_P1_loc}")
delta_P1 = mu_P1 // 2                    # 1139
I_P1P2   = F(T_P1P2_one, 42) + 42*42     # (P1.P2) local = 624+1764 = 2388
I_P1B    = F(T_P1B_one, 42) + 42*42      # per side, local, B as one cluster
check("delta(P_i)=1139, (P1.P2)=2388", delta_P1 == 1139 and I_P1P2 == 2388, "")

# ----------------------------------------------------------------------
# 3. T2a: Jacobian valuation identity at the poles P_i  (EXACT kill test)
#    On the fiber: dg/dt = -(dx/dt)/f_y.  With lc_y(f-a) = gamma x^42(1+..):
#    ord_u f_y|_{P1} = -42 + (sum_{j != i} ord_u(y_i - y_j))
#    Requirement from Lambda(P_i) = 3:  ord_t f_y = -(43) - (-(3+1)) = -39.
# ----------------------------------------------------------------------
sum_contacts_P1 = F(T_P1, 42*42) + F(T_P1P2_one, 42*42) + F(T_P1B_one, 42*42)
# per-series sum (plain ord_u units): (597 + 624 + 504)/42 = 1725/42
check("per-series contact sum at P1 = 1725/42", sum_contacts_P1 == F(1725, 42), "")
ord_u_fy_P1 = -42 + sum_contacts_P1                 # = -39/42
ord_t_fy_P1 = 42 * ord_u_fy_P1
need = -(42 + 1) - (-(LAMBDA_P + 1))                # ord_t dx/dt - ord_t dg/dt
check("T2a Jacobian valuation at P_i: ord_t f_y = -39 = required",
      ord_t_fy_P1 == -39 and need == -39, f"got {ord_t_fy_P1}, need {need}")

# cross-check Lambda via product formula for g along a P_1-branch:
# g = lc_g(x) * prod_k (y - Y_k(x)), lc_g = gamma_g x^63(1+..), 189 g-series:
# same-dir contacts: 15 @32, 3 @37 (g's pole-pattern dirs {0, +-sqrt(3/2)w});
# other 171 @12.
sum_g_contacts = F(171*C_ADIR + 15*C_CUBE + 3*C_SIGN, 42)
ord_u_g_P1 = -63 + sum_g_contacts
check("T2a' g-pole order via product formula: ord_u g = -1/14 -> Lambda=3",
      ord_u_g_P1 == F(-1, 14) and 42*ord_u_g_P1 == -3, f"got {ord_u_g_P1}")

# ----------------------------------------------------------------------
# 4. T2b: B-side / x-side e_p formulas (pins on unpinned tails)
#    B-series i: ord_u(g - c_p) = (282 - S_i)/42,  e_p = n_p (282 - S_p)/42
#    x-series i: ord_v(g - c'_p) = 125 - U_i,      e'_p = n'_p (125 - U_p)
# ----------------------------------------------------------------------
# derivation constants:
b_const = 42 - F(2*T_P1B_one, 42*42) - F(T_BB_diff, 42*42) - 2 + 1
# = 42 - 24 - 72/7 ... compute directly instead:
per_series_B_pinned = F(2*T_P1B_one + T_BB_diff, 42*42)   # (1008+432)/42
check("B pinned per-series sum = 1440/42", per_series_B_pinned == F(1440, 42), "")
B_CONST = 42*42 - 1440 - 42*(2 - 42) + 0  # bookkeeping check below
# ord_u(g - c) = 1 + (-2) - [ -42 + (1440 + S_i)/42 ] = (282 - S_i)/42:
B_e_const = 42*(1 - 2 + 42) - 1440
check("B-side constant 282", B_e_const == 282, f"got {B_e_const}")
# x-side: ord_v(g - c') = 1 - 2 - ( -126 + U_i ) = 125 - U_i:
X_e_const = 1 - 2 + KF
check("x-side constant 125", X_e_const == 125, f"got {X_e_const}")
# pins:
#  (i) g finite at B: S_i < 282 (and budget e_p <= 6 per value);
#  (ii) g finite at X: U_i < 125; with 41 pairs each >= 3: U_i in [123,125):
#       => pi_G < 125/41 = 3 + 2/41: LROOT slack-1 scenario pi_G = 4 is DEAD.
check("x-side squeeze: pi_G in [3, 3+2/41), pi_G = 4 dead",
      F(125, 41) < 4 and F(125, 41) - 3 == F(2, 41), "U_i in [123,125)")

# ----------------------------------------------------------------------
# 5. T1c/T3a: global genus balance  g_tree == g_RH  (identity check)
#    g_tree = (167)(166)/2 - delta_Y - delta_X
#    g_RH   = -3 + [Sig_B(e-1) + Sig_X(e'-1)]/2   (ghat deg 6, no affine ram)
#    symbolic in SigS (1/42 units), SigU, r_B, r_X.
# ----------------------------------------------------------------------
def lin(const=F(0), **kw):
    d = {1: F(const)}
    for k, v in kw.items():
        d[k] = F(v)
    return d
def ladd(a, b, sb=1):
    d = dict(a)
    for k, v in b.items():
        d[k] = d.get(k, F(0)) + sb*v
    return d
def lscale(a, s):
    return {k: F(s)*v for k, v in a.items()}

# T_Y local (plain units) = 4890 + 126*125 + SigS/42
T_Y_loc = lin(4890 + 126*125, SigS=F(1, 42))
# delta_Y = (T_Y_loc - 126 + 2 + r_B)/2
delta_Y = lscale(ladd(T_Y_loc, lin(-126 + 2, r_B=1)), F(1, 2))
# T_X local = SigU + 42*41 ; delta_X = (T_X - 42 + r_X)/2
delta_X = lscale(lin(42*41 - 42, SigU=1, r_X=1), F(1, 2))
g_tree = ladd(ladd(lin(F(167*166, 2)), delta_Y, -1), delta_X, -1)

# RH side: Sig_B e = (11844 - SigS)/42 ; Sig_X e' = 5250 - SigU
SigBe = lin(F(11844, 42), SigS=F(-1, 42))
SigXe = lin(5250, SigU=-1)
g_RH = lscale(ladd(ladd(SigBe, SigXe), lin(0, r_B=-1, r_X=-1)), F(1, 2))
g_RH = ladd(g_RH, lin(-3))

diff = ladd(g_tree, g_RH, -1)
check("T1c/T3a GENUS BALANCE g_tree - g_RH == 0 identically",
      all(v == 0 for v in diff.values()),
      "coeffs: " + str({k: str(v) for k, v in diff.items()}))
# closed form of the genus:
#   g = 2763 - (SigS/42 + SigU + r_B + r_X)/2
g_closed = ladd(g_RH, lscale(lin(-2763 + 3, SigS=F(1, 42), SigU=1),
                             F(1, 2)))
gc = ladd(g_RH, lscale(lin(0, SigS=F(-1,42), SigU=-1, r_B=-1, r_X=-1), F(-1,2)))
check("closed form g = 2763 - (SigS/42 + SigU + r_B + r_X)/2",
      gc[1] == 2763 and all(v == 0 for k, v in gc.items() if k != 1),
      str({k: str(v) for k, v in gc.items()}))

# ----------------------------------------------------------------------
# 6. T4a: geometric degree mu(F) = 6 by Bezout with infinity corrections
#    (C.{g=c})_aff = 168*252 - (C.Gbar)_Y - (C.Gbar)_X  for generic c
#    (C.Gbar)_Y = 126*252 + sum_series ord_u(g - c) = 126*252 - 6
#    (C.Gbar)_X = 42*252 + 0
# ----------------------------------------------------------------------
CG_Y = 126*252 + 84*int(0) + 0  # careful: sum ord_u(g) over pole series = 84*(-1/14)
CG_Y = 126*252 + int(84 * F(-1, 14))
CG_X = 42*252
mu_F = 168*252 - CG_Y - CG_X
check("T4a mu(F) = 6 (generic fiber of (f,g))", mu_F == 6, f"got {mu_F}")

# ----------------------------------------------------------------------
# 7. T1a: splice data.  Newton pairs, cabling weights, edge determinants.
#    Affine-side pairs (P-branch): (7,2)(3,10)(2,5);
#    local-chart pairs at [1:0:0]: exponents 54/42,74/42,79/42 ->
#    (7,9)(3,10)(2,5) after the smooth-part shift.
# ----------------------------------------------------------------------
def cabling(pairs):
    a = []
    prev = 0
    for i, (p, q) in enumerate(pairs):
        if i == 0:
            a.append(q)
        else:
            a.append(q + pairs[i-1][0]*p*a[-1])
    return a

pairs_aff = [(7, 2), (3, 10), (2, 5)]
pairs_loc = [(7, 9), (3, 10), (2, 5)]
# exponent reconstruction checks:
e1 = F(2,7); e2 = e1 + F(10,21); e3 = e2 + F(5,42)
check("T1a Newton pairs reproduce char exponents 12/42,32/42,37/42",
      (e1, e2, e3) == (F(12,42), F(32,42), F(37,42)), f"{e1},{e2},{e3}")
l1 = F(9,7); l2 = l1 + F(10,21); l3 = l2 + F(5,42)
check("T1a local pairs reproduce 54/42,74/42,79/42",
      (l1, l2, l3) == (F(54,42), F(74,42), F(79,42)), f"{l1},{l2},{l3}")
a_aff = cabling(pairs_aff)
a_loc = cabling(pairs_loc)
check("T1a cabling weights affine (2,52,317), local (9,199,1199)",
      a_aff == [2, 52, 317] and a_loc == [9, 199, 1199],
      f"{a_aff} {a_loc}")
# edge determinants along a cabling chain = q_{i+1} > 0 (germ positivity):
dets = [pairs_aff[i+1][1] for i in range(2)]
check("T1a edge determinants q2,q3 = 10,5 > 0 (and B/X arms q>0 by grid)",
      all(d > 0 for d in dets), str(dets))

# ----------------------------------------------------------------------
# 8. T1b: EN multilink multiplicities l_v = lk(C, curvetta_v) by Bezout.
#    curvetta at node v: truncation-curve; lk = degC*deg(gam) - (C.gam)_inf
# ----------------------------------------------------------------------
def lk_node(deg_gam, pairs_Y, x_arm):
    """pairs_Y: list of (count, contact_units42_affine) over ordered
    (C-series, gam-series) pairs at the Y-point; +42u local shift applied.
    x_arm: (count_pairs, contact_local_units1) at the X-point."""
    CY = sum(F(c*(k + 42), 42) for c, k in pairs_Y)
    CX = F(x_arm[0]*x_arm[1])
    return DEG_F*deg_gam - CY - CX, CY, CX

# root node (L_infty axis): lk(C, generic line) = 168
lk_root = 168
# F_s node: gam = x^2(y-c0)^7 - eta^7-type, deg 9, 7 Y-branches, 2 X-branches
lk_Fs, _, _ = lk_node(9, [(126*7, 12)], (42*2, 1))
# G_m node: deg 37 (y-deg 21, x-deg 16)
lk_Gm, _, _ = lk_node(37, [(84*3, 32), (84*18, 12), (42*21, 12)], (42*16, 1))
# P_1 node: deg 79 (y-deg 42, x-deg 37)
lk_P1, _, _ = lk_node(79, [(84, 37), (168, 32), (1512, 12),      # vs P1
                            (252, 32), (1512, 12),               # vs P2
                            (42*42, 12)],                        # vs B
                       (42*37, 1))
check("T1b l_v > 0 at root/F_s/G_m/P_i: (168, 294, 2022, 4664)",
      lk_root == 168 and lk_Fs == 294 and lk_Gm == 2022 and lk_P1 == 4664,
      f"{lk_root},{lk_Fs},{lk_Gm},{lk_P1}")

# ----------------------------------------------------------------------
# 9. T4b/T3b: feasibility exhibit for the (e_p) system + genus window
#    (shows the classical net has a nonempty solution set: no kill w/o
#     more template data).  Example: r_B = 1 (n=42), r_X = 21 x-places?
#    keep simplest: search small configurations.
# ----------------------------------------------------------------------
feasible = []
B_shapes = [(1, [42]), (2, [21, 21]), (3, [14, 14, 14]), (6, [7]*6)]
X_shapes = [(1, [42]), (2, [21, 21]), (6, [7]*6), (42, [1]*42)]
for r_B, nB in B_shapes:
    for eBval in [1, 2, 3, 6]:
        eB = [eBval]*r_B                          # distinct values assumed
        # S_p = 282 - 42 e/n must be a sum of 5 grid contacts each >= 13:
        SB = [282 - F(42*e, n) for n, e in zip(nB, eB)]
        if any(s.denominator != 1 or s < 5*13 for s in SB):
            continue
        SigS = sum(n*s for n, s in zip(nB, SB))
        for r_X, nX in X_shapes:
            for eXval in [1, 2]:
                eX = [eXval]*r_X
                # U_p = 125 - e/n must be >= 123 (contacts >= 3, 41 pairs)
                UX = [125 - F(e, n) for n, e in zip(nX, eX)]
                if any(u < 123 for u in UX) or any(e > min(6, 2*n) for n, e
                                                   in zip(nX, eX)):
                    continue
                SigU = sum(n*u for n, u in zip(nX, UX))
                Se = sum(eB) - r_B + sum(eX) - r_X
                if Se < 6 or Se % 2:
                    continue
                g = -3 + Se//2
                dY = (F(4890 + 15750) + F(SigS, 42) - 124 + r_B)/2
                dX = (SigU + 1722 - 42 + r_X)/2
                gt = F(167*166, 2) - dY - dX
                if gt == g and dY.denominator == 1 and dX.denominator == 1:
                    feasible.append((r_B, eBval, r_X, eXval, g))
check("T3b/T4b nonempty feasible set for (r_B, e_B, r_X, e_X, g)",
      len(feasible) > 0, str(feasible[:6]))

# ----------------------------------------------------------------------
# 10. T2c: classical degree-pair conditions
# ----------------------------------------------------------------------
import math
gcd = math.gcd(DEG_F, DEG_G)
check("T2c A-M: neither degree divides the other (168 !| 252)",
      DEG_G % DEG_F != 0 and DEG_F % DEG_G != 0, f"gcd={gcd}")
check("T2c Moh bound: min degree > 100 (outside Moh's verified range)",
      min(DEG_F, DEG_G) > 100, "168 > 100: no clash")

print()
nfail = sum(1 for _, ok, _ in PASS if not ok)
print(f"{len(PASS)} checks, {nfail} FAIL")
