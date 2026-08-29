# Preregistration: exact replay parser fix r4

Date: 2026-08-28

R3 produced clean exact mathematical stdout for both previously failed
quotient branches, but its verdict parser applied regular-expression matching
to the literal endpoint marker `x14*x72+x1*x97`; the asterisks therefore made
the parser falsely reject both branches. R3 remains pure adapter
`NO_VERDICT`; its stdout is not promoted.

R4 changes exactly one verdict-parser call from regex matching to fixed-string
whole-line matching and changes the source case path from r3 to r4. The
counted transformation of frozen r3 worker
`20e03925d105bba482901643d609a13c6cf4cb74ff450783237e25fda0d859c1`
must yield
`2e5f9c116ec77f298224273f95ca73e6623980d07563ea837461a2cfe64afa36`.
No ring, quotient factor, receiver entry, kernel operation, reducer, endpoint
coefficient, mathematical marker, cap, or verdict rule changes.

The mathematical payload manifest remains
`ecd5dba798ab3157f4bf362361b630744fbadfbfe582dbc0d85523f6183f33c6`.
Run both exact branches in one fresh pinned-r6a namespace under
`ggv_lambda0_endpoint_strata_replay_fix_r4_20260828T145500Z_r6a`. Require the
full source/runtime hash replay, exact quotient reducer and forced-mutation
selfchecks, 45/78 complete endpoint coefficients, zero swap, and clean final
no-orphan census. Any disagreement remains strict `NO_VERDICT`.
