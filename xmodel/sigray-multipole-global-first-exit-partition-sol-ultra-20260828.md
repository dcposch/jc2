# Sigray multipole global first-exit partition

**Date:** 2026-08-28  
**Producer:** Sol Ultra / Codex  
**Status:** producer candidate; different-model hostile review required before promotion

## 0. Claim and boundary

Let `U` be the union of the characteristic paths from all y-side pole
vertices to `(0,y)`, with common suffixes identified as vertices of one
rooted tree.  At every `F in U`, consolidate the transition calculus into
one set of distinct positive alternative direction-orbits at `F`; do not
repeat that set for each pole path which happens to contain `F`, and at a
merge do not count the other pole-arrival directions as alternatives.

Then the cv witnesses used to price those alternatives can be chosen
pairwise distinct over **all** pole paths.  More precisely, they admit a
canonical ownership by their unique attachment vertex in `U`.  Consequently
the passed actual-weight Corollary 7.1 gives the shared multipole budget

```text
sum_(F in U) lambda_F^exit <= td(f,g) - 1 - psi,             (MFE)
```

where every vertex of a shared suffix is counted once and `psi` is the
separate x-side charge certified by `psi*l_f<k_f`.

This is an inequality theorem only.  It does **not** restore printed
Proposition 7.5 `(22)`, literal `delta_a`, fixed-baseline `(22-cl)`, any
slack equality, cross-fibre constancy of `kappa`, or MP8's categorical
claim that no refinement can put mass in an `M=1` region.  It also does not
exclude `td=6` and does not repair any root-census cap.

## 1. Frozen inputs

The actual-weight theorem and its hostile gate are

```text
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md

727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8
  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
```

At their passed scope they prove, for any pairwise-distinct set `S` of cv
flags on a prescribed fibre,

```text
td(f,g) >= 1 + sum_(H in S) kappa_H*(pi(H)-1).               (C7.1*)
```

The singleton first-separation construction and local pricing theorem are
in Section 4.6 of

```text
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933
  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
```

and passed the exact hostile review

```text
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad
  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md.
```

The tree and merge facts used below are the corrected MP0--MP1 package in
`ladder/SHEET6-MULTIPOLE.md`: `F -> F^o` is deterministic, the union of pole
paths is a finite rooted tree, and divergent directions never remerge.  The
same-branch microstep-to-pole implication uses repaired Propositions
6.7--6.8 and the reviewed Lemma 6.1 bridge recorded in `bb033a71...`.

## 2. Global attachment lemma

Work in the y-component of the flag/Puiseux tree.  Let

```text
U = union_i C_i,
```

where `C_i` is the path from pole `P_i` to `(0,y)`.  Because every vertex
has a unique rootward successor, `U` is connected and rootward closed.

For a flag `H` outside `U`, the intersection of its root path with `U` is a
terminal interval ending at a unique vertex.  Write that vertex as `a(H)`.
Equivalently, `a(H)` is the unique attachment of the component of `T\U`
containing `H`.

**Proof.**  The root belongs to `U`, so the intersection is nonempty.  If a
root path leaves a connected rootward-closed subtree and later re-enters it,
there are two distinct paths between the exit and re-entry vertices,
contradicting the tree property.  Hence the intersection is one interval
with a unique outer endpoint.  Two components of `T\U` with different
attachments are disjoint; two distinct first edges at the same attachment
also lie in disjoint components.  QED.

This elementary lemma is the missing cross-chain version of the singleton
“first separation index.”  Shared suffixes cause no ambiguity because they
are one subset of `U`, not one copy per pole.

## 3. Which directions leave `U`

At `F in U`, group cyclically conjugate roots which represent one tree
direction exactly as in the singleton repair.  Split the direction-orbits
at `F` into:

1. pole-chain arrivals represented by edges of `U`;
2. the unique rootward continuation in `U`; and
3. all remaining direction-orbits.

A remaining **searrow** direction cannot occur outside `U`.  Indeed,
Proposition 6.7 first supplies the required positive flag; if its raw
orientation is searrow, the reviewed Proposition 6.8 bridge carries the
microstep to a down vertex and then to a pole on the same branch.  That
pole's characteristic path would then
contain the direction, putting its first edge in `U`, a contradiction.
Thus every remaining direction which is priced by corrected Statement 9.3
is a positive alternative direction leaving `U`.

