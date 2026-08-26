# Hostile text-only follow-up — D1 double-root correction rays

| Field | Value |
|---|---|
| Claim under review | Two exact finite correction-enabled Newton successors, the mandatory fan-scope erratum, the already-emitted AWS control replay, and the correction-aware recurrence design. No solver, no formal lift, no D1 |
| Overall verdict | **CORRECTION_CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | a certified Groebner/tropical traversal of every coordinate-support mask in a **finite-variable** coefficient ring. Until that certificate exists, every bounded `(M,N)` run is `SCREENING_FIXED_SLOPE` |
| Evidence tier | hand algebra in the function field `Q(z)((t))`; SHA-256 of frozen text; inspection of already-emitted AWS stdout/rc/empty stderr. No local Python, Singular, Sage, msolve, Lean, or other substantive symbolic computation |
| Reviewer / model | Grok 4.6 (xAI). Text-only algebra referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` |
| Host | Darwin. Charged replay was not re-run |

No local substantive computation was run. Hashes were checked with `shasum -a 256`. The AWS identities were read as emitted text and compared with the hand expansions below.

Frozen hashes charged in the prompt, recomputed and matched:

```text
466736cdd1a76607e6475c98d9da4b55096e88813d911722954549bdcba702c0  xmodel/max12-912-order3-d1-double-root-newton-fan-correction-firewall-20260825.md
bbbd7aec20d5a987ae619f7530ea08a3267e32be035ab3534f615543df70b2d0  cases/max12_912_order3_d1_double_root_correction_recurrence_20260825/FREEZE.sha256
2f718839bb063f3f889d5bbca2688d3fac5d5ba1a19ae7a5ca3634324a5eed40  cases/max12_912_order3_d1_double_root_correction_recurrence_20260825/aws_box02/stdout
015ed8156197ba4cfac55cbc6d33379d7545739bfe657856febd8e17c8d3913c  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/FREEZE.sha256
```

Nested hashes used below also match, including charged source `67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623`, replay script `79333f36057a60acab8d93ecb37160bd2482977c09c696929fd2dc44067f11ea`, empty stderr `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, quarantined source-review `c31cb5f1b42080bc9d9975f74669246c436d0ad9db34de98d3a4037287ce9eb7`, and `SCOPE_ERRATUM.md` at `8f642c4a82e92db102df90e3b4043b6b21a980a8ad8a2cbdadd37279676a9a70`.

Read in full before the verdict: the firewall, `SCOPE_ERRATUM.md`, `SOURCE_REVIEW_ERRATUM.md`, recurrence `DESIGN.md` / `PREREGISTRATION.md` / `AWS_REGISTRATION.md` / `README.md` / `verify_correction_controls.py` (read, not executed), the Box02 `stdout` / `rc` / empty `stderr` / `source.check`, toric `PREREGISTRATION.md` and compiler header, and Charge 3 of the quarantined source-review.

---

## Promotion

**Accept `THE TWO DISPLAYED FINITE SUCCESSORS ARE EXACT NEGATIVE CONTROLS AGAINST THE PROPOSED WHOLE LOW-FAN CLASSIFICATION. IN THE WINDOW 3β/2<α<2β THE FORCED CORRECTION R_(2β)=U/9 CANCELS THE WEIGHT-3β Q³ TAIL AFTER QR/K IS ALREADY POLYNOMIAL. ON THE FACE α=15/2, 5<β<6 THE FORCED CORRECTION R_(15-β)=−1/2 CONVERTS THE WEIGHT-15 LAYER INTO EXACTLY (2/3)/K, HENCE A PURE ROW-3 TARGET WITH CONSTANT LOAD μ=2/3. NEITHER EXAMPLE IS FORBIDDEN BY PUISEUX RAMIFICATION OR BY THE STRICT CHART Λ=t⁴, τ=t, ρ=t. NEITHER IS A FORMAL LIFT AND NEITHER PROVES D1. THE FROZEN TORIC COMPILER REMAINS EXACT FOR THE TIED CHART α=2β THAT IT ACTUALLY ENCODES; THE ERROR WAS ONLY THE WITHDRAWN FAN-COMPLETENESS SENTENCE. INDIVIDUAL COEFFICIENT-SERIES CONVOLUTION RETAINS EARLIER LAYERS; BOUNDED (M,N) RUNS REMAIN SCREENING UNTIL A FINITE FAN CERTIFICATE EXISTS; LOAD COORDINATES MUST BE CONSTANT. THE SENTENCE “HIGHER CORRECTIONS SIT IN FREE Qhat,Rhat” DOES NOT LICENSE K²-DIVISIBILITY OF A PURE LEADING NUMERATOR BEFORE THE NEXT COEFFICIENT OF AN EARLIER POLYNOMIAL QR/K LAYER IS INCLUDED AT THE SAME WEIGHT.`**

