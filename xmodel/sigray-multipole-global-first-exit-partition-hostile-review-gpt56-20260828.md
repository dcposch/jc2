# Hostile review — Sigray multipole global first-exit partition

**Date:** 2026-08-28  
**Reviewer:** GPT-5.6 Codex  
**Scope:** frozen producer only; no canonical or producer source was edited.

## Custody

The supplied frozen SHA-256 matches the live producer exactly:

```text
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8
  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
```

The directly consumed Section 7 and Section 9 packets also match the hashes
printed by the producer:

```text
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6  Section 7 producer
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8  Section 7 hostile review
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  Section 9 producer
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  Section 9 hostile review
```

The corrected 6.7/6.8 integration is `1e66bff1...`; its source audit,
different-model review, and correction are `c3d6ff92...`, `eb37373b...`,
and `050ccddd...`.  The formerly open Lemma 6.1 rider is now covered by R2
producer/review/correction `2fdbbee9...` / `5193e7b0...` / `607e0dcf...`.

## Verdict

**PASS-WITH-REPAIR.**

The claimed inequality is a correct graph-theoretic consequence of an
*ambient orbit-level rooted-tree lemma* that includes all selected cv flags.
The frozen input does not establish that lemma.  MP0--MP1 establish a finite
tree for the union of **down-vertex pole paths**, not for the quotient/orbit
object on which the selected cv flags and their direction witnesses live.
Accordingly the attachment/injectivity step is not yet licensed at the
advertised source perimeter.  This is a proof/citation blocker, not a found
counterexample to the inequality under the stated ambient-tree hypothesis.

The exact blocker is the jump from:

```text
U is a finite tree under F -> F^o
```

in MP0 to the producer's use of an ambient `T` in which every cv witness has
a unique root path, each orbit direction is a distinct child edge, and no
quotient identification can make two such child components meet.  MP0 says
only `T_a& cap V_a \ {(0,x),(0,y)} = U \ {(0,y)}` and records predecessor
facts on that down-vertex set; it does not state the needed assertion for
`T_(a,cv)` or for the cyclic-orbit quotient.  See
`ladder/SHEET6-MULTIPOLE.md` §§1--2, especially lines 53--67.  The frozen
producer itself labels the stronger fact “divergent directions never
remerge” without a supporting source theorem (producer lines 68--70), then
uses it essentially at lines 85--96 and 140--151.

## Required minimal repair

Add and prove/cite the following **orbit-tree attachment lemma** before MFE
is promoted:

> On a fixed fibre `f=a`, the y-side quotient of Puiseux flags by the
> relevant cyclic action, containing every transition direction-orbit and
> every flag in `T_(a,cv)`, is a rooted arborescence with root `(0,y)`.
> Its rootward-parent map is single-valued and acyclic.  The union `U` of
> pole paths is rootward closed in this arborescence.  A distinct local
> direction-orbit at `F` is a distinct child edge after quotienting, and
> each Statement-7.3 witness lies in the descendant component of that edge.

Equivalently, the repair may be stated only for the finite set of selected
directions and their 7.3 witnesses.  It must explicitly cover the quotient
level, not merely raw Puiseux representatives or `V_a cap T_a^searrow`.
With it, an outside witness has a unique first `U` vertex; witnesses from
different attachments or different child-orbits are distinct; and the
producer's equations (4.2) and (MFE) follow.  Also change “the unique
rootward continuation” in the three-way split to “when it exists” at the
root.

## Attack ledger

| attack | finding | disposition |
|---|---|---|
| Is `U` rootward closed? | Yes *inside the certified pole-path tree*: every suffix of a pole path is again in its union.  The proof needs the same statement in the cv/orbit object, which MP0 does not supply. | Repair needed only for ambient lift. |
| Can an off-`U` searrow direction evade a same-fibre pole? | No for a locally priced next-vertex direction satisfying the repaired bridge hypotheses.  The 6.8 recursion puts a pole on the same branch, hence its pole path contains the first edge. | Pass, conditional on `D_F` containing only actual local next-vertex direction-orbits. |
| Can a cv witness leave and reattach/remerge with `U`? | Forbidden by the required orbit-tree lemma, but not by MP0--MP1 as presently stated.  This is the load-bearing gap. | Blocked at current perimeter. |
| Can two cyclic direction-orbits give one flag? | The singleton repair counts conjugates in one orbit once and proves distinct child directions locally.  It does not by itself show injectivity after the global quotient/identification of cv flags. | Covered by the same orbit-tree lemma. |
| Are merge arrivals priced? | Correctly excluded.  The producer puts them in class 1; the two-pole merge rule says the other chain orbit is searrow and never lambda-charged. | Pass. |
| Are merge extras priced once? | Yes in the current explicit two-pole formula: `lambda(merge)=k*...`, once per non-chain orbit, not per incoming edge.  MP6 likewise has `k=0` at the all-M=1 merge and its `l` extras have no tree direction. | Pass at stated local-formula scope. |
| Does 7.3 give actual weight for each local price? | Yes.  Corrected 9.3 gives `kappa_H(pi(H)-1) >= price` for the cv vertex on the exit ray, while 7.3 gives its existence.  This is the exact quantity C7.1* consumes. | Pass. |
| Can C7.1* take all selected y flags and the x flag at once? | Yes once distinctness is proved: it is every-fibre and applies to any pairwise-distinct subset.  The Section 9 repair puts the x witness in the other component on that same prescribed fibre and supplies its `psi` weight. | Pass conditional on attachment/injectivity. |

