# Blind whole-portfolio ideation — Fable5 — round `20260827T1808Z`

Author: Fable 5 (Anthropic), exact model ID `claude-fable-5`, equal-standing
core co-researcher.
Written: 2026-08-27 ≈18:40Z.
Packet: `xmodel/ideation-20260827T1808Z-packet.md`, read in full and obeyed.

## 0. Custody, blindness, and execution boundary

All eight basis hashes and all seven pinned evidence hashes were recomputed
before use and match the packet exactly (git basis
`418e413593120d19e15e6546eb50c985f4b1f038`; `COORDINATION.md 6fb539c6…`,
`APPROACHES.md 64fda661…`, `AUDIT.md 11561125…`, `PROGRESS.md 06dafa3e…`,
`notes.md eab83c1f…`, syntheses `a03936b7…`/`24edb9cf…`, websweep
`a8a1ae4f…`; evidence `86742147…`, `6790ec5c…`, `a1b1865a…`, `46736edc…`,
`56a4b940…`, `6e3d9104…`, `94c10fd8…`).

Blindness disclosure (complete):

- I did not open, list, or search-read any `ideation-20260827T1808Z-*` file
  other than the packet and this report; every repository search excluded
  that pattern.
- I opened one section (lines 368–407, Card 2 `RECIP22`) of the prior-round
  report `xmodel/ideation-20260827T1606Z-fable5.md`. This is an earlier
  ideator report, permitted because the sealed 16:06Z synthesis explicitly
  identifies that claim (atom F2, scored 66, "do not launch") and my novelty
  adjudication in §3 needed its exact wording.
- Two matched lines of `xmodel/ideation-20260827T1349Z-actual_total_g20.md`
  appeared inside a grep result (a generic remark that `F^(3/2)`/pole-ODE
  tools are KNOWN). I did not open that file; no claim was consumed from it.
- No AWS was launched or contacted; no live job was touched; no canonical
  ledger was edited; `jc2-lean` was not read, listed, built, or
  status-inspected. All computation was desk-scale exact Python
  (`fractions.Fraction`) in `/tmp/f5id/` (hashes in §10), each run in
  seconds. The only campaign artifact written is this file.

Evidence consumed at promoted scope: R3 (`b1851156…`/`27fcd256…`), R4
(`11cad1db…`/`5187676b…`), R5 (`fd164042…`/`48fff5d5…`), R6
(`ed0e3460…`/`d9e65315…`), R7R1 (`9d35c678…`/`7ab758fa…`), D5G/D5G35
(`59e9bf2c…`, `f0fe0f5d…`/`ba7162fe…`), superelliptic endpoint criterion
(`d382c21f…`/`066095c4…`), q-gates (`46736edc…`, `56a4b940…`), NU17 narrow
core (`72f10ad7…`), V26R1F (`86742147…`/`6790ec5c…`), V24 conditional
grade-seven theorem (`d547baa2…`/`0bd97113…`). Provisional-only inputs are
labeled where used: upper cascade `6e3d9104…`, FACEPIN spec `94c10fd8…`,
V27 design `a1b1865a…` (UNRUN).

---

## F1. Lead finding — a theorem-interface composition already decides the frozen 734-generator gate

**Claim.** The frozen D5G35 exact target gate on the artificial fixture,

```text
D0=…=D21=0,  D22=1,  D23=…=D34=0    (H = X^8−1, F0=H^2, G0=H^3, 400 window slots),
```

is **empty**, and this follows from already-promoted evidence by pure
containment — no new computation is required. The sealed basis labels it
"UNSOLVED" in the D5G35 verdict, the 16:48Z overlay, the 18:08Z LIVE
STATE, and the packet itself; that label is a composition gap of exactly
the kind `COORDINATION.md`'s theorem-interface pass exists to catch.

**Chain (route 1, one step).** Any gate solution assigns polynomials to the
400 window slots, hence gives `F,G ∈ K[X][t] ⊂ K[X][[t]]` with
`F_0=H^2`, `G_0=H^3` and `12F_XG−8FG_X−t(F_XG_t−F_tG_X)=t^22+O(t^23)`
(I verified coefficientwise that this operator's `t^n` coefficient is the
row formula `Σ_{i+j=n}[(12−j)F_i'G_j+(i−8)F_iG_j']`, so the conventions
match, including the sign of the target). The promoted R3 theorem
(AUDIT.md 13:59Z block, Grok review `27fcd256…`) states verbatim: *"There
is no polynomial-X formal jet `F,G in K[X][[t]]`"* with that edge and that
congruence, quantifying over both `F` and `G`. Gate solutions are a subset
of the excluded set. Therefore the gate is inconsistent.

