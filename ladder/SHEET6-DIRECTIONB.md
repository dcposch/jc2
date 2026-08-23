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

## 7.S THE SCREEN CAMPAIGN RECORD (final, 2026-08-16)

The residual-32 nolog system (84 vars after the six §7 pins; 85 eqs
main / 91 pinned variant) resisted every Groebner instrument fielded:

  R1 (12 h caps, -t 4):  6 nolog lanes TIMEOUT; ctl0 TIMEOUT.
  R2 (48 h caps, -t 24): 3 main-prime lanes TIMEOUT; -e 45
      elimination probe TIMEOUT (all rc=124, 0-byte outs — per R6
      hygiene these are TIMEOUTS, not verdicts).
  Order portfolio (29 h): reversed + seeded-shuffle orderings both
      TIMEOUT — hardness is order-robust.
  Chamber map v1 (broad leaves, 120 G fences): a3-analogue EMPTY
      instantly; rest fence-killed.
  Chamber map v2 (hierarchical tau-orbit partition, Sol design,
      exact sizes verified): leaf a3 EMPTY at p105337 AND p200257
      (the only computed chamber verdict; banked); a1/a2/a0/b1 hit
      120 G fences in <2 h each; b2/b3 TIMEOUT at 24 h caps.
  Fleet total: ~300 lane-hours of F4 at up to 1.9 TB aggregate RSS.

HONEST READING: the system is compute-hard for msolve F4 at 2 TB
scale in every configuration tried; hardness is spread across the
support chambers (not concentrated), order-robust, and unaffected
by the -e elimination hint at these caps. The a3 chamber (tg0_40-
loaded, all other even lows zero) is EMPTY at two primes. No
NONEMPTY witness anywhere. Next-instrument decision: §7.S1 below
(the 2026-08-16 scan).

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
  UNIFORMITY (all landed, /tmp/d23_uniformity.log): PLAIN (+1,-1)
  w=(1,1): rank 67, CONSISTENT (510 s); PINNED (+1,-1) w=(1,1):
  rank 66, CONSISTENT (371 s); PINNED (+1,+1) w=(2,3): rank 66,
  CONSISTENT (442 s). Ranks identical across h-sign branches and
  pole-scale samples, matching the D21 uniformity pattern.

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

### 7.H Low-support case split of the nolog decider (leaf portfolio)

[2026-08-14, DC-authorized screen acceleration;
cases/directionb_residual32_leaves.py, checks 8/8 PASS.]
Split lattice = the 12 EVEN low tails (levels 38/40; the odd lows
39/41 enter the bands only w-weighted, no unit-kill lever -- not
split; documented reading of the "38..41 block"). COVER (overlaps
allowed), tau-conjugate chambers merged -- merge certified by the
banked tau-covariance (1c.1/§2c/gate) PLUS an exact involution
check: tau(Row) == Row for every banked VExpr row. PRE-DEAD, cited
+ machine-checked, no emission: 6 singleton-38 chambers (C6.1 is
one E-row with ALL-UNIT coefficients on the six 38s, every branch,
no 7/w-dependence); 6 singleton-40-within-38-silent chambers
(C8|{38s=0} pure-linear, every 40-var carries a unit coefficient,
every branch); {all lows = 0} (inside leaf a0; also §6.V(3)).
EMITTED (p105337, full AUDIT discipline -- paren sweep, dual-parser
round-trip at fence-consistent points, pattern-positive anchor on
the support-matching leaf a0, origin-satisfiable ctl0 for a0;
fenced leaves have no origin-tier control, documented):
  a0 {38s,40s = 0}          58/77 rows,  72 eqs, 0.41 MB
  a1/a2/a3 {38s=0, one 40 fenced}  68/77, 83 eqs, 0.76 MB each
  b1/b2/b3 {one 38 fenced}         77/77, 92 eqs, 1.98 MB each
COVER IDENTITY machine-checked: all 4096 support patterns of the
lattice land in a leaf or tau-image (pins respected, fences
witnessed); unsplit vars unconstrained => leaves + pre-dead = the
full nolog variety. LAUNCHED on Box02 ~/res32/leaves (FLEET.md
orphan-safe pattern; md5-verified transfer): 8 lanes (7 leaves +
a0-ctl0), msolve -g 2 -t 8, 86400 s caps, 120G ulimit fence +
nice 10 per lane (main lanes not crowded; 1.4T free at launch);
self-recording to ~/res32/lanes.log.

### 7.H2 Hierarchical first-nonzero tau-orbit cover (v2, Sol accel2 (b))

[2026-08-14. Replaces the v1 broad leaves (v1 flaw, Sol-confirmed:
b-leaves hard-zeroed nothing; a1-a3 shared the {38s = 0} open set;
pins appended not substituted). cases/directionb_residual32_leaves.py
rewritten to the exact accel2 design; checks 6/6 PASS.]

Design: six no-log pins SUBSTITUTED OUT everywhere (Row_10[eta^28]
= C10.6 dies identically); first-nonzero hierarchy on the tau-pairs
(tf38, tg38, tg0_38, then tf40, tg40, tg0_40): b1 fence tf1_38;
b2 tf38-pair=0 fence tg1_38; b3 +tg38-pair=0 fence tg01_38;
a1 all-38s=0 fence tf1_40; a2 +tf40=0 fence tg1_40; a3 +tg40=0
fence tg01_40; a0 all twelve even lows = 0. The seven chamber
classes C_i = leaf_i U tau(leaf_i) PARTITION the support lattice
(machine-checked: each of 4096 patterns in EXACTLY ONE class;
census 3072/768/192/48/12/3/1). tau-involution re-certified exactly.

SIZES == SOL'S PREDICTED TABLE, ALL SEVEN EXACT (wrong-object gate):
b1 76/67698/79, b2 76/50229/77, b3 76/36042/75, a1 67/24741/73,
a2 67/19983/71, a3 67/15737/69, a0 48/12079/66 (window rows/window
terms/vars). Guards: paren sweep (14 files), dual-parser round-trip
(7 leaves x 2 primes x 2 fence-consistent points), anchor on a0.
Emitted p105337 (shipped, md5-verified, Box02 ~/res32/leaves2,
launched orphan-safe -t 8 / 86400 s / 120G ulimit / nice 10) AND
p200257 (BANKED in cases/, verdict-confirmation wave, NOT launched).
Old broad lanes culled (stragglers a1-a3/b2/b3 killed to match the
coordinator's cull); old a0 + a0-ctl0 kept (same variety as v2-a0).

**FIRST LEAF VERDICT: a3 = GB [1] at p105337 -- EMPTY** (authentic
msolve header, grevlex, basis length 1; reproduced rc=0/512B TWICE
at 02:52 and 02:53). The chamber {all 38s = 0, tf40 & tg40 pairs =
0, tg0_40 loaded} is DEAD mod p105337: strong evidence, pending the
banked p200257 twin + char-0 for promotion (§6.V semantics). The
surviving low-support chambers narrow to b1/b2/b3/a1/a2 + a0.

## 7.S1 Exact symbolic band elimination (the compression instrument)

[2026-08-15/16, instrument decision xmodel/sol-instrument.md §C;
owner: cases/directionb_compress.py (phases elim | emit | guards).]

OBJECT: the nolog window (D21, §7 pins substituted, 76 rows after
C10.6 dies) is AFFINE-LINEAR in the 42 occurring high tails
(asserted: no high*high monomial exists below slot 21 since
43 + 43 = 86 > 84). Fraction-free Bareiss steps
R_t' = c_p R_t - A_t(lows) R_p with CONSTANT pivot coefficients c_p
that are variety-units (single w-monomial weight x unit of the
etale algebra E on ALL FOUR h-sign branches -- verified per pivot;
no denominators beyond the tower) eliminate the highs exactly,
branch-free. Residual = the compatibility system on the low
parameters + dead-stretch + w1, w2 (+ the untouched low bands).

STATUS AT BANKING: elimination RUNNING detached
(/tmp/compress_elim.log): 10/~16 pivots done, all unit-certified on
4 branches -- tf1/tf2_44 (Row_12), tf1/tf2_46 (Row_14), tf1/tf2_43
+ tf1/tf2_48 (Row_16), tf1_45 + tf1_50 (Row_18); remaining by
tau-symmetry: tf2_45, tf2_50, then tf1/tf2_47, tf1/tf2_52 (Row_20)
= 16 = the claim-4 generic high-rank. STRUCTURE: every unit pivot
is f-side; the tg-side high coefficients are MIXED-w constants
(h-fold makes them two-weight sums) -- correctly REFUSED as pivots
(a mixed-w constant can vanish at special w: not a variety-unit).
SHADOW PROJECTION (support-only replay, 2 s): residual support
~2.0e3 var-monomials, max var-degree 5 -- the Sol §C STOP criteria
(1e6 terms / 67,698 raw pinned mass) project as PASSED by two
orders of magnitude; exact counts on completion.

STAGED (module complete, runs on elimination completion): emission
directionb_compressed[.ms|_p105337|_p200257|_ctl0*|_a3_p105337]
with the banked xN naming; guards: paren sweep; independent scalar
REPLAY of the exact pivot sequence == symbolic residual (2 primes x
3 points incl. all-lows-0); emitted-string round-trip; rank(A) ==
16 == #pivots and rank([A|b]) jump <=> compatibility values != 0;
back-substitution kills every pivot row INCLUDING the +42 row;
claim-4 seed protocol (pins-adapted, seeds 1/5); ctl0 origin;
a3-chamber samples + the emitted _a3 msolve reproduction lane.

PRE-REGISTERED A/B GATE (3x, per the instrument decision): the
p105337 compressed lane runs on box01 (nearly idle) with a 2 h cap
against the R1 baseline = the uncompressed nolog lanes' 12 h
timeouts. PROMOTE the instrument to big iron iff the compressed
lane returns a verdict inside the cap OR -v 2 telemetry shows >= 3x
same-degree matrix/RSS improvement; else the instrument stays
local-tier (Sol §C: acceleration failure is NOT a mathematical
survival verdict). Box01 pilot is the coordinator's launch; nothing
runs locally beyond the exact-python elimination and guards.

### 7.S2 The fast elimination engine (python-flint; split-prime cores)

[2026-08-16, DC priority; cases/fastelim.py; python-flint 0.9.0
(nmod_mpoly). 18/18 checks PASS across the three banked primes.]

SPLIT-PRIME MODE: legendre(3,p) = +1 for ALL THREE banked primes
(105337, 105673, 200257 -- no replacements needed); s = sqrt3
substituted (the radical_point branch), so K3-coefficients are GF(p)
scalars and the window rows live in GF(p)[template, A1, A2, W1, HW1,
W2, HW2] with FREE radical generators (relations rejoin at emission
as minimal-poly rows; exponents lattice-reduced at emission).

WALL-TIMES, old exact engine vs flint: the 10-pivot prefix 2491 s ->
0.1 s (~25,000x); the FULL elimination (16 pivots) 0.2 s vs the
exact run's projected days (pivot 11 alone took 9650 s before the
kill). All 16 pivots are UNIT-class (single w-weight, nonzero on
all 4 h-sign branches), 0 mixed => the core is EQUIVALENCE-tier on
the w != 0 chart (projection exact), not merely necessary. 8 high
tails survive as variables (tg1/tg2/tg01/tg02 at levels 44/46); the
other 18 non-pivot highs cancel identically.

TRUE CORES (per prime, identical shape): 43 vars (34 template incl.
the 8 leftover highs + 6 radgens + 3 sat), 67 eqs (60 window rows +
7 rad/sat), 21,870 terms, template-degree profile {0:18, 1:306,
2:2310, 3:5204, 4:6120, 5:4462, 6:2268, 7:894, 8:288}, ~0.80 MB:
cases/directionb_core_p105337|105673|200257.ms (+ .rows.txt
legends). 21,870 << 67,698 raw pinned mass: Sol §C stop-criteria
PASSED with 3x margin (the char-0 partial's 135,523 failed them;
the mod-p core is the compression the instrument wanted).

