# SHEET6-DIRECTIONB-REVIEW.md — Adversarial review of SHEET6-DIRECTIONB (dc0918b)

Reviewer: Claude (adversarial pass, 2026-08-12). Status: COMPLETE.
Scope: the J-jet strike — the claimed zero-tail (zero-window-tail) kill
of the residue-A template, its identity (J), Theorem J1, the Row_20
9-on-2 system, the R1-witness corollary, and the E5-erratum
interaction. Method: every load-bearing identity re-derived from
scratch on paper; a NEW zero-shared-code verifier written for this
review (/tmp/xdb/rev_check.py) that is strictly STRONGER than the
strike's own numcheck — it drives the 7 dead-stretch coefficients with
random NONZERO values (numcheck froze them to 0, so the blindness
claim had only a single verification path before this review) and
independently re-extracts the c1/c2 coefficient system; engines re-run
(gate, rows 7, solve6, dsys 21, w4, numcheck at a fresh prime); R1/
TEMPLATE/TEMPLATE-ATTACK promoted records cross-read; two external
referees (grok, codex) run on a self-contained brief.

Verdicts:
- Front 1 (the identity): **CONFIRMED** — exponents 12/18, slot 20,
  chart Jacobian -42 t^{-11}, RHS -(42/(c_f c_g)) t^20 all re-derived
  independently; no missing Jacobian factor; x-side (1+O(t^42))
  factors provably cannot pollute rows k <= 41. grok concurs; codex
  concurs on substance (wording nit E6 on "EXACTLY").
- Front 2 (Theorem J1 / blindness): **CONFIRMED, with one downgrade**
  — the partial-fraction identity, the 315-branch equivalence and the
  h1-transport form are correct (re-derived); but the "joint-tree
  pairing" paragraph is a heuristic, NOT a proof of rows-0..19
  blindness (uf enters UNMATCHED B-factors at slot 6 and off-axis
  A-factors; the pairing argument does not cover those channels). The
  blindness itself is an exact verified identity: engine symbolic +
  THIS review's independent nonzero-dead-stretch mod-p test at two
  fresh primes + grok's and codex's own (4 paths total); codex also
  proposes the correct closed-form mechanism (2:3 orbit cancellation,
  §2 addendum — sufficiency verified by this reviewer).
- Front 3 (Row_20): **CONFIRMED** — 9 components, exact 2-term form on
  (alpha_1 w_1^4, alpha_2 w_2^4), the 8 ratio pins verified mod 2
  fresh primes AND pairwise-distinct exactly over Q(sqrt3) (28/28
  pairs); the system is LINEAR in (X_1, X_2), so w_i^4 = 0 is forced
  outright, not a factorization branch; the eta^0 row 0 = -42/(c_f c_g)
  is a second, independent absurdity that does not even need w_i != 0.
- Front 4 (wrong-object audit): **THEOREM CONFIRMED, COROLLARY
  REFUTED** — the §3 stratum theorem is real, but the §5
  retro-diagnosis and the headline/commit claim "killing every banked
  R1 witness" are a WRONG-OBJECT slip (the s1F-lesson pattern, caught
  here): the banked SHEET6-R1 §13.4/§16 witnesses carry NONZERO window
  tails tf1_47, tf2_47, tf1_52, tf2_52 (levels 47/52 = window slots
  15/20; measured in R1 §14.3, family support in §18.1) and are NOT in
  the kill stratum. "Zero-extension" (R1 sense) != "zero-tail" (strike
  sense). Residue-A is NOT closed; the genuinely new coverage is the
  pure-dead-stretch sector (details §4 below).
- Front 5 (E5 factor-of-3): **CONFIRMED INDEPENDENT** — the ring keeps
  w_1, w_2 symbolic (rnorm has no w-power reduction; the E5 relation
  enters the R1 sat-objects only as explicit rows, never this build);
  the kill uses only w_i != 0 — and even that is redundant (the eta^0
  row alone is absurd). Nothing in the strike moves under 243-vs-729.
- Front 6 (externals): grok CONFIRMED/CONFIRMED/CONFIRMED (own
  re-derivation + own nonzero-stretch mod-p product at p=200257 +
  numcheck at fresh p=314329); codex GAP(wording)/CONFIRMED/CONFIRMED
  (own nonzero-stretch product at p=400849; proposes the 2:3
  orbit-cancellation mechanism, adopted as a banked candidate lemma);
  the one split (front 1) adjudicated CONFIRMED-with-nit in §6.

THE CALL: **the zero-tail kill STANDS as a theorem** — at the
strongest verification tier in the campaign (5 independent paths). The
"biggest kill / central counterexample family" framing does NOT stand:
the killed stratum contains NONE of the banked R1 witnesses (all
tail-loaded, and already dead by the §18.1 saturation kill). What the
strike genuinely closes is the pure-dead-stretch sector; what remains
of residue-A is exactly the forced-nonzero-tail window — the 83-var
tails build plus the R1 deep strata. Details below.

## 1. Front 1 — the chart identity (J), re-derived from scratch

Verdict: **CONFIRMED**. Everything below is this reviewer's own
derivation, checked afterwards against §0 and the engine.

- Chart Jacobian: x = t^{-42}, y = P(t) + eta t^32 gives
  d(x,y)/d(t,eta) = x_t y_eta - x_eta y_t = (-42 t^{-43})(t^32) - 0
  = -42 t^{-11}. (y_t never enters: x_eta = 0.) The chain rule
  J_{t,eta}(f,g) = J_{x,y}(f,g) . J_{t,eta}(x,y) turns J_{x,y} = 1
  into J_{t,eta}(f,g) = -42 t^{-11}. No missing factor.
