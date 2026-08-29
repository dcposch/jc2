# Hostile review: two-fibre decision for the total ordered-`a1` chart

Date: 2026-08-27
Reviewer: Grok 4.6 (xAI), adversarial commutative algebra, different-model lane
Charged artifact: `xmodel/ideation-20260827T0935Z-fable5.md` §3.1 and Card F1
SHA-256 (rehashed locally, match):
`098b81d19cba6f278e93a809e60a3a4892eea7979758ffe6b0bb2997163b98c0`

**Overall: REPAIRABLE.**  The four claimed equivalences are true.  The
navigation sentence that the frozen chart is decided by one full-system
Gröbner run of `J|_{a1=1}` over the field `Q(rho)` is true after the
special-fibre half is taken from the already-reviewed V42 theorem, not
from an unpinned 17-row Gröbner basis.  The proof sketch of
dehomogenization as written is not a proof over `Q` or `Q(rho)`.  Card F1
stage 2 is false.  The generic Bézout converter does not automatically
produce `U(0)=1`.

Do not read this as a refutation of the two-fibre lemma, and do not
promote Card F1 as written.

---

## 0. Custody, constraints, and what was actually used

Session constraints honored: no heavy local CAS, no Singular/Macaulay2
run on any live system, no AWS launch, no web sweep, no canonical-ledger
edit, no contact of any kind with `jc2-lean`.  The only file written in
the repository is this report.

Git HEAD: `418e413593120d19e15e6546eb50c985f4b1f038`.

Charged ideation rehashed to the mandated digest.  The following
supporting artifacts were read as inputs to the attack, not as authority
for the two-fibre step.  Their hashes were rehashed locally.

