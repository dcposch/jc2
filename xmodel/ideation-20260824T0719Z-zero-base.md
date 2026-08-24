# Blind all-46 submission — zero-base lane — round `20260824T0719Z-c17bd25`

- Status: **FROZEN BLIND SUBMISSION / NO LAUNCH / NO PROMOTION**
- Lane: zero-base, applied only after the common all-46 scan
- Clean basis: `c17bd2542b40f3178ec619ae4a73501550555336`
- State cutoff: `2026-08-24T07:19:08Z`
- Sealed packet SHA-256:
  `ef61e5d5fe8f58081b9b36602b5bf98a83f655b9836cefe93a5a355dd90c9a2d`
- Network/browser: not used
- Computation: none; the K3 fail-closed wrapper was inspected but not run,
  because no K3 result is used below
- Blindness: no other `ideation-20260824T0719Z-*.md` submission was read

## 0. Input-integrity record

All eighteen required packet inputs matched their displayed SHA-256 digests,
and `git rev-parse HEAD` matched the clean basis.  In packet order, the
recomputed digests were:

| Input | Recomputed SHA-256 | Verdict |
|---|---|---|
| `COORDINATION.md` | `ad6388abed8cf38f9a3688525dc976b4dd249e0ef1ff072856baf0a0591942b3` | MATCH |
| `APPROACHES.md` | `5677947851abee833c56c520ba1ba14795d0aaa6844678efa47fff537fe2e044` | MATCH |
| `AUDIT.md` | `7300920f91bbd0e2aca9544ee46e32fcf5f67e2a4c9587c28d0fe01f6796c31b` | MATCH |
| `PROGRESS.md` | `861920ac07500e96ef9f2a8f3f0b5a54f777c39c94e22cfbe53faf85ac37e057` | MATCH |
| `notes.md` | `bcefda385088b59242dab495b70994dd903db42f370c72ea1a604cf27e6d7c49` | MATCH |
| `xmodel/ideation-20260824T0453Z-synthesis.md` | `76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790` | MATCH |
| `xmodel/ideation-20260824T0453Z-dedup.md` | `d100616a66115ab0fa1dedc49bfbee910b8d70a0b915268c8e974a197a11747b` | MATCH |
| `xmodel/ideation-20260824T0453Z-packet-erratum.md` | `7dfd30f0f9b7fb95bdc6c61598b69bc33a418b4281f6198df1a6066dcf39d47f` | MATCH |
| `xmodel/exact-coframe-gate-20260824.md` | `8aad8b60777fb7d52fb037df961f1204f255ee36f1775a3f8c772d1739691571` | MATCH |
| `xmodel/exact-coframe-gate-20260824-erratum.md` | `6b71a5bdae1af77ab49a4adae0a9041e1fd1193f5de84ecec65a9b5225b8894e` | MATCH |
| `xmodel/exact-coframe-gate-review-grok-20260824.md` | `f3ad02d9e104692b5e066a4926c10f92c369445a6dd47eea4e6dba22a226caea` | MATCH |
| `xmodel/exact-coframe-background-review-grok-20260824.md` | `1fa8b5cc89d35163ad0aa43e1eb0a2fc3f7f1f6a28cbcf2085af45a0dca2e553` | MATCH |
| `xmodel/completion-pair-gate-20260824.md` | `d5027984be4ae4dbe4d0b5f95161d6d57d71ed9b3c086dd6fce2f03190e6c1bc` | MATCH |
| `xmodel/completion-pair-rank2-review-grok-20260824.md` | `ab540f10a2431fd2a59c88cea983cebbd8883e5777e74d7f0a415eff0b7fc952` | MATCH |
| `xmodel/weighted-d-source-gate-20260824.md` | `04047377c778ababf07e847f5a72d39787dd452e284bc01d83538b5131f7d08a` | MATCH |
| `xmodel/weighted-d-source-review-grok-20260824.md` | `266e30b1c12f7cbc9a60a86ad1b450d5ba23d9db27f307a22be04f01c99da07e` | MATCH |
| `xmodel/k3-local-preflight-20260824.md` | `579bac61491fa4d33a2bc0d454be83f7207fd44595e88bc6240190f5f022416e` | MATCH |
| `cases/k3_local_preflight_20260824/replay_expected.py` | `7a3a1252e0d1e8ef8de9b3065fea3063e0df131dabcfa565c0240504f2d43001` | MATCH |

