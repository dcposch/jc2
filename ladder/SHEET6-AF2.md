# SHEET6-AF2.md — AF2 audit: the λ-cost rule derived from St 9.3 (24); case-IIb pricing decided

Status: COMPLETE + PROMOTED AS-IS (2026-08-07, SHEET6-A2P-REVIEW.md: all
fronts CONFIRMED; E6 proven at proof-level; two bonus tightenings noted).
**2026-08-28 scope correction:** the local per-direction pricing remains
promoted, now attached to the unique first-separation exit set rather than
literal nested `Y(F)`.  Actual-weight Corollary 7.1 supplies the singleton
global budget and, with the separately reviewed contact-tree attachment
theorem, the multipole selected-exit union budget. The old exhaustive
SF1/root census is superseded pending the
root-aware AWS rerun, except that the reviewed mixed-root/case-I theorem
plus MP1+MP4+MP5/D5 now analytically excludes the `td=6,m=2` pole-chain
root-meet branch. Broader off-axis/post-jump and SF1
completeness remain pending.
Auditor: Claude. Mission: SHEET6-CAMPAIGN.md §6
item 5 + SHEET6-HIII-REVIEW.md §§5/7 flagged asymmetry (IIb extra-orbit
pricing). Ground truth read on-page: refs/sigray_full.pdf pp. 27-45, 48-55
(text layer verified with pdftotext for every formula quoted below).

VERDICT:
- **IIb is NOT free and NOT flat-1.** Derived price (§2-3), per solved cell:
  λ_IIb ≥ k·max(1, ⌈gap⌉) + max(1, ⌈gap/ν_F⌉), gap := D_F/i − κ̄_F —
  the k extra orbits price EXACTLY like I/IIa_k/III extra roots (same
  St 9.3 (24) mechanism), and the 0-root adds its own ν_F-discounted term.
  There is NO coherent free reading: for gap > 0 the extra directions are
  forced to climb by St 6.2 alone (regularity not even needed), they land in
  distinct alternative-direction subtrees, and corrected (24) prices the cv
  flag owned by that step's first-separation exit set.
- **Both sanctioned residual classes are EXCLUDED**: the single IIb μ=4 k=1
  step at r10/M4 that carries both has gap = 12 − 5 = 7, so λ_F ≥ 8 > 3 =
  td−2 ((26)/St 9.5 alone; ψ-budget not needed). The kill is sign-robust
  (§4): under the PRINTED (mis-signed) (24) the bound is 17 > 3.
- **Historical composed nonroot/IV residual (single-pole, td ≤ 6) = 0;
  AF3-superset book: 13 → 4** (§5).  The old `SF1 residual = 0` claim is not
  exhaustive after the root-scope correction and awaits the root-aware rerun.
- **AF2's general rule is now DERIVED from St 9.3 (24)** (§2), modulo one
  new thesis erratum (E6, a sign slip in (24) as printed — repaired against
  its own proof and its three p. 53 usages) — every λ-badge the campaign,
  H3, III and composition docs ever used is retro-validated, and for
  gap > 0 roots the price is even regularity-free (a tightening, §2 R3).

## 1. Ground truth: St 9.3 (24) verbatim + a sign slip (E6)

St 9.3 (p. 49) is the thesis's ONLY quantitative λ-generator. Verbatim
(pdftotext):
  "Set F ∈ T_a↘ ∩ V_a. Assume G := F + c* ∈ T_a↗. Set G := I_P(v) for some
   P ∈ R̄_a \ R_a. Set H = I_P(w) such that H ∈ T_{a,cv}. Then
     κ_H(π(H)−1) ≥ D_F/mult(p_F,c*) − κ_F(π(F)−1)              if c* ≠ 0
     κ_H(π(H)−1) ≥ D_F/(ν_F mult(p_F,c*)) − κ_F(π(F)−1)/ν_F    if c* = 0."

