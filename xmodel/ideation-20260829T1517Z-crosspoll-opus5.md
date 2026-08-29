# Adversarial cross-pollination — Opus 5 — round `20260829T1517Z`

Identity: Opus 5. Basis `40c1ab3448209e3d87173feb947a733f6fe54f7f` (verified at
start and again before sealing). This is adversarial synthesis input, **not a
promotion**. No new exit price is asserted anywhere, so no `charge_basis` line
appears.

## 0. Custody

Packet and all six named inputs rehashed here; every value matches.

```text
fc6a6843545119a5e184755bf5a26b4edce0ae8fbe912935532704608a0c312e
  xmodel/ideation-20260829T1517Z-crosspoll-packet.md   body 8351 /
  e6963ce96110f8f0f01d568da7ca5e0fca22242099e33957b245f4ed5c399fa5
4d51f329...78045b  ideation-20260829T1517Z-sol56.md   body 21571 / fccf2517...
8790a5e9...2afc4f37 ideation-20260829T1517Z-fable5.md  body 22449 / cb03b901...
b01c4882...05d700d  ideation-20260829T1517Z-grok46.md  body 34124 / f809f402...
7d545367...8a895e7a ideation-20260829T1517Z-opus5.md   body 35263 / ce6be254...
1ec95a45...5f79bb2e k00-grade4-...-review-grok46-...md body 25176 / 41da5999...
068ed91b...54fd9bad td12-b25-resrow-...-opus5-...md    body 37413 / 2e5a062f...
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
  .../ATLAS_EXACT_POLYNOMIALS.json   (62,072,089 B)
24640d0d...348fc892  compile_fitting_atlas_v26.py  (digest convention only)
```

The last review's body ends at a literal `## Seal` heading rather than a
`BODY-END` marker; its declared `report_body_bytes = 37413` /
`2e5a062f...` reproduces under that convention.

Also read, all predating the packet, for the source-typing question of §3:
`xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md`
(`d453b956...`, 08:08:25Z) and
`xmodel/max12-812-order2-k00-v22r1-first-weighted-stratum-hostile-review-20260827.md`.

**Read-boundary disclosures.**
`xmodel/k00-grade5-rank0-plane-structural-provisional-sol56-20260829.md` exists
at 08:57:27Z, **after** the packet (08:51:54Z). I checked its timestamp and did
not open it. The concurrently owned lane
`k00-grade5-rank0-plane-twoinput-primary-fable5-40c-20260829` has `.prompt.md`,
`.log`, `.run.v2` from 08:21–08:22 and no sealed `.md`; the packet does not name
it and I did not read any of it. No web, AWS, canonical edit, commit, push, or
`jc2-lean` access of any kind. Scratch in `/tmp/op5xp/` only. Exactly one
repository file written: this one.

**Self-audit discipline.** My blind scratch (`/tmp/op5id/K00G5.py`) was not read,
executed, or consulted. §2 is a from-scratch reconstruction from the atlas bytes
under a freshly declared ring map. Where it agrees with my blind lane that is
*same-model* agreement and is weaker evidence than a different-model replay;
where it disagrees I record the disagreement as a repair against my own report.

Desk cost, all runs combined: **< 1.2 s CPU, peak RSS 17.5 MB** — far inside the
60 s / 1 GiB cap. Script digests in §8.

---

## 1. Radical versus scheme — the binary algebra, and who got it wrong

### 1.1 The identity holds, in any commutative ring

**Claim.** For ideals `I, J` of a commutative ring `R`,
`sqrt(I+J) = sqrt(sqrt(I)+J)`.

*Proof.* `⊆`: `I ⊆ sqrt(I)` gives `I+J ⊆ sqrt(I)+J`, and `sqrt` is monotone.
`⊇`: let `a ∈ sqrt(I)`, so `a^n ∈ I ⊆ I+J`, so `a ∈ sqrt(I+J)`; and
`J ⊆ I+J ⊆ sqrt(I+J)`. Since `sqrt(I+J)` is an ideal it contains the sum, so
`sqrt(I)+J ⊆ sqrt(I+J)`; apply `sqrt` and use `sqrt(sqrt(K))=sqrt(K)`. ∎

No Noetherian, reduced, or finite-type hypothesis is used.

### 1.2 What is therefore forced to agree

Over any base, and in particular set-theoretically over an algebraic closure:
the closed subscheme supports `V(I+J) = V(sqrt(I)+J)`; hence identical
**point sets**, identical **minimal primes**, identical **Krull dimension** of the
quotients, and isomorphic **reduced quotients**
`R/sqrt(I+J) ≅ R/sqrt(sqrt(I)+J)`.

**Unit/proper agrees in both directions**, which is the load-bearing corollary
and the one the blind reports get wrong. Forward: `I+J ⊆ sqrt(I)+J`, so
`I+J = (1) ⟹ sqrt(I)+J = (1)`. Backward: `sqrt(I)+J = (1) ⟹
sqrt(sqrt(I)+J) = (1) ⟹ sqrt(I+J) = (1) ⟹ I+J = (1)`. So

```text
   I+J is the unit ideal   <==>   sqrt(I)+J is the unit ideal.
```

### 1.3 What can still differ

The ideals themselves (`I+J ⊊ sqrt(I)+J` in general); nilpotents; **embedded and
associated primes**; multiplicity, degree, Hilbert function; tangent and jet
spaces; **Fitting ideals and their ranks**; obstruction to infinitesimal lifting;
flatness. Witness, verified by hand: `R = Q[x,y]`, `I=(x^2)`, `J=(y-x)`. Then
`I+J = (x^2,y-x)` with quotient `Q[x]/(x^2)` (length 2, non-reduced) while
`sqrt(I)+J = (x,y-x)` with quotient `Q` (length 1, reduced); both radicals are
`(x,y)`, one point, dimension 0, both proper.

### 1.4 The exact claims that are errors

* **Fable, Card B outcome list — REFUTED.** "Stage-1 nonempty, stage-2 unit →
  nilpotent obstruction: the nonreduced structure kills prolongation while
  points survive." This branch **cannot occur**: by §1.2 the unit verdict is the
  same on both inputs. Fable's two-variant design does anticipate a real
  divergence, but not this one, and the outcome list must be repaired or the
  card will accept an impossible reading of a real run.
* **Grok, Card 2 outcome list — REFUTED as stated.** "Unit on either input: this
  plane-branch dies at G5 on that input. Report which input." There is no "which
  input": unit is input-independent. The instruction to report it invites a
  false distinction.
* **Grok §3.2 — mis-conditioned.** "If they [Fitting ranks] agree, radical input
  covers field-valued points of *this* gate." The field-valued-points conclusion
  is **unconditional** — it does not depend on the rank comparison at all. The
  rank comparison is about the thickening only.
* **Grok's own post-blind review §7 — over-scoped.** "They must be run separately
  because `I4 ≠ sqrt(I4)`." Separate runs are needed only for scheme-level
  invariants (multiplicity, Fitting, embedded structure). For unit/proper,
  points, and dimension the radical input is not merely first, it is
  **sufficient**, and the scheme run is redundant.
