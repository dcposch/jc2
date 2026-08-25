# Q9 to Q8 Lyapunov--Schmidt discriminator

Consume the source-frozen corrected-Q10/Q9 compiler, but do not enumerate
any Q9 completion fibre.  On the exact first emitted Q9 witness, restore
only the layers that can reach the next total-degree-eight obstruction:

```text
C3,D3:  8 coefficients; accepted E_2 gives 3 rows;
W4,Z4: 10 coefficients; accepted F_3 gives 4 rows;
W6,Z6: 14 coefficients; accepted F_5 gives 6 rows.
```

After these 13 image equations, impose all nine coefficients of

```text
G_8 = (F_8/3) + {C,D}_8 + T_8 = 0 mod 3,
T=A Z_y+W_x V_y-U_y Z_x-W_y V_x.
```

Every division must be proved over the integers before reduction.  Recheck
the 23 Q9 rows, build the exact 22-by-32 affine transition matrix, split its
rank as 13 image pivots plus the rank of the induced 9-row map on the
19-dimensional kernel, and substitute a witness if compatible.

Full Kuranishi rank nine proves only that this one Q9 state has no
degree-eight obstruction for any right-hand side in the registered source
section.  Rank deficiency freezes the exact cokernel and obstruction.
Either result is pointwise and does not license a full Q9-fibre census,
recurrence, all-depth lift/no-lift, characteristic-zero counterexample, or
JC2 claim.