GATES (per prime): a2 -- all 10 banked exact pivot coefficients ==
engine's, compared sequentially mid-elimination (lattice-reduced);
a -- 10-pivot state == the banked EXACT residual mod p ROW-FOR-ROW
(66 rows); b -- tau(input at r3) == input at p-r3, all 76 rows
exactly; c1 -- independent scalar replay of the full pivot sequence
== mpoly residual at random points; c2 -- pattern-positive anchor
(6 Row_20-descended rows nonzero at tails->0; the +42 content
survives); emission guards -- paren sweep + independent-parser
round-trip, 60 rows + rad/sat x 2 points. CHAR-0 TOWER MODE:
deferred (the mod-p lanes are the screens' instrument; the banked
exact 10-pivot state remains the char-0 ground truth). Solver lanes
NOT launched (coordinator's call; box01 busy with PILOT12).

### 7.S3 CORE2 (instrument round 3: +6 low pivots, W-normalization)

[2026-08-17; Sol instrument3 §§1/7; fastelim.py run_core2 + drivers.
Forensic input accepted: the §7.S2 "true core" was NOT a degree-8
object (template-only degree count hid Laurent W-content up to
W1^2184 W2^546, actual msolve degree 2741); Sol's 6 further unit
pivots were real.]

CORE2 = 22 pivots (16 high + the 6 low: tf1_38<-Row_6[eta^2],
tf1_40<-Row_8[eta^0], tf2_40<-Row_8[eta^3], tf1_39<-Row_12[eta^8],
tf1_41<-Row_14[eta^6], tf2_41<-Row_14[eta^9]), pseudo-division for
targets nonlinear in the low pivots (pivot rows are linear there),
W-unit normalization after EVERY pivot (uW rows make W_i units;
strips recorded, reconstruction asserted -- G0.3, 143 strips).
WALL: 14 s per prime (engine build ~220 s more), vs the exact
engine's days-scale projection. CENSUS == SOL'S REPLAY EXACTLY on
the unsplit object at ALL THREE primes: 38 residual rows, 6,311
terms, 18 template coords (set identical to Sol's list), max TOTAL
degree 10 => emitted 27 vars / 45 eqs / ~0.16 MB:
directionb_core2_p{105337,105673,200257}.ms. Cross-prime monomial
SUPPORT identical row-for-row (G0.2x).

GATES (Sol §7 G0, all PASS): G0.1 22 sequential pivots, the 6 low
coefficients single radical/Laurent monomials nonzero on all 36
tower factors; G0.2 shape/support identity x3 primes; G0.3 strip
records + reconstruction; G0.4 independent dict-engine TWIN replay
== flint residual row-for-row + back-substitution (22 frozen pivot
rows incl. the +42 row vanish at back-solved points; pins held 0);
G0.5 paren/round-trip x3, tau-OUTPUT (CORE2 at r3 == tau-transported
CORE2 at p-r3, normalized row-for-row), pattern-positive anchor (6
Row_20-descended rows nonzero at tails->0), ctl0 origin; G0.6
a3=[1] REPRODUCED at 105337 AND 200257 at source level (Sol §5
mechanism verified: raw Row_8 at the a3 chamber = 10 homogeneous
rows on (tg01_40, tg02_40), rank 2 on ALL 36 fibers => fence
contradiction; transfers to CORE2 by the certified equivalence);
G0.7 fiber sweep: ALL 36 fibers, census 22 vars / 26 eqs / deg <= 8
IDENTICAL, A1 != A2 everywhere.

FIBER TERM-COUNT RECONCILIATION (the one non-exact item, stated
plainly): the fiber term count is PRESENTATION-dependent: RREF
3,997; forward echelon (min-pivot) 4,889; forward echelon
(max-pivot) 5,344; raw independent-row selection 6,011. Sol's
replay says 5,348 -- 4 terms (0.07%) from the max-pivot echelon:
same construction modulo an echelon ordering convention; the ideal
is identical in all presentations (round-trip + rank certified).
Emitted: directionb_core2_fiber_p105337.ms = the radical_point
fiber, 24 max-pivot echelon rows + 2 uW rows, 5,344 terms, 0.11 MB.
Legend: directionb_core2.rows.txt. Handed off for the 30-min A/B
pilot (box01; G1 semantics of instrument3 §7). Nothing launched
locally; no commits.

### 7.S4 The fiber locus: dimension, points, and the depth-23 filter

[2026-08-17. Pilot input: the CORE2 fiber at p105337 solved in 11 s,
GB = 397 elements, NONEMPTY over F_p-bar -- the A/B gate cleared
~4000x; the old 12h/221G record measured the defective object.]

TWIN EMISSIONS: directionb_core2_fiber_p{105673,200257}.ms emitted
(identical shape: 24 max-pivot echelon rows + 2 uW, 5,344 terms,
~0.11 MB each) -- handed off for the two-prime robustness check.

DIMENSION (from the box01 GB, initial-ideal combinatorics, exact):
**the fiber locus is 13-DIMENSIONAL** (22 fiber vars; maximal
independent set = uf18, vf1_34, vf1_36, vf2_34, vf2_36 -- the WHOLE
dead-stretch/merge block -- plus tg1_39, tg1_41, tg2_39, tg2_41,
tg01_38, tg01_40, tg02_38, tg02_40). LT-degree histogram 1..12
(mode at deg 6); top-component degree not cheaply convergent
(>1e5 standard monomials in the naive localization) -- deferred.
STRUCTURAL GEM: the GB pins the POLE SCALES: W1^4 = 57673,
W2^4 = 53212 (mod 105337) -- the fiberwise echo of the §6.V slot-20
X_i-pinning, now GLOBAL on the locus. F_p-RATIONAL POINTS: sampling
the 13 free directions randomly + solving the bound block: 12/12
tries produced verified F_p-points (all 397 GB elements vanish) --
the locus is F_p-point-rich.

THE DEPTH-23 FILTER (exact, mod p; harness /tmp/fiber_filter2.py,
to be promoted into cases/ with the D23 core): per sampled point,
the full D21 chart is reconstructed (22 pivots back-solved, pivot
rows vanish -- asserted), then the banked D23 Row_22 block (10
eta-comps) is evaluated as an affine system on the 10 deep tails
(levels 49/54), with the auxiliary D21-free tails at zeros AND at 2
random draws:

  **0/12 SAMPLED FIBER POINTS SURVIVE DEPTH 23 (36/36 point-draw
  combinations INCONSISTENT).** The D21 germ locus, nonempty and
  13-dimensional mod p, is killed at every sampled point by the
  depth-23 rows. No residue-A germ candidate through depth 23 was
  found; the D23-CORE RE-EMISSION is the next object, exactly as
  pre-registered. (Scope: 12 random points x 3 free-draws, one
  radical fiber, one prime -- a sampling statement, not a variety
  kill; the D23 core decides it.)

Q2-l12 eta0: NOT added to the filter -- obsolete per Sol
instrument3 §6.3 itself (V_bank cap Q2_l12 = empty already
certified at quotient tier; "re-running eta0 adds nothing").

## 8.S The D23-core (the decisive object)

[2026-08-17; synchronous build per the standing correction.]

CONSTRUCTION: the 22-pivot band elimination extends to the D23
window with the Row_22 block UNPIVOTED (quadratic in highs, §8/
§6.V(4): linear elimination stops at band 20). Full elimination of
the pivots INTO Row_22 was measured and rejected: it inflates the
10 Row_22-descended rows to 4,971,007 terms / max degree 32 (the
substituted tf-expressions get squared) -- banked as the measured
alternative, not emitted. THE EMITTED FORM (hybrid, variety-exact):
38 compressed D21-CORE2 rows (byte-identical to the banked
directionb_core2_p*.ms rows -- REGRESSION gate) + 22 pristine pivot
rows (re-included so the pivot coordinates are defined) + 10
pristine Row_22 rows + rad/sat: **87 vars / 77 eqs / 59,316 terms /
degree <= 13 / ~1.5 MB per prime**, identical shape at 105337,
105673, 200257: cases/directionb_core23_p{105337,105673,200257}.ms
+ the p105337 fiber variant directionb_core23_fiber_p105337.ms
(72 rows / 80 vars / 59,316 terms folded, 1.2 MB).

GATES: regression (38-row prefix byte-identical to the D21-core
files, all 3 primes); round-trip re-parse (70 rows); paren sweep;
pivot-row back-solve inherited (G0.4b machinery); **FILTER-REPLAY
CLOSURE: the 12 dead sample points are INCONSISTENT against the
EMITTED D23-core rows (deep tails symbolic, affine rank test
through the parsed emission) -- 12/12, closing the loop between the
§7.S4 filter and the artifact.** Wall: ~8 min total for all three
primes + fiber + gates (engine build 1 s, 22 raw pivots 42 s, the
one heavy step was the measured-and-rejected full-elimination
census at 469 s).

PRE-REGISTERED OUTCOMES (coordinator): EMPTY at 2+ primes =
residue-A dead at the depth-23 window tier (screening) -> char-0
certification of the small core -> on-axis td=6 closes pending the
review gauntlet; NONEMPTY = dimension/points again and iterate to
D25 (depth iteration is now minutes-cheap; the constraint ratio
improves each step). box01 lanes are the coordinator's launch.

### 8.S2 Row_22 in the D21 quotient: the compatibility object

[2026-08-18; Sol instrument4 §§2-3, built + verified independently;
synchronous. /tmp state loss (the D21/D23 window pickles aged out)
was absorbed by working FROM THE FROZEN ARTIFACTS -- G0's own point;
harnesses/GB/points now promoted into cases/ (directionb_fiber_
filter.py, directionb_row22_schur.py, directionb_row22_emit.py,
directionb_core23_{elim,emit,final}.py, directionb_fiber_gb_
p105337.out.txt, directionb_fiber_points_p105337.txt).]

SOL'S §2.1 ALGEBRA VERIFIED INDEPENDENTLY (5/5 per prime): the ten
pristine Row_22 rows are F22 = A(z) y + b(z) in the ten deep tails
y = (x74..x83); A = C diag(u_j) with each u_j a SINGLE W-monomial
(chart unit) and C CONSTANT on the radical fiber; rank(C) = 4
certified by exact row reduction with recorded invertible U;
L = bottom-6 rows of U satisfies L C = 0, hence L A = 0 for ALL
chart W-values -- the SIX rows c = L b are the complete
compatibility condition, formed BEFORE any pivot substitution.
Stage-entry census MATCHES SOL EXACTLY: c at fixed-W = 25,554
terms ("before pivot elimination").

RECONCILIATION (the one non-replayable stage, stated plainly):
Sol's §2.2 post-pivot counts (16,134 / 10,500 / 7,054) presuppose
normal-form reduction by a FRESH FIXED-W D21 basis; no such basis
exists in our banked state (both overnight artifacts are the
W-symbolic 397-GB; the box01 D23 lanes are still 0-byte), and
solver runs are off-limits locally. W-symbolic NF against the
banked 397-GB is exact but coarser (86k terms at stage 2, growing)
-- pipeline-dependent presentation, NOT a bug in either side's
algebra; reconciled by construction of an emission that NEEDS NO
QUOTIENT STEP:

THE EMITTED OBJECT (deep-eliminated, quotient-free, variety-exact):
{24-row W-symbolic D21 fiber core} + {22 pristine pivot rows,
radgens folded} + {the 6 compatibility rows c} + 2 uW rows =
**72 vars / 54 eqs / 48,621 terms / ~1.0 MB per prime**, identical
shape at 105337 / 105673 / 200257:
cases/directionb_row22compat_p{105337,105673,200257}.ms.
The TEN DEEP TAILS ARE GONE from the system (asserted): by the
certified rank-4 Schur step, a D21 point extends through depth 23
iff c = 0 -- so EMPTINESS of this object == the depth-23 kill on
the chart, with 10 fewer variables and 6 rows instead of 10.

GATES: Schur certification per prime (6/6); paren sweep; deep-var
absence asserted; **LOOP CLOSURE: all 12 banked D21 fiber points
violate >= 1 of the SIX compatibility rows (12/12) -- the §7.S4/
§8.S filter verdict reproduced through c = L b.** Twin robustness
(coordinator's overnight lanes): fiber GBs at 105673/200257 are
~10.5 MB bases, NOT [1] -- the D21 fiber locus is NONEMPTY at all
three primes, consistent with §7.S4. box01 lanes on the compat
object are the coordinator's launch.

### 8.S3 Verdict-day valuation-e pipeline (INTERNAL TOOLING, UNREVIEWED)

[2026-08-18; DEPTH-STAB route-B consumer; sol-software2 item-1 split.]
cases/valuation_e.py: msolve-GB parser + hashing (the three real fiber
GBs), 7.S3 sampling (seed-2026 == the banked 12 points), full D21
reconstruction verified vs the 54-row compat emission + 76 raw rows
(+ 77-row hybrid + Row_22 rank-4 deep solve at D23), JSON certificates;
NEGATIVE CONTROL NOT_IN_DOMAIN 36/36 at 105337 AND 105673; at 200257 the
W^4 pins are non-4th-powers (no F_p-rational chart point; fail-closes --
extract at 105337/105673). **Every e is E_CANDIDATE (EXPERIMENTAL),
never LIVE: the DEPTH-STAB minor object needs the series map + square
function block + surplus-equation bridge, NOT YET BANKED**; measured:
t-grading 32/12/W=5 exact, deep tails 54x6/49x4, Euler-pencil spec gap.
Gates: python3 cases/valuation_e.py --gates. NO PROMOTION CLAIMS; no git.

### 8.S4 row22red: the 22 unit pivots pre-eliminated (INTERNAL / UNREVIEWED)

[2026-08-18 ~20:30Z; built + gated + launched this session; race
lanes against the running row22compat originals. INTERNAL /
UNREVIEWED.]

THE OBJECT: cases/directionb_row22red_p{105337,105673,200257}.ms =
the §8.S2 compatibility object with the 22 unit-linear pivot
coordinates eliminated by exact substitution (unit pivot =>
isomorphism on the uW chart). Built FROM THE FROZEN row22compat
artifacts (no /tmp state) by FLINT pseudo-division (python-flint
0.9.0 nmod_mpoly; builder cases/directionb_row22red_build.py,
provenance + per-prime pivot log in cases/directionb_row22red.
rows.txt). Pivot identity is FROZEN-NAME, not positional: PIV22 of
cases/directionb_core23_{elim,emit}.py mapped through the D21
registry (x0-x15, x42-x45, x49, x50 <-> tf-names, row labels
Row_6..Row_20). Elimination order = Sol's item-2 safe order (3
cheap low -> 16 high -> 3 low), W-strip after every update; the 6
Schur rows are the ONLY substitution targets; 24 CORE2 rows + 2 uW
rows retained BYTE-IDENTICAL (they contain no pivot vars --
verified, which also dodges Sol's warned 4.97M-term wrong turn of
substituting into the ten pristine rows).

SHAPE + RECONCILIATION (coordinator's standing wrong-object
defense): **29 vars / 32 eqs / 12,654 terms per prime** (25 x-vars
+ W1,W2,uW1,uW2; 24 core + 6 reduced compat + 2 uW rows; ~276 KB)
-- EXACT match to Sol's independent read-only replay (xmodel/
sol-software2.md item 2), including the six-row sizes 1218 x5 +
1216, degree 9, the 25 x-vars containing CORE2's 18, and the
compat-term trajectory 26,256 -> 16,458 (3 low) -> 10,794 (19) ->
7,306 (22). The "~50v" task estimate resolves to 29v: 21 further
band variables occur ONLY through the pivot rows and drop out, so
V(row22compat) ~= V(row22red) x A^21 on the chart -- EMPTY iff
EMPTY, the depth-23 verdict is carried unchanged.

GATES (29 checks, 0 FAIL, x2 runs byte-identical; per prime):
(1) UNIT-NESS, exact, at time of use: every pivot coefficient is a
single monomial c*W1^a*W2^b, c != 0 mod p, row linear in its pivot
var (a,b identical across primes; table in rows.txt). Net unit
multiplier on each reduced row = CONSTANT (accumulated W1^11*W2^13
exactly cancelled by recorded strips): U = 23190 / 10684 / 116004
at 105337 / 105673 / 200257.
(2) ROUND-TRIP, 20 random trials per prime in the ambient chart
quotient (uW_i = W_i^-1, W_i != 0): unique unit back-solve of all
22 pivot coords (reverse at-use order); ALL 22 pristine artifact
pivot rows vanish at the lift; and reduced_j == U_j * full_j(lift)
EXACTLY on all 32 surviving rows, both sides via an independent
text parser on the two .ms artifacts -- both directions of the
correspondence (60/60 trials).
(3) FILL-IN: 12,654 terms << 150k cap (elimination SHRINKS: 3.8x
fewer terms, 43 fewer vars); degree profile banked (max total
degree 9 vs 2741-degree hazard of the old true-core presentation).
(4) Cross-prime support equality of all 30 nontrivial rows +
identical pivot (label,var) sequence; emission hygiene per
AUDIT.md (expanded/paren-free, coeffs in [0,p), independent-parser
round-trip, no bare-constant row, uW saturation carried).

LAUNCH (box01, 2026-08-18 20:28Z, pilot.log marker LAUNCH ROW22R
x3 12h-cap 6t): free -g showed 519 GB available (>= 300 gate);
scp'd with md5 match; 3 orphan-safe setsid lanes, timeout 43200,
msolve -g 2 -t 6, outputs row22red_p<p>.out. Verification: ps
count 9 (>= 3; = 3 lanes x sh/timeout/msolve, PIDs 57571-3).
Running row22compat (-t 4, ~8.6h in) and core23_ext (-t 8) lanes
UNTOUCHED. Semantics of the race: row22red [1] at a prime ==
row22compat [1] == the depth-23 kill on the chart; NONEMPTY
accepted only after full back-substitution (rows.txt DAG). If the
reduced lanes finish first, the verdict lands hours early plus a
free cross-check against the originals.

### 8.S5 det23: the determinantal projection of the D23 question (PROMOTED fiber-local/mod-p tier 2026-08-19; AUDIT entry + grok-det23-review CONFIRMED)

[2026-08-19 ~07:20Z; built + gated + emitted + launched this session.
INTERNAL / UNREVIEWED — no promotion claims. Scripts: session
scratchpad nfq/det23_{minors,rank2,sing,emit}.py + banked pkls.]

THE COMMISSIONED OBJECT. The 6 row22red compat rows reduce (8.S4 +
nf-quickshot) to NF_j = sum_k A_jk(x) tg_k + b_j(x), affine in the
4 level-44 tails (x17,x25,x32,x37) over the 22-var fiber ring. If
some tg solves all 6 rows at a fiber point x then rank[A(x)|b(x)] =
rank A(x) <= 4, hence every 5x5 minor of the 6x5 [A|b] vanishes at
x; so {397-el fiber GB + six 5x5 minors} EMPTY => row22red EMPTY
(same per-fiber-object scope). **The converse fails in general:
rank(A) can drop without solvability — minor vanishing alone NEVER
certifies a solution. This asymmetry must ride with every use of
the determinantal trick.**

MEASURED COLLAPSE (the asymmetry is TOTAL here). Payload structure:
each NF carries exactly ONE monomial per tg column, shared by all
six rows, so A = C*diag(uW1^2, uW2^2, uW1^2, uW2^2) with C a
CONSTANT 6x4 matrix — and **rank C = 2** (all 15 4x4 minors zero;
explicit nonzero 2x2 witness rows {24,25} cols {x17,x25}; identical
at all three primes). Hence **all six 5x5 minors of [A|b] are the
ZERO POLYNOMIAL** — verified by two independent flint routes
(Laplace vs cofactor factorization) AND by Singular det() from an
independent diff/subst re-derivation off the raw payload text. The
commissioned system is VACUOUS, exactly the rank-drop failure mode:
gate (a) at the 24-point kill set scores **0 points with >= 1
nonzero 5x5 minor, 24 all-zero**, while every one of those points
is UNsolvable (rank A = 2, rank [A|b] = 3 pointwise).

THE TRUE-RANK OBJECT (what was emitted + launched instead). On the
chart the uW_i are units (uW_i*W_i - 1 is in the fiber ideal;
re-verified reduce(uW_i*W_i-1, GB) = 0 in Singular), so rank A(x) =
rank C = **2 EXACTLY at every fiber point — the rank-drop escape
does not exist on this chart**. Exact linear algebra over F_p:
  exists tg solving the 6 rows at x
    <=> rank[A(x)|b(x)] = 2
    <=> ALL 3x3 minors of [A|b] vanish at x
    <=> u.b(x) = 0 for every u in leftker(C) (constant, 4-dim;
        contains the NF kernel vector a of 8.S4/nf-quickshot with
        a.b == 0 identically).
The condition space {u.b} is 3-dimensional; its RREF basis is THREE
tiny rows (w_s in leftker(C) recorded; g_s = w_s.NF exactly, tg
terms cancel):
  g1 = (x57-x65)^2*uW1^2 + c1*x53*uW1 + d1*x72   (5 terms, deg 4)
  g2 = (x57-x65)^2*uW2^2 + c2*x58*uW2 + d2*x72   (5 terms, deg 4)
  g3 = x70 + e*x72                               (2 terms, LINEAR)
with the quadratic part the perfect square (x57-x65)^2, integral
coefficients (1,-2,1) at ALL THREE primes — a char-0 pattern echo.
The 1218-term/deg-9 compat block compresses to 12 terms. Full 3x3
census: 80/200 minors nonzero (10 terms, deg 8 each), and every
nonzero one = unit-monomial * constant-combo of g1..g3 (verified
member-by-member), so {GB + g's} and {GB + all 3x3 minors} cut the
same chart variety.

SEMANTICS. V(det23) = proj_22 V(row22red) as chart-fiber sets:
**EMPTY <=> row22red EMPTY — an equivalence, both directions**,
because the rank of A is PINNED at 2 on the whole chart. (The kill
direction needs only =>; the converse is a bonus specific to this
rank pin. Any consumer who drops the pin must fall back to the
one-way reading stated above.) Scope unchanged: per-fiber at the
specialized radical_point base, per-prime, mod p; no variety-level
claim is made here — emptiness is what the launched runs decide.

GATES (23 rank-2 checks + 22 emission checks + Singular batch, 0
FAIL, x3 primes): payload re-parse struct (6x150 terms; x16/x24/x69
and x47/x52 absent; single shared tg-carrier per column); two det
routes agree; all six 5x5 == 0 (flint + Singular); rank C = 2 +
leftker dim 4 + a in leftker(C) + dim{u.b} = 3; w_s.NF == g_s exact
polynomial identities; 3x3 census + span membership; kill set 24/24
points have ALL THREE g's nonzero (profile [3]) vs 0/24 for the
5x5s; Singular independent re-derivation (ring (dp(22),dp(7)),
A/b via diff/subst, affine reconstruction 6/6, pinned 3x3 rows
{24,25,26} cols {x17,x25,b} 10 terms + g1..g3 COEFFICIENT-EXACT vs
flint); reduce(g_s, GB) sizes 5,5,2 (the g's are already normal
forms, NOT in the fiber ideal); chart saturation reduce(uW_i*W_i-1,
GB)=0, reduce(1,GB)=1; cross-prime g-supports/C-pattern/RREF-pivots/
census identical; AUDIT emission rules (paren sweep, max integer
token < p, independent-parser round-trip dict-exact on all 400
rows, satisfiability smoke: constant-bearing GB rows present, no
bare-constant row, GB block byte-VERBATIM = msolve .out elements).

EMISSION: cases/directionb_det23_p{105337,105673,200257}.ms — 22
vars (msolve fiber order), grevlex, 400 rows = 397 GB elements
VERBATIM (reduced-GB zero-cost engine prefix) + g1,g2,g3; 282,316
terms; 10.53–10.67 MB; construction, C, w_s, and semantics in the
.rows.txt companions.

LAUNCH (box01, 2026-08-19 07:14Z, pilot.log marker LAUNCH DET23 x3
48h 6t): free -g = 231 GB pre-launch (>= 150 gate); scp'd, md5 x3
match; 3 orphan-safe setsid lanes, timeout 172800, msolve -v 2 -g 2
-t 6, outputs det23_p<p>.out + .v2log telemetry, completion echoes
into pilot.log. Verified: ps count 9 (= 3 lanes x sh/timeout/
msolve, gate >= 3), msolve PIDs 63322-4 alive at 113% CPU on the
22-var input. **Caps expire 2026-08-21 07:14Z.** The running
row22red 12h lanes (caps ~08:28Z) untouched. Outcome reading: [1]
at a prime == the depth-23 kill on that prime's chart fiber (exact
equivalence, subject to this section's trust perimeter: the banked
GB, the 8.S4 row22red equivalence + payload gates, msolve/Singular/
flint arithmetic); NONEMPTY output = the compat-solvable sublocus
of the D21 fiber — direct depth-23 data either way.

VERDICT ADDENDUM (landed 2026-08-19 07:15Z, ~63 s/lane — the 48h
caps were never needed): all three lanes completed with rc=0.
**msolve reduced GB = 509 elements at EVERY prime — NOT [1].** The
det23 ideal is proper, so V(det23) is NONEMPTY over the algebraic
closure of F_p, and by this section's gated equivalence
**V(row22red) is NONEMPTY over the closure — the depth-23 exclusion
FAILS at the variety level on the radical_point chart fiber, at all
three primes (mod p).** Reconciliation with the 24-point kills: the
sampled F_p-rational points all miss the solvable sublocus; the
sublocus itself is a genuine variety (509-el basis, 405,524 terms,
3 linear elements, support identical element-for-element across the
three primes — the standard cross-prime genuineness echo). Outputs
banked: cases/directionb_det23_gb_p{105337,105673,200257}.out.txt
(md5-matched to box01; 15.2–15.4 MB). Dimension/degree of the
sublocus and F_p-rational point existence are NOT decided by -g 2
and remain open consumption items, as does the char-0 lift.
INTERNAL / UNREVIEWED; the racing row22red lanes are now a free
consistency cross-check (expect NONEMPTY there too).

### 8.S6 D23 witnesses: explicit depth-23 survivors from det23 (INTERNAL / UNREVIEWED)

[2026-08-19 ~07:43Z; the pre-registered NONEMPTY branch step 1,
executed this session (witness-extraction agent). INTERNAL /
UNREVIEWED — no promotion claims. SCOPE BOX, repeated on purpose:
one radical fiber (radical_point) of 36, residue-A B-frozen no-log
W1W2 != 0 chart with PIN42, per prime, mod p ONLY; chart-local; NOT
a family statement, NOT char 0. Within that box these are the FIRST
explicit depth-23 surviving configurations of the campaign.]

INPUTS. The banked det23 GBs (8.S5 addendum), local copies
re-md5-verified against box01 this session (0e4b9e58../0e957cc5../
9196..-919f61.. per prime); the frozen det23/row22red/row22compat
emissions (sha256s in the banked JSONs). Running lanes untouched
(row22red reds still live at PIDs 57571-3 during the work).

DIMENSION (LT staircase, all three primes). Exact max-independent-
set / min-hitting-set branch-and-bound on the 509 grevlex leading
terms: **dim V(det23) = 11 at 105337, 105673, AND 200257**, with
identical LT degree profiles (509 = 3 linear + 4 quadratic + ... +
2 deg-16), identical linear LTs {x52, x47, x70}, and the SAME max
independent set {x55,x58,x59,x60,x62,x63,x65,x66,x68,x71,x73}
(banked fiber GB control: dim 13 = |FREE|). **ANOMALY WORTH
FLAGGING: the three residual conditions g1,g2,g3 cut only
CODIMENSION 2 on the fiber (naive count 3) — one variety-level
dependency among the g's, identical at all three primes.** The
compat-solvable sublocus is a codim-2, dim-11 subvariety of the
13-dim fiber chart.

EXTRACTION (105337 and 105673; 200257 excluded per the 8.S3
measured W^4-pin obstruction — no F_p-rational chart point). The 1a
sampling discipline adapted to the det23 staircase: draw the 11
independent coords uniformly + the 7.S3 W-branch (4th-root x
i-power x sign, uW = W^-1), slicing to dim 0; solve the slice by GB
propagation (rows turning univariate; flint nmod_poly roots; DFS on
root branches). msolve was NOT needed (no propagation stalls, so
the sanctioned box01 0-dim fallback was never invoked; nothing run
locally either). **6/6 tries -> 6 points per prime** (target >= 5),
pairwise distinct, varied W-branches, seed 20260819.

VERIFICATION + RECONSTRUCTION (per point; all tiers PASS at 6
points x 3 tg-free/extras/band draws x 3 deep-kernel draws x 2
primes; python-flint evaluation, independent of msolve):
  T1 flint re-eval of the EMISSION: 397 fiber-GB rows + g1,g2,g3
     all vanish (400/400; output-GB 509/509 as well).
  T2 the six row22red compat rows at the point collapse to the
     affine system A tg = -b in (x17,x25,x32,x37) = (tg1_44,
     tg2_44, tg01_44, tg02_44); extras-(x16,x24,x69)-independent;
     A == C*diag(uW1^2,uW2^2,uW1^2,uW2^2) with the banked constant
     C re-verified pointwise; rank A = rank [A|b] = 2 — the RANK-2
     BACK-SOLVE, free tg columns {x32,x37}, 2-parameter tg family
     per fiber point (draws verified).
  T3 all 32 row22red rows vanish.
  T4 the 22 pivots back-solved from the PRISTINE row22compat pivot
     rows: the pivot block is BAND-TRIANGULAR with square affine
     groups 1(x42)+2(x44,x49)+3(x1,x9,x43)+4(x3,x11,x45,x50)+
     4(x0,x5,x8,x13)+4(x2,x6,x10,x14)+4(x4,x7,x12,x15) — weight
     purity forbids in-band pivot products; each group nonsingular.
  T5 ALL 54 row22compat rows vanish at the full 72-var witness —
     including the 6 compat rows: the depth-23 survivor signature.
  T6 registry map to the tf-chart: all 76 raw no-log D21 window
     rows vanish.  T7 valuation_e.verify_row22compat: 48/48
     membership + compat c = [0]*6 (the first non-synthetic
     traversal of the 1a survivor path; the banked 12 D21 points
     were 36/36 NOT_IN_DOMAIN).  T8 Row_22 deep solve at Schur
     rank 4 (as certified) x 3 kernel draws + verify_core23 77/77.

EXPERIMENTAL e (1b, all flag variants: pencil/weighted/rank x
tails/tailsW; ***every e is E_CANDIDATE (EXPERIMENTAL); the 1b
spec — series map + square block + surplus bridge — is STILL
UNBANKED; DEPTH-STAB e <= 11 is the eventual criterion and is NOT
tested here***): **ALL READINGS FAIL CLOSED at every witness,
every draw, both primes — no numeric e-candidate exists at window
depth D = 23.** Measured reasons, identical across primes: pencil
reaches full row rank 29/29 but the truncated-Smith valuation sum
is unstable under randomizing beyond-window coefficients (135/137
zero-fill vs 62 random-fill — the deep-tail columns are almost
entirely beyond-window at D=23); weighted/rank see Jacobian column
rank 35 (tails) / 37 (tailsW) of 77-80 columns — no nonvanishing
maximal minor, rank-deficiency consistent with the 11-dim survivor
locus plus free tg/kernel directions. Fail-closed is the honest
output of the pre-registered tool on a genuinely positive-
dimensional survivor family; a valuation verdict needs the banked
1b manifest and (likely) a deeper window.

BANKED: cases/d23_witnesses_p{105337,105673}.json — 6 witnesses
each with full 72-var coordinates (+ fiber/tg/extras/band split,
10 deep tails per kernel draw), all artifact sha256s, verification
transcript hashes, sampling metadata, dimension analysis, and the
fail-closed e diagnostics under the EXPERIMENTAL tag. Scripts +
transcripts: session scratchpad d23x/ (dim23/sample23/verify23/
phase6/bank23). No git; no fleet writes; red lanes untouched.

### 8.S7-ADDENDUM (2026-08-19 ~10:30Z): e=295 WITHDRAWN as corrected-object value
Sol round-6 adjudication (xmodel/sol-round6.md sect 1) + Grok review
(xmodel/grok-atlas-e-review.md, Object B): the eta29=0 lemma is refuted, the
corrected operator has 30 inputs/30 outputs with no free stream, and e=295
is WITHDRAWN as a value of the corrected object (it remains a correct
E_CANDIDATE diagnostic of the commissioned 29x29 object). THE SUBSTANTIVE
CONCLUSION STANDS in corrected form: exact all-30-stream replay through
t^40 certifies l+ >= 31 > 11 at all 36 sampled operators -- no DEPTH-STAB
germ certification is possible at D23 on this fiber. CYCLIC-30 retained as
an all-depth gate. The two 36es are distinct objects (36 atlas fibers vs
36 witness-draws); never conflate.

### 8.S7 Corrected valuation-e: the Euler/Ore operator at the D23 witnesses (INTERNAL / UNREVIEWED; every e is E_CANDIDATE (EXPERIMENTAL))

[2026-08-19 ~09:25Z; the round-5 corrected-e agent. INTERNAL /
UNREVIEWED — no promotion claims. ***PROMOTION GATE NOT PROVED:
sol-round5.md's CONJECTURE E-HENSEL (either an admissible
Theta-eliminating change of source coordinates, or the FILTERED
DIFFERENTIAL NEWTON LEMMA = completed-ideal bridge + delayed-
parametrix loss <= e + quadratic remainder => lifting for
D >= 2e+1) remains unbanked, and no exact Ore-Popov/Smith normal
form or causal periodic-recurrence closure is implemented; so per
sec 1.3 step 5 NO block promotes, strictly there is NO DEPTH e,
and every number below is an UNPROMOTED index/loss diagnostic
tagged E_CANDIDATE (EXPERIMENTAL). DEPTH-STAB e <= 11 is the
eventual criterion only; NO germ claims regardless of values.***
Scope box as 8.S6: one radical fiber of 36, residue-A B-frozen
no-log W1W2 != 0 chart with PIN42, mod p, chart-local.]