* **Sol §4 — CORRECT, and sharper than claimed.** Sol's radical-first scheduling
  theorem is right. Sol says the two variants "can differ in nilpotents,
  multiplicity, tangent directions, and liftability" — true — and calls the
  second run "redundant" for existence — also true. I add the direction Sol did
  not state: the *unit* verdict is redundant too.

### 1.5 What survives, and the radical-first redesign

Grok's Fitting/thickening idea and Fable's nilpotent-lifting idea both survive as
**genuinely non-geometric** questions; neither can produce a unit ideal the
radical input misses. They must be re-typed as multiplicity/Fitting questions,
not as branch-kill questions.

The redesign is stronger than "run the radical first". §2 below decides the whole
grade-five question **with no ideal computation of any kind**: the reduced
grade-four locus `{RA=RB=0}` admits an explicit polynomial parametrization
(bijective, §2.3), so the entire gate becomes substitution plus linear algebra
over `Q` and `Q(i)`. No Groebner basis, no `sat()`, no localizer ideal, no
primary decomposition. That is the correct radical-first design and it is what
made a registered heavy gate a sub-second desk run.

---

## 2. Hostile audit of `G5-COLLAPSE` — `PASS_WITH_REPAIR`

Reconstructed from `exact_terms` with `fractions.Fraction`, CPython 3.9.6.
Producer scratch not read or run.

### 2.0 Reconstruction and declared ring map

All 49 literal rows through grade six rebuilt from `exact_terms` alone and
checked against the compiler's own `p_payload`/`p_digest`/`p_text` convention:

```text
digest 49/49    term-count 49/49    singular-text 49/49
grade  0 1 2 3 4 5 6  terms per row
  g=2  [8,11,9,12,8,0,6]      g=4  [45,60,67,84,86,77,99]
  g=3  [23,26,31,33,35,21,35] g=5  [83,106,133,160,186,184,235]
                              g=6  [131,178,223,285,335,369,457]
```

`Q1_to_Q6` equals literal grade-two rows `(1,2,3,4,5,7)`; literal grade-two row 6
is the zero polynomial. I did not use the compressed list (the `q6`/row-7 trap).

**Ring map, declared then verified (FALLACY variable/ring map; Grok Repair R1).**
Name-based, jet-major, coefficient field `Q`; unmapped source names raise
`KeyError` (no positional coercion against the component-major 33-generator
atlas `ring_variables`).

```text
phi:  d0_1..d5_1 |-> (2s, t/8, s, t, s, 2t)        [the plane Pi]
      d*_2 |-> u,  d*_3 |-> v,  d*_4 |-> x,  d*_5 |-> y
      k10_0 |-> k0, k10_1 |-> k1, k10_2 |-> k2
mu(s,t) = (s^2, s t/8, 16 t^2, 0, 0, 0),   w := u - mu
RA := 16 u1 - 4 u3 + u5 - 2 s t = 16 w1 - 4 w3 + w5
RB := u0 - 4 u2 + 2 u4 - s^2 + 64 t^2 = w0 - 4 w2 + 2 w4
```

Baseline reproductions: grade two and grade three vanish identically on `Pi`
with `u` free, `7/7` and `7/7`; the grade-four closed form
`phi(Lambda_{4,r}) = Lambda_{2,r}(w)` holds `7/7`; mutating `16t^2 → 15t^2` in
`mu` breaks `6/7`. Grok's `coeff(d_j_3, Lambda_4) = coeff(d_j_2, Lambda_3)`
reproduces `42/42`.

### 2.1 Item 1 — affine-linearity and the two vanishing blocks

```text
phi(Lambda_{5,r}) term counts   42, 49, 57, 53, 64, 33, 61
deg in the d*_4 block           0 0 0 0 0 0 0      (d*_4 gone, 7/7)
deg in k10_1                    0 0 0 0 0 0 0      (k10_1 gone, 7/7)
deg in (v0..v5, k10_0) jointly  1 1 1 1 1 0 1
k10_0 present                   1,2,3,5,7 only ;  d*_3 present  1,2,3,4,5,7 only
```

**CONFIRMED**, and the term counts and per-row census agree exactly with Grok's
independent §7. **Repair R-3:** my blind §3.2 says "total degree `1` in the seven
unknowns jointly". The correct statement is **degree ≤ 1** — row 6 has degree 0,
and row 4 carries no `k10_0`. "Affine-linear" is right; "total degree 1" is not.

### 2.2 Item 2 — the shifted grade-three coefficient matrix

With `C_{r,j}(d*_1) := coeff(d_j_2, Lambda_{3,r})`:

```text
coeff(v_j, phi(Lambda_{5,r})) == C_{r,j}(w)      42/42 slots
36 of the 42 slots C_{r,j}(w) are nonzero        (the match is not vacuous)
```

**CONFIRMED.** See §4 for what this law actually is — it is not what any of the
four blind reports called it.

### 2.3 Item 3 — residuals, branches, conjugate branch

The reduced grade-four locus `W4 = {RA=RB=0}` is parametrized **bijectively** by
`(w1,w2,X,Y)` via `w = (2w2+2Y, w1, w2, 8w1-X, w2-Y, 16w1-4X)`, i.e.
`X = 8w1-w3`, `Y = w2-w4`. All seven **literal** grade-four rows vanish on it
(`7/7`), so these are scheme points, not merely radical points.

On `W4` the seven grade-five rows have exactly 15, 15, 15, 3, 15, 0, 15 terms;
row 6 is identically zero, row 4 carries **no unknown at all**, and the
`(v,k10_0)`-linear parts of rows 3, 5, 7 are exactly `-1/8`, `-1/128`, `-1/1024`
times row 1's — **including the `k10_0` slot**, so the residuals are free of every
unknown. The two unconditional necessary conditions are

```text
Phi4 = (3/32768) [ 64 s X^2 + 128 t X Y - s Y^2 ] = 0
Phi3 = (3/2048)  [ 64 t X^2 -   2 s X Y - t Y^2 ] = 0
      with  Phi5 = -(1/8) Phi3   and   Phi7 = -(1/128) Phi3   exactly.
```

**CONFIRMED, coefficient for coefficient**, against my blind §3.3.

Branch identities, all verified exactly (`II` = adjoined `i`, reduced mod `II^2+1`):

```text
t [Phi4] - s [Phi3] == 2 (s^2 + 64 t^2) X Y
[Phi3] |_{s=8it}   == -t (Y + 8iX)^2       [Phi4] |_{s=8it} == 8i [Phi3]|_{s=8it}
conjugate s=-8it   == -t (Y - 8iX)^2       (computed, not inferred)
```

Hence `V(Phi3,Phi4) = {X=Y=0} ∪ {s=t=0} ∪ {s=8it, Y=-8iX} ∪ {s=-8it, Y=+8iX}`,
exhaustively. The self-similar branch `X=Y=0` inside `W4` is **exactly `Pi`
again**, with `(s',t') = (w2, 8w1)` — verified by direct substitution.

**Second exact method (item 6), independent of the case split.** Treat `Phi4b`,
`Phi3b` as binary quadratics in `(X:Y)` with coefficients `(64s,128t,-s)` and
`(64t,-2s,-t)`. Their resultant is