The prior packet's missing-zero digest erratum, the exact-coframe citation
erratum, and the distinction between the background source review and the
actual promotion review were preserved.

## 1. Common all-46 disposition scan

Legend: `U=unchanged`, `R=raise`, `L=lower`, `O=reopen by a redesigned
mechanism`.  `O` never means resume the stopped representation unchanged.

```text
 1 U   2 U   3 U   4 L   5 U   6 U   7 R   8 U   9 U  10 L
11 U  12 U  13 U  14 U  15 U  16 O  17 U  18 U  19 O  20 U
21 U  22 U  23 U  24 U  25 R  26 U  27 U  28 R  29 U  30 U
31 O  32 U  33 L  34 R  35 U  36 O  37 U  38 O  39 U  40 U
41 U  42 U  43 U  44 U  45 U  46 U
```

Reasons for every change:

| ID | Call | Reason |
|---:|---|---|
| 4 | lower | The weighted level-two gate and hostile review stop before a source tangent exists.  Exact ambient formulae are acceptance tests, not a state, recurrence, germ, or algebraization path.  Fixed-depth D work has now returned two consecutive representation-level stops. |
| 7 | raise | The full pencil `aP+bQ`, rather than one chosen asymptotic component, gives a canonical parameter space on which to package all infinity bifurcations at once.  Card P below supplies a new finite first gate. |
| 10 | lower | A bounded HC4 source replay remains an excellent orthogonal reserve, but it attacks a stronger conjecture and has a high priority/knownness risk.  The direct-plane pencil and first-open-degree gates now have better dependency-adjusted value. |
| 16 | reopen | The row previously lacked a concrete invariant.  The proposed relative infinity-vanishing-cycle divisor of the universal target pencil is a named holonomic/microlocal object with an exact control gate. |
| 19 | reopen | Not the stopped degree-three compiler and not another Witt level.  Card S starts at the legal-degree prime `p=109` and asks first for a finite correction-support cycle, then—only after a hit—for one fixed finite-type generic-fibre question. |
| 25 | raise | Replacing a raw passport by the variation of vanishing cycles over the entire dual target pencil couples all linear target projections and the Jacobian condition.  It is not another one-cover branch-cycle census. |
| 28 | raise | A single resolved universal pencil may turn the missing global sign into a resolution-independent effective divisor and a GRR/localization degree formula.  This is a sharper log-surface question than completing another book tail. |
| 31 | reopen | Ranks two and three are known-closed, but rank four is the first open normalization rank.  The cubic-resolvent inheritance gate in Card Q is a genuine redesign and can fail decisively before any surface enumeration. |
| 33 | lower | The different-model-confirmed boundary probe already killed untwisted action-residue charge and raw primitive pole order as `COSTUME`.  `ACTION-RESIDUE-INDEPENDENCE` is not ready until it names a twisted, resolution-independent class distinct from the existing no-log identity. |
| 34 | raise | The all-Witt control and the rational Broughton/Cohn completion expose the same finite-support-versus-pole-escape phenomenon.  Card S turns that into an exact exponent-interaction discriminator rather than a generic rational ansatz. |
| 36 | reopen | Generic sparse search remains held.  A single Frobenius-derived support hypergraph at `p=109`, with a fixed monomial cap and marked collision, is a structured falsifier rather than random support search. |
| 38 | reopen | The correction-support hypergraph retains exact exponent cancellation and saturation data, addressing the prior “tropical prevariety only” objection.  It is a tool inside Card S, not an independent tropical proof claim. |

All unchanged rows retain the corrected statuses and caveats in
`APPROACHES.md`; in particular rows 1--3 and 27 remain book/local tools, row
26 remains unlicensed without a proved support bound, row 44 remains source
triage rather than a theorem, and row 46 remains verification infrastructure.

## 2. Reranked bottlenecks after the exact deltas