OBJECT (xmodel/sol-round5.md sec 1, implemented to the letter in
cases/valuation_e2.py). E = (theta Phi - 12 Phi) Gamma_eta -
Phi_eta (theta Gamma - 18 Gamma) + 42 t^20, Phi/Gamma the exact
normalized cyclic-orbit products (3 f-orbits / 6 g-orbits, B-side
frozen), rebuilt NUMERICALLY mod p over dual numbers (value +
gradient in the six build_generators tail streams) through the
gm_jet2/jrows construction; DBUILD = 42 (pure y-side, exact below
the t^42 x-side corrections; every quantity used lives at bands
<= 40, so the t^42 omission caveat never engages at this
truncation). Source points: the banked witnesses (draws[0].
witness72) + each recorded deep-kernel draw, deterministic ZERO
completion (uf30 = 0, level-51 x4 = 0, level-53 x4 = 0, all
levels >= 55 = 0; hashed; NO random fill). Held fixed: radical
branch, A_i, vf, W_i/HW_i chart units, uf dead-stretch, B-side;
PIN42 never a tangent direction; column mode tails (never
tailsW). Streams: 30 u-input residue streams (4*6 + 2*3, shifts
r_rho = 6+rho, r_4 = 16, sum 288) vs 29 eta-output streams (s_a =
6 + 2((a+1) mod 3), s_28 = 16, sum 240); per candidate free
stream c (fixed family order) the square 29x29 block B_c; scalar
entries dRow_(n,a)/dc_(q,r) used directly, with the Ore action
(O) verified as affinity in r.

GATES (all PASS at both primes; 2 intentional WARNs = the eta29
refutation below): G1 stream/shift/square-block constants (30/29,
288/240, 29N x 29N asserted per block); G2a eta^30..33 vanish
identically (value + derivative); G2c eta^29 confined to t^36
with the six residue-4 columns; G2d char-0 crosscheck (below);
G3a odd bands all vanish; G3b raw-label bijection (n,a) <->
(a,(n-s_a)/6) with n == s_a mod 6, n >= s_a — a band-41
regression of the cyclic-character grading, NOT an all-depth
proof; G4 the 29 support starts exactly s_a (incl. s_28 = 16);
G5 witness rows vanish at every band <= 22 (re-verifies the
banked witnesses through the measured deep-label identification);
G6 banked-pipeline cross-check: all 86 window-row derivative rows
(76 raw D21 pickle + 10 pristine Row_22) match the independent
valuation_e.py evaluation EXACTLY; G7 Ore structure: 2605
(a,fam,d) bins with >= 3 stream samples, ALL affine in r; G8
zeta-branch invariance (zeta -> zeta^5 rebuild identical); G9
second direct differentiation path (hand-assembled (L) == dual-
jet derivative); G10 band-22 deep block rank == 4 == the
certified Schur rank, at every point; G11 cross-prime: support
starts, Ore support pattern, and the witness-0 per-block
defect/e-index profiles IDENTICAL at 105337 vs 105673; G12
determinism: two independent full-run replays byte-identical
(modulo wall-clock), plus per-point operator/zero-completion
hashes banked.

STRUCTURAL FINDING 1 — deep-label identification (corrects the
DEEPMAP convention). The emission's x74..x83 deep-tail names
carried a tf-vs-tg split valuation_e.py documents as label-only/
not recoverable from the frozen artifacts. The exact source
constructor recovers it: matching the frozen core23 Row_22
derivative rows forces the involution (emission -> true stream)
  tf1_49<->tg1_49, tf2_49<->tg2_49, tf1_54<->tg02_54,
  tf2_54<->tg01_54, tg1_54<->tg2_54
(levels and W1/W2-side splits were already correct). Under this
identification, and only under it, the banked witnesses satisfy
every band <= 22 row of the reconstructed operator (G5/G6). The
nonzero kernel-draw-0 deep values therefore sit in the g-side
streams, not the f-side as the old labels suggested.

STRUCTURAL FINDING 2 — ***the all-depth cyclic-character lemma of
sol-round5.md sec 1.2 is REFUTED at eta^29***. E_29 is NOT
identically zero: its first occurrence is band t^36, with
derivative support exactly the six residue-4 streams' u^0
coefficients (level 48 — the C7-invariant levels == 0 mod 6, i.e.
the same residue class that PIN42 punctures). Confirmed in
CHARACTERISTIC 0 by the original exact machinery (r1_experiment
gm_jet2 + directionb_strike jrows, depth 37, all-zero-tails
configuration): the eta^29 t^36 coefficient of tf1_48 is the
rational number -147880611647231905314470776689/1024 (trivial
radkey, hence independent of every branch choice); numerically
re-verified mod both primes (gate G2d), and the six entries are
CONSTANTS (point-independent within a prime). At every banked
witness the eta^29 VALUE vanishes (a linear relation the
witnesses happen to satisfy), which is why D23-window data never
saw it. CONSEQUENCE: beyond band 22 the operator has 30 output
streams (H_29 start s_29 = 36; sum s_a = 276) against the 30
input streams — the spec's 29-output/one-free-input-stream
premise fails at depth, and with it the specific index formula
(V). The spec-literal 29x29 blocks are nevertheless computed
below as commissioned, with the eta29-augmented defects
delta_plus_eta29(N) recorded per block. eta^30..33 vanish to band
41 and every other clause of the grading held, so the lemma needs
only the E_29 clause repaired (or the row conjugated away) before
the square-block design can promote anything.

RESULTS (36 points = 6 witnesses x 3 deep-kernel draws x 2
primes; every number E_CANDIDATE (EXPERIMENTAL), nothing
promotes). Causal truncations M_c(N), N = 1..5 (bands <= 40, all
exact): defect profiles delta_c(N) = [24, 40, 52, 56, 56|57]
uniformly (rank 5, 18, 35, 60, 88-89 of 29N) — the low bands are
almost entirely syzygies, matching the banked observation that
the D21 elimination found only 3 pivots at bands <= 10.
  e-candidate distribution: e_cand = 295 at 27/36 points
  (argmin block tf1/r1, r_c = 7, d_c = 56, all three kernel
  draws of p105337 w0,w2,w3,w4,w5 and p105673 w0,w2,w4,w5);
  FAIL-CLOSED None at 9/36 (p105337 w1, p105673 w1, w3: the
  defect still drifts 57 -> 58 between N = 4 and 5, so no
  stabilized d_c is claimed). Stabilized-block index diagnostics
  span e_idx = 295..304 (= 6*56 + r_c - 48 etc.).
  ***0/36 points at or under the DEPTH-STAB threshold e <= 11.***
  Sharper, and certified within the band <= 40 window: the
  delayed-inverse-loss lower bound is ell_c >= 24 (range 24..31)
  at EVERY one of the 1080 blocks (30 x 36) — in-window coverage
  failures are genuine lower bounds for (P) because the operator
  is causal (measured: no entries with n < r), inputs above the
  window cannot reach bands <= 40. Since promotion demands
  0 <= ell_c <= e_c^idx, every block hits the sec-1.3 stop rule
  (certified bound > 11): under this object no promoted e <= 11
  can exist at these witnesses at this truncation. The old
  pencil/tails 135/137-vs-62 instability is thereby superseded by
  an exact, stable, deterministic measurement of the corrected
  object — and the corrected object says the witnesses are
  nowhere near the DEPTH-STAB window.
  Augmented (measured-grading) defects delta_plus_eta29(N) =
  delta(N) + 1 wherever the eta29 row is independent (profiles
  25/26, 41/42, 53/54, 57/58, 57..59) — the extra output only
  deepens the deficit.

ANOMALIES WORTH FLAGGING: (i) the eta^29 refutation (finding 2)
— changes the round-5 design premise; (ii) witness-1 (both
primes) and p105673 witness-3 defects not stabilized at N = 5:
witness-level rank variation inside the same chart; (iii) the
banked witnesses' deep_draws carry "schur_rank": 29 — a shadowed
variable in the 8.S6 phase6.py (the rank-4 assert did run; the
recorded 29 is the pencil matrix rank), label-only; (iv) e_idx
~ 295-304 vs sol-round5's implicit d_c ~ 7-9 expectation: the
accumulated causal defect is an order of magnitude larger than
the design anticipated; any promoted-e discussion needs the
Ore-Popov normal form the spec calls for, on the REPAIRED
30-output grading.

