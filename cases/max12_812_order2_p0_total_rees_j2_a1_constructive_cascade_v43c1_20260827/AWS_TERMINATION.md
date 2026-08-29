# Box02 expanded V43C1 termination

The expanded V43C1 replay on Box02 was terminated intentionally at
2026-08-27T13:48:16Z after the C1/C2 derivation had been invalidated, that
invalidation had passed hostile review, and the corrected V43C4 special
certificate plus V43C5 V2 total converter had replayed exactly.  It produced
no stdout, certificate, or mathematical verdict.

Only the validated Python PID 362834 was signaled.  The run ended `rc=143`
after 3:37:21 at 77,317,640 KiB maximum RSS, one core, and zero swap.  K00 and
all unrelated Box02 paths/processes were untouched.  The stop released about
72 GiB of live memory.

Post-stop evidence is in `evidence/box02_terminated_after_c4/post_stop/`.
Its termination-registration SHA-256 is
`ae33d8304588c52451170ab3e2020dab9d24c3922d807627489e62a79e63f214`;
run-metadata SHA-256 is
`5b836fd3ea789ec0619f3c5dc23d6a3ed83c5274810e341a41298ab0015bde96`;
stderr SHA-256 is
`53ac8f3c95f0c314a20c3de93ca53214410eeb4004ef88dc8bdb14ff5d5da0d3`.