**Independent route 2 (if R3's quantifier were doubted).** Promoted R4
extends the same exclusion to every squarefree `deg H ≥ 2`; `X^8−1` is
squarefree.

**Independent route 3 (different promoted stack).** R7R1
(Fable5-confirmed): an exact target `E=t^22` is attainable over
`L=K(X)(p)`, `p^4=H`, iff every `q_n dX` is exact in `L`; for
window-bounded `F,G` the gate forces `E=t^22` exactly (weights above 35
vanish by window degrees, `D35≡0` promoted). The `n=0` row is exactness of
`q0 dX = p^2 dX = ±w dX`, `w^2=H` — independent of the deformation since
`q0=(F^{1/4})_0=H^{1/2}`. The promoted superelliptic reduction
(`d382c21f…`) computes `[w dX] = −(4/5)[dX/w] ≠ 0` for `H=X^8−1`. So `q0`
is not exact and the gate is empty. (The identification "`q0` row = the
R5/superelliptic endpoint criterion" is itself already recorded — the R7
audit's "trace descent recovers R5 at `q0`" — so route 3 uses only
promoted parts.)

**What survives, precisely.** Nothing about the two R5/R6 survivor shapes
is touched: for `H=A^2` (branch P) and `H=A^2B` (branch Q) the endpoint
criterion *holds*, so the analogous window gates with edge `F0=H^2` on
those `H` are genuinely open. Those are the objects the cascade, q-gate,
and endpoint-test lanes are actually working on. Consequences to
adjudicate in synthesis:

1. Relabel the fixture gate `EMPTY-BY-COMPOSITION (R3; R4; R7R1+q0)` in a
   micro-round; the change is a lifecycle correction, not new mathematics.
2. Every plan whose deliverable is "solve the 734-generator gate" is
   provably futile and should be cancelled before compute.
3. The q1/q2 licensing sentence ("licensed when `D23=0` is imposed") keeps
   its truncation semantics but should be re-anchored to survivor-`H`
   compilations, since the fixture's own exact tier is empty.
4. The packet's proposed branch-P endpoint test (`A=X^4−1`, `F1=H`,
   `D1..D21=0, D22=1`) is untouched and becomes the sharpest open upper
   object — see Card 1, which reduces it to a closed form.

Fail-closed caveat: the only conceivable escape is that R3's AUDIT wording
over-quantifies its producer proof. Routes 2 and 3 are independent of
that; a one-hour different-model recheck of R3's quantifier closes even
the residual doubt.

---

## 1. Disposition vector over avenues 1–46

Default is `unchanged`; every non-unchanged row has a reason. Recent lane
density was not treated as evidence; each dormant route was rechecked
against this round's delta before writing `unchanged`.

