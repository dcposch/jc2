# Literal Faber exact-square affine-`mu2` support result

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; EXACT CHARACTERISTIC-ZERO REDUCED
SUPPORT AND ALL SEVEN LAURENT-TO-FABER CONNECTIONS COMPUTED.  PENDING
HOSTILE REVIEW AND SOURCE-ACCESSIBILITY PROLONGATION.**

## Correction and source system

For

```text
Q=z^4+p*z^2+c*z+r,
f=Q^2,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
```

let `h_l` be the coefficient of `z^-l` in `H`, and let `r_l` be the frozen
ordinary Faber tail after substituting the exact-square coefficients of
`f`.  When `h2` is nonzero, the unitriangular connection is load-bearing;
for example

```text
r4=h4+(p/2)*h2+(c/4)*h1.                            (1)
```

Consequently the previously computed affine Laurent system
`h1=h3=...=h7=0, h2=mu2` is valid at that scope but is not the literal
ordinary-source face.  The source-facing system is

```text
r1=0, r2=mu2, r3=...=r7=0.                         (2)
```

V2 reconstructs both families independently and verifies all seven exact
connection identities before forming any ideal.

## Exact reduced support

Put `Delta=p^2-4*r`.  The exact-Q computation proves that the reduced
support of (2) is exactly the union

```text
Square:
  c=0, Delta=0, mu2=0;

Faber affine graph:
  c=0,
  15*Delta^2-64*beta*Delta+256*gamma=0,
  Delta^2*(5*Delta-16*beta)-2048*mu2=0.             (3)
```

There is no component on `D(c)`.  Singular computed the radical of the raw
seven-row ideal and the intersection of the two proposed prime ideals
independently; reduction in both directions returned zero.  It returned
exactly two minimal associated primes and raw dimension three.  The
characteristic-65521 control independently returned the same endpoint
modulo the prime.

The zero-target Chebyshev/Pell family is the sublocus

```text
beta=5*Delta/16,
gamma=5*Delta^2/256,
mu2=0
```

inside the affine graph, not a third minimal component.  On `D(Delta)` the
coefficient `p` is free.

## Rational form and controls

Write

```text
D=Delta/4,       T=z^2+p/2,       s=5*D-4*beta.
```

Then the affine graph is

```text
beta=(5*D-s)/4,
gamma=D*(5*D-4*s)/16,
mu2=D^2*s/32.                                       (4)
```

The separate hand theorem gives

```text
P(Q)=T^4-(s+3*D)*T^2/4+D^2/16,
A=T^5-(s+5*D)*T^3/4+D*(2*s+5*D)*T/16,

A^2-Q*P(Q)^2
 =-D^2*s*T^4/16+D^2*s*(s+3*D)*T^2/64+D^5/256.      (5)
```

The first post-seven Faber sentinel is

```text
r10=-D^4*(s+D)/512.                                 (6)
```

Neither (5) nor (6) is an additional ordinary source row.  The loci
`s=0,-D,-4*D` are retained as successor controls.

## Evidence and custody

Both V2 validators report `PASS_FABER_AFFINE_MU2_PROBE`; compiler and engine
return codes are zero.  Exact Q used 0.06 seconds and 16,000 KiB maximum
RSS; the prime control used 0.05 seconds and 15,380 KiB.  Both report zero
swap.

V1 is immutable fail-closed custody.  Ambiguous power/division syntax in
three connection controls caused deterministic parser errors, followed by
undefined-symbol cascades; the prime engine eventually crashed on malformed
state.  V2 added only parentheses and repaired the failure exit syntax.  No
mathematical expression, proposed component, ring, term order, or ideal
operation changed.

## Scope firewall

This is the literal normalized exact-square ordinary-Faber face, but it is
not yet a proof that the face lies in the `J`-saturated total-Rees boundary.
The displayed exact section has `r7=J/4=0`; an accessible strict arc must
produce nonzero generic `J` through a later correction.  Square-normal
defects, connection jets, all load and target jets, Rees torsion, terminal
`[6,2]`, and both Taylor families remain to be imposed.  This result neither
constructs nor excludes a strict arc, closes order two or `(8,12)`, proves
maximum twelve, nor proves or disproves JC2.
