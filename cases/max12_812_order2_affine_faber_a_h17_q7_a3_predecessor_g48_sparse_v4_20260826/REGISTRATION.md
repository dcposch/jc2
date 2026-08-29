# Registration: corrected H17/q7/a3 grade-48 predecessor V4

Date: 2026-08-26

Status: preregistered corrected producer; no theorem.

V2 failed closed by omitting two moving-center/load terms.  V3 emitted the
complete block.  V4 validates the full formulas obtained from V3:

```text
C1=-3*r1*m^2/8+3*s0*m/4,
C2=3*d6*p^4/128-3*r0*m^2/8-d2*p^2/8+3*y^2/8-dm
   +15*kk*a^2*p^5/128,
C3=-3*r1*m^2*p/32-3*x*y*m/8+3*s0*m*p/16,
C4=3*x^2*m^2/32-3*r0*m^2*p/16-3*y^2*p/16-d4,
C5=-3*r1*m^2*p^2/256+3*x*y*m*p/32+3*s0*m*p^2/128,
C6=-d6*p^6/512-3*r0*m^2*p^2/64+d2*p^4/128
   +3*y^2*p^2/64-15*kk*a^2*p^7/1024,
C7=3*r1*m^2*p^3/1024-3*x*y*m*p^2/256
   -3*s0*m*p^3/512.
```

Here `a=a3` and `kk=kk0` are the leading center and `K10` coefficients.
The producer must verify every lower coefficient is zero, both odd-row
redundancies, and explicit zeros on both projective charts with
`p*m*a*kk` a unit.  It also checks a row-4 omission negative.

Exact Q is evidence; F65521 is a software control.  This is a fixed
normalized graph predecessor, not rational-regrading, literal source,
Rees, order-two, maximum-twelve, or JC2 coverage.
