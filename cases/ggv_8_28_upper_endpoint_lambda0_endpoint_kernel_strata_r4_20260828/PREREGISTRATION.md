# Preregistration: r4 negative-control polarity repair

Date: 2026-08-28

R2 and r3 remain `ADAPTER_FAILURE / NO_VERDICT`; neither reached a full
matrix kernel.  The frozen r3 negative control correctly saw Singular's
reserved-identifier error, but incorrectly required the interpreter not to
continue to a later independent print.  The exact r4 mutation reverses only
that continuation assertion: both the reserved-`NF` diagnostic and the later
continuation marker must occur.  It then executes the already frozen positive
`NF -> NFIELD` selfcheck materialization.

Required materialized hashes are:

```text
selfcheck  6ab9dc1a11ed4cb866379ddf4131bff7faed66fcb7dc170ae081631b5eb1359d
worker     4f5439503440bcf69ab00c22d3a75487f0999a4f3b7cb0e2b59e898971307473
runner     93321dab1959045590ac3a20b1f11fde429b10f99230931e42f80109b2d7b9b1
```

The mathematical payload remains exactly r2 compiler
`53ad2aa298b499d83c593171fb3da9c1dce39bfe7f924bf461db4887a8a6f578`
with matrix `56f09440...`, Fitting data `d9df4dd5...`, and content data
`8359a8d4...`.  All r2 exact P-chart, specialization-factor,
right-kernel, full diagonal/cross-term endpoint, rank-jump-pending, stop,
resource, zero-swap, and custody rules remain unchanged.

First launch only the `p` lane on r6a in
`ggv_lambda0_endpoint_strata_p_r4_20260828T135500Z_r6a`.  It must pass the
complete selfcheck, base build, exact factor/irreducibility census, and full
matrix parse before the `c8q1`, `c8p`, and `q1p_triple` lanes are released.
The pilot may continue into its exact generic P kernel after the gate.

All lanes retain the same instance identities, one core, 96-GiB address-space
cap, 7,200-second master cap, zero total swap, process-group/starttime guard,
and final no-orphan census.  Stop on any hash, counted mutation, parser,
factorization, reducer, replay, resource, swap, or guard disagreement.  No
mathematical inference from adapter failure, no canonical edit, no HENS
mutation, and no `jc2-lean` access.
