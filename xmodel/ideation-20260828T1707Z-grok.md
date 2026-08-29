# Whole-portfolio ideation — Grok — `20260828T1707Z`

Freeze: 2026-08-28 17:07Z  
Lane: Grok (xAI Grok 4.6), equal-standing blind whole-portfolio researcher  
Status: **SEALED.** No peer `20260828T1707Z` response was read.

This is strategy, not a proof or counterexample of JC2. Model verdicts are
not mathematical evidence.

---

## 0. Custody, blindness, execution

Packet SHA-256 verified:
`1e40e7106e2a3c16b6a6fe92e6d2387228fb1260ae5633e686b456e9f9d95f1c`.

HEAD `418e413593120d19e15e6546eb50c985f4b1f038`. All 17 custody hashes in
packet §0 matched before those files were read. Worktree cleanliness was
not inferred. `jc2-lean` was not entered, listed, searched, read, built,
modified, status-checked, or controlled. No AWS job was touched. No
Singular, msolve, Sage, Lean, or heavy local algebra was run. Canonical
files were not edited.

Assigned prompt `xmodel/ideation-20260828T1707Z-grok-prompt.md` was read.
No other `xmodel/ideation-20260828T1707Z-*` file was read except the packet
and this output.

Allowed exact checks: SHA-256 verification; a standard-library
`fractions.Fraction` arithmetic script on the residue-A MFE budget and
identities (R1)--(R3). No engine census, no `twopole_check.py` run, no
AWS.

---

## 1. Direct answers to the seven charged questions

### 1.1 Compose MFE literally with residue A — `NO HIT`

Residue A, recorded as a Q-level necessary-condition exhibit, not a
Puiseux forest or polynomial Keller map:

```text
P1 = P2 :  Q = (2, 2, 2, 2, 5)           lambda_exit = 0
merge   :  Q = (6, 12, 3, 2, 5)          reduced (dp,dq)=(6,10), lambda_exit = 0
suffix  :  Q = (42, 126, 7, 3, 5)        recorded selected-exit cost 2
terminal:  psi = 2
```

**Actual selected-exit set, by the promoted definition, not by the
withdrawn equality ledger.** `U^full` is the set-theoretic union of the
two pole segments. Selected exits at each vertex exclude pole arrivals and
the unique rootward continuation; witnesses are Statement-7.3 cv flags
off `U^full`.

| vertex | orbit anatomy | selected-exit status |
|---|---|---|
| `P1`, `P2` | one simple `ν=2` orbit; the pole ray ends here | the only positive continuation is rootward to the merge; **empty** selected-exit set |
| merge `G_m` | two simple incoming pole orbits plus one extra q-only `ν=3` orbit, `k=0` | pole arrivals excluded; rootward suffix excluded; the extra q-orbit has **no tree vertex** (MP6(e), Statement 3.18: q-roots off `p` do not continue in `T_a`) so it is **not** a selected exit |
| suffix `F` | IIa, `k=1` northeast extra, recorded `λ=2` | this is the unique priced selected exit; shared suffix counted once |
| `(0,y)` | case-IV terminal of the exhibit | not a selected positive exit of `U^full` |

MFE therefore reads

```text
sum lambda_F^exit = 0 + 0 + 2 = 2  <=  td - 1 - psi = 6 - 1 - 2 = 3.
```

**Disposition: `NO HIT` as a kill.** Slack 1. MFE does **not** sharpen the
numerical terminal menu of this cell: the two-pole sheet already used the
shared bound `Σλ <= 5-ψ = 3`. What MFE does is **license** that shared
bound, which was previously conditional on nested-`Y` disjointness. The
inequality is now GREEN; the cell still satisfies it.

**Pricing the q-only resonant orbit without reviving equality.** A selected-
exit refinement cannot charge it: it is not a selected exit. Charging it
by restoring printed `(22)`, fixed `κ`, or MP8's “no refinement can charge”
line is exactly the quarantined error. Two sound-looking +1 attempts still
fail to kill:

```text
illegal +1 at the merge on the q-orbit :  3 <= 3   (equality, R3 class lives)
L3  (prove λ(G_m) >= 1 by some other local test):  3 <= 3   (same)
```

Budget arithmetic therefore demands **at least +2 extra global charge**,
or a larger `ψ`, or a **non-budget** kill (coefficient / H1 / merged-pattern
/ Puiseux / collision). A fibre-local excess theorem that would turn the
q-orbit into a strict actual-weight jump of +2 on this prescribed fibre
does not exist; the multiplicity strengthening of the actual-weight lemma
was already rejected. Do not spend a round trying to squeeze +1 out of
MFE.