### Proof-side bottlenecks

1. **A universal polynomial-origin global defect.**  It must be defined from
   an arbitrary Keller pair, not from a chosen D window or unproved
   GGV/Sigray landing, and must have a sign or vanishing theorem stronger than
   `J=1`.  This is the leading bottleneck.
2. **Turning one critical-point-free pencil member into a coordinate.**  Every
   `H_[a:b]=aP+bQ` has no affine critical point.  The missing step is to force
   at least one member to have no bifurcation at infinity; then an `A^1`
   fibration/coordinate theorem can finish.
3. **Mixed branch and missing-sheet behavior in normalization rank at least
   four.**  Rank two's pure quadratic ramification gives a forbidden unit;
   rank three is already known.  In rank at least four a branch target can
   carry both deleted ramified sheets and affine unramified sheets, defeating
   the simple discriminant/unit argument.
4. **Global landing and cofinality.**  Hybrid work still owes `G2-PSC`, pure
   Sigray work still owes source and complete landing/coverage, residue-A work
   separately owes `G2-BD`, and no absolute/cofinal type ceiling exists.
5. **Priority-safe stronger-conjecture leverage.**  HC4 is live only after the
   Meng--Yang implication and Ni quartic mechanism are replayed exactly; a
   quintic module is not yet a JC2 lemma.

### Counterexample/disproof bottlenecks

1. **A fixed polynomial support that does not escape under p-adic lifting.**
   The promoted all-Witt seed survives only by adding one new monomial per
   level.  A counterexample route needs a finite cancellation cycle or a
   different bounded-support component, not another finite Witt level.
2. **A characteristic-zero point at legal plane degree.**  Degree-three K3
   can only produce a verticality instrument.  A positive generic fibre must
   live beyond the established degree range and retain an explicit collision.
3. **Algebraization of a formal infinity survivor.**  Modular cells and formal
   germs do not supply convergence, global gluing, polynomiality, or a
   constant global Jacobian.  This remains the D/GGV counterexample wall.
4. **A direct characteristic-zero certificate with an honest global object.**
   Exact coframes are a classical equivalent formulation; a useful search
   still needs legal degree, stable literal non-`E_2` provenance, and a family
   not already killed by known bounds.
5. **A realizable finite completion/open chart.**  A rank-at-least-four tuple
   `(X,D,pi,j)` with `j(A^2)=X-D` and Keller chart would be a direct global
   counterexample object, but low-rank failures have no cofinal meaning.

## 3. Detailed idea cards

### Card P — `DUAL-PENCIL-VANISHING-DIVISOR`

**Role:** strongest proof attack; genuinely new object; cross-avenue
connection; paper-first decisive experiment.

**Exact target claim.**  Let `F=(P,Q):A^2_C -> A^2_C` be Keller and put

```text
H_[a:b] = aP+bQ,       [a:b] in (P^1)^vee.
```

Construct, on one resolved universal pencil, a resolution-independent
effective divisor `V_F` on `(P^1)^vee` whose coefficient at `[a:b]` is the
total vanishing-cycle defect at infinity of `H_[a:b]`.  Prove the scoped
claim

```text
PENCIL-ZERO:  deg(V_F)=0.
```

Because `dP,dQ` are a basis, every `H_[a:b]` has no affine critical point.
If `V_F=0`, the required endpoint is: some generic `H_[a:b]` has no
bifurcation at infinity, hence is a locally trivial `A^1`-fibration and a
coordinate; after sending it to `x`, the Keller equation makes its partner
`y+h(x)`, so `F` is an automorphism.  The endpoint is part of the target and
must be source-checked rather than assumed.

**Avenue IDs.**  `7,16,25,28,33`, with downstream use of `6` and the exact
pure-boundary identity in `AUDIT.md`.

**Novelty.**  The fresh object is not the raw pole order of an action
primitive.  It is the pushforward to the *dual target pencil* of the relative
vanishing-cycle/characteristic-cycle contribution supported at infinity.
It connects Jelonek nonproperness, D-modules, coupled pencil monodromy, log
surface intersection theory, and the exact symplectic/pure-boundary identity.
No campaign artifact presently packages all target directions in one
effective divisor.

