# Cross-pollination decision memo — round `20260827T0145Z`

Lane: Opus 5, cross-pollination adjudicator (not an independent ideation
submission).
Date: 2026-08-27.  Repo `/Users/dc/code/math/jc2`, charged HEAD
`418e413593120d19e15e6546eb50c985f4b1f038`.

## 0. Inputs, custody, tool boundary

All seven prompt-supplied SHA-256 values were recomputed on disk before any
reading and all seven match:

```text
2b47b8003e57574583089effb1ec28dca634fa1280f13b2ed7946c650ae5690f  ideation-20260827T0145Z-root.md
08c69fd2483fc8a81dd3649809d148589de1fbe657135405f81bd5ca0c4a3fba  ideation-20260827T0145Z-grok.md
1a65cb78572c0d0677c5ae91be3875c53c730987d148e302122afcb0e3196059  ideation-20260827T0145Z-fable5.md
60e198036854cce58a74e30a11db4df20d62e10e31b61f2a698c93a1594736b0  ideation-20260827T0145Z-opus5.md
959603e311fb02254488c57c49edc1b79837dc72987d3b9253c8c176eebb1623  ...prefix-zero-sections-hostile-review-grok-20260827.md
678a087d0845a4ccba568d7a6f4977af3452e3f322724ae46b2e524bd681f93d  ...unit-k10-localizer-filing-hostile-review-grok-20260827.md
7af66e58a7262ca05bf140919ed3d6ff4e0357bdb6db3378d494907ff33baa8f  ...t-cs-direct-total-certificate-opus5-20260827.md
```

The 22 frozen exact-`Q` source rows were rehashed against the V9
`COEFFICIENTS.json` / V17 manifests before use; all 22 match the digests
printed in the two Grok reviews and in the direct-certificate report.

Tool boundary honoured: no web, no AWS read or mutation, no campaign launch,
no `jc2-lean`, no Groebner/standard basis/CAS.  Desk work was `cat`, `grep`,
`shasum`, and five short pure-`python3` sparse-`Fraction` scripts written
under `/tmp/xp0827/` (never committed, never run against AWS).  Those scripts
do exact monomial parsing, exact evaluation, exact polynomial identity
expansion, integer nullspace by Gaussian elimination, and modular point
construction — nothing that would count as heavy local algebra.  **The only
repository file written is this one.**  No source or ledger file was edited.

Evidence labels used below.  **VERIFIED-HERE** = I expanded or evaluated it
myself against the frozen bytes in this session, and the derivation is stated
so a reviewer can redo it.  **PROMOTED** = charged, different-model reviewed.
**PROVISIONAL** = exact but reviewed only by its own producer.
**NAVIGATION** = routing, not a theorem.  **SPECULATION** = proposal.
Nothing here proves or disproves JC2.

Everything labelled VERIFIED-HERE is producer-tier from this lane and needs
different-model hostile review before promotion or downstream consumption.

---

## 1. Deduplication: what the four reports actually contain

### 1.1 The eleven genuinely distinct mechanisms

Stripping restatement, the four blind reports contain eleven distinct
mechanisms, not the ~24 cards they nominally carry.

| # | Mechanism | Proposed by | Distinctness note |
|---|---|---|---|
| M1 | Exact horizontal zero-section of the frozen prefix at `k=0` (`CS0`) | root §3.1 | Only root produced the object; grok Card B's discriminator *is* this evaluation, unrun |
| M2 | `k=0` / `k10` filing and ontology (registered unit vs residual stratum) | root Card A, fable5 §3.4, grok Card B, opus5 §3.4 | Four-way, four different framings, one object |
| M3 | Vertical `rho`-torsion as an arc-exclusion certificate (`rho^N=0` without empty special fibre) | root §3.2 | Unique to root |
| M4 | Additive-to-multiplicative typing criterion (`cs^N` divides the `rho`-cofactor) | fable5 §3.2–§3.3 (Lemmas A, B) | Unique to fable5; the sharpest single piece of analysis in the four reports |
| M5 | Divided-row `E`-gate at `cs=0` | fable5 §3.4 | Unique to fable5 |
| M6 | Grading/type-directed certificate synthesis instead of ideal-membership lift | opus5 §3.2–§3.7, grok §3+§5, root §5 | Three lanes, three engines, one idea: *predict the type, then solve a linear system* |
| M7 | `J1=0` restriction as a stage-two pre-diagnostic | fable5 §3.5, grok Card C, opus5 §3.6 | Three-way; identical computation, three opposite predicted outcomes |
| M8 | Total `T-cs` fibre = unspecialised `p=0` odd sheet (same leading form) | grok §3 | Unique to grok; a genuine ledger merge |
| M9 | AS109 arithmetic `(deg_y, v_109)` Newton polygon with `AS-TRI` as first corner | root §3.3, opus5 §4.3, fable5 C2 | Three-way convergence, independently derived |
| M10 | AS109 source-gauge group and explicit gauge section | opus5 §4.1–§4.2 | Unique to opus5; supplies one of the two ingredients the `SUPPORT GRAMMAR STOP` names as missing |
| M11 | `109^K ∈ I_S` all-depth death certificate | fable5 Card 3 | Unique to fable5 |

