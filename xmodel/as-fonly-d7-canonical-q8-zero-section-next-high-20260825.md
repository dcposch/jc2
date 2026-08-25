# AS F-only `D=7`: next-high exclusion on 64 canonical Q8 zero sections

**Status: PRODUCER EXACT AT THE 64 DISPLAYED ZERO RREF-FIBRE-COORDINATE
SECTIONS; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

This successor consumes the corrected canonical sampler through its erratum:
at each of 64 sampled Q9 states, `s=0` denotes the zero coordinate in the
19-dimensional Q8 RREF fibre and the actual Q8 coefficient vector is the
displayed affine particular `y0`.  Thirteen of these `y0` vectors are zero and
51 are nonzero.

For every state, the AWS producer independently reconstructs the integer
source and verifies the 23 Q9 rows and all 22 Q8 rows at `(x,y0)`.  It then
reconstructs the 19-row Q7 system.  Uniformly:

```text
Q7 rank pair = (9,9);
Q7 solution-fibre dimension = 9;
all 3^9 = 19683 Q7 solutions are exhausted;
recursive divided rows = direct rows from the literal integer Jacobian;
no solution makes every degree-12, -11, -10, and -9 high row vanish.
```

Hence the next divided high carry excludes the entire Q7 fibre over each of
these 64 exact `(Q9,Q8)` zero-section points.  There are no survivors among
`64 * 19683 = 1259712` directly checked Q7 states.

The carry is not constant across the sample.  Exact exhaustive quadratic
presentations of the nine-variable Q7-fibre residual fall into 31 distinct
coefficient-hash clusters.  The largest cluster contains the zero state, all
22 axis samples, and three off-axis samples; the other 28 off-axis samples
split among 30 additional exact signatures.  This variation supports the
planned full-chart carry-signature census and warns against extrapolating the
fixed-branch residual.

The successful V3 run used Box02 (`ip-172-30-0-186`) at
`/home/ubuntu/jobs/as_canonical_q8_zero_next_high_20260825T042300Z_v3`,
from 04:23:11Z to 04:23:58Z, return code zero.  All 64 shard and aggregate
stderr files are empty.  Aggregate JSON SHA-256 is
`0f72ec2ff2fc5b6f8340a602acdc40d6f4b8de50995160655e066cee0cd96e83`;
the ordered state stream SHA-256 is
`96c5e8a28a12c1e845e314be03a3e6e61d6cfe25ae5aac5005fb417d9ebd0272`.

V2 is preserved as a fail-closed negative control at
`/home/ubuntu/jobs/as_canonical_q8_zero_next_high_20260825T041900Z_v2`.
It incorrectly asserted that the affine particular itself was zero, emitted
only 13 JSON outputs, and stopped with return code one.  No V2 result is used.

The exclusion is only for the zero RREF-fibre coordinate at 64 sampled Q9
states.  The other 17 Q8 compatibility directions left by the sampled Q7
equations, other Q9 states, the two omitted chart directions, six pinned
Frobenius spectators, later transitions elsewhere, fixed-cap/all-depth
lifting, counterexamples, and JC2 remain outside scope.

