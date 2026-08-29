# Promotion: corrected exact-square affine-Faber support

Date: 2026-08-26

Status: **PROMOTED NORMALIZED ORDINARY-FABER SUPPORT.  NO TOTAL-REES
ACCESSIBILITY, `J`-NONZERO ARC, TERMINAL/TAYLOR, ORDER-TWO, OR JC2
VERDICT.**

## Frozen chain

```text
77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e
  xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md
4ddc0e4837e1581129fddad70fc7b5c029d642e644f4fd8ab478a4dec59bded3
  xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-hostile-review-grok-20260826.md

86d9da43b1f7823a4673ed219478b1c6ff60503eccbb2892894733979468b19c
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/RESULT.md
8e56b7ab944e956b9d67993e54bfc8996f02b16803889ac7dfbaa59e2ee0447c
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/EVIDENCE.sha256
a779cdeb5be36ad70c09b1497c3719b8c0659c03b48798414d90464156993970
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/FREEZE.sha256
```

The exact-Q producer and characteristic-65521 software control both pass.
The independent Grok 4.6 hostile review rederived the result by hand and
ends `CONFIRMED`.  The finite-field lane is not used as a lifting argument.

## Promoted statement

Over a characteristic-zero field put

```text
Q=z^4+p*z^2+c*z+r,
Delta=p^2-4*r,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
```

and let `R_ell` be the ordinary inverse-root Faber tails in the frozen
source convention.  The reduced support of

```text
R1=R3=R4=R5=R6=R7=0,             R2=mu2
```

on the normalized exact-square chart `k10=1` is exactly

```text
square:
  c=0, Delta=0, mu2=0;

affine Faber:
  c=0,
  15*Delta^2-64*beta*Delta+256*gamma=0,
  Delta^2*(5*Delta-16*beta)-2048*mu2=0.
```

Both component ideals are prime, their intersection is the exact radical of
the raw seven-row ideal, and there are exactly two minimal primes.  On
`D(Delta)` the affine component is a rational graph with free `p`.  Writing

```text
D=Delta/4,                 s=5*D-4*beta,
```

it is

```text
gamma=D*(5*D-4*s)/16,      mu2=D^2*s/32.
```

Its zero-target section is the Chebyshev locus `s=0`; it is not a third
minimal prime.

The exact raw identity

```text
c^5+128*R5-96*p*R3-(12*p^2+32*r)*R1=0
```

holds before predecessor reduction, radical, localization, or base change.
It excludes reduced support on `D(c)` and records the raw transverse
nilpotence exponent.  It does not kill a forced square-normal correction by
itself.

## Correction and firewall

The earlier affine-`mu2` Laurent receiver is a different system.  Nonzero
`mu2` activates the unitriangular Laurent-to-Faber connection, so its
four-pivot conclusion must not be imported into this ordinary source.  The
corrected Faber component permits free `p`.

This promotion is confined to the normalized seven-row exact-square face at
`k10=1`.  It does not identify a total-Rees chart, classify square-normal or
load/target correction jets, prove `J` accessibility, treat `k10=0` or
`Delta=0`, or impose terminal `[6,2]` and the two Taylor families.  The exact
section has `R7=J/4=0`; a strict survivor must create generic `J != 0` at a
later correction.  No strict arc is constructed or excluded, and order two,
`(8,12)`, maximum twelve, and JC2 remain open.
