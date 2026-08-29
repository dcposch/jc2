# Hostile review (Fable5): ordered `T-a1` rho=0-to-total DVR design

Date: 2026-08-27
Reviewer: Fable5, different-model hostile lane
Reviewed artifact:
`xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-sol-20260827.md`
SHA-256 (verified locally):
`e3d263d5c0006bc4f05c5b7ff17bfcbd68bab52f7c1d3ccb5d323facd94448f7`

Session constraints honored: desk-scale exact checks only; no AWS launch, no
web access, no `jc2-lean` contact, no canonical-ledger edit, no campaign
artifact modified.  All review scripts were staged under `/tmp` (hashes in
the appendix).  The locally installed Singular 4.4.1 was used **only** for
seconds-scale syntax probes on one- and two-column toy modules; no live
system was reduced.

## Verdict summary

| item | verdict |
|---|---|
| 1. Ambient ring `S=Q[rho,X_19]`, weight-zero census, `K=J:a1^infinity` chart identification | **CONFIRMED** |
| 2. Specialization inclusion `sp(J:a1^infinity) subseteq sp(J):a1^infinity`, direction and strictness | **CONFIRMED** |
| 3. Four-way certificate equivalence (`K+(rho)=(1)` iff typed `a1^N*U(rho^2) in J`, `U(0)=1`) | **CONFIRMED** |
| 4. Homogeneous even toy counterexample `(f-rho^2*x)` | **CONFIRMED** |
| 5. Fixed-weight `Q[t]_(t)` module/colon/syzygy criterion and pruning | **CONFIRMED** |
| 6. W30 launch design (`N=6` floor, rho-zero gate ordering) | **CONFIRMED as mathematics; GAP in the registered V43 compiler** — invalid Singular `syz(module,vector)` calls in the generated toy-control preamble make the DVR lane fail closed; two-line repair required before launch |

No presentation map is missing.  The single defect found is an
implementation bug in the not-yet-frozen V43 compiler; it is fail-closed
(`NO VERDICT`), never unsound.  The AWS job **must not launch the DVR lane
as compiled**; the rho=0-gate portion is sound as is.  The smallest repair
is given in section 6.4.

---

## 0. Custody and inputs actually re-verified

- Producer design SHA re-hashed and matched (`e3d263d5...`).
- V42 citations resolve exactly: report `5d4c42ff...` =
  `xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-sol-20260827.md`,
  replay `f4ec7293...` = `replay_a1_cascade_closure_v42.py`, frozen
  `RESULT.json` = `01b8edd2...`.  The V42 promotion is the current top
  AUDIT.md entry (Opus5 hostile-review confirmed, 2026-08-27 08:02Z).
- Staged-calculus theorem `16ec6f54...` (forward promoted) and converse
  correction `593f953b...` (strong converse withdrawn) read in AUDIT.md.
- V38 promotion (sixteen `a1^i*k^j`, `i>=1`, `5i+4j<=25` exact-Q
  nonmembers; weights through 19 final, 20–25 prefix-relative) and V39
  (`Tg19_7` genuinely new weight-19 condition) read in AUDIT.md.
- The full 70-file frozen general-rho row corpus was independently
  re-loaded through the same hash pins the V37 loader uses (V23 parser
  `14f2de22...`, V23 `output_r1/RESULT.json` `ce4d0adb...`, V28/V30/V33/V35
  compiled `result.json` pins), **without** the rho→0 kill, by a fresh
  script (`/tmp/check_design_v43_structure.py`).  Every one of the 70
  per-row file hashes matched its frozen record.

## 1. Ambient ring, weight-zero census, and chart identification — CONFIRMED

**Independent structural findings on the actual frozen bytes** (all 70
general-rho rows, grades 10–19, rows 1–7):

- Distinct variables occurring: **66 = 65 positive-sigma-weight variables
  plus `rho`**.  `rho` is the **only** weight-zero variable present.  In
  particular `qa1` (the `T-a0` ratio, sigma weight 0 in the parser's fixed
  table) occurs nowhere, and no `q`-type a1-chart ratio occurs at all.