| # | Avenue | Disposition | Reason (only for changes) |
|--:|---|---|---|
| 1 | GGV corner farm / `8_28` faces | **raise + redesign** | F1 closes the fixture affine gate (empty by composition); the open objects are the survivor-`H` branch gates, and Card 1 gives them a closed-form decision shape; the lower FACEPIN spec gives the first family-conditional compiler. Keep the total GGV share fixed per the 16:48Z overlay; the raise is within-share priority for the endpoint decision + FACEPIN bridge over any new tower row. |
| 2 | Sheet-ladder / Eggers–Wall backbone | unchanged | |
| 3 | Vertex-gap / strip ODEs | unchanged | |
| 4 | Formal-germ certification + algebraization | unchanged | |
| 5 | Jung–van der Kulk descent | unchanged | |
| 6 | Abhyankar–Moh one-place | unchanged | |
| 7 | Jelonek asymptotic variety | unchanged | |
| 8 | Formal-inverse combinatorics | unchanged | |
| 9 | Lee–Li Conjecture E | unchanged | |
| 10 | HC4 bridge | unchanged (stopped at `NO LEVERAGE`) | |
| 11 | Mathieu/GMC ladder | unchanged (refuted) | |
| 12 | Face isolation / p-adic multinomials | unchanged | |
| 13 | Dixmier DC(2) | unchanged | |
| 14 | End(A_1) audit | unchanged | |
| 15 | Spectral surfaces / commuting PDOs | unchanged | |
| 16 | D-module / holonomic index | unchanged (still no named invariant; honesty over sentiment for my model family's unique find) | |
| 17 | BCW cubic stabilization | unchanged | |
| 18 | Graded/GIT | unchanged (closed) | |
| 19 | Char-p + Witt lifting (incl. max-12 frontier, K00, AS109) | **raise** | V26R1F is the first promoted chart-free survivor scheme (dim 3) at the max-12 order-2 frontier; my §3 kernel-structure finding (constant left covector `ℓ0`, constant right 2-plane, 690-term universal compatibility polynomial) compresses the V27 successor materially; the strongest current falsification route runs through this lane. |
| 20 | p-curvature formalism | unchanged | |
| 21 | p-adic injectivity / Hensel | unchanged | |
| 22 | Siegel integral points | unchanged | |
| 23 | Analytic global inverse | unchanged | |
| 24 | Real JC / Pinchuk | unchanged | |
| 25 | Monodromy passports | unchanged | |
| 26 | Primitive-monodromy td bound | unchanged (still the consensus cheap untried pick; nothing this round changes its rank) | |
| 27 | Links at infinity / splice | unchanged | |
| 28 | Log-BMY | unchanged | |
| 29 | LND / Hamiltonian completeness | unchanged | |
| 30 | ML invariant / classification | unchanged | |
| 31 | Integrality / ZMT / Rees | unchanged | |
| 32 | Collision ideal / injectivity | unchanged | |
| 33 | Global symplectic exactness / action residues | **reopen (as an absorbed instrument, near-zero separate cost)** | The ledger's own revival condition — "a genuinely twisted/client-specific class" — is now met: the promoted `q_n dX` classes on `p^4=H` (codim 3 on P, 4 on Q) are precisely nontrivial twisted residue/de-Rham classes of the kind row 33's untwisted gate lacked (`COSTUME`). Reopen 33 not as a route but as the correct home for tower-class bookkeeping (residue-at-infinity + `H^1_dR` functionals), feeding avenue 1. No separate budget. |
| 34 | 2D tangent-sweep / pole removal | unchanged | |
| 35 | Dim-3 descent | unchanged | |
| 36 | Guided CE search | unchanged (stays subsumed under K00/AS109 discipline) | |
| 37 | Finite-field census | unchanged | |
| 38 | Tropical | unchanged (the two-grading face work is O2 `FACE-EXP`'s thread, already tracked in avenue 1) | |
| 39 | Cohomological cluster | unchanged | |
| 40 | Free-associative lift | unchanged | |
| 41 | Naive scaling deformation | unchanged (refuted) | |
| 42 | Markus–Yamabe | unchanged | |
| 43 | Ritt decomposition | unchanged | |
| 44 | Moskowicz | unchanged (closed as proof input) | |
| 45 | Differential Galois / Liouvillian | unchanged (its mechanism — first-order rational exactness — is now the working toolbox inside avenue 1; no standalone program, per the 16:06Z hold) | |
| 46 | Lean / AI formal certification | unchanged (`jc2-lean` separate and untouched) | |

## 2. Reranked bottlenecks and falsification attacks

**Three highest-value proof bottlenecks (each with a live decisive test):**

1. **The survivor-branch affine endpoint** `D1..D21=0, D22=1` on branch-P/Q
   edges (`H=A^2`, `H=A^2B`). After F1, this is the only open exact-tier
   question on the upper face, and §9/Card 1 reduce it to one interpolation
   condition on a single forced coefficient. Decides whether the upper
   fixture face has *any* formal survivor through the endpoint, and whether
   `q1` is genuinely new information at row 23.
2. **The FACEPIN typed bridge + `LF40` family compiler** (lower face). The
   only current lane pointed at a *genuine* GGV-family object; its missing
   piece is the desk-scale typed coefficient map (flip/unflip, `ρ≠0`, 37
   slot equalities) plus the two repairs the live Opus5 review already
   flagged (the `(1,0)`/`(0,1)` typo, the P/Q relabelling, the 740-census).
   Conditional on the GGV reduction, an `I_LF40` unit certificate would be
   the first family-level exclusion instrument the campaign has ever had.
3. **K00 grade-7 rank filtration with kernel compression** (V27 `BASE4` /
   `MAX5CLASS` / `LOW-KILL`, accelerated by §3's `ℓ0`-compatibility and
   gauge reduction). Gate to order-2 max-12 reachability and to the only
   live arc-candidate pipeline.

Global landing / `G2-PSC` / `G2-BD` remains the strategic wall above all
three, but this round supplies it no new decisive instrument; its share
should be held, not raised, until the FACEPIN bridge (its only current
feeder) is typed.

**Two strongest falsification/counterexample attacks:**

1. **K00 survivor prolongation.** Drive the promoted dim-3 rank-`≤4`
   scheme to an exact rational point, lift through full `P6`, prolong to
   grade 8, then couple loads `μ2,μ4,μ6,Jdet` through order 19
   (closure-first incidence). Decisive object: a compatible coupled jet at
   an exact rational point — the first honest arc candidate at max-12
   order 2; every failure mode closes a rung exactly.
2. **AS109 residual `n=6`.** The surviving α/β content strata under the
   promoted floor (`deg_y` correction ≥ 12, `6|deg_x(q_6)`, the Cartier
   exclusions). Decisive object: an explicit integral lift candidate
   satisfying every recorded divisibility, or the exact death of the last
   content stratum.

## 3. New findings, with history adjudication

Each was preceded by a targeted repository search excluding
`ideation-20260827T1808Z-*`; labels use the packet's vocabulary.

### 3a. K00 constant-kernel/gauge-pencil structure — label: **NEW**

Desk-verified facts about the frozen V26 `7×7` grade-seven matrix `A`
(byte source `ATLAS_EXACT_POLYNOMIALS.json` inside the reviewed
`f1a6f1fc…` compiler output), all exact:

1. **A constant universal left covector.**
   `ℓ0 = (5/1024, 0, 3/128, 0, 1/8, 0, 1)` satisfies `ℓ0·A = 0` as an
   exact polynomial identity in all 49 entries (verified symbolically from
   `exact_terms`, no evaluation). Hence `ℓ0·b = 0` is a **universal
   necessary compatibility condition** for `A·y=b` at every point of the
   base, at every rank, with no localization at `W` and no minor choice.
   `ℓ0·b` is a nonzero polynomial with **690 terms** over all 33 variables
   — against the frozen `Comp6_Comp7` entries of 110,117 and 83,298 terms.
2. **A constant right-kernel 2-plane.** `A·v1 = A·v2 = 0` exactly, with
   `v1=(2,0,1,0,1,0,0)`, `v2=(0,1/16,0,1/2,0,1,0)` (symbolically
   verified). Equivalently the seven columns satisfy two exact constant
   relations `2C0+C2+C4=0` and `(1/16)C1+(1/2)C3+C5=0`: the grade-seven
   system has exactly five effective newest-variable directions and a
   globally trivial rank-2 gauge. This *explains* `I6(A)=0` (universal
   corank ≥ 2) rather than merely recording it.
3. **The second covector has one moving entry.** At every sampled point
   the left kernel is `span(ℓ0, w)` with
   `w = (1, 0, 16/3, 0, 128/3, w5(x), 0)` — constants except the single
   rational entry `w5`. All rank-5 compatibility is therefore `ℓ0·b=0`
   plus one condition whose only varying coefficient is `w5`.
4. **The two-scalar-class census is structural.** For corank 2 the `5×5`
   minor matrix (second adjugate) has rank 1: `minor_{IJ} = u_I·v_J` with
   `v` the constant right Plücker vector and `u = ℓ0 ∧ w`. Since
   `w = (const vector) + w5·e5` and the two wedge summands have disjoint
   support, every nonzero minor lies in exactly two proportionality
   classes, and the class ratio is a fixed constant times `1/w5`: at three
   random points, `minor(drop rows {0,2})/minor(drop rows {5,6})·w5 =
   1/384` exactly. This derives V26R1F's observed `90/54/2` census and
   identifies `w5` as (a constant times) the ratio of the two promoted
   minor-class representatives.

Consequences for V27 (all correctness-preserving): adjoin `ℓ0·b` to
`BASE4`, `LOW-KILL`, and the single rank-five chart as a 690-term cut
valid at all ranks (first check whether it reduces to zero mod `P6` — if
yes it is a compression, if no it is a genuinely new cut; either outcome
is useful and cheap); replace the `y`-space by the 5-dimensional gauge
quotient using `v1,v2`; and obtain the second compatibility covector from
the two promoted minor classes by division rather than kernel
computation.

Closest hits (all searched): V24 conditional theorem
(`d547baa2…`/`0bd97113…`) — rank 5 and a free rank-two **left** kernel,
but only over the prior ring **localized at `W`**, with no constancy, no
right-kernel statement, and 10^5-term compatibility representatives;
V26R1F census (records `90/54/2` as computational fact, no mechanism);
V27 design `a1b1865a…` (MAX5CLASS plans to *compare* the two classes, not
to derive them); K00 syzygy origin-image result (`65fb96a9…`) — the
even-slot parity pattern is consistent but is a statement about a
different object (constant terms of local multipliers). No prior
statement of a constant covector, constant column relations, or the
pencil mechanism was found. **NEW.**

### 3b. The forced-continuation endpoint transfer — label: **NEW as composition/decision instrument; core extraction KNOWN at rational tier**

Statement (window-bounded setting, both survivor branches; derivation and
checks in §9): on the exact solution scheme of the vanishing prefix
`D1=…=D21=0` in the frozen D3 windows,

```text
D22 = −L_22(g22),      g22 := (F^{3/2} + Σ_schedule c_n Ψ_n)_22 ∈ K(X),
L_22(R) = 2H[−10H'R − 4HR'],
```

i.e. the endpoint value is minus the weight-22 obstruction operator
applied to the *forced* weight-22 coefficient of the unique rational
continuation of `G`. Three corollaries:

- **(Exclusion.)** `L_22(K[X]) ⊆ (H)`, so on every prefix stratum where
  `g22` is polynomial, `D22 ∈ (H)` and `D22=1` is impossible. This proves
  the conjectured half of Grok's "failed attempt #9" and of the 16:06Z
  Fable5 `RECIP22` card exactly on the polynomial-`g22` strata — and
  simultaneously shows the *universal* `mixed_22 ∈ (H)` reading those two
  sources hoped for is the wrong target: `D22=1` is reachable only
  through non-polynomial `g22`.
- **(Rigidity.)** `D22=1 ⟺ L_22(g22) = −1 ⟺ g22 = −Y/(2H) + κ` with
  `M(Y)=4HY'+6H'Y=1` and `κ ∈ ker L_22 ∩ K(X)` (`= K·A^{−5}` on branch P,
  `= 0` on branch Q). R4's endpoint operator and the promoted
  superelliptic criterion appear *exactly*, now with `g22` forced by `F`
  instead of free — the difference between the reviewed rational endpoint
  theory (free `d`) and the open gate.
- **(Face uniformity.)** The same identity on the lower `(4,−1)` face
  gives `Dtil_17 = −L̃_17(g̃17)`, and with `g̃17 = g/K^2` it reduces to
  `4Kg'−3K'g = −K/(2a)` — the promoted NU17 unmixed ODE up to rescaling
  (desk-verified). So the promoted upper `M(Y)=1` reduction and the
  promoted lower ODE are the two `F`-frozen instances of one transfer
  principle, which also covers full `F`-deformation.

Closest hits (all searched): R5 hostile review `48fff5d5…` §3/§5 — the
subtraction `Δ=G−F^{3/2}−Σc_nΨ_n`, the completeness induction, and the
weight-22 extraction `−20HH'd−8H^2d'` with "no `F_j` contamination", all
**at the rational tier with `d` free** (this is the KNOWN core); upper
cascade `6e3d9104…` (2.2) — polynomial-tier forced continuation proved
through `D6` only, endpoint not composed; Grok raw-support audit
`5735ee90…` attempt #9 — the exclusion conjectured, not proved; 16:06Z
Fable5 Card 2 `RECIP22` (66, do-not-launch) — sought the exclusion via a
reciprocity pairing that this identity shows is unnecessary; R7R1 — the
same content over `L` in tower form. The window-forced composition, the
exclusion/rigidity split, and the uniform two-face application were found
nowhere. **NEW (composition), with the extraction mechanism KNOWN.**

### 3c. New connection between existing avenues — label: **NEW**

Avenue 33 ↔ avenue 1: the promoted `q_n`-gate functionals (one twisted
residue at infinity plus `H^1_dR` classes on `w^2=A`, resp. the four
branch-Q functionals) are literally the "genuinely twisted,
client-specific classes" that avenue 33's `COSTUME` verdict demanded
before any revival. This re-points a dormant avenue at zero cost and
gives the tower bookkeeping its correct classical home (residue pairings,
reciprocity, second-kind differentials). Secondary connection: §3b makes
avenue 45's mechanism (first-order rational exactness/Kovacic) the shared
engine of the upper endpoint, the lower ODE, and the q-tower — an
instrument-level unification, not a new route.

## 4. Connect or keep separate: the five named obligations

**One principle, three instances (connect).** The upper de Rham gates and
the affine `D22=1` endpoint are one object: the endpoint is the `n=0` rung
of R7R1's tower (`q0` exactness ⟺ the promoted superelliptic criterion —
already recorded in the R7 audit), and the higher `q_n` are its licensed
continuations. The §3b transfer identity binds both to the vanishing
prefix: rows 1–21 say "`G` is the forced continuation", the endpoint says
"the forced coefficient must break polynomiality in the exact shape
`−Y/(2H)+κ`, `M(Y)=1`". The lower FACEPIN target `Dtil_17=−1` is the same
principle on the second face with `K=ξ(ξ−ρ)^7` in place of `H` (§3b third
corollary; the promoted `γ≡3 mod 4` necessity and the degree-six ODE
solution are its `F`-frozen shadow). So: **connect upper gates, endpoint,
and lower target as one endpoint-transfer mechanism.**

**Data firewalls (keep separate).** The upper face's `H` data are the
artificial fixture and the two survivor shapes — never family-pinned; the
lower face's `K_ρ` *is* family-pinned, but only conditionally on the GGV22
coefficient theorem and only for the raw pre-final pair. Transporting
`H=X^8−1` into the family remains an error (native control's upper face is
`X^16−1`). So the two faces share the mechanism and must not share data.

**K00 (keep separate, one methodological bridge).** No licensed map
connects K00 to either GGV face; the only honest link is methodological:
§3a's constant right-kernel gauge quotient is the K00 analogue of "`F_n`
is pure gauge inside its own row" (both are exact gauge reductions before
solving), and both lanes are successive-constructible filtrations with
per-stage forced continuation. Keep objects separate; share the
compression pattern.