Do not promote this to: a formal D1 arc; emptiness or occupancy of the tied toric chart; a complete Newton–Puiseux tree; a bounded-denominator classification; or JC2.

---

## Charge 1 — control 1, polynomial QR and weight-`3β` cancellation

**CONFIRMED**

Work at the frozen centre `K=L²U`, `N=LU`, `L=z-1`, `U=z+2`, and start from the charged first ordinary layers

```text
(4/9) QR/K + (2/9) R²/K² − (4/81) Q³/K².                 (1)
```

Substitute the displayed jet

```text
Q = t^β N,
R = t^α L + t^(2β) (U/9),
3β/2 < α < 2β
```

(and, in the low-fan window, `0<β<6`). Expand (1) term by term.

**Lower QR layer.** The leading product is

```text
Q0 R0 / K = (N L) / (L² U) = (L U · L) / (L² U) = 1.
```

So

```text
(4/9) QR/K = (4/9) t^{β+α} + (higher weights from the displayed R-correction).
```

This is a polynomial in `z` (in fact a constant). It contributes no negative Laurent tail.

**Inequalities.** Assume `β>0`. The hypothesis `α>3β/2` forces `α>β`, hence:

| channel | weight | comparison with `β+α` and with `3β` |
|---|---|---|
| leading `QR/K` | `β+α` | strictly first: `β+α < 3β` iff `α<2β`, and `β+α < 2α` iff `β<α` |
| `Q³/K²` | `3β` | next candidate because `2α>3β` iff `α>3β/2` |
| `QR/K` from `R_(2β)` | `3β` | lands on the `Q³` weight, not earlier |
| leading `R²/K²` | `2α` | `2α>3β` |
| mixed `R²` | `α+2β` | `α+2β>3β` iff `α>β` |
| `R_(2β)²` | `4β` | `4β>3β` |

The two strict inequalities are therefore exactly the conditions that (i) the first layer is the polynomial QR term and (ii) the next visible weight is `3β`, with no `R²` contamination at or below that weight. Equality `α=3β/2` would collide `R²` with `Q³` before the `U/9` correction arrives (`2β>3β/2`). Equality `α=2β` would make `R_(2β)` part of the leading `R`, i.e. the tied ray, not this control.

**Weight-`3β` tail.** The only contributions at `3β` are

```text
(4/9) · N · (U/9) / K = (4/81) (L U · U) / (L² U) = (4/81) (U/L)
```

and

```text
−(4/81) N³ / K² = −(4/81) (L U)³ / (L⁴ U²) = −(4/81) (U/L).
```

These cancel identically in `Q(z)`, including the polar part along `L`. The complete weight-`3β` expression from (1) is `0`, not a leftover polynomial and not a remainder modulo `K` or `K²`. In particular the proposed step `K² | Q0³` is false once `R_(2β)=U/9` is retained: `Q0=N` is not `K²`-divisible as a cube, yet the actual tail vanishes.

**Omitted-term weights.** Any extra `Q` term of valuation `>β` pushes every `QR` and `Q³` monomial strictly above `β+α` or `3β`. Any extra `R` term of valuation `α'` with `α<α'≠2β` produces `QR` at `β+α'≠3β`; if `α'>2β` then `β+α'>3β` and the corresponding `R²` weights exceed `3β`. The displayed `U/9` is the particular degree-`≤2` solution of

```text
(4/9) (R_(2β)/L) = (4/81) (U/L)
```

