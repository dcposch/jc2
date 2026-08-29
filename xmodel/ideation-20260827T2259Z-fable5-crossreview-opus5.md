# Opus 5 hostile cross-review of the sealed Fable 5 `20260827T2259Z` ideation

Reviewer: **Opus 5** (Anthropic), exact model ID `claude-opus-5`, acting as an
independent hostile mathematical reviewer.
Date: 2026-08-27.
Target: `xmodel/ideation-20260827T2259Z-fable5.md`.
Report path: `xmodel/ideation-20260827T2259Z-fable5-crossreview-opus5.md` — the
only file written this session; its SHA-256 is printed to stdout at seal.

---

## 0. Custody, execution, and contamination disclosure

### 0.1 Hashes of every file read (recomputed this session)

```text
8674f511a6a88801818c7ffda5f1fdfa52ac57e871e72757234a5d0a28291240  xmodel/ideation-20260827T2259Z-packet.md
d53c352d1e2bea8ae9c2b6e607c8224897d592718ee7297224d753c3c2814db2  xmodel/ideation-20260827T2259Z-fable5.md
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md
d8a01725bc2730ce49069c96f4287956fb867b64e324ea6828076e19986e6b15  xmodel/ideation-20260827T2255Z-packet.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
5beb555075c662e76f8b86062efdf89b2c3a4dd0eb80ffd52fbf3c38bf130d55  xmodel/ideation-20260827T2137Z-fable-linear-vacuity-hostile-review-sol-ultra.md
8bad7ca04ae9a6f45efde305b208309f528173820250d20dab67d00bc32d73a4  xmodel/ideation-20260827T2137Z-postseal-exact-hostile-review.md
a40e01cd4bbfac5d0f6e2a510da08e0186347e9a20d6d5772bf9c2b8a7e095fb  APPROACHES.md
6e4eac0c500fc08a05ca8d0bc5029ce30fb203a220f6cb1ed318491a200e3afa  AUDIT.md
654c358e7c8760fc93ffeb0cfb0ea4fd62163a338195dccba13db865c2c87038  notes.md
```

Hashed but **not read** (custody verification only):

```text
19b9c190b59ba0e4bd775730498f2edd7ec58d571fe73ac0cb376743537b65d8  COORDINATION.md
0d22e3972eba15547889a883cea588a4fde4f87f58ea3187e1d458a291276686  PROGRESS.md
668d78c96088d168361874733f81d7dee724769a6177a723bd0561e60ad850d0  xmodel/ideation-20260827T2137Z-synthesis-sol.md
b3f3886c7783ce22e060865206a700f0aab356caf6f708f75f355e99b684517a  xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md
```

`git rev-parse HEAD` = `418e413593120d19e15e6546eb50c985f4b1f038` — matches the
packet basis.

### 0.2 **CUSTODY DRIFT — three canonical files no longer match the packet**

Packet section 1 states "These canonical files will not be mutated until all
blind submissions seal."  That is **false as of this session**:

| file | packet value | recomputed now | status |
|---|---|---|---|
| `APPROACHES.md`   | `f9ed44df…` | `a40e01cd…` | **DRIFTED** |
| `AUDIT.md`        | `aee767b1…` | `6e4eac0c…` | **DRIFTED** |
| `COORDINATION.md` | `743d684b…` | `19b9c190…` | **DRIFTED** |
| `PROGRESS.md`     | `0d22e397…` | `0d22e397…` | match |
| `notes.md`        | `654c358e…` | `654c358e…` | match |
| `…2137Z-synthesis-sol.md` | `668d78c9…` | `668d78c9…` | match |
| `…2137Z-opus5-crossreview-fable5.md` | `b3f3886c…` | `b3f3886c…` | match |
| `…2255Z-packet.md` | `d8a01725…` | `d8a01725…` | match |

I did **not** fail closed, because my instructions for this session name three
specific target files (all three matched nothing in the drift set) and license
targeted reads of "exact cited baseline files".  Consequence for the reader:
**where I check a Fable 5 citation against `APPROACHES.md` or `AUDIT.md` and
find agreement, that is evidence; where I were to find disagreement it could be
drift rather than producer error.**  I found no such disagreement — every
`AUDIT.md`/`APPROACHES.md` citation Fable 5 makes is present verbatim in the
drifted files — so no verdict below rests on the ambiguity.  Coordinator should
still re-pin the custody table before crediting any lane in this round.

### 0.3 Execution and boundary disclosure

- `jc2-lean` was never entered, listed, searched, read, built, statused, or
  modified.  No `find`/`grep` traversal left the `jc2` working directory.
- No AWS contact, no live-lane contact, no canonical file edited, no external
  communication, no web access.
- **Local computation was run** (my session has a shell, unlike some prior
  review sessions).  It was small, exact-rational, and pure Python with no CAS:
  Lagrange–Bürmann series to `t^24`, residue extraction, forward-mode dual-number
  Jacobians over `Q`, and a nullspace-based P-recurrence fit.  Total wall time
  under one minute.  Scripts were staged in `/tmp/jc2xr/` and are reproduced
  inline below in enough detail to replay.  Nothing was written outside `/tmp`
  and this report.
- No peer `20260827T2259Z` response was read, listed, globbed, or searched.  I
  did list `xmodel/` (to locate the R7R1 baseline); the listing exposed only
  `2137Z`-era and non-ideation filenames plus this round's packet, and I opened
  no `2259Z` file other than the packet and the assigned target.

### 0.4 Contamination

My harness auto-loads a personal memory index summarising my own prior reviewed
work on this campaign.  Two entries are materially relevant and I flag them
rather than hide them:

1. An entry labelled **"NU-LAW + GATE-PR (2259Z)"** asserting, among other
   things, "rows `m = 4 mod 8` unconditionally dead (period 8, not 4)".  This is
   my own prior-session artifact and may originate in *this* round.  **I did not
   rely on it.**  The period-8 death law appears below as result **R1** with a
   complete four-line proof derived from scratch this session and verified
   numerically in three independent fixtures.  The memory line is therefore
   corroborated, not consumed.  If a peer lane in this round has already banked
   the same statement, R1 is a **DUPLICATE** and should be credited there.
2. Entries recording my earlier R7R1 / R7R2 / torsor-capacity reviews.  Every
   load-bearing fact used below was re-read this session from the hashed files.

Nothing in this report is a face exclusion, endpoint decision, family kill,
Keller-pair statement, landing/cofinality claim, or JC2 result.

---

## 1. Verdict summary