**Evidence used.**

- EXACT: `dH_[a:b]` is nowhere zero for every `[a:b]`.
- EXACT controls: every target-linear projection of a polynomial
  automorphism is a coordinate; identity, triangular, and Hénon controls must
  return zero defect.
- EXACT hostile control: Broughton's `x+x^2y` is critical-point-free but has
  a defect at infinity; it tests whether the construction detects the missing
  global partner rather than merely `dH != 0`.
- PROMOTED correction: raw action-primitives and untwisted pole orders are
  `COSTUME`; the new object must be resolution-independent and cannot reuse
  their numerical pole order.
- EXACT input: the pure-boundary Jacobian identity is available, but no sign
  consequence has been proved.

**Dependencies and evidence tiers.**

1. `V_F` exists and is independent of the chosen common resolution —
   **PROPOSED THEOREM**.
2. Its coefficients are nonnegative vanishing-cycle multiplicities — standard
   local theory, but the universal nonproper family application is
   **SOURCE-CHECK REQUIRED**.
3. `J=1` plus the pure-boundary identity forces `deg V_F=0` — **OPEN TARGET**.
4. Zero infinity defect plus no affine critical points gives a coordinate —
   **EXPECTED CLASSICAL ENDPOINT / SOURCE-CHECK REQUIRED**.

No book landing, type bound, D source, or characteristic-p inference is a
dependency.

**Cheapest discriminator.**  On one common graph resolution of the universal
linear target pencil, derive only the first GRR/localization formula for
`deg V_F`.  Replay it on identity, `T_n`, a two-shear tame product, Hénon, and
the single-polynomial Broughton control.  Reduce every candidate term against
the pure-boundary identity and the already promoted no-log identity.  Do not
compute a residue-A client or another boundary book.

**Outcomes and interpretation.**

- `ZERO-FORMULA`: all boundary terms cancel and effectivity remains.  This is
  a provisional global lemma; enqueue different-model review and permit only
  one child proving the coordinate endpoint.
- `UNCONTROLLED-POSITIVE-TERM`: a boundary intersection survives with no
  Keller sign.  The proof target fails at its cheapest gate; bank the exact
  formula and stop this version.
- `PRESENTATION-DEPENDENT`: blow-up or source-coordinate changes alter the
  proposed divisor.  Reject the object.
- `COSTUME/DUPLICATE`: the class reduces exactly to the existing no-log or raw
  action identity.  Stop row 33's current nominee; no client calculation.
- `CONTROL-FAIL`: any automorphism receives nonzero defect.  Reject the
  construction immediately.

**Cost/time.**  Six to twelve hours of paper derivation, plus at most a small
exact symbolic checker for the controls; no AWS.

**Stop condition.**  Stop after the first resolution-independence/effectivity
check and one degree formula.  No second compactification, no new book cell,
and no client-specific tail expansion.

**Expected information gain.**  Very high.  A positive result supplies the
missing arbitrary-Keller global receiver.  A negative result cheaply retires
the strongest global-pencil mechanism and explains exactly which boundary
term survives.

**Resurrection trigger.**  A new choice-independent signed class, a theorem
identifying the surviving term with a nonnegative polynomial-origin index,
or a primary result already establishing the universal-pencil endpoint.

### Card S — `AS109-SUPPORT-CANCELLATION-GRAPH`

**Role:** strongest counterexample/falsification attack; new mechanism;
software acceleration; legal-degree bounded experiment.

**Exact target claim.**  Work at the prime `p=109`, beyond the established
plane degree range, with the exact finite-field seed

```text
P_0=x-x^109,   Q_0=y,
```

and marked collision `(0,0),(1,0) -> (0,0)`.  For a frozen cap of at most
eight correction monomials, construct the directed *Jacobian
support-cancellation hypergraph*: vertices are exponent pairs occurring in
`J(P,Q)-1`, and hyperedges are the exact derivative/bracket interactions by
which allowed `P`- and `Q`-corrections cancel a residual monomial.

The first target is the exact finite dichotomy:

