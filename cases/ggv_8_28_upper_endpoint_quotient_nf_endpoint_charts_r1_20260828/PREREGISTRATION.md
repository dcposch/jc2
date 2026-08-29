# Preregistration: reducer-safe quotient-NF endpoint charts R1

Date: 2026-08-28

This job consumes only the banked exact quotient-normal-form rank packets from
r5/r6.  It does not recompute or reinterpret a qring rank, gcd, factor, radical,
or component.  The six root strata and certified residual ranks are:

```text
P          r=9  (r6 descent)
C8P02      r=9  (r6 descent)
Q1P02      r=6  (r5)
Q1P03      r=4  (r5)
TRIPLE02   r=6  (r5)
TRIPLE03   r=4  (r5)
```

Immutable upstream packets are admitted only at these SHA-256 gates:

```text
r5 source     908b73cd46821ec6a64ebd8e3aa17365616865c089dbdd45644b18baefc28bfb
P r6          fb778b1a7078314fa1fb941d39327cb9d99eab2ad2aa5a4c6c88f45062e26173
C8P02 r6      99cccf8c0508aa8818b00541eab0f29a1596ecbf7dcad9d9beee1a220b2419e6
Q1P02 r5      992dbd0e0a81f6f37901f24c63141607c29c26d2a28195bebc37698c026b8424
Q1P03 r5      9a8cf752e526d29679fa673af1359b81b66302af73998806c022a4e80c306c9c
TRIPLE02 r5   b947a2d3e81525902a93500026020c2cf9580f070767757389daadb9a6bbe3b2
TRIPLE03 r5   1d1871532a845f2ac964886035c06abcc211ae80f5c68e153850951ba242b809
build_nf_rank 7ba6c106ff62a3bfc289be408d151bda7e85d73cb5868543d86ebe926f272b0a
```

For each stratum the job replays the original specialized 106x105 matrix in
an ambient polynomial ring with the pinned `std(I)`.  It repeats the exact 95
rational-unit pivots, performs normal form after every entry and update, and
tracks the complete 105x105 right column transformation.  The resulting
pivot and 11x10 residual files must be byte-identical to the banked packet.

The banked nonzero-NF rank witness selects rows `I`, columns `J`, and
`Delta=det(R[I,J])`.  For every free residual column, Cramer's rule constructs
the denominator-cleared adjugate kernel vector: its free coordinate is Delta
and each J-coordinate is the negative determinant with that column replaced.
All 11 residual rows are reduced against `std(I)` and must vanish; these are
the complete chart-specific bordered `(r+1)`-minor identities.  The vectors
are lifted through the tracked 95-pivot column transform, and all 106 rows of
the original matrix are independently replayed to normal form zero.

The exact quadratic is `E=x14*x72+x1*x97`.  Every diagonal and cross
coefficient on the full chart kernel basis is formed, its localization
denominator is cleared by the scaled adjugate construction (equivalently a
common `Delta^2`), and its coefficient is reduced by `std(I)`.

Strict per-chart classification:

- all coefficient normal forms zero: `ENDPOINT_DEAD_ONLY_ON_D_DELTA`;
- any coefficient normal form nonzero:
  `RING_LEVEL_SURVIVOR_ONLY_PENDING_NILPOTENCE_RADICAL`.

Neither marker is a whole-stratum or geometric verdict.  The complement is
created exactly as `I+(Delta)`, its pinned standard basis and proper/unit
status are frozen, and a proper complement is explicitly
`NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED`.  Successor recursion must use that
exact ideal; it may not infer the complement from ambient gcd/factor output.

One AWS `r6i.4xlarge` lane, one pinned core, 96-GiB address-space cap, 2-hour
hard cap, 32-GiB file cap, Linux/Amazon EC2/IMDS/job-tag/source/backend gates,
zero total swap before and throughout, process-group/starttime custody, and a
final no-orphan census are required.  Before the payload, a separately frozen
tiny Singular parser/reducer/Cramer/cross-term/complement fixture must pass.
Any banked-byte disagreement, pivot,
normal-form, kernel replay, endpoint parse, resource, or adapter failure is
`ADAPTER_FAILURE/NO_VERDICT`.  No universal endpoint, radical, nilpotence,
Keller-map, or existence/nonexistence inference is authorized.
