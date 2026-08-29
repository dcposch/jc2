# Exact-square affine-`mu2` support result

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; EXACT CHARACTERISTIC-ZERO REDUCED
SUPPORT COMPUTED, PENDING HOSTILE REVIEW AND SOURCE-LICENSED
PROLONGATION.**

Let

```text
Q=z^4+p*z^2+c*z+r,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
```

with `sqrt(Q)=z^2+O(1)` at infinity, and let `E_l` be the coefficient of
`z^-l` in `H`.  The simultaneous load/target face studied here is

```text
E1=0, E2=mu2, E3=...=E7=0.                         (1)
```

The exact-Q computation proves that the reduced support of (1) is exactly
the union of the following three components:

```text
Square:
  c=0, p^2-4*r=0, mu2=0;

Chebyshev/Pell:
  c=0,
  16*beta=5*(p^2-4*r),
  256*gamma=5*(p^2-4*r)^2,
  mu2=0;

Affine target:
  p=c=0,
  5*r^2+8*r*beta+16*gamma=0,
  32*mu2=r^2*(5*r+4*beta).
```

Singular computed `rad(I)` and the intersection of these three proposed
component ideals independently.  Reduction in both directions returned
zero, and `minAssGTZ(I)` returned exactly three minimal components.  The
off-`c=0` saturation is the unit ideal, so no reduced component exists on
`D(c)`.  An independent characteristic-65521 run returned the same endpoint
modulo the prime.

Both AWS validators report `PASS_AFFINE_MU2_PROBE`, with compiler and engine
return codes zero.  The exact-Q lane used 0.07 seconds and 16,492 KiB maximum
RSS; the prime lane used 0.06 seconds and 15,948 KiB.  Both report zero swap.

## Rational form of the new component

Put `t=5*r+4*beta`.  The affine-target component has the polynomial
parametrization

```text
beta=(t-5*r)/4,
gamma=r*(5*r-2*t)/16,
mu2=r^2*t/32.
```

The separate hand derivation records the exact generalized-Pell remainder
and the next Laurent sentinel `h10=-r^4*(t-r)/512`.  That sentinel is useful
for designing the next computation, but it is not one of the seven source
rows in (1) and is not promoted here as a Keller equation.

## Custody and firewall

V1 is preserved as fail-closed negative custody.  Its algebraic output
already matched the three-component union, but redundant Singular library
loading emitted redefinition diagnostics.  V2 removed only the redundant
load; no equation, ideal, term order, proposed component, or endpoint check
changed.

This producer classifies only the reduced support of the affine Laurent
receiver (1).  It does not identify a literal total-Rees source chart, license
the next correction row, impose the terminal `[6,2]` or Taylor receivers,
construct or exclude a strict arc, close order two or `(8,12)`, prove maximum
twelve, or prove or disprove JC2.
