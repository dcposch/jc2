# Correction delta — labelled one-P0 U2 td12 global-budget kill R1

Date: 2026-08-29 UTC  
Producer: Sol 5.6 coordinator integration lane  
Lifecycle: `PROMOTED_LABELLED_ACTUAL_LANDING_ONLY`

## 0. Custody and disposition

The sealed producer

```text
6eb9b8882766a33a23cbd37564eed252b71c39c158cb1f572ffe0a6f721a9654
  xmodel/m2-u2-one-p0-td12-global-budget-kill-r1-sol56-20260829.md
body f37ce04ef928bcb99ff8528880b1ac3e5891f598d37397da554f811dfa31cbc6
```

received independent Grok 4.6 hostile review

```text
9798a068b609bcd713734d04dab4085e50d1ca02a03fe59e9d58ede6a2b12ffe
  xmodel/m2-u2-one-p0-td12-global-budget-kill-hostile-review-grok46-76c-20260829.md
body 8f489f453181f1a323c28baf81b7420e86e48f73961afb49aee707312bbc2388
```

with verdict `PASS_WITH_REPAIR`.  The producer and review remain byte-frozen.
This delta applies the required carrier declaration and two wording
sharpenings.  It changes no arithmetic and does not widen the theorem.

## 1. Mandatory consumer declaration

Every finite-P0 price in this packet is a `REPRESENTATIVE` AF2 lower bound.
It is not a `FULL_ACTUAL_EXIT` or LL-1 full-exit reprice.  The configuration-
wide attachment is the already promoted selected-exit/MFE inequality

```text
c74fc0f99a830e3845e0821188c3f693b9b47d441e5c9f00716ac72ef2f09836
  xmodel/sigray-multipole-selected-orbit-attachment-coordinator-integration-20260828.md
```

which counts each vertex of the pole-path union once and the shared suffix
once.  The three charged pre-merge path sets are pairwise disjoint.  No
unresolved LL-1 all-actual-flag bridge enters this consumer.

## 2. Target and incoming indices

At the corrected inner merge the target data are

```text
(nu_G,X_G,kbar_G)=(1,6,3).
```

For each incoming upper vertex `H`, R2.1 forces `w_H=1` and Statement 8.4
forces `3|M_H`.  The incoming index `nu_H` remains free and is not `nu_G=1`,
a fixed target index, or a legacy search variable.  The cap-free reduced P0
closure quantifies over all its legal incoming indices.

## 3. Floors, not attainment

The unique budget-at-most-five reduced target satisfying `w_H=1` and
`3|M_H` is `(w,M,lambda_min)=(1,3,5)`.  This proves each inner-chain lower
floor five; the displayed two-step path only witnesses that the modeled
minimum is attained in the reduced grammar.  It is not an actual landing.

The outer sibling is used only through the lower floor `lambda>=1`.  The
labelled outer handshake requires `w_H=2`, while every zero-price P0 move
from the pole seed `(3/2,2)` weakly decreases reduced weight.  The exact
sibling price is not asserted.  As unused corroboration, its multiplicity
three also requires `3|M_H`, whereas zero-price moves weakly decrease the
seed multiplicity two.

## 4. Promoted theorem and firewall

Assume an **actual typed source landing** at `td=12` of the corrected
`NESTED-U2-P0-U2-RAY/v1`: two multiplicity-three children at the inner U2,
the neutral P0 continuation, and two multiplicity-three children at the
outer U2.  Source-mass equality forces three disjoint one-pole chains of
type `(alpha,beta)=(2,3)`, each starting from
`(a,b,nu)=(1,2,3)` and `(w,M)=(3/2,2)`.  Representative AF2 gives

```text
two inner chains >= 5+5,
outer sibling     >= 1,
global budget     <= td-2 = 10.
```

Thus `11>10`, so this labelled actual landing is impossible.  The same
conditional kill applies to every fixed-`t` member of the repaired
semilinear ray.

This proves no statement about other U2 routes, other one-P0 labelings, all
`td=12` configurations, source landing or its existence, coefficient
gluing, realization, a polynomial pair, a counterexample, a degree bound,
`G2-PSC`, `G2-BD`, or JC2.

*End of sealed correction body.*

---

## Seal

- Body byte count: `3685`.
- Body SHA-256:
  `716810365cd2158c5bba027ebabb3e901b3d26656f1ae0c2a011fae52d4ab401`.
- Frozen Git basis:
  `76c746f698103d20019bfeb72654a361ccc5371d`.
