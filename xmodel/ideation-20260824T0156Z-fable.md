# Blind full-spectrum submission — round `20260824T0156Z-8bf25a5` — lane: Fable

- **Model:** Claude Fable 5 (`claude-fable-5`), Anthropic. **CLI:** Claude Code 2.1.228.
- **Supplemental lens (applied after the common scan):** global geometry and proof architecture.
- **Written:** 2026-08-24T02:16Z. **State cutoff honored:** `2026-08-24T01:56:44Z`.
- **Basis:** clean commit `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4`, plus the packet-pinned dirty
  `AUDIT.md` (P1/raw-boundary and latest D43 entries not yet committed on the clean basis).
- **Packet:** `xmodel/ideation-20260824T0156Z-packet.md`, SHA-256
  `4c1e582041db9e5f7267c13dbd681cacc56b0e7176d81dc185ee2662818c967a` — recomputed locally, matches.
- **Blindness:** no other `ideation-20260824T0156Z-*` file (submissions, prompts, logs, run manifests)
  was opened. No post-cutoff review verdict was consumed: `D25 -> D27` is used only at its reviewed
  pointwise one-band MOD-p scope; P1, P2, and the external intake are used only at
  producer-checked (+ coordinator replay where recorded) lifecycle state. No claim is promoted here,
  no work is launched, no ledger is edited, no network was used.

**Files actually read (SHA-256 of all 13 recomputed and equal to the packet table):**
`COORDINATION.md` (full); `APPROACHES.md` (full, all 46 rows); `AUDIT.md` (opening erratum
lines 1–73, raw-boundary entry 1017–1043, D43 entries 1329–1426); `PROGRESS.md` (current-day
2026-08-23 entry); `notes.md` (newest `LIVE STATE`, 2026-08-24 01:05Z); `xmodel/ideation-
20260824T0035Z-synthesis.md` (full); `xmodel/ideation-20260824T0035Z-portfolio.md` (full);
`xmodel/review-d43-nf-fid-grok.md` (full); `xmodel/round1-dtransition-20260824.md` (full);
`xmodel/review-dtransition-grok.md` (full); `xmodel/intake-supermind-guo-20260824.md`
(§1 executive decision, §2 protocol/evidence labels, §9 evidence matrix and hard perimeter,
§10 recommended actions — the pinned read scope; the declared gaps are Guo's Sage-only terminal
expansions and unresolved derivational independence); `xmodel/round1-boundary-passport-20260824.md`
(full); `xmodel/round1-trace-regularity-20260824.md` (full).

Evidence-tier labels used below: **[PROOF]** established mathematics; **[ECD]** exact conditional
deduction (hypotheses explicit, re-derivation owed in-lane before any use as premise);
**[LIT]** trusted-external literature statement, to be re-verified from sources before promotion;
**[HEUR]** heuristic; **[EXP]** proposed experiment. Producer-checked round artifacts are cited as
`P1`, `P2`, `E` at their cutoff lifecycle states only.

---

## 0. Independent frame before dispositions

The three deltas that matter are, in order of architectural weight:

1. **P2 (producer-checked) reorganized the properness wall.** The equivalence
   *trace regularity ⟺ integrality ⟺ finiteness ⟺ automorphism* is not traction by itself — it is
   full-scope equivalent to what we lack — but the localization is. Over the normal ring
   `A = C[P,Q]`, `A = ∩ A_p` over height-1 primes, so **the entire global properness statement is a
   divisor-by-divisor statement about principal parts at affine target divisors**, each computed by
   an exact finite formula from completed branch data [ECD, P2 §1–2, owed re-derivation]. The 84/168
   completion collision proves the currently retained contact packet does not determine even the
   `m=2` datum. That is the first *exact witness* of packet insufficiency the campaign has ever had —
   it converts `G2-PSC`-style "fidelity" from vocabulary into a measurable property.
