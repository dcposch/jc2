# Blind whole-portfolio ideation — Opus 5 — round 20260829T1224Z

## 0. Identity, basis, and verified inputs

- **Model identity:** Opus 5 (`claude-opus-5`), blind lane, no peer submission read.
- **Clean basis:** `ccb6cd52eeab95f169b40f0a48668c3acd7a607e` (verified `git rev-parse HEAD`).
- **State packet:** `xmodel/ideation-20260829T1224Z-state-packet.md`
  - full file: `f79671cf460240ce6e200ccca30a34e65b90e305f15f5c636f7262f73db86baa` — **VERIFIED**
  - body (first 8546 bytes): `f33cd9786a1bfd914c9253addd951532af3cd359a600da212209984aa6562783` — **VERIFIED**
- **Canonical files, all eight hashes recomputed and matching the packet:**

```text
0ab0a8c643607526c12b33ffc762f91f680d4ada820415441e6d71dbab9c6b17  COORDINATION.md
701feb58eaee99a53e024dc57dfd024f24c20fe985124224ed52a29cdc0da493  APPROACHES.md
a058aad4b2faa1a235a9d31903844e12594428045e3e7c76d05f23a7423de9fd  AUDIT.md
1a0d5fc7445ed662a50fe99fe53702b7f3d41aaf14c432aea5405f536a5f4708  PROGRESS.md
a2f49415ddf72edb62fc4a86c3628a708b9e488e6b2f2871fc1b5117b53bfc80  notes.md
29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b  ladder/REDUCTION.md
b2b85ef6e4c2204ae3318089204c08ae077bf091f0165da0531f9d55e35b4d26  ops/FLEET.md
c63bd1673b2b180173799f5bee07f7fc0e51047945a41010a28a0aeeeeb92253  FALLACY.md
```

- **Additional source files inspected at basis (read-only):** `ladder/SHEET6-MULTIPOLE.md`
  §1 and D4–D6, `ladder/SHEET6-DEPTH.md` §(MP4 quote), `ladder/SHEET6-AF3.md`,
  `ladder/SIGRAY-AUDIT.md`, plus targeted history greps recorded in §3.4.
- **Compliance:** no other current-round lane artifact read; no web; no heavy
  computation; no file modified; `jc2-lean` neither entered, listed, read,
  statused, built, nor modified. Exactly one file written: this report.
- **Exit-claim declaration:** this report makes **no** new exit/first-separation
  charge claim, so no `charge_basis` line is required or supplied. Where an exit
  floor is cited it is the promoted law (`delta` if integral, else `ceil(2*delta)`),
  cited as an input, not re-derived.

### 0.1 Lifecycle/scope labels used below

Evidence tiers: `PROVED` (unconditional mathematics, producer-checked here),
`CLASSICAL` (standard external theorem, no campaign proof needed but a source
check is named), `EXACT-CONDITIONAL` (exact given a named promoted input),
`CONJECTURE`, `EXTRAPOLATION` (moral of a promoted result carried to an
unproved neighbouring regime). Lifecycle for everything originating in this
report is `DRAFT` or `PRODUCER-CHECKED`; nothing here is `PROVISIONAL` or
`PROMOTED`. Where I cite campaign results I mark them `PROMOTED`,
`PROVISIONAL`, `FORMAL`, `BOOK-RELATIVE`, or `REFUTED` as the ledgers do.

---

## 1. Disposition vector over `APPROACHES.md` avenues 1–46

Baseline is the 46-row historical inventory as modified by the live overlays.
Default is `unchanged`; only the four changes carry reasons.