| # | Claim | Verdict |
|---|---|---|
| 1 | `y^8 = F(sy)` is `mu_4`-equivariant; `z = s^4` | **CONFIRMED** (equation), **REPAIRED** (the four-section is *not* derived from it — the family is `mu_8`-equivariant) |
| 2 | Fable 5's class section is the correctly typed fixed-receiver object; no R8 §0 mistyping | **CONFIRMED** (desk identity §2.2) |
| 3 | tower survival ⟺ constancy of the class section | **CONFIRMED but tautological** |
| 4 | constancy ⟺ horizontality / flat GM section of `C_s` | **GAP** — only `flat ⟹ gate`; `C_s` degenerates in `y`-degree 14 → 8 at `s=0` |
| 5 | promoted regular-holonomic closure makes `L_j` Fuchsian | **CONFIRMED at fixed-`C`-point scope**; the "coefficients polynomial in the window slots" half is **GAP** |
| 6 | Card B: invariant-subspace kill | **REFUTED as stated** (logic inverted; background class is `0` on P and on the control); narrow repaired form survives |
| 7 | Card B cheapest discriminator on the `r=1` control | **REFUTED as informative** — receiver is 1-dimensional per character there |
| 8 | Card C displayed form `alpha_F` from R7R1 | **CONFIRMED** — every power, index and subtraction checks (§3.1) |
| 9 | Card C necessity for polynomial `G` | **CONFIRMED WITH REPAIR** (field must be `K(F)(X,s,P,p)`) |
| 10 | Card C "s-order ≥ 23" clause | **REPAIRED — redundant**, automatically satisfiable |
| 11 | Card C decidability | **CONFIRMED in principle**, with an honest cost caveat |
| 12 | Card C implies the tower termwise | **CONFIRMED**, but the required pole-order argument is missing from Fable 5 and is supplied here |
| 13 | Card C converse false-shaped (`-log(1-sX)` control) | **CONFIRMED** |
| 14 | `r=1` control: four punctured lines, residues, all `k_m=1`, maximally nonlinear | **CONFIRMED** and strengthened to a closed form (§4.1) |
| 15 | `r=1` is "the perfect sandbox" | **CONFIRMED for Cards A/C, REFUTED for Card B** |
| 16 | `N0 = k* + B` | **CONFIRMED WITH REPAIR** (`k*` must be the largest *nonnegative* integer root, convention `-1`, not `-infinity`) |
| 17 | "uniformity over a window stratum is constructible" | **REFUTED** — this is exactly R8 §7.2's firewall |
| 18 | avenue 3 raise | **SUPPORTED**, strengthened |
| 19 | avenue 16 raise | **SUPPORTED, modest** (instrument, not mechanism) |
| 20 | avenue 25 reopen | **WEAKLY SUPPORTED** — recommend token allocation, downstream only |
| 21 | avenue 45 reopen | **NOT SUPPORTED** today |
| 22 | §2 attack: "nonlinear carry residues may vanish generically ⟹ tower cuts nothing" | **REFUTED by executed computation** (§5.2) |

Three new exact results produced by this review are in §5 (`R1`, `R2`, `R3`).

---

## 2. Area 1 — `GATE-CARRIER-PF` / `GATE-INV`

### 2.1 The equivariance is real, but the "derived" four-section is not

Fable 5 §7 step 1: "`(y,s) -> (zeta y, zeta^{-1} s)`, `zeta in mu_4`, preserves
the equation … so the family is `mu_4`-equivariant … the natural base variable
is `z = s^4` … the 'four-section' structure, derived rather than postulated."

The invariance is correct.  With `y^8 = sum_{i=0}^{14} F_i(X) s^i y^i` and
`(y,s) -> (lambda y, lambda^{-1}s)`:

```text
LHS -> lambda^8 y^8 ,        RHS -> sum F_i lambda^{-i} s^i lambda^i y^i = RHS.
```

So the equation is invariant **exactly when `lambda^8 = 1`**.  The family's own
symmetry group is `mu_8`, not `mu_4`.  A derivation "from the equivariance of
the family" therefore produces `z' = s^8` and an *eight*-section, not four.

**REPAIR.**  The four-section is postulated by the *receiver*, not derived from
the family.  It comes from `p^4 = H` and R7R1's repair 2 (hashed file, "After
that base change, `q_n^sigma = zeta^(n+2) q_n`"), i.e. from the `mu_4`-Kummer
torsor `V_H` on which the classes live.  Equivalently, from the exact identity

```text
q_n in p^(n+2) A   =>   Q(X,s) = p^2 R(X, p s)        (R in A[[tau]])
```

so that the entire `s`-dependence enters through `tau = p s` and the grading is
by `n+2 mod 4` because `p` is a *fourth* root.  Fable 5 reaches the right
object with the wrong justification.

This is not cosmetic: §5's result `R1` shows the *unconditional* vanishing law
of the tower has period **8**, invisible to the `mu_4` framing.

### 2.2 Fable 5's class section is correctly typed — it is R8's object

R8 §0 warns that "`sum_k H^k q_(b+4k) z^k`" with physical `q` is the wrong
series.  Fable 5 does **not** write that; it writes `c(s) = sum_n [q_n dX] s^n`
in the fixed space `H^1_dR(V_H)` with no `H^k`.  Desk identity:

```text
p^(-m_0) q_(b+4k)  =  p^(-m_0-4k) q_(b+4k) * p^(4k)  =  H^k * c_(b,k),
```

so R8's fixed-receiver class `[H^k c_(b,k) dX] in V_(m_0)` and Fable 5's class
`[q_(b+4k) dX]` in the character block differ by the fixed isomorphism
"multiply by `p^(m_0)`", which carries `V_(m_0)` isomorphically onto the
`zeta^(m_0)`-eigenspace of `H^1_dR(V_H)`.  **They are the same object.**
`GATE-CARRIER-PF` and R8 §3 are typing-compatible.  **CONFIRMED.**

Fable 5 never states the `b -> b+2` shift, but its naming of `[p^2 dX]` as "the
`j = 2` block" is consistent with it (`q_0 = p^2` has character `zeta^2`, i.e.
`n+2` with `n=0`), and R7R1 repair 2 licenses the grading.  No error; a stated
shift would have been better.

One scope item Fable 5 drops: R7R1 repair 2 says the character decomposition "is
literal only after adjoining `mu_4`".  Over the campaign's base field the four
blocks are an exponent grading, not an eigen-decomposition.

### 2.3 "Constancy" is correct and tautological; "flat section" is a GAP

Two separate assertions are bundled in Fable 5 §3 and §7 step 3.

**(a) tower ⟺ constancy.**  `c(s)` takes values in the *fixed* finite-dimensional
space `H^1_dR(V_H)`, so "constant" literally means "all coefficients with
`n >= 1` vanish", which is the gate.  **CONFIRMED, but it is a restatement, not
a mechanism.**  All the content is in whether the coefficient sequence is
finitely controlled — and that is R8's D-finiteness, not the constancy phrasing.

**(b) constancy ⟺ flat section of the Gauss–Manin local system of `C_s`.**
Here is the hostile finding.  Write `Phi_Gamma(s) = int_Gamma Q(X,s) dX` for
`Gamma in H_1(V_H)`.  Termwise, `Phi_Gamma(s) = sum_n (int_Gamma q_n dX) s^n`,
convergent for `|s|` small since `Gamma` is compact in `U`.  The transported
contour `{(X, P(X,s))}` realises `Phi_Gamma(s)` as the pairing of the fixed
algebraic class `[y^2 dX]` on `C_s` with the flat transport of `Gamma`.  So:

```text
gate  <=>  Phi_Gamma constant for all Gamma in H_1(C_0|_U)
      <=>  nabla(sigma) annihilates the transported subspace of H_1(C_s|_U).
```

That is **weaker than `nabla(sigma) = 0`** unless the transported subspace is
everything.  It is not.  Explicitly:

```text
C_0 : y^8 = H^2  has y-degree 8 over the X-line,
C_s : y^8 = sum_{i=0}^{14} F_i s^i y^i  has y-degree 14 whenever F_14 =/= 0.
```

Take the extreme fixture `F = H^2 + F_14 t^14`.  Then `y^8 = H^2 + F_14 s^14 y^14`
and, as `s -> 0`, six of the fourteen roots satisfy `y^6 ~ 1/(F_14 s^14)`, i.e.
`|y| ~ |s|^(-7/3) -> infinity`.  **Six branches escape to infinity at `s=0`;
`b_1(C_s|_U)` jumps and `H_1(C_0|_U) -> H_1(C_s|_U)` is not surjective.**

One sub-worry does dissolve.  `C_0|_U = V_H  disjoint  V_(-H)`, and the gate only
constrains the `V_H` half; but `y = zeta_8 p` is an isomorphism
`V_H -> V_(-H)` under which the other branch's coefficients satisfy
`tilde q_n = zeta_8^(n+2) q_n`, so `[tilde q_n dX] = 0 <=> [q_n dX] = 0`.
Nothing is lost between the two components.  The loss is entirely the six
escaping branches.

**Verdict.**  `flat => gate` is correct; `gate => flat` is **not established**.
`GAP`.  A repaired statement would be: *the gate is flatness of the image of
`sigma` in the quotient of the GM system dual to the transported
`H_1(C_0|_U)`* — and that quotient is not shown to be a local subsystem away
from `z = 0` (for `z =/= 0` the curve is irreducible of `y`-degree 14 and the
component splitting that defines the subspace does not exist).

Fable 5's stated obligation list (§7(i)–(iv)) does **not** contain this one.

### 2.4 Card B's kill is logically inverted — `REFUTED as stated`

Card B: "the monodromy-invariant subspace … equals the span of the trivial
background … If proved on `S`: *no* point of `S` survives the tower except
through the background — a stratum-level kill."

