# Final hostile review: immutable V3 binary-cubic first-band package

This is the only promotion-eligible review attempt.  V1/V2 review attempts and
V1/V2 custody roots are diagnostics only.

Review the producer report
`xmodel/max12-912-order1-binary-cubic-first-two-bands-aws-20260825.md`
(SHA-256 `2a185d6dabec5c47c16be2779c45e351f9658abe8fc8140de91c4d83a9407fb7`)
against the immutable case
`cases/max12_912_order1_binary_cubic_bands_aws_20260825/` with active roots:

- `MANIFEST.postrun.v3.sha256`, SHA-256
  `38466426e3a0b113a4cbd71b447d9a44b01482bcd3e3acea4879cad96589a8e3`;
- `FREEZE.v3.sha256`, SHA-256
  `b4374cb2395cadb1c4755432dd7087dd19f44e4ac1e21265054a38aa429354d5`;
- `CUSTODY_MANIFEST_COUNT_CORRECTION.md`, SHA-256
  `d7c6caa33c6879b321acd838c922ea2f655d01a267912f3ed3190860d4b5c9ec`.

First verify all 102 V3 manifest records.  The old manifest intentionally
contains 96 valid records plus seven captured locale-warning lines; the old
V1 count erratum mistakenly says 89, and the immutable count-correction repairs
that to 96.  Determine whether this is fully fail-closed and custody-only.

Then perform all nine mathematical/source charges in
`xmodel/max12-912-order1-binary-cubic-first-two-bands-review-grok-20260825-prompt.md`
(SHA-256 `c7fe6dae6e5b79c38751c2a664201557817f78362d27b9ca978b333e96344c5b`).
Do not run any substantive CAS, exact Python, solver, or build on the local
Mac.  Source reading, hashing, and hand checks are allowed.

Do not edit any case, producer, or prior review byte.  Write only
`xmodel/max12-912-order1-binary-cubic-first-two-bands-review-grok-v3-20260825.md`
with `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `NOT_CONFIRMED`, an exact source
list/hashes, and the smallest corrected statement for every defect.

