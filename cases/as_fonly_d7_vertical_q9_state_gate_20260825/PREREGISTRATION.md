# Q9 source-state discriminator

Consume the exact corrected-Q10 predecessor and reproduce the controls
`1085103`, `629115`, `260847`, and `33225`.

For every Q10-visible state, reconstruct canonical integer representatives
of the recorded first and current high digits.  Prove the required integer
divisions and attach exactly these previously suppressed variables:

```text
C2,D2:  6 coefficients, accepted E degree 1 gives 2 rows;
C4,D4: 10 coefficients, accepted E degree 3 gives 4 rows;
W7,Z7: 16 coefficients, accepted F degree 6 gives 7 rows.
```

Then impose all ten coefficients of

```text
G9 = (M9/3) + {C,D}_9 + T9 = 0 mod 3,
```

where `T=A Z_y+W_x V_y-U_y Z_x-W_y V_x`.  This is a 23-row affine
system in 32 variables.  Classify it pointwise over F3 by exact row
reduction, retain every rank stratum, emit an explicit first witness when
one exists, and hash the ordered state/fibre stream.  Check source-honestly
that the six current degree-six Frobenius spectators remain absent.

Zero compatible Q10 states is a finite-branch obstruction at degree nine;
positive states proceed to lower rows.  Any source division, predecessor
control, affine-linearity, witness, shard, timeout, OOM, or aggregate
failure is no verdict.  No lower row, recurrence, all-depth,
characteristic-zero, no-lift, counterexample, or JC2 inference is licensed.