| # | Avenue (short) | Disposition |
|---:|---|---|
| 1 | GGV corner families + degree farm | **raise** |
| 2 | Sheet-number ladder / Sigray–Orevkov (principal) | unchanged |
| 3 | Vertex-gap / strip ODEs / residue functional | unchanged |
| 4 | Formal-germ certification + algebraization (D-series) | **lower** |
| 5 | Jung–van der Kulk degree descent | unchanged |
| 6 | Abhyankar–Moh one-place | unchanged |
| 7 | Nonproperness / Jelonek `A(F)` | unchanged |
| 8 | Formal-inverse combinatorics (BCW tree) | unchanged |
| 9 | Lee–Li Conjecture E | unchanged |
| 10 | HC4 => JC2 Hessian bridge | unchanged |
| 11 | Mathieu / GMC / Zhao ladder | unchanged (refuted) |
| 12 | Face isolation / p-adic multinomials | unchanged |
| 13 | Dixmier DC(2) | unchanged |
| 14 | End(A_1) / Zheglov audit | unchanged |
| 15 | Spectral surfaces / commuting PDOs | unchanged |
| 16 | D-module / holonomic index | unchanged |
| 17 | BCW / Druzkowski / Yagzhev stabilization | unchanged |
| 18 | Graded / equivariant / GIT | unchanged (closed) |
| 19 | Char-p counterexamples + Witt lifting | unchanged |
| 20 | Reduction mod p / p-curvature | unchanged |
| 21 | p-adic injectivity / Hensel | unchanged |
| 22 | Diophantine integral points / heights | unchanged |
| 23 | Analytic global inverse / Hadamard | unchanged |
| 24 | Real JC / Pinchuk | unchanged |
| 25 | Fiber monodromy / dessins / passports | unchanged |
| 26 | Primitive-monodromy bound on `td` | unchanged |
| 27 | Links at infinity / splice diagrams / plumbing | **reopen (narrow)** |
| 28 | Log surfaces / BMY / log-Kodaira | unchanged |
| 29 | LND / Hamiltonian-derivation completeness | unchanged |
| 30 | Affine-surface classification / ML invariant | unchanged |
| 31 | Integrality / ZMT / Rees valuations | unchanged |
| 32 | Off-diagonal collision ideal / injectivity | **raise** |
| 33 | Global symplectic exactness / action residues | unchanged (`COSTUME`) |
| 34 | 2D tangent sweep / pole removal | unchanged |
| 35 | Descent of dim>=3 counterexamples | unchanged |
| 36 | Guided CE search (SAT / sparse / small heights) | unchanged |
| 37 | Finite-field census | unchanged |
| 38 | Tropical geometry | unchanged |
| 39 | Cohomological cluster (K2/motivic/Hodge/prismatic) | unchanged |
| 40 | Free-associative / noncommutative Jacobian | unchanged |
| 41 | Naive scaling deformation | unchanged (falsified) |
| 42 | Markus–Yamabe / Hurwitz | unchanged |
| 43 | Ritt decomposition | unchanged |
| 44 | Moskowicz "no prime td" | unchanged (`REFUTED-AS-PROOF`) |
| 45 | Differential Galois / Liouvillian | unchanged |
| 46 | Lean / AI formal certification | unchanged, **`NOT_INSPECTED`** this round |

**Reasons for the four changes.**

- **1 `raise`.** Not because the farm is closer to emptying anything. Because
  avenue 1 owns the *only degree-pinned branch of the whole problem*, and §3.1
  shows that branch carries an unconditional Bezout ceiling `td <= 7776` and an
  exact bridge `td = deg f * deg g - Sum_p i_p` from boundary data to `td`. The
  farm's cell data should be re-mined for `Sum_p i_p`-relevant boundary
  content, not only for emptiness verdicts. Evidence tier of the reason:
  `CLASSICAL` + `EXACT-CONDITIONAL` on GGV22.
- **4 `lower`.** The promoted own-order absorption identity plus the
  provisional cascade result show that in the type-`(2,3)` regime an explicit
  g-side response absorbs every formal Keller row through `s<=i`, so a formal
  jet/depth-window envelope produces no kill. The D-series' persistent
  nonemptiness at every depth is exactly the same phenomenon seen from the
  other side. This is `EXTRAPOLATION`, not a theorem about the D-series, and I
  lower strategic weight only, not any banked D-series claim.
- **27 `reopen (narrow)`.** Reopened *solely* as a calculator for the boundary
  intersection deficit `Sum_p i_p` of §3.1, which the link-at-infinity/splice
  data determines without any realizability input. The avenue's recorded
  stuck-point ("admissible diagram != algebraically realizable") does not bind
  a pure arithmetic-identity use. This is **not** a reopening as an exclusion
  engine, and it needs one external source check at the next sweep.
- **32 `raise`.** The row's own complaint is that the promoted three-generator
  accelerator `I:Delta = I:Delta^inf = I + (det A)` "needs a named bounded
  family or source-derived saturated boundary datum" — i.e. it lacks a client.
  §3.3 supplies two clients that need neither: a pure-dimension/smoothness
  discriminator (`dim Off in {empty, 2}` exactly, `Off` smooth) usable as a
  cheap fail-closed test on any explicit candidate, and a non-circular `td`
  instrument. Raise is narrow: avenue 32 remains not a proof route.

**Guardrail respected.** The 09:35Z overlay forbids raising avenues 25, 26, 28,
31; I raise none of them. My §3.1 item is a Bezout/degree fact and supplies
neither target inertia, nor a type menu, nor a positive Euler decomposition,
nor a component-labelled `A(F)` packet, so it does not license those raises.

---

## 2. Reranked bottlenecks

### 2.1 Proof-side bottlenecks (reranked)

1. **`CRITICAL 4`/`CRITICAL 5` — no full-configuration landing theorem and no
   off-axis completeness certificate.** Unchanged at #1. Everything the campaign
   proves is `BOOK-RELATIVE` until this closes. The round's own evidence
   sharpens *why*: the codomain provably cannot be a finite literal-cell list
   (U1 semilinear families; U2 one-P0 bilinear family), so the obligation is now
   a **record-language** obligation, not an enumeration obligation. §3.2 is my
   attack on exactly this.
2. **`HIGH 3` — Sigray §§7–9 source trust. Promoted from #4 to #2.** This is a
   fanout x fragility judgement, per `COORDINATION.md`'s own priority rule.
   Every recent charge, mass, and budget theorem rides on §§8–9, and in the last
   48 hours §§8–9 produced: the withdrawal of `min(num(delta),2*ceil(delta))`;
   a `FAIL` on the merge-free/`V_{2,a}` composition; a missing `notin` in a
   frozen review summary; plus the earlier Prop 4.2, Prop 5.1, and Lemma 6.1
   repairs. The rollback cost of a §8/§9 error is now larger than the rollback
   cost of any single route kill. Nothing else in the campaign has this
   combination of universal consumption and demonstrated instability.
