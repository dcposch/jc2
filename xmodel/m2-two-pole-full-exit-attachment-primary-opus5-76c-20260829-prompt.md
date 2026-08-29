# Independent Opus 5 attack: two-pole full-exit attachment theorem

You are Opus 5, an equal mathematical co-researcher. Work independently at
commit `76c746f698103d20019bfeb72654a361ccc5371d` in
`/Users/dc/code/math/jc2`.

Write exactly one report:

`xmodel/m2-two-pole-full-exit-attachment-primary-opus5-76c-20260829.md`

Do not edit any existing file or create any other file. No canonical,
ladder, case, guardrail, or operations edits; no commit/push/web/AWS/heavy
computation. Never enter, enumerate, search, read, build, modify, status, or
control `jc2-lean`. Small read-only source extraction and desk checks are
allowed.

## Objective

Attack the exact blocker isolated by the stable LL-1 repricing review:

> On one fixed fibre, prove (or delimit sharply) that the physical y-side
> Eggers--Wall flag object containing every cv flag is a rooted tree; the
> union `U` of two pole paths is rootward closed; every full actual cv exit
> flag below a non-chain alternative direction has a unique attachment in
> `U`; different directions/attachments give disjoint full exit sets; and
> all those flags may be inserted once in the single Corollary-7.1 budget.

The earlier MFE hostile review called this an unproved "ambient
quotient/orbit attachment" lemma. Do not simply inherit that verdict. Audit
whether Definition 3.3 already makes the physical flag object a tree and
whether corrected Statement 3.18 supplies the only needed bridge from
cyclic polynomial-root orbits to physical child directions.

## Mandatory proof split

### A. Physical flag tree

Starting from Statement 3.2 and Definition 3.3, prove or refute explicitly:

1. The contact function on the coherently selected formal series satisfies
   `O(P,R) >= min(O(P,Q),O(Q,R))`.
2. The quotient of physical-place rays by `(P,u)~(Q,u) iff u<=O(P,Q)` has
   unique rootward restriction and no remerging: once two flags differ at
   one height, they differ at every greater height.
3. The rational/vertex subtree used by the transition calculus inherits
   this tree property. No additional quotient of already-physical flags is
   silently introduced later.
4. For the connected rootward-closed union `U` of two pole paths, every
   flag outside `U` has a unique last/outermost intersection of its root
   path with `U`; descendant components with different attachments are
   disjoint.

### B. Direction-orbit interface

Audit Notation 3.8, Statements 3.5--3.6, Statement 3.16, Proposition 3.2,
Statements 3.17--3.18, including the filed correction of Statement 3.18
from `F*c` to `F*(epsilon*c)`.

Decide whether:

- roots of `p_F` occur in `mu_(nu_F)` orbits;
- corrected Statement 3.18 gives exactly one realized microchild per
  nonzero orbit (and the zero child when present);
- different realized microchildren are different physical flag-tree child
  components and cannot later be identified;
- every non-chain priced direction in the two-pole transition calculus is
  one of these actual child components, with arrival/rootward directions
  excluded before pricing.

The abstract hostile countermodel identifies later cv representatives of
two different direction-orbits. Determine whether that model satisfies
Definition 3.3 plus the realized-microchild facts. If it does not, say
exactly which axiom it violates. If the source does not bridge root orbits
to microchildren, give the smallest countermodel that satisfies every
available statement.

### C. Full actual exit consumer

Using Statement 7.3, corrected Statement 3.13, the reviewed full-exit
coverage theorem, the actual-weight Corollary 7.1 repair, and the MFE local
same-branch/arrival-exclusion results:

1. Define the full set `E_all(F,d)` of distinct actual cv flags below an up
   non-chain direction `d`.
2. Prove or refute that all members attach at `F`; sets for different
   `(F,d)` are pairwise disjoint over the two-pole union `U`.
3. State the exact simultaneous single-budget inequality.
4. Apply it specifically to LL-1's four multiplicity-3 P0 cells
   `(17,5)@2`, `(51,15)@7`, `(85,25)@12`, `(119,35)@17`, each with
   `delta=2/3`, while keeping epsilon/zero directions separate.
5. State explicit machine-readable consumer tags. Distinguish
   `REPRESENTATIVE`, `FULL_ACTUAL_FIRST_SEPARATION`, and any weaker partial
   type you find. If the theorem is proved, include valid `charge_basis=`
   lines for the two exhaustive nonintegral branches (`q>=2` and
   `multi-flag`) with precise citations. Do not claim attainment.

## Decision classes

Use the strongest exact classification justified:

- `PROVED_FULL_TWO_POLE_ATTACHMENT`;
- `PROVED_PHYSICAL_TREE_PARTIAL_ORBIT_INTERFACE_OPEN`;
- `PROVED_SELECTED_ONLY_FULL_SET_OPEN`;
- `REFUTED`;
- `INPUT_MUTATED_NO_RESULT`.

If full proof succeeds, identify why the prior hostile review's blocker was
a perimeter omission rather than a mathematical gap. If only a partial
theorem succeeds, give the minimal missing implication and minimal
countermodel.

Include exact hypotheses, dependency graph, before/after custody table,
source line/page citations, scope limitations, and a sealed-body byte/hash
convention. Verify every frozen source before and after. If any changes,
fail closed.

## Frozen source perimeter (SHA-256)

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
ded3051d1a2009498f49bed20e5168d34b823518ab1b94ed340b380b37da6d15  ladder/SIGRAY-AUDIT.md
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004  xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
05f68f4b7278a8ac1216ba82b40e7081bfff66f351380ccd671d12a955784d84  xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md
56e95db58e53aa030ef1100cc1640d115105a77607d40e3f160e77b46174a34d  xmodel/m2-arity-law-place-conservation-source-audit-hostile-review-fable5-20260829.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14  xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
f55a00f5259d77766cc8179f3d1248ee0c1320daf411f04758487d2e94e216bb  xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md
3e3cea4aa6e0bda907dd291a0f1e62e1ffa744e84463e5596c2e0e0e408a166b  xmodel/m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829b.md
aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7  xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md
205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e  cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json
1ae50f7925de2d63a718b48ab892c78a3313e4a505b8faf7385853d591c58840  ladder/BOOK-OFFAXIS.md
93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb  ladder/SHEET6-MULTIPOLE.md
d7d0038c5fd1a3522b2908a598d99c23c64e85ec81d1280f1c7ec686c6c8ab2f  ladder/SHEET6-2POLE.md
```

The lane appends its compact reasoning guardrail; obey it.