**Global landing/receiver (connect only through the lower face).** The
upper fixture can never feed `G2-PSC` (artificial scope). The lower
`I_LF40`, if compiled and emptied, excludes the raw pre-final `8_28`
family conditional on the GGV reduction — that is the sole present
conduit from face work to the global obligations, and it still does not
touch coverage/cofinality. Receivers (K00, terminal) connect to landing
only through the max-12 order-2 lane, unchanged this round.

## 5. Strongest attacks I would launch now

**Proof attack — decide the survivor-branch endpoint (decisive object
named).** The object is the finite defect-interpolation system of Card 1:
for branch Q on the R5 pair (`B=X^2−1`, `A=X^3−(2/5)X`) and branch P on
`A=X^4−1` with the packet's fixed `F1=H`: parameters
`(V,Z,T,F4..F14 windows, schedule constants)`, constraints "forced
continuation polynomial and in-window at weights 7..21", target
"`g22 = −Y/(2H)+κ` with `M(Y)=1`". A solution is an exact rational point
of `D0..D21=0, D22=1` (the first formal survivor through the endpoint,
making `q1` genuinely new at row 23); infeasibility — combined with F1
and R4/R5 for the non-survivor shapes — closes the entire upper-face
affine target at degree eight. Either outcome is a face-level decision,
which the campaign has never had on the upper side.

