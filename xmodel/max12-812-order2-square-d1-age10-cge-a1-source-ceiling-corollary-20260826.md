# Corollary: D1 `a>=10`, `C`-contact source ceiling

Date: 2026-08-26

Status: **FROZEN PROVISIONAL EXACT COROLLARY; DISTINCT HOSTILE REVIEW
REQUIRED.**

## Frozen parent

This corollary consumes only the frozen producer

```text
2ccfdfe9c3deb4d32594d2f5e1237684023d5b75438a02229776436c38456883
  cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/RESULT.md
60b2e1d52156f0648f7f39739f06c139d7d274c28fe4147eaba8d7213dfc2f0b
  cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/PRODUCER_FREEZE.sha256
9f0184b1007103478381c474ce6e4c1802ed8a53ab23dee79e7dd77518e0168e
  cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/compile_age10_j38_r3.py
```

and every source/evidence byte pinned by that producer freeze.  The parent's
own hostile review is separate and remains a lifecycle condition for final
promotion.  The specialization argument below is not a producer PASS marker.

## Closed source-ceiling statement

In characteristic zero, after exactly the registered upstream square/D1
gates, fix integers `n,m,s>=0` and put `a=10+n`.  In the complete formal
source, allow arbitrary linear-coefficient series

```text
A in sigma^a       * k[[sigma]][z]_{<=1},
C in sigma^(a+1+m) * k[[sigma]][z]_{<=1},
R in sigma^(a+s)   * k[[sigma]][z]_{<=1}.
```

No displayed leading coefficient is required to be nonzero and none is
inverted.  Equivalently, this is the closed range

```text
a>=10,  C-contact c>=a+1,  R-contact r>=a
```

with `a` a chosen common source lower bound.  On `D(J)` the seven literal
Faber source equations have empty scheme before radicals.

## Exact specialization proof

The frozen baseline producer works modulo `sigma^39` with

```text
A = sigma^10*theta*Abar,
C = sigma^11*theta*Cbar,
R = sigma^10*theta*eta*Rbar.
```

It proves, as a polynomial identity in every normal/load/connection/target
jet and in `theta,eta`,

```text
Phi7 + (p(sigma)/4)*Phi5
     + (3*p(sigma)^2/32)*Phi3
     + (5*p(sigma)^3/128)*Phi1
  = -sigma^38*J/4                         mod sigma^39.       (1)
```

Make the formal substitutions

```text
theta = sigma^n,   eta = sigma^s,   Cbar = sigma^m*Chat.      (2)
```

Polynomial substitution preserves (1).  It gives precisely the three
closed divisibility conditions in the statement.  In particular, this is
not an inference from density of an exact-contact open.

The finite `Cbar` jet ceiling causes no gap:

- for `0<=m<=10`, (2) is the literal index shift obtained by setting the
  first `m` pairs of frozen `Cbar` coefficients to zero and relabelling the
  remaining pairs;
- for `m>=11`, the earliest `C`-dependent primitive, `k6*C/L`, moves from
  grade 28 to grade at least 39 and hence contributes zero modulo
  `sigma^39`.  Every other `C`-dependent primitive starts later.  Thus no
  unrepresented coefficient of `Chat` can enter (1).

Raising `C` cannot reveal a previously excluded family: a monomial with
`e_C` copies of `C` moves later by exactly `m*e_C`, while a `C`-free
monomial is unchanged.  Pole order is unchanged.  The frozen exhaustive
baseline has pole ceiling three through grade 38 and first pole-four family
`k6*A*C/L^4` at grade 43; after (2) that family is at grade `43+m`.
Consequently the order-three Laurent-to-ordinary functional still kills
every non-target source term.  The even targets are absent from its odd-row
combination, and the sole odd target remains `-sigma^38*J/4`.  Adjoining
`iJ*J-1` therefore gives the unit ideal exactly as in the parent.

## Exact fan consequence

For the normalized integral unit-load unique-`AC` fan, write

```text
d=c-a in {1,2,3},  s=r-a>=0,  a+3*s>d.
```

The closed source ceiling contains every such point with `a>=10`, not only
`d=1`.  In particular it closes all high-contact members of all five
previously residual families:

```text
d=2:  s=0, s=1, and s>=2, for every a>=10;
d=3:  s=0 and s>=1,       for every a>=10.
```

For `a>=10` the strict inequality `a+3*s>d` is automatic.  What remains of
those unique-`AC` families after this corollary is therefore the finite
`a<=9` threshold range (with the still-parametric `s` tails), not any
`a>=10` cell.

## Firewall

This is a specialization corollary of the frozen grade-38 source identity,
not a new landing theorem.  It does not change the parent's registered
upstream hypotheses; promote the corollary only if both the parent and this
specialization pass different-model review.  It makes no claim for `a<=9`,
`c<a+1`, `r<a`, a different fan face, positive-order leading `k10`, or an
excluded `p=0`, `k0=0`, zero/infinity, exact-square-zero, terminal/Taylor,
or global landing chart.  It does not close D1, the whole square component,
order two, `(8,12)`, maximum twelve, or JC2.