- Every monomial of every row is sigma-homogeneous of exactly its grade
  under `wt(rho)=0` (0 violations in 6,167 rho=0-surviving terms plus all
  rho-carrying terms).
- Every `rho` exponent is **even**; the maximum is `rho^8`.  So the rows
  lie in `Q[rho^2][X_19]` literally; the design's parity hypothesis is a
  fact of the bytes, not an assumption.
- rho=0 images: exactly the promoted V37 census — 51 nonzero rows, grade
  row/term counts `(11:1/1, 12:4/9, 13:5/28, 14:6/75, 15:7/187, 16:7/424,
  17:7/867, 18:7/1647, 19:7/2929)`, 65-variable census.
- `wt(a1)=5`, `wt(k)=4`, consistent with the V38 `5i+4j` target grid and
  with `w=5N=30` at `N=6`.
- Two censuses the design text leaves implicit, now pinned:
  (i) **no positive-weight variable occurs only in rho-carrying terms** —
  the general-rho variable set equals the rho=0 set, so `X_19` is the same
  65 variables on both sides; (ii) **eight rows are nonzero at general rho
  but vanish at rho=0**: `Tg11_2, Tg11_3, Tg11_5, Tg11_7, Tg12_5, Tg12_7,
  Tg13_7, Tg14_6` (59 nonzero general-rho rows total; 11 identically zero:
  all of grade 10 plus `Tg11_4, Tg11_6, Tg12_6, Tg13_6`).  Point (ii) is a
  real trap: the fixed-weight matrix `A_w(t)` must be built over the **59**
  general-rho rows, not the 51 the V37 loader returns.  The design's §1
  definition of `F_{g,r}` (general-rho emitter output) is the correct one,
  and the registered V43 compiler does build from the general-rho rows
  (`total_rows` keeps every nonzero `t`-form, including the eight
  rho=0-dead rows).  Any future reimplementation that reuses
  `v37.load_rows()` output for the total matrix would be wrong.

**Chart presentation.**  V23 builds the `a1_ordered` rows literally as
`specialize(row, J1 ∪ {a0}, {})` — the source rows with
`rs=cs=c0=c1=a0=0` killed and nothing else — matching the design's stated
source quotient.  The design's derivation of `K=J:a1^infinity` from the
unreduced second-stage presentation is exact:

- In `Q[rho, all vars, q]` the ordered a1-chart ideal is
  `(q, a1*q-a0, rs, cs, c0, c1, rows)`.  Since `q` is a generator,
  `a1*q-a0 ≡ -a0 (mod q)`, so the ideal equals
  `(q, a0, rs, cs, c0, c1) + (rows)`; the displayed variables are a
  coordinate ideal, and colon/saturation commute with the quotient by a
  coordinate ideal contained in the ideal.  Eliminating leaves exactly
  `J ⊂ S=Q[rho,X_19]` and the honest chart `C=S/(J:a1^infinity)`.
- The stated equivalence "`q=0` equivalently `a0=0` after `a1`-saturation"
  is exact both ways: `(…,q) ∋ a0` directly via the bilinear, and
  `(…,a0):a1^infinity ∋ q` since `a1*q ∈ (…,a0)`.
- **No omitted generator.**  Strict-transform/divided rows are absorbed:
  if `a1^m*G = F ∈ J` then `G ∈ J:a1^m ⊆ K`; defining the chart by
  saturation rather than by a generator list is precisely what makes the
  divided-row objection (which was live for the unsaturated `T-cs`
  E-fibre) vacuous here.  No first-stage ratio or Rabinowitsch variable
  belongs on this stratum: the `J2` stage sits over `V(J1)` in the source
  (the staged `J1`-then-`J2` tree of `16ec6f54...`), not inside a
  first-stage chart, and `J2=(a0,a1)` has exactly the two charts, with the
  terminal receiver holding `a0=a1≡0`.
