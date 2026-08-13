# SHEET6-DIRECTIONB.md — the J-jet strike at the resonant direction b

Status: COMPLETE + REVIEWED WITH CORRECTIONS (SHEET6-DIRECTIONB-REVIEW.md,
3-referee: F1 chart identity CONFIRMED, re-derived from scratch; F2
dead-stretch blindness CONFIRMED — including at random NONZERO
dead-stretch values, primes 314329/521137/200257/400849, a test the
strike's own numcheck never ran — with the MECHANISM corrected to the
2:3 orbit-cancellation (the §2b pairing story is heuristic, does not
cover the B-channels); F3 Row_20 CONFIRMED (all 18 coefficients
independently re-extracted; 8 ratios pairwise-distinct 28/28; the
eta^0 row already gives 0 = -42 with no need of w != 0); F5 the kill is
E5-independent and scale-free; F4 the "kills the banked R1 witnesses"
corollary RETRACTED as wrong-object — the banked witnesses carry
tf1/2_47, tf1/2_52 != 0 (window slots 15/20), OUTSIDE this stratum;
they were already dead via R1 §18.1 saturation. Corrections applied in
place, marked [REVIEW].) (2026-08-12.) Target: the L1 §7.2
coefficient layer at the residue-A merge (TEMPLATE-ATTACK §7 frontier;
Grok J-jet proposal xmodel/grok-eval-20260812.md item 3). Engines:
cases/directionb_strike.py (NEW, additive; reuses
cases/r1_experiment.py chart machinery READ-ONLY via import) +
cases/directionb_numcheck.py (NEW, independent verifier, zero shared
code). Gauges as SHEET6-R1 §3.0: a = 0, x0 = 0, S_R = G_R = 1 (s0 = 1),
A = 1, eta_A = 1, sigma = 6 (a1 = 3+sqrt3, a2 = 3-sqrt3, b = 4,
b2 = 9/2, B = 3/2).

HEADLINE: (1) NEW exact formulation: J(f,g) = 1 in the G_m chart is a
graded row family whose k = 0..41 orders are PURE y-side data, with a
single inhomogeneous row at chart slot 20 = the h1-resonance = the
b-direction window (§0); equivalently (Theorem J1, §2b) the whole
Jacobian condition is an h1-log-derivative transport law along the
joint tree — L1 §7.2's "global h1-accounting at b" IS the Jacobian
closure. (2) GATE: E5/E6/E7-anchored top identities reproduced (4/4).
(3) MEASUREMENT (exact, triple-prime-verified): the J-window through
slot 20 is structurally BLIND to the 7 dead-stretch coefficients;
Row_20 is a 9-component tau-covariant system loaded entirely on
(alpha_1 w_1^4, alpha_2 w_2^4) with 8 pairwise-disagreeing homogeneous
ratio pins + the nonzero inhomogeneity. (4) THEOREM: the zero-tail
(zero-extension) locus of the residue-A template is DEAD at the
J-tier, char 0, uniformly in all 7 dead-stretch coefficients — every
surviving configuration carries forced-nonzero sub-pattern tails
inside the slot-20 window. (5) The quantum V(b)-shift lands on exactly
this window; separation statement in §4.

## 0. The J-jet identity (new formulation; exact, printed-tier-free)

G_m chart: t = x^{-1/42}, y = P(t) + eta t^32, P = t^12 + uf18 t^18 +
uf24 t^24 + uf30 t^30 (the prefix arc through direction d0 = 1; the
three suffix dead-stretch coefficients at levels 18/24/30 = 9/21, 12/21,
15/21). Branch products give, with x-side leads phi_f, phi_g (deg 42, 63):

    f - a = c_f t^{-12} Phi(t,eta) (1 + O(t^42)),
    g     = c_g t^{-18} Gamma(t,eta) (1 + O(t^42)),

(t^{-12} = x^{2/7} = d_F(G_m), t^{-18} = x^{3/7} = d_g(G_m): the E7
ladder), Phi = sum_s F_s(eta) t^s, Gamma = sum_s G_s(eta) t^s, F_0 =
S_M P2(eta), G_0 = G_M P3(eta) (P2 = [(eta^3-a1)(eta^3-a2)]^2, P3 =
[...]^3; E6 leads S_M = 7^12/2^6, G_M = -7^18/2^9). The chart Jacobian
is d(x,y)/d(t,eta) = -42 t^{-11}, so J(f,g) = 1 reads EXACTLY

    (t Phi_t - 12 Phi) Gamma_eta - Phi_eta (t Gamma_t - 18 Gamma)
        = -(42/(c_f c_g)) t^20.                                   (J)

Row k (coefficient of t^k, a polynomial identity in eta):

    Row_k:  sum_{i+j=k} [(i-12) F_i G_j' - (j-18) G_j F_i'] = 0
            (k != 20),   and = -(42/(c_f c_g)) != 0 at k = 20 (eta^0).

Structural facts (all verified in the engine):
1. X-SIDE WINDOW: phi_f, phi_g enter only at t^{42} (elementary
   symmetric functions of the 42/63 x-roots ride t^{42m}), so rows
   k = 0..41 are PURE y-side data — the first 41 orders of the J-closure
   (R5) ARE expressible from the y-side model, contrary to the R1-era
   reading that deferred all of J to the x-side build.
2. RESONANCE AT SLOT 20: the inhomogeneous row sits at k = 20 = the
   eta-offset (32-12) of the chart = EXACTLY the cancellation depth at
   which h1 = g^2 - s0 f^3 surfaces at G_m (level -36 -> -16, i.e.
   d_h1 = 8/21), whose pattern H_M eta P2 (eta^3 - b) carries the
   resonant direction b. The Jacobian inhomogeneity, the h1-window top,
   and the quantum divergence V(b) != 0 (TEMPLATE-ATTACK 1c.2) all sit
   at the SAME chart order. This is the precise coefficient-tier
   coordinate of the L1 §7.2 layer.
3. Row_0 == 0 identically for ANY leads (F_0, G_0) = (S_M P2, G_M P3):
   -12 F_0 G_0' + 18 G_0 F_0' = 6 S_M G_M (-2 P^3 (P^2)' + 3 P^2 (P^3)')
   ... = 0 — the top-order gate (promoted record reproduced).

## 1. Gate status: PASS (4/4)

Engine phase `gate` (2026-08-12): E6 slot-0 leads reproduced (f-jet =
S_M[(e3-a1)(e3-a2)]^2, g-jet = G_M[...]^3, S_M = 7^12/2^6, G_M =
-7^18/2^9); E1/tower G_0^2 - F_0^3 = 0 identically (h1 drops to slot
20); Row_0 == 0 identically. The chart expansion reproduces the
promoted top-order identities BEFORE any new order is read.

## 2. First measurement (D = 7, ALL frees symbolic, exact to k = 6)

**Rows 1-5 vanish IDENTICALLY — as polynomials in ALL free template
data** (7 dead-stretch coefficients + all B-side and P-side tails, exact
arithmetic, sentinel-free at VDEG_CAP = D). Row_6 is the first
nonvacuous J-order: 10 eta-components (n = 2, 5, ..., 29, all n == 2
mod 3), each with ZERO constant part, loading ONLY:
  - linear: tf1_38, tf2_38, tg1_38, tg2_38, tg01_38, tg02_38 (the
    slot-6 f-vs-g tail mismatches on the P_i arcs),
  - weight-6 monomials in the B-side tails (bf_13..18, bg42_13..18,
    bg21_14/16/18; slot-weight exactly 6 in every monomial).