BANKED: cases/d23_ecandidates.json (sha256 d0a52d432eee538b..,
3.1 MB): per point (prime, witness, kernel draw) the zero-
completion + operator hashes, all gate outcomes, the 30 per-block
records (delta profile, delta_plus_eta29, d_c, E_INDEX e_idx,
E_LOSS ell_window + full ell profile, weighted-pivot checksum,
stopped/consistent flags, promoted: false), the eta29 refutation
data, deep-label identification, distribution, and the witness-
file sha256s. Tool: cases/valuation_e2.py (--selftest, --gates,
--point, --run; ~5 s/point). Logs: session scratchpad e2run{1,2,
3}.log + cmp_runs/analyze_e2 scripts. msolve not used; box01
untouched; no git; nothing outside cases/ + this sheet + notes.

### 8.S8 The 36-fiber D23 atlas (INTERNAL / UNREVIEWED)

[2026-08-19 ~09:30Z; the pre-registered fiber-to-family lift step
(sol-round5 §3.4: atlas BEFORE any D25 work), executed this
session. INTERNAL / UNREVIEWED — no promotion claims. SCOPE BOX:
per radical fiber, per prime, mod p ONLY; residue-A B-frozen no-log
W1W2 != 0 chart with PIN42; chart-local; NOT char 0; says nothing
about other charts, D25, or DEPTH-STAB germ certification.]

THE OBJECT. The D21 window's radical base has 3*3*2*2 = 36 finite
components (7.S3 G0.7): A1 among the three cube roots of 3+r3, A2
among the three of 3-r3, HW_i/W_i = ±h32 (2h32^2 = 3), at the
fixed split-prime embedding r3. 8.S5 decided depth-23 nonemptiness
on ONE of them (radical_point). This section runs the identical
gated chain on the other 35 and tabulates all 36. Fiber labels
a{i}{j}{u}{v}: A1 = A1_0 w^i, A2 = A2_0 w^j (w the smaller
primitive cube root of 1 mod p; A1_0, A2_0 the radical_point
roots), u,v = the HW1, HW2 signs (p/m); radical_point = a00pp.

CONSTRUCTION (per fiber, every step from FROZEN artifacts; scripts
session scratchpad atlas/, banks + all 36 .ms/.out per stage).
(1) directionb_core2_p105337.ms (unsplit CORE2, radgens symbolic)
folded at the fiber; sequential forward echelon in the byte-pinned
convention — the a00pp output reproduces the banked
directionb_core2_fiber_p105337.ms BYTE-IDENTICALLY (regression
anchor) — giving 24 rows + 2 uW rows, 5,344 terms at EVERY fiber;
span-closure gate (echelon ideal == folded ideal) per fiber.
(2) msolve -g 2 -t 4 fiber GB on box01 (35 lanes, ~11 s each,
marker ATLAS FIBGB, rc=0 x35). (3) the 10 pristine Row_22 rows of
directionb_core23_p105337.ms folded at the fiber; A = C10 diag(u)
polewise factorization with rank(C10) = 4 at ALL 36 fibers (the
8.S2 Schur gate replayed per fiber, L C10 = 0 certified); c = L b;
then the 22 unit pivots eliminated by pseudo-division (row22red
analogue; G1 unit-ness at time of use + 5-trial G2-lite round-trip
per fiber; a00pp reproduces the banked row22compat AND row22red
rows dict-exactly). All 36 reduced compat blocks: 1218 x5 + 1216
terms, the SAME support as a00pp. (4) Singular NF of the 6 reduced
rows against that fiber's GB, block order (dp(fiber22) >>
dp(extras7)) per the nf-quickshot contract, msolve order pin
(gate A: DRL-max monic + interreduced) re-verified per fiber;
a00pp NF payload == the banked nf_reduced_rows_p105337.txt.
(5) affine split in the level-44 tails (x17,x25,x32,x37); C 6x4
CONSTANT with carriers (uW1^2,uW2^2,uW1^2,uW2^2); **rank C = 2
CHECKED at every fiber** (the pre-registered anomaly trigger never
fired); leftker dim 4; {u.b} dim 3; RREF rows g1,g2,g3 with
w_s.NF == g_s exact; a00pp g rows == the banked det23 rows
398-400, and the emitted a00pp det file is BYTE-IDENTICAL to the
banked cases/directionb_det23_p105337.ms. (6) det system = fiber
GB VERBATIM + g1,g2,g3; msolve -g 2 -t 4 on box01 (35 lanes,
~65 s each, marker ATLAS DET23, rc=0 x35); dimension by the exact
LT-staircase min-hitting-set (8.S6 machinery). Spot G-C: at 4
non-radical fibers (a11pm, a20mp, a02mm, a10pp), row == NF at 72
(V(GB)-point, extras-draw, row) combos each, rank A(x) = 2 at
every sampled point, and g = 0 <=> affine solvability pointwise.

THE ATLAS (p = 105337; per-fiber rows, hashes, g rows, w vectors,
and mod-p fiber data in cases/d23_atlas_p105337.json, 87.5 KB):

  **all 36 rows of the atlas table are IDENTICAL in every recorded
  structural field** — the table is its own compression:

  fiber(s)      | D21 GB      | det23 GB    | verdict
  --------------+-------------+-------------+------------------
  a{ij}{uv},    | 397 els     | 509 els     | NONEMPTY
  all 36 combos | dim 13      | dim 11      | (36/36; 0 EMPTY,
  incl. a00pp   | 282,304 t   | 405,524 t   |  0 anomalies)

  - D21 fiber GBs: ONE full-support class (element-for-element,
    printed order; sha256/16 a9498f3c39e50803) x36; linear LTs
    {x52, x47}; max independent set = the 13 of 7.S4, identical.
  - det23 GBs: ONE full-support class (e2c2e64ef0014d15) x36;
    509 = 3 linear (x52, x47, x70) + 4 quad + ... + 2 deg-16
    (the 8.S6 profile, identical); max independent set = the same
    11 coords {x55,x58,x59,x60,x62,x63,x65,x66,x68,x71,x73}.
  - NF payload: 150 terms x6 rows, rank 5 (kernel dim 1), affine
    in the level-44 tg's, x16/x24/x69 cancel — at every fiber.
  - g rows: supports identical x36; quadratic part the perfect
    square (x57-x65)^2 with integral (1,-2,1) at every fiber;
    g's cut CODIMENSION 2, not 3 (13 -> 11) at every fiber — the
    8.S6 one-dependency anomaly is a FAMILY-WIDE structure, not a
    radical_point accident.

CROSS-FIBER TRANSPORT DATA (for the sol-round5 §3.4 transport
search; coefficients from the banked atlas JSON): the only
variation across the 36 fibers is coefficient values, and they
organize by characters of the fiber group:
  g3 = x70 + e*x72 with e taking exactly THREE values, constant
    on (j - i) mod 3 classes (12 fibers each);
  g2 = f(j, s2) — SIX coefficient classes of 6 (independent of
    the A1 root index i and of s1);
  g1 = f(i, j, s1) — EIGHTEEN classes of 2 (independent of s2).
  (Class structure of the RREF-canonical rows; the underlying
  {u.b} space, not the basis choice, is the invariant object.)
All 36 det .ms files pairwise distinct (36 md5s) — these are 36
genuinely different specializations with one shared skeleton.

FAMILY-LEVEL STATEMENT SUPPORTED (stated exactly, honest tier):
**at p = 105337, on EVERY one of the 36 radical fibers of the D21
window, V(fiberGB + g1,g2,g3) is a proper, NONEMPTY (over the
algebraic closure of F_p) subvariety of dimension 11 = 13 - 2;
by the per-fiber gated rank-2 equivalence (8.S5 semantics,
re-certified fiber-by-fiber) the depth-23 Row_22 obstruction
eliminates NO radical fiber: each of the 36 carries an
11-dimensional depth-23 survivor locus mod p.** This is the
Tier-1 target of sol-round5 §3.4 (proper D23 projection, maximal
dimension drop two, same initial staircase — here strengthened to
full support identity). What this does NOT say: nothing about
char 0, about primes other than 105337 (except the banked
three-prime a00pp chain), about other charts, about D25, or about
germ certification (Conjecture E-HENSEL untouched). Per-fiber
NONEMPTY means: there exist depth-23-surviving D21 configurations
over F_p-bar on that fiber (the 8.S5 both-directions semantics,
whose rank-2 pin was re-verified per fiber); it does NOT by
itself exhibit F_p-rational witnesses off a00pp (not attempted).

p105673 STATUS: no EMPTY and no anomalous fiber arose, so the
mandated second-prime spot-checks were VACUOUS. The 105673
stage-1/stage-3 banks were built anyway and their a00pp
regressions PASS (fiber emission byte-identical to the banked
directionb_core2_fiber_p105673.ms; compat/row22red dict-exact),
ready for a full second-prime replication if commissioned.

PROVENANCE: box01 ~/jc72108/atlas/ (35 fib_*.ms + .out, 35
det_*.ms + .out, lane scripts; pilot.log markers LAUNCH ATLAS
FIBGB 08:52Z, LAUNCH ATLAS DET23 09:10Z, 70 rc=0 lines); local
copies + stage banks in session scratchpad atlas/ (e1e34384);
md5s of every shipped/fetched artifact verified both directions;
per-fiber md5s in the atlas JSON. Runtime: ~6 min box01 solver
wall (3 lanes), ~35 min local flint/Singular chain. Nothing else
on box01 touched; no local msolve; no git.

SECOND-PRIME ATLAS (p = 105673; 2026-08-19 ~10:50Z — the
promotion-gap run commissioned after grok-atlas-e-review.md rated
the missing second prime HIGH for promotion; Object A finding 1).
The identical gated chain (stages 1-6, same scripts, same
pre-registered anomaly triggers) replayed at the second split
prime from the banked stage-1/stage-3 material above:

  **VERDICT COUNTS at p = 105673: 36/36 NONEMPTY, 0 EMPTY,
  0 anomalies** — the table is identical to the p = 105337 one in
  every recorded structural field: D21 fiber GB 397 els / dim 13 /
  282,304 terms and det23 GB 509 els / dim 11 / 405,524 terms at
  EVERY fiber; one LT-multiset class at both tiers; the same
  11-coordinate max independent set {x55,x58,x59,x60,x62,x63,
  x65,x66,x68,x71,x73}; rank C = 2 at every fiber (the anomaly
  trigger never fired); NF payload 150 terms x6, rank 5; g rows
  (5,4),(5,4),(2,1) with the (x57-x65)^2 integral square; g's cut
  codim 2 (13 -> 11) family-wide. The depth-23 Row_22 obstruction
  eliminates NO radical fiber at EITHER split prime.

  - a00pp regressions vs the banked p105673 artifacts, all exact:
    fiber emission byte-identical to directionb_core2_fiber_
    p105673.ms; NF payload == nf_reduced_rows_p105673.txt; g rows
    == directionb_det23_p105673.ms rows 398..400; det emission
    BYTE-IDENTICAL to the banked det file; det GB md5 == banked
    directionb_det23_gb_p105673.out.txt (0e957cc56528355d...).
  - COPY-ATTACK GATES (gates673.py; the grok-atlas-e-review A1/A2
    battery as explicit second-prime gates, 8 checks 0 FAIL):
    36/36 pairwise-distinct md5s at all four artifact tiers
    (fib .ms, fiber GB .out, det .ms, det GB .out); 3 coefficient
    classes on the first fiber-GB polynomial (a copied prefix
    would give 1); det-GB monomial support element-for-element
    IDENTICAL ACROSS THE TWO PRIMES (banked a00pp pair + 4 remote
    probes); every det GB a 509-element proper basis (no constant
    => 1 not in ideal => NONEMPTY over F_p-bar).
  - Class laws replayed exactly at p105673: g3 = x70 + e*x72 with
    3 values on (j-i) mod 3 (a00pp e = 9676); g2 6 classes on
    (j,s2); g1 18 on (i,j,s1).

WHAT THIS CLOSES: the single-prime promotion gap of
grok-atlas-e-review (A4/A7 finding 1) — the 8.S8 family statement
now holds verbatim at TWO split primes with disjoint solver runs
and byte-level a00pp regressions at each. What it does NOT close:
the A6 consumer hazard is only reduced (all 36 NF payloads are now
banked for both primes, session scratchpad nf_p10533{7}/
nf_p105673/, still not in-repo), and any char-0/scheme-level
reading still owes the A4 good-reduction lemma. Scope: mod p,
chart-local, primes 105337 + 105673 (+ the banked three-prime
a00pp chain) only.

PROVENANCE (second prime): banked cases/d23_atlas_p105673.json
(87.5 KB, same schema); box01 ~/jc72108/atlas/ fib/det
*_p105673.* (pilot.log markers LAUNCH ATLAS673 FIBGB x35 10:07Z
and LAUNCH ATLAS673 DET23 x35 10:26Z; 70 rc=0 lines; 3 lanes
each; ~11 s/fiber GB, ~2 min/det GB); a00pp NOT re-solved (banked
GBs reused; 35 = 36 - 1 discipline); md5 verified both directions
on every ship/fetch; local Singular stage-4 chain 1,369 s, 0
FAIL. Nothing else on box01 touched; no local msolve; no git.

## 9. FAMILY D25: the master emission + the discriminating solves (INTERNAL / UNREVIEWED)

[2026-08-19 ~23:40Z; the sol-round6 family-D25 compiler, rebuilt after
the 15:05 session-restart loss per the fleet+checkpoint doctrine and
executed end-to-end this session. INTERNAL / UNREVIEWED -- no
promotion claims. SCOPE BOX: mod p at the two split primes 105337 and
105673 ONLY; residue-A B-frozen no-log PIN42 W1W2 != 0 chart at the
fixed r3 embedding; chart-local; NOT char 0. Driver: cases/
d25_assemble.py (COMMITTED location; runs on box01), consuming the
D25RED bank (cases/d25_reduce.py, 906/906 checkpoints).]

THE OBJECT (xmodel/sol-round6.md sect 2, implemented to the letter).
Per prime, ONE master family object over the split etale coefficient
algebra B36 = F_p[A1,A2,h1,h2]/(A1^3-(3+r3), A2^3-(3-r3), 2h1^2-3,
2h2^2-3) ~= F_p^36 (36 idempotents = the 36 atlas radical fibers):

  J25 = I23 + <R_1..R_5>,  per fiber:  26-row D21 core + g1,g2,g3
  + FIVE Schur residuals   =  34 eqs / 28 vars = 22 det23 base
  + 6 surviving lift vars {x16,x24,x19,x27,x33,x38} = {tg1_43,
  tg2_43, tg1_46, tg2_46, tg01_46, tg02_46}
  -- EXACTLY the predicted (22+r)/(29+s) shape with s = 5 <= 5, r = 6.