i.e. `R_(2β) ≡ U/9 (mod L)`. Adding a multiple of `L` at weight `2β` is a later kernel direction, not an omitted earlier tail. Axis/cusp motion and `kbar` are not present in this jet; they are higher or independent and are not required for the identity.

**AWS instantiation (read, not rerun).** Normalized `β=4`, `α=7` satisfies `6<7<8`. On `Λ=t⁴` this is `Q=t^{16}N`, `R=t^{28}L+t^{32}U/9`, and weight `3β=12` is `t^{48}`. The emitted payload records every ordinary row zero through `t^{48}`.

This is a finite successor through the advertised `Q³` gate. It is not a formal series.

---

## Charge 2 — control 2, polynomial QR and exact `(2/3)/K`

**CONFIRMED**

Put `α=15/2` and `5<β<6`, and

```text
Q = t^β L,
R = t^α N − (1/2) t^{15−β}.
```

The exponent `15−β` equals `2α−β`. It is the unique weight at which `Q·R_corr` lands on `2α=15`.

**Window.** `β<α` holds because `β<6<15/2`. The remaining inequality `α<3β/2` is `15/2<3β/2`, i.e. `β>5`, exactly the stated range. Thus

```text
β < α < 3β/2 < 2β,
```

which is the complementary open to Charge 1. Then `β+α ∈ (25/2, 27/2) ⊂ (12,15)`, so the first layer is strictly below the target weight `15`. Next, `3β ∈ (15,18)`, so `Q³` is strictly above `15`. Mixed `R²` has weight `α+(15−β)=45/2−β ∈ (33/2,35/2)`, and `R_corr²` has weight `30−2β ∈ (18,20)`; both exceed `15`.

**Lower QR layer.**

```text
Q0 R0 / K = L N / (L² U) = 1.
```

Polynomial, no negative tail. Same as Charge 1, with the roles of `L` and `N` swapped.

**Weight 15.** The only contributions from (1) are the leading `R²` and the displayed `QR` correction:

```text
(4/9) · L · (−1/2) / K + (2/9) N² / K²
  = −(2/9) L/(L² U) + (2/9) (L U)² / (L⁴ U²)
  = (2/9) ( 1/L² − 1/(L U) )
  = (2/9) (U−L)/(L² U)
  = (2/9) · 3 / K
  = (2/3)/K.
```

**Sign.** The minus on `1/2` is forced among constants. Replacing it by `+1/2` yields `(2/9)(1/L²+1/(LU))=(2/9)(2z+1)/K`, which is not a constant multiple of `1/K`. Uniqueness: if `R_corr=c` is constant, the numerator of the common-denominator form is `U+2c L=(1+2c)z+(2−2c)`, and vanishing of the `z`-coefficient forces `c=−1/2`, after which the constant is `3` and the load is `μ=2/3`. Amplitude is fixed by leading coefficients `1` on `Q` and `R`; no extra rescaling is present in the displayed jet.

**Only row 3.** Unperturbed inverse of `f=K0³` is defined by `f(z0(w))=w^9` with `z0=w+⋯`, hence principal branch `K0(z0(w))=w³` and `1/K0(z0(w))=w^{−3}`. A pure multiple of `1/K0` therefore occupies only the `w^{−3}` slot, which is ordinary row 3, and no other row. The charged target on that row is `Λ^{15} μ`. The identity produces exactly `μ=2/3`.

Motion of `K` is not in the jet (`a=1`, `h=0`). Corrections to the exact inverse `z(w)` of the perturbed `f=K³+KQ+R` are higher in `(Q,R)` than the displayed degree-two layers of (1). They are not needed to evaluate (1). The already-emitted AWS full-source replay (eight independent Faber rows, not the binomial truncation) records zeros below `t^{60}` and the vector `(0,0,2/3,0,0,0,0,0)` at `t^{60}=Λ^{15}`, so those extras do not change the initial coefficient on this jet.

The simple-factor order argument (`Q0` and `R0` must vanish at `z=−2`) is the wrong obstruction at a target-facing weight: `Q0(−2)=L(−2)=−3≠0`, yet the polar part `1/L²` is converted into `1/K` rather than killed. That is allowed by row 3.

