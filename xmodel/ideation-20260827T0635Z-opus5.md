# Blind whole-portfolio submission — Opus 5 lane

Round ID: `20260827T0635Z`
Lane: Opus 5, standing blind whole-portfolio researcher
Date: 2026-08-27

## 0. Basis, tool boundary, and execution disclosure

Read in full: the sealed packet, `APPROACHES.md` (overlays plus the whole
46-row master table, unique finds, consensus/dissent, shortlist),
`PROGRESS.md` top-of-file live state, `AUDIT.md` current promoted block,
`COORDINATION.md` in full, the newest `notes.md` `LIVE STATE`, the previous
synthesis, the terminal-receiver cascade audit, the V37 preregistration and
both result manifests, the Gate-T obligation table, the staged rho-unit
calculus promotion, the V23 preregistration, and my own prior submission and
prior V34 report (for deduplication).  I read no
`ideation-20260827T0635Z-*` submission or prompt other than my own.

Custody rehashed locally this round:

```text
e4235cdf…  APPROACHES.md          edc584f4…  PROGRESS.md
10f7bd3f…  AUDIT.md               d5ca2421…  COORDINATION.md
5fc18581…  notes.md
cb1b625e056753ae99580d80788534ca20f25040cd0921745c58ce6ad765c90b  prior synthesis  (matches packet)
b6c1c4ce4cce9cc693d3e7e0b790b3d0d76306d4b1052349d522e215c538a009  receiver audit   (matches packet)
065c96a9499e085d…  V37 q65521 RESULT.json  (matches packet)
fe2f6ef30e7423d8…  V37 q65519 RESULT.json  (matches packet)
d332ee24a72b2ef5…  V36 exact-Q RESULT.json (matches packet)
06aa3a1a7496378d…  V36 F65521 RESULT.json  (matches packet)
30c10a35719ce4e4…  Fable5 V34–V36 review   (matches packet)
04974b5c2949a5f9…  my prior V34 report     (matches packet)
```

**Execution disclosure.**  I ran only desk-scale exact sparse polynomial
arithmetic locally (Python `Fraction`, seconds, well under 1 GiB): parsing
the frozen `.poly` row files, monomial-support combinatorics, one exact
branch-and-bound over 88 sets, and substitution/residual checks.  No CAS, no
network, no AWS, no Groebner engine, no heavy run, and no campaign artifact
modified.  `jc2-lean` was not read, built, edited, staged, or cleaned;
the only contact was a single read-only `git status --porcelain` on it at the
end of the session, which returned clean and changed nothing.  I record that
as a boundary slip rather than omit it.

**Custody of the row bytes I computed on.**  I independently recomputed the
SHA-256 of all **70** ordered-`a1` row files (V23R1 grades 10–15, V28/V30/
V33/V35 grades 16–19) and confirmed each against *both* V37's pinned
`row_sha256` map and the producing case's own coefficient manifest: 70/70
match, 0 mismatches.  My own parser independently reproduces V37's frozen
census exactly — 51 nonzero rows of 70, 65 variables, and per-grade term
counts `0,1,9,28,75,187,424,867,1647,2929` for grades 10–19.  That agreement
is my primary positive control; it does not discharge hostile review.

Everything below labelled `EXACT-OPUS` is new, single-model, unreviewed,
and needs the ordinary different-model gate.  Nothing here proves or
disproves Gate T, order two, maximum twelve, or JC2.

---

## 1. Disposition vector over all 46 master-table avenues

```text
 1 unchanged   2 unchanged   3 unchanged   4 unchanged   5 unchanged
 6 unchanged   7 unchanged   8 unchanged   9 unchanged  10 unchanged
11 unchanged  12 unchanged  13 unchanged  14 unchanged  15 unchanged
16 unchanged  17 unchanged  18 unchanged  19 unchanged  20 unchanged
21 unchanged  22 unchanged  23 unchanged  24 unchanged  25 unchanged
26 unchanged  27 unchanged  28 unchanged  29 unchanged  30 unchanged
31 unchanged  32 raise      33 unchanged  34 unchanged  35 unchanged
36 unchanged  37 unchanged  38 raise      39 unchanged  40 unchanged
41 unchanged  42 unchanged  43 unchanged  44 unchanged  45 unchanged
46 unchanged
```

