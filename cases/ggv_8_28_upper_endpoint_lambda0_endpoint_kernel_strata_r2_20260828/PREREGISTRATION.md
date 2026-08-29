# Preregistration: exact P chart and intersection rank strata r2

Date: 2026-08-28

## Frozen algebraic input

The exact r4 cofactor packet established, set-theoretically and without
replacing the raw Fitting ideal, that the rank-drop set of the frozen
106-by-105 receiver matrix is

```text
V(M81,M93) = V(c8*q1*P).
```

The raw ideal `(M81,M93)`, the literal signed cofactors, their multiplicities,
and all scheme data remain authoritative.  This successor neither cancels the
content nor asserts scheme equality.  Its frozen inputs are:

```text
56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c  symbolic_quadratic_q_rankdrop.sing
d9df4dd576ad4219ac24f52196945760a52989b86a888d31e6e09a8adc2a31ec  FITTING_STRATA_RAW.sing
8359a8d4875e764ea67855dd34614c95d52e5f91f2506f159de0adf22369aa4e  COFACTOR_CONTENT.txt
08da7c8e25e7fa684f6a120b61327b247d1cac669f559d806216c869c0da5cbf  process_group_guard.py
```

The exact third factor is selected only from the pinned literal
`CONTENT_FACTOR_DATA=c8,P,q1`; its textual SHA-256 is
`e986e0488d9ccc46529dd4952bb5504198151488babfe5bd03815ad9a9184f44`.
The desk compiler independently splits the polynomial as
`P=P0+c8*P1`, with exact textual hashes

```text
P0  8c487c77de9d2ad3856d93adeb7781b216388bdbf41e31d1105b80dd41b87c26
P1  3d64defb5847f38a8f9d3bc11c9a33578910856c36177788437e206bb407a5ee
```

before any CAS execution.  The frozen compiler counted 11,130 matrix entries.

## Exact questions and branch construction

The endpoint is the homogeneous quadratic

```text
E = x14*x72 + x1*x97.
```

The `P` lane must first factor `P` over `Q` and record exactly one distinct
factor, prove that `P` divides the raw content together with `c8` and `q1`,
and replay `P=P0+c8*P1` with `P1!=0`.  Only then may it use the dense exact
function-field chart

```text
c8 = -P0/P1
```

over `Q(q0,q1,q2,c4,c6)`.  The denominator is frozen verbatim; its vanishing
complement is not silently discarded or classified.  No fixed sample may be
extrapolated to the generic `P` component.

The intersection lanes specialize the exact `P` first and then factor over
`Q`, preserving the raw specialized polynomial and every factor
multiplicity:

```text
c8=q1=0,
c8=0 and P=0,
q1=0 and P=0,
c8=q1=0 and P=0.
```

Every distinct factor is an independent set-theoretic branch.  If the factor
is linear in an available parameter, the compiler uses the exact dense
function-field chart obtained by solving for that parameter and records the
literal denominator.  Otherwise it uses the exact irreducible quotient
coordinate ring.  A quotient-ring syzygy module is tested only generically:
after localization it spans the function-field kernel, but special fibers and
rank jumps remain separate strata.

For every chart or irreducible quotient branch, compute an exact right-kernel
generator matrix `N`, replay `M*N=0`, and write the complete pullback of
`E(Nt)`.  The coefficient census contains every diagonal coefficient and
every cross coefficient

```text
N14_i*N72_j + N14_j*N72_i + N1_i*N97_j + N1_j*N97_i.
```

A nonzero coefficient is an exact generic survivor: over `C`, scaling then
supplies `E=1`.  If every coefficient is zero, the strict result is only
`GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING`.  It is never a declaration that
the full component or intersection is endpoint-dead.  Every kernel basis
denominator and every quotient branch is preserved for subsequent
denominator/Fitting recursion.

## Frozen adapter hashes

```text
1d02dc3692e77bf0ea030bdd5cff8f588bad3643cd6b80069f265f7f422cd366  PLAN.json
a6cc2720e12b423cb70b5bed098bb0a8ded2bf4f58967ebddadf7a06cc4a8105  aws_preflight.py
9da22146b7a16c25b8a35bb835bdb4215d57a21dcad001a99eb577f72ea811cf  aws_run_remote.sh
8417b551c251262618fe388b8d92819d5fbb56e548287aee026104564255e718  aws_worker.sh
53ad2aa298b499d83c593171fb3da9c1dce39bfe7f924bf461db4887a8a6f578  build_strata_scripts.py
4582e1784e3acc69878fdd3649d18f8ec7d64804b4968536ff7e2aedf19c1888  selfcheck_strata.py
```

## AWS lanes and custody

Four isolated namespaces run concurrently, each on one pinned core and with
zero total swap:

```text
p            r6a i-02cb2b4a379ffcc64 r6i.4xlarge ggv_lambda0_endpoint_strata_p_r2_20260828T133400Z_r6a
c8q1         r6b i-0f089e64c378f5da3 r6i.4xlarge ggv_lambda0_endpoint_strata_c8q1_r2_20260828T133400Z_r6b
c8p          r6c i-040b7a1c2ed72d4cc r6i.4xlarge ggv_lambda0_endpoint_strata_c8p_r2_20260828T133400Z_r6c
q1p_triple   r6d i-07eeaf8ba6f0bc419 r6i.8xlarge ggv_lambda0_endpoint_strata_q1p_triple_r2_20260828T133400Z_r6d
```

Each preflight pins Amazon EC2 vendor, DMI instance, private hostname,
instance type, vCPU count, at least 110 GiB available RAM on r6a--r6c or
220 GiB on r6d, 50 GiB disk, no conflicting user computation, zero swap, and
Singular SHA-256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.
Each namespace has a 7,200-second master process-group cap, CPU 1 only, a
96-GiB address-space cap, a 32-GiB file cap, registration before work,
continuous PID/PGID/SID/starttime monitoring, final no-orphan census, and
immutable source/output custody.

## Strict stop and verdict gates

Stop with `NO_VERDICT` on source or preregistration drift, factorization or
irreducibility disagreement, P-chart identity/denominator failure,
specialization-factor census failure, matrix parse failure, quotient relation
failure, `M*N` replay failure, missing diagonal/cross terms, timeout/resource
cap, swap drift, guard failure, or orphan.  These are adapter or bounded-run
outcomes, never mathematical emptiness.

Report every branch separately.  A `PASS` requires an exact nonzero pulled-back
quadratic coefficient.  Generic zero leaves denominator and rank-jump strata
open.  No full Gröbner-basis search, nearby term-order search, K00 computation,
sample extrapolation, scheme-equality inference, canonical-ledger edit,
HENS-process mutation, or `jc2-lean` access is authorized.
