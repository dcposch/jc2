# Lambda-zero exact left-kernel/cofactor rank stratification r1

Date: 2026-08-28

## Authorized question

For the frozen 106-by-105 homogeneous odd receiver matrix
`M(q0,q1,q2,c4,c6,c8)`, extract one exactly calibrated left cofactor vector
whose 106 entries are the raw signed 105-by-105 maximal minors.  Use it to
freeze the exact rank-drop/Fitting ideal and an exact generic endpoint
row-dual certificate.  Do not compute a full Groebner basis.

The endpoint is the homogeneous quadratic form

```text
E = x14*x72 + x1*x97
  = f11_1*g11_0 + f_0*g15_1.
```

It is not a linear row functional.  Generic certificates may express
`Delta*E` using degree-one-in-`x` multipliers of `Mx`; residual strata must
eventually be classified by pulling this full quadratic form back to the
right kernel of `M`.

## Frozen input and provenance

```text
56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c  input/symbolic_quadratic_q_rankdrop.sing
8d476d225af6c9c35f737d858dfc613913c727fc71ddb9e275d9509cfde86dd5  input/equation_names.txt
58a26a4bf2c2045b96ea8c91de92648d21bda2712840e74b1ea0f09b872ccfa7  provenance/compile_symbolic_quadratic_q.py
7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1  provenance/compile_endpoint.py
6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a  provenance/verify_lambda0_q15.py
```

The compiler adapter must find exactly 11,130 matrix entries and independently
parse all 106 rows and 105 columns before elimination.

## Exact construction

Work over `Q(q0,q1,q2,c4,c6,c8)`.  Compute the one-dimensional left kernel of
`M`.  Select a nonzero component `o`, form the 105-row matrix `B` obtained by
omitting row `o`, and compute the raw determinant `Delta=det(B)` by sparse
Bareiss elimination.  Scale the left relation so that `ell_o=Delta`:

```text
ell^T M = 0,       ell_o = Delta.
```

The emitted entries of `ell` are then the 106 signed maximal minors.  They
must be written before any content analysis.  Primitive or common-factor
cancellation of this raw vector is forbidden because it can delete a genuine
rank-drop component.

Using the same `B`, solve exactly for polynomial row duals `u14,u1`:

```text
u14^T M = Delta*e14^T,
u1^T  M = Delta*e1^T.
```

The directly replayable generic quadratic certificate is

```text
Delta*E = x72*(u14^T Mx) + x97*(u1^T Mx).
```

After the raw certificate passes, compute only the gcd/content and exact
factor data of the 106-minor Fitting ideal.  Freeze the complete residual
ideal and a component queue.  No component is endpoint-dead or surviving
until a later exact chart supplies a right-kernel matrix `N` and verifies the
full pulled-back quadratic `E(Nt)`.  At rank 104 this is `E(v)` for one kernel
generator; at higher nullity every diagonal and cross coefficient is required.

## AWS registration and resources

The only authorized host is AWS r6d, instance `i-07eeaf8ba6f0bc419`, resized
while stopped to `r6i.8xlarge` (32 vCPU, 256 GiB).  The exact job tag is

```text
ggv_lambda0_left_kernel_cofactor_r1_20260828T122800Z_r6d
```

Preflight requires Amazon EC2 Linux/DMI identity, the pinned hostname and
instance ID, at least 225 GiB available RAM, at least 50 GiB disk, zero total
swap, no conflicting user job, and Singular executable SHA-256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.

Execution uses one pinned core, a 192-GiB address-space ceiling, 32-GiB file
ceiling, a 7200-second master timeout, registered PID/PGID/SID/starttime,
continuous process-group monitoring, and final no-orphan census.  Inner caps
are 60 seconds each for adapter self-check, build, and full-matrix parse;
5400 seconds for the exact left cofactor and endpoint duals; and 1200 seconds
for exact content/factor stratification.

## Required markers and stop gate

An exact intermediate certificate requires all of:

```text
LEFT_KERNEL_REPLAY_ZERO=1
RAW_DENOMINATORS_ONE=1
OMITTED_CALIBRATION=1
ENDPOINT_DUAL_REPLAY_ZERO=1
LEFT_KERNEL_CERTIFICATE_PASS=1
STRATA_GCD_PASS=1
```

Stop with `NO_VERDICT` on any source/preregistration or matrix-entry drift,
adapter/parser failure, modular-versus-exact pivot disagreement, zero selected
minor, nonpolynomial scaled cofactor, `ell^T M != 0`, failure of
`ell_o=Delta`, any cancellation of the raw minors, endpoint-dual replay
failure, reducer/factor disagreement, swap drift, resource cap, guard failure,
or orphan.  A timeout, content factor, rank number, modular value, or frozen
residual ideal is not an endpoint verdict.

The job may report `EXACT_LEFT_KERNEL_CERTIFICATE_PASS_RESIDUAL_STRATA_PENDING`
only after every exact replay above passes.  That marker certifies the raw
cofactor/Fitting data and generic `Delta != 0` endpoint chart; it does not
classify the residual rank-drop locus.  No nearby-order, K00, HENS, canonical
ledger, or `jc2-lean` file or process is in scope.