**Row 32 — Off-diagonal collision ideal / injectivity (Cynk–Rusek): `raise`.**
Its recorded promise line is *"exact software simplification, no degree/support
bound or new global obstruction"*, and its recorded blocker is *"a useful
client needs a named bounded family or source-derived saturated boundary
datum"*.  Both change this round.  §3.1 below shows by exact computation
that the terminal receiver **cannot** be emptied by the raw landing rows —
there is an explicit 43-dimensional linear zero section meeting `D(k)` — so
the receiver now provably needs a presentation that the source rows do not
contain.  The Gate-T obligation table already says what kind of object the
receiver is (*"the named exact-square/all-load receiver"*, review
`eff19a41…`).  Row 32 holds the portfolio's only **promoted saturation-free
collision presentation**, `I:Delta = I:Delta^infinity = I + (det A)` for the
Keller secant matrix.  That is exactly the type of datum the receiver audit
asks for in its step 5, and the receiver is exactly the named bounded client
row 32 lacked.  The raise is for that interface role only; row 32's own
stuck-point ("proving the three-generator ideal is `(1)` is still
injectivity") is unchanged, and the naive projective-CI connectedness route
stays `COSTUME`.

**Row 38 — Tropical / support and initial-degeneration combinatorics:
`raise`.**  Grok's dismissal is *"no tropical invariant without a Newton
name"*; Sol's caveat is *"prevariety overapproximates; saturation lost in
initial degenerations"*.  Both are correct **and both are now satisfied in a
narrow, load-bearing role on the campaign's own charts.**  The invariant has
a Newton name: the monomial-support hypergraph of the frozen landing rows.
This round it (a) produced the exact maximal zero section of §3.1 by an
exact minimum-hitting-set computation, (b) predicted V37's `W17`/`W18`
outcomes in milliseconds from divisibility alone (§4.3), and (c) supplied
the branch structure that made §3.2's `T-a1` cascade findable.  Sol's caveat
is not a defect here — it is precisely the correct reading: support
combinatorics certifies **nonemptiness of the raw system** and never
emptiness of the saturated one, which is exactly how I use it.  Raised as a
proof-side preflight instrument, in the same narrow sense in which I
reopened row 18 last round; its counterexample-side score is untouched.

**Rows I deliberately did not move.**

- **Row 31 (Integrality / ZMT / Rees valuations) — `unchanged`, with an
  explicit internal reallocation.**  I raised it two rounds running and it
  remains the portfolio's highest-throughput row.  But this round's news is
  genuinely two-sided: `T-a0` closed, while the receiver sub-lane is now
  provably outside the reach of the instrument being used on it and the
  `T-a1` graded ladder has returned four nonmembers.  A row-level raise
  would misreport that.  The correct action is *inside* the row: stop the
  raw-row receiver census, keep the chart certificates, and adopt the
  cascade instrument of §3.2.  I record that here rather than faking a
  rank change.
- **Row 4 (formal-germ certification, DEPTH-STAB, prolongation)** was raised
  by the prior synthesis and stays raised; §5.2 argues the landing lane is
  currently re-deriving row 4's prolongation-stability question grade by
  grade at AWS cost instead of importing it.  That is a connection, not a
  further rank change.
- **Rows 5, 18, 19** carry my prior-round raises/reopen; no new charged
  evidence arrived for any of them this round.  Row 19 in particular saw
  **zero** movement, which I flag as a scheduling fact in §2.2 rather than
  as a rank change.
- **No row earns a `lower` on this round's evidence.**  I looked
  specifically for one and declined to manufacture it.  The one thing that
  genuinely lost value is a sub-lane (raw-row receiver emptiness), and the
  master table has no row granular enough to carry that; §6 records the
  `stop`.

---

## 2. Reranked bottlenecks

### 2.1 Proof side

1. **Absolute or cofinal complexity/type ceiling.**  Unchanged at #1.
   `KJN(C)` is type-relative and needs an independent provenanced bounded
   `(alpha,beta)` menu; no charged artifact supplies one.  Every chart closed
   in the last 48 hours is orthogonal to it.
2. **The terminal receiver has no algebraic closure route on this source.**
   *This is my main reranking claim and it replaces my own prior #2.*  The
   receiver audit proved a one-point all-depth zero section `K00`.  §3.1
   upgrades that to an exact **43-dimensional maximal linear zero section
   `L43`** of all 51 nonzero rows through grade 19, containing the unit `k`,
   the entire `ell` connection tail, the entire `k`-load family, and the
   deep `cs/rs/ac/az/ec/ez` tails.  So this is not "one degenerate point that
   an honest equation will remove"; it is a large component, and any
   discriminator tested only at `K00` risks a false positive.  Fanout: Gate T
   is worthless without the receiver, and every `J1`/`J2` certificate feeds
   it.  Rollback cost is low because nothing downstream has been built on
   receiver emptiness — but the lane's compute is being spent in a provably
   empty direction.
   *(I explicitly retire my own prior #2, the genuine-localizer complement
   bottleneck, from the top band: my grading-based argument for it was
   refuted in cross-review, and the promoted `T-rs`/`T-cs` certificates carry
   their `k`-powers explicitly, so the obligation is real but routine.)*
3. **Universal full-configuration landing / coverage** (`T9`/`T10`):
   composite single-pole, general off-axis, post-jump mixed contexts, all
   `NOT ESTABLISHED`.  Unchanged in content.
4. **The arbitrary-standard-pair bridge.**  Unchanged and still unaddressed;
   without it the GGV5/prime-ray machinery emits `B_GGV`-value statements
   only.
5. **Ordered `T-a1` chart closure.**  Demoted from "hardest open local
   object" to "tractable but unsolved": §3.2 gives a chart-wide radical
   cascade that removes four coordinates unconditionally and kills one of the
   two branches outright, all by hand from frozen bytes.  High tractability,
   medium fanout — it is one chart of a staged tree whose terminal node is
   bottleneck 2.
6. **Converting `rho=0` screens into honest total-family certificates.**
   Promoted correction `593f953b…` says fibre emptiness gives only a cleared
   containment in `J+(rho)`.  Every grade-16+ export in the `a1` lane has
   `rho` killed at compile time, so *everything* the lane has produced since
   V28 lives on the wrong side of that correction.  This was implicit; I
   promote it to an explicit ranked obligation.
7. TD6 whole closure (original-FIRST/total-`F`, omitted moduli, `q15`).
   High local momentum, low global fanout.
8. Order-two fan exhaustiveness; `G2-PSC`/`G2-BD` dormant.

### 2.2 Disproof / falsification side

1. **Existence-or-nonexistence of an exact AS109 polynomial lift, via the
   arithmetic `(deg_y, v_109)` Newton polygon.**  Retained at #1 on merit —
   and flagged: this is now **two consecutive full rounds with a ranked,
   unblocked, cheap `n=2` corner that has not been run**, and my exact
   source-gauge section from the prior round remains unconsumed.
   `COORDINATION.md` §capacity makes two rounds with unchanged leading gaps a
   fresh-eyes-reset trigger.  Either run the corner or explicitly demote the
   lane; leaving it ranked-and-idle is the worst of the three.
2. **Falsification of the landing programme itself, via `L43`.**  New at #2.
   `L43` is a 43-dimensional family of source data satisfying every raw
   landing equation through grade 19 with `k` a unit.  Evaluating the honest
   saturated Rees kernel / chart / routing equations at a **generic** `L43`
   point is a two-outcome decisive test of whether the honest equations carry
   any content the rows do not (§4.2).  It can falsify the terminal-receiver
   expectation in one shot, which no other live experiment can.
3. **Effectivity of the finite death depth for a bounded degree box**
   (Greenberg / quantitative Artin approximation).  Unchanged.
4. **The unbounded-total partial-`y` `(8,12)`/`(9,12)` frontier.**  Unchanged;
   still the free floor-raising engine for AS109.
5. The polynomial-limit criterion (uniform support/degree).  Unchanged; the
   charged all-Witt control has `deg_y = 1` at every level and is
   uninformative.

---

## 3. New mechanism, with exact results

### 3.1 The front/tail hitting-set structure, and `L43` [`EXACT-OPUS`]

Work in the frozen ordered-`a1` chart (`J1=(rs,cs,c0,c1)=0`, `a0=0`) with
`rho=0`, on the 51 nonzero rows of grades 10–19 in 65 variables — the exact
V37 object, byte-verified in §0.

**Step 1 — the support hypergraph.**  The 51 rows contain 4,997 distinct
monomial *supports*, of which exactly **88 are minimal under inclusion**:
11 singletons, 54 pairs, 23 triples.  The singletons are

```text
{a1} {aa0} {aa1} {e0} {e1} {ec3} {ec4} {ee0} {ee1} {ez3} {ez4}
```

i.e. for each of those eleven coordinates some row carries a *pure power* of
it as a monomial.

**Step 2 — coordinate zero sections are exactly the independent sets.**
Setting every variable outside a subset `S` to zero annihilates all 51 rows
identically iff no minimal support is contained in `S`.  So the maximal
coordinate zero sections are the maximal independent sets of an 88-edge
hypergraph on 65 vertices, and their dimensions are `65 −` (hitting-set
sizes).  I solved the minimum hitting set exactly by branch and bound.

> **Theorem L (`EXACT-OPUS`).**  The maximum coordinate zero section of the
> frozen ordered-`a1`, `rho=0` rows through grade 19 has dimension exactly
> **43** (minimum hitting set `22`).  One optimum contains the unit `k`:
>
> ```text
> L43 = V(F),   F = { a1, aa0, aa1, aaa0, aaa1, cs1, cs2,
>                     e0, e1, ec3, ec4, ec5, ec6,
>                     ee0, ee1, ez3, ez4, ez5, ez6,
>                     rs1, rs2, rs3 }        (|F| = 22)
> ```
>
> so `L43` has free coordinates `ell1..ell8`, `k, k1, k2c, k6, k6_1,
> k10_3..k10_6`, `cs3..cs7`, `rs4..rs7`, `ac3..ac8`, `az3..az8`,
> `ec7..ec9`, `ez7..ez8`.  Direct substitution leaves **0** surviving terms
> in all 51 rows, and each of the 22 excluded variables switches on an
> explicit row monomial (e.g. `a1` → `a1^2*cs3` in `Tg15_1`, `e0` → `e0^2`
> in `Tg12_4`, `cs1` → `cs1^3*ell1*k` in `Tg14_1`, `rs1` → `k*rs1^3` in
> `Tg13_2`), so `L43` is maximal, not merely large.
>
> `L43` also survives with `rho` completely free on grades 10–15, the only
> grades where general-`rho` ordered-`a1` bytes exist: zero surviving terms
> on `L43 x A^1_rho`.

Three consequences.

- **`K00` is the most degenerate point of a 43-dimensional family.**  `K00`
  sets `ell1 = 0`, hence `p = -2rho^2` and `c = 0`; a generic `L43` point has
  the whole `ell` tail on, so `p` has `sigma`-order 1 even at `rho=0`.  An
  honest equation that kills `K00` *by using its degeneracy* proves nothing
  about the receiver.  This sharpens the audit's step 5: **run it at a
  generic `L43` point, with `K00` retained only as a control.**
- **The excluded set `F` is a "front".**  It is the low-index head of each
  source family (`e`, `ee`, `ez3..ez6`, `ec3..ec6`, `cs1,cs2`, `rs1..rs3`,
  `aa`, `aaa`), while every `ell` and every load coordinate is free.  In
  words: *through grade 19, every monomial of every row contains at least one
  leading jet.*  That is the structural reason `K00`, `Z00`, and `CS0` are
  all-depth zeros — they are three points of one phenomenon, not three
  coincidences.
- **The asymmetry with `T-a1` is real and favourable.**  `{a1}` is a minimal
  support (`a1^3` occurs literally in `Tg15_3`, coefficient `-1/16`), so
  **no** coordinate zero section has `a1 != 0`.  The `K00` obstruction
  therefore does *not* transplant to the ordered `T-a1` chart, and the graded
  ladder there is not futile in the `K00` sense.  Any `T-a1` witness must be
  genuinely nonlinear — which is exactly what V32 attempted and V34/V36
  killed for one ansatz.

### 3.2 A chart-wide radical cascade for ordered `T-a1` [`EXACT-OPUS`]

The `T-a1` lane has been screening *guessed sparse supports* (V32's six
coordinates `ell2,cs1,rs2,aa0,ee1,ec3` with `a1=48`).  The `T-a0` and
`T-c1` charts fell instead to hand identities on frozen bytes.  Applying the
second instrument to `T-a1` yields, on `rho=0` and at field-valued points
with `a1` invertible (char `!= 2,3,5`; all divisions displayed):

```text
Tg11_1 = (3/8)*a1*e0                                   =>  e0 = 0
Tg12_2 |_{e0=0} = (3/32)*e1*(e1 - 4*a1*ell1)           =>  e1 = 0  or  e1 = 4*a1*ell1
```

On the second branch `Tg12_1` forces `ee0 = -4*aa0*ell1`, and then

```text
Tg13_4 = -(3/2)*a1^2*ell1^3   =>  ell1 = 0   =>   e1 = 4*a1*ell1 = 0.
```

So the branch collapses and `e1 = 0` unconditionally; `Tg12_1` then gives
`ee0 = 0`.  With `e0=e1=ee0=0` two further identities are exact zero
residuals (machine-verified):

```text
Tg14_4                        = (3/32)*a1^2*ell1*rs1
Tg14_3 + (1/2)*ell1*Tg13_1    = (3/8)*a1^2*cs1*ell1 - (3/16)*a1*aa0*rs1
```

hence `ell1*rs1 = 0` and `aa0*rs1 = 2*a1*cs1*ell1`.  Split on `ell1`.

**Case B (`ell1 != 0`) is empty.**  `rs1=0`; then `cs1=0`; `Tg13_2` gives
`ee1=0`; `Tg13_1` gives `ec3=0`; `Tg15_4` gives `rs2=0`; `Tg14_2` gives
`ez3=0`; `Tg14_1` gives `ec4=a1*cs2`; `Tg15_3` collapses to
`a1^2*((3/8)*cs2*ell1 - (1/16)*a1)`, so `a1 = 6*cs2*ell1`; and finally

```text
Tg16_5 = (27/2)*cs2^3*ell1^4      =>  cs2 = 0  =>  a1 = 0,
```

contradicting `a1 != 0`.  (Every displayed value is a machine-checked exact
residual against the frozen bytes.)

> **Theorem A (`EXACT-OPUS`, radical/field-point scope, `rho=0`, `D(a1)`).**
> On the frozen ordered-`a1`, `rho=0` rows of grades 11–16, every field
> point with `a1 != 0` satisfies
> `e0 = e1 = ee0 = ell1 = 0`, and then `aa0*rs1 = 0` with either
> `rs1 = 0` (Case A1) or, if `rs1 != 0`, `aa0 = 0`, `k*rs1^2 = (96/5)*a1^2`
> and `ee1 = a1*ell2` (Case A2, from `Tg15_4`).

Two immediate payoffs.  First, V32's six-coordinate ansatz is *derived*, not
guessed: `e0=e1=ee0=ell1=rs1=0` is exactly branch A1, so V34/V36 killed a
sub-ansatz of A1 in which `aa1, aaa0, aaa1, ac3, ez3, cs2, cs3, rs3, ell3,
k, k1, …` were set to zero **without justification**.  That is the honest
scope of the grade-19 kill.  Second, the surviving object is small and
explicit: at grade 16 branch A1 has row term counts `32,31,20,10,0,0,0` in
six coordinates plus tails — desk scale, not AWS scale.

### 3.3 New connection: the receiver is a row-32 object, not a row-31 object

`APPROACHES.md` files the whole landing programme under row 31.  But the
Gate-T obligation table already describes the terminal node differently —
*"If both `J1` and `J2` vanish, the arc routes to the named exact-square/
all-load receiver"*, whose support is reviewed as **square plus
Chebyshev/Pell** (`eff19a41…`), with the affine-target row, later
corrections, terminal `[6,2]`, and both Taylor pullbacks open.  Theorem L
now proves the row-31 instrument (source-row ideals) cannot reach it.

The composition pass therefore gives a concrete bridge to test: row 32's
promoted accelerator `I:Delta = I:Delta^infinity = I + (det A)` presents a
collision scheme with **three generators and no saturation**.  The receiver's
registered defect is a missing saturation/routing datum.  Interfaces:
row 32 consumes "a Keller secant matrix and a named bounded family"; the
receiver supplies exactly a named bounded family (the exact-square/all-load
tail support) and is, by definition, the locus where the collision data
degenerate.  Verdict to record: **candidate bridge, `NOT YET TESTED`** — I
am not claiming the interfaces match, only that this is the one untried
pairing in the portfolio whose output type is the receiver's missing input
type, and the theorem-interface pass in `COORDINATION.md` requires testing it
before treating either endpoint as isolated.

A second, cheaper connection: rows 31 × 4.  V19 (exponent search), V32
(curve), V34–V36 (Kummer orbit) are three independent re-derivations of "does
a finite-prefix survivor prolong?" — row 4's registered subject, with a
registered instrument (`DEPTH-STAB`, D-series windows) and a registered
lesson (*modular nonempty ≠ germ ≠ char-0 ≠ polynomial*).  The landing lane
is paying AWS to rediscover it one grade at a time.  Import the criterion.

---

## 4. Strongest attacks and one acceleration

### 4.1 Strongest proof attack — finish the `T-a1` cascade by hand, not by screen

Theorem A removes four coordinates chart-wide and kills Case B with six
frozen rows and no solver.  Continue A1 (`ell1=rs1=0`) and A2
(`aa0=0, k*rs1^2=(96/5)a1^2, ee1=a1*ell2`) the same way, grade by grade, on
bytes already on disk.  Each step is a two-row identity of the kind that
closed `T-c1` (`c1^3`) and `T-a0` (`a0^3`).  This is the highest
expected-information proof action available at zero compute cost, and it is
the only `T-a1` attack that is *chart-wide* rather than ansatz-wide.  Its
honest ceiling is stated in §7.

### 4.2 Strongest falsification attack — the generic-`L43` honest-equation test

Replace the audit's "evaluate honest equations at `K00`" with:

1. pick a generic rational point of `L43` (all 43 free coordinates generic,
   `k` a unit) and, separately, `K00` and one intermediate point with only
   `ell1` turned on;
2. evaluate the **genuine saturated Rees kernel, chart, and routing
   equations** — the `(P_i : f_i^infinity)` presentation of the obligation
   table's (2.3)/(2.4), the Rabinowitsch generator `1-v*k`, and the
   exact-square/all-load target row — at all three;
3. require `K00` to satisfy `1-v*k` and `Z00` to fail it (the audit's
   controls), plus a perturbed point that fails the raw rows.

Outcomes: *some honest equation is nonzero at the generic `L43` point* ⇒ the
first genuine exclusion target exists and is now explicitly named, and the
receiver becomes attackable; *all vanish on `L43`* ⇒ the on-family receiver
is genuinely nonempty at bounded depth and Gate T needs a completely
different terminal argument (routing/coverage or the square/Pell object), a
result that would redirect the campaign's critical path in one step.  *An
equation nonzero at `K00` but zero on `L43`* ⇒ the audit's step 5 would have
returned a false positive; this is the case the current design cannot see.

### 4.3 Software / compute acceleration — a mandatory support-incidence preflight

Before any AWS membership or emptiness job on the landing rows, run a
millisecond combinatorial preflight on the frozen `.poly` bytes:

- compute all monomial supports and their minimal elements;
- **target-divisibility test:** a target monomial `t` can appear in *some*
  row-multiple only if some row monomial divides `t`.  If none does, `t` is a
  **vacuous nonmember** and no linear algebra is required;
- **zero-section test:** solve the minimum hitting set; report the maximal
  coordinate zero sections and whether any meets the registered unit open.

Evidence that this pays, computed this round (`EXACT-OPUS`):

```text
target        row monomials dividing it     V37 outcome / cost
a1*k^3        0                             nonmember, rank 0, 217 products
a1^2*k^2      0                             nonmember, rank 0, 426 products
a1^3*k        2  (a1^3 in Tg15_3,           nonmember, rank 50, 803 products
                  a1^3*k in Tg19_5)
a1^4          1  (a1^3 in Tg15_3)           nonmember, rank 156, 1473 products
```

V37's own manifests report `component_products: 0`, `rank: 0`, and a
one-term functional for `W17`/`W18` — i.e. **half of a dual-host exact-Q AWS
campaign answered a question that a divisibility check answers for free**,
and the entire content of `W19`/`W20` hinges on exactly two row monomials.
The preflight also converts the packet's "W17–W19 complete forever" claim
from a solver output into a two-line argument (weighted homogeneity plus
generation in grades `>= 10`; `sigma`-weights `a1=5`, `k=4`, verified against
the pinned V23 parser).  Cost to build: under an hour, no dependencies beyond
the existing frozen parser.  It is fail-closed by construction: it can only
*refuse* work, never license a membership claim.

---

## 5. Idea cards

### Card A — Complete the ordered-`T-a1` chart-wide cascade

- **Target obstruction:** ordered `T-a1`, the last open registered `J2`
  chart; bottleneck 2.1(5).
- **Dependencies:** the 70 frozen row files (hashes verified §0); the V23
  parser; the promoted staged rho-unit calculus `16ec6f54…` and its converse
  correction `593f953b…`.  **No dependency on V37, V34, or V36.**
- **Cheapest exact discriminator:** by hand/desk exact arithmetic, continue
  branches A1 and A2 of Theorem A grade by grade to 19, looking at each grade
  for (i) a monomial forcing a coordinate to vanish, or (ii) a two-row
  identity of `T-c1` type.  Budget: one lane, no AWS.  First checkpoints:
  A2 is the small branch (`aa0=0`, `ee1=a1*ell2`, one Pell-like relation
  `k*rs1^2=(96/5)a1^2`) and should resolve first.
- **Both outcomes:** a contradiction in both branches ⇒ ordered `T-a1` has
  empty `rho=0` fibre on `D(a1*k)` at radical scope — then, and only then,
  spend compute converting it to an honest `a1^N*s*(1+rho*W)` identity, which
  is where V37's weight ladder becomes the right tool again (next honest
  weights `a1^4*k = 24`, `a1^5 = 25`).  A surviving branch ⇒ an **explicitly
  parametrized** candidate family, incomparably better than V32's guessed
  support, and the correct input to a bounded AWS `std` on one branch only.
