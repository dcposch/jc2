# Preregistration: fixed branch-P upper endpoint before row 23

Date: 2026-08-27

## Frozen geometric fixture

Work over `Q` with the literal D5G recurrence

```text
D_n = sum_(i+j=n) ((12-j) F_i' G_j + (i-8) F_i G_j').
```

Fix

```text
A = X^4-1,  H=A^2,  F0=H^2,  G0=H^3,
F1=H,       c2=0.
```

Equivalently, the reviewed branch-P coordinate `F1=H V` is fixed at
`V=1`; `V` is not a surviving solver variable.

Consume the reviewed reduced/geometric branch-P cascade exactly:

```text
F2=(1+H Z)/4,  deg Z<=6,
F3=(Z+A T)/8,  deg T<=9.
```

The words “exact cascade” refer only to field-valued polynomial points and
the underlying reduced support.  No equality with the natural nonreduced
coefficient scheme is asserted.

Every D3 raw source slot in `F4,...,F14` and `G4,...,G21` is retained.  The
equations `D4=D5=D6=0` are included only to express the already-reviewed
arbitrary `F4,F5,F6` and free `c4,c6` data in literal raw `G` coordinates.
The new charged system is

```text
D7=...=D21=0,  D22=1.
```

There is no `G22` slot.  `D22=1` is therefore a slotless accumulated
compatibility equation.  Neither `D23=0` nor the `q1` image equation is an
input to any solver lane.

## Authoritative and acceleration formulations

The authoritative formulation is the coefficient ideal obtained directly
from the displayed recurrence after the fixed substitutions.  It retains
all literal later raw slots and serializes every coefficient generator.

A characteristic/weighted formulation may be generated only as an
independently replayed acceleration.  Its five P characteristic directions
are

```text
m=4: A^4,  m=6: A^3,  m=8: A^2,  m=10: A,  m=12: 1.
```

No direction may be pivoted to zero or omitted.  A contracting cross-check
may introduce `s,lambda`, homogenize `F1=sH`, use the weighted cascade, and
add `D22=lambda, lambda=s^22`; it must dehomogenize back to `s=lambda=1`
before promotion.

## Exact outcomes and stop rules

A positive outcome requires exact rational values for every surviving raw
slot, literal replay of `D0,...,D21=0,D22=1`, all raw-window checks, and an
exact proof that `F1=H` is outside the branch-P `q1` image.  Only after this
replay may the reviewed tower theorem be used to say that row `D23` adds
genuinely new information on this fixture.

A negative outcome requires both parts of one complete exact-Q account: a
saturated unit/Nullstellensatz certificate for the complete fixed-control
ideal, and a named earliest-row left-cokernel/divisibility identity locating
the affine obstruction while covering every prior stratum.  Either part by
itself is only diagnostic.  Modular unit bases, timeouts, one specialization,
and failed rational reconstruction are not negative evidence.

## Frozen mutations

The independent replay must reject all of the following byte-named
mutations:

1. replace the target by `D22=0` while keeping a positive witness;
2. add `1` to the constant coefficient of `D21`;
3. admit a synthetic constant `G22` slot (this must change the same-row
   operator and is forbidden in the charged system);
4. replace `F1=H` by a branch-P `q1`-image vector in the nonmembership check.

## Execution custody

Heavy algebra runs only on an audited idle AWS r6/Box03 node, in a fresh
immutable source namespace.  The runner must fail closed away from the pinned
Box03 `r6i.16xlarge` identity, record host/tool/source metadata, use one global
six-hour wall cap and an
explicit per-lane virtual-memory cap no larger than the 450-GiB host envelope,
record `/usr/bin/time -v` telemetry, and never write into an older output
namespace.  After the immutable 128-GiB literal `std/lp` pilot exhausted its
cap without an algebraic result, its preregistered fresh successor uses a
280-GiB VM cap and one core; at launch this must leave at least approximately
150 GiB of host headroom with zero swap.  Modular shards are discovery only.
Promotion requires exact-Q witness/certificate bytes and an independent raw
replay.  No canonical file, commit, push, or `jc2-lean` access is authorized.