Suppose (granting §2.3's missing direction) survival implies `gamma_j` flat.
Then `gamma_j(z) in Inv_j` for all `z`.  Now read the gate blockwise:

```text
j =/= 2 :  gate forces gamma_j == 0          (rows n>=1 must vanish, and k=0 is such a row)
j  = 2 :   gate forces gamma_2 == [q_0 dX] = [p^2 dX]  (constant).
```

For `j =/= 2` the required value is `0`, and `0 in Inv_j` **always**.  A *small*
invariant subspace is therefore perfectly consistent with survival; proving
`Inv_j = 0` proves nothing.  The **only** direction that kills is

```text
[p^2 dX]  not in  Inv_2   =>   no survivors on the stratum,
```

whose hypothesis is the *negation* of "Inv equals the span of the background".
Card B asserts the non-kill side and calls it a kill.  **REFUTED as stated.**

Worse, the background is the **zero class** on the campaign's own data.  `p^4 = H`
gives `p^2 = +/- sqrt(H)`, and for branch P, `H = (X^4-1)^2`, so
`p^2 = +/-(X^4-1)` is a polynomial and

```text
[p^2 dX] = [(X^4 - 1) dX] = [d(X^5/5 - X)] = 0   in H^1_dR(V_H).
```

Same on the proposed `r=1` controls (`H = X^4` gives `p^2 = X^2`;
`H = X^8` gives `p^2 = X^4`; both exact).  So "span of the trivial background"
is `{0}` and Card B's hypothesis degenerates to `Inv = 0`, the maximally
survival-friendly case.  **REFUTED.**

**Narrow repaired form (offered, not promoted).**  On a stratum where the gate's
flat-section direction can be licensed (§2.3), a proof that the flat continuation
of the class `[q_0 dX]` fails monodromy invariance would kill the stratum.  On
branch P that class is `0`, so this repaired form is *also* vacuous there.  I do
not see a live invariant-subspace kill anywhere in the current geometry.

### 2.5 The indicial discriminator is vacuous on the proposed control

Card B's "cheapest exact discriminator" counts exponent-`0` non-logarithmic
solution slots of `L_j` at `z = 0` and declares a local kill "if that count is
already 1 (background)".  Two independent objections:

1. On the proposed `r = 1` control, `dim V_m = r - 1 + k_m = 0 + 1 = 1` for
   every `m` (§4.1).  The fixed receiver is one-dimensional per character, so
   the count is `1` *by construction*, and the test passes while proving
   nothing.  **The proposed discriminator cannot fail on the proposed control.**
2. After isotypic descent the `z = 0` monodromy of the descended block is
   trivial by construction (the `u^{-b}` twist strips exactly the `mu_4`
   character), so exponent `0` without logarithms is the generic situation at
   `z = 0`, not a discriminating one.  Any genuine local structure at `z = 0`
   comes from the degeneration at infinity of §2.3, which the `mu_4` framing does
   not see.

### 2.6 Regular-holonomic closure ⟹ Fuchsian: confirmed at fixed-`C`-point scope

The AUDIT 21:30Z R7R2 block says exactly what Fable 5 cites:

> "the cyclic modules generated by `P,W` embed as submodules of an algebraic
> `j_+q_+O` object.  Hotta–Takeuchi–Tanisaki Theorem 6.1.5 and closure under
> subquotients then make them regular holonomic. … Algebraic nonproper direct
> image is covered."

**CONFIRMED as cited.**  Since regular holonomicity in the algebraic setting
includes regularity at infinity, any section of the direct image `N_j` on the
`z`-line satisfies an operator with regular singularities at every point of
`P^1` — Fuchsian.  Holonomicity over the Weyl algebra `A_1` gives D-finiteness
of every section, so the *qualitative* half of `GATE-REC` is indeed discharged
by promoted material.  Fable 5's headline claim in §8 stands.

Three scope conditions Fable 5 does not restate, all in the same AUDIT block:

- "**R2 is source-confirmed over `C`**" — this is Fable 5's obligation (i) and it
  is real, not decorative.
- "For a **polynomial client**" — harmless for the carrier, since only `P`
  (hence `Q = P^2`) is needed and `P^8 = F(X,sP)` is algebraic unconditionally.
  It *is* load-bearing for Card C, which does use `W`.
- "**After shrinking `A^2`** so that the normalization … is finite étale" — the
  regularity conclusion holds on a shrunken open; the direct image is still
  regular holonomic, so nothing breaks, but the statement is not "on `A^2`".

**GAP.**  Fable 5 §7 step 4 concludes `L_j` has "coefficients polynomial in `z`
and **in the window slots**".  The cited D-module authority is a fixed-`C`
statement and gives no parametric conclusion.  Polynomial dependence on slots
requires performing the elimination over `K(S)` (R8 §7.2), which carries R8's
explicit warning that a generic operator is not evidence on its exceptional
locus.  Fable 5 asserts more than its authority supplies.

**Correct but worth stating**: Fable 5's claim "irregularity is *not* a possible
failure mode" is right at fixed-`C`-point scope.  It is not a licence for the
symbolic-window scope.

Also a technical slip: "the singular values of the gate family are the roots of
the explicit `y`-discriminant of `y^8 - F(sy)`".  `disc_y(y^8 - F(X,sy))` is a
polynomial in **both** `X` and `s`; the singular `s`-values are where the plane
curve degenerates, i.e. (up to the boundary) the roots of `disc_X` of that
discriminant, together with the escape locus at infinity of §2.3.  **REPAIR.**
Separately, the actual Picard–Fuchs operator lives on the four-section curve `E`
of R8 (2.4), not on `C_s`; its singularities are `E`'s, related to but not equal
to `C_s`'s.

### 2.7 Is any invariant-subspace kill licensed today?

**No.**  Three independent obstructions, any one sufficient: the missing
`gate => flat` direction (§2.3); the inverted kill logic (§2.4); the vanishing
of the background class on branch P and on the control (§2.4).  `GATE-INV`
should not be funded as a kill route.  It may be revisited as instrumentation
*after* Card A produces an actual `L_j`.

---

## 3. Area 2 — `GATE-ALG-PRIM` (Card C)

### 3.1 Derivation from R7R1: every power, index and subtraction checks

R7R1 (hashed `9d35c678…`) gives, for `W = G/P^12`, `Q = P^2 = sum q_n s^n`:

```text
W_X|s = -(s^22/8)(Q + (s/2) Q_s),          w_(n+22)' = -(n+2) q_n / 16.   (R7R1 0.2)
```

Desk check chain:

```text
Q + (s/2)Q_s = sum_n q_n s^n + (1/2) sum_n n q_n s^n = (1/2) sum_n (n+2) q_n s^n
  =>  W_X = -(s^22/16) sum_n (n+2) q_n s^n,
which is  sum_m w_m' s^m  with  w_(n+22)' = -(n+2)q_n/16.               [consistent]

Fable 5's hand identity:  d_s(s^2 Q) = sum_n (n+2) q_n s^(n+1).          [CONFIRMED]
  =>  -(s^21/16) d_s(s^2 Q) = -(s^22/16) sum_n (n+2) q_n s^n = W_X.      [CONFIRMED]

n = 0 term of d_s(s^2 Q) is  2 q_0 s = 2 p^2 s,  since q_0 = p^2.        [CONFIRMED twice:
   from Q(X,0)=P(X,0)^2=p^2, and from (1.1): q_0 = [t^0]F^(1/4) = (H^2)^(1/4) = p^2]

  =>  alpha_F := -(s^21/16)(d_s(s^2 Q) - 2 p^2 s) dX
             =  sum_(m>=23) w_m' s^m dX,      s-order exactly 23.        [CONFIRMED]
```

Every exponent (`s^21`, `s^2`, `s^22`, order `23`), the factor `1/16`, and the
subtracted term `2 p^2 s` are correct.  The subtraction removes precisely row
`m = 22`, the inhomogeneous `D22 = 1` endpoint, which Fable 5 correctly declines
to touch.  **CONFIRMED.**

I also re-verified the two supporting promoted identities in exact arithmetic
(§5.1): `q_n = (2/(n+2))[t^n] F^((n+2)/8)` and
`q_n = (1/4) p^(n-6) F_n + R_n(F_1,…,F_(n-1))`, and R7R1 (0.4)'s
`q_1 = F_1/(4p^5)`, `q_2 = F_2/(4H) - F_1^2/(16H^3)`.  All reproduce.

### 3.2 Necessity for polynomial `G` — CONFIRMED WITH REPAIR

If `G` is polynomial then `W = G(X,sP)/P^12 in K(F)(X,s,P)`.  Since
`K(F)(X,s,P)` is closed under `d_s` and `d_X`, `alpha_F` is an **element of a
fixed finite algebraic extension**, not merely a formal series — the point on
which the whole card depends, and it is right.  A primitive exists:

```text
alpha_F = d_X( W - sum_(m<=22) w_m s^m ) = d_X( sum_(m>=23) w_m s^m ).
```

**REPAIR.**  The truncation's coefficients `w_m` are `s`-Taylor coefficients of
`W` at `s = 0`, hence lie in `K(F)(X)(p)`; `p` is not evidently an element of
`K(F)(X,s,P)`.  The correct ambient field is

```text
E' = K(F)(X, s, P, p),      [E' : K(F)(X,s)] <= 16 D^4   (R8 (2.5), D = 14),
```

which is exactly the adjunction R8 §2.3 already contemplates.  With `E'` in
place, necessity is **CONFIRMED**.  Stated in `K(F)(X,s,P)` alone it is
under-typed.

### 3.3 The "s-order ≥ 23" clause is redundant — REPAIR

Two primitives of `alpha_F` in `E'` differ by a `d_X`-constant, i.e. by an
element of the algebraic closure of `K(F)(s)` in `E'`.  If `V` is any primitive,
then for `m <= 22`, `d_X v_m = 0` (because `alpha_F` has `s`-order `>= 23`), so
each `v_m` is already a constant and `c(s) := -sum_(m<=22) v_m s^m` is available
in `E'`.  Hence

```text
"alpha_F has an X-primitive in E' with s-order >= 23"
    <=>  "alpha_F has an X-primitive in E'".
```

The order clause carries no information.  Dropping it also removes Fable 5's
parenthetical "weight bookkeeping to be pinned at compile time", which is then
unnecessary.

### 3.4 Decidability — CONFIRMED in principle, with a cost caveat

`E'` is an algebraic function field of one variable `X` over the constant field
`k_0` = algebraic closure of `K(F)(s)` in `E'`, and `alpha_F in E' dX`.  Deciding
`int alpha_F in E'` is the classical algebraic-integration decision (Trager
1984): Hermite reduction to at-most-simple poles, then vanishing of all residues
*and* vanishing of the remaining de Rham class.  **Decidable.  CONFIRMED.**

Honest caveat Fable 5 omits: the second half of that test *is* a de Rham
computation on a curve of degree `<= 14` over `K(F)(s)`, requiring factorisation
over that field.  It is finite, but it is not obviously cheaper than the tower it
is meant to replace, and at a symbolic window point `K(F)` is a multivariate
rational function field.  Price it as bounded-but-not-small.

### 3.5 Card C ⟹ the tower termwise — CONFIRMED, with the missing argument supplied

Fable 5 asserts "(b) implies the entire class tower (termwise)" without proof.
The naive argument fails: expanding `alpha_F = d_X V` gives
`q_n = -(16/(n+2)) d_X v_(n+22)` with `v_(n+22)` only in the *fraction field*,
whereas the gate needs a primitive in `O(V_H)`.  R8 (4.3)–(4.4) has the fix and
it transfers verbatim:

```text
q_n dX is regular on V_H;  if v had a pole of order k >= 1 at a point of V_H,
then d_X v would have a pole of order k+1 >= 2 there (char 0);  contradiction.
Hence v in O(V_H) and [q_n dX] = 0.
```

(One also needs the finite-trace descent of R8 (4.4) if the primitive is taken
in a larger field.)  With that supplied: **CONFIRMED.**

### 3.6 The converse is genuinely false-shaped — CONFIRMED

Fable 5's control is correct.  Take `alpha = s dX/(1 - sX)`, a *rational*
differential.  Each coefficient `X^(n-1) s^n dX` has the polynomial primitive
`(X^n/n) s^n`, so it is coefficientwise exact with regular primitives, yet
`int alpha = -log(1 - sX)` is transcendental over `K(X,s)`.  So
"class tower `=>` algebraic assembly" is false in shape.  **CONFIRMED.**  Card C
is a one-way filter and Fable 5 correctly labels it so.

### 3.7 What Card C actually is — and Fable 5 undersells it

Fable 5 frames Card C as "strictly stronger than the class tower".  That framing
buries the operationally important point.  The face problem's hypothesis **is**
`G` polynomial.  Therefore:

> **Card C, correctly stated, replaces an infinite tower of conditions by a
> single finite, exact, decidable de Rham vanishing over a fixed finite
> extension, and it is `G`-free.**

```text
FACE POINT at F  =>  [ alpha_F ] = 0  in  H^1_dR( E' / k_0 ),
alpha_F = -(s^21/16)( d_s(s^2 P^2) - 2 p^2 s ),      E' = K(F)(X,s,P,p).
```

This is precisely the shape the "finite control of the nonlinear gate tower"
bottleneck asks for, it needs neither Card A nor Card B, and its only
dependencies (R7R1, the all-row formula) are promoted.  In my judgement it is
**the single most valuable item in the Fable 5 submission**, and it is the one
the submission argues for least.

**Strictly stronger** remains **unproven**: no example is exhibited where Card C
cuts and the tower does not.  Retain as plausible, not as fact.

### 3.8 The Card C discriminator is ill-posed — GAP

"On the `r=1` control and ~20 random rational window points on P: run the
primitive decision and compare its cut against the class-tower ranks at the same
points."  At a *random* point the tower already fails at row 23 (my §5.3 fixture
dies at `m = 23`), so both conditions fail and nothing is compared.  A cut
comparison is only meaningful on the tower-survivor locus.