- **The ordered restriction is load-bearing.**  On the *standard*
  (non-ordered) a1-chart the ratio `q=a0/a1` survives with sigma weight
  `5-5=0`; then `S_0=Q[rho,q]`, the weight-zero projection is no longer
  univariate, and the entire `Q[t]_(t)` reduction collapses.  Only the
  ordered equation `q=0` eliminates it.  The design says this implicitly
  ("the only weight-zero variable left **on this ordered stratum**"); it
  is confirmed and should be kept as a hard precondition on any successor
  chart.
- Scope: `J` is the grade-≤19 truncation, so `K+(rho)=(1)` closes the
  frozen chart only; more equations can only shrink the chart further, so
  a positive certificate is monotone-safe.  The design's scope paragraph
  states exactly this.

## 2. Specialization map and inclusion — CONFIRMED

Direction: for `g ∈ K=J:a1^infinity` pick `N` with `a1^N*g ∈ J`; applying
the ring map `sp` (which fixes `a1`) gives `a1^N*sp(g) ∈ sp(J)=J0`, so
`sp(g) ∈ J0:a1^infinity`.  Since `sp` is surjective with kernel `(rho)`,
`(K+(rho))/(rho) = sp(K)`, giving inclusion (4) of the design **in the
stated direction**.  Strictness is witnessed by the toy of section 4:
`sp(J_toy:f^infinity) = (f) ⊊ (1) = sp(J_toy):f^infinity`.

The design's citation of V42 as the right-hand side is accurate and does
not overreach: the promoted V42 verdict is "no point with `a1 != 0` over
every characteristic-zero field," which by the Nullstellensatz over the
algebraic closure plus membership descent gives `a1^N ∈ J0` for some
**non-effective** `N`, i.e. `J0:a1^infinity = (1)`.  The design correctly
records that the displayed `a1^8` is only a branch-ideal certificate (it
lives in `J0 + (e0,e1,ee0,ell1,rs1)`, not `J0`), and correctly refuses the
withdrawn strong converse: the specialized unit is treated as a screen,
never as closure of `K+(rho)`.

## 3. Four-way certificate equivalence — CONFIRMED

I re-derived every leg independently.

- **(2)⇒(1)** is elementary and does not even need the promoted theorem:
  `a1^N*(1+rho*W) ∈ J` gives `1+rho*W ∈ J:a1^N ⊆ K`, and
  `1 = (1+rho*W) - rho*W ∈ K+(rho)`.
- **(1)⇒(3), the load-bearing step.**  `J` is generated by
  sigma-homogeneous rows (verified on the bytes) and `a1` is homogeneous,
  so `K=J:a1^infinity` is homogeneous for the positive grading whose
  graded pieces are `Q[rho]`-modules.  From `1 = k + rho*h` with `k ∈ K`,
  the weight-zero component gives `k_0 = 1 - rho*h_0 ∈ K ∩ S_0`, and
  `S_0 = Q[rho]` **exactly because rho is the only weight-zero variable**
  (section 1).  So `U(rho):=k_0 ∈ K ∩ Q[rho]`, `U(0)=1`, and saturation
  supplies `N` with `a1^N*U ∈ J`.  This is where the empirical weight-zero
  census carries the whole design.
- **(2)⇒(3) directly**: projecting an identity `a1^N*(1+rho*W) = Σ h*F`
  to weight `5N` keeps the left side intact (it is homogeneous of weight
  `5N`) and replaces `W` by its weight-zero part `W_0(rho) ∈ Q[rho]`.
- **(3)⇒(4)**: the involution `rho ↦ -rho` fixes every row (even parity
  verified on all 70 files, maximum exponent `rho^8`), hence fixes `J`;
  averaging `U(rho)` and `U(-rho)` stays in `J`-membership and keeps
  `U(0)=1`, and the even part is a polynomial in `t=rho^2`.
- **(4)⇒(2)**: `U(t)-1 ∈ (t)` makes `W=(U(rho^2)-1)/rho` a polynomial
  (indeed `rho | W`), which is the displayed normalization.