```text
Res_{(X:Y)}(Phi4b, Phi3b) = -256 (s^2 + 64 t^2)^2 .
```

Neither form is identically zero unless `s=t=0`, so for `(s,t) ≠ (0,0)` a common
projective root exists **iff** `s^2+64t^2 = 0`. This derives the trichotomy
directly and replaces my blind report's `XY = 0` case split with a cleaner
argument. It also **explains** Sol's binary-square law: `B ± 8iA = (s ± 8it)^2`
and `s = ±8it` are the isotropic directions of the same quadratic form.

**Conjugate branch: I did not rely on the Galois argument.** My blind §3.4 argues
that `Q`-conjugation settles the second branch. That argument is sound (any
automorphism of `Q(i)` extends to an algebraically closed overfield, and all
atlas coefficients are rational), but it is avoidable, so I computed the
`s = -8it` branch directly. Both branches behave identically.

### 2.4 Item 4 — exclusion of every nonzero `(s,t)` on `D(k10_0)`, and the witness

*Self-similar branch `X=Y=0`.* The `v`-part vanishes identically and every
`k10_0`-free part is zero; the surviving conditions are, up to exact scale,

```text
k10_0 * t (3 s^2 - 64 t^2) = 0        k10_0 * s (s^2 - 192 t^2) = 0
```

With `k10_0 ≠ 0`: `t=0 ⟹ s^3=0`; `t≠0 ⟹ 3s^2=64t^2`, then `s=0` gives `64t^2=0`
and `s^2=192t^2` gives `512t^2=0`, both contradictions. So `s=t=0`.

*Branches `s=±8it`, `t≠0`.* Rows 3,4,5,6,7 vanish identically. The `2×6`
`v`-coefficient matrix of rows 1,2 has **rank one** (all 15 minors vanish
identically, both branches). The polynomial left-kernel vector `λ` gives
`λ·n ≡ 0` and `λ·b = ±(15/16384) i t^3 X`, so `k10_0 ≠ 0` forces `X = 0`, hence
`Y = ∓8i·0 = 0`. Substituting `X=Y=0` and `s=±8it` into the seven rows leaves

```text
row1: k10_0 * (-5/16) t^3      row2: k10_0 * (∓5/32) i t^3     row3: k10_0*(5/128)t^3
```

so `t^3 = 0`, contradicting `t ≠ 0`. **Both branches empty.** All four branches
are therefore excluded except `s=t=0`. **CONFIRMED.**

**Repair R-2 (normalization).** My blind §3.5 reports "the surviving `k10_0`
coefficient is `-(15/16384) i t^3 X`". `λ` is defined only up to scale, so the
sign and the constant are **normalization artifacts** — with my `λ` I get `+`. The
invariant content is the zero locus `{X t^3 = 0}`. Reporting a specific
coefficient as if it were invariant is a typing slip; it does not affect the
conclusion.

*Witness above `(s,t)=(0,0)`.* Substituted into the **literal** atlas rows, no
ideal machinery:

```text
d*_1 = 0,  d*_2 = (4,1,1,0,0,-16),  d*_3 = d*_4 = d*_5 = 0,
k10_0 = 1 (nonzero),  k10_1 = k10_2 = 0
   grades 0,1,2,3,4,5 : 7/7 rows vanish at every grade.   RA = RB = 0.
Negative control: d0_2 4 -> 5 (so RB = 1) leaves 1/7 grade-four rows vanishing.
```

**CONFIRMED.**

### 2.5 Item 5 — the precise theorem is a *projection* statement (Repair R-1)

My blind §3.6 states: "the literal grade-five compatible locus is exactly
`{s=t=0}`, i.e. `d*_1 = 0`." **This is false as a statement about the locus** and
is the one substantive repair. Over `(s,t)=(0,0)` the seven rows do **not** all
vanish. Setting `s=t=0` and writing `RA(v) := 16v1-4v3+v5`,
`RB(v) := v0-4v2+2v4` (the *same two forms* that cut grade four, now on the
`d*_3` block), the entire grade-five content is

```text
row 1 = (3/1024)  [  X RB(v) +   Y RA(v) ]          rows 3,5,7 = (-1/8, -1/128,
row 2 = (3/16384) [  Y RB(v) - 64 X RA(v) ]                      -1/1024) x row 1
rows 4, 6 vanish identically;  k10_0 does not occur in any row.

        [  X    Y ] [ RB(v) ]   [0]
        [  Y  -64X] [ RA(v) ] = [0],     det = -(64 X^2 + Y^2).
```

So the fibre is a **positive-dimensional** variety, not a point, and `k10_0` is
entirely free there (the open condition costs nothing over the origin). Free
coordinates over the origin are `w1,w2,X,Y` (4), `v` (6), `k` on `G_m` (1) = 11;
each of the three strata — `det ≠ 0` (two conditions), `Y = ±8iX ≠ 0` (rank one),
`X=Y=0` (no condition) — has **dimension 9**. Grade four had dimension 13.

> **Corrected theorem (G5-COLLAPSE).** Over an algebraically closed field of
> characteristic zero, let `d*_1` range over the promoted rank-zero plane `Pi`,
> impose the reduced grade-four condition `RA = RB = 0`, and impose
> `k10_0 ≠ 0`. Then the **image of the grade-five compatible locus under
> projection to the leading two-plane** `(s,t)` is the single point `(0,0)`,
> i.e. `d*_1 = 0`. The locus itself is nonempty of dimension 9, cut over the
> origin by the displayed `2×2` kernel condition on `(RB(v), RA(v))`. Grade five
> removes both parameters of the plane and drops the dimension `13 → 9`.

This is stronger and more informative than the blind statement, and it is the
form the packet asked for.

### 2.6 Item 6 — ideal/radical/dimension and mutation controls

I make **no ideal-theoretic claim**; §1 shows none is needed for this question,
and the parametrization of §2.3 is bijective so no point is missed. Mutation
battery, all fail-closed:

```text
                          g3 vanish   d*_4 drops   affine in (v,k0)
BASE (2s,t/8,s,t,s,2t)      7/7          yes             yes
d1_1  t/8 -> t/7            0/7          NO              yes
d5_1  2t  -> 3t             0/7          NO              yes
d4_1  s   -> 2s             0/7          NO              yes
d0_1  2s  -> s              1/7          NO              yes
mu    16t^2 -> 15t^2        breaks 6/7 grade-four rows
```

**A finding that corrects my own blind §8.** "Affine in `(v,k0)`" survives every
plane mutation, and the **raw** (pre-substitution) degree of grades five and six
in their own newest block is `1` for all seven rows at both grades. So
linearity-in-the-newest-block is a **structural property of the atlas
construction**, not a discovery about `Pi`. My blind §8 proposed a
"linear-in-the-newest-block prescreen" whose trigger is therefore satisfied
generically and carries no routing information. What actually collapsed the gate
is the *vanishing* of the newest block on `Pi` (§4, Law N), which pushes the
affine structure down one level. **Repair R-5:** the prescreen must test
vanishing, not degree.

