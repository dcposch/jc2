# AWS verification attempt: fail closed

Tag: `jc2_lean_cube_f0b5823_aws_verify_20260826T023000Z_r6d`

The pinned source/archive hashes and AWS identity passed, and Mathlib's cache
completed.  `lake build` then exited nonzero because Lean reported
`failed to create thread: Resource temporarily unavailable` while r6d was
hosting many concurrent campaign shards.  No direct axiom stream was
produced, so this attempt is **NO VERDICT**.  It is an infrastructure failure,
not a source, kernel, or mathematical counterexample.

Immutable retrieved evidence is under `aws_r6d_failed/`.  Its key SHA-256
values are:

```text
b47af6f087adaaf95e81d16c2094d2c96c4518c1e38cb571645d5ce25ce9bb09  output/verify.stdout
961e871982380aa9635e78379beaa2e89d41050eb1dd81af21682d236f243672  output/verify.stderr
4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865  rc
```

The independent source-completeness review is logically separate and rates
commit `f0b5823` **FORMAL_GLUE_ONLY**: the missing source-to-landing map is not
supplied by a successful build.  The nested repository has since advanced,
so any retry should pin and audit a newer commit rather than silently reuse
these bytes.
