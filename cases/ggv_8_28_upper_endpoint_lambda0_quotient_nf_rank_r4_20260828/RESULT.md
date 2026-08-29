# Result

Strict verdict: **ADAPTER_FAILURE / NO_VERDICT**.

The `Q1P03` pilot ran on EC2 instance `i-0c73ac7019fe3eef2`
(`r6i.4xlarge`) in namespace
`/home/ubuntu/jobs/ggv_lambda0_quotient_nf_q1p03_r4_20260828T155000Z_r6g`.
The fail-closed preflight passed Linux, Amazon EC2 DMI, instance, type, host,
16-vCPU, source, preregistration, exact Singular, idle, memory, disk, tag, and
zero-total-swap checks.

The stdlib source selfcheck passed.  The backend fixture then revealed that
Singular reserves the exact identifier `NF`: `matrix NF[2][2]` produced
`wrong type declaration` parse errors.  The required terminal marker was
absent and the worker emitted `NO_VERDICT_BACKEND_SELFCHECK_MARKER`.

This happened before `BUILD_REDUCE`; the compiled and run directories are
empty.  Therefore there is zero matrix, rank, minor, factor, stratum, or
endpoint inference.  The backend fixture used 10,964 KiB maximum RSS, zero
swap, and effectively zero wall time.  Registered PGID/SID 5306 was fully
contained; worker and monitor returned zero and the final process census had
no members.

The immutable successor may change only the fixture identifier `NF` to
`REDUCED`; its mathematical compiler and payload remain unchanged.  It must
pass the literal q2 normal-form negative control and a known-nonzero mutation
before the full `Q1P03` pilot.  Fanout remains blocked until that pilot also
produces both an exact nonzero-normal-form rank witness and the complete
higher-minor structural certificate.