- Exponents 12/18 from branch counting (independent of the doc's
  d_F/d_g shortcut): 126 f-branches = 12 through (P1/P2, c = 7j) + 114
  others; normalizing through factors by t^32 and others by t^12,
  prod(y - y_i) = t^{12.32 + 114.12} Phi = t^{1752} Phi, against
  phi_f ~ c_f x^42 = c_f t^{-1764}: f - a = c_f t^{-12} Phi (1+O(t^42)).
  g-side: 18 through (Gp1/2: 12, G0p1/2: 6), 171 others: t^{2628} vs
  deg phi_g = 63: t^{-2646}: g = c_g t^{-18} Gamma (1+O(t^42)).
  Consistency: t^{-12} = x^{2/7} = d_F, t^{-18} = x^{3/7} = d_g (E7
  ladder), and 42 = kappa. All three integers (12, 18, 42) come out.
- The identity: with f = c_f t^{-12} Phi U_f(t), U_f = 1 + O(t^42)
  pure in t (phi_f's subleading terms ride x^{-1} = t^{42}; elementary
  symmetric functions of the x-roots contribute only t^{42m}),
  f_t g_eta - f_eta g_t = c_f c_g t^{-31} [ U_f U_g ((t Phi_t - 12
  Phi) Gamma_eta - Phi_eta (t Gamma_t - 18 Gamma)) + t U_f' (...) ],
  and U' = O(t^41) makes every correction O(t^42) relative. Equating
  to -42 t^{-11}: bracket = -(42/(c_f c_g)) t^20 exactly through row
  41. Slot 20 = -11 - (-31) = the eta-offset 32 - 12. Row 20 is amply
  inside the clean window.
- Row_k as printed (§0) matches jrows() in the engine term-for-term
  ((i-12)F_i G_j' - (j-18)G_j F_i', i+j = k).
- Slot-20 = h1-resonance: g^2, f^3 both lead at t^{-36}; the E1 gate
  (G_0^2 - F_0^3 = 0 identically, re-run PASS) drops h1 to t^{-16} =
  x^{8/21} = the promoted d_h1; drop depth 36 - 16 = 20 = eta-offset.
  The three-way coincidence claim (J-inhomogeneity / h1-window top /
  eta-offset) checks.
- Sign conventions: only nonzeroness of the RHS is load-bearing;
  J = const != 0 scales the RHS, never kills it. The gauge value
  c_f = c_g = 1 (S_R = G_R = 1) is not load-bearing either; caveat
  (ii) of §6 is honest.
- Chart-convention anchoring (the s1F-style wrong-object risk probed
  directly): the eta-at-level-32 convention is validated by the gate
  — F_0 = S_M[(eta^3-a1)(eta^3-a2)]^2 reproduces the promoted E6
  transport EXACTLY, which fails for any other eta-level; a wrong
  weight RATIO would break Row_0 == 0 (hand check: -e_f F_0 G_0' +
  e_g G_0 F_0' = S_M G_M P^4 P' (2e_g - 3e_f), zero iff e_g/e_f =
  3/2); the ABSOLUTE weights (12, 18) are fixed by the branch count
  above, independent of any gate. All three failure channels are
  closed by independent evidence.
- Gate re-run this review: 4/4 PASS (E6 f/g leads, E1 tower, Row_0).

## 2. Front 2 — Theorem J1 and the blindness claim

Verdict: **CONFIRMED, with the mechanism downgraded to heuristic**.

Re-derived (all correct):
- Partial fractions: J/((f-a)g) has y-deg(J) <= 126+188 = 314 < 315 =
  deg_y((f-a)g); residue at y = y_i is -(log g(x,y_i))', at z_j is
  +(log(f-a)(x,z_j))' (the phi'/phi terms reassemble exactly as
  claimed — checked by expanding sum_{i,j}(z_j'-y_i')/((y-y_i)(y-z_j))
  over 1/(z_j-y_i)).
- 315-branch equivalence: along y_i, f = a forces y_i' = -f_x/f_y, so
  (d/dx)g(x,y_i).f_y = -J|_{y_i}; conversely the 315 identities make
  J - 1 (y-deg <= 314) vanish at 315 distinct branches, hence J == 1.
  The count is tight (314 < 315) but correct; distinctness is the
  template's squarefree pattern.
- h1-restriction: h1|_{y_i} = g^2, h1|_{z_j} = -s0(f-a)^3, giving the
  -2/+3 transport laws. NIT (E3): "(f g_y)|_{z_j} = +3" should read
  ((f-a) g_y); harmless under the declared a = 0 gauge only.
- The identification with L1 §7.2 (SHEET6-L1 §7 item 2: the missing
  global h1-accounting at b) is a fair structural reading: the J-rows
  are graded pieces of an h1-log-derivative transport, and the first
  order seeing through-cluster interior data is the h1-window top.

The DOWNGRADE (shared finding with grok): §2's "Reason (joint-tree
pairing)" explains why SHARED uf/vf cancel from paired differences
z_j - y_i, but uf18/24/30 also enter UNMATCHED channels — the B/GB42/
GB21 factors (P-side dead-stretch at slots 6/12/18, nothing to pair
against) and the off-axis A-factors (uf(1 - zeta^{18c}) etc.). The
pairing argument does not cover those; a leak into Row_6..Row_19 was a
priori possible. It does not happen — but that is a MEASURED exact
identity, not a consequence of §2b. The doc's own §2 phrasing
("cancel structurally... Reason (joint-tree pairing)") overstates the
proof status of the mechanism; the vanishing itself is at the exact
tier. Recommended relabel: "verified exact cancellation; pairing
covers the A-A channels, B-channels verified by computation".

Verification of the blindness itself (now 4 independent paths where
the strike had 1):
- Engine symbolic (re-run this review): dsys 21 reproduces rows 0..19
  == 0 as polynomials in the 7; Row_20 carries no var-keys.