### 2.7 Disposition

```text
G5-COLLAPSE : PASS_WITH_REPAIR
  R-1  the theorem is a projection statement; the locus is dim 9, not a point
  R-2  the branch-2 k10_0 coefficient is lambda-normalization dependent
  R-3  "total degree 1" -> "degree <= 1" (row 6 is 0, row 4 has no k10_0)
  R-4  the K00-SHIFT-LADDER mechanism reading is withdrawn (see section 4)
  R-5  the newest-block prescreen must test vanishing, not degree
  every load-bearing computation of the blind report reproduces exactly
```

**Caveat on evidential weight.** This is an Opus-5 reconstruction of an Opus-5
blind result. It is a from-bytes rebuild under a fresh ring map and it found five
repairs, but it is **not** a different-model replay and must not be counted as
one. The owed different-model review is Launch L1.

---

## 3. Source typing — the collapse kills the valuation-one seed

The packet asks whether a confirmed collapse kills the complete normalized
valuation-one, `C6=1`, `k10_0 ≠ 0` seed at grade five. **It does.** My blind §3.8
refused to guess; the frozen record decides it, in three steps.

**(a) `d*_1` is the leading coefficient block — from the atlas's own grading.**
Assign `weight(d_i_j) = j` and `weight(k10_c) = c+2`. Every monomial of every
literal grade-`g` row has weight exactly `g`, at `g = 2,...,6` (checked: g=4
shapes `D1^4, D1^2D2, D2^2, D1D3, D1^2k0`; g=5 adds `D1D4, D1^2k1, D2D3, …`; g=6
adds `D1D5, D1^2k2, D2^3, D3^2, D2D4, …`). That is exactly the grading induced by
`d_i = Σ_j d_i_j Λ^j`, `k10 = Σ_c k10_c Λ^c`. Hence `d*_1 = x` and
`k10_0 = kappa` in the reviewed ansatz `d_i = Λ x_i + O(Λ^2)`,
`k10 = kappa + O(Λ)`, `kappa ≠ 0`.

**(b) The promoted record already asserts the same identification.** The
coordinator integration works over `R = Q[d0_1,...,d5_1]`, calls it "the leading
base", and forms `B = B2 + (F10)` — summing the six nonzero **atlas grade-two
rows** with the V22 quartic `F10` into one ideal in one ring. That sum is
well-formed only if the V22 `x`-variables and the atlas `d*_1` are the same six
variables. This is a citation, not an analogy.

**(c) `x = 0` is not a valuation-one point.** Under the ansatz, `x = 0` forces
`v_Λ(d) ≥ 2`. It is a triviality, and the reviewed V22R1 record types it exactly
that way: its allowed producer outcomes were
`M1_STRATUM_EMPTY_FORCES_HIGHER_VALUATION` and `M1_STRATUM_NONEMPTY_REMAINS`,
with the reviewer's own note that the first "would have been the correct
recording if `L` had been the unit ideal **or of affine dimension 0**". A
homogeneous leading stratum of affine dimension 0 is precisely `{x=0}`.

> **Source-scope consequence.** Composing the promoted grade-three incidence
> `V(B, P3_1..P3_7) = Pi × A^6_u` with the corrected G5-COLLAPSE: on the
> normalized valuation-one, `C6=1`, `k10_0 ≠ 0` K00 seed, over the promoted
> leading base `V(B)`, the grade-five compatible locus of **leading
> coefficients** is `{x = 0}` — empty as a valuation-one stratum. The seed is
> **dead at grade five** and forces higher valuation.

**Explicit non-claims.** This kills one seed, not K00 and not JC2. Other
coefficient valuations are untouched (a re-graded valuation-two ansatz is a
*different* seed whose rows are not the frozen atlas rows). Finite jets, arcs,
polynomial maps, source reachability, order two, maximum twelve, and JC2 are all
outside the claim. The chain consumes two promoted/reviewed inputs — the
coordinator incidence and V22R1's `F10` exclusion, which is what defines `B`; if
either is later repaired, the composition must be re-derived.

**One labelling discrepancy, logged, not load-bearing.** V22R1's
`T = (Q1,...,Q6)` has five nonzero generators (`Q6 = 0`), while the coordinator's
`B2` has six nonzero generators (atlas rows `1,2,3,4,5,7`); the coordinator
explicitly warns about this naming clash. So `V(B)` is contained in — possibly
strictly — V22R1's affine-dimension-3 stratum. That only tightens the scope and
does not affect (a)–(c).

**This answers my blind Card B.** `d*_1 = 0` is excluded upstream, so by my own
blind §4 the correct move is to lower Avenue 36 **hard on this seed** rather than
conditionally. Card B is closed, not open.

---

## 4. Shift / renormalization — one law, two grades, and three refuted towers

Verified facts, separated from any tower theorem.

**Law N — newest-block law (RAW, grade-independent).** With
`C_{r,j}(d*_1) := coeff(d_j_2, Lambda_{3,r})`:

```text
coeff( d_j_{g-1}, Lambda_{g,r} ) == C_{r,j}(d*_1)     42/42 at g = 3, 4, 5, 6
```

The *same* matrix at every grade. Since grade three vanishes on `Pi` with `u`
free, `C ≡ 0` on `Pi`, so **the newest block dies on `Pi` at every grade,
automatically**. Consequence: the "`d*_4` and `k10_1` disappear at grade five"
census — independently reported by Sol, Fable, Grok and me, and independently
verified by Grok's post-blind review — **is not a grade-five fact**. It is a
one-line corollary of Law N plus the promoted grade-three incidence, and it
predicts the same at grade six. Verified: `d*_5` and `k10_2` disappear from all
seven grade-six rows on `Pi`. The `g=4` instance is Grok's review §5 and is
`KNOWN`; the grade-independence and the `g=5,6` instances are new here.

**Law S — shifted second-newest law (on `Pi`, NEW).**

```text
coeff( d_j_{g-2}, phi(Lambda_{g,r}) ) == C_{r,j}(w)   42/42 at g = 5 and g = 6
raw analogue coeff( d_j_{g-2}, Lambda_{g,r} ) == C    0/42 at g = 5 and g = 6
```

The raw analogue is false, so Law S is genuinely a plane-plus-shift phenomenon
and not a restatement of Law N. This is the packet's authorized grade-six
linear-coefficient test, and it **passes**.

**But there is no tower.** All three proposed tower/functor mechanisms fail:

* **`K00-RENORM` (Fable) — REFUTED.** "grade `g+2` rows on the grade-`g` survivor
  equal grade-`g` rows at polynomially shifted arguments." Tested at `g=4→6`
  with `d*_1→w, d*_2→d*_3, d*_3→d*_4, k10_0→k10_1`: **0/7 rows**. The `g=2→4`
  instance is a genuine full identity; it does not iterate.