**Recommended replacement.**  Use the `r=1` control, where §5.3 gives an explicit
`N0`: construct points satisfying rows `m = 23..N0` (hence, by the `N0` theorem,
the entire tower), then run the primitive decision *there*.  Extra cutting at a
genuine tower survivor is the only informative outcome and is cheap to reach.

---

## 4. Area 3 — the `r=1` control, `N0 = k*+B`, uniformity, avenues 25/45

### 4.1 The `r=1` control: every factual claim CONFIRMED, plus a closed form

Take `H = (X-a)^e` with `4 | e` (Fable 5 proposes `e = 8`; R7R1's own
counterfixture uses `e = 4`).  Then `p = (X-a)^(e/4)`.

- **"`V_H` is four punctured lines."**  `p^4 = (X-a)^e` factors into four
  rational branches `p = zeta_4^j (X-a)^(e/4)`, so `V_H` is four disjoint copies
  of `A^1 - {a}`.  `b_1 = 4`.  Cross-check with the torsor theorem:
  `4(r-1) + c = 4*0 + 4 = 4`.  **CONFIRMED.**
- **"all periods are residues at `X = a`."**  `H^1_dR(A^1 - {a})` is spanned by
  `dX/(X-a)` and the functional is `Res_(X=a)`.  **CONFIRMED.**
- **"every `k_m = 1`."**  `k_m = 1` iff `4 | m e_i`; here `e_1 = e` with `4 | e`,
  so always.  Hence `dim V_m = r - 1 + k_m = 1` for every `m`.  **CONFIRMED.**
- **"E0 makes this control maximally nonlinear."**  With `k_m = 1` for all `m`,
  E0 (`k_m = 1` and `m >= 28`) voids the new-slot linear part at *every* row from
  28 on.  **CONFIRMED.**
- **"executable in closed form by hand."**  **CONFIRMED — and here it is.**

The receiver functional is explicit.  `d(p^m f) = p^m nabla_m(f)` with
`p^m = (X-a)^(em/4)`, so the class `[f dX] in V_m` is zero iff
`Res_(X=a)(p^m f) = 0`, and the gate row `n` (with `f = p^(-(n+22)) q_n`) is

```text
        GATE ROW n   <=>   Res_(X=a) q_n = 0.                    (r = 1)
```

Writing `a = 0`, `H = X^e`, `F = X^(2e) + sum_i F_i t^i` and
`G = sum_i F_i X^(-2e) t^i`, the all-row formula gives the fully explicit form

```text
Res_0 q_n = (2/(n+2)) * sum_j binom((n+2)/8, j) [ X^(2e j - (e/2)(n+2) - 1) ]
                 ( sum_{i_1+...+i_j = n, i_l >= 1} F_(i_1) ... F_(i_j) ).
```

Two immediate consequences, both hand-checkable:

1. **E0's threshold reproduced exactly.**  The `j = 1` term with `i_1 = n` is the
   `F_n`-linear part; its contribution is
   `(1/4)[X^((e/2)(6-n) - 1 + ... )] F_n`, which for `e = 4` is
   `(1/4)[X^(5-n)]F_n` and for `e = 8` is `(1/4)[X^(11-2n)]F_n`.  Both vanish for
   polynomial `F_n` precisely when `n >= 6`, i.e. `m = n + 22 >= 28`.  This is
   E0's threshold, derived independently and with the same constant `1/4`.
2. **`F_n` occurs in row `n` only through the `j = 1` term** (a `j >= 2` product
   has all indices `< n`).  So for `n >= 6` the row is a condition on
   `F_1, …, F_(n-1)` alone — the "no fresh slot" statement — matching the
   postseal review's `q_n = (1/4)p^(n-6)F_n + R_n(F_1,…,F_(n-1))`.

**But the control is the wrong sandbox for Card B.**  `dim V_m = 1` means the
fixed receiver is one-dimensional per character, so Card B's invariant-subspace
question is degenerate there, and (§2.4) the background class is `0`.  Fable 5's
"perfect sandbox" is perfect for Cards A and C and **useless for Card B**.

### 4.2 `N0 = k* + B` — CONFIRMED WITH REPAIR

Fable 5: write the operator on coefficients as `sum_(t=0)^B b_t(k) c_(k+t) = 0`,
let `k*` be the largest integer root of `b_B` "(or `-infinity`)", then
`N0 = k* + B`.

The propagation argument is correct: if `c_j = 0` for all `j <= k*+B` and
`b_B(k) =/= 0` for `k > k*`, then `c_(k+B)` is determined by
`c_k, …, c_(k+B-1)` (all `<= k*+B` at `k = k*+1`) and induction closes.

**Two repairs.**