**E6 (new erratum, sign slip in (24))**: κ̄_F := κ_F(1−π(F)) > 0 on every
↘ vertex, so the printed "− κ_F(π(F)−1)" = +κ̄_F. But:
- the printed proof's own chain is "κ_H(w−1) ≥ κ_F(w−1) = κ_F(w−u) −
  κ_F(u−1) ≥ κ_F d_F/mult(p_F,c*) − κ_F(u−1)"; the middle identity is false
  as printed (κ_F(w−u) − κ_F(u−1) = κ_F(w+1−2u) ≠ κ_F(w−1)) and correct
  with −κ_F(1−u); with that fix the conclusion is D_F/mult(p_F,c*) − κ̄_F;
- all three quantitative usages (p. 53, St 9.6 proof) instantiate the MINUS
  version: (A) child (7j,21j,7,3,5): "from Statement 9.3 we obtain λ_F ≥ 2"
  = 21/... = D_F/i − κ̄_F = 7 − 5; (B) (9j,75j,25,3,6): λ_F ≥ 3 = 9 − 6;
  (C) (5j,20j,5,4,4), k = 2: per-root price 1 = 5 − 4, "Since k = 2,
  λ_F ≥ 2". (The plus version would give 12, 15, 9 — absurd against the
  printed possibility lists.)
So the intended (24) is
  **κ_H(π(H)−1) ≥ D_F/mult(p_F,c*) − κ̄_F        (c* ≠ 0)
    κ_H(π(H)−1) ≥ (D_F/mult(p_F,c*) − κ̄_F)/ν_F  (c* = 0)**
(same slip family as E5's ν_F-for-ν_G on p. 53: "(π(F)−1)" printed for
"(1−π(F))" in both statement and proof line; the proof block also prints
"=≥" and "mult(p_F,c_1)" for "mult(p_F,c*)"). Everything below uses the
corrected (24); §4 shows the two residual kills do NOT depend on the fix
(the printed-literal version prices HIGHER).

