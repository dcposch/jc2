# Preregistration: tied `(a,r)=(1,2)`, closed `c>=6` maximal-pole producer

Date: 2026-08-26

Status: **PREREGISTERED EXACT-SOURCE ITERATED POLE-TWO PRODUCER.**

## Exact scope

Work only on the generic square/D1 unit-load chart

```text
D(p*k0), ord(A)=1, ord(R)=2, ord(C)>=6.
```

This is the `RA2=A2=R3` leading face strictly beyond the separate
`(a,c,r)=(1,5,2)` four-family wall.  No support-miner or neighboring-face
endpoint is imported.  The absolute ceiling is grade 16.  `C` and all
targets must be absent from that first grade, so no leading `C` coefficient
may be inverted.

## Independent source census

Re-enumerate all four frozen binomial summands through grade 16, using the
baseline `(A,C,R)=(1,6,2)` and padded-bound equality sentinels.  The accepted
inventory is exactly

```text
A2:   +(5/32) k0*A^2/L,
R3:   +(5/16) k0*R^3/L,
RA2:  -(3/8)  R*A^2/L^2,
```

all in grade 16.  `RA2` is the unique pole-two family.  `AC` first moves to
grade 17 and cannot occur.  Raising the `C` contact only delays every
`C`-dependent source, hence a grade-16 proof at the baseline covers the
entire closed `ord(C)>=6` tail.

## Iterated maximal-pole invariant

Put `L=z^2+p/2`, clear `L^2`, and reconstruct from the seven literal rows
the canonical negative-tail numerator modulo `L^2` of

```text
N2_full = (5/32)k0*A^2*L +(5/16)k0*R^3*L -(3/8)R*A^2.
```

The first root Faber pair forces `L|R*A^2`.  Exhaust the four nonzero root
value charts for the exact linear forms `A,R`.  Same-root charts must be
unit ideals; the two opposite-root survivors are, up to deck swap,

```text
A=au*(z-lambda), R=bu*(z+lambda),
A=au*(z+lambda), R=bu*(z-lambda).
```

On each survivor divide `N2` exactly by `L` and evaluate at the `A` root.
The required deck terminals are

```text
+(5/2)k0*lambda^3*bu^3, -(5/2)k0*lambda^3*bu^3,
```

with derivative-row units `5*k0*lambda^4*bu^3`.  The terminal must disappear
when `R3` is removed.  This proves emptiness only after the second
functional; the first functional is allocation, not an endpoint.

## Acceptance and execution

1. Verify frozen ancestry, the exact three-family census, padded cutoffs,
   all seven source rows, exact recursive quotients, and the full analytic/
   literal bridge.
2. Verify exact absence of `C`, every normal/connection jet, lower load, and
   every target at grade 16.  Use ordinary polynomial rings with explicit
   reductions; no Singular `qring` is allowed.
3. Verify the common numerator modulo `L^2`, its ordinary quotient,
   recurrence, both root and derivative Faber identities, all four charts,
   both exact divisions, terminals, units, and the omit-`R3` control.
4. Run exact `Q`, `F_65519`, and `F_65521` on three AWS hosts with fresh
   tags, fail-closed validators, full custody, and zero swap.

## Firewall

A PASS eliminates only the displayed closed `C`-tail on `D(p*k0)`.  It does
not amend the `(1,5,2)` producer, cover `ord(C)<=5`, another tied/primary
face, positive-order leading load, `p=0`, `k0=0`, the exact-square zero
section, a terminal/global chart, fan exhaustiveness, order two, maximum
twelve, or JC2.
