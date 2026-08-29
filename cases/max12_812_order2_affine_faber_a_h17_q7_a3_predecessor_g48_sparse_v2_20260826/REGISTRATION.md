# Registration: sparse H17/q7/a3 grade-48 predecessor replay

Date: 2026-08-26

Status: preregistered exact coefficient-only producer; no theorem.

Reconstruct all seven complete normalized source rows from frozen
`tails.json`, substitute the fixed integral H17/q7/a3 series and the full
affine load graph, and convolve only coefficients of absolute grade at most
48.  Retain `d6,d2,dm,d4`, both kernel coordinates, four complements,
moving `E,K10,M,a` jets through the maximum possible excess, and every
load/target.

The exact-Q lane must match the following complete grade-48 block:

```text
C1=-3*r1*m^2/8+3*s0*m/4,
C2=3*d6*p^4/128-3*r0*m^2/8-d2*p^2/8+3*y^2/8-dm,
C3=-3*r1*m^2*p/32-3*x*y*m/8+3*s0*m*p/16,
C4=3*x^2*m^2/32-3*r0*m^2*p/16-3*y^2*p/16-d4,
C5=-3*r1*m^2*p^2/256+3*x*y*m*p/32+3*s0*m*p^2/128,
C6=-d6*p^6/512-3*r0*m^2*p^2/64+d2*p^4/128
   +3*y^2*p^2/64,
C7=3*r1*m^2*p^3/1024-3*x*y*m*p^2/256
   -3*s0*m*p^3/512.
```

It must also verify every lower coefficient is zero, the exact odd-row
redundancies

```text
C5=(3*p^2/32)*C1-(p/4)*C3,
C7=(p^2/32)*C3-(p^3/64)*C1,
```

and explicit zeros on both `D(p*m*x)` and `D(p*m*y)`.  The F65521 lane is
a software/collection control only.  Any mismatch, missing lower zero,
source hash mismatch, control failure, or resource failure is no verdict.

This is a fixed normalized graph replay, not rational-regrading, literal
source, Rees, order-two, maximum-twelve, or JC2 coverage.
