# Hostile review: `RULE-ON-Y` for a proper intermediate block

Date: 2026-08-30 UTC  
Reviewer: Fable 5 (different-model hostile reviewer)  
Charge basis (git): `5cc7b50274df491cb09dbb91a8b528de77fc5ef4`  
Verdict: **CONFIRM_WITH_CORRECTIONS** (main chain sound; one fallback
argument in the charged audit is refuted as argued; several citation and
wording repairs)

## 0. Charge custody

All five charged files were re-hashed locally and match the charge exactly:

```text
acfcd839a4f7af77c54a75bc30c2909f26c6afb8ec35b1862dc685e27b270819
  xmodel/block-descent-a1-ruling-transfer-audit-sol56-20260830.md
b52d063d2801885c30fe92212b86d9cda1de7c97a6438a3cc1d243de1c6b30bc
  xmodel/block-descent-a1-ruling-transfer-audit-sol56-20260830.md.artifact.json
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f092a7152dea8bdee387825fa8181dffeb8145fc99cf65973d74f528491f57a0
  xmodel/bd-a2-a1-ruling-euler-boundary-cap-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

Every theorem was reconstructed from the promoted hypotheses only: `Y`
integral normal affine complex surface, `g2` finite flat surjective, `g1`
etale quasi-finite dominant, `R=NonEt_Y(g2)` nonempty pure codimension one,
`g1(A2) subset Y_sm minus R`, `Sing(Y) subset R`, and `U=Y minus R`.  No
seal, manifest, or prior-model agreement was treated as evidence.

## 1. Item 1: affineness of `U`

**Verdict: CONFIRM_WITH_CORRECTIONS.**

### 1.1 The Nagata route (the audit's route) is correct as charged

The false rule "open in affine is affine" appears nowhere in the audit; the
audit explicitly forbids it.  The theorem actually consumed is: *on the
spectrum of a two-dimensional normal excellent domain, the complement of the
support of every effective Weil divisor is affine.*  I verified the exact
attribution byte-level: the introduction of Brenner, `arXiv:math/0209298`
(*The affine class group of a normal scheme*), fetched during this review,
states verbatim that the affineness-of-hypersurface-complement property
holds when "`X` is the spectrum of a normal excellent domain `A` of
dimension two.  The first proof of this result was given by Nagata in
connection with the 14th problem of Hilbert."  No factorial, Q-factorial,
Cartier, or principality hypothesis appears, matching the audit's Section
2.2 word for word.

Because I could not check Nagata's 1956 paper itself, I reconstructed an
independent proof in the exact generality the block needs (finite-type
normal surface over `C`, deleted set pure codimension one, singular points
allowed only on the deleted set), so the review does not rest on the
attribution:

> Complete `Y` inside projective space through its affine embedding; the
> boundary is the support of an ample effective Cartier divisor `H_b`
> (hyperplane section at infinity of the closure, after normalization).
> Resolve all singular points lying on `boundary union R_bar`; since
> `Sing(Y) subset R`, the resulting surface `V` is smooth and `U` is
> untouched.  Pulling back `H_b` and subtracting exceptional curves in the
> standard way gives an ample effective divisor `H` on `V` supported exactly
> on the preimage of the old boundary.  Now take `D_m = m*H + sum_i R_i'`
> over all components `R_i'` of the total transform of `R_bar`.  Nakai:
> `D_m^2 > 0` for large `m`; for a curve `G` not in `Supp(D_m)`,
> `D_m.G >= m*H.G > 0` because `H` is ample; the finitely many components of
> `Supp(D_m)` are handled by taking `m` large.  So `D_m` is ample with
> support exactly `V minus U`, and the complement of the support of an
> effective ample divisor on a projective surface is affine.

This proof consumes purity (`R` pure codimension one) and dimension two (the
"finitely many negative curves absorbed by `m`" step is surface-specific;
Brenner's paper gives dimension-three counterexamples to the general
statement, so the dimension hypothesis is genuinely load-bearing and the
audit is right to route through the surface theorem rather than a general
principle).