### 1.2 Push the root identity — first exact missing implication

Licensed now:

- (R1) every genuine root-meet edge has `X_root = μ(1-w_G)`, hence `w_G<1`;
- (R3) all-`μ=1`, `r`-way anatomy only: `w_G = l/(r+l) ∈ (0,1)`;
- row-1 `td=6,m=2` alphabet `W={2}`.

Exact check: (R3) matches (R1) with `μ=1` and `X=r/(r+l)` for
`(r,l)∈{(2,1),(2,3),(3,1),(3,2)}`. `W={2}` is disjoint from `(0,1)`, and
any parent carrying `w=2` gives `X_root = μ(1-2) = -μ < 0`, contradicting
`D_F>0`.

**Do not extend `w=l/(r+l)` past all-`μ=1`.**

**On-axis `td=6,m=2` mixed-`μ` is not an open cell; it is empty for a
different reason than (R3).** `m=2` has at most one merge (`MP1`). Both
poles are row-1, so `M=1` at entry. `MP5` propagates `μ=1` to the first
(hence only) merge. Mixed-`μ` at that merge would need some `μ_e≥2`, hence
some `M_{H_e}≥2` (Statement 8.4), contradicting M=1 ancestry. Thus:

- interior unique merge = residue A, necessarily `μ=(1,1)`;
- root unique merge = all-`μ=1`, excluded by `W={2}` plus (R3);
- mixed-`μ` cannot appear in the on-axis two-pole `td=6` sector at all.

**First exact missing implication (do not claim it):** a mixed-`μ` formula
for `X_root` in terms of the mixed reduced pattern
`(Σ_e μ_e, extras, ν)`, valid at a genuine case-I root, without assuming
all `μ=1`. Until that identity exists, (R1) only yields the weak per-edge
`w_G<1`. Off-axis (`some b_i≥2`) and `m≥3` (two or more merges, so a
resonant jump can emit `M≥2` before a later root) are the first sectors
where mixed-`μ` can occur. Coefficient matching and off-axis `W(w_0)` for
those entries are the next licensed tests; they are not (R3).

Root `M=1` remains legal. The local `r=2,l=1` ODE/Q model with `w=1/3` is
neither a Keller map nor a row-1 reach model. SF1/full-root completeness
and off-axis root completeness remain open. AWS root-aware ledgers are
diagnostics under an ambient-orbit completeness blocker, not a premise of
(R1)--(R3).

### 1.3 Global composition — `NO HIT` on a new bound; two literal interfaces

Contact-tree attachment plus actual cluster weights is MFE. MFE is a
filter, not a ceiling. Combining it with exact terminal orbit laws, mass
`ΣΛ=td`, `s≤td/3`, `Λ≥β≥3`, or Euler/genus identities reproduces known
relations. No new depth, pole-count, `td`, type, or complexity bound.

**Interface VDB-K (new client, not a bound).** van Dobben de Bruyn
arXiv:2608.27341: a projective-bundle complement is `A^n` only for a
rigid two-divisor, fibre-degree-differ-by-one, reduced one-fibre shape; in
dimension two, an intersection of multiplicity `k>1` produces a nonlinear
`D_{k+2}` dual graph and nontrivial `π_1` at infinity. Literal missing
lemma: a translation from Sigray pole-tree / residue-A Q-data to the
minimal SNC boundary dual graph of a compactified source (or graph of the
map). If that graph is forced to contain nonlinear `D_{k+2}`, residue A
cannot be a polynomial endomorphism of `A^2`. Until the translation lemma
exists this is `NO HIT`, not a topology-at-infinity proof.

**Interface Q-GHOST (new mechanism, see §5).** The extra q-orbit is
invisible to selected-exit/MFE and to `T_a`. A charge, if it exists, must
live on a translated pair `(f,g-b)` or on the g-tree, using promoted
Proposition 5.1 (`b_P=g(P)`) and the reviewed automatic condition (7) on
`T_a^+`. Not presently a theorem.

Keep `G2-PSC` and `G2-BD` distinct. Neither is discharged by MFE, (R1), or
VDB-K.

### 1.4 Attack the concrete survivor

Ranked by expected information per wall-clock hour against residue A:

1. **Per-edge Proposition 9.3 coefficient matching of the rigid ratio
   `a1/a2=2±√3` against both parents (H1).** Finite, exact, already named
   as the highest-value H1 computation, still not executed as a closed
   two-parent check. Inconsistency kills the cell; consistency produces a
   coefficient-pinned germ, the actual counterexample seed.