```text
SUPPORT-ESCAPE: a positive integral height strictly increases on every
allowed correction interaction,
```

or

```text
SUPPORT-CYCLE: a finite strongly connected cancellation core survives all
marked-collision and normalization constraints.
```

Only `SUPPORT-CYCLE` licenses one fixed sparse coefficient scheme localized
at the seed.  A nonzero completed generic fibre after inverting 109 would
then give a legal-degree characteristic-zero Keller collision; it is not
inferred from the graph or from finite Witt points.

**Avenue IDs.**  `19,34,36,38`, with exact local-scheme logic from the
fixed-stratum work and the all-Witt control as the negative model.

**Novelty.**  This is neither unrestricted next-Witt lifting nor generic
sparse search.  It searches for a *finite exponent feedback cycle* capable of
replacing the promoted tower's one-new-monomial-per-level escape.  The object
connects the horizontal-pole obstruction, Newton support geometry, and a
verified SAT/integer-linear support certificate before any coefficient GB.

**Evidence used.**

- EXACT: over `F_109`, the seed has Jacobian one, generic degree 109, and the
  marked collision.
- EXACT first lift equation: for
  `P=P_0+109A`, `Q=Q_0+109B`, the divided first residual modulo 109 is
  `A_x+B_y-x^108`; `B=x^108y` kills it.
- PROMOTED control: the canonical all-Witt solution continues by adding
  `x^{n(108)}y`, so its support has a strict escaping ray and no finite cycle.
- K3 warning: a full low-degree coefficient scheme can be singular and
  compiler-heavy; support logic must precede coefficient algebra.

**Dependencies and evidence tiers.**

1. Complete enumeration of hyperedges under the frozen monomial/gauge cap —
   **EXACT SOFTWARE CLAIM**, requiring an independent enumerator and negative
   controls.
2. A height certificate proves escape only for the registered support class,
   not all polynomial lifts — **EXACT SCOPED NEGATIVE**.
3. A cycle is only a candidate support — **HEURISTIC/EXPERIMENTAL** until the
   coefficient scheme is formed.
4. A nonzero localized generic fibre is the first characteristic-zero bridge
   — **EXACT CONDITIONAL DEDUCTION** after faithful-flatness and collision
   replay; no modular shortcut is allowed.

**Cheapest discriminator.**  A pure integer/exponent engine enumerating at
most eight correction monomials, with collision and gauge constraints, and
returning either an explicit integral height vector or one minimal strongly
connected core.  Cross-check with an independently written enumerator.  No
coefficient Gröbner basis, no `W_3`, and no fleet job at this stage.

**Outcomes and interpretation.**

- `HEIGHT-CERT`: exact no-finite-support result for the frozen motif/cap; bank
  the certificate and stop.
- `CYCLE`: freeze the support and permit one speculative child constructing
  the exact integral coefficient scheme; enqueue hostile review first.
- `CYCLE-BUT-GAUGE`: the apparent feedback is a coordinate/normalization
  orbit; reject it.
- `COEFFICIENT-EMPTY`: if the one licensed child returns an exact unit
  certificate, close only that support.
- `GENERIC-FIBRE-NONZERO`: independently replay determinant, collision,
  degree, and characteristic-zero point; this would be a provisional direct
  counterexample candidate, not a promotion.

**Cost/time.**  Four to eight hours for the support engine and independent
replay on the local machine.  A coefficient child is separately costed and
not part of the first gate.

**Stop condition.**  One prime, one Frobenius seed, eight correction
monomials, one normalization.  No cap widening merely because no cycle was
found; no AWS and no generic fewnomial search.

**Expected information gain.**  High.  It either gives the first mechanistic
explanation of bounded-support escape or emits a small, legal-degree support
that reaches the exact fixed-scheme bridge.

**Resurrection trigger.**  A mathematically new feedback motif, an invariant
showing the cap is incomplete, or a cycle produced by a different seed.  A
request for nine rather than eight monomials is not by itself a trigger.

### Card Q — `QUARTIC-RESOLVENT-OPEN-CHART`

**Role:** direct-plane proof/falsification gate at the first open generic
degree; new cross-connection between normalization and monodromy.