### 1.2 The stronger direct route: Stacks Tag `0ECD` applies, with one repair to the charge's paraphrase

I fetched Tag `0ECD` verbatim during this review.  The actual statement is:

> **Theorem 58.29.3 (Stacks Project, Tag 0ECD; Section 58.29, "Affineness
> of complement of ramification locus").**  Let `Y` be an excellent regular
> scheme over a field.  Let `f : X -> Y` be a finite type morphism of
> schemes with `X` normal.  Let `V subset X` be the maximal open subscheme
> where `f` is etale.  Then the inclusion morphism `V -> X` is **affine**.

The charge's paraphrase ("asserts affineness of the maximal etale locus")
is inexact and, read literally as an absolute statement, false: for the
blowup `X -> A2` of the origin (finite type, `X` normal, target excellent
regular over `C`), the maximal etale locus is `X minus E ~ A2 minus {0}`,
which is not affine.  The actual conclusion — the inclusion `V -> X` is an
affine **morphism** — is consistent with that example (`E` is Cartier, so
`V` is locally a principal complement in `X`), and it upgrades to absolute
affineness exactly when `X` itself is affine.

Application to the block: take Stacks-`X := Y` (normal, promoted),
Stacks-`Y := A2_C` (excellent regular over the field `C`), `f := g2`
(finite, hence finite type).  The maximal etale open is by definition
`Y minus R` with `R` the full source non-etale support.  The theorem gives
that `U -> Y` is an affine morphism; `Y` is affine; hence the preimage of
`Y` — that is, `U` — **is an affine scheme**.

Consequences, answering the charge exactly:

1. Tag `0ECD` applies literally to `g2 : Y -> A2` with the affine-morphism
   reading plus affineness of `Y`.  No quasi-finiteness or finiteness of
   `f` is even consumed by the tag (finite type suffices), though `g2` is
   in fact finite.
2. It removes the dimension-two, purity, and nonempty-divisor dependencies
   **from the affineness step**.  `U` is affine even if one refuses to
   invoke purity of `R`, and would remain affine if `R` were empty or had
   the wrong codimension.
3. It does not remove purity from the campaign: purity is still consumed by
   the promoted block theorem itself (divisoriality of `R`, the class-
   lattice injection, the different statement) and by the Nagata route.
   But `RULE-ON-Y` as a standalone deduction can now be based on `0ECD`
   with strictly fewer hypotheses.  The audit used only Nagata; this is a
   missed strengthening, not an error.

The audit's remark that the principal-open shortcut is unavailable is
verified: `R subset Y minus g1(A2)`, and the charged Galois integration's
class-lattice injection makes every component of `R` of infinite order in
`Cl(Y)`, so no effective divisor supported in `R` is principal and `U` is
never a `D(f)`.  (Cartier-but-nonprincipal would still have sufficed via
the standard fact that `X_s` is affine for a section `s` of a line bundle
on an affine scheme; but nothing promotes `R` Cartier, and `Sing(Y)` may
lie on it, so both charged routes correctly avoid this.)

## 2. Item 2: edge cases

**Verdict: CONFIRMED** (all six probes behave as the audit says, with the
purity citation now pinned).

1. **Weil versus Cartier.**  Only the Weil support of `R` enters either
   affineness route.  Explicit control that non-Cartier deletion works
   (constructed for this review): let `X` be the affine cone over a smooth
   plane cubic `E` and `C` the ruling line over a general point `q` of `E`
   (a Weil divisor that is not Q-Cartier at the vertex for general `q`).
   Blow up the vertex to get the ruled surface `P(O + O(-3))` over `E` with
   exceptional section `E_0` (`E_0^2=-3`), section at infinity `E_inf`, and
   fibre `f_q`; the divisor `E_inf + E_0 + 4 f_q ~num 2 E_0 + 7 f` is ample
   (Hartshorne V.2.21: `a C_0 + b f` ample iff `a>0`, `b>ae`, here
   `2>0`, `7>6`), effective, with support exactly the complement of
   `X minus C`.  Hence `X minus C` is affine although `C` is not Q-Cartier.
   The vertex lies on `C`, mirroring `Sing(Y) subset R`.
2. **Support versus multiplicity.**  `U` depends only on `Supp(R)`;
   discriminant and different multiplicities never enter.  The audit's
   `R_red = sum_i R_i` convention is the correct one.
3. **Non-Q-factorial `Y`.**  Covered by both routes; see the control in
   point 1 and the independent proof in 1.1, neither of which uses any
   Q-Cartier property.
4. **Empty non-etale locus.**  Impossible for a nontrivial block: `R` empty
   makes the connected `g2` a finite etale cover of `A2_C` of degree
   `d2>=2`, contradicting triviality of the etale fundamental group of
   `A2_C`.  Even counterfactually it would be harmless for affineness
   (`U=Y`), and `0ECD` is indifferent to it.
5. **Codimension-two residue.**  This is the edge that would kill the
   conclusion: if `R` had an isolated closed point `p` away from its
   divisorial part, then `U` would be a punctured surface and never affine
   (Section 4 of the audit; the Hartogs argument is verified in item 7
   below).  So purity is load-bearing for the Nagata route.  It holds, and
   I pin the modern citation, fetched verbatim: **Stacks Tag `0EA4`
   (Lemma 58.28.3, "Purity of ramification locus", attributed to Gabber
   via [Zong, Theorem 2.4])**: if `O_{X,x}` is normal of dimension `>= 1`,
   `O_{Y,y}` is regular, `f` is locally of finite type, and `f` is etale at
   every dimension-one specialization point `x' ~> x`, then `f` is etale at
   `x`.  Applied at a hypothetical isolated non-etale closed point (all
   codimension-one generizations etale) this yields etaleness there, a
   contradiction; hence `R` is divisorial at every point.  This is
   source-side purity in exactly the promoted `Y`-normal/`A2`-regular
   situation, with no quasi-finiteness needed.
6. **Deletion of selected components only.**  If only some components of
   `R` are deleted, the complement is *still affine* (both routes: Nagata
   applies to any divisor; `0ECD`-affineness of the inclusion restricts) —
   but it is no longer smooth and `g2` is no longer etale on it, since the
   residual non-etale points and possibly `Sing(Y)` survive.  The
   Miyanishi–Sugie chain then breaks exactly at its smoothness hypothesis.
   The audit's Section 2.3 warning is correct and precisely aimed.

## 3. Item 3: etaleness of `g2|U`, smoothness, and the actual first leg

**Verdict: CONFIRM_WITH_CORRECTIONS** — the promoted chain is confirmed;
one *fallback* argument inside the audit is refuted as argued.

Confirmed:

- `U` is by definition the maximal open where `g2` is etale (non-etale
  locus is closed since the etale locus of a finite-type morphism is open),
  so `g2|U` is etale.  Etale morphisms preserve regularity in both
  directions (Stacks Tag `0AH7`, fetched: `O_{U,u}` regular iff
  `O_{A2,v}` regular), so `U` is regular, and regular + finite type over
  `C` gives smooth.  Consistent with, and independent of, the promoted
  `Sing(Y) subset R`.
- `g1(A2) cap R` empty forces the unique factorization `g1: A2 -> U`
  through the open immersion; density of the image in `Y` gives density in
  the open `U`; etaleness, quasi-finiteness, and generic degree `d1` are
  inherited.  Confirmed.
- The four loci are kept distinct throughout the audit: source
  ramification `R`; target discriminant `D=g2(R)=V(Disc g2)`; its full
  inverse image `g2^{-1}(D)`, which can strictly contain `R`; and the
  first-leg image `g1(A2)`, an open subset of `U` that need not equal `U`.
  The audit never conflates them; its Section 4 makes the second and third
  distinct by an unramified-sheet argument, which I verify with an exact
  model in item 7.

**Refuted as argued (fallback only).**  Audit Section 2.4 offers an
"independent repair if one refuses Nagata": `V := g1(A2)` is open,
`A2 -> V` is surjective etale quasi-compact, "hence fpqc.  Affineness
descends fpqc, so `V` is smooth affine."  The quoted descent principle is
false.  Counterexample: `D(x) ⊔ D(y) -> A2 minus {0}` is surjective, etale,
flat, quasi-compact — even an affine *morphism* — from an affine scheme
onto a non-affine scheme.  What descends along fpqc coverings is the
property "affine morphism", a relative notion; absolute affineness of the
base of a cover with affine total space is simply not a descent statement.
The one classical rescue, Chevalley's theorem, needs `A2 -> V` finite
(equivalently proper), which is exactly what is not known: properness of
`g1` over its image is undetermined (`A(g1) cap V` may be nonempty).

Correct retyping of the fallback: `V = U minus Z_U` with `Z_U` closed in
the (now proved) affine `U`; `V` is affine if and only if `Z_U` has no
isolated point, by Nagata on `U` in one direction and the punctured-surface
obstruction in the other.  Whether an etale quasi-finite dominant
`g1: A2 -> U` can omit an isolated point of `U` is a Jelonek-type question
(structure of `Y minus g1(A2)` inside the nonproperness curve `A(g1)`); no
promoted result decides it.  Typed **OPEN**, per FALLACY-v2, with no fill.
This does not touch the main theorem: nothing downstream consumes
affineness of `V`, only of `U`.  The audit itself presents 2.4 as optional;
the required repair is to delete the fpqc sentence or replace it by the
typed open question.

## 4. Item 4: rationality, units, log Kodaira dimension

**Verdict: CONFIRMED** (all inequality directions correct).

- **Units.**  `g1` dominant between integral schemes makes `g1*` injective
  on regular functions; a unit `u` on `U` pulls back to a unit of
  `C[x,y]`, i.e. a scalar `c`, and injectivity of `g1*` applied to `u - c`
  gives `u = c`.  So `O(U)^* = C^*`.  Only dominance is consumed.
- **Rationality.**  `C(U) = K` has index `d1 < infinity` in `C(x,y)`, so
  `U` is unirational; Castelnuovo's theorem (characteristic zero) makes a
  smooth projective model rational.  Confirmed.
- **Log Kodaira.**  The consumed monotonicity is Iitaka's: for a dominant
  **generically finite** morphism `V -> W` of smooth open varieties,
  `bar-kappa(V) >= bar-kappa(W)`.  Direction check: complete to
  `f: V-bar -> W-bar` with `f^{-1}(D_W) subset D_V` (automatic for a
  morphism of the open parts), and the logarithmic ramification divisor in
  `K_{V-bar}+D_V = f*(K_{W-bar}+D_W) + R_log` is effective, so log
  pluricanonical sections pull back injectively.  Applied to
  `g1: A2 -> U`: `-infinity = bar-kappa(A2) >= bar-kappa(U)`, exactly the
  audit's displayed inequality, hence `bar-kappa(U) = -infinity`.  Hostile
  probe of hypothesis necessity: for merely dominant maps the statement
  fails (`A1 x E -> E` has `bar-kappa = -infinity` upstairs, `0`
  downstairs), so generic finiteness is load-bearing and present.
- **Does etaleness/quasi-finiteness of `g1` strengthen this?**  No.
  Equality `bar-kappa(A2)=bar-kappa(U)` under an etale map would need
  properness (finite etale invariance); `g1` is not proper, and no stronger
  conclusion than `<=` is claimed or available.  The audit's statement that
  no compactification of `Y` is assumed is correct: `bar-kappa(U)` is
  computed on smooth completions of the already-smooth `U`.

## 5. Item 5: the exact Miyanishi–Sugie theorem

**Verdict: CONFIRM_WITH_CORRECTIONS** (statement pinned; a separate
extension step identified explicitly; no mathematical gap).

DOI `10.1215/kjm/1250522319` was resolved during this review and is
*Miyanishi–Sugie, "Affine surfaces containing cylinderlike open sets",
J. Math. Kyoto Univ. 20 (1980)* — the title itself records that the 1980
theorem's primary output is a **cylinderlike open set**.  The consumed
composite statement is:

> Let `S` be a smooth **affine** surface over an algebraically closed field
> of characteristic zero.  Then `bar-kappa(S) = -infinity` iff `S` contains
> a cylinderlike open set `C_0 x A1` (Miyanishi–Sugie, with Fujita), and in
> that case `S` itself admits a surjective morphism `rho: S -> C` onto a
> smooth curve whose general scheme-theoretic fibre is `A1`.

The cylinder-to-global-fibration upgrade is a **separate extension
theorem** — the cylinder's pencil is modified so that the fibration has no
base point on `S` (an arbitrary cylinder's pencil can have base points, as
lines through the origin in `A2` show) — recorded in Miyanishi's book *Open
Algebraic Surfaces* and quoted in exactly this surface-fibration form by
Dubouloz–Kishimoto, which is the form the charged ruling integration cites.
The output is an actual morphism on all of `U`, over `C`, with no finite
base change and no field extension.  Internal theorem numbering of the 1980
paper and the book could not be fetched (JS/paywall); disclosed in
Section 10.  The hypotheses are exactly "smooth affine `+`
`bar-kappa=-infinity`", both now proved for `U`; the audit's repair 2 (the
theorem does *not* consume "normal affine dominated by `A2`") is correct
and material, since `Y` itself is not known smooth and the theorem would
not apply to `Y`.

