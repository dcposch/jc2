# Cross-comparison: two-pole full-actual first separation

**Date:** 2026-08-29  
**Basis:** `76c746f698103d20019bfeb72654a361ccc5371d`  
**Compared researchers:** Sol 5.6 Ultra and blind Opus 5 (`effort=max`)  
**Disposition:** **CONVERGENCE on `PROVED_FULL_TWO_POLE_ATTACHMENT`**, still
provisional pending a hostile review.

## 0. Sealed inputs

Sol producer:

```text
82d2f6c3eb2c3985569da428def3d5c2e125ca5b0aa29ebfc7973b68ee843a7a
  xmodel/m2-two-pole-full-actual-first-separation-theorem-r1-sol56-20260829.md
sealed body: 21235 bytes
0c808734cf2f0c98d085503e8d0aaf8e0ca645c34adfb925c757d0beb6223428
```

Blind Opus producer:

```text
f7853d39a17fd7329feaec101f1767ef5edddd07a2f0d5f8030a0cb023f95efe
  xmodel/m2-two-pole-full-exit-attachment-primary-opus5-76c-20260829.md
sealed body: 61389 bytes
2fe6a14ca8a04033d176547704de20ccd7d1c7e5dd19599970dffab3a60cbe18
```

Blind-lane custody:

```text
ecf2698309884684da7db084f5d9526f7f910e84bed8180a612808c39da2cc3d  prompt
d1f7a4eb773b1c189e7bf294659a7be867f99461bacf86705f5656dbe2184460  log
05f48d1e666a6748c7f83b66f03b14d6be1273ef0655f6cab844728437307a7f  run.v2
```

The run header records exact `model=opus effort=max`, basis `76c746f...`,
exit code 0, `final_status=DONE`, and
`charge_basis_status=VALID:2:2/3,2/3`.  Both report-body seals were
recomputed independently.  The common 18-file source perimeter reproduced
its pinned hashes after the run; HEAD remained `76c746f...`.

## 1. Clause-by-clause comparison

| load-bearing clause | Sol route | Opus route | comparison |
|---|---|---|---|
| contact ultrametric | coherent `Omega` reduces to first-difference ultrametric | same, plus an independent deck-substitution proof | agree |
| physical flag tree | Definition 3.3 gives representative-independent root segments and no remerging | Theorems A3--A4 give the same equivalence and meet formula | agree |
| no later quotient | transition objects remain points/subsets of `T_a^*` | exhaustive typed sweep in Proposition A6 | agree; Opus gives fuller source inventory |
| pole union | `A_P=[0,max_j min(v_j,O(P,P_j))]` | identical Lemma A7 | exact agreement |
| unique off-`U` attachment | grid refinement makes an off-`U` microchild's last union height equal `u` | Theorem C1: any later pole intersection forces its coefficient into the chain-arrival set `Ch(F)` | agree; Opus route is cleaner and grid-free |
| root orbit to child | Statement 3.16 plus corrected 3.18 gives one actual child per effective orbit | Lemma B1 independently reconstructs existence/uniqueness and identifies corrected 3.18 as a section, not a quotient | agree |
| hostile countermodel | later equality violates `w<=O(P,Q)` after distinct children split | identical, localized to Definition 3.3(ii) with Definitions 3.2/Statement 3.2 | exact agreement |
| full carrier | `E_all(F,d)` is the set of unique same-ray cv flags for every place through the up child | same definition through `P(F,c)` and corrected Statement 3.13 | exact agreement |
| full coverage | Statement 7.3 is universal in each physical place `P`; place-to-flag may be many-to-one | same literal p. 35 quantifier, with an intrinsic closure characterization | exact agreement |
| disjointness | every member retains attachment `F`; different children/attachments are disjoint | Theorems C1--C3 | exact agreement |
| one budget | apply repaired C7.1 once to the disjoint union plus the x-side flag | Theorem C4 | exact agreement |
| LL-1 cells | four nonzero floors become 2; epsilon stays `1,1,1,0` | independent P0 arithmetic gives totals `3,3,3,2` | exact agreement |

The two proofs are genuinely complementary.  The Sol route first proves the
abstract ray-intersection formula, then uses a sufficiently divisible cover
grid to locate a microchild's attachment.  Opus avoids the grid in the
load-bearing step: if a ray in the realized coefficient cluster met a pole
segment above `F`, its coefficient at `F` would equal the continuing pole
coefficient and hence be a chain arrival, contradicting the exit type.  This
argument automatically covers a pole endpoint and any number of pole rays
through a merge.  It is the preferred presentation for hostile review.

## 2. Type separation: orbit, place, flag

Both proofs preserve the three distinct carrier levels:

```text
effective root orbit
  -> one actual microchild coefficient/component (corrected Statement 3.18)
  -> a finite cluster of physical places whose rays contain that child
  -> one unique cv carrier on each such ray (Statement 7.3 + corrected 3.13)
  -> E_all as a SET of distinct physical flags.
```