Supporting cast: literal Not 9.3 defines nested `Y(F)` sets and cannot be
summed along a chain.  The reviewed replacement assigns each cv flag to its
unique singleton-chain first-separation exit set `E_i`; repaired St 9.4/9.5
then gives `sum_i lambda_i^exit <= td-1-psi`, hence `<=td-2`, by
actual-weight Cor 7.1 (`c253bd12...`, gate `727f5850...`). St 7.1 (p. 35):
H ∈ T_{a,cv} ⇒ π(H) > 1. St 7.3 (p. 35): a branch with a T_a↗ vertex has a
T_{a,cv} vertex. St 6.1/6.2 (p. 29): ↘/↗ dichotomy on T_a⁺ and the
step criterion "F = G + c ∈ T_a↘ iff d_G < (1−π(G))mult(p_G,c)". Repaired
Props 6.7/6.8 (pp. 33-34; `c3d6ff92...`): a down parent with deg p>1 has
positive microsteps, and every selected down microstep reaches a same-branch
pole/next down vertex. Prop 8.1(i) (p. 39-40):
(ξ^δ p(η))^i = f_F⁺, i = deg(p_F)/M*_F — hence mult(p_F, c*) = i·mult(p, c*)
for EVERY root (true multiplicities are the reduced pattern's times i).
St 8.4 (p. 42): mult(p,c) | M_G. St 3.18 (p. 18): every root of p_F yields
exactly one direction (unique ε per ν_F-orbit; F∗0 exists iff 0 is a root).

## 2. The pricing mechanism: derivation of the general λ-rule

Setting: one chain step G = F + c (Prop 9.3; F = G° ∈ V_a ∩ T_a↘ the new
node, G the ↘ continuation, c the special root, mult(p,c) = μ | M_G). The
reduced pattern p of Prop 8.1 has roots: the c-orbit (mult μ), possibly 0
(mult 1; exactly the IIb/III patterns), and k extra ν_F-orbits c_1..c_k
(templated simple). For any root c* of p with direction ≠ that of G:

- (R1) Corrected St 3.18 gives a realizable one-grid-step point
  `E:=F*_(κ)(εc*)`; Proposition 6.7 puts `E` in `T_a+` when `deg p_F>1`
  (the only exception is already the μ=1, M=1 kill).  Proposition 3.2
  separately names the next vertex `H₁:=F+c*`.  These points need not be
  equal; sweep r2 `581219e0...` supersedes the former conflation.
- (R2) THE CLIMB.  Exact Statement 3.9 for the fixed fibre polynomial,
  applied to the microstep `E`, gives the same raw sign test as St 6.2:
  `E in T_a↘` iff `d_F < (1−π(F))*mult(p_F,c*)`.  Multiplying by κ_F > 0 and
  using D_F = κ_F d_F, κ̄_F = κ_F(1−π(F)), mult(p_F,c*) = i·w (Prop 8.1(i),
  w := mult(p, c*)):
      **E ∈ T_a↘  ⟺  D_F/(i·w) < κ̄_F  ⟺  gap(c*) := D_F/(i·w) − κ̄_F < 0.**
  If `gap<0`, repaired Proposition 6.8 transports the down microstep along
  the same branch to the next down vertex `H₁`; regularity forbids this for
  an alternative direction.  Equality is excluded by Statement 6.1, so a
  regular step forces `gap>0`.  Then `E in T_a↗` unconditionally.  This is
  the corrected Proposition 6.7/6.8 bridge `c3d6ff92...` (Opus5 review
  `eb37373b...`, correction `050ccddd...`; Lemma 6.1 R2 `2fdbbee9...`,
  Opus5 review `5193e7b0...`, correction `607e0dcf...`), and it recovers the thesis's printed regularity inference
  without assuming the next vertex positive at the outset.
- (R3) THE PRICE. `E ∈ T_a↗` on branch P ⇒ ∃H = I_P(π(H)) ∈ T_{a,cv}
  (St 7.3; printed usage p. 53: "Since G* ∈ T_a↗, there exists H = I_Q(w) ∈
  T_{a,cv}").  This alternative-direction subtree first separates at F, so
  H belongs to F's exit set. Corrected (24):
      contribution(c*) ≥ D_F/(i·w) − κ̄_F = gap(c*)        (c* ≠ 0)
      contribution(0)  ≥ gap(0)/ν_F                        (c* = 0).
- (R4) ADDITIVITY + FLOORS. `lambda_F^exit` is the sum over the distinct cv
  flags owned by F's first-separation exit set.
  Distinct directions give distinct H (branches separate at F: O(P,P') =
  π(F) < π(H), so I_P(π(H)) ≠ I_{P'}(π(H))), and every Y(F)-term is > 0
  (St 7.1: π(H) > 1). Each certified term is ≥ 1 (κ_H(π(H)−1) ∈ N, the
  St 9.4-proof integrality line — the same line the campaign always used)
  and ≥ ⌈its (24) bound⌉. The thesis's own additive practice is printed at
  9.6(C): "Since k = 2, λ_F ≥ 2".

**Derived AF2 (general λ-rule).** For a step with pattern roots as above,
    λ_F ≥ Σ_{j=1..k} max(1, ⌈gap(c_j)⌉) + [0 a root, ≠ direction of G]·
          max(1, ⌈gap(0)/ν_F⌉),
with gap(c*) = D_F/(i·mult(p,c*)) − κ̄_F. On the campaign's templates
(extra orbits simple, w = 1, all gaps equal): **λ_F ≥ k·max(1, ⌈gap⌉)
(+ the IIb 0-term max(1, ⌈gap/ν_F⌉))**, gap = D_F/i − κ̄_F. Trust
perimeter per part: the ⌈·⌉ needs the St 9.4-line integrality; the
max(·,1) floor is automatic after regularity forces every alternative gap
strictly positive; the gap-part for gap > 0 roots needs no regularity once
the direction is fixed. AF2 as reverse-engineered (campaign §0a) is exactly the
k·max(1,⌈gap⌉) clause: **DERIVED**. Every λ-badge in SHEET6-CAMPAIGN/H3/
III/HIII-REVIEW is retro-validated; the E5 λ-bound's AF2-dependence
(SHEET6-III §5) upgrades to (24)-derived.

## 3. Case dictionary: I/IIa/III reproduce AF2 exactly; IIb was underpriced

Where the extra roots sit, per Prop 9.3 case (patterns pp. 52-54, verbatim):
- **I** (ν_F = 1): p = (η−c)^μ(η−c₁)…(η−c_k), k ≥ 1 (St 3.16). No 0-root.
  λ ≥ k·max(1,⌈gap⌉). Engine: identical. (Thesis prints only the floor
  λ ≥ 1, p. 54.)
- **IIa** (pattern (a)): p = (η^ν−c^ν)^μ Π_k. No 0-root. k ≥ 1:
  λ ≥ k·max(1,⌈gap⌉) — the thesis's own p. 53 λ ≥ 2/≥ 3/≥ 2 (A)/(B)/(C)
  are exactly this rule (§1). k = 0: no extra root, λ = 0 possible
  (9.6(v), printed). Engine: identical.
- **III**: p = η^μ Π_k (the S1 structure, SHEET6-III §2: c = 0 IS the ↘
  direction). Extra roots = the k ≥ 1 nonzero orbits: λ ≥ k·max(1,⌈gap⌉).
  No 0-term (0 is the continuation, not a climbing root). Engine (E5
  arithmetic in hiii_compose): identical.
- **IIb** (pattern (b)): p = η(η^ν−c^ν)^μ Π_k. The ↘ direction is the
  c-orbit (μ ≥ 2 > 1), so BOTH the 0-root AND the k orbits are climbing
  extras:
      **λ_IIb ≥ k·max(1, ⌈gap⌉) + max(1, ⌈gap/ν_F⌉).**
  The thesis only ever cashes the 0-root at its floor ("In the case (b)
  F + 0 ∈ T_a↗, therefore λ_F ≥ 1", p. 54) because λ ≥ 1 suffices for its
  td ≤ 5 budgets — it never SOLVES (b). The engine solved (b) but priced
  it at the thesis's flat floor (sheet6_campaign.py child_from:
  `lam = max(lam, 1)` with the orbit term zeroed — even its own docstring
  said `max(that, 1)`). That flat 1 is the asymmetry HIII-REVIEW §7
  flagged. There is no reading of the thesis under which the k orbits of
  (b) are free while the SAME roots in (a)/I/III are priced: the patterns
  differ only by the η-factor, which only ADDS a direction. Free-orbit
  readings would need the orbit directions to be ↘ (second ↘ children):
  impossible when gap > 0 (R2), and excluded by the lemmas' own
  regularity hypothesis otherwise.

## 4. The two sanctioned residuals: exact kill

Both classes ride ONE step (hiii_compose trace, reproduced §5): r10/M4
entry Q(G) = (4j,4j,4,4,9) --IIb μ=4, k=1, ν_F=7-->:
  pattern (b): deg p = 5·7+1 = 36, deg q = 2·7+1 = 15 (l = 0);
  i = deg(p_G)/μ = j; ratio (b): 36/15 = 4(1+n)/(9+n) ⇒ n = 11 (≡ 3 ≡
  −κ̄_G mod ν_G ✓); child Q(F) = (12j, 36j, 7, 3, 5) — St 9.7's own
  hypothesis shape (R1); R2 = (2/3,3s+2,3,2s+2) is its λ=0 IIa_0 child.
The step's price:
  gap = D_F/i − κ̄_F = 12 − 5 = **7**;   gap/ν_F = 1.
  - Climb: by (R2), the c₁-direction is in T_a↘ iff 12 < 5 — FALSE; the
    0-direction identically; both realizable microsteps climb by the raw
    St 6.2 sign + St 6.1, after Prop 6.7 types them in `T_a+`.  Prop 6.8
    is needed only for the general negative-gap contradiction in R2.  No
    regularity input is used here.
  - Price: corrected (24): the two curve vertices contribute ≥ 7 and ≥ 1;
    λ_F ≥ 8. Integer bounds — no ⌈·⌉/integrality needed.
  - Budget: St 9.5/(26): Σ λ_{F_i} ≤ td − 2 = 3 over ANY characteristic
    sequence of a td=5 counterexample. 8 > 3 (already 7 > 3 on the orbit
    term alone). The step is impossible; R1 is never created, R2 never
    reached. **Both sanctioned residual classes EXCLUDED.**
  - Sign-robustness: under the PRINTED (uncorrected) (24) the bound is
    12 + 5 = 17 > 3 — the verdict does not depend on adjudicating E6.
  - Not needed: ψ-budget/H3q, N1/H5a/H5b, AF3 (r10/M4's M-menu is
    sanctioned), regularity, the ≥1 floors. Needed: the (a)-(d)/8.1/3.17
    arithmetic that computed the cell (H1) and the cell's own (b)-template
    (the class is DEFINED as that cell's output — same surface that
    produced it).
Exact hand-check (this audit, `python3` inline, §7): child data, n-value,
M_F = gcd(36,15) = 3, gap, both climb tests, both budget comparisons.

## 5. Recomputed composition (engine flag `iib`), new residual table

Engine: sheet6_campaign.py gets a module flag IIB_DERIVED (default False =
legacy flat-1; gate/validate untouched, gate PASS re-verified) implementing
§3's IIb price inside child_from (per-t exact, family-singleton checked as
for every other λ); hiii_compose.py gets CLI arg `iib` to set it. Purely
additive; default runs byte-identical to the promoted baseline (re-run and
diffed this audit).

RESULT (`python3 hiii_compose.py iib`, exact, 2026-08-07; frontier = 0 and
open_kinds = 0 at EVERY entry — cap-clean):

| block | baseline (HIII-REVIEW §5) | under derived IIb pricing |
|---|---|---|
| td=3, td=4 | 0 | 0 (unchanged) |
| td=5 r10/M2 | 0 | 0 |
| **td=5 r10/M4 (SANC)** | **2 classes (R1, R2)** | **0** (iv_hits 7→4, all ψ/(l)/(m)-dead) |
| td=6 sanctioned (r2,r3,r6,r8/M2,r9/M3,r11) | 0 | 0 (r8/M3-ext iv_hits 4→0 too) |
| td=6 AF3-superset | 13 classes | **4 classes** (all r9/M2 ∪ r9/M6, all via IIa_k μ=2 λ=2 routes: (1/3,7,3,5)@2, (1/4,5,4,4)@2, (2/3,3s+2,3,2s+2)@2, (3/4,4s+3,4,3s+3)@2; R ∈ {3,4}) |
| SF1 (case-I root-terminations) | 1 class ((1/2,1,2,1)@3 r8/M6) | **0** (its route rode the r8/M6 IIb μ=6 k=1 gap=7 step) |

**COMPOSED GRAND: td3: 0, td4: 0, td5: 0, td6: 4 (all AF3-ext).**
The sanctioned single-pole book is EMPTY at every td ≤ 6, and the SF1 book
is empty. What remains on the whole program: the 4 AF3-superset classes
(vanish if AF3's sanction M | gcd(D,P) is proved — campaign §6 item 6),
and the two-pole (3,3) configuration (item 4). Note the 9 killed ext
classes and the killed SF1 class all rode IIb steps whose gaps are
child-data-determined (e.g. r8/M6's μ=6 k=1 ν=7 step: gap = 50/5 − 3 = 7,
λ ≥ 8 > 4; its μ=5 k=0 family steps: gap/ν_F = (8s+6)/(4s+3) = 2, λ ≥ 2).

## 6. Errata, trust perimeter, honesty section

New thesis errata:
- **E6 (St 9.3 (24), p. 49 — load-bearing family, benign once fixed)**: the
  κ_F-term's sign is flipped in the statement AND in the proof's middle
  identity ("(π(F)−1)" for "(1−π(F))"); repaired in §1 against the proof's
  own chain and the three p. 53 usages. All quantitative λ's in §9 depend
  on (24), so the fix is load-bearing for the thesis, though every printed
  APPLICATION already uses the corrected version. (Same subscript-slip
  family as E5; the block also has "=≥" and a stray "c_1".)
- **E7 (St 9.6 proof, p. 52 — cosmetic)**: patterns (a)/(b) print q's
  c-orbit as (η^ν−c^ν)², inconsistent with the SAME proof's Diophantine
  (deg q = (k+1)ν+1 ⇒ power 1), with its solutions (21,15)/(20,16), with
  M_F = gcd(21,15) = 3, and with 9.7/9.8's printed patterns (power 1).

Trust perimeter of the two kills (§4): Prop 9.3 (a)-(d) + Prop 8.1 +
St 3.17 arithmetic (= H1, the layer that produced the cell), the cell's own
(b)-template, corrected-or-printed (24) (sign-robust), St 6.1/6.2, repaired
Props 6.7/6.8, St 7.3, Not 9.3, St 7.1, St 9.5/(26). NOT engaged by the
two numerical kills: regularity (H4's
wlog), the St 9.4-integrality line, ψ/H3q, N1/H5a/H5b, AF3, Prop 8.4.

Honesty items (no new standing hypothesis is introduced — **no H6**):
- The max(·,1) floors in the general rule (not §4's kills) ride H4
  regularity plus the repaired 6.7/6.8 bridge: a negative alternative gap
  would force a second down vertex and is excluded; every surviving gap is
  positive, so its ceiling is already at least one.  This is the corrected
  form of the thesis's own λ ≥ 1 floor (pp. 53-54).  The ⌈·⌉ on fractional
  gaps still rides the
  St 9.4-proof line "κ_G(π(G)−1) ∈ N" — both pre-existing perimeter items
  of AF2, now localized to the parts that need them. Conversely, gap > 0
  pricing is now REGULARITY-FREE (§2 R2) — a strict tightening of what
  AF2 was booked under.
- Extra orbits are priced at their template multiplicity w = 1 (pattern
  simple); for μ ≥ 4, w ∈ {2..μ−1} sub-patterns are different enumeration
  cells (pre-existing H4 pattern-template surface, shared by every branch
  and by the thesis's own printed patterns). The residual classes ARE
  w = 1 cells, so their pricing is internally exact.
- The engine's IIb grammar takes l = 0 for all k (deg q = (k+1)ν_F+1),
  generalizing 9.6(b)'s printed "Consider (b). Then by Statement 8.2 one
  has l = 0" (stated there for μ = 2 with no k ≠ 0 hypothesis) to μ ≥ 3 —
  pre-existing H1-surface item, unchanged by this audit (pricing is
  per-cell and does not depend on the grammar's completeness).
- Composed-table stack after this audit: {H1, H2, H4, AF3-sanction (ext
  rows only), H5a, H5b} + proved H3q + the derived λ-rule (this doc; =
  printed statements + E6 fix; floors mod H4). AF2 leaves the hypothesis
  list (campaign §0c) and becomes a derived rule; SHEET6-III §5's "AF2
  dependence" flag and HIII-REVIEW §7's engine asymmetry are both
  discharged.

## 7. Reproduction

    cd cases && python3 sheet6_campaign.py gate   # unchanged, PASS (flag off)
    python3 hiii_compose.py                       # baseline: reproduces
                                                  # HIII-REVIEW §5 verbatim
    python3 hiii_compose.py iib                   # this doc's §5 table (~40 s)

Engine change: sheet6_campaign.py IIB_DERIVED flag (default False) in
child_from — IIb λ = k·max(1,⌈gap⌉) + max(1,⌈gap/ν_F⌉) per-t with the
existing family-singleton/OPEN machinery; hiii_compose.py `iib` CLI arg.
Both runs re-executed this audit: baseline diff vs the promoted output is
empty; the `iib` run's only deltas are kills (survivor sets shrink, no new
OPEN kinds, frontier 0 everywhere). §4's step arithmetic hand-verified in
an inline exact script (child Q-datum, n = 11, M_F = 3, gap = 7, both
St 6.2 climb tests, 8 > 3 and 17 > 3).