**Consistency with the converse correction `593f953b...`.**  There is no
conflict.  The withdrawn converse failed because a *cleared containment*
`f^N*s^m ∈ J+(rho)` does not make the rho-cofactor divisible by the
cleared monomial.  The design never clears a containment mod `(rho)`: it
extracts the weight-zero graded component of an exact unit decomposition
in `K+(rho)`, and homogeneity plus `S_0=Q[rho]` make that component
*itself* the certificate cofactor.  In the staged typing the result is
exceptional power `a1^N`, **genuine localizer `s=1`**, rho factor
`1+rho*W`: nothing is localized, no `V(s)` residual stratum is created,
and condition (1) is the honest saturated-chart statement, not a
specialized or localized-fibre unit.  The toy of section 4 is coherent
with the equivalence: there, all four conditions fail together, while the
*specialized* unit holds — exactly the gap the equivalence does not (and
must not) bridge.

## 4. Homogeneous even toy counterexample — CONFIRMED

`S_toy=Q[rho,f,x]`, `wt(f)=wt(x)=1`, `J_toy=(f-rho^2*x)`:

- `f-rho^2*x` is homogeneous (weight 1) and even in rho — it does share
  both structural properties of the live source, so the toy really proves
  neither property alone repairs the specialization/saturation gap.
- `S_toy/J_toy ≅ Q[rho,x]` (a domain) with `f ↦ rho^2*x ≠ 0`, so
  `J_toy:f^infinity = J_toy`: already saturated.  `sp(J_toy)=(f)`, so
  `sp(J_toy):f^infinity=(1)` — the V42-shaped specialized unit holds.
- No `f^N*(1+rho*W) ∈ J_toy` for any `N`: in the domain quotient the image
  is `rho^{2N}x^N*(1+rho*Wbar)`, a product of nonzero factors
  (`1+rho*Wbar` is nonzero because its `rho=0` value is 1).  Verified.
  Hence `K_toy+(rho)=(f,rho)≠(1)`: strict failure of both specialization
  commutation and the withdrawn converse, exactly as claimed.
- The fixed-weight-one module data check out: basis `(f,x)`, single column
  `(1,-t)^T`, target `(1,0)^T`; the target is `A(0)*1` at `t=0`, the first
  correction residual is `t*(0,1)^T` with `(0,1)^T` outside the image; the
  syzygy module of the augmented pair is zero, so the colon is `(0) ⊆ (t)`
  and every exponent is obstructed — this is the exact failure mode the
  live discriminator must detect, and (section 6) the V43 preregistration
  wires this very module in as the mandatory engine negative control.
- One cosmetic slip: "retains the entire `f=x=0` exceptional direction"
  misdescribes the honest fibre, which is `V(f,rho)` — the free `x`-line
  with `f=0` — not `f=x=0`.  The algebra around it is correct; no
  consequence is drawn from the phrase.

## 5. Fixed-weight DVR module/colon formulation — CONFIRMED

- **Completeness of the fixed-weight reduction.**  Suppose
  `a1^N*U(rho^2) = Σ h_{g,r} F_{g,r}` in `S`.  Projecting to weight
  `w=5N` replaces each `h` by its weight-`(w-g)` part, a `Q[rho]`-linear
  combination of the positive-variable monomials `B_{w-g}`; taking the
  rho-even part (rows are even, left side is even) leaves `Q[t]`
  coefficients, the odd part being a syzygy that can be discarded.  So a
  typed exponent-`N` certificate exists iff `b_N ∈ im(A_w) ⊗ Q[t]_(t)`,
  iff `(im(A_w):b_N) ⊄ (t)`.  Conversely any `Q[t]`-certificate maps to
  `S` under `t ↦ rho^2`.  Multipliers never need `rho` (it lives in the
  `Q[t]` coefficients) nor variables outside the 65 (fresh-variable terms
  cancel degree-wise).  Exact both ways.
- **Syzygy-colon identity.**  The projection `Syz([A_w|b_N]) → Q[t]`,
  `(u,v) ↦ v`, is `Q[t]`-linear with image exactly `(im(A_w):b_N)`
  (`v*b_N = -A_w u` one way; lift any colon element the other way), so
  generators of the syzygy module have last coordinates generating the
  colon.  Because `(t)` is prime, "the whole colon lies in `(t)`" can be
  read off generator-wise, and one generator with `v(0)≠0` yields, after
  the rational scaling `1/v(0)`, both `U(t)` with `U(0)=1` and all row
  multipliers.  The syzygy vector is a bona fide replayable certificate
  for the **positive** outcome.
