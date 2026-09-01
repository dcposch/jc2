# DOMRINA-REPAIR-REVIEW-GPT55-20260901

Review lane: `DOMRINA-REPAIR-REVIEW`.

Charged inputs:

```text
99fc1e5870fb74d48e3d14a156115ef625fa9ecbc5843f0d8dd4a138a920e9bf  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.VI7xNM/inputs/domrina-gap-repair-opus5-20260901.md
89d794a7b79d4e43092e2dac1215272fced8a1aa0d3436adffc4ab07b87d3a71  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.VI7xNM/inputs/domrina-ii-replay2-sol56-20260901.md
```

Official source:

```text
0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018  refs/domrina2000_izv64_four_sheeted_general_case.pdf
```

All three hashes were recomputed before reading and match the charged values.
The review uses the verified English PDF as the official source.  I also used a
local `pdftotext -layout` extraction only as a navigation layer; citations below
refer to printed PDF pages.

No exit-price assertion is introduced here, so the FALLACY-v2 `charge_basis`
line is not applicable.

## Executive Verdict

Item verdicts:

```text
(1) Theorem R1/R1'                         CONFIRMED
(2) Theorem R2                              CONFIRMED
    Theorem R2'                             REPAIRED-DIFFERENTLY
(3) NEW-LEMMA[DET-LINF-NONPOS]              CONFIRMED
(4) Fork residual in sections 5-7           FORK-CONSUMED-NOWHERE
(5) No-countermodel proof                   CONFIRMED, relative to stated packages
(6) Final ledger                            DOMRINA-II = SOUND-AFTER-REPAIRS
                                             modulo {D-O-I-mu2-trust-boundary,
                                             (F1)/(F2), (S1)/(S2)/(S4)}
```

The important qualification is R2'.  The repair proves the non-fork
inessentiality that is actually consumed downstream: vertices on the
`g2~`-side before a possible fork, and paths for which the possible fork
`h~` is an endpoint rather than an interior delta factor.  The broad sentence
"every nodal, non-fork vertex of `<v~ g2~> cap Delta` is inessential" should
not be banked without a crossing-fork argument: an induction from `g2~` cannot
pass through `h~` unless the fork itself has already been controlled.  This
does not reopen sections 5-7, because the PDF's later consumers never require
the open fork clause.

The printed Lemma 3.15 remains stronger than what is needed: its companion
inessentiality clause at `h~` is still
`OPEN[LEMMA-3.15-INESSENTIAL-AT-FORK]`.  The theorem chain does not consume
that open clause in sections 5-7.

## 1. `DET-LINF-NONPOS`

Claim reviewed: `det L~_infty <= 0`, unconditionally.

Verdict: **CONFIRMED**.

The proof in the repair has three ingredients.

First, `X~ - L~_infty = F^{-1}(C^2)` is affine.  The equality is supported by
Domrina II, p. 1-2: `X~, X` compactify the two planes, `L~ = X~ \ C~^2`,
`L = X \ C^2`, and `L~_infty = F^{-1}(L)`.  Since `F : X~ -> X` is regular
between compact varieties, the restriction over `C^2` is proper.  Quasi-finiteness
is also checked correctly.  A positive-dimensional fibre over `C^2` would
contain a complete curve.  It cannot lie in `C~^2 = X~ - L~`, since affine
space contains no complete curve.  If it lies in `L~ - L~_infty`, Proposition
1.2 says it lies in one of the two dicritical components `g1~, g2~`, but
Proposition 1.2 also says `F` is non-constant there.  Thus the restriction is
proper and quasi-finite, hence finite; the source over the affine base is
affine.

Second, the Hodge-index sign step is valid with the determinant convention
used in Domrina II.  The paper defines graph determinants as determinants of
`-A_Q`, where `A_Q` is the intersection matrix.  The whole boundary has
`det L = -1` on p. 3, and the Lemma 2.12 formulas on p. 7 have the same sign
normalisation.  Since `X~ - L~ = C~^2`, the boundary components span the Picard
group.  The intersection form on `Pic(X~)` has at most one positive direction,
so the restriction to the span of `L~_infty` has at most one positive eigenvalue.
If `det L~_infty > 0`, then that restricted form is nondegenerate and has zero
positive eigenvalues, hence is negative definite.