* **`K00-POLARIZATION-SHEAR` (Grok) — REFUTED by one row, no search.** The
  even-grade functor asks for `mu_{2m}` with
  `phi(Lambda_{2m,r}) = Q_r(w - mu_{2m})` generatorwise. Literal grade-two row 6
  is the **zero polynomial**, so `Q_6(z) = 0` for *every* `z`, forcing
  `phi(Lambda_{2m,6}) = 0`. At `g=4` this holds (both sides zero). At `g=6`,
  `phi(Lambda_{6,6})` has **119 terms** and is nonzero. Therefore **no `mu_6`
  whatsoever exists**, for any candidate, and Grok's Card 1 needs no run.
  (Grok's own review flagged the `q6`/row-7 trap; the functor is killed by the
  very row that trap concerns.)
* **`K00-SHIFT-LADDER` (mine) — REFUTED as a ladder.** My blind §6.1 listed the
  `g=2→4` full identity and the `g=3→5` coefficient identity as two instances of
  one "+2 shift". They are not: the second is Law S with the *same* matrix `C`
  that already appears raw at *every* grade, not a shifted copy of grade three.
  The "+2" reading is refuted at `g=4→6`. **Repair R-4:** the mechanism claim is
  withdrawn and replaced by Law N + Law S. My blind Card A's outcome menu
  correctly anticipated "partial covariance"; the outcome is that one.

**Reconciliation: one mechanism, three wrong names.** All three proposals are
attempts to name the same pair of facts. Law N is one grade-independent
coefficient law; Law S is one shifted coefficient law verified at two grades. A
partial match must not be extrapolated, and none of the three tower readings
survives contact with grade six.

**Sol's binary-square coordinates — CONFIRMED and now explained.** `RA = 2st`,
`RB = s^2-64t^2`, `B + 8iA = (s+8it)^2` reproduce exactly, and §2.3 shows why
they matter: `s^2+64t^2` is the resultant of the two grade-five residuals, so the
square law's isotropic directions **are** the two exceptional branches. Sol's
item 3 and my ID2/ID3 are independent convergence on one structure.

This also disposes of my blind §6.4. The `s = ±8it` occurrence has a complete
internal explanation and carries **no** cross-lane content; the refusal to link it
to `TWIN-ORDER`'s `(4+3i)/5` or the U1 sibling's `(9±3i)/8` was correct, and now
has a reason rather than only a caution.

**Does grade six remain useful?** On `Pi`, grade six is affine in `(d*_4, k10_1)`
and **quadratic** in `(d*_3, k10_0)` (degrees 2,2,2,2,2,1,2), with its own newest
block dead by Law N. But by §3 the valuation-one seed is already dead at grade
five, so **grade-six work on `Pi` has no client**. A higher-valuation seed would
be re-graded and its rows would not be these rows. **Stop grade six on `Pi`.**

---

## 5. TD12 — first resonance, the S route, and the two proof-side proposals

### 5.1 Route-generality of the first-resonance collapse

`MST-4` of the reviewed B25 report is universal in `(nu, kbar, i)` for
`0 < kbar < nu`, `D = nu·i`: the two row coefficients `(D-a)` and `(D+j-kbar-a)`
coincide iff `j = kbar`, and there `R_kbar = -S_kbar'` identically. Independent
exact control (`Fraction`, random rational tails, no CAS):

```text
(nu,kbar,i)   j=kbar   j=kbar-1  j=kbar+1  j=kbar+nu
(25,17,2)     True     False     False     False
(17,13,2)     True     False     False     False
(17,13,4)     True     False     False     False
(11, 7,3)     True     False     False     False
```

The collapse is pinned to `j = kbar` and is independent of `nu`, `i`, and `D`.

> **CONDITIONAL COROLLARY (S13-VACUOUS).** For the sibling
> `(nu, kbar, D) = (17, 13, 17i)`: **if** the S route's terminal reduced-deviation
> recurrence has the same graded rows `(ROW_j)` **and** the same landing
> `ord_top(Dev_S) = kbar_S - D_S`, then `j = 13` is the unique
> total-derivative row, `R_13 = -S_13'` identically, both orbit residues vanish
> at every point of `P^1`, and row 13 is unconditionally solvable with a
> one-dimensional gauge `C_13 p^(-i)`.

The two hypotheses are exactly the **still-unreviewed S landing/deviation
bridge**. They are not established here and I do not assume them. The corollary
is conditional; the S bridge's mathematical status is `PASS_WITH_MATERIAL_REPAIRS`
with custody `FAIL_PRODUCER_BODY_SEAL`.

**Consequence for Fable's Card A — ANSWERED, not to be run.** Card A's whole
content is the residue `c = kbar_S mod 17`; with `kbar_S = 13` the residue is
nonzero, so Card A's outcome is **(iii)**, vacuous by exact derivative. And the
"structural vacuity lemma" Fable proposes to *formulate* in that branch is
already **proved** as MST-4, in far greater generality. Fable's hoped-for outcome
(ii) — a live window-internal constraint on S, "the first non-source-gated Keller
bite at td12" — is unavailable under the conditional typing. The correct
descendant is not an experiment but a **typing check** (Launch L2).

**No cheaper S landing target.** The S analogue of `j = 42` is `j = 13+17 = 30`,
with the same MST-7 closed form `Res(p^m R_j) = m·[Res(p^{m-1}p'S_j) - nu
Res(p^m U_j)]` and the same unpinned resonant gauge `C_13`. So S inherits B's
blocker structure exactly: first resonance vacuous, second needing source values
**and** an unpinned constant.

**Index discipline.** The vacuity itself is index-free — MST-4 uses only `j=kbar`
and the product rule, never the window. The claim "the window contains exactly
one resonance row" *does* need the `P_a` ↔ window-depth map, which
`OPEN(WINDOW-INDEX-B25)` records as untyped; that OPEN applies to the S route
verbatim. For B `j=42` the consumption list must include `C_17` (repair R-A):
rows 18..41 are affine in `C_17`, so the two residues are two affine conditions
in **one unpinned constant**, leaving at most one net condition after
elimination.

### 5.2 `TD12-GA-TRANSLATION-WARD` (Sol) — gauge tangent identity, not transgression

The card is **self-defeating at its own dependencies**. Sol charges "a correctly
sealed/reviewed source-translation theorem" — and the stronger that theorem is,
the more completely it kills the card. If `tau_c` preserves the Jacobian,
normalized type, degree minimality, infinity tree and S17 cell, then **any**
terminal condition that is a function of those data is `c`-independent by
construction. `tau_c` is a one-parameter unipotent action with generator
`∂_x`; "the condition holds for every `c`" is then the *definition* of
invariance, and `d/dc Φ(tau_c F)|_{c=0} = 0` is the tangent identity of the
orbit — a syzygy, not a constraint. Sol's own stop condition ("every coefficient
reducing to the existing recurrence proves that the orbit is merely equivariant
gauge") is already met by the invariance theorem the card depends on.

**The one escape, and its precise missing premise.** If the terminal condition is
stated on a *representative* (a specific chart with specific `P_a`) rather than on
the type, then `Φ(tau_c F) = 0` for all `c` is a polynomial identity in `c` whose
coefficients are relations among the `P_a`. But those relations are exactly the
induced triangular unipotent **transformation law** of the `P_a`, recovered, not
a new constraint. Content requires:

