# q=6 degree-zero typing adjudication

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `f63b8bd9400ff86eb385c2f705e885015c624068`  
Lifecycle: **EXACT PROVISIONAL REPAIR / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

The sole mathematical gap raised by the Opus 5 hostile review of the
corrected q=6 affine-ADE threat map is a type conflation, not an omitted
configuration.  A class such as `F-P_i-P_j` can have `A`-degree zero, but if
it also has `B`-degree zero then it is an exceptional Du Val root, not a
strict/nonexceptional polar prime.  At the charged F5 point the relevant
classes already occur in the subtracted exceptional divisor `M_R`.

Every irreducible component with `A.C=0` lies in exactly one of two charged
types:

```text
B.C=0: r-exceptional Du Val root, already in the local/ADE allocation;
B.C>0: nonexceptional pi-contracted carrier Z_J, already in the +Z cells.
```

All other nonexceptional primes have positive `A`-degree.  Their registered
local germs already consume the full global weighted `A`-degree eight.
Therefore no extra degree-zero strict prime and no finite replay extension is
needed.  Conditional on the charged local-contact and binding global inputs,
the v2 enumeration remains exhaustive and its zero survives without the
review's added “no `A`-degree-zero component” hypothesis.

Two unrelated Opus corrections remain binding: the overall zero does depend
on the connected root/block machinery in the old positive-`a` domain, and
the degree-one vertical candidates are eliminated by the exact join, not by
the diagnostic energy inequalities.

## 1. Frozen evidence and notation

```text
8fea7f545f058d1968ff3a402695f2d7d4bb8e4e15b280c4f2f942132e89e6f4
  xmodel/bd-a2-q6-affine-ade-threat-map-v2-sol56-20260830.md
cc55620b3d1a3fe61c3e22b7c8251f4550515836beeaa7a02bf7462572b780e6
  xmodel/bd-a2-q6-affine-ade-threat-map-v2-sol56-20260830.md.artifact.json
c2ca2874b9bf80a9612010d034118d0f854a9c0cb6167b0865d22470374a0c56
  ops/q6_f5_affine_ade_threat_replay_v2.py

d92beb90aef85742711c5a41e7c9558cb6db64101783de95a5b0d89588fdad74
  xmodel/bd-a2-q6-affine-ade-threat-map-v2-hostile-review-opus5-20260830.md
  body c968ed6f60b3cd65868050a49180a5f5bbc37ae2241042e9aa6870290f75c90f

48717ce3d8b3c5ef6926e3b5ebcf2a0d94ad7bee42ea4ea1c253fb4fd9463649
  xmodel/bd-a2-q6-local-contact-audit-sol56-20260830.md
a5bf78c8ab8704884e9bb3c084c88059e01ec7690c1d6f645a9e87a0aa70a884
  xmodel/bd-a2-normal-f5-decorated-carrier-effectivity-reduction-coordinator-integration-sol56-20260830.md
17f41e706bcae7556cd99e019263e7fad254201fe51f9a24ed158b2be68560c6
  xmodel/bd-a2-normal-singular-quadratic-incidence-coordinator-integration-sol56-20260830.md
```

On the minimal Du Val resolution `r:Xtilde->X`, use the charged nine-blowup
basis

```text
B=F,
A=2S0+5F-sum_i P_i,
H=L+S0+T,
A+B=r^* O_X(1,1).
```

Both factors of `O_X(1,1)` come from the ambient
`P2 x P1`; its restriction to `X` is ample.  The strict/nonexceptional
ramification components are kept separate from `r`-exceptional roots and
from nonexceptional curves contracted by `pi:X->P2`.

## 2. Exhaustive `A`-null trichotomy

Let `C` be an irreducible effective curve on `Xtilde` with `A.C=0`.

### 2.1 The `A.C=B.C=0` case is exceptional

Here

```text
(A+B).C=0.
```

Because `A+B` is the pullback under `r` of an ample line bundle, the
projection formula forces `r(C)` to be a point.  Thus `C` is
`r`-exceptional.  The singularities are Du Val, so every irreducible
exceptional curve is a `(-2)`-root.  It is not a strict/nonexceptional polar
prime and must be typed in the ADE allocation or in the fixed exceptional
divisor at the F5 point.

The lattice classification can be checked directly.  Write

```text
C=bF-sum_i x_iP_i
```

because `B.C=0` kills the `S0` coefficient.  Then

```text
A.C=2b-sum_i x_i=0,
C^2=-sum_i x_i^2=-2.
```

Hence exactly two `x_i` are `+/-1`.  Up to sign, the only roots are

```text
P_i-P_j,                    F-P_i-P_j.                 (2.1)
```

The first family is exactly the already-enumerated difference-root
allocation, including the charged `A5(I)+A1(O)` domain.  The second family
meets the retained section:

```text
S0.(F-P_i-P_j)=1.                                      (2.2)
```

An affine exceptional tree is disjoint from `H`, so (2.2) excludes the
`F`-root family away from the unique exceptional tree at the F5 point.  At
that point it is not missing: the charged chronological local audit gives

```text
B3/A2: R1=F-P_l-P_o1,
U3/A3: E1=F-P_o1-P_o2.                                (2.3)
```

