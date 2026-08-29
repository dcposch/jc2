# Fable 5 hostile review — td=8 cv/contact gate (Grok 4.6 primary)

Lane: Fable 5, independent hostile mathematical review. Date: 2026-08-29.
Target:
`xmodel/m2-td8-cv-weight-contact-gate-primary-grok46-20260829.md`
(full SHA-256 `93c58d63af6ff9e000531c077b10c86ef1a9d4d6f54b6b343d1f98c7d6183ecd`,
verified) and its packet
`cases/m2_td8_cv_weight_contact_gate_grok46_20260829/`.

Executed from `/Users/dc/code/math/jc2`. No web, no AWS, no commit/push, no
canonical edit, no heavy computation (desk `Fraction` arithmetic and pdftotext
page extraction only, scratch in `/tmp`), no `jc2-lean` access of any kind.
The source mathematics was reconstructed on-page from `refs/sigray_full.pdf`
(pp. 12, 16, 18, 19–20, 23, 26–28, 35–40, 46, 48–49 freshly extracted; the
stacked-fraction hazard respected — every load-bearing formula re-read as a
display block) and from the promoted ladder at the exact cited extents
(`SIGRAY-AUDIT.md`, `SHEET6-AF2.md` §§1–2, `SHEET6-H3.md` §4a,
`SHEET6-MULTIPOLE.md` MP1, `SHEET6-DEPTH.md` §1, `SOL-PROP58.md` headline,
`REDUCTION.md` Section-7 rows). The target's tests were replayed but carry no
verdict weight; every charged claim was re-derived.

---

## 0. Verdict

**`PASS_WITH_REPAIR`.**

The lead verdict `CV_CONFIGURATION_FORMALLY_SURVIVES` **stands**, at the
target's own conditional scope (reviewed td=8 equal-join row; exact-separation
premise at its `PASS_WITH_REPAIR` tier). Five of the seven charged layers are
confirmed outright, including the two the campaign most needed: the
four-vertex budget census re-derived **without** quarantined printed Prop 7.5
`(22)` (the target's Item-4 correction is exactly right per the promoted
ladder, and it corrects a real tier slip in the reviewed exact-separation
report), and the `M*_A=21 ⟹ some k_j=2` inference, which I verified is
*definitionally* airtight from Not 8.1 + Prop 8.1's printed proof line.

Two genuine repairs are required. Neither flips the survival verdict — I
exhibit the repaired witness myself in §3 — but both invalidate "PROVED" rows
of the target's firewall table as stated.

- **R1 (chain length).** "Any finite string of `(2,1)` steps is a legal
  Prop 7.1 filling" is **false at printed-source scope**. Prop 4.2's proof
  (p. 19) carries the standing inequality
  `d_F + d_{h_j,F} ≥ α_j·d_F + 1 − u`, `α_j = Σ_{i<j}(k_i−1)l_i/k_i`. On the
  A-vertex tower every degree-one-chain element has `d_{h_j,A} = d_A/2`
  ((iii) of Prop 4.2) and `α_j = j/2`, so the inequality reads
  `7(3−j) ≥ 5` with the reviewed `D_A=14`, `κ̄_A=5`: **`j ≤ 2`**. The pure
  `(2,1)` tower has length `m_A ≤ 3`, i.e. at most **two** recursion steps at
  the cv vertex. The packet's three- and four-step runs are not source-legal
  fillings, and "the printed source does not pin `m_A`" is overstated: for
  the degree-one chain it pins `m_A ∈ {2,3}` (`m_A=1` dies against the
  reviewed `deg q = 15` via Prop 8.1(ii): `deg p_{h_1,A} = 21k+15` with
  `k = i(μ−1) = −1` would be negative).