---

## Charge 3 — already-emitted AWS replay

**CONFIRMED.** Not rerun.

| check | emitted value | required |
|---|---|---|
| charged source SHA-256 | `67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623` | pinned in `verify_correction_controls.py`, `SOURCE.sha256`, `SOURCE_CLOSURE.sha256`, and the firewall |
| `source.check` | both `independent_reconstruct.py` and `verify_correction_controls.py` `OK` | preregistered pair |
| `rc` | `0\n` | zero |
| `stderr` | empty (0 bytes, SHA-256 `e3b0c442…`) | empty |
| terminal marker | exactly one line `PASS_D1_DOUBLE_ROOT_CORRECTION_CONTROLS` | preregistered |
| tag | `max12_912_order3_d1_double_root_correction_20260826T002500Z_box02` | matches `AWS_REGISTRATION.md` |
| firewall string | `finite successors only; no formal lift and no complete fan` | present in the payload |
| strict slope | `Lambda=t^4,tau=t,rho=t` | `M=4>3=3N` |

Deletion controls, as recorded and as required by the script that produced the payload:

- Control 1: `omitted_correction_has_nonzero_t48 = true`. Hand reason: dropping `U/9` leaves `(4/81)(U/L)` at weight `3β`, polar along the double root.
- Control 2: `omitted_correction_changes_t60_pattern = true`. Hand reason: dropping `−1/2` leaves `(2/9)/L²=(2/9)U/K`. Then `U(z0(w))·w^{−3}` with `U(z0)∼w+2` contaminates `w^{−2}` (row 2) and is not the pure `(2/3)` on row 3.

Coefficient images in the replay script match the displayed polynomials: control 1 is `q=(t^{16},t^{16},−2t^{16})` and `r=(0, t^{28}+t^{32}/9, −t^{28}+2t^{32}/9)`; control 2 is `q=(0,t^{22},−t^{22})` and `r=(t^{30},t^{30},−2t^{30}−t^{38}/2)`. The ninth image is empty, so this is the constant-load slice `k=0`. A zero-load finite successor still kills a classification that claimed no such ray exists.

The replay consumes the eight independent ordinary tails, not formula (1). That is the correct adversarial check of the hand identities. Formula (1) is the first-layer truncation used to *find* the corrections; the AWS payload is the evidence that the same jets survive the full source through the stated cutoffs.

---

## Charge 4 — ramification and the strict chart `Λ=t⁴, τ=t, ρ=t`

**Neither example is forbidden.**

Both jets are already realized on that strict chart in the emitted replay. `v(Λ)=4>3=3v(τ)`, so they are interior to the strict-slope open, not on the equal-slope wall `v(Λ)=3v(τ)` and not on a `τ`-unit chart.

Rational valuations are cleared by the finite ramification `Λ=t⁴`. Control 1 is integral already (`β=4`, `α=7`). Control 2 has normalized valuations `β=11/2`, `α=15/2`, which become the integral exponents `22` and `30` in `t`; the correction exponent `15−β=19/2` becomes `38`. Characteristic zero, polynomial coefficient identities: the ramified image of a rational Puiseux jet is a point of the same scheme. No extra integral-`β` hypothesis is required.

The examples are *not* points of the tied toric chart `Q=x Qhat`, `R=x² Rhat`. That is a different covering (`α=2β`) and is irrelevant to forbiddance. Control 1 has `α/β=7/4≠2`. Control 2 has `α/β=(15/2)/(11/2)=15/11≠2`. Axis frozen, loads constant (`k=0`, and on control 2 `μ=2/3` constant). Fixed-load semantics do not exclude them.

---

## Charge 5 — what the successors disprove, and what they do not prove

**They disprove the proposed whole low-fan classification. They prove neither a formal lift nor D1.**

The classification re-proved in the quarantined source-review (Charge 3 of `xmodel/max12-912-order3-d1-double-root-toric-blowup-source-review-grok-20260825.md`) asserted that the only possibility with `0<β<6` is `α=2β`, `Q0=q N`, `R0(1)=q²/3`, because after a polynomial `QR/K` layer the next pure `R²` or `Q³` numerator is never `K²`-divisible for `deg≤2`. Charges 1 and 2 are explicit counterexamples to that step, inside the same window `0<β<6`:

- Charge 1 lives in `3β/2<α<2β` and has vanishing complete tail through the `Q³` weight.
- Charge 2 lives in `β<α<3β/2` on the target face `α=15/2` and produces an *allowed* row-3 value rather than an illegal remainder.

So the sentence “sole nilpotent valuation survivor” in the toric `PREREGISTRATION.md` is correctly withdrawn by `SCOPE_ERRATUM.md`. A unit or nonunit of the tied chart cannot be promoted to a whole double-root or whole-D1 statement.

These are finite jets: control 1 is checked through `t^{48}`, control 2 through `t^{60}`. A vanishing jet is not a formal series. Matching a single target weight is not a D1 trajectory. The firewall and the AWS payload both say so, and that restriction is mandatory.

---

## Charge 6 — frozen compiler on the tied boundary `α=2β`

**The compiler remains exact for the chart it encodes. The defect is a withdrawn completeness sentence, not a source-equation bug.**

On `α=2β` the three raw weights collide:

```text
β+α = 2α = 3β.
```

There is no earlier `QR/K` layer whose next coefficient can arrive at the first visible weight. The combined numerator

```text
(4/81) Q (9 R K − Q²)
```

is therefore the correct leading object, and the remainder calculus

```text
Q0 = A N,    R0(1) = A²/3
```

is sound for that ray. The compiler substitutes exactly

```text
f = K³ + K x Qhat + x² Rhat,   x y = Λ⁶,   Λ = τ³ ρ,
```

i.e. `v(R)=2 v(Q)` identically, with moving axis/cusp, all six normal coefficients, exact eight-tail targets, and all three `Rhat` directions retained. `SCOPE_ERRATUM.md` is explicit: no equation, coefficient image, target weight, saturation, boundary equation, or normal direction is changed. `SOURCE_REVIEW_ERRATUM.md` correctly quarantines the fan-completeness re-proof and the local Darwin replay, and correctly preserves the compiler/source-equation audit.

Inference firewall, unchanged and still the only licensed reading of a future terminal:

- `H=1`: the tied `α=2β`, `0<β<6` chart is empty for every fixed load;
- `H≠1`: a total-load-space survivor in that chart only;
- neither closes the correction-enabled rays, D1, or JC2.

`SOURCE_REVIEW_ERRATUM.md` also correctly forbids citing the quarantined report for whole-fan coverage.

---

## Charge 7 — recurrence design

**CONFIRMED as architecture, with the screening firewall enforced.**

**Convolution retains earlier layers.** Tracking six coefficient series `Q_i=∑ q_{i,j} t^j`, `R_i=∑ r_{i,j} t^j` and forming

```text
[t^e] X^m = ∑_{j_1+⋯+j_{|m|}=e} ∏ X_{j_s}
```

substitutes the *full* jets, not `min v(Q_i)` and `min v(R_i)`. The next coefficient of an earlier polynomial `QR/K` layer is an ordinary later factor in the product and appears automatically at the next combinatorial weight. That is precisely the mechanism Charges 1–2 exhibit, and it is the object the seven-case table omitted.

**Tropical / Groebner traversal is a plausible completeness route, not an existing certificate.** For a polynomial ideal in finitely many variables, the Groebner fan is finite; enumerating every coordinate-support mask and every rational cone meeting

```text
v(Q_i), v(R_i), v(a−1), v(h) > 0,    v(Λ) > 3 v(τ) > 0,
```

then certifying initial ideals by a characteristic-zero standard basis and torus support by saturation, is the standard fan-completeness pattern. The certificate must include exponent matrices, primitive rays, adjacency, initial-basis hashes, and coverage of the strict-inequality region. Deduplication only after two ideal containments is the correct rigidity.

Hostile restriction: the coefficient arrays as written are infinite. A Groebner fan is a finite-variable polynomial construction. Completeness for *formal* arcs therefore still needs a finite-determinacy or Artin cut down to a polynomial ring. A traversal of the order-`20M` jet ring is complete for that jet order only. `DESIGN.md` already states that a surviving order-`20M` jet is not a lift; that sentence is mandatory and is hereby enforced. Until a finite-variable certificate actually exists, the phrase “fan-completeness proof” in the design is an architecture, not a theorem.