## 6. Item 6: base dichotomy and the fibre statement

**Verdict: CONFIRMED** (with one wording repair and an independent proof of
the fibre lemma).

- **`C = A1` or `P1`.**  `C` is dominated by the rational `U`, so Lüroth
  makes `C` rational; `rho` surjective makes `rho*` inject `O(C)^*` into
  `O(U)^* = C^*`; a smooth rational affine curve with at least two
  punctures has the nonconstant unit `(t-a)/(t-b)`.  Hence at most one
  puncture: `C = A1` or `C = P1`.  Confirmed, including the direction of
  every step.
- **The projective base is real for an affine total surface.**  Verified
  concretely: on `F_1`, `S = C_0 + 2f` is an ample section (`S^2=3`,
  `S.f=1`, `S.C_0=1`), `F_1 minus S` is a smooth rational affine surface
  with only constant units, and the ruling restricts to an `A1`-fibration
  over `P1` (each fibre loses the single point `S cap f`).  So no
  transferred hypothesis excludes `C = P1`; the audit and the ruling
  integration both refuse to discard it, correctly.
- **Gurjar–Miyanishi citation.**  DOI `10.1307/mmj/1114021083` resolves to
  *Gurjar–Miyanishi, "Automorphisms of affine surfaces with
  A1-fibrations", Michigan Math. J. 53 (2005)*; the fibre statement is a
  preliminary lemma there and is older folklore (Miyanishi).  Because the
  interior text is paywalled, I re-proved the statement so the review does
  not depend on the citation:

  > Complete `rho` to a `P1`-fibration on a smooth completion `(V,D)` of
  > `U`.  Every completed fibre is a tree of `P1`s (arithmetic genus zero).
  > The boundary `D` of the affine `U` is connected (classical; a connected
  > Stein surface has one end) and meets a general fibre in one point, so
  > its horizontal part is a single section `H`, and `H` meets each fibre
  > tree `T` in one point `p_H` lying on a single component (two components
  > through `p_H` would force `H.T >= 2`).  Every connected component of
  > the vertical boundary `D_c` inside `T` must reach `H` (else `D`
  > disconnects), hence contains the component through `p_H`; so
  > `D_c` is a connected subtree.  Each branch of `T` hanging off that
  > subtree must be a **single** `P1` — a deeper component would meet the
  > boundary nowhere and be a complete curve in the affine `U` — and it
  > loses exactly its one attachment point.  Therefore the reduced fibre in
  > `U` is a disjoint union of `A1`s.  (If `D_c` is empty the same
  > complete-curve argument forces `T` irreducible and the fibre is one
  > `A1`.)