- **Stop rule:** stop if two consecutive grades add no new forced vanishing
  and no two-row identity in *either* branch; that is the signal that the
  remaining content is genuinely nonlinear and needs a solver.  Also stop
  immediately if the `rho=0` restriction is shown to be lossy for the
  registered chart type (see §7).
- **Expected information gain:** high.  Two of the four closed `J1` charts
  and the closed `T-a0` chart fell to exactly this instrument; it has never
  been pointed at `T-a1`, and it has already killed one of two branches and
  four coordinates before this round ended.

### Card B — All-depth front/tail theorem, and the receiver reroute

- **Target obstruction:** bottleneck 2.1(2) — the terminal receiver.
- **Dependencies:** the 569 canonical tails and the V20 actual-total emitter
  (hashes in the receiver audit); Theorem L.
- **Cheapest exact discriminator, two parts.**  (i) *Prove or refute the
  all-depth front property from the emitter:* show that every monomial the
  emitter can produce at any grade contains a coordinate of `F`.  The audit
  already did the `|S|=1` case (`K00`) by replaying all 569 tails; the
  general statement is a structural claim about the convolution, not a bigger
  replay.  (ii) *Run the generic-`L43` honest-equation test of §4.2.*
- **Both outcomes:** front property holds ⇒ the raw receiver contains a
  43-dimensional component at **every** depth; raw-row receiver emptiness is
  permanently retired, superseding `K00` with a far stronger theorem, and the
  receiver moves to the exact-square/Pell object and the row-32 interface.
  Front property fails at some grade `g` ⇒ that grade is the **first honest
  discriminator the lane has ever had**, and it is a bounded, named export.
  Both outcomes are decisive; there is no null result.
