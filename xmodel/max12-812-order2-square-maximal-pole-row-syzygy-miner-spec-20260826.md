# Maximal-pole row-syzygy miner: frozen method specification

Date: 2026-08-26

Status: **FROZEN NAVIGATION/PRODUCER SPECIFICATION.  NOT A SOURCE-SUPPORT,
EMPTY-CELL, ORDER-TWO, MAXIMUM-TWELVE, OR JC2 THEOREM.**

## Purpose

For a frozen square/D1 source cell, replace a broad standard-basis attack by
the smallest exact row functional which sees the largest Laurent pole.  Once
that functional forces a root allocation or a common factor, divide it out
and repeat at the next pole.  A cell is eliminated only when a complete
source replay identifies a terminal coefficient which is a unit on every
licensed exact-contact chart.

The method is deliberately separate from the affine support miner.  A support
census may nominate a cell, but it cannot supply its primitive completeness,
row bridge, allocation, or endpoint.

## Registered input

An application must freeze the following before running.

1. A single chamber or explicitly finite list of chambers, its grade ceiling
   `T`, and every localization used.  Equality faces and deck orientations
   are separate inputs.
2. An independently generated primitive inventory through `T`, derived from
   the frozen Laurent generating function.  Cost bounds must be mechanical;
   a padded-bound replay must return the identical inventory.
3. Mechanical maxima for every source, load, moving-connection, and target
   jet.  A sentinel must show that every nonzero maximum actually enters the
   compiled source.
4. The complete seven literal source rows and the lower-unitriangular
   Laurent-to-Faber bridge through `T`.  The analytic receiver alone is not a
   source theorem.
5. The target timing row by row.  A functional may be called target-free only
   when the compiled full/source difference vanishes through its terminal
   grade.

No primitive may be deleted because its pole is smaller than the current
maximum.  It is retained in the common numerator and is allowed to reappear
after a forced factor is divided out.

## Pole functional

Let the grade-`g` analytic coefficient be

```text
H_g(z)=N_m(z)/L(z)^m,       L=z^2+P/2,
```

where `m` is the largest pole in the complete grade-`g` inventory and the
degree of `N_m` is bounded by the seven-row receiver.  The compiler must:

1. reconstruct `N_m` from the analytic rows and verify the denominator
   recurrence;
2. derive, rather than hard-code, its two root evaluations from the literal
   Faber rows;
3. verify these evaluations directly against `N_m(+-lambda)` after
   `lambda^2+P/2=0`;
4. impose no root allocation until those exact evaluations have been
   obtained from the source rows.

For odd pole `m`, the root functional is the appropriate truncation of

```text
(1-(P/2)X)^(5/2-m),
```

as licensed by the separately reviewed universal Laurent-to-ordinary
functional.  For even pole, reconstructing `N_m` gives the corresponding
even-row functional without extrapolating the odd formula.

## Iterated factor/derivative step

If both root evaluations force `L|N_m`, the computation is not finished.
The compiler must form the exact quotient `Q_{m-1}=N_m/L`, check the division
identity, and test `Q_{m-1}` at both roots.  Equivalently, on `D(P)`,

```text
Q_{m-1}(lambda)  = N_m'(lambda)/(2*lambda),
Q_{m-1}(-lambda) = N_m'(-lambda)/(-2*lambda).
```

The derivative expressions must also be reduced to explicit syzygies in the
seven literal rows.  This step is repeated until either:

- a root value is a unit on every surviving chart, giving an empty-cell
  producer; or
- a genuine residual row system survives, in which case the output is only a
  smaller successor ideal and not an emptiness verdict.

Lower-pole families which vanished in `N_m mod L` can become the unique term
in `Q_{m-1} mod L`; this is the main intended rank jump.

## Root-allocation custody

Work over the finite etale splitting cover `L=(z-lambda)(z+lambda)` on
`D(P)`.  A claimed allocation must cover all charts on which each named
leading linear form is nonzero.  The preferred check records its two root
values and covers the four products

```text
D(A(+lambda)R(+lambda)), D(A(+lambda)R(-lambda)),
D(A(-lambda)R(+lambda)), D(A(-lambda)R(-lambda)).
```

Same-root charts must be shown inconsistent, and the two opposite-root
charts must be checked separately.  Deck symmetry may shorten the prose but
does not replace the second compiled check.  Descent is only from an empty
faithfully-flat cover; exact-contact language must name the coefficients
inverted on every chart.

## Fail-closed controls

Every producer application requires:

- exact `Q` on AWS and two fresh good-prime controls with identical structural
  inventory and PASS markers;
- a wrong-pole or omitted-highest-pole negative control which fails the
  terminal test;
- an omitted-connection negative control whenever `T` is later than the
  first primitive grade;
- explicit target, load, and localization firewalls;
- zero swap and immutable source/evidence manifests.

A prime screen can validate software and support, but it cannot promote the
characteristic-zero endpoint.  A navigation-only run must say so in both its
result and review prompt.

## First application

The first registered face is the unit-load equality vector

```text
(a,c,r)=(1,5,2) on D(p*k0).
```

At absolute grade `16`, the complete candidate initial receiver is

```text
(3/4) A*C/L + (5/32) k0*A^2/L
+ (5/16) k0*R^3/L - (3/8) R*A^2/L^2.              (1)
```

The pole-two functional first tests `L|R*A^2`.  On nonzero linear `A,R`,
the only surviving geometric charts allocate them to opposite roots.  The
preregistered successor test divides the common numerator by `L`: at the
root occupied by `A`, the `AC`, `A^2`, and divided `RA^2` terms vanish, while
`(5/16)k0 R^3` remains.  Thus the candidate terminal is

```text
(5/2) k0*lambda^3*R_unit^3
```

up to the deck sign, or its derivative multiple
`5*k0*lambda^4*R_unit^3`.  This is a hypothesis until the independent
four-family census, all-seven-row bridge, both orientations, and triple-AWS
producer pass.

## Firewall

This specification licenses a reusable way to construct narrow producers.
It does not import any support-miner emptiness claim, correct a prior memo by
itself, eliminate the registered first face, cover positive-order or
ramified loads, handle `p=0` or `k0=0`, prove fan exhaustiveness, or establish
any global landing theorem.