3. **`CRITICAL 7` — the `td` ceiling. Demoted from "absolute blocker" to
   "branch-specific", and simultaneously corrected.** See §3.1: the canonical
   sentence "no upper bound on `td`" (`AUDIT.md` `(G5)`; `ladder/REDUCTION.md`
   `CRITICAL 7`) is true only on the `deg >= 125` branch of the GGV22 dichotomy.
   On the `(72,108)` branch Bezout gives `td <= 72*108 = 7776` unconditionally.
   The genuine infinitude in `CRITICAL 7` lives entirely in one branch.
4. **`G2-PSC`. Demoted to #4.** The pure-Sigray architecture bypasses it at the
   price of its own source theorem, and the campaign has in fact been running
   pure-Sigray for weeks. It should stop being scored as a blocker of the
   *active* route and be scored as a blocker of the *hybrid* route only.
5. **`HIGH 1`/`HIGH 2` — composite single-pole and on-axis survivors.** Real but
   downstream: closing them closes nothing that is not already book-relative.
6. **`CRITICAL 2` — the existential quantifier in GGV minimal selection.** Low,
   because a proof by contradiction only needs the selected pair; I keep it on
   the list because §3.1's ceiling is stated for the *selected* pair and
   inherits exactly this quantifier.

### 2.2 Counterexample/falsification-side bottlenecks (reranked)

1. **No characteristic-zero bounded seed with a completed obstruction ledger.**
   K00 is protected; the char-p lane has proved its studied family's limit is
   restricted-analytic, not polynomial. The bottleneck is *mechanism*, not
   compute: nothing converts all-Witt-level liftability into polynomiality.