These curves occur in the exceptional multiplicity sum `M_R` that is
subtracted before forming `C_str`; neither can simultaneously reappear as a
distinct strict prime.

### 2.2 The `A.C=0`, `B.C>0` nonexceptional case is a carrier

If `C` is not `r`-exceptional, `A.C=0` says that its image on `X` is
contracted by `pi`.  A positive-dimensional fibre of the cubic incidence
over a target point is the full coefficient-source `P1`; therefore
`B.C=1`.  The binding carrier theorem classifies it exactly as

```text
Z_J=S0+2F-sum_(j in J)P_j,       |J|=5,
A.Z_J=0,                         B.Z_J=1.              (2.4)
```

For the q=6 marking,

```text
J=O union K,                     K subset I, |K|=3.    (2.5)
```

The nonzero-`tau` strict total has both outside multiplicities equal to one;
every `Z_J` uses both, so its total coefficient is at most one.  This is
exactly the registered `+Z` alternative.  In the `tau=0` total one required
outside multiplicity is already zero, so no `Z_J` is effective and no `+Z`
cell exists.  Thus the existing rows exhaust (2.4), including multiplicity.

### 2.3 Positive `A`-degree leaves no hidden component

Every remaining nonexceptional prime satisfies `A.C>0`.  At the F5 cluster,
the registered physical polar germs in every one of the nine local strata
have total weighted degree

```text
sum_j w_j A.C_j=8.
```

The global strict ramification identity has the same total.  Exceptional
roots and `Z_J` carriers have `A`-degree zero.  Consequently the registered
germs exhaust every positive-degree nonexceptional prime as well; an extra
prime away from the cluster would make the global total exceed eight.

Sections 2.1--2.3 are exhaustive.  The hostile review's suggested class
`F-P_i-P_j` is real, but it belongs to the first case and is already present
in (2.3), not in the strict-prime degree multiset.

## 3. Adjudication of the hostile review

The Opus review correctly confirms all marked-surface formulas, the corrected
`a>=0` domain, the local analytic census, the finite software, ordinary and
optimized replays, mutations, all 28 deltas, the rank-zero controls, and zero
pair-condition matches.  Its independent relaxed enumerator proves a useful
strengthening: on the newly added `min(a)=0` slice, the class identities,
adjunction, weighted totals, and pair rule alone already give zero matches.

Adjudicate its four requested corrections as follows.

1. **Degree-zero scope gate: discharged by Section 2.**  Remove the proposed
   additional hypothesis.  Do not say that `A` is ample; use the ample
   pullback `A+B` to type curves that are null for both rulings.
2. **Root/block dependence: accept.**  The total zero in the old positive-
   `a` domain consumes `connected_coordinate_blocks` and
   `branch_differences`; the review found 11 relaxed positive-`a` matches if
   that machinery is discarded.  Independence holds only from the unused
   energy pruning and the post-match carrier/unlabelled-cycle filter.  The
   new `a=0` delta is independently root-machinery-free.
3. **Energy attribution: accept.**  Since `energy_pruning_applied=false` in
   every row, degree-one vertical candidates are covered by the exact join,
   not by inequalities (4.1)--(4.2).
4. **Optional strengthening: accept.**  Record the relaxed `a=0` zero as a
   robustness check, not as a replacement for the positive-domain root
   allocation.

No code change is needed: the alleged omitted objects are deliberately in
the exceptional/carrier inputs rather than in the strict-prime composition
generator.  Adding them as new strict primes would double-count curves and
break the global type decomposition.

## 4. Maximum-safe provisional theorem

> Fix the charged reduced finite normal-singular quadratic F5 frame, the
> binding Euler/ruling, rational-forest, normal-F5 carrier/effectivity inputs,
> and the complete q=6 local contact census.  Then the v2 necessary-lattice
> enumeration is exhaustive over exceptional ADE roots, all permitted
> `pi`-contracted carriers, and every strict/nonexceptional prime.  After
> admitting `B`-degree-zero strict primes via the corrected `a>=0` domain,
> all 28 affine/root and rank-zero rows have zero configurations satisfying
> the local pair conditions before carrier-forest filtering.  Hence neither
> `U3/A3` nor any `B3/A2` modulus admits a necessary global boundary
> configuration in this fixed q=6 frame.

This remains provisional until a different model reviews the typing lemma
and closes the local-contact review gate.  It is a necessary-lattice theorem,
not proof that the quadratic frame occurs, not coefficient realization or
effectivity, not a nonquadratic statement, not a polynomial map, and not JC2.

## 5. Cheapest successor

Run one narrow different-model review that reconstructs (2.1)--(2.5), checks
that the local `B3/U3` contact census is complete, and verifies that no
exceptional or contracted curve is double-counted as strict.  If it passes,
promote the fixed-presentation q=6 closure and stop all reduced finite
normal-singular F5 work.  The quadratic front then moves to the scope escapes:
nonreduced infinity, nonfinite/projective-basepoint cases, degree drops, and
quadratic-frame existence/minimization.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9818`.
- Body SHA-256:
  `650be07da65edee18d7e7d3a8482675c59e61c35c4bfc7a6ed6e90edc0c511c5`.
- Frozen basis: `f63b8bd9400ff86eb385c2f705e885015c624068`.