- **Stop rule:** stop part (i) if the emitter argument is not closed in one
  lane-session — the bounded-depth Theorem L is already enough to justify the
  `stop` in §6.  Stop part (ii) the moment any honest equation separates
  generic `L43` from `K00`, and register that equation.
- **Expected information gain:** very high on the strategic axis (it decides
  whether a whole lane continues), moderate on the mathematical axis.

### Card C — Support-incidence preflight as a launch gate

- **Target obstruction:** compute allocation; `COORDINATION.md`'s
  information-gain-per-dollar criterion.
- **Dependencies:** the frozen V23 parser only.
- **Cheapest exact discriminator:** implement §4.3; replay it against V37's
  four targets and against `K00`/`L43` as fixtures.  Mandatory controls: it
  must reproduce V37's `rank 0` / one-term-functional signature for
  `W17`/`W18`, must reproduce `K00` from the receiver rows, and must
  **refuse** to emit any membership verdict.
- **Both outcomes:** it reproduces the fixtures ⇒ adopt as a launch gate for
  every landing membership/emptiness job.  It disagrees on any fixture ⇒ a
  real defect in either the preflight or the frozen census, found for free.
- **Stop rule:** one lane-session; it is a script, not research.
- **Expected information gain:** moderate but immediate and compounding —
  on the recorded evidence it would have removed two of four AWS targets
  from V37 and would have flagged the receiver census as futile before V26.