2. **The off-scheme has no named bounded family** (avenue 32's own diagnosis).
   Newly #2 because §3.3 gives the first *cheap* falsification instrument that
   needs no such family: dimension and smoothness of `V(I + (det A))`.
3. **The degree-twelve frontier of the hypothetical AS109 lift.** Unchanged.
4. **Guided search (36).** Unchanged and still buried under the GGV cutoff.
5. **`A(F)` construction debt.** Unchanged; the ACS covering lemma is
   infrastructure, and `ACS-CEIL`/`TDIC-SET` are correctly stopped.

---

## 3. New avenue, new mechanism, new connection

### 3.1 New connection (primary): the Bezout deficit at infinity is the missing bridge between avenue 1 and avenue 2 — and it corrects `CRITICAL 7`/`(G5)`

**Statement (tier `CLASSICAL`, producer-checked here).** Let `F = (f,g)` be
dominant with `J(f,g) = 1`. For generic `q = (q1,q2)`, the fibre is the
intersection of the affine curves `{f = q1}` and `{g = q2}`. Because `J` is a
nonzero constant these intersections are all transverse, so projective Bezout
in `P^2` gives the **exact identity**

```text
   td  =  deg f * deg g  -  Sum_{p in L_infty} i_p( closure{f=q1}, closure{g=q2} ).
```

In particular `td <= deg f * deg g`, unconditionally.

Controls I ran at desk (all consistent): `(x,y)`: `1*1 - 0 = 1`. `(x, y+x^2)`:
`1*2 - 1 = 1`, the single infinity point `[0:1:0]`. `(x, y+x^3)`:
`1*3 - 2 = 1`.

**Campaign consequence, and the correction.** `ladder/REDUCTION.md`
`CRITICAL 7` says the GGV22 dichotomy "says nothing that truncates topological
degree", and `AUDIT.md`'s foundations entry records "`(G5)` NO upper bound on
`td`" without qualification. On the `(72,108)` branch this is **wrong**:
degrees are pinned, so

```text
   td  <=  72 * 108  =  7776,      and      Sum_p i_p  =  7776 - td.
```

Both statements inherit GGV22's existential selection (`CRITICAL 2`), which is
exactly the quantifier a proof by contradiction may use. The honest replacement
for `(G5)` is: *no upper bound on `td` is known on the `deg >= 125` branch; on
the degree-pinned branch the bound is `7776`.*

**Why this is a bridge and not a curiosity.** `Sum_p i_p` is a boundary
invariant. It is computable, in principle, three independent ways: from GGV
corner/chain data (avenue 1), from the link at infinity / splice diagram
(avenue 27), and from the Sigray pole tree (avenue 2). Three independent
computations of one integer is a cross-avenue consistency instrument of exactly
the kind `FALLACY.md` exists to enforce. And it runs in the *useful* direction:
a boundary-side **upper** bound on `Sum_p i_p` becomes a **lower** bound on `td`
for the degree-pinned branch, which is the one quantity the campaign has never
been able to bound from below by a source theorem.

Numerically: `{h=0}` on `L_infty` has at most `gcd(72,108) = 36` distinct points
(with `deg h = 36` and leading forms proportional to `h^2`, `h^3`). So a
`(72,108)` counterexample with `td <= 14` requires `Sum_p i_p >= 7762` spread
over at most 36 points, i.e. mean local intersection multiplicity `>= 215.6`.
That is a very strong, entirely arithmetic, desk-checkable demand on the
boundary data the campaign already computes.

**The sharp sub-observation (tier `EXACT-CONDITIONAL`, one source check
pending).** `ladder/SHEET6-MULTIPOLE.md` §1 fixes the Sigray type by
`2 <= alpha < beta`, `gcd(alpha,beta) = 1`, global by Lemma 2.1, and D4 derives
`deg p / deg p_g = alpha/beta` at poles. `72 : 108` reduces to `2 : 3`.
Therefore, **if** pole order equals degree in the normalized frame (the one
step I have not verified against the source), the GGV `(72,108)` branch **is**
a type-`(2,3)` Sigray configuration — and `(2,3)` is the *minimal* type allowed
by `2 <= alpha < beta`, `gcd = 1`. The campaign's entire current
type-`(2,3)` td12 lane (`r = 3i/2`, three `(1,2,3)` pole entries, the B25/S17
routes) would then be running on precisely the degree-pinned branch, which is
the branch that carries the Bezout ceiling.

**Novelty.** `td = deg f * deg g - Sum i_p` is textbook. The campaign use is
new to the ledger: zero occurrences of `7776`; zero hits for `td <= deg`,
`upper bound on td` outside the flat `(G5)` denial; the only Bezout-at-infinity
count in `xmodel/` is the `(8,28)` place count `56+16=72`, a different object.
The type-`(2,3)`/`(m,n)=(2,3)` identification is kept notationally *separate* in
`ladder/REDUCTION.md` §0 ("The symbols `(m,n)` are reserved for GGV's coprime
degree-ratio parameters") and is nowhere asserted.

### 3.2 New mechanism: `LIPSHITZ-CODOMAIN` — the landing compiler's record language is the existential theory of addition **with divisibility**

**The problem it addresses.** `CRITICAL 4`/`CRITICAL 5` now read: "the minimally
plausible codomain is a finite exceptional residue plus normalized *family
records*." The campaign has three data points about that language:

- U1 equal-arrival merges are labelled arithmetic-progression families
  (semilinear) — `PROMOTED`;
- Q+E5 at a fixed certified state is a finite integer menu plus an exact
  no-partition `R2.2` existence predicate — `PROMOTED`;
- the U2 one-P0 family is semilinear for each fixed `t = 5 mod 6`, but the
  two-parameter union is **provably not** semilinear: `nu = tK` has unbounded
  gaps `72,144,216,...` — `PROMOTED` (this is the witness in the stable Opus
  review of the semilinear family record).

The campaign has read the third fact as a *defeat* for a uniform record
language. **It is not.** It is a defeat for Presburger/semilinear only.
`nu = tK` with `t`, `K` both free is exactly one divisibility atom:
`t | nu  and  nu/t = K`. Products of free variables are precisely what the
divisibility predicate buys, and precisely where the decidability frontier sits.

**The mechanism.** Adopt as the compiler's target logic the **existential
fragment of `<Z, +, <, |>`** — Lipshitz's theory of addition and divisibility,
whose `exists`-fragment is decidable (Lipshitz, *The Diophantine problem for
addition and divisibility*, TAMS 1978; complexity refined in the
Lechner–Ouaknine–Worrell and Bozga–Iosif lines). Under this reading:

- every reviewed record family so far is a formula in the fragment;
- every campaign divisibility side-condition (`3|M`, `M_H | b_P`,
  `dq = 1 mod nu`, `M_G = gcd(...)`, `gcd(M_G,nu)=1`) is a native atom;
- the promoted exit floor is in the fragment: `delta = D/m - kbar` is integral
  iff `m | D - m*kbar`, and `ceil(2*delta)` is a bounded case split;
- a `NUCAP`-style numerical cap becomes provably unnecessary *inside* the
  covered fragment, and an `OPEN`-dropping enumerator becomes a detectable
  soundness bug rather than a silent one.

**What it does and does not buy.** It buys a *fail-closed coverage certificate*
by entailment check instead of by enumeration — which is exactly the fifth
requirement `CRITICAL 4` lists and the one no current artifact supplies. It
does **not** buy a `td` ceiling: `exists`-definable subsets of `N` in this
fragment need not be eventually periodic (the composites are definable). I
state this explicitly so the mechanism is not oversold into `CRITICAL 7`.

**Novelty.** Zero hits for `Lipshitz`, `Semenov`, `quantifier elimin` across
`xmodel/`, `avenues/`, `ladder/`, `cases/`, `refs/`, `papers/`, and the
top-level ledgers. `Presburger` occurs twice and only as (a) a narrow *local
chamber restatement* in the `max12` V48 compiler, explicitly firewalled to
sixteen registered rays, and (b) my own earlier use of semilinear closure as a
*refutation* tool. Nobody has proposed a decidable target logic for the landing
compiler, and nobody has noticed that the campaign's own non-semilinearity
witness lands inside Lipshitz's fragment rather than outside every fragment.

### 3.3 New mechanism (secondary): `OFF-DIM2` — the off-scheme has forced pure dimension two

**Statement (tier `PROVED` from banked inputs, producer-checked here).** Let
`F` be Keller over `C`, `X = A^2 x_{A^2} A^2`, `Off = X \ Delta` with ideal
`I + (det A)` (the promoted accelerator). Then:

1. `F` etale + target separated => `Delta` is a **clopen** subscheme of `X`
   (already banked, in `xmodel/secant-projective-review-grok-20260824.md` §"Affine
   non-contact is general" and the `secant-idempotent` review, and externally in
   `jacobian-collision-geometry`);
2. hence `Off` is a *union of connected components* of `X`, and since both
   projections `X -> A^2` are etale, **`Off` is smooth of pure dimension two**;
3. hence the first projection `Off -> A^2` is etale with generic fibre
   cardinality `td - 1` (the banked AS109 tube count `109*108` is this identity
   in the formal-tube frame).

**Consequences that are cheap and decisive.**

- `dim V(I + (det A)) in {empty, 2}` **exactly**. A component of dimension `0`
  or `1` refutes the configuration outright. This is a one-line addition to
  every collision computation the campaign already runs.
- `V(I + (det A))` is **smooth**. A singular point refutes the configuration.
- `deg(Off -> A^2) = td - 1` gives a `td` instrument that does not read the
  boundary tree, and avenue 26's row flags the boundary identity
  `td = Sum e_S - b1 + 1` as *explicitly circular*. This is the first
  non-circular cross-check available to the ladder's `td` bookkeeping.
- Positive control exists: the characteristic-three Artin-Schreier collision is
  Keller with nonempty `Off`, so the instrument can be validated on a case where
  it must return "smooth, pure dimension two", not merely "empty".

**Novelty.** Ingredients 1 and 3 are separately banked (and item 1 is
externally published). The *composition* — pure dimension two plus smoothness
as a fail-closed discriminator, and generic projection degree as a `td` oracle —
returns no hits: `grep` for `off scheme|off-scheme|off closure` intersected with
`dim|smooth|surface` is empty across `xmodel/`, `avenues/`, `ladder/`, and the
top-level ledgers. I label this **sharpening of banked facts**, not a new
theorem, and flag it for the sweep since the external collision-geometry note
may already contain it.

### 3.4 Novelty-search record (so the claims above are falsifiable)

Searched at basis, `--include="*.md"` over `xmodel avenues ladder cases refs
papers` and the top-level ledgers:

```text
Favre / valuative tree / eigenvaluation  -> PRESENT and explicitly DECLINED
                                            (grok-lateral1/2). Not proposed.
Presburger                               -> 6 files; only local-chamber and
                                            refutation uses (see 3.2).
Lipshitz / Semenov / quantifier elimin   -> ZERO hits.
7776 / td <= deg / upper bound on td     -> ZERO relevant hits; (G5) flat denial.
Bezout (as td instrument)                -> ZERO; only certificate/Bezout-identity uses.
Nori / etale complement cover            -> PRESENT (my own 0002Z round; ACS banked,
                                            ACS-CEIL and TDIC-SET correctly STOPPED).
clopen diagonal                          -> PRESENT, banked and external.
off-scheme dimension / smoothness        -> ZERO hits.
```

I therefore claim novelty only for §3.1's campaign consequence and correction,
§3.2 in full, and §3.3's composition — not for any underlying classical fact.

---

## 4. Strongest attacks now worth running

### 4.1 Strongest proof attack: `SIGMA-INFTY-BRIDGE`

On the degree-pinned branch, compute `Sum_p i_p` from boundary data and confront
it with `7776 - td`.

Concretely, in three steps, all desk-scale:

1. Verify (or refute) the source step "pole order = degree in the normalized
   frame", which decides whether `(72,108)` is Sigray type `(2,3)`. One reading
   of `Not 2.4` / `St 5.2(i)` / `Lemma 2.1`.
2. If it holds: derive the boundary-side *upper* bound on `Sum_p i_p` implied by
   the promoted pole-mass floor and the `C7.1`/`St 9.4` budget at type `(2,3)`
   with `at most 36` infinity points.
3. Compare with `7776 - td`.

Why this is the strongest available proof attack: it is the only cheap move I
can find that produces a **lower** bound on `td` from source data. Every current
campaign inequality bounds `td` from below only via configuration complexity
(`td >= 3*max(beta,2alpha)`), which does not interact with the ceiling. This one
does, because it is an *identity*, not a floor. Either outcome is decisive for
strategy: a boundary cap below `7762` kills the whole `td <= 14` range on the
degree-pinned branch (and would explain why the low-`td` books keep producing
survivors rather than emptiness — they may be enumerating a branch that cannot
host the pinned case at all); no cap tells us the boundary machinery is much
weaker than the ladder's rhetoric implies, which is itself worth knowing before
another book is enumerated.

### 4.2 Strongest counterexample/falsification attack: `OFF-DIM2` sweep

Run the §3.3 discriminator over every explicit or semi-explicit object the
campaign holds: the AS109 formal-tube data, the D-series germ truncations at
their current depth, the K00 frame, and the GGV farm's non-empty leaves. For
each, compute `dim` and the singular locus of `I + (det A)` in the *declared*
ambient ring, with `sat()` handled per `FALLACY.md` (extract the ideal
component, assert the ring, run both controls).

Interpretation is sharp both ways. Dimension `0` or `1`, or any singular point,
is an immediate refutation of that object's Keller-ness — a genuinely new kill
mechanism that costs one Groebner computation. Uniform "empty or smooth pure
dimension two" is the expected outcome and converts the instrument into a
standing regression gate for the collision lane at negligible cost.

Positive control: the characteristic-three AS collision must return smooth, pure
dimension two, nonempty. Negative control: any deliberately perturbed
non-Keller pair must return something else. Without both controls the sweep is
not evidence.

---

## 5. Software acceleration / decisive experiment

**`SIGMA-INFTY-TRIPLE` — a desk-scale, exact, three-way computation of one
integer.**

Write one small exact script (pure Python + `sympy`-free integer/resultant
arithmetic; no CAS) that, for a supplied dominant pair `(f,g)` over `Q`:

1. computes `td` as the degree of the generic fibre (resultant / elimination),
2. computes `deg f * deg g - Sum_p i_p` by homogenizing and computing local
   intersection multiplicities on `L_infty`,
3. asserts the two agree.

Seed it with the controls of §3.1 plus a ladder of pairs with genuinely `td > 1`
(`(x^2, y)`, `(x^2, y^2)`, `(x^2 - y^2, xy)`, `(x^2 + y, x^3)`), which the
Keller hypothesis excludes but the *combinatorial* half of the ladder does not.

- **Placement:** desk. Degrees are tiny; no CAS, no AWS. Expected wall clock
  under five minutes to write and under one second to run.
- **Cost:** effectively zero. `ops/FLEET.md`'s hard rule is not engaged.
- **Decisiveness:** it validates step 2 of `SIGMA-INFTY-BRIDGE` before any
  effort is spent on the `(72,108)` boundary estimate, and it establishes the
  first independent `td` oracle in the campaign.
- **Named risk, stated up front:** if the ladder's `td = Sum e_S - b1 + 1`
  derivation *uses* `J = const`, then the non-Keller test pairs validate a
  different statement and the harness value drops to "validates the Bezout
  identity only". Determining which of the ladder's combinatorial identities are
  Keller-free is itself the first informative output.

I explicitly do **not** propose AWS work this round. Nothing here is heavy, and
the two open review debts (cascade theorem, LL1-R4 software) should be
discharged before any new compute commitment.

---

## 6. Campaign-systems card

**Verdict: `UPGRADE` (one, bounded).**

**`CHARGE-BASIS-LINT` — make `FALLACY.md`'s mandated exit-claim line
machine-checked instead of prose-honoured.**

*Evidence that this is the right target.* `FALLACY.md` already mandates exactly
one line per exit claim,
`charge_basis={"delta":...,"branch":...,"flag_count":...,"citation":"path:line"}`,
and states "This declares, never infers, a basis." Nothing verifies it. In the
last two days the campaign has: withdrawn a universal exit-price formula
(`min(num(delta), 2*ceil(delta))`); recorded that previously banked `ceil(gap)`
floors undercount by roughly a factor of two; corrected a `REPRESENTATIVE`
consumer that had been read as full-actual-exit; and needed an erratum to
restore a single missing `notin` in a frozen review summary. Every one of these
is a *ledger arithmetic or typing* failure, not a mathematical failure, and
every one was caught by a human-scale reread rather than by an instrument.

*Smallest useful implementation.* A single read-only script, `ops/charge_lint.py`,
that:

1. extracts every `charge_basis={...}` line from `xmodel/**/*.md` and `ladder/*.md`;
2. parses it as strict JSON and rejects any unlisted `branch` value (allowed:
   `q=1-exact`, `q>=2`, `multi-flag`);
3. resolves `citation` as `path:line` **at the report's declared basis commit**
   and confirms the line exists (not that it says anything — existence and
   basis-pinning only);
4. recomputes the promoted safe floor from `delta` (`delta` if integral, else
   `ceil(2*delta)`) and emits a `MISMATCH` line if the report's stated floor
   differs;
5. exits nonzero on any parse failure, unknown branch, dangling citation, or
   mismatch, and prints one line per finding.

*Smallest useful test.* Two fixtures: one report with a correct
`charge_basis` and floor, one mutated fixture with `delta="3/2"` and a stated
floor of `2` (the exact shape of the withdrawn formula's error, which should
report `ceil(2*3/2) = 3`). The linter must pass the first and fail the second.
Roughly 120 lines plus fixtures; desk-scale; read-only, so it cannot damage a
ledger.

*Why bounded.* It adds no new ledger, no second live queue, no authority. It
converts an existing mandated convention into a fail-closed check, which is the
smallest possible intervention that would have caught the class of error the
campaign actually made.

*Second-order observation, deliberately **not** turned into a change request.*
`APPROACHES.md` is 327 KB and roughly 120 stacked "superseding" overlays; every
model in every round pays a large retrieval cost to find the live ranking and
the 46-row table at the very bottom. A generated live view is the obvious fix
and is also the obvious way to violate `COORDINATION.md`'s "do not maintain a
second live queue, avenue map, or evidence ledger". I record the cost and
propose nothing, because I cannot design a safe version inside this round's
budget.

---

## 7. Idea cards

### Card A — `BEZOUT-CEIL-SIGMA-INFTY`

- **Dependencies.** GGV22 dichotomy (`EXTERNAL`, preprint tier, conditional on
  the GGV-Horruitiner bridge as the campaign records it); `CRITICAL 2`'s
  existential selection; `ladder/SHEET6-MULTIPOLE.md` §1 type conventions and
  D4; the promoted pole-mass floor. No dependence on `G2-PSC`, on any
  provisional item, or on LL1-R4.
- **Exact object/mechanism.** The identity
  `td = deg f * deg g - Sum_{p in L_infty} i_p`, valid for any dominant pair and
  exact (not an inequality) when `J` is a nonzero constant, since all affine
  intersections are then transverse. Applied to the degree-pinned branch:
  `td = 7776 - Sum_p i_p`, with at most `gcd(72,108) = 36` infinity points.
- **Cheapest discriminator.** One source read deciding whether pole order equals
  degree in the Sigray normalized frame, hence whether `(72,108)` is type
  `(2,3)`. Cost: one reading of `Not 2.4`, `St 2.1`, `Lemma 2.1`, `St 5.2(i)`.
  No computation.
- **Interpretation of either result.** *Identification holds:* the whole current
  type-`(2,3)` td12 lane is running on the branch that carries a `7776` ceiling,
  and the pole-mass/budget machinery immediately becomes a candidate source of a
  `td` **lower** bound via `Sum_p i_p`. *Identification fails:* the ceiling
  correction to `(G5)`/`CRITICAL 7` still stands (it is pure Bezout), but the
  bridge to avenue 2's boundary data is severed and the card degrades to a
  ledger correction only.
- **Stop condition.** Stop if the boundary-side estimate of `Sum_p i_p` cannot
  be bounded above by any promoted theorem — that is, if step 2 of §4.1 has no
  input. Do not substitute a cap or an analogy; return typed `OPEN`.
- **Expected information gain.** High and asymmetric. At minimum, one
  `CRITICAL`-tier canonical sentence is corrected. At maximum, the degree-pinned
  branch acquires a two-sided `td` window, which is the first time any branch of
  JC2 has had one.
- **Fingerprint.**
  `td-ceiling | projective-Bezout-deficit-at-infinity | (72,108) GGV branch, Sum_p i_p | source read: is Sigray type (alpha,beta) the degree ratio?`

### Card B — `LIPSHITZ-CODOMAIN`

- **Dependencies.** `PROMOTED` U1 semilinear family schema; `PROMOTED` Q+E5
  fixed-state menu and no-partition `R2.2` predicate; `PROMOTED` U2 one-P0
  family record including the proved non-semilinearity of the two-parameter
  union; the promoted exit floor law. External: Lipshitz 1978 (decidability of
  the existential theory of `<Z,+,|>`) — `EXTERNAL`, must be pinned at the next
  sweep before any promotion.
- **Exact object/mechanism.** Fix the landing compiler's codomain as the
  existential fragment of `<Z, +, <, |>`. Each cell/record family becomes a
  formula; coverage becomes entailment; "no cell escapes" becomes an
  unsatisfiability check rather than an enumeration.
- **Cheapest discriminator.** Take the four banked objects above and write each
  as a formula in the fragment **by hand**, counting divisibility atoms. Desk,
  no code. The genuinely uncertain one is Q+E5's no-partition `R2.2` predicate:
  partition quantifiers of unbounded arity are not first-order arithmetic at
  bounded depth.
- **Interpretation of either result.** *All four go through with bounded atom
  count:* the record-language obligation in `CRITICAL 4`/`CRITICAL 5` is
  reducible to a decidable theory, `NUCAP`-style caps are provably unnecessary
  inside the covered fragment, and the compiler acquires a fail-closed coverage
  certificate for the first time. *`R2.2` (or any other) escapes:* the output is
  the precise identification of the single construct that leaves the decidable
  fragment — which is strictly more useful than the current situation, where the
  obligation is stated but its logical shape is unknown.
- **Stop condition.** Stop if two or more distinct banked constructs escape the
  fragment; at that point the fragment is the wrong target and the card should
  not be repaired by weakening the constructs.
- **Expected information gain.** High. This is the only proposal in this report
  that attacks the campaign's #1 bottleneck directly, and its failure mode is
  informative rather than merely negative.
- **Fingerprint.**
  `landing-compiler-codomain | existential Presburger-with-divisibility (Lipshitz) | U1 AP families, U2 one-P0 bilinear family, Q+E5 R2.2, exit-floor law | hand-encode all four, count divisibility atoms`

### Card C — `OFF-DIM2`

- **Dependencies.** `PROMOTED` accelerator `I:Delta = I:Delta^inf = I + (det A)`;
  the banked clopen-diagonal theorem (internal reviews plus an external
  statement in `jacobian-collision-geometry`); the banked AS109 formal-tube
  branch count. Independent of avenue 2 entirely — this is a genuinely
  orthogonal instrument.
- **Exact object/mechanism.** `Delta` clopen in `X = A^2 x_{A^2} A^2` forces
  `Off = X \ Delta` to be a union of components of a smooth surface, hence
  smooth of pure dimension two, with `Off -> A^2` etale of generic degree
  `td - 1`.
- **Cheapest discriminator.** For one explicit object — the characteristic-three
  Artin-Schreier collision, where `Off` is known nonempty — compute
  `dim V(I + (det A))` and its singular locus. Must return smooth, pure
  dimension two.
- **Interpretation of either result.** *Returns smooth pure dimension two:* the
  instrument is validated and becomes a standing one-line gate on every
  collision computation, plus a non-circular `td` oracle for explicit pairs.
  *Returns anything else:* either the clopen argument has a characteristic-`p`
  caveat I have not accounted for (likely, and worth knowing exactly), or a
  banked computation is wrong. Both outcomes are worth the one Groebner run.
- **Stop condition.** Stop if the characteristic-zero instances are all empty
  and no explicit nonempty `Off` exists to test against — the instrument would
  then have no positive control and must not be promoted on negative controls
  alone.
- **Expected information gain.** Moderate. It will most likely confirm rather
  than refute, but it converts a scattered set of banked observations into a
  cheap standing gate on the campaign's only avenue that is fully independent of
  the Sigray source.
- **Fingerprint.**
  `collision-lane falsification | clopen diagonal => Off smooth of pure dimension two | V(I + det A) for the char-3 AS collision | compute dim and singular locus, with positive and negative controls`

---

## 8. Lane dispositions

Inputs are labelled by tier: `[P]` promoted, `[V]` provisional, `[F]` formal,
`[BR]` book-relative, `[C]` conjectural.

| Lane | Disposition | Basis |
|---|---|---|
| td12 `B25`/`S17` route-separated source pair packets | **continue** | Parent recurrence and absorption identity are `[P]`; these are the named next gate and the only lane that can turn a `[F]` envelope into a `PairRef`. |
| `TD12-FORMAL-CASCADE-RANK/v1` descendants | **stop** | `[V]`, and its own content is that the `[F]` envelope has no bite: the truncated binomial response absorbs every row through `s<=i`. Further formal-envelope descendants are predicted toothless by the lane's own result. Discharge the review debt; spawn nothing. |
| LL1-R4 software | **continue** | `[V]` executable over `[P]` mathematics; finish the different-model software review, no descendants. Attack surface is already correctly named (carrier leakage into epsilon rows, mover exhaustiveness, optimized behaviour). |
| U2 coverage / gluing / landing | **redesign** | The labelled-route kill rate is high but each kill closes one label; `[P]` evidence now says the codomain is a family-record language. Redirect into Card B rather than into more labelled routes. |
| Q+E5 standalone checker | **continue** | `[P]` at fixed-state pattern scope. Build only after software review; do not migrate `cell_check`, do not edit `solve_arr`, keep `NUCAP=500`. |
| Two-pole full-exit bridge consumers | **continue** | `[P]` at complete-carrier, lower-floor-only scope. Consume as a floor; never as attainment. |
| GGV degree farm (`deg <= 150`) | **redesign** | `[BR]`. Re-mine for `Sum_p i_p`-relevant boundary content per Card A; emptiness verdicts alone cannot close the `deg >= 125` branch and therefore cannot reach `CRITICAL 7`. |
| K00 / D43 | **continue** | `[P]` field theorem, protected seed, no new fanout. |
| AS109 / char-p Witt lifting | **continue** | `[P]` at the degree-twelve frontier; add the Card C positive control at zero marginal cost. |
| ACS-CEIL / TDIC-SET | **stop** (already stopped) | Correctly stopped; nothing in this round revives them. The corrected deficit-Euler identity has negative strata and is not a positive decomposition of `td - 1`. |
| Lean formalization | **`NOT_INSPECTED`** | Out of scope by lane prompt; I record no disposition and made no inspection. |

---

## 9. Non-claims

Nothing in this report proves, disproves, or bounds JC2. Specifically I do not
claim: any landing, coverage, occurrence, or realizability result; any
attainment (every floor cited stays a floor); any `td` bound on the `deg >= 125`
branch; any `G2-PSC` or `G2-BD` progress; any counterexample; any promotion. The
`(72,108)` ceiling is `CLASSICAL` mathematics applied to an `EXTERNAL`
preprint-tier dichotomy and inherits its existential selection. The type
`(2,3)` identification is `EXACT-CONDITIONAL` on one unverified source step and
must not be consumed before that step is read. Card B's external decidability
input is unpinned and must be verified at the next sweep before any promotion.
Card C's third bullet is a sharpening of banked facts, not a new theorem, and
may be duplicated by the external collision-geometry note.

## Seal

- Body length: `39035` bytes (all bytes before this heading).
- Body SHA-256: `0bade1558867775ebc36a4ee943acb21e39f2903827a331515d5819b31f59ffb`.
- Basis: `ccb6cd52eeab95f169b40f0a48668c3acd7a607e`. Lane: Opus 5, blind.
