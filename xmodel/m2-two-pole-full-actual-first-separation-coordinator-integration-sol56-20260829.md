# Coordinator integration — two-pole full actual first separation and LL-1

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Lifecycle: `PROMOTED_TWO_POLE_FULL_EXIT_FLOOR_AND_LL1_13_TO_7`

## 0. Evidence and custody

Two independent proofs and their comparison are frozen as

```text
82d2f6c3eb2c3985569da428def3d5c2e125ca5b0aa29ebfc7973b68ee843a7a
  xmodel/m2-two-pole-full-actual-first-separation-theorem-r1-sol56-20260829.md
f7853d39a17fd7329feaec101f1767ef5edddd07a2f0d5f8030a0cb023f95efe
  xmodel/m2-two-pole-full-exit-attachment-primary-opus5-76c-20260829.md
32402983a357ef25de363a9532a47fa9a2cb4b4e8e1bab918d6f6e07a3fb3a10
  xmodel/m2-two-pole-full-actual-first-separation-cross-comparison-sol56-opus5-76c-20260829.md
```

Fresh stable-basis Grok 4.6 hostile review is

```text
1b3be27da8ba495d80cbf473d844055583a672d136ccea40611dfe9fc0b7023e
  xmodel/m2-two-pole-full-actual-first-separation-hostile-review-grok46-76c-20260829b.md
body 32456 bytes:
  3be6ab6b8db8ba7c89c0f382f201a17b2bae6000720d2c04ef2de3925b90a47a
```

with verdict `PASS_WITH_REPAIR`, all 20 inputs and `HEAD=76c746f...`
unchanged before and after, and charge validator `VALID:2:2/3,2/3`.
The earlier same-model attempt is diagnostic only because one charged file
was transiently changed and restored during its run.  Its explicit custody
quarantine is `b139a21a07ebc0fbd34d028b59519c3d95b681c1f5ce8e09cb5eff50fd7129e1`;
neither its report nor its apparent verdict is promotion evidence.

## 1. Promoted attachment theorem

On one fixed fibre, Definition 3.3 makes physical flags a common-prefix tree:

```text
I_P(t)=I_Q(t)  iff  t<=O(P,Q).
```

After two rays separate they cannot remerge.  For the set-theoretic union
`U` of the two pole paths, every actual up non-chain microchild at a vertex
`F in U` has a full set `E_all(F,d)` of distinct same-ray cv flags covering
all physical places through that child.  Corrected Statement 3.18 supplies
the orbit-to-actual-child section; it does not identify root multiplicity,
cover series, physical places, and flags.  Statement 7.3 is universal in the
physical place.  Every flag in `E_all(F,d)` has unique outer attachment `F`.

Full sets from distinct directions or distinct attachment vertices are
pairwise disjoint.  Shared suffix vertices occur once, and pole arrivals are
removed before pricing.  The union of all these y-side flags plus the
separate x-side witness therefore enters one repaired actual-weight
Corollary-7.1 inequality.  The attachment statement is H5a-free; its numeric
consumer separately imports the reviewed jump/max `kappa`, integrality,
up-direction typing, `L_safe`, and C7.1 inputs.

## 2. Mandatory carrier dictionary

The sole hostile-review repair is nomenclature:

```text
canonical FULL_ACTUAL_EXIT = FULL_ACTUAL_FIRST_SEPARATION
  = complete set of distinct actual cv carriers + a lower floor only.
```

It never means that the floor is attained.  `REPRESENTATIVE` remains the
strictly weaker one-selected-witness consumer.  No representative price may
be upgraded by analogy.

For the nonintegral LL-1 defect `delta=2/3`, the exhaustive full-set branches
are one flag with `q>=2`, or at least two flags; singleton `q=1` exact is
impossible.  Both branches give lower floor two.  Zero and epsilon directions
keep their separately reviewed floors.

## 3. LL-1 consequence

The previously reviewed arithmetic now has its missing carrier.  Exactly four
LL-1 P0 cells change:

```text
(17,5)@2, (51,15)@7, (85,25)@12, (119,35)@17.
```

Their nonzero full-set floor rises `1 -> 2`; total cell floors are
`3,3,3,2`.  No other cell, zero term, epsilon term, or td12 thirteen-edge row
changes.  The exact checker
`cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py` produces
byte-identical ordinary and optimized output with SHA-256

```text
4498beacf2f119d4f3d1b1750e857549e98f76900899983dd32db5d4e5da0011.
```

At the frozen LL-1 reduced-superset scope, `ALIVE/ALIVE_FRAGILE` rows fall
from 13 to 7:

```text
ALIVE:          (2/3,3,2), (2/5,5,3)
ALIVE_FRAGILE:  (3/4,4,2), (2/7,7,4), (2/9,9,4),
                (3/10,10,4), (3/8,8,4).
```

The hash-pinned `ll1_book.json` remains the immutable legacy input; it is not
silently rewritten.  This integration and the exact reprice checker are the
superseding numerical consumer.

## 4. Scope firewall

Inherited menu completeness, pooled-replay legitimacy, and reduced-superset
semantics remain exactly as reviewed.  `ALIVE` is not occurrence.  This
integration proves no attainment, landing, realizability, other-td theorem,
degree bound, polynomial pair, counterexample, `G2-PSC`, `G2-BD`, or JC2.

*End of sealed integration body.*

---

## Seal

- Body byte count: `4646`.
- Body SHA-256:
  `c2141599234e14c92d3b1d69e6ca3a4fcb7968414c1c4490e1b5bfb34007c0e7`.
- Frozen input basis:
  `76c746f698103d20019bfeb72654a361ccc5371d`.
