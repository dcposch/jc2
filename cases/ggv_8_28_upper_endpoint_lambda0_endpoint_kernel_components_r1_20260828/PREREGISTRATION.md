# Lambda-zero endpoint-on-kernel component successor r1

Date: 2026-08-28

## Frozen theorem input

The exact r4 cofactor packet proves that the frozen 106-by-105 receiver matrix
`M` has generic rank 105, that its 106 raw signed maximal minors are nonzero
only in literal slots 81 and 93, and that

```text
V(M81,M93) = V(c8*q1*P)
```

set-theoretically.  The factor `P` is the explicit third irreducible factor of
the exact content polynomial.  This statement does not replace the raw ideal
`(M81,M93)`, cancel its content, or assert scheme equality.  The complete raw
Fitting/content files are pinned as inputs to this successor.

```text
56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c  input/symbolic_quadratic_q_rankdrop.sing
d9df4dd576ad4219ac24f52196945760a52989b86a888d31e6e09a8adc2a31ec  input/FITTING_STRATA_RAW.sing
a6ec975c07bfc27fd7e383bb3afbdee2cc87d009a1361499e94542e42416391d  input/LEFT_KERNEL_RAW.sing
8359a8d4875e764ea67855dd34614c95d52e5f91f2506f159de0adf22369aa4e  input/COFACTOR_CONTENT.txt
```

## Authorized exact question

For each set-theoretic component, compute a right-kernel matrix `N` for `M`
and the complete pullback of the homogeneous quadratic

```text
E = x14*x72 + x1*x97.
```

For kernel coordinates `t`, every diagonal and cross coefficient of `E(Nt)`
must be tested.  A nonzero coefficient over the component function field, or
at an exact point of the component, is a component `PASS`: over `C` a scalar
extension then supplies `E=1`.  An identically zero generic pullback makes
only the generic rank-104 chart endpoint-dead; rank-jump intersections remain
pending.  A timeout, sampled zero, parse failure, or adapter failure is
`NO_VERDICT`.

## Component methods

The `c8=0` and `q1=0` components are computed symbolically over the exact
function fields of their remaining independent parameters.  The complete
right-kernel and quadratic coefficient tables are frozen and `M*N=0` must
replay exactly.

The third factor `P` is verified independently from the frozen content.  It is
linear in `c8` on a dense chart.  Six exact rational samples are preregistered
for the first bounded screen, with `(q0,q1,q2,c4,c6)` equal to

```text
(1,1,0,1,1)
(1,1,1,1,1)
(1,2,1,1,1)
(2,1,1,1,1)
(1,1,2,2,1)
(2,3,1,1,2).
```

At each sample, `c8=-P(c8=0)/(P(c8=1)-P(c8=0))` is computed exactly.  The
script verifies `P=M81=M93=0` and `c8*q1!=0` before computing the right kernel
and full quadratic pullback.  One nonzero pullback is an exact existence
certificate on `P`; absence of a survivor across all six samples remains
`NO_VERDICT`, not generic endpoint-death.

Pairwise/triple intersections are a registered successor trigger only where
a generic component is endpoint-dead or rank jumps.  This first job does not
infer intersection behavior from a generic chart.

## AWS custody and resources

The three lanes run concurrently in separate immutable namespaces on three
audited `r6i.4xlarge` AWS hosts (16 vCPU / 128 GiB each):

```text
c8  r6a  i-02cb2b4a379ffcc64  ip-172-30-0-34   ggv_lambda0_endpoint_kernel_c8_r1_20260828T132000Z_r6a
q1  r6b  i-0f089e64c378f5da3  ip-172-30-0-106  ggv_lambda0_endpoint_kernel_q1_r1_20260828T132000Z_r6b
P   r6c  i-040b7a1c2ed72d4cc  ip-172-30-0-150  ggv_lambda0_endpoint_kernel_p_r1_20260828T132000Z_r6c
```

Preflight requires Amazon EC2 identity, the pinned host/instance/product,
zero total swap, at least 110 GiB available RAM, at least 50 GiB disk, no
conflicting user job, and pinned Singular SHA-256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.
Each lane uses CPU 1 only, a 96-GiB address-space ceiling, 32-GiB file ceiling,
3600-second master cap, process-group/session/starttime custody, continuous
telemetry, and a final no-orphan census.  No namespace or worker is shared.

Inner caps are 60 seconds for selfcheck/build/each parser, 1800 seconds for
each symbolic linear component, and 300 seconds per exact `P` sample.

## Stop and classification gates

Stop without a mathematical verdict on any source/preregistration drift,
matrix-entry count drift, specialization token drift, raw-Fitting hash drift,
failure of `M*N=0`, incomplete quadratic cross-term census, factor-selection
or linear-chart disagreement, sample off the raw rank-drop ideal, swap drift,
resource cap, guard failure, or orphan.

Report `C8`, `Q1`, and `P` separately.  No scheme equality, intersection
classification, nearby-order computation, K00 computation, full Groebner
basis, canonical-ledger mutation, HENS-process mutation, or `jc2-lean` access
is authorized.