**The 7 dead-stretch coefficients (uf18, uf24, uf30, vf1_34, vf1_36,
vf2_34, vf2_36) are ABSENT from every J-row through k = 6** — not
"linear at the first non-constant order" (Grok item 3's geometry is
refuted as stated): they cancel structurally. [REVIEW F2: the
blindness FACT is confirmed — including by direct evaluation at
random NONZERO dead-stretch values at four further primes — but the
"joint-tree pairing" story below is HEURISTIC only (it does not cover
the B-channels); the verified mechanism is the reviewers' 2:3
orbit-cancellation (sufficiency checked).] Heuristic picture: J
depends on branch data through log-derivatives of pairwise DIFFERENCES
z_j - y_i (f = phi_f prod(y - y_i), g = phi_g prod(y - z_j) gives
J = fg[sum_j c_j/(y-z_j) - sum_i d_i/(y-y_i)], c_j, d_i =
log-derivative sums of (z_j - y_i)); coefficients SHARED between f-
and g-arcs riding the same tree edge (uf, vf — forced shared by the
E7 exact d_g ladder) cancel in low-order differences. What the first
J-orders see is the data the joint tree does NOT pair: the f-vs-g
tail splits (tf vs tg) and the B-cluster tails.

Row_6 solved exactly (phase `solve6`): flattening the 10 eta-components
over the radical-monomial basis gives 78 K3-rows on 31 var-monomial
columns, rank EXACTLY 8 — eight new J-tier conditions, all homogeneous
(zero-extension survives), pinning 8 g-side B-cluster/0-direction tail
functionals (bg21/bg42-monomials, tg01_38, tg02_38) against the free
f-side data. Pivot set is tau/pole-swap symmetric (tg01/tg02 enter
symmetrically; all coefficients in Q(zeta42, eta_B): no sqrt3 — the 1c.1
covariance checksum PASSES). Deep degeneracy 78 -> 8 = the orbit
covariance at work.

Frozen-stratum probe (phase `dsys`, all tails and B-frees pinned 0,
only the 7 dead-stretch coefficients free): rows k = 1..10 vanish
IDENTICALLY (D = 11 run; includes the w-mismatch orders k = 5, 10 —
the slot-5 w_i / hw_i / 0-direction data cancels too). Engagement of
the 7, if anywhere, is at the resonance window k <= 20: D = 21 run
below.

## 2b. Theorem J1 (the J-identity IS h1-transport along the joint tree)