Third, the Grauert step is legitimate.  If the connected divisor `L~_infty`
were negative definite, Grauert contracts it analytically to a normal compact
surface `Z`.  The complement `X~ - L~_infty` is then `Z` minus finitely many
points.  A regular function on the complement is holomorphic there, extends
across those points by normality, and is constant on compact connected `Z`.
That contradicts the affineness and two-dimensionality of `F^{-1}(C^2)`.

There is no hidden division by a determinant in this proof.  The argument also
does not assert strict negativity; the conclusion is exactly the floor
`det L~_infty <= 0`, which is all Lemma 2.12 needs.

## 2. `ROOT-U-LAST-CHAIN`

Claim reviewed: Theorem R1 and R1', repairing Corollary 3.8(b), p. 10.

Verdict: **CONFIRMED**, with one harmless correction to the exposition.

The official problem is real.  Corollary 3.8(b) says that if a component
`U~ subset U^0` is incident to `g1~`, then `v~ notin delta(g1~ h~)` and the
relevant nodal vertices are inessential for `g1~`.  The printed proof only
cites Lemmas 2.3, 2.4 and Lemma 3.7(b).  Those lemmas require exact determinant
inputs at selected vertices, while Lemma 3.7(b) supplies only the structure of
branches over `U_c` and one positive linear branch.  The one-line proof is
under-specified.

R1 supplies the missing selected-vertex argument.  If
`v~ in delta(g1~ h~)`, choose the unique interior path vertex `q~` at which the
root hangs off the path, and put `B = br_{q~}(v~)`.  Since the path from
`g1~` to `g2~` runs through `q~`, Lemma 2.12 can be applied at `q~`.

The determinant checks survive hostile review:

```text
det(q~ g1~) = 1
det delta(q~ g1~) >= 1
det Q3 >= 1
det(q~ g1~) <= (det delta(q~ g1~))^2 det Q3
```

The first equality uses Lemma 3.7(b)'s branch dichotomy correctly.  The branch
towards `g1~` is neither the branch containing `h^0` nor the exceptional linear
`R_q` branch; if `g1~` is attached directly to `q~`, the interval is empty and
the determinant is `1`.  Otherwise it is one of the components of `F^{-1}(U_q)`,
and Lemma 3.7(b) gives determinant `1`.

The positivity checks do not divide by an unproved nonzero.  `delta(q~ g1~)`
does not contain the root and therefore has positive determinant by the
root-positivity lemma imported from [4].  `Q3` is a product of branch
determinants.  The root branch `B` is either a lifted `U_q` component of
determinant `1` or the positive linear branch from Lemma 3.7(b); all other
factors avoid the root and are positive.

There is one sentence in the repair that should be deleted or weakened: it says
that every branch hanging off the interior of `<g1~ h~>` is contained in `U~`.
The exceptional linear `R_q` branch need not be contained in `U~`.  The proof
itself immediately allows that case and uses only `B subset Q3`, not
`B subset U~`; therefore the overstatement is not load-bearing.

With `DET-LINF-NONPOS`, Lemma 2.12 forces `v~ in Q1 union Q2`, contradicting
`v~ in B subset Q3`.  R1 is confirmed.

R1' is also confirmed.  Enumerate the nodal vertices of
`<g1~ v~> cap U~` from `g1~` inward.  The same branch computation gives
`det(s_j~ g1~)=1`.  For the first nodal vertex, `delta(s_1~ g1~)` is empty.
After Lemma 2.3 makes `s_1~` inessential, all off-path branch determinants
behind the next vertex are `1`; induction gives `det delta(s_j~ g1~)=1` for
each subsequent nodal vertex.  No endpoint is skipped, and no conclusion is
used before it is proved.