- **What remains uncontrolled.**  Exactly two things, and the audit names
  the first: (i) **multiplicities** — `rho^*(c) = sum m_i F_i` with
  `m_i >= 1` arbitrary; multiple fibres genuinely occur on smooth affine
  surfaces (tom Dieck–Petrie-type examples), and nothing here bounds them;
  (ii) **counts** — the number of degenerate fibres and of components
  `q_t` per fibre is qualitatively unbounded; the only known bounds are
  Euler-theoretic and quadratic-scope (Section 9).  One wording repair: the
  audit's Section 0 phrase "every reduced fibre is a disjoint union of
  affine lines" should everywhere read as its own Section 3 does — *every
  fibre, taken with reduced structure*, is a disjoint union of affine
  lines.  "Every reduced fibre" invites a support/multiplicity confusion
  that FALLACY-v2 forbids.

## 7. Item 7: explicit controls and counterexample attempts

**Verdict: CONFIRMED** (all controls behave as claimed; two new exact
controls constructed; no counterexample to the surface theorems found).

1. **Punctured normal surface (audit Section 4).**  Verified: for the
   quadric cone `Y0 = Spec C[x,y,z]/(z^2-xy)` over `A2_(x,y)`, the smooth
   locus `Y0 minus {o}` has the same global functions as `Y0` (normality
   plus depth two), so were it affine its canonical morphism to
   `Spec Gamma = Y0` would be an isomorphism restoring `o` — contradiction.
   Meanwhile the full non-etale locus is `V(z)` (support of `xy=z^2`), and
   `D(z)` is smooth affine.  This cleanly separates "smooth locus" from
   "delete the full ramification support", and the audit correctly brands
   it a local-logic control only: its ramification divisor is principal,
   violating the promoted nonprincipality, and it is no sandwich.
