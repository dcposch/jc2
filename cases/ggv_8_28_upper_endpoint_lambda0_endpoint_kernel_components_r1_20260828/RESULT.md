# Result: first endpoint component portfolio

## Strict verdict

The combined verdict is

```text
NO_VERDICT_COMPONENT_INTERSECTIONS_PENDING
```

The component classifications must remain separate:

- `c8=0`: `GENERIC_ENDPOINT_DEAD_INTERSECTIONS_PENDING`.
- `q1=0`: `GENERIC_ENDPOINT_DEAD_INTERSECTIONS_PENDING`.
- `P=0`: `NO_VERDICT_FIXED_SAMPLE_SCREEN`.

Thus no whole component, pairwise/triple intersection, or rank-jump stratum
is declared endpoint-dead by this packet.

## Symbolic generic component charts

On `c8=0`, exact computation over the function field of the remaining
parameters gives right-kernel dimension 1 (generic matrix rank 104).
`M*N=0` replays exactly.  The complete pullback of
`E=x14*x72+x1*x97` has one coefficient, and that coefficient is exactly zero.

On `q1=0`, exact computation over the function field of the remaining
parameters gives right-kernel dimension 4 (generic matrix rank 101).
`M*N=0` replays exactly.  The complete quadratic pullback has all ten
diagonal/cross coefficients present, and all ten are exactly zero.

These are generic-chart statements only.  Their pairwise/triple
intersections and any further rank jumps can have larger kernels and require
new complete quadratic pullbacks.

## Exact fixed-sample screen on `P`

The lane independently selected the unique high-degree factor `P` among the
three distinct frozen content factors.  At each preregistered point it solved
the chart linear in `c8`, verified exactly that `P=M81=M93=0` and
`c8*q1!=0`, obtained a one-dimensional right kernel, replayed `M*N=0`, and
found the sole pullback coefficient to be exactly zero:

```text
id  (q0,q1,q2,c4,c6)  c8
01  (1,1,0,1,1)       -27633/128
02  (1,1,1,1,1)       -1468394349/14680064
03  (1,2,1,1,1)       -6897/64
04  (2,1,1,1,1)       -1010612528455/19947552768
05  (1,1,2,2,1)       -42691354465/510806016
06  (2,3,1,1,2)       -2525795221/11818816
```

Six sampled zeros do not prove that the pullback vanishes over the function
field of `P`; accordingly the strict `P` verdict is
`NO_VERDICT_FIXED_SAMPLE_SCREEN`, not generic endpoint-death.

## Scope and next exact step

The inherited decomposition

```text
V(M81,M93) = V(c8*q1*P)
```

is used only set-theoretically.  This packet neither cancels the raw ideal
`(M81,M93)` nor asserts ideal or scheme equality.  The registered successor
must compute a symbolic exact function-field chart for `P`, then compute
complete quadratic pullbacks on all pairwise/triple intersections and
stratify further wherever the matrix rank drops.

## Custody and exact artifacts

All lanes passed frozen-source/preregistration checks, audited AWS preflight,
zero-total-swap checks, worker/monitor exit-code checks, and final no-orphan
census.  Each lane used one pinned core under the registered resource caps.

```text
lane  instance               namespace suffix                                                   PID
c8    i-02cb2b4a379ffcc64    ggv_lambda0_endpoint_kernel_c8_r1_20260828T132000Z_r6a             1436
q1    i-0f089e64c378f5da3    ggv_lambda0_endpoint_kernel_q1_r1_20260828T132000Z_r6b             1450
P     i-040b7a1c2ed72d4cc    ggv_lambda0_endpoint_kernel_p_r1_20260828T132000Z_r6c              1487
```

The `c8` symbolic stage took 4.49 s and 35,440 KiB max RSS; the `q1` stage
took 0.28 s and 16,432 KiB max RSS.  Every lane ended with
`ENDPOINT_COMPONENT_JOB_COMPLETE`.

Frozen packet hashes:

```text
9acd614a153f5263548ac36ad98632cabbb127083f682359de4f40c2b9a51f05  SOURCE.sha256
42c2cc562c3801e73955829cd449fe74b67b27ce6042d97e8c9d2f52bb112292  PREREGISTRATION.sha256
3f5fc38b4ab3ff6083add2aa129c081d2d5b53888f0face4c47071489201a7b5  SOURCE.tar.gz (each lane)
```

Remote evidence-manifest hashes:

```text
4082ccb5d48a86c54ed5c0b18f348f39900776bdc6b35414f00d353d53299f46  c8/EVIDENCE.sha256
316db45fb35cbfb4dfdebaae25e5fbefaad84fd7e11df454710d7c8f39d1ac94  q1/EVIDENCE.sha256
4d087ef5166afcd0f4a466987e2235df13a5f311daa542e589406cc33c696faa  P/EVIDENCE.sha256
```

Key exact output hashes:

```text
fd3faba8bbe629654dd290aac4aea26a015a72ca6749ce5fe79c93012e9419f8  C8_ENDPOINT_PULLBACK_FIELD.tsv
54cffd1e4430e516f1558ec7817e8eb1aa3b4da61708bec5b2c823ea359ece19  C8_RIGHT_KERNEL_FIELD.tsv
4b8c0a00cd3cc55b660999114f762c25417a0de9b66f551ae6fb25a37988a754  Q1_ENDPOINT_PULLBACK_FIELD.tsv
f1b855a7d14a1cc2f9c997f6e5191d9fcbf97d5fe5bb6b38d395d8f8411dd52b  Q1_RIGHT_KERNEL_FIELD.tsv
fd3faba8bbe629654dd290aac4aea26a015a72ca6749ce5fe79c93012e9419f8  each P_SAMPLE_*_ENDPOINT_PULLBACK.tsv
```