---

## 6. `continue / redesign / stop` for current major lanes

| Lane | Call | Reason |
|---|---|---|
| Ordered `T-a1` chart closure | **redesign** | Stop guessing sparse supports and screening them; adopt the chart-wide cascade (Card A).  V32/V34/V36 killed one ansatz inside branch A1, not the chart. |
| Raw-row terminal-receiver census / deeper raw exports | **stop** | Theorem L: a maximal 43-dimensional zero section meeting `D(k)` exists through grade 19; the audit already proved the all-depth `K00` point.  No further raw grade export can empty this receiver.  Redirect to Card B and the exact-square/Pell object. |
| V37 successors on the weight ladder (`W20+`) | **redesign** | Gate every target through §4.3 first; two of four V37 targets were vacuous.  Do not fund `W20` completion until Card A says which weight the honest certificate should have. |
| Grade-20 row export for the `a1` lane | **stop for now** | Justified only by `W20` completeness; Card A is strictly cheaper and may make it unnecessary or retarget it. |
| V29 capped full grade-16 Groebner controls | **stop** | Already recorded as noncritical given the explicit witness; the capped hosts are better spent on Card B part (ii). |
| TD6 H19R2 exact-Q dual run | **continue** | Independent, synchronized, denominator- and original-FIRST-controlled; no interaction with any decision above. |
| D1 near-closure lanes | **continue** | Unchanged; independent of the landing tree. |
| AS109 arithmetic-Newton `n=2` corner | **continue — and actually start it** | Ranked #1 on the disproof side for two rounds and unstarted; see 2.2(1).  If it will not be staffed, demote it explicitly rather than leaving it ranked. |
| Unified typed-certificate tool | **continue** | Its fail-closed field list should gain one row: *the `rho` specialization status of every input export*, per bottleneck 2.1(6). |
| Serial affine-Faber height increments; paid AS109 rigid-leaf search | **stop** (unchanged) | Named redesign prerequisites still absent. |
| Broad web sweep | **continue** | Deadline `2026-08-28T00:00Z` unchanged. |