2. **Merged-pattern realizability / L1 (Prop 8.1(iv) at two simple searrow
   orbits with `l≥1`).** Would kill A, historical A′, and B together. Harder
   than (1) because it is a local ODE existence question already answered
   *yes* at the rigid ratio; the live question is joint parent-ratio
   compatibility, which is (1).
3. **Actual selected-exit ownership compiler replay** of this cell
   (software; expected `NO HIT` confirmation, not a kill).
4. **h-family / tower compatibility** at `G_m` and the suffix, using the
   complete Proposition 4.2 repair. Secondary; does not see the q-orbit.
5. **Puiseux algebraization then polynomialization** (Avenue 4). This is
   the disproof endgame, not the cheapest kill test.
6. **Direct collision/nonproper construction** from the Q-template. Only
   after (1) returns consistent coefficients.

Cheapest exact test with the highest chance of either killing residue A
**or** turning it into a counterexample seed: **(1)**. L3 (`λ(merge)≥1`)
is cheaper than (1) but, by §1.1, cannot kill the R3 class even if true.

### 1.5 Optimize the GGV recursion

Endpoint death on `D(Δ)` is a dense-open fact. It never kills a reducible
branch. Fastest complete treatment of rank-chart complements:

**Do not saturate or radicalize first.** Do not start another Groebner
presentation of the same ideal. Do not primitive-clear a rational left
kernel (that deletes cofactor content).

**Design: Fitting-indexed minor atlas with adjugate right kernels.**

- Object: the frozen `106×105` receiver matrix `M`, quadratic endpoint
  `E=x14*x72+x1*x97`, raw signed cofactors with no common-factor
  cancellation, already supported generically in slots `{81,93}`.
- Stratum `k`: `{rank M = k}` cut out by Fitting ideals, computationally
  by a generating set of `(k)`-minors. Current certificates:
  `P,C8P02` residual/total `9/104`; `Q1P02,TRIPLE02` `6/101`;
  `Q1P03,TRIPLE03` `4/99`; each with a nonzero-NF witness and exhaustive
  next-minor vanishing.
- On each nonempty open `D(Δ)` of a rank-`k` chart: form the adjugate
  right kernel, lift through the 95 rational pivots, pull `E` back.
  Verdicts allowed: `E≡0` (endpoint-dead on that open), `E` a unit after
  scaling (endpoint-alive; keep the germ), or `NO_VERDICT` if the
  identity is not decided.
- Complement `V(Δ)`: recurse on the next Fitting jump. Every complement
  is born as
  `NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED` until its own atlas is
  finished. A module presentation of `coker M` is the proof object that
  makes the atlas independent of a particular minor generating set; it is
  the verification gate, not the first compute.

**AWS fanout.** One isolated zero-swap job per live chart
(`P`, `C8P02`, `Q1P02`, `Q1P03`, `TRIPLE02`, `TRIPLE03`) for the current
complement layer; inside a chart, fan out over a generating set of next
minors, not over equivalent monomial orders. Active chart size 16 vCPU /
128 GiB is enough per open; additional mathematically nonduplicate
instances only when a chart splits into genuinely distinct Fitting jumps.
Cap: 512 vCPU campaign-wide, ≤1 TiB RAM, zero swap required. Fail closed
on reducer traps: pinned ambient standard basis, normal form after every
operation, `q2 mod (q2)=0` negative control.

**Proof-object gates (all mandatory before any emptiness claim):**
(i) pinned `M`, `E`, pivot list, ambient `std(I)` hash;
(ii) residual/total rank certificate with nonzero-NF witness and
next-minor vanishing;
(iii) exact kernel generators on `D(Δ)` and the pulled-back polynomial
`E|_(ker)`;
(iv) explicit complement list, each tagged
`NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED` or a completed child
certificate;
(v) no radical/saturation/component inference from rank or from one open.

### 1.6 Re-rank proof versus disproof

Proof-side, the source-trust stack through Sections 7--9 is no longer the
third bottleneck. The finite obstruction that actually blocks even `td=6`
is residue A plus landing of everything else. Disproof-side, residue A is
now a better-typed seed than it was at 12:24Z, but it is still not a
germ, and K00 remains the only source-open bounded point-search that does
not depend on Sigray.

Under-resourced routes that could beat the backbone, if any, are
**not** renamed conductor identities or larger Groebner jobs. The only
ones with a chance are: (i) the H1 coefficient match on residue A
(hours, not weeks); (ii) VDB-K dual-graph translation (a lemma, not a
classification project); (iii) Q-GHOST on a translated pair; (iv) K00
full-`P6` plus one prolongation. Avenue 10 (HC4) and Avenue 33 (symplectic
primitives) already returned `NO LEVERAGE` / `COSTUME` at their named
first gates; do not reopen them on slogans.

