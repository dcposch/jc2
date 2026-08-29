# Registration: `H16/q6/a4` grade-48 rational witness controls

Date: 2026-08-26

Status: exact-source positive-control producer; no fan theorem.

Use `p=m=a=K10=1` and the two grade-44 survivor representatives.  The
hand cancellation diagnostic predicts the following leading values:

```text
D(x): x=1,y=0,r0=1/2,r1=s0=0,
      d6=16,d2=7,dm=-11/16;

D(y): x=0,y=1,r0=-1,r1=s0=0,
      d6=-74,d2=-61/2,dm=181/64.
```

For each chart, retain independent grade-48 coefficients of both kernels,
all four complements, all three transverse deviations, and `mu4`.
Reconstruct all seven complete source rows, require every coefficient below
48 to vanish, print all seven grade-48 equations and a reduced standard
basis.  A proper ideal is a positive witness over an algebraic closure; a
unit ideal falsifies the hand-selected leading point but does not decide the
full equality chart.  Exact Q is evidence and F65521 is a control only.

This client is deliberately a fixed rational slice.  It does not replace
the complete moving-series V2 producer, prove rational regrading, source or
Rees coverage, order two, maximum twelve, or JC2.