**Exact target claim.**  Let `R/A`, `A=C[P,Q]`, be the finite free normal
rank-four algebra in the canonical Zariski-Main completion of a hypothetical
Keller map, with `U=Spec C[x,y]` open in `X=Spec R`.  Form the oriented cubic
resolvent algebra `C(R)/A`.  Test the precise inheritance lemma

```text
QROI: the A^2 open chart and Keller-etale locus induce on Spec C(R) an open
rank-three chart with trivial units/class group data strong enough for the
Orevkov degree-three no-go.
```

`QROI` would exclude generic degree four.  The gate is equally designed to
produce an exact mixed-sheet countermodel showing that the resolvent does not
inherit the required chart.

**Avenue IDs.**  `31,25,26`, with the rank-two completion perimeter and
Orevkov's degree-two/three theorem as evidence, not as a new result.

**Novelty.**  Rank-three continuation is known and therefore stopped.  The
new connection is to use the cubic resolvent of the *first open rank* and to
track deleted versus affine sheets under the action on the three pair
partitions of four sheets.  This is not an unbounded primitive-group census.

**Evidence used.**

- EXACT: `R` is finite free; `U` is an open chart; boundary classes freely
  generate `Cl(X)`; units on `R` and `U` are constants.
- KNOWN: Galois function-field extensions are closed; Orevkov excludes
  generic degrees two and three.
- EXACT obstruction from rank two: a branch target has only the ramified
  sheet, so the trace-zero generator becomes a forbidden unit.
- OPEN rank-four issue: a branch target may mix deleted ramified sheets with
  affine unramified sheets; this is precisely what the resolvent incidence
  must retain or expose.

**Dependencies and evidence tiers.**

1. Global cubic-resolvent construction for the registered finite locally free
   quartic algebra — **STANDARD THEORY / SOURCE-CHECK**.
2. Open-chart/unit/class inheritance — **OPEN TARGET**, not implied by the
   rank-two proof.
3. Application of Orevkov requires the inherited object to have the exact
   polynomial/Keller hypotheses, not merely degree three — **LOAD-BEARING**.

**Cheapest discriminator.**  Enumerate the five transitive quartic monodromy
types (`S4,A4,D4,V4,C4`) and their inertia cycle types, then compute the
induced action on the three pair partitions.  Track, symbolically, ramified
boundary sheets versus affine unramified sheets and the corresponding unit
and divisor-localization data.  Stop as soon as one admissible mixed-sheet
pattern destroys `QROI`, or all patterns force the inherited open chart.

**Outcomes and interpretation.**

- `QROI-FORCED`: a provisional rank-four no-go after the polynomial/Keller
  hypotheses are independently checked.
- `MIXED-SHEET-CONTROL`: the resolvent bridge is false under the exact
  perimeter; stop rank-four continuation and retain the control for all
  completion proofs.
- `GALOIS-ONLY`: the calculation recovers only Campbell/Razar/Wright; no new
  result, stop.
- `NEEDS-POLYNOMIAL-INPUT`: group/divisor data permit both outcomes.  Do not
  enumerate more groups; the missing polynomial-origin invariant becomes the
  explicit resurrection condition.

**Cost/time.**  Six to ten hours of paper algebra plus a tiny exact
permutation/incidence checker; no surface construction and no AWS.

**Stop condition.**  Generic degree four only.  No rank five, no family of
finite covers, and no claim from group incidence alone.

**Expected information gain.**  Medium-high.  It either closes the first
open mapping degree by a direct plane argument or pinpoints why all
discriminant/resolvent proofs lose the polynomial chart.

**Novelty/priority risk.**  High: quartic-resolvent JC literature may already
contain the gate or its failure.  Primary-source sweep is required before any
novelty claim.

**Resurrection trigger.**  A polynomial-unit theorem eliminating the mixed
pattern, a source proving `QROI`, or an explicit quartic completion/open-chart
control.

## 4. Nominee adjudication

### `ACTION-RESIDUE-INDEPENDENCE`