### 1.7 Software acceleration

**Target: a typed selected-exit ownership compiler** on the exact-pair
tree, emitting for each vertex of `U^full` the actual direction-orbit set,
the excluded pole-arrival/rootward pair, the Statement-7.3 witnesses, and
the MFE ledger. This is now on the critical path because MFE is GREEN and
residue A composition is the live question. Secondary, in the same
harness: a two-parent H1 coefficient-reach matcher for cell `(r,ν,l)=(2,3,1)`.

**Verification gate.**

- Negative control: tame automorphism `(x,y+x^2)` — no counterexample
  poles, compiler must refuse to emit a residue-A-type ledger.
- Positive control: residue A Q-data must replay `sum λ^exit=2`, `ψ=2`,
  `2<=3`, extra q-orbit **not** selected, shared suffix counted once.
- Mutation: duplicate a shared-suffix vertex or price a merge arrival per
  incoming edge; the compiler must fail closed.
- H1 matcher: on `(2,3,1)` with parents both row-1, `n=(5,5)`, emit
  either an exact incompatibility certificate or the pinned
  `a1/a2=2±√3` joint solution as a proof object.

Do not rebuild HENS-CT's generic composition backend. Do not enter
`jc2-lean`.

---

## 2. Disposition vector, avenues 1--46

Legend: `unchanged` / `raise` / `lower` / `reopen`. `G2-PSC` and `G2-BD`
are never merged.

### Changed this round

| # | call | reason |
|--:|---|---|
| 2 | **raise** | MFE is GREEN; all-`M=1` `td=6,m=2` root meet is analytically empty; §§7--9 trust is review-closed at corrected scope. Residue A is now a licensed composition target, not a source-debt hostage. Still no landing, no `RPMC(C)`, no cofinal ceiling, no `td=6` exclusion. |
| 4 | **raise** narrowly | Exact terminals certify germs; residue A is the distinguished missing algebraization arrow. MFE does not kill the cell, so germ-to-polynomial plus collision/nonproper end is higher value per hour than another tree identity. |
| 7 | **raise** narrowly | Resonant q-orbits are not selected exits of `T_a`. The only honest extra-charge home is a puncture/translated-pair/`A(F)` object (Q-GHOST), using promoted Proposition 5.1. Not a global `A(F)` classification project. |
| 27 | **raise** narrowly | New primary source supplies a Ramanujam/`π_1`-at-infinity `D_k` filter that was absent from the avenue ledger at the 05:24Z sweep. This is a dual-graph translation lemma for residue A, not a splice-diagram rerun. Historical Avenue 27 already died on one x-side branch and left the template; do not repeat that census. |
| 28 | **raise** narrowly | Companion of 27: if VDB-K produces a forbidden dual graph, log-Kodaira/BMY is the secondary numerical check. Still `NEEDS-DATA` until the graph exists. |
| 36 | **raise** / protect | K00/full-`P6` remains the strongest source-open bounded falsifier and is independent of Sigray. Do not starve it because residue A is fashionable. K00 is **not** Avenue 19. |

### Unchanged (omit none)

**Proof-adjacent, keep current rank.**
1 unchanged as a JC2 proof (no `td`/degree ceiling); **continue the
redesigned Fitting/adjugate complement path only**. Generic `D(Δ)` death
is not a branch kill. 3 unchanged (strip ODE scope). 5 unchanged (JvdK
does not bite non-automorphisms). 6 unchanged (fibres are multi-place;
one-place objects remain unpinned `A(F)` components). 8, 9 unchanged.
16 unchanged at its already-lowered execution rank (HENS-CT timeout; no
generic composition rerun). 25 unchanged, gated pilot only; L5 still does
not give coupled two-coordinate inertia. 31 unchanged as a better-typed
Rees/integrality pilot, not a bound.

**Dead, refuted, or costume at named gates.**
10 unchanged (`NO LEVERAGE`). 11 unchanged (Zhao/Mathieu ladder dead).
12 unchanged. 17 unchanged (category error). 18 unchanged (Shaska: graded
plane Keller maps are automorphisms). 33 unchanged (`COSTUME` at the
ordinary residue gate). 41 unchanged (naive scaling falsified by dim-3
CE). 44 unchanged (Moskowicz proof unsupported; retain only the repaired
membership theorem).