```text
MISSING PREMISE (GA-WARD):  a proof that the c-degree of the transported
terminal functional strictly exceeds the number of free parameters of the
induced action on the finite packet.
```

Without it no contradiction follows, at any `c`. **Cheapest exact discriminator:**
one derivative — compute `d/dc` of the endpoint functional at `c=0` and test
whether it lies in the span of the induced action's generators. No coefficient
emission, no `P_k`. If it does (expected), stop the card.

### 5.3 `TD12-ROW-PROPORTIONALITY` (mine) — REFUTED, interface absent

The packet asks whether td12 rows at different grades are even maps with a common
typed unknown block. **They are not**, and my own blind Card C fails its first
typing check.

K00 worked because seven rows at **one** grade share **one** unknown block
`(v0..v5, k10_0)` and are affine in it, so coefficient vectors live in a common
`Q`-vector space and proportionality is meaningful. The td12 cascade is
structurally different: row `j` is `i λ_f p^{i-1} L_j[T_j] = R_j`, where

1. the genuinely new unknown of row `j` is the **single function** `T_j`, so the
   "coefficient vector in the unknown block" is a 1-vector and any two are
   trivially proportional — the test is **vacuous**;
2. the only block genuinely shared across rows is the source values `(P_1, P_2,
   …)`, and rows are **not linear** in them: `R_j` contains products
   `P_a T_{j-a}` where `T_{j-a}` is itself built from `P_1..P_{j-a}`, so the
   degree grows with `j`.

Proportionality of coefficient vectors is therefore not definable without first
linearizing, and the packet's instruction applies: **stop the idea, its claimed
interface is absent.** My blind §6.2's claim that this "attacks bottleneck #4
without first solving bottleneck #2" is withdrawn.

**Salvage.** The one place a shared unknown block does exist is the *two*
deck-orbit residues at a *single* row. There the count is already fully known: at
`j = kbar` both are identically zero (MST-5); at `j = kbar + nu·m` they are two
affine conditions in one unpinned gauge constant, hence at most one net
condition (R-A). Nothing remains for a proportionality search to find.

### 5.4 `TD12-U1-ACTUAL-LANDING` versus further local-row work

**It should outrank local-row work**, on four grounds:

1. every local-row lane is now answered or blocked — `j=17` vacuous (reviewed),
   `j=13` vacuous (conditional, §5.1), `j=42`/`j=30` blocked four ways,
   homogeneous windows transparent, row-proportionality interface absent (§5.3),
   translation-Ward gauge-only (§5.2);
2. all four blind reports independently rank occurrence/coverage as bottleneck
   #1, and this lemma is the narrowest statement that would convert the promoted
   local kills into a coverage step;
3. it assumes an actual equality record rather than constructing one, so it does
   not require the serialized `PairRef` that blocks bottleneck #2;
4. it is desk-theoretical: no source values are needed to *state* it.

**But it is not free of the cofinality wall.** "Every actual continuation meets a
reviewed contradiction **or a named** B25/S17 occurrence" quantifies over
continuations and needs a finite/cofinal type menu — Grok's bottleneck 6, Sol's
bottleneck 4. The lemma relocates that cost into the word "named". It is the
right *place* to pay it, not a way to avoid it, and it must be launched with that
stated rather than discovered later.

---

## 6. Systems — the smallest nonduplicative `CAPRUN/v1`

All four blind reports independently select one repo-owned wait-authoritative
capped runner. That is four-way convergence on need, and `DUPLICATE ×4` on
content: one file plus fixtures, **no `ops/lane.sh` migration in this wave**.

**Measured correction to the shared feature list — all four reports overclaim
memory caps.** Sol, Fable, Grok and I each write "wall/CPU/RSS caps" as if all
three were enforceable. Probed on the campaign desk host (Darwin 23.6.0, arm64,
CPython 3.9.6), by two independent routes:

```text
RLIMIT_CPU  (1,1) on a spinning child       -> rc = -24  SIGXCPU     ENFORCED
RLIMIT_AS   (200MB, RLIM_INFINITY)          -> ValueError            REFUSED
RLIMIT_AS   (200MB, 200MB)                  -> ValueError            REFUSED
RLIMIT_RSS  (50MB, 50MB)                    -> ValueError            REFUSED
bash `ulimit -v 204800`                     -> setrlimit failed      REFUSED
```

This is the same behaviour Grok's own post-blind review disclosed ("Darwin
refused `RLIMIT_AS` … RSS polled via `ps`"), now measured rather than incidental,
and `RLIMIT_RSS` is additionally a no-op on modern Linux kernels. Under the
packet's rule — *reject features whose portable correctness cannot be tested* —
the v1 contract must be:

```text
CPU  : RLIMIT_CPU, authoritative, but PER-PROCESS not per-group.
       A forking child multiplies the budget. Declare this; do not
       advertise a group CPU cap.
WALL : Popen.wait(timeout) authoritative for status; NOT a reaper.
MEM  : TELEMETRY ONLY + best-effort supervisor poll-and-kill, typed
       rss_cap_enforced=false when setrlimit refuses. NEVER called a cap.
```

Verified-available primitives (all testable, all keep): `start_new_session` with
`pgid == pid`; `os.getpgid`; start identity via `ps -o lstart=` (Darwin) /
`/proc/PID/stat` field 22 (Linux); `os.killpg` with confirmed `rc = -15`.

**Retained from the blind reports, deduplicated:** argv-only; stdin `DEVNULL`
unless an explicit regular `--stdin-file`; generated Singular scripts end with
`quit;`; PID/PGID/start-identity revalidated **before** signalling (PID reuse);
TERM to the exact validated PGID, bounded grace, KILL to the same PGID, one
authoritative reap; typed outcome distinguishing normal exit / timeout / CPU cap
/ signal / runner failure; output hashes computed **after** reap; no `pkill`, no
name matching, no bare `kill -0` completion loop.

**My one non-duplicative addition, with measured evidence.** Telemetry must go to
a **separate file descriptor, not stderr**. In my blind session
`/usr/bin/time -l python3 K00G5.py > out 2> timing` produced an empty stdout and
a normal-looking timing block while the real `FileNotFoundError` sat inside the
timing file — a caller checking "stdout produced, resource block present" scores
a hard failure as a quiet success. Same failure class as the incident, one layer
up, one design line to prevent.

**Fixture matrix (union of all four, deduplicated, plus two new):**

```text
1  clean exit 0, output on stdout        -> status 0, telemetry on fd 3 only
2  nonzero exit, empty stdout            -> not reported clean
3  child writes stderr then exits 0      -> stderr preserved, not merged with fd 3
4  child holds stdin open (the incident) -> exits < 2 s, full stdout, no orphan
5  child ignores TERM                    -> TERM to exact PGID, grace, then KILL
6  child forks a grandchild outliving it -> whole PGID reaped, none survives
7  same-name decoy outside the PGID      -> survives untouched (no name matching)
8  child exits before the first poll     -> true exit status (wait authority)
9  CPU cap on a spinning child           -> typed cpu-cap verdict, cap in telemetry
10 grep fixture: `kill -0` in the source -> FAILS the build   [Grok's, keep]
11 NEW: on a host refusing setrlimit(AS/RSS), the runner emits
   rss_cap_enforced=false and does NOT claim enforcement
12 NEW: telemetry fd is closed and flushed before the outcome is typed
```

