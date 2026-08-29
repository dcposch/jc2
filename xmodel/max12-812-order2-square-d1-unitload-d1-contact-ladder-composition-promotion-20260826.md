# Promotion: unit-load D1 unique-`AC`, `d=1` contact ladder

Date: 2026-08-26

Status: **PROMOTED AFTER LITERAL COVERAGE AUDIT AND DIFFERENT-MODEL
HOSTILE REVIEW.**

## Composition custody

```text
52ab6ce6a9628dfc019d1e99aa2deba8af9a6f467f23f2821ff1f30109a56d85
  xmodel/max12-812-order2-square-d1-unitload-d1-contact-ladder-composition-audit-20260826.md
bd5b3dd52274024941edc663c4ef95222f6abb205cdb9e347d8b80b3483e74cb
  xmodel/max12-812-order2-square-d1-unitload-contact-ladder-composition-hostile-review-grok-20260826.md
973f7953d42fdd994d9c7da8ea70fceffc2e8da9002b33f38ea1a17c6922d6d1
  xmodel/max12-812-order2-square-d1-finite-band-a2-a5-promotion-20260826.md
829ac12faceed48ad0ec599a60764d038835895bf33c2abce0dceb141605ea0f
  xmodel/max12-812-order2-square-d1-load-transition-a6-a7-promotion-20260826.md
3d847561946751c68a081db55f2f514b3808c22f7ac6e236fcbff10911ab1ce6
  xmodel/max12-812-order2-square-d1-a8-k6-mu2-v3-promotion-20260826.md
dfabe08283e8fe9cb1ea6cef28a9eac6a4728d0f7c482e8c642b2835798d0459
  xmodel/max12-812-order2-square-d1-a9-full-composition-promotion-20260826.md
d4aceedbead2d0c27546e143ae8bb2b820faa32dd08454c58650f280593d0fb2
  xmodel/max12-812-order2-square-d1-age10-j38-order3-promotion-20260826.md
```

The ladder review returned `CONFIRMED_CONDITIONAL`: its mathematical routing
passed, and its only condition was promotion of the two reviewed early bands
and the independently confirmed `a>=10` producer.  The three promotion SHAs
above satisfy those lifecycle conditions.  The overlapping promoted
`a>=13` order-two theorem is an independent control and is not needed for
coverage.

## Exact fan cell

On the normalized integral unit-load horizontal chart put

```text
q=ord(k10)=0,  a=ord(A)>=1,  c=ord(C)>=3,
r=ord(R)>=2,  d=c-a,  s=r-a.
```

Strict comparison of the five unit-load lower-hull weights

```text
AC=a+c, C2=2c, R3=3r, RC=1+r+c, A2=4+2a
```

shows that the unique-`AC`, `d=1` cell is exactly

```text
a>=2,  c=a+1,  r=a+s with s>=0.                   (D1-AC1)
```

The integral interval is literally partitioned by

```text
{2,3,4,5}, {6,7}, {8}, {9}, {a>=10}.
```

There is no unassigned integer contact.

## Promoted composition theorem

In characteristic zero, after the reviewed generic-square first-normal,
half-weight, and `M=0` gates, no finite-order normalized DVR source arc on
`D(p*k0*J)` has a contact in (D1-AC1):

```text
ord_sigma(A)=a,  ord_sigma(C)=a+1,
ord_sigma(R)>=a, a>=2.
```

Here `k10` in the early producers and `k0` in the later producers are the
same leading unit-load coefficient.  On a Keller source `J` is a unit, so
the usual campaign name for the open is `D(p*k0)`.

The conclusion is arcwise/set-theoretic.  The early bands prove rootwise
arc exclusion, the `a=9` package proves stronger scheme-theoretic source
ideal emptiness on its fixed contact, and the `a>=10` package proves a unit
ideal on `D(J)`.  Their common consequence is arcwise emptiness; the mixed
theorem types do not assert reduced scheme structure for the union.

## Exhaustive load and `R` routing

- `a<=5`: `k6`, `k2`, and targets occur after the decisive two-grade
  receiver.
- `a=6,7`: every in-window `k60,k61` term is retained without inversion.
- `a=8`: `D(k60) union V(k60)` is exhaustive; the closed section retains
  free `k61,k62`, including their simultaneous vanishing.
- `a=9`: the scheme split
  `D(k60) union (V(k60) intersect D(k60_1)) union V(k60,k60_1)` is
  exhaustive; positive-valuation DVR intermediates specialize into the
  already empty opens, and higher load/target corrections remain present.
- `a>=10`: no load jet is inverted.  The mechanically complete grade-38
  source retains all jets through `k10_6,k6_10,k2_6`; its row functional is
  independent of their values.

For the finite bands, the free leading `R` section and its zero face cover
every `r>=a` because the next `R` jet is later than the decisive window.  At
`a=9` the theorem already states all `r>=9`; at `a>=10` the homogeneous
`eta` substitution covers all `r>=a` without inversion.  Thus no lower-load
valuation or `R`-contact section remains inside (D1-AC1).

## Residual firewall

This promotion closes one fan cell, not D1.  It does not cover:

1. unique-`AC` `d=2` with `s=0,1,>=2`, or `d=3` with `s=0,>=1`, nor their
   small-`a` equality boundaries.  A separately reviewed source-ceiling
   corollary may later remove the `a>=10` tails but is not imported here;
2. primary `C2`, `R3`, `RC`, and `A2` faces or their equality
   intersections, including `RA2=A2=R3` at `(a,r)=(1,2),c>=5`, `d=4`
   `AC=A2` faces such as `(1,5,r)`, the `d=1` equality point `(4,5,3)`,
   and the `AC=RC` family `c=a+1,r=a-1` for `a>=5`;
3. the `a=1` charts, including `(1,3)` and `(1,4)`, or the separately
   treated `r=1` receiver;
4. positive-order leading `k10`, where `A3` can enter and the unit-load fan
   changes;
5. `p=0`, `k0=0`, the exact-square zero section, zero/infinity receivers,
   terminal/Taylor landing, other lifecycle charts, or global source
   landing/coverage.

The whole square component, nonsquare/Pell receiver, exact order two,
`(8,12)`, maximum twelve, and JC2 remain separate obligations.