| Artifact | SHA-256 | Role |
|---|---|---|
| Charged ideation (Fable5 `20260827T0935Z`) | `098b81d19cba6f278e93a809e60a3a4892eea7979758ffe6b0bb2997163b98c0` | theorem + Card F1 |
| Total-rho design (Sol) | `e3d263d5c0006bc4f05c5b7ff17bfcbd68bab52f7c1d3ccb5d323facd94448f7` | reviewed four-way criterion |
| Fable5 correction review | `98003865784355ec24169ff4dfd95dde005a2f24e11f42d039d68dc55beebf95` | 66-variable ring, `ez9` spectator, even-rho parity |
| Sealed packet (read only as the ideation's cited evidence list) | `e871e3d71a8777ca50f7c796bf7547023a8c2ca8e2930c6a0981ddcebd6ae3db` | 17-row assertion, V42/V43 status |

The two-fibre lemma is a new implication.  The reviewed criterion

```text
K+(rho)=(1)  iff  some a1^N U(rho^2) lies in J with U(0)=1
```

is used as a black box for the left-hand side only, after an independent
re-derivation of the weight-zero projection `(1)⇒(3)` in the design (needed
to compare `S'` against `K+(rho)`).  Nothing below treats “the criterion is
reviewed” as a license for the generic-fibre, dehomogenization, 17-row, or
compute-plan claims.

No producer PASS string, no AWS `RESULT.json`, and no 17-row Gröbner
transcript was executed or trusted as a computation.

---

## Verdict summary

| Attack | Charge | Verdict |
|---|---|---|
| 1 | Four equivalences; primes of `T^{-1}Q[rho]`; embedded primes; vertical fibres `rho=c≠0`; nilpotents; radical ascent/descent | **CONFIRMED** as statements.  Sketch `(ii)` is sloppy on powers vs elements; the contraction classification is exact |
| 2 | `a1 ∈ √(J S')` vs `K+(rho)=(1)`; denominators; saturation exponents; even `U(rho^2)` | **CONFIRMED**.  Evenness is a reviewed extra, not a hidden hypothesis of the two-fibre lemma |
| 3 | Dehomogenization over non-closed `Q(rho)`; `wt(a1)=5`; faithful-flat descent; `a1=1` as a radical slice | **REPAIRABLE**.  Conclusion true; the written `G_m`-scaling + Nullstellensatz-over-`Q(rho)` sketch is false as a proof |
| 4 | 17-row subideal unit after `rho=0,a1=1` ⇒ full special-fibre condition; literal `J0` membership | **REPAIRABLE**.  Subideal implication is sound.  “Already computed” is not a pinned reviewed input.  The special-fibre half is already supplied by promoted V42 |
| 5 | Selected-row one-sidedness; full-system nonunit decisive; full-system unit needs a certificate | **REPAIRABLE**.  One-sidedness and frozen two-sidedness of a *complete* full-system run are true.  Stage 2 of Card F1 is false.  Generic rehomogenization need not yield `U(0)≠0` |
| 6 | Toy; overstrong versions; frozen grade-through-19 vs all-depth vs Gate T | **CONFIRMED** toy.  Overstrong versions **REFUTED**.  Frozen-chart scope is mostly respected; “first honest surviving landing geometry” oversells a prefix-relative negative |

**Smallest failing implication.**  Card F1 cheapest-discriminator stage 2:
“exact-`Q` unit at one random rational `c` places `c` in the at-most-finite
exceptional set of a generically nonempty family, so it is decisive-grade
evidence pending stage 3.”  A unit fibre at one `c≠0` is consistent with a
*nonunit* generic fibre (an exceptional empty closed fibre).  It is not
evidence of generic emptiness.

**Smallest failing hypothesis in the desk proof.**  “Over an algebraically
closed field any point with `a1≠0` scales onto the `a1=1` slice, plus the
Nullstellensatz over `Q(rho)` and `Q`.”  Neither `Q` nor `Q(rho)` is
algebraically closed, `z↦z^5` is not surjective on either, and the
Nullstellensatz is not valid over those fields.  The *conclusion*
`a1∈√(I) ⇔ I|_{a1=1}=(1)` for a positively weighted homogeneous ideal is
nevertheless true, by a graded-unit argument that never scales points
(§3).

---

## 1. Attack 1 — primes, fibres, nilpotents, the four equivalences

### 1.1 Rings

Let `k=Q`.  Let `S=k[rho,X]` with a positive grading, `wt(rho)=0`,
`wt(x)>0` for every variable `x` in `X`, and `a1∈X` of weight 5.  Let `J`
be a weighted-homogeneous ideal (the frozen ordered-`a1` total rows
through grade 19; the lemma does not use the count 66 until the compute
plan).  Let `K=J:a1^∞` and `J0=J|_{rho=0}⊂k[X]`.  Let

```text
T = { u ∈ k[rho] : u(0) ≠ 0 } = k[rho] \ (rho),
S' = T^{-1} S = k[rho]_{(rho)}[X].
```

`T^{-1}k[rho]` is the DVR `k[rho]_{(rho)}`, maximal ideal `(rho)`, residue
field `k`, fraction field `k(rho)`.

### 1.2 Primes of the localized coefficient ring

The prime ideals of `k[rho]` are `(0)` and `(rho-c)` for `c∈k`.  A prime
survives in `T^{-1}k[rho]` if and only if it does not meet `T`.

- `(rho-c)` for `c≠0` meets `T`: `(rho-c)(0)=-c≠0`.  These are inverted.
- `(rho)` does not meet `T`.
- `(0)` does not meet `T`.

So the primes of `T^{-1}k[rho]` are exactly `(0)` and `(rho)`.  There is
no vertical closed fibre at `rho=c≠0` in `Spec S'`.  There is no third
height-one prime.  There is no embedded prime of the coefficient DVR
(it is regular of dimension one).

Primes of `S'` are in inclusion-preserving bijection with primes `P` of
`S` such that `P∩T=∅`, i.e.

```text
P ∩ k[rho] ∈ { (0), (rho) }.
```

The candidate’s contraction classification is exact.

### 1.3 Radical membership on a DVR base, with embedded primes and nilpotents

Let `I = J S'`.  Then `a1 ∈ √I` if and only if `a1` lies in every prime
of `S'` containing `I`.  As a set of points,

```text
Spec S'  =  (generic fibre over (0))  ∪  (special fibre over (rho)).
```

Every prime of `S'`, associated or not, embedded or not, contracts to
one of those two.  The nilradical of `S'/I` is the intersection of *all*
such primes.  Therefore

```text
a1 ∈ √(J S')
  ⇔  a1 lies in every prime of S containing J with P∩k[rho]=(0)
     and in every prime of S containing J with P∩k[rho]=(rho)
  ⇔  a1 ∈ √( J k(rho)[X] )   and   a1 ∈ √(J0).
```

No geometric Nullstellensatz is used.  Embedded primes of `J` are
included.  Nilpotent thickenings are included, because the statement is
radical membership rather than reduced support.  Vertical components
supported over `rho=c≠0` are discarded by the localization, which is
correct: they do not meet `V(rho)` and cannot witness `K+(rho)≠(1)`.

Ascent is elementary and does not need primes:

- `a1 ∈ √(J S')` means some `u∈T` and `N` with `u a1^N ∈ J`.  Inverting
  `rho` as well gives `a1 ∈ √(J k(rho)[X])`.  Setting `rho=0` gives
  `u(0) a1^N ∈ J0` with `u(0)≠0`, hence `a1^N ∈ J0`.

Descent is the prime classification above.  It is existential.  An
explicit cofactor `u∈T` is not produced by writing the two fibre
identities next to each other; extracting it is a computation in
`S'` (Gröbner, syzygy-colon, or the reviewed fixed-weight DVR module).
That is a converter problem, not a gap in the equivalence.

### 1.4 First two equivalences, independently of evenness

The reviewed design’s `(1)⇔(3)` is: `K+(rho)=(1)` if and only if there
exist `N` and `U(rho)∈k[rho]` with `U(0)=1` and `a1^N U ∈ J`.  The
load-bearing direction is the weight-zero projection, which uses only
that `J` is homogeneous and that `rho` is the unique weight-zero
variable (reconfirmed on the 66-positive-variable ring by the Fable5
correction review).  From `1=k+rho h` with `k∈K`, the weight-zero piece
is `U(rho)∈K∩k[rho]` with `U(0)=1`; saturation supplies `N`.

Now `a1 ∈ √(J S')` means some `N` and some `u∈T` with `u a1^N ∈ J`.
Scale by the nonzero rational `1/u(0)` (the ideal is a `Q`-vector space)
to get `U(0)=1`.  Conversely, `U(0)=1` puts `U` in `T`.  Therefore

```text
K+(rho)=(1)   ⇔   a1 ∈ √(J S')
              ⇔   a1 ∈ √(J k(rho)[X])  and  a1 ∈ √(J0).
```

The candidate’s parenthetical in sketch `(ii)`, “if `u a1 ∈ P` then
`a1 ∈ P`,” is the element-membership case.  The lemma is radical.  The
repair is to write `u a1^N`.  The classification does not change.

### 1.5 Third equivalence: dehomogenization, postponed to §3

The remaining claimed step is

```text
a1 ∈ √(J k(rho)[X])  ⇔  J|_{a1=1} = (1)  in  k(rho)[X \ {a1}],
a1 ∈ √(J0)           ⇔  J0|_{a1=1} = (1)  in  k[X \ {a1}].
```

This is true and proved in §3 by a different argument from the sketch.

All four equivalences therefore hold.

---

## 2. Attack 2 — `√(J S')` versus `K+(rho)=(1)`, denominators, evenness

### 2.1 Direct comparison

The reviewed criterion’s typed form is `a1^N U(rho^2)∈J` with `U(0)=1`.
The `S'` form is `a1^N u(rho)∈J` with `u(0)≠0`.  These differ in two
places: evenness, and the normalization `U(0)=1` versus `u(0)≠0`.
Normalization is rational scaling, as above.  Evenness is not used.

So `a1 ∈ √(J S')` is exactly the reviewed `(3)`, hence exactly
`K+(rho)=(1)`, with no extra hypothesis.

The positive-weight projection is already the proof of `(1)⇒(3)`: the
unit decomposition `1=k+rho h` in `K+(rho)` is homogeneous, the
weight-zero summand lives in `k[rho]`, and that summand is the
denominator-cleared cofactor.  Localization at `T` is the same move in
the opposite language: invert every weight-zero unit at `rho=0`.

Saturation exponents need not match fibrewise.  If `a1^{N1}` dies on the
generic fibre after multiplying by `rho^k w(rho)` with `w(0)≠0`, and
`a1^{N0}∈J0`, the combined exponent `N` for a cofactor in `T` may
strictly exceed both `N0` and `N1`.  The lemma does not claim equality
of exponents.  V43’s floor `N≥7` (provisional as a result; the floor
`N≥6` from V38 is promoted) is a lower bound on any such `N`, not a
conflict.

### 2.2 Even `U(rho^2)` is not a hidden hypothesis

The involution `rho ↦ -rho` fixes every frozen row (even exponents,
maximum `rho^8`, independently verified in the Fable5 correction
review).  It therefore fixes `J`.  If `a1^N U(rho)∈J`, then
`a1^N U(-rho)∈J`, and the even part still has the same constant term.
The typed form `(4)` follows from `(3)` by averaging.

The two-fibre lemma never needs this.  It would remain valid for a
non-even homogeneous `J` (the candidate’s own toy is odd in `rho`; see
§6).  Treating evenness as a load-bearing input to Card F1 would be a
mistake; treating the DVR-typed certificate `U(rho^2)` as the
*promotion* object is correct, because that is the reviewed identity.

Denominator clearing from `S'` to `S` produces some `u∈k[rho]`, not
automatically an even polynomial.  Average after clearing, then
normalize.

---

## 3. Attack 3 — dehomogenization over `Q(rho)`

### 3.1 The written sketch is not a proof

The sketch says the dehomogenization equivalences use the weight `G_m`
action (`wt(a1)=5`; over an algebraically closed field any point with
`a1≠0` scales onto `a1=1`) plus the Nullstellensatz over `Q(rho)` and
over `Q`.

Two independent defects:

1. **The slice is not `G_m`-reachable over the base field.**  The action
   is `λ·(a1,x)=(λ^5 a1, λ^{wt(x)} x)`.  Scaling a point with `a1≠0` onto
   `a1=1` requires a 5th root of `1/a1`.  The map `z↦z^5` is not
   surjective on `Q` or on `Q(rho)`.  A `Q`-point with `a1=2` need not be
   `Q`-equivalent to a point with `a1=1`.  The geometric sentence is
   false over the fields in which the computation will be run.

2. **Nullstellensatz is not valid over `Q` or `Q(rho)`.**  A proper ideal
   need not have a point (e.g. `(x^2+y^2+1)` in `Q[x,y]`).  Citing the
   Nullstellensatz “over `Q(rho)` and `Q`” is a proof of nothing.

Faithful-flat descent from an algebraic closure *would* repair the
geometric argument, and that repair is recorded here so it cannot be
confused with the sketch:

- Let `F` be `Q` or `Q(rho)` and `Fbar` an algebraic closure.  Over
  `Fbar`, `z↦z^5` is surjective, so every point with `a1≠0` is in the
  `G_m`-orbit of a point with `a1=1`.  Homogeneous vanishing is
  orbit-invariant.  The affine Nullstellensatz over `Fbar` then gives
  `I|_{a1=1}=(1)` over `Fbar` if and only if `V(I)⊂V(a1)` over `Fbar` if
  and only if `a1∈√I` over `Fbar`.
- Membership of `1` in an ideal, and membership of `a1^N` in an ideal,
  are linear systems with coefficients in `F`.  A solution over `Fbar`
  is a solution over `F` (field extensions are faithfully flat).  So
  both sides descend.

That is a correct proof.  It is not the proof that was written.  It also
hides the grading in a geometric lemma that the live converter does not
use.  The algebraic argument below is the one that matches
rehomogenization.

### 3.2 Graded-unit lemma (works over any field, no 5th roots)

Let `R=F[a1,Y]` be positively weighted-homogeneous, `wt(a1)=d>0`, every
variable of `Y` of positive weight, `F` a field (here `F=Q` or
`F=Q(rho)`).  Let `I⊂R` be homogeneous.  Write `A=R/I`, internally
graded, so `A=⊕_{n≥0} A_n` with `A_0` a quotient of `F`.  If `I∩F≠0`
then `I=(1)` and both sides of the claimed equivalence are true.  So
assume `A_0=F`.

**`(⇒)`.**  If `a1^N∈I` then substituting `a1=1` yields `1∈I|_{a1=1}`.
No grading is required.  Valid over any ring.

**`(⇐)`.**  `I|_{a1=1}=(1)` means `I+(a1-1)=(1)` in `R`, hence `a1-1` is
a unit in `A`.  Let `u∈A` satisfy `(a1-1)u=1`.  Write `u=∑_{j≥0} u_j`
with `u_j∈A_j`.  Compare degrees in `a1 u - u = 1`:

- degree 0: `-u_0=1`, so `u_0=-1∈F`;
- degree `n>0`: `a1 u_{n-d} - u_n = 0` (with `u_m=0` for `m<0`).

Thus `u_n=0` unless `d` divides `n`, and `u_{kd}=a1^k u_0=-a1^k`.  The
sum is finite, say `u_{md}` is the last nonzero piece.  The next
recurrence forces `a1 u_{md}=0`, i.e. `-a1^{m+1}=0` in `A`.  Therefore
`a1^{m+1}∈I`.

No algebraic closure, no 5th root of a *value* of `a1`, no
Nullstellensatz.  The integer 5 enters only as the step of the
recurrence.  The same lemma with `d=wt(a1)` is valid for any positive
weight.

This is why `a1=1` is a valid slice for *radical* membership of a
positive-degree homogeneous element in a positively graded algebra over
a field.  It would fail without the grading (ordinary Rabinowitsch
inverts `1-t a1` in a different ring) and it would fail if a
weight-zero variable other than the coefficient field were present in
`Y` (then `A_0` would not be a field and `-u_0=1` need not make `u_0` a
unit of a field).  On the generic fibre the coefficient field is
`Q(rho)` and every remaining variable has positive weight.  On the
special fibre the coefficient field is `Q` and `ez9` is a free
spectator of weight 14, which does not disturb `A_0=Q`.

### 3.3 Rehomogenization as `Z/5Z` projection, matching the live converter

The graded-unit lemma is existence.  The campaign’s cascade homogenizer
(`homogenize_cascade_lift_v43.py`) does the constructive form: from a
Bézout identity `1=∑ m_i f_i|_{a1=1}`, keep only those multiplier
monomials whose total sigma weight is `0 mod 5`, attach `a1^{D-w/5}`,
and replay `a1^D` against the homogeneous rows.  Because the target `1`
has weight 0, other residue classes of the inhomogeneous identity sum
to zero and may be dropped.  This is a proof that `a1=1` is a valid
slice, and it is the converter Card F1 should cite.  It is not
`G_m`-scaling of points.

Over `Q(rho)` the same projection applies after the multipliers are
written with coefficients in `Q(rho)`.  Clearing a common denominator
`v(rho)∈Q[rho]` first produces

```text
v(rho) a1^D ∈ J
```

with `v` possibly vanishing at 0.  That is §5.3.

### 3.4 Verdict on Attack 3

The equivalence is **CONFIRMED**.  The written proof is **REFUTED**.
The attack item as a whole is **REPAIRABLE**: replace the sketch by the
graded-unit lemma (or by algebraic closure plus faithful-flat descent of
membership, plus the observation that `z↦z^5` becomes surjective only
after that extension).

---

## 4. Attack 4 — the 17-row special-fibre subideal

### 4.1 Subideal implication

If `I⊂J0` and `I|_{a1=1}=(1)` in `Q[X']`, then `J0|_{a1=1}=(1)`.  By §3,
`a1∈√(J0)`.  A selected-row *unit* after `rho=0,a1=1` is sound for the
full special-fibre half.  A selected-row *nonunit* would be worthless;
that is not what is claimed.

### 4.2 The seventeen rows as objects

The V43 cascade-dehom compiler names them, in order:

```text
Tg11_1,
Tg12_1, Tg12_2,
Tg13_1, Tg13_2, Tg13_4,
Tg14_1, Tg14_2, Tg14_3, Tg14_4,
Tg15_3, Tg15_4,
Tg16_5, Tg16_6,
Tg17_5, Tg18_6, Tg19_7.
```

These are the V42 cascade rows: ordinary ordered-`a1` source polynomials,
not the Laurent branch multipliers of the V42 A1 certificate, not chart
bilinears, not a localization.  The ordered-`a1` presentation kills
`rs,cs,c0,c1,a0` at emission; the ratio `q` does not occur (that is the
reviewed reason `S_0=Q[rho]`).  The compiler loads them through
`v37.load_rows()`, which returns the rho-zero images, then substitutes
only `a1=1`.  No extra localizer is inverted.

None of the eight rows that vanish at `rho=0`
(`Tg11_2,Tg11_3,Tg11_5,Tg11_7,Tg12_5,Tg12_7,Tg13_7,Tg14_6`) is in the
list, so the seventeen survive specialization.  `Tg19_2` is not in the
list, so `ez9` is absent; on the special fibre `ez9` is a polynomial
spectator and omitting it is correct for `J0`.

As named polynomials, they are literal members of `J0`.  They do not
import a stale general-rho alphabet into the special-fibre run, provided
the loader is the V37 rho-zero loader and not the literal-total
regenerator.  (The total-dehom compiler is a different object: it
regenerates general-`t` rows and then sets `t=0` as a *control*.)

### 4.3 What is not pinned

The charged ideation treats the 17-row `rho=0,a1=1` unit Gröbner basis
as “already computed (packet §1).”  Packet §1 asserts the unit basis
and a 192-GiB failure to extract the exponent, and gives **no** producer
SHA, **no** `RESULT.json` digest, and **no** independent review SHA.
Card F1 itself says “modulo custody pinning.”  This review did not run
the Gröbner basis and does not confirm that it is the unit ideal.

A wired control in the total-dehom compiler
(`FAIL_V43_TOTAL_DEHOM_SPECIAL_CONTROL` if `std(I|_{t=0})` does not
reduce `1` to 0) is a belief about the 17-row special fibre, not a
harvested theorem.

### 4.4 The special-fibre half does not need the 17-row GB

Promoted V42, independently reviewed (Opus5), is: the frozen raw
ordered-`a1`, `rho=0` system through grade 19 has no characteristic-zero
field point on `D(a1)`.  The ideal is homogeneous, the base field
extension `Q→Qbar` is faithfully flat, and the Nullstellensatz over
`Qbar` plus descent give `a1∈√(J0)` in the 65-variable ring.  The
correction review transports this to the 66-variable ring because `ez9`
is a free spectator after `rho=0`.  Equivalently
`(J0:a1^∞)=(1)`, with a non-effective exponent; the displayed `a1^8` is
only an A1-branch certificate and is not used here.

So the second conjunct of the two-fibre lemma is already a promoted
theorem for the *full* `J0`.  The 17-row unit, if and when it is
custody-pinned, is an explicit dehomogenized generating certificate of
the same conjunct, and a route to an effective special-fibre exponent.
It is not the load-bearing input.

### 4.5 Verdict on Attack 4

**REPAIRABLE.**  Repair: pin V42 (`5d4c42ff...` / `a4f6b931...`) as the
special-fibre half; treat the 17-row GB as an optional effective
certificate whose unit conclusion, *if* the named rows are the V42
cascade rows above, is algebraically sound for `J0|_{a1=1}=(1)` and
does not import bilinears or localizers.  Do not let Card F1 depend on
an unpinned packet sentence.

---

## 5. Attack 5 — computational consequences

### 5.1 Selected-row generic unit / nonunit

Let `J_sel ⊂ J` be any subideal (in particular the seventeen cascade
rows, with or without `Tg19_2`).

- If `J_sel|_{a1=1}=(1)` over `Q(rho)`, then `J|_{a1=1}=(1)` over
  `Q(rho)`.  Combined with `a1∈√(J0)`, the lemma gives `K+(rho)=(1)`.
  **One-sided decisive for the positive direction.**  If the extracted
  cofactor after rehomogenization already has nonzero constant term,
  one has a typed certificate in `J_sel` and therefore in `J`.
- If `J_sel|_{a1=1}≠(1)` over `Q(rho)`, nothing follows about `J`.
  **A selected-row nonunit is not a theorem.**  The already-live
  selected-row total-rho elimination lanes remain exactly this
  one-sided instrument.  The candidate states this correctly.

### 5.2 Full-system generic nonunit

If the *full* frozen `J|_{a1=1}` is not the unit ideal over the field
`Q(rho)`, then `a1∉√(J Q(rho)[X])`, hence `a1∉√(J S')`, hence
`K+(rho)≠(1)` for this truncation.  That is a theorem about the frozen
grade-through-19 ordered `T-a1` chart.  It is not Gate T, not all-depth,
and not a license that later grades leave a survivor (§6).

Mandatory generators and variables for “full”:

- all 59 nonzero general-rho rows, including the eight that vanish at
  `rho=0` (`Tg11_2,Tg11_3,Tg11_5,Tg11_7,Tg12_5,Tg12_7,Tg13_7,Tg14_6`);
  those eight are invisible to every special-fibre computation and can
  still kill the generic fibre;
- the unique general-only term `(3/8)rho^2 a1 ez9` in `Tg19_2`; after
  `a1=1` this is `(3/8)rho^2 ez9`, a linear pivot with unit coefficient
  in `Q(rho)`, so `ez9` is eliminated immediately on the generic fibre
  and is *not* a spectator there;
- the 66 positive-weight variables, not the 65-variable rho-zero
  alphabet.

A reduced Gröbner basis over the *field* `Q(rho)` not equal to `{1}` is
a proof of nonunit.  A timeout, a memory kill, or a computation in
`Q[rho][X']` that has not been interpreted as a coefficient-field run
is not a proof.  In `Q[rho][X']`, a nonzero element of `Q[rho]` in the
ideal *is* a unit over `Q(rho)`; Card F1’s “GB reaching `[1]`” is too
narrow as software and should accept “GB meets `Q(rho)^*`.”

### 5.3 Full-system generic unit does not by itself give `U(0)=1`

Suppose `J|_{a1=1}=(1)` over `Q(rho)`.  Then there is a Bézout identity
with coefficients in `Q(rho)[X']`.  Clearing a common denominator
produces `v(rho)∈Q[rho]\0` with `v` in the dehomogenized ideal over
`Q[rho]`.  Rehomogenizing as in §3.3 gives

```text
v(rho) a1^D ∈ J.
```

Two cases:

- `v(0)≠0`: this *is* the `S'` certificate.  Average to even, normalize
  to `U(0)=1`, replay at weight `5D`.  Promotable after that replay.
- `v(0)=0`: this is only the generic-fibre conjunct.  The special-fibre
  conjunct is still required, and the combined cofactor in `T` may need
  a larger exponent than `D`.  The identity `v a1^D∈J` does **not**
  rehomogenize “directly to `a1^D u∈J` already of weight 0 with
  `u(0)≠0`.”

Toy for the second case, homogeneous and even: `J=(rho^2, a1^2)`.  Then
`J|_{a1=1}=(rho^2)` is the unit ideal over `Q(rho)` after inverting
`rho`, the cleared identity is `rho^2·1 ∈ J|_{a1=1}`, rehomogenization
gives `rho^2 a1^0` or `rho^2 a1^2` according to weight, and `v(0)=0`.
The special fibre is `J0=(a1^2)`, unit after `a1=1`.  Both conjuncts
hold, `K+(rho)=(1)` because `a1^2∈J` already, but the generic Bézout’s
denominator vanished at 0.  The candidate’s converter paragraph is
false as a general algorithm.  It is true on the open set of Bézout
identities whose content is in `T`.

Promotion standard: a software `{1}` over `Q(rho)` plus V42 is
mathematically `K+(rho)=(1)` by the lemma.  The campaign’s reviewed
certificate type is an explicit `a1^N U(rho^2)∈J` with `U(0)=1`.  Do
not promote a chart closure on an engine-dependent unit without that
replay.  Card F1 stage 4 (extract, then V43-style fixed-weight
verification) is the right gate; it is not optional polish.

### 5.4 Card F1 staged discriminator

| Stage | Claim | Verdict |
|---|---|---|
| 0. Different-model check of the lemma | correctly ordered | this report |
| 1. Modular `(p, rho=c≠0)` census | heuristic only | a nonunit at one `p` is reduction and proves nothing; nonunits at infinitely many `p` with no bound on the eliminant degree still do not replace stage 3; a unit at good `p` is the expected reduction of a generic unit *or* of an exceptional empty fibre |
| 2. Exact `Q` at one random rational `c`, “decisive-grade evidence” if unit | **REFUTED** | see smallest failing implication, and the explicit family below |
| 3. Full `Q(rho)` run | **CONFIRMED** as the decision, both directions, for the frozen chart, provided “full” is as in §5.2 and a unit is not promoted before stage 4 |
| 4. Extract `(D,u)`, replay `a1^D u∈J` | **CONFIRMED** as the promotion gate; **REPAIRABLE** as an algorithm (handle `v(0)=0`) |
| Controls: rho=0 specialization of the stage-3 input reproduces the known special-fibre unit; a low-grade subset returns nonunit | **CONFIRMED** as controls, not as proofs | the positive control is V42 / 17-row; the negative control (low-grade survivors) is documented |

**Counterexample to stage 2.**  In `Q[rho,x]`, let `I=(x, rho-1)`.  Then
`I⊗Q(rho)=(x)≠(1)` (generic nonunit) while `I|_{rho=2}=(x,1)=(1)` (unit
at a rational `c≠0`).  Empty closed fibres of a generically nonempty
family are a proper closed set.  A unit at one `c` is the expected
behaviour of an exceptional empty fibre, not evidence of generic
emptiness.  The candidate has the semicontinuity backwards.

A nonunit at one rational `c` is likewise not a generic nonunit: it is
consistent with a generic unit whose eliminant vanishes at that `c`.
Several independent nonunit fibres make a generic unit unlikely, but
without a degree bound on `I∩Q[rho]` they are not a proof.

Stage 1 “consistent nonunits ⇒ skip to the survivor hunt” is navigation,
not a theorem.  It may be a resource rule.  It must not be reported as
`K+(rho)≠(1)`.

### 5.5 Asymmetric finality

Adjoining later-grade rows enlarges `J`.  Membership persists; nonunit
need not.  The candidate’s V38-style asymmetry is correct for the frozen
chart:

- frozen unit (with certificate) ⇒ the ordered `T-a1` special fibre is
  empty through grade 19 and stays empty after later rows of the same
  presentation;
- frozen nonunit ⇒ `K_{≤19}+(rho)≠(1)`; `K_{≤20}+(rho)` is a different
  ideal.  Unholding grade-20+ exports is a purpose, not a theorem that
  a survivor survives.

---

## 6. Attack 6 — toy, overstrong versions, three objects

### 6.1 The candidate’s toy

`J=(x(x-rho y))` in `Q[rho,x,y]`, weights `wt(x)=wt(y)=1`.  Homogeneous
of weight 2.  Odd in `rho`, so it is *not* a model of the even-parity
source; it is a legal model of the two-fibre lemma, which does not use
evenness.

- Special: `J0=(x^2)`, `x∈√(x^2)`, and `J0|_{x=1}=(1)`.  Conjunct two
  holds.
- Generic: the point `(x,y)=(rho,1)` over `Q(rho)` lies on `V(J)` with
  `x≠0`, so `x∉√(J Q(rho)[x,y])`, and `J|_{x=1}=(1-rho y)≠(1)`.  Conjunct
  one fails.
- Saturation: `K=(x-rho y)`, `K+(rho)=(x,rho)≠(1)`.

The three sides of the lemma fail together.  The toy does what is
claimed.  Hand arithmetic only; no CAS.

The reviewed design’s even toy `J=(f-rho^2 x)` likewise has special
fibre unit (`f∈J0`) and `K+(rho)≠(1)`, with generic fibre nonunit in
the domain `Q(rho)[x]`.  Both toys kill the overstrong converse
“special fibre empty on `D(a1)` ⇒ total chart empty.”  That converse
was already withdrawn (`593f953b...`); the two-fibre lemma does not
revive it, because it demands the generic conjunct as well.

### 6.2 Overstrong versions, each with a counterexample

**O1.**  `a1∈√(J0) ⇒ K+(rho)=(1)`.  False.  Both toys.

**O2.**  `a1∈√(J k(rho)[X]) ⇒ K+(rho)=(1)`.  False.  `J=(rho)`: generic
fibre is the zero ring, so `a1` is vacuously in the radical; `J0=(0)`,
`a1∉√(J0)`; `K=(rho)`; `K+(rho)=(rho)≠(1)`.  Homogeneous, even.

**O3.**  `J|_{a1=1}=(1)` over an algebraic closure of `Q(rho)`, but not
over `Q(rho)`.  False: unit-ideal membership descends along field
extensions.

**O4.**  Selected-row generic nonunit ⇒ frozen `K+(rho)≠(1)`.  False.
Any proper subideal can fail to be `(1)` while the full ideal is `(1)`.
The 17-row generic fibre is this case until it is proved to generate
the same radical as `J` after `a1=1`, which is not claimed and not
true a priori.

**O5.**  Full frozen generic nonunit ⇒ all-depth source survivor, or
Gate T negative, or a landing-side counterexample.  False.  See §6.3.

**O6.**  Generic Bézout `1=∑ m_i T_i|_{a1=1}` over `Q(rho)` rehomogenizes
to `a1^D u∈J` with `u(0)≠0`.  False.  §5.3.

**O7.**  Exact-`Q` unit at one `rho=c≠0` ⇒ generic unit up to a finite
exceptional set.  False.  §5.4.

**O8.**  `a1∈√(J S')` requires `U` even.  False.  §2.2.  The candidate
does not claim O8; Card F1’s converter should not accidentally claim
it either.

### 6.3 Three objects, not one

**Frozen grade-through-19 ordered `T-a1` chart.**  This is the object of
the lemma.  `J` is a finite list of homogeneous rows.  A positive
certificate closes this chart’s special fibre and is monotone in later
rows of the same presentation.  A negative is a nonempty special fibre
of *this* saturated truncation.  Later source rows of grade `≥20` are
absent; they can only shrink `K`.

**All-depth source.**  The actual-total series continues past grade 19.
A frozen negative is not an all-depth survivor: one new row can kill
the prefix-relative component.  A frozen positive is an identity in the
truncated ideal and remains an identity in the all-depth ideal, so it
does close the all-depth ordered `T-a1` special fibre *provided* the
later rows are still in the same ring and the same presentation.  It
does not close other charts, the terminal receiver, or ramified
`rho=0` deck/square.  Weight-35 duals of the truncated matrix are
frozen-chart theorems; advertising them as all-depth is O5.

**Gate T.**  Gate T is the global landing comparison (total versus
special, covering the ordered `T` charts and the Jacobian condition).
`K+(rho)=(1)` on this one chart is not Gate T.  `K+(rho)≠(1)` on this
one chart is not a Gate T negative.  The candidate’s firewall in
unrelated rows is mostly intact; the phrase “first honest surviving
landing geometry” in Card F1’s non-unit branch is the place it slips.
A prefix-relative nonempty special fibre of one truncated chart is a
truncated-chart survivor.  Parametrizing it is a new producer, centered
at the origin only after §3.3’s cone argument, and still not Gate T.

§3.3 of the ideation (origin funnel) is not charged as a numbered
equivalence.  For the record: if `P` is a homogeneous prime containing
`K` with `P∩Q[rho]⊆(rho)` and `a1∉P`, then `V(P)` is a cone, the
`G_m`-limit of any of its points is the origin, and that origin has
`rho=0`.  Every homogeneous saturated-chart survivor meets the terminal
origin section.  That is a reason the receiver stays load-bearing under
*either* Card F1 outcome.  It is not a reason to call a frozen negative
a landing-side counterexample, and the `G_m`-limit here is on a cone in
affine space over an algebraic closure, which is legitimate because one
is describing support, not writing a membership identity over `Q`.

---

## 7. Strongest exact theorem

Let `k` be a field.  Let `S=k[rho,X]` be positively graded with
`wt(rho)=0` and `wt(x)>0` for all `x∈X`.  Let `a1∈X` have positive
weight.  Let `J⊂S` be a weighted-homogeneous ideal, `K=J:a1^∞`,
`J0=J|_{rho=0}`.  Let `T=k[rho]\(rho)` and `S'=T^{-1}S`.  Then the
following are equivalent:

1. `K+(rho)=(1)` in `S`.
2. There exist `N≥0` and `U(rho)∈k[rho]` with `U(0)=1` and
   `a1^N U(rho)∈J`.
3. `a1 ∈ √(J S')`.
4. `a1 ∈ √(J k(rho)[X])` and `a1 ∈ √(J0)`.
5. `J|_{a1=1}=(1)` in `k(rho)[X\{a1}]` and
   `J0|_{a1=1}=(1)` in `k[X\{a1}]`.

If `J` is invariant under `rho↦-rho`, these are further equivalent to

2′. There exist `N≥0` and `U(t)∈k[t]` with `U(0)=1` and
    `a1^N U(rho^2)∈J`.

No algebraic closure is required.  Vertical fibres `rho=c≠0` are
irrelevant.  Embedded primes and nilpotents are included.  Exponents on
the two fibres need not equal the combined exponent.  The even form
(2′) is not needed for (1)–(5).

**Specialization to the frozen ordered `T-a1` total chart through grade
19.**  Here `k=Q`, `X` has 66 positive-weight variables, `rho` is the
unique weight-zero variable, `J` is the literal homogeneous total
ideal, and `ez9` occurs only as `(3/8)rho^2 a1 ez9` in `Tg19_2`.  The
right-hand conjunct of (5) is the promoted V42 theorem (full `J0`,
non-effective exponent), independently of any 17-row Gröbner basis.
The left-hand conjunct of (5) is the one remaining computation.

---

## 8. Safe compute plan

Replace Card F1’s stages with the following.  Nothing here is a launch.

0. **Lemma.**  Use §7, not the ideation’s sketch `(iii)`.  Pin the
   special-fibre conjunct to V42 (`5d4c42ff...` / `a4f6b931...`), with
   the Fable5 spectator transport of `ez9`.  Optionally pin a 17-row
   `rho=0,a1=1` unit basis, if and when a harvested digest exists, as
   an *effective* special-fibre certificate in the cascade subideal;
   do not block the generic run on that pin.

1. **Ring of the generic run.**  `Q(rho)[X\{a1}]` as a polynomial ring
   over a field, generators all 59 nonzero general-rho rows with `a1=1`,
   including `Tg19_2` and the eight rho-only-nonzero rows.  Linear
   pre-elimination of `ez9` against `(3/8)rho^2 ez9` is exact over
   `Q(rho)` and is recommended.  Any monomial order that can detect
   `(1)` is valid; elimination order is not required for unit detection.

2. **Heuristic screens, demoted.**  Modular `(p,c)` and exact-`Q` fibres
   at finitely many `c≠0` are resource probes and negative controls for
   software.  They are not theorems in either direction.  Do not skip
   stage 3 on consistent modular nonunits.  Do not treat a unit at one
   rational `c` as generic evidence.

3. **Decision.**  One complete Gröbner basis of the full dehomogenized
   generic fibre over `Q(rho)`.

   - **Nonunit** (reduced GB over the field, not `{1}`, no resource
     kill): theorem `K+(rho)≠(1)` for the frozen grade-through-19
     ordered `T-a1` chart.  Stop.  Unhold later-row exports as
     navigation.  Primary decomposition of the `a1=1` slice is a new
     producer, not a corollary.  Firewall: not all-depth, not Gate T,
     not a landing-side counterexample, not JC2.
   - **Unit** (GB meets `Q(rho)^*`): do not promote.  Proceed to 4.
   - **No verdict** (timeout, memory, incomplete basis): fall back to
     the per-`N` DVR ladder as a floor-raiser, exactly as the packet
     already allows.  The ladder still cannot prove existence.

4. **Certificate, required for a positive promotion.**  Lift the Bézout
   identity, project to weights `0 mod 5`, rehomogenize, clear
   denominators to `v(rho) a1^D ∈ J`.

   - If `v(0)≠0`: even-average, normalize `U(0)=1`, replay the identity
     at weight `5D` against the literal total rows with the V43
     unrestricted-support verifier.  That replay is the promotion
     object.
   - If `v(0)=0`: the generic conjunct is proved but the typed
     cofactor is not in `T`.  Combine with a special-fibre power
     (V42 existence, or an effective 17-row exponent if pinned) by the
     reviewed syzygy-colon over `Q[t]_{(t)}` at a weight large enough
     to carry both exponents.  Do not declare `U(0)=1` from the generic
     Bézout alone.

5. **Selected-row lanes, still live, still one-sided.**  A selected-row
   generic unit with extracted `U(0)≠0` is a positive certificate for
   the full ideal and ends the search.  A selected-row nonunit is
   discarded.  This is the only sense in which the already-running
   eliminant jobs can decide Card F1 without the full-system run.

6. **Stop rule.**  Keep a resource cap.  Crossing it without a complete
   GB is `NO VERDICT`, not a negative.  A complete nonunit is a
   negative for the frozen chart even if it arrives late.

---

## 9. What this review does not do

It does not prove or disprove `K+(rho)=(1)`.  It does not run a Gröbner
basis.  It does not certify the packet’s 17-row unit computation.  It
does not review V43’s dual as a result.  It does not close the terminal
receiver, ramified `rho=0` deck/square, source/landing coverage, Gate T,
order two, maximum twelve, or JC2.  It does not authorize promotion of
Card F1 as written.

It does confirm that the two-fibre lemma, once the dehomogenization
step is proved by the graded-unit argument rather than by scaling
points over `Q(rho)`, is an exact decision procedure for the frozen
ordered `T-a1` special fibre, with the special-fibre conjunct already
in the ledger via V42, and with the generic fibre over `Q(rho)` as the
one remaining algebra.

---

## Line-item recap

| Item | Verdict |
|---|---|
| `K+(rho)=(1) ⇔ a1∈√(J S')` | **CONFIRMED** |
| `a1∈√(J S') ⇔` generic and special radical membership | **CONFIRMED** |
| those ⇔ `J|_{a1=1}=(1)` over `Q(rho)` and `J0|_{a1=1}=(1)` over `Q` | **CONFIRMED** (proof **REPAIRABLE**) |
| Primes of `T^{-1}Q[rho]` are `(0)` and `(rho)` only | **CONFIRMED** |
| Vertical fibres `rho=c≠0`, embedded primes, nilpotents break the lemma | **REFUTED** as attacks; they do not |
| Even `U(rho^2)` required for the two-fibre lemma | **REFUTED**; it is a reviewed extra for the typed DVR form |
| Written `G_m`+Nullstellensatz-over-`Q(rho)` sketch | **REFUTED** as a proof |
| `a1=1` valid radical slice for this grading | **CONFIRMED** |
| 17-row subideal unit ⇒ full special-fibre unit | **CONFIRMED** as algebra, rows are the right kind of object |
| 17-row GB “already computed” as a load-bearing pin | **REPAIRABLE**; use V42 |
| Selected-row generic unit / nonunit one-sidedness | **CONFIRMED** |
| Full-system generic nonunit decisive for the frozen chart | **CONFIRMED** |
| Full-system generic unit promotes without an explicit `U(0)=1` identity | **REFUTED** |
| Card F1 stage 2 “one rational unit is decisive-grade” | **REFUTED** |
| Toy | **CONFIRMED** |
| Frozen negative = all-depth or Gate T | **REFUTED** |

**Strongest exact theorem:** §7.

**Safe compute plan:** §8.

**Smallest failing implication:** Card F1 stage 2, as quoted in the
verdict summary.

REPAIRABLE
