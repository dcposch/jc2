# AS F-only `D=7`: exact global Q7 Kuranishi map on the unreduced affine-lift chart

**Status: PRODUCER EXACT ON THE DISPLAYED UNREDUCED AFFINE-LIFT CHART;
PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

On the frozen fixed-predecessor branch, the Q9-to-Q8 presentation has 13 free
Q9 Kuranishi parameters `t` and a fixed 19-dimensional Q8 kernel `s`.  A
source audit shows that, for unreduced affine integer representatives, the
chosen Q8 section is affine in `(t,s)`, the Q7 unknown-coefficient matrix is
affine, and the Q7 right side has total degree at most two.  The only nonlinear
source term is the bilinear bracket `[C,D]_7`; exact divisions by three do not
increase degree.

The AWS producer evaluates zero, both nonzero scalar multiples of every one
of the 32 basis vectors, and all 496 pair sums.  The basis evaluations force
the affine Q7 matrix to be globally constant, of rank nine with
ten-dimensional left cokernel and SHA-256
`f30baed043492c723d80a787571d6cb743626da643a20f031da5b95091e6dd50`.
The 561-point design then reconstructs the exact degree-two cokernel map.
Sixty-four deterministic off-grid points substitute back exactly.

There are only four nonzero coefficients, all linear:

```text
kappa_5 = s15,
kappa_6 = 2 t6,
kappa_8 = s17,
kappa_9 = 2 t8,
all other kappa coordinates = 0.                       (1)
```

Every square and cross coefficient, including all interactions among the 28
other coordinates, is zero.  Hence the exact Q7 compatibility locus in this
unreduced affine-lift chart is the 28-dimensional affine subspace

```text
t6=t8=s15=s17=0.                                      (2)
```

This upgrades the axis and active-plus-one samples to a whole-chart statement:
inactive parameters cannot nonlinearly cancel the four active obstructions in
the licensed unreduced presentation.

The canonical boundary remains load-bearing.  Coefficientwise reduction of
the 64 off-grid unreduced controls gives:

```text
36: Q9 rows pass, Q8 rows fail;
28: Q9 and Q8 rows pass, Q7 has rank pair (9,10);
 0: directly reduced canonical Q7 survivor.
```

These controls demonstrate, rather than close, the carry gap.  Reducing an
integer digit representative before an exact `/3` can create a higher-degree
carry function.  The theorem is therefore not a global canonical-digit
classification.  The precise successor must retain the representative/carry
translation state (or prove an existence-preserving carry conjugacy) and then
canonical-verify the resulting strata.

The source-frozen 36-shard run used Box02 (`ip-172-30-0-186`) at
`/home/ubuntu/jobs/as_global_q7_kuranishi_20260825T040000Z`, from
03:58:57Z to 03:59:39Z, return code zero, with every stderr empty.  The
presentation SHA-256 is
`8207120ff8c5d08204005dd941de2b6bce2b5f62c8b10172b2811ae714306d65`;
the ordered shard stream SHA-256 is
`10744f1a874446b63e7cac000265e35a72b78a3f36c407dd0c85f10c027a05fc`.

The six frozen predecessor Frobenius spectators, canonical carry translation,
other predecessors, subsequent rows, fixed-cap/all-depth lifting,
counterexamples, and JC2 remain outside scope.