**Disproof / characteristic-p / local computational, no rank change.**
13, 14, 15 unchanged (Dixmier/End(`A_1`)/PDO dictionary). 19 unchanged
(char-`p`/Witt; first live bounded partial-degree frontier remains
maximum twelve; no all-Witt-to-polynomial inference). 20 unchanged
(p-curvature consumes false PC(2)/JC(4)). 21 unchanged (Hensel does not
kill `A_∞`). 22, 23, 24 unchanged (low). 29, 30 unchanged. 32 unchanged
(secant idempotent is an accelerator, not an obstruction). 34, 35
unchanged (2D sweep / dim-3 descent structurally blocked). 37, 38, 39,
40, 42, 43, 45 unchanged (low or renaming). 46 unchanged: Lean/AI is not
a discovery route; `jc2-lean` stays untouched by this campaign lane.

**Already down, stay down.**
26 unchanged/down: generic `td=6..9` monodromy already hit the `A_d/S_d`
wall; do not rerun.

---

## 3. Bottleneck rerank

### Proof

1. **Universal, provenance-preserving full-configuration landing.** Still
   the architectural wall for a proof of JC2. On-axis marked-event books
   omit post-jump mixed/`M≥2` suffixes; off-axis has no completeness
   theorem; implemented enumeration stops at `td=14`; no cofinal `td`
   bound. Source-trust through §9 is no longer this item.
2. **Residue A / resonant-jump realizability at `td=6`.** The last
   load-bearing finite obstruction on the two-pole `td=6` spine now that
   MFE is GREEN and the all-`M=1` root layer is empty. This is not a
   substitute for landing, but it is the cheapest object that can close
   or seed the `td=6` case.
3. **`RPMC(C)`, independently sourced type control, and a cofinal
   `td`/complexity ceiling.** A type-relative kill at finitely many `td`
   values is not JC2. `G2-PSC` is not this item; a pure Sigray proof
   bypasses `G2-PSC` and still owes (1)--(3). `G2-BD` is a separate
   post-residue-A delay bound, not a substitute for (1) or (3).

### Disproof / counterexample

1. **Characteristic-zero algebraization of residue A (or any certified
   germ) with an actual collision or nonproper end.** The Q-exhibit is
   now coefficient-rigid; it is still not a Puiseux forest and not a
   polynomial map. L5 certifies germs; it does not algebraize them.
2. **A source-open, rank-exact K00 / full-`P6` point plus one
   prolongation.** Independent of Sigray. A selected chart or capped
   solve is not evidence.
3. **A GGV Fitting-stratum survivor that is not merely dense-open-dead.**
   Honest test: quadratic `E` on every completed complement, then
   Kuranishi on a genuine positive-dimensional germ if one appears. The
   known 17-dimensional deep-locus first-order dual is automatic and
   must not be counted again.

---

## 4. New avenue and new connection

### New mechanism: Q-GHOST (dual-pattern / translated-pair visibility)

**Compared with repository history.** MP8's local `λ=0` anatomy, Theorem
O's “q-extras are invisible except through `deg q`”, 2POLE L1/L3, and
MFE's selected-exit definition all agree that the extra q-orbit is not a
`T_a` exit. No numbered avenue currently owns a *different-fibration*
charge of that orbit. Avenue 7 (`A(F)` / punctures) was scored as
“rebuilding the compactification”; Avenue 25 coupled CSP ignored the
Jacobian pairing at pattern roots; Proposition 5.1's forced centre was
promoted only this morning. Q-GHOST is not a rename of conductor/Euler
and not a revival of `(22)`.

**Mechanism.** At `G_m`, `q` has a simple root that `p` does not. That
root does not continue in `T_a`. For a shift `b` near the corresponding
leading `g`-value, promoted Proposition 5.1 plus automatic condition (7)
on `T_a^+` may make that direction a finite-puncture threshold of
`(f,g-b)`, hence a genuine vertex of a translated tree, carrying a cv
witness that MFE on the unshifted pair cannot see. Cheap discriminator:
one exact local chart at the rigid `(2,3,1)` ratio; either a translated
threshold appears, or a negative control shows the q-root remains
non-continuable for every `b`. Stop if the only construction uses
cross-fibre `κ` transport or equality `(22)`.

### New connection: MFE × DEPTH (R1) × MP1 on-axis emptiness of mixed-`μ`

MFE licenses the shared budget but does not kill residue A (§1.1). DEPTH
plus (R3) kills the all-`M=1` root meet. MP1 plus MP5 plus the row-1
`M=1` pin kill mixed-`μ` *on this sector* without (R3). The three
together give a clean two-pole `td=6` on-axis dichotomy: the only
remaining object is the interior first-step merge residue A. That
dichotomy was not stated as a composed theorem in the 12:24Z synthesis
(the mixed-`μ` door was left open at the wrong scope). It still does not
touch off-axis, `m≥3`, SF1, or `td>6`.

