# V22 R0 pre-algebra failure

Date: 2026-08-27

R0 failed closed before invoking Singular.  The compiler required every one
of the six unloaded rows to have a nonzero quadratic initial.  That
precondition is ill-typed for the frozen K00 source: `Q1,...,Q5` are nonzero,
whereas the reviewed exact source has `Q6=0` (row six starts in transverse
normal degree three).

The registered AWS run
`max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827T125930Z_r6b`
exited 1 after 1.49 seconds with maximum RSS 41,728 KiB and zero swap.  It
created no output directory and made no algebraic, stratum, jet, arc, or
closure decision.  Its compiler stderr is frozen at SHA-256
`4e96a9f0919b0fd9b92c54305a6983f9e8ef9ce5659118ea92b887dde026343f`;
the shipped R0 compiler is frozen under `aws_r6b_r0_failed/source/` at
SHA-256 `9515d3a95eec7fe28d00149d3567a6029725256674a8df050b1b9ddbbdc61cf4`.

R1 may change only this source-profile predicate, add mutations for a
nonzero `Q6` and a zero `Q_i` for one `i<=5`, and add the R1 preregistration
hash gate.  The extraction, D3-lift replay, D4-dual pairing, exact Singular
question, scope, and resource caps remain unchanged.