1. `k*` must be **the largest *nonnegative* integer root, with the convention
   `k* = -1` when there is none** — not `-infinity`, which makes `k*+B`
   undefined, and not "largest integer root", which can *undershoot*.
   Counterexample: `b_B(k) = k + 5` has largest integer root `-5`, giving
   `N0 = B - 5`; but the induction needs the `B` starting values
   `c_0, …, c_(B-1)`, so the true bound is `B - 1`.
2. Fable 5's normalisation to shifts `t = 0..B` is only available after shifting
   `ell_min` to zero (R8 (6.3)); the "startup indices" of R8 (6.4) then have to
   be carried.  R8's version is the safe one.

With those repairs, **CONFIRMED**; and §5.3 below exhibits a worked instance
where the correction matters (the `b=0` sector's leading coefficient has `k=0`
as a root, so `N0` there is `2`, not `1`).

### 4.3 "Uniform stratification" — REFUTED

Fable 5 §7 step 5: "Uniformity over a window stratum is constructible: `b_B`'s
integer-root locus is controlled by polynomials in the slots, exactly the
'explicit singular-index control' the synthesis demanded".

This is exactly the gap R8 §7.2 firewalls, and R8 supplies the refuting shape:

```text
A(N, theta) = N - theta.
```

`A` is a nonzero polynomial over `K(theta)`, so no "degenerate stratum" is
involved and Fable 5's escape hatch ("leading coefficient identically zero …
descending induction on strata") does not apply.  Yet its largest nonnegative
integer root at a specialised point is `theta` itself, unbounded over any
positive-dimensional cell.  Constructibility of `{slots : b_B(k) = 0}` for each
fixed `k` does not bound the union over `k`.

**REFUTED as stated.**  The correct statement is R8 §7.2's: pointwise `N0` is
effective; a cell-wide numerical `N0` needs a further uniform singular-index or
multiplicity theorem that nobody has.  Card A's headline ("the stratum-uniform
finite-decision bound `N0 = k* + B`") should be **de-scoped to pointwise**
before it is funded, or the card will be read as delivering more than it can.

### 4.4 Avenue reopen recommendations

- **Avenue 3 (raise): SUPPORTED, and I strengthen the case.**  Post-E0 the
  residue/period functional really is the only live exact instrument above row
  27, and §4.1 plus §5 turn that from a slogan into two theorems and a fixture.
- **Avenue 16 (raise): SUPPORTED but modest.**  The D-module reading does
  discharge the qualitative half (§2.6), which is a genuine and, as Fable 5
  says in §8, an under-recognised consequence of an audit block written for a
  different purpose.  But R8 obtains the *same and stronger* conclusion
  effectively, by elementary algebraic four-sectioning plus Chen–Kauers–Koutschan
  reduction, with an order bound and no D-module theory.  Raise avenue 16 as an
  **instrument** (structural sanity, regularity guarantees), not as a mechanism
  that changes what is computable.
- **Avenue 25 (reopen, narrow): WEAKLY SUPPORTED — token allocation only.**  The
  claim of "zero base-typing debt" is overstated: the operator lives on the
  four-section curve `E`, not on `C_s`; the fixed-receiver-vs-varying-GM
  identification is unresolved (§2.3); and the `AUDIT.md` R7R2 block already
  "Retain[s] … Avenue 25's branch-cycle CSP carve-out", so the reopen adds little
  that was closed.  Branch-cycle tools become useful only *after* Card A yields
  an actual `L_j` and one wants its singularities.  Do not fund as an
  independent kill route.
- **Avenue 45 (reopen, narrow): NOT SUPPORTED today.**  Its sole named client is
  Card B's invariant-subspace kill, which is not licensed (§2.4–§2.7).
  Additionally "Kovacic-style" is a category slip: Kovacic's algorithm decides
  order-2 operators, while `dim V_m = 3 or 4` on branch P forces `L_j` of order
  `>= 3` generically.  Keep 45 closed; revisit only downstream of a computed
  operator, at which point it is a *tool* choice, not an avenue.

---

## 5. New exact results produced by this review

All three are desk-scale, exact-rational, and independently replayable.  I offer
them as promotable content in their own right; they were produced while testing
Fable 5's claims, and two of them bear directly on its program decisions.

### 5.1 Replay basis

Pure-Python exact Laurent/series arithmetic over `Q` (no CAS).  Verified against
the hashed record before use:

```text
q_n = (2/(n+2)) [t^n] F^((n+2)/8)                      (postseal review, line 94)
q_n = (1/4) p^(n-6) F_n + R_n(F_1,...,F_(n-1))         (postseal review, line 108)
q_0 = p^2,  q_1 = F_1/(4p^5),  q_2 = F_2/(4H) - F_1^2/(16H^3)     (R7R1 (0.4))
```

All reproduced exactly for `H = X^4`, `p = X`, arbitrary rational windows.
R7R1's counterfixture also reproduces: `F = X^8 + 4X^4 t` gives `q_1 = 1/X` with
`Res_0 q_1 = 1 =/= 0`.

### 5.2 `R1` — unconditional death of rows `m = 4 (mod 8)`, `m >= 28` (all `H`, all windows)

**Theorem.**  Let `n >= 6` with `n = 6 (mod 8)`, equivalently
`m = n + 22 = 4 (mod 8)` with `m >= 28`.  Then for every `H`, every window `F`,
and every branch, the gate class of row `m` vanishes identically:
`[p^(-m) q_n dX] = 0` in `V_m`.

**Proof.**  Put `N = (n+2)/8 in Z_(>=1)`.  Then `F^((n+2)/8) = F^N` is a
polynomial in `t` with polynomial `X`-coefficients, so
`q_n = (2/(n+2)) [t^n] F^N in K[X]`.  Also `m = 8N + 20 = 4(2N+5)`, so `4 | m`
and `H^(m/4) in K[X]`.  Set

```text
Phi = int q_n dX  in K[X],        g = Phi / H^(m/4)  in  A = K[X, H^(-1)].
```

Then, using `nabla_m(g) = H^(-m/4) d( H^(m/4) g )` and `p^m = H^(m/4)`,

```text
nabla_m(g) = H^(-m/4) d(Phi) = H^(-m/4) q_n dX = p^(-m) q_n dX.        QED
```

**Why it matters.**  This **strictly strengthens E0** at those rows.  E0 voids
only the new-slot *linear* part, under the hypothesis `k_m = 1`; `R1` voids the
row *entirely*, nonlinear carry included, with no hypothesis on `k_m`, `r`, `c`,
the branch, or the window.  Rows `m = 28, 36, 44, 52, …` are dead for free.

**Free structural constraint on any candidate operator.**  `n = 6 (mod 8)`
implies `n = 2 (mod 4)`, i.e. sector `b = 2`, with `k = (n-2)/4` **odd**.  Hence

```text
        C_2(z)  in  V_(m_0)[[ z^2 ]]      —  the sector-2 class series is EVEN in z.
```

Any telescoper, recurrence, or `L_2` produced by `GATE-REC`, Card A, or any lane
must reproduce `c_(2,k) = 0` for all odd `k`.  This is a sharper, zero-cost
mutation test than the ones in Card A's discriminator list, and it is exact.