Acceptance: 12/12 deterministic on Darwin **and** one Linux host, ordinary and
`-O`, byte-identical logs modulo declared time/PID fields. Failure of any fixture
fails the card closed with the fixture retained. No mathematical scheduling
penalty; nothing live is touched.

---

## 7. Deduplicated novelty table

| Item | Owner(s) | Label | Basis |
|---|---|---|---|
| `sqrt(I+J) = sqrt(sqrt(I)+J)` radical-first scheduling | Sol | **NEW / CONFIRMED**, sharpened | §1: unit/proper agrees **both** directions, so the scheme run is redundant for branch-kill too |
| Binary-square / Veronese coordinates `B±8iA=(s±8it)^2` | Sol | **NEW / CONFIRMED**; **DUPLICATE-CONVERGENT** with Opus ID2/ID3 | §2.3; independent convergence preserved — the square law's isotropic directions *are* the two exceptional branches |
| G5 affine normal form `M5 v + k b5 + c5` | Sol (predicted) | **CONFIRMED** | §2.1, degree ≤ 1 |
| `K00-RENORM` period-two tower | Fable | **REFUTED** | §4, `g=4→6` full shift identity 0/7 |
| `K00-POLARIZATION-SHEAR` even-grade functor | Grok | **REFUTED** (one row, no search) | §4, `Q_6 ≡ 0` vs `phi(Λ_{6,6})` 119 terms |
| `K00-SHIFT-LADDER` as a ladder | Opus (mine) | **REFUTED** | §4; survives only as Law N + Law S |
| Law N — newest-block coefficient law, grade-independent | — | `g=4` **KNOWN** (Grok review §5); grade-independence + `g=5,6` **NEW** | §4, 42/42 at g=3,4,5,6 |
| Law S — shifted second-newest coefficient law on `Pi` | — | **NEW** | §4, 42/42 at g=5,6; raw analogue 0/42 |
| "`d*_4`/`k10_1` disappear at grade five" | Sol, Fable, Grok, Opus + Grok review | **KNOWN, and demoted** | §4: a corollary of Law N, not a grade-five fact; predicts `d*_5`/`k10_2` at g=6 (verified) |
| Origin-fibre closed form (2×2 kernel on `(RB(v),RA(v))`) | — | **NEW** | §2.5 |
| `G5-COLLAPSE` | Opus | **PASS_WITH_REPAIR** | §2 |
| `d*_1 = 0` admissibility (blind Card B) | Opus | **ANSWERED** — excluded upstream | §3 |
| `K00-G5-THICKENING-FITTING` | Grok | **SCOPE-CONFLICT** on unit/proper (radical decides both); survives as a multiplicity/Fitting question, now clientless | §1.4, §3 |
| `K00-G5-STAGED-DECISION` | Fable | staging **CONFIRMED**; one outcome branch **REFUTED** (impossible) | §1.4 |
| `TD12-S-RESONANCE-PLACEMENT` | Fable | **ANSWERED** as outcome (iii), conditional; not an experiment | §5.1 |
| "structural vacuity lemma" to be formulated | Fable | **DUPLICATE** — already proved as MST-4 | §5.1 |
| `TD12-GA-TRANSLATION-WARD` | Sol | **REFUTED at promoted scope** (gauge tangent identity); one named missing premise | §5.2 |
| `TD12-ROW-PROPORTIONALITY` | Opus (mine) | **REFUTED — interface absent** | §5.3 |
| `TD12-HERMITE-TRANSGRESSION-SHAPE` | Grok | **KNOWN-OPEN**, untouched; now the only proof-side local card with a declared interface, and subordinate to occurrence | — |
| Gaussian-integer cross-lane pattern | Opus §6.4 | **REFUTED as a connection**, correctly declined, now with a reason | §4 |
| `CAPRUN/v1` wait-authoritative runner | Sol, Fable, Grok, Opus | **DUPLICATE ×4**, convergent; **corrected** on memory caps | §6 |
| "wall/CPU/**RSS** caps" as three caps | all four | **REFUTED** (measured) | §6 |

---

## 8. Launches — three mathematical, one systems

**L1 — `K00-G5-COLLAPSE` different-model hostile review and concurrent-lane
adjudication.** *Falsification; promotion gate.*
Owner: Grok 4.6 or Fable 5 (**not** Opus — §2.7). Reviewer: the other.
Desk (proved sub-second; no AWS, no Groebner). Depends on: this report's §2
corrections R-1…R-5 in the prompt; the concurrently owned
`k00-grade5-rank0-plane-twoinput-primary-fable5` sealed report once it exists;
Grok's grade-four `PASS_WITH_REPAIR` (already closed).
Both outcomes: *reproduces* → promote the corrected projection theorem and §3's
source-scope consequence, then lower Avenue 36 hard on the valuation-one seed;
*disagrees* → adjudicate this report against the owned lane, and treat neither as
evidence until reconciled. Agreement is evidence about a computation, never proof.
Stop: one review. Do not extend to grade six (§4).

**L2 — `TD12-S13-VACUITY` typing check.** *Falsification of a proposal; closes a
card without running it.*
Owner: Fable 5 (owns Card A). Reviewer: Sol 5.6 (owns the S bridge). Desk,
reading only, no coefficient emission.
Question: does the S route's terminal reduced-deviation recurrence have (i) the
graded rows `(ROW_j)` with coefficients `(D-a)` and `-(kbar-D-j+a)`, and (ii)
landing `ord_top(Dev_S) = kbar_S - D_S`? Nothing else is needed.
Both outcomes: *yes* → MST-4 applies verbatim, `j=13` is vacuous, Card A is
closed as outcome (iii), and the two-route structural vacuity is a theorem;
*no* → the B/S asymmetry is itself the datum, and it is a finding for the
in-flight S reconstruction. Stop: one typing verdict, or typed `OPEN` if the S
bridge's reseal has not landed. Do **not** launch `j=30`.

**L3 — `TD12-U1-ACTUAL-LANDING` typed statement.** *Proof side; the packet's named
narrow lemma.*
Owner: Sol 5.6. Reviewer: Grok 4.6. Desk-theoretical; no `PairRef`, no source
values, no AWS. Must be launched with the cofinality dependency stated up front
(§5.4): the dichotomy quantifies over continuations and needs a finite/cofinal
type menu, which it relocates rather than removes.
Both outcomes: *the dichotomy is derivable* → the promoted local kills become a
coverage step and bottleneck #1 moves for the first time in several rounds;
*it is not* → the obstruction is isolated to the type menu, which is itself the
first sharp statement of that wall. Stop: one verdict or typed `OPEN`. Two
non-informative attempts on the same representation force a redesign per
`COORDINATION`.

