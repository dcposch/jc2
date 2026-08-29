# Result: `H16/q6/a4` grade-48 rational witness controls

Date: 2026-08-26

Status: **DUAL-AWS PASS; BOTH HAND-SELECTED RATIONAL SLICES ARE EMPTY.
FIXED-SLICE FALSIFIER, NOT A FULL EQUALITY-FAN THEOREM.**

Both exact-Q controls and both F65521 software controls completed with
engine rc `0`, coefficient-extractor control `1`, and every source-row
coefficient below grade 48 equal to zero.  On each chart the complete
seven-row grade-48 ideal has reduced standard basis `1`.

The exact-Q odd rows expose the same small obstruction on both slices.
Put

```text
T=2*s04-r14.
```

On the selected `D(x)` point, rows `C1,C3,C7` are

```text
C1= 3*T/8-1,
C3= 3*T/32-3*y4/8-3/16,
C7=-3*T/1024-3*y4/256-11/512.
```

On the selected `D(y)` point they are

```text
C1= 3*T/8+11/4,
C3= 3*T/32-3*x4/8-3/4,
C7=-3*T/1024-3*x4/256-25/256.
```

In both cases the exact row combination is the nonzero constant

```text
C7-(1/32)*C3+(1/64)*C1=-1/32.                (1)
```

Thus cancelling `K48` with the free leading `d6` is necessary but not
sufficient: another odd compatibility remains.  Equation (1) is a strong
positive control for the live full moving-series producer.

This result proves only that the two registered rational leading points
are empty at grade 48.  It does not yet show that (1) is independent of
the unspecialized grade-44 survivor parameters, so it does not close the
full equality wall.  The complete V2 chart ideals remain controlling for
that question.  No source/Rees, rational-regrading, order-two,
maximum-twelve, or JC2 conclusion is made.
