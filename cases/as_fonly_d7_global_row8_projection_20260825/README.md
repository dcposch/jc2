# AS F-only D7 global Q9 row-8 projection

Status: **PRODUCER-EXACT / PENDING DIFFERENT-MODEL REVIEW**.

This case consumes the corrected Q10-to-Q9 compiler at SHA-256
`54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2`
and projects every complete Q9 affine fibre to
`(c2_1,c2_2,d2_0,d2_1)`.  It does not reuse the old 13-trit canonical chart.

The frozen preregistration swapped the labels `rx` and `ry`.  Read it only
with `PREREGISTRATION_ERRATUM_V2.md`.  The corrected scalar is

```text
omega = floor((c2_1+2*d2_0)/3)
        + 2*h*floor((2*c2_2+d2_1)/3) mod 3.
```

Corrected V2 and control-complete V3 were separately executed in 27 shards on
AWS Box02.  Every shard returned rc zero and directly reconstructed the
literal integer source expression on every projected tuple.  Their ordered
state-stream digest agrees.  Exact aggregate:

```text
Q10 source states                 33,225
nonempty Q9 predecessor states    11,881
Q9 completions             8,096,356,425,843
omega=0,1,2 each           2,698,785,475,281
zero-locus class on all fibres    zero-partial
compatible structural bases       79
```

Thus `omega` is not an obstruction at Q9 alone: every current nonempty Q9
fibre contains `omega=0` completions.  Q8 through Q3 restoration has not been
imposed and remains open.

AWS custody:

- corrected V2:
  `/home/ubuntu/jobs/as_global_row8_projection_20260825T1417Z_v2`;
- control-complete V3:
  `/home/ubuntu/jobs/as_global_row8_projection_20260825T1422Z_v3`;
- aggregates:
  `/home/ubuntu/jobs/as_global_row8_projection_aggregate_20260825T1420Z_v2`.

The V1 source at SHA-256 `9cca43b1...` implemented the swapped formula.  Its
15 fail-closed shards and 12 coincidental passes are a negative control, not
evidence.  V2 and V3 are distinct corrected source hashes `8d1b070c...` and
`c0951aaf...`; V3 adds rank-pair and fibre-size controls.  They are separate
executions of closely related source, not independent implementations.

Replay the aggregate on AWS (not the local Mac):

```text
python3 aggregate_projection.py SHARD_ROOT OUTPUT_JSON
python3 aggregate_projection.py --require-v3-controls SHARD_ROOT OUTPUT_JSON
```

Refusal scope: no Q8/Q7/Q6/Q5/Q4/Q3 restoration, no complete finite-depth
map, no all-depth lift, no counterexample, and no JC2 inference.