**S1 — `CAPRUN/v1`.** *Exactly one bounded systems trial.*
Owner: whoever holds the systems slot. One new file plus the twelve fixtures of
§6. No `ops/lane.sh` migration, no D43 script mutation, no `FALLACY-v2` /
`ROUNDVIEW` churn. Acceptance 12/12 on Darwin and one Linux host, ordinary and
`-O`. Both outcomes: *pass* → the nine bare loops migrate later as a separate
reviewed task; *fail* → fails closed with the fixture retained, and in particular
fixture 11 failing means the memory-cap claim must be deleted from the contract,
not weakened. Blocks nothing; runs beside research.

---

## 9. Stop and defer

**Stop.** Grade six on `Pi` (no valuation-one client, §3–§4). The three tower
mechanisms `K00-RENORM`, `K00-POLARIZATION-SHEAR`, `K00-SHIFT-LADDER` (all
refuted, §4). `TD12-ROW-PROPORTIONALITY` — my own card, interface absent (§5.3).
`TD12-S-RESONANCE-PLACEMENT` as an experiment (answered; replaced by L2).
`TD12-GA-TRANSLATION-WARD` unless the `c`-degree premise of §5.2 is supplied.
Any `j=42` or `j=30` lane. The scheme-input G5 variant as a *separate unit/proper
run* (§1). Rank-three-through-five K00 charts; homogeneous-window descendants;
`TWIN-ORDER`; LL-1 inventory expansion — unchanged, all four reports agree.

**Defer / bank.** Grok's Fitting-rank thickening comparison — mathematically
legitimate, but §3 removes its client; bank until a re-graded seed exists.
Grok's `TD12-HERMITE-TRANSGRESSION-SHAPE` — the surviving proof-side local card;
keep behind L3. `ROUNDVIEW/v2` index split (my blind §9 secondary) — efficiency,
not correctness; below S1.

**Typed OPEN, not filled.** `OPEN(WINDOW-INDEX-B25)` and its S analogue.
`OPEN(J42-NONVACUITY)` and `OPEN(J30-NONVACUITY)`.
`OPEN(NONRESONANT-EXISTENCE-B25)` and its S analogue. `MISSING PREMISE
(GA-WARD)`. Whether the atlas construction admits a valuation-two re-grading at
all — a source-semantics question, not filled here by cap or analogy.

---

## 10. Synthesis recommendation

The round's real result is not the grade-five collapse; it is that the collapse
now has a **source consequence**. Composing the promoted grade-three incidence,
the reviewed grade-four survivor, and the corrected projection theorem with the
frozen valuation-one ansatz, the normalized valuation-one `C6=1`, `k10_0 ≠ 0`
K00 seed is **dead at grade five** and forces higher valuation. That answers the
question my blind report left open and it is the strongest falsification-side
statement the campaign has. It kills one seed, not K00 and not JC2.

Everything else deflates. All three K00 tower mechanisms are refuted at grade six
— one of them by a single zero row, at no cost. The "newest block disappears"
census that four reports reported independently is a corollary of a
grade-independent coefficient law, not a discovery. On the proof side, three of
the four new local proposals lose their interface: mine has none, Sol's
translation orbit is the tangent identity of the gauge it depends on, and
Fable's S residue is already answered by a theorem in the reviewed record.

So: run L1 to close the K00 seed properly, run L2 to *close* a card rather than
execute it, and move the proof slot to `TD12-U1-ACTUAL-LANDING` (L3) with its
cofinality dependency declared rather than discovered. Stop grade six. Build
`CAPRUN/v1` with memory typed as telemetry, because it measurably is not a cap.

## 11. Nonclaims and resources

Not claimed: any JC2 proof or disproof; any counterexample, Keller pair,
polynomial map, `PairRef`, occurrence, landing, attainment, realization,
coverage, or cofinal type theorem; any degree, support, or `td` bound; any exit
price (`charge_basis` absent by design and by task); any source value `P_k` for
`k ≥ 1`; any statement about coefficient valuations other than one; any promotion.
A finite formal jet is not a polynomial map. `REPRESENTATIVE` is not
`FULL_ACTUAL_EXIT`. The §5.1 corollary is conditional on two unreviewed S
hypotheses and is not a theorem on the S route. Grade-four inputs are consumed at
`PASS_WITH_REPAIR`; the coordinator incidence and V22R1's `F10` exclusion are
consumed as promoted/reviewed.

Engine: CPython 3.9.6, `fractions.Fraction`, stdlib only; no CAS, no Groebner
basis, no modular reduction, no floats. All runs combined: **< 1.2 s CPU, peak
RSS 17.5 MB.** Scratch `/tmp/op5xp/` (not custody; the reconstruction procedure
of §2.0 is the archival substitute).

```text
91005f4d5a66856592243261c8b1c575585a6e4d70a97265c092fe3f0bf64897  lib.py
d867433fff1e8830af0f469968c5143d9a4104480f8186ab39bb6278abcb82e2  extract.py
6e1f97757871075f69bcca95dc3bcd07bff370770f42069f49a520c5c387e1a6  step1.py
2f4ee42c55cbaa06571c95f2dd973164fc0cf616684c5021b974a4fdf5ecfca8  step2.py
3ed70bc4672309f8122a67a1c0c8dc36d702f1a8ed77b3ad9dc2088bfb701a7e  step3.py
bfcfa2e38b0579997cd37fb4af84878338e5e6608fb96802af8001ef9e2f6a86  step4.py
82d00c9836521df9e0a28af4d49e745b4f3d2880be2d277ad533bf1cca960401  step5.py
31e79727393b01629bdebccd45fcb69cd24471c703b3ec98f8486e161cbdc771  step6.py
80862dcfb82619a7969ca3a4b960abad7e9b0c7a0e7e6f30068b2cc47d78f793  step7.py
5b1643196fbc7c3f15d1b55ef162a8864c2f8f0081cb5a15496edfac64d8c3c6  step8.py
b9c5fe1364c10362ad6e27ed15789a841f775d2850c95f8468adfd060c47cefc  step9.py
c6a824f17640977193471f49e62ef3eaeebb5f12ffb6aa92b2e11a78787718ba  step10.py
0eac64db628a16f633a05eb5dc9a2e581d41a02d6b90c0eff9c299a45cb57426  step11b.py
13b52442d6dbf175ff8befbc2e012c1f43550ebd4703ac576dc79debad6f2a2f  step12.py
835513708c3bb820b98ef10e369eccc3b3aec5a112c05564f49f8a5138ebf4d1  sib.py
210dd13a6b2d998822ebcceeaaddbcc3559cef59d158bd5769e936d4faf8b11f  asprobe2.py
70e7d8b9cd455fa0263458dc0fdfa6b3ae0671f56756c9ef005287c673a6cc3f  rssprobe.py
```

`step11.py` (`9d592a74...`) is retained but superseded: its first form applied a
simultaneous substitution that left a stray target variable, which I detected via
the `v`-part diagnostic and corrected in `step11b.py`. Both are listed so the
disclosure is checkable.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `50242`.
- Body SHA-256:
  `5660e085121ba6d490f220ea3b825518fd985372124c758459aad6efa0f83e9a`.
- Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
- Charge basis: absent (no new exit price asserted).
- Disposition: `G5-COLLAPSE = PASS_WITH_REPAIR`; adversarial synthesis input,
  not a promotion.