VDB-K × residue A is a second connection, currently `NO HIT` pending the
dual-graph translation lemma (§1.3).

---

## 5. Strongest next attacks

**Proof attack.** Two-parent H1 coefficient match of residue A
(`a1/a2=2±√3` against both row-1 parents at `n=(5,5)`), then, if
inconsistent, stop the cell; if consistent, feed the pinned germ to
Q-GHOST and to the selected-exit compiler. Do not wait for a +1 MFE
refinement.

**Falsification attack.** Same H1 match read in the opposite direction:
a consistent rigid coefficient pair is the cheapest characteristic-zero
germ that could algebraize. In parallel, keep K00 full-`P6` plus one
prolongation on separate AWS capacity, replay against undeduplicated
equations, and do not treat a selected chart as a point.

---

## 6. Software / decisive experiment

Exact target: selected-exit ownership compiler plus `(2,3,1)` H1 matcher
(§1.7). Verification gate as above. Estimated cost: one reasoning slot
for the compiler spec and negative/positive controls; the H1 matcher is
local exact arithmetic, not an AWS Groebner job. Do not launch AWS
root-aware recensus as a proof dependency; harvest the four terminated
OPEN ledgers as diagnostics only.

---

## 7. Idea cards (three)

### Card A — Residue-A two-parent H1 match

- **Dependencies / licensed assumptions.** Promoted MP6/MP7 anatomy;
  H1 = Proposition 9.3(a)--(d) per edge; rigid ODE ratio `a1/a2=2±√3`
  from Prop 8.1(iv) at `(r,ν,l)=(2,3,1)`; row-1 parent Q-data
  `(2,2,2,1,5)` with `n=(5,5)`; complete Proposition 4.2 repair if an
  h-family is consulted. Not using printed `(22)`, MP8 equality, or AWS
  root censuses.
- **Cheapest discriminator.** Exact two-edge resultant / coefficient
  comparison: the two case-II ratio equations plus the single rigid
  `(iv)` scale. Finite, characteristic zero, no CAS required beyond
  standard-library polynomials in two parent scales.
- **Outcomes.** Incompatibility: residue A dies at Q-level; two-pole
  `td=6` on-axis collapses to the two historical boundary classes (already
  weaker) and the prime remaining `td=6` work is off-axis/SF1/single-pole
  composite. Compatibility: a coefficient-pinned germ; start Q-GHOST and
  algebraization (Card C / Avenue 4).
- **Stop / rollback.** Stop if the matcher silently assumes `M-PAT`
  beyond the two-orbit searrow rule already in the exhibit, or if it
  transports `κ` across fibres. Rollback any “td=6 excluded” sentence
  that used only one parent.
- **Cost.** Hours of exact algebra plus different-model hostile review.
  No AWS.
- **Information gain.** Highest in the campaign: kills or seeds the
  unique remaining on-axis two-pole `td=6` object.

### Card B — Fitting minor-atlas complements

- **Dependencies.** Frozen `106×105` matrix and `E`; raw cofactors
  `{81,93}`; reducer-safe rank certificates `9/104`, `6/101`, `4/99`;
  preliminary `D(Δ)` endpoint-zero on `P`, `C8P02`, `Q1P02`, `Q1P03` with
  every complement `NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED`.
- **Discriminator.** On each complement, the next minor atlas plus
  adjugate right-kernel pullback of `E` (§1.5).
- **Outcomes.** All complements endpoint-dead: that chart dies; still no
  JC2, still no other charts. A complement with `E` a unit: genuine
  survivor germ, send to Kuranishi / prolongation. Adapter failure: fail
  closed, do not reuse the packet.
- **Stop.** Swap, unreduced representatives, common-factor cancellation
  of cofactors, radical/saturation claimed as emptiness, or any launch
  that treats dense-open death as a branch kill.
- **Cost.** Existing 16 vCPU / 128 GiB zero-swap lane, fanout per
  mathematically distinct Fitting jump only.
- **Information gain.** Completes the only honest finite GGV
  discriminator; low probability of resolving JC2, high probability of
  closing or seeding Avenue 1.

### Card C — Q-GHOST at the rigid merge

- **Dependencies.** Card A compatibility (otherwise there is no rigid
  local `g`-value to shift toward); promoted Proposition 5.1; automatic
  (7) on `T_a^+`; Statement 3.18; **not** (R3), **not** MFE equality.
