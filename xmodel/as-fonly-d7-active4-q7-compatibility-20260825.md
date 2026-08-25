# AS F-only `D=7`: the four observed active predecessor coordinates are independent Q7 obstructions

**Status: PRODUCER EXACT ON THE PREREGISTERED FOUR-COORDINATE SLICE;
PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

The preceding 66-state low-weight sampler found four basis directions whose
nonzero scalar multiples fail at the Q7 compatibility equation: Q9 Kuranishi
coordinates `t6,t8` and Q8 solution-kernel coordinates `s15,s17`.  This gate
exhausts their full combined cube

```text
(t6,t8,s15,s17) in F_3^4                         (81 states),
```

while holding the other Q9/Q8 predecessor coordinates at the canonical base
state (`t17=1`).  At every state the replay reconstructs the Q9 and Q8 digits,
asserts all 23 Q9 source rows and all 22 Q8 transition rows, and forms the
19-by-18 Q7 affine system.

The Q7 coefficient matrix is constant on the cube, has rank nine and
ten-dimensional left cokernel, and has SHA-256
`f30baed043492c723d80a787571d6cb743626da643a20f031da5b95091e6dd50`.
In the replay's fixed RREF cokernel basis, the exact compatibility map is

```text
kappa_5 = s15,
kappa_6 = 2 t6,
kappa_8 = s17,
kappa_9 = 2 t8,
all other kappa coordinates = 0.
```

The script interpolates every degree-at-most-two term and substitutes all 81
points back into the source-derived right-hand sides.  There are no quadratic
or mixed terms.  Consequently the origin is the unique Q7-compatible point
on this four-coordinate slice: none of these four previously observed
obstructions cancels another, even when they vary jointly.

The source-frozen replay ran on Box02 (`ip-172-30-0-186`) under
`/home/ubuntu/jobs/as_active4_q7_compat_20260825T032738Z`, from
03:29:06Z to 03:29:26Z, return code zero, with empty stderr.  The exact JSON
presentation has SHA-256
`fad344a6fe1e9e2ead811541e6684d2f235a5f8764a978e9fe43b87d992e0214`.

This is exhaustive only on the displayed four-coordinate affine slice.  It
does not classify the remaining Q9 Kuranishi or Q8 kernel coordinates, their
mixed interactions with these four coordinates, the six pinned Frobenius
spectators, other accepted predecessor states, fixed-cap/all-depth lifting,
counterexamples, or JC2.

