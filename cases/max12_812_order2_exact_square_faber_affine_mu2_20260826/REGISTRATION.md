# Registration: literal Faber exact-square affine-`mu2` face

Date: 2026-08-26

Status: **PREREGISTERED EXACT-Q PRODUCER PLUS GOOD-PRIME CONTROL.**

The earlier affine-`mu2` client correctly classified the seven raw
`z`-Laurent coefficients of

```text
sqrt(Q)*(Q^2+beta*Q+gamma),
Q=z^4+p*z^2+c*z+r.
```

It is not the literal ordinary Faber source when the target `h2=mu2` is
nonzero: the unitriangular Laurent-to-Faber connection has load-bearing
later-row terms.  This client therefore starts again from the frozen exact
ordinary tails `r1,...,r7`, substitutes the exact-square coefficients of
`f=Q^2`, and imposes

```text
r1=0, r2=mu2, r3=...=r7=0.                         (1)
```

It independently reconstructs the raw Laurent coefficients and checks all
seven explicit connection identities before any ideal operation.  The
preregistered reduced-support hypothesis, with `Delta=p^2-4*r`, is

```text
Square:
  c=0, Delta=0, mu2=0;

Faber affine graph:
  c=0,
  15*Delta^2-64*beta*Delta+256*gamma=0,
  Delta^2*(5*Delta-16*beta)-2048*mu2=0.             (2)
```

The exact-Q lane is theorem-producing.  Characteristic 65521 is an
independent control only.  Both are AWS-only, one capped core each.  A
failed connection, diagnostic, timeout, extra/missing component, or failed
validator is no verdict.  Even a PASS concerns only the normalized
exact-square Faber face (1); total-Rees accessibility, higher corrections,
`J`-saturation, terminal `[6,2]`, Taylor, order two, and JC2 remain open.