- **Discriminator.** For the extra q-root `e` of the `(6,10)` pattern,
  test whether any constant `b` makes direction `e` a Proposition-5.1
  finite-puncture threshold of `(f,g-b)` with a Statement-7.3 witness off
  the unshifted `U^full`.
- **Outcomes.** A witness: extra actual charge, possibly + enough to
  break `2<=3` only if the new flag is independent of the suffix
  witness (needs a distinctness check; +1 alone still does not kill).
  No witness: q-orbit remains locally invisible; stop this charge line.
- **Stop.** Any argument that uses printed `(22)`, `(22-cl)`,
  cross-fibre `κ`, or the rejected multiplicity strengthening of
  actual weights.
- **Cost.** Local exact chart, then different-model review. No AWS.
- **Information gain.** Only remaining sound extra-charge route. Even a
  hit may not kill residue A (slack arithmetic); a miss closes a
  tempting false path.

---

## 8. Lane calls: `continue` / `redesign` / `stop`

| lane | call | why |
|---|---|---|
| Pure Sigray / exact-pair | **continue** | Principal proof backbone. Compose MFE; run Card A; land configurations; do not claim `td≠6`. |
| Hybrid `G2-PSC` | **stop** as critical path | Pure Sigray bypasses `G2-PSC`. The typed-interface remainder (`H-TRUNC`, live `CornerData` coefficient hole, other-chart obstruction) is real and not JC2-critical. Keep the name distinct from `G2-BD`. |
| Arbitrary-`Q` / rank-drop GGV | **continue** on Card B only | Reducer-safe ranks are certificates. Complements required. No equivalent Groebner clone. |
| Lambda-nonzero / raw-window GGV | **redesign** | Stop isolated face-order increments. Seek all-order row-ideal invariance or complete raw-window/endpoint incidence. Orders four/five already regular. |
| LF40 | **stop** | FACEPIN GB already capped / empty at row zero on the exact lane; another monomial-order clone of Avenue 1. |
| K00 / order-two / TD6 | **continue** K00 protected; **stop** isolated order-two face marching; **continue** TD6 only as residue-A / germ algebraization (Avenue 4), not as another book bash | Full-`P6` plus one prolongation is the independent falsifier. |
| D43 | **continue** only as a named Avenue-4 client if the nonempty modular family is still the same residue-A germ; **stop** further modular expansion | Modular nonempty ≠ char-0 ≠ polynomial. |
| Artin--Schreier | **continue** only at the bounded partial-degree-twelve frontier; **stop** unrestricted Witt towers | Growing-support lifts through every Witt level do not give a polynomial Keller gauge. |
| HENS-CT | **stop** generic composition; **continue** only with a structural adapter and a named client | Backend timeout, not a mathematical verdict. |
| External intelligence | **continue** | Next broad sweep due 2026-08-29 05:24Z. van Dobben is a filter, not a plane CE. Matysiak remains unsound. |

Root-aware AWS recensus: **continue as diagnostic harvest only**, not as
a proof lane. The analytic all-`M=1` exclusion does not use it. Mixed-
`μ`/off-axis/SF1 completeness still does.

---

## 9. Likely-missed insight and cheapest test

**Insight.** A successful +1 charge of the resonant q-orbit — the
refinement everyone wants from MFE — **still does not kill residue A**.
The recorded ledger is `2<=3`. +1 at the merge, or L3 `λ(G_m)≥1`, yields
`3<=3`. The R3 suffix class is robust to any single extra unit. Closing
`td=6` two-pole on-axis by Euler accounting needs +2 or a non-budget
argument.

**Cheapest test.** The `fractions.Fraction` arithmetic already run:

```text
2 <= 3     NO HIT
3 <= 3     still NO HIT
```

No engine required. Consequence: deprioritize MFE-refinements and L3;
prioritize Card A.

Second missed scoping fact, same cheapness: mixed-`μ` is impossible on
on-axis `td=6,m=2` by MP1+MP5+row-1 `M=1`, so “mixed-`μ` remains open”
must be read as off-axis / `m≥3` / SF1, not as a second two-pole `td=6`
cell.

---

## 10. Epistemic ledger

### Promoted facts (campaign-internal unless noted)

- Packet custody hashes and HEAD as in §0.
- Żoładek Theorem 6.12: `td≤5` invertible (refereed). Internal repaired
  Section 9 reconstruction of `counterexample => td>=6` is independent
  confirmation, not a `td≠6` theorem.
- Proposition 5.4 q-half; Propositions 6.7--6.8; Lemma 6.1; every-fibre
  replacement of printed Proposition 5.8; Proposition 5.1 sided
  non-leakage; Proposition 4.2 complete repair with (7) automatic on
  `T_a^+` for every target shift.