- **Support-component pruning is exact** provided incidence is computed
  over the `Q[t]`-supports (a coordinate that is a nonzero polynomial in
  `t` counts as an edge even if it vanishes at `t=0`): columns outside the
  target's connected component touch no basis row of the component, so
  their contribution to any solution restricts to an outside syzygy and
  can be dropped; restricted solutions extend by zero.  The registered
  V43 compiler does compute the total component on the `t`-form supports
  and a *separate* component for the `t=0` gate — both correct.  A
  reimplementation that pruned the total system on `t=0` supports would be
  wrong; flagging for successors.
- **The `t=0` gate is exact and final for negatives.**  At rho=0 every
  variable has positive weight, `J0` is homogeneous, so `a1^N ∈ J0` is
  decided by weight-`5N` linear algebra over `Q` with the complete
  complementary product set, and an exact rational separating functional
  is a final negative certificate for that exponent (specializing any
  typed identity at rho=0 gives `a1^N ∈ J0`).  Confirmed.
- **One evidentiary asymmetry to record** (design already tiers it, I
  make it explicit): a *negative* DVR outcome at the syzygy stage has no
  freestanding replay certificate — it rests on the engine returning a
  complete generating set of `Syz([A_w|b_N])`.  The exact-Q lane plus the
  independent finite-field lane is acceptable for a stop-and-report
  discriminator, but a promoted *obstruction* claim at some future `N`
  would need either a second independent syzygy engine or a posted
  cokernel-torsion witness.  Positive outcomes are fully replayable.

## 6. W30 launch design — mathematics CONFIRMED; registered compiler GAP

### 6.1 The `N=6` floor is sound

A typed exponent-`N` certificate specializes at rho=0 to `a1^N ∈ J0`.
The promoted V38 floor gives exact-Q nonmembership of `a1^i` for
`i=1..5` in exactly this `J0` (the grade-≤19 prefix ideal): weights
through 19 are final, and the weight-20 (`a1^4`) and weight-25 (`a1^5`)
statements are prefix-relative — which is precisely the ideal `J0` in
play, so relativity costs nothing here.  Hence no typed certificate
exists for `N≤5` and the first permitted exponent is `N=6` at weight 30.
The V42 promotion guarantees *some* `N` works for the rho=0 membership
(non-effectively); nothing guarantees `N=6` does, and the design correctly
labels the run a discriminator with result pending.

### 6.2 The gate ordering is logically sufficient

rho=0 nonmembership at weight 30 ⇒ final negative for exponent 6 (exact
separating functional; no DVR solve needed).  rho=0 membership is
necessary-only; the toy is the exact witness that the DVR stage can still
obstruct, so the design's "gate first, then univariate solve" ordering is
the correct and complete decision procedure for the fixed exponent.
Obstruction at `N=6` refutes nothing about `K+(rho)`; the stop-and-report
rule before any `N>6` is the honest reading and is preregistered.

### 6.3 Registered V43 compiler: independent audit findings

`cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/`
(preregistration `97fa7074...`, compiler `90b01406...`, validator
`5a737941...`; **no FREEZE.sha256 exists yet** at review time).

Correct and verified against the design:

- pins the design (`e3d263d5...`), V42 report/replay/RESULT, V35 emitter
  chain, and V37 loader by SHA; re-derives the general-rho rows through
  the V35→V33→V28→V20 chain and bridges every rho=0 image to the 70
  hash-pinned frozen rows (canonical-form equality over hash-verified
  bytes);
- enforces even rho parity and per-monomial sigma homogeneity at runtime
  (`total_to_t` hard-fails on violations — both already verified facts);
- builds `A_30(t)` from **all nonzero general-rho rows** (the eight
  rho=0-dead rows included), with the complete complementary-monomial
  census over the 65 variables and no degree/support caps;
