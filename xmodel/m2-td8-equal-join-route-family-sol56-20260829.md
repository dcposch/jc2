# D2 executed: an affine equal-join route family at the fixed td=8 entry

Date: 2026-08-29 UTC. Producer: Sol Ultra integration lane. Lifecycle:
`PROVISIONAL / DIFFERENT-MODEL REVIEW REQUIRED`.

## Result

Inside the current promoted off-axis book grammar, the unique `td=8,m=2`
entry has an explicit infinite affine family of full merge cells. Every
member:

- is reached by the same two priced chain steps;
- satisfies the complete case-II edge labels and congruences, not merely a
  reduced `(w,M)` test;
- has one common reduced merge successor;
- accepts the same full parent-dependent trunk step; and
- meets the current terminal lambda-budget **lower-bound filter** at
  equality.

Thus the first repaired D2 discriminator is positive: at this fixed entry,
the full formal-cell set is infinite even though the reduced-state quotient
is finite. A numerical `kbar` cap cannot be the completeness mechanism. The
next proof obligation is the exact parametric Prop. 8.1(iv)/log equation on
this family.

This is a family of budget-fitting **superset-formal** routes. The recorded
lambda values are lower bounds, not proved exact costs; no member is asserted
realizable by a polynomial Keller map.

## Fixed entry and incoming chains

Exact `book_offaxis.census(8)` gives the sole off-axis entry

```text
type (alpha,beta)=(2,3), td=8, m=2,
pole 1 = pole 2 = (Lambda,a,b,nu)=(4,1,2,3).
```

Each entry chain begins at `(w,M)=(3/2,2)` and takes the printed P0 `(A)`
step

```text
l=2, nu=7, eps=0, k=1, Sm=1, lex=0,
(dp,dq,E)=(21,15,9),
(kbar,X,rho,w_child,M_child)=(5,7,1/3,2/3,3),
recorded lambda lower bound = 2.
```

The unique extra orbit has multiplicity one and price
`ceil(X-kbar)=2`. These are the already named `(21,15)` escape data.

## Infinite equal-join family

Let `t>=0` and set

```text
nu_G   = 4+3t,
dp_G   = 24+18t,
dq_G   = 9+6t,
M_G    = 3,
kbar_G = 6+4t,
X_G    = 16+12t,
rho_G  = 2/3.
```

This is the equal-arrival pattern with two nonzero arrivals
`(mu,w)=(3,2/3)`, no 0-root, no nonchain orbit, and no q-extra:

```text
dp_G=2*mu*nu_G, dq_G=2*nu_G+1,
E_e=mu*dq_G-dp_G=3,
kbar_G=w*dq_G,
X_G=mu*(kbar_G-w),
X_G/kbar_G=dp_G/dq_G.
```

The progression `nu_G=4 mod 3` is exactly the integrality condition
`3 | 2nu_G+1`. It also gives
`M_G=gcd(6nu_G,2nu_G+1)=3`, `gcd(M_G,nu_G)=1`, and the T-law
`M_G | T=6`. The trunk state is constant:

```text
w_tr=(kbar_G-rho_G)/nu_G=4/3.
```

For each incoming edge, the complete positive case-II label is

```text
n_e = nu_H*kbar_G-kbar_H = 37+28t,
nu_H=7, kbar_H=5, rho_H=1/3.
```

It satisfies identically

```text
(kbar_H+n_e)/nu_H = kbar_G,
3*(rho_H+n_e)/nu_H = X_G.
```

So the family is not an artifact of forgetting the incoming frame.

## Uniform trunk and terminal

From the merge frame take the fixed P0 step

```text
l=3, nu_F=17, eps=0, k=1, Sm=2, lex=0,
(dp_F,dq_F,E_F)=(85,35,20),
(kbar_F,X_F,rho_F,w_F,M_F)=(7,17,1/5,2/5,5),
recorded lambda lower bound = 2.
```

Its parent-dependent edge label is

```text
n_F = nu_G*kbar_F-kbar_G = 22+17t.
```

For every `t>=0`, it is positive and satisfies

```text
(kbar_G+n_F)/nu_G = kbar_F,
(rho_G+n_F)/(kbar_G+n_F) = dp_F/(3*dq_F)=17/21.
```

Thus the same trunk cell composes with every member of the affine merge
family at the full-frame level. At the terminal,

```text
w_F=2/5, M_F=5,
j=M_F*(1-w_F)=3,
psi=ceil(M_F/j)-1=1.
```

The recorded lower-bound sum is

```text
2 + 2 + 0 + 2 = 6 = td-1-psi.
```

Hence every member survives the printed budget filter at equality. This is
not a proof that the true lambda cost equals its recorded lower bound.

## Exact packet

Packet: `cases/m2_td8_equal_join_route_family_r1_20260829/`.

```text
48d1288e9235fa9a079b7a9b29d9c10b3800454d6bdb4c557165fae89dea4a94  td8_equal_join_route_family_r1.py
dccd335edebc9bb2d329df9c95da8e27265e5a7e6f705f6cadbe3d3b257b72c4  test_td8_equal_join_route_family_r1.py
69e3d1ea1f4951f963f48354dc8d0f7eb811eebb3969798ab4375b092cdaeae4  README.md
2cb4eddcda8feeb89d766dcfcfa6c712adce5b81939c3d8d1237e4c15cb483e2  charged JSON output
```

Ordinary and optimized suites each pass 80,097 checks. They verify the
fixed entry step, 10,001 consecutive family members with both incoming and
trunk edge labels, the exact terminal and budget lower-bound equality,
neighboring failed integrality classes, distinct-full-cell versus
single-reduced-state behavior, invalid parameters, and optimized certificate
identity. The large finite scan is a mutation/regression battery; the affine
identities above are the proof for all `t`.

## Strategic consequence

This executes Grok's repaired D2 and answers the combinatorial question.
The full cell book at fixed `td=8` is infinite at the recorded superset tier;
the reduced successor is the single state `(4/3,3)`. Therefore:

1. compile this family as one normalized arithmetic-progression record;
2. emit the exact Prop. 8.1(iv) equation symbolically in `t`;
3. seek a D9-style uniform log obstruction, a finite exceptional set, or an
   explicit formal survivor family;
4. keep fixed-entry reachability, lambda-exactness, source landing, and
   realizability as separate gates.

This is consistent with the repaired M2 quotient: quotienting is necessary,
and a finite reduced state set does not imply a finite full-cell set.

## Scope firewall

No exact Prop. 8.1(iv) equation has been solved here. The result proves no
geometric configuration cover, source landing, actual configuration,
topological-degree ceiling, Keller counterexample, or JC2 conclusion.

---
Report-body SHA-256 (bytes before the separator line above): `bd35c43baf91c6306d4bb651a09e4886340ab7eb836ffd41d6b1ba6a85ea02d7`