### Details behind the passing rows

1. **Same-fibre pole manufacture.**  The repaired 6.8 recursion ends at a
   pole on the original branch, not merely an equivalent class
   (`sigray-prop67-prop68-source-audit-sol-ultra-20260828.md` lines
   290--316).  Its bridge distinguishes a grid microstep from the next
   vertex and proves the latter is down in the relevant raw-inequality case
   (lines 318--369).  This validates producer lines 112--119 once `D_F` is
   read as a priced local vertex direction, including at a merge.

2. **Local price and actual cv weight.**  The Section 9 repair gives the
   corrected minus-sign bound for precisely a down vertex, up exit child,
   and cv vertex on that ray (`sigray-section9-source-audit-sol-ultra-20260828.md`
   lines 252--276).  AF2 independently records the orbit-by-orbit version,
   its same-branch 7.3 witness, and local distinctness (SHEET6-AF2.md
   lines 91--137).  Thus no unproved multiplicity of a *cluster* is being
   used here.

3. **Merge accounting.**  `SHEET6-2POLE.md` lines 216--233 charge only the
   `k` northeast extras and explicitly exclude the other chain arrival.
   `SHEET6-MULTIPOLE.md` lines 81--86 records the all-M=1 merge's `k=0`
   and that its `l` q-only extras have no tree direction.  The frozen
   definition `lambda_F^exit=sum_(d in D_F) price(F,d)` is therefore the
   right consolidation, provided `D_F` remains a set of quotient orbits.

4. **C7.1* and the x side.**  The actual-weight repair states C7.1* for
   every fibre and every pairwise-distinct subset
   (`sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md`
   lines 29--41).  The Section 9 first-exit repair adds the x-side witness
   once and obtains the exact `td-1-psi` form (Section 9 audit lines
   329--338).  No fixed cross-fibre `kappa` transport or equality is being
   smuggled into this step.

## Concrete double-count stress test

No remerging counterexample exists after the required orbit-tree lemma: a
rooted arborescence gives every selected flag one rootward path and therefore
one first `U` edge.

There *is* a precise abstract countermodel to the currently cited input
perimeter.  Retain the MP0 tree `P -> F -> R`, so `U={P,F,R}`.  Let two
different local direction-orbits `d_1,d_2` at `F` lead to distinct raw
branches.  Suppose the cyclic/orbit quotient identifies their later cv
representatives `H_1,H_2` as one cv flag `H`, retaining both incidences.  Let
each local 9.3 price be one.  Then the producer's `D_F={d_1,d_2}` has
`lambda_F^exit=2`, while the pairwise-distinct C7.1* set is only `{H}` and
contributes one weight.  The MP0--MP1 assertions about `U`, the pole paths,
and their merges are unchanged.  What fails is exactly the unproved
single-valued parent/child structure of the **quotient** containing `H`.

The same diagram can make `H` appear attached to two different vertices of
`U`; that is the requested leave/re-enter/remerge failure.  It is not claimed
to be realised by Sigray's actual Eggers--Wall object.  Rather, it proves that
the finite down-vertex-tree statement alone cannot discharge the global
injectivity assertion.

## Theorem truth versus consumer conformity

**Theorem truth after the repair.**  The graph argument is then sound:
rootward closure gives a unique attachment, the 6.7/6.8 bridge excludes an
off-`U` down alternative, 9.3/7.3 price one witness in each distinct exit
component, and C7.1* is applied once to their union plus the x-side witness.
It proves only MFE.

**Current consumers are not yet GREEN consumers.**  This is intentional and
currently conformant with the pre-repair state:

- `SHEET6-2POLE.md` calls the shared sum an AMBER target because its global
  distinctness proof is owed (lines 138--152).
- `SHEET6-MULTIPOLE.md` likewise keeps MP8 conditional and quarantines
  `(22)`, `(22-cl)`, equality/slack, and no-refinement rhetoric (lines
  3--14 and 90--96).
- AF2 is a singleton/local pricing theorem; its local direction-distinctness
  does not itself update a multipole engine.

Therefore this review does **not** authorise changing a current engine or
ledger to GREEN.  After the orbit-tree lemma is landed, a consumer update
must use the vertex set `U` and one orbit-set `D_F` per vertex, excluding
arrival directions.  It must not revive literal `Y(F)`, printed (22),
`delta_a`, fixed `(22-cl)`, equality/slack, MP8's no-refinement claim, a root
`M!=1` inference, an exhaustive root census, or a `td=6` exclusion.

## Final classification

```text
Frozen inequality at its presently cited perimeter:       PASS-WITH-REPAIR
Ambient quotient/orbit attachment certificate:             BLOCKER
Local 6.7/6.8 same-branch pole bridge:                     PASS
Local 9.3/7.3 price-to-cv witness step:                    PASS
Single-fibre C7.1* plus x-side charge:                     PASS conditional on injectivity
Merge-arrival exclusion / one-time local pricing:          PASS
Printed (22), delta_a, (22-cl), equality/no-refinement:    REJECTED / quarantined
Automatic promotion of current two-pole or MP8 consumers:  NOT AUTHORISED
```

No heavy computation was needed.  `jc2-lean` was not entered, listed,
searched, read, built, modified, status-checked, or controlled in this
review.