- THIS REVIEW's verifier /tmp/xdb/rev_check.py — written from scratch
  against the R1 §3.0 data model, zero shared code, direct 315-factor
  product over F_p[eta,t]/(t^21) with the 7 dead-stretch coefficients
  at RANDOM NONZERO values (two independent draws + the zero draw,
  five (w1,w2) points): rows 0..19 vanish and Row_20 is IDENTICAL
  across all draws, at p = 314329 and p = 521137. This is the test
  numcheck could not perform (it hardcodes the 7 to 0); the strike's
  "triple-prime zero-shared-code" verification did NOT cover the
  blindness claim — it does now.
- grok's own product with nonzero stretch values at p = 200257: same.
- codex's own product with the 7 at (111,...,777), p = 400849: same.
Schwartz-Zippel: each row has degree <= ~330 in the 7; the
independent random draws at three primes bound a false-vanishing at
< 10^-10, on top of the exact symbolic run.

ADDENDUM (codex's proposed closed-form mechanism, banked as the
candidate replacement for §2b's pairing story): the orbit-block
products carry an exact 2:3 structure — pairing c with c+21, a
through f-block is A_c^2 - q_c (q_c = O(t^10)) while the matching
Gp+G0p-block is A_c(A_c^2 - (3/2)q_c) = A_c^3 (1 - q_c/A_c^2)^{3/2}
+ O(q^2), and the off-axis/B-blocks are exact square/cube pairs, so
Phi = C_F H^2 + O(t^20), Gamma = C_G H^3 + O(t^20) for a COMMON H.
Sufficiency verified by this reviewer: for ANY H(t,eta), the bracket
with (Phi, Gamma) = (c1 H^2, c2 H^3) and weights (12, 18) vanishes
IDENTICALLY (functional mod-p test, 0 nonzero coefficients; control
at weights (12,19): 900 nonzero — the vanishing is exactly the
2 e_g = 3 e_f resonance). This also explains Row_20's shape: the
first 3/2-vs-square mismatch is O(q^2) = O(t^20) and q's t^5-content
is the w-term — hence the pure alpha_i w_i^4 loading. Proposed as a
lemma worth proving exactly (it would upgrade the blindness from
measured identity to closed form); NOT yet at proof tier.

## 3. Front 3 — Row_20: the 9-on-2 system and the contradiction

Verdict: **CONFIRMED**, at the strongest tier available.

- dsys 21 re-run this review (fresh build, §7 ledger): rows
  0..19 identically zero with the 7 symbolic; Row_20 = exactly 9
  eta-components (0,3,...,24), each with empty var-support and radical
  support inside {a1 w1^4, a2 w2^4}; w4 re-run: 33/33 PASS including
  tau-covariance c2 = conj(c1) and det(eta^3, eta^6) != 0.
- Independent coefficient extraction (this review): probing my own
  315-factor product at (w1,w2) = (1,0)/(0,1) recovers c1[n], c2[n];
  the eight ratios -c2/c1 match the doc's §2c table EXACTLY mod both
  fresh primes; linearity (no cross-terms, no w-degree other than 4)
  confirmed at two generic (w1,w2) points; c1[0], c2[0] != 0
  confirmed; Row_20 == 0 at w1 = w2 = 0 (so the bracket has NO pure
  constant at eta^0 — the entire -42 must come from the RHS, i.e. the
  eta^0 row is a genuine constraint, not an identity).
- Pairwise distinctness: verified EXACTLY over Q(sqrt3) — all 28
  pairs of the 8 ratios distinct (a 2-line exact computation; the doc
  only needs one distinct pair, it has 28).
- Forcing, not branching: the system is linear in (X1, X2); rank 2
  gives X1 = X2 = 0 as the unique solution — there is no residual
  factorization branch to hide in. alpha_i^3 = 3 +- sqrt3 != 0 in
  every embedding, so w_i^4 = 0 follows; w_i = 0 contradicts the E5
  pin/Prop 5.3 squarefreeness. INDEPENDENTLY, the eta^0 row reads
  0 = -42/(c_f c_g) with no reference to w at all. The kill is
  double-anchored; it needs NO saturation rule (contrast the §17
  s1F story) — the "direct" claim of §3 is justified.
- The numcheck engine itself: audited (zero shared code confirmed —
  plain ints, own root-finder, own product; the only import from the
  strike side is the banked pkl it compares AGAINST, which is the
  point). Re-run at a fresh prime: PASS. Nthrough = 12, orbit census
  126/189 verified against the promoted §3.0 data model.
- NIT (E2): the unused engine phase `danal` still contains the
  PRE-measurement expectation ("Row_20 eta^0 const == -42... the
  zero-extension satisfies the inhomogeneous J-row") — the opposite
  of the measured verdict; it FAILs against the banked pickle. Dead
  code, not cited by the doc; should be deleted or fixed to avoid a
  future wrong-object reading.

## 4. Front 4 — the wrong-object audit: what the kill actually covers

Verdict: **the §3 theorem is real; the §5 retro-diagnosis and the
headline "killing every banked R1 witness" are REFUTED** — this is
the one-wrong-object-per-layer slip of this sheet, and it is in the
INTERPRETATION layer, not the mathematics.

The measured facts, from the R1 record itself:
- SHEET6-R1 §14.3 (both primes): at the banked §13.4 witnesses "the
  only NONZERO back-mapped values are x15, x18, x28, x31 = tf1_47,
  tf1_52, tf2_47, tf2_52 — F_s slots 35 and 40". Levels 47 and 52 are
  G_m window slots 15 and 20 — INSIDE the strike's window (slots
  1..20). §18.1's symbolic family build confirms the support
  ({tf1/2_42, tf1/2_47, tf1/2_52, tg1/2_42}, the 42-levels vanishing
  at the banked points but not identically). Artifact-anchored this
  review: systems/r1/r1_minimal_ext.rows.txt lines 340/343/353/356
  print the var map verbatim ("x15 = tf1_47 (level 47)" etc.) — no
  naming ambiguity between the R1 F_s registry and the strike's G_m
  registry (same build_generators tails).
- The strike's kill stratum (§3 SCOPE): ALL tf*/tg* (levels 38..52)
  and bf/bg* (13..32) = 0. The banked witnesses are therefore NOT in
  the kill stratum — they miss it in exactly 4 coordinates.
- Diagnosis: "zero-extension" in the R1 record means FREE directions
  set to 0 (plus zero-extension beyond depth 54); the 4 nonzero tails
  are ELIMINATED coordinates back-mapped through the §10/§13 chains —
  the R1 core itself FORCES them nonzero on its witness section. The
  strike doc conflated the two senses. (Historical note: the witness
  family was in any case already DEAD — §18.1's char-0 saturated
  quotient-tier kill; the strike could at most have re-killed it.)
- Is zero-tail template-forced or a choice? A CHOICE: the tails are
  free 1c data (TEMPLATE §4 inventory; R1 §18.0: tails "NOT forced —
  free template parameters"). Nonzero tails are consistent with the
  promoted genome — indeed the R1 record's only surviving sections
  are tail-loaded. So the kill closes a stratum, exactly as caveat
  (i) of §6 states — the doc's own fine print is honest; its
  headline/§5/commit-message are not.

What the strike GENUINELY adds (and it is real):
- The pure-dead-stretch sector {any values of the 7, all window tails
  0} was previously covered by NOTHING: the R1 §19.2 l13 proof-tier
  kill ZEROES uf18/uf24 (slots 6/12 < 13) on its stratum, so
  configurations with uf-support and no tails were out of its scope.
  The strike kills them all, char 0, uniformly, saturation-free, and
  by frame-homogeneity on all 10 residue-A panels (the rows k <= 20
  consume only the shared merge genome; panel differences are x-side/
  entry data, which cannot enter before t^42 — front-1 verified).
  This resolves Grok item 3 (the seed proposal) in the refined form
  the doc states: the grid is J-blind through slot 20; the kill is
  one level down, on the pole scales.
- The composition statement (§3 SCOPE end) is correct once restated:
  survivors need a nonzero free below slot 13 (R1 §19.2, on the l13
  complement) AND nonzero window tails (this strike) — two
  independent row systems. The banked witnesses already satisfied
  both requirements, which is exactly why neither system kills them.
- The retro-diagnosis SHOULD read: the band/quotient ladder never saw
  the J-closure, and the survivor sections it produced are precisely
  tail-loaded in the slot-15/20 window — consistent with (and mild
  evidence for) the strike's forced-nonzero-tail theorem; NOT killed
  by it. The "receding discriminant" resolution claim survives in
  this weakened form.

MANDATE R1 (blocking for promotion): rewrite §5's retro-diagnosis
paragraph and the commit-message claim; the strike kills the
zero-tail stratum, not the banked witnesses. The doc must not enter
the trust ledger with "every banked R1 witness shape killed".

MANDATE R2 (the real next object, unchanged from the doc's own §6):
the 83-var tails build (running at close of the strike session) is
where the actual banked-witness shapes get decided; its Row_15/Row_20
tail columns are exactly the coordinates the witnesses live on.

## 5. Front 5 — the E5 243-vs-729 interaction

Verdict: **CONFIRMED INDEPENDENT — nothing in the strike moves**.

- Code fact (audited): the radical ring reduces h_i^2 -> (3/2)w_i^2,
  alpha_i^3 -> a_i, etaB^7 -> 3/2, z via Phi42 — and has NO reduction
  on w-powers (rnorm, r1_experiment.py). w1, w2 are genuinely free
  ring radicals; the E5 quartic relation w_i^4 = k_i alpha_i^2 is
  imposed ONLY as explicit rows in the R1 §18 saturated objects,
  never in this build. (The §3.0 prose listing w_i^4 = k_i alpha_i^2
  among the RING relations is stale vs the implementation — a
  pre-existing R1 doc nit, harmless here and actually load-bearing
  in the strike's favor.)
- Consequently Row_20's c1/c2 never consumed any E5 constant; my
  independent verifier reproduces them with no E5 input at all.
- The kill consumes E5 only via "w_i != 0", which holds under BOTH
  readings (the pin k_i is nonzero iff a_i != b and H_M != 0 — scale
  free; the TEMPLATE erratum note itself says H_M is unit-rescalable
  in every consumer). And the eta^0 contradiction 0 = -42 does not
  consume w != 0 at all. Double insulation.
- The disputed constant also does not touch the g-side scale used in
  the build (hw_i^2 = (3/2) w_i^2 = the B = 3/2 gauge datum, §3.0),
  which my verifier consumed independently and which the banked
  ratios confirm.
- Status note: the parallel adjudication has in fact LANDED
  (SOL-ALGEBRAIZATION header, 2026-08-12): E5 factor decided in SOL's
  favor (cleared-row constant 243; TEMPLATE line 239 patched;
  "unit-rescalable, NO banked verdict flips" — and SOL independently
  notes the w1^4/w2^4 RATIO is unchanged). The strike is insulated
  from the dispute under either outcome; under the landed one, even
  the w != 0 citation is undisturbed.

## 6. Front 6 — external referees (both run on the self-contained
## brief, fronts 1-3; full outputs /tmp/xdb_grok.out, /tmp/xdb_codex.out)

- grok: FRONT1 CONFIRMED (own re-derivation, including the branch
  count 12.32 + 114.12 route and the O(t^42) pollution bound);
  FRONT2 CONFIRMED (own residue computation; independently flags the
  pairing mechanism as "a correct leading heuristic, not a
  closed-form proof" — adopted above); FRONT3 CONFIRMED (banked
  constants re-extracted; ratios pairwise distinct; "linear, not a
  factorisation"; 243-vs-729 unused; own nonzero-dead-stretch mod-p
  product at p = 200257 + numcheck at fresh p = 314329: all PASS).
- codex (finished within budget, exit 0): FRONT1 GAP (wording only:
  "all weights, signs, and rows through 20 are correct, but 'EXACTLY'
  omits the x-unit terms unless those units are absorbed" — its own
  computation puts the first unit correction at slot 42, RHS unit
  correction at slot 62); FRONT2 CONFIRMED ("J1, the 315-branch
  equivalence, and no leakage below 20 hold; the stated
  pairwise-cancellation explanation must be replaced by orbit-level
  2:3 cancellation" — see front 2 addendum below; own 315-factor
  product at p = 400849 with the 7 at (111,...,777): rows 0..19 zero,
  Row_20 unchanged); FRONT3 CONFIRMED ("exact rank-two homogeneous
  block forces X1 = X2 = 0, the eta^0 RHS is then impossible,
  independent of 243 versus 729"; exact norms of all 28 pairwise
  ratio differences nonzero, e.g. N(r3 - r6) = -3136/11891 —
  re-verified exactly by this reviewer; also independently found the
  danal defect = E2, and confirmed the ring keeps w free).
- Adjudication: no disagreement to adjudicate on the mathematics —
  both externals' COMPUTATIONS agree with each other and with this
  review's on every number checked (rows 0..19 vanishing, Row_20
  support/constants, ratio table, blindness under nonzero
  dead-stretch). Independence note: grok completed BEFORE this review
  file existed (clean referee); codex read the in-progress review
  file mid-session (its transcript, lines 2641/2779), AFTER its own
  fronts-1-3 computations were designed and largely run — its
  numerical work is independent, its final wording may not be. The
  one substantive external contribution beyond confirmation is
  grok's B-channel observation (front 2 downgrade), independently
  found by this reviewer and adopted; codex sharpens it further (the
  pairing sentence is not merely incomplete but false if read across
  phases: u18 contributes u18(zeta^{18c} - zeta^{18d}) in
  differently-phased differences). The single verdict-level split —
  codex FRONT1 GAP vs grok/this-review CONFIRMED — is adjudicated
  CONFIRMED-with-nit: the doc's §0 display carries the (1+O(t^42))
  factors explicitly, so "EXACTLY" correctly scopes to rows < 42
  (all that is used); codex agrees every row through 20 is clean.
  Recorded as wording nit E6, not a gap in the kill.

## 7. Ledger

Checks run this review (all on the strike's declared gauges):
- gate 4/4 PASS; rows 7 (Row_1..5 == 0 with ALL frees; Row_6 = 10
  components, all consts 0, no dead-stretch vars — §2 reproduced);
  solve6 (rank EXACTLY 8, homogeneous) PASS.
- dsys 21 fresh rebuild (701 s): rows 0..19 identically 0 with the 7
  symbolic, Row_20 = 9 components; w4 on the fresh pickle: 33/33 PASS,
  ratio table byte-identical to §2c.
- numcheck at fresh prime p = 400849: PASS (rows 0..19 + all 40
  eta-slots of Row_20 vs the fresh exact constants).
- NEW cross-path closure: the fresh pickle's exact K3 constants
  compared against THIS review's independent extraction for ALL 9
  components including eta^0 (which the doc's table omits): 18/18
  MATCH at p = 314329. For the record, c1[0] =
  K(-1/512 + sqrt3/1024), c2[0] = conj, K =
  49293537215743968438156925563 — both nonzero, tau-covariant.
- /tmp/xdb/rev_check.py (this review's independent verifier):
  p = 314329 and p = 521137, 16/16 checks each, CLEAN — including
  nonzero-dead-stretch blindness, Row_20 2-term linearity, ratio
  table, dets, and the no-pure-constant fact at eta^0.
- Exact pairwise-distinctness of the 8 ratios over Q(sqrt3): 28/28.

Errata/nits (non-blocking except E1):
- E1 = MANDATE R1 (§4): wrong-object retro-diagnosis — blocking for
  any promotion of the "banked witnesses killed" reading.
- E2: stale `danal` expectation (pre-measurement hypothesis, FAILs
  against the banked system); delete or fix.
- E3: §2b "(f g_y)" for "((f-a) g_y)" — harmless under a = 0 only.
- E4: §2/§2b blindness mechanism is heuristic for the B-channels;
  relabel as measured identity (front 2 above).
- E5-nit: §1 "gate 4/4" and §2c "PASS x3" claims reproduce; the
  commit's "33/0" is the w4 check count (33 checks, 0 fail),
  reproduced.
- E6 (codex): "EXACTLY" in §0 should say "exactly through row 41" or
  absorb the x-side units into hatted Phi/Gamma; rows <= 20 (all that
  is used) are unconditionally clean — wording only.

Trust perimeter of this review: promoted genome (SHEET6-TEMPLATE,
SHEET6-L1, R1 §3.0 gauges) taken as given, per the strike's own §6(a)
scope; the thesis chart conventions were checked against the R1
engine's promoted data model, not re-derived from Sigray. The §4
quantum rider was spot-checked against TEMPLATE-ATTACK 1c.2 (V(b) =
-878 sigma^9/9261 matches the banked value; direction-honesty of
(ii)/(iii) verified — no kill is claimed there and none should be
read there).

## R1 internal review (Fable, 2026-08-13)

VERDICT: **SOUND-WITH-ERRATA** — the survival claim ("NOT
EMPTY-BY-KILL: the 83-var forced-nonzero-tail window does not kill
residue-A") reproduces exactly, survives a wrong-object audit of the
load-bearing relaxation, and its §6.V claim (4) is confirmed by an
independent reconstruction this review had to build (no engine phase
implements it); the errata are (i) the `slot20` phase FAILs 24/27 of
its own checks (stale pre-result check text asserting the OPPOSITE of
the banked narrative) and prints a nonexistent "explicit point", (ii)
one §6.V justification states a wrong mechanism (eta^0 at low = 0),
and (iii) several §6.V sentences claim more quantifier coverage
(functionals, "uniformly in the 7", branch coverage of the shipped
command, B-side freeze omitted from V's definition) than the code
path proves. No finding flips the verdict.

Scope: SHEET6-DIRECTIONB §6.T (line ~383) + §6.V (line ~469-545 at
review time; the doc was under ACTIVE concurrent edit during this
review — a depth-23 status note and a "GROEBNER-TIER EMISSION"
paragraph were inserted mid-review and are NOT reviewed here).
Engine: cases/directionb_window.py @ 747 lines; state
/tmp/directionb_tails_D21.pkl (md5 8ab35ec3... == the repo bank
directionb_tails_D21.pkl; conditions pkl 4590681b... == repo bank).
Posture: hostile in both directions per the campaign's prior
wrong-object retraction (front 4 above).

### R1.0 Reproduction (check 1): EXACT MATCH
- `gate`: 16/16 PASS, 2.3 s (= 12 window checks + 4 relayed strike
  anchors; claim 16/16, ~3 s).
- `verdict`: 7/7 PASS, 105.4 s local (claim 89 s): every printed
  number identical to §6.V — (1) Row_20 relax 10 x 2718 rank 10
  CONSISTENT; full window 77 x 5106 rank 57 CONSISTENT; (2) 77 x 76
  rank 29 INCONSISTENT at both dead-stretch samples; (3) strata
  10/10/4, 19/20/8, 48/50/16, all INCONSISTENT.
- `bands` (19 s): §6.T ledger table verbatim — tier S dims/ranks
  18x6->2 ... 451x1341->173; tier V ranks 1,4,6,7,10,10,9 identical
  on all 4 branches (sum 47); NO unreduced leftovers; printed
  C6.1 / C10.6 / C16.10 match the doc character-for-character.

### R1.1 Findings, ranked

**W1 (erratum, engine-vs-doc contradiction; not verdict-breaking).**
The `slot20` phase FAILS 24 of its 27 checks: TOTAL: 27 checks,
24 FAIL. Its check text (directionb_window.py:613-617 "SOLVABLE",
cond `(not incons) and undec == 0`; :622-624 "EXACT certificate")
was written EXPECTING solvability, and the measured result is
inconsistent=True with residual defect {20: [12,15,18,21,24,27]} on
all 12 (w-sample x branch) combos — i.e. the run CONFIRMS §6.T's
prose (lines 446-457: rank 2/6, rank 4/10, obstruction eta^12..27,
uniform) while the harness records it as failure. The phase then
prints an "explicit point" (directionb_window.py:628-635) for a
system it just found inconsistent — the point satisfies nothing
(certificate defect nonzero); stale output, same pattern as E2
(`danal`) in the 2026-08-12 review. The REPRODUCTION block lists
`slot20` with no warning, so a reproducing reader meets 24
unexplained FAILs. Fix: invert/relabel the two chk conditions to the
measured semantics and delete the explicit-point print, or annotate
the REPRODUCTION line. §6.V itself does not cite slot20 check
counts, and the `verdict` phase re-establishes stratum (a)
inconsistency with correct semantics — hence not verdict-breaking.

**W2 (reproducibility gap; claim CONFIRMED by reconstruction).**
§6.V claim (4) (lines 500-507: cascade-fixed low data, 32 unreduced
rows, seed-dependent obstruction vectors, 6 rows at low = 0) has NO
code path: `cascade()` (directionb_window.py:502) is called by no
phase, and as written it could not emit the report (returns early on
incons/undec). This review reconstructed it (scratchpad claim4.py):
two cascade seeds solving bands 6/8/10 exactly (CERTIFIED: exact
`evaluate` of every banked row shows defect keys exclude 6/8/10 —
the seeds genuinely satisfy the band conditions, answering the
review brief's check 4), then bands 12..20 jointly over the 50
level>=43 unknowns: 48 eqs, rank 16, 32 residual rows, labels
(12,8)...(20,27) incl. Row_20 eta^12..27; SAME pivot set for both
seeds and residual vectors DIFFERING in all 32 of 32 rows; at
low = 0 exactly 6 nonzero residual rows, precisely Row_20
eta^{12,15,18,21,24,27}. Every quantitative element of claim (4)
checks out; the doc should either ship the phase or mark the claim
as reproduced-by-review-script only.

**W3 (wrong mechanism stated in §6.V test (3); conclusion right).**
The parenthetical at lines 497-498 — "(the third is forced: with
levels < 43 zero, the degree-3 low monomials feeding eta^0 vanish
and 0 = -42 returns)" — is FALSE as a mechanism: at low = 0 the
eta^0 row remains individually solvable (its 8 linear level-47/52
terms survive; the doc itself says at line 463-464 that the 14
linear terms alone solve eta^0). The measured obstruction is the 6
components eta^12..27 of Row_20 — eta^0 is NOT among the residual
rows (reconstruction above, and slot20's own defect print). The
stratum IS inconsistent (verified), but by the rank-4-of-10
simultaneity mechanism the doc states correctly everywhere else,
including its own claim (4). Strike or fix the parenthetical.

**W4 (quantifier/wording overclaims a hostile referee strikes).**
(a) "No functional annihilates all tail columns while detecting the
-42" (§6.V lines 480-481): proven for E-LINEAR functionals of the 77
depth-21 window rows, per (w, h-branch) fiber — not for "functionals"
simpliciter (the strata of test (3) are killed by NON-linear-tier
reasoning on the same rows, and rows 21+/Groebner deciders remain,
as §6.V's own NEXT OBJECT concedes). Say "no E-linear functional of
this row set". Likewise "the direction-b J-window is exhausted as a
killing instrument at depth 21" (lines 528-530) — exhausted at the
LINEAR tier only; the doc's own Groebner-tier NEXT OBJECT on V
contradicts "exhausted" read broadly.
(b) Test (2) "uniformly in the dead-stretch values (7 free, incl.
all-zero)" (lines 487-488): the code (directionb_window.py:715-717)
runs exactly TWO specializations — all-zero (included, as claimed)
and ONE rational sample from genval() — not a symbolic/generic-rank
proof over the polynomial ring in the 7. The sample is also not in
general position: genval gives vf2_34 = vf2_36 = 1 (repeated
values). "Uniformly ... (7 free)" overstates; write "at the all-zero
and one generic sample of the 7".
(c) Test (3b) label "levels 45/47/50/52 + the 7 : 19 eqs, 20 unk"
(line 495): the 7 are NOT among the 20 unknowns — they are FIXED at
the genval sample (code path :724-728); inconsistency is proven at
that sample of the 7 only. (3a) is sample-independent in the 7 (no
7-cross-terms reach that stratum) and was verified on all 12
(w, branch) combos by slot20; (3b)/(3c) as shipped are one-sample.
(d) §6.V preamble "one h-sign branch shown, ranks identical on all
4" (line 472): TRUE — but not established by any shipped command:
`verdict` runs ONLY (s1,s2) = (+1,+1) at w = (1,1)
(directionb_window.py:699, :744; no loop). Verified THIS review by
driver sweep: branches (+,-), (-,+), (-,-) at w=(1,1) and branch
(+,+) at w=(2,3), (1/5,7): 7/7 PASS each, ranks 10/57/29/29/4/8/16
identical everywhere. The claim should cite a command that shows it.

**W5 (object scope: what "the window" quietly excludes).**
(a) B-side freeze: the build pins ALL bf/bg* frees to 0
(directionb_strike.py:227-236, "B-side frozen"; state census: 183
registry vars, the 100 B-vars occur in NO row). §6.T/§6.V never
state this; §6.V's displayed V (lines 516-518) omits the B = 0 tag,
and "the honest surviving locus is exactly V" (line 514) is
wrong-object as written — V is the B = 0 SLICE of the J-window
locus (Row_6 loads B-side monomials when they are free, §2).
DIRECTION-SAFE for the survival verdict: restoring B-columns only
enlarges the relaxation's column span, so CONSISTENT stands a
fortiori; but the characterization sentence needs the tag.
(b) The pre-registered item-1 object (now line ~621: "R1 depth-84
quotient tier + the J-window ... with P-side tails + B-frees free")
was only HALF delivered: B-frees frozen (see (a)) and the R1
quotient-tier rows never imposed. Its [CLOSED] note is fair about
"no full-window residue-A kill" if "full-window" = all J-rows
6..20, but the JOINT object's kill question (extra R1-tier rows =
extra equations, which CAN still kill) remains open — consistent
with §6.V's "burden moves" sentence, inconsistent with reading
item 1 as closed-negative.
(c) w-fiber scope (the one caveat §6.V does not state): with tails
on, consistency is a PER-FIBER statement (relax evaluates w
numerically, directionb_window.py:350-361). Certified fibers:
w = (1,1) all 4 branches + (2,3), (1/5,7) on (+,+) (this review; the
shipped command covers one). The honest template PINS w_i^4 by the
E5 lead transport (SHEET6-TEMPLATE ~line 230-240, corrected value),
an algebraic point outside E that no run touches; consistency does
not transfer across fibers (span inclusion can fail on special
loci), so "does NOT kill residue-A" is certified for the free-w
window variety V — the E5-pinned fiber remains formally untested at
the linear tier. Contrast the asymmetry: the §3 zero-tail KILL was
scale-free (valid at every w != 0, a fortiori the honest one); the
survival direction is scale-SAMPLED. The 3-fiber robustness above
makes a pinned-fiber kill implausible but not excluded; one more
`relax` run over E extended by the w4-pin relations would close it.

### R1.2 Wrong-object audit of the load-bearing relaxation: CLEAN

The §6.V verdict hangs on test (1) (relax(), directionb_window.py:
638-658). Audited against the review brief's three failure modes:
(i) COLUMN COMPLETENESS — columns are keyed by the state's var-key
tuples: 2718 (Row_20) / 5106 (full window) distinct monomials
reproduced by independent census; all keys canonical sorted tuples,
zero sort-collisions, so nothing is silently merged; nothing is
dropped (every nonempty vk gets a column; only vk = () feeds the
const). Row_20[eta^0] census matches §6.T exactly: 2034 monomials,
degree profile {1:14, 2:184, 3:532, 4:582, 5:386, 6:222, 7:78,
8:36}, linear levels 42/47/52 only. (Direction note: for the
CONSISTENT verdict even a merge/drop would have been conservative —
a true kill functional annihilates every monomial column, hence any
sums/subsets; none was needed.)
(ii) ROW COMPLETENESS — the full-window call runs over sorted(byk) =
bands 6,8,...,18,20, all 77 eta-components (9+10+10+9+10+10+9+10),
the same rows the bands phase certified; odd rows are identically
absent from the state (checked).
(iii) INHOMOGENEITY — the -42 enters once, as +42 at (20, eta^0)
(RHS42, :348, :654-655), i.e. Row_20[eta^0] = -(42/(c_f c_g)) with
the c_f c_g = 1 gauge; matches (J) at §0 and the 2026-08-12 front-1
scratch re-derivation (chart Jacobian -42 t^-11); the E5-corrected
TEMPLATE ~239 erratum touches only the w_i^4 pin value, which this
build does not consume (w free ring radicals — front 5 above), so
the normalization is E5-insulated. Also re-confirmed with tails on:
J-blindness holds (0 monomials carry a dead-stretch var without a
tail factor — the 7 enter only via cross-terms, §6.T line 428-429).
Registry nits, harmless: levels 49/51 exist as vars but occur in NO
row (stratum (3c)'s "50 unknowns" counts 8 vacuous columns; the
cascade STAGES' omission of 49/51 is vacuous for the same reason).

### R1.3 Spot check (review brief item 6): band 8, two paths
(a) The banked echelon for band 8, branch (+,+) (conditions pkl:
rank 4, leftover 0) GENERATES the raw rows: all 10 raw band-8
E-rows reduce to 0 against it (unit-pivot reduction re-run).
(b) Independent-ish jet path: numcheck is frozen-stratum-only (no
tails), so no zero-shared-code check exists for tail rows — noted
as a perimeter gap; instead a FRESH frozen build at D = 9 (fresh
registry + orbit rebuild, 57 s) reproduces bands 6 AND 8 of the
banked D = 21 state coefficient-for-coefficient (name-keyed, all
19 eta-components). Same machinery, different run/depth: checks the
banked pkl, not the orbit model itself (which is guard-certified
upstream, trust note (b)).

### R1.4 Run ledger (this review)
- gate 16/16 (2.3 s); verdict 7/7 (105.4 s); bands ledger (19 s);
  slot20 27 checks / 24 FAIL (3.7 s; see W1 — math content confirms
  §6.T).
- Branch/w sweep driver (sweep.py): 5 further verdict runs, 7/7
  PASS each, all ranks identical (W4d).
- census.py: vars 183 registry / 83 free (76 tf,tg + the 7; 100
  B-vars pinned, occur nowhere); 77 rows; monomial counts, canonical
  keys, eta^0 degree profile, level census (50 / 16 / 20) — all §6.T
  and §6.V dims reproduced independently of relax()'s own counting.
- claim4.py: §6.V claim (4) reconstructed and confirmed in full
  (W2); also demonstrates W3 (eta^0 not an obstruction row at
  low = 0).
- spot8.py: R1.3 (a)+(b).
- State integrity: /tmp/directionb_tails_D21.pkl and
  /tmp/directionb_window_conditions.pkl md5-match the repo banked
  copies; D = 21 asserted on load. (The live depth-23 build
  overwrites only /tmp/directionb_tails.pkl; the analysis engine
  prefers the _D21 bank — verified in code, STATE at
  directionb_window.py:54-56.)
Scripts + logs banked under the session scratchpad
(claude-501/.../scratchpad: sweep_*.log, census.py, claim4.{py,log},
spot8.{py,log}, bands_run.log, slot20_run.log, verdict_run.log).

### R1.5 Bottom line
The pre-registered call is honestly adjudicated: the kill test came
out CONSISTENT at every certified fiber, the sharpness
inconsistencies (2)/(3) and the obstruction structure (4) are real
(now independently reconstructed), and the §3 zero-tail theorem is
untouched. Survival of residue-A on the forced-nonzero-tail locus
STANDS as claimed, with V read as the B = 0 slice at the linear
tier, per W5. Errata W1 and W3 should be fixed before this sheet is
cited further; W2's reconstruction should be adopted as a phase;
none of W1-W5 flips the verdict. The one genuinely open kill-shaped
residue at depth 21 is the E5-pinned w-fiber (W5c) — cheap to close
and worth closing before the depth-23/Groebner tier is spent.

### R1.6 Post-adjudication repair pass (Fable, 2026-08-13, same day)
Coordinator adjudicated this review + the parallel external one
(xmodel/grok-directionb-review.md, F1-F5; F1=W4b, F2=W4a, F4=W4d,
F5=W2, F3 new: gate never certified the RHS42 the analysis
consumes). Combined errata APPLIED in one pass:
- DOC (SHEET6-DIRECTIONB.md §6.T/§6.V): test (2) reworded to
  sampled + rank-stable (2 harness samples x 5 fibers + the review
  extras; uf30 dummy noted, W4b/F1); test (1) scoped to E-linear
  functionals of the 77 depth-21 rows with the not-excluded tiers
  listed (W4a/F2); test (3) parenthetical replaced with the correct
  6-obstruction-row mechanism (W3) and the 7 marked as fixed
  parameters in (3b)/(3c) (W4c); GATE para + REPRODUCTION block
  updated to the new counts with a note crediting both replays for
  the 4-branch identity and claim (4) (W4d/F4, W2/F5).
- ENGINE (cases/directionb_window.py): slot20 checks now assert the
  MEASURED inconsistent result incl. the exact 6-component defect,
  phantom "explicit point" print deleted (W1) — 27/27 PASS, 3 s;
  claim4 shipped as a phase (esolve_res + certified cascade seeds)
  (W2/F5) — 6/6 PASS, 10 s; gate adds the RHS42-vs-chart-Jacobian
  + no-scalar-const certification (F3) — 17/17 PASS; verdict loops
  tests (1)(2) over all 4 h-branches at w=(1,1) + (+,+) at w=(2,3)
  with an explicit cross-fiber dims/ranks/verdicts identity check
  (W4d/F4) — 24 checks, ~8 min.
- NOT applied (out of the adjudicated list, still open as findings):
  W5a (B = 0 tag on V's display), W5b (item-1 joint object), W5c
  (E5-pinned w-fiber), "exhausted as a killing instrument" wording.
Re-run counts after repair: gate 17/17, slot20 27/27, claim4 6/6,
verdict pending-at-banking then confirmed in §6.V's REPRODUCTION
block; no check FAILs anywhere with the honest assertions.
