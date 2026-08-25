# AS F-only `D=7`: Q9-fibre Kuranishi chart and Q8 survivor

**Status: PRODUCER EXACT AT DISPLAYED CHART/WITNESS SCOPE; PROVISIONAL
PENDING DIFFERENT-MODEL REVIEW.**

The first Q9 predecessor has a 19-dimensional affine solution fibre in the
32 restored coefficients.  Taking the frozen canonical Q9 witness as origin
and an exact RREF kernel basis, the next 22 rows split into thirteen image
rows and nine degree-eight obstruction rows.  The AWS compiler constructs

```text
B(t)s + kappa(t) = 0,                             (1)
```

where `t,s in F3^19`.  Unreduced integral affine lifts are used so the
source formulas give `deg B<=1` and `deg kappa<=2` without a digit-reduction
discontinuity.  Exact interpolation and 64 deterministic off-grid controls
give

```text
B(t) = 0,
kappa_1=t_10,  kappa_2=t_13,  kappa_4=t_11,
kappa_5=t_15,  kappa_7=t_12,  kappa_8=2+t_17,      (2)
```

with the other three obstruction coordinates zero.  Thus (1), in this
affine-lift chart, has the exact 13-dimensional zero locus

```text
t_10=t_11=t_12=t_13=t_15=0,  t_17=1,             (3)
```

containing `3^13=1,594,323` parameter points.  Every image solution `s` is
then free because `B=0`.

The bounded search stopped at its first point of (3), `t=e_17`, after 36
distinct points.  For that point the compiler independently reduces the
Q9 coordinates to canonical digits and solves the full 22-row canonical
transition.  It obtains

```text
Q9 vector: x_23=x_30=1, all other x_i=0,
Q8 vector: all 32 entries zero,
full Q8 rank pair: (13,13).                        (4)
```

Both the Q9 source rows and all 22 Q8 rows are substituted at (4).  Hence
the earlier pointwise obstruction at the chart origin does **not** kill the
predecessor: a nearby canonical Q9 point survives the displayed Q8 gate.

The source-frozen run on Box02, tag
`as_q9_fibre_kuranishi_q8_20260825T021044Z`, took 11.74 seconds and 21,736
KiB maximum RSS, with return code zero and empty standard error.  A separate
coordinator relaunch under tag
`as_q9_fibre_kuranishi_q8_root_20260825T0220Z` produced byte-identical
standard output and JSON.  Their shared hashes are

```text
stdout       523d2eec3ca119332db6d195263562a733a784ae2f2c0aee412f9db7f73071ff
presentation c3e4d492b54945b80d16a392dfdec53dcf72b7e88e0f9372d884b2144ca85676
stderr       e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
```

Two boundaries remain.  Equation (3) is an exact description for the
unreduced affine-lift presentation; canonical digit-lift equivalence was
tested on the 36 searched points, not exhaustively on all `3^19` points.
Also, the six derivative-zero degree-six `C6,D6` Frobenius digits that were
spectators at Q9 are fixed to zero here.  Thus (4) is a valid canonical
survivor, but (3) is not yet a classification of the full `3^25` fibre.
Degree seven and all lower rows remain open.  No recurrence, all-depth
lift/no-lift, counterexample, or JC2 conclusion is licensed.