- Corrected Proposition 8.4 nonroot-only; Statement 8.5 root
  divisibility; root `M=1` legal.
- Actual-weight `(C7.1*)`; singleton first-separation; MFE at
  selected-exit/shared-inequality scope after the pole-endpoint
  truncation repair.
- All-`μ=1` root-meet identity (R1)/(R3) and `W={2}` exclusion in
  `td=6,m=2`.
- Reducer-safe residual/total ranks `9/104`, `6/101`, `4/99` as rank
  certificates only.
- No external JC2 proof or counterexample at 05:24Z. Matysiak SSRN
  papers unsound. van Dobben arXiv:2608.27341 is a topology-at-infinity
  filter, not a plane construction.

### Provisional inputs

- CORNER-M1 (`M_F=1` at a later constant corner) still provisional;
  unused here.
- Preliminary `D(Δ)` endpoint-zero on `P`, `C8P02`, `Q1P02`, `Q1P03`;
  `TRIPLE02/03` running; all complements
  `NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED`.
- Four root-aware AWS OPEN ledgers: diagnostics, not (R1)--(R3)
  premises.
- M-PAT merged-pattern shape rule (2POLE §4a): flagged, used only as
  the exhibit's already-stated two-orbit searrow anatomy.
- Residue A's recorded suffix `λ=2` and `ψ=2`: taken from the promoted
  Q-exhibit, not recomputed by a fresh selected-exit engine.

### Conjectures / not theorems

- Q-GHOST.
- VDB-K translation lemma.
- Mixed-`μ` `X_root` formula.
- Any `td=6` exclusion, landing, `RPMC(C)`, cofinal ceiling, `G2-PSC`,
  `G2-BD`, MP8 no-refinement, printed `(22)` / `(22-cl)`.

### Failed approaches (do not rerun)

- Printed `(22)`, fixed-baseline `(22-cl)`, cross-fibre jump/max `κ`.
- First Section 7 repair via transported `κ`.
- Actual-weight multiplicity strengthening.
- Display `(3.2)` `O(P,P_j)=u` at pole endpoints (conclusions survived
  by `min(v_j,O)`).
- Case-IV labelling of genuine root merges; l-free phase-3 root census;
  `M=1`-before-root engine filters; silent MU1 caps.
- Quotient-ring reducer trap (`q2^2` on `q2=0`); primitive-clearing
  cofactors; dense-open death as a branch kill; equivalent Groebner /
  face-order clones; LF40 as a decision computation.
- Matysiak; Moskowicz as a proof; naive dim-2 descent of the 3D CE;
  HC4 first gate; ordinary action-residue gate.

### Hidden assumptions in this report

- Residue A Q-data and suffix cost are the promoted exhibit, not a
  newly executed census.
- “No tree continuation” for the extra q-orbit is MP6(e)/Statement 3.18
  as used by the promoted MP package, not a new Puiseux check.
- On-axis mixed-`μ` emptiness uses MP1 (`≤ m-1` merges) and MP5
  (`μ=1` to the first merge) at their promoted perimeters.
- Small arithmetic checks assume the recorded integers `td=6`, `ψ=2`,
  suffix `λ=2`, and the algebraic identities (R1)--(R3) as integrated.

### Checks run

- SHA-256 of the packet and all 17 custody files; `git rev-parse HEAD`.
- Existence of the assigned grok prompt; absence of a pre-existing grok
  output.
- `python3` `fractions.Fraction` script: MFE `2<=3`; +1 still `3<=3`;
  (R3) matches (R1) on four `(r,l)` pairs; `w=2` yields negative
  `X_root` for `μ=1,2,3`; row-1 `w_0=2`.

### Failed attempts

- None computationally. No engine was started. No AWS call. No file
  write except this report.

### Contamination

- Independent. No peer `1707Z` response read. An initial `ls` of
  `xmodel/` (first 100 alphabetical entries) showed historical `as-*`
  artifacts, not `1707Z` ideation files. Subsequent path checks used
  exact grok-prompt / grok-output names only. `jc2-lean` untouched.
  No contamination affecting independence.

### Scope

- Strategy for the whole 46-avenue campaign at freeze 2026-08-28 17:07Z.
- Not a proof of JC2, not a counterexample, not a promotion of Q-GHOST
  or VDB-K, not an endpoint theorem, not a root census, not a `td=6`
  exclusion.
- Local execution limited to hashing, read-only inspection of sealed
  inputs, and the tiny exact-arithmetic script.
- Only write: this file.

### Model

Grok 4.6, xAI, via the campaign grok adapter / this session. A model
verdict is not mathematical evidence.