2. **Non-Cartier complement.**  The elliptic-cone control of Section 2.1
   above: deletion of a non-Q-Cartier ruling line from a normal affine
   cone has affine complement, witnessed by an explicit ample boundary
   divisor.  Nagata's generality is real, not decorative.
3. **Target-discriminant deletion losing an unramified sheet — exact
   model.**  Take `Y = A2_(x,t)`, `g2(x,t) = (x, (t^3-3xt)/2)`, the Whitney
   family `t^3 - 3xt - 2z` over `A2_(x,z)`.  Then `R = V(t^2 - x)` and
   `Disc = 108(x^3 - z^2)`, and the hand-verified identity
   `(t^3-3xt)^2 - 4x^3 = (t^2-x)^2 (t^2-4x)` gives

   ```text
   g2^{-1}(V(Disc)) = V(t^2-x) union V(t^2-4x) = R union (unramified sheet).
   ```

   So `Y minus g2^{-1}(D)` is strictly smaller than `U = Y minus R`: over a
   general discriminant point one source point is unramified and survives
   in `U`.  The audit's Section 4 and its repair 3 (the `branch(g2)`
   ambiguity; only the source reading types the open correctly, and the
   target-preimage open cannot silently replace `U` because the block
   theorem only promises `g1` avoids `R`) are verified against this model.