- **R2 (double root / recursion polynomial).** Two conflated overreaches.
  (a) In Prop 7.1/7.3 the recursion's `p := p_F` is the **f-pattern** at the
  cv vertex — Prop 7.3's printed `p(c) = a` forces this — so
  `p = p_{f−a,H} + a`. The object with the double root is `p_H − a`, not
  `p_H`; for fiber value `a ≠ 0` the recursion's quadratic has two *distinct*
  roots, the pure-power collapse does not occur (verified exactly: remainder
  degrees `0,4,8` at `l=1,3,5`), and the claim that nontrivial subtop is
  "forced by the recursion rather than by St 3.9(ii)" evaporates off the
  `a=0` fiber. (b) Even for `p_H − a`, `Δ_A = 2` forces a double root only
  for separation level `θ > 7`; the contact boundary `θ = 7` (separation
  exactly at the cv level, explicitly included in the reviewed
  exact-separation report's `Δ_A=2 ⟺ deg(p_H)=2`) leaves `p_H − a` with two
  simple roots. The target's "a split pattern at H would already be a V_2
  event" begs the question: a `V_2` event *at* `π(H)` is not excluded by
  `Δ_A = 2`. `H° = A` itself is robust in all `Δ_A=2` cases and is confirmed.

Compatibility with the reviewed exact-separation report
`ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370`: two
substantive divergences, one resolved in each direction (§4). The target
correctly refuses that report's `δ_a = 0` clause (which rode quarantined
printed `(22)`); that report correctly includes the `θ = 7` boundary that the
target's double-root claim excludes.

Survival proves no gluing, landing, realizability, counterexample, degree
ceiling, or JC2 result — the target's own firewall on this is accurate.

---

## 1. Custody, seals, replay

Target full hash matches the charge; body self-hash
`39f94bf51b4c78e90ba5e48a0f35f81c8db64a4650fcf9f6ee9fe9104a38cfeb`
reproduces (cut = all bytes above the `report_body_sha256` line). All five
custody-table hashes and byte counts reproduce exactly (prompt 3665 B, Opus
allegation 32759 B, Sol56 row 5623 B, Grok D2 review 20866 B, Grok
exact-lambda 21095 B). Packet seals reproduce
(`8a457b21…`, `7f5474e2…`, `d98da18a…`). Replay:

```text
python3 test_cv_weight_contact_gate_td8.py     TD8_CV_WEIGHT_CONTACT_GATE_GROK46_TEST_PASS checks=351
python3 -O …                                   identical
python3 cv_weight_contact_gate_td8.py --json | shasum -a 256
  85beaff0d4fe939cf96519e80d09201bc47c965b1eb1f904997e6c8fb497745f   (matches seal)
```

The no-`assert` claim is accurate (line-start scan of both files; the only
occurrences are in the test docstring/scanner). The certificate hash is
recomputed by the replayed suite from the sorted compact JSON with the hash
key removed. Of the ten `/tmp` producer mutations I replicated one
(`M*` taken as `42`): rejected at the `M*_A` guard, matching the table row.
Suite character, disclosed: most checks restate producer formulas; the
verdict weight in this review comes from the on-page reconstruction below,
not from the replay.

