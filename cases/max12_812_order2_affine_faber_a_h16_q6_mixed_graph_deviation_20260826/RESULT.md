# Result: mixed graph-deviation/quadratic predecessor at `H=16,q=6`

Date: 2026-08-26

Status: **DUAL-AWS PASS; MIXED FACE SURVIVES.  DIAGNOSTIC PRODUCER,
NOT AN ARC OR EXCLUSION THEOREM.**

The exact-Q Box03 lane and F65521 r6d control reconstruct all seven frozen
ordinary source rows.  Grades below 44 vanish, arbitrary moving `E` and
`K10` tangent jets cancel on the exact affine graph, and the complete
grade-44 block is

```text
C1=-3*r1*m^2/8+3*s0*m/4,
C2= 3*d6*p^4/128-3*r0*m^2/8-d2*p^2/8+3*y^2/8-dm,
C3=-3*r1*m^2*p/32-3*x*y*m/8+3*s0*m*p/16,
C4= 3*x^2*m^2/32-3*r0*m^2*p/16-3*y^2*p/16,
C5=-3*r1*m^2*p^2/256+3*x*y*m*p/32+3*s0*m*p^2/128,
C6=-d6*p^6/512-3*r0*m^2*p^2/64+d2*p^4/128
   +3*y^2*p^2/64,
C7= 3*r1*m^2*p^3/1024-3*x*y*m*p^2/256
   -3*s0*m*p^3/512.
```

Eliminating the three transverse deviations begins with

```text
r1*m^2-2*s0*m,
x*y*m,
x^2*m^2-2*r0*m^2*p-2*y^2*p,
```

and the exact full elimination ideal is printed identically in both lanes.
Neither projective chart is a unit (`UNIT_X=UNIT_Y=0`).  On `D(p*m*x)` a
simple representative is

```text
y=0,       r0=x^2/(2*p),       s0=r1*m/2,
```

with `d2` then solved from `C6` and `dm` from `C2`.  On `D(p*m*y)` one has

```text
x=0,       r0=-y^2/m^2,        s0=r1*m/2,
```

and again `C6,C2` solve transverse deviations.  Thus a graph-deviation
tie can absorb the first quadratic obstruction; the low-kernel empty block
cannot simply be reapplied after the grade-42 graph.

The next exact functional on this survivor has center-bearing initial part

```text
a*lambda^2*(-3*M^2*X^2/8+3*E*Y^2/2).
```

It is a unit on either projective chart whenever it strictly precedes the
intrinsic cubic.  For general valuations this suggests the finite split

```text
alpha < H-2q: center functional first, unit on both charts;
alpha > H-2q: intrinsic cubic first;
alpha = H-2q: one rational equality face on each chart.
```

That composition is a successor design, not proved by this fixed
representative.  V1 stopped before algebra because the wrapper pre-created
the compiler output directory; it is deployment-negative only.

This result does not prove rational-regrading invariance, the iterative
graph lift, the equality-face equations beyond the displayed functional,
literal source coverage, total Rees, order two, maximum twelve, or JC2.
