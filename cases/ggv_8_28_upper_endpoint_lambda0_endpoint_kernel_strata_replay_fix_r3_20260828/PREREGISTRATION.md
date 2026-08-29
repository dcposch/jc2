# Preregistration: exact quotient-replay fix r3

Date: 2026-08-28

Diagnostics r1 and r2 remain diagnostic-only `NO_VERDICT`. R2 showed on both
failed quotient branches that raw polynomial representatives of the exact
syzygy replay are nonzero, their exact normal forms modulo
`std(ideal(basering))` are all zero, and a forced non-kernel mutation retains
many reduced nonzeros and a nonzero pivot.

R3 is a fresh mathematical replay of only the two previously failed strata.
It preserves the exact quotient factor, 106-by-105 receiver matrix, syzygy
kernel, endpoint `E=x14*x72+x1*x97`, all diagonal and cross terms, and strict
rank-jump-pending rule. The adapter change is solely that kernel replay is
certified by exact quotient-ideal normal forms. The forced mutation remains a
mandatory non-vacuity selfcheck but does not change the original kernel.

The unchanged mathematical payload manifest is
`ecd5dba798ab3157f4bf362361b630744fbadfbfe582dbc0d85523f6183f33c6`.
The exact input scripts are `bed61e93582dfef...` and `e1c50b669a90e...`;
the generated fixed scripts must be
`08bdc93c56b6e7ed8ab313413e9fd22af2eda098ef14814a9f6d68bbc8a46cf6`
and
`1feba464ee914d93935d4ef4165be7d260044940c6c28cb632f662b8cf7066ea`.

For C8P02 require 45 full pullback coefficients; for TRIPLE02 require 78.
A nonzero coefficient with exact replay is a survivor. All coefficients zero
with exact replay is only generic endpoint death with rank-jump substrata
pending. Any build, reducer, mutation, replay, endpoint-count, resource, or
custody disagreement is strict `NO_VERDICT`.

Run on pinned r6a under
`ggv_lambda0_endpoint_strata_replay_fix_r3_20260828T145000Z_r6a`, one core,
16-GiB address cap, 900-second master cap, zero swap, immutable source,
continuous PGID/starttime custody, and final no-orphan census.