**Bounded `(M,N)` runs are screening.** Enumerating denominators to a numerical bound never proves slope uniformity. Every fixed `(M,N)` or bounded-denominator execution is `SCREENING_FIXED_SLOPE`: inconsistency through `20M` excludes that chart only; consistency is a finite jet; a list of tested slopes is not a fan. The two correction controls must pass before any recurrence output is consumed. The present AWS replay is exactly that firewall, on one strict slope.

**Loads must be constant.** `k,μ,ν` are declared coefficient-field constants (order-zero arrays only). Total-space emptiness is a uniform exclusion. A total-space survivor must be split by Groebner strata in `(k,μ,ν)` and rerun with those loads held constant. A Puiseux point with varying load coordinates is not a fixed-load arc. Control 2 respects this: `μ=2/3` is a field constant.

---

## Charge 8 — why “higher corrections sit in free `Qhat,Rhat`” does not license premature `K²` divisibility

**The sentence is true as a coverage remark on the tied chart and false as a leading-term calculus on any other ray.**

Quarantined Charge 3 wrote: the leading polynomials `Q0,R0` are the min-valuation forms; higher-valuation corrections sit in the free `Qhat,Rhat` and are included in the closure. In the chart `Q=x Qhat`, `R=x² Rhat` that sentence means: a unit coefficient of `Qhat` or `Rhat` is already part of `(Q0,R0)`, and a positive-valuation coefficient is a later power of `x`. On the tied ray the first weight is `3β=2α=β+α`, so those later powers do **not** arrive at the first layer. Imposing `K²`-divisibility on the combined numerator is then legitimate, which is why Charge 6 stands.

It does not follow that one may impose `K² | Q0³` or `K² | R0²` on a ray with `α≠2β` *before* including the next coefficient of an earlier polynomial `QR/K` layer at the same weight. Those next coefficients are not “higher-valuation corrections in the tied chart”:

1. They do not live in `R=x² Rhat` with `v(x)=β`. Control 1 has leading `v(R)=α<2β`; the cancelling term is at `2β`, which is not a higher term of a series whose leading valuation is already `2β`. Control 2 has `v(R)/v(Q)=15/11≠2`.
2. Even as abstract power series, “higher than the global minimum valuation” is not “absent from the next combinatorial weight”. Once `K | Q0 R0`, the layer `QR/K` is holomorphic at the first weight and its subsequent coefficients are ordinary holomorphic (or polar) contributions at later weights. The `Q³` or `R²` leading remainder is computed in the same graded piece. Truncating to `(Q0,R0)` before adding `R_(2β)` or `R_(2α−β)` is a truncation of that graded piece, not a leading-term argument.
3. The remainder of `Q0³` modulo `K²` can be cancelled by `(4/9) Q0 R_next / K` without `R_next` belonging to `R0` and without `Q0³` becoming `K²`-divisible. Charge 1 is the identity. Likewise Charge 2: `(2/9) R0²/K²` is not `K²`-divisible, but adjoining the same-weight `QR` correction supplies the missing factor of `K` and leaves a multiple of `1/K`.

The earlier report used the tied-chart coverage sentence to underwrite independent divisibility conditions on the three pure leading numerators. That is the precise illicit step. Free `Qhat,Rhat` on `α=2β` cannot see a coefficient of `R` at valuation other than `2β`, and cannot be invoked to discard rays that are not in that chart.

---

## Custody and non-claims

`SCOPE_ERRATUM.md` is a mandatory consumer firewall on the immutable prelaunch freeze. `SOURCE_REVIEW_ERRATUM.md` correctly splits a still-usable compiler audit from a quarantined fan-completeness re-proof and from a policy-violating local CPython replay. The Box02 control replay is AWS custody of two finite identities, not a fan traversal.

Not proved, and not claimed by the frozen correction package: a formal lift of either successor; emptiness or occupancy of the tied chart; completeness of the double-root Newton tree; D1; JC2.

CORRECTION_CONFIRMED