The repair's correction of the printed second clause is also right.  The PDF
prints a `delta(g1~ v~) cap U~` inessentiality phrase, but Definition 2.2 only
defines essentiality for nodal vertices on the closed path `<g_i~ v~>`.  The
usable and typed statement is with `<g1~ v~> cap U~`, matching the parallel
wording in Lemma 3.15.

## 3. `ROOT-DELTA-G2-APPLICATION`

Claim reviewed: R2 and R2', repairing Lemma 3.15, p. 14-15.

Verdict for R2: **CONFIRMED**.

Verdict for R2': **REPAIRED-DIFFERENTLY**.

Lemma 3.15's printed proof supplies a structure package and then cites Lemma
3.7(b), Lemma 2.5 and Lemma 2.6.  The structure package extracted in the repair
is faithful to p. 15:

```text
(S1) det delta(a~ g2~) > 0.
(S2) each component of delta(a~ g2~) - U^0 is linear.
(S3) every nodal non-fork s~ in <a~ g2~> has det(s~ g2~) = 2.
(S4) the only possible fork of Delta is h~, and U^0-components at h~ have determinant 1.
```

This review treats `(S1)`, `(S2)` and `(S4)` as structure-package trust inputs,
exactly as the repair declares.  `(S3)` is independently recoverable from
Proposition 3.4, Lemma 1.5, Proposition 1.3 and Definition 3.2, provided the
selected vertex is non-fork.  That non-fork condition is essential.

For R2, suppose `v~ in delta(a~ g2~)`.  Let `q~` be the interior vertex of
`<a~ g2~>` at which the root hangs and let `B = br_{q~}(v~)`.  Because `Delta`
is incident to `g2~` and non-incident to `g1~`, the full `g1~`--`g2~` path
passes through `a~` and then through `q~`; Lemma 2.12 is available at `q~`.

If `q~` is not the fork, then `B` is linear by `(S2)`, `det(q~ g2~)=2` by
`(S3)`, and `det delta(q~ g2~)` is a positive integer because it avoids the
root.  If that determinant is at least `2`, Lemma 2.12 gives an immediate
contradiction.  If it is `1`, Lemma 2.5 gives `q~` inessential for `g2~`; the
corrected `g2~` form of Lemma 2.6 then applies because the route from `q~` to
`v~` is linear.  Lemma 2.6 gives `det B < 0`, while `(S1)` and root-positivity
give `det B > 0`.  No negative-branch determinant is left floating.

If `q~ = h~`, the repair correctly separates the two numerical possibilities.
When `n(h~)=1`, `det(h~ g2~)=1`, and Lemma 2.12 again contradicts
`v~ in Q3`.  When `n(h~)=2`, the case is empty: the local degree formula and
Riemann-Hurwitz force `Deg(h~)=4`, `m(h~)=2`, and `h^0={h~}`.  The
valency-three case overcounts local branches.  In valency four, the count
leaves exactly one `U^0` component at `h~`; since `g1~` is incident to a
`U^0` component and `h^0` is a singleton, that component would lie in `Delta`,
contrary to the hypothesis that `Delta` is non-incident to `g1~`.

This proves the first conclusion of Lemma 3.15 over the stated structure
package.

R2' needs sharpening.  The induction from `g2~` inward is valid until it reaches
the possible fork `h~`: each prior non-fork has `det(s~ g2~)=2`, and the
previously proved inessential vertices make the required `delta` determinant
equal to `1`, so Lemma 2.5 applies.  But if a later non-fork vertex lies on the
far side of `h~`, the determinant `det delta(s~ g2~)` includes the off-path
branches at the fork.  Without the still-open inessentiality of `h~`, the
induction has not proved that product is `1`.  The repair's sentence "identical
induction to R1'" quietly crosses the fork unless it is read with this stop rule.

The downstream-safe replacement is therefore:

```text
R2'-usable:
Every nodal non-fork vertex on the g2~-side before the first possible fork h~
on the relevant Delta path is inessential for g2~.  The same holds on any
consumer path for which h~ is not an interior vertex of the delta product.
```

