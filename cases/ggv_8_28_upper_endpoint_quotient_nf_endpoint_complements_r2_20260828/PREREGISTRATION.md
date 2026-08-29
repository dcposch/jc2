# Preregistration: reducer-safe endpoint chart-complement recursion R2

Date: 2026-08-28

This successor consumes only the clean root-chart terminal archive with SHA-256
`1fe30b1ccf142791149b5152db519761681368b3e01c94cd82844802dee39787`.
It starts independently on each of the six exact proper ideals
`I+(Delta_root)` frozen there: P, C8P02, Q1P02, Q1P03, TRIPLE02, and
TRIPLE03.  The inherited exact quotient-rank upper bounds are respectively
9, 9, 6, 4, 6, and 4.  Rank cannot increase under the registered quotient
map; this base-change fact is the only inherited upper-bound step.

At every recursive node the job:

1. constructs a pinned ambient `std(J)` for the literal accumulated ideal;
2. normal-forms every matrix entry and every elimination update, replays the
   95 rational-unit pivots, and tracks the full 105x105 right transformation;
3. computes the 11x10 residual support after normal form;
4. starting at the inherited rank bound, tests every support-matchable minor
   until it finds a nonzero normal form, or proves the entire size zero;
   support-nonmatchable minors are frozen as literal structural zeros;
5. uses the first exact rank witness to build every denominator-cleared
   adjugate right-kernel vector, verifies all 11 residual rows and all 106
   original rows after normal form, and pulls back the complete quadratic
   `E=x14*x72+x1*x97`, including every cross term;
6. if all endpoint coefficients are zero, replaces the remainder by the exact
   ideal `J+(Delta)` and repeats without factor, gcd, content, radical, or
   primitive normalization.

Before an open chart is used, the job computes the exact saturation
`J:Delta^infinity`.  A unit saturation records an empty/nilpotent chart and
skips its kernel claim.  A proper saturation becomes the chart reducer for the
fresh pivot transform, adjugate kernel, row replay, and endpoint coefficients.
The inherited rank bound is accepted only after the exact upstream complete
rank-certificate archive and marker are independently hash-gated.

Strict terminal classifications are:

- a nonzero endpoint coefficient NF:
  `RING_LEVEL_SURVIVOR_ON_CHART_PENDING_NILPOTENCE_RADICAL`;
- a unit exact remainder after finitely many endpoint-dead nonempty charts:
  `EXACT_ENDPOINT_DEAD_ON_FINITE_GEOMETRIC_CHART_COVER`;
- a proper remainder at the iteration/time cap: `NO_VERDICT_OPEN_REMAINDER`;
- any parser, backend, replay, byte, pivot, normal-form, resource, or identity
  disagreement: `ADAPTER_FAILURE_NO_VERDICT`.

No chart-local result is promoted to a whole-stratum result until the literal
remainder ideal is the unit ideal.  The finite recursion is a geometric-point
cover; it does not assert a scheme-theoretic decomposition of `J` into its
saturation and `J+(Delta)` without an independently verified saturation-power
intersection identity.  A nonzero coefficient NF in the saturated chart ring
is ring-level only and does not assert a complex point until coefficient
nilpotence/radical is resolved.
Every node ideal, standard basis, residual, support census, rank witness,
kernel, endpoint coefficients, and successor Delta is frozen.

Pilot policy: Q1P03 runs first.  Other components remain held until the pilot
passes the full rank-witness/adjugate/original-row/endpoint/complement contract.
Thereafter independent one-core AWS lanes may fan out.  Each lane has Linux,
Amazon EC2, IMDS instance, hostname, source-hash, backend, job-tag, zero-swap,
process-group/starttime, continuous telemetry, 96-GiB address, 32-GiB file,
2-hour hard-cap, and no-orphan gates.  No heavy computation is local.  No
endpoint or HENS namespace outside this packet is mutated.

R1 is frozen as `ADAPTER_FAILURE_NO_VERDICT`: a generated reduction script
retained the literal token `REDUCER_PLACEHOLDER`, Singular emitted parser
diagnostics with return code zero, and the required pivot marker rejected the
run before any rank/minor/endpoint inference.  R2 changes only the adapter
substitution and adds an immutable generator mutation gate: the exact Q1P03
reduction must contain the intended reducer and pivot certificate marker, no
placeholder/TODO token may remain, and a deliberately injected placeholder
must be rejected before Singular starts.