**Do not launch as stated.**  The promoted raw-boundary probe already found
that untwisted action-residue charge and raw primitive pole order are
presentation-dependent or consequences of `J=1`.  Merely reducing one more
action residue modulo the Jacobian/no-log ideal risks repeating that exact
`COSTUME` result.  It can be resurrected only with a named boundary twist or
minimization theorem that is resolution-independent and a preregistered
quotient proving the class differs from the existing no-log pin.

Card P retains the useful symplectic insight but changes the object: it varies
the entire target pencil and measures vanishing cycles, not raw primitive
poles.  It therefore outranks the action nominee.

### `HC4-QUINTIC-MODULE`

**Keep as the sole orthogonal paper reserve, not the primary root.**  The
bounded gate is soundly designed: primary-source freeze of the Meng--Yang
implication and Ni quartic argument, exact quartic replay, then one quintic
`GL_4` obstruction module.  It stops before degree six or an all-degree
claim.  It ranks below Cards P and Q because it attacks a stronger conjecture,
has the campaign's largest model dissent, and may only show that the quartic
method does or does not extend.  It ranks above reopening any stopped D/K3
representation because its input can be made finite and source-complete.

### Better alternative

`DUAL-PENCIL-VANISHING-DIVISOR` is the better first root.  It starts from
every arbitrary plane Keller pair, is intrinsically two-dimensional, has a
coordinate endpoint, uses no unproved landing/type bound, and has a one-formula
fail gate.  Its risk is mathematical rather than provenance or compiler
ambiguity.

## 5. Major-program calls

| Program | Call | Exact scope |
|---|---|---|
| D-series/formal germ | **STOP unchanged representation; REDESIGN only** | No band 28, deeper D, Ore/Spencer/Hankel, or integral D43 until a named full-polynomial source point and tangent functor exists.  A new source compiler or genuine algebraization theorem is a resurrection event. |
| GGV/Sigray | **CONTINUE theory; STOP new cells** | Work only on `G2-PSC`, pure-Sigray source and complete landing/coverage, and `G2-BD` where residue-A is actually reached.  Do not conflate the gaps or use the farm as proof input without transport. |
| Boundary/action/trace | **REDESIGN** | Raw passports, untwisted action charges, primitive pole orders, and the current trace packet stay stopped.  Card P is the allowed fresh global object; a richer trace receiver still owes coordinate multiplication and target-divisor-tagged branch pairing. |
| Local-bound programs | **STOP census expansion; REDESIGN around realization** | No more DIR/A-SCALE census or fixed-type bound.  The live question is whether the formal pole/carrier families algebraize, or whether one universal polynomial-origin sign excludes them. |
| Witt/characteristic-p | **REDESIGN** | Stop K3 and unrestricted next levels of the existing seed.  Card S permits one legal-degree support-cycle gate; a cycle must enter one fixed integral scheme before any characteristic-zero language. |
| Exact coframe | **STOP fixed row and low-degree orbit** | Bank the classical equivalence and reviewed Broughton/Cohn no-go.  Reopen only for an obstruction-preserving parametric family whose possible integrated degree is legal and whose first gate is not cap creep. |
| Finite normalization | **CONTINUE via rank-four redesign** | Do not run rank three.  Card Q tests the first open rank and stops on mixed-sheet inheritance failure; no cover enumeration. |
| External artifacts/intelligence | **CONTINUE** | Complete broad sweep #9 and primary-source checks for Card P's endpoint, quartic resolvents, and HC4.  Exact-equivalent artifacts remain one mathematical lineage, not independent votes.  No public contact or disclosure. |

## 6. Shared hidden assumptions and hostile self-attack

### Shared hidden assumptions

1. A single compactification of the universal target pencil exists with
   enough functoriality to make `V_F` resolution-independent.
2. Vanishing-cycle multiplicities at infinity assemble into an effective
   divisor on the dual pencil rather than a complex with cancellations.
3. Zero infinity defect plus no affine critical points really forces an
   `A^1`-fibration/coordinate, including connectedness and special-fibre
   issues exposed by Broughton.
4. Polynomial origin contributes more than the already exhausted determinant
   and no-log identities to the degree of `V_F`.