**Counterexample attack — K00 rational point + coupled prolongation
(decisive object named).** The object is an exact rational point of
`V(B+I5(A))` (dimension 3, six variables — search accelerated by the §3a
pencil: on the rank-`≤4` locus both minor classes vanish, so the locus is
cut by the two class representatives plus `B`, a 9-generator system a
rational-point search can attack directly), lifted through the 35-generator
`P6` with the `ℓ0·b` cut, prolonged to grade 8, then coupled to
`μ2,μ4,μ6,Jdet` through order 19. The decisive object is the coupled
compatible jet; its existence at every tested depth is the strongest
available counterexample signal at the frontier, and each exact death
closes a rung with a certificate.

## 6. One correctness-preserving software/AWS acceleration

**`PS21` — survivor-branch prefix compiler + endpoint interpolation, with
per-row certificates.** (This is the compute half of Card 1.)

- **Exact inputs.** D3 windows from `RAW_INPUT.json` (`28b9b05c…`); the
  promoted row formula (D5G35 `f0fe0f5d…`, freeze `1668795f…`); branch
  data `A=X^4−1` (P) and the R5 pair (Q); the cascade case
  `cases/ggv_8_28_upper_cascade_w3_w6_20260827/` (PROVISIONAL, rollback
  branch: if its live review's repairs change the w≤6 parametrization,
  recompute rows 1–6 from scratch — the compiler re-derives every row
  anyway, so the dependency is soft).
- **Decomposition.** Weight-triangular: at each weight `n=7..21`, the row
  is `L_n(R_n) = −mixed_n(earlier)` — one exact linear solve in the `G_n`
  window plus a divisibility condition on earlier parameters (the
  `A^k | (explicit polynomial)` pattern of rows 2–6). Parallelize over
  (branch × gcd-stratum × weight-frontier); strata are independent
  after their defining substitutions.
- **Certificate/replay format.** Per row and stratum: the particular
  solution, kernel constants, and the divisibility *quotient* polynomials
  (so replay is multiplication-only); at the end: the forced `g22`, the
  particular `Y` with `M(Y)=1` (exists on survivor branches by the
  promoted criterion), and the final linear system over the residual
  parameters with an exact solution vector or an exact infeasibility
  covector. Every certificate is an identity in `Q[X]`; replay never
  re-solves.
- **Resource estimate.** Degrees ≤ 40 in `X`, ≤ 120 parameters handled
  triangularly with stratum substitution; the analogous rows 1–6 ran in
  seconds on a laptop. Budget: one 64-vCPU box, ≤ 4 h wall, ≤ 32 GiB;
  hard cap 6 h per COORDINATION speculative rules.
- **Evidence firewall.** Producer-tier output only; `PROVISIONAL` tags on
  the cascade input; no promotion without different-model review; the two
  fixed fixtures run before any generic-`A` sweep; a mutation set (drop a
  row, flip the target to `D22=0`, un-saturate a leading coefficient) must
  fire.
