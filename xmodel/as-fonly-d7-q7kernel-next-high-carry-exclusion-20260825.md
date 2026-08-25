# AS F-only `D=7`: exhaustive exclusion below one Q8 survivor

**Status: PRODUCER EXACT AT THE DISPLAYED FIXED-Q9/Q8 BRANCH; PROVISIONAL
PENDING DIFFERENT-MODEL REVIEW.**

Fix the canonical Q9 vector with `x23=x30=1` and the zero Q8 restored
vector.  The following Q7 transition is a homogeneous 19-by-18 system over
`F3` of rank nine, so its full solution set is a nine-dimensional kernel.
The source-frozen compiler computed its canonical RREF basis and exhausted
all `3^9=19,683` kernel points in 27 disjoint shards.

For each point it reconstructed the integral digit representatives and
formed the next fifth-order residual in two independent ways:

```text
R = G4/3 + S(U,V;H,J) + Rmix(C,D;W,Z),
R = (det J(P,Q)-1)/243  (mod 3).
```

All preceding divisions are asserted exact over the integers.  The two
constructions agree coefficientwise in homogeneous degrees 12 through 7
for every state.  The ordered degree-12-through-9 stream has SHA-256
`6e4df88330f8a9ee169d3ec105ba08c655f13ae6d5c6a50dbb53f375a1265c10`.

The next Q6 equation is a seven-row divergence equation in sixteen
homogeneous degree-seven coefficients.  Its coefficient matrix has rank
seven, hence every Q7 state has a nine-dimensional Q6 solution fibre.
Termwise source reconstruction on all sixteen coordinate directions shows
that those Q6 digits enter the following carry only in degrees at most
eight.  Thus degrees 12 through 9 are independent of the choice inside the
Q6 fibre.

The complete high-row map on the nine Q7-kernel coordinates is exactly
quadratic—and in fact constant:

```text
R12=R11=R9=0,
R10=x^10
```

for all 19,683 points.  Its zero locus is empty; every state first obstructs
in degree ten.  Since the divergence of a fifth cap-seven correction has
degree at most six, no Q7 or Q6 choice beneath this fixed Q9/Q8 state can
continue one more digit.

The AWS-only execution ran on Box02 (`ip-172-30-0-186`) under tag
`as_q7kernel_next_high_20260825T030036Z`, from 03:01:09Z to 03:01:24Z,
with return code zero.  All 27 shard sentinels and the aggregate sentinel
are present, and every stderr file is empty.  The aggregate JSON has
SHA-256 `87f63bdd0a9408ac1b2a019b4de9e17645625293fc75b3460a334b70e8f0a96f`.

This is an exhaustive branch theorem only after fixing that canonical Q9
vector and the zero Q8 vector.  It does not cover the thirteen other free
directions in the earlier Q8 affine zero locus, the six Q9 Frobenius
spectators pinned to zero there, other Q9 predecessors, the full cap-seven
system, an all-depth lift/no-lift statement, a counterexample, or JC2.