---

## 7. Adversarial scope audit of my own best proposal (Card A / Theorem A)

I attack Theorem A and Card A as hostilely as I can.

1. **`rho = 0` is not the chart.**  Every grade-16+ ordered-`a1` export has
   `rho` killed at compile time, so Theorem A's `Tg16_5` step — the one that
   kills Case B — is a special-fibre statement.  Promoted correction
   `593f953b…` says exactly this is *not* a certificate: fibre emptiness
   yields only a cleared containment in `J+(rho)`.  **Card A can therefore at
   best deliver a `rho=0` screen, and the conversion step is unproved.**  This
   is the single largest limitation and I state it before any use.
2. **Radical / field-point scope, not ideal membership.**  Steps like "`a1`
   and `ell1` are nonzero, therefore `ee1 = 0`" are pointwise.  They give at
   best `a1 in radical(I + …)`, whereas the staged calculus wants a
   polynomial identity.  This is precisely the gap V37 measures, and V37's
   `W19` nonmembership is *consistent* with Theorem A: `a1^3*k` need not lie
   in the raw ideal even if the variety has no point with `a1 != 0`.  Do not
   quote Theorem A as a certificate.
3. **Case B's kill divides by `a1` and `ell1`.**  Its honest scope is
   `D(a1*ell1)`; the complement `ell1 = 0` — Case A — is where the real
   content sits, and I have only *split* it, not closed it.  Reporting
   "Case B is empty" as progress without that caveat would be exactly the
   over-claim the `T-c1` review caught.