Everything else in the four reports is either charged history restated
(`RHO-STAGED`, `DECK-ISO`, `PROJ-IRR`, `A(F)-ENDPOINT`, `AS12-PINCER`,
`3P-STRIP`, `EFFECTIVE-DEATH` as a ranking), process hygiene (opus5 §5.1
covering-lemma column, grok's unordered-`T-c1` scope note), or software
packaging of M6 (root's telescoping IR, fable5's `CERT-TYPER`, grok's bounded
ansatz, opus5's bigrading validator — four names for one tool).

### 1.2 Convergences that raise confidence

**C-A. `k=0` is the single named object all four lanes independently ranked
into their top three.**  Four different derivations, no shared premise beyond
the freeze.  This is the strongest signal in the round and the post-freeze
news confirms both halves of the filing question.

**C-B. The certificate type is predictable before it is searched (M6).**
Three lanes reached this by different routes: grok by "first surviving row",
opus5 by a grading lattice, root by divided-difference polarisation.  I
tested it and it is **substantially right, with one of the two proposed
gradings wrong** (§2.4).  The predicted-then-solved architecture is correct;
one of the three lanes' specific instrument is not.

**C-C. The AS109 next move is a two-axis arithmetic Newton polygon, not
another rectangle (M9).**  Root, opus5 and fable5 derived the same `n≥2`
corner equation independently and reached compatible conclusions about where
integrality stops being automatic.  Three-way independent convergence on a
disproof-side mechanism is rare in this campaign and should be weighted.

**C-D. Saturation and residue-preserving shear are the two legal
replacements for a false inversion (grok §3, methodological).**  This
correctly unifies the `T-c0`/`T-c1` exceptional-unit repair with `AS-TRI`'s
refusal to invert the top `y`-coefficient.  It is not a theorem and should
not be promoted, but as a review heuristic it has now caught two real defects
and is worth writing into the promotion checklist.

**C-E. Independent blind lanes found the same syzygy.**  opus5 §3.5's
collapse argument and the direct certificate's §3 core rest on the identical
two combinations.  I verified both against the bytes (§2.2).  Two blind lanes
plus one producer converging on `Tg10_3 - (rho^2/2)Tg10_1 = (3/16) c0 c1` is
meaningful corroboration of the frozen `Tg10_1`/`Tg10_3` bytes.

### 1.3 Genuine disagreements the coordinator must adjudicate

| Item | Split | My adjudication |
|---|---|---|
| Row 5 (JvdK descent) | root R, opus5 R / grok U, fable5 U | **Raise.** Both raises give the same, correct reason: `AS-TRI` closes by *integrality*, not automorphy, which is precisely the recorded stuck-point |
| Row 21 (p-adic injectivity) | root R, grok R / fable5 U, opus5 U | **Bookkeeping only.** Score `AS-TRI` under 19, cross-reference 21. No capacity consequence either way; do not spend adjudication time |
| Row 18 (graded/GIT) | opus5 `reopen` / others U | **Reopen, weakened.** A rank-two torus does act (§2.4 confirms rank exactly 2). The *specific* second grading opus5 named does not exist. Reopen as a proof tool; the counterexample-side closure stands |
| Row 31 (Rees/ZMT) | root R, grok R, opus5 R / fable5 U | **Raise**, 3–1, on independent evidence |
| Stage two cost | opus5 §3.6 "row-disjoint, fresh computation" / fable5 §3.5 and grok Card C "cheap diagnostic first" | **fable5/grok are right and opus5 §3.6 is refuted** (§2.5). I ran the diagnostic |
| V19 disposition | grok "continue then type-gate", fable5 "continue", opus5 "redesign" | **Stop the mathematics, keep the protocol run.** See §5 |

---

## 2. Attack: each connection, at its true scope

I attacked the load-bearing claims by expanding them against the frozen
bytes.  Six survive, three need scope repair, two are refuted.

### 2.1 EXACT and confirmed — the `deg_s` grading (repair of opus5 §3.2)

**VERIFIED-HERE.**  I built the integer exponent matrix of all 22 frozen rows
(40 variables, 641 homogeneity constraints) and computed the nullspace
exactly.

```text
grading lattice rank = 2                      <- opus5's rank-two claim CONFIRMED
```

The lattice contains a distinguished element: the unique-up-to-scale grading
with `deg_s(rho) = 0`, normalised by `deg_s(cs) = 2`.  It extends to **all
forty** names, all weights are `>= 0`, and

```text
deg_s( Tg{g}_j ) = g   for all 22 rows, with no exceptions.
```

The full table (this is new data; the campaign has only ever used the row
label):

```text
0: rho
1: ell1
2: cs, ell2, rs
3: cs1, ell3, rs1
4: cs2, ell4, k, rs2
5: a0, a1, c0, c1, cs3, k1, rs3
6: aa0, aa1, cs4, e0, e1, k2c, rs4
7: aaa0, aaa1, ee0, ee1, k10_3
8: ac3, az3, ec3, ez3, k10_4
9: ac4, az4, ec4, ez4
```

Read it: `deg_s` is the **sigma-order** of a jet.  Each sigma-derivative
raises it by exactly one (`k→k1→k2c→k10_3→k10_4` = 4,5,6,7,8;
`cs→cs1→cs2→cs3→cs4` = 2,3,4,5,6; `c0→e0→ee0`, `a0→aa0→aaa0`,
`ell1→ell2→ell3→ell4`).  This is a hard, checkable fact about the frozen
prefix and it is the backbone of §4.

### 2.2 EXACT and confirmed — the grade-10 core and the collapse theorem

**VERIFIED-HERE.**  The genuine full bytes of `Tg10_1..Tg10_4` are exactly
what opus5 §3.1 displayed (those four displays are not truncations).
Therefore opus5 §3.5 stands as written, and there is a sharper unconditional
form it did not state:

```text
Tg10_3 - (rho^2/2)*Tg10_1  =  (3/16) c0 c1        identically, no k=0 needed
(32/3) Tg10_4              =  c0^2 + rho^2 c1^2
```

from which `V(k) ∩ V(Tg10_1..4) ⊂ V(c0,c1)` follows by opus5's three-line
argument, which I re-expanded and confirm.  This is the same pair of
combinations the direct-certificate producer calls `alp` and `bet`.  Two
blind lanes and one producer, independently.

### 2.3 EXACT and confirmed — branch (a) of the pending direct `T-cs` claim

This is the highest-value verification in the memo, because a live review is
running on it.

**VERIFIED-HERE.**  Working in the substituted presentation
(`rs → 0`, `c0 → cs*qc0`, `c1 → cs*qc1`), with the printed cofactors
`A1..A4` of §4 of the direct-certificate report, expanded term by term
against the frozen bytes:

```text
cs^6 * k^2 * rho^6 = A1*E(Tg10_1) + A2*E(Tg10_2) + A3*E(Tg10_3) + A4*E(Tg10_4)
                     residual: 0 terms.   EXACT IDENTITY CONFIRMED.
```

I also confirmed the four core identities `gam`, `del`, `alp`, `bet` and the
auxiliary `Tg10_5 = (rho^2/2)Tg10_3 - (3/8)rho^4 Tg10_1`.

I did **not** verify branch (b): its two reductions (5.3), (5.4) are 1880-
and n-step machine rewritings whose cofactor vectors `C`, `D` are published
only as SHA-256, and the producer itself flags them as not of hand-checkable
character.  Branch (b) is the whole of the live review risk.  §3 exploits the
fact that branch (a) alone is enough to make that risk small.

### 2.4 REFUTED — opus5's second grading `deg_2`, and with it §3.4's `M >= 1`

**VERIFIED-HERE.**  opus5 §3.2 posits a second grading with
`deg_2(rho) = deg_2(cs) = 0`, `deg_2(k) = 2`, `deg_2(c0,c1,a0,a1,e0,e1) = 1`,
conditional on all rows being `deg_2`-homogeneous of degree 2.  That
condition is **false**, and the obstruction is structural rather than a
coefficient accident:

> Any element `g` of the grading lattice with `g(rho) = 0` is proportional to
> `deg_s` (that condition cuts the rank-two lattice down to one dimension),
> and `deg_s(cs) = 2 != 0`.  Hence **no grading of the frozen row set has
> `g(rho) = 0` and `g(cs) = 0` simultaneously.**  `deg_2` is not extendable.

Concretely, with the unassigned names taken as weight zero, `Tg12_2` realises
`deg_2 ∈ {0,1,2,3}` and `Tg14_5` realises `{0,1,2,3,4}`.  opus5's own Card A
stage 1 is exactly this check; it returns *falsify*, in minutes, as the card
predicted it might.

**Consequences, and what survives.**

- **Withdraw** opus5 §3.4 ("on the `rs`/`cs` charts the `k`-localizer power
  is forced, `M >= 1`") and the `deg_2` half of §3.7.  The proof uses
  `deg_2(cs) = 0` and `deg_2(k) = 2` and has no replacement in the true
  lattice.  It must not be cited, and in particular **must not be imposed as
  a V19 acceptance gate** — that gate would have been unsound.
- **Survives, now unconditional rather than conditional:** for a certificate
  `cs^N k^M (1 + rho W)` that consumes a grade-`g` row, taking the
  `deg_s`-homogeneous component (legitimate, since every generator is
  `deg_s`-homogeneous and every variable has `deg_s >= 0`) forces the
  cofactor to have `deg_s = 2N + 4M - g >= 0`.  With `g = 14`:

  ```text
  2N + 4M >= 14 ,  i.e.  N + 2M >= 7 .
  ```

  The pending `(N,M) = (447,164)` satisfies this with enormous slack.
- **Survives:** opus5 §3.7's *other* argument — that a grade `>= 13` row is
  mandatory — is independent of `deg_2`.  It reduces `(*)` mod `rho` and
  invokes the promoted nonempty grade-10–12 prefix fibre.  That argument is
  correct, and "nonzero `Tg14_5` cofactor" remains a sound acceptance gate.
- **Survives:** row 18's reopen.  A rank-two torus really does act.  Only the
  particular second character was misidentified.

### 2.5 REFUTED — opus5 §3.6, "stage two is row-disjoint from stage one"

**VERIFIED-HERE.**  I ran the diagnostic that fable5 §3.5 and grok Card C both
queued (restrict all 22 frozen rows to `rs = cs = c0 = c1 = 0`):

```text
first nonzero grade on V(J1) : 11        (not "no information")
rows surviving               : Tg11_1,2,3,5,7  Tg12_1,2,3,4,5,7  Tg14_5   (12 of 22)
a0 or a1 present             : in 11 of those 12
```

opus5 §3.6's claim is true of the five rows it could read verbatim and false
of the row set.  The correct statement is the opposite of the one filed:
**stage two is not a fresh computation on a disjoint support; the frozen
prefix already sees `a0`, `a1` on `V(J1)` from grade 11 onward.**  §4 shows
it sees them in a very specific shape.

grok Card C's four-way outcome menu is therefore resolved to its third
branch ("genuine two-chart `J2` problem"), and fable5 §3.5's ten-minute desk
pass is discharged: the answer is grade 11.

### 2.6 SCOPE REPAIR — fable5 §3.4's `k=0` mechanism

fable5 argues: *on the prefix fibre `12 e1^2 = 5 cs^4 k`, so `k=0` forces
`e1=0`, killing `Tg14_5 ∝ cs e1^2`; hence the `k=0` decisive grade is `>14`.*

The **conclusion is right**.  The **stated mechanism is a ring/scope
mismatch** and must not be reused.  `12e1^2 = 5cs^4 k` is the restriction of
`Tg12_2` to the five-zero slice `qrs=rho=qc0=qc1=e0=a0=ell1=0` *inside*
`D(cs*k)`.  At `k=0` one is off `D(cs*k)`, and the full `Tg12_2` has 36
terms, not two.  I exhibit an explicit counter-witness in §4.3: a point with
`k = 0` and `e1 != 0` at which all 22 frozen rows vanish.  The true reason
grade `<= 14` cannot decide `k=0` is the zero-section/point evidence of §4.3,
not the slice relation.

### 2.7 SCOPE REPAIR — fable5's Lemma B consequence, and the `E`-gate

fable5's Lemma B ("a typed total certificate exists iff an additive
certificate exists whose `rho`-cofactor is `cs^N`-divisible mod the ideal") is
**correct as a biconditional** — a typed certificate *is* such an additive
one.  The inference drawn from it is not:

> *"the entire gap ... is `cs^N`-divisibility of the `rho`-cofactor, i.e. an
> obstruction that lives on `E = V(cs)`"*, and *"if the E-restricted ideal
> has a positive-dimensional `rho`-non-unit locus, no amount of cofactor
> harvesting repairs it."*

Two defects.

1. **The divisibility can be bought rather than found.**  See §3.1: given any
   additive certificate and any `rho`-torsion certificate, one multiplies and
   obtains a typed certificate with `W = 0` outright.  Failure of
   divisibility at one `(N,M)` says nothing about existence at another.
2. **The proposed computation tests the wrong ideal.**  fable5 §3.4's `E`-gate
   restricts the *naive divided rows* `row∘subst / cs^{d_row}`.  Those
   generate a subideal of the honest chart ideal `(I : cs^∞)`, not the
   saturation.  A positive-dimensional `rho`-non-unit locus for the subideal
   does not obstruct a typed certificate.

Empirically the gate is already discharged where it matters.  Branch (a)
(§2.3) gives `cs^6 k^2 rho^6 ∈ I`, hence `k^2 rho^6 ∈ (I : cs^6) ⊆ (I : cs^∞)`,
so **in the saturated chart ring `rho` is nilpotent on `D(k)` all the way
down to `E`**.  fable5's Card 1 outcome (ii) — "explicit nonunit residual ⟹
stop all V19-successor cycles at once" — cannot occur on `D(k)`.  Card 1 is
off the critical path.

### 2.8 CORRECT but weaker than filed — grok §3's odd-sheet identification (M8)

grok's observation that `Tg14_5 = -(7/256) cs^5 k` on the `T-cs` fibre and the
order-two `p=0` odd-sheet raw unit `E_(5,14) = -(7/256) k0 cs^5` are the same
leading form in two presentations is a real and useful ledger merge, and the
`k = k0` half of it is now independently confirmed by the unit-`k10` filing
review.  Two cautions.

- The consequence *"the `k=0` complement of `T-cs` is the total-source lift of
  the old `k0=0` residual"* is **NAVIGATION, not a theorem**.  Agreement of a
  leading form on one fibre does not identify two schemes.  The `k10` filing
  review makes exactly this point when it refuses to collapse the exact-square
  hyperplane `k10=0` with the total-source series readings.
- grok's inference *"spending V19 on `D(k)` does not touch it"* is correct and
  is now doubly supported.

### 2.9 The `k10` filing, and the one ring mismatch that matters

The post-freeze filing review settles M2 and, in doing so, refutes one
sentence that several lanes were relying on informally.  Restating it because
it is the single most abused piece of scope in the round:

- `k = k0 =` **the constant term** of the source series `k10`.  It is **not**
  the series.
- The series `k10 ∈ R[[sigma]]` is a unit iff its constant term is a unit of
  `R`; over the polynomial coefficient ring `R` the indeterminate `k` is *not*
  a unit.  "Formal-series unit", "field-valued nonzero", and "algebraic
  localizer in a certificate" are three operations in three rings and are not
  one `iff`.
- Licensed filing: the named Gate-T family's registered open **is** `D(k)`, so
  `V(k)` is not an *extra on-family* Gate-T residual to budget beside the six
  Rees charts.  Off-family is **not** closed.  The factor `k` stays literally
  in every identity; it is not exceptional and may not be dropped.
- The complement is a **sibling load-timing fan** with at least two readings
  the review explicitly refuses to collapse: *zero leading load* and
  *delayed / positive-order load*.

Root's Card A outcome (ii) is the one that obtained.  Root's outcome (i)
("makes `D(k)` scope-free ... removes the apparent complement from both first-
stage charts") is the reading the review **declines**: `D(k)` is intrinsic to
the *named family*, which removes a double count, not a boundary.

### 2.10 Disproof-side connections: what is exact, bridge, and speculation

| Claim | Tier | Note |
|---|---|---|
| `AS-TRI` is the `n=1` corner of a `(deg_y, v_109)` polygon (root §3.3, opus5 §4.3) | **plausible bridge** | The corner equation `p_m^n = c q_n^m` with leading forms powers of a common `h` is standard; that `AS-TRI` instantiates it at `n=1` is exact. That the polygon *walks* is unproved |
| `x`-side descent is one-directional (opus5 §4.3) | **exact given `deg_x(109A) < 109`** | Stated with its hypothesis; the hypothesis is not free and must be carried |
| Quadratic-residue obstruction at `n=2`, `m` even (fable5 C2) | **plausible bridge** | `p_m^2 = c q_2^m` needs `c` square in `Q_109`; whether a nonresidue blocks or twists is genuinely open and cheap |
| Source-gauge group is free (opus5 §4.1) | **exact**, and the Fermat-quotient/`mod 109^2` caveat is correctly stated | Compatible with the wild-symplectic gate; opus5 states the distinction precisely and I accept it |
| Gauge section for `deg_x A <= 108` (opus5 §4.2) | **exact at that scope**, supplies *one of two* named missing ingredients | Does not touch the `(x + 109 y^m, y)` triangular family that generated the `SUPPORT GRAMMAR STOP`. opus5 says so |
| `109^K ∈ I_S` ⟹ all-depth death (fable5 M11) | **exact and elementary; the client does not exist** | Registration scope distinction from the held rigid-leaf lane is real and fable5 flags it |
| Staged certificate calculus exported to residue-A book cells (fable5 C1) | **speculation** | fable5 states the blocker honestly: the cells have no finite presentation. If one cannot be written, that failure *is* the landing/coverage wall. Do not fund |

---

## 3. Re-ranking, conditional on both outcomes of the direct-`T-cs` reviews

### 3.1 The lemma that makes the conditional cheap

**VERIFIED-HERE (elementary).**  Let `I` be an ideal of a commutative ring
and `rho` an element.

> **Torsion-multiplier lemma.**  If `f - c*rho ∈ I` (a special-fibre
> certificate: `f ∈ I + (rho)`) and `g*rho^r ∈ I` (a `rho`-torsion
> certificate), then `g * f^r ∈ I`.
>
> *Proof.*  `f ≡ c*rho (mod I)`, so `f^r ≡ c^r rho^r`, so
> `g f^r ≡ c^r (g rho^r) ≡ 0`.  ∎

Apply it with `f = cs^N k^M` and `g = cs^n k^m`:

```text
cs^N k^M ∈ I + (rho)   and   cs^n k^m rho^r ∈ I
        ==>   cs^{rN+n} k^{rM+m}  ∈ I ,   i.e.  the typed form with W = 0.
```

Now instantiate.  The **promoted** `T-cs` grade-14 fibre theorem, read as a
Nullstellensatz certificate and cleared of its Rabinowitsch variables
(fable5's Lemma A step: elementary, and the only unreviewed link in this
chain), gives `cs^N k^M ∈ I + (rho)` for some `N, M`.  Branch (a), which I
**verified exactly** in §2.3, gives `cs^6 k^2 rho^6 ∈ I`.  Therefore

```text
cs^{6N+6} * k^{6M+2} * (1 + rho*0)  ∈  I .
```

**This is the direct total-family certificate, with `W = 0`, obtained from
the already-promoted fibre theorem plus one hand-checkable four-cofactor
identity, with branch (b) removed from the argument entirely.**

This is the memo's most decision-relevant finding.  It also generalises what
the producer did: the producer's §6.1 composition is this lemma at `r = 3`
against its own branch (b).  Nothing is lost by substituting the promoted
theorem for branch (b) except exponent quality, which was never claimed.

Note what it does to the two blind proposals it touches.  Root's M3
(`rho`-torsion) was filed as an *alternative* to emptiness for residual
components; fable5's M4 was filed as the *only* bridge from fibre to total.
The truth is that M3 is precisely the multiplier that upgrades M4's additive
certificate to a typed one, with `W = 0` for free.  Neither report states it.

### 3.2 Conditional re-ranking

**Branch A — the direct `T-cs` certificate is CONFIRMED by Fable5/Grok.**

*Proof queue.*
1. `J1=0` diagnostics, then the two second-stage `a0/a1` charts on the shape
   §4 supplies. **Now the top item**, because it is the first obligation with
   a computed rather than estimated shape.
2. Terminal receiver `V(J1+J2)`.
3. Literal source universe/coverage and the generic deck/square bridge — the
   step that converts chart emptiness into the registered Gate-T theorem.
4. TD6 H19R2 harvest, then omitted-moduli cover and source/landing
   composition.
5. Global walls (arbitrary-standard-pair landing, `G2-PSC`, any invoked
   `G2-BD`, cofinal degree/type).  Unmoved, still terminal, still without a
   cheap experiment.

`k=0` **leaves the Gate-T proof queue** and becomes one global sibling-fan
item, per the filing review — with the §4.3 witness attached so no successor
retries it on the frozen prefix.

*Counterexample queue.*  Unchanged by this branch.  Local landing wins do not
touch AS109.

**Branch B — the direct certificate FAILS on branch (b).**

This is the branch the campaign is currently over-weighting.  By §3.1 the
**conclusion survives** — `cs^{6N+6} k^{6M+2}` with `W = 0`, from the promoted
fibre theorem and branch (a), which I verified independently of the producer.
What is lost:

- the `(447,164)` exponents and the "no Groebner anywhere" provenance;
- the producer's §5 as an independent derivation of the `rho=0` half;
- nothing in the proof queue above, which is unchanged in content and order.

The re-rank difference between Branch A and Branch B is therefore **one
promotion-custody line, not a queue reordering**.  Reviewers should be told
this so they do not treat branch (b) as load-bearing: they should focus their
budget on Lemma 0 (the substituted-to-honest-ordered translation, which is
where the presentation risk actually is and which is *also* unrecorded in the
V18/V19 preregistrations) rather than on re-deriving 1880 rewrites.

**Branch C — branch (a) itself fails.**  I expanded it to zero residual
against hash-matched frozen bytes, so this requires an error in my own
expansion or in the frozen bytes.  If it happens, it is a custody finding
about `Tg10_1..Tg10_4`, not a landing finding — and note `Tg10_2` is
independently over-determined by the promoted `(C1)` cubic plus `Tg10_4`
(opus5 §3.1, a genuinely good review instrument that I endorse and recommend
adding to the checklist).

---

## 4. Synthesis-generated mechanism: `sigma`-descent of the frozen prefix

This section is not in any of the four blind reports or either post-freeze
review.  It is the answer to prompt item 6.  Everything is VERIFIED-HERE
against the frozen bytes and is producer-tier from this lane.

### 4.1 The jet-shift identity

Let `D` be the `sigma`-jet derivation
`cs↦cs1, rs↦rs1, k↦k1, c0↦e0, c1↦e1, a0↦aa0, a1↦aa1, ell1↦ell2, rho↦0`
(and one further step on each tower), and let `p := rho^2` (all `rho` powers
in all 22 rows are even).  Then, **exactly, for all `j = 1..7`**:

```text
Tg11_j  =  D(Tg10_j)  -  ell1 * d(Tg10_j)/dp  +  k * R_j ,        R_j ∈ (c0, c1).
```

The residuals are tiny and explicit, e.g.

```text
k*R_1 = (5/16) c0 cs k + (5/64) c1 k rs
k*R_4 = 0
```

This is forced by §2.1: `D` raises `deg_s` by exactly one, `ell1` has
`deg_s = 1`, and `d/dp` preserves `deg_s` because `deg_s(rho) = 0`.  Grade 11
is grade 10 plus one.  **The row tower is the sigma-jet tower and `deg_s` is
the sigma-order.**

### 4.2 What the shift does to the certificate

Write the grade-10 core in the ordered `T-cs` chart, with `u := c0`,
`w := c1`, `kap := (5/6) cs^3 k p` (this is the direct certificate's §3, which
I verified):

```text
gam = a0 w + a1 u + kap        del = a0 u + (1/4) w^2 + p a1 w
alp = u w                      bet = u^2 + p w^2
```

Branch (a)'s Proposition 3.1 is: `alp = 0` and `bet = 0` force `u = w = 0`,
whence `gam = kap != 0` on `D(cs*k*rho)` — a contradiction.  **The whole
emptiness comes from the load term `kap` being a unit.**

Now apply the shift.  On each degenerate stratum the same four shapes
reappear one jet level up, with the load term degenerated:

| stratum | shifted core (VERIFIED-HERE) | load term |
|---|---|---|
| `V(k)`, in the `T-cs` chart, after the collapse `c0=c1=0` | `a0e1+a1e0+kap1`, `a0e0+p a1e1`, `e0e1-2cs(a0^2+p a1^2)`, `e0^2+p e1^2-8p cs a0a1` | `kap1 = (5/6) cs^3 k1 p` — alive on `D(cs*k1)` |
| `V(J1)` (the `J2`/receiver prefix) | `a0e1+a1e0`, `a0e0+p a1e1`, `e0e1`, `e0^2+p e1^2` | **absent** at grades 11–12 |

The `V(J1)` column is exact, from
`(8/3)Tg11_1`, `(8/3)Tg11_2`, `(32/3)Tg12_4`, and
`(16/3)(Tg12_3 - (p/2)Tg12_1) + (1/2) ell1 (8/3) Tg11_1 = e0 e1`.

So on `V(J1)` the shifted `alp` and `bet` still force `e0 = e1 = 0` on
`D(rho)` — the descent **collapses the jet pair and continues** rather than
terminating, exactly because the load term is gone.  On `V(J1)` the load
reappears only at grade 14, as `-(5/128) a0 a1 k rho^4` plus `cs1`-weighted
corrections; it is `a0a1`-weighted, hence **dies on the ordered stratum
`qa1 = 0`**.

That last sentence *derives* the post-freeze `A00` and `A10` horizontal
sections, which the Grok review recorded as brute facts.  All three confirmed
zero-sections — `CS0`, `A00`, `A10` — are precisely the points where the
shifted load term degenerates.  One mechanism, three confirmed instances.

**The mechanism, stated:**

> Each degenerate stratum of the frozen prefix inherits, one grade up, a
> jet-shifted copy of the *same* four-shape grade-10 core in the next jet
> pair.  The core terminates in emptiness **iff** its shifted load term is a
> unit on the relevant open; otherwise it collapses that jet pair and
> descends to the next.  `k=0` and `J2` are not new charts needing new source
> emission — they are the next two steps of one descent, and the decisive
> question at each step is a *single load-unit question*, not a fresh
> Groebner problem.

This is **NAVIGATION plus two exact identities**, not a proof engine.  It
predicts where certificates can exist; §4.3 shows it also predicts, correctly,
where they cannot.

### 4.3 The witness: the `k=0` sibling is unreachable in *both* readings

**VERIFIED-HERE.**  Root's `CS0` section (`cs=1`, `k=0`, all other source
names `0`, `rho` free) I reproduced independently — all 22 rows vanish in
`Q[rho]` — along with `A00` and `A10`.  But `CS0` sets `k1 = k2c = k10_3 =
k10_4 = 0` as well, so it lives in the **zero-leading-load** sub-fan.  The
`k10` filing review explicitly refuses to collapse that with the
**delayed-load** sub-fan `V(k) ∩ D(k1)`, and nobody tested the latter.  I
tested it.  The frozen prefix *does* see `k1` (93 occurrences), and at
`cs=1, k=0, k1` free the prefix does **not** vanish:

```text
Tg11_1| = (5/16) rho^2 k1     Tg11_3| = (5/32) rho^4 k1
Tg11_5| = -(5/128) rho^6 k1   Tg11_7| = (5/256) rho^8 k1
```

so the delayed-load direction is genuinely visible, and root's `CS0` control
does **not** cover it.  Nevertheless the stratum is still not empty.  Solving
the shifted core of §4.2 gives, over the algebraic closure, for every
`cs*k1*rho != 0`:

```text
S := a0 + a1/t ,  D := a0 - a1/t ,  E := e0 + e1/t ,  F := e1/t - e0 ,  t := rho
E  = ± 2 sqrt(t*cs) S ,   F = ± 2 i sqrt(t*cs) D ,
S^2 = ∓ (5/12) cs^{5/2} k1 t^{5/2} ,   D^2 = ± i (5/12) cs^{5/2} k1 t^{5/2} ,
```

with `k2c`, `rs1`, `k10_4` then determined by `Tg12_1`, `Tg12_2`, `Tg14_5`
(pivots `(5/16)cs^3 rho^2`, `(15/64)cs^2 k1 rho^2`, `-(5/128)cs^3 rho^6`, all
nonzero on `D(cs*k1*rho)`), and `Tg12_3`, `Tg12_5`, `Tg12_7` then vanishing
automatically at `ell1 = cs1 = ell2 = 0`.  I realised this as an exact point
and checked **all 22 frozen rows vanish**, independently over three primes:

```text
p = 65521    k1=1  a0=48966  a1=4891    e0=3387   e1=38806    all 22 rows = 0
p = 1000033  k1=5  a0=740566 a1=154990  e0=852940 e1=938172   all 22 rows = 0
p = 1000081  k1=1  a0=18714  a1=528026  e0=910186 e1=183294   all 22 rows = 0
```

with `cs = 1`, `rho = 1`, `k = rs = c0 = c1 = 0`, hence
`qrs = qc0 = qc1 = 0` and `u = 1` — a genuine point of the ordered `T-cs`
chart presentation, **with `rho != 0`**, off the special fibre.

**Consequences.**

1. No certificate `cs^a k1^b rho^c ∈ I` exists on `V(k) ∩ D(cs*k1)` from the
   frozen prefix.  Root's M3 (`rho`-torsion) returns **negative** on the
   delayed-load sub-fan, as `CS0` already returns it on the zero-load sub-fan.
   Root's own instinct — that `CS0` is a *required negative control* — is
   vindicated and now extends to the harder reading.
2. fable5 §3.4's mechanism is counter-witnessed: this point has `k = 0` and
   `e1 = 38806 != 0`.
3. opus5's Card B payoff branch ("restricted fibre empty ⟹ the `k=0`
   complements of all four `J1` charts are discharged") is **refuted**.  Card
   B lands on its second branch; §4.2–§4.3 supply the explicit residual it
   asked for.
4. grok's Card B first branch ("some grade `<= 16` row is a unit on this
   open") is **refuted for the frozen prefix**, at the harder sub-fan, before
   any AWS spend.  grok's second branch obtains: *park it; do not spend V19*.
5. The two sub-fan readings the filing review refused to collapse now have
   **different evidence and the same verdict**.  That is a clean scope
   statement for the ledger.
6. Any future `k=0` attempt requires genuinely new exported source (grade 13,
   the other grade-14 rows, or higher) **or** a routing/receiver theorem.  The
   campaign already owns machinery for the delayed-load concept in the
   affine-Faber presentation (`k10 = Lambda^12 K10`, promoted
   `xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composite-promotion-20260826.md`).
   The bridge between that presentation and the total-Rees one is the standing
   source/landing composition debt, not a new lane.

Modular caveat, stated plainly: three primes exclude any exact-`Q` certificate
whose cofactor denominators are integral at those primes.  The algebraic
description above is the characteristic-zero statement and is why I believe
the modular evidence rather than merely reporting it; it has not been
re-derived by a second model and must be reviewed before promotion.

---

## 5. Bounded discriminators, and routing

### 5.1 Already discharged in this memo (do not re-fund)

| Item | Owner(s) who queued it | Result |
|---|---|---|
| Grading-lattice parse (opus5 Card A stage 1) | opus5 | Rank 2 confirmed; `deg_s` extended to 40 names; `deg_2` **refuted** (§2.1, §2.4) |
| `J1=0` prefix census | fable5 §3.5, grok Card C | First nonzero grade **11**; `a0,a1` present; opus5 §3.6 refuted (§2.5) |
| `k=0` evaluation at the zero-load point | grok Card B | `CS0` reproduced; all 22 vanish (§4.3) |
| `k=0` at the delayed-load point | **nobody** | New; all 22 vanish at `rho != 0` (§4.3) |
| Branch (a) of the direct certificate | live review | Exact identity confirmed (§2.3) |
| opus5 §3.5 collapse theorem | opus5 Card B stage 1 | Confirmed on the genuine full bytes (§2.2) |

Roughly two days of queued desk work across three lanes is closed here.  Every
one of these was correctly identified as cheap by its proposer; the value of
cross-pollination was running them once instead of three times.

### 5.2 Next bounded desk checks (hours, no AWS)

**DD1. Grade-12 extension of the jet-shift identity.**  Is
`Tg12_j = (1/2)D^2(Tg10_j) + (second-order ell/connection terms) + (k)`?
`deg_s` forces the shape; only the Faà-di-Bruno coefficients are unknown.
*Payoff:* if it holds, the descent is a tower rather than one step, and the
stage-two certificate shape is determined without any search.  *Stop:* one
sitting; if the second-order connection terms do not close, report the exact
obstruction and stop — do not go to grade 13.

**DD2. `deg_s`-type the other campaign row sets.**  Run the same 30-line
nullspace parser on the D1, affine-Faber and TD6 row sets.  This is opus5 §7's
speculation, restated correctly: ask whether the localizers `D(p k0)`, `D(J)`,
`D(E M)`, `D(U H B3)` are *forced by the grading lattice* rather than
incidental.  *Payoff:* an a-priori bound on every future certificate search in
three lanes.  *Stop:* if any of the three row sets has grading lattice rank 0,
record it and stop — that lane's certificates cannot be typed this way.

**DD3. Lemma 0 spot-audit.**  The substituted-to-honest-ordered translation is
unrecorded in the V18/V19 preregistrations and is the real presentation risk
in both the direct certificate and any V19 harvest.  Re-expand it for the
three rows with the largest cofactors (`Tg14_5`, `Tg12_7`, `Tg12_5`).  *Stop:*
one sitting; a single failure is a high-priority custody finding.

### 5.3 Heavy items, routed to named idle AWS capacity

Live at this instant: **r6a** and **box01** carry TD6 H19R2; **r6c** and
**r6b** carry V19 Q / F65521.  The V18R1 groups on **Box02** (Q) and **r6d**
(F65521) were terminated at 01:10Z and those slots are free; **Box03** has
carried no campaign job since the 17:58Z-era entries and is the historical
spare-CPU host.  Recommended routing — **this memo launches nothing; all three
require root static audit and coordinator sign-off first**:

**H1 → Box02 (largest RAM, exact `Q`).  Minimal-exponent typed `T-cs`.**
Given §3.1, the open question is no longer existence but exponent quality.
Enumerate `deg_s`-homogeneous cofactor slots at a requested `(N,M)` with
`2N + 4M >= 14`, and solve one exact linear system.  The `deg_s` table of
§2.1 bounds every slot a priori, which is what turns this from a 26-generator
membership lift into a sized linear solve.  *Negative controls:* the three
promoted certificates must type; one deliberately mistyped `T-c0` variant must
fail closed.  *Stop:* two consecutive infeasible `deg_s` levels with no new
structure (standing two-attempt rule), or 12 hours, whichever first.

**H2 → r6d (F65521 mirror + exact `Q` control).  The `rho`-order question.**
Is `cs^a k^b rho^2 ∈ I_10`?  The direct-certificate producer names this as the
single lever that would collapse `N = 447` to `N = A' + 6` and states the
surviving obstruction is `a0^n w^n`.  It is bounded, it is the only item that
improves the certificate rather than re-proving it, and by §3.1 its answer
multiplies straight through.  *Stop:* two degree increments; hard 12-hour cap.

**H3 → Box03.  Stage-two ordered `T-a0` core on `D(qa1)`.**
§4.2 gives the exact shifted core on `V(J1)` and predicts the stage-two load
term dies on `qa1 = 0`.  Scope the job to `D(qa1)` and make the `A00`/`A10`
horizontal sections a **mandatory negative control**: the job must *fail* on
`qa1 = 0`.  A run that reports success there has a presentation bug.  *Stop:*
one dual run; if `D(qa1)` also fails at grade `<= 14`, stop and report the
first surviving grade rather than escalating.

**Not routed, deliberately.**  No `k=0` emptiness or `rho`-torsion job on the
frozen prefix: §4.3 proves such a job would be deciding a false statement, in
both sub-fan readings.  No new arbitrary AS109 rectangle.  No third serial
affine-Faber `H` increment without written justification.

---

## 6. Explicit decisions

| Item | Decision | Reason and stop rule |
|---|---|---|
| **`J1` completion** | **start now** — but the remaining work is *review*, not computation | Three of four ordered `J1` charts are promoted; the fourth has a certificate that survives both outcomes of its own review (§3.1). Point Fable5/Grok review budget at Lemma 0 and at the fibre-theorem-to-Nullstellensatz step, not at branch (b)'s 1880 rewrites |
| **`k10=0` sibling fan** | **stop** as a Gate-T computation; **await dependency** as one global item | Off-family per the confirmed filing; and §4.3 proves the frozen prefix cannot reach either sub-fan reading, at `rho = 0` or `rho != 0`. Dependency is new source emission or the source/landing composition to the existing affine-Faber delayed-load lane. Record the §4.3 witness so no successor retries it |
| **Cheap `J1=0` diagnostics before `J2`** | **done — see §2.5/§4.2**; the follow-on (`DD1`) **starts now** | Answer: first nonzero grade 11, `a0/a1` present, and the shifted core is explicit. This was the single highest-leverage item in the round and it cost one parser |
| **Vertical `rho`-torsion / Fitting** | **start now, retargeted; stop the Fitting half** | The mechanism is real and already realised: branch (a) is exactly `rho^6 = 0` on `D(cs*k)` from grade-10 rows alone, and §3.1 shows torsion is the *upgrade multiplier*, which is more valuable than root's original standalone framing. The sparse-Fitting-minor half of root's Card B is **not** funded: §4.3 shows the intended client (`k=0`) is non-torsion, so there is no target |
| **Certificate typing / software IR** | **start now, one tool, one owner** | Root's telescoping IR, fable5's `CERT-TYPER`, grok's bounded ansatz and opus5's validator are one instrument. Build it once. **Mandatory correction before build:** drop the `M >= 1` acceptance gate (§2.4 — it is unsound); keep the nonzero-`Tg14_5` gate (§2.4 — it is sound); add `deg_s`-homogeneity and the Lemma-0 translation as fail-closed fields. Controls: the three promoted certificates plus one mistyped variant. Stop: abandon on control failure after one diagnosis pass |
| **AS109 arithmetic Newton descent** | **start now, bounded to `n = 2`** | Three-way independent convergence (C-C); hand-scale; symmetric payoff. Include identity and triangular Keller automorphisms as positive controls and a residue-changing valuation-zero shear as a negative control. **Stop:** hard stop after `n=2` and `n=3` if neither yields a determinate integrality verdict. Do not enumerate supports; the rigid-leaf hold stands |
| **AS109 gauge section** | **start now, as a free preprocessor** | Exact at `deg_x A <= 108`, zero cost, removes one continuous parameter from any enumeration, and discharges one of the two ingredients the `SUPPORT GRAMMAR STOP` names. Apply it *before* any polygon enumeration. Claim nothing about the triangular family |
| **TD6 H19R2** | **continue** (running on `r6a`, `box01`; static audit passed) | Design is fail-closed and dual-run. Auditor note carried forward from fable5: Stage-5's `e >= 1` assumption and the `{U,V,V^2-4U^3}`-only denominator assertion are the two load-bearing stop rules and must print the offending factor on failure. **Redesign trigger:** if it falls back to normalized coordinate arithmetic instead of emitting all 38 original-FIRST multipliers, stop and redesign |
| **V19** (`r6c` Q, `r6b` F65521) | **stop the mathematics; let the protocol run to its existing cap** | §3.1 makes V19 mathematically redundant: the typed certificate follows from the promoted fibre theorem plus verified branch (a). V19's residual value is exponent quality and an independent machine check — neither justifies a successor. Do **not** launch any V19 successor. If it returns, apply the §7 divisibility test on `psi(L_24)` and the Lemma-0 translation before any harvest, and use the corrected gate list |

---

## 7. Top-five action queue

1. **Re-point the direct-`T-cs` hostile reviews.**  Tell Fable5 and Grok that
   branch (a) is independently confirmed (§2.3) and that §3.1 derives the same
   typed conclusion from the promoted fibre theorem without branch (b).  Their
   budget belongs on **Lemma 0** (the substituted-to-honest-ordered
   translation, unrecorded in V18/V19 preregistration) and on the
   fibre-theorem-to-Nullstellensatz clearing step.  Highest value per reviewer
   hour in the queue.
2. **File the three scope corrections before they propagate.**  (a) opus5's
   `deg_2` does not exist; withdraw `M >= 1` and do not make it a V19 gate.
   (b) opus5 §3.6's stage-two row-disjointness is false; the correct first
   nonzero grade on `V(J1)` is 11.  (c) fable5 §3.4's `k=0` mechanism is a
   scope error with an explicit counter-witness, though its conclusion holds.
   Each of these was about to be consumed by a live lane.
3. **Run `DD1` (grade-12 jet shift) and `DD2` (`deg_s`-type the D1 /
   affine-Faber / TD6 row sets).**  Hours of desk work; `DD1` determines the
   stage-two certificate shape without a search, `DD2` bounds three other
   lanes' searches a priori.
4. **Route `H1` (Box02), `H2` (r6d), `H3` (Box03) after root static audit**,
   with the stop rules of §5.3 and with `A00`/`A10` as `H3`'s mandatory
   negative control.  These are the only heavy items in the portfolio whose
   payoff is a shape rather than a hope.
5. **Start the AS109 `n = 2` corner by hand, with the gauge section applied
   first.**  Cheapest item with a genuinely symmetric outcome: forced
   integrality raises the one-sided floor for free; forbidden integrality
   yields the first small explicit AS109 search target.

---

## 8. Scope firewall

Everything in §2.1–§2.5, §3.1, and §4 is **producer-tier from this lane and
unreviewed**.  It requires different-model hostile review before promotion or
downstream consumption, exactly like any other producer output.  In
particular the refutations of opus5's `deg_2` and of opus5 §3.6, the scope
repairs to fable5 §3.4 and §3.3, the jet-shift identity, the torsion-
multiplier lemma, and the `k=0` delayed-load witness are all claims of this
memo, not promotions.

This memo does **not** establish, and must not be read as establishing:
JC2 or its negation; Gate T; closure of the direct `T-cs` chart (its review is
live, and §3.1's alternative route contains one elementary unreviewed step);
emptiness or nonemptiness of the `k10=0` sibling fan (§4.3 is a *negative*
result about the frozen prefix's reach, not a closure); either `J2` chart; the
terminal receiver; chart overlaps; the deck/square bridge; the generic
comparison; literal source universe or coverage; whole TD6, SP-2, or the
q15/omitted-moduli cover; order two; maximum twelve; arbitrary-standard-pair
landing; `G2-PSC`; any invoked `G2-BD`; any cofinal degree or type bound;
existence or nonexistence of an AS109 polynomial lift; exclusion of the
unbounded-total partial-`y` cells `(8,12)` and `(9,12)`; or any Lean
statement.

Every result here is conditional on the frozen V9/V17 exact-`Q` bytes and
inherits their upstream literal-source (Faber emitter) provenance debt in
full.  The `deg_s` grading and the jet-shift identity are statements about
*those bytes*, not about the source ideal, and say nothing about unexported
grade-13, the other grade-14 rows, or higher grades.  The `k=0` witness is
verified exactly over three primes with a characteristic-zero algebraic
description; the modular verification excludes exact-`Q` certificates whose
cofactor denominators are integral at those primes, and the
characteristic-zero statement has not been independently re-derived.

No AWS state was read or mutated, no campaign computation was launched, no
web access was made, `jc2-lean` was not accessed, and no heavy local CAS was
run.  The only repository file written is this one; no source or ledger file
was edited.