The fork itself remains open in the repair's own sense:

```text
OPEN[LEMMA-3.15-INESSENTIAL-AT-FORK]
```

This is not a refutation of R2.  It is a scope correction for the companion
inessentiality clause.

## 4. Fork Consumer Audit

Task: intersect the sections 5-7 dependency graph with the residual
`OPEN[LEMMA-3.15-INESSENTIAL-AT-FORK]`.

Verdict: **FORK-CONSUMED-NOWHERE**.

I found every direct occurrence of "Lemma 3.15" in the official PDF after the
lemma itself.  The list below records the mathematical use, not just the
dependency tag in the replay.

```text
Lemma 5.3(2), p. 18:
  The paper uses Lemma 3.15 to make (a~ g2~) linear.
  In Fig. 12 rows 1-4, h~ is on the g1~-side of a~; the a~--g2~ route has no
  interior h~.  Uses R2/R2'-usable only.

Lemma 5.3(3), p. 18:
  Uses Lemma 3.15 with Lemmas 2.7/2.8 to make the a~--g2~ and v~--a~ pieces
  linear while v~ lies in (h~ a~).
  h~ is not an interior delta factor on the consumed g2~ route.  No fork use.

Lemma 5.3(4), p. 18:
  Uses Lemma 3.15 to make (v~ g2~) linear after v~ is already on (a~ g2~).
  The possible fork h~ is outside that open route.  No fork use.

Lemma 5.4(3), p. 19:
  Uses Lemma 3.15 and Assertion 5.2 to make (v~ g2~) linear.
  The selected vertices are on the g2~-side route; no h~ inessentiality is used.

Lemma 5.5, p. 19:
  Uses Lemmas 2.5 and 3.15 to force v~ into D_h~ when v~ is not in (h~ g2~).
  The h~-inessentiality used later in this lemma is obtained directly from
  Lemma 2.5 in the det(h~ g2~)=2 branch, not from the open det=1 fork case of
  Lemma 3.15.  No fork residual is consumed.

Lemma 5.6(1), p. 19-20:
  Uses Lemma 3.15 to make (h~ g2~) linear.
  h~ is an endpoint of that open interval; delta(h~ g2~) does not include
  branches incident at h~.  No fork use.

Lemma 5.6(3), p. 20:
  Uses Lemma 3.15 to make (v~ g2~) linear after v~ lies in (h~ g2~).
  The segment from v~ to g2~ is strictly on the g2~-side of h~.  No fork use.

Lemma 5.7(1), p. 20:
  Uses Lemma 3.15 to make (h~ g2~) linear.
  Again h~ is an endpoint, not an interior delta factor.  No fork use.

Lemma 5.8(1), p. 21:
  Uses Lemma 3.15 for det delta(a~ g2~)=1.
  In rows 11-12 the subsequent sentence places h in the left/type-3 side
  controlled by Lemma 3.16; h~ is not an interior vertex of a~--g2~.  No fork use.

Lemma 5.10(3), p. 22:
  Uses Lemma 3.15 with Lemmas 2.7/2.8 to make the v~--a~ and a~--g2~ pieces
  linear.  This is the same right-vertex g2~ route as the class 1b/1c setup.
  No fork use.

Lemma 5.10(4), p. 22:
  Uses Lemma 3.15 to make (v~ g2~) linear with v~ already in (a~ g2~).
  No fork use.

Lemma 5.11(2a), p. 22:
  In the lower-arm case a=h and v~ lies in (a~ g2~)=(h~ g2~).
  Lemma 3.15 supplies only the g2~-side linear/unit data beyond v~; h~ is behind
  v~ and not in delta(v~ g2~).  No fork use.

Lemma 6.1, p. 23:
  The lower-port subcases use Lemma 3.15 in the canonical substitutions for
  v~ in (a~ b~) and v~ in (a~ g2~).
  The possible h=b type-1 port is treated separately before those subcases.
  The consumed g2~ data are non-fork or endpoint data.  No fork use.

Lemma 6.7, p. 26:
  Uses Lemma 3.15 to make (a~ g2~) linear.
  The possible h~ is not consumed as an interior inessential vertex.  No fork use.

Lemma 6.8(2), p. 26:
  Uses Lemma 3.15 to make (a~ g2~) linear while the root is in br_a~(b~).
  The argument needs the g2~ route, not h~ inessentiality.  No fork use.

Lemma 7.8, p. 32:
  Uses Lemma 3.15 for det delta(b2~ g2~)=1.
  In Fig. 14, b2~ is the right fork endpoint of the g2~ route.  If b=h, then
  h~ is still an endpoint of delta(b2~ g2~), and endpoints are excluded from
  the delta product.  No fork use.

Lemma 7.9, p. 32:
  Uses Lemma 3.15 in the canonical data after v~ is assumed in (b2~ g2~).
  The path to g2~ is strictly beyond b2~, so an h~=b2~ fork is behind the root
  segment.  No fork use.

Lemma 7.10, p. 32:
  Uses Lemmas 3.15 and 7.5 to assert
  det delta(b2~ g2~)=det delta(g1~ a2~)=1.
  The Lemma 3.15 half is again delta(b2~ g2~), with the possible fork at the
  endpoint b2~, not inside delta.  No fork use.
```

