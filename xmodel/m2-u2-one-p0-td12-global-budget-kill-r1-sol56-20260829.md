# Labelled one-P0 U2 td12 global-budget kill R1

Date: 2026-08-29 UTC  
Producer: Sol 5.6 coordinator lane  
Lifecycle: `PROVISIONAL_READY_FOR_DIFFERENT_MODEL_REVIEW`

## 0. Result and exact scope

Assume an **actual typed source landing** at `td=12` of the corrected
labelled route

```text
two pole branches --mu=3,w=1--> inner U2
inner U2 --l=3--> clean neutral P0 --h=3,w=2--> outer U2
third pole branch ----------------------h=3,w=2--> outer U2.
```

Under the reviewed P0 grammar, AF2 prices, and global Statement 9.5 budget,
this route is impossible.  The two inner arrivals cost at least five lambda
units each; the third branch costs at least one.  Their distinct pre-merge
vertices therefore contribute at least `11`, while `td=12` permits at most
`td-2=10`.

This kills the corrected labelled `NESTED-U2-P0-U2-RAY/v1` at `td=12`,
including every member of its fixed-`t` semilinear rays.  It does **not**
exclude every one-P0 or U2 route, prove a universal landing theorem, construct
or exclude a polynomial pair outside this route, prove a degree bound, or
settle JC2.

## 1. Frozen dependencies

The derivation starts from clean pushed HEAD
`76c746f698103d20019bfeb72654a361ccc5371d`.  Full SHA-256 pins:

```text
1ae50f7925de2d63a718b48ab892c78a3313e4a505b8faf7385853d591c58840  ladder/BOOK-OFFAXIS.md
570f4f18d46178d8b86fe2276dbb2e35cb91e845842530b8c56df80bc16461f0  ladder/SHEET6-AF2.md
6bff49a12b9a2b8a97f137905ec87a7cbfb0025da39e59f54970458323b7344c  ladder/SHEET6-H3.md
3a7c604b1972681ef90982a94a10c61076d1f16502603ac39cefc802d7439398  xmodel/m2-finite-reduced-chain-skeleton-r2-repair-sol56-20260829.md
11d45ecaab58e82d3a5ef44bb14b5a90b617a8be8d287a1e947447fff43d1069  xmodel/m2-finite-reduced-chain-r2-hostile-review-opus5-20260829.md
b6f363407af9ea16f83bb5c0b7ff5c659e0e69b372ef2ace47d1f53b8b768afb  cases/m2_finite_reduced_chain_skeleton_r2_20260829/finite_chain_skeleton_r2.py
99670c469b66e7639f3046169ca3a7f8bbcda24890b19fe2018674adc23f7e19  cases/m2_finite_reduced_chain_skeleton_r2_20260829/test_finite_chain_skeleton_r2.py
4dde1c471b04d88db466293bc197c78529bc16743cc7ccde176e594bceb622dc  xmodel/m2-u2-one-p0-semilinear-family-record-r1-correction-sol56-20260829.md
84c648a721f42d8197a9c78648795e9830e5bb75521a3e00a8a9d5a80f495cb6  xmodel/m2-u2-one-p0-semilinear-family-record-r1-hostile-review-opus5-20260829.md
f9dd2035bbe5a47561cce263ba1288a9245526dec748c3ef031545e443bf510f  xmodel/m2-u2-one-p0-source-mass-floor-hostile-review-fable5-c359-20260829.md
```

Opus gives the finite-chain R2 implementation verdict
`PASS_IMPLEMENTATION_R2`; the underlying finite-closure theorem already had
independent Fable and Grok reviews.  Opus gives the labelled family
`PASS_WITH_REPAIR`, with `inner_u2.dq=3` supplied by the pinned correction.
Fable's source-floor review is `FAIL` on the old `td>=15` proof but proves the
weaker equality profile used here.  No withdrawn M-descent assertion enters
this argument.

## 2. What `td=12` equality forces

The repaired source-mass theorem gives three disjoint arrival subtrees, each
of mass at least `max(beta,2alpha)`.  Equality at total mass 12 is possible
only at type `(alpha,beta)=(2,3)`, with all three subtree masses equal to four.
The unique pole row of mass four is

```text
(a,b,nu)=(1,2,3),  Lambda=4,  kbar=5,  rho=1/2,
(w_entry,M_entry)=((5-1/2)/3,2)=(3/2,2).
```