CONSTRUCTION (all from frozen/banked artifacts + the D25 jets bank):
(1) shared pristine Row 24: the bank's nine k=24 cells; Row 23 == 0;
eta support {2,5,...,26}; frontier census 10/10; the 90-entry
first-occurrence digest REPRODUCED EXACTLY (sha256 ab5ee038.., the
sol_algkill.py::check_row24 serialization, len 10800). (2) the
factorization A24 = C24 diag(A1W1, A1^2, A2W2, A2^2, A1HW1, A1^2,
A2HW2, A2^2, A1^2, A2^2) holds ENTRY-EXACTLY at radkey level with
zero per-row W-normalizers; C24 constant 9x10, rank 4, pivot columns
{0,1,2,3}; L24 = the canonical-RREF rank-5 left kernel (per-prime
mod-p serialization sha256s in the manifests) -- ONE universal Schur
transform to five residuals c_nu = L24.b24 on all 36 fibers. (3) the
D23-manifest reconstruction DAG replayed family-wide over the bank:
22-pivot at-use cascade (G1 unit-ness at every use, forms NF-reduced
through the fiber's cached 509-el det23 G23), level-44 unit 2x2 solve
of (x17,x25) with (x32,x37) free (rank C44 = 2, pivots [0,1] at every
fiber), Row-22 rank-4 deep solve in the CORRECTED sol-round6 1.3
registry (solved tg02_54, tg01_54, tg2_49, tg1_49; kernel tg1_54,
tg2_54, tf1_54, tf2_54, tf1_49, tf2_49; solve sizes 588/588/747/888
terms -- reproducing the lost run's ~588-term telemetry), substituted
ONLY into the five Schur rows per spec 2.5. (4) coefficientwise NF
through the 36 cached G23 bases (support-identical skeleton, one
leading-monomial index); residuals 144-148 NF terms per fiber.

STRUCTURAL FINDINGS. (i) Row_22^{D25} == Row_22^{D23} and the 22
pivot rows match the frozen core23 pristine rows DICT-EXACTLY (unit
scale 1) -- the level-cap structure holds; bands <= 22 carry NO
new-at-D25 variables, so the D23-truncation is the identity there.
(ii) EXCEPTION THAT PROVED THE REGRESSION: the jets bank OMITS the
+42 t^20 no-log pin constant (sol-round5 E-object "+ 42 t^20") in
cell (20,0) -- caught by the frozen-artifact comparison (the only
discrepancy in 32 rows: one bare constant 42 at scale 1), restored in
assembly, and afterwards every witness gate passed. (iii) the five
residuals survive on ALL 36 components (five all-ones masks; no
idempotent splits were needed: every intermediate pivot/carrier was a
family unit). (iv) the kernel-6 deep tails, x32/x37, uf24/uf30, and
every level-48+ coordinate CANCEL out of the final residuals: the
D25 obstruction to Row 24 lives entirely over the 22 det23 base plus
the six shallow lift coordinates above.

MANDATORY GATES (all PASS, x2 primes, identical structure):
  shape reconciliation vs sol-round6: (22+6) vars / (29+5) eqs,
    s = 5 <= 5; max residual 148 terms << the 50k sparse cap;
  witness-truncation regression: all banked d23_witnesses points
    satisfy the D25 system's D23-truncation componentwise -- 1566
    row evaluations == 0 per prime (bands <= 20 x 6 witnesses x 3
    band draws; band 22 x 3 kernel draws on draw 0, the draw the
    banked deep solves were recorded against; corrected deep-label
    involution load-bearing: the old-name control fails 9/10 rows);
  component count 36: selector algebra has 36 distinct evaluations,
    radical laws A1^3 = 3+r3, A2^3 = 3-r3, 2h^2 = 3 at every fiber,
    evaluation/interpolation round trips EXACT for all 34 family
    rows x 36 labels x 2 primes;
  Schur rank 4: rank C24 = 4 verified per prime (pivots 0-3), L24
    complete rank-5 left kernel, L24 kills the folded frontier block
    at random points (2/2 per fiber), rank C10 = 4 with the solved-4
    columns full-rank;
  plus: 90-entry digest MATCH; forward inclusion NF(26 core + 3 g)
    == 0 on every fiber; kernel compat closure u.b44 == 0 mod I23
    (4/4) and full compat closure (6/6) -- Row 22 adds NOTHING to
    I23 at D25; fiber .ms md5s == atlas JSON; core support skeleton
    identical x36; AUDIT emission hygiene (paren-free, coeffs in
    [0,p), independent-parser round trip dict-exact on all 38 rows,
    no bare-constant row); 36 parked per-fiber specializations
    pairwise-distinct md5s.

EMISSION (per AUDIT.md rules; one file per prime + 36 parked):
cases/d25fam_p{105337,105673}.ms = the selector-variable union
system (sol-round6 2.5/2.6 flattening): 38 rows = 26 core + 3 g + 5
residuals (each interpolated through the 36-point radical algebra)
+ 4 selector defining rows; 32 vars = 6 lift aliases + the 22 det23
base + A1r, A2r, h1r, h2r; 6,104 terms / 0.17 MB per prime; md5
feacc800ea5d0583f1cf823c2b203936 / e3009eb7e98603469835017aa6c89f84
(box01-fetched, matched both directions). Its variety is the exact
disjoint union of the 36 fiber quotients. Manifests: cases/
asm_manifest_p{105337,105673}.json (C24/L24/C10/L10, serialization +
RREF rule, carriers, masks, per-fiber gate record, per-fiber md5s).

LAUNCH (box01, 2026-08-19 23:39:08Z, pilot.log marker LAUNCH D25FAM
x2 48h 8t): free -g = 979 GB pre-launch; 2 orphan-safe setsid lanes,
timeout 172800, msolve -v 2 -g 2 -t 8, outputs d25fam_p<P>.out +
.v2log, completion echoes "D25FAM p<P>: rc=.. size=.." into
pilot.log. Verified: ps pattern "[m]solve.*d25fam" count 8 >= 2
(2 msolve PIDs 90409/90410 + wrappers). **Caps expire 2026-08-21
23:39:08Z.**

THE DISCRIMINATION LOGIC (xmodel/sol-round6.md, quoted VERBATIM;
this section's verdicts are to be read against it and nothing else):

> ## 3. The exact D25 discrimination logic
> 
> Let
> 
> \[
>  V_{25}=\bigsqcup_{\lambda\in\Lambda}V_{25,\lambda}
> \]
> 
> denote the variety defined by the exact family object, with quotient/backsolve equivalence and every chart guard certified.
> 
> ### 3.1 D25 EMPTY
> 
> If $J_{25}^{B}=(1_B)$, equivalently every one of the 36 specializations is `[1]`, then
> 
> \[
>  V_{25}=\varnothing.
> \]
> 
> Every formal germ has a depth-25 truncation. Therefore:
> 
> > **THEOREM AT THE STATED SCOPE:** family-wide D25 EMPTY proves that every D23 survivor was a finite-depth mirage and that no mod $p$ formal germ exists on the residue-A, B-frozen, no-log, `PIN42`, $W_1W_2\ne0$ chart at that prime and the atlas's fixed $r_3$ embedding.
> 
> This kill direction uses neither valuation $e$, CYCLIC-30, nor E-HENSEL. One empty component kills only that component. A union-level NONEMPTY result does not show that all components survive, which is why the 36-bit mask is mandatory.
> 
> D25 EMPTY is the point at which the residue-A kill campaign **resumes**, not the point at which a characteristic-zero theorem may already be announced. Repeat the exhaustive family calculation at a second good prime, then seek an exact $\mathbf Q(\sqrt3)$ identity with source-row provenance and discharge the conjugate $r_3$ embedding, other charts, no-log/`PIN42` coverage, and B-unfreezing. Modular emptiness alone is a screening-tier result.
> 
> ### 3.2 D25 NONEMPTY
> 
> D25 NONEMPTY proves only that at least one point of $V_{25}$ projects to the D23 survivor locus. It deepens finite-window survival; it does not produce an inverse-limit point, a formal germ, a characteristic-zero germ, an algebraic branch, or a polynomial Keller pair.
> 
> For every surviving component, record the image and fiber dimensions of
> 
> \[
>  \pi_{25,23}:V_{25,\lambda}\longrightarrow V_{23,\lambda}.
> \]
> 
> A severe image contraction is useful mirage evidence, while a positive-dimensional image shared across the coefficient classes is germ-track evidence. Neither is a theorem about infinite depth.
> 
> ### 3.3 The corrected $e$-test at D25
> 
> The D25 threshold is
> 
> \[
>  \left\lfloor\frac{25-1}{2}\right\rfloor=12.
> \]
> 
> Recompute the exact low-band part of $L_s^+$ at genuine reconstructed D25 points using the true deep labels. A finite D25 point does **not** determine its $t^{42+}$ x-side completion. Before following $H_{29}$ beyond its first coefficient, do one of three things: use a sufficiently long explicitly compatible lift that supplies every coefficient consumed; prove a finite-range invariance lemma; or retain and quantify over the unspecified completion variables. Never silently zero-fill them.
> 
> Track compatible points
> 
> \[
>  s_{25}\leftarrow s_{27}\leftarrow s_{29}\leftarrow\cdots,
> \]
> 
> not unrelated random witnesses or unrelated zero completions. Only an all-depth compatible chain, or a proved finite-determinacy result, supplies an all-depth operator.
> 
> | corrected D25 behavior | exact conclusion |
> |---|---|
> | A **promoted** $e^+(s)\le12$, with CYCLIC-30, an exact delayed parametrix, the completed-ideal bridge, and E-HENSEL banked | A mod $p$ formal germ exists: decisive germ-track. |
> | A stable, internally consistent `E_CANDIDATE^+ <= 12` with measured \(\ell^+\le12\) | Strong germ-track evidence; no theorem. |
> | Finite promoted $e^+(s)>12$ | D25 is too shallow; target $D=2e^+(s)+1$. |
> | Certified \(\ell^+(s)>12\) | This point cannot supply a D25 Hensel certificate; it may still extend singularly. |
> | Drifting/unbounded \(\delta^+(N)\), resonance, or $e^+=\infty$ | Mirage-like or singular-track behavior; not a kill. |
> | Some later exact window is EMPTY | Definitive finite-depth mirage. |
> 
> Thus a small promoted $e^+$ distinguishes germ-track as a theorem; no large-$e$ observation distinguishes mirage as a theorem. The empirical germ-track signature is a bounded, stabilized defect and delay along one compatible chain, eventually with $D\ge2e^++1$. The empirical mirage signature is continued image contraction plus growing defect/loss, followed ultimately by EMPTY. A genuinely singular formal germ can imitate the latter until very deep order.
> 
> A locus-wide claim that no D25 point has $e^+\le12$ requires symbolic stratification of every D25 component. Witness sampling cannot prove it. If the present \(\ell^+\ge31\) obstruction persists at a D25 point, then any finite-$e$ target for that point is at least D63; this is not itself evidence of nonextension.
> 

VERDICT SLOT: lanes running at write time; rc/size echoes land in
box01 pilot.log; outcome to be banked here by the consuming session
under the quoted logic (36-bit mask semantics: the union GB decides
all-EMPTY at once; a NONEMPTY union output is specialized through
the 36 parked per-fiber systems for the componentwise mask).
PROVENANCE: box01 ~/jc72108/d25/{directionb_tails_D25.pkl, ckpt/
(906), asm/ (72 + 2 asmB), asm_p<P>.log}, ~/jc72108/d25fam/ (2 union
+ 72 parked .ms + manifests); local copies md5-verified. No git; no
local msolve; the running lanes untouched by everything above.

### 9.S1 The per-fiber race decomposition (INTERNAL / UNREVIEWED)

[2026-08-20 ~16:20-17:50Z; the race hedge commissioned while the
union D25FAM lanes ground at F4 round 9 (~580k-row matrices, 17h in).
INTERNAL / UNREVIEWED. SCOPE BOX: p = 105337 ONLY (second-prime
spot-checks at 105673 reserved, atlas discipline: only for an EMPTY
or anomalous fiber, none arose); same chart/scope as section 9.]

THE OBJECT (cases/d25_perfiber.py, runs on box01; atlas 8.S8
pattern "fiber GB VERBATIM + new rows"): per fiber,

  d25pf_p105337_<label>.ms = the fiber's 509-el det23 GB G23
    (gbcache == banked atlas det GB) + the 5 D25 Schur residuals of
    the parked d25fam_p105337_<label>.ms  =  514 rows / 28 vars
    (22 det23 base + 6 lift aliases x33,x38,x16,x19,x24,x27),

plain F_p coefficients, so each solve starts from the banked
depth-23 GB instead of re-grinding the D23 core.

UNION-vs-PERFIBER EQUIVALENCE (stated precisely): per fiber,
ideal(G23 + R_1..R_5) = ideal(26 core + 3 g + R_1..R_5) = the
<label>-component of the union system, because (a) G23 is the
banked atlas det23 GB of <26 core + 3 g> (8.S8, both primes,
md5-gated), (b) NF_G23(26 core + 3 g) == 0 was RE-verified per
fiber at emission (GATE-PF3, 29/29 x36), and (c) the union rows
specialize dict-exactly to the parked per-fiber rows at every
fiber's selector values (GATE-PF2, independent parser, 34 rows x
36 fibers + 4 selector rows vanishing). Hence the componentwise
verdicts of the union system equal the per-fiber verdicts, and the
two lanes are exact cross-checks of one another.

EMISSION GATES (2026-08-20 16:21Z, all PASS, wall 22 s): PF1 md5s
vs asm_manifest + gbcache support skeleton identical x36; PF2 as
above; PF3 as above; PF4 witness truncation -- the banked a00pp
D23 witnesses satisfy the emitted D25 system's D23-truncation:
9162 G23-row evaluations == 0 over 18 banked witness draws; PF5
AUDIT hygiene (paren-free, coeffs in [0,p), no bare-constant row,
independent reparse dict-exact on all 514 rows x36, 36 pairwise-
distinct md5s). Cross-host regression: the a00pp emission built
independently on the local machine and on box01 is byte-identical
(md5 179d1ad59a7aeeb5a204050d8d8cd035).

THE RACE RESULT + REDIRECT (2026-08-20): batch-1 of the 36-lane
race (4 lanes x msolve -g 2 -t 4, cap 3600 s, markers D25PF) ran
a00mm/a00mp/a00pm/a00pp: ALL FOUR rc=124 at the caps (secs
3601-3602, 0-byte .out never read as verdicts; v2log telemetry
shows F4 round ~9, ~1.2M x 2.9M matrices at ~11 GB RSS -- the
per-fiber systems are mid-weight at D25, NOT the 63-s D23 scale).
REDIRECT per the support-identity logic: 8.S8 shows one GB support
skeleton and one term profile across all 36 fibers, so per-fiber
difficulty is expected uniform -- 36 one-hour timeouts carry no
more information than 4. The 4/4 UNIFORM 1h-timeout table IS the
banked batch result (evidence of uniform mid-weight difficulty);
batch-2 (a01**, ~30 min in) was cancelled by literal inspected
PIDs (no pattern kills), and ONE representative fiber -- a00pp,
the historically banked one -- was relaunched at a 24 h cap:
LAUNCH D25PF1 a00pp p105337 24h t8 2026-08-20T17:48:31Z (marker
D25PF1; cap expires 2026-08-21T17:48:31Z). The union D25FAM lanes
(PIDs 90409/90410) and the l44 union lane were UNTOUCHED
throughout and continue as the primary verdict routes.

VERDICT TABLE (banked cases/d25_perfiber_p105337.json): 0 EMPTY /
0 NONEMPTY / 4 TIMEOUT@3600s (a00mm, a00mp, a00pm, a00pp) / 32
CANCELLED (redirect); no dims yet (no fiber GB completed). Verdict
semantics unchanged from section 9 (sol-round6 sect 3, 36-bit
mask); dimension tooling = the exact LT-staircase min-hitting-set
(cases/d25pf_verdict.py; regression: reproduces the banked det23
dim 11 and the exact 8.S8 max independent set on the banked a00pp
det GB). PROVENANCE: box01 ~/jc72108/d25pf/ (36 .ms + ck/ + out/ +
pf_manifest_p105337.json + verdicts_p105337.json), pilot.log
markers LAUNCH D25PF x36 16:22:11Z / 4 rc=124 lines / CANCELLED
17:47:59Z / LAUNCH D25PF1 17:48:31Z; scripts cases/{d25_perfiber.
py, d25pf_run.sh, d25pf_lane.sh, d25pf_verdict.py, d25pf1_run.sh}
shipped md5-verified both directions. No git; no local msolve.

### 8.S6-CORRECTION (2026-08-19): the dependency claim was wrong
The 8.S6 statement that the three residual rows carry "rank 5 ... one
cross-prime-identical dependency" is RETRACTED: two independent
recomputations (xmodel/sol-conjecture-k.md; confirmed hostile,
xmodel/grok-k-g5-review.md target A) show g1,g2,g3 have NO constant-linear
dependency at any of the 72 atlas fibers. The codim-2 cut (dim 11, which
STANDS as computed) has a different mechanism -- Sol's torsion/component
proposal, currently CONJECTURE with gaps per the review. Conjecture K as
originally phrased is dead; the open question is the corrected mechanism.

### 8.S9 The e+ CERTIFIER: Newton-lemma application gates at the D23 witnesses (INTERNAL / UNREVIEWED)

[2026-08-20; the e+ certifier build agent. INTERNAL / UNREVIEWED — no
promotion claims. Consumes the PROMOTED filtered differential Newton
lemma (xmodel/sol-newton-lemma.md Thm 3.1/Cor 3.2/Thm 6.1; hostile
review CONFIRMED, xmodel/grok-newton-review.md; AUDIT tail 2026-08-19)
as a theorem and implements its four open APPLICATION GATES
(CYCLIC-30 / BRIDGE-30 / PARAM-30 / FILTER-30) as executable checks.
Scope box as 8.S6/8.S7: one radical fiber (radical_point) of 36,
residue-A B-frozen no-log W1W2 != 0 chart with PIN42, mod p,
chart-local, per the named deterministic hashed ZERO completion.]

TOOL. cases/eplus_certify.py (--selftest / --gates / --point P W K /
--run / --file). Engine: the banked 8.S7 dual-jet constructor
(valuation_e2.py, reused verbatim: DBUILD = 42 pure-y exact below
t^42, measured DEEP_RELABEL, PIN42 pinned, tails mode), regraded to
the CORRECTED object of sol-round6 sect 1 = sol-newton-lemma (1.0)-
(1.4): ONE square 30-input/30-output operator L_s^+ (sum r_q = 288,
sum s_a = 276, s_29 = 36), no free stream, no 29-minor minimization.
e+ per the lemma's OWN definition: e = loss of an exact causal right
section ((2.1)-(2.3)) — not a proxy. The tool constructs NO section,
so e_plus_certified = None ALWAYS (fail-closed); its window scan
returns a CERTIFIED LOWER BOUND on ell+ (in-window coverage failures
are certified by measured causality: inputs with r > 40 and the t^42+
x-side terms cannot reach bands <= 40), evaluated at every constant-
coverage interval's lower endpoint including the LITERAL n = 0 of
(2.1). d+/(e+)^idx are None (fail-closed): M+(N >= 2) reaches the
t^42 band of H_29 = the unbanked x-side (sol-round6 1.1). Controls:
diag(t^e) scanner returns exactly e; the (4.5) char-p resonance is
invisible at a short window (ell = 0 vs true infinity) and detected
once in-window — the measured reason a window reading NEVER promotes.

GATE TIER TABLE (what is executable vs what stays conjectural):
  CYCLIC-30  executable: band-41 regression of the corrected
             30-output grading (eta30..33 = 0, odd bands = 0, graded
             bijection incl. H_29 at s_29 = 36, exact support starts,
             30-ladder input partition of the 170 tangent coords).
             PENDING: the all-depth identity (9.1).
  BRIDGE-30  executable: direct pristine replay at the point — the
             residual from raw coefficients per (1.11), the 86-row
             banked-pipeline derivative match (exact), band-22 deep
             Schur rank 4. PENDING: the universal levelwise (5.9)
             identities on the whole Newton ball (point-evaluated
             identities explicitly insufficient).
  FILTER-30  executable: measured causality (no entry with n < r),
             nonnegative-shift audit, chart-unit audit (W_i, uW_i W_i
             = 1, HW_i = h32 W_i, 2h32^2 = 3, A_i^3 = 3 +/- r3, z of
             exact order 42, scalar denominators prime to p), Ore
             A + B*Theta affinity in all populated bins; on --gates/
             --heavy also zeta -> zeta^5 invariance + the second
             differentiation path. PENDING: the restricted-series
             property on s+F^1X incl. x-side (Lemma 4.2 + the inverse
             telescope, grok-newton-review Issue 1).
  PARAM-30   executable IN THE FAIL DIRECTION ONLY: the certified
             delayed-loss floor. ell_lb > floor((D-1)/2) is a
             CERTIFIED refutation at the named completion; a PASS
             would additionally need the exact all-depth causal Ore
             section closing every p-resonance (unproved).

RESULTS (36 points = 6 witnesses x 3 deep-kernel draws x 2 primes;
banked cases/d23_eplus.json; gates suite 47/47, exit 0; every value
below labeled by its gate outcome):

  ALL 36 POINTS: CYCLIC-30 checks PASS (tier E_PLUS_CANDIDATE),
  BRIDGE-30 checks PASS (tier E_PLUS_CANDIDATE), FILTER-30 checks
  PASS (tier E_PLUS_CANDIDATE), PARAM-30 = FAIL-CERTIFIED at the
  named zero completion. Executable-check failures: 0.

  ell+ >= 37 CERTIFIED at every point (uniform; distribution
  {37: 36}); the binding pair is (n = 0, the H_29 u^0 target at
  level 36) — an independent replay of sol-newton-lemma (8.7),
  strengthening Round 6's n = 6 bound ell+ >= 31. nu_window = 24 at
  every point (exact actual residual order; nu >= D = 23 confirmed;
  the sharp gate (7.3) nu > 2e still demands e <= 11). Window rank
  117/174 at 27 points and 115/174 at 9 — EXACTLY the Round-6 banked
  split, and the 9 low-rank points are precisely the 8.S7
  defect-unstable witness-points (w1 at both primes, w3 at 105673;
  those also show delta+(1) = 26 vs 25). delta+(N >= 2), d+,
  (e+)^idx: not computable from the pure-y build — withheld, not
  approximated.

  E+ DISTRIBUTION: e_plus_certified = None at 36/36 (no section
  exists to certify; fail-closed). E_PLUS_CANDIDATE (window floor,
  = certified lower bound) = 37 at 36/36. Points at/below the D23
  certification threshold e+ <= 11: **0/36**. Formal germs
  certified: **0**.

PROMOTION CONDITION (Theorem 6.1, stated for the record): a witness
at which ALL FOUR gates hold at the PROVED tier (all-depth CYCLIC-30
or its BRIDGE-30 surplus alternative; universal (5.9); FILTER-30
sigma = 0; PARAM-30 with an exact causal section of certified loss
e+), with a legal full completion, nu >= D, and 2 e+ + 1 <= D
(D = 23: e+ <= 11), IS a certified scoped mod-p formal germ.
E_PLUS_CANDIDATE-tier gate results do NOT promote. At these 36
points the condition FAILS CERTIFIEDLY at PARAM-30: ell+ >= 37 > 11,
so no causal section of loss <= 11 exists at this completion —
DEPTH-STAB germ certification at D23 is impossible on this fiber at
the zero completion, now by a per-point certificate rather than the
sampled Round-6 statement. Consequence unchanged from 8.S7-ADDENDUM:
any finite-e Newton target for these points is at least D75
(nu >= 75 needed for e+ = 37 by (7.3)); the tool stands ready as the
zero-latency germ test for any D25 survivor with a better-
conditioned completion.

CAVEATS (explicit): the ell+ floor is completion-dependent (levels
51/53 enter window entries; only the named zero completion is
measured) and says nothing about other completions, other fibers, or
all-depth loss (which can only be larger in-window terms aside).
Nothing here weakens D23 NONEMPTY (8.S5/8.S6): survival stands;
certification does not. No git; running lanes untouched; local run
~40 s total.

### 9.S2 INDEPENDENT MECHANICAL REPLAY of the D25 triangular certificate (INTERNAL / UNREVIEWED, pending Grok)

[2026-08-21 ~12:00. INTERNAL / UNREVIEWED. Independent replay of the
sol-ideas-0821.md item-1 certificate by a fresh agent with its OWN
parser and exact mod-p arithmetic (pure local Python, ~22 s; no
Singular, no msolve, no reuse of Sol transcript code; no lane
touched). SCOPE BOX: MODULAR ONLY, both registered primes p=105337
and p=105673, residue-A fixed-r B-frozen no-log PIN42 W1*W2!=0
chart; the EMISSION-FIDELITY caveat is inherited -- the objects
replayed are the emitted .ms rows, sha256-verified identical between
cases/ and box01:~/jc72108/d25fam on all 74 files. Banked:
cases/d25_certificate_replay.json (all counts, points, pivots,
hashes; rng seed 20260821).]

POINT EVALUATION (raw rows, no canonicalization): Sol's explicit
all-x-zero point annihilates 38/38 union rows at BOTH primes
(selector (50630,10114,50267,50267), W (31931,9457,64754,22756) at
105337; (38664,46664,35053,35053), (8021,20111,13662,64399) at
105673; uW_i = W_i^-1 exactly). On parked fibers: 34/34 at a00pp
(and, incidentally, at the whole a00** quartet, which shares the
quartic constants); exactly 28/34 on each of the other 32 fibers
(different (c1,c2), as the certificate itself predicts). Every one
of the 72 fibers received its OWN derived all-x-zero witness (W from
its fiber's fourth roots): 34/34 vanish at 72/72.

PIVOT STRUCTURE VERIFIED: (i) the R1,R2 x33/x38 minor is
scalar*uW1^2*uW2^2 at ALL 72 fibers (a00pp scalars 75772 / 9899
exactly as claimed) -- a Laurent unit on the chart; (ii) Sol's eight
base pivots (x71<-hlin, x55<-hcore, x70/x53/x58/x52/x47/x54 <- rows
28/26/27/10/11/13) all have scalar-times-Laurent-monomial unit
leading coefficients, the substitution DAG is acyclic, and all 34
source rows reduce to ZERO through it modulo the terminal quartics;
(iii) hcore and hlin themselves reduce to zero through a fully
independent greedy elimination built ONLY from the 34 raw rows
(Cramer-derived compatibility rows as pivot sources), so both lie in
the chart-localized ideal -- the two inclusions close and the
identification is exact, not merely a lower bound. The independent
elimination reaches the IDENTICAL terminal 6x3 (W1^4,W2^4,1) matrix
printed in sol-ideas-0821.md, rank 2, (W1^4,W2^4) = (57673,53212)
resp. (44399,92038). Also confirmed en route: the constant relation
R2+6R3+30R4+144R5=0 is the UNIQUE constant relation (72/72), lift
rank exactly 2, full residual rank 4, compatibility rows lift-free.

DERIVED (recomputed, not transcribed): per parked fiber, free vars =
10 base (x57,x59,x60,x62,x63,x65,x66,x68,x72,x73) + 4 lifts
(x16,x19,x24,x27) => DIMENSION 14; c1,c2 nonzero fourth powers with
exactly 4 fourth roots each (p = 1 mod 8) => 16 disjoint copies of
A^14, at 72/72 fibers. Union: the 4 selector rows have exactly
3*3*2*2 = 36 common zeros; specializing the 34 non-selector rows at
each reproduces exactly one parked file (row-set equality up to
per-row scaling, bijective onto the 36 labels, both primes) =>
UNION = 576 copies of A^14, dimension 14. Jacobian ranks at the
witnesses: 14 (parked, 34x28) and 18 (union, 38x32). Point counts
16 p^14 per fiber / 576 p^14 per union follow.

CODIM-2 PRE-REGISTRATION ADJUDICATED (xmodel/sol-codim2.md, locked
2026-08-21T03:04:29Z, before any verdict existed): predicted
projected base 11->9 via a height-TWO pair, lane dimension 13,
carrier pair (9,<=8). Found: projected base dimension 10 (the pair
cuts height ONE), lane dimension 14, carrier pair (10,9) -- the
reduced q is associate to a monic-linear form in x59 on every one of
the 16 branches, so q=0 cuts exactly one dimension on every
component. VERDICT: CONJECTURE ECO-D25 is REFUTED at both registered
primes, by the pre-registration's own table row ("NONEMPTY,
dimension 14 ... REFUTED"); ECO-D25-CARRIER's numbers are refuted
(+1 each); the mechanism's exact skeleton (row identity, rank-2
obstruction, quotient isomorphism, equivariant uniformity 36/36 per
prime, cross-prime agreement, q a genuine divisor meeting every
component) all HELD.

NEGATIVE CONTROLS (seed 20260821): perturbing the witness in 3
random coordinates left 5-26 rows nonvanishing in every one of 24
trials (never zero); 3 fully random points per system had ALL rows
nonvanishing (34/34 resp. 38/38), across both unions and parked
a00pp/a11mp/a22pm at both primes.

STATUS: this replay CONFIRMS the certificate mechanically at the
registered modular scope: D25 is NONEMPTY of dimension 14 with
16/576 A^14 components per parked fiber/union, at both primes.
INTERNAL / UNREVIEWED until the Grok verdict-tier review lands; no
characteristic-zero statement is made or implied (sol-ideas item 5
remains the bridge); the 48 h union GB lanes are moot as verdict
lanes for D25.

### 9.S3 The e+ LANDSCAPE on the D25 A^14 cells (INTERNAL / UNREVIEWED)

[2026-08-21 ~14:30. INTERNAL / UNREVIEWED -- no promotion claims;
every numeric value below is E_PLUS_CANDIDATE or a certified LOWER
bound per the 8.S9 gate discipline (cases/eplus_certify.py:
e_plus_certified = None ALWAYS, no section is constructed, no germ is
certified). Stage: corrected-e+ measurement at D = 25 on the promoted
D25 verdict (AUDIT tail 2026-08-21: 576 disjoint A^14 cells, 16/fiber
x 36 fibers, both primes; certificate xmodel/sol-ideas-0821.md items
1-2; replay 9.S2 + cases/d25_certificate_replay.json; Grok
xmodel/grok-d25cert-review.md). The Newton criterion is consumed as
promoted: D >= 2e+1, so GERM-TRACK at D = 25 needs e+ <= 12. Driver:
cases/d25_eplus.py (--selftest / --crosscheck / --run); bank:
cases/d25_eplus.json (sha256 891fb93761b33cc2236283806f1d83b1
0b3640a47f85887be4ec9f8bea1bc6c4). SCOPE BOX: mod p ONLY (105337,
105673); residue-A B-frozen no-log W1W2 != 0 chart with PIN42;
chart-local; per the deterministic completions named below; the
emission-fidelity caveat of sect 9 is inherited.]

SAMPLE (360 points, 360 accepted / 0 rejected):
  (1) the 72 banked per-fiber witnesses (36 fibers x 2 primes; the
      9.S2 derived_witness: all cell coordinates zero, W from the
      fiber quartic fourth roots), run --heavy (zeta^5 + path-A);
  (2) 288 interior samples: 3 random points in EVERY one of the 16
      cells of a00pp at BOTH primes (96) + all 16 cells x 3 at
      p=105337 for a00mm, a01pp, a10pm, a22mp (192; character
      coverage: pure h-sign flip, each C3 factor, omega^2-omega^2
      with mixed signs). Free draws (seed 20260821) on
      T = (x57,x59,x60,x62,x63,x65,x66,x68,x72,x73) + lifts
      (x16,x19,x24,x27); dependent coordinates solved through the
      certificate's unit-pivot structure (greedy Laurent-unit
      elimination + the NUMERICALLY RE-DERIVED Cramer compatibility
      rows -- the hcore/hlin span recomputed per fiber from the
      residuals' lift-column left kernel -- + the R1,R2 2x2 lift
      solve); every sample verified to annihilate ALL 34 raw fiber
      rows exactly BEFORE use (fail-closed; 0 sampler rejections).

RECONSTRUCTION (cell point -> full chart point; fiber-frame-native).
The 8.S6 reconstruction discipline replayed on the pristine rows with
the fiber's selector frame (A1r, A2r and the PER-SIDE HW law
HW_i = h_ir W_i, atlas values; the banked evaluators generalize by
pow(h1r,h1)*pow(h2r,h2) in the radkey fold): (a) 22-pivot groupwise
back-solve from the raw D21 window rows in the banked band-triangular
groups 1+2+3+4+4+4+4 (PIV22_SEQ), each group row asserted to vanish
exactly after its square affine solve; (b) the level-44 tg pair --
which feeds the band >= 12 pivot rows -- pinned by EXACT AFFINE
PROBING of the band-22 compatibility residual c(tg) = K.b(tg)
(probes (0,0),(1,0),(0,1); affinity VERIFIED at (1,1); K = canonical
left kernel of the constant deep-column matrix; rank-2 solve);
(c) rank-4 deep solve, kernel frees = 0; (d) the BAND-24 FRONTIER
COMPLETION: the nine k = 24 residual cells solved over the ten banked
frontier directions (levels 51/56, cases/d25_reduce.FRONTIER) at rank
4 with kernel frees = 0, THROUGH THE CERTIFIER'S OWN dual-jet
operator, guarded per point by the measured level cap (no frontier
operator entry below band 24 -- the sect-9 "bands <= 22 carry no
new-at-D25 variables" finding re-measured 360/360); jets rebuilt at
the completed point. All remaining frees 0. COMPLETION NOTE (the
sect-9 covenant "never silently zero-fill"): at the 72 witnesses the
frontier solve is identically zero and the completion IS the 8.S9
ZC_RULE; at all 288 interior points the completion differs from
ZC_RULE exactly in the frontier block (4 nonzero level-51/56 values,
rank 4, deterministic, hashed into zc_hash). Measured and banked:
WITHOUT the frontier stage an interior cell point sits at nu = 24 --
not a depth-25 chart point at the zero completion. The t^42+ x-side
and levels >= 55 outside the frontier remain zero-COMPLETED as in
8.S9: the floor below is per named completion, nothing more.

VALIDATION (before any measurement was banked): (i) from ONLY the 24
cell coordinates of the banked D23 witness w0, the pipeline
reproduces the ENTIRE banked witness72 (72/72 coordinates, including
all 22 pivots and the banked row22red tg values x17 = 39329,
x25 = 46025) AND the banked draw-0 deep tails EXACTLY, and passes
row22compat 48/48 + six compat zeros, row22red 32/32, core23 77/77;
(ii) --crosscheck: at the banked a00pp D25 witnesses the driver
equals the UNMODIFIED cases/eplus_certify.py --file run at both
primes (operator hash + every CYCLIC/BRIDGE/PARAM check +
ell+/rank/delta+/nu); (iii) negative controls: single-coordinate
perturbation of a sample leaves 23/34 fiber rows nonvanishing.

RESULTS (all values E_PLUS_CANDIDATE-tier unless stated):

  THE LANDSCAPE IS FLAT. ell+ >= 37 CERTIFIED at every point
  (distribution {37: 360}) -- the identical binding pair as D23
  ((n = 0, the H_29 u^0 target at level 36), sol-newton-lemma (8.7)).
  Points at/below the D = 25 threshold e+ <= 12: **0/360**. Formal
  germs certified: **0**. e_plus_certified = None at 360/360
  (fail-closed). PARAM-30 = FAIL-CERTIFIED at the named completion
  at every point: no causal section of loss <= 12 exists for any
  sampled operator at its completion.

  RESIDUAL ORDERS (exact): nu_window = 30 at all 72 witnesses,
  nu_window = 26 at all 288 interior points -- both >= 25 (b1/b2
  PASS 360/360; D23 points sat at nu = 24). The locus deepens the
  residual; the window floor DOES NOT MOVE. The sharp gate (7.3)
  nu > 2e still demands e <= 14 (witnesses) / e <= 12 (interior):
  both far below the certified floor 37.

  WINDOW INVARIANTS (exact): window rank 115/174 and delta+(1) = 26
  at every point, both primes, all 36+4 fiber runs, all cells, all
  samples. The 8.S9 D23 split (117/25 generic at 27/36 points,
  115/26 at the 9 defect-unstable points) COLLAPSES at D25: the
  defect-unstable profile is the UNIQUE D25 cell profile.

  GATES: CYCLIC-30 / BRIDGE-30 / FILTER-30 executable checks PASS
  (cand tier) at all 288 interior points, incl. per-side unit audit
  at the mixed-sign fibers; heavy f6/f7 PASS at all 72 witnesses.
  ONE measured exception: c4_support_starts_exact FAILS at exactly
  the 72 all-cell-zero witnesses (the s_a = 10 output streams'
  measured gradient support starts at 16 there, not 10; the banked
  tool run on the same points agrees -- a point degeneracy of the
  witnesses, not a pipeline artifact; interior starts exact 30/30).

  CROSS-STRUCTURE: NO dependence of (ell+, rank, delta+(1), nu) on
  prime, fiber, character, cell (fourth-root branch), or position
  inside a cell: one profile at witnesses, one at interior points,
  differing only in nu (30 vs 26) and c4. Consistent with the
  promoted fiber-equivariance theorem; measured, not inferred.

VERDICT OF THE STAGE (per the sect-9 verdict table, per-point
certified in the FAIL direction only): every sampled D25 point has
certified ell+ >= 37 > 12 at its named completion, so NO SAMPLED
POINT CAN SUPPLY A D25 HENSEL CERTIFICATE -- the deeper, smoother
locus does NOT drop the delayed-parametrix loss; germ certification
at D = 25 fails certifiedly on every sampled cell at these
completions. By (7.3), a finite-e Newton target through this
operator needs nu >= 75 (D75-scale), unchanged from 8.S7/8.S9. Per
the table's own scope line: witness sampling CANNOT prove the
locus-wide claim (that needs symbolic stratification over the 14
free parameters); and a large ell+ is NOT a kill -- the points "may
still extend singularly". The discriminating question moves to
(a) completions: the floor is completion-dependent; the frontier
completion is the FIRST measured nonzero completion and it did not
move the floor; a completion-family scan (or the finite-range
invariance lemma of the sect-9 quote) is the remaining germ-side
lever at D25; (b) the kill side: a mechanism terminating a cell
tower whose codimension (11 -> 14) grows strictly slower than depth
(23 -> 25).

CAVEATS (explicit): window floors are certified lower bounds AT THE
NAMED COMPLETIONS only; no upper bound on e+, no all-depth
statement, no locus-wide statement; the four application gates stay
open (8.S9 tier table); frontier-completion points sit outside the
literal 8.S9 ZC_RULE (deterministic + hashed per point); c4 at
witnesses is a measured degeneracy; emission-fidelity caveat
inherited. Runtime 1570 s local, detached + checkpointed; no git;
the capping union lanes untouched.

## 10. THE D43 PROGRAM: level-42 window, x-side, and the prolongation obstruction (INTERNAL / UNREVIEWED)

[2026-08-21 ~16:30. INTERNAL / UNREVIEWED -- no promotion claims.
Commission: the D43 discriminator of xmodel/sol-h29-dichotomy.md
(sects 4, 7), implemented per xmodel/sol-xside-spec.md EXACTLY (every
CONJECTURE fail-closed); review anchor xmodel/grok-h29-review.md.
SCOPE BOX (all subsections): mod p ONLY (105337, 105673); residue-A
B-frozen no-log W1W2 != 0 chart with PIN42; chart-local; named
deterministic completions; POINTWISE at named cells/completions --
sampling proves NO locus-wide claim (CONJECTURE LOCUS-UNIVERSAL-H29
is not consumed; the sect-9 quantifier discipline applies verbatim).
Tools: cases/eplus43.py, cases/d43_hunt.py, cases/d43_slices.py,
cases/build_tails_modp.py (+ box01 build_tails43.py char-0 gold lane),
cases/d43_reduce.py / d43_reduce_modp.py / d43_family.py. Artifacts:
cases/d43_regress.json, d43_smoke.json, d43_liftquad.json,
d43_slices.json. No git.]

### 10.1 The extended operator (stage 1) and its mandatory gate

cases/eplus43.py builds the band-<=42 window as a CONFIGURED engine
instance: a source-configured copy of the banked valuation_e2.py with
DBUILD = 43, RMAX = 42 (GIDX/GD/Toeplitz/slot arrays recomputed from
the configuration; nothing mutated after import), plus the REAL
level-42 x-side of the spec: U_f = 1 + alpha t^42, U_g = 1 + beta
t^42 multiplied into the dual jets BEFORE the Euler-row constructor,
+42 t^20 added once.  alpha, beta carry the MANDATORY tangent
classification (spec 2.2): INDEPENDENT (case 3), because CONJECTURE
X-SIDE-DERIVATION is undischarged and no repository value exists; the
legal window is therefore

    184 rows x 182 columns  (180 y-columns + Dalpha + Dbeta),

never the conditional 184x180; their completion value is the NAMED
finite-support choice alpha = beta = 0 (recorded + hashed in a full
source-consumption manifest -- absence is never the value zero).

Executable spec-sect-9 gates, all implemented and passing at every
point run: ROW42-IDENTITY ((3.5)/(3.9)/the exact p^4p' vector 3.3;
x columns 126/-84 S_M G_M p4p'; H29u1 entries 756/-504 S_M G_M; the
3:-2 ratio), TWO-PATH-DIFFERENTIAL ((3.2) grouped path AND the
hand-assembled path-A grouping == the production dual path, values
and all 182 gradient columns), XSIDE-ONSET (alpha/beta perturbations
change nothing below band 42, measured), NEGATIVE-XSIDE-CONTROLS,
CAUSALITY-42 (measured, incl. the x columns), ORE/GRADING-42,
OUTPUT-CENSUS-42 (row-42 eta support exactly {2,5,...,26,29}; eta
30..33 surplus identically zero, retained as sidecar), SOURCE-
CENSUS-42 (180-column ladder census + manifest), M2 (the exact 60x60
M+(2): rank 17, delta+(2) = 43; NO stabilization claim), LOSS-BRUTE/
FAST agreement (literal n = 0..42 scan == interval scan; profile
records min included column level AND eligible-column count), sparse
dual witnesses replayed after deserialization, REGISTRY/HASH.

MANDATORY GATE (spec sect 8) PASSED IN FULL: at all 360 banked 9.S3
D25 completions (72 witnesses --heavy + 288 interior, the exact RNG
replay) the extended build restricted to bands <= 40 and the old 170
columns, reordered to the exact old registries, is BYTE-IDENTICAL to
the banked object: arrays, per-point operator hash, and every
CYCLIC/BRIDGE/FILTER/PARAM gate output; additionally the unmodified
9.S3 driver record is reproduced (seconds stripped), the d23 w0k0
fixtures replay likewise at both primes, and the char-0 eta29/tf1_48
crosscheck passes through the configured engine at both primes.
360/360 + spot + crosschecks: ALL PASS (cases/d43_regress.json).

### 10.2 D25_COMPLETION_BAND42 smoke (spec C0) -- NOT a depth result

At 12 banked witness completions (6 fibers x both primes), mode-2
gates all pass; ell+ >= 37 re-certified through the 184x182 window
(window rank 125, nu = 30, delta+(1) = 26 -- the universal 9.S3
profile persists); H29u0 (t^36 e29) remains uncovered at n = 0 with
fresh dual witnesses banked (Y0-RECHECK).  THE LEVEL-42 SPLIT:

  * H29u1 = t^42 e29 is UNCOVERED in the 180 y-columns: the exact
    sparse y180 dual witness is banked per point.  This is the
    CONDITIONAL shifted-obstruction certificate: under CONJECTURE
    X-SIDE-30 (or a proved fixed/derived alpha, beta classification)
    it would read ell+ >= 43 at these completions.
  * H29u1 IS covered once the two independent x-tangent columns
    enter, so FAIL-CLOSED nothing beyond ell+ >= 37 is certified.

The growth-vs-flat verdict at these completions therefore hinges
EXACTLY on the x-side tangent classification, as spec 2.2 anticipated
("it cannot be quotiented away from a single-window kernel
observation").  These are mode-2 objects: not D43 survivors, not a
third depth measurement (cases/d43_smoke.json).

### 10.3 The D43 prolongation obstruction (pointwise; the real find)

Extending a completed D25 cell point to a D43 survivor (nu >= 43)
means solving the even bands 26..42 over the adjoined completion
coordinates: the 90 provisional first-occurrence tails (levels 53..74
incl. the formerly dormant 53/55), the band-24 frontier and deep-tail
kernel freedom re-opened, and the two x-side coordinates.  Bands
<= 40 are EXACTLY jointly affine in these unknowns (any product of
two undetermined tails has level >= 21+21 = 42), so consistency of
one measured linear system A u = b decides pointwise prolongability
below band 42 with no approximation.

MEASURED (cases/d43_hunt.py, d43_slices.py):

  * At EVERY sampled point -- witnesses and random interiors, both
    primes, fibers a00pp/a11mp/a22pm/a10pm/a01pp, multiple cells --
    b does NOT lie in colspan(A): the D25 point does not prolong.
    Generic interior points fail already at band 26 (no D27
    prolongation from the D25 zero/frontier completion family);
    witnesses fail from band 30.
  * The obstruction survives re-opening the frontier (levels 51/56)
    and deep (49/54) kernel directions and adjoining alpha/beta.
  * ~35 canonical kernel pairings are nonzero per point; a nested
    peel (deg-1/2 interpolated roots along lifts) zeroes them one at
    a time with NO collapse -- the obstruction is not one scalar.
  * DECISIVE SLICE TEST: freezing the 10 base parameters at random
    values, ALL 37 pairings are validated quadratics in the 4 lift
    coordinates with span rank 10, and Singular lex-GB of that
    quadric system is the UNIT IDEAL (dim -1): the entire 4-dim lift
    slice carries no prolongable point OVER THE ALGEBRAIC CLOSURE.
    The multi-slice census (2 primes x 5 fibers x cells x 2 slices
    each) returns EMPTY_SLICE uniformly (cases/d43_slices.json).

READING (scoped): the depth tower CUTS THE BASE from D27 on -- the
completion-only ladder that carried D23 -> D25 ends at D25.  The D43
survivor locus over each A^14 cell is contained in a proper
subvariety that avoided every sampled point and every sampled
4-dim lift slice (closure-level).  This is pointwise EVIDENCE for
D43-EMPTY over the scoped cells; it is NOT a scheme-theoretic kill
(sol-algkill Prop 3.3 discipline: emptiness needs 1 in the ideal,
per rank chart, exhaustively).

### 10.4 The family instrument (stage 2, in flight) and structure

Measured rung structure at every even rung k = 26..42 (both primes,
multiple points): the ten first-occurrence columns factor as A_k =
C_k diag(d_j) with C_k CONSTANT of rank 4 and constant column space
-- the banked Row-24 Schur pattern persists through the x-side row.
So each rung contributes 5-6 CONSTANT left-kernel compat rows
(53 total), and the D43 family object over a fiber compresses to
{parked 34 rows} + {53 compat rows} by the D25 certificate method
(pivot/Schur first, NO GB).  Pipeline (per prime, fiber a00pp pilot):
mod-p symbolic bank (cases/build_tails_modp.py -- the structural
mirror of the byte-identically-regressed numeric engine; D25 control:
builds in 4 s and reproduces every row value/gradient exactly; D43
banks building on box01) -> NF-reduction through the cached 509-el
det23 GB (d43_reduce_modp.py; the swell-killer, exact modulo I23 on
the survivor locus) -> rung compat extraction + verdict
(d43_family.py; C_k diag factorization verified SYMBOLICALLY,
fail-closed) -> EMPTY (1 in <parked + compat>) or NONEMPTY (+dim,
witnesses -> the floor measurement) per cell/chart; msolve fallback
with caps on box01 only if the pivot route stalls.  The char-0
build_tails43.py gold lane runs in parallel on box01 (per-orbit
checkpoints; ~days) as the eventual cross-validation of the mod-p
bank.  OUTCOME 2026-08-22: the chain completed; the family stage
aborted FAIL-CLOSED at rung 28 -- NO VERDICT.  See 10.5.

CAVEATS: everything above is at the named deterministic completions
and named charts; rank-chart exhaustion, POST41-FIRST-OCCURRENCE at
Row 42 (verified numerically per point, not proved), CYCLIC-30/
BRIDGE-30/FILTER-30/X-SIDE-* remain open as in the spec ledger
(sect 10 of the spec); no all-depth statement; no upper bound on e+;
no germ; emission-fidelity caveat inherited.

### 10.5 The family chain outcome (2026-08-22): stage 1 BANKED,
### stage 2 fail-closed abort at rung 28 -- NO VERDICT

[2026-08-22 ~01:40. INTERNAL / UNREVIEWED -- no promotion claims;
the sect-10 scope box applies verbatim.  The box01 automated chain
(cases43/run_d43_chain.sh, fiber a00pp pilot, both primes) completed
its first pass 00:06/00:08 UTC.  Evidence on box01: cases43/
d43chain.log, d43modp_p{105337,105673}.log, d43red_p*.log +
d43red/*_summary.json, d43fam_p*.log, d43famchk_p*.log.]

STAGE 1 (mod-p symbolic bank + NF reduction) PASSED AT BOTH PRIMES
-- banked here separately from, and unaffected by, the stage-2 abort:

  * build_tails_modp.py: 189-var D=43 bank, all 184 (h,s) rows built
    per prime (~2300 s); structural gates (odd/surplus/congruence)
    PASS; V1 replay at 2 points: 184 row values + 36 gradients EXACT
    against the byte-regressed numeric engine, both primes.
  * d43_reduce_modp.py: NF through the cached 509-el det23 GB; every
    even band 6..42 banked, drop = 0 at every (band, eta) cell,
    rc = 0, ~454 s per prime.  The two primes' logs differ only in
    thread interleaving and per-coefficient term counts.
  * Recall the stage-1 MANDATORY GATE of 10.1 (184x182 extended
    operator; bands-<=40/old-170-column restriction BYTE-IDENTICAL
    at 360/360 banked completions; d43_regress.json): banked
    2026-08-21, stands independently.

STAGE 2 (d43_family2.py, and the independent d43_famcheck.py re-run)
ABORTED FAIL-CLOSED, IDENTICALLY at both primes (4/4 runs):

  * Rung 26 (tails {tf1,tf2,tg1,tg2}_53 + {tf*,tg*,tg0*}_58, i.e.
    the dormant level 53): the C-diag factorization VERIFIES
    symbolically; rank C = 4; 6 constant compat rows extracted
    (~20.9k-term entries; the lone 20901-vs-20902 term-count
    difference at p105337 is one coefficient vanishing mod p --
    benign).
  * Rung 28 (tails {tf1,tf2,tg1,tg2}_55 + {tf*,tg*,tg0*}_60):
    AssertionError ('C-diag factorization FAILS', 28, 'tf1_55', 9)
    at d43_family2.py:200.  Decoded: in the band-28 block (rows
    h = 1,4,...,28), the affine coefficient column of tf1_55 -- the
    FIRST column checked at this rung -- is polynomial-proportional
    across the nine rows h = 1..25 but NOT at the tenth row h = 28,
    the boundary eta cell of the rung.  Same rung, same variable,
    same row index at both primes: the failure is PRIME-SYMMETRIC,
    hence structural in the emitted object, not a mod-p accident.

READING (scoped): the D25 rank-2 Row-24 Schur structure
A = C.diag(uW^2) -- which pointwise NUMERIC measurement (10.4)
showed persisting as a constant rank-4 C_k through every even rung
26..42 at both primes -- does NOT persist naively at D43 at the
SYMBOLIC level.  First failure: a level-55 tail variable at the
rung-28 boundary row.  Level 55 is one of the two formerly DORMANT
D25 levels (sol-xside-spec.md 6.1: banked slots whose values the old
evaluator never solved -- implicit zero via vals.get(r,0); 6.3
demands their explicit reconstruction; the surrounding 118/123
counts are conditional on CONJECTURE POST41-FIRST-OCCURRENCE and
CONJECTURE X-SIDE-30).  The failure thus lands squarely in territory
the spec marks CONJECTURE-conditional -- and the OTHER dormant level
(53, rung 26) passes.

OPEN ADJUDICATION (characterized; deliberately NOT concluded):

  (A) Emission/spec defect: the mod-p bank or the family emitter
      mishandles the dormant-55 reconstruction at the boundary cell
      (an inherited implicit zero, or a boundary-census slip).  Note
      the V1 gate replays only row VALUES at 2 points, so a wrong
      term inside ONE column's h=28 entry can pass V1 and still
      break the symbolic factorization.
  (B) Genuine structural change at depth 43: A_28 truly is not
      C.diag(d_j) -- the h=28 entry of the tf1_55 column carries an
      extra non-proportional polynomial.  Then the 53-compat-row
      compression of 10.4 is invalid as designed and rungs >= 28
      need the full affine block (or a higher-rank/non-diag
      factorization).  The 10.4 pointwise rank-4 measurements would
      then mean the deviation polynomial VANISHES at every sampled
      completion -- which would itself be structure worth naming.

Discriminators queued for the next pass (NOT run): print col[i0]
and col[9] of the tf1_55 column and diff monomial supports; test
proportionality after explicit dormant-55 reconstruction; evaluate
the deviation term at the banked witnesses; demote the assert to a
census and map which rungs/columns/rows fail across 28..42.

PROGRAM STATUS: this completes the D43 program's FIRST PASS.  The
family EMPTY/NONEMPTY verdict was NOT obtained; nothing is promoted;
the ell+ ledger is unchanged (ell+ >= 37 stands; the conditional
level-42 split of 10.2 stands; the pointwise prolongation
obstruction of 10.3 is unaffected -- it used the numeric engine, not
the C-diag compression).  The char-0 build_tails43.py gold lane
continues on box01 as the eventual cross-check of the mod-p bank.
With this record banked, the repo-reorg trigger condition (notes.md
2026-08-21 ~15:40: "D43 final report banked") is MET.

RESOLUTION (2026-08-22 ~10:15; xmodel/sol-d43-adjudication.md +
empirical validation gate).  **ADJUDICATED: checker defect, not
structural failure.**  At rung 28 the four dormant level-55 columns
vanish EXACTLY in the boundary row h=28; the `proportional` helper
shared by d43_family.py / d43_family2.py returned None for the valid
lambda = 0 case (a zero polynomial IS 0*pa) and the caller reported
'C-diag factorization FAILS'.  Outcome (A)-corrected: the dormant-55
emission is CORRECT (the zero is an emitted support zero, not an
inherited implicit-zero assignment -- raw bank, NF bank, and the
separate numeric eplus43 gradient all agree); the rank-two ordinary
carrier does NOT terminate at rung 28; alternative (B) is refuted.
Sol's exact zero-safe fix applied to BOTH files (box01 cases43/ +
local cases/ mirrors, byte-identical; d43_family2.py sha256 now
f55354d3...; pre-fix c4e97d95... as recorded in the adjudication).

EMPIRICAL VALIDATION GATE (substitutes for prose review of the
adjudication): FRESH independent code -- cases43/d43_valgate.py, no
import of the patched checker, own affine split / factorization /
rank / hash -- verifies at BOTH primes: rung 28 A = C.diag(d_j)
EXACT as dict equality over all 10 columns INCLUDING the four
lambda=0 boundary entries; C_28 = [v1 v2 v1 v2 w1 w2 w1 w2 w1 w2]
equal to the adjudication's published tables; level-55 subblock rank
2, level-60 rank 2, rank C_28 = 4; the (1,4,7,10) x
(tf1_55,tf2_55,tf1_60,tf2_60) minor = 37062 / 84146; canonical
sha256 of normalized C_28 matches the adjudication (a9c13cba... /
29db8072...); d_j leading units match; rung 26 re-verified EXACT and
UNCHANGED (rank 4, 6 compat rows; log line byte-identical to the
first pass).  18/18 checks PASS per prime (d43valgate_p*.log).

STAGE 2 RERUN COMPLETE, BOTH PRIMES, 4/4 rc=0 (rerun_stage2.sh,
box01, 09:50-10:12 UTC): d43_family2.py -- ALL rungs 26..42 pass at
each prime; ranks 4,4,4,4,4,4,4,4 and rung 42 rank 5 (the
independent-x model: the two x columns are proportional, ratio 3:-2,
adding exactly one direction), so 6+6+5+6+6+6+6+6+5 = 52 compat rows
+ parked 34 = the 86-row verdict system, exactly adjudication (5.2)
(86 equations, 120-37 = 83 remaining coordinates; the conditional
180-column model's 87/53 counts must NOT be quoted for this object).
The independent d43_famcheck.py gate PASSES at both primes: 104
compat-row evaluations per prime (2 completed cell points,
randomized rung/deep tails) EXACTLY equal L . (numeric band values)
from the byte-regressed engine.  Notable: one rung-36 compat row is
a 6-term CONSTANT-coefficient LINEAR relation on the six level-48
tails, PRIME-SYMMETRIC with rational 2:1 structure
c1*(tf1_48+tf2_48) + c2*(2*(tg1_48+tg2_48) + (tg01_48+tg02_48)):
(c1,c2) = (48635,54013) at p105337 (2*54013 = 2689 mod p) and
(50809,18288) at p105673 (2*18288 = 36576).  Emission footnote: the
first verdict emission listed 6 variables twice in the .ms/.sing
headers (x16,x19,x24,x27,x33,x38 -- deep tails renamed into parked
x-names but not deduplicated against the GBVARS segment; msolve
rejects duplicate names).  allvars dedup applied to d43_family2.py
(both mirrors, sha256 8c0f7fd3...) and the emitted headers rewritten
in place -- generator sections verified byte-identical by sha256, so
no mathematical content changed; true variable count 172.  The prior
10.5 abort record above is retained as history; its OPEN
ADJUDICATION is CLOSED by this block.

### 10.6 D43 NF-certificate route: structural hardening, no verdict (INTERNAL / UNREVIEWED)

The NF route was executed on the two validated 86-row a00pp verdict
systems without passing either full file to msolve.  The new exact
replay (`cases/d43_nf_certificate.py`, sha256 41865448...) starts from
the fact that the 52 compatibility rows are already normal forms
modulo the D23 basis, then eliminates the 34 parked rows with the D25
residual-left-kernel plus triangular/pair pivot certificate.  For each
prime the parked quotient splits into 16 W-components with 14 free
parameters and 10 reconstructed coordinates.  All 34 parked
polynomials reduce identically to zero on all 32 prime-components.
The negative control perturbs a reconstructed coordinate by one and
makes at least five parked polynomials nonzero on every component.

AFFINE HUNT.  On one certified W-component per prime, fixing the 14
D25-free parameters to 1,...,14 leaves 52 exact compatibility
polynomials in 144 external variables.  They first become affine in
the 92 tails of level >= 53.  At four deterministic lower-tail draws,
both primes give rank(A)=44 and rank([A|b])=45; hence the evaluated
left nullity is 8.  This is a pointwise rank profile, not a proof that
the lower-tail residual ideal is empty.  The coefficient matrix has
2592 nonzero polynomial entries, depends on all 52 lower variables,
has coefficient degree <= 3 (b degree <= 6), and does NOT admit the
D25 global A=C.diag(d_j) factorization: the first prime-symmetric
failure is row 12 / tf1_53, not scalar-proportional.  Rung 26 alone
does factor, but the global D25 rank-2 signature is gone by D43.

NEGATIVE SLICES / SOLVER GATES.  With the 14 D25-free parameters fixed
to zero, the exact 52-row witness slice has 116 variables and 46,428
terms; its threshold-53 ranks are 30/31 at the zero lower-tail point
and 32/33 at three nonzero draws.  msolve and Singular each timed out
at 900 seconds at both primes, with no crash and no basis output.  In
the complementary external-tail-zero slice, one representative
W-component gives 51 nonzero polynomials in the 14 D25-free
parameters (953056/953055 terms): linear-row rank 51, no unit/constant
linear combination, origin Jacobian ranks 14/15, and no witness on
any coordinate axis.  msolve timed out at 1800 seconds and Singular
at 900 seconds at both primes.  The 52x144 generic cell slices likewise
timed out (msolve 1800 seconds, Singular 900 seconds).  Singular's
polynomial left-syzygy computation on the 92x52 affine transpose timed
out at 900 seconds, so no honest small residual system was emitted.

GATES / INTERPRETATION.  The banked family checks remain 104/104 exact
compatibility-row evaluations per prime, and the independent D43
validation gates remain 18/18 per prime.  The fixed-D25-point slices
and the external-tail-zero slice are deliberately labelled negative
structural probes; neither represents the full D25 quotient family.
Therefore this route establishes neither EMPTY nor NONEMPTY, supplies
no dimension or witness, and does not authorize an eplus43 floor run.
There is NO FLOOR NUMBER from this pass; the comparison with 37 is
unchanged and the ledger remains ell+ >= 37.  Machine-readable details,
hashes, ranks, solver caps, and artifact paths are banked in
`cases/d43_nf_certificate_report.json`; the raw capped-run ledger is
`cases/d43_nf_solver_gates.log` (both INTERNAL / UNREVIEWED).

### 10.7 D43 residual second layer: compressed ideal NONEMPTY, graph lift fails; intended family still unresolved (2026-08-23, INTERNAL / UNREVIEWED)

This pass resolves the literal 86-row object emitted by the stage-2
compression, but also finds a semantic omission that prevents promotion of
that literal verdict to the intended D43 prolongation family.  The two
statements must be kept separate:

  * LITERAL EMITTED IDEAL: NONEMPTY at both primes.  It consists of the 34
    parked rows plus 52 compatibility rows, without the rung reconstruction
    graph equations.  Each prime has a verified smooth point on a
    dimension-106 component (global dimension at least 106).
  * GRAPH-PRESERVING D43 FAMILY: still UNRESOLVED.  Both literal witnesses
    fail the mandatory forward reconstruction gate at rung 28, and the one
    fully reconstructed D25 point tested is empty already at rung 26.  This
    is not a locus-wide emptiness proof.

SECOND AFFINE/NF LAYER.  At the certified D25 point used in 10.6, the exact
52x144 compatibility system is affine in the 92 level >= 53 variables.  At
the lower-variable origin its coefficient rank is 44.  A canonical
constant 44x44 minor eliminates those high pivots; the analytic Schur
residual Jacobian has rank 8, with pivot lower variables
`tf1_49,tf1_51,tf2_49,tf2_51,tg1_49,x0,x1,x13`.  Keeping those eight and
the 44 high pivots, and setting the other 92 external coordinates to zero,
produces an exact 52-equation/52-variable slice with 3146 terms and degree
at most 3.  The rung-36 six-term linear negative-control row survives as a
nonzero `x13` term.

On box01, msolve 0.10.1 (`-g 2 -t 4 --random-seed 843`) solves each small
slice in 0.01 seconds: the reduced basis has 52 completely linear elements
and 103 terms, hence a unique rational F_p point on the slice.  Independent
NF replay gives 34/34 parked plus 52/52 compatibility rows zero, Jacobian
ranks 14+52, and a `tf1_49 += 1` control makes 51 compatibility rows
nonzero.  A separate streaming replay against the original ~1 GB verdict
files verifies all 86 rows directly (30,993,910 / 30,993,618 terms replayed;
source hashes `00c9a4...881b6` / `df0af1...48105`).  Thus the literal
compressed ideal has a smooth component of dimension
`172 - 14 - 52 = 106`; this proves no upper bound on its other components.

STAGEWISE PROFILE.  For last rungs 26,28,30,32,34,36,38,40,42, the
compatibility row counts are 6,12,17,23,29,35,41,47,52; the ranks in the
level >= 53 affine layer are 4,8,10,16,22,27,33,39,44; and the Schur residual
counts are 2,4,7,7,7,8,8,8,8.  The nonlinear residual therefore stabilizes
by rung 36; later blocks add full affine row rank.  At the literal witness
the prefix Jacobian ranks equal every row count, giving smooth full-cell
component dimensions 152,146,141,135,129,123,117,111,106 respectively.
In particular the literal rung-<=38 prefix is NONEMPTY of smooth component
dimension 117.  The historical raw `upto38.ms` did NOT solve: p105337 hit
the 3-hour cap with rc=124 and a zero-byte output (340,672,955-byte input,
sha256 `fdbe3f2c...06e7ddc7`).  The earlier description of that run as
"solved" was incorrect.

MANDATORY GRAPH-LIFT GATE.  A rung compatibility is a left-kernel condition
for existence of that rung's first-occurrence coordinates.  Some eliminated
coordinates occur again in later rungs, so eliminating them independently
without adjoining their graph equations enlarges the solution set.  Both
compressed witnesses show this exactly: rung 26 has rank(A)=rank([A|b])=4
and reconstructs its coordinates, changing six values from the compressed
assignment; after that substitution, rung 28 has ranks 4/5 and is
inconsistent.  Hence neither compressed witness is a D43 survivor and
neither may enter the floor measurement.

SECOND NF AGAINST RECONSTRUCTED COORDINATES.  The corrected fixed-point
probe reconstructs every D25 represented/deep/frontier coordinate via
`d25_eplus.reconstruct_point + eplus43.completed_point_v2`, then retains all
89 pristine rung graph rows.  At the same certified D25 point
(free values 1,...,14), the system has 89 rows in 98 genuine completion
variables, 4958 terms, degree at most 2; one zero row is dropped before
solver emission.  Both 88x98 small systems solve to reduced GB `[1]` in
0.01 seconds.  The first obstruction is already the ten linear rung-26
rows: rank(A)=8, rank([A|b])=9 at both primes.  Two independent random
assignments per prime replay all 89 specialized rows against the eplus43
jet engine (178/178 exact per prime), and a coefficient perturbation is
detected.  An additional pointwise search over 21 completed a00pp D25
points per prime finds 0/42 prolongations: every joint bands-26-through-40
affine system is inconsistent.  These are strong pointwise obstructions,
not an empty-family certificate for the A^14 cell.

EQUIVARIANCE.  The promoted G=(C3)^2 x (C2)^2 action is free and transitive
on the 36 fibers.  The stabilizer of a00pp is therefore trivial.  It reduces
36 fiber computations to the one representative fiber, but supplies no
nontrivial character decomposition within the fixed a00pp fiber and hence
reduces none of its 144 residual variables.

VERDICT / LEDGER.  No full verdict file was passed to msolve in this lane;
only the small 52x52 and 88x98 systems were solved.  The sharpest honest
result is: the emitted compatibility-only ideal is NONEMPTY at both primes,
with a smooth dimension-106 component, but it is an overapproximation; the
intended graph-preserving D43 a00pp family remains EMPTY/NONEMPTY unresolved.
No liftable witness exists from this pass, eplus43 floor mode was not run,
and the ledger stays `ell+ >= 37`.  Machine details and hashes are in
`cases/d43_residual_final_report.json`; the principal drivers and gates are
`cases/d43_residual_deepen.py`, `cases/d43_lift_witness.py`,
`cases/d43_raw_point_system.py`, `cases/d43_verdict_witness_gate.py`, and the
paired `d43_{second_layer,witness,raw_witness_gate,lift_witness,
reconstructed_full,reconstructed_numeric_gate}_p*.{ms,out,json}` artifacts.

### 10.8 Graph-row re-emission: the commissioned 175-row ideal is NONEMPTY, but the survivor floor exposes a second omitted reconstruction layer (2026-08-23, INTERNAL / UNREVIEWED)

This pass re-emits exactly the object commissioned after the 10.7/Grok
review and decides that algebraic object.  It also runs the mandatory
`eplus43` survivor/floor gate.  The two outcomes split again:

  * COMMISSIONED GRAPH-ROW IDEAL: **NONEMPTY at both primes**, with an
    explicit smooth component of dimension 81.  Rung 28 does not kill it.
  * TRUE `D43_SURVIVOR` LOCUS: **still UNRESOLVED**.  The commissioned
    system restores the rung-26-through-42 graph, but still omits the older
    D23/D25 reconstruction graph hidden by the parked quotient.  Its
    algebraic witnesses fail the full residual gate in bands 6 through 24
    and therefore are not eligible for a floor.

EMISSION AND A CENSUS CORRECTION.  On box01 the two audit systems are

```
34 parked + 52 compatibility + 89 pristine rung graph = 175 rows.
```

Every compatibility row is regenerated as its exact constant left-kernel
combination of the graph rows and agrees BYTE-FOR-BYTE with the banked
86-row source (52/52 per prime).  The parked prefixes agree 34/34 and all
89 graph rows are retained.  A retained-coefficient perturbation changes
the derived compatibility row.  The full expanded files are:

```
p105337  2,340,905,280 bytes  sha256 015c26d57e2c...7b5ce323
p105673  2,341,124,763 bytes  sha256 367b5c30d178...2b9c380
```

They live on box01 as
`cases43/d43graph_p{105337,105673}_a00pp_full175.ms`; no full file was
passed to msolve.  Direct independent streaming evaluation of the expanded
text gives 175/175 zeros at both witnesses, respectively replaying
69,536,652 and 69,536,382 terms.

The true graph header has **184**, not 172, variables.  The compatibility
header had eliminated twelve final-rung first-occurrence coordinates:
`Xf_alpha,Xg_beta`, `tf1_69,tf1_74,tf2_69,tf2_74`,
`tg1_69,tg1_74,tg2_69,tg2_74`, and `tg01_74,tg02_74`.  Retaining the
rung-42 equations requires adjoining them.  Thus the statement in the
10.7 review that the 89 graph rows live in the 172-coordinate ring is
source-inconsistent and is corrected here.

NONEMPTY CERTIFICATE AND DIMENSION.  At the same certified parked-cell
point used by 10.6/10.7, the 89 graph rows have 156 external variables and
288,171/288,178 terms.  A canonical origin-Jacobian pivot slice keeps 89
variables and sets the other 67 graph variables to zero.  Its 89 equations
have 13,236 terms and degree at most 3.  msolve 0.10.1 (`-g 2 -t 4`, seed
843) returns in 0.01 seconds at each prime a reduced basis of 89 completely
linear elements.  Decoding those bases gives explicit 184-coordinate
points.  Exact replay gives

```
parked 34/34 + compatibility 52/52 + graph 89/89 = 175/175 zero.
```

At each point the parked Jacobian rank is 14 and the graph Jacobian rank in
the external coordinates is 89.  Compatibility rows are redundant graph
combinations, so the combined rank is 103.  Conversely the parked cell is
smooth of dimension 14 and 89 graph equations can cut its 156-dimensional
external bundle by at most 89.  Hence the witnessed local dimension is
exactly

```
184 - 14 - 89 = 81,
```

and the component is smooth.  This is a component dimension, not an upper
bound on every component.

RUNG-26/28 GATE AND THE <=38 PREFIX.  At both explicit points the exact
current-rung ranks are

```
rung 26: rank(A) = rank([A|b]) = 4; prefix Jacobian rank 10/10,
rung 28: rank(A) = rank([A|b]) = 4; prefix Jacobian rank 20/20.
```

Thus forward reconstruction has a consistent section at rung 26 and still
has one at rung 28; the rung-28 gate does **not** cut this component to
empty.  The prior rank 4/5 result concerned one nonpivot-zero section of a
different compressed witness and is not locus-wide.  At rung <=38 the same
witness gives graph Jacobian rank 69/69.  An independently emitted 69x69
prefix slice (6,549 terms) solves in msolve in 0.01 seconds at each prime to
a 69-element completely linear basis.  In the prefix's 162-variable used
ring the combined rank is 14+69, so its witnessed smooth component has
dimension 79.  This is the requested first-depth test: it is NONEMPTY, not
a first depth kill.

PIVOT/NF ATTEMPT.  Exact substitution of the parked triangular map on the
derived W-component turns the unsliced rung <=28 graph prefix into 20 rows
in 98 variables, with 134,891/134,892 terms and degree at most 14.  All 12
prefix compatibility rows are re-derived exactly, the coefficient
perturbation is detected, and the graph Jacobian has full row rank 20 at
both the origin and the deterministic sequence point.  The uncut systems
hit the 1,800-second msolve cap at both primes with zero-byte basis output.
This route is therefore solver-inconclusive; the explicit linear slices
and their direct full-system replay, not this timeout, prove NONEMPTY.

GATES.  The parked NF replay passes all 32 prime-components, with 34/34
parked polynomials identically zero and every reconstructed-coordinate
negative control firing.  The independent jet-engine replay gives 178/178
exact raw graph-row comparisons per prime at two random assignments, and a
coefficient perturbation is detected.  At each algebraic witness,
`Xf_alpha += 1` makes ten graph equations nonzero.  Both primes have the
same row/rank/dimension/floor-failure signatures.

MANDATORY FLOOR GATE -- REJECTED.  Feeding either algebraic point to the
full `eplus43` `D43_SURVIVOR` gate makes 94 of the older selected residual
coefficients nonzero.  Their band census is

```
band 6:9, 8:10, 10:9, 12:9, 14:10,
     16:9, 18:9, 20:10, 22:10, 24:9
```

at both primes.  Therefore `s9_d43_residual_184_zero` and `s9_nu_ge_43`
fail.  The reason is structural: variables representing coordinates that
the D23/D25 parked presentation had eliminated were reintroduced as free
deep variables when the D43 rows were emitted.  Adding the 89 later graph
rows repairs the 10.7 omission but does not adjoin those earlier
reconstruction equations.  This is why the 175 equations can vanish while
the underlying jet has nonzero older bands.  The fully reconstructed
point probe of 10.7 (rung-26 rank 8/9) remains valid pointwise evidence in
the opposite direction; it is still not an A^14-family certificate.

VERDICT / LEDGER.  The exact answer for the commissioned 175-row ideal is
**NONEMPTY, smooth dimension 81**, both primes; rung <=38 is already
NONEMPTY of smooth dimension 79 and rung 28 is consistent.  But the
identification of that ideal with the true D43 survivor family is refuted
by the mandatory residual gate.  No `eplus43` floor is reportable (the
internally computed window number 37 is diagnostic only), no first depth
kill is proved, and the honest true-family status remains UNRESOLVED with
`ell+ >= 37` unchanged.

Machine record: `cases/d43_graph_final_report.json`; emissions and direct
replays: `cases/d43_graph_{emission,full_gate}_p*.json`; explicit points and
floor rejection: `cases/d43_graph_{witness,floor}_p*.json`; prefix solve:
`cases/d43_graph_prefix_slice_p*_upto38.{ms,out,err,json}`.  Principal
drivers are `cases/d43_graph_family.py`, `cases/d43_graph_witness.py`,
`cases/d43_graph_full_gate.py`, `cases/d43_graph_prefix_slice.py`,
`cases/d43_graph_nf.py`, and the corrected non-reconstructed x-name path in
`cases/d43_raw_point_system.py`.  All artifacts are INTERNAL / UNREVIEWED.
