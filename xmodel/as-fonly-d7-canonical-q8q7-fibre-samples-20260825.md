# AS F-only `D=7`: 64 canonical Q8-to-Q7 fibre samples

**Status: PRODUCER EXACT AT 64 DISPLAYED CANONICAL PREDECESSOR POINTS;
QUADRATIC FIBRE PRESENTATION IS A CONTROL, NOT A WHOLE-FIBRE THEOREM;
PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

The canonical-carry question differs from the previously frozen unreduced
affine-lift calculation because reducing a digit before an exact division by
three can create a higher-degree F3 carry function.  This producer samples the
11-dimensional slice `t6=t8=0` of the canonical Q9 chart at 64 deterministic
states: zero, both nonzero multiples of each of the eleven coordinate axes,
and 41 off-axis controls.

At every sampled state, direct source substitution gives:

```text
all 23 Q9 rows = 0;
Q8 rank pair = (13,13), with a 19-dimensional solution fibre;
the canonical Q8 particular solution y0 is the zero vector;
at y0, the Q7 coefficient matrix has rank 9 and cokernel dimension 10;
the Q7 cokernel RHS at y0 is zero.
```

Thus the zero Q8-fibre coordinate is an actual, directly substituted
Q7-compatible witness at all 64 sampled Q9 states.  The common Q7 matrix hash
is
`f30baed043492c723d80a787571d6cb743626da643a20f031da5b95091e6dd50`.
This is a pointwise continuation result and falsifies any claim that the
canonical Q8-to-Q7 gate already kills these sampled predecessors.

For navigation, each shard also fitted the Q7 cokernel function on the 19 Q8
RREF coordinates from the 381-point quadratic design (zero, plus and minus
each basis vector, and all pair sums) and checked 64 deterministic off-grid
points.  All 64 fitted presentations are identical and linear:

```text
kappa_5 = s15,
kappa_8 = s17,
all other displayed fitted coefficients = 0.
```

The fitted presentation has model zero count `3^17 = 129140163` at each
sample.  **This is only `MODEL_COUNT`.**  The 64 controls do not prove a global
degree-two bound for the canonical carry circuit.  Consequently neither the
formula nor `3^17` is promoted to a whole-fibre theorem.  Every successor must
directly substitute its consumed witnesses, or first prove a degree bound or
exhaustive functional identity.

The source-frozen 64-lane run used Box02 (`ip-172-30-0-186`) at
`/home/ubuntu/jobs/as_canonical_q8q7_samples_20260825T041000Z`, from
04:07:56Z to 04:08:40Z, return code zero, with every shard and aggregate
stderr empty.  The aggregate JSON SHA-256 is
`c829b22e8cf65cc7cc025215b08fdf9ecddea84fc931c418c5c046e996dbb1eb`;
the ordered sample stream SHA-256 is
`9cdc77bd0c6f2eff9f01d83b456f5711c5b4f1b8630e04103bf455be8c8294dc`.

Only these 64 Q9 states and their zero Q8-fibre coordinates are covered
pointwise.  The other Q8 fibre coordinates, the other Q9 states (including
the two omitted chart directions), the six pinned Frobenius spectators,
later divided carries, fixed-cap/all-depth lifting, counterexamples, and JC2
remain outside scope.