2. **The polar support of that datum is a known, extremely rigid object.** The affine divisors where
   trace principal parts can be nonzero are exactly the components of Jelonek's asymptotic variety
   `A(F)` (non-integrality at `p` ⟺ a valuation over `p` with `x` or `y` unbounded ⟺ non-properness
   over the generic point of `V(p)`) [ECD, obligation below]. For plane maps, `A(F)` components are
   parametrized rational curves with one place at infinity [LIT, Jelonek 1993; Chau's Keller-map
   refinements adjacent]. Row 6's recorded diagnosis ("AM was run on the wrong object; the correct
   one-place objects are `A(F)` components, whose place data are unpinned") and row 7's "A(F) never
   constructed from the books" are both answered by the same construction: **on any resolved model,
   `A(F)` components are the images of boundary divisors not mapped into the target line at
   infinity, i.e. of exactly the dicritical-type divisors the campaign's books already enumerate.**
   And the Keller identity pins arithmetic there: for any boundary divisor `E` with affine image,
   `ord_E(dx∧dy) = ord_E(F*(du∧dv)) ≥ 0`, since `du∧dv` is regular and nonzero at affine points
   [ECD, three-line derivation, owed care for contracted divisors]. So the missing P2 datum — the
   target-affine-divisor-tagged completed branch pairing with coefficient convolutions — lives on
   finitely many book-enumerable divisors carrying a Keller-pinned ramification budget.
3. **P1 COSTUME (producer-checked) and the confirmed one-band D signal shrink the live surface.**
   Raw presentation-dependent boundary invariants are dead at tested scope; the D tower is now one
   reviewed pointwise MOD-p measurement plus one running full-cell child (`D2-CELL26`) whose
   compatible-base-locus verdict is the only thing that can move that lane. Everything else in the
   D-series is correctly gated behind it.

