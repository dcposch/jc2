# Fable 5 cross-pollination and adversarial synthesis — round `20260827T0935Z`

Date: 2026-08-27
Author: Fable 5, cross-pollination lane (independent of the coordinator's synthesis)
Status: **ADVERSARIAL SYNTHESIS / NAVIGATION.  The one new theorem proved here
(Theorem 1) is a desk proof from promoted inputs and carries its own complete
argument; everything else is audit, reconciliation, and routing.  No lifecycle
label of any cited artifact is changed by this file.**

## 0. Custody and verdict summary

All fourteen prompt-listed files were SHA-256-verified in this session and
matched the manifest exactly (packet `e871e3d7…`, sol `98a494a5…`, fable5
`098b81d1…`, grok `265cfa73…`, opus5 `32954026…`, V43 producer `7345d4a8…`,
V43 Opus review `64e49a36…`, naturality interface `1cfa10b4…`, its Fable5
review `b66f8c0c…`, three-row syzygy interface `2354703a…`, V45 RESULT
`234cc402…`, V45 PASS_EVIDENCE `b669f942…`, V14 CUSTODY_GAP `ecbc2c20…`,
V14R1 PREREGISTRATION `65ee7849…`).  Post-snapshot evidence is treated as
labeled: V45 exact but under Opus review; V14R1 producer-pass provisional.

Ledger drift disclosure: at write time `COORDINATION.md` still matches its
packet pin `72d789d3…`; `APPROACHES.md`, `AUDIT.md`, `PROGRESS.md` have
moved past their pins (concurrent campaign waves).  The §7 history checksum
is therefore best-effort against the current ledgers plus the four blind
reports' quoted snapshots.

Headline verdicts, one line each:

1. **The two-fibre criterion is TRUE** as a four-way equivalence (Theorem 1),
   proved here with every hypothesis named; homogeneity is load-bearing in
   exactly two of the three steps and I exhibit one counterexample that
   breaks both when it is dropped.  Fable §3.1 and Opus Theorem A are the
   same theorem, independently derived blind; this file is a third
   independent derivation.
2. **Opus's §6.2 eliminant-predicate defect is real** — verified from the
   live source this session — with one improvement: the harvested
   `eliminant_ideal.txt` and `ELIMINANT_SIZE` telemetry are written *before*
   the mislabeled quit, so completed or running lanes can be re-adjudicated
   post hoc without relaunch.
3. **The seventeen selected rows are literal frozen `Tg` rows** (read from
   `SELECTED` in the live compiler), so Grok's not-in-`J0` custody hazard is
   discharged for this lane, and the positive branch of the generic-fibre
   run is sound for the full chart.
4. The exponent ladder is **decision-irrelevant**; it survives only as a
   bounded certificate-materialization/fallback instrument (§4).
5. K00: local membership is provisionally **decided positive** (V14R1,
   `h = 63*d4+20`); global/local coexistence is fully explained; the full
   syzygy module *does* yield a representation-invariant first deformation
   obstruction for the mixed problem, formalized in §5.
6. UAC: naturality + three-row syzygy + V45 remove serial `G22/G24+`
   exporters from the critical path **conditionally** on a short finite list
   of freeze/review obligations (§6); all scope firewalls survive.
7. Opus adds significant correctness-adjusted unique capability beyond
   Fable this round (§12): complementary, not duplicative.

---

## 1. The two-fibre criterion: proved, with hypotheses and failure modes

### 1.1 Theorem

> **Theorem 1 (two-fibre criterion).**  Let `S = Q[rho, X]` carry a grading
> in which every `X`-variable has strictly positive weight, `wt(rho) = 0`,
> and `rho` is the **only** weight-zero variable, so `S_0 = Q[rho]` (H1).
> Let `J ⊆ S` be homogeneous (H2), let `a1 ∈ X` with `wt(a1) > 0` (H3), put
> `K = J : a1^infinity`, `T = {u ∈ Q[rho] : u(0) != 0}`,
> `D = T^{-1} Q[rho] = Q[rho]_(rho)`, and `J0 = ` image of `J` under
> `rho -> 0` in `Q[X]`.  Then the following are equivalent:
>
> ```text
> (a)   K + (rho) = S;
> (a')  exists N and u in Q[rho], u(0) != 0, with u*a1^N in J
>       [normalizable to a1^N U(rho^2) in J, U(0)=1, when J is stable
>        under rho -> -rho, as the frozen even rows are];
> (b)   a1 in sqrt( J * T^{-1}S ) = sqrt( J * D[X] );
> (c)   a1 in sqrt( J * Q(rho)[X] )   AND   a1 in sqrt( J0 );
> (d)   J|_(a1=1) * Q(rho)[X\{a1}] = (1)   AND   J0|_(a1=1) = (1) in Q[X\{a1}].
> ```

**Proof.**

*(a) ⟺ (a').*  `⟸` is unconditional: `u*a1^N ∈ J ⟹ u ∈ K`, and
`u ≡ u(0) mod (rho)` with `u(0)` a unit, so `K + (rho) = S`.  `⟹` uses H1+H2:
`K` is homogeneous (colon of a homogeneous ideal by the homogeneous `a1`),
`(rho)` is homogeneous, so `K + (rho) = S` iff its weight-zero part contains
`1`; that part is `(K ∩ Q[rho]) + rho*Q[rho]` because `S_0 = Q[rho]`, so some
`u ∈ K ∩ Q[rho]` has `u(0) != 0`, and `u ∈ K` unpacks to `u*a1^N ∈ J`.  For
the `U(rho^2)` form: apply `rho -> -rho` and multiply,
`u(rho)u(-rho) = U(rho^2)`, `U(0) = u(0)^2 != 0`, then normalize.

*(a') ⟺ (b).*  Pure localization, unconditional: `x ∈ I*T^{-1}S` iff
`t*x ∈ I` for some `t ∈ T`; apply to `x = a1^N`, `I = J`, and take radicals.

*(b) ⟺ (c).*  Unconditional.  `Spec D` has exactly two primes, `(0)` and
`(rho)`.  `sqrt(J*D[X])` is the intersection of primes `P ⊇ J*D[X]`,
stratified by `P ∩ D`: the `P ∩ D = (0)` stratum is in inclusion-preserving
bijection with primes of `Q(rho)[X]` over `J*Q(rho)[X]`; the `P ∩ D = (rho)`
stratum with primes of `Q[X]` over `J0` (the image of `J*D[X]` in
`D[X]/(rho) = Q[X]` is `J0`, images of generators).  So `a1` lies in every
prime over `J*D[X]` iff it lies in both fibre radicals.

*(c) ⟺ (d).*  `(c) ⟹ (d)` is trivial and unconditional
(`a1^N ∈ I ⟹ 1 = a1^N|_(a1=1) ∈ I|_(a1=1)`, in each fibre).
`(d) ⟹ (c)` uses H2+H3, once per fibre field `k ∈ {Q(rho), Q}`, ideal
`I ∈ {J*Q(rho)[X], J0}` (each homogeneous for the positive weights on `X`;
over `Q(rho)` the scalar `rho` has weight 0):  suppose `a1 ∉ sqrt(I)`.
Radical membership at each fixed exponent is a linear system for the
cofactors, so it fails over the algebraic closure `k̄` too; by the
Nullstellensatz there is `p ∈ V(I)(k̄)` with `a1(p) != 0`.  `V(I)` is stable
under the weight `G_m`-action `λ·x_j = λ^{w_j} x_j`; choose `λ ∈ k̄` with
`λ^{wt(a1)} a1(p) = 1`; then `q = λ·p ∈ V(I)`, `a1(q) = 1`, so
`I|_(a1=1) != (1)` over `k̄`, hence over `k` (membership of `1` is a linear
system, field-stable).  Contrapositive gives `(d) ⟹ (c)`.  ∎

Opus's Theorem A is parts (a)/(a')/(b) plus, given the special conjunct,
`E != 0 ⟺` the generic conjunct (with `E = K ∩ Q[rho]`; note `E != 0 ⟺
∃ u != 0, u a1^N ∈ J ⟺` generic radical membership, by clearing
denominators).  Opus's geometric proof (components of
`V(K) = closure(V(J) ∩ D(a1))`, `rho` constant on each once `E != 0`) is
independently correct — I re-checked the two nonstandard steps:
`V(I : f^∞) = closure(V(I) \ V(f))` via `sqrt(I : f^∞) = sqrt(I) : f^∞`,
and density of `C ∩ D(a1)` in each component `C`.  The lemma is now
**triply derived** (Fable blind §3.1, Opus blind §3.2, this file).  It is
load-bearing; a fourth, different-model, one-hour check should still ride
along with the launch, but it is no longer a single-point risk.

### 1.2 Failure modes, each with a witness

- **FM1 — drop homogeneity (H2): two steps break at once.**
  `S = Q[rho, a1]`, `wt(a1) = 1`, `J = (rho*a1 - 1)`.  Then `a1` is
  invertible mod `J`, so `K = J` and `K + (rho) = (rho*a1 - 1, rho) = (1)`:
  **(a) holds**.  But evaluating at the generic-fibre point `a1 = 1/rho`
  kills any `u(rho)*a1^N ∈ J` unless `u = 0`: **(a') and (b) fail**, and the
  generic conjunct of (c) fails (the point has `a1 != 0`) while
  `J0 = (-1) = (1)` makes the special conjunct trivially hold, so **(c)
  fails**.  Meanwhile `J|_(a1=1) = (rho - 1) = (1)` over `Q(rho)` and
  `J0|_(a1=1) = (1)`: **(d) holds**.  One inhomogeneous ideal thus breaks
  both `(a) ⟹ (a')` and `(d) ⟹ (c)` while `(a') ⟺ (b) ⟺ (c)` survives
  (they are unconditional).  Engineering consequence: the pipeline's
  homogeneity gates (`total_to_t` raising on any wrong-weight monomial) are
  part of the proof, not hygiene.
- **FM2 — a second weight-zero variable.**  With `S_0 = Q[rho, q]` the
  weight-zero projection lands in `Q[rho, q]` and the certificate/localization
  forms break.  This is exactly the audited `qa1`/`ez9` alphabet discipline;
  the V43 gates (`66/65` counts, `general_only == ["ez9"]`, positive-weight
  check) enforce H1 at run time.
- **FM3 — selected-row subideal.**  Rows generating `J' ⊆ J`: every
  positive conclusion ascends (`E' != 0 ⟹ E != 0`; a subideal fibre unit
  forces the full fibre unit), every negative is void.  Sharper sufficient
  condition: rows in `K = J : a1^infinity` (i.e. derived by `a1`-saturation
  steps) still prove the positive branch, since `J' ⊆ K ⟹ K' ⊆ K`; rows
  derived by localization at **any other** variable do not.  Empirically
  discharged for the live lane: `SELECTED` in
  `compile_total_dehom_eliminant_v43.py` is seventeen literal frozen names
  (`Tg11_1, Tg12_1, Tg12_2, Tg13_1, Tg13_2, Tg13_4, Tg14_1..Tg14_4, Tg15_3,
  Tg15_4, Tg16_5, Tg16_6, Tg17_5, Tg18_6, Tg19_7`), pulled from
  `reconstruct_rows()` by name with per-row `total_t` hashes recorded —
  honest elements of `J`.
- **FM4 — non-flatness is the content, not a hypothesis.**  No flatness is
  assumed anywhere in Theorem 1.  The criterion exists precisely because
  saturation does not commute with specialization: for the design toy
  `J = (f - t*x)` one has `J0 : f^∞ = (f) : f^∞ = (1)` (naive fibrewise
  saturation is unit) while `K = J` and `K + (rho) != (1)`; Theorem 1(c)
  locates the failure in the generic fibre (survivor point `(f,x) = (t,1)`).
  Note `S/J ≅ Q[t,x]` is `Q[t]`-flat here — flatness of the quotient
  neither helps nor is needed; "non-flat counterexamples" cannot break a
  theorem that never invokes flatness, and this toy shows the naive
  flat-sounding inference ("fibre saturation unit ⟹ chart closes") is the
  thing that is false.
- **FM5 — characteristic.**  Everything is over `Q`.  Modular `(p, rho=c)`
  screens are routing heuristics only (§2, outcome v).

### 1.3 What the already-proved special-fibre unit contributes

It is exactly **one of the two conjuncts** of (c)/(d) — nothing more and
nothing less.  Alone it proves nothing about (a) (FM4 toy).  Its three
roles:

1. It makes the generic-fibre computation **decisive in both directions**:
   unit ⟹ both conjuncts hold ⟹ `K + (rho) = (1)`; non-unit ⟹ the generic
   conjunct fails ⟹ `K + (rho) != (1)` outright.  Without it, a generic
   non-unit would still leave the special conjunct open.
2. In the geometric proof it is what excludes survivor components inside
   `{rho = 0}`.
3. On the positive branch it supplies the `N0` consumed by the certificate
   converter when the eliminant is `t`-divisible (§2.3).

Evidence status of the conjunct: `a1 ∈ sqrt(J0)` is promoted (V42 radical
cascade + review, per Opus's citation — noting Opus's own later correction
that V42's *explicit* certificate is in the branch ideal `I_A1`, so the
promoted content is the radical statement, not an unsplit exponent), and
independently the 17-row dehomogenized unit gives the subideal statement,
which ascends.  Both suffice.

---

## 2. The generic-eliminant computational predicate, audited from source

Source read this session: `compile_total_dehom_eliminant_v43.py`
(hash-gated import of `compile_total_dvr_w30_v43.py` at `0de6a2b2…`).
Verified facts: the seventeen `SELECTED` rows are literal `Tg` names (FM3);
census gates re-imposed (70 hashes, 59 nonzero, 66/65 alphabet,
`general_only == ["ez9"]`); the special control
`I0 = subst(I,t,0); reduce(1,std(I0)) == 0` **gates every run before
elimination** (built-in positive control); the eliminant `E = eliminate(I,
prod(active))` with block order `(dp(n),dp(1))`, `t` last, so `E` is exactly
`Ê = I ∩ Q[t]` for the dehomogenized subideal; `write(eliminant_path, E)`
and `ELIMINANT_SIZE` are emitted **before** the outcome branch; the outcome
predicate is byte-for-byte as Opus quoted (`candidate != 0 &&
subst(candidate,t,0) != 0` sets `unitfactor`, else `no-unit-eliminant` and
quit); the `lift` phase materializes and replays multipliers on the
`unit-eliminant` branch only.

### 2.1 Outcome semantics (subideal `J'`, dehomogenized ideal `I ⊂ Q[t][X']`)

First the ring distinction: over the **field** `Q(t)`, "unit ideal" means
`I*Q(t)[X'] = (1)`, and `I*Q(t)[X'] = (1) ⟺ Ê != 0` (⟸ a nonzero `e(t)` is
a `Q(t)`-unit; ⟹ clear denominators of `1 = Σ (h_i/q_i) g_i`).  Over the
**polynomial ring** `Q[t]`, "unit ideal" means `Ê` contains a nonzero
constant.  The constant term of `e` is irrelevant to the generic fibre.

| Outcome | For the subideal `J'` | For the full chart (`J`, 59 rows) |
|---|---|---|
| (i) unit over `Q(t)` (⟺ `Ê != 0`) | generic fibre of `J'` empty on `D(a1)` | **decisive positive**: with the special control (already gating), Theorem 1 gives `K + (rho) = (1)`; the chart closes |
| (ii) nonzero eliminant `e(t)`, `e(0) = 0` | same as (i) | same as (i) — currently mislabeled `no-unit-eliminant`; correct token `chart-closes-by-escape` |
| (iii) constant nonzero eliminant | `I = (1)` over `Q[t][X']`: every fibre `t = c` empty | strongest positive; direct certificate with `u = 1` after rehomogenization, no `N0` needed |
| (iv) zero elimination ideal (`Ê = 0`, `ELIMINANT_SIZE = 0`) | generic fibre of `J'` **nonempty** — exact for the subideal | **inconclusive**; escalate to all 59 rows.  Full-system `Ê = 0` ⟹ `K + (rho) != (1)` definitively: honest survivor, prefix-relative |
| (v) modular / specialized `rho = c` | see below | routing only, never decision |

(v) semantics, exactly: if the generic fibre is empty (`e != 0`), every
fibre `t = c` with `e(c) != 0` is empty — all but finitely many `c`.  If the
generic fibre is nonempty, the `t`-image of the horizontal component
contains a cofinite set of `Q̄`-points, but a specific rational `c` can be
exceptional, and mod `p` both directions can additionally be corrupted by
bad primes.  Hence: an exact-`Q` unit at one random `c != 0` is strong
one-sided evidence (either generic-empty or `c` exceptional); a non-unit at
one `c` is **weak** (vertical component at `c` possible — witness
`I = (t - c)`, unit over `Q(t)`, zero ideal at `t = c`); mod-`p` results in
either direction are heuristic.  Decision requires (i)/(ii)/(iii)/(iv) over
`Q(t)` or `Q[t]`.  This corrects my own blind stage-2 wording ("decisive-
grade") to "strong one-sided", and Grok's specialization-probe claim (§4).

### 2.2 Verdict on Opus's §6.2 claim

**Sound, verified from source.**  Outcomes (ii) and (iv) are conflated into
the single token `no-unit-eliminant`, and (ii) is a positive being reported
as a failure.  Two refinements:

- The defect is **decision-completeness relative to Theorem 1**, not a
  soundness bug: the predicate was internally coherent for the lane's
  original purpose (extract a *direct* `u(0) != 0` certificate, for which
  `e(0) != 0` genuinely is needed), and an emitted `unit-eliminant` is sound
  and comes with a lift-phase replayed certificate.
- **Completed and in-flight runs can be re-adjudicated without relaunch**:
  `ELIMINANT_SIZE` and `eliminant_ideal.txt` are emitted before the quit.
  `ELIMINANT_SIZE >= 1` on a `no-unit-eliminant` run *is* outcome (ii) =
  chart-closes-by-escape (the special control necessarily passed to reach
  elimination); `ELIMINANT_SIZE = 0` is outcome (iv).  Repair spec: three
  outcome tokens plus a selected-vs-full scope bit (Opus hidden assumption
  9, now written down), keep `unit-eliminant` as the stronger self-contained
  outcome, keep the lift phase.

### 2.3 The certificate converter, made explicit

Positive branch with `t`-divisible eliminant `e(t) = t^k v(t)`, `v(0) != 0`:
rehomogenizing the identity `e = Σ m_i T_i|_(a1=1)` (multiply by `a1^M`,
homogenize cofactors; legitimate since `J'` is homogeneous and `e` has
weight 0) gives `e(t)*a1^D ∈ J'`.  Take any **explicit** special identity
`j = a1^{N0} + rho*g ∈ J` (equivalently, an explicit `a1^{N0} ∈ J0` plus any
preimage).  Then mod `J`:

```text
a1^{N0} ≡ -rho*g   ⟹   a1^{2N0} ≡ t*g^2   ⟹   a1^{2kN0} ≡ t^k*g^{2k}
⟹  v(t)*a1^{D + 2k*N0} ≡ (e(t)*a1^D)*g^{2k} ≡ 0,
```

so `u = v`, `N = D + 2k*N0` is an explicit certificate with `u(0) != 0`.
Consequences: the **decision** never needs `N0`; an **explicit** certificate
needs `N0` only in case (ii).  This adjudicates the Fable/Opus divergence on
the 192-GiB multiplier extraction: Opus's "never needed" is right for the
decision; a single bounded lift on the smallest sufficient row subset is the
one surviving justified use, conditional on landing in case (ii) and on the
campaign wanting a self-contained certificate rather than a decision-tier
GB record.  Item 3 gives the cheaper route to `N0`.

---

## 3. The constructive radical-certificate tree, formalized

The combination lemmas requested, with proofs (all elementary; the value is
the exact bookkeeping):

> **C1 (product split).** If `x^m ∈ I + (f)`, `x^n ∈ I + (g)`, `fg ∈ I`,
> then `x^{m+n} ∈ I`.
> *Proof:* `x^m = i_1 + a f`, `x^n = i_2 + b g` ⟹
> `x^{m+n} = i_1 i_2 + i_1 b g + a f i_2 + a b (fg) ∈ I`.  ∎
>
> **C2 (absorbed multiplier).** If `x^m ∈ I + (f)` and `x f ∈ I`, then
> `x^{m+1} ∈ I`.  *Proof:* `x^{m+1} = x i_1 + a (x f)`.  ∎
>
> **C3 (localized branch).** If `x^m ∈ I + (f)` and `f^k x^n ∈ I`, then
> `x^{mk+n} ∈ I`.  *Proof:* `(i_1 + a f)^k = i' + a^k f^k` with `i' ∈ I`
> (every cross term carries `i_1`), so
> `x^{mk+n} = i' x^n + a^k (f^k x^n) ∈ I`.  C2 is `k = n = 1`.  ∎
>
> **C4 (radical-only shadow).** If `x ∈ sqrt(I + (f))`, `x ∈ sqrt(I + (g))`,
> `fg ∈ sqrt(I)`, then `x ∈ sqrt(I)` — pointwise: on `V(I)` either `f = 0`
> or `g = 0`, and `x` vanishes on both loci.

**Ideal identities vs radical reasoning, separated.**  C1–C3 consume and
emit *explicit cofactor lists* and produce an explicit exponent; C4 consumes
Gröbner unit-ideal facts in quotient/localized rings and produces **no
exponent**.  V42's promoted statement `a1 ∈ sqrt(J0)` is C4-type (that is
all Theorem 1's special conjunct needs — the decision path never requires
the constructive tree).  V42's one known explicit identity is C1/C3-input
shape: `a1^8 ∈ I_A1 = J0 + (rs1)`-branch (Opus's V43-review correction).

**Exponent recurrence and DAG.**  A cascade node with split element `f`:
left leaf `a1^m ∈ J0 + (f)` (explicit), right leaf `f^k a1^n ∈ J0`
(explicit) ⟹ root `a1^{mk+n} ∈ J0`.  Nested splits compose the same way
(`N` grows multiplicatively through `k > 1` levels, additively when
`k = 1`).  Executable DAG: leaves = cofactor files; internal nodes = the C1/C3
assembly (sparse polynomial arithmetic); root verification = one
fixed-weight full-product replay at weight `5N` (V43 validator shape, with
a **row-data** mutation control per Opus repair 1, not the tautological
target-coefficient control).

**Can the known branches be combined today?**  Not from the frozen record
alone: the `rs1`-invertible branch is recorded as radical/GB-tier, not as an
explicit `rs1^k a1^n ∈ J0`.  Each missing leaf is a bounded fixed-weight
linear solve (weight `5n + 3k`; `wt(rs1) = 3`), far cheaper than the 192-GiB
whole-unit lift.  Classification: **certificate materialization only** —
execute only if M1's positive branch lands in case (ii) and an explicit
unsplit certificate is wanted; it then supplies `N0` (any explicit
`a1^{N0} ∈ J0` lifts to `a1^{N0} + rho*g ∈ J` by taking any preimage of the
cofactors under `sp`).

---

## 4. Reconciling N=6, seeded N=7, and the generic-fibre decision

- **V43 (`a1^6 ∉ J0`)** stands, now with a completed hostile review (Opus,
  post-snapshot: no FAIL; REPAIRABLE on the mutation control and three
  custody/disclosure items).  Per the prompt's instruction and Opus §5.4:
  the target-coefficient mutation control is **not** treated as an
  independent check anywhere in this synthesis — the result rests on the
  full-product replay plus Opus's independent 26,200-equation exact replay
  and the disjointness argument.  The free corollary `a1^i ∉ J0` for all
  `i <= 6` (ideal property; V38 needed only for mixed `a1^i k^j`) is
  already frozen in my memory of the review and re-endorsed.
- **Is the ladder still decision-relevant?  No.**  Theorem 1 contains no
  `N`; given the promoted `a1 ∈ sqrt(J0)`, the ladder's positive branch is
  guaranteed-and-uninformative (Opus's bit-budget argument), its negatives
  are prefix-fragile (grade-20+ rows can only destroy them), and its cost is
  superlinear (Opus sizing: w35 ≈ 9.5x, w40 ≈ 77x).
- **What survives of it.**  (α) The `D >= 7` floor is a free sanity gate on
  any certificate M1 extracts.  (β) The V43 compiler/validator is the
  independent fixed-weight verifier for §2.3/§3 materialization.  (γ) The
  seeded `N=7` dual is the registered **fallback** if M1 breaches its stop
  rule — and only then, with unrestricted replay mandatory and the Opus
  custody repairs (row-data mutation; custody block moved out of `main()`;
  compiler-harvest source manifest; `rc=1` disclosure; census addendum in
  the freeze) applied to any descendant.
- **Grok's specialized floor-raiser, corrected.**  "Specialized
  nonmembership at one prime ⟹ `Q`-nonmembership" is **wrong as stated**:
  a `Q`-certificate reduces mod `p` only at primes not dividing its
  denominators, which are unknown a priori — and V43's own denominator
  `2^23·3^11·5^5·7^5·11·19^2·23^2·37·59·157·617` (Opus's desk
  factorization) shows small primes genuinely occur.  Repaired form: ≥ 2
  independent large primes, routing-only, never a promotable floor.  (Both
  selector primes 65519/65521 are coprime to the V43 denominator — lucky,
  but that is an observation about one certificate, not a guarantee.)
- **Custody dividend.**  The Opus review's from-scratch confirmations of the
  shared `reconstruct_rows`/`build_products` layer (284,766 census that
  discriminates 65/66/67 alphabets; the `sha256("[]")` 11-zero-row collision
  census; 70-row bridge) directly de-risk M1, which reuses the same layer.
  The named residual risk also transfers: no review has yet re-derived the
  literal row coefficients from the V20/V28/V35 emitter chain; M1 inherits
  that single shared point of failure and must say so in its freeze.

---

## 5. K00: V8/V9, D8, V14R1, and the mixed first-deformation obstruction

### 5.1 Coexistence, exactly

V14R1 (provisional producer pass, awaiting different-model review) exhibits
`h = 63*d4 + 20`, `h(0) = 20`, with `h*r7 = Σ u_i r_i` explicitly, all 36
lift-matrix entries serialized and a fresh-process replay — precisely the
Escape-Lemma witness three blind reports specified (Sol Card 1, Fable Card
F2, Opus Card B) and precisely the custody discipline the V14 gap demanded.
Global nonmembership and local membership coexist with no tension: the
failure locus of membership is the support of `(I + (r7))/I ≅ R/(I : r7)`,
a closed set contained in `V(h) = {d4 = -20/63}`, which **misses the
origin**.  `r7 ∉ I` globally because no element of `(I : r7)` has a nonzero
constant *polynomial* — the promoted V8/V9 statements are untouched.

Consequences, contingent only on the V14R1 freeze/review: by Krull
(`I + m^n` is `m`-primary-supported, so local membership descends to every
truncation), `r7 ∈ I + (d)^n` for **all** `n`; D7/D8 compatibility was the
expected pattern; the "first filtered obstruction degree" **does not
exist** and leaves the obligation list; D9+ is terminated as discovery.
D8's residual value is a consistency control — with the correction (my own
blind Card F2 overstated this) that the comparison is *"the truncations of
`u_i/h` form a valid degree-`n` lift"*, not entrywise equality with the
harvested 273/492-entry lifts, since lifts are unique only modulo the
syzygy module.

### 5.2 The representation-invariant first deformation obstruction — yes

The prompt asks whether the full syzygy module yields a
representation-invariant first deformation obstruction for the mixed
`Lambda^19`/load/target/`Jdet` problem.  **It does; here is the object.**
Let `R_m = Q[d]_((d))`, `I = (r1..r6)`, `λ_i = u_i/h ∈ R_m` (so
`r7 = Σ λ_i r_i`), and let `s_1,…,s_7` be the first-order mixed perturbation
rows from the reviewed load-normal stencil (rows `r_i + ε s_i`, `ε^2 = 0`).
Then `r7 + ε s7 ∈ (r_1 + ε s_1, …, r_6 + ε s_6) R_m[ε]` iff

```text
obs := [ s7 - Σ λ_i s_i ]  =  0   in   N := R_m / ( I·R_m + Syz_m(r1..r6)·s ),
```

where `Syz_m(r)·s = {Σ a_i s_i : (a_i) a syzygy of (r1..r6)}`.  (Compute:
`r7 + ε s7 - Σ λ_i (r_i + ε s_i) = ε(s7 - Σ λ_i s_i)`, and
`ε x ∈ (r_i + ε s_i)` iff `x ∈ I·R_m + Syz·s`.)  **Invariance:** two
multiplier choices `λ, λ'` differ by a syzygy of `(r1..r6)`, shifting the
representative by an element of `Syz·s`; the class is independent of the
choice — this is exactly what the *full* syzygy module buys.  It is
invariant under change of generators of `I`; it is **not** automatically
invariant under change of chart/section — the honesty of the `C6 = 1`,
zero-load section is precisely the open reachability question and stays an
explicit hypothesis (Grok's flag, kept).

Everything needed is already harvested or cheap: V14R1's run recomputed the
**87-generator syzygy module** and its seventh-coordinate projection; the
stencil rows are reviewed input; the class evaluation is small linear
algebra (localize by inverting `h`, or work globally and saturate at `h`).
V14R1's own scope line already names "the next mixed `Lambda<=19`
syzygy-cokernel calculation" — so I label this **a formalization of a
registered step** (the invariant-class statement and its invariance proof
are the delta), not a new avenue.

### 5.3 Cheapest exact discriminator and stop rule

Discriminator: (1) freeze + different-model review of V14R1 (the identity
replay is 37 s exact-Q); (2) one desk-to-small-AWS evaluation of `obs` from
the harvested syzygy module and the frozen stencil, two term orders.
Outcomes: `obs != 0` ⟹ first load-aware, representation-invariant local
exclusion at K00 — the mixed deformation does not extend at first order
(receiver-side cutting result); `obs = 0` ⟹ first-order extension exists —
proceed to the second-order class or the direct mixed membership, and
**do not** infer a germ.  Stop rule: no evaluation before the stencil's
review status is confirmed; one AWS-day cap; on any V14R1 review reversal,
freeze §5 entirely.  Grok's `M2,M4,M6(0)` attainability test is the
zeroth-order companion and merges into the same card.  Firewall (prompt's
instruction, restated): the unloaded local identity licenses **no** closure,
incidence, Taylor-realization, order-two, maximum-twelve, or JC2 claim.

---

## 6. UAC: naturality + three-row syzygy + V45

- **Naturality.**  My hostile review (this round) CONFIRMED the interface as
  a provisional source-transport theorem with two repairable wording items;
  the surviving theorem is unconditional over any `Z[1/2]`-algebra, all
  `(a,c,r)`, via the jet-reindexing reading.  I re-checked the three-row
  syzygies of the second interface by hand this session:
  `C1*g2 - C0c*g1 = (3/8)A1*D`, `C0c*g2 - rho^2*C1*g1 = -(3/8)A0c*D`,
  `(32/3)g4 ± D = {2rho^2C1^2, 2C0c^2}` — all four hold, and the radical
  conclusion `C0c, C1 ∈ sqrt(I[rho^{-1}, A0c^{-1} or A1^{-1}])` follows
  exactly as claimed; it is a clean set-theoretic statement with only
  `rho != 0`, `(A0c,A1) != (0,0)` load-bearing.  Its scope conditions 1–4
  (polar purity through `G`/`T_C2`, target walls `G < 28`, `T_C2 < 32`,
  literal-row bridge) are the right fail-closed gates; the twelve-contact
  list and the wall formulas (`RA^2/L^2` iff `r <= 2d-2`; `A^3/L^3` iff
  `a <= 2d-5`; `k6` at `a >= 7`; `k2` ties) are inventory-mechanical and
  match my review's independent census.
- **V45** is the first executed instance of the generated-map linker pattern
  at a real contact `(2,5,>=3)`: 294 exact coefficient equalities, map
  generated from the pinned `B23` inventory rather than hand-entered, and —
  independent convergence worth recording — its mechanically derived depths
  `p/A/C=3, R=1, k10=2, k6=0, k2=0` are **exactly** the in/out ceilings my
  review's single-jet tagging predicted at `(2,5,3), T=20` before V45
  existed.  Provisional pending its own review; consumes V44R3 custody.
- **Do they remove serial `G22/G24+` exporters from the critical path?**
  **Yes, conditionally.**  The finite outstanding schema/verifier list, and
  nothing else: (1) schema freeze with the seven formulas normative (not the
  `sigma^13` Kummer-hard-coded emitter), tails `d72f774c…`/`6eed03d4…`,
  delays `4/12/20`, targets `28/32/36/38`, alias table (`k2c` vs `k2load`;
  D1AC's reuse of `a1,a0,c1,c0`); (2) recorded compiler-agreement lemmas;
  (3) per-manifest primitive comparison by the linker; (4) generated (never
  hand-written) renaming maps — V45 demonstrates this duty; (5) the frozen
  V0–V4 verifier (~15 s desk prototype exists) plus one different-model
  review, now including Opus's two-sided finite-jet control with my
  review's refinement (raw-valuation upper bounds are sound-but-wasteful
  for all families and **vacuous for `P`-jets**, where the reviewed polar
  inventory is the only nontrivial bound); (6) the `(8,3)` narrow promotion
  or an explicit conditional label, with endpoint status bound to
  promotion-artifact **hashes**, never filenames (the `a8d3` "PROMOTED ROUTE
  FALSIFICATION ONLY" trap).  The three-row linker adds a seventh, parallel
  item for its twelve contacts.  Until those land, `ACT-TOT` custody
  discipline stays; V44R3 stays banked as defense in depth.
- **Firewalls, kept hard:** everything here is strict unique-`AC` on
  `D(rho)`.  No ramified `rho=0`, equality-face, `k=0`, `V(k)`, staged-Rees,
  terminal/receiver, `G2-PSC`/`G2-BD`, Gate-T, order-two, maximum-twelve, or
  JC2 content.  Chamber emptiness remains eleven (plus twelve three-row)
  independent imports with mixed theorem types, never one residue argument.

---

## 7. Whole-inventory rescan, new connections, history checksum

**Disposition deltas that survive cross-examination** (against the four
blind vectors): raise 2 and 31 (three-model convergent; evidence-backed);
row 4 conditional trigger sharpened — V14R1 plus a vanishing `obs` at all
computed orders would make K00 the leading formal-germ candidate, while
`obs != 0` re-kills it (either way row 4 gets its first named experiment);
row 19 — Fable raise vs Opus lower resolves as **capped continue on the
`n=6` corner only** (the two positions differ on share, not on cap/stop;
Sol's Card 3 and my Card F3 are sibling designs — run Sol's gauge-quotient
first, my band extraction as its instrument, two-band stop); rows 16/26 —
idle-capacity fillers, no ledger prior art found (`b-function`,
`primitive group`: zero hits), still unexecuted, keep contingent; row 12
subordinate reopen serving 19 only; rows 7/36/18/41 — Opus's Jelonek
complex, **hold** pending a re-read of the actual paper at the next sweep
(Opus's own caveat; no capacity move on a one-line summary), with the
falsifiable small-`D` prediction ("components containing an automorphism
are generically automorphisms") registered for that day; row 41 reopen
lemma-only endorsed (the refuted `G_m`-purity bridge is exactly the trap the
lemma prevents).

**History checksum, best-effort under ledger drift** (COORDINATION at pin;
APPROACHES/AUDIT/PROGRESS drifted): "two-fibre", "Escape Lemma",
"origin-funnel", "horizontal component", "deformation obstruction",
"syzygy-cokernel" have **no canonical-ledger prior art** under any of those
names; "colon" appears once at the top of the current AUDIT recording this
round's convergence (post-snapshot echo, not prior art); "eliminant" hits
are the pre-existing *instrument* lanes both Fable and Opus already
credited as prior art for the instrument (novelty claimed only for the
theorem and the decision-completeness reading); "Jelonek" appears only as
the long-standing avenue-7/11 topic, not the genericity reading.  Checksum
verdicts: the two-fibre theorem, the eliminant re-adjudication observation,
the `obs`-class formalization (delta over V14R1's registered scope line),
and the Jelonek reading are this round's genuinely new items; everything
else in the four reports is convergence, refinement, or navigation.

**Connections none of the individual reports made** (the assignment's ask):

1. **V14R1's witness feeds the invariant obstruction class directly** —
   `λ = u/h` plus the already-harvested 87-generator syzygy module is the
   complete input for §5.2; no blind report connected the colon witness to
   the deformation cokernel in the invariant form (V14R1's scope line names
   the calculation; the invariance statement is the missing piece that
   makes it representation-independent).
2. **The eliminant lane's existing telemetry already decides the conflated
   case** (§2.2): Opus found the defect; the observation that
   `ELIMINANT_SIZE` + `eliminant_ideal.txt` rescue completed runs without
   relaunch is new here and changes the launch plan (re-adjudicate first,
   relaunch second).
3. **Opus's denominator factorization is the concrete refutation of Grok's
   single-prime skip rule** (§4): two reports, one connection — certificate
   denominators demonstrably carry many small primes, so specialized floors
   need ≥ 2 large primes and stay routing-only.
4. **The certificate converter closes the Fable/Opus disagreement about the
   192-GiB lift** (§2.3): not "never needed" and not "needed" — needed
   exactly on the positive branch in case (ii), for explicitness only, and
   then obtainable more cheaply via §3's bounded per-leaf solves.

---

## 8. Claim matrix

Verdicts: `sound` / `sound-SC` (sound with scope correction) /
`unsupported` / `wrong`.

| # | Source | Claim | Verdict | Note |
|---|---|---|---|---|
| S1 | Sol | Raise 2/31/32; K00 redesign to colon/syzygy + mixed test | sound | convergent; executed (V14R1) |
| S2 | Sol | T-a1 and K00 ladders are one persistence object; one incremental engine | sound-SC | true as mechanism; both ladders now leave the decision path, engine demoted to materialization/fallback |
| S3 | Sol | Card 1 colon criterion `(I:r7) ⊄ m` via syzygy projection | sound | = Escape Lemma; triple-convergent; V14R1 is its execution |
| S4 | Sol | Card 2 seeded `N=7` persistence chain | sound-SC | engineering sound; decision-dominated; fallback only |
| S5 | Sol | Card 3 AS109 gauge-conductor at W2/W3 | sound | orthogonal; capped; merge with Fable F3 (Sol's design leads) |
| S6 | Sol | "Find the minimal exponent or a direct eliminant" as bottleneck 2 | sound-SC | the minimal exponent is not part of the question (Thm 1); the eliminant half is the whole question |
| F1 | Fable | §3.1 two-fibre lemma + both-direction decisiveness | sound | proved here as Theorem 1; blind proof sketch was correct but under-specified on descent and did not exhibit the homogeneity counterexample |
| F2 | Fable | Certificate converter "follows by tracing … rehomogenization" | sound-SC | complete only for `e(0) != 0`; the `t`-divisible case needs §2.3's `N = D + 2kN0` with an explicit `N0` — the case Opus's §6.2 exposes |
| F3 | Fable | Special half already computed; selected rows sound for unit conclusion | sound | now source-verified: 17 literal `Tg` rows; added sharpening: rows in `K` suffice, other-variable localization does not |
| F4 | Fable | §3.3 origin-funnel: every survivor component passes through the total origin | sound-SC | conclusion correct; blind proof was sloppy for horizontal components; repaired here (cone + dominant-image closure argument) |
| F5 | Fable | Card F2 jet cross-validation "agree coefficientwise with 273/492-entry lifts" | sound-SC | overstated: lifts unique only mod syzygies; correct check is valid-lift, not entrywise equality |
| F6 | Fable | Stage-2 exact-`Q` at one rational `c` is "decisive-grade" | sound-SC | one-sided-strong only (unit direction); non-unit at one `c` is weak (vertical components) |
| F7 | Fable | Naturality hostile review verdicts (jet-map repair; `P`-jet vacuity; a8d3 trap; V0–V4) | sound | V45's depths match the review's independent tagging exactly |
| G1 | Grok | Sandwich `7 <= N_J0 <= N_17` (custody-conditional) | sound | correctly hedged; now decision-dominated; ceiling relevant to materialization only |
| G2 | Grok | Specialized nonmembership at one prime ⟹ `Q`-nonmembership; skip exact `N` | wrong | bad primes; V43's own denominator carries many small primes; repaired ≥2-prime version is sound routing only |
| G3 | Grok | 17 rows may not lie in `J0` (presentation hazard) | sound-SC | right demand, empirically discharged: `SELECTED` are literal frozen rows (source-read this session) |
| G4 | Grok | Infinitesimal special-fibre calculus; nested chain; duals transport only where test monomial survives | sound | good scope dictionary; decision-dominated but retained as discipline |
| G5 | Grok | Card B: attainability before D9; stop unloaded increments after two compatible degrees | sound-SC | attainability keeps; the D-ladder fate is now decided by V14R1 rather than by a redesign heuristic |
| G6 | Grok | V11/V13 = software evidence; one bounded Mora repair attempt | sound-SC | first half sound; the repair attempt is superseded — colon route answers the question with no local ordering |
| G7 | Grok | Homogenization caution: "inhomogeneous slices can lie" | sound-SC | legitimate in general (FM1 is the witness); discharged for this lane by enforced homogeneity + Theorem 1 |
| O1 | Opus | Escape Lemma + ladder corollary | sound | textbook, correctly applied |
| O2 | Opus | Theorem A (generic fibre decides, given `a1 ∈ sqrt J0`) | sound | independently re-proved here; identical content to F1 |
| O3 | Opus | Exponent ladder guaranteed to reach uninformative positive branch | sound | given promoted `a1 ∈ sqrt J0` |
| O4 | Opus | Card A self-contained on 17 rows; "does not even consume V42" | sound-SC | correct given rows-in-`J` custody (now verified); the sufficiency weakening (rows in `K`) and the FM3 hazard deserve explicit statement in the lane scope |
| O5 | Opus | §6.2 outcome-token conflation defect | sound | byte-verified; plus post-hoc rescue via `ELIMINANT_SIZE` (new here) |
| O6 | Opus | Toy `J = (f - t x)` as mandatory pipeline negative control | sound | seconds; adopted in M1 |
| O7 | Opus | Jelonek: CE locus open ⟹ dense in component; reframe avenue 36 | sound-SC | valid deduction *conditional on the one-line sweep summary*; Opus says so itself; hold until the paper is re-read |
| O8 | Opus | §4.2 self-refutation of the `G_m`-purity bridge | sound | the refutation is correct and worth filing |
| O9 | Opus | Avenue 19 lower | sound-SC | resolves against Fable's raise as capped-continue on the `n=6` corner; a share dispute, not a math dispute |
| O10 | Opus | 14-lane census: no lane ever computed the generic-`rho` object | sound | load-bearing navigation fact behind M1's priority |
| O11 | Opus | V43 hostile review (PASS + REPAIRABLEs; 7.3 corollary; V42 branch-ideal correction; mutation-control quantification) | sound | high quality throughout; nothing found to reverse |
| P1 | Packet | 17-row unit ⟹ some higher exponent exists in the special fibre | sound | for the subideal, rows literal (verified); exponent itself not exhibited |
| P2 | Coordinator | V14R1 endpoints pass incl. fresh replay of `-h*r7 + Σ u_i r_i = 0`, `h = 63*d4+20` | unsupported→provisional | consistent with the on-disk producer RESULT (read this session, "AWAITING DIFFERENT-MODEL HOSTILE REVIEW"); not promotable until frozen + reviewed, per prompt |
| V45 | Producer | Exact source/D1 finite-jet identity + custody composition at `(2,5,>=3)` | sound-SC | exact producer evidence; contact exclusion remains provisional pending Opus review; depths independently corroborated by F7 |

---

## 9. Strongest unique contributions and independent convergence

After deduplication:

- **Sol** — the *executed* colon/syzygy design and its custody discipline:
  V14R1's 87-generator syzygy module, seventh-coordinate projection, and
  fresh-process replay realize Sol's Card 1 exactly; plus the standing
  production doctrine (separated solve/certify paths, full unrestricted
  replay as the endpoint gate) that made V43 survive hostile review.
- **Fable** — the four-way two-fibre formulation with the dehomogenized
  halves, the observation that the special half is already in hand, the
  origin-funnel theorem (every survivor component passes through the
  terminal origin — the structural reason receiver work is load-bearing
  under *either* M1 outcome), and the UAC hostile review whose jet-ceiling
  tagging V45 then reproduced exactly.
- **Grok** — the custody-attack catalogue (row-provenance hazard,
  homogenization caution, seeded-dual fail-open, `ez9` live-in-`J`/dead-in-
  `J0`, weight-35 non-finality, prefix-fragility of negatives): the best
  single checklist of the round; most of M1's fail-closed gates trace to it.
- **Opus** — the Escape/Theorem-A instrument-level identification (the
  `E != 0` weakest predicate, the §6.2 defect, the toy control, the
  preflight), the 14-lane `rho=0` scope census, ladder hygiene as a
  portfolio gate, and the V43 review's forensic artifacts (discriminating
  census, denominator factorization, 4.29 % mutation-control
  quantification, V42 branch-ideal correction).

Independent convergences that raise confidence: (i) the two-fibre/generic-
fibre decision — Fable and Opus blind, third derivation here; (ii) the
K00 colon — Sol, Fable, Opus blind, executed as V14R1; (iii) the ladder
critique — all four, sharpest in Opus; (iv) the UAC linker path — all four
plus V45 plus the Fable review, with the V45-depths/tagging match as a
quantitative cross-check.

---

## 10. Merged idea cards (four)

### M1 — `TA1-GENERIC-FIBRE-DECISION` (launch now)

- **Target.**  `Ê != 0` for the 17-row dehomogenized subideal (escalate to
  all 59 on a subideal zero); by Theorem 1 + the gating special control this
  decides `K + (rho) = (1)` in both directions.
- **Dependencies.**  Theorem 1 (triply derived; enqueue one cheap external
  check with the launch); the §2.2 predicate repair (three tokens + scope
  bit) — but **first re-adjudicate any completed/running `no-unit-eliminant`
  output from its harvested `ELIMINANT_SIZE`/`eliminant_ideal.txt` before
  relaunching anything**; row custody verified (literal `Tg` rows); shared
  emitter-chain residual risk disclosed (§4).
- **Cheapest discriminator.**  Harvested-telemetry re-adjudication (free);
  then modular `t0` preflights (minutes); then the exact `Q(t)`/`Q[t]`
  run.
- **Controls.**  Opus toy `J = (f - t x)` must report nonempty; `t=0`
  special control must pass (positive); corrupted-row flip; two independent
  `t0`; low-grade-only row subset must return non-unit (negative).
- **Both outcomes.**  *Unit/nonzero eliminant:* the frozen ordered `T-a1`
  chart closes; cancel `N=7`/w35, DVR syzygy, high-memory exponent retries;
  materialize the certificate directly if `e(0) != 0`, else via §2.3+§3
  (bounded per-leaf solves; policy call whether decision-tier suffices).
  *Full-system zero eliminant:* `K + (rho) != (1)` — first honest survivor
  geometry: extract the horizontal component, parametrize it centered at
  the total origin (origin-funnel), unhold grade-20+ row exports with
  purpose; prefix-relative.
- **Resource.**  AWS small-to-medium; hours-scale expected.
- **Stop rule.**  Two orderings + modular-first strategy exhausted on both
  17-row and 59-row systems within registered caps ⟹ fall back to the
  seeded `N=7` dual and the ≥2-prime specialization floor-raiser, both
  labeled floor-only.
- **Scope firewall.**  Frozen grade-≤19 chart only; closing it says nothing
  about receiver, coverage, `G2-*`, Gate T, or JC2; a negative is
  prefix-relative.

### M2 — `K00-LOCAL-FORK-AND-FIRST-OBSTRUCTION` (launch now)

- **Target.**  (i) Freeze + different-model review of V14R1; on
  confirmation, terminate the `(d)`-adic ladder as discovery (D8 review
  completes as lifecycle; D9+ stops).  (ii) Evaluate the invariant
  obstruction class `obs = [s7 - Σ λ_i s_i] ∈ R_m/(I R_m + Syz·s)` (§5.2)
  for the reviewed mixed stencil.  (iii) Grok's `M2,M4,M6(0)` attainability
  as the zeroth-order companion.
- **Dependencies.**  V14R1 artifacts (witness + 87-generator syzygy module,
  already harvested); reviewed stencil status confirmed before any `obs`
  evaluation; no D8 dependence.
- **Cheapest discriminator.**  The V14R1 review itself (37-s exact-Q
  replay); then small linear algebra for `obs`, two term orders.
- **Both outcomes.**  `obs != 0`: first load-aware, representation-invariant
  local exclusion at K00 — a genuinely cutting receiver-side result.
  `obs = 0`: first-order mixed extension exists; escalate to second order or
  direct mixed membership; no germ inferred.  V14R1 review reversal:
  freeze the card; local question reopens; do **not** resurrect V11/V13.
- **Resource.**  Desk to small AWS.  **Stop.**  One AWS-day; stencil-custody
  gate strict.
- **Scope firewall.**  Unloaded local identity ⟹ no closure/incidence/
  Taylor/order-two/max-twelve/JC2 claim; section honesty (`C6=1`, zero
  loads) is an explicit hypothesis, not a conclusion.

### M3 — `UAC-SCHEMA-VERIFIER-FREEZE` (launch now, desk)

- **Target.**  Freeze the schema object and the V0–V4 verifier (with the
  two-sided finite-jet control, `P`-jet exception, hash-bound endpoint
  status, generated renaming maps); one different-model review; then retire
  serial `G22/G24+` exporters from the critical path; three-row linker for
  its twelve contacts as the complementary route; V45 and chamber reviews
  continue in background.
- **Dependencies.**  §6's six-item list; nothing else.
- **Cheapest discriminator.**  The verifier run (seconds–minutes, desk).
- **Both outcomes.**  Pass ⟹ endpoint manifests replace exporters; any
  layer-2 mismatch ⟹ transport unlicensed for that chamber only, exporters
  resume there; either way the eleven+twelve emptiness imports keep their
  own lifecycles.
- **Resource.**  Desk.  **Stop.**  One review cycle; no growth into a
  framework.
- **Scope firewall.**  `D(rho)` strict unique-`AC` only; no ramified,
  equality-face, `k=0`, Rees, receiver, `G2-*`, Gate-T, or coverage claim.

### M4 — `LADDER-HYGIENE-AND-ORTHOGONAL-FILLERS` (continue, capped)

- **Target.**  Install Opus's ladder-hygiene registration (termination
  proof, escape reformulation, or explicit negative-info budget) —
  retroactively: `T-a1` exponent ladder → fallback-only; K00 D-ladder →
  terminated on M2(i); AS109 floors → budgeted, `n=6` corner only, Sol's
  gauge-conductor (W2/W3, two-band stop) as the next rung with my band
  extraction as its instrument.  Idle-capacity fillers: row 16 one-afternoon
  b-function test; row 26 primitive-group database run; row 9 V43-compiler
  retarget.  Jelonek: registered prediction, no capacity until the paper is
  re-read.
- **Cheapest discriminator.**  Each item is its own one-shot.
- **Both outcomes.**  Fillers either produce a named object or bank a null
  result with an object; hygiene either reclassifies lanes (install) or
  costs a day (drop).
- **Resource.**  Desk/idle only; zero AWS-algebra-quota contention.
- **Stop.**  Per-item one-shot budgets; AS109 two-band stop; no degree-2–5
  or unconstrained-support searches.
- **Scope firewall.**  No filler output feeds a landing-lane conclusion
  without its own review.

---

## 11. Decisions (wall-clock-optimized, nonblocking review)

**Launch now.**  M1 (telemetry re-adjudication first, then predicate-fixed
runs); M2(i) V14R1 freeze/review and M2(ii) `obs` preparation; M3 schema +
verifier freeze.

**Continue in background.**  D8 hostile review (lifecycle only); V45
different-model review; `(2,3,>=2)`/`(2,4,>=3)` transport reviews; V44R1
chamber endpoint; TD6 H19R2 to caps; mixed `Lambda^19` lanes; web-sweep
clock (`2026-08-28T00:00Z`); M4 fillers as capacity allows.

**Hold.**  Seeded `N=7`/weight-35 dual (fallback only, M1 stop-rule
trigger); Jelonek/avenue-36 reframe (until the paper is re-read); full
`3P-E31` (firewall stands); grade-20+ row exports (unhold only on an M1
full-system negative, with the survivor-parametrization purpose).

**Merge.**  Fable F1 + Opus A + Sol eliminant lanes + Grok custody gates →
M1.  Sol Card 1 + Fable F2 + Opus B + V14R1 + Grok attainability + the §5.2
obstruction class → M2.  Naturality + three-row + V45 → M3.  Opus hygiene +
Sol Card 3 + Fable Card F3 + fillers → M4.  Sol's persistence engine folds
into M1's materialization branch only.

**Stop.**  192-GiB/1-TiB whole-unit multiplier extraction as an exponent
hunt (reclassified: conditional bounded materialization per §2.3/§3 only);
K00 D9+ as discovery (on M2(i) confirmation); V11/V13 local-order repair
(superseded; do not repair the Mora transform); serial `ACT-TOT-G22/G24+`
as critical path (on M3 completion; V44R3 stays banked); unseeded weight-35
dual from scratch; the `a1`-exponent ladder as a decision lane.

---

## 12. Does Opus add significant correctness-adjusted unique capability beyond Fable?

**Yes.**  The core theorem was independently convergent (both models found
it blind, equal credit), but Opus additionally: (i) audited the *live lane
source* and found the §6.2 outcome-token defect — the single most
actionable finding of the round, which my blind submission missed because I
specified the pipeline without reading the deployed predicate; (ii) ran the
14-lane scope census establishing that no lane had ever computed the
generic-`rho` object — the fact that makes M1 the top priority rather than
one option among four; (iii) delivered a hostile review of V43 whose
techniques (generating-function census that discriminates alphabet size,
denominator factorization, mutation-control power quantification, the V42
branch-ideal scope correction) are now reusable campaign instruments.
Correctness-adjusted: essentially no errors this round; its two claims
needing scope correction (O4's custody nuance, O7's conditionality) were
either self-flagged or minor.  The profiles are complementary rather than
redundant — Opus strongest at artifact-level/code-level forensics, Fable at
theorem-level formulation and formal-series review depth (the V45 ↔ F7
match is the concrete evidence).  Recommendation: retain Opus, and pair the
two profiles on load-bearing reviews (one takes the algebra, one takes the
bytes) rather than serializing them.

---

## 13. Global non-claims

Nothing in this file proves or disproves JC2, Gate T, order two, maximum
twelve, `G2-PSC`, `G2-BD`, source/landing coverage, the terminal/Taylor
receiver, the ramified `rho=0` fibre, or any cofinal degree/type bound.
Theorem 1 concerns the frozen grade-through-19 ordered `T-a1` chart only.
V45 and V14R1 remain provisional pending their different-model reviews; the
coordinator's V14R1 delta statement was used only as provisional context.
No promoted claim is contradicted; the only defect asserted is the §6.2
reporting logic (verified from source), and the only blind-round claims
corrected are the scope corrections tabulated in §8, including four against
my own submission (F2, F4, F5, F6).

---

## 14. File-read / tool / edit disclosure

- **Hash verification:** `shasum -a 256` over all fourteen prompt-listed
  files (all matched); drift check over `APPROACHES.md`, `AUDIT.md`,
  `PROGRESS.md`, `COORDINATION.md` (only COORDINATION at pin).
- **Files read in full:** the fourteen prompt-listed files; additionally
  `cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dehom_eliminant_v43.py`
  (predicate and row-provenance verification) and
  `cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/RESULT.md`
  (provisional-status characterization).  Directory listings of the V14R1
  and V43 case directories.
- **Searches:** keyword greps over `APPROACHES.md`, `AUDIT.md`,
  `PROGRESS.md`, `notes.md` for the §7 history checksum (colon, eliminant,
  generic fibre, Jelonek, b-function, Bernstein, primitive group,
  syzygy-cokernel, Escape Lemma, two-fibre, deformation obstruction,
  origin-funnel, horizontal component), plus three context greps.
- **Computation:** hand algebra only — Theorem 1 and its counterexamples,
  the FM1 witness, the §2.3 converter, lemmas C1–C4, the §5.2 invariance
  argument, and re-derivation of the four three-row syzygies.  No AWS, no
  web access, no heavy or light CAS execution, no Singular/msolve/FLINT.
- **Not touched:** `jc2-lean` (not entered, read, built, or
  status-inspected); no canonical ledger, case artifact, or xmodel file
  edited or created other than this report.
- **Written:** exactly one repository file —
  `xmodel/ideation-20260827T0935Z-fable5-crossreview.md` (this file).