- computes the total target component on `Q[t]`-supports and the rho=0
  component separately; the exact-Q gate lane reuses the promoted V38
  `exact_certificate` machinery (flint exact solve, exact residual replay,
  separating functional on nonmembership) with the finite-prime lane as
  screen only;
- the validator is genuinely fail-closed: it requires the V42 replay to
  equal the frozen RESULT byte-for-byte including the corrupted-`Tg19_7`
  residual hash `bdbc1c36...`, requires the fixed census
  (70 rows / 65 rho=0 variables / weight 30 / exponent 6), requires
  single-occurrence PASS banners, and rejects any transcript containing
  `FAIL_`, `Traceback`, or `error occurred`.

**Defect (the GAP).**  The generated Singular script's toy-control
preamble calls

```text
module NZ=syz(NEG,NT);   ...   module PZ=syz(POS,PT);
```

`syz(module, vector)` is not valid Singular.  Locally verified on
Singular 4.4.1 (arm64-Darwin): the call fails with
"`? syz(`module`,`vector`) failed / ? expected syz(`module`,`string`)`",
`NZ`/`PZ` stay undefined, the loops error, `negFound` stays 0 (vacuous
pass of the negative guard), `posFound` stays 0, and the script prints
`FAIL_DVR_POSITIVE_CONTROL` and quits **before the main solve**.  So the
DVR stage can never produce a verdict as compiled.  The failure is safely
contained: the validator rejects the transcript on three independent
grounds (missing `V43_DVR_TOY_CONTROLS=1`, present `FAIL_`, present
`error occurred`), so the outcome is `NO VERDICT`, never a wrong verdict.
The main solve block itself (`module E=M,T; module Z=syz(E);` plus the
last-coordinate scan, unit normalization, and `matrix(E)*matrix(Z)`
replay) uses correct syntax — the producer's own
`MODULE_SYNTAX_PROBE.sing` (`59ae6db7...`) exercises exactly the correct
pattern and passes locally; the wrong two-argument form crept into
`write_singular` only for the controls.

### 6.4 Smallest repair, and launch disposition

Replace the two control lines in `write_singular` of
`compile_total_dvr_w30_v43.py` with augmented-module syzygies:

```text
module NEG=(1)*gen(1)+(-t)*gen(2); vector NT=gen(1);
module NE=NEG,NT; module NZ=syz(NE);
...
module POS=(1)*gen(1); vector PT=gen(1);
module PE=POS,PT; module PZ=syz(PE);
```

I ran exactly this repaired block locally: it prints
`V43_DVR_TOY_CONTROLS=1`, the negative toy's syzygy module is the zero
module (one zero column — the `NZ[2,cj]` scan handles it correctly, no
unit found), and the positive toy yields last coordinate 1.  I also
verified the main-solve pattern end-to-end on two one-column probes: a
column `(1+t)*gen(1)` against target `gen(1)` returns member with
normalized `U=t+1`, `U(0)=1`; a column `t*gen(1)` against `gen(1)`
returns nonmember with syzygy last coordinate `t` — the genuine-unit and
DVR-obstruction behaviors the design requires.

Disposition: **stop the DVR lane until the repair is applied**; since V43
carries no freeze yet, this is a pre-freeze edit of an unlaunched case,
not a mutation of frozen evidence.  Nothing already promoted is affected.
A launch without the repair would be sound-but-futile whenever the rho=0
gate passes (lane burned to `NO VERDICT`); the rho=0-gate-only phases
(preflight, exact-Q gate, gate-negative final answer) are sound as
compiled and may run.  Weight-30 product-census feasibility is untested
here (V37's largest harvested weight was 20 with 1,473 products; weight 30
over 65 weighted variables will be far larger), but the preregistered
six-hour/192-GiB caps and the `NO VERDICT` outcome policy govern that
risk correctly.

## Firewall