At a merge this observation is essential: the other pole arrivals are in
class 1, not class 3.  They are not charged.  Any `k` non-chain positive
orbits in the merge calculus are in class 3 and are charged once at the
merge vertex, not once per incoming pole edge.

## 4. Globally injective cv witnesses

For each `F in U`, let `D_F` be the set of distinct class-3 positive
direction-orbits that the local transition/merge calculus prices.  For
each `d in D_F`, Statement 7.3 supplies a cv flag `H(F,d)` farther out on
that same branch.  The singleton local-pricing proof gives

```text
kappa_(H(F,d))*(pi(H(F,d))-1) >= price(F,d),                 (LP)
```

with the corrected sign and the orbit conventions already reviewed in the
Section 9 packet.

The assignment `(F,d) -> H(F,d)` is injective:

- `H(F,d)` lies outside `U`, since its first edge at `F` is not an edge of
  `U`;
- its attachment is exactly `a(H(F,d))=F`;
- distinct direction-orbits at one `F` lie in different components of
  `T\U`; and
- witnesses attached at different vertices have different attachment
  vertices.

No choice made inside a component can spoil injectivity: one witness is
chosen per component, and distinct components are disjoint.

Define the consolidated exit charge

```text
lambda_F^exit = sum_(d in D_F) price(F,d).                   (4.1)
```

If a stronger local theorem prices several distinct cv flags in one
direction-component, include those flags as a set and use its proved local
sum; the same attachment argument still separates it from every other
component.  What is forbidden is repeating the same local set for multiple
incoming edges or multiple pole-path copies of a shared vertex.

Summing (LP) over the injective witness set gives

```text
sum_(F in U) lambda_F^exit
  <= sum_(F in U) sum_(d in D_F)
       kappa_(H(F,d))*(pi(H(F,d))-1).                        (4.2)
```

## 5. Add the x-side charge once

The x-side cv flag used in Statement 9.4 belongs to the other tree
component (Statement 3.3), so it is distinct from every y-side witness in
(4.2).  When `psi*l_f<k_f`, its integral weight is at least `psi`.

Apply `(C7.1*)` once to the pairwise-distinct set consisting of that x-side
flag and all witnesses `H(F,d)`.  Then

```text
td(f,g) - 1
  >= psi + sum_(F in U) sum_(d in D_F)
       kappa_(H(F,d))*(pi(H(F,d))-1)
  >= psi + sum_(F in U) lambda_F^exit.
```

This is (MFE).

## 6. Consumer consequences if hostile review passes

The following would move from AMBER to GREEN:

- the shared two-pole inequality in `SHEET6-2POLE.md`, provided every merge
  charge is consolidated once as in (4.1);
- the corresponding `m`-pole budget in MP8, at inequality/local-exit scope;
- shared-suffix deduplication by using the vertex set `U`, rather than a
  multiset of path occurrences.

The following remain quarantined:

- literal `Y(F)` sums (nested along paths);
- printed `(22)`, literal `delta_a`, and `(22-cl)`;
- equality/slack/no-refinement consequences;
- a claim that every actual cv flag is one of the selected witnesses;
- any root `M!=1` inference or any exhaustive finite root census;
- any exclusion of `td=6`.

The existing two-pole arithmetic exhibit is therefore still only a
necessary-condition object.  This theorem validates its **shared inequality
ledger**, not its realizability and not its historical capped survivor
counts.

## 7. Hostile-review checklist

1. Verify that MP0 really makes `U` rootward closed in the ambient flag tree,
   not merely in the induced down-vertex graph.
2. Check the use of repaired Proposition 6.8 in “down outside `U` implies a
   pole on the same branch,” including merge vertices.
3. Check that every locally priced direction is positive and that pole
   arrivals at a merge are excluded before pricing.
4. Check cyclic orbit grouping: no two representatives of one tree
   direction are counted twice.
5. Check that the current two-pole and multipole engines consolidate a merge
   price once; the theorem does not license per-incoming-edge duplication.
6. Try to construct a cv flag whose root path meets `U`, leaves it, and
   re-enters it; such an example would refute the attachment lemma or show
   that the ambient object is not a tree at the required level.
7. Verify that `(C7.1*)` permits the selected witnesses from all y-side
   branches on the same prescribed fibre and the separate x-side flag.
8. Reject any attempted promotion of MP8 equality/no-refinement rhetoric.

No web or AWS computation is needed for this theorem.  `jc2-lean` was not
entered, listed, searched, read, built, modified, status-checked, or
controlled.
