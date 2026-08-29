# Result: exact generic cofactor certificate and rank-drop set

## Verdict

`PASS` for the exact generic left-kernel/cofactor theorem and the
set-theoretic rank-drop decomposition below.  The endpoint equation on the
rank-drop components remains `NO_VERDICT`: this packet does not yet pull the
quadratic endpoint form back to their right kernels.

## Exact theorem certified

Let `M` be the frozen 106-by-105 matrix over
`Q[q0,q1,q2,c4,c6,c8]`.  Over its fraction field, `M` has rank 105 and a
one-dimensional left kernel.  The calibrated signed-maximal-minor vector has
all 106 literal slots preserved and has nonzero support exactly

```text
{81, 93}.
```

No numerator extraction, primitive normalization, content cancellation, or
cross-minor gcd cancellation was applied.  The field relation and its mapping
back to the polynomial ring both replay exactly:

```text
ell^T M = 0,
ell_93 = Delta,
u14^T M = Delta*e14^T,
u1^T M = Delta*e1^T.
```

Consequently the generic endpoint certificate is

```text
Delta*(x14*x72 + x1*x97)
  = x72*(u14^T Mx) + x97*(u1^T Mx).
```

The raw rank-drop ideal is exactly

```text
I_raw = (M81, M93).
```

Writing `g=gcd(M81,M93)` without replacing either raw generator, the exact
quotients are rational scalar multiples of

```text
R93 = c6 - 5*q0^2/6144,
R81 = c8 + 3*q0*c6/64 - 5*q0^3/131072.
```

Thus `R93=0` reduces `R81` exactly to `c8`, so
`V(R81,R93)` lies inside `V(c8)`.  Exact factorization of `g` has distinct
set-theoretic factors `c8`, `q1`, and the explicit polynomial `P` frozen in
the archive.  Therefore

```text
V(I_raw) = V(g) = V(c8*q1*P)
```

set-theoretically.

This is not a claim that `I_raw=(g)`, nor a claim of scheme equality.  The raw
ideal, multiplicities, residual quotients, and content polynomial remain
frozen verbatim for denominator/Fitting and intersection recursion.

## Endpoint scope

The endpoint is the homogeneous quadratic
`E=x14*x72+x1*x97`, not a linear functional.  On each rank-drop component the
next exact step must compute a right-kernel matrix `N` and test the complete
pulled-back quadratic `E(Nt)`, including every cross term on higher-nullity
intersections.  Nonzero pullback over `C` supplies an `E=1` point by scaling;
identically zero pullback makes only that stratum endpoint-dead.

## Custody and resources

- AWS instance: `i-07eeaf8ba6f0bc419`, `r6i.8xlarge`, 32 vCPU / 256 GiB.
- Namespace: `/home/ubuntu/jobs/ggv_lambda0_left_kernel_cofactor_r4_20260828T125900Z_r6d`.
- Registered PID/PGID/SID: `3505/3505/3505`.
- Exact left stage: 1.76 s, 21,676 KiB max RSS.
- Content stage: 0.02 s, 13,784 KiB max RSS.
- One pinned core; 192-GiB address-space cap; zero swap throughout.
- Worker rc 0, monitor rc 0, final census empty, terminal
  `LEFT_KERNEL_JOB_COMPLETE`.
- Source manifest SHA-256:
  `858ed2954b9cf7c8809af298b49bfb7171f88acd54f3bfae8dcf5e3d21b749e4`.
- Full archive SHA-256:
  `359102f984b80a0bee6f362b2e266566508c30e1b272f06de956a96b39f48f98`.
- Remote evidence-manifest SHA-256:
  `f8805b7f97afe76e2d8b7dfbf4949605b8350325298e1eb7cb7802326be8aff7`.

Key exact artifact hashes:

```text
a6ec975c07bfc27fd7e383bb3afbdee2cc87d009a1361499e94542e42416391d  LEFT_KERNEL_RAW.sing
f88aa7e49f76111f11c66ae7e3239845095decd4c354e47bc0f5e9413a6be0b7  LEFT_KERNEL_RAW.tsv
3d9881b9563672c02d1f89c79c34e676cbefb983d9bfe68b0454033f3e638d17  ENDPOINT_DUALS_RAW.tsv
82bf8844f3fc685b23002dd96892433443b5e367260ab454bfc15b347ed3ba1d  LEFT_KERNEL_ZERO_PATTERN.txt
8359a8d4875e764ea67855dd34614c95d52e5f91f2506f159de0adf22369aa4e  COFACTOR_CONTENT.txt
d9df4dd576ad4219ac24f52196945760a52989b86a888d31e6e09a8adc2a31ec  FITTING_STRATA_RAW.sing
```