- **Stop rule.** Stop at the first weight where a stratum's condition is
  not principal-divisibility-plus-linear (structure break ⟹ redesign);
  or on endpoint decision; or at the wall cap. A `D22=0`-only outcome on
  all strata is itself decisive (endpoint empty on that branch).

Second, free acceleration (no new run): adjoin the §3a `ℓ0·b` 690-term
cut and the `v1,v2` gauge quotient to every registered V27 job; both are
exact identities verified from frozen bytes, and they only ever shrink
systems.

## 7. Idea cards (three)

### Card 1 — Decide the survivor-branch affine endpoint by defect interpolation

- **Target gap:** the only open exact-tier upper-face question after F1:
  is `D0..D21=0, D22=1` solvable in the frozen windows on branch P/Q?
  Includes the packet's named branch-P `F1=H` test as a sub-case.
- **Mechanism/hypotheses:** §3b transfer identity (desk-verified);
  R5-review completeness at rational tier (reviewed); promoted endpoint
  criterion for the particular `Y`; per-row window solves re-prove
  polynomial-tier completeness as they go (no reliance on the provisional
  cascade beyond row-1..6 cross-checks).
- **Cheapest discriminator (desk, hours):** on branch Q the kernel `κ=0`,
  so `g22` must equal `−Y/(2H)` up to the *finitely many* `M(Y)=1`
  solutions; compute the denominator profile of `(F^{3/2}+modes)_22` on
  the row-3 deviation stratum (`A∤T`) and check whether an `H`-denominator
  of the required exact shape is reachable at all. If the reachable defect
  lattice misses `−Y/(2H)+κ` already at the leading pole orders, the
  endpoint dies on that stratum with a two-page proof.
- **PASS (point found):** first formal survivor through the endpoint;
  `q1` (codim 3/4) becomes genuinely new information at row 23; the
  q-tower instruments get their first live client; continue to `D23..D34`
  with the same machinery.
- **FAIL (infeasible):** with F1 + R4/R5, the complete degree-eight
  upper-face affine target is empty — the first face-level decision of
  the campaign's flagship control; redirects all upper-face budget to the
  lower/family side.
- **Stop condition:** PS21's stop rules; or the cheapest-discriminator
  kill.
- **Rollback subtree:** children tag the cascade `PROVISIONAL`; F1's
  relabel is independent; nothing else consumes this card's outputs until
  review.
- **Expected information gain:** decisive either way at face level; also
  retires or confirms the last conjectural piece of `RECIP22`/attempt-#9.

### Card 2 — K00 kernel-structure certificate and compressed V27

- **Target gap:** V27's `BASE4`/`MAX5CLASS`/`LOW-KILL` are designed but
  unrun; compatibility representations are 10^5-term objects; the
  two-class collapse is unexplained.