**Numerical corroboration.**  Two independent random rational windows in the
`r=1` control (`H = X^4`; `F_1..F_5` of degree `<= 3` and `<= 5`; seeds 11 and
23) give `Res_0 q_n = 0` at `n = 6, 14` and nonzero at `n = 10, 18`, exactly the
odd-`k`/even-`k` pattern.  The closed-form fixture of §5.3 gives `0` at
`n = 6, 14, 22, 30` and nonzero elsewhere.

### 5.3 `R2` — Fable 5's own §2 "cheap test", executed: the nonlinear tower is **not** vacuous

Fable 5 §2, second falsification attack: "If the nonlinear carry residues also
vanish generically (cheap test: residues of `[NL(F_1..F_5)]` at random rational
prefixes), the tower cuts nothing and the whole face question collapses onto the
endpoint."

I ran exactly that test in the `r=1` control, where §4.1 makes the gate literally
`Res_0 q_n = 0`.  Procedure: random rational `F_1..F_5` (`F_i = 0` for `i >= 6`),
solve rows `m = 23..27` triangularly for their fresh slots, then evaluate rows
`m >= 28` and compute the exact Jacobian of `(row_6, …, row_K)` with respect to
all window coordinates by forward-mode dual numbers over `Q`.

```text
seed 23, deg F_i <= 5, 30 window coordinates, rows 6..18 (m = 28..40):

  Res_0 q_n :  n=6:0   n=7:-111/512   n=8:-75/128   n=9:12669/4096  n=10:-399/64
               n=11:2625/512  n=12:43877/8192  n=13:-156387/16384  n=14:0
               n=15:-375777/262144  n=16:2259475/32768  n=17:-191228235/1048576
               n=18:162499/1024

  Jacobian rank of rows 6..K:
      K =  6  7  8  9 10 11 12 13 14 15 16 17 18
   rank =  0  1  2  3  4  5  6  7  7  8  9 10 11
```

A second seed (11, degree `<= 3`, 20 coordinates, rows to `m = 38`) gives the
same picture: rank `0,1,2,3,4,4,5,6,6,7,7`, with the rank plateaus falling
exactly on the `R1` rows `m = 28, 36` and on rows whose residue happens to vanish
at that point.

**Verdict: the hypothesis is REFUTED in the control.**  The nonlinear carry
residues do **not** vanish generically; rows past E0's linear death remain
functionally independent and keep cutting.  The `2255Z` appendix's open question
— "no theorem currently makes it generically nonzero" — now has an affirmative
answer at least for `r = 1`.  Consequences:

- Fable 5's §2 attack ("E0 makes this *cheaper than previously priced*… the
  tower cuts nothing and the whole face question collapses onto the endpoint") is
  **mis-priced in the optimistic direction** and should be re-ranked.
- Conversely, this is *good* news for Card A: an infinite tower that genuinely
  cuts is exactly the object for which a finite-decision `N0` is valuable.

Scope: `r = 1` control, `H = X^4`, `F_i = 0` for `i >= 6`, two seeds.  Not branch
P, not a survivor-locus codimension statement, not a face conclusion.

### 5.4 `R3` — a first end-to-end numerical `N0` (fixed point, `r=1` control)

R8 §0 lists "one numerical campaign-wide `N0` — **NOT YET PRODUCED**".  Here is
one at R8 §7.1 scope (fixed `H`, one fixed `F` point), obtained entirely by desk
algebra.

**Fixture.**  `H = X^4`, `p = X`, `F = X^8 + (X^7 + X^4 + 1) t`, all other slots
zero.  Only `j = 1`-index products occur, and
`[X^(7n-3)](X^7+X^4+1)^n = n` (the unique solution of `3b + 7c = 3` with
`a+b+c=n` is `(b,c) = (1,0)`), giving the **closed form**

```text
        Res_0 q_n = (2n/(n+2)) * binom( (n+2)/8 , n ).
```

Verified against the direct Lagrange–Bürmann series for `n = 0..14`.

**`R1` visible in the closed form.**  When `(n+2)/8 = N in Z_(>=1)` and `N < n`
(true for all `n >= 2`), `binom(N, n) = 0`.  Independent second proof of the
period-8 law.

**Exact recurrence.**  Using
`binom(alpha,n) = (-1)^n Gamma((7n-2)/8)/(Gamma(n+1) Gamma(-(n+2)/8))`, the shift
`n -> n+8` gives a first-order relation with polynomial coefficients:

```text
   D(n) * c_(n+8) = N(n) * c_n,
   D(n) = n (n+10) prod_(i=1..8) (n+i),
   N(n) = (n+8)(n+2) * ( -(n+10)/8 ) * prod_(i=0..6) ( (7n-2)/8 + i ).
```

Verified exactly for `n = 1..59` (zero violations).

**`N0`.**  `D` has `n = 0` as its only nonnegative integer root, so
`c_n = 0  =>  c_(n+8) = 0` for every `n >= 1`.  Since `c_0 = 0` identically:

```text
        rows  m = 23, ..., 30   decide the entire infinite tower at this point.
        N0 = 30      (eight rows).
```

At this fixture `c_1 = 1/4 =/= 0`, so the point dies at `m = 23`; the value of
the computation is the *bound*, produced end-to-end.

**Independent corroboration and a check on R8 §2.**  Blind P-recurrence fitting
(exact nullspace, no closed form used) on each four-section
`c_k = Res_0 q_(b+4k)`, `k = 0..57`, returns for **every** `b in {0,1,2,3}` a
unique operator of shift-order 2 and polynomial degree 7, with zero violations
over the whole range; the `b = 0` leading coefficient has `k = 0` as a root and
the other three do not — matching the closed-form `D(n)` exactly, and
illustrating §4.2's repair (the `b=0` sector needs `N0 = 2`, the others `1`).
Meanwhile the **unsectioned** sequence `c_n` admits **no** recurrence in the
searched `(order <= 6, degree <= 8)` box.  That is independent evidence that R8
§2's four-section is the right object and not a convenience.

Scope: one fixed `F` point, `r = 1`, `H = X^4`.  **Not** a campaign `N0`, not
branch P, not uniform over any cell, and it does not disturb R8 §7.2/§7.3's
firewalls in any way.

---

## 6. Narrowest promotable content

From the Fable 5 submission, promotable **as is** after the stated repairs:

1. **`GATE-ALG-PRIM` forward direction** (§3.1–§3.6), stated as:
   > For a face/Keller pair at a window point `F` (so `G` polynomial), the
   > explicit algebraic differential
   > `alpha_F = -(s^21/16)( d_s(s^2 P^2) - 2 p^2 s ) dX`
   > has an `X`-primitive in the fixed finite extension `E' = K(F)(X,s,P,p)`;
   > existence is decidable by algebraic Hermite reduction plus the residue /
   > de Rham class test; and it implies the entire licensed class tower.
   > The converse is false in shape (`-log(1-sX)` control).
   Repairs required: adjoin `p`; drop the redundant order-23 clause; supply the
   pole-order argument for the termwise implication; replace the discriminator
   with the survivor-locus version of §3.8.  **Label: NEW.**