All other entries in the replay's dependency graph are transitive through these
direct consumers.  Therefore the residual does not propagate to the theorem.
The exact fork ledger is:

```text
FORK-CONSUMED-AT[ ] = empty
FORK-CONSUMED-NOWHERE
```

## 5. No-Countermodel Proof

Verdict: **CONFIRMED**, relative to the stated structural inputs.

The repair's no-countermodel paragraph is not a finite enumeration of
convenient cases.  It rests on R1 and R2 as determinant/geometry theorems over
the state space supplied by Domrina II plus the declared structure packages.

For `ROOT-U-LAST-CHAIN`, a countermodel would be a source tree satisfying
Proposition 1.2, Proposition 1.3, Lemma 3.7's branch package, and the determinant
conventions, with the root hanging from the interior of `<g1~ h~>`.  R1 excludes
that configuration for an arbitrary selected hanging vertex `q~`; no case list
or bounded enumeration is used.

For `ROOT-DELTA-G2-APPLICATION`, a countermodel to the first conclusion of
Lemma 3.15 would satisfy `(S1)`-`(S4)` and have the root in
`delta(a~ g2~)`.  R2 excludes all possibilities: non-fork `q~` by Lemma 2.12
or Lemma 2.5/2.6, and fork `q~=h~` by the `n(h~)=1` Lemma 2.12 branch plus the
`n(h~)=2` Riemann-Hurwitz emptiness argument.  Again, this covers the full
declared state space; it is not a search over sample diagrams.

The proof is not absolute over arbitrary weighted trees.  It is conditional on
the same packages the repair names:

```text
(F1)/(F2) from Lemma 3.7;
(S1)/(S2)/(S4) from the undisputed structural part of Lemma 3.15;
REPAIRED[LEMMA-2.6-g1-TO-g2] from the first-half replay;
the D-O I technical determinant/canonical formulas at their stated hypotheses.
```

That is an honest theorem-relative-to-inputs, not an enumeration.

## 6. Final Ledger

The final ledger line I recommend is:

```text
DOMRINA-II = SOUND-AFTER-REPAIRS
modulo {
  D-O-I-mu2-trust-boundary,
  structure packages (F1)/(F2)/(S1)/(S2)/(S4)
}
```

Do not include the fork residual in the theorem ledger: sections 5-7 do not
consume it.  Do retain it as an unbanked statement about the full printed Lemma
3.15:

```text
LEMMA-3.15 full companion inessentiality at h~ = OPEN, unused by sections 5-7.
R2' universal non-fork formulation past h~       = not promoted.
R2'-usable non-fork-before-fork formulation      = confirmed and sufficient.
```

