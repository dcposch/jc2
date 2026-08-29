# Preregistration: exact qring-symbol repair and pilot r5

Date: 2026-08-28

R2, r3, and r4 remain adapter `NO_VERDICT`; none reached a full receiver
kernel.  The r4 pilot proved both prior selfcheck mutations, then exposed that
an ambient polynomial identifier is not defined after Singular changes to a
`qring`.  The same pattern occurred in the real irreducible-branch compiler.

R5 makes exactly two semantically identical corrections:

1. The tiny quotient control tests `u==0` after quotienting by `(u)`, rather
   than referring to the vanished ambient identifier `F`.
2. A real quotient branch redeclares the exact factor expression as
   `BRANCH_FACTOR_Q` inside the qring, then requires
   `BRANCH_FACTOR_Q==0` before any kernel calculation.

The counted transform of frozen r2 compiler
`53ad2aa298b499d83c593171fb3da9c1dce39bfe7f924bf461db4887a8a6f578`
must be
`575f0f34065bf06b76311a51fa71622d42d2e9a75fbb85979f79d9da97f3c06e`.
The complete patched r2 selfcheck, including `NF -> NFIELD` and
`F==0 -> u==0`, must be
`10da4b9658d40a25679386f6600f9d113f417f38b6cf85ffa78cffd97a5b60b4`.
The runtime worker must be
`8acf14af1b27476ff8a9134f9ad9e40d3a1a260963cae24835fe33632ac35256`.

No equation, factorization target, chart, matrix entry, endpoint coefficient,
branch ordering, verdict rule, or cap changes.  The exact endpoint remains
`E=x14*x72+x1*x97`; every diagonal and cross term is required.  A nonzero
generic pullback is `PASS`; generic zero remains
`GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING`, never whole-component death.

First launch only the P lane on r6a under
`ggv_lambda0_endpoint_strata_p_r5_20260828T140000Z_r6a`.  It must pass the
full adapter selfcheck, base build, exact P irreducibility/factor census, and
full matrix parse before the other three lanes are released.  The pilot may
continue into its exact P kernel.

Retain the four pinned EC2 identities, one core, 96-GiB address-space cap,
zero swap, 7,200-second process-group cap, exact source/runtime hashes,
continuous starttime custody, and final no-orphan census.  Stop on every hash,
factor, parser, reducer, relation, replay, resource, swap, or guard
disagreement.  No inference from adapter failure, no sample extrapolation,
canonical edit, HENS mutation, or `jc2-lean` access.

Frozen r5 source file hashes:

```text
2320d387396735f99a55e5f9bfc92be7d84c3597ae86e460cb41cce2bf2eff1f  aws_preflight.py
a59841bdd79d2f155ace3f87d9639d7e904cc896a6dfec5ca934dd9ecada2b5f  aws_run_remote.sh
0b6f999fd3e19711e20fb2c2e476db5f250771e2e02165864e5d55ea9553f793  build_compiler_r5.py
f96516301b0aa7eca182e9b0cbfc7ceea2f28161d3de8cc9086f97f57e64944b  build_worker_r5.py
fcb2816b1d1a63fff8e3aece919315d5716450cdd1b49f0ccd6e0c7c3c43210b  selfcheck_strata_r5.py
```