Fable's exact-separation review was identified by hash as
`xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md`
and read for the compatibility charge. The target's firewall statement that
it did **not** read that file is consistent with everything in the target
(its §2 derivation differs exactly where that review's §2.6 differs).

---

## 2. Charge-by-charge audit

### 2.1 Exact budget / four-vertex census (target §2, Item 4) — **PASS**

Reconstructed independently; the derivation is sound and, critically, uses
only promoted material:

- **Ceiling.** St 9.4 `(25)` re-read on p. 49; its printed proof already
  contains the x-side mechanism the target uses: `(0,x) ∈ T_a↗` ⟹ St 7.3
  gives an x-side cv vertex `G`, St 3.11 gives `π(G) > ψ`, and the proof's
  own integrality line plus St 7.1 give weight `≥ ψ`. H3-psi (`SHEET6-H3`
  §4a, promoted) supplies `ψ = ⌈M/j⌉ − 1 = ⌈5/3⌉ − 1 = 1` on the reviewed
  row (`j = M(1−w) = 3`), the first-separation exit sets replace literal
  nested `Y(F)`, and the two-pole union rides the promoted MFE partition.
  Ceiling `td − 1 − ψ = 6`. ✓
- **Floors.** Corrected `(24)` (E6 sign repair re-verified on p. 49 against
  the proof's own chain and `SHEET6-AF2` §1): A-copies
  `D/m − κ̄ = 14/2 − 5 = 2`; trunk `17/2 − 7 = 3/2 → 2` by (INT), which the
  exact-separation review proved at printed-proof scope from Prop 7.3's
  geometric proof (re-read here on pp. 37–38: `Λ(Q) = κ_G π(G) − κ_G` at the
  generic perturbation, a positive integer). Merge `λ_G = 0` is the St 3.18
  arrival identity (reviewed). `2+2+0+2 = 6` meets the ceiling; each priced
  charge is exactly 2. ✓
- **Saturation.** Corollary 7.1 as the promoted **actual-weight inequality**
  (`c253bd12…` / Terra gate `727f5850…`) — correctly *not* the printed
  corollary, whose printed proof (p. 39, verified) derives it from
  quarantined Prop 7.5/7.4. Applied to
  `{H_{A1}, H_{A2}, H_{tr}} ∪ (x-side)`: `8 ≥ 1 + 6 + W_x` gives `W_x ≤ 1`;
  with `W_x ≥ ψ = 1`, `W_x = 1`, one weight-one x-side vertex ((INT) makes
  every cv weight a positive integer). A fifth cv vertex would give
  `td ≥ 9`. Distinctness: MP1 (`Σ(r(G)−1) = m−1 = 1`, re-read) — the two
  A-branches part at the unique equal join at level `< 1`, so their cv flags
  at `u_0 > 1` are distinct, and trunk/x-side are separated by level and
  component. ✓
- **The quarantine is real.** `SIGRAY-AUDIT.md` §4 and `REDUCTION.md`
  (Section-7 row): printed `(22)`, literal per-puncture `δ_a`, and `(22-cl)`
  are "invalid/unproved"; only the Cor 7.1 inequality is promoted. So
  `δ_a = 0` is **not** forced, exactly as the target says, and the omitted
  nonnegative `δ_a` indeed adds no cv vertex (it is a sum of
  `Λ(P) − weight ≥ 0` excesses at existing cv flags, Not 7.3 re-read on
  p. 38). The target's Item-4 correction of the Opus/exact-separation
  `δ_a = 0` clause is the ladder-correct position (§4 below).

One citation compression, no repair: the firewall row credits
"Cor 7.1 + H3-psi + St 7.1 + MP1"; the floors also need corrected `(24)` +
(INT) + the reviewed merge identity, all used in the body.

### 2.2 Proposition 7.1 at a quadratic cv vertex (target §3a) — **PASS**

Prop 7.1 re-read verbatim (pp. 35–36): `p := p_F`, `q := p_{g,F}`,
`G := F°`, tower `(K,L,S)_{G,0}` from Prop 4.2, recursion
`r_{j+1} = r_j^{k_j} − s_j p^{l_j}` for `j ≤ m−2`, degree law
`deg(r_j) = (l_j/k_j)·deg(p)` for `0 ≤ j ≤ m−1`. Prop 4.2 re-read
(pp. 19–20): `gcd(k_j,l_j)=1`, `k_j,l_j ∈ N*` printed, with the promoted
complete repair admitting exactly one terminal `(1,0,c)` shift
(`gcd(k,0)=k`). At `deg(p)=2`, `k_j | 2l_j` with coprimality gives
`k_j ∈ {1,2}`, `l_j` odd when `k_j=2` — elementary and correct; the window
scan is decoration. Scope note (feeds R2): `p` here is the f-pattern
including the fiber constant; the *degree* conclusions are insensitive to
that, so this layer is unaffected.

### 2.3 `Δ_A = 2` and the double-root consequence (target §3b) — **PASS on the equivalence and `H°=A`; REPAIR_REQUIRED on the double root (R2)**

Confirmed by reconstruction: St 3.10 (p. 16) gives the convex descent;
`D=14, κ̄=5, m=2` give the no-drop charge `2` and the drop menus
(`9−θ` contact with `θ ∈ N*`; `2(9−θ)` conjugate with `θ ∈ ½+N`); any
integer `≥ 3` at one A-copy overshoots the ceiling with the other floors;
hence `Δ_A = 2 ⟺` no drop before `d=0` and no `κ` jump `⟺ deg(p_H)=2` —
identical to the reviewed Theorem B, including menus `{8..3}` and
`{17,…,5}` (recomputed). `H° = A` confirmed: Not 3.3 (p. 12) makes `F°` the
last *vertex* strictly below; on `(π(A), π(H))` a `V_1` would jump `κ` and a
`V_2` would drop the degree, both excluded by `Δ_A = 2`; only the pair's own
events could create vertices there (all other branches left at or below
`A`); the microstep `A*c*` is not a vertex. This holds in every `Δ_A = 2`
case, including `θ = 7`.

**Not confirmed:** "`p_H` is a double root, `c(η−r)²`". See R2 in §0/§3:
wrong polynomial (`p_H − a`, not the recursion's `p_H`) and wrong at the
allowed boundary `θ = 7`, where `H` is itself the `V_2` vertex, `p_H − a`
splits, and there are two directions at `H` each with the Prop 7.3
*equality* `Λ(P) = 2`. The firewall row "`H°=A`; `p_H` a double root —
PROVED from `Δ_A=2`" must be split: first clause PROVED, second clause
repaired to "`p_H − a` is a double root **or** splits exactly at the cv
vertex (`θ=7` contact)". No downstream budget quantity changes (the `θ=7`
place structure contributes `0` to `δ_a` just as the double root does).

### 2.4 The `M*=21` / `k_j=2` inference (target §3c) — **PASS**

Not 8.1 (p. 39) *defines* `M*_F := gcd(deg p_F, deg p_{h_0,F}, …,
deg p_{h_{m−1},F})`, and Prop 8.1's proof (p. 40) prints
`M*_F | deg(p_{h_j,F}) = (l_j/k_j)deg(p_F)` — both verified verbatim. With
`i_A = 2` (St 3.17(i) chain from the row-4 pole, reviewed prior),
`M*_A = 42/2 = 21` is definitional. Then `21 | d_j = 42·(l_j/k_j)` gives
`l_j/k_j ∈ ½N`, hence `k_j ∈ {1,2}` — **independently of the H-side
quadratic** — and `gcd = 21` odd against `42` even forces some `d_j` odd,
i.e. some `k_j = 2` with `l_j` odd. `m_A = 0` excluded (`M*` would be 42).
Bonus consistency the target did not note but which I verified: the
Q-badge's `M_A = 3` (Not 8.1 *with* the terminal; Not 9.1 `(14,42,7,3,5)`)
is satisfied identically by the Prop 8.1(ii) terminal degree `21k + 15`
(`gcd(21, 21k+15) = 3` for every `k`), and it *excludes* the promoted
`(1,0,c)`-shift terminal at `A` (that terminal degree `42(μ−1)+1` would give
`M_A = 1`). The all-`(2,1)` chain realizes `M* = 21` exactly (`d_j = 21`
each), as claimed.

### 2.5 Finite `(2,1)` chain versus pure-power collapse (target §3d) — **PASS_WITH_REPAIR (R1, R2)**

Degree-stability is correct and robust: on either `p = η²` or the honest
`p = c₀(η−r)² + a`, a `(2,1)` step with leading cancellation maps a generic
degree-1 remainder to a degree-1 remainder (verified exactly both ways).
Pure-power collapse is **model-bound**: it happens iff `p` is a perfect
square, i.e. on the `a = 0` fiber; for `a ≠ 0` the remainder has degree
`2l−2` and nothing in the recursion forces subtop (the jet-freedom stands
on the reviewed Theorem E alone). And the *legality* claim is where R1
bites: the Prop 4.2 δ-ledger caps the pure chain at `m_A ≤ 3` (§0, §3), so
"any finite string" is false, the packet's 3-/4-step exhibits are dead
data, and the legal exhibit set is `m_A ∈ {2,3}` (one or two recursion
steps at `H`). Longer towers exist only with higher-degree openers (e.g. a
`(1,1)` first pair, `deg r_0 = 2`, keeps `α` at 0 and admits three
subsequent `(2,1)`s) — outside the target's displayed family.

### 2.6 Pole / place census (target §4a) — **PASS**

Everything reconstructed verbatim: table `(23)` row 4 on p. 46
(`(2,3)`, `(D,D_g) = (2,3)`, `(deg p, deg q) = (4,6)`, `ν = 3`, `Λ = 4`);
Prop 5.6 `(19)` `Λ(F) = D_g·deg(p)/ν = 4` with the unique-ε
(corrected St 3.18) one-direction-per-orbit proof; formula `(18)` places
`(1, c=0)` and `(3, nonzero)`; Prop 5.4(ii) pattern split
(`p = ηp*(η³)`, `deg p* = 1`; `q = q*(η³)`, `deg q* = 2`; the other case
non-integral); corrected St 5.2 ratio `2/3`; Prop 5.7 `Λ ≥ β = 3` with
printed proof; Prop 5.8 by the promoted every-fiber `SOL-PROP58`
replacement, so two row-4 poles exhaust `td = 8` and a third is impossible.
Four pole-places, `Λ` sum `8`. The per-direction Prop 7.3 reading at the
A-cv ("inequality, not equality, at a double root") is the correct printed
reading, with the `θ=7` caveat of §2.3.

### 2.7 Does the displayed filling prove only survival at printed-data scope? — **YES, with a narrowed exhibit (R1/R2) and one packet nit**

The certificate's negative booleans (no route kill, no landing, no gluing,
no realizability, no counterexample, no degree ceiling, no JC2, conditional
flags set) are accurate, and the survival claim is the right tier: what is
shown is consistency of the alleged configuration against the assembled
constraint set. But "meets every sum, gcd, orbit, place, and distinctness
constraint **used here**" leans on its last two words: the packet omits
(a) the Prop 4.2 δ-ledger — which its own 3-/4-step exhibits violate,
(b) the `M_F = 3` terminal-gcd condition (satisfied identically, so
harmless, but unchecked), and (c) the `p` vs `p − a` identity (R2). After
repairs a legal filling survives everything I could throw at it (§3), so
the verdict tier is unchanged. Packet nit: `nearrow_ode_kill_control()`
asserts its `both_13_and_14` collisions rather than computing them — it is
a control on a case the report itself proves empty (`G = A`), so it carries
no verdict weight, but it should not be described as a check.

---

## 3. The repaired witness

For the record, the surviving filling after R1+R2, all constraints named:

```text
Fiber a arbitrary; A-copy cv vertex H, parent G = H° = A.
p := p_{f,H} = c0·(η−r)² + a   (θ>7 branch; θ=7 uses c0(η−r1)(η−r2)+a).
Tower at A: m_A = 3, pairs (2,1),(2,1),(2,1);
  δ-ledger (κ/κ_A units): 16, 9, 2 > 0, terminal 0 — printed inequality
  7(3−j) ≥ 5 holds for j = 0,1,2 and forbids j = 3;
  μ_A = 3/2, Prop 8.1(ii) k = i(μ−1) = 1, terminal degree 21+15 = 36;
  M*_A = gcd(42,21,21,21) = 21 ✓, M_A = gcd(21,36) = 3 ✓ (= gcd(21,15));
  m_A = 2 variant (k = 0, terminal degree 15) equally legal.
At H: r_0 = a₁η + b₁ (deg 1, b₁ ≠ −a₁r), two (2,1) recursion steps,
  remainders stay degree 1 (verified exactly on the honest p);
  k_j ∈ {1,2} law ✓; some k_j = 2 ✓.
Census: two table-(23) row-4 poles, Λ = 4+4 = 8, four pole-places (1,3)×2;
  T_{a,cv} = {H_A1, H_A2, H_tr, H_x}, weights 2,2,2,1, δ_a unforced;
  MP1 distinctness ✓; ceiling 6 = 2+2+0+2 ✓; W_x = 1 ✓.
```

Nothing in the printed source or the promoted ladder that I checked kills
this configuration, uniformly in `t`. The smallest genuinely unpinned datum
remains the subtop/contact level (the reviewed exact-separation report's
`P_2(c*)` / `O(P*,P**)`); the tower length, contrary to the target, is
pinned to a two-element menu for the degree-one chain.

---

## 4. Compatibility with the reviewed exact-separation report (`ec355795…`)

Agreements (everything load-bearing): the A-step menus and
`Δ_A = 2 ⟺ deg(p_H) = 2`; the trunk criterion kept out of scope; the merge
identity `λ_G = 0`; `ψ = 1` and the ceiling 6; (INT); the i-chain
(`i_A = 2`, `i_G = 14`); the corrected `(24)` sign; and the target is a
faithful execution of that report's own two endorsed next-lemma attacks.

Divergence 1 — **target correct**. The exact-separation review (§2.6)
endorsed Opus Theorem F's final clause through "Prop 7.5's identity",
forcing `δ_a = 0`. The promoted ladder (SIGRAY-AUDIT §4; REDUCTION
Section-7 row) holds printed `(22)` and literal `δ_a` unestablished; only
the Cor 7.1 inequality is promoted. The target's census reaches the same
four-vertex conclusion from promoted material only and correctly leaves
`δ_a` unforced. Consequence for the record: `ec355795…`'s confirmation of
that one sub-clause should be read at printed-proof tier, not promoted
tier; its other layers are untouched.

Divergence 2 — **exact-separation report correct**. That report and its
review explicitly include the boundary `θ = 7` (contact separation exactly
at `u_0`) inside `Δ_A = 2`; the target's "double root, PROVED from
`Δ_A = 2`" excludes it without a supporting statement. R2 restores
agreement.

Also noted: the target's §0.2 sentence that the missing jet is "forced by
the recursion rather than by St 3.9(ii)" overstates novelty relative to
`ec355795…` — off the `a = 0` fiber the recursion forces nothing (no
collapse), and the underdetermination rests where that report put it
(Theorem E).

---

## 5. Clause-level scorecard

| target claim | verdict |
|---|---|
| Four cv vertices, weights `2,2,2,1`, from Cor 7.1(actual-weight) + H3-psi + St 7.1 + (24)/INT + MP1; printed `(22)`/`δ_a=0` quarantined | **CONFIRMED** (the Item-4 correction is ladder-right) |
| `δ_a` not forced to zero; excess is not a fifth vertex | **CONFIRMED** |
| Prop 7.1 degree law verbatim; `deg(p)=2 ⟹ k_j ∈ {1,2}`, `l_j` odd at `k_j=2`; terminal `(1,0)` unique | **CONFIRMED** |
| `Δ_A=2 ⟺` no drop & no jump `⟺ deg(p_H)=2`; menus `{3..8}`, `{5,7,…,17}` | **CONFIRMED** |
| `H° = A` | **CONFIRMED** (robust incl. `θ=7`) |
| "`p_H` is a double root" from `Δ_A=2` | **REPAIR (R2)**: it is `p_H − a`, and only for `θ>7`; `θ=7` splits it |
| `M*_A=21` forces `k_j ∈ {1,2}` and some `k_j=2` | **CONFIRMED** (definitional via Not 8.1 + Prop 8.1 proof line; `M_A=3` consistency verified, shift-terminal excluded) |
| Pure-power filling collapses ⟹ subtop forced by the recursion | **REPAIR (R2)**: true only on the `a=0` fiber |
| "Any finite string of `(2,1)` steps is a legal filling"; packet runs 1–4 steps | **REPAIR (R1)**: Prop 4.2 δ-ledger caps the pure chain at `m_A ≤ 3` (≤ 2 steps); 3-/4-step exhibits illegal |
| "Printed source does not pin `m_A`" | **NARROWED**: `m_A ∈ {2,3}` for the degree-one chain |
| Two row-4 poles, `Λ=8`, no third pole, four places `(1,3)×2` | **CONFIRMED** (verbatim + SOL-PROP58) |
| Prop 7.3 inequality-only at a double-root cv | **CONFIRMED**, `θ=7` caveat (two directions, equality each, `δ_a` unchanged) |
| Survival-only scope firewall; conditional flags | **ACCURATE** ("used here" narrowed per §2.7) |
| Custody, seals, `-O` identity, no-assert, 351 checks | **VERIFIED** (one of ten mutations replicated) |

---

## 6. Maximum safe consequence, exclusions, next discriminator

**Maximum safe consequence.** On the reviewed td=8 equal-join affine route,
conditional on the exact-separation premise at its reviewed tier: the
alleged knife-edge configuration — two table-(23) row-4 poles exhausting
`td=8` with places `(1,3)` each; `T_{a,cv}` of exactly four vertices with
weights `2,2,2,1`, derived from promoted material with `δ_a` left unforced;
quadratic A-copy cv vertices with parent `A`, tower pairs `k_j ∈ {1,2}` and
some `k_j = 2` forced independently by `M*_A = 21` and by the quadratic
degree law — is consistent at formal source-data scope, witnessed by a
degree-one `(2,1)`-chain filling of tower length `m_A ∈ {2,3}` with
nontrivial subtop, on either the `p_H − a` double-root branch (`θ>7`) or
the `θ=7` split branch, uniformly in `t`. The route is not killed at this
gate. The genuinely free printed-data datum remains the pair's contact
level (equivalently the second `κ_F`-graded subtop value), not the tower
length.

**Exclusions.** No route kill and no route promotion; no exact `λ`; no
source landing, gluing, realizability, Keller counterexample, degree
ceiling, or JC2 consequence; `Δ_A = 2` on the actual branches remains an
unproved contact statement; `δ_a = 0` remains unestablished; this review
did not re-derive the promoted actual-weight Cor 7.1 theorem, SOL-PROP58,
the St 3.17(i) i-chain, or the MFE multipole partition (all used at
promoted/reviewed tier); nine of the ten `/tmp` mutations were taken on
the table's word; no AWS was or is authorized.

**Cheapest next discriminator.** Emit the complete finite tower book at
`A`: all Prop 4.2-legal `(K,L)` with `k_j ∈ {1,2}` (forced by `M*=21`),
the δ-ledger `α`-budget `α_j ≤ 1 + ρ_j − 5/14`, the `M*`/`M_A` gcd laws,
and the H-side degree law `deg r_j = 2ρ_j` — a strictly desk-scale
enumeration (the pure chain contributes `m ∈ {2,3}`; higher-degree openers
contribute finitely many more shapes). Each surviving shape is a typed
value of the missing jet datum, so the book converts the contact-gate
question into finitely many `V_{2,a}` alternatives; the same ledger run at
the trunk (`D = 17i_F`, `κ̄ = 7`, `m = 2i_F`) may narrow Theorem C's
defect profile for free. Adding the ledger check and the honest-`p`
recursion to the existing packet is a few dozen lines.

---

## 7. Reproduction

```sh
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/m2-td8-cv-weight-contact-gate-primary-grok46-20260829.md').read_bytes()).hexdigest())"
cd cases/m2_td8_cv_weight_contact_gate_grok46_20260829
python3 test_cv_weight_contact_gate_td8.py && python3 -O test_cv_weight_contact_gate_td8.py
python3 cv_weight_contact_gate_td8.py --json | shasum -a 256
# R1 ledger: delta_j ∝ 7(3−j)−5 = 16, 9, 2, −5 → pure (2,1) tower has m ≤ 3.
# R2: run the (2,1) recursion on p = c0(η−r)²+a, a ≠ 0: remainders stay
#     degree 1; pure powers leave degree 2l−2 ≠ −1 (no collapse).
# pdftotext -f P -l P -layout refs/sigray_full.pdf for P in
#   {12,16,18,19,20,23,26,27,28,35,36,37,38,39,40,46,48,49}.
```

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = f972253c571a547eab2bf67c79298d59a47fb800a4b367710458e343d93a2fa6