2. **Carrier typing** (§2.2): Fable 5's fixed-space class section is identical to
   R8 (3.7)–(3.8) under `x p^(m_0)`.  Worth recording because it means two
   independently derived formulations agree, which is a real cross-check on both.
   **Label: KNOWN / consistency.**

3. **The qualitative half of `GATE-REC` from the promoted 21:30Z R7R2 block**
   (§2.6), at fixed-`C`-point scope, with the three restated scope conditions.
   **Label: KNOWN, correctly re-read.**  Fable 5's §8 "cross-tradition insight"
   is fair and I endorse it, with the de-scoping.

4. **The `r = 1` control reduction** (§4.1): gate `<=>` `Res_(X=a) q_n = 0`, plus
   the explicit residue formula and the independent rederivation of E0's exact
   `m >= 28` threshold and constant `1/4`.  **Label: NEW (desk).**

**Not promotable:**

- `GATE-INV` / Card B in any current form (§2.4–§2.7).
- The stratum-**uniform** half of Card A's `N0` claim (§4.3); the pointwise half
  is fine and is R8 §7.1's.
- "The four-section is derived from the family's equivariance" (§2.1).
- "Tower survival is equivalent to horizontality" (§2.3) — only one implication.
- Avenue 45's reopen as stated.

**From this review**, promotable as new content: `R1` (§5.2, with proof),
`R2` (§5.3, as an executed control-scope experiment with its scope stated),
`R3` (§5.4, as a fixed-point `N0` demonstration).  `R1` may be a **DUPLICATE**
of a peer lane in this round — see §0.4.

---

## 7. Promotion advice

1. **Re-pin custody before crediting this round.**  `APPROACHES.md`, `AUDIT.md`
   and `COORDINATION.md` have drifted from the packet values (§0.2).  A blind
   round whose custody set mutates mid-flight cannot support "byte-for-byte
   verified" claims from any lane.
2. **Fund Card C, de-scoped and repaired.**  It is the only item in the
   submission that converts an infinite tower into one finite decidable test for
   the actual object of interest, and it depends on nothing provisional.  Start
   on the `r=1` control at a genuine tower survivor (reachable now, via `R3`'s
   `N0` mechanism), not at random points.
3. **Fund Card A pointwise; do not fund its uniformity claim.**  Restate the
   deliverable as R8 §7.1 scope.  Add `R1`'s "sector-2 series is even in `z`" as
   a mandatory, free mutation test for any produced operator, alongside the
   licensed-table check Fable 5 proposes.
4. **Do not fund Card B / `GATE-INV`, and do not reopen avenue 45 on its
   strength.**  Reopen avenue 25 at token allocation only, explicitly downstream
   of a computed `L_j`.
5. **Re-price the §2 survivor-march falsification attack.**  Its stated
   cost advantage rested on the nonlinear carry being generically vacuous;
   `R2` says it is not, in the one place the test is cheap.
6. **Build Fable 5's §4 fixture bank + replay verifier.**  I endorse it without
   reservation; §5.3–§5.4 are a working prototype (exact class-coordinate
   vectors, a certified recurrence, and two free zero-tests from `R1`).  It is
   correctness-preserving by construction and desk-scale.
7. **Merge with the `GATE-REC` lane rather than duplicating.**  R8 already proves
   the fixed-instance theorem with an effective order bound; Fable 5's route
   reaches the qualitative half independently, which is a genuine cross-check.
   Credit both, and take R8's §6/§7 formulations of `N0` and of the uniformity
   firewall over Fable 5's, which are looser at exactly those two points.

---

## 8. Process ledger

**Checks actually run.**  All custody hashes plus `git rev-parse HEAD` (§0.1,
§0.2).  Full reads: the `2259Z` packet, the Fable 5 submission, the R8 report,
sections 1–4 of the `2255Z` appendix, R7R1 in full.  Targeted reads after hash
verification: the E0 review (derivation and rank tables), `AUDIT.md` lines
270–330 (R7R2 block), `APPROACHES.md` avenue rows 3/16/25/45, the postseal
review's all-row formula lines, novelty greps in the five canonical files.
Exact computations: Lagrange–Bürmann series to `t^24` with residue extraction;
R7R1 (0.4) and the counterfixture reproduced; E0's threshold and constant
rederived; the `R1` proof plus three numerical corroborations; `R2`'s Jacobian
ranks at two seeds; `R3`'s closed form, recurrence (`n = 1..59`), and blind
four-sector P-recurrence fit (`k = 0..57`).  Hand algebra: the `mu_8`
equivariance, the `alpha_F` chain (§3.1), the primitive-ambiguity argument
(§3.3), the `y`-degree `14 -> 8` degeneration (§2.3), the `zeta_8` identification
of the two `s=0` components, the `N0` off-by-one counterexample (§4.2).

**Failed attempts, disclosed.**  (1) I first tried to fit a P-recurrence to the
*unsectioned* `Res_0 q_n` and found none in the `(order <= 6, degree <= 8)` box;
rather than concluding against R8 I re-read R8 §2 and tested the four-sections,
which succeeded — the failure is itself reported above as evidence *for* R8's
construction.  (2) My first fixture (`F_1 = X^3 + X`, `F_2 = X^2`) produced an
identically zero tower; a degree count showed the window was too low-degree to
support any residue for `n >= 2`, and I replaced it.  I report this because a
naive reading of that first run would have looked like a spectacular survivor.
(3) I attempted to decide whether `gate => flat` could be repaired by showing the
transported subspace is monodromy-stable, and could not; that is left as the
gap in §2.3, not papered over.  (4) I did not attempt to compute `L_j` on branch
P — outside desk scope and outside my licence.

**Assumptions.**  The hashed files are ground truth for promoted content;
E0, the all-row formula, R7R1, the torsor count, and the R7R2 audit block are
taken as promoted; R8 is treated as *unreviewed* and is used only as a
comparison target, never as authority — except where I explicitly credit its
argument (the pole-order descent of §3.5) and verify it myself.  `BI-FACE-FROZEN`
is treated as provisional and consumed nowhere.  The `GATE-REC` lane's result is
assumed in neither direction.  All geometry in §2.3–§2.5 is over `C`.

**Conjectural leaps of my own, labelled.**  `R2` is an experiment in the `r=1`
control, not a theorem about branch P; the inference "the tower keeps cutting" is
a functional-independence statement at the tested points, not a codimension
theorem at survivor points.  `R3`'s `N0` is for one fixed `F` and inherits R8
§7.2's firewall unchanged.  My assessment that Card C is the most valuable item
in the submission is a judgement, not a result.

**Contamination.**  As disclosed in §0.4: an auto-loaded personal memory index
including one entry that may originate in this very round; `R1` was nonetheless
re-derived and re-verified from scratch and should be credited to whichever lane
banked it first.  No `2259Z` peer response was read, listed, globbed, or
searched.  No `2255Z` lane response exists to read.  The harness supplied a git
status snapshot at session start (branch name, a modified `jc2-lean` gitlink
line, untracked `cases/…` directory names); I acted on none of it and it contains
no peer round content.

— end of cross-review —
