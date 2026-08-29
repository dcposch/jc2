# Preregistration: narrow adapter repair and unchanged strata relaunch r3

Date: 2026-08-28

## Frozen predecessor and classification

All four r2 lanes passed AWS identity, resource, zero-swap, source, process
group, and no-orphan custody, then stopped before the full matrix computation
at `NO_VERDICT_ADAPTER_SELFCHECK`.  The common cause is exact and
non-mathematical: the tiny selfcheck declared a matrix named `NF`, but `NF` is
a reserved Singular identifier.  The frozen diagnostic reproduced

```text
last reserved name was `NF`
```

before the expected field-replay marker.  No r2 rank or endpoint conclusion
exists.  Preserve r2 as `ADAPTER_FAILURE / NO_VERDICT`.

Frozen r2 hashes:

```text
SOURCE.sha256  5f14a73bc9473d05a466954c1474cad73bfb33ea8eea65db30bebac857205f16
PREREGISTRATION.md  31bf1c6e772a1dfd7dc9e1ce71e610e266bc559b491a6fb1d616921fddb92312
source archive  b01ad61bf69aa3ce9a405b0c5cd6f149afb2d7b784b6b75e5467764863a2bef4
frozen selfcheck  4582e1784e3acc69878fdd3649d18f8ec7d64804b4968536ff7e2aedf19c1888
```

Diagnostic r1 source hashes are
`d6c0440fbb14d66805d43c7909ce5be17c9d551dd20701c7f8213e1a567f6600`
for `tiny.sing` and
`740e96bbfe2ff954b18f751e005f06c5edcc868662fe401749bc24f0636994e3`
for its source archive.

## Only authorized mutation

The mathematical compiler, 106-by-105 matrix, exact `P`, Fitting data,
factorization logic, charts, quotient branches, complete quadratic pullback,
classification, resource caps, and lane ordering are byte-identical to r2.

The r3 selfcheck verifies the frozen r2 selfcheck hash and exactly six
standalone `NF` tokens.  It first runs a negative control that must reproduce
the reserved-name error and must not print an unexpected-success marker.  It
then replaces only those six tokens by `NFIELD`.  The exact materialized
selfcheck hash must be

```text
de8be7ab8b715a7487166283178142ca4e039a4f05c266703ba5823fb523b9cb
```

and the entire r2 selfcheck must pass.  The runtime worker is likewise an
exact, counted path-only transform of frozen r2 worker
`8417b551c251262618fe388b8d92819d5fbb56e548287aee026104564255e718`:
it points the case/preflight/selfcheck at r3 while retaining the r2 compiler.
Its required generated SHA-256 is
`8c5705b1124efead1649724d3db7eb03f33e8ff44311ce6114d6a3f8efaf90da`.

Frozen r3 adapter hashes:

```text
9c7048e137b2395e0e7d7a2025ff6f7789c7db904e382c5f32c6b7582fe827f8  PLAN.json
8f91b523c1b481ae699042a940b407d8914152c69878176095e5985c4199ed0a  aws_preflight.py
73657e5498878c2fb041b8a4e4905c57f9c6c467170c4196b2d8ad19780ad710  aws_run_remote.sh
b72e54fc9f5c04ae3187352d62171cf5b0c59f5fe83131a49b5f59d83317c43f  build_worker_r3.py
b6c2d94dedae4ecaf23032368273d2b25967f6cac593da8b24087dc5b64c80b0  selfcheck_strata_r3.py
```

## Unchanged exact target and strict verdicts

Replay r2's exact irreducibility proof and dense function-field chart for
`P`, and its exact factor/multiplicity decomposition for `c8=q1=0`, `c8=P=0`,
`q1=P=0`, and `c8=q1=P=0`.  On every chart/irreducible branch replay `M*N=0`
and every diagonal and cross coefficient of

```text
E(Nt),  E=x14*x72+x1*x97.
```

A nonzero coefficient is `PASS_EXACT_GENERIC_ENDPOINT_SURVIVOR`.  Complete
generic zero is only `GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING`; it does not
classify the whole component or rank-jump fibers.  Timeouts, reducer errors,
factor disagreement, or replay failures remain `NO_VERDICT`.

## AWS custody

Relaunch the unchanged four mathematical lanes on the same audited hosts in
fresh namespaces and updated exact job tags:

```text
p            i-02cb2b4a379ffcc64 r6i.4xlarge ggv_lambda0_endpoint_strata_p_r3_20260828T135000Z_r6a
c8q1         i-0f089e64c378f5da3 r6i.4xlarge ggv_lambda0_endpoint_strata_c8q1_r3_20260828T135000Z_r6b
c8p          i-040b7a1c2ed72d4cc r6i.4xlarge ggv_lambda0_endpoint_strata_c8p_r3_20260828T135000Z_r6c
q1p_triple   i-07eeaf8ba6f0bc419 r6i.8xlarge ggv_lambda0_endpoint_strata_q1p_triple_r3_20260828T135000Z_r6d
```

Retain r2's Amazon EC2/DMI/idle/Singular checks, one pinned core, 96-GiB
address-space cap, 32-GiB file cap, zero total swap, 7,200-second master cap,
continuous PID/PGID/SID/starttime custody, and no-orphan final census.

Stop on any source, counted-transform, generated-hash, mutation-control,
factorization, chart, quotient, kernel, endpoint-census, resource, swap,
guard, or orphan disagreement.  No canonical edit, HENS mutation,
sample extrapolation, scheme claim, broad Gröbner search, or `jc2-lean`
access is authorized.