Expanded disposition:

```text
NEW-LEMMA[DET-LINF-NONPOS]               = CONFIRMED
GAP-CANDIDATE[ROOT-U-LAST-CHAIN]         = CONFIRMED-REPAIRED
GAP-CANDIDATE[ROOT-DELTA-G2-APPLICATION] = CONFIRMED-REPAIRED for root exclusion
LEMMA-3.15 non-fork downstream use        = CONFIRMED under R2'-usable
OPEN[LEMMA-3.15-INESSENTIAL-AT-FORK]     = OPEN but FORK-CONSUMED-NOWHERE
NO-COUNTERMODEL                          = CONFIRMED relative to packages
DOMRINA-II theorem chain                  = SOUND-AFTER-REPAIRS modulo stated trust boundaries
```

This is stronger than the replay-2 ending, because both inherited root
obligations have now been repaired for the portions the theorem actually uses.
It is weaker than promoting every sentence of Lemma 3.15, because the fork
inessentiality clause remains open and the broad R2' induction cannot be pushed
past that fork without a new argument.

## 7. Hostile Checklist

This section records the failure modes I specifically checked before promoting
the ledger line.

Unproved nonzeros.  R1 and R2 use Lemma 2.12 only after proving the relevant
`Q3` determinant is positive.  R1 proves positivity factor-by-factor from
Lemma 3.7(b) and root-positivity.  R2 proves `det B > 0` from `(S1)` plus
root-positivity for every other delta component; this is a product argument in
integers, not a cancellation by an unknown determinant.  The only cancellation
in the R2 fork count is `Deg(h~)=m(h~)n(h~)` with `n(h~)=2`, and that is a
local degree identity, not a determinant division.

Endpoint and last-segment indices.  R1 selects the first path vertex `q~` where
the root leaves `<g1~ h~>`.  The branch toward `g1~` and the branch toward `h~`
are then distinct, so `Q1`, `Q2`, and `Q3` in Lemma 2.12 are disjoint in the
required way.  R1' orders only nodal vertices on `<g1~ v~> cap U~`, so the
base case has empty delta and the induction never asks for a determinant past
the root.

Circularity.  R1 consumes Corollary 3.8(a), Lemma 3.7(b), and `DET-LINF`, but
not Corollary 3.8(b).  R2 consumes the structural part of Lemma 3.15's proof,
but not the conclusion `v~ notin delta(a~ g2~)` and not the fork
inessentiality clause.  The only imported correction from replay-1 is the
typed `g2~` version of Lemma 2.6.

Sign conventions.  The edge determinant identity is used with Domrina II's
`det L=-1` convention.  The sign is independently visible in Proposition
1.3(2d), p. 3, and in the displayed proof of Lemma 2.12, p. 7.  R2's negative
branch determinant is not treated as a contradiction by itself; it is compared
to the separately proved positivity of the same branch `B`.

Fork restriction.  The non-fork word in R2' is necessary but not sufficient if
one wants the full printed Lemma 3.15.  A non-fork vertex located beyond `h~`
from `g2~` would require `det delta(s~ g2~)=1`, and that delta product sees
the off-path branches at `h~`.  The report therefore banks only the
before-fork/endpoint-safe version.  The consumer audit above is what permits
the final theorem ledger to close without banking the full fork clause.

Figure/label discipline.  I did not identify repeated numerals across different
figures or branches.  The section 7 labels `d0,d1,d2,d3` remain figure
parameters, while the canonical degrees in Lemmas 2.9-2.11 are separate
variables.  This matters most in Lemma 7.9, where the printed `d2=2` is not
the later canonical `D2=4`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->`
  line, including its terminating newline; this seal is outside the body.
- Body bytes: `21058`
- Body SHA-256: `36635c98876fb866c1f31f2b919c342865ca7cb971b9b9de4e2c988382781e5d`
- Frozen basis: `e7130d487508479fc67cd95ff7ca6dc0d9265b91e097f19cca871e25dcd8751d`
