# Preregistration: tied `(a,c,r)=(1,5,2)` maximal-pole producer

Date: 2026-08-26

Status: **PREREGISTERED EXACT-SOURCE ITERATED POLE-TWO PRODUCER.**

## Exact scope

Work only on the generic square/D1 unit-load chart

```text
D(p*k0),  ord(A)=1, ord(C)=5, ord(R)=2.
```

No neighboring lower-hull cell, support-miner endpoint, contact-raising
closure, or later grade is imported.  The absolute ceiling is grade `16`, so
all source series are leading jets and all target rows must be absent.

## Independent source census

Re-enumerate the four binomial summands of the frozen Laurent receiver from
their atom costs through grade `16`, with a padded-bound equality sentinel.
The accepted inventory is exactly

```text
AC:   +(3/4)  A*C/L,
A2:   +(5/32) k0*A^2/L,
R3:   +(5/16) k0*R^3/L,
RA2:  -(3/8)  R*A^2/L^2,
```

all first appearing in grade `16`.  There must be no fifth primitive and the
unique maximal-pole family must be `RA2`.

## Two-stage invariant

Put `L=z^2+p/2` and clear `L^2`:

```text
N2 = (3/4)A*C*L + (5/32)k0*A^2*L
   + (5/16)k0*R^3*L - (3/8)R*A^2.                 (1)
```

The compiler must reconstruct (1) from the analytic rows, verify the pole-two
recurrence, and identify `N2(+-lambda)` with the exact Faber functionals

```text
Phi4 +- lambda*(Phi3+(p/4)Phi1),  lambda^2+p/2=0.
```

The first root equations give `L|R*A^2`.  Cover every nonzero-`A`, nonzero-`R`
root-value chart.  The same-root charts are inconsistent; the two survivors
are, up to units and deck swap,

```text
A=au*(z-lambda),  R=bu*(z+lambda),
A=au*(z+lambda),  R=bu*(z-lambda).
```

On each survivor verify exact division `N2=L*Q1`.  Evaluate `Q1` at the root
where `A` vanishes.  The required terminals are the deck pair

```text
+(5/2)k0*lambda^3*bu^3,  -(5/2)k0*lambda^3*bu^3,
```

and the derivative-row functional gives the unit multiple
`5*k0*lambda^4*bu^3`.  Both must be derived from the literal grade-16 source
rows, not asserted from the displayed receiver.

## Acceptance

1. Verify frozen ancestry, the exact four-family inventory, padded cutoff,
   all seven source rows, recursive extraction, and the complete Faber bridge.
2. Verify the common numerator, both pole-two root functionals, the four-chart
   allocation cover, both exact quotient identities, and both terminal units.
3. Verify the derivative functional is a literal-row syzygy and all seven
   targets are absent through grade `16`.
4. Negative controls must show that removing `R3` destroys the terminal and
   that stopping after `L|N2` yields only allocation, not emptiness.
5. Run exact `Q`, `F_65519`, and `F_65521` on AWS under fresh tags, with
   fail-closed validators and zero swap.

## Firewall

A PASS eliminates only the displayed equality vector on `D(p*k0)`.  It does
not amend the earlier hand triage until independently reviewed; it says
nothing about another face, load chamber, `p=0`, `k0=0`, the exact-square zero
section, terminal/Taylor receivers, fan exhaustiveness, order two,
maximum twelve, or JC2.
