# Preregistration: one-stratum-per-host Fitting census r2

Date: 2026-08-28

R1's four remote setup attempts ended before registration, preflight, or any
algebra because the transport extracted `jc2/` directly under the job instead
of under `source/`.  Their immutable setup-failure packets are preserved.
R2 changes only transport and dispatch: the r1 mathematical compiler with
SHA-256 `409d0f586e14750df2792ab9c0027dfc4678f4fe1848eba1087dbefbd5ef9ce9`
is imported byte-for-byte, and each job builds/runs exactly one of its nine
genuine strata.  The r1 exact-unit filtering, quotient properness guards,
rational-unit-pivot algorithm, residual matrix, generic residual rank, scope,
and no-inference verdict are unchanged.

The endpoint is reserved as `E=x14*x72+x1*x97` but is not tested.  A clean
job is strictly `NO_VERDICT_FITTING_CENSUS_ONLY`.  Unit factors C8P01=1,
Q1P01=16, and TRIPLE01=16 remain recorded `EMPTY_UNIT_FACTOR` and never
become quotient rings.  No minor, full Groebner basis, content cancellation,
component death, or endpoint survivor is licensed in this job.

Each exact component has a fresh immutable namespace, one CPU, 96-GiB
address-space cap, 32-GiB file cap, 3,600-second component cap, 7,200-second
process-group cap, zero total swap, exact EC2/DMI/Singular/source/tag checks,
continuous PID/starttime custody, and a no-orphan terminal census:

```text
c8        i-02cb2b4a379ffcc64  ip-172-30-0-34   r6i.4xlarge
  ggv_lambda0_fitting_census_c8_r2_20260828T152000Z_r6a
q1        i-0f089e64c378f5da3  ip-172-30-0-106  r6i.4xlarge
  ggv_lambda0_fitting_census_q1_r2_20260828T152000Z_r6b
p         i-040b7a1c2ed72d4cc  ip-172-30-0-150  r6i.4xlarge
  ggv_lambda0_fitting_census_p_r2_20260828T152000Z_r6c
c8_q1     i-07eeaf8ba6f0bc419  ip-172-30-0-45   r6i.8xlarge
  ggv_lambda0_fitting_census_c8_q1_r2_20260828T152000Z_r6d
c8p02     i-0793fef088620f2c1  ip-172-30-0-131  r6i.4xlarge
  ggv_lambda0_fitting_census_c8p02_r2_20260828T152000Z_r6e
q1p02     i-0fdde459d4ab36b95  ip-172-30-0-79   r6i.4xlarge
  ggv_lambda0_fitting_census_q1p02_r2_20260828T152000Z_r6f
q1p03     i-0c73ac7019fe3eef2  ip-172-30-0-248  r6i.4xlarge
  ggv_lambda0_fitting_census_q1p03_r2_20260828T152000Z_r6g
triple02  i-0d71d73e0fe8a8cae  ip-172-30-0-220  r6i.4xlarge
  ggv_lambda0_fitting_census_triple02_r2_20260828T152000Z_r6h
triple03  i-072ccec67b0933088  ip-172-30-0-128  r6i.4xlarge
  ggv_lambda0_fitting_census_triple03_r2_20260828T152000Z_r6i
```

The five new nodes were launched from Canonical Ubuntu image
`ami-052355af2a014bd2c`, each with a distinct task tag and a 200-GiB gp3 root.
Singular 4.3.2 was installed from the Ubuntu repository and must reproduce
the frozen binary SHA-256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.
They are paid ephemeral workers and must be terminated after terminal archive
harvest.  No HENS process or namespace is touched.