Two poles would already contribute at least `2beta=6`, so each equality
subtree has exactly one pole leaf.  It is consequently merge-free before its
specified first merge, and the three pre-merge chain vertex sets are pairwise
disjoint.

Apply the corrected inner-U2 record

```text
(dp,dq,kbar,mu)=(6,3,3,3).
```

Its frame value is `X=kbar*dp/dq=6`.  The R2.1 handshake
`X=mu*(kbar-w_H)` therefore forces

```text
w_H = 3-6/3 = 1
```

on each of the two inner arrivals, while Statement 8.4 requires `3|M_H`.
The corrected labelled outer record separately requires its two equal-weight
arrivals at `w=2`; in particular the third, unused sibling subtree must move
from the same pole seed `(3/2,2)` to weight two.

## 3. Exact inner-branch price

The promoted cap-free finite P0 closure theorem computes all reduced states
reachable from `(w,M)=(3/2,2)` within lambda budget five.  Its charged payload
has 69 states and state-table hash

```text
c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad.
```

Filtering it by the exact arrival condition `w=1` and `3|M` gives one state:

```text
(w,M,lambda_min)=(1,3,5).
```

This is a lower bound without assuming that the eventual path itself fits
budget five: any path of price at most four would occur in the cap-free
budget-five closure, and none does.  A minimum witness also exists:

```text
(3/2,2) --dirty (dp,dq,nu)=(20,16,5), lambda=2--> (3/4,4)
        --pure-epsilon (l,eps,E)=(4,1,3), lambda=3--> (1,3).
```

Thus each inner pole branch contributes at least five.  Because the branches
are disjoint until the inner merge, these are two distinct sets of charged
vertices and contribute at least ten in total.

## 4. The outer sibling cannot be free

For the same P0 grammar, every modeled-zero-price transition is either a
neutral step, which leaves `w` fixed, or a clean resonance, which weakly
decreases reduced `w` (strictly unless it is the neutral case).  This is a
theorem of the finite-closure packet and is independently gated in R2 as
`zero_cost_reduced_nonincrease=true`.

The third equality subtree starts at `w=3/2` but the labelled outer merge
requires its child at `w=2`.  Hence its pre-merge chain contains at least one
positive-price vertex and contributes at least one lambda unit.  This uses
neither an M-divisibility descent nor an assumed realization of a particular
positive-price witness.

## 5. Shared-budget contradiction

Statement 9.5/(26), as compiled in `BOOK-OFFAXIS` P1 and `SHEET6-AF2`, gives
for any pairwise-distinct selected down-tree vertices of one configuration

```text
sum lambda_F <= td-2.
```

Choose the priced pre-merge vertices from the three disjoint pole subtrees.
At `td=12` the upper bound is ten, while Sections 3--4 give

```text
sum lambda_F >= 5+5+1 = 11,
```

a contradiction.  Merge and trunk prices are nonnegative and were omitted,
so no terminal `psi` sharpening is needed.  If either inner branch costs more
than five, or the outer sibling more than one, the contradiction only
strengthens.

## 6. Executable replay and firewall

The standalone exact replay is
`cases/m2_u2_one_p0_td12_budget_kill_r1_20260829/check.py`.  It pins the R2
closure source, reproduces the 69-state hash and unique inner target, checks
the minimum witness, verifies the zero-price obstruction, rebuilds the
corrected handshake and equality pole entry, and checks `11>10`.  Ordinary
and optimized Python produce identical stdout:

```text
stdout sha256 = 1c857adfc4a2614c948ea76a2a4000c076561999db0417b65ea0d34d01c87a1e
check.py sha256 = f12565cef14e99e2b2f9c4114e98956711e3b8b0b352a3720469a41b4eaafbf8
README.md sha256 = 7d98035fb03dc17e9c2e80ed609653ff2b66a6154fee6ef9617389a04d188d21
```

The executable declares `LABELLED_ROUTE_ACTUAL_LANDING_ONLY`.  Its negative
firewall fields for other U2 routes, all td12 configurations, landing,
realizability, and JC2 are load-bearing.  This producer result remains
provisional until a different model rechecks source scope, branch
distinctness, the closure consumer, and the global-budget attachment.

*End of sealed report body.*

---

Sealed body: 7,422 bytes.  SHA-256:
`f37ce04ef928bcb99ff8528880b1ac3e5891f598d37397da554f811dfa31cbc6`.