With f - a = phi_f(x) prod_i (y - y_i(x)) (EXACT: deg f = 168 = 126+42
puts x^42 y^126 on the Newton polygon, so the y-lead of f - a is
phi_f(x), deg 42; same for g with phi_g, deg 63), a two-line partial-
fraction computation gives the EXACT identity

  J(f,g) = fg [ sum_j (log f(x,z_j))' / (y - z_j)
              - sum_i (log g(x,y_i))' / (y - y_i) ],

(z_j = g-branches; the phi'/phi terms reassemble into the logs). Since
J - 1 has y-degree < 126+189 and the 315 branches are distinct,
J(f,g) = 1 is EQUIVALENT to the 315 per-branch x-series identities

  (d/dx) g(x, y_i(x)) . f_y(x, y_i(x)) = -1     (126 f-branches)
  (d/dx) f(x, z_j(x)) . g_y(x, z_j(x)) = +1     (189 g-branches)

— the R5 "J-closure" reduced to y-side data + the two x-side leads.
Along f-branches h1 = g^2 - s0(f-a)^3 restricts to g^2, along
g-branches to -s0(f-a)^3, so these read

  (log h1)'|_{y_i} . (g f_y)|_{y_i} = -2,
  (log h1)'|_{z_j} . (f g_y)|_{z_j} = +3 :

**the Jacobian condition at this configuration is EXACTLY a global
h1-log-derivative transport law along the joint tree** — L1 §7.2's
"h1-branch accounting at the resonant direction" is not an analogue of
the missing kill, it IS the Jacobian closure. The J-jet rows of §0 are
the graded pieces of these identities at G_m; the first order at which
they see the through-cluster interior data is the h1-window top
(slot 20), where (eta^3 - b) surfaces — consistent with the observed
identical vanishing of rows 1..10 on the frozen stratum and with ALL
dead-stretch discriminating power sitting at/above the resonance
window. [REVIEW F2: this reading is heuristic; the proof-grade
mechanism for the blindness is the reviewers' 2:3 orbit-cancellation,
banked in SHEET6-DIRECTIONB-REVIEW.md with a sufficiency check. The
identity J1 itself and the per-branch equivalence are CONFIRMED (F1).]

## 2c. The depth-21 measurement: the J-window is dead-stretch-BLIND
## and lands 9-on-2 on the pole scales

Frozen stratum (ALL tail/B-side frees = 0; the 7 dead-stretch
coefficients SYMBOLIC; w_1, w_2 symbolic ring radicals), chart depth
D = 21, exact, sentinel-free:

- **Rows 0..19 vanish IDENTICALLY as polynomials in the 7** (engine
  phase `dsys`; the 7 never appear).
- **Row_20 has exactly 9 eta-components (eta^0, eta^3, ..., eta^24),
  NONE containing any of the 7**, each a constant of the exact form

      Row_20[eta^n]:  c1[n] . (alpha1 w1^4) + c2[n] . (alpha2 w2^4),
      c2[n] = tau(c1[n])   (tau-covariant conjugate pairs, 1c.1 PASS),

  and the J-identity demands Row_20 = -(42/(c_f c_g)) . eta^0, RHS
  nonzero unconditionally (c_f, c_g = the y-lead constants of f - a, g;
  the S_R = G_R = 1 gauges make them 1, but only nonzeroness is used).

The system on X_i = alpha_i w_i^4 (exact K3 values banked in
/tmp/directionb_dsys.pkl and in phase `w4` output):

  eta^3 :  X1/X2 = (266 + 153 r3)/23        eta^15: (136226 - 77815 r3)/19799
  eta^6 :  X1/X2 = (9926 + 5723 r3)/517     eta^18: (6998 - 1541 r3)/6469
  eta^9 :  X1/X2 = -(602 + 345 r3)/73       eta^21: (86 + 35 r3)/61
  eta^12:  X1/X2 = -(133 + 44 r3)/109       eta^24: -1

Eight PAIRWISE-DISAGREEING ratio pins (already eta^3 vs eta^6 has
nonzero determinant): the homogeneous block has rank 2 on 2 unknowns,
forcing X1 = X2 = 0; then eta^0 reads 0 = -42/(c_f c_g). Both ends are
absurd: w_i != 0 is template-forced (2c-E5 lead, Prop 5.3
squarefreeness of the pole pattern), and the RHS is nonzero for every
Jacobian pair.

VERIFICATION (adversarial, independent path): the entire computation
re-run as a DIRECT product of all 315 branch factors over
F_p[eta,t]/(t^21) — plain modular integers, all radicals instantiated
as field elements, zero shared code (cases/directionb_numcheck.py).
At p = 105337, 105673 (the campaign's banked primes) and 200257:
rows 0..19 vanish exactly; Row_20(eta) equals the banked exact
constants coefficient-for-coefficient (all 40 eta-slots). PASS x3.

## 3. Verdict

**THEOREM (J-tier zero-extension kill; char 0, exact).** In the
residue-A td = 6 genome there is NO polynomial pair (f, g), J(f,g) =
const != 0, whose y-side branch data has all free tail/B-side
coefficients in the G_m window (chart slots 1..20) equal to zero —
for ANY values of the 7 on-lattice dead-stretch coefficients uf18,
uf24, uf30, vf1_34, vf1_36, vf2_34, vf2_36. The J-jet Row_20 forces
alpha_i w_i^4 = 0 (8 exact, pairwise-independent homogeneous rows on
2 unknowns) and simultaneously 0 = -42/(c_f c_g). Uniform in the 7;
no saturation subtleties (the kill is direct — no Rabinowitsch rows,
no forced-nonzero-scale bookkeeping; [REVIEW F3] the eta^0 row alone
closes it without even using w != 0). [REVIEW F4: scope precision —
this stratum is the PURE-DEAD-STRETCH sector. The banked R1 witnesses
(SHEET6-R1 §13.4/§16) are NOT in it: they carry tf1/2_47, tf1/2_52
!= 0 (window slots 15/20); those died via the §18.1 saturation
mechanism, a different object. The two kills are complementary, not
nested.]

Adjudication of the three pre-registered outcomes:
- NOT "INCONSISTENT on the dead-stretch grid" as Grok item 3 posed it:
  the J-jet's first 20 orders are structurally BLIND to the grid
  ([REVIEW F2] verified fact; mechanism = 2:3 orbit-cancellation);
  the grid coefficients enter the window
  only multiplied by tail data (cross-terms), never linearly.
- INSTEAD: **INCONSISTENT one level down** — the window is
  overdetermined 9-to-2 on the pole scales (w_1^4, w_2^4), and kills
  the entire zero-tail locus outright.
- The dead-stretch grid itself: UNDETERMINED BY J AT THIS WINDOW —
  honest characterization: no J-datum through slot 20 constrains the
  7; every constraint they satisfy at this tier comes from the R1
  band/quotient ladder, not from J.

SCOPE, stated precisely: the kill covers the stratum {all P-side tails
tf*/tg* (levels 38..52), all B-side frees bf/bg* (levels 13..32) = 0}
of the template variety, uniformly in the 7 + both w 4th-root branches
+ every A-embedding (the ratio contradiction lives in Q(sqrt3)).
Every surviving residue-A configuration MUST carry nonzero
sub-pattern tail data inside the slot-20 window — the direction-b
window is now a FORCED-NONZERO-TAIL regime. This composes with the
§19.2 stratum kill (survivors need a nonzero free below slot 13,
proof-tier on the UU chart) into: the residue-A survivor locus is
pushed off every zero-extension in two independent row systems
(h1-band tier AND J-tier).

## 4. The quantum transfer (derivation + honest implication direction)

Datum (TEMPLATE-ATTACK 1c.2/S3, computational core verified 3/3): at the
residue-A merge the first Moyal correction is parameter-free, V(t) =
Pi^3(f_top, g_top), deg 9, p | V (V(a_i) = 0), V(b) = -878 sigma^9/9261
!= 0; quantum-R1 = classical-R1 + (1/24) p.W; the (2,3)-entries are
exactly quantum-critical (D_crit = D_F + D_g - 3 kappa-bar = 0).

In the J-jet frame of §0 this becomes an exact statement about ROWS:
the Weyl-pair identity [F,G] = 1 has symbol expansion {f,g} +
(1/24) Pi^3(f,g) + (higher) = 1. D_crit = 0 at the residue-A merge
means the chart order of Pi^3(f,g) relative to {f,g} is EXACTLY the
classical window height: the correction lands on the SAME slot-20 row
family as the classical inhomogeneity (J)'s -42/(c_f c_g), shifted
entirely into the b-root column of the h1-window (p | V kills the
a_i-columns). So:

  QUANTUM Row_20 = CLASSICAL Row_20 + (1/24) V-column,
  V-column = 0 at the pinned handoffs a_i, = -(1/24).878 sigma^9/9261
             != 0 at the resonant direction b,

and every other row family is correction-free (corrections land 2
kappa-bar below their window tops — the S3 shield). TRANSFER:

(i) IF the classical slot-20 layer closes with zero slack (i.e. the
    b-column functional of the slot-20 system is FORCED = 0 on every
    template-conform solution — which is what a zero-slack classical
    closure of L1 §7.2 means in these coordinates), THEN the quantum
    layer is strictly infeasible: the same forced functional must equal
    the nonzero constant -(1/24)V(b). No Weyl-algebra pair with
    [F,G] = const has residue-A-conform symbol data.
(ii) DIRECTION, with total honesty: the known implication is
    JC_2 => DC_1 (Tsuchimoto / Belov-Kanel--Kontsevich: JC_{2n} =>
    DC_n; plus DC_n => JC_n trivially by symbols). A JC_2
    counterexample is NOT required to lift to A_1: quantum
    infeasibility of the template does NOT kill residue-A. What (i)
    proves is a SEPARATION: if residue-A algebraizes, the resulting
    (f,g) is a Jacobian pair whose Weyl lift is obstructed at first
    order, and the obstruction is concentrated at the single direction
    b — the same coordinate every classical attack converges on. This
    is evidence + delimitation (no quantum-tier kill exists; no
    classical-vertex kill exists; the discriminating datum is the
    slot-20 b-column), not a proof of death.
(iii) What WOULD make it bite: (a) the classical zero-slack closure of
    the slot-20 layer itself (the J-Row_20 build below is the missing
    row family), PLUS (b) a transfer theorem forcing Weyl-liftability
    of (a deformation of) any minimal JC_2 counterexample — (b) is
    open; it is exactly the JC_2 <=> DC_1 gap. We state (b) as the
    precise missing lemma rather than claim the chain bites.

RIDER after the §3 theorem: on the zero-tail locus the classical
slot-20 window is now INFEASIBLE outright, so the quantum statement is
vacuous there (both layers dead). The live content of the transfer
moves WITH the survivor locus: on any tail-loaded solution locus, the
classical Row_20 pins a tail/w^4-functional to -42/(c_f c_g) while the
quantum row pins the SAME functional to -42/(c_f c_g) - (1/24)V(b)
(the V-column is concentrated in the b-block: p | V); the difference
-(1/24)V(b) = 878 sigma^9/(24.9261) != 0 is FIXED and
parameter-free. So classical-conform and quantum-conform template data
can never coincide — the separation of §4(ii) holds on every stratum,
now anchored at a window whose classical half is measured (9-on-2
overdetermined) rather than hypothesized.

## 5. Consequences for the 10 residue-A panels + 6 sibling templates

What parameterizes (frame-homogeneity): the chart identity (J) used
NOTHING template-specific except the three integers (e_f, e_g, off) =
(kappa d_F, kappa d_g, kappa(pi_P - pi_Gm) offset) = (12, 18, 20) and
the joint-tree orbit model. For ANY merge cell IIa(r, l, .)/ZCH with
pole level pi_P, merge level pi_Gm, chart t = x^{-1/kappa_P}:

    (t Phi_t - e_f Phi) Gamma_eta - Phi_eta (t Gamma_t - e_g Gamma)
        = -(kappa_P / (c_f c_g)) t^{off},

off = the eta-offset of the chart; rows k < min(off, kappa-lattice) are
pure y-side and homogeneous; the inhomogeneity sits at k = off = the
h1-resonance of that cell (level arithmetic: e_g/e_f = d_g/d_F = 3/2
for every (2,3)-type cell makes 2 e_g - 3 e_f = 0, so the g^2 - f^3 top
cancels and h1 surfaces exactly at the offset). Theorem J1 holds
verbatim for every template in the book (only the factorization form
and the h-tower exponents enter): for each of the 7 classes / 23 live
instances the J-closure is the corresponding h-tower log-transport law.
So: (i) the J-jet row machinery transfers to all 10 residue-A panels
unchanged (same merge genome, same chart); the §3 zero-extension kill
is a statement about the shared genome and propagates to every
residue-A panel by frame-homogeneity. (ii) For the @w4/@w3/@w2
siblings (231@w4, 271@w4, 251@w3, 351@w2, 471@w2, ZCH@w6) the rows
parameterize by (e_f, e_g, off) and the cell's own pattern
polynomials — the row builder needs only each cell's
build_generators analogue; whether their resonance windows are also
overdetermined on the pole scales is the natural next run (NOT
claimed here). (iii) The forced-nonzero-tail regime composes with the
banked R1 record: every residue-A survivor now needs BOTH a nonzero
free below slot 13 (SHEET6-R1 §19.2, proof-tier stratum) AND nonzero
window tails at the J-tier — the two systems (h1-band and J) are
independent row families on the same unknowns, and their JOINT
depth-84-with-J-rows build is the sharpest next object in the
program (spec: §6).

Retro-diagnosis of the R1 record [REVIEW F4: CORRECTED — the original
"every banked witness was a zero-extension" claim was wrong-object]:
the banked witness families (SHEET6-R1 §13.4/§16) carry tf1/2_47,
tf1/2_52 != 0 and live OFF this stratum; their kills came from the
§18.1 saturation mechanism, not from these rows. What survives of the
diagnosis: the J-closure (R5) was recorded as "not expressible from
y-side data" and so was never imposed in ANY R1 object; §0's
x-side-window observation shows the first 41 J-orders were
y-side-expressible all along, and they carry an overdetermined
row family (9-on-2 at slot 20) that no banked system contained. The
"receding discriminant" phenomenology (Grok stress-test A) is
PARTIALLY resolved: a genuinely new, independent row family existed
one tier down at the single window every diagnostic pointed to —
residue-A itself remains open on the forced-tail locus.

## 6. Ledger, trust perimeter, reproduction, next objects
[build resumed 2026-08-13 (retry, prior attempt died at startup): 83-var forced-nonzero-tail window build, phase `tails`]

### 6.T The 83-var forced-nonzero-tail window build (analysis, 2026-08-13)

Builder banked /tmp/directionb_tails.pkl (D = 21, 2998.7s, exact,
sentinel-free; copy /tmp/directionb_tails_D21.pkl). Analysis engine:
cases/directionb_window.py (phases gate | bands | slot20 | verdict |
claim4).

GATE (17/17 PASS = 13 window checks + the 4 relayed strike anchors,
which the strike gate itself re-runs 4/4; directionb_window.py gate):
tails -> 0 kills rows
6..18 term-by-term (every monomial tail-loaded); Row_20's const part
== the banked zero-tail system coefficient-for-coefficient (all 9
eta-comps; the extra eta^27 comp is pure-tail); the 9-on-2 block and
the 0 = -42/(c_f c_g) contradiction re-derived from the tails state
itself; E5/E6 anchors + E1 tower + Row_0 (strike gate) 4/4; RHS42
certified against the chart-Jacobian constant (x_t y_eta = -42
t^-11 => LHS + 42 = 0 at c_f c_g = 1) with a no-scalar-const check
on both banked eta^0 consts, so the -42 enters exactly once and a
silent edit of RHS42 now breaks the gate [REVIEW 2026-08-13,
Grok F3].

BAND LEDGER, rows 6..19 (odd rows + Row_7..19-odd identically 0;
`directionb_window.py bands`, 11s). Two tiers per band. Tier S =
the pre-registered "Row_6-type" split (radical monomials as free
K3-module basis; structural census). Tier V = the VERDICT tier:
one row per eta-component over the etale algebra E = K3[a1,a2,mu]/
(a1^3-(3+r3), a2^3-(3-r3), mu^2-3/2), h_i |-> s_i mu w_i per h-sign
branch (s1,s2), w-monomials kept as explicit column weights; Gaussian
elimination with UNIT pivots only (norm != 0 <=> invertible in every
field factor), so each band's echelon rows are an exact generating
set of its conditions on EVERY branch of the radical tower.

  band | eta | tier S rows x cols -> rank | tier V rank over E (x4 branches)
   6   |  9  |  18 x    6 -> 2   |  1
   8   | 10  |  48 x   18 -> 6   |  4
  10   | 10  |  63 x   48 -> 16  |  6
  12   |  9  | 113 x  127 -> 40  |  7
  14   | 10  | 191 x  292 -> 74  | 10
  16   | 10  | 321 x  628 -> 111 | 10
  18   |  9  | 451 x 1341 -> 173 |  9

Tier V ranks IDENTICAL on all 4 h-sign branches; NO unreduced
leftover rows anywhere => 47 exact polynomial conditions per branch
(banked: /tmp/directionb_window_conditions.pkl). NO tail is pinned
to 0: already Row_6 has E-rank 1 on its 6 level-38 tails (the
zero-tail cascade DIES at the first band); sample clean conditions:
  C6.1:  [(-3/2-r3/2) a1^2 a2] tf1_38 - 3 tf2_38 + [(1/2+r3/6) a1^2 a2] tg01_38
         + tg02_38 + [(1+r3/3) a1^2 a2] tg1_38 + 2 tg2_38 = 0
  C10.6: -(3/2)(tf1_42+tf2_42) + (1/2)(tg01_42+tg02_42) + tg1_42 + tg2_42 = 0
  C16.10: (3/184)(tf1_48+tf2_48) - (1/184)(tg01_48+tg02_48)
          - (1/92)(tg1_48+tg2_48) + (6 nonlinear terms) = 0
The 7 dead-stretch coefficients enter ONLY in tail cross-terms
(J-blindness persists with tails on).

SLOT-20, THE INHOMOGENEOUS TAIL CONDITION (`slot20` phase). With
tails on, X_i = alpha_i w_i^4 is NO LONGER a free unknown (it is the
pole-scale value); Row_20 reads, per eta-component,

  [w4-block const](eta^n) + sum_j c_j(eta^n) . tail_j
      + (quadratic tail cross-terms) + 42.[n = 0] = 0,

i.e. the promoted 0 = -42 becomes: THE TAILS MUST CANCEL THE -42 AND
the w4-block, in all 10 eta-components simultaneously.

Stratum S = the 16 tails entering Row_20 LINEARLY (levels 42/47/52).
Exact structural facts (checked): bands 6,8,12,14,16,18 vanish
IDENTICALLY on S; Row_10|S is linear in the six level-42 tails;
Row_20|S = const + linear(S) + 21 quadratic monomials in level-42.

FIRST SUB-STRATUM (level-42 = 0, unknowns = the 10 level-47/52
tails), solved exactly over E for h-signs (+-,+-) x pole scales
w = (1,1), (2,3), (1/5,7):
  Row_10|S rank 2/6 (level-42 NOT pinned: 4 free directions);
  Row_20 linear map on the 10 level-47/52 tails has RANK ONLY 4 of
  10 eta-rows, uniformly in every branch and every w-sample, and the
  inhomogeneous target is NOT in its image:
  **INCONSISTENT, with residual defect exactly in eta^12, 15, 18,
  21, 24, 27** (6 obstruction components).
So the -42 CANNOT be cancelled by slot-20-linear tails alone: any
survivor must carry DEEPER tail loading (levels 38..46 cross-terms
and/or the level-42 quadratic block). Escalation below.

WHICH TAIL COMBINATIONS CANCEL THE -42 (the eta^0 row, exact
support): Row_20[eta^0] carries 2034 tail monomials -- 14 of tail-
degree 1 (levels 42/47/52), 184 of degree 2, 532 of degree 3 (e.g.
tf1_38.tf1_38.tf1_40, tf1_38.tf1_39.tf1_39, tf1_38.tf1_39.vf1_34),
up to degree 8. The eta^0 equation ALONE is easily solvable (already
the 14 linear ones suffice); the kill pressure is NOT at eta^0 --
it is the SIMULTANEITY across the other 9 eta-components. Precisely,
the level-47/52 linear map has rank 4, and the residual obstruction
sits in the 6 components eta^12, 15, 18, 21, 24, 27.

## 6.V VERDICT — **PROMOTED 2026-08-13 after dual review + repair**
(Grok hostile replay: SOUND-WITH-ERRATA, xmodel/grok-directionb-review.md;
internal referee: SOUND-WITH-ERRATA + engine repair, SHEET6-DIRECTIONB-
REVIEW.md R1 + R1.6; all errata applied; harness green: gate 17/17,
slot20 27/27, verdict 24/24 across all 4 h-branches + extra fiber,
claim4 6/6.)

Decisive tests (`directionb_window.py verdict`, 24/24 PASS, 451 s;
all exact over E. [REVIEW 2026-08-13] tests (1)(2) are now
harness-certified on all 4 h-sign branches at w = (1,1) AND on
branch (+,+) at w = (2,3), with an explicit dims/ranks/verdicts
identity check across the 5 fibers -- previously one fiber ran and
"ranks identical on all 4" was doc-only; both review replays also
confirm it, adding w = (1/5,7). Strata (3) run on the default fiber;
(3a) is additionally 12-combo-certified by `slot20`):

(1) LINEARIZATION RELAXATION (every var-monomial an INDEPENDENT
    unknown -- an OVER-approximation of the true solution set, so
    INCONSISTENT here would prove EMPTY outright):
      Row_20 alone : 10 rows x 2718 monomial cols, rank 10 -- CONSISTENT
      full window  : 77 rows x 5106 monomial cols, rank 57 -- CONSISTENT
      (identical dims/ranks/verdicts on every certified fiber)
    The -42 target IS in the column span. **There is NO linear-algebra
    kill of the forced-tail window.** Precisely [REVIEW 2026-08-13]:
    no E-LINEAR functional of these 77 depth-21 rows, on any
    certified (h-branch, w) fiber, annihilates all tail columns while
    detecting the -42 -- the exact mechanism that killed the
    zero-tail stratum (9-on-2 on the pole scales) has no analogue
    once tails are on.  NOT excluded by this tier: nonlinear /
    Groebner-tier combinations of the 47+1 conditions, rows k >= 21,
    and the unfrozen B-side -- exactly the escalations the burden
    moves to below.

(2) THE DIFFERENTIAL at the zero-tail point (tail-degree <= 1 part;
    the promoted theorem's point is the origin of this system):
    77 rows x 76 tail cols, rank 29, INCONSISTENT -- at the all-zero
    AND at a generic dead-stretch sample, on every certified fiber
    (harness), and rank-29-stable inconsistent on 4 further hostile
    dead-stretch samples (a 2nd rational point, a mixed-E value, the
    uf18-axis, ds = 0 at w = (2,3)) in the review replays.  Honest
    scope [REVIEW 2026-08-13]: this is SAMPLED rank-stability, not a
    closed-form identity in the 7 -- the differential genuinely
    moves with them (20488 tail x dead-stretch cross-terms over 67
    of the 77 rows), and uf30 is a dummy (absent from every window
    monomial: 6 genuine parameters + 1). So the -42 is NOT
    cancellable to FIRST ORDER at any tested point: the survivor
    locus does not meet the first-order deformations of the
    zero-tail point there. This is the exact sense in which the
    promoted kill "almost" propagates.

(3) EXACT AFFINE STRATA (all solved in closed form over E; in (3b)
    and (3c) the 7 enter as PARAMETERS fixed at a generic sample,
    not as unknowns):
      levels 47/52 only          : 10 eqs, 10 unk, rank 4  -- INCONSISTENT
      levels 45/47/50/52 + the 7 : 19 eqs, 20 unk, rank 8  -- INCONSISTENT
      levels >= 43 (low tails 0) : 48 eqs, 50 unk, rank 16 -- INCONSISTENT
    (mechanism of the third, corrected [REVIEW 2026-08-13]: with
    levels < 43 zero, eta^0 STAYS individually solvable -- its
    linear level-47/52 terms survive; the kill is the slot-20
    SIMULTANEITY: the solve leaves exactly the 6 obstruction rows
    Row_20[eta^12,15,18,21,24,27] reading 0 = nonzero, the same
    defect (4) finds at low = 0 and the slot20 phase certifies.
    The earlier parenthetical here -- "0 = -42 returns at eta^0" --
    stated the wrong mechanism.)

(4) THE OBSTRUCTION IS NOT A FIXED CONTRADICTION. Fixing the low data
    (levels <= 42) by an exact cascade solve of bands 6/8/10 and
    solving bands 12..20 jointly over all 50 high unknowns leaves 32
    unreduced rows -- and their exact E-values DEPEND on the low data
    (two independent cascade seeds give different obstruction vectors;
    at low = 0 only 6 obstruction rows remain, exactly eta^12..27 of
    Row_20). So these are genuine polynomial CONDITIONS on the low
    tails + the 7, not a constant absurdity.  [REVIEW 2026-08-13:
    now a shipped phase, `claim4` (6/6 PASS, 10 s) -- both cascade
    seeds are CERTIFIED to satisfy bands 6/8/10 by exact raw-row
    evaluation before the joint solve; residual vectors differ at
    32 of 32 labels; both external replays reproduced the claim
    independently before it had a code path.]

**THE VERDICT (pre-registered semantics of §6): NOT EMPTY-BY-KILL.
The 83-var forced-nonzero-tail window does NOT kill residue-A.**
The zero-tail theorem of §3 stands and is now sharp in two directions
at once: it fails at first order (2) and on every closed-form
stratum (3), but it does NOT extend to the full window (1). The
honest surviving locus is exactly

   V = { tails, the 7, w_1, w_2 != 0 :
         47 band conditions (6.T, banked, exact, all 4 branches)
         AND the slot-20 inhomogeneous condition (6.T) },

a genuinely NONLINEAR variety: any point of it must carry
simultaneously nonzero LOW-level tails (38..42) whose degree-2/3
cross-terms feed the eta^12,15,18,21,24,27 obstruction components,
plus high-level tails absorbing the rest. Scope caveat, stated
plainly: NONEMPTINESS IS NOT CERTIFIED -- no explicit point was
extracted (every stratum admitting a closed-form solve is dead, and
the residual system is a polynomial system in ~28 low parameters
with 32 highly-degenerate conditions). What IS certified: no kill.
Residue-A survives this build; the direction-b J-window is exhausted
as a killing instrument at depth 21 and the burden moves to the
Q2 l8/l4 route and to rows 21+.

REPRODUCTION
    cd cases && python3 directionb_window.py gate      # 17/17, 3 s
    python3 directionb_window.py bands                 # ledger, 19 s
    python3 directionb_window.py slot20                # 27/27, 3 s
    python3 directionb_window.py verdict               # 24/24, 451 s
    python3 directionb_window.py claim4                # 6/6, 10 s
[REVIEW 2026-08-13, post-adjudication repair pass: the all-4-branch
rank identity of tests (1)(2) and claim (4) were first verified by
BOTH external replays (SHEET6-DIRECTIONB-REVIEW.md "R1 internal
review (Fable)"; xmodel/grok-directionb-review.md) and are now
harness-certified -- `verdict` loops (1)(2) over the 4 h-branches
+ w = (2,3) with an explicit rank-identity check, `claim4` is a
shipped phase, `slot20`'s checks assert the MEASURED inconsistent
defect (its earlier pre-result text asserted the opposite and
mis-reported 24 stale FAILs; the phantom "explicit point" print is
deleted), and `gate` pins RHS42 to the chart Jacobian.]
State: /tmp/directionb_tails_D21.pkl (banked copy of the build),
/tmp/directionb_window_conditions.pkl (the 47 band conditions,
per branch, as E-echelon rows).

[depth-23 build status 2026-08-13 12:08: ALIVE and detached (PID
21586, PPID 1, nohup; ~99% CPU, mid-GB42 orbit). Log:
/tmp/tails23.log (= /tmp/directionb_d23.log, symlinked). On
completion it OVERWRITES /tmp/directionb_tails.pkl with the D = 23
state; the D = 21 state stays banked at /tmp/directionb_tails_D21.pkl
(analysis reads the _D21 copy first).]

NEXT OBJECT (unchanged in kind, sharpened in target): decide V by
solving the 32 obstruction conditions on the low data -- a Groebner-
tier job in ~28 parameters, or a depth-23 rerun (rows 21/22, build
running) which adds rows that may collapse the degeneracy. Until
then residue-A is ALIVE on the forced-nonzero-tail locus.

GROEBNER-TIER EMISSION (2026-08-13, `directionb_residual32_emit.py`,
guards 5/5 PASS): the residual decider emitted msolve-ready as
cases/directionb_residual32*.ms (+ .rows.txt legend). Content: all
77 window rows (bands 6..18 + Row_20 with the +42 inhomogeneity,
LHS+42 = 0 form), fully expanded integer-coefficient monomial sums
(emit_expanded; guard A: zero parens), the r1_minimal_ext radical
block (r3^2-3, A1^3-3-r3, A2^3-3+r3, 2*HW_i^2-3*W_i^2), and
Rabinowitsch saturation for every forced-nonzero scale that is a
datum of this chart: uW1*W1-1, uW2*W2-1, uA*A1-uA*A2-1. NOT
saturated, with reason: c_f c_g (consumed at the (J)-derivation
tier, gauge 1 banked, §6 trust (e) -- not a chart variable); z, B
(absent from every window radkey, asserted at emission). 84 vars =
74 occurring template frees (42 high tails levels >= 43 + 26 low
tails + 6 of the 7: uf30 NEVER occurs in the window, it enters
first beyond depth 21) + uW1,uW2,uA + W1,HW1,W2,HW2,A1,A2,r3. VARIABLE
ORDER: the 42 highs + 3 u's head the header; `msolve -e 45` projects
onto the ~28 low+7 parameters + radical tower = THE residual-32
system (its closed form is Groebner-tier by nature: the rank-16
elimination transform is rational in the low data, §6.V(4)).
Char-0 lane (directionb_residual32.ms, 2.0 MB, EMITTED NOT RUN) +
3 banked-prime lanes (p = 105337, 105673, 200257; coefficients in
[0,p)) + ctl0 satisfiability-guard variant (constant blocks dropped;
origin-satisfiable, guard D; GB=[1] there = transcription error,
ctlA convention). Anchors: guard B independent-parser round-trip
char0+p vs internal ring eval (85 rows x 2 points x 2 primes);
guard C pattern-positive -- at tails=0 exactly the 9 zero-tail
Row_20 comps survive and equal the banked dsys constants (+42 at
eta^0) mod p, 9/9 nonzero. VERDICT SEMANTICS: main-lane GB = [1]
at the primes = strong evidence the forced-tail window variety is
EMPTY (then char-0 [1] = proof-tier residue-A window kill);
GB != [1] = V alive mod p, dimension/degree data for the fleet.
Sizes: main 2,035,641 B char-0; 1,983,334 / 1,983,734 / 2,006,543 B
at p = 105337 / 105673 / 200257; ctl0 1,949,393 B char-0 + 3
p-lanes ~1.98-2.00 MB; legend 3,753 B; 85 eqs (77 window + 5
radical + 3 saturation) x 84 vars per file.
SCREENS (local, msolve 0.10.1, -g 2 -t 4, 1200 s cap each;
/tmp/directionb_res32_screen.log):
  ctl0 p105337: TIMEOUT 1200 s (0-byte .out != NONEMPTY, R6 §19.2
  hygiene) -- banked for the fleet; RSS ~1.6 GB, F4 grinding, so the
  system FITS in memory and is fleet-runnable.
  main p105337: TIMEOUT 1200 s, 0-byte .out, RSS ~1.1-1.6 GB.
  main p105673 / p200257: running at the same cap at close of
  session; verdict lines land in /tmp/directionb_res32_screen.log
  and cases/*.out as they finish (expected: same TIMEOUT class).
  READING: no local mod-p verdict; the decider is a FLEET job
  (memory fits, wall does not). The emission + guards are the
  banked deliverable; -e 45 elimination lane for the residual-32
  projection, -g 2 lanes for the EMPTY/alive call.

Trust: (a) the chart identity (J) is elementary calculus on the exact
factorizations f - a = phi_f prod(y - y_i), g = phi_g prod(y - z_j)
(Newton-polygon corner argument for the y-leads, §2b) — no printed
statement of the thesis is used beyond the promoted genome
(SHEET6-TEMPLATE, SHEET6-L1, both promoted); (b) jets = the
r1_experiment orbit model (guard-certified machinery, reused
read-only; VDEG_CAP raised to keep every row EXACT — sentinel-freedom
asserted on every build); (c) gate: E6 slot-0 leads, E1 tower
cancellation, Row_0 == 0 (4/4 PASS) before any new order read; (d)
the verdict rows independently re-derived by a zero-shared-code
mod-p direct product at 3 primes (numcheck), coefficient-for-
coefficient; (e) the final contradiction is 2x2 exact linear algebra
over Q(sqrt3). Caveats: (i) the kill is a STRATUM statement (window
zero-extensions), not a full-variety kill; (ii) c_f c_g != 0 is used
(unconditional), the gauge value 1 is not load-bearing; (iii) the
orbit model's freeze of off-grid/odd-slot coefficients is the
promoted Q-datum (1c), inherited, not re-derived here.

Reproduction:
    cd cases && python3 directionb_strike.py gate       # 4 checks, ~2 s
    python3 directionb_strike.py rows 7                 # k<=6 full frees
    python3 directionb_strike.py solve6                 # Row_6 rank 8
    python3 directionb_strike.py dsys 21                # ~11 min, banks pkl
    python3 directionb_strike.py w4                     # verdict solve
    python3 directionb_numcheck.py [100003|105400|200000]  # independent
State: /tmp/directionb_dsys.pkl (exact Row_20 constants),
/tmp/directionb_tails.pkl (full-window tails build, phase `tails`).

Next objects, in order of value:
1. JOINT object: banked R1 depth-84 quotient tier + the J-window rows
   k = 6..20 with P-side tails + B-frees free (the tails build, phase
   `tails`, is the first half; its row structure characterizes the
   forced-nonzero-tail locus and couples the 7 via tail cross-terms).
   A rank deficit or inconsistency there is the FULL residue-A kill.
   [CLOSED 2026-08-13 -- see §6.T/§6.V. The build completed
   (2998.7 s, /tmp/tails21.log); the analysis is done and the
   pre-registered call is CONSISTENT, not INCONSISTENT: no
   full-window residue-A kill. Rows 6..19 turned out NOT to be
   "tail pins" (nothing is pinned to 0 -- already Row_6 has E-rank 1
   on its 6 level-38 tails); they are 47 exact E-module conditions.
   A depth-23 rerun (rows 21/22, /tmp/tails23.log) is running to test
   whether the extra rows collapse the degeneracy.]
2. Extend (J) to rows 21..41 (still pure y-side; the h2-resonance
   b2 = (3/4) sigma sits at slot 24-ish content) — same machinery,
   deeper truncation.
3. Port the row builder to the 6 sibling templates (§5(ii)) — their
   resonance windows may be overdetermined the same way; a uniform
   9-on-2-type theorem would drain the whole book's zero-extension
   loci.
4. Rows k = 42+ with the x-side model (LR2 pin, SHEET6-R1 §16.5):
   the first x-side-coupled J-orders — the R5 completion.

## 7. Level-42 no-log pins (Keller action residues, Sol avenue 1)

[2026-08-13; GATE 1 of the avenues sweep xmodel/sol-avenues2.md §1.
Adversarial re-derivation in THIS document's chart conventions.
VERDICT: THE LEMMA IS VALID HERE — 9 pins, 6 live in the banked
residual-32 system, each a PURE VARIABLE pin. Derivation:]

**(1) Closed, hence exact, on A^2.** J(f,g) = c != 0 constant gives
d(f dg - c x dy) = (J - c) dx^dy = 0 and d(g df - c y dx) = 0.
H^1_dR(A^2) = 0 in char 0 (elementary: integrate the closed form
term-by-term in x, the remainder is a closed form in y alone), so
there are POLYNOMIALS P, Q with f dg - c x dy = dP and
g df - c y dx = dQ. Our banked gauge has c = 1 (S_R = G_R = 1);
nothing below consumes the value beyond c != 0.

**(2) Pull back along a fibre branch.** §2b (promoted, F1):
f - a = phi_f(x) prod_i (y - y_i(x)), g = phi_g(x) prod_j (y - z_j(x))
— the y_i are EXACT root series of f = a, the z_j of g = 0. Let
phi: Spec K((t)) -> A^2, phi = (x(t), y_i(t)) be an f-place. Then
phi*f = a IDENTICALLY, so pulling back g df - y dx = dQ kills the
first term: y_i(t) dx(t) = -d(Q o phi). Q is a polynomial and x, y_i
are Laurent, so Q o phi in K((t)) — finite principal part, NO log,
NO essential part (this is the entire "no-log" content; a log t in a
primitive is exactly what a nonzero residue would require). Purely
formal; no convergence is consumed. Hence Res_t(y_i dx) = 0 at EVERY
f-place separately (the primitive is global-polynomial, so this is
per-place, strictly stronger than the residue-theorem sum). On g = 0
the same argument with f dg - x dy = dP (phi*g = 0, so the f dg term
dies) gives Res_t(x(t) dz_j(t)) = 0 at every g-place.

**(3) The residue in OUR chart.** §0: t = x^{-1/42}, so x = t^{-42}
EXACTLY at every 42-ramified place (P1, P2, B, Gp1, Gp2, GB42).
y = sum_m c_m t^m gives Res_t(y dx) = -42 c_42 and
Res_t(x dy) = +42 c_42; either way the pin is c_42 = 0: the
T-LEVEL-42 COEFFICIENT of the root series dies. For the 21-ramified
places (G0p1, G0p2, GB21; series in u = t^2, x = u^{-21}, registry
sizes 21 with even support — build_generators, r1_experiment.py
:357-404): Res_u(x dy) = 21 gamma_21 with gamma_k = c_{2k}, so the
pin is again the t-level-42 coefficient. Signs and the 42 are
IRRELEVANT to the pin (homogeneous, char 0); the inhomogeneous -42
of Row_20 is a different object (the t^20-slot of (J)) and does not
interact. [Nit vs the avenue doc: the pole pair is 3±sqrt3 (A1c/A2c,
r1_experiment.py:126), not "2±sqrt3"; the value is not consumed.]

**(4) Exact variable mapping (hazard (a)/(d), from the registry,
r1_experiment.py build_generators).** Level-42 carries a LONE free
tail var in every orbit series; skeleton support stops at level 37
(P-places: 12, uf 18/24/30, alpha at 32, vf 34/36, w at 37), at 32
(G0-places), at 12 (B-places). So each pin is PURE, not a
tail+skeleton combination:

  place  series-var at t^42   emitted name     status
  P1     tf1_42               x46              LIVE pin
  P2     tf2_42               x51              LIVE pin
  Gp1    tg1_42               x56              LIVE pin
  Gp2    tg2_42               x61              LIVE pin
  G0p1   tg01_42              x64              LIVE pin
  G0p2   tg02_42              x67              LIVE pin
  B      bf_42                (frozen 0, D21)  trivially satisfied
  GB42   bg42_42              (frozen 0, D21)  trivially satisfied
  GB21   bg21_42              (frozen 0, D21)  trivially satisfied

The three B-side pins are exact too but the banked D21 object
freezes those tails at 0, so they add nothing here; bank them for
depth-23+/Q2 AFTER the B-place parameter-normalization guard that
the avenue doc itself flags.

**(5) Adversarial cross-checks (all reproduced independently).**
Sol's mapping x46/x51/x56/x61/x64/x67 verified against
directionb_residual32.rows.txt; term count of the banked emission
79,590 EXACT match; pin-substituted independent-monomial relaxations
reproduce EXACTLY: Row_20 10 x 2295 rank 10 CONSISTENT, full window
76 x 4351 rank 56 CONSISTENT (so the pins are NOT a standalone
depth-21 kill — the avenue's own label); Row_10[eta^28] (= §6.T's
C10.6, the only pure-K3 window condition at level 42) has 0
surviving terms under the pins — the window already contained
exactly the Galois-symmetric SHADOW of the pins, and nothing more:
strong wrong-object exclusion (the new rows refine, never
contradict, the banked ones).

**Trust chain:** (i) step (1) is elementary char-0 calculus;
(ii) step (2) consumes ONLY the promoted §2b factorization (F1);
(iii) step (3) the §0 chart normalization; (iv) step (4) the orbit
registry (guard-certified machinery, read-only). Same tier as the
J-rows themselves. The pins are NECESSARY conditions on every
residue-A realization; adding them to the residual-32 decider is
sound (GATE 2, §6.V addendum).

### 7.G GATE 2 — the no-log decider (emission + screens)

`directionb_residual32_emit.py nolog` (guards 2/2 PASS + per-file
regression gates): the 6 live §7 pins appended, append-only, to all
8 banked residual-32 lanes -> cases/directionb_residual32_nolog
[_ctl0][_p105337|_p105673|_p200257].ms, 91 eqs x 84 vars each
(79,596 expanded terms on the main lane, = banked 79,590 + 6; ~2.0
MB/file). Discipline: prefix BYTE-IDENTICAL to the banked emission
(so guard B round-trip transfers by composition), paren sweep on all
8, pin mapping re-verified 6/6 against rows.txt, pattern-positive
anchor re-run on the _nolog main (tails=0 satisfies the pins;
9 zero-tail Row_20 comps == dsys constants, +42 at eta^0). Pins
also appended as a comment block to directionb_residual32.rows.txt.
SCREENS: launched detached 2026-08-13 (runner PID 46709, PPID 1,
nice 5, msolve -g 2 -t 4, 12 h cap/lane, order: ctl0_p105337 then
the 3 main lanes; self-recording to /tmp/directionb_res32_nolog.log,
final line "ALL NOLOG SCREENS DONE"). Verdict semantics unchanged
(§6.V): main GB=[1] at the primes = strong-evidence EMPTY window
(then char-0 for proof tier); alive = the pins do not close the
escape alone (Sol's own expectation; the 6 rows remain banked
permanently either way — they are exact and free).

## 8. The depth-23 window (rows 21/22): decision analysis

[2026-08-13. Build: directionb_strike.py tails 23 (5587.2s, exact,
sentinel-free, 93 free vars, tails to level 54); state banked
/tmp/directionb_tails_D23.pkl. Engine: directionb_window.py with
DIRECTIONB_STATE=/tmp/directionb_tails_D23.pkl (D21 default path
untouched).]

GATE (17/18): all D21 anchors reproduce on the D23 state -- rows
6..18 die at tails=0 term-by-term; Row_20 zero-tail block == banked
dsys constants coefficient-for-coefficient; 9-on-2 + 0 = -42
re-derived; E5/E6/E1/Row_0 strike anchors 4/4. REGRESSION: rows
6..20 of the D23 build == the D21 build ROW-FOR-ROW (compared by
variable NAME across the two registries; no level-53/54 monomial
enters any row <= 20) -- the window rows are depth-stable. The ONE
designed FAIL is the finding:

**Row_21 == 0 identically; Row_22 is NEW and does NOT die at
tails=0.** Its zero-tail part is, per eta-component (8 comps,
eta^1,4,...,22), bilinear:

   alpha1 vf1_34 . L1n(X1, X2) + alpha2 vf2_34 . L2n(X1, X2) = 0,
   X_i = alpha_i w_i^4,

i.e. THE J-WINDOW'S FIRST DIRECT (LINEAR) SIGHT OF THE MERGE
COEFFICIENTS vf1_34, vf2_34 -- at depth 23, the §2c statement "the
grid is undetermined by J at this window" EXPIRES: the grid enters
linearly (times pole scales), no longer only through tail
cross-terms. On the zero-tail stratum this adds nothing (Row_20
already forces X = 0 = absurd there); in the full window it is new
coupling.

BAND LEDGER DELTA: Row_22 = 10 eta-comps, tier S 631 x 5349 rank
425; tier V rank 10/10 over E on ALL 4 h-sign branches, no
leftovers => +10 exact E-conditions per branch (§6.T's 47 -> 57).

THE DECISIVE RELAXATIONS (independent-monomial over-approximation;
INCONSISTENT would be EMPTY-BY-KILL of the whole forced-tail locus):
  PLAIN  (+1,+1) w=(1,1): 87 rows x 10328 monomial cols ->
         rank 67, CONSISTENT, 0 undecided. NO KILL.
  [pinned + second-branch lanes: below]
  PINNED (+1,+1) w=(1,1): the 6 §7 no-log pins applied (monomials
         containing a pinned var dropped): 86 rows x 8623 cols ->
         rank 66, CONSISTENT, 0 undecided (the one dead row is
         Row_10[eta^28] = C10.6, implied by the pins, §7(5)).
         NO KILL.
  Uniformity lanes ((+1,-1) w=(1,1) plain+pinned; (+1,+1) w=(2,3)
  pinned) running at close; results land in /tmp/d23_uniformity.log
  (same CONSISTENT expected -- all D21 ranks were branch-uniform).

**DEPTH-23 VERDICT (same semantics as §6.V): NO EMPTY-BY-KILL.**
Rows 21/22 do NOT close the window, with or without the level-42
no-log pins. The forced-tail locus stays alive at depth 23;
relaxation rank grows 57 -> 67 (plain), 56 -> 66 (pinned) on 87/86
rows -- rows 21/22 add exactly 10 independent relaxation directions
and Row_22's 10 E-conditions.

RESIDUAL-32 DELTA: the D21 residual object changes SHAPE, not by
shrinking: (i) rows <= 20 and their 32 obstruction conditions are
UNCHANGED (depth-stability, row-for-row); (ii) Row_22 adds 10
conditions that are QUADRATIC in the high tails (e.g. tg1_43^2 at
level sum 86) and introduces 10 new high vars (levels 53/54) -- the
§6.V(4) linear high-elimination does NOT extend verbatim past band
20; a D23 Groebner emission would need the quadratic block kept.
(iii) NEW GRID COUPLING: zero-tail Row_22 = 8 bilinear conditions
alpha1 vf1_34 L1n(X) + alpha2 vf2_34 L2n(X) = 0 -- the first
J-window rows in which the dead-stretch grid appears linearly
(times pole scales); any future grid-sector analysis must consume
them.

Reproduction:
    cp <build> /tmp/directionb_tails_D23.pkl
    DIRECTIONB_STATE=/tmp/directionb_tails_D23.pkl \
        python3 directionb_window.py gate      # 17/18, the FAIL is
                                               # the Row_22 finding
    (bands/relaxations: §8 scripts inline; python3 - snippets in
    the session log; the engine functions are directionb_window.py's
    band_tierS/band_erows/relax/esolve, state-parameterized)
Trust: same perimeter as §6.T/§6.V -- exact E-arithmetic, unit
pivots, all 4 h-sign branches on the band tier; relaxation lanes
(+1,+1)/(+1,-1), w = (1,1)/(2,3).
