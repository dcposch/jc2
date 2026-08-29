# Preregistration: quotient-ideal replay reducer diagnostic r2

Date: 2026-08-28

R1 showed that raw polynomial representatives of `M*N` are nonzero on C8P
branch 02; its first representatives visibly share the frozen quotient
factor. R1 remains strict diagnostic `NO_VERDICT` and does not license a
mathematical claim.

R2 reruns both frozen failed scripts, byte-identical through the quotient
kernel computation. It records raw replay entries and also reduces every
entry by the exact standard basis of `ideal(basering)`. It performs the same
operation on a forced non-kernel mutation obtained by adding the first basis
coordinate to the first generator. The receiver matrix has exact first entry
`1/4`, so the reduced mutation must remain nonzero.

Pass is componentwise and requires raw replay nonzero, quotient-ideal reduced
replay identically zero, reduced mutated pivot and replay nonzero, the exact
quotient/reducer guards, and the downstream full endpoint calculation using
the reduced replay predicate. Both C8P branch 02 and triple branch 02 must
pass before any adapter change is licensed. Any Singular error or normal-form
disagreement remains diagnostic `NO_VERDICT`.

Frozen r6 result archive:
`cfd2c020b204beecaca5b60ee062aed8a1fe274a399c2ebda93d0d300a00c0f4`.
Unchanged mathematical payload manifest:
`ecd5dba798ab3157f4bf362361b630744fbadfbfe582dbc0d85523f6183f33c6`.
Generated exact diagnostic scripts must be
`08bdc93c56b6e7ed8ab313413e9fd22af2eda098ef14814a9f6d68bbc8a46cf6`
and
`1feba464ee914d93935d4ef4165be7d260044940c6c28cb632f662b8cf7066ea`.

Run on pinned r6a under
`ggv_lambda0_endpoint_strata_replay_diag_r2_20260828T144500Z_r6a`, one core,
16-GiB address cap, 900-second master cap, zero swap, immutable source,
continuous PGID/starttime custody, and final no-orphan census.