4. **A smooth affine `bar-kappa=-infinity` surface breaking the global
   fibration or base statement.**  Sought and not found.  The pencil-base-
   point worry (a cylinder whose fibre closures all pass through a point of
   `U`, as for lines through the origin in `A2`) is dissolved by the
   extension theorem's freedom to change the cylinder, exactly as the
   parallel ruling does for `A2`; Danielewski surfaces, tom Dieck–Petrie
   surfaces, and `F_n minus S` all carry the asserted global fibrations,
   with `F_n minus S` witnessing that the `P1` base cannot be dropped.  I
   record explicitly that a *bona fide* counterexample here would refute
   Miyanishi–Sugie, not just the audit.
5. **"Consistency control" pricing.**  Verified: any full model
   `(Y,g1,g2)` meeting the promoted constraints has `F = g2 o g1` etale
   everywhere on `A2` (etale `g1` composed with `g2` etale at every image
   point, since the image avoids `R`) of generic degree `d1*d2 >= 4`, i.e.
   is a noninvertible Keller map.  The audit's Section 5 is right that a
   "cheap consistent sandwich" would be a solution to JC2 itself; only
   step-local controls are honest.

## 8. Item 8: what transfers and what does not

**Verdict: CONFIRMED.**

Transfers (qualitative, block-general, presentation-free): `U` smooth
rational affine; `O(U)^*=C^*`; `bar-kappa(U)=-infinity`; dominated by the
actual etale quasi-finite `g1`; surjective `A1`-fibration `rho: U -> C`;
`C = A1 or P1`; every fibre reduced-supportwise a disjoint union of affine
lines.  None of this consumes the trace-zero frame, the incidence surface
`[X]=2A+3B`, `F5` boundary data, or any fixed coefficient presentation.