The first arrow is injective across effective orbits.  The second arrow is
not a cardinality equality: one child may contain several physical places.
The last map is deliberately allowed to be many-to-one: several places may
share one cv flag.  Corollary 7.1 charges that shared flag once.  Distinct
children cannot share a later flag because Definition 3.3 forbids remerging;
different base vertices cannot share one because attachment is a function.

This is exactly the distinction the stable repricing rereview required.
Neither proof identifies root multiplicity, cover-series count, physical-place
count, and flag count.

## 3. C7.1 union and numerical perimeter

For any collection of priced actual up non-chain directions on the two-pole
union,

```text
S_y = disjoint_union_(F,d) E_all(F,d)
```

is a finite set of pairwise-distinct y-side cv flags on one prescribed fibre.
The separate x-side witness lies in the other Definition-3.3 component.
Thus the reviewed actual-weight Corollary 7.1 applies once to
`{H_x} union S_y` and gives

```text
sum_(F,d) sum_(H in E_all(F,d)) kappa_H(pi(H)-1)
  <= td(f,g)-1-psi.
```

The **attachment/disjointness theorem is independent of H5a**.  The numerical
floor is not: its consumer perimeter still imports the reviewed jump/max
reading of `kappa`, the positive-integral weight line, the actual-weight
Corollary 7.1 repair, the repaired 6.7/6.8 up/arrival typing, and the promoted
`L_safe` lemma.  Neither producer re-proves those inputs or claims
cross-fibre `kappa` transport.

At each of

```text
(17,5)@2, (51,15)@7, (85,25)@12, (119,35)@17,
```

the sole nonzero orbit has multiplicity 3, `(X,kbar)=(17,5)`, and
`delta=2/3`.  The exhaustive full-set alternatives are singleton with
`q>=2` or at least two flags; both give total weight at least 2.  Singleton
`q=1` would force the nonintegral exact weight `2/3` and is impossible.
The zero/epsilon summands remain `1,1,1,0`; no attainment is asserted.

Both reports pass `ops/validate_charge_basis.py` with
`VALID:2:2/3,2/3`.

## 4. One wording repair

Opus Section C.5 momentarily distinguishes the canonical name
`FULL_ACTUAL_EXIT` as if it additionally meant attainment.  That is not the
canonical definition.  `ladder/BOOK-OFFAXIS.md` explicitly defines
`FULL_ACTUAL_EXIT` as the complete actual carrier using the piecewise **lower
floor**, and says the floor is never an attainment theorem.

Safe dictionary:

```text
REPRESENTATIVE
  = one selected Statement-7.3 witness; legacy one-witness floor only.

FULL_ACTUAL_EXIT (canonical) = FULL_ACTUAL_FIRST_SEPARATION (precise tag)
  = all distinct actual cv flags below the up child, assigned to their unique
    first attachment in U and inserted once into C7.1; lower floor only.

ATTAINED_FULL_ACTUAL_EXIT
  = not proved and must not be inferred.
```

This is a nomenclature repair, not a mathematical disagreement.  Every
inequality and cell price in the Opus report is explicitly floor-valued and
its final disposition says `attainment NOT CLAIMED`.

## 5. Provisional disposition and hostile-review targets

Independent convergence supports:

```text
physical flag tree                              PROVED
root-orbit -> actual-child interface            PROVED (corrected St 3.18)
full per-place cv coverage                      PROVED (literal universal St 7.3)
full attachment/disjointness over two poles     PROVED
single C7.1 union                               PROVED at reviewed input scope
four LL-1 nonzero full-set floors               2,2,2,2
epsilon/zero floors                             1,1,1,0 (unchanged)
overall                                         PROVED_FULL_TWO_POLE_ATTACHMENT
attainment / landing / JC2                      NOT CLAIMED
```

A hostile review should concentrate on:

1. whether corrected Statement 3.18 really gives a section from effective
   root orbits to actual children, with no root-orbit/physical-place collapse;
2. whether Opus Theorem C1's coefficient/non-arrival contradiction is valid
   for every physical place through the child, including pole endpoints and
   merge vertices;
3. whether Statement 7.3 is literally universal in `P` and corrected 3.13
   makes the same-ray cv flag unique;
4. whether `E_all` as a set remains exhaustive when the place-to-flag map is
   many-to-one;
5. whether different full sets can share a flag despite Definition 3.3 or a
   unique attachment;
6. whether repaired C7.1 accepts their entire union plus the x-side flag in
   one application; and
7. whether any of H5a, integrality, or `L_safe` is being strengthened beyond
   its already reviewed scope.

No canonical, ladder, case, guardrail, or operations file was edited.  No
commit, push, web, AWS, or heavy CAS was used.  Hostile review remains the
next gate; no promotion is made here.

<!-- END-SEALED-BODY::m2-two-pole-full-actual-first-separation-cross-comparison-sol56-opus5-76c-20260829 -->

## Seal (outside the sealed body)

Convention: the sealed body is the byte range from the first byte through
and including the newline terminating the unique marker above.  This section
is excluded.

- Sealed-body bytes: `9484`
- Sealed-body SHA-256:
  `1026e3a240b93563a3f521acd07ab139f329a6658568f8dc2c83a4634c58ec22`