5. The eight-monomial support hypergraph is complete modulo the declared
   gauge and collision constraints; a missing coordinate orbit could fake
   either escape or a cycle.
6. `p=109` is useful because it is beyond the established degree range, but
   high degree alone does not make a modular component more likely to lift.
7. Quartic resolvents preserve enough of an affine open chart to make
   Orevkov relevant; field-degree reduction alone plainly does not.
8. Literature priority is incomplete for all three cards.  “Fresh to this
   campaign” is not a novelty claim.

### Hostile attack on Card P

The likely failure is that `V_F` is well-defined and effective but has a
strictly positive degree measuring boundary complexity.  The pure-boundary
identity controls a determinant, not the positive part of a relative
vanishing-cycle cycle—exactly the sign failure seen in DIR/RPMC and raw
boundary capacity.  Defects can move with `[a:b]` while their total remains
positive, so packaging every pencil direction may merely conserve the missing
mass rather than kill it.  Worse, a common resolution may introduce vertical
components whose multiplicities change under harmless blowups; forcing
resolution independence could quotient away precisely the hoped-for sign.

The first gate is therefore deliberately hostile: derive the degree formula
before computing any Keller client.  If an uncontrolled positive boundary
term remains, stop.  Do not reinterpret it as “promising evidence”.

### Event that invalidates this ranking

Any of the following forces an immediate rerank:

- a primary theorem or exact control showing the universal-pencil defect is
  presentation-dependent, identical to no-log, or can have positive degree
  under the full Keller hypotheses;
- a source-verified HC4 quintic module with a decisive vanishing map, which
  would move HC4 above Card Q;
- an independently confirmed finite support cycle at legal degree, which
  would move Card S to the campaign's leading counterexample root;
- a known quartic generic-degree theorem or a mixed-sheet counterexample to
  `QROI`, which closes Card Q before launch;
- any credible proof/counterexample or external actor result, per the outer
  loop's critical-event rule.

## 7. Proposed four-root portfolio

This is a scheduling recommendation only.  With four reasoning slots, the
coordinator remains one slot and activates at most three roots at once; the
fourth stays queued as the orthogonal replacement.  Shares are campaign
wall-clock targets, not simultaneous slot fractions.

| Root | Share | First deliverable | Immediate stop |
|---|---:|---|---|
| **P — dual-pencil vanishing divisor** | 35% | Resolution-independence/effectivity statement and first exact degree formula on controls | presentation dependence, costume/duplicate, uncontrolled positive term, or control failure |
| **S — AS109 support-cancellation graph** | 25% | Independently replayed height certificate or one minimal support cycle at the frozen cap | height certificate, gauge cycle, no cycle at cap, or any silent cap widening |
| **Q — quartic resolvent/open chart** | 20% | Rank-four monodromy/resolvent incidence table with exact chart-inheritance verdict | mixed-sheet control, Galois-only recovery, or need for an unnamed polynomial invariant |
| **H — HC4 source/quintic reserve** | 20% | Primary-source bridge freeze, quartic replay, and at most one quintic obstruction module | source mismatch, quartic replay failure, first decisive module map, or degree-six expansion |

Governance for every root:

- a producer result must pass the five-part provisional gate before any child;
- different-model hostile review is enqueued immediately on provisional
  status;
- at most one cheap, reversible dependency generation is allowed;
- no publication, fleet expansion, public contact, or held representation is
  unlocked by a producer verdict;
- box01's checkpointed legacy process is untouched; Box02/Box03 stay stopped;
- a stopped first root is replaced by H rather than widened;
- unrelated roots continue while review runs.

## 8. Final zero-base verdict

Do not choose between the two packet nominees as though they exhaust the
space.  The action nominee is currently too close to a reviewed `COSTUME`;
HC4 is a valid but indirect reserve.  The best next proof discriminator is
the universal dual-pencil vanishing-cycle divisor.  The best counterexample
discriminator is a legal-degree finite support-cycle search at `p=109`, with
the generic-fibre bridge held explicit.  The first-open-degree quartic
resolvent gate is the direct-plane structural hedge.

No statement here proves or disproves JC2.  No claim is promoted and no work
is launched.