Does **not** transfer, exactly as the audit rules: `e(X)=13`/Noether,
`e(U)=12-r-c`, `r+c<=11`, the `P1` sharpening `r+c<=10`, `c=3+k` and the
`F5` caps `r+k<=8`/`<=7`, the `A7`/`A8` table, the `D9` lattice and
markings, boundary rank, any bounded adapted completion, any Picard/Euler
cap, and any finite-presentation occurrence statement.  All of these are
functions of the charged quadratic completion in the ruling integration and
have no meaning for the abstract `Y`.  Also confirmed: nothing here says
anything about the primitive/no-proper-block sector; the whole theorem is
conditional on a proper intermediate field existing.

One boundary note, typed as a *free successor seed*, not silently promoted:
the ruling integration's fibre stratification identity
`e(U) = e(C) + sum_t (q_t - 1)` (its (4.1)) is itself presentation-free —
its proof uses only topological Euler additivity, the cylinder over a dense
open subcurve, and the reduced-fibre structure — hence
`e(U) >= e(C) >= 1`, with `e(U) >= 2` on the `P1` branch, holds for every
block `U`.  What is quadratic-only is the *evaluation* `e(U)=12-r-c`.  The
charged audit does not claim the identity; promoting it block-generally is
the natural successor (Section 12) and must be reviewed there, not imported
by analogy here.

## 9. Itemized verdicts

```text
Item 1 affineness:            CONFIRM_WITH_CORRECTIONS
  - Nagata route CONFIRMED (Brenner intro fetched verbatim; independent proof supplied);
  - Tag 0ECD fetched verbatim; applies via "V -> X affine morphism" + Y affine;
    removes dim-2/purity/nonemptiness from the affineness step;
  - charge-prompt paraphrase of 0ECD too strong as absolute statement (blowup control).
Item 2 edge cases:            CONFIRMED (purity pinned to Tag 0EA4, Gabber).
Item 3 etale/smooth/factor:   CONFIRM_WITH_CORRECTIONS
  - main chain CONFIRMED (0AH7 for smoothness);
  - audit Sec 2.4 fallback "affineness descends fpqc" REFUTED AS ARGUED
    (explicit counterexample); fallback conclusion retyped OPEN; main theorem unaffected.
Item 4 units/rational/kappa:  CONFIRMED (directions checked; generic finiteness necessary;
                              etaleness adds nothing).
Item 5 Miyanishi--Sugie:      CONFIRM_WITH_CORRECTIONS (1980 = cylinder theorem;
                              separate extension step identified; no base change,
                              no field extension; numbering unfetchable, disclosed).
Item 6 base + fibres:         CONFIRMED (dichotomy exact; P1 branch real; fibre lemma
                              independently re-proved; multiplicities and counts
                              uncontrolled; "reduced fibre" wording repair).
Item 7 controls:              CONFIRMED (cone, elliptic cone, Whitney sheet, F_n minus S;
                              no counterexample found).
Item 8 firewall:              CONFIRMED (no numeric import; primitive sector untouched;
                              Euler identity typed as successor seed only).
```

## 10. Execution disclosure