- **Mechanism:** §3a. Deliverables: (i) frozen exact certificates
  `ℓ0·A=0`, `A·v1=A·v2=0` (already verified here; freeze bytes + replay);
  (ii) `ℓ0·b` and its normal form mod `P6` (decides "new cut vs
  compression"); (iii) the `w5`-pencil derivation of the two minor
  classes with the `1/384` normalization pinned; (iv) V27 jobs rerun on
  the 5-dimensional gauge quotient with the `ℓ0`-cut adjoined.
- **Dependencies:** V26R1F (promoted); V24R6R1 (promoted); V27 design
  (UNRUN — this card *amends* it, additively).
- **Cheapest discriminator (desk, minutes):** the `P6`-normal form of
  `ℓ0·b`; and whether `w5` clears to a polynomial ratio of the two class
  representatives everywhere on `V(B)` (three-point check done; do the
  symbolic division once).
- **PASS:** `LOW-KILL` and the rank-five chart shrink by the compression;
  a nonzero `ℓ0·b` mod `P6` is a brand-new grade-7 cut obtained for free.
- **FAIL modes and meaning:** `ℓ0·b ≡ 0 mod P6` — pure compression, still
  worth adjoining; the pencil failing off the sampled locus —
  would mean the left-kernel module is not free on some substratum, itself
  a sharp structural fact the rank filtration must know.
- **Stop condition:** all four deliverables are bounded desk/1-hour-AWS
  items; stop after (iv) launches or at the first structural surprise.
- **Rollback subtree:** none beyond V27's own rollback tags (additive).
- **Expected information gain:** high per cost; converts the promoted
  minor census into mechanism, and every V27 consumer gets smaller exact
  systems.

### Card 3 — FACEPIN desk bridge, then `LF40` by forced continuation

- **Target gap:** the family-conditional lower exclusion instrument: the
  442-slot compiler through `Dtil_40` exists only as a spec; the typed
  coefficient map is the missing desk piece; the live Opus5 review lists
  required repairs (TeX `(1,0)`/`(0,1)` typo custody, P/Q relabel ledger,
  740-generator census).
- **Mechanism:** implement the spec's §6 smallest experiment verbatim
  (family record from `get_*` functions; flip serialization; 37
  coefficient equalities; `γ=6`, `ρ=0`, and both non-Keller-control
  mutations), then compile `LF40` with the §3b transfer as its solver
  architecture: rows `1..16` as forced continuation in
  `(a,b,ρ)`-parametrized windows, the row-17 target as
  `g̃17 ∈ (particular of 4Kg'−3K'g=−K/(2a)) + ker`, rows 18..40 as
  continuation constraints. Same certificate format as PS21.
- **Dependencies:** FACEPIN spec `94c10fd8…` (PROVISIONAL, under Opus5
  review — consume only after its verdict; the desk bridge itself is
  reversible and review-independent); NU17 narrow promoted core; GGV22
  primary-source pins.
- **Cheapest discriminator (desk):** the 37-coefficient equality check
  plus the two negative-control replays (`Dtil_4`/`Dtil_8` onsets) — an
  afternoon; it converts the external semantic sentence into a typed map
  or fails closed at a named coefficient.
- **PASS meaning:** `LF40` compiles; a later `I_LF40` unit certificate
  excludes the raw pre-final `8_28` family conditional on the GGV
  reduction — the first genuine family exclusion route.
- **FAIL meaning:** a named coefficient mismatch in the bridge —
  quarantines the family pin before any heavy algebra is spent on it.
- **Stop condition:** desk bridge one session; `LF40` compile under PS21
  stop rules; Gröbner/saturation of `I_LF40` is AWS-only and separately
  registered.
- **Rollback subtree:** everything tags the FACEPIN spec and, where used,
  the GGV reduction as conditional; no `G2-PSC` claim anywhere.
- **Expected information gain:** the highest family-level leverage in the
  portfolio; even the bridge alone retires a semantic gap flagged by two
  reviews.

## 8. Lane decisions

| Lane | Decision | Rule |
|---|---|---|
| K00 (grade-7 atlas, V27) | **continue, amended** | Run V27 with Card 2's compression; exact-Q binaries first; superloci stay one-sided until `BASE4`. |
| GGV upper (fixture/tower/cascade) | **continue, redesigned** | F1: fixture gate relabel `EMPTY-BY-COMPOSITION`; all "solve the gate" plans cancelled; budget moves to Card 1 on survivor branches; no new tower rows before the endpoint decision. |
| GGV lower (FACEPIN/LF40) | **continue** | Card 3 order: desk bridge → review → compile; controls before algebra. |
| Coverage/landing (`G2-PSC`/`G2-BD`/cofinal) | **continue at top proof priority** | Unchanged; face endpoints are inputs, never the transport theorem; only the lower lane feeds it. |
| TD6 / Artin–Schreier + specialization | **continue at registered caps** | No new blind windows; AS109 only on surviving content strata. |
| Formal-germ algebraization | **continue narrowly** | K00-fed only; jets are not arcs; the coupled reachability test is the sole closure discriminator. |
| Sparse/guided counterexample search | **stop (remain stopped)** | Clients are K00 + AS109; no ambient random search or census. |
| External-claim audit (Matysiak) | **continue bounded** | Lawful acquisition; dependency-first audit; no reranking without primary text. |
| C5/total-certificate custody | **bank / narrow (unchanged)** | No new exponent ladders; typed transports only. |
| V47/V48 strict compiler | **stay stopped as research** | Banked infrastructure only. |

## 9. The insight a comparably strong, differently trained researcher likely misses

**The affine endpoint is not a bilinear evaluation to be attacked with
reciprocity identities or Gröbner bases; on the prefix scheme it is a
first-order ODE condition on one forced coefficient.** Everyone who
touched `D22` so far — the q-gate review ("`D22=mixed_22`, a single
bilinear evaluation"), Grok's attempt #9 (conjectured `mixed_22∈(H)`,
couldn't prove it), the 16:06Z `RECIP22` card (sought a residue-pairing
identity), and D5G35 (compiled 734 generators) — treated the endpoint as
an opaque pairing of lower slots. The transfer identity dissolves it.

Derivation (complete, checkable): let `(F,G)` solve `D1=…=D21=0` in the
frozen windows. By the R5-review completeness induction (rational tier,
reviewed; my per-row solves re-prove it in the window setting), `G` agrees
through weight 21 with the forced continuation
`G_cont = F^{3/2} + Σ_schedule c_nΨ_n`, `Ψ_n = t^nR_q(F/H^2)^{(12−n)/8}`.
Since the `G_22` window is empty, `Δ := G − G_cont` starts at weight 22
with `Δ_22 = −g22`, `g22 := (G_cont)_22`. `E` is linear in its second
slot and `E(F,G_cont)=0` exactly, so `E(F,G) = E(F,Δ)`; the weight-22
coefficient of `E(F,Δ)` has only the `(i,j)=(0,22)` term, giving
`D22 = (12−22)F_0'Δ_22 + (0−8)F_0Δ_22' = L_22(Δ_22) = −L_22(g22)` with
`L_22(R)=2H[−10H'R−4HR']`. Exact desk verification: branch P,
`A=X^4−1`, `F=H^2+F_1t+F_2t^2` generic, `G=trunc_{≤21}(F^{3/2})` — the
identity holds exactly and `D5=D13=D21=0` (script `check1b.py`; a
one-slot hand proof via the `C(3/2,n)` ratio `(3/2−21)/22=−39/44`
matches both sides' coefficients). Immediate corollaries: (i)
`L_22(K[X]) ⊆ (H)` (explicit factor `2H`), so `D22=1` forces `g22`
non-polynomial — the exclusion half of attempt #9 proved, the universal
half refuted; (ii) `L_22(N/H) = −2M(N)` with `M(Y)=4HY'+6H'Y`
(`check4.py`), so `D22=1 ⟺ g22 = −Y/(2H)+κ`, `M(Y)=1`, `κ ∈ ker L_22 ∩
K(X)` — R4's operator and the promoted superelliptic criterion appear
with `g22` *forced*, which is precisely what distinguishes the open gate
from the solved rational endpoint theory; (iii) the same computation on
the lower face reproduces the promoted `4Kg'−3K'g` ODE exactly
(`check2.py`), so one principle covers both faces and both `F`-frozen
promoted reductions.

Why differently trained researchers miss it: an elimination-first
researcher sees 734 generators and reaches for Gröbner; a
residue-calculus researcher (the `RECIP22` instinct — my own model
family's prior round) reaches for pairing identities; both attack
`mixed_22` as a sum. The identity instead *names the sum*: it is
`−L_22` of a single coefficient of `F^{3/2}` — because the prefix has
already spent every degree of freedom in `G`.

And the same discipline of "compose promoted interfaces before computing"
yields F1: the fixture gate everyone carries as "unsolved" is a literal
sub-case of promoted R3.

## 10. Honest ledger

**Conjectural leaps (labeled, not consumed as evidence):**
- Window-tier completeness of the forced continuation at weights 7..21 is
  re-proved row-by-row by PS21 as it runs, but has only been executed
  through weight 6 (cascade, provisional, under live review with two known
  repairs); my §3b statement is conditioned accordingly.
- The §3a pencil facts (3) and (4) are symbolic for `ℓ0,v1,v2` but
  pointwise (3–4 random points) for the `w5`-pencil and the `1/384`
  ratio; Card 2 freezes the symbolic division.
- Card 1's "FAIL closes the degree-eight upper affine target" additionally
  uses R4/R5 to dispose of non-survivor `H`-shapes; that composition is
  parallel to F1 and should be checked by the same reviewer.
- F1's route 1 rests on R3's quantifier as written in AUDIT; routes 2–3
  are independent, and I recommend the one-hour recheck anyway.

**Failed attempts this session:** the first endpoint-identity verifier
(`check1.py`) used unreduced rational-function arithmetic and timed out at
2 minutes; rewritten with an `N/H^k` normal form (`check1b.py`) it runs in
seconds — recorded because the wrong representation, not the identity, was
the failure. My first guess for the K00 class-ratio orientation
(`ratio ∝ w5`) was wrong; the data forced `ratio·w5 = const` (reciprocal
orientation), recorded in §3a as verified.

**Assumptions:** frozen bytes as hashed above; promoted rows consumed only
at their stated scopes; the D3 windows (including lower degree bounds)
as re-stated in the Grok46 review; no assumption anywhere that a fixture
is a family, a jet is an arc, or a proper superlocus is a witness.

**Checks actually performed:**
1. All 15 packet hashes recomputed and matched (§0).
2. Row-formula ⇔ R3-operator coefficient identity (hand).
3. `D22 = −L_22(g22)` exact on a generic two-slot branch-P fixture, with
   `D5=D13=D21=0` (script + independent one-slot hand proof).
4. `L_22(K[X]) ⊆ (H)` (script).
5. `L_22(N/H) = −2M(N)` (hand + script), and the `g=4HY` bridge
   `2Hg'+H'g=2H ⟺ M(Y)=1` (hand).
6. Lower-face `L̃_17(g/K^2) = −2a(4Kg'−3K'g)/K` (hand + script) and
   solvability of the promoted ODE with `deg g ≤ 6` at `γ=7` (script).
7. K00: `ℓ0·A=0` and `A·v1=A·v2=0` as exact polynomial identities from
   frozen `exact_terms`; ranks/kernels at 4+6 random points; right-plane
   constancy; left-plane non-constancy with single moving entry `w5`;
   21×21 five-minor matrix rank 1 at a point; `ratio·w5=1/384` at three
   points; `ℓ0·b ≠ 0` with 690 terms (scripts).
8. Targeted history searches (pattern-excluding this round) for:
   forced continuation / endpoint transfer, `F^{3/2}` priors, `L_22` /
   `mixed_22` priors, `RECIP22`, attempt #9, Plücker/compound/adjugate,
   left-kernel priors, constant-kernel priors, `q0`-criterion
   identification, `2Hg'+H'g=2H` occurrences.

Desk-script custody (all in `/tmp/f5id/`, pure Python 3, exact rational
arithmetic, no CAS, each ≤ seconds except the superseded first verifier):

```text
787203d7aab98eaa3acdbb223ff09a3bc9250c5dd211a32253acc2462dd7e397  check1.py   (superseded; timeout, representation failure)
4d40bf7f35cc7f417829a6c8ee0fb6b6c6dc58b880a763b803ab2a401db1ffaa  check1b.py  (endpoint-transfer identity; exclusion lemma)
90e66ddb082c7bbfecff0a8be220243b7dd84ae18956c9a80b2689d25d1e3dfa  check2.py   (lower-face reduction; promoted ODE solvability)
bf03420421787b01559a0400ac2b584c89a3bd74fb53f7731bc4ccd48b09b7e4  check3.py   (K00 ranks/kernels/minor-matrix rank 1)
9dbd10b50bdd819eb6cf42a4ea027cd1f328c91eda584237e7305ec2dafb45a2  check3b.py  (ℓ0 and right-kernel symbolic identities)
deae4b92cf47ff2fa508e241d64779dc7a5bf1d8c96e8fc7cee002197894cc95  check3c.py  (ℓ0·b census)
d8ca42ed96c725e2f77f99199b5253f41942fd2766f5330972a21a050923ffde  check4.py   (L_22/M bridge; class-ratio·w5 constancy)
```

Scope firewall: nothing in this report proves or disproves JC2, any GGV
family exclusion, `G2-PSC`, `G2-BD`, a cofinal bound, K00 closure, order
two, or maximum twelve. F1 empties one artificial-fixture algebraic gate
by composition of promoted theorems; the §3 findings are instruments; all
cards are producer-tier proposals subject to the standard different-model
review gates.