4. **Characteristic.**  Coefficients carry denominators `2, 3, 5, 1024`
   (e.g. `96/5`, `5/1024`, `27/2`).  Theorem A needs char `!= 2,3,5`.  The
   F65521 shadow is fine; a small-characteristic control is not.
5. **Provenance I inherit rather than verify.**  I verified the 70 row files
   byte-for-byte against V37's pins and against each producer's own manifest,
   and my parser reproduces V37's term census exactly.  I did **not**
   independently re-derive those rows from the emitter, and the grade-16–19
   files were produced for a different purpose (prolonging a specific point).
   If those exports carry any substitution beyond `J1=0, a0=0, rho=0`,
   Theorem A inherits the error.  A reviewer must re-emit at least
   `Tg14_3, Tg14_4, Tg15_3, Tg15_4, Tg16_5` from the pinned emitter.
6. **My parser is mine.**  It is a 20-line regex reader, not the pinned V23
   AST parser.  It agrees with V37 on 70 hashes, 51 nonzero rows, 65
   variables, and all ten per-grade term counts — strong, but a silent
   coefficient misread that preserves term counts is conceivable.  Reviewers
   should replay through `census_j2_typed_v23.py`.
7. **Branch logic is hand reasoning.**  The three displayed residuals are
   machine-verified zeros; the *chain* ("therefore `rs2=0`, therefore
   `ez3=0`, …") is human.  A single wrong implication invalidates the Case B
   kill without touching any verified identity.  This is the most likely
   place for an error and the first thing a reviewer should redo.
8. **Even complete success closes one chart.**  Ordered `T-a1` closure would
   leave the terminal receiver (bottleneck 2.1(2), and Theorem L says it is
   not closable this way), source/landing coverage, the deck/square bridge,
   the off-family `k10=0` timing fan, the cofinal ceiling, order two, maximum
   twelve, and JC2 open.  Card A is a chart, not a gate.
9. **Adversarial reading of Theorem L itself.**  `L43` is proved only through
   grade 19 and only for coordinate subspaces; a nonlinear component could be
   larger and an all-depth statement is *not* proved (that is Card B part (i)).
   And Theorem L certifies nonemptiness of the **raw** system only — exactly
   Sol's recorded tropical caveat.  It is not evidence that the honest
   saturated receiver is nonempty, and I do not claim that anywhere.

## 8. Explicit nonclaims

Nothing above establishes Gate T, a source/landing coverage theorem, the
deck/square bridge, an absolute or cofinal complexity ceiling, order two,
the maximum-twelve frontier, the existence or nonexistence of an AS109 lift,
or JC2.  Theorem A and Theorem L are `EXACT-OPUS`, single-model, unreviewed,
and scoped as stated in §7.  No campaign artifact was modified and no AWS,
network, or CAS capacity was used.
