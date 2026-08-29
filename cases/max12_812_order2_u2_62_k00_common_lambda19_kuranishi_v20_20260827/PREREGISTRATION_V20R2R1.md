# V20R2R1 runner-only fresh-output repair

Date: 2026-08-27

Status: **FROZEN AFTER R0 FAILURE AND BEFORE R1 EXECUTION.**

R0 failed before algebra solely because its wrapper pre-created the exact
output directory which the frozen compiler requires to be fresh.  R1 may
remove only `"$aws_job/output"` from the wrapper's initial `mkdir -p` list.

The mathematical compiler remains byte-identical at SHA-256
`13342b16367b347680d6cbb4fb726798b7c1904422b10a661f31f5b7b59974b0`.
All source hashes, the five boundary restrictions, exact residual,
66/87-module controls, and the target-sign, load-weight,
restriction-before-saturation, and contraction-order mutation gates remain
unchanged.  Any further error fails closed and requires a new frozen repair.

R0 evidence and chronology remain immutable and nonpromotable.
