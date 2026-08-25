# AS F-only `D=7`: no one-coordinate mixed cancellation of the four Q7 obstructions

**Status: PRODUCER EXACT ON 28 PREREGISTERED FIVE-COORDINATE SLICES;
PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

The reviewed chart has 13 free Q9 Kuranishi coordinates and a 19-dimensional
Q8 solution kernel.  The preceding active-four theorem singled out
`t6,t8,s15,s17`.  For each of the other 28 coordinates `u`, this gate exhausts

```text
(t6,t8,s15,s17,u) in F_3^5                     (243 points per slice).
```

At every point the replay reconstructs the Q9 digit, solves the exact Q8
affine system, uses its canonical RREF kernel chart, asserts all 23 Q9 source
rows and 22 Q8 transition rows, and forms and solves the 19-by-18 Q7 system.
The 28 shards cover 6,804 evaluations, with deliberately overlapping `u=0`
control faces.

Every slice has exactly the same outcome:

```text
Q7 rank pair (9,9):   3 points,
Q7 rank pair (9,10): 240 points,
compatible points:   (0,0,0,0,u), u=0,1,2.
```

In particular, no point with nonzero active-four projection is compatible.
An arbitrary scalar in any *one* remaining predecessor direction cannot
cancel any combination of the four displayed Q7 obstructions.  The Q7 matrix
is in fact constant at every reported point and across every shard, with the
same SHA-256
`f30baed043492c723d80a787571d6cb743626da643a20f031da5b95091e6dd50`
as the active-four gate.

The source-frozen V2 replay ran in 28 parallel lanes on r6a
(`ip-172-30-0-34`) under
`/home/ubuntu/jobs/as_active4_plus_one_v2_20260825T034300Z`, from
03:44:31Z to 03:44:52Z, return code zero, with all stderr files empty.  Its
ordered shard-JSON stream SHA-256 is
`45195188b230c9065d2daef794fe7249f791b2bb0bb52ec78d1c1981ab6fe092`;
the aggregate JSON SHA-256 is
`b46f04b4d3ce1dec9f9d61dcc5dbd0e128c73eda685e8a5e02797655db67d11f`.

V1 is retained as a failed-aggregation negative control: all mathematical
shards ran, but a result-path bug overwrote bootstrap files and caused the
aggregate to fail closed.  V2 pins V1 and makes only the registered two-line
output-routing correction before rerunning from source.

This does not test interactions involving two or more of the remaining 28
coordinates.  It does not free the six pinned Frobenius spectators or classify
other predecessors, later carries, fixed-cap/all-depth lifting,
counterexamples, or JC2.