Nothing in this review is, or evidences, the certificate result itself.
`K+(rho)=(1)` remains **open**; V43 is a discriminator whose outcome is
pending.  A future positive result would close only the frozen
grade-through-19 ordered `T-a1` chart; it would not establish
source/landing coverage, the terminal receiver, Gate T, order two,
maximum twelve, or JC2.  A future negative at `N=6` would exclude only
that exponent.  This review edits no canonical ledger and touches no
campaign artifact other than creating this report file.

## Appendix: evidence and hashes

Reviewed/consumed artifacts (all re-hashed locally):

```text
e3d263d5c0006bc4f05c5b7ff17bfcbd68bab52f7c1d3ccb5d323facd94448f7  design (producer)
5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f  V42 report
f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459  V42 replay
01b8edd2b699d7c4b65452ea6eba47a98bf25c1cd5a18022a035e2346c973566  V42 RESULT.json
ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b  V37 solve_graded_ladder_v37.py
843a66318dc36ecacee05f1df3616d36e375d8f93f714cf667b1fb67992543dc  V35 evaluate_grade19_orbit_v35.py
14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501  V23 census_j2_typed_v23.py
ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641  V23 output_r1/RESULT.json
97fa7074ef0c116b87feb5d2edeac3b6788db603227361f78715b085468345a0  V43 PREREGISTRATION.md
90b014066706e15ebfdcd655ff68cd12d8adcd75904e00688674f81e13d70fa4  V43 compile_total_dvr_w30_v43.py
5a737941ee4a98de488d1198847163fe3ca3d44e80c666f816dab71edaf7cd83  V43 validate_total_dvr_w30_v43.py
59ae6db7742c59cd1a2181b42776801803f2ae495cf483dca279b1c254ed471b  V43 MODULE_SYNTAX_PROBE.sing
```

Review scripts staged under `/tmp` (not campaign artifacts):

```text
a7e1527a66ffb237d63eadd9d1f38b7533030dd87174441855f17734c021eef0  /tmp/check_design_v43_structure.py
4f0b45592e835ac265dafbb267cee168ac444ad45c68a1aafbba2b84fd4d3bef  /tmp/v43_syntax_probe.sing
daa9bdcd6c25e37c93fad14b9abdbe468b3a948f223d904e3461b5c8c3c0116f  /tmp/v43_repaired_controls.sing
5e28c87d5bee9e1301626cfef415383452eda4e05f6738725e2cb0860a4932d2  /tmp/v43_main_pattern.sing
```

Key transcript excerpts:

```text
# /tmp/check_design_v43_structure.py
files hashed+parsed: 70
general-rho nonzero rows: 59 / 70
total distinct variables in general-rho rows: 66
weight-zero variables present: ['rho']
positive-weight variables: 65
'qa1' present anywhere: False
'a1' weight: 5, 'k' weight: 4
inhomogeneous monomials: 0
odd-rho monomials: 0
max rho exponent: 8
rho=0 nonzero rows: 51 (expect 51)   [all ten grade censuses OK]
rho=0 variable census: 65 (expect 65)
positive vars occurring only in rho-carrying terms: []
rows nonzero general-rho but zero at rho=0: ['Tg11_2','Tg11_3','Tg11_5',
  'Tg11_7','Tg12_5','Tg12_7','Tg13_7','Tg14_6']

# Singular 4.4.1, verbatim control-block probe (as generated by V43)
? syz(`module`,`vector`) failed
? expected syz(`module`,`string`)
...
FAIL_DVR_POSITIVE_CONTROL

# Singular 4.4.1, repaired control block
V43_DVR_TOY_CONTROLS=1
NEG_NCOLS=1
NEG_Z=0

# Singular 4.4.1, main-solve pattern probes
CASE_A=member U=t+1 U0=1
CASE_B=nonmember Z2=t*gen(2)-gen(1)
```

Execution-gap disclosure: I did not rebuild the emitter chain
(V20→V28→V33→V35) from scratch; the general-rho rows were taken from the
same hash-pinned frozen files the V37/V43 custody chain uses, and my
checks are independent parses and censuses of those bytes plus hand
algebra for every claimed equivalence.  No heavy reduction, no AWS
launch, no `jc2-lean` access, and no canonical-ledger edit occurred.
