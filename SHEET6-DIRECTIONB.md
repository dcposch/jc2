# SHEET6-DIRECTIONB.md — the J-jet strike at the resonant direction b

Status: COMPLETE, UNREVIEWED (2026-08-12). Target: the L1 §7.2
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
refuted as stated): they cancel structurally. Reason (joint-tree
pairing): J depends on branch data through log-derivatives of pairwise
DIFFERENCES z_j - y_i (f = phi_f prod(y - y_i), g = phi_g prod(y - z_j)
gives J = fg[sum_j c_j/(y-z_j) - sum_i d_i/(y-y_i)], c_j, d_i =
log-derivative sums of (z_j - y_i)); coefficients SHARED between f- and
g-arcs riding the same tree edge (uf, vf — forced shared by the E7
exact d_g ladder) cancel in every low-order difference. What the first
J-orders see is precisely the data the joint tree does NOT pair: the
f-vs-g tail splits (tf vs tg) and the B-cluster tails.

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
(slot 20), where (eta^3 - b) surfaces — this explains the observed
identical vanishing of rows 1..10 on the frozen stratum and locates ALL
dead-stretch discriminating power at the resonance window.

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
no saturation subtleties (contrast SHEET6-R1 §17-19: the R1-tier
witness kills needed the s1F-saturation standing rule; the J-tier kill
of the same zero-extension locus is direct).

Adjudication of the three pre-registered outcomes:
- NOT "INCONSISTENT on the dead-stretch grid" as Grok item 3 posed it:
  the J-jet's first 20 orders are structurally BLIND to the grid
  (Theorem J1 mechanism: shared joint-tree data cancels from the
  log-derivative transport); the grid coefficients enter the window
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

Retro-diagnosis of the R1 record: every banked witness family
(SHEET6-R1 §13.4/§16) was a zero-extension — exactly the locus the
J-rows kill outright. The band/quotient ladder could always be
satisfied by zero-extensions because the J-closure (R5) was never
expressible in the y-side model as then formulated; §0's x-side-window
observation shows the first 41 J-orders WERE expressible all along.
The "receding discriminant" phenomenology (Grok stress-test A) is
resolved: the discriminating rows existed, one tier further down, at
the single window every diagnostic pointed to.

## 6. Ledger, trust perimeter, reproduction, next objects

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
   [Status at close of session: the 83-var tails build (7 dead-stretch
   + all P-side tails free, B frozen) is LAUNCHED and running
   (/tmp/tails21.log, banks to /tmp/directionb_tails.pkl); the
   f-side through-orbits are built; sizing is jet-tier (est. 1-3 h
   local). Its verdict semantics, pre-registered: rows 6..19 = linear
   tail pins (Row_6-type, rank measured per row); Row_20 = the
   inhomogeneous window with the w^4-block of §2c + tail columns +
   (7 x tail) cross-terms; INCONSISTENT = full-window residue-A kill;
   consistent = exact characterization of the forced-tail locus.]
2. Extend (J) to rows 21..41 (still pure y-side; the h2-resonance
   b2 = (3/4) sigma sits at slot 24-ish content) — same machinery,
   deeper truncation.
3. Port the row builder to the 6 sibling templates (§5(ii)) — their
   resonance windows may be overdetermined the same way; a uniform
   9-on-2-type theorem would drain the whole book's zero-extension
   loci.
4. Rows k = 42+ with the x-side model (LR2 pin, SHEET6-R1 §16.5):
   the first x-side-coupled J-orders — the R5 completion.