The synthesis of my lens: **properness is a divisor problem, not a degree problem.** A Keller
counterexample must carry a one-place rational curve in the target along which finitely many exact
coefficient convolutions fail to vanish; the campaign owns (a) the machinery that enumerates the
candidate carriers (books), (b) the exact functional that must vanish on them (P2), and (c) exact
controls on both sides (tame/Hénon; the nonproper `(x², xy)` map, whose single trace pole `2q²/t`
sits precisely on its `A(F) = {u=0}` — consistency I checked against P2's own table). What it does
not yet own is the pairing datum in the middle. That is where this round's proof attack, its
counterexample attack, and its instrument should all point.

---

## 1. Disposition vector (avenues 1–46)

Baseline = the 46-row map plus the 00:35Z portfolio overlay (not the historical survey scores).

```
1 unchanged   2 raise      3 unchanged  4 unchanged  5 unchanged  6 raise
7 raise       8 unchanged  9 unchanged 10 unchanged 11 unchanged 12 unchanged
13 unchanged 14 unchanged 15 unchanged 16 unchanged 17 unchanged 18 unchanged
19 raise     20 unchanged 21 unchanged 22 unchanged 23 unchanged 24 unchanged
25 raise     26 unchanged 27 unchanged 28 unchanged 29 unchanged 30 unchanged
31 raise     32 unchanged 33 lower    34 unchanged 35 unchanged 36 unchanged
37 unchanged 38 unchanged 39 unchanged 40 unchanged 41 unchanged 42 unchanged
43 unchanged 44 unchanged 45 unchanged 46 unchanged
```

Reasons for every change (note: raises 2/6/7/25/31 are **correlated** — all flow from the single
P2 delta read through the Jelonek localization; they are one idea's footprint, not five independent
votes):

- **2 raise.** The boundary trees become the natural *carrier* of the newly named missing datum
  (dicritical branch coefficients and their target tags), and the `a_E ≥ 0` pinning is a
  tree-decoration statement; this raises the lane's promise without releasing the new-cells hold.
- **6 raise.** The one-place/semigroup machinery is restored to its correct object with an exact
  functional attached: `A(F)` components are one-place rational curves and the trace principal
  parts give the first concrete thing their "unpinned place data" must feed.
- **7 raise.** P2's equivalence plus divisor-localization makes `A(F)` exactly the polar support of
  the trace package, answering half of Grok's "not cheaper than rebuilding the compactification"
  objection: the books and a resultant-based trace calculator are two independent constructors.
- **19 raise** (allocation-driven, not evidence-driven). With the D-series reduced to one running
  child, raw boundary invariants costumed, and most CE lanes held, the registered odd-prime/other-
  support W2-survivor refinement is the highest-information *available* orthogonal disproof lane.
- **25 raise.** The coupled two-cover CSP acquires the layer whose absence made passports "too
  generous": branch-coefficient convolutions along dicritical divisors, plus the covering-of-
  `C²∖A(F)` framing that anchors transitivity constraints on the target side.
- **31 raise** (the strongest single change). P2 turned integrality/ZMT from an unexecuted slogan
  into a map-by-map exact equivalence with a divisor-local criterion and one named missing datum;
  row 31 is now the campaign's most precise statement of what a proof must supply.
- **33 lower.** P1's exact suite (producer-checked, review running) executed the automorphism half
  of G27's own designed experiment and it returned COSTUME — untwisted action residues vanish
  identically and primitive pole orders are presentation artifacts — so the surviving twisted/
  signed variants inherit a proved-tautology burden before any new run; the residue-A half stays
  blocked on uncertified tails.

No reopens: none of the closed rows (11, 18, 41) or currently stopped/held items is touched by the
deltas.

---

## 2. Reranked principal bottlenecks

**Proof side (rank, movement):**

- **P-1 (new #1).** *Determination of trace principal parts by certified boundary data.* The
  canonical target-affine-divisor-tagged completed branch pairing with coefficient convolutions —
  P2's named missing datum — restated as a property: a packet schema is JC2-sufficient only if it
  determines every `PP_C Tr(z^m)`. This subsumes the fidelity half of `G2-PSC` and gives the queued
  `PSC-FINGERPRINT` a universal receiver instead of an ad-hoc collision target.
- **P-2 (unchanged #2).** *Complete landing/coverage and choice independence* for a pure Sigray
  source (a hybrid route still owes `G2-PSC` outright). Now testable against P-1's receiver: a
  landing theorem that cannot feed the receiver is not complete.
- **P-3 (unchanged).** *Absolute/cofinal td ceiling.* KJN stays type-relative; no provenanced
  bounded type menu exists. Untouched by the deltas.
- **P-4 (new, replaces vague "properness endgame").** *`A(F)`-component rigidity:* prove no
  one-place rational affine curve admits a Keller-compatible dicritical direct image (using
  `a_E ≥ 0`, semigroup admissibility, and convolution constraints). This is the honest endgame
  shape of rows 6/7/31 after P2; it kills the divisor rather than chasing unbounded moments `m ≤ d`.
- **P-5 (unchanged).** *Characteristic-zero certificate repair* for the reopened cCa2/cCa6 uses;
  externally mitigated (SuperMind/Guo terminals, producer-checked) but unpromoted and still
  conditional on the GGV reduction/transcription bridge.

**Counterexample/disproof side:**

- **D-1 (new #1).** *`D2-CELL26`'s compatible base locus.* The six band-26 compatibility functions
  cut the D25 base (two named interior points are outside the one-band image at both primes —
  reviewed scope); whether a nonempty positive-dimensional compatible stratum survives on the full
  `A^14` cell is the sole live internal gate for the tower. Every deeper D question is correctly
  queued behind it.
- **D-2 (new).** *Existence of any exact char-0 pole-surviving local model.* Nobody has ever
  exhibited even a *local* branch package along a candidate `A(F)` component satisfying the
  provable Keller boundary constraints with a surviving trace pole. P2's collision shows the
  retained packet permits one; whether the Keller pairing does is open in both directions and cheap
  to attack (Card 2). This is now the cheapest genuinely two-sided CE-side bottleneck.
- **D-3 (unchanged, gated).** *Modular-to-integral bridge* for the D tower: common integral model,
  flatness/Hensel — open per the D43-NF-FID review (CONFIRMED WITH GAPS; band-42 `Xf_alpha`/
  `Xg_beta` P4P1 correction outside the traces; 122 fat rows corroborated, not regenerated). Held
  behind D-1 as ordered.
- **D-4 (unchanged).** *Char-p Witt refinement:* F3/F5 low-support collision search keeping
  W2-survivors — the consensus untried extension, fully orthogonal to everything above, not on the
  hold list.
- **D-5 (unchanged).** *Algebraization architecture* (stages 3–8, stage 7 hardest) — unchanged and
  downstream of everything.

---

## 3. Idea cards (exactly three)

### Card 1 — `A(F)`-anchored trace receiver (proposed new avenue row 47)

Covers: **genuinely new avenue/mechanism**, **new cross-avenue connection**, **strongest proof
attack**.

- **Target claim.** (i) [ECD to re-derive in-lane] For dominant `F=(P,Q)` with `J ∈ C*`: the polar
  support of `{Tr(x^m), Tr(y^m)}_{m≤d}` is exactly the union of affine `A(F)` components; each
  principal part is the P2 convolution formula summed over the dicritical-type boundary divisors
  mapping onto that component; and `ord_E(dx∧dy) ≥ 0` with equality iff `F` is unramified along
  `E`, for every boundary divisor `E` with affine image. (ii) [EXP] Decide whether one certified
  residue-A book plus `J=1` *determines* the `m ≤ 2` convolutions along its dicritical-type
  divisors, or whether the P2 `b`-slot freedom persists under the dicritical tagging.
- **Avenue IDs.** 7 + 31 core; 2 (carrier), 6 (one-place/semigroup), 25 (coupled pairing); proposed
  as new row 47 "asymptotic-divisor direct image / trace receiver" because no existing row combines
  enumeration (books), topology (covering of `C²∖A(F)`), and arithmetic (principal parts) into one
  falsifiable object.
- **Novelty.** Row 7 records `A(F)` "never constructed from the books" and the cross-fiber
  correspondence "underived"; row 6 records the correct one-place objects as unpinned; P2 names the
  missing datum without naming its geometric support. The new step is the identification: *the
  missing datum is the direct image of branch data along book-enumerated dicritical divisors, with
  the Keller two-form supplying one exact pinned invariant (`a_E`) per divisor.* It also gives
  `G2-PSC` fidelity its first receiver semantics (P-1).
- **New evidence used.** P2's exact equivalence + principal-part formula + 84/168 collision
  (producer-checked); P1 COSTUME closing raw-passport alternatives (producer-checked + coordinator
  replay); promoted controls (pure-boundary identity, Hénon tower, class-kill family). The D result
  is *not* consumed. Jelonek/Chau structure statements are [LIT] and re-verified in-lane before any
  use beyond motivation.
- **Dependencies / tiers.** Stage 0 re-derives P2's conditional algebra and the localization
  lemma independently inside the lane (it is a half-page of Newton identities over a DVR plus
  `A = ∩ A_p`), so the lane does not consume the unreviewed P2 proposition as a premise; the
  collision example is re-run exactly. Books = promoted internal artifacts. Everything produced is
  INTERNAL-UNREVIEWED until different-model review.
- **Cheapest discriminator.** Stage 0 (≤ one session): verify polar-support = `A(F)` on the four
  exact controls with Card 3's instrument (automorphisms: empty `A(F)`, zero principal parts;
  `(x²,xy)`: `A(F)={u=0}`, `PP Tr(y²)=2q²/t`; class-kill: non-Keller behavior). Stage 1 (≤ 6h):
  parse one certified residue-A book to dicritical tags with `a_E`, write the `m≤2` convolution
  unknowns, and test determination vs. persistent `b`-type freedom.
- **Outcomes and interpretation.** (a) Book data + `J=1` pins the `m≤2` convolutions → candidate
  separating identity; package the *smallest* claim for hostile review; boundary packets are
  potentially sufficient and P-1 collapses to a theorem obligation. (b) Freedom persists → exact,
  named insufficiency fingerprint: the precise valuation datum absent from every current packet;
  feeds `PSC-FINGERPRINT` as registered and licenses Card 2's search space as genuinely open.
  (c) A control fails the formula → an error in P2 found; urgent input to the running P2 review.
  (d) The book cannot be parsed to tags → `SCHEMA-ONLY`; names the concrete transport gap.
  Every branch is actionable; none promotes a claim.
- **Cost/time.** Days; exact CAS (SymPy/Singular) locally; no fleet; no held item touched.
- **Stop condition.** Hard stop at the stage-1 verdict or 6h/stage; no trace "engine," no
  positivity/finiteness program, and no band/depth work regardless of outcome.
- **Expected information gain.** High: decides whether the boundary program has a receiver, or
  states exactly what is missing — the first exact yes/no on packet sufficiency after the P2
  collision made the question well-posed.
- **Resurrection trigger.** If stopped on (b): resurrect when any packet schema carrying
  coefficient-level data exists. If the P2 review refutes the algebra: rebuild stage 0 on the
  corrected statement before anything else.

### Card 2 — realize-or-refute: pole-surviving dicritical local models

Covers: **strongest counterexample/falsification attack** (two-sided by construction).

- **Target claim.** [EXP] In a bounded complexity class (mirroring P2's collision class:
  denominator ≤ 42, ≤ 4 characteristic pairs, bounded coefficient support), either exhibit an exact
  char-0 local model — a one-place-parametrized candidate `A(F)` component with completed branch
  package — satisfying every *provable* Keller boundary constraint (`a_E` pinning, two-form
  pairing, semigroup admissibility, exactness of the untwisted action forms per P1) while retaining
  a nonvanishing `m ≤ 2` trace principal part; or prove the class empty, which is a bounded
  separating identity — the exact lemma P2 could not find from contact data alone.
- **Avenue IDs.** 7, 6; 33's residue machinery as tooling; 4-adjacent only in that promoted
  A-SCALE formal escape families serve as honest *controls* (single-model tier, flagged). This is
  **not** the held generic sparse search (row 36): it searches structured local divisor data under
  exact admissibility constraints, not Keller-map coefficient space.
- **Novelty.** First CE-side use of the trace receiver: it converts "counterexample hunt" from a
  held global search into a local, exactly constrained existence question whose *negative* answer
  is itself the proof-side lemma. The P2 `b`-slot is the seed degree of freedom.
- **New evidence used.** P2 collision and formula (producer-checked, re-derived via Card 1 stage 0);
  P1's exactness facts for untwisted forms (producer-checked); promoted controls.
- **Dependencies / tiers.** Depends on Card 1 stage 0 (the constraint list must be written exactly
  before searching); INTERNAL-UNREVIEWED outputs; a "survivor" is explicitly **not** a
  counterexample — no global map exists, no germ or char-0 point is inferred, and no modular jet is
  consulted.
- **Cheapest discriminator.** Exhaustive exact scan of the smallest admissible class; the first
  survivor or the emptiness certificate for that class is the answer.
- **Outcomes and interpretation.** (a) Survivor → a concrete local obstruction to the proof route
  and a template for any future global realization hunt; triggers a full round; still zero
  implication for JC2's truth. (b) Class empty → bounded separating identity candidate; package for
  review; suggests induction on complexity and directly repairs P2's `INSUFFICIENT-DATA` from the
  Keller side. (c) Constraints cannot be written exactly → names the missing local theorem; pairs
  with Card 1 outcome (b) as the same fingerprint seen from the other side.
- **Cost/time.** Days; exact local CAS; no fleet.
- **Stop condition.** Complexity cap fixed in advance; 6h per stage; no class enlargement without a
  recorded reason; no global gluing attempt without independent review of a survivor.
- **Expected information gain.** High either way: the proof consensus currently has no
  Keller-specific reason trace poles cannot survive, and the CE side has no local model — one
  bounded computation removes exactly one of those two ignorances.
- **Resurrection trigger.** If stopped empty at the cap: resurrect one tier up only after review
  and only if Card 1 outcome (a) failed (a pinned identity would make larger tiers moot).

### Card 3 — `trace_atlas`: exact `A(F)` + principal-part instrument

Covers: **software acceleration / decisive experiment**.

- **Target claim.** [EXP/tool] A reusable exact calculator that, for any explicit polynomial pair,
  computes: the characteristic polynomial of multiplication by `x`, `y` via bivariate resultants;
  the polar affine divisors (an exact `A(F)` equation as denominator support); and `PP_C Tr(z^m)`
  for `m ≤ 3` at each polar divisor via divisor-local expansion — pure exact arithmetic, no
  numerics, preregistered controls.
- **Avenue IDs.** 7 and 31 (primary); accelerates 25/26's future coupled CSP; instrument for
  Cards 1–2. Tool tier per COORDINATION: INTERNAL-UNREVIEWED until smoke-tested and reviewed.
- **Novelty.** Row 7 records that `A(F)` has never been constructed in-campaign; this is the first
  direct constructor, and it makes P2's audit repeatable on arbitrary specimens (external systems,
  class-kills, future candidates) rather than a one-off.
- **New evidence used.** P2's frozen `results.json` and control tables as the byte-stable
  regression target; promoted Hénon/tame controls; the `(x²,xy)` nonproper control.
- **Dependencies / tiers.** None mathematical; engineering only. Its outputs never license an
  inference — it is a measurement device.
- **Cheapest discriminator.** Byte-stable replay of P2's tables plus the four controls:
  automorphisms must return empty `A(F)` and zero principal parts; `(x²,xy)` must return
  `{u=0}` and `2q²/t`.
- **Outcomes and interpretation.** Pass → instrument available to Cards 1–2 and all future explicit
  specimens. Fail on a control → either a tool bug or an error in P2's tables; the latter is urgent
  input to the running review.
- **Cost/time.** ~1 day. Degree-42+ Hénon full resultants may exceed local budget: the registered
  fallback is divisor-local slices (specialize one target coordinate transversally) — bounded and
  exact; heavy-degree full mode only ever on box01 with authorization (none requested now).
- **Stop condition.** Stop at control-suite verdict; no feature growth beyond `m ≤ 3` and divisor-
  local mode.
- **Expected information gain.** Multiplicative: every later lane that touches traces, `A(F)`, or
  packet sufficiency reuses it; also the cheapest independent cross-check of P2 while its review
  runs.
- **Resurrection trigger.** Not applicable (instrument); revisit heavy-degree mode only when a
  specimen requires it.

---

## 4. Major-lane calls

- **D-series: CONTINUE, unchanged scope.** `D2-CELL26` runs as the sole child under its registered
  stops (derive the six band-26 compatibility functions from source, stratify the rank-4 pivot,
  saturate by cell units, decide the compatible base locus; stop before band 28 and before
  D43/integral work). No new depth, no B=168/D75, no integral engineering before D-1's verdict plus
  review. Outcome triggers: empty compatible base locus → decisive modular route-kill for this
  chart/fiber, full round; nonempty typed stratum → review, then and only then queue the
  common-integral question; inconclusive → redesign, not extension.
- **GGV/Sigray: CONTINUE the fork discipline; REDESIGN the PSC sub-lane.** Keep the fork explicit
  (hybrid owes `G2-PSC`; pure Sigray cannot import GGV restrictions and owes choice independence
  and complete landing/coverage). Redesign: adopt the trace receiver as the fidelity criterion —
  a packet/tree schema is sufficient only if it determines trace principal parts — so the queued
  `PSC-FINGERPRINT` becomes "exhibit or refute determination," which Card 1 stage 1 starts. No new
  book cells (hold respected).
- **Boundary/trace: REDESIGN (already half-executed by events).** P1's COSTUME stops all raw
  presentation-dependent passports at tested scope (pending its running review); P2's registered
  `INSUFFICIENT-DATA` stop fired, so no trace engine. The continuation is the dicritical
  direct-image/tagged-pairing program (Cards 1–3), which is a different object: divisor-supported,
  coefficient-level, receiver-tested — not another raw invariant under a new name.
- **Local bound programs (DIR/KJN/A-SCALE/G2-BD): CONTINUE as controls only.** No new census
  (held), no unrestricted UCD/K2C, no standalone sublinear-type hunt; KJN stays type-relative;
  the formal escape families serve as adversarial controls for Cards 1–2.
- **External-artifact work: CONTINUE, bounded.** Let the running Grok review land; keep the
  three-edge provenance vocabulary (correctness / coordinate equivalence / lineage) and the
  unchanged public perimeter (conditional on the GGV reduction/transcription bridge). Close Guo's
  Sage-container replay gap once, when cheap, within the documented 30 GB bound — a coordinator
  resource decision, not urgent. No author contact, no public wording change (held).

---

## 5. Shared hidden assumptions (explicit)

1. **Landing completeness.** Nearly all boundary work implicitly assumes a counterexample must land
   in the books' normalization; complete landing/coverage is unproved (P-2). My Card 1 inherits a
   bounded form: the dicritical census over a given affine curve must be complete on the chosen
   resolved model — flagged as an in-lane proof obligation, not assumed.
2. **Finite-packet sufficiency.** The whole boundary/trace program assumes *some* finite tagged
   packet determines the needed arithmetic. P2 proved the current packet insufficient; it did not
   prove any finite enrichment sufficient. Card 1(b)/Card 2(c) are the honest failure modes.
3. **Attention-allocation bias toward the D tower.** Everyone correctly disclaims that MOD-p jets
   imply nothing char-0, yet the portfolio's CE-side attention keeps concentrating there because it
   is measurable. The reviewed one-band result is consistent with the tower dying at D2; orthogonal
   CE capacity (char-p, Card 2) should not wait on it.
4. **Model correlation.** Four of five prior-round ideators were Codex-family; the boundary-
   invariant consensus that P1 then costumed is a documented instance of correlated enthusiasm.
   Convergence across this round's submissions should again be treated as weak evidence.
5. **Reorganization = progress.** My own frame assumes that restating properness as divisor-local
   arithmetic is traction. Logically it is an equivalence (P2 said so at full scope); the claimed
   gain — finite exact data per divisor, rigid carriers, book access, a pinned `a_E` — must prove
   itself at Card 1 stage 1 or the frame is `J=1` in costume too.
6. **External corroboration ≠ independence.** SuperMind/Guo share the GGV reduction, the degree-21
   core, the exact quintic, and a model family; treating them as two votes would double-count one
   lineage (E's own warning, kept).

---

## 6. Strongest hostile attack on my leading proposal (Card 1)

The localization is classical (Jelonek 1993; Chau's Keller-map papers), and the campaign already
recorded its operational core in rows 6/7 — including exactly where it stalls: *place data
unpinned, cross-fiber correspondence underived*. The attack: Card 1 re-derives known structure with
new vocabulary and stalls at the same wall, because (i) `a_E ≥ 0` pins ramification but not
coefficients, and P2's `b`-slot sits *above* the last characteristic exponent — plausibly above
anything any tree decoration pins, so stage 1 likely returns "freedom persists," which is just
P2's `INSUFFICIENT-DATA` with extra steps; (ii) the receiver needs the branch census over each
candidate divisor to be complete, which smuggles landing/coverage (assumption 1) back in; (iii) the
moment bound `m ≤ d` is unbounded, and the escape — "kill the divisor, not the moments" — requires
a rigidity theorem for one-place curves that forty years of AM-era work did not produce; (iv) the
evidentiary base is producer-checked P1/P2, both under running review — a refutation of either
drops the frame's premises. Mitigation, not rebuttal: every stage is a cheap two-sided
discriminator with hard stops, outcome (b) is *designed* to be valuable (an exact fingerprint of
what no packet carries), and stage 0 independently re-derives the borrowed algebra before anything
depends on it.

---

## 7. Events that would invalidate this ranking

- The running **P2 review** refutes the conditional algebra, the localization, or the 84/168
  collision → raises on 6/7/25/31 and Cards 1–3 lose their basis; restore the 00:35Z ordering.
- The running **P1 review** refutes COSTUME → un-lower 33; raw passports revive at reviewed scope.
- **`D2-CELL26`** returns an empty compatible base locus (D-series CE lane collapses at this
  chart/fiber; shift CE weight to 19/Card 2) or a large coherent stratum (D-series rises; the
  integral-bridge bottleneck D-3 activates).
- The running **external-intake review** finds `FAIL-IDENTITY` or collapses the lineages into one
  (changes the (72,108) support posture and P-5's urgency).
- Any credible external proof/counterexample announcement, or refutation of a promoted control
  (pure-boundary identity, Hénon tower) — trivially resets everything.

---

## 8. Proposed four-root portfolio (legal under current constraints)

Respects: at most four roots including coordination; at most one unreviewed dependency generation;
background review running (P1, P2, external intake) with no root blocked on it; all holds (B=168,
D75, new book cells, DIR/A-SCALE census, cCa6 F4, HC4 expansion, generic sparse search, public
wording/author contact, msolve upstream); and the already-running sole D child. No heavy compute.

| Root | Work | Unreviewed-premise exposure |
|---|---|---|
| **C — coordinate/harvest** | Absorb the three pending review verdicts as they land, propagate through the claim DAG, keep clocks, trigger the next round on any decisive gate. | none |
| **D — running sole child** | `D2-CELL26` continues untouched under its registered stops; no sibling, no depth, no integral work; harvest + different-model review of whatever it returns. | none new (rests on promoted D25 plus the reviewed one-band scope) |
| **P — trace receiver (Cards 1+3, then Card 2 as stage 2)** | Stage a: build `trace_atlas`, re-derive the P2 algebra + localization in-lane, verify controls. Stage b: one-book determination probe. Stage 2 (only after a stage-b verdict, same root, handoff): realize-or-refute pole-surviving local models. Producer: this lane; reviewer: a non-Codex different model for any candidate claim. | ≤ 1 (P2, producer-checked), and stage a's independent re-derivation is designed to retire even that before stage b consumes it |
| **X — char-p Witt refinement (row 19)** | Registered G17(i)–(iii) extension: F3/F5 low-support collision search, keep W2-survivors; strictly bounded enumeration sized to local CPU; explicitly distinct from the held char-0 generic sparse search. Any survivor is a claim for hostile review, not a lift. | none (consumes promoted char-p artifacts only) |

Discipline: P's stage 2 may not consume an unreviewed stage-b candidate (a `CANDIDATE` at stage b
suppresses stage 2 and goes to review first — same suppression rule the 00:35Z portfolio used).
Two consecutive non-informative attempts on any representation force redesign. At most one
extension of ≤ 6h per root, with artifact + sharp question + completion estimate. Rebalance at the
first decisive gate — expected to be `D2-CELL26` or P stage b — not at the timer.

**Bottom line.** The round's deltas do not move JC2's truth status; they move its *architecture*.
P2 made packet-sufficiency a measurable property and the collision proved the current packet fails
it; Jelonek's localization says the failure lives on book-enumerable one-place divisors; P1 cleared
the costumed alternatives out of the way; the D tower is now one running, well-gated child. The
correct spend this cycle is one proof-side receiver test, one two-sided local realize-or-refute,
one instrument, and one orthogonal char-p lane — all cheap, all exact, all with named reviewers and
hard stops, none consuming an unreviewed verdict.