Network fetches performed and used as primary evidence: Stacks tags `0ECD`,
`0EA4`, `0EB7` (Hartshorne–Lichtenbaum ingredient; title only), `0AH7`
(statements extracted from the live pages); Brenner `arXiv:math/0209298`
title, abstract, and the introduction's Nagata paragraph; DOI resolutions
for Miyanishi–Sugie 1980 and Gurjar–Miyanishi 2005 (titles and venues only;
interior text JS-blocked/paywalled — the two consumed statements are
therefore also independently proved or reconstructed above).  Nagata's 1956
paper itself was not fetched; the audit's use is covered by the fetched
Brenner attribution plus the independent proof in Section 1.1.  No CAS was
run; the only computation is the hand-checked identity
`(t^3-3xt)^2-4x^3=(t^2-x)^2(t^2-4x)` and small intersection numbers.
`jc2-lean` was not inspected, listed, or touched; no q6/D3 report or
sibling external-model material was read; no input, Git state, or canonical
artifact was modified.  This review makes no exit-price assertion and emits
no `charge_basis` line; receipt status `ABSENT` is expected.

## 11. Maximum safe theorem

> **Proper-block ruling theorem (repaired form).**  Assume a noninvertible
> complex Keller map admits a proper intermediate field, with promoted
> block factorization `A2 --g1--> Y --g2--> A2` and full source non-etale
> support `R = NonEt_Y(g2)`.  Set `U = Y minus R`.  Then:
> `U` is a smooth rational affine complex surface (affine by Stacks `0ECD`
> applied to the finite-type `g2` with `Y` affine, or equivalently by
> Nagata's dimension-two theorem via purity `0EA4`); the actual first leg
> factors as a dominant etale quasi-finite `g1: A2 -> U` of generic degree
> `d1`; `O(U)^* = C^*` and `bar-kappa(U) = -infinity`; `U` admits a
> surjective `A1`-fibration `rho: U -> C` with `C = A1` or `C = P1`, with
> no base change or field extension; and every fibre of `rho`, taken with
> its reduced structure, is a disjoint union of affine lines.  Moreover
> `e(U) = e(C) + sum_t (q_t - 1) >= e(C)`, where `q_t` counts reduced fibre
> components at degenerate values.
>
> Uncontrolled: fibre multiplicities; the number of degenerate fibres and
> components; the choice between the two bases; every numeric cap of the
> quadratic presentation; existence of the block; and everything about the
> primitive sector.

## 12. Exact dependencies and cheapest decisive successor

Dependencies, in consumption order: promoted block structure theorem
(items 1–4 of the structure integration); Stacks `0ECD` (or: Gabber purity
`0EA4` + Nagata via Brenner) for affineness; `0AH7` + characteristic zero
for smoothness; dominance for units; Castelnuovo + Lüroth for rationality
of `U` and `C`; Iitaka log monotonicity for `bar-kappa`; Miyanishi–Sugie
1980 + the cylinder-to-fibration extension (Miyanishi's book, as quoted by
Dubouloz–Kishimoto); the fibre lemma (re-proved here from boundary
connectedness and genus-zero fibre trees).  The class-lattice injection and
nonprincipal different (Galois integration) are consumed only to bar the
principal-open shortcut, not by the theorem itself.

Cheapest decisive successor: **BD-A1-EULER-LEDGER** — promote the
presentation-free identity `e(U) = e(C) + sum_t (q_t - 1)` block-generally
(free half, review-only), then produce the sandwich-side ledger
`e(U) = e(Y) - e(R)` with `e(Y)` computed from the finite flat `g2` by
stratification over the discriminant curve and `e(A2)=1` propagated through
the etale quasi-finite `g1` with nonproperness corrections along `A(g1)`.
Any wedge between the two ledgers is a numeric constraint on `d1, d2`, the
base branch, or the fibre counts that — unlike everything in Section 8's
forbidden list — would be born block-general.  Secondary successor, dearer:
a `d1 >= 2` obstruction for the `P1` base (the `F_n minus S` control only
realizes generic degree one, so the branch is genuinely open).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31098`.
- Body SHA-256:
  `f2b0d3ae2f800e3a9958bc9c467db219cd16025ddfd42d459b78341eddd86d6f`.
- Frozen basis: `5cc7b50274df491cb09dbb91a8b528de77fc5ef4`.
